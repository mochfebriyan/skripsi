# BAB I PENDAHULUAN

18 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20
**Status: DRAF.** Revisi total Bab I agar selaras dengan rancangan TO-BE (Bab II). Perubahan terhadap Bab I lama dan hal yang belum tervalidasi dicatat di [catatan-validasi-bab-i-ii.md](../../skripsi/catatan-validasi-bab-i-ii.md).

Judul usulan: Kustomisasi Modul Odoo untuk Pengelolaan Pelaksanaan Praktikum Berbasis Instrumen Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta) **[KONFIRMASI pembimbing]**

## 1.1 Latar Belakang

Laboratorium merupakan sarana utama perguruan tinggi untuk menunjang pelaksanaan tridharma, terutama pembelajaran praktik yang membentuk kompetensi mahasiswa. Mutu layanan laboratorium dijamin melalui Sistem Penjaminan Mutu Internal (SPMI), yang wajib dikembangkan setiap perguruan tinggi dan dijalankan dalam siklus penetapan, pelaksanaan, evaluasi, pengendalian, dan peningkatan standar (Kementerian Pendidikan Tinggi, Sains, dan Teknologi, 2025). Dalam siklus tersebut, evaluasi hanya dapat dilakukan bila pelaksanaan meninggalkan rekaman yang dapat diperiksa.

Mulai tahun 2026, laboratorium di lingkungan Universitas Pembangunan Nasional "Veteran" Jakarta (UPNVJ) dinilai menggunakan Instrumen Monev Laboratorium UPNVJ 2026 v1.1 (Universitas Pembangunan Nasional "Veteran" Jakarta, 2026). Instrumen ini antara lain mengacu pada SNI ISO/IEC 17025:2017 tentang persyaratan umum kompetensi laboratorium (Badan Standardisasi Nasional, 2018). Instrumen menilai 21 indikator pada aspek pengelolaan, pengembangan, persiapan, proses, dan evaluasi dengan skor 1 sampai 4 per indikator. Indikator yang buktinya tidak dapat diverifikasi diberi skor 1, walaupun kegiatannya telah dilakukan. Dengan demikian, pemenuhan indikator ditentukan oleh tersedianya bukti yang dapat ditelusuri, bukan hanya oleh terlaksananya kegiatan.

Kegiatan praktikum dinilai melalui enam indikator, yang dalam penelitian ini diberi kode PKG-15 sampai PKG-20. PKG-15 (Persiapan 15) mensyaratkan jadwal penggunaan laboratorium dan modul praktikum tersedia sebelum setiap kegiatan. PKG-16 (Persiapan 16) mensyaratkan peralatan, perangkat lunak, dan utilitas dinyatakan siap sebelum setiap sesi, sedangkan PKG-17 (Persiapan 17) mensyaratkan bahan yang sesuai bagi praktikum yang memakai bahan fisik. PKG-18 (Proses 18) mensyaratkan sesi terlaksana sesuai jadwal, modul, dan waktu yang ditetapkan. PKG-19 (Evaluasi 19) mensyaratkan kompetensi praktikan dinilai secara individual dengan rubrik, dan PKG-20 (Evaluasi 20) mensyaratkan kepuasan pengguna diukur, dianalisis, dan dipakai untuk perbaikan layanan (Universitas Pembangunan Nasional "Veteran" Jakarta, 2026).

