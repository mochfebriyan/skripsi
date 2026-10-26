# Spesifikasi Teknis: MVP Organization Management LabFIK

26 Oktober 2026 · Febriyan · Pendamping [PRD v0.3](prd-mvp-pengelolaan-1-3.md) · Status: **Diimplementasikan (MVP)**

Dokumen ini menjelaskan **bagaimana** kebutuhan di PRD dibangun. Bila ada perbedaan, PRD yang berlaku. Nama model dan field di sini masih bisa berubah saat implementasi.

## 1. Lingkungan

| Komponen | Pilihan | Catatan |
|---|---|---|
| Odoo | Image resmi `odoo:17.0` Community | Kunci ke *digest* image setelah instalasi pertama berhasil (NFR-05). Image resmi sudah membawa wkhtmltopdf untuk cetak PDF |
| Basis data | `postgres:16` | Volume terpisah |
| Add-on | Folder lokal `addons/` di-*mount* ke `/mnt/extra-addons` | Modul dikembangkan langsung di repositori |
| Konfigurasi | `config/odoo.conf` | `addons_path`, `admin_passwd`, `dbfilter`, `without_demo = False` saat pengembangan |
| Bahasa | `id_ID` dipasang saat inisialisasi | NFR-01, NFR-10 |

Struktur folder yang diusulkan:

```
projek-fiklab/odoo-pengelolaan-mvp/
├── docker-compose.yml
├── config/odoo.conf
├── addons/
│   └── labfik_org/
└── README.md          # cara menjalankan, backup, restore
```

`docker-compose.yml` (garis besar):

```yaml
services:
  db:
    image: postgres:16
    environment: [POSTGRES_DB=postgres, POSTGRES_USER=odoo, POSTGRES_PASSWORD=odoo]
    volumes: [db-data:/var/lib/postgresql/data]
  odoo:
    image: odoo:17.0
    depends_on: [db]
    ports: ["8069:8069"]
    volumes:
      - odoo-data:/var/lib/odoo          # filestore (lampiran)
      - ./addons:/mnt/extra-addons
      - ./config:/etc/odoo
volumes: {db-data: {}, odoo-data: {}}
```

**Backup (NFR-04):** `pg_dump` basis data + salin volume `odoo-data` (filestore). Keduanya wajib, karena file lampiran tidak tersimpan di basis data. Prosedur dan uji *restore* ditulis di `README.md`.

## 2. Modul

| Atribut | Nilai |
|---|---|
| Nama teknis | `labfik_org` |
| Versi | `17.0.0.1.0` |
| `depends` | `['base', 'mail']` (NFR-08). Tidak bergantung pada modul Rafika atau OpenEduCat |
| Kategori | `LabFIK` |

```
labfik_org/
├── __manifest__.py
├── security/   groups.xml, ir.model.access.csv, rules.xml
├── data/       jabatan_standar.xml, sequence.xml, cron.xml, config_default.xml
├── demo/       demo_d1.xml ... (dataset skenario PRD Lampiran D)
├── models/     personel.py, jabatan.py, sk.py, periode.py, ruang.py,
│               dokumen.py, rencana.py, kpi.py, rapat.py, evaluasi.py,
│               kepatuhan.py, res_config_settings.py
├── wizard/     tolak_wizard.py, snapshot_wizard.py
├── report/     rencana_kerja.xml, bagan_organisasi.xml, matriks_kewenangan.xml, laporan_pelaksanaan.xml
├── views/      ... + menu.xml + checklist_mulai.xml
├── static/     kerangka_sop.docx (FR-E3)
└── tests/      test_sk_akses.py, test_dokumen.py, test_skor_p2.py, test_tangga_p1_p3.py
```

## 3. Model data

Semua model transaksi mewarisi `mail.thread` dan `mail.activity.mixin`. Field penting diberi `tracking=True` (NFR-02).

### Master

