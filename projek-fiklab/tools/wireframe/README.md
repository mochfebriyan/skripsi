# Alat wireframe Odoo 17

Skrip bersama untuk membuat wireframe modul LabFIK berupa screenshot layar Odoo 17 Community berisi data rekaan.
Alur lengkap (matriks view, kelas view di DCD, addon tipis, data rekaan, jebakan Odoo 17, naskah):
[wireframe-CLAUDE.md](../../../wireframe-CLAUDE.md).

| File | Fungsi |
|---|---|
| `docker-compose.yml` | Odoo 17 + PostgreSQL 15; addon dibaca dari `projek-fiklab/prototipe/` |
| `build.sh` | Hapus database lama, pasang addon dari nol, jalankan Odoo di `localhost:8069` (admin/admin), ambil screenshot |
| `shoot.py` | Playwright (1440×860, skala 2×, id-ID): login, buka tiap layar di `<addon>/wireframe_shots.json`, simpan PNG |

```bash
bash projek-fiklab/tools/wireframe/build.sh labfik_wireframe_<slug> labfik_wf_<slug> projek-fiklab/rancangan/wireframe-<slug>
```

Butuh Docker Desktop. Satu wireframe berjalan dalam satu waktu (port 8069).