PKG-15 sampai PKG-19 dinilai dengan persentase unit yang memenuhi seluruh kriteria. Unitnya adalah sesi untuk PKG-15 sampai PKG-18 dan praktikan untuk PKG-19. Skor 4 diberikan bila 100% unit memenuhi, skor 3 untuk 90% sampai kurang dari 100%, skor 2 untuk 70% sampai kurang dari 90%, dan skor 1 di bawah 70%. PKG-20 dinilai dengan empat kriteria berurutan, mulai dari penetapan survei sampai pembandingan efektivitas perbaikan antarperiode (Universitas Pembangunan Nasional "Veteran" Jakarta, 2026). Artinya, setiap sesi dan setiap praktikan harus memiliki buktinya sendiri, dan bukti persiapan harus bertanggal sebelum sesi dimulai. Persyaratan ini sejalan dengan SNI ISO/IEC 17025:2017, yang mewajibkan verifikasi peralatan sebelum digunakan (klausul 6.4.4), rekaman teknis yang dibuat pada saat kegiatan dilakukan (klausul 7.5.1), serta umpan balik pelanggan yang dianalisis untuk perbaikan (klausul 8.6.2) (Badan Standardisasi Nasional, 2018).

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta, yang mengelola delapan ruang praktikum **[VALIDASI KaLab]**, akan menjalani monev tersebut. Studi dokumen terhadap prosedur dan data praktikum LabFIK menunjukkan bahwa kegiatan praktikum sudah berjalan, tetapi rekamannya belum dapat dihitung per sesi. Prosedur Operasional Baku (POB) Manajemen Praktikum dan Asistensi sudah disusun, tetapi belum disahkan. Pada *sheet* alokasi pertemuan asisten, kolom hari dan jam kosong pada seluruh 222 baris kelas selama tiga periode, dan tidak ada kolom ruang maupun jumlah mahasiswa, sehingga laboratorium tidak memegang daftar sesi praktikum yang bertanggal. Pemakaian laboratorium di luar praktikum dan penyelesaian bentrok jadwal juga belum diatur dalam POB. Akibatnya, jadwal yang disahkan, pemeriksaan bentrok ruang, dan kesesuaian kapasitas yang diminta PKG-15 belum dapat dibuktikan. Kondisi ini umum terjadi: penjadwalan laboratorium yang disusun tanpa rujukan jadwal bersama baru menemukan bentrok pada rapat persiapan (Warsono & Mulyono, 2022), dan praktikum yang dikelola secara manual kerap berjalan di luar rencana serta saling tumpang tindih (Iswanto & Mulyono, 2021).

Pelaksanaan sesi dilaporkan asisten melalui Google Form "Pelaksanaan Asistensi Praktikum", dengan 1.147 laporan selama empat periode. Pelaporan ini dibuat untuk keperluan honor asisten, sehingga hanya 64–75% sesi berasisten yang terlaporkan, dan kelas tanpa asisten, yang mencapai 42–56% kelas per periode, tidak memiliki rekaman sama sekali. Laporan yang ada juga memuat laporan ganda, durasi yang tidak valid, dan pengisian yang terlambat. Modul tidak berversi dan diunggah ulang pada setiap laporan, kesiapan sarana dicatat asisten sesudah sesi tanpa keputusan tunda, dan jejak pemakaian bahan hampir tidak ada. Penilaian praktikan tersimpan di LeADS dan presensi rinci di SIMPEL, tanpa rubrik dan tanpa tautan ke sesi. Kuesioner kepuasan sudah dilampirkan pada POB, tetapi data responsnya tidak ditemukan **[KONFIRMASI KaLab]**. Pencatatan pemakaian laboratorium komputer yang manual memang cenderung lambat dan kurang akurat (Damanik et al., 2026), padahal survei kepuasan diperlukan agar laboratorium mengetahui atribut layanan yang belum memuaskan (Cahyaningrum et al., 2024). Akibatnya, skor aspek persiapan, proses, dan evaluasi berisiko rendah bukan karena kegiatannya tidak dilakukan, melainkan karena buktinya tidak tersedia per sesi dan per praktikan.

