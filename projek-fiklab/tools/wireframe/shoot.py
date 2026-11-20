"""Ambil screenshot wireframe dari Odoo dengan Playwright.

Dijalankan oleh build.sh di container Playwright pada jaringan docker compose.
Argumen: URL dasar Odoo, folder keluaran, nama addon, nama database.
Daftar layar dibaca dari <addon>/wireframe_shots.json (lihat _catatan di file itu).
"""
import json
import re
import sys
import xmlrpc.client
from playwright.sync_api import sync_playwright

BASE, OUT, ADDON, DB = sys.argv[1:5]
USER = PWD = "admin"
W, H = 1440, 860

uid = xmlrpc.client.ServerProxy(f"{BASE}/xmlrpc/2/common").authenticate(DB, USER, PWD, {})
rpc = xmlrpc.client.ServerProxy(f"{BASE}/xmlrpc/2/object")


def xid(name):
    return str(rpc.execute_kw(DB, uid, PWD, "ir.model.data", "check_object_reference", [ADDON, name])[1])


def resolve(url):
    url = url.replace("{m}", ADDON)
    url = re.sub(r"\{xids:([^}]+)\}", lambda m: ",".join(xid(n.strip()) for n in m.group(1).split(",")), url)
    return re.sub(r"\{xid:([^}]+)\}", lambda m: xid(m.group(1)), url)


spec = json.load(open(f"/addons/{ADDON}/wireframe_shots.json", encoding="utf-8"))["shots"]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2, locale="id-ID",
                            timezone_id="Asia/Jakarta")
    page.goto(f"{BASE}/web/login")
    page.fill("input[name=login]", USER)
    page.fill("input[name=password]", PWD)
    page.click("button[type=submit]")
    page.wait_for_selector(".o_main_navbar")
    for shot in spec:
        url = resolve(shot["url"])
        page.set_viewport_size({"width": W, "height": shot.get("height", H)})
        page.goto("about:blank")
        page.goto(BASE + url)
        page.wait_for_selector(shot["wait"], timeout=20000)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        for teks in shot.get("expand", []):
            page.locator(".o_hierarchy_node", has_text=teks).get_by_text("Buka").click()
            page.wait_for_timeout(1200)
        if shot.get("expand"):
            page.locator(".o_content").evaluate("e => e.scrollTop = 0")
            page.wait_for_timeout(500)
        page.screenshot(path=f"{OUT}/{shot['name']}.png", full_page=url.startswith("/report"))
        print("ok", shot["name"])
    browser.close()
