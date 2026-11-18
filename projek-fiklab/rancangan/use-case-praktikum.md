# Use Case TO-BE Modul Pelaksanaan Praktikum

16 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF. Diagram ini masuk proposal (Bab II 2.3).** Langkah 6 rancangan TO-BE.

Diagram: [use-case-praktikum.drawio](use-case-praktikum.drawio), 3 halaman. Skrip pembuatnya: [tools/drawio/praktikum/use_case.py](../tools/drawio/praktikum/use_case.py) (pola dari `contoh-tata-kelola/use_case.py`; data dan prefiks `prk-uc` diganti). `validate.py` dengan prefiks `prk-`: **OK** di ketiga halaman. Pemeriksaan tampilan [cek_tampilan.py](../tools/drawio/praktikum/cek_tampilan.py) (garis yang menembus kotak lain): **0 temuan** (16 Nov 2026). Tampilan sudah dicek lewat ekspor PNG draw.io desktop (16 Nov 2026); label yang tertimpa dan garis yang menyilang sudah dirapikan. **Gaya diubah ke polos hitam-putih** (17 Nov 2026, CLAUDE.md bagian 5): tanpa warna, huruf Times New Roman, judul dan catatan dipindah ke halaman `Catatan … (bahan kerja)` di akhir file. Diperiksa ulang 18 Nov 2026: `validate.py` dengan prefiks `prk-` **OK** di semua halaman; `cek_tampilan.py` **0** garis menembus kotak lain. Tampilan di draw.io belum dilihat ulang setelah perubahan gaya.

Input: [proses-bisnis-praktikum.md](proses-bisnis-praktikum.md) (activity A1–A5, state machine S1–S3, kandidat use case bagian 4.2), [kebutuhan-praktikum.md](kebutuhan-praktikum.md) (KF-PRK-01 s.d. 51), kontrak Core bersama ([kontrak-core.md](kontrak-core.md)).

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Use case dari tugas «user» di activity. Tugas yang langsung menyusul (termasuk «service» otomatis) masuk use case yang sama; tugas yang bisa ditunda (beda hari atau beda aktor) dipisah | §4.5 | Bagian 4.1 |
| Use case dari event yang mengubah status di state machine | §4.6 | Bagian 4.2 |
| Satu sesi: dimulai dan selesai tanpa jeda panjang; boleh disimpan sebagai draf lalu dilanjutkan | §4.3.1 | *Kirim Jurnal Sesi* mencakup isi jurnal, presensi petugas, dan *log book*, karena dikerjakan sekaligus setelah sesi |
| Interaktif: harus ada aktor. Proses internal bukan use case | §4.3.2 | Bangkitkan sesi, cek bentrok, status Sesi, persentase, dan kriteria K1–K4 dihitung sistem, bukan use case |
| Hasil konsisten; bukan fragmen | §4.3.3 | Tidak ada "Login", "Buka jadwal", "Pilih kelas" |
| *Essential*: tanpa teknologi antarmuka | §4.3.4 | "Terbitkan Laporan Bukti" (hasilnya dokumen resmi untuk penilai), bukan "Cetak/Ekspor PDF"; "Lihat Laporan …" «report» |
| Hindari «include»/«extend» kecuali bagian bersama yang utuh | §4.3 | Tidak dipakai. Keputusan *tunda* di Periksa Kesiapan diteruskan dengan Ajukan Perubahan Sesi sebagai use case terpisah |
| Konsep yang hanya dikelola menjadi «CRUDL» | §4.3 | Mata Kuliah, Kelas, Pengaturan Praktikum |
| Aktor = peran, bukan profil keamanan; sistem luar menjadi aktor hanya bila berinteraksi langsung | §4.2 | Aktor abstrak *Petugas Praktikum*; LeADS, SIAKAD, SIMPEL, tim jadwal fakultas bukan aktor (impor berkas dan tautan) |
| Batas sistem: hanya use case yang diotomasi | §4.3.6 | Tugas «manual» (susun jadwal fakultas, laksanakan praktikum, tanda tangan) di luar batas |
| Matriks konsep × CRUDL untuk menemukan use case yang hilang | §4.8.2 | Bagian 6 |

---

## 2. Aktor