Sejumlah penelitian telah memanfaatkan sistem informasi untuk mengelola praktikum. Aji (2024) membangun sistem penjadwalan praktikum berbasis Android untuk menyampaikan jadwal dan mencegah bentrok antarmata kuliah, dosen, dan rombongan belajar. Warsono dan Mulyono (2022) merancang prototipe penjadwalan yang menyediakan rujukan jadwal lintas program studi secara *real-time*. Hidayati et al. (2025) mengembangkan M-Room berbasis Google Spreadsheet untuk pemesanan ruang laboratorium, pengecekan ketersediaan ruang, dan rekap pemakaian bulanan. Damanik et al. (2026) mengembangkan sistem informasi pemakaian laboratorium komputer yang mencakup jadwal, peminjaman, serta pelaporan kerusakan dan pemeliharaan perangkat. Aditia et al. (2023) menerapkan sistem kehadiran praktikum berbasis *QR code* untuk menggantikan kartu kontrol kertas. Wijaya et al. (2022) menurunkan kebutuhan sistem informasi manajemen laboratorium dari klausul-klausul SNI ISO/IEC 17025:2017.

Penelitian-penelitian tersebut menangani penjadwalan, kondisi perangkat, atau kehadiran secara terpisah, dan tidak dirancang untuk menghasilkan bukti penilaian mutu. Belum ditemukan penelitian yang menautkan persiapan, pelaksanaan, dan evaluasi praktikum pada unit sesi yang sama, lalu menghitung pemenuhan setiap indikator monev beserta buktinya.

Permasalahan bukti tersebut tidak hanya terjadi pada praktikum, sehingga ditangani melalui proyek bersama LabFIK Compliance, yaitu sistem berbasis Odoo 17 Community yang dikembangkan oleh beberapa penelitian. Proyek ini mencakup 21 indikator instrumen monev yang dikelompokkan ke dalam modul fungsional: tata kelola dan dokumen, sumber daya manusia dan kompetensi, pelaksanaan praktikum, aset, serta keselamatan. Seluruh modul memakai data bersama, seperti personel, periode, ruang laboratorium, dan sesi praktikum, sehingga satu fakta cukup dicatat sekali dan dapat menjadi bukti bagi lebih dari satu indikator. Sistem yang dibangun terpisah per unit cenderung menghasilkan data yang ganda dan tidak sinkron (Ulya et al., 2024). Odoo dipilih karena bersifat *open source* dan dapat dikonfigurasi serta dikustomisasi sesuai kebutuhan organisasi (Nurrohmah & Wiratama, 2023). Penerapan Odoo di LabFIK telah dicontohkan oleh Anandar (2026) pada perencanaan asisten praktikum dengan OpenEduCat. Penelitian ini tidak memakai OpenEduCat; sesi praktikum dirancang sebagai data bersama milik proyek agar modul lain cukup bergantung pada addon bawaan Odoo.

Penelitian ini menangani modul Pelaksanaan Praktikum, yang memegang PKG-15 sampai PKG-20 dan menjadi pembangkit sesi bertanggal yang juga dipakai modul lain. Pada tahap persiapan, modul membangkitkan sesi dari jadwal kelas, memeriksa bentrok ruang dan kapasitas, menetapkan jadwal yang disahkan, mencatat pengajuan pemakaian laboratorium, mengelola versi modul praktikum, serta merekam pemeriksaan kesiapan alat, perangkat lunak, utilitas, dan bahan per sesi. Pada tahap proses, modul merekam jurnal sesi yang memuat presensi petugas, jumlah praktikan hadir, modul yang dipakai, dan *log book*, serta perubahan sesi yang disetujui. Pada tahap evaluasi, modul menyimpan tautan bukti penilaian LeADS dan rubrik per kelas, serta mengelola survei kepuasan pengguna beserta evaluasi dan rencana tindak lanjutnya. Status setiap indikator dihitung dari rekaman tersebut; untuk PKG-20, sistem hanya menunjukkan kriteria tertinggi yang datanya lengkap, sedangkan skor akhir tetap ditetapkan penilai. Sistem ini diposisikan sebagai alat pencatatan, pembuktian, dan pemantauan, dan tidak menjamin kenaikan skor monev, karena skor tetap bergantung pada terlaksananya kegiatan oleh pengelola laboratorium.

## 1.2 Identifikasi Masalah

Berdasarkan latar belakang tersebut, masalah pada persiapan, proses, dan evaluasi praktikum di LabFIK diidentifikasi sebagai berikut:

