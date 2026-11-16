# Expanded Use Case dan Aturan Bisnis Modul Pelaksanaan Praktikum

16 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Langkah 7 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Bahan kerja**, bukan diagram. Dipakai untuk SSD (langkah 8), conceptual model (langkah 9), pemetaan aturan ke mekanisme Odoo (langkah 10), dan Rencana Pengujian Bab II 2.4.

Sumber: [use-case-praktikum.md](use-case-praktikum.md) (UC-PRK-01–28), [kebutuhan-praktikum.md](kebutuhan-praktikum.md) (KF *hidden* dan KNF), [proses-bisnis-praktikum.md](proses-bisnis-praktikum.md) (S1–S3), analisis PKG-15–20 (aturan "memenuhi"), [kontrak-core.md](kontrak-core.md) (Sesi, `approval.mixin`, `criteria.mixin`).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Alur utama = urutan transaksi aktor → sistem, lurus, tanpa *if* atau perulangan | §6.2, §6.4 | Bagian 4 |
| Varian (V) = cara lain mencapai tujuan; eksepsi (E) = hambatan. Setiap alternatif berakhir jelas: berhasil, gagal, atau kembali ke langkah *n* | §6.3.2–6.3.3 | Bagian 4 |
| Setiap aturan bisnis biasanya melahirkan satu eksepsi | §6.3.3 | Eksepsi merujuk kode AB-PRK |
| *Essential*: tanpa tombol, layar, atau menu; identifikasi dan pemilihan ditulis generik ("memilih sesi") | §6.4.1, §6.4.3 | Semua alur |
| Data yang dipertukarkan disebut eksplisit | §6.4.2 | Semua langkah aktor dan sistem |
| Hanya langkah wajib (*system event* dan *system return*); proses internal tidak ditulis | §6.4.4 | Perubahan status dan hitungan ditulis sebagai akibat langkah sistem |
| Prakondisi = fakta yang benar sebelum mulai; yang baru diketahui di tengah alur = eksepsi | §6.6.2 | Bagian 3 |
| Use case berpola («CRUDL», «report») cukup satu pola bersama | §6.7 | Bagian 5 |

---

## 2. Katalog aturan bisnis

Kode AB-PRK dipakai oleh eksepsi di bagian 3–5. **Lapis**: W = Inti, O = Pelengkap (berlaku hanya bila KF Pelengkapnya dibangun). Pemetaan ke mekanisme Odoo dilakukan di langkah 10. Aturan pengesahan jadwal memakai AB-01–09 milik Tata Kelola (`labfik.approval.mixin`); tidak ditulis ulang.

### 2.1 Jadwal dan Sesi (PKG-15)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-01 | **Tidak boleh bentrok:** dua Sesi berstatus `terjadwal` bermoda **luring**, atau Sesi seperti itu dan pemakaian lab berstatus Disetujui, tidak boleh memakai ruang yang sama pada waktu yang tumpang tindih. Sesi daring tidak memakai ruang (diperjelas saat audit 16 Nov 2026) | PKG-15 C2; KF-PRK-04 | UC-PRK-03, 07, 08, 15 | W |
| AB-PRK-02 | **Satu Sesi asli per (kelas, pertemuan ke-).** Setiap kelas dibangkitkan 16 pertemuan dari pola mingguan; pertemuan 8 berjenis UTS, 16 berjenis UAS, sisanya praktikum | Kontrak Core C-9; keterangan Herrens 14 Nov 2026 | UC-PRK-03 | W |
| AB-PRK-03 | **Kapasitas:** bila jumlah mahasiswa kelas > kapasitas ruang, sistem memperingatkan; Sesi tetap tersimpan tetapi tidak memenuhi C3 | PKG-15 C3; KF-PRK-05 | UC-PRK-03, 26 | W |
| AB-PRK-04 | **Impor jadwal** suatu periode (termasuk kelas baru) hanya dapat dilakukan selama periode itu **tidak** punya Penetapan Jadwal berstatus Diajukan atau Disahkan; Sesi kelas yang sudah punya jurnal tidak diganti. Di luar itu, perubahan hanya lewat Perubahan Sesi. Dengan begitu setiap Sesi asli yang terbaca terpublikasi pasti tercantum di jadwal yang ditandatangani (diperketat saat audit 16 Nov 2026) | Kontrak Core C-9 (aturan pakai bersama); S1 *hapus*; PKG-15 C1; AB-01 Tata Kelola (isi dokumen hanya berubah saat Draf) | UC-PRK-03 | W |
| AB-PRK-05 | **Satu Penetapan Jadwal aktif per periode:** paling banyak satu yang berstatus Draf, Diajukan, atau Disahkan; yang Dicabut tidak dihitung, sehingga jadwal yang dicabut dapat disusun ulang (diperjelas saat audit 16 Nov 2026). Dapat diajukan hanya bila setiap kelas periode itu punya Sesi. Pengesahan memakai wewenang (`mengesahkan`, `jadwal_praktikum`) dan berkas bertanda tangan (AB-04, AB-05 Tata Kelola) | PKG-15 C1; kontrak Core I-4; KF-PRK-45 | UC-PRK-04 + UC-01–06 Tata Kelola | W |
| AB-PRK-06 | `is_terpublikasi` Sesi = Penetapan Jadwal periodenya berstatus Disahkan; **tanggal publikasi** = tanggal sah. Bila jadwal dicabut, Sesi terbaca belum terpublikasi | PKG-15 C1, bukti 4; KF-PRK-06, 45 | (hitung) | W |