| Aktor | Jenis | Turunan dari | Keterangan |
|---|---|---|---|
| ***Petugas Praktikum*** | Abstrak | — | Peran yang bertugas di satu sesi: mengisi jurnal, mengajukan perubahan, membaca modul. Menggantikan "Pengisi Jurnal" dan "Pengaju" di activity A3–A4. Tidak ada orang yang "hanya" Petugas Praktikum |
| **Asisten** | Manusia | Petugas Praktikum | `hr.employee` dengan jabatan Asisten Praktikum; grup `labfik_asisten` |
| **Dosen** | Manusia | Petugas Praktikum | Juga menerbitkan modul, menyetujui substitusi bahan, mencatat penilaian kelas; grup `labfik_dosen`. Pengisi jurnal kelas tanpa asisten **[ASUMSI]** |
| **Laboran** | Manusia | Petugas Praktikum | Laboran/PLP, teknisi. Juga mengimpor jadwal, menyusun penetapan jadwal, memeriksa kesiapan; grup `labfik_laboran` (Core) |
| **KaLab** | Manusia | — | Mengesahkan jadwal (lewat use case Tata Kelola), memutuskan pemakaian lab dan perubahan sesi, mengelola survei, menerbitkan laporan bukti; grup `labfik_kalab` (Core) |
| ~~Pengguna Lab~~ | Bukan aktor | — | Tidak punya akun Odoo (keterangan Herrens, 16 Nov 2026); laboran mencatat permintaannya (§4.2: hanya yang berinteraksi langsung yang menjadi aktor) |
| **Responden** | Manusia | — | Praktikan, dosen, asisten; mengisi survei lewat tautan tanpa login |

Bukan aktor: tim jadwal fakultas (berkasnya diimpor laboran), Dekan dan pejabat penanda tangan, penilai monev (menerima PDF), pihak eksternal (kontrak Core I-9), LeADS/SIAKAD/SIMPEL. **Tidak ada aktor «system» Penjadwal**, karena status yang bergantung waktu dihitung (`is_terlewat`, dibuka/ditutup survei), tidak dijadwalkan.

Grup akses mengikuti kontrak Core bagian G: `labfik_pengguna`, `labfik_laboran`, `labfik_kalab` di Core; `labfik_dosen`, `labfik_asisten` di `labfik_praktikum`.

---

## 3. Daftar use case

Kolom **Lapis**: W = Inti, O = Pelengkap. Lapis hanya dicatat di tabel ini; diagram tidak membedakannya.

