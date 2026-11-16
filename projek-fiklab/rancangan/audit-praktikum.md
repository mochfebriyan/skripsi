# Audit dan Perbaikan Rancangan Modul Pelaksanaan Praktikum

16 November 2026 · Herrens (disusun dengan bantuan Claude Code) · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Bahan kerja, tidak masuk proposal. Mencatat audit lintas-branch atas rancangan Langkah 0–10 modul Praktikum, perbaikan yang dilakukan di branch `herrens-skripsi`, dan keputusan yang masih menunggu pihak lain. Branch lain **tidak diubah**. Perubahan di-commit dan di-push ke `herrens-skripsi` atas permintaan Herrens (16 Nov 2026).

---

## A. Ringkasan

| | Sebelum audit | Sesudah audit |
|---|---|---|
| Langkah rancangan | 0–10 lengkap; diagram lolos `validate.py` | Sama, tidak ada langkah yang hilang |
| Keterlacakan ID | KF-PRK-01–51, UC-PRK-01–28, AB-PRK-01–34 utuh | Nomor tidak digeser. Satu nomor baru: KF-PRK-52 (Pelengkap, pembacaan master Alat Core; G.2) |
| Logika bisnis | 3 cacat: jalan buntu setelah jadwal dicabut (AB-PRK-05); kelas baru bisa terpublikasi tanpa masuk jadwal bertanda tangan (AB-PRK-04); Sesi daring ikut dihitung bentrok (AB-PRK-01). 1 AB tanpa mekanisme lengkap (AB-PRK-13) | Keempatnya diperbaiki di expanded use case, SSD, CM, DCD, dan diagram |
| Konsistensi dengan Core/Tata Kelola/SDM | 1 rekomendasi keliru ke SDM (memakai `is_terpublikasi` yang tidak terbaca SDM); UC-04/06 Tata Kelola tidak dirujuk; aktor Admin memakai grup yang tidak ada; brief menulis *hook* publikasi yang sudah tidak dipakai | Diperbaiki di dokumen Praktikum. Konflik di file milik Febriyan dan Zahir dicatat sebagai usulan (bagian I) |
| Dokumen usang | Brief masih berstatus "Langkah 0", pola PKG-19 lama, daftar langkah berikutnya usang, nama status Jurnal tidak seragam (*dikirim*/*terkirim*) | Diperbarui |

## B. Snapshot branch

`git fetch origin main febriyan-skripsi zahir-skripsi herrens-skripsi` (tanpa *pull*, *prune*, atau *checkout*). Pembandingan lewat `git show`/`git diff` pada referensi `origin/*`.

| Branch | Commit | Pemilik (diverifikasi dari penulis commit dan isi file) | Kondisi |
|---|---|---|---|
| `herrens-skripsi` | `1ca3783` | Herrens (21 commit atas nama Herrens; sisanya sinkronisasi file bersama dari Febriyan) | Aktif, bersih sebelum audit; tertinggal 8 commit dari `main` tetapi seluruh file bersama identik |
| `main` | `36659ea` | Febriyan (pemilik Core) | Sumber `kontrak-core.md`, `model-core.drawio`, CLAUDE.md, brief bersama |
| `febriyan-skripsi` | `ff46281` | Febriyan | Sejak snapshot CM Praktikum (`2df910f`) hanya berubah di rujukan folder |
| `zahir-skripsi` | `e5d705f` | Zahir (11 commit atas nama Zahir) | Sejak snapshot CM Praktikum (`322c9ac`) hanya berubah di rujukan folder |

`kontrak-core.md`, CLAUDE.md, `brief-seluruh-projek.md`, dan `pemetaan-package-instrumen.md` **identik** di keempat branch. Branch `shared-to-aset-safety` tidak termasuk lingkup audit.

## C. Matriks konsistensi

### C.1 Herrens vs Main (kontrak Core)

| Hal | Kontrak Core (`main`) | Praktikum | Status |
|---|---|---|---|
| `labfik.sesi.state` | I-1: {terjadwal, terlaksana, batal} | Sama di proses bisnis, CM, DCD | Sesuai |
| Atribut hitung Sesi | C-9 menulis `is_terpublikasi`, `is_ditunda`, `is_terlewat` di `labfik.sesi` (Core) | Ditaruh di perluasan `labfik.sesi` oleh `labfik_praktikum`; hanya `is_diganti` di Core. Alasannya teknis: Core hanya `depends: ['hr', 'mail']` dan tidak bisa membaca Penetapan Jadwal/Perubahan/Jurnal | **Konflik**, usulan ke Febriyan (I.1) |
| *Hook* `_setelah_disahkan()` jadwal | Bagian 5: "menandai Sesi terpublikasi" | Tidak diisi; `is_terpublikasi` dihitung | **Konflik**, usulan ke Febriyan (I.1) |
| Arah addon | I-7: Praktikum → SDM | `depends: ['labfik_core', 'labfik_sdm', 'survey']` | Sesuai |
| Presensi petugas | I-8: `employee_id` → `hr.employee` | `labfik.praktikum.jurnal.petugas.employee_id` | Sesuai |
| Wewenang | I-4: hanya `mengesahkan` + `selection_add` 4 `jenis_dokumen` | Sama | Sesuai |
| Grup akses | I-5: 3 grup Core; dosen, asisten di Praktikum; tidak ada `labfik_admin` | DCD sesuai; kebutuhan masih menulis `labfik_admin` | **Diperbaiki** |
| `labfik.ruang.kapasitas`, `labfik.periode` tanggal | I-3 disetujui; C-6 sudah punya tanggal | Brief masih menulis [KONFIRMASI kelompok] | **Diperbaiki** |
| `labfik.bahan` (C-13) | Usulan Aset & Safety, [KONFIRMASI kelompok] | Dipakai Versi Modul dan substitusi; brief batasan masih menulis "bahan ditulis per modul" | **Diperbaiki** (brief), tetap [KONFIRMASI kelompok] |
| `labfik.alat` + `check_ketersediaan_sesi()` | Aturan pakai domain aset: Praktikum mengecek PC/alat lewat `labfik.alat`; I-13 hanya addon Aset yang mengubah `status`; I-16 versi Core memeriksa `status` dan `ruang_id` | Awalnya tidak dipakai. Sejak putaran ketiga **hanya dibaca** di Pemeriksaan Kesiapan (KF-PRK-52, O); butir tetap per kategori; `status` tidak ditulis | **Diperbaiki** (G.2). Sisa: label PKG di C-10 dan rumus `workstation_count` (I.1, I.3) |
| Pertanyaan terbuka no. 1 kontrak Core | "Pemetaan 6 → 3 status dapat diterima? (Herrens)" | Diterima 16 Nov 2026 (brief) | Jawaban perlu dicatat Febriyan (I.1) |

### C.2 Herrens vs Febriyan (Tata Kelola)

| Hal | Tata Kelola | Praktikum | Status |
|---|---|---|---|
| Use case pengesahan | UC-01 Ajukan, 02 Terbitkan, 03 Unggah, 04 Kembalikan, 05 Sahkan, 06 Cabut | Hanya UC-01, 02, 03, 05 dirujuk; KF-PRK-45 bergantung pada pencabutan | **Diperbaiki**: UC-04 dan 06 ditambahkan (dokumen + diagram UC halaman 1) |
| Operasi SSD | `ajukan_dokumen`, `terbitkan_dokumen`, `unggah_berkas_ttd`, `kembalikan_dokumen`, `sahkan_dokumen`, `cabut_dokumen`, `koreksi_rekaman` | Nama yang dirujuk benar; kembalikan/cabut belum | **Diperbaiki** |
| AB Tata Kelola | AB-01–09 pengesahan; AB-04 berkas, AB-05 wewenang | Rujukan AB-04, AB-05, AB-01–09 benar | Sesuai |
| `approval.mixin` | Template Method `action_sahkan()`; turunan hanya mengisi *hook* | `labfik.praktikum.jadwal` mengisi `_jenis_dokumen()`, `_cek_kelengkapan()`; tidak meng-*override* method utama | Sesuai |
| `evidence.mixin` | `action_koreksi()`, `_boleh_dikoreksi()`, `unlink()` ditolak | Dipakai Pemeriksaan, Jurnal, Penilaian, Evaluasi Survei | Sesuai |
| Nama model | Tata Kelola memakai `labfik.plan*`, `labfik.document*`, … | Semua `labfik.praktikum.*`; tidak ada bentrok | Sesuai |
| Contoh referensi di perbandingan proses bisnis | Versi *sweet spot* di `febriyan-skripsi` (Penjadwal hanya kedaluwarsa, Pelengkap) | Masih merujuk tag lama `rancangan-tatkel-v1` ("kedaluwarsa, pengingat") | **Diperbaiki** |

### C.3 Herrens vs Zahir (SDM)

| Hal | SDM | Praktikum | Status |
|---|---|---|---|
| Bentuk penugasan | `labfik.sdm.surat.tugas` (approval) + `labfik.sdm.penugasan` (asisten → kelas, laboran → ruang, `berlaku_mulai`/`berlaku_sampai`, `berlaku_pada()`) | `labfik.sesi.get_petugas_ditugaskan()` membaca `labfik.sdm.penugasan`; pencocokan di Praktikum (KF-PRK-51) | Sesuai |
| Dosen ditugaskan? | Tidak (peran {asisten, laboran}) | Dosen dibaca dari `labfik.kelas.dosen_ids` | Sesuai |
| `labfik.sesi.state` | `kontrak-core-sdm.md` 2.3: 6 nilai lama; `kebutuhan-sdm.md` KF-SDM-12: sudah 3 nilai | 3 nilai | **Konflik di file Zahir** (I.2) |
| Rekomendasi Praktikum ke SDM | — | CM isu 7 menyarankan SDM memakai `is_terpublikasi`, padahal field itu di `labfik_praktikum` dan SDM tidak boleh bergantung ke Praktikum | **Kesalahan Praktikum, diperbaiki**: SDM cukup `state` Core |
| Dependensi addon | `kontrak-core-sdm.md` mencatat `labfik_praktikum → labfik_sdm` "opsional" (mengikuti brief Praktikum lama) | Wajib (I-7) | **Konflik di file Zahir** (I.2) |
| Tulis ke Mata Kuliah, Kelas, Sesi | SDM tidak menulis | Hanya Praktikum yang mengubah `state` | Sesuai |
| Brief "yang disediakan" | — | Brief menulis presensi petugas "dipakai PKG-04 untuk mencocokkan" | **Diperbaiki**: pencocokan di Praktikum (I-7) |

## D. Master Data dan Core Data

| Model | Pemilik | Sumber kebenaran | Hasil |
|---|---|---|---|
| `hr.employee`, `hr.job`, `labfik.jabatan.wewenang` | Febriyan (Core) | `kontrak-core.md` C-1, C-2, C-4 | Dipakai, tidak diduplikasi. Praktikum hanya `selection_add` `jenis_dokumen` |
| `labfik.ruang`, `labfik.periode` | Febriyan (Core) | C-5, C-6 | Dipakai; usulan `kapasitas` sudah disetujui |
| `labfik.mata.kuliah`, `labfik.kelas`, `labfik.sesi` | Herrens (dirancang Praktikum, ditempatkan di Core) | C-7–C-9 + DCD-1 Praktikum | Field tersimpan sama dengan kontrak; tipe ditetapkan di DCD-1. Atribut hitung di perluasan Praktikum (konflik C.1) |
| `labfik.bahan` | Kelompok Aset & Safety (Core, usulan) | C-13 | Dipakai dengan jalan pengganti teks bila ditolak |
| `labfik.alat` | Kelompok Aset (Core, usulan) | C-10 | Hanya dibaca lewat `check_ketersediaan_sesi()` (Pelengkap, KF-PRK-52). Jalan pengganti bila master Alat belum terisi: laboran mengisi jumlah stasiun kerja berfungsi sendiri |
| Mahasiswa | — | Pemetaan bersama | Tidak dipakai (praktikan = jumlah, atau NIM di baris nilai Pelengkap) |
| Master lokal Praktikum | — | — | Nol. *Software* ditulis per Versi Modul |

Tidak ditemukan model yang dibuat ulang padahal sudah dimiliki modul lain, dan tidak ada nama model yang bentrok.

## E. Keterlacakan

Diperiksa dengan skrip (bukan hanya keberadaan ID, juga rentang dan rujukan silang):

| Rantai | Hasil |
|---|---|
| Instrumen → kriteria → KF | Setiap kriteria PKG-15 C1–C4, 16 S1–S4, 17 B1–B3, 18 C1–C5, 19 P1–P4, 20 K1–K4 punya KF (kebutuhan bagian 5) |
| KF → UC | 52/52 KF tertutup UC atau perilaku sistem (use case 7.1). Daftar KF *hidden* di kebutuhan bagian 5 dilengkapi dengan 45, 46, 49, 51, 52 |
| Activity / state machine → UC | Setiap tugas «user» dan event S1–S3 punya UC (use case 4.1–4.2). Transisi *hapus* Sesi diselaraskan dengan AB-PRK-04 baru |
| UC → AB | 34/34 AB dirujuk UC (expanded use case bagian 2) |
| UC → operasi SSD | 28/28 UC punya operasi (SSD 6.1); 21 command dan 32 query dihitung ulang dan cocok |
| DTO → CM | Semua isi kamus DTO punya tempat (CM bagian 4) |
| Operasi → method, AB → mekanisme Odoo | 53 operasi + pola CRUDL terpetakan (DCD 5); 34/34 AB terpetakan (DCD 6). AB-PRK-13 kini lengkap |
| Rujukan rusak | Tidak ada KF/UC/AB di luar rentang; tidak ada tautan Markdown rusak |

## F. Logika bisnis

Simulasi konseptual alur utama (impor → penetapan → kesiapan → jurnal → perubahan → survei) menemukan:

| No | Skenario | Masalah | Perbaikan |
|---|---|---|---|
| F1 | KaLab mencabut Penetapan Jadwal yang salah, lalu laboran ingin menyusun yang benar | `_cek_satu_per_periode()` menolak jadwal kedua untuk periode yang sama: **jalan buntu**, Sesi periode itu tidak pernah bisa terpublikasi lagi | AB-PRK-05 = satu jadwal **aktif** (draf/diajukan/disahkan) per periode; `_cek_satu_aktif_per_periode()` |
| F2 | Setelah jadwal disahkan, fakultas mengirim kelas tambahan dan laboran mengimpornya | Kelas baru belum punya Sesi, jadi lolos E2; Sesinya langsung terbaca terpublikasi (dihitung per periode) padahal tidak ada di PDF bertanda tangan. Bukti PKG-15 C1 menjadi tidak jujur | AB-PRK-04: impor seluruh periode terkunci selama jadwal diajukan atau disahkan (selaras AB-01 Tata Kelola: isi dokumen hanya berubah saat Draf). Kelas tambahan masuk lewat cabut → impor → susun ulang |
| F3 | Perubahan "daring" disetujui, lalu ada pengajuan pemakaian ruang pada jam itu | `cari_bentrok()` masih menghitung Sesi daring sehingga pemakaian ditolak, padahal ruang kosong | AB-PRK-01 dan `cari_bentrok()` hanya Sesi `luring` |
| F4 | Laboran mencatat pemeriksaan kesiapan untuk Sesi yang jadwalnya belum disahkan | AB-PRK-13 mensyaratkan Sesi terpublikasi, tetapi DCD tidak punya mekanisme | `labfik.praktikum.kesiapan._cek_sesi()` @constrains |
| F5 | KF-PRK-26 menyebut "keputusan tunda" mengubah status Sesi | Sejak I-1, tunda tidak mengubah `state` (hanya memicu Perubahan Sesi) | Bunyi KF-PRK-26 diperbaiki |

Diperiksa dan **tidak** diubah, karena bukan cacat atau tidak berdasar kriteria:
- Dua Perubahan Sesi yang diajukan bersamaan untuk Sesi yang sama: yang kedua gagal di E2 (Sesi tidak lagi `terjadwal`) dan dapat ditolak KaLab. Tidak buntu, jadi tidak perlu aturan baru.
- Pemakaian lab yang disetujui lalu batal dipakai: tetap pertanyaan P3 untuk KaLab.

## G. Diagram

| File | Halaman | Diubah | Validasi |
|---|---|---|---|
| `activity-state-praktikum.drawio` | 8 | S1: *guard* transisi *hapus*; S2: judul "Pemakaian Lab" | `validate.py prk-` OK; `cek_tampilan.py` 0 temuan |
| `use-case-praktikum.drawio` | 3 | Halaman 1: catatan Tata Kelola + UC-04, UC-06 (tinggi catatan dan halaman ditambah 20 px) | OK; 0 temuan |
| `ssd-praktikum.drawio` | 5 | SSD-1: teks E2 (AB-PRK-04) | OK. `cek_tampilan.py` melaporkan pesan yang melintasi *lifeline* tengah dan fragmen `opt`; itu bentuk normal SSD, bukan cacat (sudah begitu sebelum audit) |
| `conceptual-model-praktikum.drawio` | 4 | CM-1: invarian AB-PRK-05 | OK; 0 temuan |
| `class-praktikum.drawio` | 5 | DCD-1: `_cek_satu_aktif_per_periode()`, `_cek_terkunci(periode, kelas)`, `cari_bentrok` (luring); DCD-3: `_cek_sesi()` di Pemeriksaan Kesiapan | OK; 0 temuan |

Sebelum diubah, kelima `.drawio` di-*generate* ulang dari skripnya dan **identik byte demi byte**, jadi skrip adalah sumber yang benar. Setelah diubah, semuanya di-*generate* ulang dari skrip. Notasi diperiksa terhadap CLAUDE.md bagian 5: CM tanpa method dan tanpa tipe Odoo; DCD memakai mixin ungu, «Core» putus-putus, Template Method + *hook*; semua ID berawalan `prk-`.

### G.1 Pemeriksaan visual di draw.io (16 Nov 2026, putaran kedua)

Ke-25 halaman diekspor ke PNG dengan draw.io desktop (`draw.io -x -f png -p n`), lalu dibaca satu per satu untuk mengecek logika alur, kecocokan dengan dokumen, dan keterbacaan. Temuan dan perbaikannya:

| No | Halaman | Temuan | Jenis | Perbaikan |
|---|---|---|---|---|
| V1 | A2 | Sesudah *Ubah waktu pemakaian*, alur kembali ke *Catat pengajuan pemakaian*, sehingga pengajuan seolah dicatat dua kali | Logika | Alur kembali ke *merge* sebelum *Periksa bentrok ruang* |
| V2 | A5 | Sesudah *Lengkapi survei*, alur kembali ke *Susun survei periode* (menyusun ulang), padahal di S3 kelengkapan adalah *guard* transisi *tetapkan* | Logika | Alur kembali ke *merge* sebelum *Tetapkan survei*; catatan bahwa kelengkapan = *guard* S3 |
| V3 | S2, proses bisnis 3.2 | *Guard* `setujui` tidak memuat *tidak bentrok*. Karena AB-PRK-01 hanya menghitung pemakaian yang Disetujui, dua pengajuan untuk slot yang sama bisa sama-sama Diajukan. DCD 4.1 (`_sebelum_disetujui`) sudah memeriksa ulang, tetapi diagram dan tabel belum | Logika (tidak konsisten antar-artefak) | *Guard* `[KaLab ∧ tidak bentrok]`; catatan A2 "Cek ulang saat disetujui"; teks A2 di proses bisnis |
| V4 | A1, A2, proses bisnis A1, expanded UC-PRK-03 E1 dan UC-PRK-10 | "Bentrok yang ditemukan menjadi rekaman konflik" bertentangan dengan CM (rekaman konflik bukan konsep; bentrok saat impor tidak tersimpan) dan DCD (laporan dari `karena_bentrok` + Sesi diganti) | Konsistensi | Semua teks diseragamkan: bentrok saat impor atau saat dicatat hanya ditampilkan **[ASUMSI]**; rekaman konflik = penolakan `karena_bentrok` + Sesi yang diganti |
| V5 | DCD-1 | Label `periode_id 1 (unik)` pada Penetapan Jadwal bertentangan dengan AB-PRK-05 versi audit (satu jadwal **aktif** per periode; yang dicabut tetap tersimpan) | Logika | Label menjadi `periode_id 1` |
| V6 | SSD-1 E2 | Teks "kelas itu dilewati; perubahannya lewat UC-PRK-14" tidak menyebut jalan untuk kelas baru (F2) | Konsistensi | Ditambah "kelas baru menunggu jadwal dicabut (UC-06 Tata Kelola) lalu disusun ulang", selaras dengan expanded E2.2 |
| V7 | SSD-3 E1, expanded UC-PRK-13 E1 | Tidak menyebut Sesi yang tidak `terjadwal` (mis. batal), padahal AB-PRK-17 mensyaratkannya | Konsistensi | Ditambahkan |
| V8 | CM-1 | Garis generalisasi PemakaianLab → Pengajuan menumpuk di segmen yang sama dengan asosiasi Sesi–PerubahanSesi, sehingga PemakaianLab tampak berasosiasi dengan Sesi | Keterbacaan yang menyesatkan | Jalur kedua garis dipisah |
| V9 | CM-2 | Multiplisitas `1` di ujung Sesi (asosiasi ke PemeriksaanKesiapan) tertutup label `0..1 pemeriksaan` | Keterbacaan | Kotak Sesi dipersempit; label terlihat |
| V10 | UC-1–3 | Legenda menyebut "aktor miring biru", padahal yang biru hanya isi kepala aktor | Notasi | "Aktor bernama miring (kepala biru muda)" |
| V11 | A1, A2, A5, S2 | Teks catatan meluber keluar kotak atau menumpuk dengan catatan berikutnya | Keterbacaan | Tinggi catatan disesuaikan; catatan S2 digeser |

Diperiksa dan **tidak** diubah:
- A4 menggambar *Setujui perubahan* sebelum *Periksa bentrok waktu pengganti*, sedangkan SSD-4 memeriksa bentrok sebelum keputusan dikirim. Keduanya terjadi dalam satu sesi kerja KaLab, dan perintah `putuskan_pengajuan()` baru dijalankan sesudah cek lolos. Jadi activity hanya lebih kasar, tidak bertentangan.
- Pesan SSD yang melintasi *lifeline* tengah dan fragmen `opt` (laporan `cek_tampilan.py`): jumlahnya sama dengan versi yang sudah di-commit, dan itu bentuk normal SSD.
- Teks yang mepet ke tepi kanan beberapa catatan (Notasi SSD, catatan CM-3 dan CM-4): masih terbaca, tidak terpotong.

### G.2 Pengecekan ulang alat dan bahan Core (16 Nov 2026, putaran ketiga)

Kontrak Core (`main`) menambah domain aset: `labfik.alat` (C-10), kategori alat (C-11), lokasi simpan (C-12), `labfik.bahan` (C-13), serta keputusan I-12, I-13, I-15, I-16. Isinya dicocokkan dengan rancangan Praktikum. Keputusan Herrens: ikuti ketentuan Core dengan prinsip *sweet spot*.

| Hal | Kontrak Core | Rancangan Praktikum sebelum | Tindakan |
|---|---|---|---|
| Master Bahan (C-13) | `kode`, `name`, `satuan`, `jenis`, `stok_minimum`, `lokasi_simpan_id`, `is_berbahaya_b3` | KebutuhanBahan dan substitusi merujuk Bahan (kode, nama, satuan) | Sesuai, tidak diubah |
| Stok bahan berjalan (I-15) | Dicatat di addon Aset/Safety, bukan Core | `jumlah_tersedia` diisi laboran saat pemeriksaan (analisis PKG-17) | Sesuai: Praktikum tidak bergantung ke addon Aset, jadi tetap diisi manual |
| Aturan pakai: Praktikum mengecek PC/alat lewat `labfik.alat` | Ditulis sebagai aturan pakai bersama | Alat tidak dipakai | **Diselaraskan** (lihat bawah) |
| Status alat (I-13) | Hanya addon Aset yang mengubah `status` | — | Praktikum hanya membaca |
| `check_ketersediaan_sesi(sesi)` (I-16) | Versi Core memeriksa `status` dan `ruang_id`; Aset meng-*override* untuk peminjaman | — | Dipanggil Praktikum; hasil *override* Aset ikut terbaca tanpa `depends` ke Aset |
| `labfik.ruang.workstation_count` (I-12) | {compute}, rumus ditetapkan Aset | `jumlah_dibutuhkan` dari jumlah mahasiswa kelas | Ditampilkan sebagai pembanding saja |

Rancangan *sweet spot* yang diterapkan:
- **Lantai tetap sama.** PKG-16 S2 sudah terbukti lewat butir per kategori yang diisi laboran; tidak ada kriteria yang gagal tanpa master Alat. Karena itu bagian Alat masuk lapis **Pelengkap (O)**, sebagai KF-PRK-52.
- **Hanya membaca.** Saat form dibuka, alat di ruang Sesi yang `check_ketersediaan_sesi()` = salah ditampilkan sebagai peringatan pada butir kategori padanannya (`hardware_pc` → stasiun kerja, `jaringan` → jaringan, `multimedia` → proyektor/audio; jenis lain tidak relevan untuk lab komputer **[ASUMSI]**). Jumlah PC yang tersedia menjadi isian awal `jumlah_berfungsi`.
- **Tidak dirancang:** butir per unit alat, perubahan `status` alat dari Praktikum, kalibrasi (Core hanya punya penanda, tanpa masa berlaku), dan dependensi ke addon Aset.

| File | Perubahan |
|---|---|
| `analisis/analisis-data-persiapan-16.md` | Bagian 5 baris Alat (hanya dibaca, jalan pengganti); bagian 6 dependensi Alat dan catatan pemetaan |
| `brief/brief-praktikum.md` | Kontrak "Yang dipakai" + baris master Alat; baris di "tidak dipakai" dipersempit menjadi butir per unit |
| `rancangan/kebutuhan-praktikum.md` | KF-PRK-52 (H, O); jumlah 52 KF (41 W, 11 O); daftar KF *hidden* |
| `rancangan/proses-bisnis-praktikum.md`, `activity_state.py` | A3: teks dan catatan "Kaitan ke kriteria" |
| `rancangan/use-case-praktikum.md`, `use_case.py` | KF-PRK-52 → UC-PRK-11 (*hidden*); 52 KF; catatan UC-2 |
| `rancangan/expanded-use-case-praktikum.md` | AB-PRK-14 diperluas (tanpa AB baru); UC-PRK-11 langkah 4 |
| `rancangan/ssd-praktikum.md`, `ssd.py` | Catatan `form_kesiapan`; `dto_form_kesiapan` + `alat_tidak_tersedia*`, `jumlah_pc_tersedia`, `workstation_count` (O); label SSD-2 |
| `rancangan/conceptual-model-praktikum.md`, `conceptual_model.py` | CM-2: stub Alat, asosiasi turunan Sesi `/alat_tidak_tersedia`, `/jumlah_pc_tersedia`; temuan 5.2 no. 2; isu terbuka |
| `rancangan/design-class-praktikum.md`, `design_class.py` | DCD-3: stub «Core» `labfik.alat`, `alat_tidak_tersedia_ids` {compute}, `jumlah_pc_tersedia` {compute}, `_compute_ketersediaan_alat()`; pemetaan operasi, AB-PRK-14, tabel revisi, cek silang |

Halaman A3, UC-2, SSD-2, CM-2, dan DCD-3 dirender ulang dan diperiksa. Satu masalah tampilan ditemukan dan diperbaiki: label *return* SSD-2 terlalu panjang sehingga melewati *lifeline* Laboran.

## H. Changelog

| File | Masalah awal | Perbaikan | Dasar |
|---|---|---|---|
| `brief/brief-praktikum.md` | Status "Langkah 0, belum ada rancangan"; pola C masih "penilaian di Jurnal Sesi" dan hitungan 8 transaksi; *hook* publikasi; presensi "dipakai PKG-04"; `kapasitas`/periode masih [KONFIRMASI]; batasan "bahan ditulis per modul"; langkah berikutnya usang; tidak ada tabel keputusan | Status, pola C, hitungan 9 transaksi, *hook* dihapus, I-7, I-3/C-6, `labfik.bahan` + `labfik.alat` dicatat, batasan 4, langkah berikutnya, tabel "Arahan pembimbing dan keputusan" (merangkum keputusan yang sudah tercatat) | Kontrak Core I-3, I-7, C-6, C-13; keputusan 14 Nov (PKG-19); DCD 2 dan 4.3; CLAUDE.md langkah 1 |
| `rancangan/kebutuhan-praktikum.md` | Aktor Admin + grup `labfik_admin` yang tidak ada; KF-PRK-26 "keputusan tunda"; daftar KF *hidden* kurang 45, 46, 49, 51 | Admin bukan aktor modul (`base.group_system`); KF-PRK-26 dibetulkan; daftar dilengkapi | Kontrak Core G; I-1; use case 7.1 |
| `rancangan/proses-bisnis-praktikum.md` | Sisa status lama (Diganti/Dibatalkan, "Dicabut → Rencana"); Jurnal *Dikirim*; *hook* publikasi; isu KF-PRK-45 masih terbuka; perbandingan memakai tag lama | Diselaraskan dengan 3 status; Jurnal *Terkirim*; tanpa *hook*; isu ditutup; perbandingan versi *sweet spot* | I-1; DCD 4.3; brief Tata Kelola |
| `rancangan/use-case-praktikum.md` | UC-04/06 Tata Kelola tidak dirujuk; label "Rencana Pemakaian Lab"; *guard* hapus | Ditambahkan; label baku; *guard* | KF-PRK-45; CM temuan 5; AB-PRK-04 |
| `rancangan/expanded-use-case-praktikum.md` | F1–F3 | AB-PRK-01, 04, 05; UC-PRK-03 E2; UC-PRK-04; catatan temuan 6.3 | Bagian F |
| `rancangan/ssd-praktikum.md` | Operasi kembalikan/cabut tidak dirujuk | Ditambahkan; catatan audit | SSD Tata Kelola |
| `rancangan/conceptual-model-praktikum.md` | Rekomendasi `is_terpublikasi` untuk SDM keliru; invarian AB-PRK-05 | Dibetulkan; catatan perubahan bagian 6 | I-7; `kebutuhan-sdm.md` KF-SDM-12 |
| `rancangan/design-class-praktikum.md` | F1–F4; operasi kembalikan/cabut; isu SDM | Bagian 4.3, 5.1, 6, 8 (tabel revisi), 10 | Bagian F, C |
| `analisis/analisis-data-proses-18.md`, `analisis/bedah-dokumen-praktikum.md` | Status *dikirim*, field `tanggal_kirim` | *terkirim*, `waktu_kirim` | DCD-4 |
| `tools/drawio/praktikum/*.py` + 5 `.drawio` | Lihat bagian G | Lihat bagian G | — |
| Putaran kedua (pemeriksaan visual): `activity_state.py`, `ssd.py`, `conceptual_model.py`, `design_class.py`, `use_case.py`, 5 `.drawio`, `proses-bisnis-praktikum.md` (A1, A2, tabel 3.2), `expanded-use-case-praktikum.md` (UC-PRK-03 E1, UC-PRK-13 E1, UC-PRK-10) | V1–V11 | Lihat G.1 | Render PNG tiap halaman |
| Putaran ketiga (alat dan bahan Core): 9 dokumen + 5 skrip + 5 `.drawio` | `labfik.alat` belum diselaraskan dengan aturan pakai domain aset | KF-PRK-52, lihat G.2 | Kontrak Core C-10–C-13, I-12, I-13, I-15, I-16 |

## I. Keputusan yang belum selesai

Hal di bawah ini **tidak** diputuskan sepihak. Rancangan Praktikum memakai pilihan sementara yang paling aman.

**I.1 Untuk Febriyan (pemilik `kontrak-core.md`, branch `main`)**
1. C-9: pindahkan `is_terpublikasi`, `is_ditunda`, `is_terlewat` dari daftar field Core ke "perluasan `labfik_praktikum`"; hanya `is_diganti` di Core. Sementara: DCD Praktikum sudah begitu.
2. Bagian 5: hapus "*hook* `_setelah_disahkan()` menandai Sesi terpublikasi"; jadwal tidak mengisi *hook* itu.
3. Bagian 7 no. 1: catat jawaban Herrens: pemetaan 6 → 3 status **diterima** (16 Nov 2026).
4. C-10 menulis pemakai pemeriksaan kesiapan sebagai "PKG-15/18"; pemeriksaan kesiapan adalah **PKG-16**. Usulan: label diganti PKG-16 (dan PKG-17 untuk bahan). Aturan pakai "Praktikum mengecek PC/alat lewat `labfik.alat`" sudah diikuti sebagai Pelengkap (G.2). *Butir ini menggantikan usulan lama agar aturan itu dijadikan opsional.*

**I.2 Untuk Zahir (`kontrak-core-sdm.md`, branch `zahir-skripsi`)**
1. Bagian 2.3: `state` Sesi = {terjadwal, terlaksana, batal}; asumsi pengganti "sesi `terjadwal` yang tanggalnya lewat" (sudah dipakai di `kebutuhan-sdm.md` KF-SDM-12). Jangan memakai `is_terpublikasi`: field itu ada di `labfik_praktikum`.
2. Catatan dependensi "`labfik_praktikum` → `labfik_sdm` opsional" diganti **wajib** (kontrak Core I-7).

**I.3 Untuk kelompok Aset & Safety**
- Master Bahan `labfik.bahan` (C-13) disetujui masuk Core? Bila tidak, Versi Modul kembali memakai nama dan satuan bahan sebagai teks.
- Rumus `labfik.ruang.workstation_count` (I-12). Praktikum hanya menampilkannya sebagai pembanding; isian awal `jumlah_berfungsi` dihitung sendiri dari alat jenis `hardware_pc` yang tersedia **[KONFIRMASI kelompok Aset]**.
- Pemetaan jenis kategori alat → kategori butir kesiapan (`hardware_pc`, `jaringan`, `multimedia`) **[ASUMSI]**.

**I.4 Untuk KaLab (wawancara P1–P19, belum dilakukan)**
- Pengesah jadwal (P5), pengisi jurnal kelas tanpa asisten (P10, P13), pemeriksaan per sesi atau per hari (P8), isi berkas jadwal fakultas (P2), sesi daring sah (P12), pemakaian lab yang batal (P3), siapa boleh mengoreksi jurnal terkirim (P11), data wewenang Kepala Laboratorium untuk empat jenis dokumen Praktikum, isi awal 8 ruang.

**I.5 Untuk Pak Widi**
- Judul; cakupan rancangan (brief, Langkah 1); PKG-19 lewat tautan LeADS per kelas; skor PKG-20 ditetapkan penilai; rekaman konflik dari impor tidak disimpan (hanya penolakan `karena_bentrok`).

**I.6 Saat implementasi [VALIDASI]**
- Nama field dan method `survey.survey` Odoo 17 (`access_mode`, `_create_answer`, `answer_done_count`).

**I.7 Asumsi kerja sementara (16 Nov 2026, atas permintaan Herrens)**

Sampai ada jawaban dari pihak di I.1–I.5, rancangan memakai keputusan di bawah ini. Semuanya sudah sesuai dengan isi rancangan sekarang, jadi tidak ada artefak yang berubah karenanya. Bila jawaban nanti berbeda, butir terkait diperbarui.

| No | Hal | Asumsi yang dipakai **[ASUMSI]** | Alasan |
|---|---|---|---|
| 1 | Atribut hitung Sesi (I.1 no. 1) | `is_terpublikasi`, `is_ditunda`, `is_terlewat` di perluasan `labfik_praktikum`; hanya `is_diganti` di Core | Core `depends: ['hr', 'mail']` tidak bisa membaca model Praktikum |
| 2 | *Hook* publikasi (I.1 no. 2) | Tidak dipakai; `is_terpublikasi` dihitung | Prinsip "hitung, bukan jadwalkan" |
| 3 | Pemetaan 6 → 3 status Sesi (I.1 no. 3) | Diterima | Sudah diputuskan Herrens |
| 4 | Label PKG di C-10 (I.1 no. 4) | Pemeriksaan kesiapan = PKG-16 (bahan PKG-17) | Bunyi indikator di instrumen |
| 5 | Kontrak SDM (I.2) | SDM membaca `state` Core; `labfik_praktikum` → `labfik_sdm` wajib | Kontrak Core I-1, I-7 |
| 6 | Master Bahan C-13 (I.3) | Disetujui masuk Core | Sudah tercantum di kontrak Core; jalan pengganti teks tetap dicatat |
| 7 | `workstation_count` (I.3) | Hanya pembanding; isian awal `jumlah_berfungsi` = jumlah alat `hardware_pc` di ruang Sesi yang tersedia | Tidak bergantung pada rumus kelompok Aset |
| 8 | Jenis alat → kategori butir (I.3) | `hardware_pc` → stasiun kerja, `jaringan` → jaringan, `multimedia` → proyektor/audio; `instrumen_ukur` dan `mesin_lab` tidak dipakai | Lab FIK adalah lab komputer |
| 9 | Pengesah jadwal (P5) | KaLab | Sudah dipakai di KF-PRK-06 |
| 10 | Pengisi jurnal kelas tanpa asisten (P10, P13) | Dosen yang mengajar | Sudah dipakai di aktor Petugas Praktikum |
| 11 | Pemeriksaan per sesi atau per hari (P8) | Per sesi | Bunyi instrumen PKG-16 |
| 12 | Berkas jadwal fakultas (P2) | Impor berkas Excel dengan templat baku, tanpa API | Sudah dipakai di UC-PRK-03 |
| 13 | Sesi daring sah (P12) | Sah, sebagai nilai awal pengaturan yang dapat diubah KaLab (KF-PRK-43) | Tidak mengurangi bukti; tetap bisa diubah tanpa ubah rancangan |
| 14 | Pemakaian lab disetujui lalu batal (P3) | Tidak dirancang; ruang tetap tercatat terpakai | Tidak ada kriteria yang gagal tanpanya (batasan masalah) |
| 15 | Koreksi jurnal terkirim (P11) | Hanya grup laboran dan KaLab, tercatat di riwayat | Usulan penulis di DCD 4 |
| 16 | Arahan pembimbing (I.5) | Cakupan brief, PKG-19 lewat tautan LeADS, skor PKG-20 ditetapkan penilai, bentrok saat impor tidak disimpan | Sudah dipakai di seluruh rancangan |

## J. Verifikasi akhir

| Pemeriksaan | Hasil |
|---|---|
| Branch aktif | `herrens-skripsi`; branch lain tidak di-*checkout*, tidak diubah |
| `git diff --check` | Bersih |
| File berubah | 21 file berubah (213 baris ditambah, 145 dihapus, terhitung sampai putaran ketiga) + laporan ini sebagai file baru; tidak ada file yang dihapus |
| `validate.py <file> prk-` | OK untuk 25 halaman di 5 file |
| `cek_tampilan.py` | 0 temuan di activity/state, use case, CM, DCD; SSD hanya melaporkan pola normal (bagian G) |
| Render visual draw.io | 25/25 halaman diekspor ke PNG dan diperiksa; 11 temuan (G.1) diperbaiki; halaman yang berubah dirender ulang dan dicek lagi. Putaran ketiga: A3, UC-2, SSD-2, CM-2, DCD-3 dirender ulang (G.2) |
| Skrip vs `.drawio` | Kelima file `.drawio` = hasil skrip terbaru |
| ID | 52 KF, 28 UC, 34 AB terdefinisi berurutan; 0 rujukan di luar rentang di 13 dokumen Praktikum |
| Cakupan pemetaan | 34/34 AB di DCD; 28/28 UC punya operasi SSD |
| Tautan Markdown relatif | 0 rusak |
| Data pribadi | Tidak ada pola NIM, nomor HP, e-mail, rekening, atau KTP di baris yang ditambahkan |
| File milik orang lain | `kontrak-core.md`, CLAUDE.md, file bersama, file Febriyan dan Zahir, `skripsi_rafika/`: tidak disentuh |
| Commit / push | Dilakukan atas permintaan Herrens, hanya ke `herrens-skripsi` |

## K. Kesimpulan

**READY WITH OPEN DECISIONS.**

Rancangan Langkah 0–10 lengkap dan saling terlacak. Setiap kriteria instrumen PKG-15–20 punya kebutuhan, aturan bisnis, operasi, dan mekanisme Odoo. Diagram lolos validator dan sudah diperiksa secara visual di draw.io. Cacat logika yang ditemukan (bagian F dan G.1) sudah diperbaiki tanpa menambah fitur. Modul siap dipakai untuk Bab II 2.3 dan sebagai dasar implementasi.

Domain aset baru di kontrak Core sudah dicocokkan (G.2): Bahan sesuai, Alat dibaca sebagai Pelengkap tanpa menambah tabel atau dependensi.

Status belum READY karena: (1) tiga penyesuaian kontrak Core dan dua penyesuaian kontrak SDM masih harus dilakukan pemiliknya (I.1, I.2); (2) master Bahan Core belum disetujui kelompok (I.3); (3) wawancara KaLab belum dilakukan, sehingga beberapa aktor dan wewenang masih **[ASUMSI]** (I.4); (4) cakupan dan dua aturan skor belum dikonfirmasi pembimbing (I.5). Untuk sementara semuanya dijalankan dengan asumsi di I.7. Tidak satu pun yang menghalangi penulisan proposal. Butir (1) dan (3) perlu selesai sebelum kode `labfik_core` ditulis.