### 2.2 Versi Modul (PKG-15, dipakai 16, 17, 19)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-07 | **Satu versi berlaku** per MK per periode. Saat versi baru diterbitkan, versi berlaku sebelumnya menjadi Diganti | PKG-15 C4; ISO 7.2.1.3; KF-PRK-13 | UC-PRK-05 | W |
| AB-PRK-08 | Versi modul hanya dapat diterbitkan bila ada **berkas atau tautan LeADS** dan **nomor versi** yang unik dalam MK dan periode itu. Rubrik tidak wajib saat terbit, tetapi tanpa rubrik PKG-19 P2 tidak lolos | PKG-15 C4; PKG-19 P2 | UC-PRK-05 | W |
| AB-PRK-09 | Dosen hanya dapat menerbitkan modul untuk **MK yang diampunya** (tercatat sebagai dosen koordinator atau dosen kelas pada salah satu kelas MK itu di periode tersebut) | KNF-PRK-02 | UC-PRK-05 | W |

### 2.3 Pengajuan (pemakaian lab, perubahan sesi)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-10 | Pengajuan diputuskan oleh pemegang wewenang (`mengesahkan`, `pemakaian_lab` / `perubahan_sesi`), yaitu **KaLab**. Penolakan wajib disertai **alasan** | Keputusan 14 Nov 2026; kontrak Core I-4; S2 | UC-PRK-08, 15 | W |
| AB-PRK-11 | Pengajuan hanya dapat **ditarik** oleh pengaju (atau laboran yang mencatatnya) selama berstatus Diajukan | S2 *tarik kembali*; KF-PRK-47 | UC-PRK-09 | O |
| AB-PRK-12 | **Perubahan Sesi** hanya untuk Sesi `terjadwal`. Jenis: pindah jadwal atau ruang (wajib usulan tanggal, jam, ruang pengganti), daring, batal. Pengganti dibangkitkan dengan `sesi_asal_id` dan harus memenuhi AB-PRK-01 | PKG-18 bukti 6–7; S1 | UC-PRK-14, 15 | W |

### 2.4 Kesiapan (PKG-16, 17)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-13 | **Satu Pemeriksaan Kesiapan per Sesi**, untuk Sesi yang terpublikasi. Pemeriksaan yang waktu periksanya ≥ jam mulai Sesi tetap tersimpan tetapi tidak memenuhi S1 | PKG-16 S1 | UC-PRK-11 | W |
| AB-PRK-14 | Butir *software* dan bahan dibentuk dari **Versi Modul berlaku** pada tanggal Sesi; butir kategori tetap (PC, jaringan, listrik, proyektor) selalu ada. *Software* berbayar wajib bertanda **lisensi sah** agar butirnya berhasil baik. Data master Alat (Core C-10) di ruang Sesi **hanya dibaca** lewat `check_ketersediaan_sesi()`: menjadi peringatan dan isian awal, bukan hasil butir; hasil tetap ditetapkan laboran, dan Praktikum tidak mengubah status alat (kontrak Core I-13). Bagian Alat ini lapis Pelengkap (KF-PRK-52) | PKG-16 S2–S3; PKG-17 B1 | UC-PRK-11 | W (bagian Alat: O) |
| AB-PRK-15 | Keputusan **siap** hanya bila tidak ada butir *bermasalah*; butir yang sudah diperbaiki sebelum sesi menghasilkan *siap setelah perbaikan*; selain itu keputusan **tunda** | PKG-16 S4 | UC-PRK-11 | W |
| AB-PRK-16 | **Substitusi bahan** wajib mencatat bahan pengganti dan alasan, dan baru sah setelah **disetujui dosen kelas** Sesi itu | PKG-17 B3 | UC-PRK-11, 12 | W |

### 2.5 Pelaksanaan Sesi (PKG-18)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-17 | Jurnal hanya untuk Sesi `terjadwal` yang **terpublikasi** dan tanggalnya ≤ hari ini. **Satu jurnal terkirim per Sesi** | PKG-18 C1; S1; studi dokumen A17 (laporan ganda) | UC-PRK-13 | W |
| AB-PRK-18 | Jam selesai aktual **>** jam mulai aktual | PKG-18 C3; studi dokumen A17 (durasi tidak valid) | UC-PRK-13 | W |
| AB-PRK-19 | Jurnal hanya dapat dikirim bila ada **presensi dosen dan laboran**, **jumlah praktikan hadir**, **Versi Modul** yang dipakai, dan minimal **satu entri *log book***. Presensi asisten wajib bila Sesi berasisten | PKG-18 C4–C5 | UC-PRK-13 | W |
| AB-PRK-20 | Presensi petugas merujuk `hr.employee`. Petugas hadir yang tidak ada di penugasan SDM, atau ditugaskan tetapi tidak hadir, hanya **ditandai** (tidak menolak jurnal) | Kontrak Core I-7, I-8; KF-PRK-51 | UC-PRK-13 | O |
| AB-PRK-21 | Jurnal **terlambat** bila dikirim lebih dari batas hari (pengaturan) setelah tanggal Sesi; hanya penanda | ISO 7.5.1; KF-PRK-30 | UC-PRK-13 | O |
| AB-PRK-22 | **Memenuhi PKG-18:** durasi aktual ≥ ambang (pengaturan) × durasi rencana; sesi daring hanya sah bila pengaturan mengizinkan; Sesi `batal` dengan pengganti dihitung memenuhi bila pengganti terlaksana sebelum **tanggal selesai periode** | PKG-18 C2–C3, catatan sesi tertunda | UC-PRK-26 | W |