1. Laboratorium tidak memegang jadwal sesi praktikum bertanggal yang disahkan, bentrok ruang dan kesesuaian kapasitas tidak diperiksa, dan pemakaian laboratorium di luar praktikum tidak tercatat. Akibatnya, kriteria jadwal pada PKG-15 tidak dapat dibuktikan.
2. Modul praktikum tidak berversi dan tidak terbukti tersedia sebelum sesi. Akibatnya, kriteria modul berlaku pada PKG-15 tidak dapat dibuktikan.
3. Kesiapan alat, perangkat lunak, dan utilitas dicatat asisten sesudah sesi dan tanpa keputusan tunda. Akibatnya, PKG-16 tidak dapat dihitung per sesi.
4. Bahan untuk praktikum yang memakai bahan fisik tidak diperiksa sebelum sesi, dan penggantian bahan tidak tercatat. Akibatnya, PKG-17 tidak dapat dibuktikan untuk sesi yang mensyaratkannya.
5. Pelaksanaan sesi hanya dilaporkan untuk keperluan honor asisten, kelas tanpa asisten tidak terekam, dan perubahan sesi tidak tercatat persetujuannya. Akibatnya, PKG-18 tidak dapat dihitung terhadap seluruh sesi yang direncanakan.
6. Bukti penilaian individual berada di LeADS tanpa tautan ke kelas di laboratorium, dan rubrik penilaian belum ada. Akibatnya, PKG-19 tidak dapat ditelusuri.
7. Survei kepuasan pengguna belum memiliki data respons, belum mencakup seluruh aspek yang diminta instrumen, dan belum ditindaklanjuti dalam satu rangkaian. Akibatnya, kriteria berurutan PKG-20 tidak dapat dibuktikan.
8. Pemenuhan keenam indikator dihitung manual menjelang monev dan tidak tertelusur ke sesi, kelas, atau survei asalnya. Akibatnya, pemenuhan indikator tidak dapat dipantau sepanjang periode penilaian.

## 1.3 Batasan Masalah

Agar penelitian lebih terarah, ruang lingkupnya dibatasi sebagai berikut:

1. Penelitian mencakup enam indikator Instrumen Monev Laboratorium UPNVJ 2026 v1.1, yaitu PKG-15 (jadwal dan modul), PKG-16 (kesiapan alat dan perangkat lunak), PKG-17 (bahan praktikum), PKG-18 (sesi terlaksana), PKG-19 (penilaian individual), dan PKG-20 (kepuasan pengguna). PKG-17 hanya diterapkan pada sesi yang modulnya mencantumkan bahan.
2. Studi kasus dilakukan pada praktikum di Laboratorium FIK UPN "Veteran" Jakarta.
3. Modul dikembangkan sebagai kustomisasi Odoo 17 Community tanpa OpenEduCat dan tanpa addon Enterprise, sebagai bagian dari proyek LabFIK Compliance.
4. Data bersama, yaitu personel, jabatan, periode, ruang, mata kuliah, kelas, sesi, alat, dan bahan, ditempatkan di addon inti proyek. Penelitian ini mengisi mata kuliah, kelas, dan sesi, tetapi tidak mengembangkan master lain. Pengesahan dokumen memakai alur modul Tata Kelola, dan penugasan petugas dibaca dari modul SDM.
5. Data alat hanya dibaca sebagai peringatan pada pemeriksaan kesiapan. Penelitian ini tidak mengelola kalibrasi, stok, inventaris, maupun pemeliharaan alat dan bahan.
6. Jadwal kelas dari fakultas masuk melalui impor berkas. Penilaian praktikan tetap dilakukan di LeADS dan presensi rinci tetap dicatat di SIMPEL; modul hanya menyimpan tautan bukti penilaian per kelas dan tautan presensi pada jurnal sesi, tanpa integrasi langsung dengan SIAKAD, LeADS, maupun SIMPEL.
7. Rancangan dibatasi pada fitur yang dibutuhkan untuk membuktikan kriteria instrumen. Penjadwalan otomatis, kalender libur, pengingat, pemeriksaan per unit komputer, dan rekap honor asisten tidak dirancang.
8. Sistem menghitung persentase PKG-15 sampai PKG-18 dan persentase kelas berbukti PKG-19 dari rekaman yang tersimpan. Untuk PKG-20, sistem hanya menunjukkan kriteria tertinggi yang datanya lengkap. Sistem tidak menjamin kenaikan skor monev dan tidak menggantikan penilaian oleh penilai.
9. Data uji dan data demo bersifat fiktif; data nyata hanya dikutip sebagai angka agregat.

