# BAB II RANCANGAN PROYEK (Modul Pelaksanaan Praktikum)

18 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20
**Status: DRAF.** Naskah Bab II proposal, seluruh subbab sudah berisi. Garis besar dan alasan susunannya ada di [kerangka-bab-2-praktikum.md](kerangka-bab-2-praktikum.md).

Catatan untuk penulis (hapus sebelum naskah diserahkan):
- **SSD dan *conceptual model* dimasukkan kembali** (2.3.5 dan 2.3.6) mengikuti misi penulisan 18 Nov 2026, yang menggantikan permintaan sebelumnya "tanpa *sequence*". Bila pembimbing meminta naskah tanpa SSD, hapus 2.3.5 beserta Gambar 2.12–2.16 dan Tabel 2.20, lalu nomori ulang.
- Gambar 2.1–2.25 seluruhnya diambil dari diagram yang sudah ada; tidak ada gambar baru.
- Setiap gambar diekspor dari halaman diagram di `projek-fiklab/rancangan/*.drawio`, bukan dari halaman "Catatan … (bahan kerja)".
- Penanda [ASUMSI], [KONFIRMASI], dan [VALIDASI] dibiarkan sampai wawancara KaLab dan bimbingan berikutnya, lalu dihapus atau diganti sumbernya.
- Angka di 2.1.2 adalah olahan penulis atas data nyata (hanya angka agregat). Minta izin KaLab sebelum dikutip **[KONFIRMASI]**.

---

## 2.1 Observasi

Observasi bertujuan memahami cara Laboratorium FIK UPN "Veteran" Jakarta (LabFIK) mengelola pelaksanaan praktikum saat ini, lalu membandingkannya dengan kriteria Instrumen Monev Laboratorium UPNVJ 2026. Hasil observasi menjadi dasar usulan solusi pada subbab 2.2.

### 2.1.1 Metode Observasi

Observasi dilakukan dengan tiga cara. Pertama, studi dokumen terhadap dokumen dan data yang dipakai LabFIK untuk mengelola praktikum. Kedua, telaah Instrumen Monev Laboratorium UPNVJ 2026 v1.1 untuk enam indikator yang menjadi lingkup modul ini (PKG-15 sampai PKG-20), beserta klausul SNI ISO/IEC 17025:2017 yang dirujuk instrumen. Ketiga, wawancara dengan Kepala Laboratorium (KaLab) dan laboran. Daftar pertanyaan wawancara (19 pertanyaan) sudah disusun, tetapi wawancara **belum dilaksanakan** pada saat naskah ini ditulis **[KONFIRMASI: jadwal wawancara]**. Karena itu, kondisi saat ini pada subbab 2.1.2 hanya diambil dari isi dokumen dan data, dan hal yang masih memerlukan keterangan narasumber diberi penanda.

Dokumen yang dikaji ditunjukkan pada Tabel 2.1. Dokumen dibedakan menjadi dokumen nyata dan draf. Draf hanya dipakai sebagai pembanding format dan tidak dijadikan bukti kondisi laboratorium.

Tabel 2.1 Dokumen yang Dikaji

| No | Dokumen | Sifat | Periode | Indikator |
|---|---|---|---|---|
| D1 | Prosedur Operasional Baku (POB) Manajemen Praktikum dan Asistensi FIK, 17 langkah dan 10 lampiran | Nyata, belum disahkan | 2025 | PKG-15–20 |
| D2 | *Sheet* Alokasi Pertemuan Asisten Praktikum | Data nyata | 2025/2026 Ganjil s.d. 2026/2027 Ganjil (3 periode) | PKG-15, 18 |
| D3 | Google Form Pelaksanaan Asistensi Praktikum beserta *sheet* responsnya (1.147 laporan) | Data nyata | 2024/2025 Genap s.d. 2026/2027 Ganjil (4 periode) | PKG-15, 16, 18 |
| D4 | Paket dokumen manajemen praktikum 2026 (23 dokumen) | Draf **[VALIDASI ke KaLab]** | 2026 | PKG-15–20 |
| D5 | Paket dokumen monev laboratorium | Draf | 2026 | PKG-15–20 |

Data D2 dan D3 memuat data pribadi asisten dan dosen. Data tersebut tidak dikutip; yang diambil hanya struktur kolom dan angka agregat. Dokumen nyata tidak ditemukan untuk jadwal kuliah praktikum bertanggal, daftar perangkat lunak dan lisensinya, stok bahan, rubrik penilaian, rekap nilai, dan hasil survei kepuasan.

### 2.1.2 Kondisi Saat Ini

**Prosedur.** LabFIK sudah memiliki POB Manajemen Praktikum dan Asistensi (D1) yang disusun dalam lima kelompok tahap: perencanaan, pelaksanaan, evaluasi, pengendalian, dan peningkatan. Namun, POB tersebut belum disahkan: nomor dokumen, tanggal efektif, dan lembar pengesahan masih kosong. Prosedurnya ada, tetapi belum menjadi dokumen yang terkendali.

**Jadwal dan ruang.** POB menyebut bahwa asisten berkoordinasi dengan dosen berdasarkan tabel jadwal kelas, tetapi tabel tersebut tidak dilampirkan dan berada di luar laboratorium. Pada *sheet* alokasi (D2), kolom hari, jam mulai, dan jam selesai kosong di seluruh 222 baris kelas selama tiga periode, dan tidak ada kolom ruang maupun jumlah mahasiswa. Dengan kata lain, laboratorium tidak memegang daftar sesi praktikum yang bertanggal. Akibatnya, jumlah sesi yang seharusnya terlaksana tidak dapat dihitung, dan bentrok ruang tidak dapat diperiksa sebelum semester. POB juga tidak mengatur pemakaian laboratorium di luar praktikum maupun cara menyelesaikan bentrok jadwal.

**Modul.** Template modul pada lampiran POB memiliki kolom penyusun, pereviu, dan pengesah, tetapi tidak memiliki nomor versi. Dalam praktik, modul diunggah ulang oleh asisten pada setiap laporan sesi: dari 1.064 laporan yang memuat modul, terdapat 1.062 berkas yang berbeda. Tidak ada satu modul acuan yang dapat dibuktikan tersedia sebelum sesi.

**Kesiapan sarana dan bahan.** POB merancang pemantauan kesiapan sarana secara berkala oleh laboran per kelas dan per ruang. Dalam praktik, kesiapan dicatat oleh asisten melalui formulir laporan (D3) sesudah sesi berlangsung. Sebanyak 104 laporan menyatakan "Siap" tetapi sekaligus mencatat kendala, dan 11 sesi yang dinyatakan "Belum Siap" tetap dilaksanakan; tidak ada keputusan untuk menunda sesi. Kendala sarana muncul pada sekitar 14% laporan, terutama pada komputer (31 laporan), jaringan (27), perangkat lunak (22), proyektor dan audio (16), serta jumlah komputer yang kurang (8). Jejak pemakaian bahan habis pakai hanya ditemukan pada tiga laporan (praktik *crimping* kabel jaringan), sehingga pemeriksaan bahan hanya relevan untuk sebagian kecil sesi **[KONFIRMASI: pemakaian komponen pada praktikum IoT]**.

**Pelaksanaan sesi.** Formulir laporan (D3) hanya diisi asisten, dan rekapnya menghitung jumlah sesi per asisten. Pencatatan ini dirancang untuk keperluan honor asisten, bukan sebagai bukti mutu. Akibatnya, kelas tanpa asisten tidak memiliki rekaman sama sekali, padahal jumlahnya 56%, 42%, dan 56% dari seluruh kelas pada tiga periode. Pada kelas yang berasisten pun, laporan hanya mencakup 75% dan 64% sesi. Kualitas laporan juga rendah: terdapat 62 laporan ganda, 148 laporan (13%) dengan durasi yang tidak valid, median keterlambatan pelaporan yang mencapai 29,5 hari pada periode terburuk, 55 sesi daring tanpa persetujuan yang tercatat, dan 70 laporan dengan asisten yang berbeda dari rencana. Presensi laboran tidak dicatat, dan presensi praktikan hanya berupa jumlah. POB menyerahkan penyesuaian jadwal kepada asisten, dan formulir penyesuaian jadwal yang disebut di POB tidak dilampirkan.

**Penilaian.** Penilaian praktikan dikerjakan dosen di LeADS UPNVJ. Formulir laporan dan lembar pelaksanaan asistensi tidak memiliki kolom nilai, rubrik, atau umpan balik, sehingga laboratorium tidak memegang bukti penilaian individual. Template modul hanya mencantumkan bobot nilai, tanpa rubrik.

**Kepuasan pengguna.** POB melampirkan kuesioner peserta berisi 15 butir skala 1–5 dan satu butir saran. Kuesioner tersebut meminta nama praktikan, tidak memuat butir keselamatan dan akses, serta tidak menetapkan populasi dan target jumlah responden. Data respons kuesioner tidak ditemukan **[KONFIRMASI: pernah dijalankan atau tidak]**. Di sisi lain, POB sudah memiliki lembar evaluasi kendala dan tindak lanjut dengan pola analisis penyebab, solusi, penanggung jawab, dan tenggat, yang dapat dijadikan dasar rencana tindak lanjut.

**Aliran informasi.** Berdasarkan dokumen D1–D3, informasi praktikum saat ini mengalir melalui media yang terpisah. Jadwal kelas berasal dari fakultas dan tidak disimpan laboratorium. Alokasi asisten dicatat laboran pada *sheet* alokasi (D2). Sesudah sesi, asisten mengisi Google Form (D3), yang responsnya terkumpul di *sheet* dan direkap untuk honor. Modul berpindah sebagai lampiran laporan, nilai berada di LeADS, dan presensi rinci berada di SIMPEL. Tidak ada satu data yang menghubungkan rencana sesi, kesiapan, pelaksanaan, dan penilaian, sehingga untuk menjawab satu indikator monev data harus dikumpulkan dan dicocokkan secara manual dari beberapa media. Alur pengisian tersebut disimpulkan dari struktur dokumen dan belum dikonfirmasi narasumber **[KONFIRMASI: wawancara KaLab dan laboran]**.

Ringkasan kondisi tersebut ditunjukkan pada Tabel 2.2.

Tabel 2.2 Ringkasan Kondisi Saat Ini

| Area | Kondisi | Sumber |
|---|---|---|
| Prosedur | POB ada tetapi belum disahkan | D1 |
| Jadwal | Tidak ada sesi bertanggal; hari dan jam kosong di 222 baris kelas; tidak ada ruang dan jumlah mahasiswa; pemakaian lab lain dan bentrok tidak diatur | D1, D2 |
| Modul | Tanpa nomor versi; diunggah ulang pada setiap laporan (1.062 berkas berbeda dari 1.064 laporan) | D1, D3 |
| Kesiapan | Dicatat asisten sesudah sesi; 104 laporan "Siap" dengan kendala; 11 sesi "Belum Siap" tetap berjalan | D3 |
| Bahan | Jejak hanya pada 3 laporan | D3 |
| Pelaksanaan | Pencatatan untuk honor; 42–56% kelas tanpa rekaman; cakupan laporan 64–75%; laporan ganda, durasi tidak valid, keterlambatan; perubahan sesi tidak tercatat | D2, D3 |
| Penilaian | Di LeADS; laboratorium tidak memegang bukti | D1, D3 |
| Kepuasan | Kuesioner ada, data respons tidak ditemukan; belum mencakup keselamatan dan akses | D1 |

Secara ringkas, LabFIK sudah memiliki prosedur praktikum dan lebih dari seribu laporan pelaksanaan, tetapi rekaman itu dibuat untuk honor asisten, bukan sebagai bukti mutu. Jadwal tidak bertanggal, modul tidak berversi, kesiapan dinilai asisten sesudah sesi, perubahan sesi tidak tercatat, kelas tanpa asisten tidak terekam, dan bukti penilaian serta kepuasan tidak ada di laboratorium.

### 2.1.3 Kesenjangan terhadap Instrumen

Setiap indikator pada Instrumen Monev memiliki kriteria yang harus dibuktikan. Perbandingan antara kriteria tersebut dan kondisi saat ini ditunjukkan pada Tabel 2.3.

Tabel 2.3 Kesenjangan Kondisi Saat Ini terhadap Instrumen Monev

| Indikator | Kriteria instrumen (ringkas) | Kondisi saat ini | Kesenjangan |
|---|---|---|---|
| PKG-15 Jadwal dan modul tersedia sebelum kegiatan | C1 jadwal sah dan dipublikasikan sebelum sesi; C2 tanpa bentrok ruang; C3 sesuai kapasitas ruang; C4 modul berlaku tersedia sebelum sesi | Tidak ada sesi bertanggal; modul tanpa versi | Belum ada jadwal sesi yang disahkan, pemeriksaan bentrok dan kapasitas, serta modul berversi |
| PKG-16 Alat dan perangkat lunak siap sebelum sesi | S1 diperiksa sebelum sesi; S2 semua butir wajib siap; S3 perangkat lunak sesuai modul dan berlisensi; S4 keputusan siap atau tunda tercatat | Dicatat asisten sesudah sesi; tidak ada keputusan tunda | Belum ada pemeriksaan oleh laboran sebelum sesi dengan keputusan yang tercatat |
| PKG-17 Bahan sesuai sebelum sesi (bersyarat) | B1 bahan diperiksa sebelum sesi; B2 jumlah, mutu, dan label sesuai; B3 penggantian bahan disetujui | Hampir tidak ada rekaman bahan | Belum ada daftar bahan per modul dan pemeriksaannya |
| PKG-18 Sesi terlaksana sesuai jadwal | C1 terlaksana; C2 sesuai jadwal atau perubahan disetujui; C3 durasi memenuhi; C4 sesuai modul; C5 presensi dan *log book* lengkap | Laporan untuk honor; kelas tanpa asisten tidak terekam; perubahan tanpa persetujuan | Belum ada satu jurnal per sesi untuk semua kelas dan perubahan sesi yang disetujui |
| PKG-19 Penilaian individual | P1 bukti unjuk kerja individual; P2 rubrik; P3 umpan balik; P4 remediasi | Di LeADS; rubrik belum ada | Belum ada tautan bukti penilaian per kelas dan rubrik pada modul |
| PKG-20 Kepuasan pengguna | K1 survei ditetapkan; K2 mencakup enam aspek dan target respons; K3 dilaksanakan dan dianalisis; K4 ditindaklanjuti dan dibandingkan antarperiode | Kuesioner ada, data respons tidak ditemukan | Belum ada survei per periode yang ditetapkan, dianalisis, dan ditindaklanjuti |

Kesenjangan ini menunjukkan bahwa masalah utamanya bukan ketiadaan kegiatan, melainkan ketiadaan rekaman yang dibuat pada saat kegiatan terjadi oleh orang yang bertanggung jawab, sehingga kegiatan tersebut tidak dapat dibuktikan saat monev.

### 2.1.4 Pelaku dan Perannya Saat Ini

Pelaku yang terlibat dalam pengelolaan praktikum, menurut POB dan data yang dikaji, ditunjukkan pada Tabel 2.4. Kolom terakhir menunjukkan posisi pelaku terhadap sistem yang diusulkan.

Tabel 2.4 Pelaku Pengelolaan Praktikum

| No | Pelaku | Peran saat ini | Posisi terhadap sistem usulan |
|---|---|---|---|
| 1 | Kepala Laboratorium | Mengelola praktikum, meninjau alokasi, mengevaluasi kendala dan kuesioner | Pengguna sistem |
| 2 | Laboran dan teknisi | Menyiapkan sarana, memantau alokasi dan kesiapan secara manual | Pengguna sistem |
| 3 | Asisten praktikum | Membantu sesi, melaporkan sesi melalui Google Form untuk honor | Pengguna sistem |
| 4 | Dosen | Memberi materi, memperbarui modul, menilai di LeADS | Pengguna sistem |
| 5 | Praktikan | Mengikuti praktikum, mengisi kuesioner | Mengisi survei tanpa akun |
| 6 | Tim jadwal fakultas | Menyusun jadwal kelas praktikum | Di luar sistem; berkasnya diimpor laboran **[ASUMSI]** |
| 7 | Koordinator Program Studi, Wakil Dekan, Dekan, Tata Usaha | Mengajukan dan menyetujui alokasi, mengesahkan POB, mengurus honor | Di luar sistem |
| 8 | LeADS, SIMPEL, Google Form | Penilaian, presensi rinci, laporan sesi | LeADS dan SIMPEL ditautkan; Google Form digantikan |

## 2.2 Usulan Solusi

### 2.2.1 Gambaran Solusi

