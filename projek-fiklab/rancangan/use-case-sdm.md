# Use Case TO-BE Modul SDM & Kompetensi

15 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 6 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (use case diagram).

Diagram: [use-case-sdm.drawio](use-case-sdm.drawio), 4 halaman. Dibuat dengan skrip [tools/drawio/sdm/use_case.py](../tools/drawio/sdm/use_case.py). Fungsi gambar skrip itu disalin dari `contoh-tata-kelola/use_case.py` **versi branch `febriyan-skripsi`**; yang diganti data, prefiks `sdm-`, kode `UC-SDM-nn`, dan warna modul `#EEFAF3`/`#4E9A6B`. Skrip ini menambah satu gaya: package rujukan abu-abu putus-putus. Diagram lolos `validate.py` dengan prefiks `sdm-`. **Tampilan visual belum dicek di draw.io**, karena draw.io tidak tersedia saat diagram dibuat.

Sumber:
- [proses-bisnis-sdm.md](proses-bisnis-sdm.md): activity A1–A3, state machine S1–S3.
- [kebutuhan-sdm.md](kebutuhan-sdm.md): KF-SDM-01–43 dan aktor.
- [kontrak-core-sdm.md](kontrak-core-sdm.md): pemakaian `approval.mixin` dan K-3.
- [use-case-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/use-case-tata-kelola.md) (branch `febriyan-skripsi`): use case pengesahan UC-01–06 yang dipakai ulang.

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| *Use case* diturunkan dari tugas «user» di activity. Tugas yang harus langsung menyusul, termasuk «service» otomatis, masuk *use case* yang sama. Tugas yang bisa ditunda (beda hari atau beda aktor) dipisah | §4.5 | Bagian 4.1 |
| *Use case* diturunkan dari event yang mengubah status di state machine | §4.6 | Bagian 4.2. Event *catat pemicu* dan *putuskan* pada S2 dipisah karena status *Terbuka* di antaranya adalah jeda nyata |
| Satu sesi: dimulai dan selesai tanpa jeda panjang; boleh disimpan lalu dilanjutkan | §4.3.1 | Susun Rencana Pelatihan mencakup kebutuhan dan item dalam satu draf |
| Interaktif: harus ada aktor. Proses internal bukan *use case* | §4.3.2 | Status S1–S4 per sesi dan per pasangan, status berlaku, dan kriteria tertinggi dihitung, bukan *use case*. Tidak ada aktor Penjadwal (kontrak Core K-3) |
| Hasil konsisten, bukan fragmen | §4.3.3 | Tidak ada "Login", "Pilih kelas", atau "Isi kebutuhan otomatis" sebagai *use case* |
| *Essential*: tanpa teknologi antarmuka | §4.3.4 | Penerbitan PDF memakai "Terbitkan Dokumen Resmi" (UC-02 Tata Kelola). Laporan bukti untuk penilai termasuk di "Lihat Status Monev SDM" «report» |
| Hindari «include» dan «extend» kecuali bagian bersama yang utuh | §4.3 | Tidak dipakai. Pengesahan memakai *use case* Tata Kelola yang berdiri sendiri, karena terjadi di sesi dan hari yang berbeda dari penyusunan |
| Konsep yang hanya dikelola digabung menjadi «CRUDL»; satu *use case* untuk mengubah beberapa field konsep yang sama | §4.3 | Kompetensi, Syarat Kompetensi Jabatan, Bukti Kompetensi, Tugas/Alat (termasuk pelaksana) |
| Matriks konsep × CRUDL untuk menemukan *use case* yang hilang | §4.8.2 | Bagian 6 |
| Aktor bukan profil keamanan; aktor abstrak untuk mengelompokkan peran | §4.2 | *Pengelola Lab* (abstrak) dengan turunan KaLab dan Laboran/PLP, sama dengan Tata Kelola |
| Komponen yang sudah bekerja tertutup untuk diubah, terbuka untuk diperluas | §4.7.1 | Pengesahan tidak dirancang ulang; SDM memakai UC-01–06 Tata Kelola |

---

## 2. Aktor

| Aktor | Jenis | Turunan dari | Keterangan |
|---|---|---|---|
| ***Pengelola Lab*** | Abstrak | — | Peran pencatat rekaman bukti dan penyusun draf dokumen. Tidak ada orang yang "hanya" Pengelola Lab. Nama sama dengan aktor abstrak Tata Kelola |
| **Laboran/PLP** | Manusia | Pengelola Lab | Laboran, PLP, teknisi |
| **KaLab** | Manusia | Pengelola Lab | Menetapkan master, syarat, kebutuhan petugas, dan rencana; menyusun otorisasi; satu-satunya pencatat pengesahan |

Di Tata Kelola, *Pengelola Lab* adalah turunan *Pengguna Lab* (dosen, asisten), yang membaca dokumen berlaku. Modul SDM tidak punya *use case* untuk Pengguna Lab, jadi aktor itu tidak digambar di sini. Hierarkinya tetap sama bila kedua diagram digabung.

**Bukan aktor:** Dekan, Wadek, Koor Prodi (hanya menandatangani; tercatat sebagai pengesah atau penyetuju pengecualian), asisten praktikum, calon yang tidak lulus, dan penilai monev (menerima PDF). Alasannya ada di [kebutuhan-sdm.md](kebutuhan-sdm.md) bagian 1. **Penjadwal tidak dipakai**: status berlaku Bukti Kompetensi, Otorisasi, dan baris penugasan dihitung dari tanggal saat dibaca.