| Model | Field utama | FR |
|---|---|---|
| `labfik.periode` | `name`, `jenis` (akademik/anggaran), `tanggal_mulai`, `tanggal_selesai`, `semester_ids` (anak: Ganjil/Genap dengan tanggal) | E5 |
| `labfik.ruang` | `kode`, `name`, `lokasi`, `is_virtual` (untuk "Portal LabFIK") | E6 |
| `labfik.personel` | `name`, `jenis` (dosen/tendik/mahasiswa/eksternal), `nomor_induk` (NIP/NIM, unik, hanya grup Admin/KaLab), `user_id` → `res.users` (opsional), `active`, `jabatan_line_ids` (compute) | A1 |
| `labfik.jabatan` | `name`, `uraian_tugas` (Html), `kewenangan` (Html), `atasan_id` → jabatan, `pengganti_id` → jabatan, `group_ids` → `res.groups`, `pemangku_ids` (compute), `is_puncak` | A2, A8 |

**Acuan master Rafika untuk `labfik.personel`** (keputusan D2):

| Rafika | Dipetakan ke | Catatan |
|---|---|---|
| `mst_dosen.kode_dosen`, `nama_dosen` | `nomor_induk`, `name` (jenis = dosen) | Saat integrasi, tambahkan `mst_dosen_id` opsional |
| `op.student.assistant` (`assistant_type`, `start_date`, `end_date`, `state`) | `labfik.personel` (jenis = mahasiswa) + baris jabatan Asisten berperiode | Periode asisten di Rafika sejalan dengan baris personel–jabatan |
| `res.users` (di-*inherit* Rafika) | `user_id` | Akun login dipakai bersama |

### Struktur

| Model | Field utama | FR |
|---|---|---|
| `labfik.sk` | `nomor`, `tanggal`, `pengesah_id` → personel, `tanggal_mulai`, `tanggal_selesai`, `state` (draf/berlaku/dicabut), `dokumen_versi_id` → versi dokumen di register, `line_ids` | A3 |
| `labfik.sk.line` | `sk_id`, `personel_id`, `jabatan_id`, `tanggal_mulai`, `tanggal_selesai`, `is_aktif` (compute) | A3, A4 |
| `labfik.rapat` | `periode_id`, `semester`, `tanggal`, `agenda`, `peserta_ids` → personel, `keputusan`, `notulen` (lampiran) | A6 |
| `labfik.evaluasi.struktur` | `periode_id`, `tanggal`, `temuan`, `keputusan`, `sk_revisi_id`, `jabatan_revisi_ids` | A7 |

### Dokumen

| Model | Field utama | FR |
|---|---|---|
| `labfik.dokumen` | `kode` (unik), `name`, `jenis` (sop/ik/formulir/eksternal), `kategori`, `dasar_kebutuhan`, `ruang_ids`, `pemilik_id` → personel, `versi_ids`, `versi_berlaku_id` (compute) | B1, B8 |
| `labfik.dokumen.wajib` | `periode_id`, `dokumen_id`, `terkunci` | B1, B9 |
| `labfik.dokumen.versi` | `dokumen_id`, `revisi`, `attachment_id`, `ringkasan`, `state` (draf/diajukan/berlaku/dicabut), `alasan_tolak`, `pengesah_id`, `tanggal_sah`, `tanggal_tinjau` | B2, B3 |
| `labfik.dokumen.distribusi` | `versi_id`, `ruang_id`, `tanggal`, `petugas_id` | B4 |
| `labfik.dokumen.sosialisasi` | `versi_id`, `tanggal`, `metode`, `bukti` (lampiran), `peserta_ids` → personel | B5 |

Penolakan dicatat lewat wizard `labfik.tolak.wizard` (alasan wajib), dipakai bersama oleh versi dokumen dan rencana kerja.

### Rencana kerja

| Model | Field utama | FR |
|---|---|---|
| `labfik.kpi` | `kode`, `name`, `definisi`, `pembilang`, `penyebut`, `satuan`, `sumber_data`, `sumber_otomatis` (C, *hook*) | C1, C10 |
| `labfik.renstra.sasaran` | `tingkat` (upnvj/upps/prodi), `kode`, `uraian`, `dokumen_id` | C2 |
| `labfik.rencana` | `name`, `jenis` (strategis/tahunan), `periode_id`, `pemilik_id`, `narasi`, `state` (draf/diajukan/disahkan/diganti/selesai), `pengesah_id`, `dokumen_versi_id` (PDF bertanda tangan), `rencana_asal_id` (revisi) | C3, C6 |
| `labfik.rencana.item` | `rencana_id`, `sasaran`, `renstra_ids`, `renstra_teks`, `kpi_id`, `target`, `satuan`, `pic_id` → personel, `tanggal_mulai`, `tanggal_selesai`, `anggaran` | C4 |
| `labfik.rencana.realisasi` | `item_id`, `semester`, `capaian`, `anggaran_terpakai`, `bukti` (lampiran), `pelapor_id` | C7 |
| `labfik.rencana.tinjauan` | `rencana_id`, `tanggal`, `peserta_ids`, `ringkasan`, `keputusan_ids` (anak: uraian + `item_berikut_id`) | C9 |