### 2.6 Penilaian Individual (PKG-19)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-23 | **Satu Penilaian Kelas per kelas per periode**, dengan **tautan LeADS** wajib | PKG-19 (keputusan 14 Nov 2026) | UC-PRK-17 | W |
| AB-PRK-24 | Baris nilai hasil impor hanya memuat **NIM tanpa nama**; NIM unik dalam satu kelas. Impor ulang mengganti seluruh baris kelas itu; berkas lama tetap tersimpan sebagai riwayat | KNF-PRK-03; CLAUDE.md bagian 3 | UC-PRK-18 | O |
| AB-PRK-25 | **Praktikan lengkap** = P1 (tugas individual ≥ 1) ∧ P2 (modul MK punya rubrik) ∧ P3 (ada umpan balik) ∧ P4 (bila nilai akhir < batas lulus, sudah diremediasi). Batas lulus = pengaturan (awal 60) | PKG-19 P1–P4 | UC-PRK-26 | O (hanya bila diimpor) |

### 2.7 Kepuasan Pengguna (PKG-20)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-26 | Survei hanya dapat **ditetapkan** bila: keenam aspek (alat, bahan, layanan, keselamatan, akses, pengalaman belajar) masing-masing punya ≥ 1 butir skala; ada ≥ 1 butir terbuka; populasi > 0; target *response rate* terisi; tanggal buka > tanggal penetapan; tanggal tutup > tanggal buka; penetap berwenang (`mengesahkan`, `survei_kepuasan`) | PKG-20 K1–K2; kontrak Core I-4 | UC-PRK-20 | W |
| AB-PRK-27 | Penetapan hanya dapat **dibatalkan** sebelum tanggal buka | S3 | UC-PRK-21 | O |
| AB-PRK-28 | Respons **anonim** dan hanya diterima selama survei **dibuka** (antara tanggal buka dan tutup) | KNF-PRK-04; S3 | UC-PRK-22 | W |
| AB-PRK-29 | **Evaluasi** hanya dicatat setelah tanggal tutup; satu evaluasi per survei; setiap RTL wajib aspek, tindakan, PIC (`hr.employee`), dan tenggat | PKG-20 K3–K4 | UC-PRK-23 | W |
| AB-PRK-30 | **Efektivitas** RTL hanya dinilai bila survei periode berikutnya sudah dievaluasi; sistem menampilkan rerata aspek RTL itu pada kedua periode sebagai dasar | PKG-20 K4 | UC-PRK-24 | W |

### 2.8 Umum dan status monev

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-PRK-31 | **Rekaman bukti** (Pemeriksaan Kesiapan, Jurnal Sesi terkirim, Penilaian Kelas, Evaluasi Survei) tidak dapat dihapus; hanya dikoreksi, dan setiap koreksi terlacak. **Master** (Mata Kuliah, Kelas) hanya dapat dihapus bila belum dirujuk Sesi | KNF-PRK-07; matriks CRUDL | Semua | W |
| AB-PRK-32 | **Persentase PKG-15, 16, 17, 18** per periode = unit memenuhi ÷ unit pembagi, dengan pembagi dan cek dari analisis PKG (15: Sesi rencana, C1–C4; 16: Sesi terlaksana, S1–S4; 17: Sesi berbahan, B1–B3, N/A bila nol; 18: Sesi rencana, C1–C5 + AB-PRK-22). Ditampilkan beserta daftar unit tidak memenuhi dan cek yang gagal | Analisis PKG-15–18; KF-PRK-39 | UC-PRK-26 | W |
| AB-PRK-33 | **PKG-19:** persentase kelas berbukti = kelas dengan tautan LeADS dan rubrik ÷ seluruh kelas periode; bila ada impor, juga persentase praktikan lengkap (AB-PRK-25). Skor tanpa impor ditetapkan penilai | Analisis PKG-19; KF-PRK-40 | UC-PRK-26 | W |
| AB-PRK-34 | **PKG-20:** kriteria tertinggi K1–K4 dihitung `labfik.criteria.mixin` (`kriteria_tertinggi`, `get_kriteria(tanggal_acuan)`): K1 survei ditetapkan; K2 lolos AB-PRK-26; K3 ada respons, *response rate* terhitung, evaluasi tercatat; K4 setiap RTL dinilai efektivitasnya. Skor akhir ditetapkan penilai | Analisis PKG-20; KF-PRK-41 | UC-PRK-26 | W |

---

## 3. Tabel deskripsi use case