---

## 3. Daftar use case

Kolom **Lapis**: W = Inti, O = Pelengkap. Lapis hanya dicatat di tabel ini; diagram tidak membedakannya.

| UC | Nama | Stereotype | Aktor | Sumber | KF | Lapis |
|---|---|---|---|---|---|---|
| **Paket Kompetensi** (halaman 1/4) | | | | | | |
| UC-SDM-01 | Kelola Kompetensi | «CRUDL» | KaLab | Master (KF) | KF-SDM-01 | W |
| UC-SDM-02 | Kelola Syarat Kompetensi Jabatan | «CRUDL» | KaLab | Master (KF) | KF-SDM-02 | W |
| UC-SDM-03 | Kelola Bukti Kompetensi | «CRUDL» | Pengelola Lab | Master (KF); proses-bisnis bagian 2 | KF-SDM-03, 04 (H) | W |
| UC-SDM-04 | Lihat Matriks Kompetensi | «report» | KaLab | KF | KF-SDM-05, 04 (H) | W |
| **Paket Pengesahan Dokumen SDM: memakai UC Tata Kelola** (halaman 1/4, tidak diberi nomor SDM) | | | | | | |
| UC-01 (TK) | Ajukan Dokumen | — | Pengelola Lab | TK-A1, S1 *ajukan* | KF-SDM-06; 11, 23, 32 (H) | W |
| UC-02 (TK) | Terbitkan Dokumen Resmi | — | Pengelola Lab | TK-A1 | KF-SDM-17, 39 | O |
| UC-03 (TK) | Unggah Dokumen Bertanda Tangan | — | Pengelola Lab | TK-A1, S1 *unggah berkas* | KF-SDM-06 | W |
| UC-04 (TK) | Kembalikan Dokumen | — | KaLab | TK-A1, S1 *kembalikan* | KF-SDM-06 | W |
| UC-05 (TK) | Sahkan Dokumen | — | KaLab | TK-A1, S1 *sahkan*; A2 *Ganti otorisasi lama* | KF-SDM-06; 24, 43 (H) | W |
| UC-06 (TK) | Cabut Dokumen | — | KaLab | A2 *Cabut otorisasi*, S1 *cabut* | KF-SDM-06 | W |
| **Paket Penugasan Petugas, PKG-04** (halaman 2/4) | | | | | | |
| UC-SDM-05 | Tetapkan Kebutuhan Petugas | — | KaLab | A1 *Tetapkan kebutuhan petugas* | KF-SDM-09 | W |
| UC-SDM-06 | Catat Hasil Seleksi Asisten | — | Pengelola Lab | A1 *Catat hasil seleksi*, *Buat personel asisten* | KF-SDM-07, 08 | W |
| UC-SDM-07 | Susun Surat Tugas | — | Pengelola Lab | A1 *Susun surat tugas*; S1 TK *buat* | KF-SDM-10, 15 (O) | W |
| UC-SDM-08 | Buat Revisi Surat Tugas | — | KaLab | A1 *Buat revisi surat tugas* | KF-SDM-14 | O |
| UC-SDM-09 | Catat Orientasi Petugas Baru | — | Pengelola Lab | KF (tidak digambar di activity, proses-bisnis bagian 2) | KF-SDM-16 | O |
| UC-SDM-10 | Lihat Daftar Petugas per Sesi | «report» | KaLab | KF | KF-SDM-13, 12 (H) | W |
| **Paket Otorisasi Personel, PKG-10** (halaman 3/4) | | | | | | |
| UC-SDM-11 | Kelola Tugas/Alat Berkewenangan Khusus | «CRUDL» | KaLab | A2 *Tetapkan pelaksana tugas/alat* | KF-SDM-18, 19, 28 (O) | W |
| UC-SDM-12 | Catat Asesmen Keterampilan | — | Pengelola Lab | A2 *Catat asesmen keterampilan*, *Buat bukti kompetensi* | KF-SDM-20, 21 (H) | W |
| UC-SDM-13 | Susun Otorisasi | — | KaLab | A2 *Susun otorisasi*; S1 *buat*, *hapus* | KF-SDM-22 | W |
| UC-SDM-14 | Catat Pemicu Evaluasi Ulang | — | Pengelola Lab | A2 *Catat evaluasi ulang otorisasi*; S2 *catat pemicu* | KF-SDM-25 | W |
| UC-SDM-15 | Putuskan Evaluasi Ulang Otorisasi | — | Pengelola Lab | A2 *Catat evaluasi ulang otorisasi*; S2 *putuskan* | KF-SDM-25 | W |
| UC-SDM-16 | Lihat Daftar Operator Sah | «report» | KaLab | KF | KF-SDM-27, 26 (H) | W |
| **Paket Pelatihan PLP/Laboran, PKG-14** (halaman 4/4) | | | | | | |
| UC-SDM-17 | Susun Rencana Pelatihan | — | KaLab | A3 *Buat rencana*, *Isi kebutuhan*, *Lengkapi kebutuhan*, *Susun item*; S3 *tambah item*, *hapus item* | KF-SDM-29, 30 (H), 31 | W |
| UC-SDM-18 | Catat Realisasi Pelatihan | — | Pengelola Lab | A3 *Catat realisasi pelatihan*; S3 *catat realisasi* | KF-SDM-33 | W |
| UC-SDM-19 | Catat Evaluasi Efektivitas Pelatihan | — | Pengelola Lab | A3 *Catat evaluasi efektivitas*, *Buat bukti kompetensi* | KF-SDM-34, 35 (H) | W |
| UC-SDM-20 | Batalkan Item Pelatihan | — | KaLab | A3 *Tandai item batal*; S3 *tandai batal* | KF-SDM-37 | O |
| UC-SDM-21 | Lihat Rekap Pelatihan Personel | «report» | KaLab | KF | KF-SDM-38 | O |
| **Paket Status Monev** (halaman 4/4) | | | | | | |
| UC-SDM-22 | Lihat Status Monev SDM | «report» | KaLab | KF | KF-SDM-40, 42; 12, 26, 36, 41 (H) | W |

