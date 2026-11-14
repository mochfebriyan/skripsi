# Analisis Data Indikator Persiapan 15 (Jadwal dan Modul)

14 November 2026 · Herrens · PKG-15 Persiapan 15 (jadwal dan modul) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab; wawancara bagian Pelaksanaan Praktikum belum dijawab.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2: **target → aturan memenuhi → luaran (bukti dukung) → data transaksi → master data → dependensi dan jalan pengganti → yang ditunda → pertanyaan untuk narasumber**. Contoh format: `analisis-data-pengelolaan-1-3.md` di tag `rancangan-tatkel-v1` dan analisis awal Proses 18 (`git show 62e50ce:projek-fiklab/analisis/analisis-data-proses-18.md`).

Sumber utama: baris ID 15 di *Instrumen Monev Laboratorium UPNVJ 2026 v1.1* (Sheet1 dan tab *Analysis* baris 32), [pemetaan-package-instrumen.md](pemetaan-package-instrumen.md) bagian 5–6, dan dokumen lab yang dibedah di bagian 0.

---

## Ringkasan

| | Persiapan 15 |
|---|---|
| Inti | Setiap sesi praktikum punya jadwal sah tanpa konflik, dan modul versi berlaku sudah tersedia sebelum sesi dimulai |
| PJ (instrumen) | KaLab; dosen pengampu |
| Jenis skor | **Persentase** |
| Unit | 1 sesi praktikum yang direncanakan pada periode monev |
| Level cakupan (usulan) | **Otomatis**. Relevansi isi modul tetap dinilai penilai |
| Posisi dalam dependensi | **Hulu modul Praktikum**. Sesi yang dibangkitkan di sini dipakai PKG-04, 08, 16, 17, 18, 19 |
| Acuan ISO/IEC 17025 | 7.2.1.2–7.2.1.3 (metode dan dokumen pendukung mutakhir, tersedia, versi valid terbaru) · 8.3 (pengendalian dokumen) · 6.3.1 (fasilitas sesuai kegiatan) |
| Kompleksitas (kasar) | **7** (rincian di bagian 8) |

**Temuan utama:**
1. **Pembagi indikator belum bisa dibentuk dari data lab saat ini.** Tidak ada daftar sesi bertanggal. Sheet alokasi hanya berisi pertemuan 1–15 per kelas tanpa hari dan jam (A1). Karena itu tugas pertama PKG-15 adalah **membangkitkan Sesi bertanggal**, yang sekaligus menjadi pembagi PKG-18.
2. **Tidak ada modul acuan bersama.** Hampir setiap laporan sesi membawa berkas modulnya sendiri (1.062 tautan unik dari 1.064 laporan), tanpa nomor versi, dan dikirim sesudah sesi (A4, A9). Tidak ada rekaman bahwa modul tersedia sebelum sesi.
3. **Pemakaian lab di luar praktikum dan konflik jadwal tidak diatur di dokumen nyata mana pun** (A5). Bukti 1, 2, dan 5 instrumen belum punya padanan *as-is*. Laporan sesi memuat 24 tumpang tindih ruang dan waktu yang ternyata akibat salah isi jam (A11). Ini memperkuat alasan jam sesi harus berasal dari jadwal yang ditetapkan, bukan diketik ulang asisten saat melapor.
4. **Data untuk cek kapasitas belum ada.** Sheet alokasi tidak punya kolom ruang maupun jumlah mahasiswa (A10).

**Keputusan yang sudah diambil (Herrens, 14 Nov 2026):**
- Sesi, Mata Kuliah, dan Kelas masuk `labfik_core`. Sesi menjadi model sendiri tanpa mewarisi `op.session`, supaya `labfik_core` tetap `depends: ['hr', 'mail']`. Sudah dicatat di kontrak Core (CLAUDE.md bagian 6), tabel keputusan brief bersama, dan pemetaan bagian 5.
- Modul **cukup diterbitkan dosen dengan nomor versi**, tanpa tahap pengesahan.