Semua use case selain «CRUDL» dan «report». Tanda ★ = alurnya dirinci di bagian 4. Prakondisi umum: aktor sudah teridentifikasi dan memegang grup akses yang sesuai.

| UC | Tujuan | Aktor | Prakondisi | Pascakondisi sukses | Eksepsi |
|---|---|---|---|---|---|
| UC-PRK-03 ★ Impor Jadwal Kelas | Membangkitkan Sesi bertanggal semua kelas satu periode dari berkas jadwal fakultas | Laboran | Periode, Ruang Lab, dan Personel dosen terdaftar | Mata Kuliah dan Kelas yang belum ada tercatat; 16 Sesi `terjadwal` per kelas; peringatan kapasitas tercatat | AB-PRK-01, 02, 03, 04 |
| UC-PRK-04 Susun Penetapan Jadwal | Menyiapkan dokumen jadwal periode untuk disahkan | Laboran | Ada Sesi untuk periode itu | Penetapan Jadwal berstatus Draf dengan daftar Sesi; selanjutnya diajukan dan disahkan lewat use case Tata Kelola | AB-PRK-05 (sudah ada penetapan aktif untuk periode itu) |
| UC-PRK-05 Terbitkan Versi Modul | Menyediakan modul berlaku sebelum sesi | Dosen | Dosen mengampu MK itu di periode tersebut | Versi baru berlaku; versi lama Diganti | AB-PRK-07, 08, 09 |
| UC-PRK-06 Baca Modul Berlaku | Membaca modul yang berlaku untuk MK yang diampu atau diasistensi | Petugas Praktikum | — | Tidak ada perubahan data | — |
| UC-PRK-07 Ajukan Pemakaian Lab | Mencatat permintaan pemakaian ruang di luar praktikum | Laboran | — | Pengajuan berstatus Diajukan; KaLab diberi tahu (O) | AB-PRK-01 |
| UC-PRK-08 Putuskan Pemakaian Lab | Menyetujui atau menolak pemakaian ruang | KaLab | Ada pengajuan Diajukan | Pengajuan Disetujui (masuk jadwal terpadu) atau Ditolak dengan alasan | AB-PRK-01, 10 |
| UC-PRK-09 Tarik Pengajuan (O) | Membatalkan pengajuan sebelum diputuskan | Petugas Praktikum | Ada pengajuan Diajukan oleh aktor | Pengajuan Ditarik | AB-PRK-11 |
| UC-PRK-11 ★ Periksa Kesiapan Sesi | Menyatakan alat, *software*, utilitas, dan bahan siap sebelum sesi | Laboran | Ada Sesi terpublikasi hari itu | Pemeriksaan tercatat dengan butir dan keputusan; bila tunda, laboran melanjutkan ke UC-PRK-14 | AB-PRK-13, 14, 15, 16 |
| UC-PRK-12 Setujui Substitusi Bahan | Mengesahkan bahan pengganti | Dosen | Ada butir bahan bersubstitusi pada kelas yang diampu | Substitusi disetujui; butir bahan dapat berhasil baik | AB-PRK-16 |
| UC-PRK-13 ★ Kirim Jurnal Sesi | Merekam pelaksanaan sesi | Petugas Praktikum | Ada Sesi terpublikasi yang sudah berlangsung | Jurnal terkirim; Sesi `terlaksana`; penanda terlambat dan ketidaksesuaian penugasan (O) tercatat | AB-PRK-17, 18, 19, 20, 21 |
| UC-PRK-14 Ajukan Perubahan Sesi | Meminta sesi dipindah, dijadikan daring, atau dibatalkan | Petugas Praktikum | Ada Sesi `terjadwal` | Perubahan Diajukan; Sesi terbaca ditunda; KaLab diberi tahu (O) | AB-PRK-12 |
| UC-PRK-15 ★ Putuskan Perubahan Sesi | Memutuskan perubahan dan membangkitkan pengganti | KaLab | Ada Perubahan Diajukan | Perubahan Disetujui atau Ditolak; bila disetujui: Sesi asal `batal` (+ Sesi pengganti) atau moda daring | AB-PRK-01, 10, 12 |
| UC-PRK-17 Catat Penilaian Kelas | Menautkan bukti penilaian individual kelas | Dosen, Laboran | Kelas terdaftar | Penilaian Kelas tercatat dengan tautan LeADS | AB-PRK-23 |
| UC-PRK-18 Impor Nilai Kelas (O) | Mengimpor nilai per praktikan dari ekspor Excel LeADS | Dosen, Laboran | Ada Penilaian Kelas | Baris nilai per NIM tercatat; status lengkap P1–P4 terhitung | AB-PRK-24 |
| UC-PRK-19 Susun Survei Kepuasan | Menyusun survei periode | KaLab | Periode terdaftar | Survei Draf dengan butir beraspek | — |
| UC-PRK-20 Tetapkan Survei Kepuasan | Menetapkan survei sebelum dibuka | KaLab | Ada survei Draf | Survei Ditetapkan; tautan isi tersedia | AB-PRK-26 |
| UC-PRK-21 Batalkan Penetapan Survei (O) | Mengembalikan survei ke Draf | KaLab | Survei Ditetapkan, belum dibuka | Survei Draf | AB-PRK-27 |
| UC-PRK-22 Isi Survei Kepuasan | Memberi penilaian kepuasan | Responden | Survei sedang dibuka | Respons anonim tercatat | AB-PRK-28 |
| UC-PRK-23 ★ Catat Evaluasi Survei | Menganalisis hasil dan menetapkan tindak lanjut | KaLab | Survei Ditetapkan, tanggal tutup lewat | Evaluasi dan RTL tercatat; survei Dievaluasi; K1–K3 terhitung | AB-PRK-29 |
| UC-PRK-24 Nilai Efektivitas Tindak Lanjut | Menilai apakah RTL memperbaiki aspek | KaLab | Survei Dievaluasi dan survei periode berikutnya Dievaluasi | Setiap RTL punya penilaian efektivitas; siklus selesai; K4 terhitung | AB-PRK-30 |
| UC-PRK-27 Terbitkan Laporan Bukti | Menghasilkan laporan resmi per indikator untuk penilai | KaLab | — | Laporan bukti periode tersedia; tidak ada perubahan data | — |