**Jumlah:** 22 *use case* milik SDM (UC-SDM-01–22), ditambah 6 *use case* Tata Kelola yang dipakai ulang. Dari 22 *use case* SDM, lapis Inti ada 18 dan Pelengkap 4 (UC-SDM-08, 09, 20, 21). Menurut jenis: «CRUDL» 4, «report» 5, lainnya 13.

Ringkasan isi *use case* yang tidak jelas dari namanya:
- **UC-SDM-02 Kelola Syarat Kompetensi Jabatan:** KaLab memilih Kompetensi wajib untuk tiap Jabatan. Untuk Asisten Praktikum hanya syarat umum; syarat per MK dicek lewat seleksi. Secara teknis ini tab di formulir `hr.job` (langkah 10). Di sini ia dijadikan *use case* tersendiri karena Kelola Jabatan adalah milik Tata Kelola (UC-09) dan Core tidak diubah.
- **UC-SDM-03 Kelola Bukti Kompetensi:** «CRUDL», karena Bukti Kompetensi tidak punya status dan proses (proses-bisnis bagian 2). Rekaman ini tidak dapat dihapus, hanya dikoreksi (bagian 6, catatan 1). Bukti juga dibuat otomatis oleh UC-SDM-12 dan 19.
- **UC-SDM-06 Catat Hasil Seleksi Asisten:** hanya untuk calon yang lulus atau lulus dengan pengecualian. Pengecualian mencatat alasan dan penyetuju, yang menyetujui di atas kertas. Bila calon belum ada sebagai Personel, sistem membuatnya (`jenis_personel` = asisten, Jabatan = Asisten Praktikum).
- **UC-SDM-07 Susun Surat Tugas:** membuat dan mengubah draf Surat Tugas bergaris per periode (asisten → kelas, laboran → ruang, dengan rentang berlaku), termasuk berkas komitmen petugas (Pelengkap). Kelengkapan (KF-SDM-11) diperiksa saat UC-01 Ajukan, bukan di sini.
- **UC-SDM-11 Kelola Tugas/Alat Berkewenangan Khusus:** termasuk daftar **pelaksana**, yaitu penyebut PKG-10 (KB-1), dan cara pembatasan akses (Pelengkap).
- **UC-SDM-14 dan 15:** pemicu dicatat saat terjadi, lalu evaluasi ulang berstatus *Terbuka* dan S4 gagal sampai diputuskan. Keputusan diambil setelah personel dinilai ulang. Keputusan *diperpanjang/dibatasi/naik level* diikuti Susun Otorisasi baru (UC-SDM-13); *dicabut* diikuti UC-06 Cabut Dokumen; *tetap berlaku* tidak diikuti apa pun (KP-1).
- **UC-SDM-17 Susun Rencana Pelatihan:** sistem mengisi awal daftar kebutuhan dari selisih Kompetensi wajib dan Bukti Kompetensi berlaku setiap PLP/laboran dan teknisi aktif. KaLab melengkapinya dan menambah item. Semuanya dalam satu draf yang bisa disimpan dan dilanjutkan (§4.3.1). Kebutuhan dibekukan saat UC-01 Ajukan.
- **UC-SDM-22 Lihat Status Monev SDM:** persentase PKG-04 dan PKG-10, kriteria tertinggi K1–K4 PKG-14 yang lengkap secara data, daftar unit yang belum memenuhi beserta syarat yang gagal, dan tautan ke rekaman bukti. Hasilnya diserahkan ke penilai sebagai PDF (KF-SDM-42). Bentuk keluaran adalah detail teknologi (§4.3.4). Skor akhir PKG-14 ditetapkan penilai.

---

## 4. Penurunan use case

### 4.1 Dari activity (§4.5)