| UC | Nama | Stereotype | Aktor | Sumber | KF | Lapis |
|---|---|---|---|---|---|---|
| **Paket Jadwal (PKG-15)** (halaman 1/3) | | | | | | |
| UC-PRK-01 | Kelola Mata Kuliah | «CRUDL» | Laboran | KF (master Core, §3.4) | 01 | W |
| UC-PRK-02 | Kelola Kelas | «CRUDL» | Laboran | KF (master Core, §3.4) | 01 | W |
| UC-PRK-03 | Impor Jadwal Kelas | — | Laboran | A1 *Impor jadwal kelas* (+ «service» bangkitkan sesi, periksa bentrok, periksa kapasitas); S1 *bangkitkan*, *hapus* | 02, 03, 04, 05 | W |
| UC-PRK-04 | Susun Penetapan Jadwal | — | Laboran | A1 *Susun penetapan jadwal* | 06 | W |
| UC-PRK-10 | Lihat Laporan Jadwal | «report» | Laboran, KaLab, Petugas Praktikum | KF | 10, 11 | W |
| (Tata Kelola) UC-01, 02, 03, 05 | Ajukan / Terbitkan Dokumen Resmi / Unggah Dokumen Bertanda Tangan / Sahkan Dokumen | — | Laboran, KaLab | A1 «call behavior» *Sahkan dokumen* | 06, 07 | W |
| (Tata Kelola) UC-04, 06 | Kembalikan Dokumen / Cabut Dokumen | — | KaLab | S1 Tata Kelola *kembalikan*, *cabut* (berlaku untuk semua dokumen `approval.mixin`) | 06, 45 | W |
| **Paket Modul (PKG-15, dipakai 16, 17, 19)** (halaman 1/3) | | | | | | |
| UC-PRK-05 | Terbitkan Versi Modul | — | Dosen | A1 *Terbitkan versi modul* (+ «service» ganti versi lama) | 12, 13 | W |
| UC-PRK-06 | Baca Modul Berlaku | — | Petugas Praktikum | KF | 14 | W |
| **Paket Pemakaian Lab (PKG-15)** (halaman 1/3) | | | | | | |
| UC-PRK-07 | Ajukan Pemakaian Lab | — | Laboran (atas permintaan pengguna lab) | A2 *Catat pengajuan pemakaian*, *Ubah waktu pemakaian*; S2 *ajukan* | 04, 08, 49 | W |
| UC-PRK-08 | Putuskan Pemakaian Lab | — | KaLab | A2 *Tinjau*, *Setujui/Tolak pemakaian*; S2 *setujui*, *tolak* | 09, 49 | W |
| UC-PRK-09 | Tarik Pengajuan | — | Petugas Praktikum (laboran untuk pengajuan pemakaian) | S2 *tarik kembali* | 47 | O |
| **Paket Kesiapan (PKG-16, 17)** (halaman 2/3) | | | | | | |
| UC-PRK-11 | Periksa Kesiapan Sesi | — | Laboran | A3 *Mulai pemeriksaan*, *Isi hasil butir*, *Tetapkan keputusan* (+ «service» buat butir) | 15, 16, 17, 18, 19, 52 | W |
| UC-PRK-12 | Setujui Substitusi Bahan | — | Dosen | A3 *Setujui substitusi bahan* | 20 | W |
| **Paket Pelaksanaan Sesi (PKG-18)** (halaman 2/3) | | | | | | |
| UC-PRK-13 | Kirim Jurnal Sesi | — | Petugas Praktikum | A3 *Isi jurnal*, *Catat presensi*, *Catat log book*, *Kirim*, *Perbaiki* (+ «service» validasi, ubah status); S1 *kirim jurnal* | 22, 23, 24, 25, 26, 30, 51 | W |
| UC-PRK-14 | Ajukan Perubahan Sesi | — | Petugas Praktikum | A4 *Ajukan perubahan sesi*; A3 «call» A4; S2 *ajukan* | 27, 49 | W |
| UC-PRK-15 | Putuskan Perubahan Sesi | — | KaLab | A4 *Tinjau*, *Setujui/Tolak*, *Tentukan waktu pengganti lain* (+ «service» periksa bentrok, bangkitkan pengganti, ubah status asal); S1 *perubahan disetujui*, *bangkitkan pengganti*; S2 *setujui*, *tolak* | 04, 26, 28, 49 | W |
| UC-PRK-16 | Lihat Laporan Pelaksanaan | «report» | KaLab | KF | 21, 29 | O |
| **Paket Penilaian Individual (PKG-19)** (halaman 3/3) | | | | | | |
| UC-PRK-17 | Catat Penilaian Kelas | — | Dosen, Laboran | KF (satu aktor, tidak digambar di activity, §3.4) | 31 | W |
| UC-PRK-18 | Impor Nilai Kelas | — | Dosen, Laboran | KF | 50 | O |
| **Paket Kepuasan Pengguna (PKG-20)** (halaman 3/3) | | | | | | |
| UC-PRK-19 | Susun Survei Kepuasan | — | KaLab | A5 *Susun survei periode*; S3 *buat* | 33 | W |
| UC-PRK-20 | Tetapkan Survei Kepuasan | — | KaLab | A5 *Tetapkan survei* (+ «service» periksa kelengkapan), *Lengkapi survei*; S3 *tetapkan* | 34 | W |
| UC-PRK-21 | Batalkan Penetapan Survei | — | KaLab | S3 *batalkan penetapan* | 48 | O |
| UC-PRK-22 | Isi Survei Kepuasan | — | Responden | A5 *Isi survei* | 35 | W |
| UC-PRK-23 | Catat Evaluasi Survei | — | KaLab | A5 *Catat evaluasi*, *Tetapkan RTL* (+ «service» hitung rekap, perbarui K1–K3); S3 *catat evaluasi* | 36 | W |
| UC-PRK-24 | Nilai Efektivitas Tindak Lanjut | — | KaLab | A5 *Nilai efektivitas* (+ «service» perbarui K4); S3 *nilai efektivitas* | 37 | W |
| UC-PRK-25 | Lihat Laporan Survei | «report» | KaLab | KF | 38 | W |
| **Paket Status Monev** (halaman 3/3) | | | | | | |
| UC-PRK-26 | Lihat Status Monev Praktikum | «report» | KaLab | KF | 32, 39, 40, 41 | W |
| UC-PRK-27 | Terbitkan Laporan Bukti | — | KaLab | KF | 42 | W |
| UC-PRK-28 | Kelola Pengaturan Praktikum | «CRUDL» | KaLab | KF | 43 | W |

