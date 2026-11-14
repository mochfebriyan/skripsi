# Analisis Data Indikator Persiapan 17 (Bahan Praktikum)

14 November 2026 · Herrens · PKG-17 Persiapan 17 (bahan praktikum) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab atau laboran; wawancara bagian Pelaksanaan Praktikum belum dijawab.

PIC analisis awal di sheet adalah Zahir (tab *Analysis* baris 35: Daftar Kebutuhan Bahan per Sesi, *Checklist* Penerimaan & Substitusi Bahan, Stok Bahan [R]; master bahan/reagen dan master mata kuliah/sesi). Dokumen ini melanjutkannya. Rujukan "PKG-16 A3" berarti temuan A3 di [analisis-data-persiapan-16.md](analisis-data-persiapan-16.md), dan seterusnya.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2.

---

## Ringkasan

| | Persiapan 17 |
|---|---|
| Inti | Untuk sesi yang memakai bahan fisik, bahan tersedia dalam jumlah, mutu, dan kondisi yang sesuai sebelum sesi |
| Penerapan | **Bersyarat**: hanya praktikum yang menggunakan bahan fisik |
| PJ (instrumen) | PLP/laboran |
| Jenis skor | **Persentase** |
| Unit | 1 sesi praktikum yang **menggunakan bahan** pada periode monev |
| Level cakupan (usulan) | **Otomatis** |
| Posisi dalam dependensi | Menumpang di Pemeriksaan Kesiapan PKG-16; daftar bahan dari Versi Modul PKG-15 |
| Acuan ISO/IEC 17025 | 6.6 (produk dan jasa dari pihak luar: verifikasi sebelum dipakai; dirujuk instrumen) · 6.4 (dirujuk instrumen) |
| Kompleksitas (kasar) | **5** (rincian di bagian 8) |

**Temuan utama:**
1. **PKG-17 tidak sepenuhnya N/A, tetapi berlaku untuk sedikit sesi.** Praktikum FIK hampir seluruhnya berbasis komputer. Jejak bahan fisik hanya ada di sesi *crimping* kabel LAN (Praktikum Jaringan Komputer) dan kemungkinan di Praktikum *Internet of Things* (A2, A3).
2. **Tidak ada rekaman bahan sama sekali.** Formulir laporan sesi tidak punya kolom bahan, dan kendala tidak pernah menyebut bahan (A4).
3. Karena pembaginya kecil, PKG-17 **tidak perlu tabel sendiri**. Bahan cukup menjadi kategori butir di Pemeriksaan Kesiapan PKG-16, dan kebutuhannya ditulis di Versi Modul PKG-15 **[USULAN PENULIS]**.

---

## 0. Sumber dan temuan *as-is*

### Dokumen dan data yang dipakai