## 1.4 Tujuan dan Manfaat

### 1.4.1 Tujuan

Tujuan penelitian ini adalah sebagai berikut:

1. Menganalisis proses persiapan, pelaksanaan, dan evaluasi praktikum di LabFIK yang berjalan saat ini terhadap kriteria PKG-15 sampai PKG-20 pada Instrumen Monev Laboratorium UPNVJ 2026 v1.1.
2. Merancang modul Odoo untuk pelaksanaan praktikum dengan pendekatan berorientasi objek, yang menautkan setiap rekaman persiapan, pelaksanaan, dan penilaian ke sesi atau kelas asalnya.
3. Mengimplementasikan dan menguji modul tersebut sehingga pemenuhan keenam indikator dapat dihitung atau ditunjukkan dan dapat ditelusuri ke buktinya.

### 1.4.2 Manfaat

Manfaat penelitian ini adalah sebagai berikut:

1. Bagi LabFIK: jadwal, kesiapan, pelaksanaan, penilaian, dan kepuasan pengguna tercatat pada sesi dan periode yang sama, sehingga bentrok dan ketidaksiapan dapat diketahui sebelum sesi dan bukti monev tidak perlu dikumpulkan manual.
2. Bagi laboran, asisten, dan dosen: pemeriksaan kesiapan, penerbitan modul, jurnal sesi, dan tautan penilaian dilakukan melalui alur yang sama untuk setiap sesi, tanpa bergantung pada pelaporan untuk honor.
3. Bagi proyek LabFIK Compliance: sesi bertanggal yang dihasilkan modul ini menjadi dasar bagi indikator lain, seperti penugasan petugas pada modul SDM.
4. Bagi penelitian selanjutnya: rancangan modul dapat dikembangkan untuk fitur yang dibatasi pada penelitian ini, seperti integrasi langsung dengan sistem universitas.

## 1.5 Jadwal Kegiatan

Jadwal kegiatan penelitian ditunjukkan pada Tabel 1.1. Tanggal untuk kegiatan yang sudah selesai diambil dari riwayat dokumen rancangan; tanggal kegiatan berikutnya belum ditetapkan.

Tabel 1.1 Jadwal Kegiatan

| No | Kegiatan | Waktu | Status |
|---|---|---|---|
| 1 | Analisis indikator PKG-15 sampai PKG-20 dan studi dokumen | 14–16 November 2026 | Selesai (draf) |
| 2 | Kebutuhan sistem dan proses bisnis TO-BE | 14–18 November 2026 | Selesai (draf) |
| 3 | *Use case*, *expanded use case*, SSD, *conceptual model*, dan *design class diagram* | 16–18 November 2026 | Selesai (draf) |
| 4 | Penyusunan proposal (Bab I dan Bab II) | November 2026 | Berjalan |
| 5 | Wawancara KaLab dan laboran | [diisi] | Belum |
| 6 | Bimbingan dan revisi rancangan | [diisi] | Belum |
| 7 | Implementasi modul | [diisi] | Belum |
| 8 | Pengujian *black box*, kecocokan status monev, dan UAT | [diisi] | Belum |
| 9 | Penyusunan laporan akhir | [diisi] | Belum |

## Daftar Pustaka

