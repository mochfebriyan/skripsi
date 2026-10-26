# MVP LabFIK Organization Management (Pengelolaan 1, 2, 3)

Modul Odoo 17 Community `labfik_org` untuk indikator tata kelola Instrumen Monev Laboratorium UPNVJ 2026:

| Indikator | Yang dikelola sistem | Skor |
|---|---|---|
| **Pengelolaan 1** · rencana kerja tahunan | Form rencana + item (sasaran, KPI, target, PIC, jadwal, anggaran, Renstra), cetak format baku, pengesahan dengan PDF bertanda tangan, revisi, realisasi per semester, tinjauan | Tangga K1–K4 (semi-otomatis) |
| **Pengelolaan 2** · SOP dan IK | Daftar induk, daftar SOP wajib per periode (bisa dikunci), versi `draf → diajukan → berlaku → dicabut`, tolak dengan alasan, distribusi per ruang, sosialisasi, tinjau ulang, pengingat | Persentase → skor 1–4 (otomatis) |
| **Pengelolaan 3** · struktur organisasi | Personel, jabatan (tugas, kewenangan, atasan, pengganti), SK penetapan berperiode, hak akses otomatis dari jabatan, rapat koordinasi, evaluasi struktur, bagan organisasi, matriks kewenangan | Tangga K1–K4 (semi-otomatis) |

Kebutuhan dan aturannya ada di [PRD v0.3](../prd/prd-mvp-pengelolaan-1-3.md) dan [spesifikasi teknis](../prd/spesifikasi-teknis-mvp-pengelolaan-1-3.md).

## Menjalankan

Prasyarat: Docker Desktop berjalan.

```bash
cd projek-fiklab/odoo-pengelolaan-mvp
./scripts/init-db.sh labfik_demo --demo   # basis data dengan data contoh fiktif
./scripts/init-db.sh labfik               # basis data kosong untuk dipakai sungguhan
```

Buka **http://localhost:8069**, pilih basis data, lalu login.

| Basis data | Login | Kata sandi | Peran |
|---|---|---|---|
| keduanya | `admin` | `admin` | Admin LabFIK + administrator Odoo (**segera ganti**) |
| `labfik_demo` | `kalab` | `kalab` | Kepala Laboratorium (Sari Wulandari, fiktif) |
| `labfik_demo` | `laboran` | `laboran` | Laboran (Dodi Pratama, fiktif) |
| `labfik_demo` | `asisten` | `asisten` | Pengguna Lab / asisten (Rani Putri, fiktif) |
| `labfik_demo` | `penilai` | `penilai` | Penilai / GKM (Gilang Ramadhan, fiktif) |

Perintah lain:

```bash
docker compose up -d          # menyalakan
docker compose stop           # mematikan (data tetap tersimpan di volume)
./scripts/run-tests.sh        # menjalankan seluruh test di basis data sementara
./scripts/backup.sh labfik    # backup basis data + filestore ke backups/
./scripts/restore.sh backups/labfik-YYYYMMDD-HHMMSS labfik_pulih
```

Setelah mengubah kode modul: `docker compose run --rm odoo odoo -d labfik -u labfik_org --stop-after-init && docker compose restart odoo`.

## Memulai di basis data kosong

Login sebagai `admin`, buka **LabFIK › Status monev › Mulai di sini**, lalu ikuti urutannya:

1. **Konfigurasi › Periode**: buat tahun akademik (semester Ganjil/Genap dibuat otomatis). Isi juga **Ruang dan lokasi**.
2. **Struktur › Jabatan**: lengkapi lima jabatan standar (uraian tugas, kewenangan, atasan, pengganti).
3. **Struktur › Personel**: tambah atau impor (⚙ › Impor, kolom `name, jenis, nomor_induk, email`). Tombol **Buat akun login** membuat akun; kata sandinya diatur di Pengaturan › Pengguna.
4. **Struktur › SK penetapan**: isi personel–jabatan, unggah PDF SK, tekan **Berlakukan SK**. Hak akses pemangku jabatan diperbarui otomatis.
5. **Dokumen**: daftarkan SOP, unggah draf, ajukan, sahkan. Lalu di **Periode › Daftar SOP wajib**, tetapkan SOP wajib dan kunci sebelum monev.
6. **Rencana kerja**: isi item, ajukan, cetak (⚙ Cetak › Rencana kerja), mintakan tanda tangan, unggah PDF, sahkan.

Status ketiga indikator ada di **Status monev › Status tata kelola** (atau tombol **Lihat status monev** di periode).

## Struktur folder