Solusi yang diusulkan adalah modul Pelaksanaan Praktikum di atas Odoo 17 Community, sebagai bagian dari sistem LabFIK Compliance. Sistem ini dibangun bersama oleh beberapa anggota kelompok; setiap anggota memegang satu modul fungsional, dan data yang dipakai bersama ditempatkan di satu addon inti. Modul ini memegang enam indikator, yaitu PKG-15 sampai PKG-20, dan bertugas membangkitkan Sesi praktikum yang juga dipakai modul lain.

Benang merah solusinya adalah setiap sesi praktikum dapat ditelusuri dari rencana, kesiapan, pelaksanaan, sampai penilaian, dan direkam saat kegiatan terjadi oleh orang yang bertugas. Sesi bertanggal menjadi tulang punggung: jadwal membangkitkan sesi, laboran memeriksa kesiapan sesi, dan petugas mengirim jurnal sesi. Versi modul menjadi daftar kebutuhan: perangkat lunak, bahan, dan rubrik yang tercantum di modul menjadi acuan pemeriksaan kesiapan dan penilaian. Status indikator tidak diisi manual, tetapi dihitung dari rekaman tersebut.

Susunan addon dan pembagian tanggung jawab antara modul ini, addon inti, dan modul anggota lain dijelaskan pada subbab 2.3.1.

### 2.2.2 Fitur Utama

Rancangan modul ini dibatasi dengan prinsip titik tengah (*sweet spot*): setiap kriteria instrumen harus dapat dibuktikan, tetapi fitur yang tidak dibutuhkan untuk membuktikan kriteria dan menambah kerumitan tidak dirancang. Fitur dibagi menjadi dua lapis. Lapis Inti adalah fitur yang bila tidak ada membuat suatu kriteria tidak terbukti. Lapis Pelengkap adalah fitur yang memperkuat rancangan dengan biaya kecil. Fitur per area ditunjukkan pada Tabel 2.5.

Tabel 2.5 Fitur Utama per Area

| Area | Inti | Pelengkap |
|---|---|---|
| Jadwal dan modul (PKG-15) | Impor jadwal kelas dan pembangkitan sesi bertanggal; pemeriksaan bentrok ruang dan kapasitas; penetapan jadwal yang disahkan dan ditandatangani; pengajuan pemakaian laboratorium dengan persetujuan; versi modul berisi berkas, perangkat lunak, bahan, dan rubrik; jadwal terpadu dan rekaman konflik | Impor mata kuliah dan kelas dari *sheet* alokasi; penarikan pengajuan; notifikasi pengajuan dan keputusan |
| Kesiapan (PKG-16, 17) | Pemeriksaan kesiapan per sesi dengan butir per kategori dan keputusan siap atau tunda; butir bahan dengan persetujuan penggantian | Rekap kesiapan per ruang; peringatan alat yang tidak tersedia dari master alat bersama |
| Pelaksanaan (PKG-18) | Jurnal sesi berisi jam aktual, modul yang dipakai, presensi petugas, jumlah praktikan hadir, dan *log book*; perubahan sesi dengan persetujuan dan sesi pengganti | Rekap keterlaksanaan per kelas; penanda jurnal terlambat; penanda petugas yang tidak sesuai penugasan |
| Penilaian (PKG-19) | Tautan bukti penilaian LeADS per kelas; rubrik pada versi modul | Impor nilai dari ekspor Excel LeADS sehingga kelengkapan per praktikan dihitung sistem |
| Kepuasan (PKG-20) | Survei per periode dengan enam aspek, populasi, dan target respons; respons anonim; evaluasi dan rencana tindak lanjut; penilaian efektivitas | Pembatalan penetapan survei sebelum dibuka |
| Status monev | Persentase PKG-15–18, persentase kelas berbukti PKG-19, kriteria tertinggi PKG-20, laporan bukti untuk penilai | — |

Fitur yang tidak dirancang meliputi penjadwalan otomatis, kalender libur, pengingat (modul, jurnal, lisensi, survei), pemeriksaan per unit komputer, rekap honor asisten, dan integrasi langsung dengan SIAKAD, LeADS, maupun SIMPEL. Hubungan antara masalah pada Bab I subbab 1.2, kebutuhan, usulan solusi, fitur, dan indikator ditunjukkan pada Tabel 2.6. Kode M1–M8 sesuai dengan butir 1 sampai 8 identifikasi masalah pada Bab I subbab 1.2.

Tabel 2.6 Matriks Masalah, Kebutuhan, Usulan Solusi, dan Fitur

| Masalah | Kebutuhan | Usulan Solusi | Fitur | Package |
|---|---|---|---|---|
| M1. Laboratorium tidak memegang jadwal sesi bertanggal yang disahkan; bentrok ruang dan kapasitas tidak diperiksa; pemakaian lab di luar praktikum tidak tercatat | KF-PRK-01–11, 45, 47, 49 | Sesi bertanggal dibangkitkan dari jadwal kelas, diperiksa bentrok dan kapasitasnya, lalu disahkan; pemakaian lab diajukan dan diputuskan | Impor jadwal kelas, penetapan jadwal, pemakaian laboratorium, laporan jadwal | PKG-15 C1–C3 |
| M2. Modul tidak berversi dan tidak terbukti tersedia sebelum sesi | KF-PRK-12–14 | Satu versi modul berlaku per mata kuliah per periode, berisi berkas, rubrik, perangkat lunak, dan bahan | Versi modul | PKG-15 C4 |
| M3. Kesiapan alat, perangkat lunak, dan utilitas dicatat asisten sesudah sesi, tanpa keputusan tunda | KF-PRK-15–18, 21, 52 | Pemeriksaan kesiapan oleh laboran sebelum sesi, dengan butir dari modul dan keputusan siap atau tunda | Pemeriksaan kesiapan | PKG-16 S1–S4 |
| M4. Bahan habis pakai tidak diperiksa dan penggantian bahan tidak tercatat | KF-PRK-19, 20 | Butir bahan dibentuk dari daftar bahan modul; penggantian bahan disetujui dosen kelas | Butir bahan, persetujuan substitusi | PKG-17 B1–B3 (bersyarat) |
| M5. Pencatatan pelaksanaan untuk honor asisten; kelas tanpa asisten tidak terekam; perubahan sesi tanpa persetujuan | KF-PRK-22–30, 46, 47, 49, 51 | Satu jurnal per sesi untuk semua kelas; perubahan sesi diajukan dan diputuskan KaLab | Jurnal sesi, perubahan sesi, laporan pelaksanaan | PKG-18 C1–C5 |
| M6. Bukti penilaian individual tidak ada di laboratorium dan rubrik belum ada | KF-PRK-31, 32, 50 | Tautan bukti penilaian LeADS per kelas; rubrik pada versi modul; impor nilai sebagai pelengkap | Penilaian kelas, impor nilai | PKG-19 P1–P4 |
| M7. Survei kepuasan tidak memiliki data respons, tidak mencakup seluruh aspek, dan tidak ditindaklanjuti | KF-PRK-33–38, 48 | Survei per periode yang ditetapkan, diisi anonim, dievaluasi, dan dinilai efektivitas tindak lanjutnya | Survei kepuasan, evaluasi survei, laporan survei | PKG-20 K1–K4 |
| M8. Status indikator dihitung manual dan tidak tertelusur ke bukti | KF-PRK-39–44 | Status indikator dihitung dari rekaman dan setiap angka tertaut ke rekaman sumbernya | Status monev, laporan bukti | PKG-15–20 |

### 2.2.3 Kebutuhan Sistem

Kebutuhan fungsional dibedakan menjadi kebutuhan yang tampak (*evident*), yaitu dikerjakan pengguna melalui sistem, dan kebutuhan tersembunyi (*hidden*), yaitu dikerjakan sistem tanpa diminta pengguna (Wazlawick, 2024, hlm. 51). Modul ini memiliki 52 kebutuhan fungsional, terdiri atas 41 kebutuhan lapis Inti dan 11 kebutuhan lapis Pelengkap. Ringkasannya per kelompok ditunjukkan pada Tabel 2.7; rincian lengkapnya dimuat di lampiran.

Tabel 2.7 Ringkasan Kebutuhan Fungsional

| Kelompok | Kode | Isi ringkas | Inti | Pelengkap |
|---|---|---|---|---|
| A. Jadwal dan sesi | KF-PRK-01–11 | Mengelola mata kuliah dan kelas, impor jadwal dan pembangkitan sesi, penolakan bentrok, peringatan kapasitas, penetapan jadwal, pemakaian laboratorium, jadwal terpadu, rekaman konflik | 10 | 1 |
| B. Versi modul | KF-PRK-12–14 | Menerbitkan versi modul, menjaga satu versi berlaku, membaca modul berlaku | 3 | 0 |
| C. Kesiapan | KF-PRK-15–21 | Pemeriksaan kesiapan, butir otomatis dari modul, lisensi, keputusan, butir bahan, persetujuan penggantian, rekap kesiapan | 6 | 1 |
| D. Pelaksanaan sesi | KF-PRK-22–30 | Jurnal sesi, presensi petugas, *log book*, pengiriman jurnal, status sesi, perubahan sesi, rekap keterlaksanaan, penanda terlambat | 7 | 2 |
| E. Penilaian | KF-PRK-31–32 | Penilaian kelas dengan tautan LeADS, daftar belum lengkap | 1 | 1 |
| F. Kepuasan | KF-PRK-33–38 | Menyusun dan menetapkan survei, mengisi survei, evaluasi dan tindak lanjut, efektivitas, rekap per aspek | 6 | 0 |
| G. Status monev | KF-PRK-39–44 | Persentase dan kriteria tertinggi, laporan bukti, pengaturan modul, jejak audit | 6 | 0 |
| H. Temuan tabel status × transisi | KF-PRK-45–52 | Pencabutan jadwal, penolakan perubahan, penarikan pengajuan, pembatalan penetapan survei, notifikasi, impor nilai, penanda penugasan, pembacaan master alat | 2 | 6 |
| **Jumlah** | | | **41** | **11** |

Kebutuhan nonfungsional dikelompokkan menurut karakteristik mutu ISO/IEC 25010 dan hanya diisi untuk karakteristik yang dibutuhkan (Wazlawick, 2024, hlm. 51), seperti pada Tabel 2.8.

Tabel 2.8 Kebutuhan Nonfungsional

| Kode | Kebutuhan | Karakteristik |
|---|---|---|
| KNF-PRK-01 | Berjalan di Odoo 17 Community tanpa OpenEduCat dan tanpa addon Enterprise | *Compatibility* |
| KNF-PRK-02 | Hak akses berbasis grup pengguna; dosen dan asisten hanya mengakses data kelasnya | *Security* |
| KNF-PRK-03 | Data per praktikan dibatasi: presensi berupa jumlah; nilai hasil impor hanya NIM tanpa nama | *Security* |
| KNF-PRK-04 | Respons survei anonim | *Security* |
| KNF-PRK-05 | Identitas sesi tidak diketik ulang oleh pengisi jurnal | *Usability* |
| KNF-PRK-06 | Validasi masukan mencegah jam tidak valid dan laporan ganda | *Usability* |
| KNF-PRK-07 | Rekaman bukti tidak dapat dihapus; setiap koreksi tercatat | *Security* |
| KNF-PRK-08 | Model memakai pewarisan (*inheritance*) dari *mixin* bersama dan addon bawaan | *Maintainability* |
| KNF-PRK-09 | Modul lain dapat merujuk Sesi tanpa menambah *field* ke Sesi | *Maintainability* |
| KNF-PRK-10 | Tanpa integrasi langsung dengan SIAKAD, LeADS, dan SIMPEL; data masuk lewat impor berkas dan tautan | *Compatibility* |
| KNF-PRK-11 | Antarmuka berbahasa Indonesia | *Usability* |
| KNF-PRK-12 | Ambang durasi, batas hari pengisian jurnal, sah tidaknya sesi daring, dan batas lulus dapat diubah KaLab | *Portability* |
| KNF-PRK-13 | Jadwal periode dan laporan bukti diterbitkan sebagai PDF | *Usability* |
| KNF-PRK-14 | Jurnal sesi dapat diisi dari peramban ponsel | *Usability* |
| KNF-PRK-15 | Data uji fiktif; data nyata hanya dikutip sebagai angka agregat | *Security* |

Setiap kriteria instrumen harus memiliki kebutuhan yang membuktikannya. Keterlacakan kriteria ke kebutuhan ditunjukkan pada Tabel 2.9.

Tabel 2.9 Keterlacakan Kriteria Instrumen ke Kebutuhan

| Indikator | Kriteria | Kebutuhan (KF-PRK-) |
|---|---|---|
| PKG-15 | C1 jadwal sah dan dipublikasikan | 06, 07, 45 |
| PKG-15 | C2 tanpa bentrok | 04, 08, 09, 10, 11 |
| PKG-15 | C3 sesuai kapasitas | 01, 05 |
| PKG-15 | C4 modul berlaku sebelum sesi | 12, 13, 14 |
| PKG-16 | S1–S4 | 15, 16, 17, 18 |
| PKG-17 | B1–B3 | 12, 16, 19, 20 |
| PKG-18 | C1–C5 | 22–28, 43 |
| PKG-19 | P1–P4 | 12, 31, 40, 50 |
| PKG-20 | K1–K4 | 33–38, 41 |
| Semua | Persentase, kriteria tertinggi, laporan bukti | 39–42, 44 |

### 2.2.4 Metode Pengembangan dan Perancangan

Metode pengembangan sistem mengikuti kesepakatan kelompok dan arahan pembimbing. Naskah Bab I versi sebelumnya menyebut metode *agile*, tetapi metode ini belum ditetapkan bersama pembimbing **[KONFIRMASI pembimbing: metode pengembangan, seragam untuk satu kelompok]**. Penulis mengusulkan pengembangan bertahap per area, dimulai dari area jadwal dan sesi karena Sesi menjadi dasar bagi area lain dan bagi modul anggota kelompok lain **[USULAN PENULIS]**.

Metode perancangan mengikuti analisis dan desain berorientasi objek dari Wazlawick (2024), yang memakai UML dan memisahkan pemahaman bisnis, kebutuhan, dan desain. Langkah yang dipakai ditunjukkan pada Tabel 2.10. Setiap langkah memakai hasil langkah sebelumnya, sehingga setiap kelas pada rancangan akhir dapat ditelusuri ke proses bisnis dan kriteria instrumen.

Tabel 2.10 Langkah Perancangan

| No | Langkah | Hasil | Tempat |
|---|---|---|---|
| 1 | Analisis indikator | Kriteria, bukti, data, dan pembagi per PKG | Lampiran |
| 2 | Studi dokumen | Temuan kondisi saat ini | 2.1 |
| 3 | Kontrak data bersama | Master, Sesi, dan *mixin* yang dipakai bersama modul lain | 2.3.1 |
| 4 | Kebutuhan sistem | Kebutuhan fungsional dan nonfungsional | 2.2.3 |
| 5 | Proses bisnis | Diagram aktivitas dan diagram mesin status | 2.3.2 |
| 6 | *Use case* | Diagram *use case* dan deskripsinya | 2.3.3 |
| 7 | *Expanded use case* | Alur utama, varian, eksepsi, dan aturan bisnis | 2.3.4 |
| 8 | *System sequence diagram* | Operasi sistem (*command* dan *query*) beserta datanya | 2.3.5 |
| 9 | *Conceptual model* | Konsep, atribut, dan asosiasi tanpa unsur teknologi | 2.3.6 |
| 10 | *Design class diagram* | Model Odoo dengan *method*, tipe *field*, dan pewarisan | 2.3.7 |

### 2.2.5 Platform dan Modul yang Diperluas

Sistem dibangun di atas Odoo 17 Community dengan lisensi LGPL-3. Modul ini memperluas tiga addon bawaan. Addon `hr` dipakai untuk data pegawai dan jabatan, sehingga dosen, laboran, dan asisten dicatat sebagai pegawai dengan jabatannya, dan hak memutuskan ditentukan oleh jabatan. Addon `mail` dipakai untuk riwayat perubahan dan notifikasi. Addon `survey` dipakai untuk survei kepuasan karena sudah menyediakan formulir publik, respons anonim, dan rekap jawaban, sehingga modul ini cukup menambahkan aspek, populasi, target respons, dan penetapan.

Modul ini tidak memakai OpenEduCat. Sesi praktikum dirancang sebagai model sendiri di addon inti agar addon inti cukup bergantung pada `hr` dan `mail`, dan agar data mahasiswa tidak perlu disimpan di sistem laboratorium.

## 2.3 Rancangan Proyek