**Jumlah:** 28 use case (24 W, 4 O: UC-PRK-09, 16, 18, 21), ditambah 6 use case pengesahan milik Tata Kelola yang dipakai ulang (UC-01–06; UC-04 dan 06 ditambahkan saat audit 16 Nov 2026 karena pencabutan jadwal dipakai KF-PRK-45).

---

## 4. Penurunan use case

### 4.1 Dari activity (§4.5)

| Activity | Tugas «user» (aktor) | Use case | Alasan penggabungan / pemisahan |
|---|---|---|---|
| A1 | Impor jadwal kelas (Laboran) | UC-PRK-03 | «service» bangkitkan sesi, periksa bentrok, periksa kapasitas langsung menyusul |
| A1 | Susun penetapan jadwal (Laboran) | UC-PRK-04 | Bisa hari lain setelah bentrok diselesaikan fakultas |
| A1 | «call behavior» Sahkan dokumen (KaLab) | UC-01–06 Tata Kelola | Dipakai ulang, beda aktor dan hari |
| A1 | Terbitkan versi modul (Dosen) | UC-PRK-05 | Jalur paralel, aktor lain |
| A2 | Catat pengajuan pemakaian, Ubah waktu pemakaian (Laboran) | UC-PRK-07 | Ubah waktu terjadi di sesi yang sama saat bentrok ditemukan; *Minta pemakaian lab* dan *Sampaikan keputusan* adalah «manual» |
| A2 | Tinjau, Setujui/Tolak pemakaian (KaLab) | UC-PRK-08 | Satu sesi keputusan |
| A3 | Mulai pemeriksaan, Isi hasil butir, Tetapkan keputusan (Laboran) | UC-PRK-11 | Berurutan tanpa jeda, satu aktor |
| A3 | Setujui substitusi bahan (Dosen) | UC-PRK-12 | Aktor lain, bisa beda waktu |
| A3 | Isi jurnal, Catat presensi, Catat entri *log book*, Kirim, Perbaiki (Petugas Praktikum) | UC-PRK-13 | Satu sesi kerja setelah praktikum; boleh disimpan draf |
| A3 / A4 | Ajukan perubahan sesi (Petugas Praktikum) | UC-PRK-14 | Dari keputusan tunda (A3) atau langsung (A4); bukan «include» |
| A4 | Tinjau, Setujui/Tolak, Tentukan waktu pengganti lain (KaLab) | UC-PRK-15 | Satu sesi keputusan |
| A5 | Susun survei periode (KaLab) | UC-PRK-19 | Bisa disimpan dan dilanjutkan |
| A5 | Tetapkan survei, Lengkapi survei (KaLab) | UC-PRK-20 | Penetapan bisa hari lain; melengkapi terjadi saat penetapan ditolak sistem |
| A5 | Isi survei (Responden) | UC-PRK-22 | Aktor lain |
| A5 | Catat evaluasi survei, Tetapkan RTL (KaLab) | UC-PRK-23 | Berurutan, satu sesi |
| A5 | Nilai efektivitas tindak lanjut (KaLab) | UC-PRK-24 | Periode berikutnya |

Tugas «manual» (susun jadwal kelas dan kirim berkas oleh fakultas, sampaikan bentrok ke fakultas, laksanakan praktikum) berada di luar batas sistem (§4.3.6).

### 4.2 Dari state machine (§4.6)

| State machine | Event | Use case |
|---|---|---|
| S1 Sesi | bangkitkan | UC-PRK-03 |
| S1 Sesi | hapus [jadwal tidak diajukan/disahkan ∧ belum ada jurnal] | UC-PRK-03 (impor ulang menggantikan sesi kelas itu) |
| S1 Sesi | kirim jurnal [valid ∧ is_terpublikasi] | UC-PRK-13 |
| S1 Sesi | perubahan disetujui [pengganti / batal / daring]; bangkitkan pengganti | UC-PRK-15 |
| S2 Pengajuan | ajukan | UC-PRK-07, 14 |
| S2 Pengajuan | setujui, tolak | UC-PRK-08, 15 |
| S2 Pengajuan | tarik kembali | UC-PRK-09 |
| S3 Survei | buat | UC-PRK-19 |
| S3 Survei | tetapkan | UC-PRK-20 |
| S3 Survei | batalkan penetapan | UC-PRK-21 |
| S3 Survei | catat evaluasi + RTL | UC-PRK-23 |
| S3 Survei | nilai efektivitas semua RTL | UC-PRK-24 |

