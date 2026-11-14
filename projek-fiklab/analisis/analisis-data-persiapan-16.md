# Analisis Data Indikator Persiapan 16 (Kesiapan Alat dan *Software*)

14 November 2026 · Herrens · PKG-16 Persiapan 16 (kesiapan alat dan *software*) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab atau laboran; wawancara bagian Pelaksanaan Praktikum belum dijawab.

PIC analisis awal di sheet adalah Zahir (tab *Analysis* baris 34: Checklist Kesiapan Sesi, Uji Fungsi Alat/*Software*, Keputusan Siap/Tunda Sesi, Status Kalibrasi Alat [R]; master alat, *software* dan lisensi, ruang lab). Dokumen ini melanjutkannya. Rujukan "PKG-15 A1" berarti temuan A1 di [analisis-data-persiapan-15.md](analisis-data-persiapan-15.md), dan seterusnya.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2.

---

## Ringkasan

| | Persiapan 16 |
|---|---|
| Inti | Sebelum setiap sesi, alat, *software*, dan utilitas yang dibutuhkan diperiksa dan dinyatakan siap; ketidaksiapan diselesaikan atau sesi ditunda |
| PJ (instrumen) | PLP/laboran; dosen |
| Jenis skor | **Persentase** |
| Unit | 1 sesi praktikum yang **dilaksanakan** pada periode monev (pembagi berbeda dari PKG-15 dan PKG-18 yang memakai sesi rencana) |
| Level cakupan (usulan) | **Otomatis** |
| Posisi dalam dependensi | Butuh Sesi dan Versi Modul dari PKG-15; tidak dipakai package lain |
| Acuan ISO/IEC 17025 | 6.4.4 (peralatan diverifikasi sebelum dipakai; dirujuk langsung oleh instrumen) · 6.4.13 (rekaman peralatan) · 6.3 (fasilitas dan utilitas) |
| Kompleksitas (kasar) | **3** (rincian di bagian 8) |

**Temuan utama:**
1. **Kesiapan per sesi dicatat asisten, bukan laboran**, sebagai satu pilihan di formulir laporan sesi yang dikirim sesudah sesi (A2). Tidak ada rekaman pemeriksaan oleh laboran sebelum sesi, padahal PJ instrumen adalah laboran.
2. **Status kesiapan tidak bisa dipercaya dan tidak ada keputusan tunda.** 104 laporan bertanda "Siap" justru mencatat kendala sarana, dan 11 sesi bertanda "Belum Siap" tetap berjalan (A3).
3. **Tidak ada daftar *software*, versi, maupun lisensi** di dokumen atau data mana pun. Kebutuhan *software* hanya disebut di bagian "Alat dan Bahan" template modul (A6).

---

## 0. Sumber dan temuan *as-is*

### Dokumen dan data yang dipakai

| Sumber | Sifat | Tanggal | Yang relevan untuk PKG-16 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`) | **Nyata**, belum disahkan | 2025 | Peringatan, langkah 8 dan 16, Formulir Monitoring Kesiapan Sarana Prasarana, Template Modul bagian 5 |
| Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" (Responses) | **Data nyata** (tidak dikutip per baris) | Diolah 14 Nov 2026 (1.147 laporan) | Kolom "Kesiapan Sarana Praktikum" dan "Keterangan Kendala Praktikum" |
| Kode `skripsi_rafika/PendaftaranAsisten/models/readiness_checklist.py` | Kode acuan (tidak di-*extend*) | 2026 | Model `lab.readiness.checklist` |
| Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (FRM-PRK-04 Checklist Kesiapan dan Penutupan Lab, STD-PRK-04 Standar Pengelolaan PC, Jaringan, dan Sarana, FRM-PRK-08 Insiden) | **Draf**, kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep–Okt 2026 | Contoh format saja |
| Paket Dokumen Monev `DOCUMENTS/13`, `15`, `16`, `18` | **Draf GPT** | Okt 2026 | Contoh format saja |

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | POB 2025 menugaskan **laboran** memeriksa dan menyesuaikan sarana dan prasarana sesuai kebutuhan kelas praktikum (langkah 8, durasi 1 minggu, hasil "Laporan Kesiapan Sarana Prasarana Praktikum"), serta menyesuaikan bila ada permintaan atau kendala (langkah 16). Bagian Peringatan meminta peralatan dipastikan baik dan kesiapan dokumen, perangkat, dan ruang dicek **sebelum setiap sesi** | POB 2025 |
| A2 | Lampiran "Monitoring Kesiapan Sarana Prasarana Praktikum" bersifat **berkala** ("Monitoring Ke-"), per kode MK dan kelas × 8 ruang, dengan kolom A (alat), B (bahan), C (konektivitas); keterangannya menyebut D (*software*) tetapi kolomnya tidak ada; diparaf laboran. Tidak ada contoh terisi | POB 2025 lampiran |
| A3 | Dalam praktik, kesiapan per sesi diisi **asisten** di formulir laporan sesi: Siap 1.039, Dapat Disesuaikan 87, Belum Siap 11, kosong 10. Dari yang "Siap", **104 mencatat kendala sarana**; dari 11 "Belum Siap", semuanya tetap dilaporkan terlaksana. Tidak ada rekaman keputusan siap/tunda | Google Form (diolah 14 Nov 2026) |
| A4 | Kendala sarana tercatat di 163 dari 1.147 laporan (14%). Penggolongan kata kunci (satu kendala bisa masuk lebih dari satu golongan): PC/komputer mati atau rusak 31, jaringan/internet 27, *software*/instalasi 22, proyektor/layar/audio 16, jumlah PC kurang 8, listrik 1, AC 1 | Google Form (diolah 14 Nov 2026) |
| A5 | Porsi "Dapat Disesuaikan" tertinggi di FIKLAB-303 (30 dari 134 laporan, 22%); ruang lain 2–9% | Google Form (diolah 14 Nov 2026) |
| A6 | Tidak ada daftar *software*, versi, atau lisensi di dokumen nyata maupun data. Kebutuhan *software* hanya disebut per modul di Template Modul bagian 5 "Alat dan Bahan" (OS, RAM, *software* dan versinya, koneksi internet) | POB 2025 lampiran Template Modul |
| A7 | Kode Rafika punya `lab.readiness.checklist` per **fasilitas** (bukan per sesi): tanggal periksa, laboran pemeriksa, status fisik, status *software*, catatan. Acuan saja | `skripsi_rafika` |
| A8 | Utilitas gas dan air tidak relevan untuk 8 ruang lab komputer FIK; utilitas yang relevan adalah listrik dan jaringan. Alat yang perlu kalibrasi kemungkinan tidak ada **[ASUMSI; KONFIRMASI wawancara P6]** | Daftar ruang (Core) |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Peralatan, perangkat lunak, dan utilitas yang diperlukan dinyatakan siap sebelum setiap sesi praktikum |
| Penerapan / PJ | Umum / PLP/laboran; dosen |
| Unit | 1 sesi praktikum |
| Pembilang | Jumlah sesi dengan seluruh alat/*software*/utilitas wajib siap dan diterima sebelum dimulai |
| Pembagi | Seluruh sesi praktikum yang **dilaksanakan** pada periode monev |
| Memenuhi bila | Fungsi dan kelengkapan sesuai modul; keamanan terverifikasi; status kalibrasi berlaku bila perlu; *software* sah dan bekerja; ketidaksiapan diselesaikan sebelum sesi |
| Skor | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan → 1 |
| Referensi instrumen | Pedoman Diklatfung PLP 2022 (pengoperasian), SNI ISO/IEC 17025:2017 6.4.4, Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

Bukti dukung: (1) *checklist* sebelum sesi, (2) uji fungsi, (3) status kalibrasi bila relevan, (4) versi/lisensi *software* sesuai penggunaan, (5) pemeriksaan listrik/gas/air, (6) keputusan siap/tunda.

## 2. Aturan "memenuhi"

Satu sesi yang dilaksanakan (Sesi dengan Jurnal Sesi terkirim, PKG-18) dinyatakan **memenuhi** bila keempat cek lolos.

| Cek | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| S1 Diperiksa sebelum sesi | Ada pemeriksaan kesiapan untuk sesi itu, dilakukan sebelum jam mulai | Pemeriksaan Kesiapan tertaut ke Sesi, waktu periksa < jam mulai Sesi | — |
| S2 Semua butir wajib siap | PC/stasiun kerja, *software* sesuai modul, jaringan, listrik, dan proyektor berfungsi | Semua butir berhasil "baik" atau "diperbaiki sebelum sesi"; jumlah stasiun kerja berfungsi ≥ jumlah praktikan kelas | — |
| S3 *Software* sah | *Software* yang diminta modul terpasang, versinya sesuai, dan lisensinya berlaku | Setiap *software* di daftar Versi Modul (PKG-15) punya butir pemeriksaan berhasil baik; untuk *software* berbayar, tanda "lisensi sah" dicentang laboran | Keabsahan lisensi |
| S4 Keputusan tercatat | Ada keputusan siap atau tunda sebelum sesi | Keputusan = *siap* (atau *siap setelah perbaikan*). Bila *tunda*, Sesi itu tidak dilaksanakan dan diproses lewat Perubahan Sesi PKG-18, sehingga tidak masuk pembagi | — |

Catatan aturan:
- **Status kalibrasi** dan **gas/air** dianggap tidak berlaku untuk lab komputer FIK (A8). Bila ternyata ada alat yang perlu kalibrasi, status kalibrasinya cukup di-*import* dari PKG-05 Pengelolaan 5 (kalibrasi alat) milik kelompok Aset **[KONFIRMASI wawancara P6]**.
- **Keamanan terverifikasi** dicakup butir listrik (kabel, stop kontak) di pemeriksaan. Keselamatan yang lebih luas adalah wilayah modul Safety.
- **Satu pemeriksaan per sesi** mengikuti bunyi instrumen ("sebelum setiap sesi"). Bila KaLab menetapkan pemeriksaan cukup per ruang per hari, satu pemeriksaan boleh berlaku untuk semua sesi di ruang itu pada hari yang sama sampai ada pemeriksaan berikutnya **[KONFIRMASI wawancara P8]**.
- **Kendala yang muncul saat sesi** berlangsung dicatat di Jurnal Sesi PKG-18, bukan di sini.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| *Checklist* sebelum sesi | 1, 2 | Pemeriksaan Kesiapan beserta butir dan hasil uji fungsinya |
| Status kalibrasi | 3 | Tidak berlaku (A8), atau di-*import* dari PKG-05 |
| Versi/lisensi *software* | 4 | Daftar *software* di Versi Modul + butir *software* (dengan tanda lisensi sah) di pemeriksaan |
| Pemeriksaan listrik | 5 | Butir listrik di pemeriksaan |
| Keputusan siap/tunda | 6 | Keputusan di Pemeriksaan Kesiapan |
| Persentase PKG-16, daftar sesi tidak memenuhi, rekap kesiapan per ruang | — | Dihitung, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Pemeriksaan Kesiapan** | [T] | 1 per Sesi | Sesi, ruang, pemeriksa (laboran), waktu periksa, jumlah stasiun kerja berfungsi, keputusan (siap / siap setelah perbaikan / tunda), catatan. Anak: **butir pemeriksaan** (kategori: PC/stasiun kerja, *software*, jaringan, listrik, proyektor/audio, dan **bahan** untuk sesi berbahan (milik PKG-17, lihat [analisis-data-persiapan-17.md](analisis-data-persiapan-17.md)); nama dan versi *software* bila kategori *software*; tanda lisensi sah untuk *software* berbayar; hasil: baik / diperbaiki sebelum sesi / bermasalah; keterangan) | Menggabungkan tiga transaksi di sheet (*checklist*, uji fungsi, keputusan siap/tunda) menjadi satu, seperti usulan pemetaan. Butir *software* dibuat otomatis dari daftar *software* Versi Modul |
| **Daftar Sesi Tidak Memenuhi** | [R] | — | Sesi beserta cek S1–S4 yang gagal | Dasar persentase |
| **Rekap Kesiapan per Ruang** (+) | [R] | — | Jumlah pemeriksaan, butir bermasalah per kategori, dan keputusan tunda per ruang per periode | Menjawab kebutuhan rekap di wawancara P19 dan temuan A5 |

Tambahan kecil pada **Versi Modul** (PKG-15): daftar *software* yang dibutuhkan, berupa baris teks (nama, versi minimal, jenis lisensi bebas/berbayar), mengikuti bagian 5 template modul (A6).

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo.

## 5. Master data

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Sesi, Ruang Lab | Sesi yang diperiksa, ruang | Core | — |
| Kelas | Jumlah mahasiswa untuk cek stasiun kerja (S2) | Core | Cek stasiun kerja dilewati |
| Personel | Laboran pemeriksa | `hr.employee` diperluas | — |
| Alat | **Tidak dipakai** di cakupan ini. Pemeriksaan dilakukan per kategori di tingkat ruang, bukan per unit alat | Core (dikelola PKG-07 kelompok Aset) | — |

PKG-16 **tidak punya master lokal**. Master *Software* yang diusulkan di sheet tidak dibuat (keputusan Herrens, 14 Nov 2026): tidak ada kriteria instrumen yang gagal tanpanya, karena kebutuhan *software* sudah ditulis per modul dan keabsahan lisensi dinyatakan laboran saat pemeriksaan (prinsip "teks bebas sebelum master baru").

Pilihan tetap: kategori butir, hasil butir, keputusan, jenis lisensi.

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Sesi (jam mulai, ruang) | PKG-15 Persiapan 15 (jadwal), lewat Core | **Wajib** | — |
| Daftar *software* per modul | PKG-15 (Versi Modul) | Wajib untuk S3 | Butir *software* diisi manual oleh laboran |
| Sesi dilaksanakan (pembagi) | PKG-18 Proses 18 (Jurnal Sesi) | Wajib untuk pembagi | Pembagi = sesi rencana yang tidak ditunda |
| Status kalibrasi alat | PKG-05 Pengelolaan 5 (kelompok Aset) | Opsional | Dianggap tidak berlaku (A8) |

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-16--persiapan-16-kesiapan-alat-dan-software): master Alat tidak lagi dibutuhkan, sehingga PKG-16 tidak bergantung pada kelompok Aset kecuali untuk kalibrasi yang opsional.