---

## 4. Alur lengkap use case kunci

Dipilih karena mengubah status, membangkitkan data, atau memuat banyak aturan. Menjadi dasar SSD di langkah 8.

### UC-PRK-03 Impor Jadwal Kelas

**Alur utama**
1. Laboran menyerahkan periode dan berkas jadwal kelas (per baris: kode MK, nama MK, prodi, kelas, hari, jam mulai, jam selesai, ruang, dosen, jumlah mahasiswa) beserta tanggal pertemuan pertama. [V1]
2. Sistem menampilkan pratinjau per kelas: MK, kelas, pola mingguan, ruang, 16 tanggal pertemuan (8 = UTS, 16 = UAS), dan peringatan kapasitas. [E1, E2, E3]
3. Laboran mengonfirmasi impor.
4. Sistem menampilkan ringkasan: jumlah Mata Kuliah dan Kelas baru, jumlah Sesi `terjadwal` yang dibangkitkan, dan daftar kelas yang melebihi kapasitas.

**Varian**
- **V1 Tanpa berkas (jalan pengganti).** V1.1 Laboran menyerahkan satu kelas beserta pola mingguannya (hari, jam mulai, jam selesai, ruang) dan tanggal pertemuan pertama. V1.2 Kembali ke langkah 2.

**Eksepsi**
- **E1 Bentrok ruang (AB-PRK-01).** E1.1 Sistem menampilkan pasangan yang bentrok (kelas, tanggal, jam, ruang); karena Sesinya tidak dibangkitkan, bentrok ini tidak tersimpan sebagai rekaman konflik **[ASUMSI; KONFIRMASI pembimbing]**. E1.2 Use case gagal untuk kelas yang bentrok; laboran menyampaikan bentrok ke fakultas (di luar sistem).
- **E2 Jadwal periode sudah diajukan atau disahkan, atau Sesi kelas sudah punya jurnal (AB-PRK-04).** E2.1 Sistem menampilkan kelas yang terkunci. E2.2 Kelas itu dilewati; perubahan Sesi yang ada lewat UC-PRK-14. Kelas baru setelah jadwal disahkan menunggu jadwal dicabut lalu disusun ulang (UC-06 Tata Kelola, UC-PRK-04).
- **E3 Baris tidak valid** (ruang atau dosen tidak dikenal, jam selesai ≤ jam mulai). E3.1 Sistem menampilkan baris dan kolom bermasalah. E3.2 Kembali ke langkah 1.

Catatan: peringatan kapasitas (AB-PRK-03) tidak menggagalkan impor.

### UC-PRK-11 Periksa Kesiapan Sesi

**Alur utama**
1. Laboran meminta daftar Sesi hari ini.
2. Sistem menampilkan daftar Sesi terpublikasi hari ini: MK, kelas, jam mulai, ruang, dan ada tidaknya pemeriksaan.
3. Laboran memilih satu Sesi.
4. Sistem menampilkan butir pemeriksaan: kategori tetap (PC/stasiun kerja, jaringan, listrik, proyektor/audio), *software* dan bahan dari Versi Modul berlaku (nama, versi atau jumlah dibutuhkan), serta jumlah mahasiswa kelas. Bila master Alat ruang sudah terisi (O, KF-PRK-52), butir kategori juga menampilkan alat yang tidak tersedia (perbaikan / dipinjam / afkir) dan jumlah PC tersedia sebagai isian awal jumlah stasiun kerja berfungsi. [E1]
5. Laboran menyerahkan hasil setiap butir (baik / diperbaiki sebelum sesi / bermasalah, keterangan), jumlah stasiun kerja berfungsi, tanda lisensi sah untuk *software* berbayar, dan untuk bahan: jumlah tersedia, kondisi, berlabel. [V1]
6. Sistem menampilkan keputusan yang dapat dipilih sesuai hasil butir. 
7. Laboran menyerahkan keputusan (siap / siap setelah perbaikan / tunda). [E2, E3]
8. Sistem menampilkan pemeriksaan tercatat dengan waktu periksa dan keputusan. [E4]

