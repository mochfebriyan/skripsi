# Wireframe Odoo: dari DCD view sampai screenshot

Panduan untuk Claude Code (dan anggota) di **semua modul** LabFIK Compliance. Isinya alur end-to-end setelah design class diagram (langkah 10 [CLAUDE.md](CLAUDE.md) bagian 4) sampai wireframe berupa **screenshot layar Odoo 17 asli** berisi data rekaan. Alur ini sudah dijalankan penuh untuk modul Tata Kelola (Febriyan, 20 November 2026); hasilnya menjadi **contoh referensi** (bagian 9).

Dasar: catatan bimbingan Pak Widi 19 November 2026 (class diagram memuat kelas view; rancangan UI dengan view kanban, pivot, tree, Gantt) dan Wazlawick (2024) Bab 16 *Interface tier design*. Bahasa kerja: Indonesia.

## 0. Prasyarat (cek dulu, jangan lompat)

| Prasyarat | Cara cek | Bila belum ada |
|---|---|---|
| Langkah 1–10 modul selesai: use case, SSD + katalog operasi, DCD | `projek-fiklab/rancangan/` berisi `use-case-<slug>.md`, `ssd-<slug>.md`, `design-class-<slug>.md`, `class-<slug>.drawio` | **Berhenti.** Kerjakan dulu sesuai CLAUDE.md bagian 4 |
| Docker Desktop menyala | `docker info` | Minta pengguna menyalakan Docker Desktop |
| Alat wireframe bersama | `projek-fiklab/tools/wireframe/` (`docker-compose.yml`, `build.sh`, `shoot.py`) | Ambil dari `main` (`git checkout origin/main -- projek-fiklab/tools/wireframe wireframe-CLAUDE.md`) |

Baca juga [OOAD_Wazlawick_2024_Knowledge_Pack/…/16_Ch16_Interface_Tier_Design_IFML.md](projek-fiklab/docs/OOAD_Wazlawick_2024_Knowledge_Pack/OOAD_Wazlawick_2024_Knowledge/16_Ch16_Interface_Tier_Design_IFML.md) sebelum mulai.

## Ringkasan alur

| # | Langkah | Output | Masuk proposal |
|---|---|---|---|
| 1 | Matriks model × jenis view | Bagian "Lapisan antarmuka" di `design-class-<slug>.md` | Tidak (bahan kerja); alasannya diringkas di paragraf DCD |
| 2 | Pilih view inti (5–8) | Tabel view inti di bagian yang sama | — |
| 3 | Verifikasi fitur view di kode sumber Odoo 17 (Docker) | Catatan "diperiksa di image odoo:17" | — |
| 4 | Kelas view di DCD drawio | Kotak «form»/«kanban»/… + garis «view» di `class-<slug>.drawio` | **Ya**, menyatu dengan gambar DCD |
| 5 | Addon wireframe tipis + data rekaan | `projek-fiklab/prototipe/labfik_wireframe_<slug>/` | — |
| 6 | Bangun, jalankan, screenshot | PNG di `projek-fiklab/rancangan/wireframe-<slug>/` | **Ya** (2.3.5) |
| 7 | Periksa screenshot satu per satu, perbaiki | — | — |
| 8 | Commit; tulis naskah | DCD + 2.3.5 Desain Antarmuka | **Ya** |

---

## 1. Matriks model × jenis view

Untuk **setiap model** di DCD, tentukan view yang disediakan. Aturan:

| Aturan | Sumber |
|---|---|
| Antarmuka diturunkan dari use case/SSD: setiap view menyebut UC yang dilayaninya; view tanpa UC tidak dibuat | Wazlawick §16.1 |
| List = view `tree` ("tree" dalam arahan Pak Widi), Details + Form = view `form`. **Satu view selalu milik satu model utama**; model lain ikut tampil lewat field relasi (Many2one, One2many di tab) | §16.3 |
| Pola *master-detail* = form dengan tab One2many; pola *search* = view `search` (filter + *group by*) | §16.5 |
| Tombol = operasi sistem: tombol header form memanggil method `action_*` dari katalog operasi SSD | §16.6 |
| *Sweet spot*: model «CRUDL» cukup list + form. Kanban, calendar, pivot, graph, hierarchy **hanya** bila menjawab kebutuhan/bukti tertentu | CLAUDE.md bagian 1 |