Rancangan proyek disusun dengan pendekatan berorientasi objek menggunakan *Unified Modeling Language* (UML), mengikuti urutan analisis dan perancangan dari Wazlawick (2024). Subbab ini diawali dengan arsitektur dan batas modul. Selanjutnya rancangan disusun berurutan: proses bisnis, *use case* yang diturunkan dari proses bisnis, *expanded use case* beserta aturan bisnisnya, *system sequence diagram* yang menghasilkan daftar operasi sistem, *conceptual model* yang memuat informasi yang harus disimpan, dan *design class diagram* yang disesuaikan dengan struktur model Odoo. Dengan urutan ini, setiap elemen rancangan dapat ditelusuri kembali ke proses dan ke kriteria Instrumen Monev Laboratorium UPNVJ 2026 yang menjadi dasarnya.

### 2.3.1 Arsitektur dan Batas Modul

Sistem LabFIK Compliance dibangun bersama oleh beberapa anggota kelompok. Setiap anggota memegang satu modul fungsional yang diwujudkan sebagai satu addon Odoo, sedangkan data yang dipakai lebih dari satu modul ditempatkan di addon inti `labfik_core`. Penulis memegang modul Pelaksanaan Praktikum (`labfik_praktikum`). Addon inti dan *mixin* bersama dirancang dalam modul Tata Kelola, sedangkan Mata Kuliah, Kelas, dan Sesi diusulkan penulis ke addon inti; penempatan ini masih menunggu konfirmasi kelompok **[KONFIRMASI kelompok: penempatan `labfik_core`]**. Susunan addon yang dipakai modul ini ditunjukkan pada Tabel 2.11.

Tabel 2.11 Susunan Addon

| Addon | Pemilik | Isi yang dipakai modul ini | Bergantung pada |
|---|---|---|---|
| `hr`, `mail` | Odoo 17 Community | Data pegawai dan jabatan, riwayat perubahan, notifikasi | — |
| `survey` | Odoo 17 Community | Formulir survei publik, respons anonim, rekap jawaban | — |
| `labfik_core` | Bersama | Master Periode, Ruang Lab, Mata Kuliah, Kelas, Bahan, dan Alat; transaksi Sesi; *mixin* pengesahan, rekaman bukti, dan kriteria | `hr`, `mail` |
| `labfik_sdm` | Modul SDM (anggota lain) | Penugasan asisten per kelas dan laboran per ruang | `labfik_core` |
| `labfik_praktikum` | Modul ini (penulis) | Penetapan jadwal, pengajuan, versi modul, pemeriksaan kesiapan, jurnal sesi, penilaian kelas, survei dan evaluasinya, status monev | `labfik_core`, `labfik_sdm`, `survey` |

Batas modul ditentukan dengan prinsip bahwa modul ini hanya mengubah data miliknya sendiri. Data milik addon inti atau modul lain hanya dibaca, dan perubahan pada addon inti hanya diajukan sebagai usulan kepada pemiliknya. Pembagian tanggung jawab tersebut ditunjukkan pada Tabel 2.12.

Tabel 2.12 Pembagian Tanggung Jawab Data

| Data | Pemilik | Peran modul ini |
|---|---|---|
| Periode, Ruang Lab, Personel (`hr.employee`), Jabatan (`hr.job`) | Addon inti | Membaca |
| Mata Kuliah, Kelas | Addon inti (diusulkan penulis) | Mengisi melalui impor jadwal dan «CRUDL» |
| Sesi | Addon inti (diusulkan penulis) | Membangkitkan, mengubah status, dan memperluas dengan *field* hitung |
| Bahan, Alat | Addon inti; Alat diisi modul Aset (kelompok lain) | Membaca untuk butir bahan dan peringatan alat |
| *Mixin* pengesahan, rekaman bukti, kriteria | Addon inti (dirancang modul Tata Kelola) | Mewarisi |
| Pengesahan dokumen dan riwayatnya | Modul Tata Kelola | Memakai alurnya untuk Penetapan Jadwal |
| Penugasan petugas | Modul SDM | Membaca untuk penanda petugas |
| Penetapan Jadwal, Pengajuan, Versi Modul, Pemeriksaan Kesiapan, Jurnal Sesi, Penilaian Kelas, Survei, Evaluasi Survei | Modul ini | Membuat, mengubah, dan membaca |

Sesi menjadi titik temu antarmodul. Modul ini membangkitkan Sesi, sedangkan modul SDM dan modul lain merujuk Sesi tanpa menambahkan *field* ke dalamnya (KNF-PRK-09). Data dari sistem universitas, yaitu jadwal fakultas, LeADS, dan SIMPEL, tidak diintegrasikan langsung; jadwal masuk melalui impor berkas, sedangkan penilaian dan presensi rinci masuk sebagai tautan (KNF-PRK-10).

### 2.3.2 Proses Bisnis

Pemodelan proses bisnis bertujuan memahami lingkungan tempat sistem akan dipakai, masalah yang ada di dalamnya, dan perbaikan yang dapat diberikan oleh sistem, sehingga kebutuhan sistem dapat diturunkan darinya (Wazlawick, 2024, hlm. 27). Proses bisnis modul Pelaksanaan Praktikum digambarkan dalam dua jenis diagram, yaitu diagram aktivitas (*activity diagram*) dan diagram mesin status (*state machine diagram*).

Diagram aktivitas UML dipakai untuk menggambarkan proses yang melibatkan lebih dari satu aktor dan memiliki percabangan (Wazlawick, 2024, hlm. 26). Setiap aktor digambarkan dalam satu lajur (*swimlane*), ditambah satu lajur Sistem. Tugas dibedakan menjadi tiga jenis (Wazlawick, 2024, hlm. 29–30): tugas «user» yang dikerjakan aktor dengan memakai sistem, tugas «service» yang dikerjakan sistem secara otomatis, dan tugas «manual» yang dikerjakan aktor di luar sistem. Tugas yang memanggil diagram aktivitas lain diberi stereotipe «call behavior». Kondisi percabangan ditulis di dalam kurung siku pada panah, dan simbol jam pasir menandai tugas yang menunggu waktu tertentu.

Diagram mesin status menggambarkan status yang dapat dimiliki sebuah objek bisnis dan peristiwa yang memindahkannya dari satu status ke status lain (Wazlawick, 2024, hlm. 36). Setiap transisi ditulis dengan pola `peristiwa [kondisi] / efek`: peristiwa adalah pemicu perpindahan, kondisi adalah syarat agar perpindahan terjadi, dan efek adalah tindakan yang dijalankan sebagai akibat perpindahan (Wazlawick, 2024, hlm. 36–37). Status yang dapat dihitung dari data lain, misalnya "sudah dipublikasikan" atau "terlewat", tidak dijadikan status tersendiri, tetapi diperlakukan sebagai atribut turunan yang hanya dapat dibaca (Wazlawick, 2024, hlm. 126). Pilihan ini membuat jumlah status tetap sedikit dan sama dengan status yang dipakai modul lain.

Modul ini memiliki lima diagram aktivitas dan tiga diagram mesin status, seperti pada Tabel 2.13. Data yang hanya dikelola tanpa alur bertahap, seperti mata kuliah dan kelas, tidak digambarkan dalam diagram aktivitas.

Tabel 2.13 Daftar Diagram Proses Bisnis

| Diagram | Isi | Indikator |
|---|---|---|
| A1 | Persiapan jadwal dan modul periode | PKG-15 |
| A2 | Pemakaian laboratorium di luar praktikum | PKG-15 |
| A3 | Pelaksanaan satu sesi praktikum | PKG-16, 17, 18 |
| A4 | Perubahan sesi | PKG-18 |
| A5 | Survei kepuasan pengguna per periode | PKG-20 |
| S1 | Status sesi praktikum | PKG-15, 18 |
| S2 | Status pengajuan pemakaian laboratorium dan perubahan sesi | PKG-15, 18 |
| S3 | Status survei kepuasan | PKG-20 |

Penilaian individual praktikan (PKG-19) tidak memiliki diagram aktivitas. Penilaian dikerjakan dosen di LeADS UPNVJ, sedangkan di sistem ini dosen atau laboran hanya mencatat tautan bukti penilaian per kelas dalam satu langkah, sehingga tidak ada alur bertahap yang perlu digambarkan.

#### 2.3.2.1 Diagram Aktivitas Persiapan Jadwal dan Modul

Persiapan dilakukan sebelum semester dimulai. Pada tahap ini jadwal sesi praktikum disusun dan disahkan, dan modul praktikum yang berlaku diterbitkan. Alurnya digambarkan pada Gambar 2.1.

> [Gambar 2.1 Diagram Aktivitas Persiapan Jadwal dan Modul] `activity-state-praktikum.drawio`, halaman "Activity TO-BE (1-5) - Persiapan Jadwal dan Modul"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.1, persiapan berjalan dalam dua jalur paralel. Pada jalur pertama, Tim Jadwal Fakultas menyusun jadwal kelas praktikum dan mengirimkan berkasnya di luar sistem. Laboran mengimpor berkas tersebut **[ASUMSI: impor berkas, tanpa integrasi dengan sistem jadwal fakultas]**, lalu sistem membangkitkan sesi bertanggal untuk setiap kelas dan memeriksa bentrok ruang. Bila ada bentrok, laboran menyampaikannya kepada fakultas untuk diperbaiki, dan alur kembali ke penyusunan jadwal. Bila tidak ada bentrok, sistem memeriksa kapasitas ruang terhadap jumlah mahasiswa kelas, kemudian laboran menyusun penetapan jadwal periode.

Penetapan jadwal disahkan oleh Kepala Laboratorium (KaLab) melalui alur pengesahan dokumen milik modul Tata Kelola, yang dipanggil dengan «call behavior» dan tidak digambar ulang. Setelah disahkan, sistem mencatat tanggal publikasi, dan seluruh sesi periode itu terbaca sebagai sudah dipublikasikan. Pada jalur kedua, dosen menerbitkan versi modul praktikum yang memuat berkas modul, rubrik penilaian, daftar perangkat lunak, dan daftar bahan, lalu sistem menandai versi sebelumnya sebagai versi yang diganti. Kedua jalur bertemu sebelum alur selesai.

Diagram ini menghasilkan bukti untuk PKG-15, yaitu jadwal yang disahkan dan dipublikasikan sebelum sesi berlangsung (kriteria C1), jadwal tanpa bentrok ruang (C2), jadwal yang sesuai kapasitas ruang (C3), dan modul berlaku yang tersedia sebelum sesi (C4).

#### 2.3.2.2 Diagram Aktivitas Pemakaian Laboratorium

Selain untuk praktikum terjadwal, ruang laboratorium juga dipakai untuk kegiatan lain. Pemakaian ini perlu tercatat dan disetujui agar tidak bentrok dengan jadwal praktikum. Alurnya digambarkan pada Gambar 2.2.

> [Gambar 2.2 Diagram Aktivitas Pemakaian Laboratorium] `activity-state-praktikum.drawio`, halaman "Activity TO-BE (2-5) - Pemakaian Lab"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.2, pengguna laboratorium yang tidak memiliki akun sistem menyampaikan permintaan pemakaian kepada laboran, lalu laboran mencatat pengajuan tersebut. Sistem memeriksa bentrok ruang dengan sesi praktikum dan pemakaian lain yang sudah disetujui. Bila bentrok, laboran mengubah waktu pemakaian dan sistem memeriksa ulang. Bila tidak bentrok, sistem mengirimkan notifikasi kepada KaLab.

KaLab meninjau pengajuan, lalu menyetujui atau menolaknya. Persetujuan disertai pemeriksaan bentrok ulang, karena pengajuan lain untuk ruang dan waktu yang sama mungkin sudah disetujui lebih dahulu. Bila disetujui, sistem memperbarui jadwal terpadu ruang. Bila ditolak, KaLab menuliskan alasannya, dan penolakan karena bentrok ditandai tersendiri. Sistem kemudian mengirimkan notifikasi keputusan, dan laboran menyampaikan keputusan itu kepada pengguna.

Diagram ini mendukung PKG-15 kriteria C2. Jadwal terpadu memuat praktikum dan kegiatan lain dalam satu tampilan (bukti 1 instrumen), dan penolakan karena bentrok menjadi rekaman konflik yang tertangani (bukti 5 instrumen).

#### 2.3.2.3 Diagram Aktivitas Pelaksanaan Sesi

Diagram ini menggambarkan satu sesi praktikum, mulai dari pemeriksaan kesiapan sebelum sesi sampai pelaporan sesudah sesi. Alurnya digambarkan pada Gambar 2.3.

> [Gambar 2.3 Diagram Aktivitas Pelaksanaan Sesi] `activity-state-praktikum.drawio`, halaman "Activity TO-BE (3-5) - Pelaksanaan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.3, sebelum jam mulai sesi laboran memulai pemeriksaan kesiapan. Sistem membuat butir pemeriksaan dari dua sumber: kategori tetap (stasiun kerja, jaringan, listrik, proyektor dan audio) dan kebutuhan perangkat lunak serta bahan yang tercantum pada versi modul yang berlaku. Bila data alat ruang sudah tersedia di master bersama, sistem juga menampilkan alat yang sedang tidak tersedia sebagai peringatan, dan jumlah komputer yang tersedia menjadi isian awal. Laboran kemudian mengisi hasil setiap butir. Bila ada bahan yang harus diganti, penggantian itu disetujui terlebih dahulu oleh dosen kelas.

Laboran lalu menetapkan keputusan kesiapan. Bila keputusannya tunda, laboran mengajukan perubahan sesi dengan memanggil diagram aktivitas Perubahan Sesi (A4). Bila siap, praktikum dilaksanakan pada jam mulai sesi di luar sistem. Sesudah sesi, Pengisi Jurnal mengisi jurnal sesi, mencatat presensi petugas, dan mencatat entri *log book*, kemudian mengirimkan jurnal. Pengisi Jurnal adalah aktor abstrak yang diperankan asisten yang bertugas, atau dosen yang mengajar bila kelas tidak memiliki asisten **[ASUMSI]**. Sistem memvalidasi jurnal, misalnya jam selesai harus setelah jam mulai dan hanya ada satu jurnal terkirim untuk setiap sesi. Jurnal yang tidak valid dikembalikan untuk diperbaiki. Jurnal yang valid mengubah status sesi menjadi Terlaksana.

Diagram ini menghasilkan bukti untuk PKG-16 (pemeriksaan kesiapan sebelum sesi, kriteria S1–S4), PKG-17 (bahan diperiksa sebelum sesi, jumlah, mutu, dan labelnya sesuai, serta penggantian bahan disetujui, B1–B3; hanya berlaku untuk sesi yang modulnya memakai bahan), dan PKG-18 (jurnal sesi, presensi petugas, dan *log book*, C1–C5).

#### 2.3.2.4 Diagram Aktivitas Perubahan Sesi

Jadwal sesi berlaku tetap selama semester, kecuali ada perubahan yang diajukan dan disetujui. Perubahan dapat berasal dari keputusan tunda pada pemeriksaan kesiapan, atau dari dosen pengampu yang memindahkan jadwal atau mengubah sesi menjadi daring. Alurnya digambarkan pada Gambar 2.4.

> [Gambar 2.4 Diagram Aktivitas Perubahan Sesi] `activity-state-praktikum.drawio`, halaman "Activity TO-BE (4-5) - Perubahan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.4, pengaju (dosen pengampu, Pengisi Jurnal, atau laboran) mengajukan perubahan sesi, dan sistem mengirimkan notifikasi kepada KaLab. KaLab meninjau lalu menolak atau menyetujui pengajuan. Persetujuan memiliki dua kemungkinan. Pertama, perubahan dengan sesi pengganti: sistem memeriksa bentrok pada waktu pengganti, KaLab menentukan waktu lain bila bentrok, lalu sistem membangkitkan sesi pengganti yang merujuk sesi asal. Kedua, perubahan tanpa pengganti: sesi dibatalkan, atau sesi tetap dilaksanakan dalam moda daring. Pada kedua kemungkinan, sistem mengubah status sesi asal, lalu mengirimkan notifikasi keputusan kepada pengaju.

Diagram ini menjaga agar setiap sesi yang tidak berjalan sesuai jadwal tetap memiliki rekaman: sesi yang diganti dapat ditelusuri ke sesi penggantinya, dan sesi yang dibatalkan memiliki keputusan yang tercatat. Keduanya dibutuhkan untuk menghitung keterlaksanaan sesi pada PKG-18.

#### 2.3.2.5 Diagram Aktivitas Survei Kepuasan

Survei kepuasan pengguna laboratorium dilaksanakan sekali setiap periode dan dilanjutkan dengan evaluasi serta rencana tindak lanjut. Alurnya digambarkan pada Gambar 2.5.