**Varian**
- **V1 Substitusi bahan.** V1.1 Laboran menyerahkan bahan pengganti dan alasannya pada butir bahan. V1.2 Sistem menampilkan butir menunggu persetujuan dosen (UC-PRK-12). V1.3 Kembali ke langkah 5.

**Eksepsi**
- **E1 Sesi sudah punya pemeriksaan (AB-PRK-13).** E1.1 Sistem menampilkan pemeriksaan yang ada. E1.2 Laboran mengoreksinya; kembali ke langkah 5.
- **E2 Ada butir *bermasalah* tetapi keputusan *siap* (AB-PRK-15).** E2.1 Sistem menampilkan butir bermasalah. E2.2 Kembali ke langkah 7.
- **E3 Substitusi bahan belum disetujui tetapi keputusan *siap* (AB-PRK-16).** E3.1 Sistem menampilkan butir yang menunggu. E3.2 Kembali ke langkah 7.
- **E4 Waktu periksa ≥ jam mulai Sesi (AB-PRK-13).** E4.1 Sistem menampilkan bahwa pemeriksaan tercatat terlambat. E4.2 Use case berhasil, tetapi Sesi tidak memenuhi PKG-16 S1.

Catatan: bila keputusan *tunda*, laboran melanjutkan dengan UC-PRK-14 (use case terpisah).

### UC-PRK-13 Kirim Jurnal Sesi

**Alur utama**
1. Petugas Praktikum meminta daftar Sesi kelasnya yang sudah berlangsung dan belum punya jurnal terkirim.
2. Sistem menampilkan daftar Sesi: MK, kelas, pertemuan ke-, jenis pertemuan, tanggal, jam rencana, ruang, moda, dan penanda terlewat.
3. Petugas Praktikum memilih satu Sesi.
4. Sistem menampilkan identitas Sesi, Versi Modul berlaku, petugas yang ditugaskan (dari SDM, bila ada), dan jumlah mahasiswa kelas. [E1]
5. Petugas Praktikum menyerahkan jam mulai dan selesai aktual, topik, Versi Modul yang dipakai, jumlah praktikan hadir, tautan presensi SIMPEL (opsional), kendala, foto, presensi petugas (personel, peran, kehadiran penuh / sebagian / tidak), dan entri *log book* (waktu, uraian). [V1]
6. Sistem menampilkan jurnal lengkap beserta penanda petugas yang tidak sesuai penugasan (O). [E2]
7. Petugas Praktikum mengirim jurnal.
8. Sistem menampilkan jurnal terkirim, waktu kirim, Sesi berstatus `terlaksana`, dan penanda terlambat bila ada (O). [E3]

**Varian**
- **V1 Simpan sebagai draf.** V1.1 Petugas Praktikum menyimpan isian. V1.2 Sistem menampilkan jurnal berstatus draf. V1.3 Use case berhasil; dapat dilanjutkan kemudian dari langkah 5.

**Eksepsi**
- **E1 Sesi tidak `terjadwal` (mis. batal), belum terpublikasi, belum berlangsung, atau sudah punya jurnal terkirim (AB-PRK-17).** E1.1 Sistem menampilkan alasannya. E1.2 Use case gagal.
- **E2 Jam selesai ≤ jam mulai (AB-PRK-18).** E2.1 Sistem menampilkan jam yang bermasalah. E2.2 Kembali ke langkah 5.
- **E3 Isian wajib belum lengkap (AB-PRK-19):** presensi dosen atau laboran, jumlah hadir, Versi Modul, *log book*, atau presensi asisten pada Sesi berasisten. E3.1 Sistem menampilkan bagian yang kurang. E3.2 Kembali ke langkah 5.

### UC-PRK-15 Putuskan Perubahan Sesi

**Alur utama**
1. KaLab meminta daftar Perubahan Sesi yang Diajukan.
2. Sistem menampilkan daftar: Sesi asal (MK, kelas, pertemuan, tanggal, jam, ruang), jenis perubahan, alasan, pengaju, usulan pengganti.
3. KaLab memilih satu perubahan dan menyerahkan keputusan *disetujui* beserta tanggal, jam, dan ruang pengganti (boleh mengubah usulan). [V1, V2, V3]
4. Sistem menampilkan perubahan Disetujui, Sesi asal berstatus `batal`, dan Sesi pengganti `terjadwal` yang merujuk Sesi asal. Pengaju diberi tahu (O). [E1, E2]

**Varian**
- **V1 Daring.** V1.1 KaLab menyerahkan keputusan *disetujui* untuk perubahan berjenis daring. V1.2 Sistem menampilkan Sesi asal tetap `terjadwal` dengan moda daring. V1.3 Use case berhasil.
- **V2 Batal tanpa pengganti.** V2.1 KaLab menyerahkan keputusan *disetujui* untuk perubahan berjenis batal. V2.2 Sistem menampilkan Sesi asal `batal` tanpa pengganti. V2.3 Use case berhasil.
- **V3 Ditolak.** V3.1 KaLab menyerahkan keputusan *ditolak* beserta alasan. V3.2 Sistem menampilkan perubahan Ditolak; Sesi asal tidak lagi terbaca ditunda. V3.3 Use case berhasil. [E3]