| Activity | Tugas «user» (+ «service» yang langsung menyusul) | Use case | Alasan |
|---|---|---|---|
| A1 | Tetapkan kebutuhan petugas | UC-SDM-05 | Rekaman bukti S1 (`evidence.mixin`), bukan master; karena itu bukan «CRUDL» |
| A1 | Catat hasil seleksi + Buat personel asisten | UC-SDM-06 | Personel dibuat otomatis langsung setelah hasil seleksi disimpan |
| A1 | Susun surat tugas | UC-SDM-07 | Bisa ditunda dari seleksi (beda hari) |
| A1, A2, A3 | Sahkan dokumen (TK-A1) «call behavior» | UC-01, 03, 04, 05 (TK) | Satu *use case* per event pengesahan, sama dengan Tata Kelola |
| A1 | Buat revisi surat tugas | UC-SDM-08 | Pelengkap; aktor KaLab |
| A2 | Tetapkan pelaksana tugas/alat | UC-SDM-11 (ubah) | Pelaksana adalah bagian data Tugas/Alat. Sama dengan "Lengkapi data jabatan" → Kelola Jabatan di Tata Kelola |
| A2 | Catat asesmen keterampilan + Buat bukti kompetensi | UC-SDM-12 | Bukti dibuat otomatis bila *layak* |
| A2 | Susun otorisasi | UC-SDM-13 | |
| A2 | Ganti otorisasi lama «service» | Bagian dari UC-05 (TK) | Langsung menyusul pengesahan, lewat *hook* `_dokumen_diganti()` |
| A2 | Catat evaluasi ulang otorisasi | UC-SDM-14 + UC-SDM-15 | **Dipecah** karena S2 menunjukkan jeda (*Terbuka*) antara pemicu dan keputusan. Lihat bagian 8 |
| A2 | Cabut otorisasi | UC-06 (TK) | |
| A3 | Buat rencana + Isi kebutuhan dari matriks + Lengkapi kebutuhan + Susun item | UC-SDM-17 | Satu draf rencana yang bisa disimpan dan dilanjutkan (§4.3.1); pengisian kebutuhan otomatis langsung menyusul |
| A3 | Tandai item batal | UC-SDM-20 | Pelengkap |
| A3 | Catat realisasi pelatihan | UC-SDM-18 | Menunggu jadwal pelatihan |
| A3 | Catat evaluasi efektivitas + Buat bukti kompetensi | UC-SDM-19 | Menunggu waktu evaluasi; bukti dibuat otomatis bila *efektif* |

Tugas «manual» (seleksi calon, setujui pengecualian, uji keterampilan, ikuti pengembangan, ikuti pelatihan, terapkan keterampilan) **tidak** menjadi *use case* karena terjadi di luar sistem.

### 4.2 Dari state machine (§4.6)

| State machine | Event (transisi) | Use case |
|---|---|---|
| S1 Otorisasi | buat (● → Draf) | UC-SDM-13 |
| S1 | hapus (Draf → ◉) | Bagian D dari UC-SDM-13 |
| S1 | ajukan | UC-01 (TK) |
| S1 | kembalikan | UC-04 (TK) |
| S1 | unggah berkas bertanda tangan | UC-03 (TK) |
| S1 | sahkan; otorisasi baru pasangan sama disahkan (→ Diganti) | UC-05 (TK) |
| S1 | when(hari ini > berlaku_sampai) | — (sub-status dihitung) |
| S1 | cabut `[evaluasi ulang: dicabut]` | UC-06 (TK), setelah UC-SDM-15 |
| S2 Evaluasi Ulang | catat pemicu (● → Terbuka) | UC-SDM-14 |
| S2 | putuskan (tiga varian guard, termasuk *tetap berlaku*) | UC-SDM-15 |
| S3 Item Pelatihan | tambah item; hapus item `[rencana Draf]` | UC-SDM-17 |
| S3 | catat realisasi `[rencana Disahkan]` | UC-SDM-18 |
| S3 | tandai batal | UC-SDM-20 |
| S3 | when(setiap realisasi punya evaluasi) | — (sub-status dihitung, berubah sebagai akibat UC-SDM-19) |
| S1 Tata Kelola (Surat Tugas, Rencana Pelatihan) | buat | UC-SDM-07, 08 (Surat Tugas); UC-SDM-17 (Rencana) |
| S1 Tata Kelola | ajukan, kembalikan, unggah, sahkan, cabut | UC-01, 03–06 (TK) |
| S1 Tata Kelola | when(periode berakhir), hanya Rencana Pelatihan | UC-07 (TK, Penjadwal, Pelengkap Tata Kelola) |

Semua transisi punya *use case* atau dihitung oleh sistem.

---

## 5. Keputusan granularitas

| Keputusan | Alasan |
|---|---|
| Pengesahan tidak dirancang ulang; dipakai UC-01–06 Tata Kelola | Mekanismenya satu (`approval.mixin` di Core). Merancang ulang akan membuat dua versi perilaku yang sama (§4.7.1; CLAUDE.md bagian 6) |
| UC Tata Kelola digambar sebagai package rujukan abu-abu putus-putus, bukan hanya catatan | Pembaca proposal bisa melihat aktor SDM mana yang mengajukan dan mengesahkan dokumen SDM tanpa membuka diagram modul lain |
| Evaluasi ulang dipecah menjadi Catat Pemicu dan Putuskan | Ada jeda nyata (status *Terbuka*) yang menentukan S4; satu *use case* akan melanggar kriteria satu sesi (§4.3.1, §4.6) |
| Pelaksana tugas/alat masuk «CRUDL» Tugas/Alat, bukan *use case* sendiri | Pelaksana adalah atribut Tugas/Alat; satu *use case* untuk mengubah beberapa field konsep yang sama (§4.3) |
| Kebutuhan Petugas bukan «CRUDL» | Rekaman bukti S1 dengan aturan (tidak dihapus, dicatat per kelas per periode), sama dengan perlakuan "Catat Rapat Koordinasi" di Tata Kelola |
| Bukti Kompetensi tetap «CRUDL» | Tidak punya status atau proses (proses-bisnis bagian 2). Larangan hapus ditulis di matriks dan menjadi aturan bisnis |
| Syarat Kompetensi Jabatan dipisah dari Kelola Jabatan | Kelola Jabatan milik Tata Kelola (UC-09) dan Core tidak diubah. Syarat ditambahkan oleh `labfik_sdm` |
| Pengecualian seleksi tidak menjadi *use case* sendiri | Persetujuan terjadi di luar sistem; pencatatannya bagian dari mencatat hasil seleksi yang sama |
| Laporan bukti untuk penilai (KF-SDM-42) digabung ke Lihat Status Monev SDM | Tidak mengubah data; PDF adalah bentuk keluaran (§4.3.4). Sama dengan UC-28 Tata Kelola |
| Status S1–S4, status berlaku, dan kriteria tertinggi tidak menjadi *use case* | Proses internal, tidak interaktif (§4.3.2) |
| Tidak ada *use case* untuk revisi Rencana Pelatihan | Tidak ada KF-nya dan tidak dibutuhkan kriteria K1–K4 (bagian 8, KU-2) |