> [Gambar 2.5 Diagram Aktivitas Survei Kepuasan] `activity-state-praktikum.drawio`, halaman "Activity TO-BE (5-5) - Survei Kepuasan"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.5, KaLab menyusun survei periode lalu menetapkannya. Sebelum survei dapat ditetapkan, sistem memeriksa kelengkapannya: butir survei mencakup enam aspek yang diminta instrumen, terdapat butir terbuka, dan target jumlah responden sudah ditentukan. Survei yang belum lengkap dikembalikan kepada KaLab untuk dilengkapi. Setelah ditetapkan, survei menunggu tanggal buka, kemudian responden mengisinya selama survei dibuka. Setelah tanggal tutup terlewati, sistem menghitung rekap per aspek.

KaLab kemudian mencatat evaluasi survei dan menetapkan rencana tindak lanjut, dan sistem memperbarui status kriteria K1 sampai K3. Pada periode berikutnya, setelah survei periode itu dianalisis, KaLab menilai efektivitas tindak lanjut sebelumnya, dan sistem memperbarui status kriteria K4. Sistem hanya menunjukkan kriteria tertinggi yang datanya sudah lengkap; skor akhir tetap ditetapkan oleh penilai monev.

#### 2.3.2.6 Diagram Mesin Status Sesi

Sesi praktikum adalah objek utama modul ini. Sesi dipakai pula oleh modul lain, misalnya modul SDM yang menghitung penugasan petugas per sesi. Status sesi digambarkan pada Gambar 2.6.

> [Gambar 2.6 Diagram Mesin Status Sesi] `activity-state-praktikum.drawio`, halaman "State Machine TO-BE (1-3) - Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.6, sesi hanya memiliki tiga status: Terjadwal, Terlaksana, dan Batal. Jumlah ini disepakati bersama dalam kontrak data bersama (Core) agar sama dengan status yang dibaca modul SDM. Sesi berstatus Terjadwal ketika dibangkitkan dari jadwal kelas (A1) atau sebagai sesi pengganti (A4). Sesi menjadi Terlaksana ketika jurnalnya dikirim dan valid, dengan syarat jadwal periodenya sudah dipublikasikan. Sesi menjadi Batal ketika perubahan sesi disetujui, baik dengan sesi pengganti maupun tanpa pengganti. Perubahan ke moda daring tidak mengubah status; sesi tetap Terjadwal dengan moda yang diperbarui. Sesi Terjadwal hanya dapat dihapus melalui impor ulang, dan hanya bila jadwal periodenya tidak sedang diajukan atau disahkan serta sesi tersebut belum memiliki jurnal.

Keadaan lain dari sesi tidak disimpan sebagai status, tetapi dihitung dari data lain. Sesi dianggap sudah dipublikasikan bila penetapan jadwal periodenya sudah disahkan; ditunda bila ada pengajuan perubahan yang belum diputuskan; terlewat bila tanggalnya sudah lewat tetapi jurnalnya belum ada; dan diganti bila ada sesi lain yang merujuknya sebagai sesi asal. Akibatnya, ketika penetapan jadwal dicabut atau pengajuan perubahan ditolak, status sesi tidak perlu diubah, karena keadaannya terbaca langsung dari data tersebut.

Untuk memastikan tidak ada perpindahan status yang terlewat, setiap pasangan status diperiksa dalam tabel status × transisi (Wazlawick, 2024, hlm. 37–38), seperti pada Tabel 2.14. Setiap sel kosong ditanyakan apakah perpindahan tersebut mungkin terjadi.

Tabel 2.14 Tabel Status × Transisi Sesi

| Dari \ Ke | Terjadwal | Terlaksana | Batal |
|---|---|---|---|
| (awal) | bangkitkan; bangkitkan pengganti | — | — |
| Terjadwal | perubahan disetujui [daring] / ubah moda | kirim jurnal [jurnal valid ∧ sudah dipublikasikan] | perubahan disetujui [dengan pengganti atau batal] |
| Terlaksana | tidak diizinkan **[ASUMSI]**: jurnal yang salah dikoreksi tanpa mengubah status, dan koreksinya tercatat di riwayat | — | — |
| Batal | tidak diizinkan: dibuat pengajuan baru untuk sesi pengganti | — | — |

#### 2.3.2.7 Diagram Mesin Status Pengajuan

Pengajuan pemakaian laboratorium (A2) dan pengajuan perubahan sesi (A4) memiliki pola persetujuan yang sama, sehingga keduanya digambarkan dalam satu diagram mesin status pada Gambar 2.7.

> [Gambar 2.7 Diagram Mesin Status Pengajuan] `activity-state-praktikum.drawio`, halaman "State Machine TO-BE (2-3) - Pengajuan Pemakaian dan Perubahan"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.7, pengajuan dimulai dengan status Diajukan. Untuk pemakaian laboratorium, pengajuan hanya dapat dibuat bila waktunya tidak bentrok. Dari status Diajukan terdapat tiga kemungkinan. Pengajuan menjadi Disetujui bila disetujui oleh pejabat berwenang, yaitu KaLab, dan tetap tidak bentrok saat diputuskan; efeknya, jadwal terpadu diperbarui atau sesi diubah sesuai Gambar 2.6. Pengajuan menjadi Ditolak bila ditolak dengan alasan yang terisi. Pengajuan menjadi Ditarik bila pengaju menariknya kembali sebelum diputuskan. Transisi tarik kembali ditemukan melalui tabel status × transisi dan ditandai dengan tanda bintang (\*) pada diagram. Ketiga status tersebut adalah status akhir; pengajuan yang ditolak tidak diajukan ulang, tetapi dibuat pengajuan baru agar riwayat penolakannya tetap ada.

Satu diagram untuk dua jenis pengajuan ini nantinya diwujudkan sebagai satu kelas induk bersama pada *design class diagram* (subbab 2.3.7), sehingga aturan persetujuan cukup ditulis satu kali.

#### 2.3.2.8 Diagram Mesin Status Survei Kepuasan

Status survei kepuasan berkaitan langsung dengan kriteria berurutan K1 sampai K4 pada PKG-20. Status tersebut digambarkan pada Gambar 2.8.

> [Gambar 2.8 Diagram Mesin Status Survei Kepuasan] `activity-state-praktikum.drawio`, halaman "State Machine TO-BE (3-3) - Survei Kepuasan"
>
> Sumber: Rancangan penulis (2026), berkas `activity-state-praktikum.drawio`

Berdasarkan Gambar 2.8, survei dibuat dengan status Draf. Survei menjadi Ditetapkan bila mencakup enam aspek, memiliki butir terbuka, memiliki target respons, dan ditetapkan oleh pejabat berwenang; pada status ini data untuk kriteria K1 dan K2 sudah lengkap. Sebelum tanggal buka, penetapan masih dapat dibatalkan sehingga survei kembali menjadi Draf. Transisi ini ditemukan melalui tabel status × transisi dan ditandai dengan tanda bintang. Setelah tanggal tutup terlewati, KaLab mencatat evaluasi dan rencana tindak lanjut, sehingga survei menjadi Dievaluasi dan kriteria K3 lengkap. Survei menjadi Siklus Selesai setelah efektivitas seluruh rencana tindak lanjutnya dinilai pada periode berikutnya, dan pada titik ini kriteria K4 lengkap.

Selama berstatus Ditetapkan, survei dapat terbaca belum dibuka, sedang dibuka, atau sudah ditutup. Keadaan ini dihitung dari tanggal buka dan tanggal tutup, sehingga tidak disimpan sebagai status tersendiri.

### 2.3.3 *Use Case*

*Use case* sistem adalah satu proses yang dikerjakan aktor dengan sistem dalam satu sesi kerja dan menghasilkan hasil yang utuh bagi aktor tersebut (Wazlawick, 2024, hlm. 43). Langkah seperti "masuk ke sistem" atau "membuka halaman" bukan *use case*, karena tidak menghasilkan apa pun bila dihentikan di tengah jalan. *Use case* modul ini diturunkan dari dua sumber: tugas «user» pada diagram aktivitas (Wazlawick, 2024, hlm. 50) dan peristiwa yang mengubah status pada diagram mesin status (Wazlawick, 2024, hlm. 51). Tugas yang dikerjakan berurutan oleh satu aktor tanpa jeda digabung menjadi satu *use case*; tugas yang dapat dikerjakan pada hari lain atau oleh aktor lain dipisah.

*Use case* yang hanya mengelola data diberi stereotipe «CRUDL» (*create, retrieve, update, delete, list*), dan *use case* yang hanya menampilkan data diberi stereotipe «report». Relasi «include» dan «extend» tidak dipakai, karena setiap *use case* sudah berdiri sendiri dan urutannya sudah digambarkan pada diagram aktivitas.

Aktor adalah peran yang berinteraksi langsung dengan sistem, bukan jabatan atau profil keamanan (Wazlawick, 2024, hlm. 42). Aktor modul ini dijelaskan pada Tabel 2.15.

Tabel 2.15 Deskripsi Aktor

| No | Aktor | Deskripsi |
|---|---|---|
| 1 | *Petugas Praktikum* (aktor abstrak) | Peran orang yang bertugas pada satu sesi. Diperankan oleh Asisten, Dosen, atau Laboran. Dapat membaca modul berlaku, mengirim jurnal sesi, mengajukan perubahan sesi, dan menarik pengajuan |
| 2 | Asisten | Asisten praktikum. Mewarisi seluruh *use case* Petugas Praktikum untuk kelas yang diasistensi |
| 3 | Dosen | Dosen koordinator atau dosen kelas. Mewarisi *use case* Petugas Praktikum. Dapat menerbitkan versi modul, menyetujui penggantian bahan, mencatat penilaian kelas, dan mengimpor nilai kelas |
| 4 | Laboran | Laboran atau teknisi. Mewarisi *use case* Petugas Praktikum. Dapat mengelola mata kuliah dan kelas, mengimpor jadwal kelas, menyusun penetapan jadwal, mencatat pengajuan pemakaian laboratorium, memeriksa kesiapan sesi, dan mencatat penilaian kelas |
| 5 | KaLab | Kepala Laboratorium. Dapat mengesahkan jadwal, memutuskan pemakaian laboratorium dan perubahan sesi, menyusun dan menetapkan survei, mencatat evaluasi survei dan menilai efektivitas tindak lanjut, melihat status monev, menerbitkan laporan bukti, dan mengatur modul |
| 6 | Responden | Praktikan, dosen, atau asisten yang menjadi sasaran survei. Dapat mengisi survei kepuasan tanpa akun dan tanpa nama |

Pengguna laboratorium di luar praktikum tidak menjadi aktor karena tidak memiliki akun; permintaannya dicatat oleh laboran. Tim jadwal fakultas, pejabat penanda tangan, penilai monev, serta LeADS, SIAKAD, dan SIMPEL juga bukan aktor, karena tidak berinteraksi langsung dengan sistem. Modul ini juga tidak memiliki aktor penjadwal waktu, karena keadaan yang bergantung pada waktu, seperti sesi terlewat atau survei sedang dibuka, dihitung saat dibaca, bukan dijadwalkan.

Diagram *use case* dibagi menjadi tiga halaman menurut area. Halaman pertama ditunjukkan pada Gambar 2.9.

> [Gambar 2.9 Diagram *Use Case* Jadwal, Modul, dan Pemakaian Laboratorium] `use-case-praktikum.drawio`, halaman "UC TO-BE (1-3) - Jadwal, Modul, dan Pemakaian Lab"
>
> Sumber: Rancangan penulis (2026), berkas `use-case-praktikum.drawio`

Berdasarkan Gambar 2.9, paket Jadwal berisi lima *use case*. Laboran mengelola data mata kuliah (UC-PRK-01) dan kelas (UC-PRK-02), mengimpor jadwal kelas yang sekaligus membangkitkan sesi (UC-PRK-03), dan menyusun penetapan jadwal periode (UC-PRK-04). Laboran, KaLab, dan Petugas Praktikum dapat melihat laporan jadwal yang memuat jadwal terpadu dan rekaman konflik (UC-PRK-10). Pengajuan dan pengesahan penetapan jadwal tidak dibuat ulang, tetapi memakai *use case* pengesahan dokumen milik modul Tata Kelola (Ajukan, Terbitkan Dokumen Resmi, Unggah Dokumen Bertanda Tangan, Kembalikan, Sahkan, dan Cabut Dokumen). Paket Modul berisi penerbitan versi modul oleh dosen (UC-PRK-05) dan pembacaan modul berlaku oleh Petugas Praktikum (UC-PRK-06). Paket Pemakaian Lab berisi pencatatan pengajuan oleh laboran (UC-PRK-07), keputusan oleh KaLab (UC-PRK-08), dan penarikan pengajuan sebelum diputuskan (UC-PRK-09).

Halaman kedua memuat pelaksanaan sesi dan hierarki aktor, seperti pada Gambar 2.10.

> [Gambar 2.10 Diagram *Use Case* Kesiapan dan Pelaksanaan Sesi] `use-case-praktikum.drawio`, halaman "UC TO-BE (2-3) - Pelaksanaan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `use-case-praktikum.drawio`

Berdasarkan Gambar 2.10, paket Kesiapan berisi pemeriksaan kesiapan sesi oleh laboran (UC-PRK-11) dan persetujuan penggantian bahan oleh dosen (UC-PRK-12). Paket Pelaksanaan Sesi berisi pengiriman jurnal sesi (UC-PRK-13) dan pengajuan perubahan sesi (UC-PRK-14) oleh Petugas Praktikum, keputusan perubahan sesi oleh KaLab (UC-PRK-15), dan laporan pelaksanaan (UC-PRK-16). Keputusan tunda pada pemeriksaan kesiapan tidak dihubungkan dengan «include», karena pengajuan perubahan merupakan *use case* tersendiri yang juga dapat dilakukan tanpa pemeriksaan kesiapan. Bagian kanan diagram menunjukkan hierarki aktor: Asisten, Dosen, dan Laboran adalah turunan Petugas Praktikum, sehingga ketiganya dapat mengerjakan seluruh *use case* Petugas Praktikum.

Halaman ketiga memuat penilaian, kepuasan, dan status monev, seperti pada Gambar 2.11.

> [Gambar 2.11 Diagram *Use Case* Penilaian, Kepuasan, dan Status Monev] `use-case-praktikum.drawio`, halaman "UC TO-BE (3-3) - Penilaian, Kepuasan, dan Status Monev"
>
> Sumber: Rancangan penulis (2026), berkas `use-case-praktikum.drawio`

Berdasarkan Gambar 2.11, paket Penilaian Individual berisi pencatatan penilaian kelas (UC-PRK-17) dan impor nilai kelas (UC-PRK-18) oleh dosen atau laboran. Paket Kepuasan Pengguna berisi penyusunan survei (UC-PRK-19), penetapan survei (UC-PRK-20), pembatalan penetapan (UC-PRK-21), pencatatan evaluasi (UC-PRK-23), penilaian efektivitas tindak lanjut (UC-PRK-24), dan laporan survei (UC-PRK-25) oleh KaLab, serta pengisian survei oleh Responden (UC-PRK-22). Paket Status Monev berisi laporan status monev (UC-PRK-26), penerbitan laporan bukti untuk penilai (UC-PRK-27), dan pengaturan modul (UC-PRK-28).

Secara keseluruhan modul ini memiliki 28 *use case*: 24 lapis Inti dan 4 lapis Pelengkap (UC-PRK-09, 16, 18, dan 21). Deskripsi *use case* selain «CRUDL» dan «report» ditunjukkan pada Tabel 2.16. Kolom Aturan merujuk kode aturan bisnis pada subbab 2.3.4.

Tabel 2.16 Deskripsi *Use Case*