**Eksepsi**
- **E1 Waktu pengganti bentrok (AB-PRK-01).** E1.1 Sistem menampilkan Sesi atau pemakaian yang bentrok. E1.2 Kembali ke langkah 3.
- **E2 Sesi asal tidak lagi `terjadwal` (AB-PRK-12)**, misalnya sudah terlaksana. E2.1 Sistem menampilkan status Sesi. E2.2 Use case gagal.
- **E3 Alasan penolakan kosong (AB-PRK-10).** E3.1 Sistem menampilkan bahwa alasan wajib. E3.2 Kembali ke V3.1.

### UC-PRK-23 Catat Evaluasi Survei

**Alur utama**
1. KaLab meminta daftar survei yang sudah ditutup dan belum dievaluasi.
2. Sistem menampilkan daftar survei: periode, jenis responden, tanggal tutup.
3. KaLab memilih satu survei.
4. Sistem menampilkan rekap: populasi, jumlah responden, *response rate* dibanding target, rerata per aspek dan per butir, serta jawaban terbuka. [E1]
5. KaLab menyerahkan kesimpulan per aspek dan Rencana Tindak Lanjut (per baris: aspek, prioritas, tindakan, PIC, tenggat).
6. Sistem menampilkan evaluasi tercatat, survei berstatus Dievaluasi, dan kriteria tertinggi PKG-20 yang lengkap secara data. [E2]

**Eksepsi**
- **E1 Survei belum ditutup atau sudah dievaluasi (AB-PRK-29).** E1.1 Sistem menampilkan status dan tanggal tutup. E1.2 Use case gagal.
- **E2 Baris RTL tidak lengkap (AB-PRK-29).** E2.1 Sistem menampilkan baris yang kurang. E2.2 Kembali ke langkah 5.

---

## 5. Pola bersama «CRUDL» dan «report» (§6.7)

### 5.1 Pola «CRUDL»

**Create:** 1. Aktor menyerahkan data konsep. 2. Sistem menampilkan data yang tercatat. [E1]
**Retrieve:** 1. Aktor memilih satu rekaman. 2. Sistem menampilkan seluruh datanya beserta data terkait.
**Update:** 1. Aktor memilih satu rekaman dan menyerahkan data yang diubah. 2. Sistem menampilkan data terbaru. [E1]
**Delete:** 1. Aktor memilih satu rekaman untuk dihapus. 2. Sistem menampilkan bahwa rekaman sudah tidak ada. [E2]
**List:** 1. Aktor menyerahkan filter (opsional). 2. Sistem menampilkan daftar rekaman yang sesuai.

**Eksepsi bersama**
- **E1 Data wajib kosong, tidak valid, atau melanggar keunikan.** Sistem menampilkan field yang bermasalah; kembali ke langkah 1.
- **E2 Rekaman masih dirujuk data lain (AB-PRK-31).** Sistem menampilkan rujukannya dan menawarkan pengarsipan; use case gagal untuk penghapusan.

| UC | Konsep | Data wajib | Aturan khusus |
|---|---|---|---|
| UC-PRK-01 Kelola Mata Kuliah | Mata Kuliah | Kode (unik), nama, prodi | AB-PRK-31 |
| UC-PRK-02 Kelola Kelas | Kelas | Mata kuliah, periode, nama kelas (unik per MK dan periode), jumlah mahasiswa, dosen | AB-PRK-31 |
| UC-PRK-28 Kelola Pengaturan Praktikum | Pengaturan | Ambang durasi minimal (%), batas hari pengisian jurnal, sesi daring sah (ya/tidak), batas lulus PKG-19 | Satu rekaman; tidak dihapus |

### 5.2 Pola «report»

1. Aktor menyerahkan filter laporan. 2. Sistem menampilkan isi laporan. Laporan tidak mengubah data; bentuk keluarannya (layar atau PDF) adalah keputusan desain (§4.3.4).

| UC | Filter | Isi | Aturan |
|---|---|---|---|
| UC-PRK-10 Lihat Laporan Jadwal | Periode, ruang, minggu | Jadwal terpadu per ruang (Sesi + pemakaian disetujui); rekaman konflik (pemakaian ditolak beralasan bentrok dan Sesi yang diganti; bentrok saat impor atau pencatatan hanya ditampilkan, tidak disimpan) | AB-PRK-01 |
| UC-PRK-16 Lihat Laporan Pelaksanaan (O) | Periode, kelas, ruang | Rekap kesiapan per ruang (butir bermasalah per kategori, keputusan tunda); rekap keterlaksanaan per kelas (rencana, terlaksana, memenuhi) | AB-PRK-13–22 |
| UC-PRK-25 Lihat Laporan Survei | Survei, periode | Responden, *response rate*, rerata per aspek dan butir, jawaban terbuka, perbandingan antarperiode per aspek, RTL dan efektivitasnya | AB-PRK-29, 30 |
| UC-PRK-26 Lihat Status Monev Praktikum | Periode, tanggal acuan | PKG-15–18: persentase, skor, daftar unit tidak memenuhi dan cek yang gagal. PKG-19: kelas berbukti; per praktikan bila diimpor. PKG-20: kriteria tertinggi K1–K4 dan tautan bukti | AB-PRK-32, 33, 34 |

---