### Kepatuhan

| Model | Isi | FR |
|---|---|---|
| `labfik.kepatuhan` | Model `TransientModel` atau *SQL view* yang menghitung status per indikator dan periode: persentase dan skor P2, daftar SOP gagal beserta cek; tangga K1–K4 P1 dan P3 dengan tautan rekaman; `skor_penilai` disimpan terpisah di `labfik.kepatuhan.penilaian` | D1–D3 |
| `labfik.kepatuhan.snapshot` | `periode_id`, `tanggal`, `indikator`, `hasil_json`, `bukti_ids` (salinan tautan), `dibuat_oleh` | D4 |

## 4. Hak akses

### Grup (`security/groups.xml`)

| XML ID | Nama | Mewarisi |
|---|---|---|
| `group_labfik_pengguna` | LabFIK / Pengguna Lab | `base.group_user` |
| `group_labfik_penilai` | LabFIK / Penilai | Pengguna |
| `group_labfik_laboran` | LabFIK / Laboran | Pengguna |
| `group_labfik_kalab` | LabFIK / KaLab | Laboran |
| `group_labfik_admin` | LabFIK / Admin | KaLab |

Matriks CRUD mengikuti PRD Lampiran B dan diterjemahkan ke `ir.model.access.csv`. Aturan baris (`rules.xml`):
- Pengguna Lab hanya melihat `labfik.dokumen.versi` berstatus *berlaku*.
- Laboran hanya mengubah realisasi item yang ia PIC-i.
- Field `nomor_induk` memakai atribut `groups="labfik_org.group_labfik_kalab"`.

### Sinkronisasi jabatan → grup (FR-A4)

- **Pemicu:** `create`/`write` pada `labfik.sk.line`, perubahan `state` SK, perubahan `group_ids` jabatan, dan `ir.cron` harian pukul 00:30.
- **Logika:** untuk setiap personel yang punya `user_id`:
  ```
  grup_dikelola = gabungan group_ids dari semua jabatan
  grup_seharusnya = gabungan group_ids dari jabatan pada baris SK yang aktif hari ini (SK berlaku)
  tambah (grup_seharusnya − grup_user ∩ grup_dikelola)
  cabut  ((grup_user ∩ grup_dikelola) − grup_seharusnya)
  ```
- Grup di luar `grup_dikelola` tidak disentuh (PRD §8.4).
- Setiap perubahan dicatat sebagai pesan di *chatter* personel.

## 5. Aturan dan perhitungan

| Aturan | Implementasi |
|---|---|
| Satu versi berlaku (B3) | Method `action_sahkan()`: cek grup KaLab → set versi lain milik dokumen yang sama dari *berlaku* menjadi *dicabut* → set `tanggal_tinjau = tanggal_sah + siklus` |
| File versi berlaku terkunci | `write()` menolak perubahan `attachment_id` bila `state == 'berlaku'` |
| Hak "Sahkan" | Tombol memakai `groups="...group_labfik_kalab"`, dan method memanggil `self.env.user.has_group(...)` (pertahanan ganda) |
| Skor P2 (D1) | Untuk setiap `labfik.dokumen.wajib` pada periode: evaluasi S1–S5 terhadap `tanggal_penilaian`; persen → skor sesuai PRD §8.1; penyebut 0 → N/A |
| Tangga P1/P3 (D2) | Evaluasi K1→K4 berurutan; berhenti di kriteria pertama yang belum lengkap; kembalikan `kriteria_tertinggi` + daftar tautan rekaman per kriteria |
| Ambang (E7) | `res.config.settings` dengan `ir.config_parameter`: `labfik.siklus_tinjau_bulan` = 12, `labfik.pengingat_hari` = 30, `labfik.p1_k3_min_realisasi_per_semester` = 1, `labfik.p3_k3_min_rapat_per_semester` = 1, `labfik.k4_min_per_tahun` = 1 |
| Pengingat tinjau (B7) | `ir.cron` harian membuat `mail.activity` untuk `pemilik_id.user_id` bila `tanggal_tinjau − hari ini ≤ pengingat_hari` |
| Kunci daftar wajib (B9) | `labfik.dokumen.wajib.terkunci = True` → `write`/`unlink` ditolak |