Setiap event di S1–S3 punya use case. Atribut hitung Sesi (`is_terpublikasi`, `is_ditunda`, `is_diganti`, `is_terlewat`) bukan event, jadi tidak menjadi use case (§4.3.2).

---

## 5. Keputusan granularitas

| Keputusan | Alasan |
|---|---|
| Mata Kuliah dan Kelas dua «CRUDL» terpisah | Menghindari nama dengan "dan" (CLAUDE.md bagian 8); keduanya konsep berbeda |
| Bangkitkan sesi tidak menjadi use case sendiri | Langsung menyusul impor (§4.5); manual pola mingguan adalah varian UC-PRK-03 di Langkah 7 |
| Pengesahan jadwal memakai use case Tata Kelola | Pola pengesahan sama (`approval.mixin`); membuat ulang berarti duplikasi |
| Susun dan Tetapkan Survei dipisah | Penetapan bisa terjadi hari lain dan mengubah status (S3), sejajar dengan Susun vs Ajukan di Tata Kelola |
| Catat Evaluasi Survei mencakup RTL | RTL adalah bagian evaluasi yang dikerjakan sekaligus |
| Periksa Kesiapan satu use case | Mulai, isi butir, keputusan dikerjakan satu orang tanpa jeda sebelum sesi |
| Kirim Jurnal Sesi satu use case | Isi jurnal, presensi, *log book*, dan kirim dikerjakan sekaligus; draf boleh disimpan |
| Satu Tarik Pengajuan untuk pemakaian lab dan perubahan sesi | Satu pola state (S2) untuk dua objek |
| Laporan digabung per area (jadwal, pelaksanaan, survei, status monev) | Cukup untuk bukti dukung; menghindari daftar «report» yang panjang |
| Terbitkan Laporan Bukti bukan «report» | Menghasilkan dokumen resmi untuk penilai (sejajar dengan Terbitkan Dokumen Resmi di Tata Kelola) |

---

## 6. Matriks konsep × CRUDL (§4.8.2)

C = create, R = retrieve, U = update, D = delete, L = list. **X** = tidak diizinkan aturan bisnis.

| Konsep | C | R | U | D | L | Dibaca oleh |
|---|---|---|---|---|---|---|
| Mata Kuliah | UC-01, 03 | UC-01 | UC-01 | UC-01 (1) | UC-01 | UC-02, 03, 05, 10 |
| Kelas | UC-02, 03 | UC-02 | UC-02 | UC-02 (1) | UC-02 | UC-03, 10, 17, 18, 26 |
| Sesi | UC-03, 15 | UC-10 | UC-13, 15 (state, moda) | UC-03 (2) | UC-10 | UC-11, 13, 14, 16, 26 |
| Penetapan Jadwal | UC-04 | UC-04 | UC-04 (draf) | UC-04 (draf) | UC-04 | Pengesahan Tata Kelola, UC-10, 26 |
| Versi Modul (+ *software*, bahan) | UC-05 | UC-06 | UC-05 (draf) | UC-05 (draf) | UC-06 | UC-11 (butir), 13 (modul dipakai), 17 (rubrik), 26 |
| Pemakaian Lab | UC-07 | UC-08 | UC-08, 09 (status) | X (3) | UC-10 | UC-10, 26 |
| Pemeriksaan Kesiapan (+ butir) | UC-11 | UC-16 | UC-11, 12 (substitusi) | X (3) | UC-16 | UC-26, 27 |
| Jurnal Sesi (+ petugas, *log book*) | UC-13 | UC-16 | UC-13 (draf, koreksi) | X (3) | UC-16 | UC-26, 27 |
| Perubahan Sesi | UC-14 | UC-15 | UC-15, 09 (status) | X (3) | UC-15 | UC-16, 26 |
| Penilaian Kelas (+ baris nilai) | UC-17, 18 | UC-26 | UC-17, 18 | X (3) | UC-26 | UC-26, 27 |
| Survei (+ butir) | UC-19 | UC-22 | UC-19, 20, 21 | UC-19 (draf) | UC-25 | UC-22, 23, 26 |
| Respons Survei | UC-22 | UC-25 | X (4) | X (4) | UC-25 | UC-23, 26 |
| Evaluasi Survei (+ RTL) | UC-23 | UC-25 | UC-23, 24 | X (3) | UC-25 | UC-26, 27 |
| Pengaturan Praktikum | UC-28 | UC-28 | UC-28 | X | UC-28 | UC-13 (validasi), 26 |