**Keluar:** PKG-17 Persiapan 17 (bahan) menumpang di Pemeriksaan Kesiapan sebagai butir berkategori bahan. Keputusan *tunda* memicu Perubahan Sesi di PKG-18.

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan S1–S4, jadi tidak dirancang (calon isi batasan masalah):
- Pemeriksaan per unit PC (ID stasiun kerja), riwayat kerusakan per alat, dan register insiden (gagasan draf paket 2026; wilayah PKG-07/PKG-12 kelompok Aset).
- Daftar *software* terpasang per ruang dan per PC.
- Permintaan instalasi *software* dari dosen sebagai alur tersendiri.
- Pemeriksaan penutupan lab sesudah sesi.
- Master *Software* dan cek kedaluwarsa lisensi otomatis. Baru perlu dibuat bila laboran menyebut ada banyak *software* berbayar yang masa lisensinya harus dipantau.
- Pengingat kedaluwarsa lisensi.

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 1 (Pemeriksaan Kesiapan) | 0 | 1 (PKG-15) | 0 | 0 | +1 (Sebagian: diisi asisten sesudah sesi, A3) | **3** |

Pemetaan menghitung T = 3 (*checklist*, uji fungsi, keputusan) dan M = 1 (*Software* dan Lisensi). Ketiga transaksi digabung menjadi satu, dan master *Software* tidak dibuat.

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `sesi dilaksanakan` · Sumber `Google Form (diisi asisten)` · Status `Sebagian` · Dependensi ID `Persiapan 15 (jadwal)` · Eksternal `—` · Level `Otomatis` · Kompleksitas `3`.

## 9. Pertanyaan untuk narasumber

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P6 (KaLab, laboran) | S1–S3, A8 | Siapa mengecek PC, *software*, jaringan, listrik, proyektor, kapan, dan apakah dicatat; bagaimana permintaan *software* dari dosen dan lisensi dikelola |
| P7 (KaLab, laboran) | S4 | Siapa memutuskan sesi jalan, ditunda, atau pindah ruang bila ada PC mati atau *software* belum terpasang |
| P8 (KaLab) | Satuan pemeriksaan | Per sesi, per hari, atau per awal semester; siapa mengisi; siapa berhak menunda |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] (Laboran) Apakah ada daftar *software* dan lisensi yang terpasang di tiap ruang? *Software* berbayar apa saja yang dipakai?
- [ ] (Laboran) Berapa jumlah PC/stasiun kerja di tiap ruang?
- [ ] (Laboran) Apakah ada alat di lab FIK yang perlu kalibrasi?
- [ ] (KaLab) Apakah kolom "Kesiapan Sarana Praktikum" yang sekarang diisi asisten akan diganti pemeriksaan oleh laboran?
