# Use Case Sistem Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Ini Step 6 rancangan TO-BE, yang menggantikan use case versi sebelumnya (UC-01–23). Diagram: [use-case-tata-kelola.drawio](use-case-tata-kelola.drawio) (3 halaman).

Use case di sini **diturunkan** dari proses bisnis di [proses-bisnis-tata-kelola.md](proses-bisnis-tata-kelola.md): activity A1–A4 dan state machine S1–S2. Aturan penurunannya mengikuti Wazlawick (2024) Bab 4:

| Aturan | Isi | Penerapan |
|---|---|---|
| §4.5 | Tugas yang dikerjakan berurutan **tanpa jeda panjang** = satu use case. Tugas yang bisa ditunda = use case terpisah | *Terbitkan dokumen resmi* dan *Hasilkan PDF* digabung. *Unggah dokumen bertanda tangan* dan *Sahkan dokumen* dipisah (beda aktor, beda hari) |
| §4.6 | Setiap **event** yang mengubah status di state machine adalah use case | Event S1: ajukan, tarik kembali, periksa, kembalikan, sahkan, cabut, `when(periode berakhir)` |
| §4.3.1–4.3.3 | Satu sesi, interaktif, hasilnya konsisten | Tugas «service» masuk ke use case yang memicunya. Fragmen tidak digambar |
| §4.3.2 | Aktor sistem seperti jam boleh memicu use case | Aktor «system» **Penjadwal** untuk transisi berbasis waktu |
| §4.3.4 | *Essential*, tanpa teknologi antarmuka | Tidak ada "Cetak", "Ekspor PDF", atau "Login". "Cetak dokumen" dan "Tanda tangani" adalah tugas «manual» di luar sistem |
| §4.3 | Pola **CRUDL** untuk konsep sederhana | Stereotype «CRUDL» |
| §4.8.2 | Matriks **Konsep × CRUDL** untuk mencari use case yang hilang | [Bagian 4](#4-matriks-konsep--crudl-48-2) |
| §4.2 | Aktor = peran, bukan profil keamanan | Aktor peran **Penyusun Dokumen** dan **Pengesah Dokumen**, dengan generalisasi dari KaLab, Laboran, dan Dekan |

## 1. Aktor

| Aktor | Jenis | Keterangan |
|---|---|---|
| *Penyusun Dokumen* | Peran (abstrak) | Yang menyusun dan mengajukan dokumen. Diperankan **KaLab** (rencana, SK) dan **Laboran** (SOP/IK) |
| *Pengesah Dokumen* | Peran (abstrak) | Jabatan yang berwenang mengesahkan atau mencabut jenis dokumen tertentu. Diperankan **KaLab** (mis. POB lab) dan **Dekan** (SK, rencana) |
| Pemeriksa | Manusia | Wakil Dekan / unit mutu / GKM. Opsional per jenis dokumen |
| KaLab | Manusia | Kepala Laboratorium |
| Laboran/PLP | Manusia | Termasuk teknisi |
| Dekan | Manusia | Hanya sebagai Pengesah. Login atau tidak masih **[KONFIRMASI]** |
| Pengguna Lab | Manusia | Dosen, asisten, mahasiswa |
| Penilai Monev | Manusia | Auditor internal, LPMPP, tim monev. Hanya membaca |
| Admin | Manusia | Pengelola data master |
| **Penjadwal** | «system» | Pemicu berbasis waktu. Di Odoo diwujudkan sebagai tugas terjadwal (`ir.cron`) |

## 2. Daftar use case

Kolom **Sumber** menunjukkan asal penurunan: tugas «user» di activity (A1–A4), event di state machine (S1–S2), atau matriks CRUDL (bagian 4).

### Pengesahan dokumen (bersama, halaman 1/3)

| ID | Use case | Aktor | Sumber | Isi (tugas yang tergabung) | KF |
|---|---|---|---|---|---|
| UC-21 | Ajukan Dokumen | *Penyusun* | A1, S1 *ajukan* | Ajukan → sistem cek kelengkapan → catat pengajuan → kirim notifikasi | 24, 31 |
| UC-22 | Tarik Pengajuan Dokumen | *Penyusun* | S1 *tarik kembali* | Diajukan → Draf, dengan alasan | **39** |
| UC-23 | Periksa Dokumen | Pemeriksa | A1, S1 *periksa* | Diajukan → Diperiksa | 31, 32 |
| UC-24 | Kembalikan Dokumen | Pemeriksa, *Pengesah* | A1 *Kembalikan / Catat pengembalian*, S1 *kembalikan* | Diajukan/Diperiksa → Draf, dengan alasan | **40** |
| UC-25 | Terbitkan Dokumen Resmi | *Penyusun* | A1 *Terbitkan* + *Hasilkan PDF* | Dokumen rutin (rencana, SK) menjadi dokumen resmi untuk ditandatangani | 04, 25 |
| UC-26 | Unggah Dokumen Bertanda Tangan | *Penyusun* | A1 | Berkas bertanda tangan manual dilampirkan | 33 |
| UC-27 | Sahkan Dokumen | *Pengesah* | A1, S1 *sahkan* | Validasi wewenang dan berkas → Disahkan → catat jejak → (untuk versi SOP/IK) versi lama Diganti, jadwal tinjau dibuat | 11, 14, 31, 33, 34 |
| UC-28 | Cabut Dokumen | *Pengesah* | A2, S1 *cabut* | Disahkan → Dicabut, dengan alasan | **41** |
| UC-31 | Kedaluwarsakan Dokumen Berperiode | Penjadwal | A3, S1 `when(periode berakhir)` | Rencana/SK yang periodenya habis → Kedaluwarsa | **42** |
| UC-32 | Kirim Pengingat Jadwal | Penjadwal | A2 *pengingat tinjau ulang*, A3 *pengingat realisasi*, S2 `when` | Pengingat tinjau ulang dan pengisian realisasi | 15, **43** |

### Struktur organisasi dan pengendalian dokumen (halaman 2/3)

| ID | Use case | Aktor | Sumber | Isi | KF |
|---|---|---|---|---|---|
| UC-01 | Kelola Personel «CRUDL» | Admin, KaLab | Matriks CRUDL | — | 01 |
| UC-02 | Kelola Jabatan «CRUDL» | KaLab | A4 *Lengkapi uraian jabatan* | Tugas, wewenang, atasan, pengganti | 02 |
| UC-03 | Susun SK Penetapan Pengelola | KaLab | A4 | Termasuk menyusun SK baru dari SK sebelumnya (revisi) | 03 |
| UC-04 | Catat Rapat Koordinasi | KaLab | A4 | — | 07 |
| UC-05 | Catat Evaluasi Struktur | KaLab | A4 | — | 08 |
| UC-06 | Lihat Laporan Struktur Organisasi «report» | KaLab, Penilai | Matriks CRUDL (R/L) | Bagan organisasi, matriks kewenangan, riwayat SK, rapat, evaluasi | 05, 06 |
| UC-07 | Kelola Dokumen Induk «CRUDL» | KaLab, Laboran | A2 *Daftarkan dokumen induk* | — | 09 |
| UC-08 | Unggah Versi Dokumen | Laboran | A2 | Draf versi baru SOP/IK | 10 |
| UC-09 | Catat Distribusi Dokumen | Laboran | A2 | — | 12 |
| UC-10 | Catat Sosialisasi Dokumen | Laboran | A2 | — | 13 |
| UC-11 | Tinjau Ulang Dokumen | Laboran, KaLab | A2, S2 *tinjau* | Hasil: tetap berlaku / perlu revisi / tidak diperlukan lagi | 38 |
| UC-12 | Baca Dokumen Berlaku | Pengguna Lab | Matriks CRUDL (R) | Hanya versi berlaku | 16 |
| UC-13 | Lihat Laporan Pengendalian Dokumen «report» | KaLab, Laboran, Penilai | Matriks CRUDL (R/L) | Daftar induk, riwayat revisi, distribusi, sosialisasi, tinjau ulang | 17 |

### Perencanaan, status monev, dan pengaturan (halaman 3/3)

| ID | Use case | Aktor | Sumber | Isi | KF |
|---|---|---|---|---|---|
| UC-14 | Kelola KPI «CRUDL» | KaLab | Matriks CRUDL | — | 18 |
| UC-15 | Kelola Sasaran Renstra «CRUDL» | KaLab, Admin | Matriks CRUDL | — | 19 |
| UC-16 | Susun Rencana | KaLab | A3 *Susun analisis gap*, *Susun item rencana*, *Buat revisi rencana* | Semua jenis rencana. Analisis gap untuk jenis pengembangan. Termasuk revisi dari rencana yang disahkan | 20–23, 26 |
| UC-18 | Isi Realisasi Rencana | Laboran, KaLab | A3 | — | 27 |
| UC-19 | Catat Tinjauan Rencana | KaLab | A3 *Catat tinjauan*, *Ukur manfaat*, *Tetapkan keputusan* | Satu sesi | 29 |
| UC-20 | Lihat Laporan Rencana «report» | KaLab, Penilai | Matriks CRUDL (R/L) | Laporan capaian, matriks keterkaitan Renstra | 28, 30 |
| UC-29 | Lihat Status Monev «report» | KaLab, Penilai | Matriks CRUDL (R/L) | Persentase PKG-02, kriteria tertinggi K1–K4 beserta buktinya | 35–37 |
| UC-30 | Atur Pengaturan Modul | KaLab | Analisis PKG-02 ("pengaturan KaLab") | Tahap pemeriksaan per jenis dokumen, siklus tinjau ulang | 32 |

Nomor UC-17 sengaja kosong: *Revisi Rencana* digabung ke UC-16 (lihat bagian 3). Nomor tidak digeser supaya rujukan tetap stabil.

## 3. Keputusan granularitas

| Keputusan | Alasan (Wazlawick) |
|---|---|
| *Ajukan* dipisah dari *Susun Rencana*, *Susun SK*, dan *Unggah Versi* | Penyusunan bisa disimpan sebagai draf dan diajukan hari lain (§4.5, contoh *Register* vs *Send proposal*). Karena itu tidak ada «include» |
| *Periksa* dan *Kembalikan* dipisah | Masing-masing event berbeda di S1 (§4.6). *Kembalikan* juga dilakukan Pengesah, bukan hanya Pemeriksa |
| *Unggah Dokumen Bertanda Tangan* dan *Sahkan* dipisah | Beda aktor (Penyusun vs Pengesah) dan beda hari. Ini membatalkan usulan sebelumnya yang menganggap unggah sebagai fragmen |
| *Ganti versi lama* dan *Jadwalkan tinjau ulang* masuk ke *Sahkan* | Tugas «service» yang langsung terjadi setelah pengesahan, tanpa jeda (§4.5, contoh *Allocate funds* + *Publish*) |
| *Catat Distribusi* dan *Catat Sosialisasi* dipisah | Dua tugas, bisa terjadi di waktu berbeda. Nama dengan "dan" dihindari (§3.2.4) |
| *Revisi Rencana* digabung ke *Susun Rencana* | Hasilnya sama-sama rencana berstatus draf. Bedanya hanya sumber isian awal. Sama seperti *Susun SK* yang mencakup SK pengganti |
| *Ukur manfaat* dan *Tetapkan keputusan* masuk *Catat Tinjauan Rencana* | Dilakukan dalam satu sesi tinjauan |
| Laporan dikelompokkan per area «report» | Mengurangi jumlah use case tanpa kehilangan informasi (§4.3, aturan kedua) |
| Login, Cetak, Tanda tangani tidak digambar | Login bukan use case (§4.3.3). Cetak adalah teknologi (§4.3.4). Tanda tangan adalah tugas «manual» di luar sistem |

## 4. Matriks Konsep × CRUDL (§4.8.2)

X = operasi yang **tidak diizinkan** aturan bisnis. Rekaman bukti tidak boleh dihapus. Koreksinya lewat ubah, dan semua perubahan tercatat (KF-34).

| Konsep | Create | Retrieve | Update | Delete | List |
|---|---|---|---|---|---|
| Personel | UC-01 | UC-01 | UC-01 | X (diarsipkan) | UC-01 |
| Jabatan | UC-02 | UC-02, UC-06 | UC-02 | X (diarsipkan) | UC-02, UC-06 |
| SK Penetapan | UC-03 | UC-06 | UC-03 (draf) | UC-03 (draf saja) | UC-06 |
| Rapat Koordinasi | UC-04 | UC-06 | UC-04 | X | UC-06 |
| Evaluasi Struktur | UC-05 | UC-06 | UC-05 | X | UC-06 |
| Dokumen Induk | UC-07 | UC-07, UC-13 | UC-07 | X (diarsipkan) | UC-07, UC-13 |
| Versi Dokumen | UC-08 | UC-12, UC-13 | UC-08 (draf) | UC-08 (draf saja) | UC-13 |
| Distribusi | UC-09 | UC-13 | UC-09 | X | UC-13 |
| Sosialisasi | UC-10 | UC-13 | UC-10 | X | UC-13 |
| Tinjau Ulang | UC-11 | UC-13 | X | X | UC-13 |
| KPI | UC-14 | UC-14, UC-20 | UC-14 | X (diarsipkan) | UC-14 |
| Sasaran Renstra | UC-15 | UC-15, UC-20 | UC-15 | UC-15 | UC-15 |
| Rencana (+ item, gap) | UC-16 | UC-20 | UC-16 (draf) | UC-16 (draf saja) | UC-20 |
| Realisasi | UC-18 | UC-20 | UC-18 | X | UC-20 |
| Tinjauan Rencana | UC-19 | UC-20 | UC-19 | X | UC-20 |
| Status dokumen (S1) | UC-21–28, 31 | UC-29 | — | — | UC-29 |
| Pengaturan | X | UC-30 | UC-30 | X | X |

**Hasil pengecekan:** setiap konsep yang dibuat juga dibaca oleh minimal satu use case, sehingga **tidak ada informasi yang dibuat tetapi tidak pernah dipakai**. Tiga use case «report» (UC-06, 13, 20) serta UC-12 dan UC-29 ditambahkan karena matriks ini. Sebelumnya laporan hanya berupa satu use case umum "Cetak Laporan".

**[KONFIRMASI]** Aturan "rekaman bukti tidak boleh dihapus" adalah usulan penulis demi keterlacakan monev.

## 5. Perbandingan dengan use case versi sebelumnya

| Versi lama | Versi baru | Perubahan |
|---|---|---|
| UC-01 Kelola Personel | UC-01 «CRUDL» | Diberi stereotype |
| UC-02 Kelola Jabatan | UC-02 «CRUDL» | Diberi stereotype |
| UC-03 Susun SK | UC-03 | Tetap |
| UC-04 Lihat Bagan & Matriks | UC-06 «report» | Digabung dengan laporan struktur lain |
| UC-05, 06 | UC-04, 05 | Nomor bergeser |
| UC-07 Kelola Dokumen Induk | UC-07 «CRUDL» | Diberi stereotype |
| UC-08 Unggah Versi | UC-08 | Tetap |
| UC-09 Catat Distribusi & Sosialisasi | UC-09, UC-10 | Dipecah |
| UC-10 Baca SOP/IK Berlaku | UC-12 | Nama lebih umum |
| UC-11 Kelola KPI & Sasaran Renstra | UC-14, UC-15 | Dipecah per konsep |
| UC-12 Susun Rencana | UC-16 | Mencakup revisi |
| UC-13 Isi Realisasi | UC-18 | Tetap |
| UC-14 Catat Tinjauan | UC-19 | Tetap |
| UC-15 Ajukan | UC-21 | Aktor menjadi *Penyusun* |
| UC-16 Periksa | UC-23 | Relasi «extend» dihapus |
| UC-17 Sahkan | UC-27 | Relasi «include» dihapus. Aktor menjadi *Pengesah* |
| UC-18 Ekspor PDF | UC-25 Terbitkan Dokumen Resmi | Nama *essential* |
| UC-19 Cetak Laporan | UC-06, 13, 20 «report» | Dipecah per area. "Cetak" dihapus |
| UC-20 Lihat Status Monev | UC-29 «report» | Tetap |
| UC-21 Tinjau Ulang | UC-11 | Tetap |
| UC-22 Unggah PDF Bertanda Tangan | UC-26 | Berdiri sendiri, tanpa «include» |
| UC-23 Atur Pengaturan | UC-30 | Tetap |
| — | UC-22 Tarik Pengajuan, UC-24 Kembalikan, UC-28 Cabut | **Baru**, dari S1 |
| — | UC-31 Kedaluwarsakan, UC-32 Kirim Pengingat | **Baru**, aktor Penjadwal |

## 6. Langkah berikutnya

Step 7 adalah **expanded use case** (Wazlawick Bab 6): alur utama dan alternatif untuk use case yang **bukan** «CRUDL» atau «report». Use case «CRUDL» cukup memakai satu pola bersama (§6.7). Prioritasnya use case di halaman 1/3, karena dipakai semua dokumen.