```
odoo-pengelolaan-mvp/
├── docker-compose.yml        odoo:17.0 + postgres:16, volume terpisah untuk DB dan filestore
├── config/odoo.conf
├── scripts/                  init-db, run-tests, backup, restore
└── addons/labfik_org/
    ├── models/               personel, jabatan, sk, dokumen, rencana, kepatuhan (mesin skor), dll.
    ├── views/  report/  wizard/  security/  data/  demo/
    ├── static/src/kerangka_sop.docx
    └── tests/                87 test case
```

## Validasi yang sudah dilakukan (26 Oktober 2026)

| Lapisan | Hasil |
|---|---|
| Unit/integration test Odoo (`./scripts/run-tests.sh`) | **87/87 lulus** |
| Uji ujung-ke-ujung lewat HTTP/JSON-RPC pada basis data demo baru (5 peran, alur SOP, tolak, hak akses, skor, snapshot, 4 PDF hasil wkhtmltopdf, unduh kerangka SOP, 18 model × daftar/form) | **27/27 lulus** |
| Tangkapan layar Chrome headless (status P2, versi dokumen, rencana, SK, jabatan, checklist, tampilan asisten) | Tampil benar |
| Upgrade modul (`-u labfik_org`) pada basis data yang sudah berisi data | Berhasil |
| Backup → restore → membuka laporan dan file SOP di basis data hasil pemulihan | Berhasil |

Pemetaan test ke PRD:

| File | Jumlah | Mencakup |
|---|---|---|
| `test_struktur.py` | 15 | Jabatan standar, konsistensi atasan/pengganti, SK (syarat, kunci, akhiri penetapan), lampiran tersimpan sekali di register, riwayat pemangku, personel nonaktif, bagan dan matriks, impor CSV, buat akun (TC-P3-01…07) |
| `test_akses.py` | 17 | Sinkronisasi jabatan → grup (berlaku, berakhir, cron, dua jabatan, grup manual tidak disentuh, akun dilepas), hak per peran, tombol tersembunyi, versi berlaku saja, privasi PDF SK/rencana, NIP/NIM, realisasi milik sendiri, skor penilai (TC-AKS, Lampiran B, D-4) |
| `test_dokumen.py` | 15 | Alur draf→berlaku, revisi mencabut versi lama, tolak dengan alasan, kunci file, status hanya lewat tombol, tinjau ulang, siklus dari pengaturan, distribusi/sosialisasi, pencarian per ruang, kunci daftar wajib, pengingat (TC-P2-01…07) |
| `test_skor_p2.py` | 9 | Ambang skor, **D-1 (60% → 1)**, **D-2 (90% → 3)**, N/A, 100% → 4, status dan snapshot (TC-P2-08, FR-D1, FR-D4) |
| `test_rencana.py` | 9 | Validasi item, PDF bertanda tangan, kunci isi, tolak, revisi, realisasi, tinjauan, cetak (TC-P1-01…06) |
| `test_tangga.py` | 15 | **D-3a…d**, sifat berurutan, semester berjalan, ambang dari pengaturan, K4 dengan tindak lanjut (TC-P1-06…09, TC-P3-06…09) |
| `test_umum.py` | 7 | Semester otomatis, checklist, pengaturan, status periode, semua tampilan dan menu per peran |

## Batasan yang perlu diketahui

- **Belum diuji dengan pengguna nyata.** UAT dan SUS (PRD O1, O4, O5) belum dilakukan.
- **Klik antarmuka belum diotomasi penuh.** Tampilan sudah divalidasi lewat RPC dan tangkapan layar, tetapi belum ada skenario klik browser (*tour*). Coba alurnya sekali secara manual sebelum demo.
- **Skor akhir Pengelolaan 1 dan 3 diisi Penilai** (keputusan D8 di PRD, masih menunggu persetujuan dosen). Sistem hanya menilai "lengkap secara data".
- **Ambang kriteria (K3/K4, siklus tinjau 12 bulan) adalah usulan penulis.** Ubah di Konfigurasi › Pengaturan (hanya administrator Odoo).
- **Pengaturan hanya untuk administrator Odoo** (batasan bawaan Odoo pada halaman pengaturan), bukan KaLab.
- **Tanda tangan digital tidak ada.** Pengesahan dibuktikan dengan PDF bertanda tangan yang diunggah.
- **Belum terhubung ke modul Rafika atau OpenEduCat.** Master personel dibuat sendiri dengan field mengacu ke `mst_dosen`, `op.student.assistant`, dan `res.users`; integrasinya direncanakan lewat modul jembatan.
- **Kata sandi contoh dan `admin_passwd` di `config/odoo.conf` hanya untuk laptop pengembang.** Ganti sebelum dipasang di server.
- Semua data contoh **fiktif** dan diberi label "CONTOH".
