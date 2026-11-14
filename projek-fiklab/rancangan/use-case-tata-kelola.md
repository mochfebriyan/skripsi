# Use Case TO-BE Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 6 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (use case diagram).

Diagram: [use-case-tata-kelola.drawio](use-case-tata-kelola.drawio), 3 halaman. Dibuat dengan skrip [use_case.py](../tools/drawio/contoh-tata-kelola/use_case.py) dan lolos `validate.py` dengan prefiks `tk-`. **Tampilan visual belum dicek di draw.io.**

Sumber: [proses-bisnis-tata-kelola.md](proses-bisnis-tata-kelola.md) (activity A1–A4, state machine S1–S2) dan [kebutuhan-tata-kelola.md](kebutuhan-tata-kelola.md) (KF-01–45, aktor).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Use case dari tugas «user» di activity. Tugas yang harus langsung menyusul (termasuk «service» otomatis) masuk use case yang sama; tugas yang bisa ditunda (beda hari atau beda aktor) dipisah | §4.5 | Bagian 4.1 |
| Use case dari event yang mengubah status di state machine | §4.6 | Bagian 4.2 |
| Satu sesi: dimulai dan selesai tanpa jeda panjang; boleh disimpan lalu dilanjutkan | §4.3.1 | Susun Rencana mencakup temuan gap dan item, karena keduanya bagian dari satu draf yang bisa disimpan dan dilanjutkan |
| Interaktif: harus ada aktor. Proses internal bukan use case | §4.3.2 | Penanda "perlu ditinjau" dan status kriteria dihitung, bukan use case. Kedaluwarsa dipicu aktor «system» Penjadwal |
| Hasil konsisten; bukan fragmen | §4.3.3 | Tidak ada "Login", "Buka halaman", "Pilih jenis dokumen" |
| *Essential*: tanpa teknologi antarmuka ("cetak", "ekspor") | §4.3.4 | "Terbitkan Dokumen Resmi" (hasilnya dokumen yang akan ditandatangani), "Lihat Laporan …" «report» |
| Hindari «include» dan «extend» kecuali bagian bersama yang utuh | §4.3 | Tidak dipakai. Pengesahan dipisah per event (ajukan, unggah, sahkan) karena terjadi di hari yang berbeda |
| Konsep yang hanya dikelola digabung menjadi «CRUDL» | §4.3 | Personel, Jabatan, Dokumen Induk, KPI, Renstra |
| Matriks konsep × CRUDL untuk menemukan use case yang hilang | §4.8.2 | Bagian 6 |
| Aktor bukan profil keamanan | §4.2 | Aktor abstrak dipakai untuk mengelompokkan peran; grup akses diatur terpisah (kebutuhan bagian 1) |

---

## 2. Aktor

| Aktor | Jenis | Turunan dari | Keterangan |
|---|---|---|---|
| **Pengguna Lab** | Manusia | — | Dosen dan asisten. Membaca dokumen berlaku |
| ***Pengelola Lab*** | Abstrak | Pengguna Lab | Peran penyusun dokumen dan PIC item rencana. Tidak ada orang yang "hanya" Pengelola Lab |
| **Laboran/PLP** | Manusia | Pengelola Lab | Laboran, PLP, teknisi |
| **KaLab** | Manusia | Pengelola Lab | Juga satu-satunya pencatat pengesahan |
| **Penjadwal** | «system» | — | Pemicu berbasis waktu (`ir.cron`) |

Hierarki ini sejalan dengan usulan grup akses berjenjang di kebutuhan bagian 1 (KaLab ⊃ Laboran ⊃ Pengguna). Dalam use case, KaLab dan Laboran sama-sama turunan *Pengelola Lab*, karena KaLab bukan jenis laboran.

---

## 3. Daftar use case

Kolom **Lapis**: W = Inti, O = Pelengkap. Lapis hanya dicatat di tabel ini; diagram tidak membedakannya.