| *Use case* | Tujuan | Aktor | Prakondisi | Pascakondisi | Aturan |
|---|---|---|---|---|---|
| UC-PRK-03 Impor Jadwal Kelas | Membangkitkan sesi bertanggal semua kelas satu periode dari berkas jadwal fakultas | Laboran | Periode, ruang, dan dosen terdaftar | Mata kuliah dan kelas baru tercatat; 16 sesi Terjadwal per kelas; peringatan kapasitas tercatat | AB-PRK-01–04 |
| UC-PRK-04 Susun Penetapan Jadwal | Menyiapkan dokumen jadwal periode untuk disahkan | Laboran | Ada sesi untuk periode itu | Penetapan jadwal berstatus Draf; selanjutnya diajukan dan disahkan melalui *use case* Tata Kelola | AB-PRK-05 |
| UC-PRK-05 Terbitkan Versi Modul | Menyediakan modul berlaku sebelum sesi | Dosen | Dosen mengampu mata kuliah itu pada periode tersebut | Versi baru berlaku; versi lama Diganti | AB-PRK-07–09 |
| UC-PRK-06 Baca Modul Berlaku | Membaca modul berlaku untuk mata kuliah yang diampu atau diasistensi | Petugas Praktikum | — | Tidak ada perubahan data | — |
| UC-PRK-07 Ajukan Pemakaian Lab | Mencatat permintaan pemakaian ruang di luar praktikum | Laboran | — | Pengajuan Diajukan; KaLab diberi tahu | AB-PRK-01 |
| UC-PRK-08 Putuskan Pemakaian Lab | Menyetujui atau menolak pemakaian ruang | KaLab | Ada pengajuan Diajukan | Pengajuan Disetujui dan masuk jadwal terpadu, atau Ditolak dengan alasan | AB-PRK-01, 10 |
| UC-PRK-09 Tarik Pengajuan | Membatalkan pengajuan sebelum diputuskan | Petugas Praktikum | Ada pengajuan Diajukan oleh aktor | Pengajuan Ditarik | AB-PRK-11 |
| UC-PRK-11 Periksa Kesiapan Sesi | Menyatakan alat, perangkat lunak, utilitas, dan bahan siap sebelum sesi | Laboran | Ada sesi yang sudah dipublikasikan hari itu | Pemeriksaan tercatat dengan butir dan keputusan | AB-PRK-13–16 |
| UC-PRK-12 Setujui Substitusi Bahan | Mengesahkan bahan pengganti | Dosen | Ada butir bahan yang diganti pada kelas yang diampu | Penggantian disetujui | AB-PRK-16 |
| UC-PRK-13 Kirim Jurnal Sesi | Merekam pelaksanaan sesi | Petugas Praktikum | Ada sesi yang sudah dipublikasikan dan sudah berlangsung | Jurnal terkirim; sesi Terlaksana | AB-PRK-17–21 |
| UC-PRK-14 Ajukan Perubahan Sesi | Meminta sesi dipindah, dijadikan daring, atau dibatalkan | Petugas Praktikum | Ada sesi Terjadwal | Perubahan Diajukan; sesi terbaca ditunda; KaLab diberi tahu | AB-PRK-12 |
| UC-PRK-15 Putuskan Perubahan Sesi | Memutuskan perubahan dan membangkitkan sesi pengganti | KaLab | Ada perubahan Diajukan | Perubahan Disetujui atau Ditolak; bila disetujui, sesi asal Batal dengan sesi pengganti, Batal tanpa pengganti, atau tetap Terjadwal bermoda daring | AB-PRK-01, 10, 12 |
| UC-PRK-17 Catat Penilaian Kelas | Menautkan bukti penilaian individual kelas | Dosen, Laboran | Kelas terdaftar | Penilaian kelas tercatat dengan tautan LeADS | AB-PRK-23 |
| UC-PRK-18 Impor Nilai Kelas | Mengimpor nilai per praktikan dari ekspor Excel LeADS | Dosen, Laboran | Ada penilaian kelas | Baris nilai per NIM tercatat; kelengkapan P1–P4 terhitung | AB-PRK-24, 25 |
| UC-PRK-19 Susun Survei Kepuasan | Menyusun survei periode | KaLab | Periode terdaftar | Survei Draf dengan butir beraspek | — |
| UC-PRK-20 Tetapkan Survei Kepuasan | Menetapkan survei sebelum dibuka | KaLab | Ada survei Draf | Survei Ditetapkan; tautan pengisian tersedia | AB-PRK-26 |
| UC-PRK-21 Batalkan Penetapan Survei | Mengembalikan survei ke Draf | KaLab | Survei Ditetapkan dan belum dibuka | Survei Draf | AB-PRK-27 |
| UC-PRK-22 Isi Survei Kepuasan | Memberi penilaian kepuasan | Responden | Survei sedang dibuka | Respons anonim tercatat | AB-PRK-28 |
| UC-PRK-23 Catat Evaluasi Survei | Menganalisis hasil dan menetapkan tindak lanjut | KaLab | Survei Ditetapkan dan tanggal tutup sudah lewat | Evaluasi dan rencana tindak lanjut tercatat; survei Dievaluasi | AB-PRK-29 |
| UC-PRK-24 Nilai Efektivitas Tindak Lanjut | Menilai apakah tindak lanjut memperbaiki aspek | KaLab | Survei Dievaluasi dan survei periode berikutnya Dievaluasi | Setiap tindak lanjut memiliki penilaian efektivitas; survei Siklus Selesai | AB-PRK-30 |
| UC-PRK-27 Terbitkan Laporan Bukti | Menghasilkan laporan resmi per indikator untuk penilai | KaLab | — | Laporan bukti periode tersedia | — |

*Use case* «CRUDL» dan «report» memakai satu pola bersama (Wazlawick, 2024, hlm. 101). Pada «CRUDL», aktor menyerahkan, memilih, mengubah, menghapus, atau menyaring data, dan sistem menampilkan hasilnya; penghapusan ditolak bila data masih dirujuk data lain. Pada «report», aktor menyerahkan saringan laporan dan sistem menampilkan isinya tanpa mengubah data. *Use case* yang mengikuti pola tersebut ditunjukkan pada Tabel 2.17.

Tabel 2.17 *Use Case* «CRUDL» dan «report»

| *Use case* | Stereotipe | Isi |
|---|---|---|
| UC-PRK-01 Kelola Mata Kuliah | «CRUDL» | Kode (unik), nama, program studi |
| UC-PRK-02 Kelola Kelas | «CRUDL» | Mata kuliah, periode, nama kelas, jumlah mahasiswa, dosen |
| UC-PRK-28 Kelola Pengaturan Praktikum | «CRUDL» | Ambang durasi minimal, batas hari pengisian jurnal, sah tidaknya sesi daring, batas lulus |
| UC-PRK-10 Lihat Laporan Jadwal | «report» | Jadwal terpadu per ruang dan rekaman konflik |
| UC-PRK-16 Lihat Laporan Pelaksanaan | «report» | Rekap kesiapan per ruang dan keterlaksanaan per kelas |
| UC-PRK-25 Lihat Laporan Survei | «report» | Responden, tingkat respons, rerata per aspek, jawaban terbuka, perbandingan antarperiode, tindak lanjut |
| UC-PRK-26 Lihat Status Monev Praktikum | «report» | Persentase PKG-15–18 dengan daftar sesi yang tidak memenuhi, kelas berbukti PKG-19, kriteria tertinggi PKG-20 |

### 2.3.4 *Expanded Use Case* dan Aturan Bisnis

*Expanded use case* merinci satu *use case* menjadi pasangan langkah antara aktor dan sistem. Alur utama ditulis lurus tanpa percabangan; pilihan yang sah ditulis sebagai varian, sedangkan keadaan yang membuat langkah tidak dapat diteruskan ditulis sebagai eksepsi, masing-masing dengan akhir yang jelas: berhasil, gagal, atau kembali ke langkah tertentu (Wazlawick, 2024, hlm. 91–95). Alur lengkap disusun untuk lima *use case* kunci, yaitu UC-PRK-03 Impor Jadwal Kelas, UC-PRK-11 Periksa Kesiapan Sesi, UC-PRK-13 Kirim Jurnal Sesi, UC-PRK-15 Putuskan Perubahan Sesi, dan UC-PRK-23 Catat Evaluasi Survei. Kelimanya dipilih karena memuat aturan paling banyak dan menjadi sumber bukti utama indikator. Sebagai contoh, alur UC-PRK-13 ditunjukkan pada Tabel 2.18; alur keempat *use case* lainnya dimuat di lampiran.

Tabel 2.18 *Expanded Use Case* UC-PRK-13 Kirim Jurnal Sesi

| Langkah | Aktor (Petugas Praktikum) | Sistem |
|---|---|---|
| 1–2 | Meminta daftar sesi kelasnya yang sudah berlangsung dan belum memiliki jurnal terkirim | Menampilkan daftar sesi: mata kuliah, kelas, pertemuan ke-, jenis pertemuan, tanggal, jam rencana, ruang, moda, dan penanda terlewat |
| 3–4 | Memilih satu sesi | Menampilkan identitas sesi, versi modul berlaku, petugas yang ditugaskan (dari modul SDM, bila ada), dan jumlah mahasiswa kelas [E1] |
| 5–6 | Menyerahkan jam mulai dan selesai aktual, topik, versi modul yang dipakai, jumlah praktikan hadir, tautan presensi SIMPEL (opsional), kendala, foto, presensi petugas, dan entri *log book* [V1] | Menampilkan jurnal lengkap beserta penanda petugas yang tidak sesuai penugasan [E2] |
| 7–8 | Mengirim jurnal | Menampilkan jurnal terkirim, waktu kirim, sesi berstatus Terlaksana, dan penanda terlambat bila ada [E3] |
| V1 | Menyimpan isian sebagai draf | Menampilkan jurnal berstatus draf; *use case* berhasil dan dapat dilanjutkan dari langkah 5 |
| E1 | Sesi tidak Terjadwal, belum dipublikasikan, belum berlangsung, atau sudah memiliki jurnal terkirim (AB-PRK-17) | Menampilkan alasannya; *use case* gagal |
| E2 | Jam selesai tidak setelah jam mulai (AB-PRK-18) | Menampilkan jam yang bermasalah; kembali ke langkah 5 |
| E3 | Isian wajib belum lengkap (AB-PRK-19) | Menampilkan bagian yang kurang; kembali ke langkah 5 |

Berdasarkan Tabel 2.18, data yang sudah ada di sistem, seperti identitas sesi dan versi modul berlaku, ditampilkan sistem dan tidak diketik ulang oleh petugas (KNF-PRK-05). Setiap eksepsi merujuk satu kode aturan bisnis, sehingga aturan yang sama dapat diuji pada subbab 2.4.

Aturan bisnis adalah ketentuan yang harus dipenuhi agar suatu *use case* dapat diselesaikan. Setiap aturan bisnis pada umumnya melahirkan satu eksepsi pada alur *use case*, yaitu keadaan ketika aturan tersebut dilanggar dan sistem menolak atau mengembalikan masukan aktor (Wazlawick, 2024, hlm. 91–95). Aturan bisnis modul ini disusun dari kriteria instrumen dan rincian alur *use case*, lalu diberi kode AB-PRK agar dapat dirujuk dari *use case*, rancangan kelas, dan skenario pengujian. Aturan pengesahan jadwal tidak ditulis ulang karena memakai aturan pengesahan dokumen milik modul Tata Kelola. Katalog aturan bisnis ditunjukkan pada Tabel 2.19.

Tabel 2.19 Katalog Aturan Bisnis

| Kode | Aturan | Dasar |
|---|---|---|
| **Jadwal dan sesi** | | |
| AB-PRK-01 | Dua sesi luring yang Terjadwal, atau sesi luring dan pemakaian laboratorium yang Disetujui, tidak boleh memakai ruang yang sama pada waktu yang beririsan. Sesi daring tidak memakai ruang | PKG-15 C2 |
| AB-PRK-02 | Satu sesi asli untuk setiap pasangan kelas dan pertemuan. Setiap kelas dibangkitkan 16 pertemuan; pertemuan 8 berjenis UTS dan pertemuan 16 berjenis UAS | Kontrak Core |
| AB-PRK-03 | Bila jumlah mahasiswa kelas melebihi kapasitas ruang, sistem memberi peringatan; sesi tetap tersimpan tetapi tidak memenuhi C3 | PKG-15 C3 |
| AB-PRK-04 | Impor jadwal hanya dapat dilakukan selama periode itu tidak memiliki penetapan jadwal yang Diajukan atau Disahkan; sesi yang sudah memiliki jurnal tidak diganti | PKG-15 C1 |
| AB-PRK-05 | Paling banyak satu penetapan jadwal aktif per periode; penetapan hanya dapat diajukan bila setiap kelas periode itu memiliki sesi | PKG-15 C1 |
| AB-PRK-06 | Sesi terbaca sudah dipublikasikan bila penetapan jadwal periodenya Disahkan; tanggal publikasi sama dengan tanggal pengesahan | PKG-15 C1 |
| **Versi modul** | | |
| AB-PRK-07 | Hanya satu versi berlaku per mata kuliah per periode; versi lama menjadi Diganti saat versi baru terbit | PKG-15 C4 |
| AB-PRK-08 | Versi modul hanya dapat terbit bila memiliki berkas atau tautan LeADS dan nomor versi yang unik | PKG-15 C4, PKG-19 P2 |
| AB-PRK-09 | Dosen hanya dapat menerbitkan modul untuk mata kuliah yang diampunya | KNF-PRK-02 |
| **Pengajuan** | | |
| AB-PRK-10 | Pengajuan diputuskan oleh pemegang wewenang, yaitu KaLab; penolakan wajib disertai alasan | Keputusan modul |
| AB-PRK-11 | Pengajuan hanya dapat ditarik oleh pengaju selama berstatus Diajukan | Tabel status × transisi |
| AB-PRK-12 | Perubahan hanya untuk sesi Terjadwal; perubahan berjenis pindah wajib menyertakan usulan waktu dan ruang pengganti yang memenuhi AB-PRK-01 | PKG-18 C2 |
| **Kesiapan** | | |
| AB-PRK-13 | Satu pemeriksaan kesiapan per sesi yang sudah dipublikasikan; pemeriksaan yang dicatat pada atau setelah jam mulai tetap tersimpan tetapi tidak memenuhi S1 | PKG-16 S1 |
| AB-PRK-14 | Butir perangkat lunak dan bahan dibentuk dari versi modul berlaku; perangkat lunak berbayar wajib bertanda lisensi sah; data alat bersama hanya menjadi peringatan dan isian awal | PKG-16 S2–S3, PKG-17 B1 |
| AB-PRK-15 | Keputusan siap hanya bila tidak ada butir bermasalah | PKG-16 S4 |
| AB-PRK-16 | Penggantian bahan wajib mencatat bahan pengganti dan alasan, dan baru sah setelah disetujui dosen kelas | PKG-17 B3 |
| **Pelaksanaan sesi** | | |
| AB-PRK-17 | Jurnal hanya untuk sesi Terjadwal yang sudah dipublikasikan dan sudah berlangsung; satu jurnal terkirim per sesi | PKG-18 C1 |
| AB-PRK-18 | Jam selesai aktual harus setelah jam mulai aktual | PKG-18 C3 |
| AB-PRK-19 | Jurnal hanya dapat dikirim bila ada presensi dosen dan laboran, jumlah praktikan hadir, versi modul yang dipakai, dan minimal satu entri *log book*; presensi asisten wajib bila sesi berasisten | PKG-18 C4–C5 |
| AB-PRK-20 | Petugas hadir yang tidak ada di penugasan, atau ditugaskan tetapi tidak hadir, hanya ditandai | Pelengkap |
| AB-PRK-21 | Jurnal yang dikirim melewati batas hari setelah sesi ditandai terlambat | Pelengkap |
| AB-PRK-22 | Sesi memenuhi PKG-18 bila durasi aktual tidak kurang dari ambang; sesi daring hanya sah bila pengaturan mengizinkan; sesi yang diganti memenuhi bila penggantinya terlaksana sebelum periode berakhir | PKG-18 C2–C3 |
| **Penilaian** | | |
| AB-PRK-23 | Satu penilaian kelas per kelas, dengan tautan LeADS wajib | PKG-19 |
| AB-PRK-24 | Nilai hasil impor hanya memuat NIM tanpa nama; impor ulang mengganti seluruh baris kelas, dan berkas lama tetap tersimpan | KNF-PRK-03 |
| AB-PRK-25 | Praktikan lengkap bila memiliki tugas individual, modulnya memiliki rubrik, ada umpan balik, dan sudah diremediasi bila nilainya di bawah batas lulus | PKG-19 P1–P4 |
| **Kepuasan** | | |
| AB-PRK-26 | Survei hanya dapat ditetapkan bila keenam aspek memiliki butir, ada butir terbuka, populasi dan target respons terisi, tanggal buka setelah tanggal penetapan, tanggal tutup setelah tanggal buka, dan penetap berwenang | PKG-20 K1–K2 |
| AB-PRK-27 | Penetapan survei hanya dapat dibatalkan sebelum tanggal buka | Tabel status × transisi |
| AB-PRK-28 | Respons anonim dan hanya diterima selama survei dibuka | PKG-20 K3 |
| AB-PRK-29 | Evaluasi hanya dicatat setelah tanggal tutup, satu per survei; setiap tindak lanjut wajib memiliki aspek, tindakan, penanggung jawab, dan tenggat | PKG-20 K3–K4 |
| AB-PRK-30 | Efektivitas tindak lanjut hanya dinilai bila survei periode berikutnya sudah dievaluasi | PKG-20 K4 |
| **Umum dan status monev** | | |
| AB-PRK-31 | Rekaman bukti tidak dapat dihapus, hanya dikoreksi dengan jejak; master hanya dapat dihapus bila belum dirujuk sesi | KNF-PRK-07 |
| AB-PRK-32 | Persentase PKG-15–18 per periode sama dengan jumlah sesi yang memenuhi dibagi jumlah sesi pembagi; PKG-17 dinyatakan tidak berlaku bila tidak ada sesi berbahan | PKG-15–18 |
| AB-PRK-33 | Persentase PKG-19 sama dengan jumlah kelas yang memiliki tautan penilaian dan rubrik dibagi seluruh kelas periode | PKG-19 |
| AB-PRK-34 | Kriteria tertinggi PKG-20 adalah kriteria K1–K4 tertinggi yang datanya lengkap secara berurutan; skor akhir ditetapkan penilai | PKG-20 |

