"""Ambil screenshot wireframe dari Odoo (labfik_wireframe) dengan Playwright.

Dijalankan di container Playwright pada jaringan docker compose (lihat README.md).
Argumen: URL dasar Odoo, folder keluaran.
"""
import sys
import xmlrpc.client
from playwright.sync_api import sync_playwright

BASE, OUT = sys.argv[1], sys.argv[2]
DB, USER, PWD = "labfik_wf", "admin", "admin"

uid = xmlrpc.client.ServerProxy(f"{BASE}/xmlrpc/2/common").authenticate(DB, USER, PWD, {})
rpc = xmlrpc.client.ServerProxy(f"{BASE}/xmlrpc/2/object")


def xid(name):
    return rpc.execute_kw(DB, uid, PWD, "ir.model.data", "check_object_reference",
                          ["labfik_wireframe", name])[1]


def act(name):
    return f"labfik_wireframe.{name}"


monev_ids = ",".join(str(xid(n)) for n in ("mon_01", "mon_02", "mon_03", "mon_13"))
SHOTS = [
    ("01-list-dokumen-induk", f"/web#action={act('action_document')}&view_type=list", ".o_list_renderer"),
    ("02-kanban-versi-sop", f"/web#action={act('action_version')}&view_type=kanban", ".o_kanban_renderer"),
    ("03-form-versi-sop", f"/web#action={act('action_version')}&model=labfik.document.version&view_type=form&id={xid('ver_sop01_r02')}", ".o_form_view"),
    ("04-form-rencana", f"/web#action={act('action_plan')}&model=labfik.plan&view_type=form&id={xid('plan_dev')}", ".o_form_view"),
    ("05-kalender-item-rencana", f"/web#action={act('action_plan_line')}&view_type=calendar", ".o_calendar_renderer"),
    ("06-pivot-realisasi", f"/web#action={act('action_realisasi')}&view_type=pivot", ".o_pivot"),
    ("06b-grafik-realisasi", f"/web#action={act('action_realisasi')}&view_type=graph", ".o_graph_renderer"),
    ("07-bagan-jabatan", f"/web#action={act('action_jabatan')}&view_type=hierarchy", ".o_hierarchy_renderer"),
    ("08-laporan-status-monev", f"/report/html/labfik_wireframe.report_status_monev_doc/{monev_ids}", "table"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 860}, device_scale_factor=2, locale="id-ID",
                            timezone_id="Asia/Jakarta")
    page.goto(f"{BASE}/web/login")
    page.fill("input[name=login]", USER)
    page.fill("input[name=password]", PWD)
    page.click("button[type=submit]")
    page.wait_for_selector(".o_main_navbar")
    for name, url, sel in SHOTS:
        page.goto("about:blank")
        page.goto(BASE + url)
        page.wait_for_selector(sel, timeout=20000)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        if name == "07-bagan-jabatan":
            page.set_viewport_size({"width": 1440, "height": 1080})
            for jabatan in ("Kepala Laboratorium", "Laboran/PLP"):
                page.locator(".o_hierarchy_node", has_text=jabatan).get_by_text("Buka").click()
                page.wait_for_timeout(1200)
            page.locator(".o_content").evaluate("e => e.scrollTop = 0")
            page.wait_for_timeout(500)
        page.screenshot(path=f"{OUT}/{name}.png", full_page=url.startswith("/report"))
        page.set_viewport_size({"width": 1440, "height": 860})
        print("ok", name)
    browser.close()