---

## 0. Sumber dan temuan *as-is*

### Dokumen yang dipakai

| Dokumen | Sifat | Tanggal | Yang relevan untuk PKG-15 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`, Drive LabFIK) | **Nyata**, belum disahkan (nomor dan tanggal pengesahan kosong) | 2025 | Langkah 1 (alokasi MK), 7 (modul), 14–15 (penyesuaian jadwal dan modul); Formulir Alokasi Praktikum; Template Modul Praktikum |
| Sheet "Alokasi Pertemuan Asisten Praktikum" | **Data nyata** (berisi data pribadi, tidak dikutip) | Dibaca penuh 17 Okt 2026 (catatan di brief bersama dan `brief-role-3.md` commit `d6fcc5c`); struktur tab dan kolom dicek ulang 14 Nov 2026 | Bentuk rencana per kelas; kolom yang tersedia |
| Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" (Responses) | **Data nyata** (berisi data pribadi, tidak dikutip) | Dibaca penuh 17 Okt 2026; diolah ulang 14 Nov 2026 (1.147 laporan, data sampai 10 Nov 2026). Yang dikutip hanya angka agregat | Kolom periode, MK, kelas, tanggal, jam, ruang, pertemuan, dan "Modul Praktikum" |
| Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (STD-PRK-02, TPL-PRK-01, FRM-PRK-01, FRM-PRK-07) | **Draf**, kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep–Okt 2026 | Contoh format saja. Bukan sumber kebutuhan |
| Paket Dokumen Monev `DOCUMENTS/18_Standar_Modul_Jadwal_Kesiapan_Praktikum` | **Draf GPT** | Okt 2026 | Contoh format saja |

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | Rencana praktikum disimpan per kelas, dengan 14 kolom pertemuan (1–7 dan 9–15; 8 = UTS, 16 = UAS) yang diisi nama asisten. **Kolom hari, jam mulai, dan jam selesai kosong di seluruh 222 baris kelas** (2025/2026 Ganjil 71, 2025/2026 Genap 79, 2026/2027 Ganjil 72). Jadi tidak ada sesi bertanggal | Sheet Alokasi (diunduh dan diolah penuh 14 Nov 2026) |
| A2 | Kelas tanpa asisten tetap tercantum di sheet Alokasi, tetapi kolom pertemuannya kosong: 40 dari 71 (56%), 33 dari 79 (42%), dan 40 dari 72 (56%) kelas per periode. Pertemuan berasisten yang direncanakan: 344, 644, dan 303 | Sheet Alokasi (diolah 14 Nov 2026) |
| A3 | Daftar MK praktikum dan jumlah kelas diajukan Koordinator Program Studi, ditinjau KaLab, dan disetujui Wakil Dekan Bidang Akademik (Formulir Alokasi Praktikum). Formulir ini tidak memuat hari, jam, atau ruang | POB 2025 langkah 1 dan lampiran formulir |
| A4 | Modul hanya muncul sebagai tautan di laporan sesi yang dikirim asisten. Tautan terisi 92% secara keseluruhan (27% kosong di 2024/2025 Genap). Tidak ada nomor versi, dan tanggal kirimnya sesudah sesi | Google Form, kolom "Modul Praktikum" (17 Okt 2026) |
| A5 | POB 2025 tidak mengatur pemakaian lab di luar praktikum (ujian, seminar, riset, peminjaman) maupun penyelesaian bentrok jadwal | POB 2025 (seluruh langkah) |
| A6 | POB 2025 menyebut "Formulir Penyesuaian Jadwal Praktikum" (langkah 14), tetapi formulir itu tidak dilampirkan. Penyesuaian jadwal dilakukan asisten bila sesi tertunda | POB 2025 langkah 14 |
| A7 | Template Modul POB 2025 memuat identitas (kode MK, semester, pertemuan ke-), serta kolom disusun (dosen), direviu (laboran), disetujui (KaLab), dan tanggal pengesahan. **Tidak ada kolom nomor versi** | POB 2025 lampiran Template Modul |
| A8 | Pembaruan modul dilakukan dosen; asisten mengembangkan soal tugas berdasarkan pembaruan itu dan menyesuaikan modul bila perlu | POB 2025 langkah 7 dan 15 |
| A9 | Semua tautan modul mengarah ke berkas Google Drive. Dari 1.064 laporan bertautan ada **1.062 tautan unik**. Tidak ada satu tautan pun yang dipakai lebih dari satu kelas, dan pada 102 dari 104 kombinasi MK–kelas–periode (dengan ≥3 laporan) setiap laporan membawa tautan berbeda. Hanya 6 tautan yang memuat penanda versi. Kolom "Modul Praktikum" adalah **kolom unggah berkas**, jadi modul diunggah ulang oleh asisten di setiap laporan, bukan dirujuk dari satu modul acuan | Google Form, kolom "Modul Praktikum" (diolah 14 Nov 2026); jenis kolom: keterangan Herrens, 14 Nov 2026 |
| A10 | Tab alokasi dibuat **satu per periode**, dengan susunan kolom yang berubah tiap periode (kolom Periode, Semester, dan Nama Lengkap MK hanya ada di 2025/2026 Ganjil; kolom Dosen Tandem baru muncul di 2026/2027 Ganjil). Kolom yang selalu ada: prodi, kode dan nama MK, kelas, hari, jam mulai, jam selesai, dosen koordinator, dosen kelas, pertemuan 1–7, UTS, 9–15, UAS. **Tidak ada kolom ruang dan jumlah mahasiswa.** Jumlah MK praktikum per periode: 19, 19, 15 | Sheet Alokasi (diolah 14 Nov 2026) |
| A11 | Laporan sesi hanya memakai 8 nilai ruang (FIKLAB-201, 301–304, 401–403), sama dengan daftar ruang lab. Dari 999 laporan yang tanggal, jam, dan ruangnya valid, ada **24 pasangan laporan dari MK/kelas berbeda yang tumpang tindih di ruang dan waktu yang sama** (2024/2025 Genap 9, 2025/2026 Ganjil 4, 2025/2026 Genap 11). Menurut keterangan pemegang modul, kelas-kelas itu memang memakai ruang yang sama tetapi **jamnya seharusnya berbeda**, jadi tumpang tindih ini berasal dari **jam yang salah diisi asisten**, bukan bentrok sungguhan. Karena jam rencana tidak tercatat di mana pun (A1), kesalahan seperti ini tidak bisa dideteksi | Google Form (diolah 14 Nov 2026); penyebab: keterangan Herrens, 14 Nov 2026 **[KONFIRMASI laboran]** |
| A12 | Penulisan periode tidak seragam di formulir ("2425 Genap", "2526 Ganjil", "2026/2027 Ganjil"), begitu pula nama MK antarperiode | Google Form (diolah 14 Nov 2026) |
| A13 | POB 2025 langkah 6 menyebut asisten berkoordinasi dengan dosen "berdasarkan **tabel jadwal kelas** mata kuliah praktikum". Jadi jadwal kelas ada, tetapi di luar lab: tidak dilampirkan di POB dan tidak masuk sheet Alokasi | POB 2025 langkah 6 (studi dokumen, [bedah-dokumen-praktikum.md](bedah-dokumen-praktikum.md) A4) |

Yang **belum diketahui** dan menunggu wawancara KaLab: di mana tabel jadwal kelas itu disimpan (SIAKAD, prodi, atau BAAK), kapan ditetapkan, dan bagaimana diumumkan **[KONFIRMASI wawancara P2]**.

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Jadwal penggunaan laboratorium dan modul praktikum tersedia sebelum setiap kegiatan |
| Penerapan / PJ | Umum / KaLab; dosen pengampu |
| Unit | 1 sesi praktikum |
| Pembilang | Jumlah sesi praktikum dengan jadwal sah tanpa konflik serta modul berlaku tersedia sebelum sesi |
| Pembagi | Seluruh sesi praktikum yang direncanakan pada periode monev |
| Memenuhi bila | Jadwal sesuai kapasitas; kegiatan lain tercatat; modul relevan tersedia dan dapat diakses sebelum pelaksanaan |
| Skor | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan → 1 |
| Referensi instrumen | Pedoman Diklatfung PLP 2022 (perencanaan/metode), Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

Bukti dukung: (1) jadwal terpadu praktikum dan kegiatan lain, (2) persetujuan pemakaian, (3) modul versi berlaku, (4) bukti publikasi sebelum sesi, (5) rekaman konflik jadwal.

## 2. Aturan "memenuhi"

Satu sesi rencana dinyatakan **memenuhi** bila keempat cek lolos. Skor = jumlah sesi memenuhi ÷ seluruh sesi rencana pada periode monev.

| Cek | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| C1 Jadwal sah dan dipublikasikan | Sesi termasuk jadwal periode yang sudah ditetapkan, dan jadwal itu dipublikasikan sebelum sesi | Sesi berada di jadwal berstatus *ditetapkan*, ada penetap dan tanggal; tanggal publikasi < waktu mulai sesi | Keabsahan penetap |
| C2 Tanpa konflik | Tidak ada sesi lain atau pemakaian lab yang disetujui di ruang yang sama pada waktu yang tumpang tindih | Cek tumpang tindih ruang × waktu terhadap Sesi lain dan Rencana Pemakaian Lab yang disetujui | — |
| C3 Sesuai kapasitas | Jumlah mahasiswa kelas tidak melebihi kapasitas ruang | Jumlah mahasiswa kelas ≤ kapasitas ruang | — |
| C4 Modul berlaku tersedia sebelum sesi | Ada modul versi berlaku untuk MK sesi itu, terbit sebelum sesi, dan dapat diakses | Ada versi modul berstatus *berlaku* untuk MK dan periode sesi, tanggal terbit < waktu mulai sesi, berkas atau tautan terisi | **Relevansi isi modul** terhadap sesi |

Catatan aturan:
- **"Kegiatan lain tercatat"** bukan cek per sesi. Syarat ini terpenuhi dengan adanya Rencana Pemakaian Lab yang disetujui, dan menjadi masukan C2. Tanpa data itu, C2 tidak bisa dipercaya.
- **C3 adalah cek kapasitas sederhana** (jumlah mahasiswa vs kapasitas ruang). Cek rinci (stasiun kerja, rasio supervisi) milik PKG-08 Pengelolaan 8 (kapasitas sesi) di kelompok Aset. PKG-15 tidak mengulangnya.
- **Perubahan jadwal setelah publikasi** (sesi dipindah atau diganti) dicatat sebagai Perubahan Sesi di PKG-18. Sesi yang dipindah dengan perubahan yang disetujui tetap dianggap sah untuk C1 **[ASUMSI]**.
- **Modul per MK atau per pertemuan?** Template POB 2025 berisi kolom "pertemuan ke-" (A7), sedangkan data *as-is* tidak memberi petunjuk karena setiap laporan membawa berkas sendiri (A9). Usulan sementara: satu modul berversi **per MK per periode**, boleh berisi seluruh pertemuan **[ASUMSI; KONFIRMASI wawancara P4]**.
- **Modul tidak perlu disahkan** (keputusan 14 Nov 2026). C4 cukup memeriksa bahwa versi modul sudah *diterbitkan* dosen sebelum sesi.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Jadwal terpadu per ruang | 1 | Gabungan Sesi dan Rencana Pemakaian Lab yang disetujui. Dihasilkan dari data, tidak diinput |
| Persetujuan pemakaian | 2 | Status dan penyetuju di setiap Rencana Pemakaian Lab |
| Modul versi berlaku | 3 | Versi Modul berstatus *berlaku* per MK per periode |
| Bukti publikasi | 4 | Tanggal publikasi dan penetap di Penetapan Jadwal periode |
| Rekaman konflik jadwal | 5 | Daftar tumpang tindih yang terdeteksi beserta penyelesaiannya (pemakaian ditolak atau sesi dipindah) |
| Persentase PKG-15 dan daftar sesi tidak memenuhi | — | Dihitung dari C1–C4, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Sesi** | [T] Core | 1 sesi praktikum bertanggal | Kelas (dan MK), pertemuan ke-, tanggal, jam mulai–selesai rencana, ruang, status | **Milik Core** (keputusan Herrens, 14 Nov 2026), **dibangkitkan di PKG-15** dari kelas × pola mingguan (hari, jam, ruang) × jumlah pertemuan dalam periode. Pola mingguan cukup menjadi masukan saat membangkitkan, tidak disimpan sebagai tabel **[USULAN PENULIS]** |
| **Penetapan Jadwal** | [T] | 1 jadwal per periode (atau per prodi per periode) | Periode, status (draf → diajukan → ditetapkan), penetap, tanggal tetap, tanggal publikasi, berkas jadwal sah | Pola pengesahannya sama dengan `labfik.approval.mixin` di Core. Satuan per periode atau per prodi **[KONFIRMASI wawancara P2, P5]** |
| **Rencana Pemakaian Lab** | [T] | 1 pengajuan pemakaian di luar praktikum | Jenis kegiatan (ujian, seminar, riset, peminjaman, lainnya), ruang, tanggal dan jam, pengaju, status (diajukan → disetujui/ditolak), penyetuju, alasan penolakan | Bukti 1 dan 2; masukan C2 |
| **Versi Modul** | [T] | 1 versi modul per MK per periode | MK, periode, nomor versi, berkas atau tautan, **berkas rubrik** (dipakai PKG-19), **daftar *software*** berupa teks: nama, versi minimal, bebas/berbayar (dipakai PKG-16), **daftar bahan per pertemuan** berupa teks (dipakai PKG-17), tanggal terbit, status (draf → berlaku → diganti), penyusun (dosen) | Diterbitkan dosen **tanpa pengesahan** (keputusan 14 Nov 2026). Saat versi baru terbit, versi lama otomatis berstatus *diganti*. Kode dan revisi bisa memakai `labfik.controlled.mixin`; `labfik.approval.mixin` tidak dipakai |
| **Jadwal Terpadu** | [R] | — | Sesi + Rencana Pemakaian disetujui, per ruang per minggu | Bukti 1 |
| **Rekaman Konflik Jadwal** | [R] | — | Tumpang tindih ruang × waktu yang terdeteksi, beserta status penyelesaiannya | Bukti 5. Bila sistem menolak bentrok saat input, rekaman berasal dari Rencana Pemakaian yang ditolak karena bentrok **[USULAN PENULIS]** |
| **Daftar Sesi Tidak Memenuhi** | [R] | — | Sesi beserta cek C1–C4 yang gagal | Dasar persentase |

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo. Tidak perlu tabel tambahan.

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-15--persiapan-15-jadwal-dan-modul): ditambah **Penetapan Jadwal** [T] (+), karena bukti 4 "publikasi sebelum sesi" butuh tanggal dan penetap, dan pemetaan belum menyediakan tempatnya.

## 5. Master data

Semua master **di-*import* dari Core**. PKG-15 tidak punya master lokal.

| Master | Dipakai untuk | Sumber (Core) | Bila belum tersedia |
|---|---|---|---|
| Periode | Batas pembagi; masa berlaku jadwal dan modul | `labfik.periode` | Periode monev dianggap sama dengan semester **[ASUMSI]** |
| Mata Kuliah | Identitas sesi dan modul | **Core**, `labfik.mata.kuliah` (keputusan 14 Nov 2026; nama model [USULAN PENULIS]) | Diimpor dari tab alokasi per periode (A10). Kode MK dipakai sebagai kunci karena nama MK tidak seragam (A12) |
| Kelas | Identitas sesi; dosen kelas; jumlah mahasiswa untuk C3 | **Core**, `labfik.kelas` (sama seperti Mata Kuliah) | Diimpor dari tab alokasi. Jumlah mahasiswa **tidak ada di data lab saat ini** (A10), jadi diinput manual per kelas **[KONFIRMASI wawancara: sumber jumlah mahasiswa]** |
| Ruang Lab | Lokasi sesi dan pemakaian; kapasitas untuk C3 | `labfik.ruang` (8 ruang: FIKLAB-201, 301–304, 401–403; cocok dengan nilai ruang di laporan sesi, A11) | Kapasitas tiap ruang belum diketahui **[KONFIRMASI laboran]** |
| Personel | Dosen koordinator, dosen kelas, dosen tandem, penyusun modul, pengaju pemakaian, penetap jadwal | `hr.employee` diperluas | Dosen diimpor dari kolom dosen di tab alokasi (A10) |
| Jabatan | Siapa berwenang menetapkan jadwal, menyetujui pemakaian, dan mengesahkan modul | `hr.job` diperluas (`cari_pemegang_berwenang`) | KaLab untuk semua persetujuan **[ASUMSI]** |

Selain master di atas, cukup **pilihan tetap**: jenis kegiatan pemakaian, status sesi, status penetapan, status pemakaian, dan status versi modul.

## 6. Dependensi dan jalan pengganti

**Masuk (yang dibutuhkan PKG-15):**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Sesi, Periode, Ruang Lab, Personel, Jabatan | Core | Wajib | — (Core dikerjakan bersama) |
| Mata Kuliah, Kelas, jumlah mahasiswa | Core, diisi dari jadwal kuliah prodi/SIAKAD (eksternal) | Wajib | Impor dari berkas (CSV/sheet) yang disusun laboran; jumlah mahasiswa diinput manual |
| Hari, jam, dan ruang tiap kelas | Jadwal kuliah prodi/BAAK/SIAKAD (eksternal) **[KONFIRMASI wawancara P2]**. Kolom hari dan jam sudah ada di tab alokasi tetapi kosong; kolom ruang tidak ada (A1, A10) | Wajib | Diinput laboran saat membangkitkan Sesi |
| Berkas modul | Dosen pengampu | Wajib untuk C4 | Tautan ke berkas di Drive/LeADS disimpan sebagai versi modul |

PKG-15 **tidak bergantung** ke package lain. Ini sesuai posisinya sebagai hulu.

**Keluar (yang dipakai package lain):**

| Dipakai oleh | Data |
|---|---|
| PKG-04 Pengelolaan 4 (penugasan) | Sesi (petugas ditempelkan ke Sesi) |
| PKG-08 Pengelolaan 8 (kapasitas sesi), kelompok Aset | Sesi |
| PKG-16 Persiapan 16 (kesiapan alat) | Sesi; daftar *software* di Versi Modul |
| PKG-17 Persiapan 17 (bahan) | Sesi; daftar bahan di Versi Modul |
| PKG-18 Proses 18 (sesi terlaksana) | Sesi sebagai pembagi; Versi Modul untuk mencocokkan modul yang dipakai |
| PKG-19 Evaluasi 19 (penilaian individual) | Sesi (melalui PKG-18); rubrik di Versi Modul |

## 7. Ditunda

Bagian berikut tidak dibutuhkan untuk membuktikan C1–C4, jadi tidak dirancang (calon isi batasan masalah):
- Integrasi langsung dengan SIAKAD atau sistem jadwal fakultas. Cukup impor berkas.
- Penjadwalan otomatis (sistem menyusun jadwal sendiri untuk menghindari bentrok).
- Modul per pertemuan dengan *review cycle*, *dry-run*, dan *improvement backlog* (gagasan draf paket 2026).
- Pengingat ke dosen bila modul belum terbit menjelang sesi. Status cukup terlihat di daftar sesi tidak memenuhi.
- Kalender libur akademik. Tanggal libur dilewati manual saat membangkitkan Sesi.
- Pengumuman jadwal ke mahasiswa lewat kanal lain (email, portal). Bukti publikasi cukup tanggal publikasi di sistem.

## 8. Kompleksitas

Hitungan kasar sesuai [pedoman](pedoman-pengisian-sheet-analisis.md#6-cara-menghitung-kompleksitas) bagian 6.

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 3 (Penetapan Jadwal, Rencana Pemakaian Lab, Versi Modul) | 0 | 0 | 1 (jadwal kuliah prodi/SIAKAD) | 2 (penetapan jadwal, persetujuan pemakaian) | +1 (Sebagian: alokasi tanpa hari/jam, modul tanpa versi) | **7** |

- Sesi tidak dihitung di T karena milik Core. Membangkitkan Sesi tetap menjadi pekerjaan PKG-15.
- Penerbitan modul tidak dihitung di A karena tidak ada pengesahan (keputusan 14 Nov 2026).

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `sesi rencana` · Sumber `Google Sheets (Alokasi) + Google Form (tautan modul)` · Status `Sebagian` · Dependensi ID `—` · Eksternal `Jadwal kuliah prodi/SIAKAD` · Level `Otomatis` · Kompleksitas `7`.

## 9. Pertanyaan untuk narasumber

Pertanyaan utamanya sudah ada di sheet "Wawancara FIKLAB Compliance" bagian Pelaksanaan Praktikum. Wawancara **belum dijawab KaLab** (per 14 Nov 2026). Tabel ini mencatat jawaban apa yang ditunggu PKG-15 dari setiap nomor.

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P2 (KaLab, laboran) | Penetapan Jadwal, Sesi | Sumber jadwal (SIAKAD/prodi/BAAK), kapan ditetapkan, siapa membagi kelas ke ruang, bagaimana diumumkan |
| P3 (KaLab, laboran) | Rencana Pemakaian Lab, C2 | Jenis pemakaian di luar praktikum, siapa menyetujui, siapa memutuskan bentrok, contoh kejadian bentrok |
| P4 (KaLab) | Versi Modul, C4 | Penyusun modul, ada tidaknya pengesahan atau versi, kapan modul harus siap, perbedaan modul dosen dan asisten |
| P5 (KaLab) | C1, C4 | Siapa menetapkan jadwal dan mengesahkan modul; batas waktu modul tersedia |
| P18a, P19 (KaLab) | Seluruh PKG-15 | Kendala terbesar persiapan; rekap yang paling dibutuhkan |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan, untuk ditambahkan bila memungkinkan):
- [ ] Apakah periode monev sama dengan semester? Kapan periode monev ditutup?
- [ ] Apakah modul disusun satu berkas per mata kuliah, atau satu berkas per pertemuan?
- [ ] Data jumlah mahasiswa per kelas dan kapasitas tiap ruang lab bisa diperoleh dari mana?
- [ ] (Laboran) Jam rencana tiap kelas praktikum sebenarnya dicatat di mana? (A1: kolom hari dan jam di sheet alokasi selalu kosong; A11: jam di laporan sesi bisa salah isi)

Yang perlu disampaikan ke kelompok (Febriyan, Zahir):
- [ ] Sesi, Mata Kuliah, dan Kelas masuk `labfik_core` (keputusan Herrens, 14 Nov 2026), Sesi tanpa `op.session`. Sudah ditulis ke CLAUDE.md bagian 6, brief bersama, dan pemetaan bagian 5; anggota lain perlu diberi tahu karena file itu dipakai bersama.
