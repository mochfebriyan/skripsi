"""Package diagram addon modul Tata Kelola & Dokumen (Gambar 2.1 naskah Bab II), 1 halaman + catatan.

Pemakaian: python3 -I package.py projek-fiklab/rancangan/package-tata-kelola.drawio
"""
import sys
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def esc(s): return escape(s, {'"': "&quot;"})
# Gaya polos hitam-putih; garis putus-putus hanya untuk dependency (notasi UML).
FONT = "fontFamily=Times New Roman;"
PKG = ("shape=folder;tabWidth=110;tabHeight=18;tabPosition=left;html=1;whiteSpace=wrap;verticalAlign=top;align=left;"
       "spacingLeft=10;spacingTop=20;spacingRight=8;fontSize=12;fillColor=#FFFFFF;strokeColor=#000000;" + FONT)
DEP = ("endArrow=open;endSize=12;dashed=1;html=1;strokeColor=#000000;fontSize=11;labelBackgroundColor=#FFFFFF;"
       "edgeStyle=orthogonalEdgeStyle;rounded=0;" + FONT)
NOTE = ("shape=note;whiteSpace=wrap;html=1;size=14;align=left;verticalAlign=top;spacingLeft=6;spacingTop=4;"
        "fontSize=11;fillColor=#FFF2CC;strokeColor=#D6B656;")
TITLE = "text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;"


class Page:
    def __init__(s, pid, name):
        s.P, s.id, s.name, s.cells, s.maxx, s.maxy = f"tk-pkg{pid}-", f"tk-pkg{pid}", name, [], 0, 0

    def v(s, id, val, style, x, y, w, h):
        s.maxx, s.maxy = max(s.maxx, x + w), max(s.maxy, y + h)
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                       f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

    def e(s, id, a, b, label="«depends»", style=DEP):
        s.cells.append(f'<mxCell id="{s.P}{id}" value="{esc(label)}" style="{style}" edge="1" parent="1" '
                       f'source="{s.P}{a}" target="{s.P}{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    def xml(s):
        w, h = s.maxx + 40, s.maxy + 30
        return (f'<diagram id="{s.id}" name="{esc(s.name)}"><mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" '
                f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" math="0" shadow="0">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(s.cells) + "</root></mxGraphModel></diagram>")


def isi(stereo, nama, baris):
    head = (f"«{stereo}»<br>" if stereo else "") + f"<b>{nama}</b>"
    return head + ("<br>" + "<br>".join(baris) if baris else "")


p = Page(1, "Package TO-BE (1-1) - Addon Modul Tata Kelola dan Dokumen")
# baris atas: addon yang bergantung pada Core
p.v("org", isi("", "labfik_org", [
    "Tata Kelola dan Dokumen (PKG-01, 02, 03, 13)",
    "• Dokumen Induk dan versi SOP/IK",
    "• Distribusi, sosialisasi, tinjau ulang",
    "• Renstra, rencana, item, temuan gap",
    "• SK penetapan, rapat, evaluasi struktur",
    "• Realisasi, tinjauan, KPI",
    "• Status monev"]), PKG, 40, 30, 330, 180)
p.v("lain", isi("", "Modul fungsional lain", [
    "labfik_sdm (SDM dan Kompetensi)",
    "labfik_praktikum (Pelaksanaan Praktikum)",
    "Modul Aset",
    "Modul Safety"]), PKG, 430, 30, 330, 180)
# baris tengah: Core
p.v("core", isi("Core", "labfik_core", [
    "• Master bersama: personel (hr.employee), jabatan (hr.job), ruang, periode, mata kuliah, kelas, sesi",
    "• Mixin: approval, period, criteria, evidence",
    "• Riwayat pengesahan (approval.log)"]), PKG, 140, 300, 520, 130)
# baris bawah: addon bawaan Odoo
p.v("hr", isi("Odoo", "hr", ["Karyawan dan jabatan"]), PKG, 200, 520, 170, 80)
p.v("mail", isi("Odoo", "mail", ["Riwayat perubahan dan aktivitas"]), PKG, 430, 520, 170, 80)
p.e("d1", "org", "core")
p.e("d2", "lain", "core")
p.e("d3", "core", "hr")
p.e("d4", "core", "mail")

# halaman catatan (bahan kerja, tidak disisipkan ke naskah)
c = Page("-notes", "Catatan Package TO-BE (bahan kerja)")
c.v("title", "Catatan package diagram (bahan kerja, tidak disisipkan ke naskah)", TITLE, 40, 10, 900, 36)
c.v("legend", "<b>Notasi</b> (UML package diagram)<br>"
    "• Folder = package (addon Odoo). «Odoo» = addon bawaan Odoo 17 CE (LGPL-3); «Core» = master dan mixin bersama proyek; "
    "tanpa stereotype = addon milik modul.<br>"
    "• Panah putus-putus berkepala terbuka «depends» = dependency, sama dengan isi <code>depends</code> pada manifest addon.",
    NOTE, 40, 56, 900, 80)
c.v("src", "<b>Sumber</b><br>• CLAUDE.md §6 (kontrak Core), brief-tata-kelola-dokumen.md (Platform dan addon), "
    "kontrak-core.md · Draf 18 Nov 2026 · Febriyan<br>"
    "• Gambar 2.1 naskah Bab II (subbab 2.2.1).", NOTE, 40, 150, 900, 70)
c.v("konf", "<b>Isu terbuka</b><br>• Penempatan Core di addon terpisah <code>labfik_core</code> masih [KONFIRMASI kelompok].<br>"
    "• Nama addon Aset dan Safety belum ditetapkan kelompok lain, jadi ditulis sebagai nama modul.<br>"
    "• Modul lain yang perlu Dokumen Induk atau KPI memakai modul jembatan yang bergantung pada addonnya dan "
    "<code>labfik_org</code> (mis. <code>labfik_safety_org</code>); tidak digambar agar diagram tetap ringkas.",
    NOTE, 40, 234, 900, 100)

open(OUT, "w").write('<mxfile host="app.diagrams.net">' + p.xml() + c.xml() + "</mxfile>")