| UC | Nama | Stereotype | Aktor | Sumber | KF | Lapis |
|---|---|---|---|---|---|---|
| **Paket Pengesahan Dokumen** (halaman 1/3) | | | | | | |
| UC-01 | Ajukan Dokumen | — | Pengelola Lab | A1, S1 *ajukan* | KF-01, 07, 30 | W |
| UC-02 | Terbitkan Dokumen Resmi | — | Pengelola Lab | A1 | KF-35 (W); KF-26, 41 (O) | W |
| UC-03 | Unggah Dokumen Bertanda Tangan | — | Pengelola Lab | A1, S1 *unggah berkas* | KF-02, 07 | W |
| UC-04 | Kembalikan Dokumen | — | KaLab | A1, S1 *kembalikan* | KF-03, 07 | W |
| UC-05 | Sahkan Dokumen | — | KaLab | A1, S1 *sahkan*, *revisi disahkan* | KF-04, 05, 07, 08, 15, 38 | W |
| UC-06 | Cabut Dokumen | — | KaLab | A2, S1 *cabut* | KF-06, 07 | W |
| UC-07 | Kedaluwarsakan Dokumen Berperiode | — | Penjadwal | S1 *when(periode berakhir)* | KF-09 | O |
| **Paket Struktur Organisasi, PKG-03** (halaman 2/3) | | | | | | |
| UC-08 | Kelola Personel | «CRUDL» | KaLab | Master (KF) | KF-19 | W |
| UC-09 | Kelola Jabatan | «CRUDL» | KaLab | A4 *Lengkapi data jabatan* | KF-20 | W |
| UC-10 | Susun SK Penetapan Pengelola | — | KaLab | A4, S1 *buat* | KF-21 | W |
| UC-11 | Catat Rapat Koordinasi | — | KaLab | A4 | KF-22 | W |
| UC-12 | Catat Evaluasi Struktur | — | KaLab | A4 | KF-23 | W |
| UC-13 | Lihat Laporan Struktur Organisasi | «report» | KaLab | KF | KF-24, 25 | W |
| **Paket Pengendalian Dokumen, PKG-02** (halaman 2/3) | | | | | | |
| UC-14 | Kelola Dokumen Induk | «CRUDL» | Pengelola Lab | A2 *Daftarkan dokumen induk* | KF-10 | W |
| UC-15 | Unggah Versi Dokumen | — | Laboran/PLP | A2, S1 *buat* | KF-11, 18 | W |
| UC-16 | Catat Distribusi Dokumen | — | Laboran/PLP | A2 | KF-12 | W |
| UC-17 | Catat Sosialisasi Dokumen | — | Laboran/PLP | A2 | KF-13 | W |
| UC-18 | Tinjau Ulang Dokumen | — | Pengelola Lab | A2, S2 *tinjau* | KF-14, 15 | W |
| UC-19 | Baca Dokumen Berlaku | — | Pengguna Lab | KF | KF-17 | O |
| UC-20 | Lihat Laporan Pengendalian Dokumen | «report» | Pengelola Lab | KF | KF-16 | W |
| **Paket Perencanaan, PKG-01 dan PKG-13** (halaman 3/3) | | | | | | |
| UC-21 | Kelola KPI | «CRUDL» | KaLab | Master (KF) | KF-27 | W |
| UC-22 | Kelola Renstra | «CRUDL» | KaLab | S1 *buat* (Renstra) | KF-28 | W |
| UC-23 | Susun Rencana | — | KaLab | A3 *Catat temuan gap*, *Susun item rencana*; S1 *buat* | KF-29, 36, 39, 42 | W |
| UC-24 | Buat Revisi Rencana | — | KaLab | A3 | KF-37 | O |
| UC-25 | Isi Realisasi Rencana | — | Pengelola Lab (PIC item) | A3 | KF-31 | W |
| UC-26 | Catat Tinjauan Rencana | — | KaLab | A3 *Catat tinjauan*, *Catat ukuran manfaat* | KF-32, 40 | W |
| UC-27 | Lihat Laporan Rencana | «report» | KaLab | KF | KF-33, 34 | W |
| **Paket Status Monev** (halaman 3/3) | | | | | | |
| UC-28 | Lihat Status Monev | «report» | KaLab | KF | KF-43, 44, 45 | W |

**Jumlah:** 28 use case. Lapis Inti 25, Pelengkap 3 (UC-07, 19, 24). «CRUDL» 5, «report» 4, lainnya 19.