---

## 6. Matriks konsep × CRUDL (§4.8.2)

C = create, R = retrieve, U = update, D = delete, L = list. **X** = tidak diizinkan oleh aturan bisnis.

| Konsep | C | R | U | D | L | Dibaca oleh |
|---|---|---|---|---|---|---|
| Kompetensi | SDM-01 | SDM-01 | SDM-01 | SDM-01 (2) | SDM-01 | SDM-02, 03, 04, 11, 17 |
| Syarat Kompetensi Jabatan | SDM-02 | SDM-02 | SDM-02 | SDM-02 | SDM-02 | SDM-04, 17 (isi kebutuhan), 10 dan 22 (S3) |
| Bukti Kompetensi | SDM-03, 12, 19 | SDM-03, 04 | SDM-03 (koreksi) | X (1) | SDM-03, 04 | SDM-04, 13 dan UC-01 TK (kelengkapan otorisasi), 17, 10 dan 22 (S3) |
| Personel (asisten) | SDM-06; UC-08 TK | UC-08 TK | UC-08 TK | X (3) | UC-08 TK | SDM-07, 10, 22 |
| Kebutuhan Petugas | SDM-05 | SDM-05 | SDM-05 (koreksi) | X (1) | SDM-05, 10 | SDM-10, 22 (S1) |
| Seleksi Asisten | SDM-06 | SDM-06 | SDM-06 (koreksi) | X (1) | SDM-06 | UC-01 TK (kelengkapan Surat Tugas), SDM-10, 22 (S4) |
| Surat Tugas (+ baris penugasan) | SDM-07, 08 | SDM-07 | SDM-07 (draf) | SDM-07 (draf) | SDM-07 | SDM-10, 22 (S2) |
| Orientasi Petugas | SDM-09 | SDM-09 | SDM-09 (koreksi) | X (1) | SDM-09 | SDM-22 (laporan bukti, rekaman pendukung) **(4)** |
| Tugas/Alat (+ pelaksana, pembatasan akses) | SDM-11 | SDM-11 | SDM-11 | SDM-11 (2) | SDM-11 | SDM-12, 13, 16, 22 (penyebut) |
| Asesmen Keterampilan | SDM-12 | SDM-12 | SDM-12 (koreksi) | X (1) | SDM-12 | SDM-13 (dasar), UC-01 TK, SDM-22 (S1) |
| Otorisasi | SDM-13 | SDM-13 | SDM-13 (draf) | SDM-13 (draf) | SDM-13, 16 | SDM-13 (supervisor), 14, 15, 16, 22 (S2, S3) |
| Evaluasi Ulang Otorisasi | SDM-14 | SDM-14, 15 | SDM-15 (hanya *Terbuka*) | X (1) | SDM-14, 15 | SDM-22 (S4) |
| Rencana Pelatihan (+ kebutuhan, item) | SDM-17 | SDM-17 | SDM-17 (draf), 20 (batal item) | SDM-17 (draf) | SDM-17 | SDM-18, 19, 21, 22 (K1–K2) |
| Realisasi Pelatihan | SDM-18 | SDM-18 | SDM-18 (koreksi) | X (1) | SDM-18, 21 | SDM-19, 21, 22 (K3) |
| Evaluasi Efektivitas | SDM-19 | SDM-19 | SDM-19 (koreksi) | X (1) | SDM-19, 21 | SDM-21, 22 (K4) |
| Riwayat Pengesahan (Core) | UC-01, 03–06 TK | SDM-22 (tautan bukti) | X | X | UC-01 TK | SDM-22 |

Catatan:
1. Rekaman bukti (`evidence.mixin`) tidak dihapus, hanya dikoreksi, dan setiap koreksi terlacak (KNF-SDM-05; keputusan yang sama di Tata Kelola, 14 November 2026). Ditulis sebagai aturan bisnis di langkah 7.
2. Kompetensi dan Tugas/Alat hanya bisa dihapus bila belum dipakai (belum dirujuk syarat, bukti, asesmen, otorisasi, atau item). Selebihnya diarsipkan.
3. Personel tidak dihapus oleh modul SDM; pengelolaannya milik UC-08 Kelola Personel (Tata Kelola).
4. **Temuan dari matriks:** Orientasi Petugas (KF-SDM-16) dibuat, tetapi di langkah 4 tidak ada KF yang membacanya untuk keperluan monev. Padahal rekaman ini adalah bukti dukung 7 PKG-04. Koreksi: laporan bukti di UC-SDM-22 (KF-SDM-42) juga memuat rekaman pendukung, yaitu orientasi (bukti 7 PKG-04) dan cara pembatasan akses (bukti 4 PKG-10). Tidak ada *use case* baru; KF-SDM-42 perlu diperjelas (bagian 9.3).

Selain catatan 4, tidak ada konsep yang dibuat tetapi tidak dibaca, dan tidak ada yang dibaca tetapi tidak dibuat.