Setiap kriteria instrumen memiliki sedikitnya satu aturan bisnis yang dapat diuji, sehingga katalog ini sekaligus menjadi dasar skenario pengujian pada subbab 2.4.

### 2.3.5 *System Sequence Diagram*

*System sequence diagram* (SSD) menggambarkan pertukaran informasi antara aktor dan sistem pada satu *use case*, dengan sistem dipandang sebagai kotak hitam (Wazlawick, 2024). Setiap SSD memiliki tiga garis hidup (*lifeline*): aktor, antarmuka (*boundary*), dan pengendali (*controller*). Aktor hanya berinteraksi dengan antarmuka, sedangkan antarmuka memanggil operasi sistem pada pengendali. Operasi sistem dibedakan menjadi dua jenis menurut prinsip pemisahan perintah dan kueri (*command-query separation*): *command* mengubah data dan tidak mengembalikan nilai, sedangkan *query* hanya membaca data dan mengembalikan hasil tanpa mengubah apa pun. Operasi bersifat *stateless*, artinya identitas pengguna dan rekaman yang dipilih dikirim ulang ke setiap operasi. Alur varian dan eksepsi digambarkan sebagai fragmen `opt`, dan rujukan ke *use case* lain digambarkan sebagai fragmen `ref`.

SSD disusun untuk lima *use case* kunci yang alurnya sudah dirinci pada subbab 2.3.4. *Use case* lain tidak digambar, karena operasinya sudah tercakup dalam daftar operasi dan tidak menambah operasi baru. SSD pertama ditunjukkan pada Gambar 2.12.

> [Gambar 2.12 *System Sequence Diagram* UC-PRK-03 Impor Jadwal Kelas] `ssd-praktikum.drawio`, halaman "SSD TO-BE (1-5) - UC-PRK-03 Impor Jadwal Kelas"
>
> Sumber: Rancangan penulis (2026), berkas `ssd-praktikum.drawio`

Berdasarkan Gambar 2.12, laboran menyerahkan periode, berkas jadwal, dan tanggal pertemuan pertama. Antarmuka membaca berkas menjadi baris jadwal, lalu memanggil *query* `pratinjau_impor()`, yang menghitung 16 tanggal per kelas, bentrok, kelas terkunci, baris salah, dan peringatan kapasitas tanpa menyimpan apa pun. Setelah laboran menyetujui pratinjau, antarmuka memanggil *command* `impor_jadwal()` yang membangkitkan sesi, lalu *query* `ringkasan_jadwal()` untuk menampilkan hasilnya. Fragmen eksepsi menunjukkan penolakan karena bentrok (AB-PRK-01), periode yang terkunci (AB-PRK-04), dan baris yang tidak valid.

> [Gambar 2.13 *System Sequence Diagram* UC-PRK-11 Periksa Kesiapan Sesi] `ssd-praktikum.drawio`, halaman "SSD TO-BE (2-5) - UC-PRK-11 Periksa Kesiapan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `ssd-praktikum.drawio`

Berdasarkan Gambar 2.13, laboran memilih sesi hari itu dari *query* `daftar_sesi()`. *Query* `form_kesiapan()` menyusun butir pemeriksaan dari kategori tetap dan versi modul berlaku, lalu *query* `keputusan_tersedia()` menampilkan keputusan yang sah untuk hasil butir yang diisi. *Command* `catat_pemeriksaan()` menyimpan pemeriksaan, butir, dan waktu periksa. Bila ada bahan yang diganti, fragmen `ref` merujuk UC-PRK-12, yaitu persetujuan penggantian bahan oleh dosen kelas.

> [Gambar 2.14 *System Sequence Diagram* UC-PRK-13 Kirim Jurnal Sesi] `ssd-praktikum.drawio`, halaman "SSD TO-BE (3-5) - UC-PRK-13 Kirim Jurnal Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `ssd-praktikum.drawio`

Berdasarkan Gambar 2.14, Petugas Praktikum memilih sesi dari `daftar_sesi()`, dan *query* `konteks_jurnal()` menampilkan identitas sesi, versi modul berlaku, petugas yang ditugaskan, dan jumlah mahasiswa. *Command* `simpan_jurnal()` menyimpan isian sebagai draf dan boleh diulang, sedangkan *command* `kirim_jurnal()` mengirim jurnal dan mengubah status sesi menjadi Terlaksana. Karena *command* tidak mengembalikan nilai, daftar isian yang kurang pada eksepsi E3 dibaca melalui *query* tersendiri, `cek_kelengkapan_jurnal()`.

> [Gambar 2.15 *System Sequence Diagram* UC-PRK-15 Putuskan Perubahan Sesi] `ssd-praktikum.drawio`, halaman "SSD TO-BE (4-5) - UC-PRK-15 Putuskan Perubahan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `ssd-praktikum.drawio`

Berdasarkan Gambar 2.15, KaLab memilih pengajuan dari `daftar_pengajuan()` dan membaca rinciannya. Untuk perubahan berjenis pindah, *query* `cek_bentrok()` memeriksa waktu dan ruang pengganti sebelum keputusan dikirim. *Command* `putuskan_pengajuan()` mencatat keputusan, dan efeknya bergantung pada jenis perubahan: sesi pengganti dibangkitkan, moda diubah menjadi daring, atau sesi dibatalkan. Garis hidup kedua di sebelah kanan menunjukkan notifikasi keputusan kepada pengaju.

> [Gambar 2.16 *System Sequence Diagram* UC-PRK-23 Catat Evaluasi Survei] `ssd-praktikum.drawio`, halaman "SSD TO-BE (5-5) - UC-PRK-23 Catat Evaluasi Survei"
>
> Sumber: Rancangan penulis (2026), berkas `ssd-praktikum.drawio`

Berdasarkan Gambar 2.16, KaLab memilih survei yang siap dievaluasi, membaca rekap per aspek melalui `rekap_survei()`, lalu menyerahkan kesimpulan per aspek dan rencana tindak lanjut melalui *command* `catat_evaluasi_survei()`. Sistem kemudian menampilkan status survei dan kriteria tertinggi PKG-20 melalui `status_survei()`.

Hasil utama SSD adalah daftar operasi sistem. Operasi utama dari kelima SSD ditunjukkan pada Tabel 2.20; daftar lengkap untuk seluruh *use case* beserta kamus datanya dimuat di lampiran.

Tabel 2.20 Operasi Sistem Utama

| Operasi | Jenis | *Use case* | Masukan utama | Respons sistem | Aturan |
|---|---|---|---|---|---|
| `pratinjau_impor()` | *Query* | UC-PRK-03 | Periode, baris jadwal, tanggal pertemuan pertama | Pratinjau sesi, bentrok, kelas terkunci, baris salah, peringatan kapasitas | AB-PRK-01–04 |
| `impor_jadwal()` | *Command* | UC-PRK-03 | Periode, baris jadwal, tanggal pertemuan pertama | Mata kuliah, kelas, dan 16 sesi Terjadwal per kelas | AB-PRK-01–04 |
| `cek_bentrok()` | *Query* | UC-PRK-03, 07, 08, 15 | Waktu, ruang, rekaman yang dikecualikan | Daftar sesi atau pemakaian yang bentrok | AB-PRK-01 |
| `form_kesiapan()` | *Query* | UC-PRK-11 | Sesi | Butir pemeriksaan dari kategori tetap dan versi modul | AB-PRK-13, 14 |
| `catat_pemeriksaan()` | *Command* | UC-PRK-11 | Sesi, hasil butir, keputusan | Pemeriksaan tersimpan dengan waktu periksa | AB-PRK-13–16 |
| `konteks_jurnal()` | *Query* | UC-PRK-13 | Sesi | Identitas sesi, versi modul, petugas ditugaskan, jumlah mahasiswa | AB-PRK-17 |
| `simpan_jurnal()` | *Command* | UC-PRK-13 | Sesi, isian jurnal | Jurnal draf | AB-PRK-18 |
| `kirim_jurnal()` | *Command* | UC-PRK-13 | Sesi | Jurnal terkirim; sesi Terlaksana | AB-PRK-17, 19 |
| `putuskan_pengajuan()` | *Command* | UC-PRK-08, 15 | Pengajuan, keputusan, alasan, tanda bentrok, usulan pengganti | Pengajuan Disetujui atau Ditolak beserta efeknya | AB-PRK-01, 10, 12 |
| `catat_evaluasi_survei()` | *Command* | UC-PRK-23 | Survei, kesimpulan per aspek, rencana tindak lanjut | Survei Dievaluasi | AB-PRK-29 |
| `status_monev()` | *Query* | UC-PRK-26 | Periode, tanggal acuan | Persentase PKG-15–19 dan kriteria tertinggi PKG-20 | AB-PRK-32–34 |

### 2.3.6 *Conceptual Model*

*Conceptual model* menggambarkan informasi yang harus disimpan sistem, berupa konsep, atribut, dan asosiasi, tanpa *method* dan tanpa unsur teknologi (Wazlawick, 2024). Atribut hanya bertipe sederhana; hubungan dengan konsep lain selalu digambarkan sebagai asosiasi bernama peran dengan multiplisitas di kedua ujungnya, bukan sebagai atribut. Atribut yang dihitung dari data lain diberi tanda garis miring (`/`), misalnya `/is_terpublikasi`, sehingga nilai tersebut tidak disimpan dua kali. Data yang baru muncul ketika status berubah, seperti keputusan pengajuan atau pengiriman jurnal, dimodelkan sebagai konsep kejadian tersendiri, bukan sebagai atribut opsional pada konsep induknya. Model ini dibagi menjadi empat halaman. Halaman pertama ditunjukkan pada Gambar 2.17.

> [Gambar 2.17 *Conceptual Model* Jadwal, Sesi, dan Pengajuan] `conceptual-model-praktikum.drawio`, halaman "CM TO-BE (1-4) - Jadwal, Sesi, dan Pengajuan"
>
> Sumber: Rancangan penulis (2026), berkas `conceptual-model-praktikum.drawio`

Berdasarkan Gambar 2.17, Mata Kuliah dan Kelas adalah master bersama, sedangkan Sesi adalah satu-satunya transaksi bersama. Sesi memiliki tiga status yang disimpan, yaitu terjadwal, terlaksana, dan batal, serta sejumlah atribut turunan seperti `/is_terpublikasi`, `/is_ditunda`, dan `/is_terlewat`. Penetapan Jadwal merupakan turunan konsep Dokumen Disahkan milik modul Tata Kelola, sehingga status dan riwayat pengesahannya tidak digambar ulang. Pemakaian Lab dan Perubahan Sesi adalah turunan konsep abstrak Pengajuan, karena keduanya mengikuti diagram mesin status yang sama. Keputusan Pengajuan dan Penarikan dimodelkan sebagai konsep kejadian. Usulan Pengganti dipisah dari Perubahan Sesi karena hanya ada untuk perubahan berjenis pindah.

> [Gambar 2.18 *Conceptual Model* Versi Modul dan Kesiapan Sesi] `conceptual-model-praktikum.drawio`, halaman "CM TO-BE (2-4) - Versi Modul dan Kesiapan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `conceptual-model-praktikum.drawio`

Berdasarkan Gambar 2.18, Versi Modul memiliki bagian Kebutuhan Software dan Kebutuhan Bahan; Kebutuhan Bahan merujuk master Bahan bersama. Pemeriksaan Kesiapan, paling banyak satu per sesi, terdiri atas Butir Pemeriksaan abstrak dengan empat turunan, yaitu butir utilitas, stasiun kerja, *software*, dan bahan, karena setiap kategori memiliki atribut sendiri. Substitusi Bahan dan Persetujuan Substitusi dimodelkan sebagai konsep kejadian. Alat hanya dibaca untuk peringatan alat yang tidak tersedia.

> [Gambar 2.19 *Conceptual Model* Pelaksanaan Sesi dan Penilaian] `conceptual-model-praktikum.drawio`, halaman "CM TO-BE (3-4) - Pelaksanaan Sesi dan Penilaian"
>
> Sumber: Rancangan penulis (2026), berkas `conceptual-model-praktikum.drawio`

Berdasarkan Gambar 2.19, Jurnal Sesi, paling banyak satu per sesi, terdiri atas Presensi Petugas dan Entri *Log Book* yang berurutan. Pengiriman Jurnal dimodelkan sebagai konsep kejadian yang mencatat waktu kirim dan pengirim. Petugas yang ditugaskan dibaca dari penugasan modul SDM sebagai asosiasi turunan, tidak disalin ke setiap sesi. Penilaian Kelas, satu per kelas, menyimpan tautan LeADS dan, bila nilai diimpor, baris nilai per NIM tanpa nama. Pengaturan Praktikum adalah konsep tunggal (*singleton*) yang menyimpan ambang durasi, batas hari jurnal, sah tidaknya sesi daring, dan batas lulus.

> [Gambar 2.20 *Conceptual Model* Survei Kepuasan Pengguna] `conceptual-model-praktikum.drawio`, halaman "CM TO-BE (4-4) - Survei Kepuasan Pengguna"
>
> Sumber: Rancangan penulis (2026), berkas `conceptual-model-praktikum.drawio`

Berdasarkan Gambar 2.20, Survei memiliki butir beraspek dan menerima Respons yang tidak berasosiasi dengan personel, sehingga anonimitas responden dijamin oleh struktur model, bukan oleh pemeriksaan. Evaluasi Survei terdiri atas Kesimpulan Aspek dan Rencana Tindak Lanjut, sedangkan Penetapan Survei dan Penilaian Efektivitas dimodelkan sebagai konsep kejadian. Ringkasan konsep utama ditunjukkan pada Tabel 2.21.

Tabel 2.21 Konsep Utama *Conceptual Model*

| Konsep | Jenis | Atribut konseptual utama | Relasi dan kardinalitas |
|---|---|---|---|
| Mata Kuliah | Master (Core) | kode «unique», nama, prodi, semester | memiliki Kelas 0..*; memiliki Versi Modul 0..* |
| Kelas | Master (Core) | nama, jumlah_mahasiswa | Mata Kuliah 1; dosen 1..*; Sesi 0..*; Penilaian Kelas 0..1 |
| Sesi | Transaksi (Core) | pertemuan_ke, jenis_pertemuan, moda, tanggal, jam, status; /is_terpublikasi, /is_ditunda, /is_terlewat | Kelas 1; Ruang 0..1; sesi_asal 0..1; Pemeriksaan Kesiapan 0..1; Jurnal Sesi 0..1 |
| Penetapan Jadwal | Transaksi (turunan Dokumen Disahkan) | /tanggal_publikasi, /jumlah_sesi | Periode 1 (satu per periode) |
| Pengajuan (abstrak) | Transaksi | tanggal_ajukan, /status | pengaju 1; Keputusan Pengajuan 0..1; Penarikan 0..1 |
| Pemakaian Lab, Perubahan Sesi | Turunan Pengajuan | keperluan, jam / jenis, alasan | Ruang 1 / Sesi 1; Usulan Pengganti 0..1 |
| Versi Modul | Transaksi | nomor_versi, berkas, tautan_leads, rubrik, tanggal_terbit, status | Mata Kuliah 1; Periode 1; Kebutuhan Software 0..*; Kebutuhan Bahan 0..* |
| Pemeriksaan Kesiapan | Transaksi (rekaman bukti) | waktu_periksa, keputusan, /tepat_waktu | Sesi 1; Butir Pemeriksaan 1..* |
| Jurnal Sesi | Transaksi (rekaman bukti) | jam_aktual, topik, jumlah_hadir, kendala, /status | Sesi 1; Versi Modul 1; Presensi Petugas 1..*; Entri *Log Book* 1..* |
| Penilaian Kelas | Transaksi (rekaman bukti) | tautan_leads, /ada_rubrik, /berbukti | Kelas 1; Baris Nilai 0..* |
| Survei | Transaksi | judul, jenis_responden, populasi, target_response_rate, masa_buka; /response_rate, /kriteria_tertinggi | Butir Survei 1..*; Respons 0..*; Evaluasi Survei 0..1 |
| Evaluasi Survei | Transaksi (rekaman bukti) | — | Kesimpulan Aspek 1..*; Rencana Tindak Lanjut 1..* |
| Pengaturan Praktikum | «singleton» | ambang_durasi, batas_hari_jurnal, sesi_daring_sah, batas_lulus | — |