Catatan:
1. Mata Kuliah dan Kelas hanya bisa dihapus bila belum dipakai Sesi; selebihnya diarsipkan.
2. Sesi hanya terhapus lewat impor ulang selama jadwal periode tidak sedang diajukan atau disahkan dan Sesi belum punya jurnal (AB-PRK-04; aturan pakai bersama Sesi, kontrak Core C-9).
3. Rekaman bukti tidak dihapus, hanya dikoreksi, dan setiap koreksi terlacak (KNF-PRK-07, KF-PRK-44).
4. Respons survei anonim tidak diubah atau dihapus oleh lab.

Penomoran UC di matriks disingkat (UC-01 = UC-PRK-01).

**Temuan dari matriks:** tidak ada konsep yang dibuat tetapi tidak pernah dibaca. Semua rekaman bukti dibaca oleh UC-PRK-26 dan 27. Tidak ada use case baru.

---

## 7. Cek silang

### 7.1 KF → use case

| KF | Use case | KF | Use case |
|---|---|---|---|
| 01 | UC-PRK-01, 02 | 27 | UC-PRK-14 |
| 02 | UC-PRK-03 (impor MK/kelas dari berkas) | 28 | UC-PRK-15 |
| 03 | UC-PRK-03 | 29 | UC-PRK-16 |
| 04 | UC-PRK-03, 07, 15 (*hidden*) | 30 | UC-PRK-13 (*hidden*) |
| 05 | UC-PRK-03 (*hidden*) | 31 | UC-PRK-17 |
| 06 | UC-PRK-04 + pengesahan Tata Kelola (UC-01–06) | 32 | UC-PRK-26 |
| 07 | UC-02 Tata Kelola (Terbitkan Dokumen Resmi) | 33 | UC-PRK-19 |
| 08 | UC-PRK-07 | 34 | UC-PRK-20 |
| 09 | UC-PRK-08 | 35 | UC-PRK-22 |
| 10, 11 | UC-PRK-10 | 36 | UC-PRK-23 |
| 12 | UC-PRK-05 | 37 | UC-PRK-24 |
| 13 | UC-PRK-05 (*hidden*) | 38 | UC-PRK-25 |
| 14 | UC-PRK-06 | 39, 40, 41 | UC-PRK-26 (*hidden*) |
| 15, 17, 18, 19 | UC-PRK-11 | 42 | UC-PRK-27 |
| 16 | UC-PRK-11 (*hidden*) | 43 | UC-PRK-28 |
| 20 | UC-PRK-12 | 44 | Perilaku sistem di semua use case (`mail.thread`, `evidence.mixin`) |
| 21 | UC-PRK-16 | 45, 46 | Perilaku hitung Sesi (`is_terpublikasi`, `is_ditunda`), terbaca di UC-PRK-10, 13, 26; pemicu 45 = UC-06 Cabut Dokumen (Tata Kelola), pemicu 46 = UC-PRK-15 |
| 22, 23, 24, 25 | UC-PRK-13 | 47 | UC-PRK-09 |
| 26 | UC-PRK-13, 15 (*hidden*) | 48 | UC-PRK-21 |
| | | 49 | UC-PRK-07, 08, 14, 15 (*hidden*) |
| | | 50 | UC-PRK-18 |
| | | 51 | UC-PRK-13 (*hidden*) |
| | | 52 | UC-PRK-11 (*hidden*, O; ditambahkan 16 Nov 2026) |

Semua 52 KF tertutup oleh use case atau dicatat sebagai perilaku sistem.

### 7.2 Pemeriksaan lain