Ringkasan isi use case yang tidak jelas dari namanya:
- **UC-02 Terbitkan Dokumen Resmi:** menghasilkan dokumen resmi (PDF format lab) dari isi rencana atau SK, untuk ditandatangani. Termasuk *essential*, karena hasilnya adalah dokumen yang masuk alur pengesahan, bukan sekadar tampilan cetak. Rencana tahunan di lapis Inti; rencana pengembangan dan SK di lapis Pelengkap.
- **UC-05 Sahkan Dokumen:** KaLab mencatat pengesah tercatat dan tanggal sah. Sistem memeriksa berkas dan wewenang, mengubah status, mengganti dokumen lama, mencatat riwayat, dan untuk versi SOP/IK menghitung tanggal tinjau berikutnya.
- **UC-13:** bagan organisasi (daftar hierarki), uraian tugas per jabatan, dan matriks kewenangan.
- **UC-20:** daftar induk dokumen, riwayat revisi, serta rekaman distribusi, sosialisasi, dan tinjau ulang per versi.
- **UC-27:** matriks keterkaitan (item per rujukan Renstra) dan laporan pelaksanaan per periode lapor.
- **UC-28:** persentase SOP wajib yang memenuhi S1–S5 dan kriteria tertinggi K1–K4 untuk PKG-01, 03, 13, dengan tautan bukti. Hasilnya diserahkan ke penilai dalam bentuk PDF (bentuk keluaran adalah detail teknologi, §4.3.4).

---

## 4. Penurunan use case

### 4.1 Dari activity (§4.5)

| Activity | Tugas «user» (+ «service» yang langsung menyusul) | Use case | Alasan |
|---|---|---|---|
| A1 | Ajukan dokumen + Periksa kelengkapan + Ubah status Diajukan | UC-01 | Pemeriksaan dan perubahan status otomatis, langsung setelah pengajuan |
| A1 | Lengkapi isi dokumen, Perbaiki dokumen | UC-10, 15, 22, 23 (ubah draf) | Mengubah draf adalah bagian dari use case pembuat dokumen itu |
| A1 | Terbitkan dokumen PDF + Hasilkan PDF | UC-02 | Bisa ditunda dari pengajuan |
| A1 | Kembalikan dokumen + Ubah status Draf | UC-04 | Aktor berbeda (KaLab) |
| A1 | Unggah PDF bertanda tangan | UC-03 | Setelah tanda tangan di kertas, beda hari dengan pengajuan |
| A1 | Sahkan dokumen + Periksa berkas dan wewenang + Ubah status Disahkan + Ganti dokumen lama + Catat riwayat | UC-05 | Satu sesi KaLab; empat tugas sistem langsung menyusul |
| A2 | Daftarkan dokumen induk | UC-14 | CRUDL Dokumen Induk |
| A2 | Unggah versi dokumen | UC-15 | |
| A2 | Hitung tanggal tinjau berikutnya | Bagian dari UC-05 | Langsung menyusul pengesahan versi |
| A2 | Catat distribusi dokumen; Catat sosialisasi dokumen | UC-16; UC-17 | Paralel dan bisa beda hari, jadi dua use case |
| A2 | Tandai versi perlu ditinjau | — | Dihitung dari tanggal (KF-15), bukan tugas siapa pun |
| A2 | Tinjau ulang dokumen + Perbarui tanggal tinjau | UC-18 | |
| A2 | Cabut dokumen + Ubah status Dicabut | UC-06 | |
| A3 | Catat temuan gap + Susun item rencana | UC-23 | Satu draf rencana yang bisa disimpan dan dilanjutkan (§4.3.1) |
| A3 | Isi realisasi item | UC-25 | Aktor PIC, menunggu periode lapor |
| A3 | Buat revisi rencana | UC-24 | |
| A3 | Catat tinjauan rencana + Catat ukuran manfaat | UC-26 | Ukuran manfaat diisi dalam tinjauan yang sama |
| A4 | Lengkapi data jabatan | UC-09 | Mengubah Jabatan = CRUDL |
| A4 | Susun SK penetapan pengelola | UC-10 | |
| A4 | Catat rapat koordinasi; Catat evaluasi struktur | UC-11; UC-12 | Beda waktu |