Status indikator monev tidak dijadikan konsep, karena hanya merupakan hasil hitung dari atribut turunan pada Sesi, Penilaian Kelas, dan Survei. Pemeriksaan kelengkapan dilakukan dengan memastikan setiap data yang dikirim atau dibaca melalui operasi pada Tabel 2.20 memiliki tempat pada model ini.

### 2.3.7 *Design Class Diagram*

*Design class diagram* disusun dari model konseptual dengan empat langkah: menambahkan *method*, memberi arah pada asosiasi, merinci tipe atribut, dan mengubah struktur bila diperlukan oleh platform (Wazlawick, 2024, hlm. 277). Tanggung jawab diberikan kepada kelas yang memegang datanya, bukan dikumpulkan di satu kelas pengendali (Wazlawick, 2024, hlm. 276). Karena sistem dibangun di atas Odoo, setiap kelas diwujudkan sebagai model Odoo, asosiasi diwujudkan sebagai *field* relasi (Many2one, One2many, Many2many), dan aturan bisnis diwujudkan sebagai validasi (*constraint*), *field* hitung (*compute*), atau *method*.

Pewarisan (*inheritance*) dipakai dengan dua cara. Pertama, perilaku yang sama pada beberapa model ditulis satu kali sebagai *mixin*, yaitu model abstrak (*AbstractModel*) yang tidak memiliki tabel sendiri, lalu diwarisi oleh model lain melalui atribut `_inherit`. Kedua, model yang sudah ada, baik model bawaan Odoo maupun model bersama, diperluas dengan `_inherit` tanpa membuat model baru, sehingga *field* dan perilakunya tidak disalin. Modul ini memakai tiga *mixin* bersama dari addon inti, yaitu `labfik.approval.mixin` untuk dokumen yang disahkan, `labfik.evidence.mixin` untuk rekaman bukti yang tidak boleh dihapus, dan `labfik.criteria.mixin` untuk indikator berkriteria K1–K4, ditambah satu *mixin* milik modul ini, yaitu `labfik.praktikum.pengajuan.mixin`.

Notasi diagram mengikuti konvensi kelompok. Jenis kelas dibedakan dengan stereotipe: «AbstractModel» dengan nama miring untuk *mixin*, «Odoo» untuk model bawaan, «Core» untuk model bersama, dan «SDM» untuk model milik modul SDM. Model baru milik modul ini tidak diberi stereotipe. Kepala kelas memuat nama teknis, nama yang mudah dibaca beserta label [M] untuk master atau [T] untuk transaksi, dan `{inherit: …}` bila kelas mewarisi *mixin*. *Field* warisan tidak ditulis ulang. Tanda `+` menandai *method* publik, `#` menandai *method* internal, «override» menandai *method* bawaan yang diganti, dan {hook} menandai *method* yang diisi oleh model turunan. Daftar model ditunjukkan pada Tabel 2.22.

Tabel 2.22 Daftar Model

| Model | Mewarisi | Label | Halaman |
|---|---|---|---|
| `labfik.mata.kuliah`, `labfik.kelas` | — (model bersama, diisi modul ini) | [M] | DCD-1 |
| `labfik.sesi` | Model bersama; diperluas dengan `_inherit` di modul ini | [T] | DCD-1 |
| `labfik.praktikum.jadwal` | `labfik.approval.mixin` | [T] | DCD-1 |
| `labfik.praktikum.impor.jadwal` (+ `.baris`) | *TransientModel* | *wizard* | DCD-1 |
| `labfik.praktikum.pengajuan.mixin` | *AbstractModel*, `mail.thread` | — | DCD-2 |
| `labfik.praktikum.pemakaian` | `labfik.praktikum.pengajuan.mixin` | [T] | DCD-2 |
| `labfik.praktikum.perubahan` | `labfik.praktikum.pengajuan.mixin` | [T] | DCD-2 |
| `labfik.praktikum.modul` (+ `.software`, `.bahan`) | `mail.thread` | [T] | DCD-3 |
| `labfik.praktikum.kesiapan` (+ `.butir`) | `labfik.evidence.mixin` | [T] | DCD-3 |
| `labfik.praktikum.jurnal` (+ `.petugas`, `.logbook`) | `labfik.evidence.mixin` | [T] | DCD-4 |
| `labfik.praktikum.penilaian` (+ `.baris`) | `labfik.evidence.mixin` | [T] | DCD-4 |
| `res.config.settings` | Diperluas dengan `_inherit` | — | DCD-4 |
| `survey.survey`, `survey.question` | Diperluas dengan `_inherit`; `survey.survey` juga mewarisi `labfik.criteria.mixin` | [T] | DCD-5 |
| `labfik.praktikum.evaluasi.survei` (+ `.kesimpulan`, `.rtl`) | `labfik.evidence.mixin` | [T] | DCD-5 |
| `labfik.praktikum.monev` | *AbstractModel* (layanan hitung tanpa tabel) | [R] | DCD-5 |

Halaman pertama *design class diagram* ditunjukkan pada Gambar 2.21.

> [Gambar 2.21 *Design Class Diagram* Jadwal dan Sesi] `class-praktikum.drawio`, halaman "DCD TO-BE (1-5) - Jadwal dan Sesi"
>
> Sumber: Rancangan penulis (2026), berkas `class-praktikum.drawio`

Berdasarkan Gambar 2.21, Mata Kuliah, Kelas, Periode, Ruang Lab, dan Sesi adalah model bersama di addon inti. Sesi di addon inti hanya menyimpan data yang dibutuhkan semua modul: kelas, pertemuan ke-, jenis pertemuan, moda, tanggal, jam, ruang, status, dan sesi asal bila sesi tersebut pengganti. Modul ini memperluas Sesi dengan `_inherit` untuk menambahkan *field* hitung yang datanya berasal dari modul ini, seperti `is_terpublikasi`, `is_ditunda`, `is_terlewat`, dan `melebihi_kapasitas`, serta *method* `cari_bentrok()` yang dipakai bersama oleh impor jadwal, pemakaian laboratorium, dan perubahan sesi. Dengan cara ini addon inti tidak bergantung pada modul mana pun. Penetapan Jadwal mewarisi `labfik.approval.mixin`, sehingga pengajuan, pengunggahan berkas bertanda tangan, pengesahan, pencabutan, dan riwayatnya tidak ditulis ulang. Penetapan Jadwal cukup mengisi *hook* pemeriksaan kelengkapan, yaitu setiap kelas periode itu sudah memiliki sesi. Impor Jadwal adalah model sementara (*TransientModel*) untuk menampilkan pratinjau sebelum sesi dibangkitkan.

Halaman kedua memuat pengajuan, seperti pada Gambar 2.22.

> [Gambar 2.22 *Design Class Diagram* Pengajuan] `class-praktikum.drawio`, halaman "DCD TO-BE (2-5) - Pengajuan"
>
> Sumber: Rancangan penulis (2026), berkas `class-praktikum.drawio`

Berdasarkan Gambar 2.22, pemakaian laboratorium dan perubahan sesi sama-sama mewarisi `labfik.praktikum.pengajuan.mixin`, sesuai dengan satu diagram mesin status pengajuan pada Gambar 2.7. *Mixin* ini memuat status, pengaju, pemutus, tanggal keputusan, alasan penolakan, dan tanda penolakan karena bentrok. Urutan keputusan ditulis satu kali sebagai *Template Method* `action_putuskan()`, yaitu *method* yang menetapkan urutan langkah baku dan menyerahkan langkah yang berbeda kepada *method* *hook* yang diisi model turunan (Gamma dkk., 1994). Urutannya adalah memeriksa status Diajukan, memeriksa wewenang pemutus melalui jabatannya, mewajibkan alasan bila ditolak, menjalankan *hook* `_sebelum_disetujui()`, mencatat keputusan, menjalankan *hook* `_efek_disetujui()`, dan mengirim notifikasi. Isi *hook* untuk masing-masing turunan ditunjukkan pada Tabel 2.23. Dengan pola ini, pemeriksaan wewenang tidak dapat terlewat, karena model turunan tidak menulis ulang `action_putuskan()`.

Tabel 2.23 Isi *Hook* Pengajuan

| Model | Jenis pengajuan | `_sebelum_disetujui()` | `_efek_disetujui()` |
|---|---|---|---|
| `labfik.praktikum.pemakaian` | Pemakaian laboratorium | Tidak ada bentrok dengan sesi luring dan pemakaian lain yang disetujui | — (masuk jadwal terpadu melalui statusnya) |
| `labfik.praktikum.perubahan` | Perubahan sesi | Sesi asal masih Terjadwal; untuk pindah, waktu pengganti tidak bentrok | Pindah: membangkitkan sesi pengganti dan membatalkan sesi asal. Daring: mengubah moda. Batal: membatalkan sesi asal |

Halaman ketiga memuat versi modul dan pemeriksaan kesiapan, seperti pada Gambar 2.23.

> [Gambar 2.23 *Design Class Diagram* Versi Modul dan Kesiapan] `class-praktikum.drawio`, halaman "DCD TO-BE (3-5) - Versi Modul dan Kesiapan"
>
> Sumber: Rancangan penulis (2026), berkas `class-praktikum.drawio`

Berdasarkan Gambar 2.23, Versi Modul memiliki dua tabel anak, yaitu kebutuhan perangkat lunak dan kebutuhan bahan. Kebutuhan bahan merujuk master Bahan bersama. *Method* `get_berlaku()` mengembalikan versi yang berlaku untuk satu mata kuliah pada tanggal tertentu, dan dipakai oleh pemeriksaan kesiapan, jurnal, dan penilaian. Pemeriksaan Kesiapan mewarisi `labfik.evidence.mixin`, sehingga tanggal, pelapor, bukti, dan larangan penghapusan diperoleh dari *mixin*. Butir pemeriksaan dirancang sebagai satu model dengan atribut kategori, bukan empat model terpisah, karena seluruh butir diisi pada satu formulir; isian yang berbeda per kategori dijaga oleh validasi `_cek_isian_kategori()`. Master Alat bersama hanya dibaca untuk menampilkan alat yang tidak tersedia dan jumlah komputer tersedia sebagai isian awal; modul ini tidak mengubah status alat.

Halaman keempat memuat jurnal, penilaian, dan pengaturan, seperti pada Gambar 2.24.

> [Gambar 2.24 *Design Class Diagram* Jurnal, Penilaian, dan Pengaturan] `class-praktikum.drawio`, halaman "DCD TO-BE (4-5) - Jurnal, Penilaian, Pengaturan"
>
> Sumber: Rancangan penulis (2026), berkas `class-praktikum.drawio`

Berdasarkan Gambar 2.24, Jurnal Sesi mewarisi `labfik.evidence.mixin` dan memiliki dua tabel anak, yaitu presensi petugas dan entri *log book*. Presensi petugas merujuk data pegawai, lalu dicocokkan dengan penugasan petugas milik modul SDM untuk menandai petugas yang tidak sesuai penugasan. *Method* `action_kirim()` memeriksa sesi dan kelengkapan isian, mencatat waktu kirim, lalu memanggil `_tandai_terlaksana()` pada Sesi. *Method* tersebut menjadi satu-satunya jalan bagi sesi untuk berstatus Terlaksana. Penilaian Kelas menyimpan tautan LeADS per kelas, dan bila nilai diimpor, menyimpan baris nilai per NIM beserta berkas aslinya. Pengaturan modul memperluas `res.config.settings`, yaitu cara baku Odoo untuk menyimpan satu set nilai pengaturan.

Halaman kelima memuat survei dan status monev, seperti pada Gambar 2.25.

> [Gambar 2.25 *Design Class Diagram* Survei dan Status Monev] `class-praktikum.drawio`, halaman "DCD TO-BE (5-5) - Survei dan Status Monev"
>
> Sumber: Rancangan penulis (2026), berkas `class-praktikum.drawio`

Berdasarkan Gambar 2.25, survei memperluas `survey.survey` bawaan Odoo dan sekaligus mewarisi `labfik.criteria.mixin`. Dari addon `survey` diperoleh formulir publik, respons anonim, dan penyimpanan jawaban, sehingga respons dan jawaban memakai model bawaan tanpa perluasan. Dari `labfik.criteria.mixin` diperoleh atribut hitung `kriteria_tertinggi` dan *method* `get_kriteria()`, sedangkan survei cukup mengisi empat *method* abstrak `_cek_k1()` sampai `_cek_k4()` sesuai kriteria PKG-20. Ini adalah contoh polimorfisme: *mixin* yang sama dapat dipakai modul lain untuk indikator berkriteria K1–K4 dengan isi pemeriksaan yang berbeda. Butir survei memperluas `survey.question` dengan atribut aspek. Evaluasi Survei mewarisi `labfik.evidence.mixin` dan memiliki tabel anak kesimpulan per aspek dan rencana tindak lanjut. Status Monev adalah model abstrak tanpa tabel yang menghitung persentase PKG-15 sampai PKG-19 dan membaca kriteria tertinggi PKG-20 dari rekaman yang ada, lalu menerbitkan laporan bukti.

Setiap aturan bisnis pada Tabel 2.19 diwujudkan dalam mekanisme Odoo. Aturan keunikan, seperti satu jurnal per sesi dan satu pemeriksaan per sesi, diwujudkan dengan batasan basis data (`_sql_constraints`). Aturan antar-*field*, seperti jam selesai setelah jam mulai, diwujudkan dengan validasi `@api.constrains`. Keadaan turunan, seperti sudah dipublikasikan dan persentase indikator, diwujudkan dengan *field* `compute`. Urutan yang tidak boleh terlewat diwujudkan dengan *Template Method* dan *hook*. Pemetaan lengkap aturan bisnis ke mekanismenya dimuat di lampiran.

## 2.4 Rencana Pengujian Proyek

Pengujian dilakukan dengan tiga cara. Pengujian *black box* memeriksa setiap fungsi berdasarkan masukan dan keluarannya, tanpa melihat kode program (Wazlawick, 2024, hlm. 310). Pengujian kecocokan status monev memeriksa apakah angka indikator yang dihitung sistem sama dengan hitungan manual. *User acceptance testing* dilakukan oleh calon pengguna untuk menilai apakah sistem dapat diterima (Wazlawick, 2024, hlm. 307–309). Seluruh pengujian memakai data fiktif.

### 2.4.1 Pengujian *Black Box*

Skenario *black box* diturunkan dari alur utama, varian, dan eksepsi *use case*. Karena setiap eksepsi berasal dari satu aturan bisnis, setiap skenario dikaitkan dengan aturan yang diujinya. Untuk setiap aturan, sedikitnya satu masukan yang diterima dan satu masukan yang ditolak diuji, sesuai teknik pembagian kelas ekuivalen (Wazlawick, 2024, hlm. 310). Skenario juga mencakup perubahan status (misalnya BB-07, BB-23, BB-30, dan BB-42) dan hak akses (BB-10, BB-14, BB-22, BB-28, dan BB-45). Skenario hak akses diturunkan dari grup pengguna dan aturan akses rekaman pada rancangan kelas, yaitu dosen dan asisten hanya mengakses data kelasnya, sedangkan keputusan pengajuan dan status monev hanya untuk KaLab. Skenario pengujian ditunjukkan pada Tabel 2.24. Pengujian belum dilaksanakan; tabel ini adalah rencana.

Tabel 2.24 Skenario Pengujian *Black Box*