| Cek (CLAUDE.md bagian 4) | Hasil |
|---|---|
| Setiap use case non-CRUDL punya sumber | Ya. UC-PRK-06, 17, 18, 27 bersumber dari KF (satu aktor, tidak digambar di activity sesuai §3.4) |
| Setiap kriteria instrumen punya kebutuhan dan use case | Ya, lewat tabel 7.1 dan bagian 5 kebutuhan |
| Setiap transisi state machine punya use case | Ya (bagian 4.2). Tidak ada Penjadwal |
| Status dan nama konsep sama di semua dokumen | Ya setelah penyesuaian kontrak Core 16 Nov 2026 (Sesi 3 status) |
| Rujukan nomor | KF-PRK-01–52 tidak digeser; UC baru bernomor UC-PRK-01–28 |

### 7.3 Ketidaksesuaian dengan langkah sebelumnya

- Activity A3–A4 memakai nama lajur "Pengisi Jurnal" dan "Pengaju"; di use case keduanya menjadi aktor abstrak **Petugas Praktikum**. Nama lajur di activity dibiarkan karena menjelaskan peran pada proses itu.
- Kebutuhan dan brief sebelumnya menulis aktor *Pengisi Jurnal*; **sudah disamakan** menjadi *Petugas Praktikum* (16 Nov 2026).
- **Audit 16 Nov 2026:** use case Tata Kelola UC-04 *Kembalikan Dokumen* dan UC-06 *Cabut Dokumen* belum dirujuk, padahal KF-PRK-45 bergantung pada pencabutan Penetapan Jadwal; kini ditambahkan (bagian 3 dan catatan diagram halaman 1). Label matriks CRUDL "Rencana Pemakaian Lab" disamakan menjadi **Pemakaian Lab** (nama baku conceptual model). Aktor *Admin* di kebutuhan dinyatakan bukan aktor modul (grup `base.group_system` bawaan).

---

## 8. Perbandingan dengan Tata Kelola

| | Tata Kelola (`febriyan-skripsi`) | Praktikum |
|---|---|---|
| Jumlah use case | 28 | 28 + 4 milik Tata Kelola dipakai ulang |
| Aktor abstrak | *Pengelola Lab* (KaLab, Laboran) | *Petugas Praktikum* (Asisten, Dosen, Laboran) |
| Penjadwal | Ada (kedaluwarsa dokumen) | Tidak ada |
| Pengesahan | Paket sendiri (UC-01–07) | Memakai paket Tata Kelola untuk jadwal |
| Halaman | 3 per area | 3 per area |

---

## 9. Temuan untuk Langkah 7 (expanded use case)

**Kandidat aturan bisnis (AB-PRK):** tidak ada sesi bentrok ruang dan waktu; kapasitas sebagai peringatan; satu jurnal terkirim per sesi; jam selesai > jam mulai; jurnal hanya untuk sesi terpublikasi; pemeriksaan kesiapan sebelum jam mulai; substitusi bahan disetujui dosen kelas; satu versi modul berlaku per MK per periode; perubahan sesi dan pemakaian lab diputuskan KaLab; survei wajib enam aspek, butir terbuka, dan target respons; rekaman bukti tidak dihapus; data nilai hanya NIM tanpa nama.

**Use case kunci untuk alur lengkap dan SSD (Langkah 7–8):** UC-PRK-03 Impor Jadwal Kelas, UC-PRK-11 Periksa Kesiapan Sesi, UC-PRK-13 Kirim Jurnal Sesi, UC-PRK-15 Putuskan Perubahan Sesi, UC-PRK-23 Catat Evaluasi Survei.

**Varian yang perlu ditulis:** UC-PRK-03 isian pola mingguan manual (tanpa berkas); UC-PRK-13 sesi asesmen UTS/UAS, sesi daring; UC-PRK-15 dengan pengganti / batal / daring.

---

## 10. Isu terbuka

- [x] Tampilan diagram dicek lewat ekspor PNG draw.io (16 Nov 2026): hierarki aktor halaman 2 dipindah ke bingkai tersendiri, UC-PRK-22 dipindah ke urutan terakhir paket Kepuasan agar garis Responden tidak menyilang
- [ ] Siapa pengisi jurnal kelas tanpa asisten (dosen, [ASUMSI]) dan pengesah jadwal (KaLab, [ASUMSI]) — wawancara P5, P10, P13
- [x] Pengguna Lab tidak punya akun Odoo (16 Nov 2026): aktor UC-PRK-07 menjadi Laboran; activity A2 diperbarui