Tugas «manual» (susun naskah SOP/IK, cetak, tinjau isi dokumen cetak, tanda tangani) **tidak** menjadi use case karena terjadi di luar sistem.

### 4.2 Dari state machine (§4.6)

| State machine | Event (transisi) | Use case |
|---|---|---|
| S1 | buat (● → Draf) | UC-10 (SK), UC-15 (versi), UC-22 (Renstra), UC-23 (rencana), UC-24 (revisi) |
| S1 | hapus (Draf → ◉) | Bagian D dari use case pembuatnya |
| S1 | ajukan | UC-01 |
| S1 | kembalikan | UC-04 |
| S1 | unggah berkas bertanda tangan | UC-03 |
| S1 | sahkan; revisi/versi baru disahkan | UC-05 |
| S1 | cabut | UC-06 |
| S1 | when(periode berakhir) | UC-07 (Penjadwal) |
| S2 | when(tanggal tinjau terlewati) | — (sub-status dihitung) |
| S2 | tinjau | UC-18 |

Semua transisi punya use case atau dihitung oleh sistem.

---

## 5. Keputusan granularitas

| Keputusan | Alasan |
|---|---|
| Pengesahan dipecah menjadi Ajukan, Unggah, Kembalikan, Sahkan, Cabut (bukan satu "Kelola Pengesahan") | Setiap event terjadi di sesi berbeda dan sering oleh aktor berbeda (§4.3.1, §4.5) |
| Pengesahan tidak di-«include» ke Susun SK, Unggah Versi, Susun Rencana | Pengajuan tidak harus langsung setelah penyusunan (§4.5) |
| Satu UC Susun Rencana untuk rencana tahunan dan pengembangan | Satu konsep rencana yang dibedakan jenisnya (brief, pola bersama). Perbedaannya ditulis sebagai varian di expanded use case (langkah 7) |
| Kelola Renstra sebagai «CRUDL» | Renstra hanya diunggah dengan periodenya, lalu disahkan lewat paket pengesahan |
| Catat Rapat, Catat Evaluasi, Catat Distribusi/Sosialisasi bukan «CRUDL» | Rekaman kejadian yang menjadi bukti kriteria, dengan aturan (misalnya hanya untuk versi berlaku). Koreksi rekaman termasuk di use case yang sama |
| Laporan digabung per paket (UC-13, 20, 27) dan satu UC status monev | Satu laporan per area cukup untuk membuktikan bukti dukung; menghindari daftar «report» yang panjang |
| Penanda perlu ditinjau dan status kriteria tidak menjadi use case | Proses internal, tidak interaktif (§4.3.2) |

---

## 6. Matriks konsep × CRUDL (§4.8.2)

C = create, R = retrieve, U = update, D = delete, L = list. **X** = tidak diizinkan oleh aturan bisnis.

| Konsep | C | R | U | D | L | Dibaca oleh |
|---|---|---|---|---|---|---|
| Personel | UC-08 | UC-08 | UC-08 | UC-08 | UC-08 | UC-10, 13, 23, 25, 05 (pengesah) |
| Jabatan (+ tugas, wewenang) | UC-09 | UC-09 | UC-09 | UC-09 | UC-09 | UC-05 (cek wewenang), 10, 13 |
| SK Penetapan (+ baris) | UC-10 | UC-10 | UC-10 (draf) | UC-10 (draf) | UC-10 | UC-12, 28 |
| Rapat Koordinasi | UC-11 | UC-11 | UC-11 | X (1) | UC-11 | UC-28 |
| Evaluasi Struktur | UC-12 | UC-12 | UC-12 | X (1) | UC-12 | UC-28 |
| Dokumen Induk | UC-14 | UC-14 | UC-14 | UC-14 (2) | UC-14 | UC-15, 19, 20, 28 |
| Versi Dokumen | UC-15 | UC-19, 20 | UC-15 (draf) | UC-15 (draf) | UC-20 | UC-16, 17, 18, 28 |
| Distribusi | UC-16 | UC-20 | UC-16 | X (1) | UC-20 | UC-28 |
| Sosialisasi (+ peserta) | UC-17 | UC-20 | UC-17 | X (1) | UC-20 | UC-28 |
| Tinjau Ulang | UC-18 | UC-20 | X (3) | X (1) | UC-20 | UC-28 |
| KPI | UC-21 | UC-21 | UC-21 | UC-21 (2) | UC-21 | UC-23, 27 |
| Renstra | UC-22 | UC-22 | UC-22 (draf) | UC-22 (draf) | UC-22 | UC-28 |
| Rencana (+ item, temuan gap) | UC-23, 24 | UC-23 | UC-23 (draf) | UC-23 (draf) | UC-23 | UC-25, 26, 27, 28 |
| Realisasi | UC-25 | UC-25, 27 | UC-25 | X (1) | UC-27 | UC-28 |
| Tinjauan Rencana (+ ukuran manfaat) | UC-26 | UC-26 | UC-26 | X (1) | UC-26 | UC-27, 28 |
| Riwayat Pengesahan | UC-01, 03–07 | UC-20, 28 | X | X | UC-20 | UC-28 |