## 6. Cek silang

### 6.1 Kriteria instrumen → AB

| PKG | Kriteria | AB |
|---|---|---|
| 15 | C1 jadwal sah dan dipublikasikan | AB-PRK-05, 06 |
| 15 | C2 tanpa bentrok | AB-PRK-01 |
| 15 | C3 kapasitas | AB-PRK-03 |
| 15 | C4 modul berlaku sebelum sesi | AB-PRK-07, 08 |
| 16 | S1–S4 | AB-PRK-13, 14, 15 |
| 17 | B1–B3 | AB-PRK-14, 16 |
| 18 | C1–C5 | AB-PRK-12, 17, 18, 19, 22 |
| 19 | P1–P4 | AB-PRK-08 (rubrik), 23, 25, 33 |
| 20 | K1–K4 | AB-PRK-26, 28, 29, 30, 34 |

Setiap kriteria punya aturan bisnis yang dapat diuji.

### 6.2 AB → use case

Setiap AB-PRK dirujuk minimal satu use case (kolom UC di bagian 2). AB-PRK-06 dan perhitungan di AB-PRK-32–34 adalah perilaku hitung, dibaca oleh UC-PRK-10, 13, 26.

### 6.3 Temuan dan kesalahan di langkah sebelumnya

| Temuan | Tindakan |
|---|---|
| Impor jadwal butuh **jumlah mahasiswa** dan **dosen** per kelas, padahal berkas fakultas belum tentu memuatnya | Kolom tersebut opsional di impor; bila kosong, diisi lewat UC-PRK-02 **[KONFIRMASI P2]** |
| Batas lulus PKG-19 belum ada di pengaturan (KF-PRK-43 hanya menyebut ambang durasi, batas hari, sesi daring) | Ditambahkan ke isi UC-PRK-28; KF-PRK-43 sudah diperbarui |
| Jurnal Sesi butuh jumlah mahasiswa dan petugas yang ditugaskan untuk ditampilkan | Sudah tersedia lewat Kelas (Core) dan SDM (kontrak Core I-7) |
| UC-PRK-04 butuh syarat "setiap kelas punya Sesi" sebelum diajukan | Dicatat sebagai AB-PRK-05; mengisi *hook* kelengkapan `approval.mixin` di langkah 10 |
| **Audit 16 Nov 2026.** (a) Setelah Penetapan Jadwal dicabut (KF-PRK-45), "satu per periode" memblokir penyusunan ulang: jalan buntu. (b) Kelas baru masih bisa diimpor setelah jadwal disahkan, sehingga Sesinya terbaca terpublikasi tanpa ada di jadwal bertanda tangan (PKG-15 C1). (c) Sesi daring ikut dihitung bentrok padahal tidak memakai ruang | AB-PRK-05 menjadi "satu aktif per periode"; AB-PRK-04 mengunci impor seluruh periode selama jadwal Diajukan/Disahkan; AB-PRK-01 hanya Sesi luring. Nomor AB tidak berubah |

---

## 7. Temuan untuk langkah 8 (SSD)

| Use case kunci | Command (mengubah data) | Query (membaca) |
|---|---|---|
| UC-PRK-03 | `impor_jadwal(periode_id, berkas, tanggal_mulai)`, `konfirmasi_impor(impor_id)` | `pratinjau = pratinjau_impor(periode_id, berkas, tanggal_mulai)` |
| UC-PRK-11 | `catat_hasil_butir(pemeriksaan_id, butir[])`, `tetapkan_keputusan(pemeriksaan_id, keputusan)` | `daftar = daftar_sesi(filter)`, `pemeriksaan = mulai_pemeriksaan(sesi_id)` |
| UC-PRK-13 | `simpan_jurnal(sesi_id, isian)`, `kirim_jurnal(jurnal_id)` | `daftar = daftar_sesi(filter)`, `konteks = get_konteks_jurnal(sesi_id)` |
| UC-PRK-15 | `putuskan_perubahan(perubahan_id, keputusan, pengganti, alasan)` | `daftar = daftar_perubahan(filter)` |
| UC-PRK-23 | `catat_evaluasi(survei_id, kesimpulan, rtl[])` | `daftar = daftar_survei(filter)`, `rekap = get_rekap_survei(survei_id)` |

`daftar_sesi(filter)` dipakai bersama oleh UC-PRK-11 dan 13 (CLAUDE.md Langkah 8: satukan operasi berpola sama dengan parameter filter). `mulai_pemeriksaan` adalah command (membuat butir) dan query (mengembalikan butir) sekaligus; di SSD dipecah sesuai CQS (§7.1).

---

## 8. Isu terbuka

- [ ] Isi berkas jadwal fakultas (jumlah mahasiswa, dosen ada atau tidak) **[KONFIRMASI P2]**
- [ ] Ambang durasi minimal, batas hari pengisian jurnal, dan sesi daring sah **[KONFIRMASI P12, P13]**
- [ ] Apakah pemeriksaan kesiapan yang terlambat masih boleh dicatat (AB-PRK-13 mengizinkan dengan penanda) **[KONFIRMASI P8]**
- [x] KF-PRK-43 kini menyebut batas lulus PKG-19 (16 Nov 2026)