Pedoman memilih jenis view:

| Jenis view | Dipakai bila |
|---|---|
| Kanban per `state` | Dokumen yang melewati alur status (semua turunan `labfik.approval.mixin`). Satu pola untuk semua turunan |
| Calendar (`date_start` + `date_stop`) | Ada tanggal kejadian atau jadwal berentang. **Pengganti Gantt** |
| Pivot / graph | Ada angka yang perlu dirangkum per dimensi (target vs capaian, jumlah per periode) |
| Hierarchy (`parent_field`) | Ada Many2one ke model yang sama (struktur organisasi, induk–anak) |
| Laporan QWeb (bukan view) | Use case «report» |

**Gantt tidak dipakai**: view `gantt` hanya ada di Odoo **Enterprise** (`web_gantt`); sistem memakai Community. Tulis alasannya di naskah.

Tulis hasilnya sebagai bagian baru di `design-class-<slug>.md` (contoh: bagian 11 `design-class-tata-kelola.md`): aturan, tabel jenis view yang tersedia, matriks (kolom List, Form, Kanban, Calendar, Pivot/Graph, Lainnya, Laporan QWeb, UC), alasan tiap view tambahan, filter tersimpan utama (sebutkan operasi SSD yang diwakilinya, mis. filter "Item saya" = `daftar_item_pic(user_id)`).

Sambil menyusun matriks, catat **field yang dibutuhkan view tapi belum ada di DCD** (contoh Tata Kelola: `labfik.realisasi.target` related agar pivot bisa menampilkan target vs capaian). Laporkan ke pengguna sebagai perubahan DCD kecil.

## 2. Pilih view inti

Kelas view **hanya digambar untuk view inti**, bukan semua model (bila semua digambar, halaman DCD sesak). Kriteria view inti:
- Menjalankan use case kunci (yang punya alur lengkap di expanded use case / SSD).
- Memperlihatkan jenis view yang diminta pembimbing (kanban, pivot, calendar, hierarchy).
- Biasanya 5–6 view, ditambah satu contoh list dan laporan «report» utama untuk wireframe.

Buat tabel: # · kelas view (XML ID) · halaman DCD · UC kunci · yang ditunjukkan.

## 3. Verifikasi fitur view di Odoo 17 Community

Jangan mengandalkan ingatan. Periksa kode sumber di image resmi:

```bash
docker pull odoo:17
docker run --rm --entrypoint bash odoo:17 -c '
A=/usr/lib/python3/dist-packages/odoo/addons
ls -d $A/web_hierarchy $A/web_gantt 2>&1                         # gantt tidak ada di Community
grep -n "parent_field\|child_field" $A/web_hierarchy/static/src/hierarchy_arch_parser.js
grep -n "default_group_by\|records_draggable" $A/web/static/src/views/kanban/kanban_arch_parser.js
grep -n "date_stop\|\"mode\"\|quick_create" $A/web/static/src/views/calendar/calendar_arch_parser.js
grep -n "initial_date" $A/web/static/src/views/calendar/calendar_model.js
odoo --version'
```

Catat build Odoo yang diperiksa (mis. `17.0-20260908`) di dokumen DCD.

## 4. Kelas view di DCD drawio

**Edit file drawio yang sudah ada secara langsung** (skrip Python yang menyisipkan sel ke halaman yang tepat), bukan membuat ulang dari skrip pembuat diagram, supaya rapian manual pengguna tidak tertimpa. Simpan cadangan file sebelum menambal.

Notasi (konsisten dengan CLAUDE.md bagian 5, gaya polos hitam-putih):