| ID | Fitur/Use Case | Skenario Pengujian | Kondisi Awal | Input/Tindakan | Hasil yang Diharapkan |
|---|---|---|---|---|---|
| BB-01 | Impor jadwal (UC-PRK-03) | Impor jadwal valid (AB-PRK-02) | Periode, ruang, dan dosen terdaftar; belum ada penetapan jadwal | Laboran mengimpor berkas jadwal dua kelas dengan ruang yang cukup | 32 sesi Terjadwal dibangkitkan; pertemuan 8 berjenis UTS dan pertemuan 16 berjenis UAS |
| BB-02 | Impor jadwal (UC-PRK-03) | Kapasitas ruang terlampaui (AB-PRK-03) | Ruang berkapasitas 30 | Laboran mengimpor kelas berisi 40 mahasiswa di ruang tersebut | Impor berhasil dengan peringatan kapasitas; sesi kelas itu ditandai tidak memenuhi C3 |
| BB-03 | Impor jadwal (UC-PRK-03) | Bentrok ruang saat impor (AB-PRK-01) | Belum ada sesi pada periode itu | Laboran mengimpor dua kelas luring di ruang, hari, dan jam yang beririsan | Kelas yang bentrok tidak dibangkitkan; pasangan bentrok ditampilkan |
| BB-04 | Impor jadwal (UC-PRK-03) | Periode terkunci (AB-PRK-04) | Penetapan jadwal periode berstatus Diajukan | Laboran mengimpor jadwal untuk periode tersebut | Kelas pada periode itu ditampilkan terkunci dan dilewati |
| BB-05 | Impor jadwal (UC-PRK-03) | Input tidak valid | Periode terdaftar | Laboran mengimpor baris dengan jam selesai sebelum jam mulai, atau ruang yang tidak dikenal | Baris dan kolom bermasalah ditampilkan; tidak ada sesi yang dibangkitkan |
| BB-06 | Penetapan jadwal (UC-PRK-04) | Kelas tanpa sesi (AB-PRK-05) | Ada kelas periode itu yang belum memiliki sesi | Laboran mengajukan penetapan jadwal | Pengajuan ditolak; kelas tanpa sesi ditampilkan |
| BB-07 | Penetapan jadwal (UC-PRK-04) | Perubahan state publikasi (AB-PRK-06) | Penetapan jadwal berstatus Diajukan dengan berkas bertanda tangan | KaLab mengesahkan penetapan, lalu mencabutnya | Setelah disahkan, seluruh sesi periode terbaca sudah dipublikasikan dengan tanggal publikasi sama dengan tanggal sah; setelah dicabut, terbaca belum dipublikasikan |
| BB-08 | Versi modul (UC-PRK-05) | Versi baru menggantikan versi lama (AB-PRK-07) | Versi 1 berlaku | Dosen menerbitkan versi 2 untuk mata kuliah dan periode yang sama | Versi 2 berlaku; versi 1 berstatus Diganti |
| BB-09 | Versi modul (UC-PRK-05) | Input tidak lengkap atau ganda (AB-PRK-08) | Versi 1 berlaku | Dosen menerbitkan versi tanpa berkas dan tanpa tautan, atau dengan nomor versi yang sudah dipakai | Penerbitan ditolak |
| BB-10 | Versi modul (UC-PRK-05) | Hak akses dosen (AB-PRK-09) | Dosen tidak mengampu mata kuliah X | Dosen menerbitkan modul untuk mata kuliah X | Penerbitan ditolak |
| BB-11 | Pemakaian lab (UC-PRK-07) | Bentrok dengan sesi luring (AB-PRK-01) | Ada sesi luring Terjadwal di ruang R | Laboran mencatat pemakaian ruang R pada waktu yang beririsan | Pengajuan ditolak; sesi yang bentrok ditampilkan |
| BB-12 | Pemakaian lab (UC-PRK-07) | Sesi daring tidak memakai ruang (AB-PRK-01) | Sesi di ruang R sudah diubah menjadi daring | Laboran mencatat pemakaian ruang R pada waktu sesi tersebut | Pengajuan diterima |
| BB-13 | Keputusan pemakaian (UC-PRK-08) | Penolakan tanpa alasan (AB-PRK-10) | Ada pengajuan Diajukan | KaLab menolak tanpa mengisi alasan | Penolakan ditolak sistem; alasan diminta |
| BB-14 | Keputusan pemakaian (UC-PRK-08) | Hak akses pemutus (AB-PRK-10) | Ada pengajuan Diajukan | Pengguna tanpa jabatan KaLab, misalnya laboran, memutuskan pengajuan | Keputusan ditolak |
| BB-15 | Tarik pengajuan (UC-PRK-09) | Perubahan state tidak sah (AB-PRK-11) | Pengajuan berstatus Disetujui | Pengaju menarik pengajuan | Penarikan ditolak |
| BB-16 | Kesiapan sesi (UC-PRK-11) | Butir dibentuk dari modul (AB-PRK-14) | Versi modul berlaku mencantumkan dua perangkat lunak dan satu bahan | Laboran membuka pemeriksaan untuk sesi tersebut | Butir kategori tetap, dua butir perangkat lunak, dan satu butir bahan dibuat otomatis |
| BB-17 | Kesiapan sesi (UC-PRK-11) | Pemeriksaan tepat waktu (AB-PRK-13) | Sesi sudah dipublikasikan; jam mulai belum lewat | Laboran mengisi semua butir baik dan menetapkan siap | Pemeriksaan tercatat; sesi memenuhi S1 |
| BB-18 | Kesiapan sesi (UC-PRK-11) | Keputusan tidak sah (AB-PRK-15) | Ada butir bermasalah | Laboran menetapkan keputusan siap | Keputusan ditolak; butir bermasalah ditampilkan |
| BB-19 | Kesiapan sesi (UC-PRK-11) | Substitusi belum disetujui (AB-PRK-16) | Butir bahan diganti dan belum disetujui dosen | Laboran menetapkan keputusan siap | Keputusan ditolak; butir yang menunggu persetujuan ditampilkan |
| BB-20 | Kesiapan sesi (UC-PRK-11) | Pemeriksaan terlambat (AB-PRK-13) | Jam mulai sesi sudah lewat | Laboran mencatat pemeriksaan | Pemeriksaan tersimpan dengan tanda terlambat; sesi tidak memenuhi S1 |
| BB-21 | Kesiapan sesi (UC-PRK-11) | Pemeriksaan ganda (AB-PRK-13) | Sesi sudah memiliki pemeriksaan | Laboran membuat pemeriksaan kedua untuk sesi yang sama | Pemeriksaan yang sudah ada ditampilkan untuk dikoreksi |
| BB-22 | Substitusi bahan (UC-PRK-12) | Hak akses penyetuju (AB-PRK-16) | Ada butir bahan bersubstitusi di kelas A | Dosen yang tidak mengampu kelas A menyetujui substitusi | Persetujuan ditolak |
| BB-23 | Jurnal sesi (UC-PRK-13) | Pengiriman berhasil (AB-PRK-17) | Sesi sudah dipublikasikan dan sudah berlangsung | Asisten mengirim jurnal lengkap | Jurnal terkirim; status sesi berubah dari Terjadwal menjadi Terlaksana |
| BB-24 | Jurnal sesi (UC-PRK-13) | Simpan draf (varian V1) | Sesi sudah berlangsung | Asisten menyimpan isian sebagai draf | Jurnal berstatus draf; sesi tetap Terjadwal |
| BB-25 | Jurnal sesi (UC-PRK-13) | Jam tidak valid (AB-PRK-18) | Sesi sudah berlangsung | Asisten mengisi jam selesai sebelum jam mulai | Pengiriman ditolak; jam bermasalah ditampilkan |
| BB-26 | Jurnal sesi (UC-PRK-13) | Isian wajib kurang (AB-PRK-19) | Sesi sudah berlangsung | Asisten mengirim jurnal tanpa presensi laboran atau tanpa entri *log book* | Pengiriman ditolak; bagian yang kurang ditampilkan |
| BB-27 | Jurnal sesi (UC-PRK-13) | Sesi tidak memenuhi syarat (AB-PRK-17) | Sesi Batal, belum dipublikasikan, atau sudah memiliki jurnal terkirim | Petugas mengirim jurnal untuk sesi tersebut | Pengiriman ditolak dengan alasannya |
| BB-28 | Jurnal sesi (UC-PRK-13) | Hak akses kelas (KNF-PRK-02) | Asisten hanya bertugas di kelas A | Asisten membuka atau mengisi jurnal sesi kelas B | Sesi kelas B tidak tampil dan pengisian ditolak |
| BB-29 | Perubahan sesi (UC-PRK-14) | Pengajuan perubahan (AB-PRK-12) | Sesi Terjadwal | Dosen mengajukan perpindahan dengan usulan waktu dan ruang pengganti | Perubahan Diajukan; sesi terbaca ditunda; KaLab diberi tahu |
| BB-30 | Keputusan perubahan (UC-PRK-15) | Perpindahan disetujui (AB-PRK-12) | Ada perubahan berjenis pindah yang Diajukan; waktu pengganti tidak bentrok | KaLab menyetujui | Sesi asal Batal; sesi pengganti Terjadwal merujuk sesi asal |
| BB-31 | Keputusan perubahan (UC-PRK-15) | Pengganti bentrok (AB-PRK-01) | Waktu pengganti beririsan dengan sesi luring lain | KaLab menyetujui | Keputusan ditolak; sesi atau pemakaian yang bentrok ditampilkan |
| BB-32 | Keputusan perubahan (UC-PRK-15) | Perubahan menjadi daring (AB-PRK-12) | Ada perubahan berjenis daring yang Diajukan | KaLab menyetujui | Sesi tetap Terjadwal dengan moda daring |
| BB-33 | Keputusan perubahan (UC-PRK-15) | Sesi sudah Terlaksana (AB-PRK-12) | Sesi asal sudah Terlaksana | KaLab memutuskan perubahan untuk sesi itu | Keputusan ditolak; status sesi ditampilkan |
| BB-34 | Keputusan perubahan (UC-PRK-15) | Penolakan dengan alasan (AB-PRK-10) | Ada perubahan yang Diajukan | KaLab menolak dengan alasan | Perubahan Ditolak; sesi tidak lagi terbaca ditunda |
| BB-35 | Penilaian kelas (UC-PRK-17) | Input tidak lengkap atau ganda (AB-PRK-23) | Kelas terdaftar | Dosen mencatat penilaian tanpa tautan LeADS, atau mencatat penilaian kedua untuk kelas yang sama | Pencatatan ditolak |
| BB-36 | Impor nilai (UC-PRK-18) | NIM ganda lalu impor ulang (AB-PRK-24) | Kelas memiliki penilaian kelas | Dosen mengimpor berkas dengan NIM ganda, lalu mengimpor ulang berkas yang sudah diperbaiki | Impor pertama ditolak; impor ulang mengganti seluruh baris kelas, hanya NIM tanpa nama yang tersimpan, dan berkas lama tetap ada di riwayat |
| BB-37 | Penetapan survei (UC-PRK-20) | Survei tidak lengkap (AB-PRK-26) | Survei Draf tanpa butir aspek keselamatan atau tanpa target respons | KaLab menetapkan survei | Penetapan ditolak; kekurangan ditampilkan |
| BB-38 | Batalkan penetapan (UC-PRK-21) | Perubahan state tidak sah (AB-PRK-27) | Survei Ditetapkan dan sudah dibuka | KaLab membatalkan penetapan | Pembatalan ditolak |
| BB-39 | Isi survei (UC-PRK-22) | Di luar masa buka (AB-PRK-28) | Survei Ditetapkan | Responden mengisi sebelum tanggal buka atau setelah tanggal tutup | Respons ditolak |
| BB-40 | Isi survei (UC-PRK-22) | Anonimitas respons (AB-PRK-28) | Survei sedang dibuka | Responden mengisi survei melalui tautan tanpa masuk akun | Respons tersimpan tanpa identitas responden |
| BB-41 | Evaluasi survei (UC-PRK-23) | Evaluasi terlalu dini atau tidak lengkap (AB-PRK-29) | Survei Ditetapkan, tanggal tutup belum lewat | KaLab mencatat evaluasi, atau mencatat tindak lanjut tanpa penanggung jawab | Pencatatan ditolak |
| BB-42 | Evaluasi survei (UC-PRK-23) | Perubahan state ke Dievaluasi (AB-PRK-29, 34) | Survei Ditetapkan, tanggal tutup sudah lewat | KaLab mencatat evaluasi lengkap | Survei Dievaluasi; kriteria tertinggi PKG-20 terbaca K3 |
| BB-43 | Efektivitas tindak lanjut (UC-PRK-24) | Survei berikutnya belum dievaluasi (AB-PRK-30) | Survei periode berikutnya belum Dievaluasi | KaLab menilai efektivitas | Penilaian ditolak |
| BB-44 | Rekaman bukti (umum) | Larangan hapus (AB-PRK-31) | Ada jurnal terkirim | Pengguna menghapus jurnal, lalu mengoreksinya | Penghapusan ditolak; koreksi tersimpan beserta riwayatnya |
| BB-45 | Status monev (UC-PRK-26) | Hak akses laporan (KNF-PRK-02) | Pengguna masuk sebagai asisten | Asisten membuka menu status monev | Menu tidak tersedia; akses ditolak |

### 2.4.2 Pengujian Kecocokan Status Monev

Pengujian ini memastikan bahwa angka indikator yang ditampilkan sistem sama dengan hasil hitungan manual pada data uji yang sama. Data uji fiktif disusun untuk satu periode dengan dua kelas, yaitu kelas A yang berasisten dan kelas B tanpa asisten, masing-masing dengan 16 sesi. Rancangan data uji dan hasil yang diharapkan ditunjukkan pada Tabel 2.25. Angka pada tabel ini adalah rancangan awal dan akan disesuaikan saat data uji dibuat.

Tabel 2.25 Rancangan Pengujian Kecocokan Status Monev

| Indikator | Data uji | Hasil yang diharapkan |
|---|---|---|
| PKG-15 | 32 sesi pada jadwal yang disahkan dan modul berlaku; kelas B berisi 40 mahasiswa di ruang berkapasitas 30 | 16 dari 32 sesi memenuhi (50%); 16 sesi kelas B tercantum gagal C3 |
| PKG-16 | 31 sesi terlaksana; 28 diperiksa sebelum jam mulai dengan semua butir baik, 2 diperiksa terlambat, 1 tanpa pemeriksaan | 28 dari 31 sesi memenuhi (90,3%); 3 sesi tercantum beserta kriteria yang gagal |
| PKG-17 | Tidak ada modul yang mencantumkan bahan | Dinyatakan tidak berlaku (N/A) |
| PKG-18 | 32 sesi; 30 jurnal memenuhi, 1 jurnal dengan durasi di bawah ambang, 1 sesi tanpa jurnal | 30 dari 32 sesi memenuhi (93,75%); 2 sesi tercantum gagal C3 dan C1 |
| PKG-19 | Kelas A memiliki tautan LeADS dan rubrik; kelas B memiliki tautan tanpa rubrik | 1 dari 2 kelas berbukti (50%) |
| PKG-20 | Survei ditetapkan lengkap, memiliki respons, evaluasi tercatat, tindak lanjut belum dinilai | Kriteria tertinggi K3 |

Pengujian dinyatakan berhasil bila seluruh angka dan daftar sesi yang tidak memenuhi sama dengan hasil yang diharapkan.

### 2.4.3 *User Acceptance Testing*

*User acceptance testing* dilakukan setelah pengujian *black box* dan pengujian kecocokan status monev selesai. Pengujian melibatkan perwakilan setiap aktor, yaitu KaLab, laboran, dosen, dan asisten **[KONFIRMASI: ketersediaan responden]**. Setiap peserta mengerjakan tugas sesuai perannya dengan data fiktif: laboran mengimpor jadwal dan memeriksa kesiapan sesi, asisten atau dosen mengirim jurnal sesi dan mengajukan perubahan, dosen menerbitkan versi modul, dan KaLab memutuskan pengajuan, menetapkan survei, serta membaca status monev.

Setelah mengerjakan tugas, peserta mengisi kuesioner *System Usability Scale* (SUS) yang terdiri atas sepuluh pernyataan dengan skala 1–5 dan menghasilkan skor 0–100 (Brooke, 1996) **[KONFIRMASI: instrumen UAT seragam untuk satu kelompok]**. Selain skor, catatan kesulitan peserta pada setiap tugas dikumpulkan sebagai bahan perbaikan.

---

## Daftar Pustaka sementara (Bab II)

- Badan Standardisasi Nasional. (2018). *SNI ISO/IEC 17025:2017 Persyaratan umum kompetensi laboratorium pengujian dan laboratorium kalibrasi*. BSN. **[VALIDASI: disamakan dengan entri Bab I; cek judul dan tahun persis]**
- Brooke, J. (1996). SUS: A "quick and dirty" usability scale. Dalam P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Ed.), *Usability evaluation in industry* (hlm. 189–194). Taylor & Francis. **[VALIDASI]**
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley.
- International Organization for Standardization. (2011). *ISO/IEC 25010:2011 Systems and software engineering — Systems and software quality requirements and evaluation (SQuaRE) — System and software quality models*. ISO.
- Universitas Pembangunan Nasional "Veteran" Jakarta. (2026). *Instrumen Monev Laboratorium UPNVJ 2026 v1.1*. **[VALIDASI: penerbit persis]**
- Wazlawick, R. S. (2024). *Object-oriented analysis and design for information systems: Agile modeling with BPMN, OCL, IFML, and Python* (2nd ed.). Morgan Kaufmann/Elsevier.