- Aditia, S., Miharja, M. N. D., & Aguswin, A. (2023). Implementasi sistem kehadiran praktikum berbasis QR-code dengan WhatsApp gateway menggunakan metode Rapid Application Development (RAD). *Jurnal Ilmiah Rekayasa dan Manajemen Sistem Informasi, 9*(2), 82–88. https://doi.org/10.24014/rmsi.v9i2.23693
- Aji, H. S. (2024). Sistem informasi penjadwalan praktikum berbasis Android pada Laboratorium Geografi Fakultas Ilmu Sosial Universitas Negeri Semarang. *Indonesian Journal of Laboratory, 7*(2), 59–65. https://doi.org/10.22146/ijl.v5i2.76651 **[VALIDASI: volume 7 tetapi DOI v5i2]**
- Anandar, R. (2026). *Pengembangan modul perencanaan asisten praktikum berbasis Odoo OpenEduCat (Studi kasus: Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta)*. http://repository.upnvj.ac.id/id/eprint/51635
- Badan Standardisasi Nasional. (2018). *SNI ISO/IEC 17025:2017 Persyaratan umum kompetensi laboratorium pengujian dan laboratorium kalibrasi*. BSN.
- Cahyaningrum, D., Sulistyawati, & Sari, H. T. M. (2024). Kepuasan pengguna laboratorium pendidikan. *Jurnal Pengelolaan Laboratorium Pendidikan, 6*(1), 17–23. https://ejournal2.undip.ac.id/index.php/jplp/article/view/17350
- Damanik, B., Alhaq, M. I., Ginting, R. U., & Situmorang, H. (2026). Sistem informasi pemakaian laboratorium komputer. *Jurnal Mahajana Informasi, 11*(1), 7–15. https://doi.org/10.51544/jurnalmi.v11i1.6235
- Hidayati, A., Argianto, & Rini, B. P. (2025). Inovasi sistem penjadwalan laboratorium terpadu melalui aplikasi M-Room berbasis Google Spreadsheet di Poltekkes Kemenkes Jakarta I. *Jurnal Pengelolaan Laboratorium Pendidikan, 7*(2), 139–150. https://ejournal2.undip.ac.id/index.php/jplp/article/view/27113
- Iswanto, D., & Mulyono, H. B. (2021). Analisis manajemen laboratorium terpadu mikroskopis di Fakultas Kedokteran Universitas Cenderawasih Jayapura Papua (Studi kasus). *Indonesian Journal of Laboratory, 4*(1), 21–29. https://journal.ugm.ac.id/ijl/article/view/65346
- Kementerian Pendidikan Tinggi, Sains, dan Teknologi. (2025). *Peraturan Menteri Pendidikan Tinggi, Sains, dan Teknologi Nomor 39 Tahun 2025 tentang Penjaminan Mutu Pendidikan Tinggi*.
- Nurrohmah, W. M., & Wiratama, J. (2023). Enterprise Resource Planning (ERP) SAP Business One evaluation and improvement recommendation using customized Odoo. *Ultima InfoSys: Jurnal Ilmu Sistem Informasi, 13*(2), 77–84. https://doi.org/10.31937/si.v13i2.2802
- Ulya, D. I., Khair, A., & Amrozi, Y. (2024). A problem of information system integration at a university in Indonesia. *SAINTEKBU*. https://ejournal.unwaha.ac.id/saintek/article/view/838
- Universitas Pembangunan Nasional "Veteran" Jakarta. (2026). *Instrumen Monev Laboratorium UPNVJ 2026 v1.1*. Dokumen internal.
- Warsono, & Mulyono, H. (2022). Sistem informasi manajemen penjadwalan penggunaan laboratorium pada Poltekkes Kemenkes Jambi. *Jurnal Manajemen Sistem Informasi, 7*(1), 40–50. https://ejournal.unama.ac.id/index.php/jurnalmsi/article/view/1077
- Wijaya, G. F., Oktadini, N. R., Sevtiyuni, P. E., & Buchari, M. A. (2022). Adoption of SNI ISO/IEC 17025:2017 principles for laboratory management information system development. *Ultima InfoSys: Jurnal Ilmu Sistem Informasi, 13*(1), 37–45. https://doi.org/10.31937/si.v13i1.2678