| Elemen | Bentuk |
|---|---|
| Kelas view | Kotak kelas biasa (swimlane, 3 kompartemen). Header: `«kanban»` / `«form»` / `«calendar»` / `«pivot»` / `«hierarchy»`, lalu **XML ID view** tebal (mis. `plan_view_form`), lalu baris kecil `Label → model.utama (UC-xx)` |
| Atribut | Field yang tampil, dikelompokkan per bagian layar (`header:`, `isi:`, `tab Item: line_ids`) + atribut arsitektur view (`default_group_by: state`, `date_start: …`, `row/col/measure`) |
| Operasi | Tombol: `+ [Sahkan] → action_sahkan(pengesah, tanggal_sah) {groups: labfik_kalab}` |
| Relasi ke model | Garis **putus-putus, panah terbuka, label «view»**, dari view **ke** model utama (dependensi: view memakai model; model tidak bergantung pada view). Hanya ke model utama; model lain terlacak lewat field relasi |
| ID | Prefiks modul + halaman: `sdm-dcd2-v-<nama>`, garis `sdm-dcd2-v-<nama>-e` |
| Letak | Di halaman DCD yang sama dengan modelnya, di bawah kelas yang ada; perbesar `pageHeight`. Garis dibelokkan lewat celah kosong |

Tambahkan satu catatan notasi kelas view di halaman `Catatan DCD TO-BE (bahan kerja)`. Lalu:
- `python3 -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/class-<slug>.drawio <prefiks>` harus bersih.
- Cek tumpang-tindih kotak (bounding box) per halaman.
- Laporkan bahwa tampilan visual belum dicek di draw.io; minta pengguna membuka dan merapikan.
- Perbarui `design-class-<slug>.md`: baris di tabel "perubahan dibanding versi sebelumnya", cek silang ("setiap UC punya layar"), isu terbuka.

## 5. Addon wireframe tipis

### 5.1 Alat bersama dan contoh addon

Alat bersama (`projek-fiklab/tools/wireframe/`) tidak perlu diubah per modul. Contoh addon lengkap ada di branch `febriyan-skripsi`; baca sebagai acuan, jangan disalin mentah:

```bash
git fetch origin
git ls-tree -r --name-only origin/febriyan-skripsi projek-fiklab/prototipe/labfik_wireframe
git show origin/febriyan-skripsi:projek-fiklab/prototipe/labfik_wireframe/models/__init__.py
git show origin/febriyan-skripsi:projek-fiklab/prototipe/labfik_wireframe/wireframe_shots.json
```

Buat addon sendiri: `projek-fiklab/prototipe/labfik_wireframe_<slug>/` (mis. `labfik_wireframe_sdm`). Nama addon dan database berbeda per modul, sehingga semua addon wireframe bisa berada di satu folder `prototipe/`. `build.sh` membuat `prototipe/.gitignore` (`__pycache__/`) bila belum ada.

### 5.2 Struktur addon

```
labfik_wireframe_<slug>/
  __init__.py            # post_init: aktifkan id_ID, terjemahan, bahasa admin
  __manifest__.py        # depends: hr, mail (+ web_hierarchy bila ada hierarchy)
  models/__init__.py     # model tipis
  views/*.xml            # view inti + list/form pendukung + action + menu
  report/*.xml           # laporan QWeb «report» (qweb-html)
  data/*.xml             # data rekaan (master dulu, lalu transaksi)
  security/ir.model.access.csv
  wireframe_shots.json   # daftar layar untuk screenshot
```

**Model tipis:** nama model dan nama field **sama dengan DCD** (agar wireframe = DCD dan XML view bisa dipakai lagi di addon asli). Hanya field yang tampil di view. **Tanpa aturan bisnis**; tombol `action_*` cukup mengubah `state`. Mixin cukup versi tiruan (`labfik.approval.mixin` dengan `state`, penyusun, pengesah, tanggal, `log_ids` compute). Model Core yang dibutuhkan (`hr.job` diperluas, `labfik.periode`, `labfik.ruang`, `labfik.sesi`, …) ditiru seperlunya di addon ini. AbstractModel layanan tanpa tabel (seperti `labfik.org.monev`) dibuat sebagai model biasa berisi baris hasil rekaan. **Addon wireframe tidak boleh dipasang bersama addon asli.**

