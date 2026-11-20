# Prototipe wireframe Tata Kelola (Odoo 17 Community)

20 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: bahan kerja.** Odoo tiruan untuk menghasilkan wireframe view inti modul Tata Kelola & Dokumen
(`design-class-tata-kelola.md` bagian 11.4) sebagai screenshot layar Odoo asli.

- `labfik_wireframe/`: addon tipis. Nama model dan field sama dengan DCD, **tanpa aturan bisnis**; tombol hanya
  mengubah status. **Jangan dipasang bersama addon asli** (`labfik_core`, `labfik_org`) karena nama modelnya sama.
- Data rekaan di `labfik_wireframe/data/`. **Semua nama orang fiktif**; kode dan judul dokumen hanya contoh.
- Antarmuka berbahasa Indonesia (`id_ID`), mata uang rupiah.

## Menjalankan

Butuh Docker Desktop. Dari root repo:

```bash
bash projek-fiklab/tools/wireframe/build.sh labfik_wireframe labfik_wf projek-fiklab/rancangan/wireframe
```

- Odoo: http://localhost:8069, login `admin` / `admin`.
- Daftar layar yang di-screenshot: `labfik_wireframe/wireframe_shots.json`.
- Alat bersama dan alur untuk modul lain: `projek-fiklab/tools/wireframe/` dan [wireframe-CLAUDE.md](../../wireframe-CLAUDE.md).

## Screenshot dan view inti

| File | View | Kelas view di DCD |
|---|---|---|
| `01-list-dokumen-induk.png` | List Dokumen Induk (contoh pola list) | — |
| `02-kanban-versi-sop.png` | Kanban Versi SOP/IK per status | V1 `document_version_view_kanban` |
| `03-form-versi-sop.png` | Form Versi SOP/IK berstatus Diajukan | V2 `document_version_view_form` |
| `04-form-rencana.png` | Form Rencana Pengembangan, tab Item Rencana | V3 `plan_view_form` |
| `05-kalender-item-rencana.png` | Calendar jadwal kegiatan, Februari 2027 | V4 `plan_line_view_calendar` |
| `06-pivot-realisasi.png`, `06b-grafik-realisasi.png` | Pivot dan grafik realisasi | V5 `realisasi_view_pivot` |
| `07-bagan-jabatan.png` | Hierarchy jabatan dari `atasan_id` | V6 `hr_job_view_hierarchy` |
| `08-laporan-status-monev.png` | Laporan HTML status monev (hasil `get_status()` rekaan) | — (UC-28 «report») |
