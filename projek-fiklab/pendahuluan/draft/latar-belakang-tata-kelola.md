# Draf 1.1 Latar Belakang: Modul Tata Kelola & Dokumen

1 November 2026 (revisi 1) · Febriyan · Draf, belum ditinjau dosen

**Usulan judul (draf):** Kustomisasi Modul Odoo untuk Tata Kelola dan Pengendalian Dokumen Laboratorium Berbasis Instrumen Monev (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

**Penanda:**
- **[KONFIRMASI]**: klaim yang harus dibuktikan dengan wawancara atau dokumen sebelum proposal diajukan.
- **[CEK]**: rujukan yang isinya masih perlu dibaca langsung dari teks lengkapnya.

**Kebijakan rujukan:**
- Utamakan jurnal, standar, dan regulasi.
- Skripsi hanya satu, yaitu Anandar (2026), karena menjadi satu-satunya rujukan penerapan Odoo di LabFIK.
- Bab 1 judul-judul terkait di `pendahuluan/reference/` hanya dipakai sebagai contoh pola penulisan, tidak disitasi.

---

## Rancangan per paragraf

Latar belakang berbentuk corong: dari masalah bersama FIKLAB Compliance mengerucut ke modul Tata Kelola & Dokumen. P2 memuat klaim inti bersama dari [brief-seluruh-projek.md](../../brief/brief-seluruh-projek.md#permasalahan-bersama-untuk-bab-1), tetapi kalimat dan sudut pandangnya milik penulis sendiri, yaitu sisi pengelolaan.

| # | Fungsi | Gagasan utama | Rujukan |
|---|---|---|---|
| P1 | Konteks | Mutu lab dijamin lewat SPMI. Lab UPNVJ kini dinilai dengan instrumen monev yang menuntut **bukti** | Kemendiktisaintek 2025; UPNVJ 2026; BSN 2018 |
| P2 | Permasalahan awal FIKLAB Compliance | Data dan bukti tersebar, dikumpulkan manual menjelang monev, dan tidak terpantau | Wawancara KaLab; Ulya dkk. 2024; Sihombing 2022 |
| P3 | Arah solusi proyek | FIKLAB Compliance: Odoo, 21 indikator, modul fungsional, master data bersama | Nurrohmah dan Wiratama 2023; Anandar 2026 |
| P4 | Mengerucut ke tata kelola | Empat indikator fondasi. Dokumennya belum ada. Bukti "dijalankan/dievaluasi" butuh rekaman dan pengendalian dokumen | BSN 2018; Abdul Rahman dan Awang 2024; wawancara KaLab |
| P5 | Penelitian terdahulu dan celah | Sistem SPMI/AMI, SI lab berbasis ISO 17025, *dashboard* ketercapaian. Celahnya ada pada keterlacakan dari penyusunan dokumen sampai bukti per butir instrumen | Pramudya dkk. 2026; Wijaya dkk. 2022; Nurramadhona dkk. 2025 |
| P6 | Solusi dan penegasan | Modul Tata Kelola & Dokumen, beserta batas klaim sistem | — |

Keterkaitan dengan 1.2 Identifikasi Masalah (M1–M4 di [brief Tata Kelola](../../brief/brief-tata-kelola-dokumen.md#rancangan-proposal)):

| Masalah | Muncul di |
|---|---|
| M1 dokumen tata kelola belum ada | P4, kalimat kondisi LabFIK |
| M2 bukti "dijalankan/dievaluasi" butuh rekaman | P4, kalimat kriteria berurutan |
| M3 pengendalian dokumen belum ada | P4, kalimat ISO 8.3 |
| M4 status dihitung manual dan tidak tertelusur | P2 (masalah bersama) dan P6 |

---

## Draf prosa

**P1.** Laboratorium merupakan sarana utama perguruan tinggi untuk menunjang pelaksanaan tridharma, terutama pembelajaran praktik yang membentuk kompetensi mahasiswa. Mutunya dijamin melalui Sistem Penjaminan Mutu Internal (SPMI), yang wajib dikembangkan setiap perguruan tinggi dan dijalankan dalam siklus penetapan, pelaksanaan, evaluasi, pengendalian, dan peningkatan standar (Kemendiktisaintek 2025). Mulai tahun 2026, laboratorium di lingkungan Universitas Pembangunan Nasional "Veteran" Jakarta dinilai menggunakan Instrumen Monev Laboratorium UPNVJ 2026 v1.1 (UPNVJ 2026). Instrumen ini antara lain mengacu pada SNI ISO/IEC 17025:2017 tentang persyaratan umum kompetensi laboratorium (BSN 2018) **[KONFIRMASI: dasar resmi acuan ISO]**. Standar tersebut tidak hanya mengatur kompetensi teknis, tetapi juga persyaratan manajemen, seperti struktur organisasi, pengendalian dokumen, dan rekaman yang dapat ditelusuri (BSN 2018). Instrumen menilai aspek pengelolaan, pengembangan, persiapan, proses, dan evaluasi praktikum dengan skor 1 sampai 4 per indikator. Indikator yang buktinya tidak dapat diverifikasi diberi skor 1, walaupun kegiatannya telah dilakukan. Dengan demikian, pemenuhan indikator ditentukan oleh tersedianya bukti yang dapat ditelusuri, bukan hanya oleh terlaksananya kegiatan.

**P2.** Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta, yang mengelola delapan ruang praktikum, akan menjalani monev tersebut. Namun, pengelolaannya belum disiapkan untuk menghasilkan bukti. Keputusan, dokumen, dan rekaman kegiatan laboratorium tidak dikelola di satu tempat. Sebagian tercatat di Google Form dan Google Sheets, sebagian berada di LeADS dan SIMPEL, sebagian lagi tersimpan sebagai dokumen kertas atau file perorangan, dan sebagian belum terdokumentasi sama sekali **[KONFIRMASI: wawancara KaLab]**. Akibatnya, bukti harus dikumpulkan dan dihitung secara manual menjelang monev, sulit ditelusuri kembali ke kegiatan asalnya, dan kondisinya tidak dapat dipantau sepanjang periode penilaian. Masalah ini umum di perguruan tinggi. Sistem yang dibangun terpisah per unit menghasilkan data yang ganda dan tidak sinkron (Ulya dkk. 2024), sehingga laporan untuk penilaian mutu seperti akreditasi menjadi tidak konsisten dan sulit diandalkan (Sihombing 2022). Dalam kondisi tersebut, skor laboratorium berisiko rendah bukan karena kegiatannya tidak dilakukan, melainkan karena buktinya tidak tersedia ketika dibutuhkan.

**P3.** Permasalahan tersebut dijawab melalui proyek bersama FIKLAB Compliance, yaitu sistem berbasis Odoo yang dikembangkan oleh beberapa penelitian. Proyek ini mencakup 21 indikator instrumen monev yang dikelompokkan ke dalam modul fungsional: tata kelola dan dokumen, sumber daya manusia dan kompetensi, pelaksanaan praktikum, aset, serta keselamatan. Seluruh modul memakai master data bersama, seperti personel, periode, dan ruang laboratorium, sehingga satu fakta cukup dicatat sekali dan dapat menjadi bukti bagi lebih dari satu indikator. Odoo dipilih karena bersifat *open source* dan dapat dikonfigurasi serta dikustomisasi sesuai kebutuhan organisasi (Nurrohmah dan Wiratama 2023). Penerapannya di LabFIK juga telah dicontohkan oleh Anandar (2026) pada perencanaan asisten praktikum, yang dijadikan rujukan dalam proyek ini. Penelitian ini menangani modul tata kelola dan dokumen.

**P4.** Di antara indikator-indikator tersebut, tata kelola merupakan fondasi. Modul ini mencakup empat indikator: Pengelolaan 1 tentang rencana kerja tahunan; Pengelolaan 2 tentang SOP dan instruksi kerja; Pengelolaan 3 tentang struktur organisasi, tugas, dan wewenang; serta Pengembangan 13 tentang rencana pengembangan yang didasarkan pada analisis kesenjangan. Personel, jabatan, dan dokumen yang ditetapkan pada keempat indikator ini menjadi rujukan bagi indikator lain, misalnya penugasan petugas dan pelaksanaan praktikum. Berdasarkan keterangan Kepala Laboratorium, LabFIK belum memiliki SK pengelola, SOP yang disahkan, rencana kerja, maupun rencana pengembangan **[KONFIRMASI: wawancara tertulis]**. Akibatnya, kriteria pertama keempat indikator belum terpenuhi. Kendala ini juga tidak selesai hanya dengan menyusun dokumen. Tiga dari empat indikator dinilai dengan kriteria berurutan: setelah dokumen disahkan dan isinya lengkap, laboratorium masih harus membuktikan bahwa dokumen itu dijalankan dan dievaluasi. Pembuktian tersebut menuntut rekaman kegiatan, seperti realisasi, rapat koordinasi, dan tinjauan, serta pengendalian dokumen yang mencakup versi berlaku, pengesah yang berwenang, distribusi, dan tinjau ulang, sebagaimana dipersyaratkan klausul 5 dan 8.3 SNI ISO/IEC 17025:2017 (BSN 2018). Persyaratan sistem manajemen seperti ini tidak mudah dipenuhi laboratorium perguruan tinggi. Evaluasi terhadap laboratorium universitas yang lama belum berhasil terakreditasi menemukan bahwa kesesuaiannya terhadap persyaratan sistem manajemen ISO/IEC 17025 (klausul 8) baru sekitar 40% (Abdul Rahman dan Awang 2024).

**P5.** Sejumlah penelitian telah memanfaatkan sistem informasi untuk pembuktian mutu. Pramudya dkk. (2026) mengembangkan aplikasi E-SPMI berbasis web untuk mendukung pelaksanaan audit mutu internal. Wijaya dkk. (2022) menurunkan kebutuhan sistem informasi manajemen laboratorium dari klausul-klausul SNI ISO/IEC 17025:2017 untuk mendukung perencanaan, pengelolaan, dan pelaporan laboratorium. Nurramadhona dkk. (2025) menambahkan fitur analisis ketercapaian standar dan *dashboard* pada aplikasi e-SPMI, sehingga capaian hasil audit tidak lagi dihitung secara manual. Penelitian-penelitian tersebut menangani dokumen mutu di tingkat institusi, operasional laboratorium, atau tahap evaluasi hasil audit secara terpisah. Belum ditemukan penelitian yang menangani tata kelola laboratorium sejak penyusunan dan pengesahan dokumen hingga terbentuknya bukti untuk setiap butir instrumen monev, dengan keterlacakan antara butir instrumen, bukti, dan status pemenuhannya.

**P6.** Oleh karena itu, penelitian ini mengembangkan modul Odoo Tata Kelola dan Dokumen sebagai bagian dari FIKLAB Compliance. Modul ini menuntun laboratorium menyusun dan mengesahkan struktur organisasi, SOP, rencana kerja, dan rencana pengembangan. Modul ini juga mengendalikan versi dokumen, merekam pelaksanaan dan evaluasinya, serta menampilkan status keempat indikator beserta buktinya. Untuk indikator yang dinilai dengan persentase, skor dihitung oleh sistem. Untuk indikator dengan kriteria berurutan, sistem menunjukkan kriteria yang sudah berbukti, sedangkan skor akhir tetap ditetapkan oleh penilai. Pengembangan dilakukan dengan metode **[belum diputuskan]**. Sistem ini diposisikan sebagai alat pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin kenaikan skor monev, karena skor tetap bergantung pada terlaksananya kegiatan oleh pengelola laboratorium.

---

## Daftar pustaka

Format sementara mengikuti pola penulis–tahun; sesuaikan dengan gaya selingkung FIK. Bila ada DOI, tautan memakai DOI. Nomor halaman sengaja tidak dicantumkan.

| # | Rujukan | Tautan | Dipakai di | Status |
|---|---|---|---|---|
| 1 | Abdul Rahman, M. D., & Awang, M. (2024). A critical analysis of ISO/IEC 17025 practices at UniKL MITEC laboratory towards improvement opportunities. *Malaysian Journal of Industrial Technology, 8*(2). | [ejournal.unikl.edu.my/…/658](https://ejournal.unikl.edu.my/index.php/mjit/article/view/658) (tidak ada DOI) | P4 | Teks lengkap dicek: kesesuaian terhadap klausul 8 (persyaratan manajemen) 40%, per subklausul 37,5–42,5%. Celah terbesar di 8.2 dan 8.5; 8.3 dan 8.4 (dokumen, rekaman) celahnya paling kecil. Studi kasus satu lab, jadi jangan dipakai untuk klaim "paling sering" |
| 2 | Anandar, R. (2026). *Pengembangan modul perencanaan asisten praktikum berbasis Odoo OpenEduCat (Studi kasus: Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta)* [Skripsi, UPN "Veteran" Jakarta]. | [repository.upnvj.ac.id/id/eprint/51635](http://repository.upnvj.ac.id/id/eprint/51635) | P3 | Judul dan tahun dicek |
| 3 | Badan Standardisasi Nasional. (2018). *SNI ISO/IEC 17025:2017 Persyaratan umum kompetensi laboratorium pengujian dan laboratorium kalibrasi*. BSN. | Tidak ada tautan publik (dokumen SNI berbayar); salinan di [docs/](../../docs/SNI%20ISO-IEC%2017025-2017_ID.md) | P1, P4 | Teks tersedia |
| 4 | Kementerian Pendidikan Tinggi, Sains, dan Teknologi. (2025). *Peraturan Menteri Pendidikan Tinggi, Sains, dan Teknologi Nomor 39 Tahun 2025 tentang Penjaminan Mutu Pendidikan Tinggi*. | [JDIH Kemdiktisaintek](https://jdih.kemdiktisaintek.go.id/dokumen/Peraturan/d72231a2-03bb-4c77-99ca-ab30af9d9524) · [PDF peraturan.go.id](https://peraturan.go.id/files/permendiktisaintek-no-39-tahun-2025.pdf) | P1 | Teks resmi dicek. Pasal 67 ayat (1): perguruan tinggi wajib melaksanakan penjaminan mutu internal dengan mengembangkan SPMI. Pasal 68 ayat (1): siklus penetapan, pelaksanaan, evaluasi, pengendalian, dan peningkatan standar. Ditetapkan 28 Agustus 2025. Menggantikan Permendikbudristek 53/2023 |
| 5 | Nurramadhona, R. D., Ismail, A., & Arief, S. N. (2025). Integrasi fitur analisis ketercapaian standar dalam aplikasi e-SPMI. *Jurnal Informatika Polinema, 12*(1). | [doi.org/10.33795/jip.v12i1.8432](https://doi.org/10.33795/jip.v12i1.8432) | P5 | Judul, penulis, dan abstrak dicek |
| 6 | Nurrohmah, W. M., & Wiratama, J. (2023). Enterprise resource planning (ERP) SAP Business One evaluation and improvement recommendation using customized Odoo. *Ultima InfoSys: Jurnal Ilmu Sistem Informasi, 13*(2). | [doi.org/10.31937/si.v13i2.2802](https://doi.org/10.31937/si.v13i2.2802) | P3 | Judul, penulis, dan abstrak dicek. Terbit 31 Jan 2023 (label volume 2022) |
| 7 | Pramudya, H. A., Ismail, A., & Arief, S. N. (2026). Pengembangan aplikasi E-SPMI (Sistem Penjaminan Mutu Internal) audit berbasis web Politeknik Negeri Malang. *Jurnal Informatika Polinema, 12*(3). | [doi.org/10.33795/jip.v12i3.9580](https://doi.org/10.33795/jip.v12i3.9580) | P5 | Judul dan penulis dicek. Urutan penulis mengikuti situs jurnal (sebelumnya dicatat "Ismail dkk.") |
| 8 | Sihombing, D. J. C. (2022). Academic data warehouse modeling in higher education using nine-step design methodology. *Journal of Information Systems and Informatics, 4*(4). | [doi.org/10.51519/journalisi.v4i4.399](https://doi.org/10.51519/journalisi.v4i4.399) | P2 | Judul dan abstrak dicek |
| 9 | Ulya, D. I., Khair, A., & Amrozi, Y. (2024). A problem of information system integration at a university in Indonesia. *SAINTEKBU: Jurnal Sains dan Teknologi, 14*(2). | [ejournal.unwaha.ac.id/…/838](https://ejournal.unwaha.ac.id/saintek/article/view/838) (tidak ada DOI) | P2 | Dicek di situs jurnal: label terbitan Vol. 14 No. 02 (Agustus 2022), tetapi tanggal terbit 18 Agustus 2024. Ditulis 2024, mengikuti tanggal terbit (sama seperti Nurrohmah dan Wiratama) |
| 10 | Universitas Pembangunan Nasional "Veteran" Jakarta. (2026). *Instrumen Monev Laboratorium UPNVJ 2026 v1.1*. Dokumen internal. | Dokumen internal; salinan di [docs/](../../docs/) | P1 | Tersedia |
| 11 | Wijaya, G. F., Oktadini, N. R., Sevtiyuni, P. E., & Buchari, M. A. (2022). Adoption of SNI ISO/IEC 17025:2017 principles for laboratory management information system development. *Ultima InfoSys: Jurnal Ilmu Sistem Informasi, 13*(1). | [doi.org/10.31937/si.v13i1.2678](https://doi.org/10.31937/si.v13i1.2678) | P5 | Judul, penulis, dan abstrak dicek |

Komposisi: 7 jurnal, 1 standar, 1 regulasi, 1 dokumen internal, 1 skripsi.

**Perubahan dari revisi sebelumnya:**
- Yeşilören Akal (2025) dikeluarkan. Kalimatnya di P1 diganti dengan rujukan langsung ke SNI ISO/IEC 17025.
- Permendikbudristek 53/2023 sudah **dicabut** dan diganti Permendiktisaintek 39/2025.
- "Ismail dkk. 2026" menjadi "Pramudya dkk. 2026", mengikuti urutan penulis di situs jurnal.
- Nurrohmah dan Wiratama ditulis tahun 2023 (tanggal terbit). Kata "modular" dihapus dari P3 karena tidak ada di abstraknya.

- Keputusan Dekan FIK 3258/2025 dikeluarkan, karena dokumennya belum pernah dibaca langsung (sebelumnya hanya dikenal dari sitasi di skripsi lain).
- Kalimat P4 tentang persyaratan manajemen dilunakkan: dari "paling sering belum dipenuhi" menjadi "tidak mudah dipenuhi". Studi Thailand atas 134 laboratorium (data 2015) justru menemukan 39% ketidaksesuaian pada persyaratan manajemen dan 61% pada persyaratan teknis, sehingga klaim "paling sering" tidak didukung.

**Rujukan yang sengaja tidak dipakai:**
- Skripsi Tiara, Bimasetyo, Nada, dan Haikal, karena skripsi dibatasi.
- Standar SPMI UPNVJ 2025, karena judul resminya belum ditemukan.
- Timotheou dkk. (2023), karena konteksnya sekolah K-12.
- Yeşilören Akal (2025), atas permintaan penulis.
- Keputusan Dekan FIK 3258/UN61/KP.04.00/2025, karena belum pernah dilihat langsung.

## Yang harus dipenuhi sebelum diajukan

- [ ] Wawancara KaLab terdokumentasi (nama, jabatan, tanggal). Isinya:
  - kondisi data dan bukti yang tersebar (P2);
  - status SK, SOP, rencana kerja, dan rencana pengembangan (P4).
- [ ] Dasar resmi bahwa monev mengacu ke ISO 17025. Bila tidak ada, cukup kalimat "antara lain mengacu".
- [ ] Metode pengembangan (P6).
- [ ] Cek similarity P2 terhadap tulisan anggota lain, karena substansinya sama.