---

## 7. Cek silang

### 7.1 KF → use case

| KF | UC | KF | UC | KF | UC |
|---|---|---|---|---|---|
| KF-SDM-01 | SDM-01 | KF-SDM-16 | SDM-09 | KF-SDM-31 | SDM-17 |
| KF-SDM-02 | SDM-02 | KF-SDM-17 | UC-02 TK | KF-SDM-32 | UC-01 TK (H) |
| KF-SDM-03 | SDM-03 | KF-SDM-18 | SDM-11 | KF-SDM-33 | SDM-18 |
| KF-SDM-04 | SDM-03, 04, 17, 22 (H) | KF-SDM-19 | SDM-11 | KF-SDM-34 | SDM-19 |
| KF-SDM-05 | SDM-04 | KF-SDM-20 | SDM-12 | KF-SDM-35 | SDM-19 (H) |
| KF-SDM-06 | UC-01, 03–06 TK | KF-SDM-21 | SDM-12 (H) | KF-SDM-36 | SDM-22 (H) |
| KF-SDM-07 | SDM-06 | KF-SDM-22 | SDM-13 | KF-SDM-37 | SDM-20 |
| KF-SDM-08 | SDM-06 | KF-SDM-23 | UC-01 TK (H) | KF-SDM-38 | SDM-21 |
| KF-SDM-09 | SDM-05 | KF-SDM-24 | UC-05 TK (H) | KF-SDM-39 | UC-02 TK |
| KF-SDM-10 | SDM-07 | KF-SDM-25 | SDM-14, 15 | KF-SDM-40 | SDM-22 |
| KF-SDM-11 | UC-01 TK (H) | KF-SDM-26 | SDM-16, 22 (H) | KF-SDM-41 | SDM-22 (H) |
| KF-SDM-12 | SDM-10, 22 (H) | KF-SDM-27 | SDM-16 | KF-SDM-42 | SDM-22 |
| KF-SDM-13 | SDM-10 | KF-SDM-28 | SDM-11 | KF-SDM-43 | UC-05 TK (H) |
| KF-SDM-14 | SDM-08 | KF-SDM-29 | SDM-17 | | |
| KF-SDM-15 | SDM-07 | KF-SDM-30 | SDM-17 (H) | | |

(H) = KF *hidden*, dijalankan sistem di dalam *use case* itu (§4.7.2). **Semua 43 KF punya *use case*.** Empat KF *hidden* (11, 23, 32, 43) dan satu KF *hidden* (24) berjalan di dalam *use case* Tata Kelola lewat *hook* `approval.mixin` (`_cek_kelengkapan()`, `_sebelum_ajukan()`, `_dokumen_diganti()`) yang diisi model SDM. Ini kontrak lintas modul; dirinci di langkah 8 dan 10.

### 7.2 Pemeriksaan lain

| Cek | Hasil |
|---|---|
| Setiap *use case* non-CRUDL/non-report punya sumber di activity atau state machine | ✓, kecuali UC-SDM-09 Catat Orientasi Petugas Baru, yang bersumber dari KF-SDM-16 saja. Ini disengaja: proses-bisnis bagian 2 tidak menggambarnya karena hanya satu tugas pencatatan (Pelengkap). Perlakuan yang sama dengan UC-19 Tata Kelola |
| Setiap transisi state machine punya *use case* atau dihitung | ✓ (bagian 4.2) |
| Setiap kriteria instrumen punya kebutuhan dan rekaman | ✓ lewat KF → UC. PKG-04 S1 SDM-05, S2 SDM-07 + UC-05 TK, S3 SDM-02/03, S4 SDM-06. PKG-10 penyebut SDM-11, S1 SDM-12/03, S2 SDM-13 + UC-05 TK, S3 SDM-13, S4 SDM-14/15. PKG-14 K1 SDM-17 + UC-05 TK, K2 SDM-17, K3 SDM-18, K4 SDM-19 |
| Nama status dan konsep sama dengan langkah 5 | ✓ Draf, Diajukan, Disahkan (Berlaku/Lewat masa berlaku), Diganti, Dicabut; Terbuka, Diputuskan; Direncanakan, Terlaksana, Batal |
| Aktor | ✓ Hanya KaLab, Laboran/PLP, dan *Pengelola Lab* (abstrak). Tidak ada Dekan, penilai, asisten, atau Penjadwal |
| Nama *use case* | ✓ Tanpa "dan/atau", tanpa "cetak/ekspor/login". "Daftar Sesi dan Petugas" (nama bukti 1 di analisis) diganti "Daftar Petugas per Sesi" agar tidak terbaca sebagai dua hal |
| Lantai instrumen | ✓ Semua kriteria hanya bergantung pada *use case* lapis Inti. *Use case* Pelengkap (SDM-08, 09, 20, 21; UC-02 TK) bisa dibuang tanpa kriteria yang gagal |

### 7.3 Ketidaksesuaian dengan langkah sebelumnya

