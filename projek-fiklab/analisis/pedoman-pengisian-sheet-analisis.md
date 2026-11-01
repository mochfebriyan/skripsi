# Pedoman Pengisian Sheet Analisis Instrumen Monev

26 Oktober 2026 · Draf oleh Febriyan, untuk dibahas bersama Zahir dan Herrens (dan kelompok lain yang memakai sheet yang sama)

Sheet: **Instrumen Monev Laboratorium UPNVJ 2026 v1.1 – PIC dan Data** (tab *Analysis*). Salinannya ada di [docs/](../docs/).

## 1. Tujuan

Dosen meminta kita **menganalisis dulu** modul, data, dan dependensi antarinstrumen **sebelum** pembagian role. Tujuannya ada dua:

1. Melihat indikator mana yang **kompleks** dan mana yang **mudah**, supaya beban tiap skripsi seimbang.
2. Melihat indikator mana yang **saling bergantung** atau **memakai data yang sama**, supaya tidak ada yang membangun hal yang sama dua kali.

Kedua hal itu hanya bisa dibandingkan kalau **semua orang mengisi dengan cara dan istilah yang sama**. Pedoman ini mengatur caranya.

Kolom **PIC - Skripsi** di sheet adalah **PIC analisis**, bukan pembagian skripsi. Setelah analisis, pembagian kerja dilakukan **per modul**, dan PIC analisis suatu baris bisa berbeda dari pemegang modulnya. Pemegang modul tercatat di [brief-seluruh-projek.md](../brief/brief-seluruh-projek.md#modul-dan-pemegangnya).

## 2. Alur analisis per indikator

Kerjakan setiap indikator dengan urutan berikut. Jangan loncat ke tabel atau field sebelum langkah 1–3 jelas.

```
Target → Aturan memenuhi → Luaran (bukti dukung) → Transaksi → Master → Dependensi → Kompleksitas
```

| Langkah | Pertanyaan yang dijawab | Sumber |
|---|---|---|
| 1. Target | Apa yang dinilai? Unitnya apa? Skornya persentase atau kriteria berurutan? | Kolom TARGET, Target Satuan, Kriteria |
| 2. Aturan memenuhi | Kapan satu unit dianggap memenuhi? Bagian mana yang bisa dicek sistem, dan mana yang harus dinilai manusia? | Kolom Kriteria |
| 3. Luaran | Bukti apa yang harus bisa ditunjukkan saat monev? | Kolom Bukti Dukung |
| 4. Transaksi | Kejadian apa yang perlu dicatat supaya bukti itu ada? | Analisis kita |
| 5. Master | Data acuan apa yang dipakai transaksi tersebut? | Analisis kita |
| 6. Dependensi | Data apa yang harus datang dari indikator lain atau sistem lain? | Analisis kita |
| 7. Kompleksitas | Seberapa berat dibangun? | Hitungan di bagian 6 |

Contoh lengkap: [analisis Pengelolaan 1–3](analisis-data-pengelolaan-1-3.md) dan [analisis Pengembangan 13](analisis-data-pengembangan-13.md). Analisis awal Proses 18 tersimpan di riwayat git (`git show 62e50ce:projek-fiklab/analisis/analisis-data-proses-18.md`).

## 3. Kolom yang diisi

### 3a. Kolom yang sudah ada

| Kolom | Cara mengisi | Contoh |
|---|---|---|
| **PIC - Skripsi** | Nama orang yang menganalisis | Febriyan |
| **Modul** | Pilih **satu** dari daftar modul baku (bagian 4c). Jangan membuat nama modul baru tanpa disepakati | Practicum Management |
| **Entity Table Apa Saja** | Satu baris per entitas, dengan format `- Nama Entitas [T/M/R]` (lihat bagian 4a). Hanya entitas **milik indikator ini**. Master ditulis di kolom berikutnya | `- Sesi [T]` |
| **Master Data** | Satu baris per master, memakai **nama baku** dari daftar master (bagian 4b) | `- Personel` |

### 3b. Kolom tambahan (usulan, perlu disepakati sebelum ditambahkan ke sheet)

| Kolom | Isi | Pilihan / format |
|---|---|---|
| **Jenis Skor** | Cara instrumen menilai | `Persentase` / `Kriteria berurutan` |
| **Unit Hitung** | Apa yang dihitung | Contoh: sesi, praktikan, SOP, personel–alat, paket dokumen |
| **Sumber Data Saat Ini** | Di mana data/bukti ini ada sekarang | `Google Form`, `Google Sheets`, `LeADS`, `SIMPEL`, `SIAKAD`, `Dokumen kertas`, `Belum ada`, `Belum diketahui` |
| **Status Data** | Ketersediaan data saat ini | `Ada` / `Sebagian` / `Belum ada` / `Belum diketahui` |
| **Dependensi ID** | Indikator lain yang datanya **wajib** dipakai. Tulis aspek + nomor + kata kunci (nomor tidak unik) | `Persiapan 15 (jadwal)`, `Pengelolaan 3 (struktur)` |
| **Sistem / Dokumen Eksternal** | Sistem atau dokumen di luar Odoo yang dibutuhkan | `SIMPEL`, `LeADS`, `SK Dekan`, `Renstra UPNVJ` |
| **Level Cakupan** | Seberapa jauh sistem bisa membuktikan | `Otomatis` / `Semi-otomatis` / `Bukti tertaut` (definisi di bagian 5) |
| **Skor Kompleksitas** | Hasil hitungan bagian 6 | Angka |
| **Catatan / Pertanyaan** | Hal yang belum jelas, perlu ditanyakan ke KaLab/dosen | Teks bebas |

Kalau kolom tambahan belum disetujui, tulis isinya di kolom **Catatan Perbaikan** dengan format `Jenis Skor: ... | Unit: ... | Dependensi: ...` supaya tetap bisa dibaca.

## 4. Konvensi penamaan

### 4a. Label jenis entitas

| Label | Arti | Ciri | Contoh |
|---|---|---|---|
| **[T] Transaksi** | Kejadian yang dicatat berulang dan punya tanggal | Bertambah terus; punya status atau tanggal | Sesi, Jurnal Sesi, Perubahan Sesi, Versi SOP |
| **[M] Master** | Data acuan yang jarang berubah | Dipilih dari daftar oleh transaksi | Ruang Lab, Personel, Mata Kuliah |
| **[R] Report** | Hasil olahan dari T dan M, **tidak diinput** | Bisa dihitung ulang kapan saja | Daftar Sesi dan Petugas, Matriks Kewenangan, Bagan Organisasi |

Aturan:
- **Report tidak dihitung sebagai tabel yang harus dibangun.** Kalau sebuah bukti bisa dihasilkan dari data yang ada, tulis `[R]`, bukan `[T]`.
- **Tabel anak cukup ditulis di dalam induknya**, misalnya `- Jurnal Sesi [T] (anak: presensi, log book)`.
- **Pilihan tetap bukan master.** Status, jenis, kategori, dan peran cukup ditulis sebagai pilihan (*selection*), bukan master. Contoh: kategori SOP dan status sesi.
- **Pengaturan bukan master.** Ambang durasi, siklus tinjau ulang, dan sejenisnya adalah pengaturan KaLab.

### 4b. Daftar master baku (draf)

Pakai nama di kolom **Nama baku**. Kalau master yang kamu butuhkan belum ada di daftar, **tambahkan ke tab Master Data** (bagian 7) lebih dulu, baru dipakai. Jangan membuat sinonim (misalnya "Petugas", "Staf", dan "Personel" untuk hal yang sama).

| Nama baku | Isi | Bukan / jangan disebut |
|---|---|---|
| Periode | Semester/tahun akademik, tahun anggaran, periode monev | Semester (cukup sebagai jenis periode) |
| Mata Kuliah | MK praktikum, termasuk jumlah SKS praktikum | — |
| Kelas | Kelas per MK per periode, jumlah mahasiswa | Kode kelas |
| Ruang Lab | 8 ruang FIKLAB, kapasitas | Lab, Lokasi (kecuali lokasi non-ruang) |
| Personel | Semua orang yang punya peran di lab: KaLab, PLP/laboran, dosen, asisten, petugas K3 | Petugas, Staf, Dosen (dosen adalah jenis personel) |
| Jabatan | Jabatan/peran beserta uraian tugas, kewenangan, atasan, pengganti | Role |
| Mahasiswa | Praktikan | Praktikan (praktikan adalah mahasiswa dalam konteks sesi) |
| Alat | Peralatan dan perangkat lab | Aset, Inventaris (inventaris adalah transaksi pemeriksaan) |
| Bahan | Bahan habis pakai | BHP |
| Dokumen Induk | Daftar induk SOP/IK/formulir | SOP (SOP adalah kategori dokumen) |
| KPI | Definisi indikator kinerja lab | — |
| Sasaran Renstra | Sasaran Renstra UPNVJ/UPPS/prodi | — |
| Kompetensi | Jenis kompetensi/sertifikasi yang disyaratkan | Skill |
| Indikator Monev | Registri indikator proyek (21, PKG-01–21): aspek, nomor, bunyi, jenis skor | — |

Daftar ini **draf** dan akan bertambah. Yang penting, setiap master hanya punya satu nama.

### 4c. Daftar modul baku (dari sheet saat ini)

`Organization Management` · `Practicum Management` · `Asset Management` · `Safety Management`

Kalau sebuah indikator tidak cocok dengan keempatnya, tulis usulan di Catatan dan bahas bersama. Jangan langsung membuat modul baru.

**Pembaruan (28 Okt – 1 Nov 2026):** untuk kelompok Febriyan, Zahir, dan Herrens, modul sudah diklasifikasi ulang menjadi **Tata Kelola & Dokumen**, **SDM & Kompetensi**, dan **Pelaksanaan Praktikum**, ditambah **Core** untuk master bersama. Asset Management dan Safety Management tetap. Rinciannya ada di [pemetaan-package-instrumen.md](pemetaan-package-instrumen.md#2-hierarki-modul).

### 4d. Menyebut indikator

Penomoran di sheet tidak rapi. Nomor dipakai ganda (tiga baris "Pengelolaan 10", dua baris "Evaluasi 19"), sebagian baris tanpa aspek, dan sebagian berkode Q/E. Sejak 1 November 2026 proyek memakai **21 indikator**, satu per package, dan **nomor PKG menjadi identitas resmi** (lihat [pemetaan](pemetaan-package-instrumen.md#3-ringkasan-package)). Selalu tulis **PKG + aspek + nomor + kata kunci**:

- ✅ `PKG-10 Pengelolaan 10 (otorisasi)`, `PKG-19 Evaluasi 19 (penilaian individual)`
- ❌ `ID 10`, `target 19`

## 5. Level cakupan

| Level | Arti | Contoh |
|---|---|---|
| **Otomatis** | Skor dihitung sistem dari data operasional yang dicatat di Odoo | Proses 18, Pengelolaan 2 |
| **Semi-otomatis** | Sistem mengelola alur dan bukti per kriteria, lalu menunjukkan kriteria mana yang sudah berbukti. Skor akhir ditetapkan penilai | Pengelolaan 1, 3, Pengembangan 13, 14 |
| **Bukti tertaut** | Data utama ada di sistem lain. Odoo hanya menyimpan tautan/lampiran bukti | Evaluasi 19 (LeADS, SIMPEL) |

Patokan cepat:
- **Kriteria berurutan** biasanya semi-otomatis, karena ada pengesahan dan penilaian kualitas oleh manusia.
- **Persentase** biasanya otomatis, kecuali datanya ada di sistem lain.

## 6. Cara menghitung kompleksitas

Hitungan ini **kasar**. Gunanya hanya untuk membandingkan antarindikator, bukan memperkirakan waktu.

| Komponen | Cara hitung |
|---|---|
| **T** | Jumlah tabel transaksi **baru** (tabel anak tidak dihitung terpisah; report tidak dihitung) |
| **M** | Jumlah master **baru**, yaitu yang belum ada di Odoo/OpenEduCat/modul Rafika dan belum dibuat indikator lain |
| **D** | Jumlah dependensi **wajib** ke indikator lain (yang opsional tidak dihitung) |
| **E** | Jumlah sistem atau dokumen eksternal yang dibutuhkan |
| **A** | Jumlah alur persetujuan/pengesahan |
| **Status data** | Ada = +0, Sebagian = +1, Belum ada / Belum diketahui = +2 |

**Skor Kompleksitas = T + M + D + E + A + status data**

Contoh:

| Indikator | T | M | D | E | A | Data | Total |
|---|---|---|---|---|---|---|---|
| Proses 18 | 3 | 1 | 1 | 1 | 1 | +1 | **8** |
| Pengelolaan 1 | 4 | 2 | 1 | 2 | 2 | +2 | **13** |
| Evaluasi 19 | 0 | 0 | 1 | 2 | 0 | +0 | **3** |

Selain angka, catat juga **posisi dalam dependensi**:
- **Hulu:** dipakai banyak indikator lain, misalnya Pengelolaan 3 (personel, jabatan). Indikator hulu harus dikerjakan atau disepakati duluan.
- **Hilir:** memakai data banyak indikator lain, misalnya *dashboard*.

Indikator hulu berbobot keputusan besar walaupun angkanya kecil.

## 7. Tab Master Data (usulan tab baru)

Supaya dependensi terlihat, buat tab **Master Data** dengan satu baris per master:

| Kolom | Isi | Contoh |
|---|---|---|
| Nama baku | Dari daftar bagian 4b | Personel |
| Isi utama | Atribut penting, cukup garis besar | Nama, jenis (dosen/laboran/asisten/K3), NIP/NIM, jabatan |
| Sumber saat ini | Di mana data ini ada | `mst_dosen`, `op.student.assistant`, `res.users`; laboran belum ada |
| Model Odoo kandidat | Model yang sudah ada atau perlu dibuat | `hr.employee` / model baru |
| Dipakai oleh | Semua indikator yang memakai master ini | Pengelolaan 1, 2, 3, 4, 10; Pengembangan 14; Proses 18 |
| Diusulkan dikelola oleh | Indikator/modul yang paling hulu | Pengelolaan 3 |
| Keputusan / pertanyaan | Hal yang perlu disepakati | Asisten masuk `hr.employee` atau tidak? |

Master yang **dipakai oleh banyak indikator** adalah kandidat **komponen bersama** dan harus dirancang paling awal.

## 8. Contoh baris terisi

**Proses 18 (sesi terlaksana)**

| Kolom | Isi |
|---|---|
| Modul | Practicum Management |
| Entity Table | `- Sesi [T]` · `- Jurnal Sesi [T] (anak: presensi, log book; tautan SIMPEL)` · `- Perubahan Sesi [T]` · `- Daftar Sesi Tidak Memenuhi [R]` |
| Master Data | `- Periode` · `- Mata Kuliah` · `- Kelas` · `- Ruang Lab` · `- Personel` · `- Mahasiswa` |
| Jenis Skor / Unit | Persentase / sesi rencana |
| Sumber / Status data | Google Form + Sheets (hanya sesi berasisten) / Sebagian |
| Dependensi ID | Persiapan 15 (jadwal) |
| Eksternal | SIMPEL |
| Level cakupan | Otomatis |
| Kompleksitas | 8 |

**Pengelolaan 2 (SOP)**

| Kolom | Isi |
|---|---|
| Modul | Organization Management |
| Entity Table | `- Versi SOP [T]` · `- Distribusi [T]` · `- Sosialisasi [T] (anak: peserta)` · `- Daftar SOP Tidak Memenuhi [R]` |
| Master Data | `- Dokumen Induk` · `- Ruang Lab` · `- Personel` · `- Jabatan` |
| Jenis Skor / Unit | Persentase / SOP wajib |
| Sumber / Status data | Belum diketahui |
| Dependensi ID | Pengelolaan 3 (struktur) |
| Eksternal | — |
| Level cakupan | Otomatis |
| Kompleksitas | 8 |

## 9. Yang **tidak** perlu diisi sekarang

- Rincian field/atribut, tipe data, dan nama model teknis. Itu dibahas saat perancangan, setelah role dibagi.
- Desain tampilan dan alur layar.
- Estimasi waktu pengerjaan.
- Data pribadi apa pun (nama asisten, NIM, nomor HP, nilai). Kalau perlu contoh, pakai data dummy.

## 10. Checklist sebelum menandai satu baris selesai

- [ ] Jenis skor dan unit hitung sudah jelas
- [ ] Entity ditulis dengan label `[T]`, `[M]`, atau `[R]`, dan report tidak dihitung sebagai tabel
- [ ] Master memakai nama baku. Master baru sudah ditambahkan ke tab Master Data
- [ ] Dependensi ditulis dengan aspek + nomor + kata kunci
- [ ] Sumber dan status data saat ini terisi, atau ditulis `Belum diketahui` disertai pertanyaan di Catatan
- [ ] Level cakupan dan skor kompleksitas terisi
- [ ] Untuk analisis yang panjang, ada file analisis di folder `projek-fiklab/analisis/` dengan format yang sama seperti contoh