## 6. Laporan (QWeb PDF)

| Laporan | Isi | FR |
|---|---|---|
| Rencana Kerja | Sampul (lab, periode, status, pengesah), narasi, tabel item, matriks keterkaitan Renstra, kolom tanda tangan | C5 |
| Laporan Pelaksanaan | Target vs realisasi per item per semester | C8 |
| Bagan Organisasi | Hierarki jabatan (indentasi per tingkat atasan) dengan nama pemangku | A5 |
| Matriks Kewenangan | Baris jabatan × kolom kewenangan, plus pengganti | A5 |

Format tanggal Indonesia (`%d %B %Y` dengan locale `id_ID`). Template dipisah per laporan agar bisa diganti bila Dekanat menetapkan format.

## 7. Pengujian

| Jenis | Isi | PRD |
|---|---|---|
| Unit test (`TransactionCase`) | Sinkronisasi akses (TC-AKS), aturan versi, kunci file, skor P2 untuk D-1/D-2, tangga untuk D-3a–d, kasus pinggir §8.4 | NFR-09, Lampiran D |
| Data skenario | `demo/` memuat D-1 sampai D-4 | Lampiran D |
| Black box | Satu test case per baris Lampiran A | Kriteria rilis |
| UAT | Skenario S-01 sampai S-06 (mulai dari nol, susun struktur, siklus SOP, susun rencana, lapor realisasi, tunjukkan bukti ke penilai) + SUS | O1, O4, O5 |

Menjalankan test: `docker compose run --rm odoo odoo -d test_db -i labfik_org --test-enable --stop-after-init`.

## 8. Catatan integrasi dengan modul lain

- Modul kelompok lain sebaiknya bergantung pada `labfik_org` untuk personel, jabatan, periode, ruang, dan register dokumen, bukan membuat versinya sendiri.
- Saat digabung dengan modul Rafika: tambahkan modul jembatan (misalnya `labfik_org_rafika`) yang menautkan `labfik.personel` ke `mst_dosen` dan `op.student.assistant`, supaya `labfik_org` tetap tidak bergantung pada OpenEduCat.

## 9. Catatan implementasi (26 Oktober 2026)

Kode ada di [`odoo-pengelolaan-mvp/`](../odoo-pengelolaan-mvp/README.md). Penyesuaian terhadap rancangan di atas:

| Bagian | Rancangan | Implementasi | Alasan |
|---|---|---|---|
| Basis data | `postgres:15` | `postgres:16` | Image sudah tersedia di mesin pengembang |
| Kewenangan | Teks di jabatan | Master `labfik.kewenangan` (8 kewenangan standar) + uraian tambahan | Agar matriks kewenangan berupa tabel jabatan × kewenangan yang sebenarnya |
| Lampiran SK/rencana | Tautan ke register | Mixin `labfik.lampiran.mixin`: unggah di form SK/rencana, file tersimpan sekali sebagai versi di register | FR-A3/FR-B8, tanpa langkah ganda bagi pengguna |
| Riwayat chatter | `message_post` | `_message_log` | `message_post` gagal bila pengguna belum punya email |
| Aturan baris versi | Pengguna: versi berlaku | Pengguna: versi berlaku **dan** jenis SOP/IK/formulir | PDF SK dan rencana kerja tidak terlihat oleh asisten |
| Checklist mulai | Window action | Server action yang menyimpan rekaman dulu | Kolom terhitung tidak terisi pada rekaman baru yang belum tersimpan |
| SK berlaku | Baris dapat diedit tanggal selesainya | Baris read-only + tombol "Akhiri hari ini" per baris | Mencegah tombol tambah/hapus yang pasti ditolak server |
| Test | 4 file | 7 file, 87 test case | Lihat README |