| Sumber | Sifat | Tanggal | Yang relevan untuk PKG-17 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`) | **Nyata**, belum disahkan | 2025 | Peralatan/perlengkapan, Monitoring Kesiapan Sarana Prasarana (kolom B Bahan), Template Modul bagian 5 |
| Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" (Responses) | **Data nyata** (tidak dikutip per baris) | Diolah 14 Nov 2026 (1.147 laporan) | Topik dan kendala yang menyebut bahan |
| Sheet "Alokasi Pertemuan Asisten Praktikum" | **Data nyata** (tidak dikutip per baris) | Diolah 14 Nov 2026 | Daftar MK praktikum |
| Paket Dokumen Monev `DOCUMENTS/12_SOP_Aset_Stok_Limbah`, `18_Standar_Modul_Jadwal_Kesiapan_Praktikum` | **Draf GPT** | Okt 2026 | Contoh format saja |

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | POB 2025 menyebut "alat-alat dan bahan yang dikelola Laboratorium FIK" sebagai perlengkapan, dan lembar Monitoring Kesiapan Sarana Prasarana punya kolom **B (Bahan)** per MK dan kelas per ruang. Tidak ada contoh terisi, daftar bahan, atau aturan stok | POB 2025 |
| A2 | Dari 1.147 laporan sesi, hanya **3** yang topiknya menyebut kegiatan berbahan fisik, semuanya "*Crimping* Kabel LAN *Straight* dan *Cross*" di Praktikum Jaringan Komputer (kabel UTP dan konektor RJ45 adalah bahan habis pakai). 45 laporan Jaringan Komputer lainnya berupa simulasi atau kuis | Google Form (diolah 14 Nov 2026) |
| A3 | MK "Praktikum *Internet Of Thing*" tercantum di sheet alokasi, tetapi **tidak punya satu pun laporan sesi**, kemungkinan karena kelasnya tanpa asisten (PKG-18 A1). Apakah praktikum ini memakai komponen fisik (mikrokontroler, sensor, kabel *jumper*) belum diketahui **[KONFIRMASI wawancara P9]** | Sheet Alokasi × Google Form |
| A4 | Formulir laporan sesi tidak punya kolom bahan; kolom kesiapan sarana hanya satu pilihan umum (PKG-16 A3); kendala tidak pernah menyebut bahan | Google Form |
| A5 | Template Modul POB 2025 bagian 5 "Alat dan Bahan" hanya mencontohkan komputer, *software*, koneksi internet, dan modul; tidak ada contoh bahan fisik | POB 2025 lampiran Template Modul |
| A6 | MK praktikum di sheet alokasi seluruhnya bertema komputasi (pemrograman, basis data, jaringan, sistem operasi, *big data*, pengolahan citra, keamanan data, *mobile*, IoT). Tidak ada praktikum kimia, biologi, atau sejenisnya, sehingga bukti 3 instrumen (persiapan larutan/media) tidak relevan | Sheet Alokasi (diolah 14 Nov 2026) |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Bahan praktikum tersedia dalam jumlah, mutu, dan kondisi yang sesuai sebelum setiap sesi |
| Penerapan / PJ | **Bersyarat: praktikum menggunakan bahan fisik** / PLP/laboran |
| Unit | 1 sesi praktikum yang menggunakan bahan |
| Pembilang | Jumlah sesi yang seluruh kebutuhan bahan wajibnya terpenuhi dan diterima sebelum dimulai |
| Pembagi | Seluruh sesi praktikum yang **menggunakan bahan** pada periode monev |
| Memenuhi bila | Jumlah cukup; mutu dan masa pakai sesuai; bahan diberi label; substitusi disetujui dan tidak mengubah tujuan atau keamanan |
| Skor | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan → 1 |
| Referensi instrumen | Pedoman Diklatfung PLP 2022 (bahan), SNI ISO/IEC 17025:2017 6.4 dan 6.6, Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

Bukti dukung: (1) daftar kebutuhan per sesi, (2) stok/lot/kedaluwarsa, (3) persiapan larutan/media, (4) kriteria penerimaan, (5) *checklist* dan catatan substitusi.

## 2. Aturan "memenuhi"

**Sesi yang menggunakan bahan** = Sesi yang Versi Modul-nya mencantumkan bahan untuk pertemuan ke- sesi itu (PKG-15). Sesi lain tidak masuk pembagi. Bila dalam satu periode tidak ada sesi semacam itu, PKG-17 dinyatakan **tidak berlaku (N/A)** untuk periode tersebut.

Satu sesi yang menggunakan bahan dinyatakan **memenuhi** bila ketiga cek lolos. Pemeriksaannya dilakukan bersamaan dengan Pemeriksaan Kesiapan PKG-16, sebagai butir berkategori **bahan**.

| Cek | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| B1 Diperiksa sebelum sesi | Setiap bahan yang dibutuhkan diperiksa sebelum jam mulai | Setiap bahan di daftar Versi Modul untuk pertemuan itu punya butir bahan di Pemeriksaan Kesiapan, waktu periksa < jam mulai Sesi | — |
| B2 Jumlah, mutu, dan label sesuai | Jumlah tersedia ≥ jumlah dibutuhkan; kondisi baik dan masih layak pakai; bahan berlabel | Jumlah tersedia ≥ jumlah dibutuhkan; hasil butir = baik; tanda "berlabel" dicentang | Kewajaran kondisi bahan |
| B3 Substitusi sah | Bila bahan diganti, penggantinya disetujui dan tidak mengubah tujuan atau keamanan | Bila butir ditandai substitusi: bahan pengganti, alasan, dan penyetuju (dosen pengampu) terisi | Kesetaraan bahan pengganti |

Catatan aturan:
- **Kedaluwarsa dan lot** hanya diisi bila relevan untuk bahan tersebut. Kabel UTP, konektor, dan komponen elektronik umumnya tidak berkedaluwarsa.
- **Persiapan larutan/media** (bukti 3) tidak berlaku untuk lab FIK (A6).
- **Stok bahan** tidak dihitung di sini. Laboran mencatat jumlah tersedia saat memeriksa. Kartu stok adalah milik PKG-07 Pengelolaan 7 (inventaris) di kelompok Aset dan cukup dirujuk bila sudah ada.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Daftar kebutuhan bahan per sesi | 1 | Daftar bahan per pertemuan di Versi Modul (PKG-15) |
| Stok/lot/kedaluwarsa | 2 | Jumlah tersedia (dan kedaluwarsa bila relevan) di butir bahan; kartu stok PKG-07 bila ada |
| Persiapan larutan/media | 3 | Tidak berlaku (A6) |
| Kriteria penerimaan | 4 | Hasil butir bahan (jumlah, kondisi, label) |
| *Checklist* dan catatan substitusi | 5 | Butir bahan + catatan substitusi dan penyetujunya |
| Persentase PKG-17 dan daftar sesi tidak memenuhi | — | Dihitung, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Butir bahan** pada Pemeriksaan Kesiapan | [T] anak Pemeriksaan Kesiapan (PKG-16) | 1 per bahan per sesi | Nama bahan, jumlah dibutuhkan (dari modul), jumlah tersedia, kondisi (baik/tidak), berlabel (ya/tidak), kedaluwarsa (bila relevan), substitusi (ya/tidak), bahan pengganti, alasan, penyetuju | Kategori butir tambahan di PKG-16, jadi tidak dihitung sebagai tabel terpisah |
| Daftar bahan pada **Versi Modul** | Atribut [T] milik PKG-15 | — | Baris teks: pertemuan ke-, nama bahan, jumlah per praktikan atau per kelompok | Mengikuti bagian 5 template modul (A5) |
| **Daftar Sesi Tidak Memenuhi** | [R] | — | Sesi berbahan beserta cek B1–B3 yang gagal | Dasar persentase |

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-17--persiapan-17-bahan-praktikum) dan isian sheet: dua transaksi (Kebutuhan Bahan per Sesi; Penerimaan dan Substitusi Bahan) dilebur menjadi daftar bahan di modul dan butir bahan di Pemeriksaan Kesiapan PKG-16. Report Stok Bahan diganti jumlah tersedia saat pemeriksaan.

## 5. Master data

PKG-17 **tidak punya master lokal** dan **tidak memakai master Bahan** (Core, dikelola PKG-07 kelompok Aset). Bahan ditulis sebagai teks di Versi Modul dan butir pemeriksaan, mengikuti prinsip "teks bebas sebelum master baru" dan keputusan serupa untuk *software* di PKG-16.

| Master | Dipakai untuk | Sumber |
|---|---|---|
| Sesi, Ruang Lab | Melalui Pemeriksaan Kesiapan | Core |
| Personel | Laboran pemeriksa, dosen penyetuju substitusi | `hr.employee` diperluas |

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Daftar bahan per pertemuan | PKG-15 Persiapan 15 (Versi Modul) | **Wajib** (menentukan sesi mana yang masuk pembagi) | Laboran menandai sesi berbahan secara manual |
| Pemeriksaan Kesiapan | PKG-16 Persiapan 16 (kesiapan alat) | **Wajib** (tempat butir bahan) | — |
| Kartu stok bahan | PKG-07 Pengelolaan 7 (kelompok Aset) | Opsional | Jumlah tersedia dicatat langsung saat pemeriksaan |

Dibanding pemetaan, dependensi wajib ke PKG-07 (stok bahan) **dilepas** menjadi opsional, sehingga PKG-17 tidak bergantung pada kelompok Aset.

**Keluar:** tidak dipakai package lain.

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan B1–B3, jadi tidak dirancang (calon isi batasan masalah):
- Master Bahan, kartu stok, dan lot di modul Praktikum (wilayah PKG-07 kelompok Aset).
- Persiapan larutan/media (tidak relevan untuk lab FIK).
- Permintaan atau pengadaan bahan.
- Pengurangan stok otomatis setelah sesi.

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 0 (butir bahan adalah anak Pemeriksaan Kesiapan) | 0 | 2 (PKG-15, PKG-16) | 0 | 1 (persetujuan substitusi oleh dosen) | +2 (Belum ada) | **5** |

Pemetaan menghitung T = 2, M = 0, D = 2 (PKG-07, PKG-15). Transaksi dilebur ke PKG-15 dan PKG-16; dependensi ke PKG-07 menjadi opsional, diganti dependensi ke PKG-16.

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `sesi berbahan` · Sumber `Belum ada` · Status `Belum ada` · Dependensi ID `Persiapan 15 (modul)`, `Persiapan 16 (kesiapan)` · Eksternal `—` · Level `Otomatis` · Kompleksitas `5`.

## 9. Pertanyaan untuk narasumber

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P9 (KaLab, laboran) | Penerapan bersyarat, B1–B3 | Praktikum mana yang memakai bahan fisik (komponen IoT/elektronika, kabel dan konektor jaringan, filamen *3D printer*); bagaimana kebutuhan per sesi ditentukan, stok dicek, dan siapa menyiapkan; bila tidak ada, apakah setuju indikator dinyatakan tidak berlaku |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] (Laboran) Apakah Praktikum *Internet of Things* memakai komponen milik lab? Komponen dipinjam (dikembalikan) atau habis pakai?
- [ ] (Laboran) Kabel UTP dan konektor RJ45 untuk praktikum *crimping* disediakan lab atau dibawa mahasiswa?

Pertanyaan untuk kelompok: brief bersama mencatat pertanyaan terbuka "Apakah Persiapan 17 dinyatakan N/A untuk lab FIK, atau dicakup terbatas?". Usulan dokumen ini: **dicakup terbatas**, yaitu berlaku hanya untuk sesi yang modulnya mencantumkan bahan, dan N/A untuk periode tanpa sesi semacam itu. Pertanyaan terbuka itu baru ditutup setelah wawancara P9.