**Bahasa dan mata uang:**
- `post_init_hook`: `env["res.lang"]._activate_lang("id_ID")`, `_update_translations(["id_ID"])` pada modul terpasang, `base.user_admin.lang = "id_ID"`, `tz = "Asia/Jakarta"`.
- Rupiah **di data XML pertama**, sebelum data beranggaran: aktifkan `base.IDR` dan set `base.main_company.currency_id`.

**Data rekaan:**
- **Semua nama orang fiktif**; kode/judul dokumen contoh; tidak ada data dari dokumen nyata (CLAUDE.md bagian 3).
- Konsisten antar-layar: angka di laporan status monev harus cocok dengan data di kanban/pivot.
- Sebar status (draf/diajukan/disahkan) agar kanban terisi semua kolom; tanggal di rentang yang masuk akal (mis. periode sprint 2027) dan beberapa rentang bertumpuk di satu bulan agar calendar terlihat.
- Rekaman yang mewarisi `mail.thread` dibuat dengan `context="{'mail_create_nolog': True}"` agar chatter tidak menampilkan "… created" berbahasa Inggris.

### 5.3 Jebakan yang sudah ditemukan (Odoo 17)

| Gejala | Penyebab | Solusi |
|---|---|---|
| `TypeError: a bytes-like object is required` saat memuat data | `<field type="base64">` berisi teks langsung | Pakai `file="addon/data/contoh.pdf"` |
| Peringatan "should be searchable" lalu registry gagal | Field `related` ke field compute non-store | Jadikan compute biasa dengan `@api.depends` |
| Kolom kanban kosong tidak muncul | Tidak ada `group_expand` | `group_expand="_expand_state"` yang mengembalikan daftar status |
| Mata uang "$" | Rupiah diaktifkan setelah data dibuat | Atur rupiah di data XML pertama |
| Judul Many2one di `<h1>` form terpotong | Input editable sempit | `readonly="state != 'draf'"` + `options="{'no_open': True}"` |
| Calendar membuka bulan sekarang | Data di bulan lain | Context action `{'initial_date': '2027-02-01 00:00:00'}` |
| Hierarchy hanya satu tingkat | Node anak tertutup | `child_field` (One2many balik) + `expand` di `wireframe_shots.json` |
| Baris Total pivot tidak bermakna | Satuan tiap item berbeda | `group_operator="max"` untuk target; jelaskan di naskah bahwa yang dibaca baris per item |
| Rincian laporan berjarak ganda | `white-space: pre-line` + `t-field` Text (sudah jadi `<br>`) | Hapus `pre-line` |
| `name_get` tidak berpengaruh | Dihapus di Odoo 17 | `_compute_display_name` |
| `<string>:38: (ERROR/3) Unexpected indentation` | Peringatan docutils saat membaca deskripsi modul | Abaikan |
| `__pycache__` ikut ter-stage | — | `prototipe/.gitignore` (dibuat otomatis oleh `build.sh`) |

## 6. Bangun, jalankan, screenshot

Isi `wireframe_shots.json` (lihat `_catatan` di contoh): `name`, `url` (`/web#action={m}.<action>&view_type=<jenis>`, form dengan `&model=…&id={xid:<xml_id>}`, laporan `/report/html/{m}.<template>/{xids:a,b}`), `wait` (selector: `.o_list_renderer`, `.o_kanban_renderer`, `.o_form_view`, `.o_calendar_renderer`, `.o_pivot`, `.o_graph_renderer`, `.o_hierarchy_renderer`, `table`), opsional `expand` dan `height`.

Dari root repo:

```bash
bash projek-fiklab/tools/wireframe/build.sh labfik_wireframe_<slug> labfik_wf_<slug> projek-fiklab/rancangan/wireframe-<slug>
```