| Langkah | Ketidaksesuaian | Penanganan |
|---|---|---|
| 4 | KF-SDM-08 beraktor "KaLab", padahal pencatatan pengecualian adalah bagian dari Catat Hasil Seleksi yang beraktor *Pengelola Lab* (lajur Laboran di A1) | Aktor KF-SDM-08 diubah menjadi "KaLab, Laboran" (bagian 9.3). Yang menyetujui pengecualian tetap pejabat di luar sistem |
| 4 | KF-SDM-42 tidak menyebut rekaman pendukung (orientasi, pembatasan akses), sehingga Orientasi tidak punya pembaca | Diperjelas (bagian 6, catatan 4) |
| 4 | KF-SDM-25 belum memuat keputusan *tetap berlaku* | Masih KP-1. UC-SDM-15 memakainya sebagai *default* |
| 5 | A2 hanya punya satu tugas "Catat evaluasi ulang otorisasi", padahal S2 menunjukkan jeda antara pemicu dan keputusan | A2 sebaiknya memecah tugas menjadi *Catat pemicu evaluasi ulang* → ⧗ *personel dinilai ulang* → *Putuskan evaluasi ulang* (bagian 9.3) |
| 5 | Catatan 5 di S3 ("pelatihan pengganti dibuat sebagai item baru di revisi rencana") merujuk revisi Rencana Pelatihan, yang tidak punya KF | Catatan diganti menjadi "pelatihan pengganti masuk rencana tahun berikutnya" (KU-2) |
| 5 | Bagian 6.5 mengusulkan Kebutuhan Petugas sebagai «CRUDL» | Tidak diikuti; alasannya di bagian 5 |
| Brief | Paragraf aktor masih mencantumkan Penjadwal (kedaluwarsa otorisasi). Ini sudah dicatat di kebutuhan bagian 7.4 tetapi belum diubah | Tetap perlu diubah (bagian 9.3) |

---

## 8. Perbandingan dengan contoh Tata Kelola

Dibandingkan dengan [use-case-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/use-case-tata-kelola.md) (branch `febriyan-skripsi`):

| Aspek | Tata Kelola | SDM (dokumen ini) |
|---|---|---|
| Struktur dokumen | Aturan, aktor, daftar UC, penurunan (activity, state machine), keputusan granularitas, matriks CRUDL, cek silang, perubahan versi, temuan langkah 7, isu | Sama, ditambah tabel ketidaksesuaian dengan langkah 4–5 dan perbandingan ini. Tanpa "perubahan versi" karena ini versi pertama |
| Jumlah | 28 UC (Inti 25, Pelengkap 3); «CRUDL» 5, «report» 4 | 22 UC SDM (Inti 18, Pelengkap 4); «CRUDL» 4, «report» 5; ditambah 6 UC Tata Kelola dipakai ulang |
| Kode | UC-01–28 (tanpa prefiks) | **UC-SDM-01–22**; UC Tata Kelola dirujuk sebagai "UC-01 (TK)" |
| Halaman | 3: pengesahan + hierarki aktor; struktur + dokumen; perencanaan + monev | 4: kompetensi + pengesahan (rujukan) + hierarki; PKG-04; PKG-10; PKG-14 + monev. Satu halaman per PKG agar tiap PKG terbaca sendiri |
| Pengesahan | Didefinisikan (UC-01–07) | **Dipakai ulang**, digambar sebagai package rujukan abu-abu putus-putus |
| Aktor | Pengguna Lab, *Pengelola Lab*, KaLab, Laboran, Penjadwal | *Pengelola Lab*, KaLab, Laboran. Tanpa Pengguna Lab dan Penjadwal |
| Pemecahan dari state machine | Tidak ada *use case* yang dipecah karena status menunggu | Evaluasi ulang dipecah dua karena status *Terbuka* (S2) |
| *Use case* dengan pembuatan rekaman otomatis | UC-05 (tanggal tinjau) | UC-SDM-06 (Personel), 12 dan 19 (Bukti Kompetensi), 17 (kebutuhan dari matriks) |
| Temuan matriks CRUDL | Tidak ada | 1 (Orientasi tidak punya pembaca → KF-SDM-42 diperjelas) |
| Tata letak diagram | Package berdampingan, aktor di kiri dan kanan | Package bertumpuk dalam satu kolom, aktor di kiri, catatan di kanan. Garis aktor tidak melintasi package lain |

---

## 9. Temuan, isu terbuka, dan perubahan dokumen lain

### 9.1 Temuan untuk langkah 7 (expanded use case)

**Kandidat use case kunci** (alur lengkap dan SSD di langkah 8). Dipilih karena punya aturan bisnis, membuat rekaman otomatis, atau menghitung status:

| UC | Alasan |
|---|---|
| UC-SDM-06 Catat Hasil Seleksi Asisten | Pengecualian wajib alasan dan penyetuju; Personel dibuat bila belum ada |
| UC-SDM-07 Susun Surat Tugas | Baris asisten → kelas, laboran → ruang; kelengkapan saat diajukan (KF-SDM-11, KB-3) |
| UC-SDM-12 Catat Asesmen Keterampilan | *Layak* → Bukti Kompetensi otomatis |
| UC-SDM-13 Susun Otorisasi | Supervisor wajib dan harus berotorisasi mandiri bila *terbimbing*; masa berlaku awal dari master |
| UC-SDM-15 Putuskan Evaluasi Ulang Otorisasi | Empat varian keputusan dan tindak lanjutnya |
| UC-SDM-17 Susun Rencana Pelatihan | Kebutuhan diisi dari matriks; pembekuan saat diajukan |
| UC-SDM-19 Catat Evaluasi Efektivitas Pelatihan | *Efektif* → Bukti Kompetensi otomatis |
| UC-SDM-22 Lihat Status Monev SDM | Perhitungan S1–S4 PKG-04 dan PKG-10, K1–K4 PKG-14 |