Catatan:
1. **Keputusan (14 November 2026):** rekaman bukti tidak dihapus, hanya dikoreksi, dan setiap koreksi terlacak (KNF-05). Ditulis sebagai aturan bisnis di langkah 7.
2. Dokumen Induk dan KPI hanya bisa dihapus bila belum dipakai (belum punya versi atau belum dirujuk item rencana). Selebihnya diarsipkan.
3. Hasil tinjau ulang tidak diubah. Bila keliru, dicatat tinjauan baru.

**Temuan dari matriks:** tidak ada konsep yang dibuat tetapi tidak pernah dibaca, dan tidak ada yang dibaca tetapi tidak pernah dibuat. Tidak ada use case baru.

---

## 7. Cek silang

### 7.1 KF → use case

| KF | UC | KF | UC | KF | UC |
|---|---|---|---|---|---|
| KF-01 | UC-01 | KF-16 | UC-20 | KF-31 | UC-25 |
| KF-02 | UC-03 | KF-17 | UC-19 | KF-32 | UC-26 |
| KF-03 | UC-04 | KF-18 | UC-15 (H) | KF-33 | UC-27 |
| KF-04 | UC-05 | KF-19 | UC-08 | KF-34 | UC-27 |
| KF-05 | UC-05 (H) | KF-20 | UC-09 | KF-35 | UC-02 |
| KF-06 | UC-06 | KF-21 | UC-10 | KF-36 | UC-23 |
| KF-07 | UC-01, 03–07 (H) | KF-22 | UC-11 | KF-37 | UC-24 |
| KF-08 | UC-05 (H) | KF-23 | UC-12 | KF-38 | UC-05 (H) |
| KF-09 | UC-07 | KF-24 | UC-13 | KF-39 | UC-23 |
| KF-10 | UC-14 | KF-25 | UC-13 | KF-40 | UC-26 |
| KF-11 | UC-15 | KF-26 | UC-02 | KF-41 | UC-02 |
| KF-12 | UC-16 | KF-27 | UC-21 | KF-42 | UC-23 (H) |
| KF-13 | UC-17 | KF-28 | UC-22 | KF-43 | UC-28 (H) |
| KF-14 | UC-18 | KF-29 | UC-23 | KF-44 | UC-28 (H) |
| KF-15 | UC-05, 18 (H) | KF-30 | UC-01 (H) | KF-45 | UC-28 |

(H) = KF *hidden*, dijalankan sistem di dalam use case itu (§4.7.2). Semua 45 KF punya use case.

### 7.2 Pemeriksaan lain

- **Setiap use case non-CRUDL/non-report punya sumber** di activity atau state machine (kolom "Sumber" bagian 3). UC-19 bersumber dari KF-17 saja; ia sengaja tidak digambar di activity (proses-bisnis bagian 2).
- **Setiap transisi state machine** punya use case atau dihitung sistem (bagian 4.2).
- **Kriteria instrumen:** setiap kriteria K1–K4 dan S1–S5 tetap terhubung lewat KF → UC (kebutuhan bagian 4.2).
- **Nama status dan konsep** sama dengan S1 (Draf, Diajukan, Disahkan, Diganti, Dicabut, Kedaluwarsa).
- **Aktor:** tidak ada Dekan, Penilai, Pemeriksa, Admin, atau pihak eksternal.