Skrip ini: menghapus database lama (`docker compose down -v`), memasang addon dari nol (`-i`, tanpa demo), menjalankan Odoo di `localhost:8069` (admin/admin), lalu menjalankan container Playwright (1440×860, skala 2×, locale id-ID) yang login dan menyimpan PNG. Error pemasangan muncul di keluaran; cari baris `ERROR`/`Traceback` dan perbaiki addon, lalu ulangi. Cek status modul bila ragu:

```bash
(cd projek-fiklab/tools/wireframe && docker compose exec -T db psql -U odoo -d labfik_wf_<slug> -tc "select state from ir_module_module where name='labfik_wireframe_<slug>';")
```

Hanya satu wireframe yang bisa jalan sekaligus (port 8069). Hentikan dengan `(cd projek-fiklab/tools/wireframe && docker compose down)`.

## 7. Periksa screenshot

Buka **setiap** PNG (Read) sebelum melapor. Periksa: teks terpotong, mata uang, bahasa campuran, kolom kanban kosong, calendar di bulan yang benar, node hierarchy terbuka dan tidak tergulir, tabel laporan utuh, angka konsisten antar-layar, tidak ada nama orang nyata. Perbaiki lalu jalankan ulang `build.sh`. Laporkan ke pengguna hal yang memang bawaan Odoo (mis. node hierarchy yang tidak dibuka tampak pudar; baris Total pivot).

## 8. Commit dan naskah

- Commit terpisah per langkah, pesan bahasa Indonesia huruf kecil (CLAUDE.md bagian 11), mis. `tambah kelas view inti di dcd <modul>`, `tambah prototipe odoo wireframe dan screenshot view inti <modul>`. Cek data pribadi dengan `grep` sebelum commit. Jangan push tanpa diminta.
- **Naskah DCD (2.3.4):** kalimat tentang kelas view ditambahkan ke paragraf yang ada (pengantar: jenis view yang dipakai dan alasan Gantt tidak dipakai; notasi: stereotype dan garis «view»; tiap subbab gambar DCD: kelas view di gambar itu; keterlacakan: UC → tombol → method → AB). Tanpa subbab matriks tersendiri.
- **Naskah 2.3.5 Desain Antarmuka** (pola semua skripsi referensi di `projek-fiklab/penulisan-skripsi/reference/BAB_2_Gabungan.md`): satu paragraf pengantar (wireframe dibuat langsung di Odoo 17 Community dengan data rekaan), lalu satu sub-subbab per layar berisi gambar + satu paragraf (apa yang dilihat/dilakukan pengguna, UC, kelas view di DCD). Tabel *Need Analysis UI/UX* tidak perlu karena komponen layar bawaan Odoo.
- Perubahan di Google Docs memakai penanda yang disepakati pemilik naskah (Febriyan: tambahan sorot hijau, hapusan merah dicoret). Gambar disisipkan pengguna sendiri (konektor Docs hanya menerima URL publik).

## 9. Contoh referensi: Tata Kelola (branch `febriyan-skripsi`)

| Langkah | File |
|---|---|
| 1–2 Matriks, view inti | `projek-fiklab/rancangan/design-class-tata-kelola.md` bagian 11 |
| 4 Kelas view | `projek-fiklab/rancangan/class-tata-kelola.drawio` (DCD-2: hierarchy; DCD-3: kanban + form Versi; DCD-4: form Rencana, calendar Item, pivot Realisasi) |
| 5 Addon | `projek-fiklab/prototipe/labfik_wireframe/` |
| 6 Skrip | `projek-fiklab/tools/wireframe/` (bersama), `projek-fiklab/prototipe/labfik_wireframe/wireframe_shots.json` |
| 6–7 Hasil | `projek-fiklab/rancangan/wireframe/` (9 PNG) |
| Commit | `3a8d368` (kelas view DCD), `836eeec` (prototipe + screenshot) di branch `febriyan-skripsi` |