UC-01 dan UC-05 Tata Kelola tidak diulang. Langkah 7 cukup mencatat **variasi per jenis dokumen SDM** (isi `_cek_kelengkapan()` untuk Surat Tugas, Otorisasi, dan Rencana Pelatihan; `_dokumen_diganti()` untuk Otorisasi).

**Kandidat aturan bisnis (AB-SDM):**
- Dari KF *hidden*: KF-SDM-08, 11, 23, 24, 32, 37, 43.
- Dari langkah 5: `berlaku_sampai ≥ hari ini` saat otorisasi diajukan; catat realisasi hanya bila rencana disahkan.
- Dari matriks CRUDL: rekaman bukti tidak dihapus; master hanya dihapus bila belum dipakai; evaluasi ulang hanya diputuskan saat *Terbuka*.

### 9.2 [KONFIRMASI]

| No | Pertanyaan | Ke siapa | *Default* yang dipakai |
|---|---|---|---|
| KP-1 | Tambah keputusan **tetap berlaku** pada evaluasi ulang otorisasi? | Zahir | Ya (varian UC-SDM-15) |
| KB-1 | Penyebut PKG-10 = pelaksana yang ditetapkan KaLab per tugas/alat? | Zahir | Ya (UC-SDM-11) |
| KB-3 | Surat Tugas ditolak saat diajukan bila ada asisten tanpa seleksi lulus? | Zahir; KaLab | Ya (UC-01 TK untuk Surat Tugas) |
| **KU-1** | Apakah pemicu dan keputusan evaluasi ulang biasanya di hari yang berbeda? Bila selalu sehari, UC-SDM-14 dan 15 bisa digabung | KaLab (wawancara no. 16–18) | Dipecah dua |
| **KU-2** | Revisi Rencana Pelatihan setelah disahkan tidak dirancang; pelatihan pengganti masuk rencana tahun berikutnya. Setuju? | Zahir | Tidak dirancang |
| **KU-3** | Laporan bukti (UC-SDM-22) memuat rekaman pendukung orientasi dan pembatasan akses? | Zahir | Ya |
| **KU-4** | Nomor UC-01–06 Tata Kelola dirujuk langsung. Febriyan perlu tahu bahwa SDM bergantung pada nomor dan *hook*-nya | Febriyan | Dirujuk apa adanya |
| Lama | K7 (pengesah Surat Tugas), K10 (pengesah Rencana Pelatihan), KB-2 (kebutuhan laboran per kelas) | KaLab | — |
| Visual | Tampilan diagram belum dicek di draw.io **[VALIDASI]** | Zahir | — |

### 9.3 Dokumen lain yang perlu ikut berubah

| Dokumen | Perubahan |
|---|---|
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-08 | Aktor "KaLab" → "KaLab, Laboran" |
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-42 | Laporan bukti juga memuat rekaman pendukung (orientasi, pembatasan akses) (KU-3) |
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-25 | Tambah keputusan *tetap berlaku* (KP-1; sudah dicatat di langkah 5) |
| [proses-bisnis-sdm.md](proses-bisnis-sdm.md) A2 + [activity-state-sdm.drawio](activity-state-sdm.drawio) | Pecah "Catat evaluasi ulang otorisasi" menjadi *Catat pemicu evaluasi ulang* → ⧗ → *Putuskan evaluasi ulang* (bila KU-1 disetujui) |
| [proses-bisnis-sdm.md](proses-bisnis-sdm.md) S3 catatan 5 | "Revisi rencana" → "rencana tahun berikutnya" (KU-2) |
| [proses-bisnis-sdm.md](proses-bisnis-sdm.md) bagian 6.5 | Tandai bahwa Kebutuhan Petugas akhirnya bukan «CRUDL» |
| [brief-sdm.md](../brief/brief-sdm.md) paragraf aktor | Hapus Penjadwal (tertunda sejak langkah 4) |
| `tools/drawio/contoh-tata-kelola/*.py` di `main` dan branch ini (file bersama) | Masih versi lama (`rancangan-tatkel-v1`): aktor Dekan/Pemeriksa, UC lama. Versi sweet spot hanya ada di `febriyan-skripsi`. Disampaikan ke Febriyan agar disinkronkan; **tidak diubah** di sini |
| Use case Tata Kelola (Febriyan) | Tidak perlu diubah. Febriyan cukup diberi tahu bahwa UC-01 dan UC-05 dipakai untuk jenis dokumen SDM (KU-4) |

### 9.4 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| Langkah 5, A2 | Tugas "Catat evaluasi ulang otorisasi" menggabungkan dua event S2 yang dipisah status menunggu. Activity dan state machine saya sendiri tidak konsisten | 7.3 dan 9.3 |
| Langkah 5, S3 catatan 5 | Merujuk revisi Rencana Pelatihan, fitur yang tidak ada di KF maupun cakupan brief | KU-2 |
| Langkah 4, KF-SDM-42 | Orientasi (KF-SDM-16) dibuat tanpa pembaca; bukti dukung 7 PKG-04 tidak sampai ke penilai | Bagian 6 catatan 4 |
| Langkah 5, skrip `sdm/activity_state.py` | Docstring menyebut fungsi gambar disalin dari `contoh-tata-kelola/activity_state.py` tanpa menyebut versi. Di branch ini file itu versi lama (`rancangan-tatkel-v1`), bukan versi sweet spot di `febriyan-skripsi`. Konvensi hasilnya sama dan lolos validasi, tetapi asal salinannya tidak tertelusur | Skrip use case kali ini menyebut versinya; docstring skrip activity perlu diperjelas |