### 7.3 Ketidaksesuaian dengan langkah sebelumnya

- KF-14 dan KF-10 menyebut aktor "Laboran, KaLab". Di use case, aktornya *Pengelola Lab* (abstrak). Artinya sama; tidak perlu diubah.
- KF-45 berbunyi "melihat status monev **dan menerbitkan** laporan bukti". Di sini cukup satu UC «report» (UC-28), karena laporan bukti tidak mengubah data. Tidak ada perubahan KF.

---

## 8. Perubahan dibanding versi sebelumnya

Versi sebelumnya ada di tag `rancangan-tatkel-v1` (UC-01–32, 3 halaman). Dokumen ini **disusun ulang dengan penomoran baru**; nomor lama tidak berlaku.

| Versi lama | Versi ini | Alasan |
|---|---|---|
| Tarik Pengajuan Dokumen, Periksa Dokumen | Dihapus | Tidak dirancang; pemeriksaan menyatu dengan pengesahan |
| Kelola Sasaran Renstra | Kelola Renstra (unggahan) | Rujukan Renstra cukup teks |
| Atur Pengaturan Modul, Kirim Pengingat Jadwal | Dihapus | Prinsip "hitung, bukan jadwalkan"; siklus tinjau per Dokumen Induk |
| Aktor Dekan, Pemeriksa, Penilai Monev, Admin; aktor abstrak Penyusun dan Pengesah | Aktor abstrak *Pengelola Lab* dan hierarki Pengguna Lab | Keputusan 14 November 2026 |
| Revisi rencana digabung ke Susun Rencana | Buat Revisi Rencana terpisah (Pelengkap) | Lapis berbeda; bisa dibuang tanpa mengubah UC-23 |
| — | Kolom lapis Inti/Pelengkap di daftar use case, matriks konsep × CRUDL lengkap | Konvensi sweet spot dan §4.8.2 |

---

## 9. Temuan untuk langkah 7 (expanded use case)

**Kandidat use case kunci** (alur lengkap dan SSD di langkah 8), dipilih karena punya aturan bisnis atau mengubah status:

| UC | Alasan |
|---|---|
| UC-01 Ajukan Dokumen | Cek kelengkapan per jenis dokumen (KF-30) |
| UC-03 Unggah Dokumen Bertanda Tangan | Hanya saat Diajukan |
| UC-05 Sahkan Dokumen | Inti mekanisme: cek berkas dan wewenang, ganti dokumen lama, riwayat, tanggal tinjau |
| UC-15 Unggah Versi Dokumen | Satu versi dalam proses (KF-18), nomor revisi |
| UC-18 Tinjau Ulang Dokumen | Hanya versi berlaku; memperbarui tanggal tinjau |
| UC-23 Susun Rencana | Dua varian (tahunan, pengembangan) |
| UC-25 Isi Realisasi Rencana | Hanya untuk rencana Disahkan; hanya PIC item |
| UC-28 Lihat Status Monev | Perhitungan S1–S5 dan K1–K4 |

**Kandidat aturan bisnis (AB):** dari KF *hidden* (KF-05, 08, 15, 18, 30, 38, 42, 43, 44) dan dari catatan matriks CRUDL (rekaman bukti tidak dihapus; master hanya dihapus bila belum dipakai; rekaman hanya untuk versi atau rencana yang berlaku).

## 10. Isu terbuka

- [x] Rekaman bukti hanya dikoreksi, tidak dihapus (bagian 6, catatan 1). Disetujui Febriyan, 14 November 2026
- [x] Laboran juga boleh melihat laporan pengendalian dokumen (UC-20). Disetujui Febriyan, 14 November 2026; aktor UC-20 menjadi *Pengelola Lab* dan KF-16 disesuaikan
- [ ] Tampilan diagram belum dicek di draw.io **[VALIDASI]**
