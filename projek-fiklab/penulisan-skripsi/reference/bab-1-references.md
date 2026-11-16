Rafika Anandar: Modul Perencanaan Asisten Praktikum berbasis Odoo OpenEduCat, Lab FIK  
\# \*\*BAB 1 PENDAHULUAN\*\* 

\# \*\*1.1 Latar Belakang\*\* 

Teknologi industri saat ini memainkan peran vital yang didorong secara masif oleh kemajuan IPTEK, terutama dalam bentuk komputerisasi sistem yang diaplikasikan untuk berbagai kebutuhan organisasi secara global (Tanjung 2022). Transformasi digital telah mendorong integrasi teknologi informasi ke dalam proses pembelajaran, menjadikannya lebih efektif dan dinamis. Dalam pendidikan tinggi, teknologi yang relevan adalah \_Enterprise Resource Planning\_ (ERP) yang digunakan untuk mengintegrasikan fungsi bisnis utama guna meningkatkan efisiensi operasional (Sholeh 2024). Untuk memahami kompleksitas ERP, pembelajaran berbasis praktik sangat krusial, sehingga pelaksanaan praktikum yang didukung oleh asisten laboratorium yang kompeten menjadi strategi penting dalam memastikan kualitas pembelajaran (Alkodri \_et al.\_ 2022). 

Laboratorium komputer berfungsi sebagai fasilitas pendidikan utama yang mendukung pengembangan kompetensi mahasiswa melalui kegiatan praktis berbasis digital (Fahrurrozi \_et al.\_ 2024). Integrasi teknologi digital dalam pendidikan telah mentransformasi cara institusi mengelola pembelajaran melalui optimalisasi laboratorium (Timotheou \_et al.\_ 2023). Laboratorium, baik virtual maupun fisik, terbukti mampu meningkatkan keterampilan proses ilmiah serta motivasi belajar mahasiswa (Zhang \_et al.\_ 2023). Oleh karena itu, kegiatan praktikum menjadi bagian krusial di Fakultas Ilmu Komputer UPN "Veteran" Jakarta, yang mencakup berbagai bidang keilmuan dan membutuhkan perencanaan yang matang. 

Pada realitanya, pengelolaan laboratorium di Fakultas Ilmu Komputer UPN "Veteran" Jakarta menghadapi tantangan efisiensi manajemen, khususnya pada fase \_Establish\_ dalam Prosedur Operasional Baku (POB) Manajemen Praktikum. Meskipun Laboratorium FIK UPNVJ telah memiliki \_website\_ , sistem informasi yang tersedia masih terfragmentasi dan belum terintegrasi. Formulir pendaftaran asisten dan modul penjadwalan berada pada halaman yang terpisah, sehingga mengharuskan navigasi berulang, menyulitkan koordinasi, dan menciptakan redundansi data. Masalah utamanya adalah belum adanya subsistem perencanaan 

1 

yang mampu memetakan kebutuhan jumlah asisten berdasarkan rasio praktikan dan kelas. Hal ini menyebabkan proses pendaftaran asisten berjalan tanpa proyeksi kuota yang akurat, sehingga sering memicu ketidakseimbangan alokasi beban kerja asisten. 

Upaya perbaikan sistem ini sejalan dengan kebijakan Fakultas Ilmu Komputer UPN "Veteran" Jakarta dalam memperkuat tata kelola yang efisien dan terpadu, sebagaimana diatur dalam Keputusan Dekan Nomor 3258/UN61/KP.04.00/2025 (Fakultas Ilmu Komputer UPN “Veteran” Jakarta 2025). Urgensi pengembangan sistem terintegrasi ini juga didukung oleh Peraturan Menteri Komunikasi dan Digital Nomor 6 Tahun 2025 tentang Sistem Pemerintahan Berbasis Elektronik (SPBE), yang menekankan pentingnya keterpaduan aplikasi untuk berbagi pakai dan mengintegrasikan proses bisnis (MENTERI KOMUNIKASI DAN DIGITAL REPUBLIK INDONESIA 2025). 

Oleh karena itu, penelitian ini bertujuan untuk mengembangkan sebuah modul perencanaan praktikum berbasis Odoo di Laboratorium FIK UPNVJ. Odoo dipilih sebagai platform ERP karena kemampuannya dalam menyatukan berbagai fungsi manajemen ke dalam satu ekosistem yang terintegrasi. Pengembangan modul ini merupakan langkah strategis untuk menciptakan sistem perencanaan yang lebih terstruktur, terpusat, dan akuntabel, sehingga diharapkan pengelolaan praktikum dapat berjalan lebih efisien dan menjadi model tata kelola digital bagi unit lain. 

\# \*\*1.2 Rumusan Masalah\*\* 

Berdasarkan uraian latar belakang, maka rumusan masalah dalam penelitian ini adalah sebagai berikut: 

1\. Bagaimana merancang modul perencanaan yang terintegrasi dengan sistem pendaftaran asisten praktikum berbasis Odoo OpenEduCat yang sesuai dengan proses bisnis fase \_establish\_ di Laboratorium Fakultas Ilmu Komputer UPNVJ? 

2\. Bagaimana mengimplementasikan rancangan modul perencanaan untuk sistem perencanaan asisten praktikum tersebut ke dalam platform \_Odoo Community Edition\_ dengan modul OpenEduCat? 

2 

3\. Bagaimana tingkat penerimaan pengguna ( \_user acceptance\_ ) terhadap fungsionalitas dan kemudahan penggunaan modul praktikum ERP Odoo yang telah dikembangkan? 

\# \*\*1.3 Batasan Masalah\*\* 

Agar penelitian ini lebih fokus, maka ruang lingkup masalah dibatasi sebagai 

berikut: 

1\. Penelitian ini merupakan proyek riset pengembangan sistem, yang berfokus pada perancangan dan pengembangan modul perencanaan ERP menggunakan Odoo tanpa mencakup implementasi penuh di lingkungan laboratorium. 

2\. Penelitian ini berfokus pada pengembangan modul perencanaan yang memfasilitasi fase \_Establish\_ berdasarkan POB Praktikum FIK. Modul lain seperti \_execute, evaluate, enforce dan enhance\_ tidak akan dibahas. 

3\. Pengembangan dilakukan menggunakan platform Odoo \_Community Edition\_ (versi 17.0) sehingga fitur yang digunakan terbatas pada modul yang tersedia secara open-source. Penelitian tidak membandingkan Odoo dengan platform ERP lainnya. 

4\. Pengujian fungsionalitas dilakukan dengan metode \_black-box testing\_ . Pengujian penerimaan pengguna ( \_user acceptance\_ ) hanya melibatkan mahasiswa, asisten praktikum laboratorium FIK UPNVJ, staff laboran, dan kepala lab sebagai responden. 

\# \*\*1.4 Tujuan dan Manfaat Penelitian\*\* 

Adapun tujuan dari penelitian ini yaitu sebagai berikut: 

1\. Menghasilkan rancangan (desain) arsitektur dan alur kerja modul perencanaan ERP Odoo yang sesuai dengan kebutuhan praktikum Laboratorium FIK UPNVJ. 

2\. Mengimplementasikan dan membangun modul perencanaan pada \_platform\_ Odoo yang fungsional dan siap digunakan untuk kegiatan praktikum. 

3\. Menganalisis dan mengukur tingkat penerimaan pengguna terhadap modul yang telah dikembangkan berdasarkan aspek fungsionalitas dan kemudahan penggunaan. 

3 

Melalui pengembangan sistem ini, penelitian diharapkan dapat memberikan beberapa 

manfaat kedepannya yaitu sebagai berikut: 

1\. Manfaat Praktis 

   \- a. Bagi Laboratorium FIK UPNVJ: Memberikan sistem manajemen fase \_establish\_ yang terintegrasi untuk mengoptimalkan efisiensi alokasi asisten dan transparansi data pendaftaran. 

   \- b. Bagi Mahasiswa: Mempermudah proses pendaftaran asisten praktikum dan akses informasi penjadwalan melalui satu pintu sistem terintegrasi. 

2\. Manfaat Akademis 

   \- a. Bagi Komunitas Akademik: Menjadi referensi studi mengenai implementasi dan kustomisasi ERP Odoo dengan modul \_OpenEduCat\_ untuk tata kelola operasional laboratorium Pendidikan. 

   \- b. Bagi Penulis: Meningkatkan pemahaman teknis dalam pengembangan modul warisan ( \_inheritance\_ ) dan konfigurasi basis data relasional pada \_framework\_ Odoo. 

\# \*\*1.5 Sistematika Penulisan\*\* 

Sistematika dari penulisan ini merupakan penjelasan mengenai setiap bab. Detail rincian terkait penjelasan setiap bab adalah sebagai berikut : 

\# \*\*BAB I PENDAHULUAN\*\* 

Bab ini menguraikan dasar pemikiran penelitian yang mencakup latar belakang masalah terkait manajemen asisten di Laboratorium Fakultas Ilmu Komputer (FIK) UPN "Veteran" Jakarta, perumusan masalah, batasan masalah yang difokuskan pada fase \_Establish\_ (rekrutmen dan penjadwalan), tujuan yang ingin dicapai, manfaat penelitian bagi pihak terkait, serta sistematika penulisan skripsi. 

\# \*\*BAB II TINJAUAN PUSTAKA\*\* 

Bab ini memaparkan landasan teori yang relevan dan menjadi acuan dalam penyelesaian masalah. Teori yang dibahas mencakup konsep \_Enterprise Resource Planning\_ (ERP), modul Odoo \_OpenEduCat\_ , metodologi pengembangan SDLC 

4 

\_Waterfall\_ , \_Unified Modeling Language\_ (UML), instrumen pengujian perangkat lunak, serta tinjauan terhadap penelitian-penelitian terdahulu yang relevan dengan topik yang diangkat. 

\# \*\*BAB III METODOLOGI PENELITIAN\*\* 

Bab ini menjelaskan secara rinci kerangka kerja dan tahapan pelaksanaan penelitian. Pembahasan difokuskan pada penerapan model pengembangan sistem penerapan model pengembangan sistem SDLC Waterfall, metode perancangan sistem menggunakan pemodelan UML, instrumen evaluasi sistem menggunakan \_Black-box Testing\_ dan \_System Usability Scale\_ (SUS), serta rincian alat, bahan, dan jadwal pelaksanaan penelitian. 

\# \*\*BAB IV HASIL DAN PEMBAHASAN\*\* 

Bab ini merupakan bagian inti yang menguraikan hasil dari seluruh tahapan penelitian. Pembahasan diawali dengan profil Laboratorium FIK UPN "Veteran" Jakarta, disusul dengan analisis sistem berjalan dan \_Fit/Gap Analysis\_ , perancangan sistem usulan, hingga implementasi kustomisasi pada \_platform\_ Odoo \_OpenEduCat\_ . Selanjutnya, bab ini juga memaparkan hasil evaluasi dan validasi sistem berdasarkan pengujian fungsionalitas ( \_Black-box Testing\_ ) dan pengujian tingkat kebergunaan sistem ( \_System Usability Scale\_ ). 

\# \*\*BAB V PENUTUP\*\* 

Bab ini berisi kesimpulan akhir yang ditarik dari seluruh rangkaian hasil penelitian dan pengujian kelayakan sistem yang telah dilakukan, guna menjawab rumusan masalah dan tujuan penelitian. Pada bab ini juga dilampirkan saran-saran konstruktif sebagai bahan pertimbangan untuk pengembangan dan penyempurnaan sistem di masa yang akan datang. 

5 

**Ahmad Razi: SI Peminjaman Ruangan dan Barang FIK UPNVJ berbasis Mobile**  
\# \*\*BAB 1\. PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Di era dimana perkembangan teknologi semakin pesat, maka kegiatan – kegiatan yang dulunya dilakukan secara konvensional kini telah dialihkan untuk memanfaatkan teknolgi agar kegiatan tersebut dapat dilakukan dengan lebih mudah dan lebih efisien. Contoh dari pemanfaatan teknologi tersebut adalah kegiatan – kegiatan di kampus yang awalnya dilakukan secara konvensional seperti mengisi kartu rencana studi, pendaftaran sidang skripsi, pengajuan cuti, dan lain – lain. Salah satu fakultas kampus yang sudah menerapkan mengalihkan kegiatan – kegiatan untuk menerapkan teknologi ini adalah Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. 

Untuk mengetahui lebih lanjut mengenai detail dari peminjaman ruangan dan barang di fakultas ilmu komputer Universitas Pembangunan Nasional Veteran Jakarta, saya melakukan wawancara terhadap petugas di tata usaha fakultas ilmu komputer yang bertugas untuk mengurus peminjaman ruangan dan barang. Dari wawancara yang telah saya, saya jadi tahu bahwa masalah yang ada di prosedur peminjaman ruangan dan barang di fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta masih mengharuskan peminjam untuk datang langsung ke kampus untuk mengetahui ruangan atau barang yang tersedia untuk dipinjam atau membuat surat peminjaman ruangan atau barang. 

Masalah selanjutnya yang ada di prosedur peminjaman ruangan dan barang di fakultas ilmu komputer adalah adanya beberapa mahasiswa atau dosen yang bukan berasal dari fakultas ilmu komputer yang meminjam ruangan atau barang di fakultas ilmu komputer, dan dari wawancara yang telah saya lakukan, persoalan tersebut menyebabkan beberapa kali mahasiswa atau dosen dari fakultas ilmu komputer tidak bisa meminjam ruangan atau barang yang ada di fakultas ilmu komputer karena ruangannya telah dipinjam oleh mahasiswa atau dosen dari fakultas lain. 

Maka dari itu saya melakukan penelitian untuk merancang sistem informasi peminjaman ruangan dan barang berbasis aplikasi Mobile di fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta untuk memudahkan kegiatan peminjaman ruangan di fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Sistem informasi peminjaman ruangan dan barang berbasis aplikasi Mobile ini akan dibangun menggunakan metode \_Waterfall\_ karena metode \_Waterfall\_ memiliki sistem rangkain yang jelas untuk sistem informasi yang akan saya rancang. 

\# \*\*1.2. Rumusan Masalah\*\* 

Berdasarkan latar belakang yang tertera di atas, maka rumusan masalah dari penelitian ini adalah: 

1\. Bagaimana cara membuat sistem informasi peminjaman ruangan dan barang FIK UPNVJ berbasis mobile untuk membuat proses peminjaman ruangan di FIK UPNVJ lebih efektif dan efisien ? 

1 

2\. Bagaimana cara mengimplementasikan fitur untuk mempriotiaskan peminjam dari fakultas ilmu komputer di sistem informasi peminjaman ruangan FIK UPNVJ berbasis mobile? 

\# \*\*1.3. Batasan Masalah\*\* 

Batasan masalah atau ruang lingkup pada penelitian ini adalah sebagai berikut: 

1\. Sistem informasi yang akan dirancang adalah sistem informasi peminjaman ruangan dan barang yang berbasiskan aplikasi Mobile. 

2\. Sistem ini berfokus pada proses peminjaman ruangan dan barang di fakultas ilmu komputer Universitas Pembagunan Nasional "Veteran" Jakarta. 

\# \*\*1.4. Tujuan Penelitian\*\* 

Berdasarkan rumusan masalah yang tertera di atas, maka tujuan dari penelitian ini adalah: 

1\. Membuat sistem informasi peminjaman ruangan dan barang untuk Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. 

\# \*\*1.5. Manfaat Penelitian\*\* 

Manfaat yang bisa didapatkan dari hasil penelitian ini adalah sebagai berikut: 

1\. Memudahkan kegiatan peminjaman ruangan dan barang di fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta. 

2\. Hasil dari penelitian ini bisa memberikan informasi kepada pembaca terutama mengenai penggunaan metode \_Waterfall\_ untuk perancangan sistem informasi. 

\# \*\*1.6. Luaran Penelitian\*\* 

Penilitian ini akan menghasilkan luaran berupa sistem informasi  peminjaman ruangan dan barang berbasis aplikasi Mobile untuk fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta. 

\# \*\*1.7. Sistematika Penulisan\*\* 

Dalam pembuatan proposal skripsi, terdapat sistematika penulisan yang dibagi menjadi beberapa bab, yaitu : 

\# BAB I PENDAHULUAN 

Bab ini menjelaskan secara singkat dan jelas mengenai latar belakang masalah, rumusan masalah, batasan masalah, tujuan penelitian dan manfaat penelitian, dan sistematika penulisan. 

\# BAB II TINJAUAN PUSTAKA 

Bab ini menguraikan teori-teori yang mendasari pembahasan secara detail, dapat berupa definisi-definisi atau model matematis yang langsung berkaitan dengan ilmu atau masalah yang diteliti dan penelitian terdahulu. 

\# BAB III METODE PENELITIAN 

Bab ini menguraikan tentang tahapan penelitian, alat dan bahan serta jadwal penelitian. 

2 

\# BAB IV HASIL DAN PEMBAHASAN 

Bab ini dijabarkan profil dari fakultas ilmu komputer Universitas Pembangunan Nasional "Veteran" Jakarta secara singkat, serta membahas analisis sistem yang berjalan serta analisis sistem usulan . 

BAB V PENUTUP 

Bab ini menguraikan tentang kesimpulan dan saran penelitian berikutnya. 

3 

**Felita Tiara: Modul Perencanaan & Monitoring IKU dan Perjanjian Kinerja FIK**  
\# \*\*BAB 1\. PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Transformasi digital pada sektor pendidikan tinggi tidak lagi berhenti pada penyediaan layanan akademik berbasis elektronik, melainkan telah merambah pada aspek tata kelola dan pengendalian kinerja institusi. Teknologi informasi kini diposisikan sebagai instrumen manajerial yang memungkinkan pimpinan memantau pencapaian organisasi secara berkelanjutan, bukan sekadar sarana pengarsipan dokumen. Laudon dan Laudon (2020) menegaskan bahwa sistem informasi manajemen berperan mendukung pengambilan keputusan dan pengendalian organisasi melalui pengumpulan, pemrosesan, penyimpanan, dan distribusi informasi yang terintegrasi. Pandangan tersebut sejalan dengan Sutabri (2016) yang menempatkan sistem informasi sebagai penghubung antara data operasional dengan kebutuhan informasi pada tingkat manajerial. Dalam konteks perguruan tinggi, kedua pandangan tersebut menjadi relevan ketika institusi dituntut mempertanggungjawabkan capaian kinerjanya secara terukur kepada pemangku kepentingan. 

Universitas Pembangunan Nasional "Veteran" Jakarta memiliki visi menjadi universitas unggul berkualitas internasional yang inovatif, berdaya saing, dan beridentitas bela negara untuk pembangunan masyarakat Indonesia. Pencapaian visi tersebut diukur melalui serangkaian indikator kinerja yang penetapannya diatur secara nasional. Indikator Kinerja Utama perguruan tinggi saat ini mengacu pada Keputusan Menteri Pendidikan Tinggi, Sains, dan Teknologi Republik Indonesia Nomor 358/M/KEP/2025 tentang Indikator Kinerja Utama Perguruan Tinggi dan Lembaga Layanan Pendidikan Tinggi di Lingkungan Kementerian Pendidikan Tinggi, Sains, dan Teknologi, sebagai bagian dari arah kebijakan Diktisaintek Berdampak. Pada regulasi sebelumnya indikator kinerja utama berjumlah delapan indikator, namun melalui ketentuan terbaru jumlahnya diperluas menjadi dua belas indikator yang dikelompokkan ke dalam tiga kategori, yaitu Indikator Kinerja Utama Wajib, Pilihan, dan Partisipatif. Penetapan targetnya dilakukan pada tingkat perguruan tinggi melalui Perjanjian Kinerja antara pimpinan perguruan tinggi dengan Menteri, yang selanjutnya diturunkan secara berjenjang atau cascading kepada unit kerja di bawahnya, termasuk fakultas. 

Mekanisme cascading tersebut menempatkan Fakultas Ilmu Komputer bukan sebagai penetap indikator, melainkan sebagai penerima dan pengelola target turunan dari universitas. Konsekuensinya, fakultas menanggung tiga beban kerja sekaligus, yaitu membagi porsi target kepada jurusan, program studi, dosen, serta tenaga kependidikan; menghimpun realisasi beserta dokumen buktinya; dan melaporkan rekapitulasi capaian kepada Biro Perencanaan, Keuangan, dan Umum untuk diverifikasi menjadi angka capaian final universitas. Rangkaian kerja ini bersifat berulang setiap periode pelaporan dan melibatkan banyak pihak dengan 

1 

kewenangan yang berbeda, sehingga membutuhkan penelusuran yang jelas mengenai siapa bertanggung jawab atas porsi target yang mana. 

Berdasarkan observasi dan wawancara dengan Ibu Erly Krisnanik, S.Kom., M.M. selaku Wakil Dekan 1 Bidang Akademik yang bertanggung jawab atas pengelolaan Indikator Kinerja Utama dan Perjanjian Kinerja di Fakultas Ilmu Komputer, seluruh rangkaian kerja tersebut hingga saat ini masih berjalan secara manual. Pembagian target disampaikan melalui surat-menyurat dan percakapan grup, rekapitulasi capaian disusun menggunakan berkas Excel yang diperbarui secara bergantian, sedangkan dokumen bukti pendukung diunggah ke folder penyimpanan awan tanpa struktur penamaan yang seragam. Kondisi ini menimbulkan beberapa kendala yang saling berkaitan. Porsi target yang telah didistribusikan sulit ditelusuri sehingga kerap terjadi selisih antara jumlah target yang dibagikan dengan target yang diterima fakultas. Dokumen bukti yang tersebar menyulitkan proses penelusuran kembali ketika Biro Perencanaan, Keuangan, dan Umum meminta klarifikasi atas suatu indikator. Selain itu, angka realisasi yang diajukan unit kerja tidak selalu sama dengan angka yang disahkan Biro Perencanaan, Keuangan, dan Umum, sementara riwayat perbedaan tersebut tidak terekam pada satu tempat yang dapat diaudit. 

Dampak lanjutan dari kondisi tersebut adalah lambatnya proses rekapitulasi, meningkatnya risiko duplikasi dan kesalahan data, serta tidak tersedianya gambaran capaian kinerja secara real-time bagi pimpinan fakultas. Pimpinan baru mengetahui posisi capaian ketika periode pelaporan hampir berakhir, sehingga ruang untuk melakukan intervensi terhadap indikator yang tertinggal menjadi sangat sempit. Padahal, pemantauan capaian yang berlangsung sepanjang periode merupakan prasyarat bagi evaluasi kinerja yang objektif dan berkelanjutan sebagaimana dituntut oleh prinsip tata kelola yang transparan dan akuntabel. Sejumlah penelitian terdahulu menunjukkan bahwa digitalisasi pengelolaan indikator kinerja memberikan dampak positif bagi institusi. Monintja et al. (2021) menemukan bahwa perancangan sistem informasi Indikator Kinerja Utama di lingkungan universitas mempermudah pengolahan data dan penyusunan laporan sekaligus meningkatkan akuntabilitas institusi. Indriati et al. (2023) menambahkan bahwa pemutakhiran data melalui sistem terpadu berperan penting dalam pencapaian indikator kinerja karena meningkatkan kesadaran sivitas akademika terhadap pentingnya validasi data secara berkala. Namun demikian, penelitianpenelitian tersebut umumnya berhenti pada tataran pencatatan dan pelaporan capaian, dan belum secara khusus membahas mekanisme distribusi target secara berjenjang beserta pengelolaan dokumen buktinya pada tingkat fakultas. Celah inilah yang menjadi ruang bagi penelitian ini. 

Berangkat dari permasalahan tersebut, dikembangkan Sistem Informasi Pelaporan Kinerja Indikator Kinerja Utama dan Perjanjian Kinerja pada Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Sistem ini dikembangkan secara berkelompok dan terbagi menjadi dua lingkup 

2 

pengembangan. Penelitian ini secara khusus membahas modul perencanaan target, realisasi capaian, dan monitoring, yang mencakup pengelolaan master indikator dengan struktur hierarki bertingkat, disposisi target secara berjenjang dari dekan hingga dosen dan tenaga kependidikan, perekaman realisasi beserta unggahan dokumen bukti, validasi capaian secara bertahap oleh atasan, monitoring capaian pada tingkat unit kerja maupun keseluruhan fakultas, serta verifikasi akhir oleh Biro Perencanaan, Keuangan, dan Umum. Adapun modul autentikasi, manajemen pengguna, dan penyusunan Sasaran Kinerja Pegawai dikembangkan pada lingkup penelitian yang terpisah. 

Salah satu karakteristik yang membedakan sistem ini adalah pengelolaan dokumen bukti yang tidak disimpan di dalam sistem itu sendiri, melainkan diintegrasikan dengan Sistem Repository yang telah lebih dahulu digunakan di lingkungan fakultas. Integrasi tersebut dirancang menggunakan pola proxy, yaitu permintaan unggah dari antarmuka pengguna diteruskan oleh backend sistem pelaporan kinerja menuju backend Repository, dengan penempatan berkas mengikuti struktur folder yang disusun berdasarkan kode indikator. Pendekatan ini menjaga agar dokumen bukti tetap terkelola pada satu sistem penyimpanan institusional, sekaligus memastikan setiap berkas terhubung langsung dengan indikator yang dibuktikannya. 

Dari sisi teknologi, sistem dibangun berbasis web menggunakan Next.js pada sisi frontend dan NestJS pada sisi backend. Next.js dipilih karena dukungannya terhadap server-side rendering dan routing berbasis berkas yang menghasilkan antarmuka responsif untuk menampilkan data monitoring secara dinamis. NestJS dipilih karena menerapkan rancangan modular dan menyediakan dependency injection, middleware, serta guard yang memudahkan pengaturan otorisasi antar peran pengguna sekaligus komunikasi antar layanan. Proses pengembangan menggunakan metode Rapid Application Development yang menekankan pembangunan prototipe secara iteratif dengan pelibatan pengguna, sehingga rancangan alur disposisi dan validasi dapat disesuaikan dengan praktik kerja yang berlaku di fakultas. 

Dengan demikian, pengembangan modul perencanaan target, realisasi, dan monitoring pada Sistem Informasi Pelaporan Kinerja Indikator Kinerja Utama dan Perjanjian Kinerja ini diharapkan mampu menjawab kebutuhan Fakultas Ilmu Komputer akan mekanisme distribusi target yang tertelusur, pencatatan capaian yang berbasis bukti, serta pemantauan kinerja yang dapat diakses sewaktu-waktu oleh pimpinan. Sistem ini tidak hanya berfungsi sebagai sarana administrasi pelaporan, tetapi juga sebagai alat bantu manajerial dalam pengambilan keputusan berbasis data, yang pada akhirnya mendukung terwujudnya tata kelola fakultas yang efektif, transparan, dan akuntabel selaras dengan visi universitas. 

3 

\# \*\*1.2. Identifikasi Masalah\*\* 

Berdasarkan dari permasalahan tersebut, peneliti menemukan identifikasi masalah dalam penelitiannya, berikut masalah yang dirumuskan: 

1\. Distribusi target Indikator Kinerja Utama dan Perjanjian Kinerja dari fakultas kepada jurusan, program studi, dosen, dan tenaga kependidikan masih dilakukan melalui surat-menyurat sehingga porsi target yang telah dibagikan sulit ditelusuri dan berpotensi melebihi target yang diterima fakultas. 

2\. Pencatatan realisasi capaian masih menggunakan rekapitulasi berkas Excel yang diperbarui secara terpisah oleh masing-masing unit, sehingga proses penggabungan data memakan waktu lama dan meningkatkan risiko kesalahan serta duplikasi data. 

3\. Dokumen bukti pendukung capaian tersimpan secara tersebar tanpa struktur penamaan dan penempatan yang seragam, sehingga menyulitkan penelusuran kembali ketika diperlukan klarifikasi atas suatu indikator. 

4\. Belum tersedia mekanisme validasi capaian secara berjenjang yang terekam pada sistem, sehingga perbedaan antara realisasi yang diajukan unit kerja dengan angka yang disahkan oleh Biro Perencanaan, Keuangan, dan Umum tidak terdokumentasi dan sulit diaudit. 

5\. Belum tersedia sarana pemantauan capaian kinerja secara real-time bagi pimpinan fakultas, sehingga evaluasi baru dapat dilakukan menjelang akhir periode pelaporan dan mempersempit ruang perbaikan terhadap indikator yang belum tercapai. 

\# \*\*1.3. Batasan Masalah\*\* 

Berikut batasan dari penelitian ini : 

1\. Penelitian ini membahas modul master indikator, disposisi target, perekaman realisasi capaian, monitoring capaian, verifikasi Biro Perencanaan, Keuangan, dan Umum, serta integrasi dengan Sistem Repository. 

2\. Target Indikator Kinerja Utama dan Perjanjian Kinerja yang dikelola merupakan target turunan yang diterima dari universitas. 

3\. Integrasi dengan sistem eksternal terbatas pada Sistem Repository untuk keperluan penyimpanan dan penelusuran dokumen bukti pendukung capaian. 

4\. Sistem dikembangkan berbasis website dan diimplementasikan pada lingkungan Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. 

\# \*\*1.4. Tujuan dan Manfaat Penelitian\*\* 

Berikut adalah tujuan yang didapatkan dari identifikasi masalah penelitian 

ini: 

1\. Merancang dan membangun modul pengelolaan master indikator dengan struktur hierarki bertingkat yang mampu merepresentasikan sasaran program 

4 

beserta turunan indikator dan sub indikatornya, sekaligus mengakomodasi keterkaitan antara Indikator Kinerja Utama dengan Perjanjian Kinerja. 

2\. Membangun mekanisme disposisi target secara berjenjang yang dilengkapi validasi agar akumulasi porsi target yang didistribusikan tidak melebihi target yang tersedia, serta menyediakan visualisasi rantai disposisi untuk menelusuri tanggung jawab pemenuhan target. 

3\. Membangun fitur perekaman realisasi capaian yang terintegrasi dengan Sistem Repository sebagai media penyimpanan dokumen bukti, disertai alur validasi bertahap oleh atasan hingga verifikasi akhir oleh Biro Perencanaan, Keuangan, dan Umum. 

4\. Menyediakan fasilitas monitoring capaian pada tingkat unit kerja maupun keseluruhan fakultas yang dapat diakses secara real-time beserta kemampuan mengekspor laporan capaian dalam format yang sesuai dengan kebutuhan pelaporan institusional. 

5\. Menerapkan metode Rapid Application Development dengan framework Next.js dan NestJS dalam pengembangan sistem, serta menguji kelayakan fungsionalitasnya melalui pengujian black box dan pengujian penerimaan pengguna. 

Pengembangan sistem informasi pelaporan Indikator Kinerja Utama  dan Perjanjian Kinerja  ini diharapkan memberikan manfaat sebagai berikut: 

1\. Bagi Fakultas Ilmu Komputer 

   \- Menyediakan sarana digital yang terpusat untuk mendistribusikan target secara berjenjang, mencatat realisasi capaian beserta dokumen buktinya, dan memantau perkembangan capaian kinerja sepanjang periode pelaporan, sehingga proses rekapitulasi menjadi lebih cepat, tertelusur, dan mendukung tata kelola yang transparan serta akuntabel. 

2\. Bagi Pimpinan dan Unit Kerja Memberikan gambaran posisi capaian setiap indikator secara real-time sebagai dasar pengambilan keputusan, sekaligus memperjelas tanggung jawab masingmasing unit kerja terhadap porsi target yang diterimanya. 

3\. Bagi Peneliti dan Pengembang Sistem Menjadi studi kasus penerapan metode Rapid Application Development dengan framework Next.js dan NestJS, khususnya pada perancangan hierarki indikator bertingkat, algoritma distribusi target berjenjang, dan integrasi antarlayanan dengan sistem penyimpanan dokumen. 

5 

\# \*\*1.5. Tempat dan Waktu\*\* 

Penelitian ini dilakukan di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta Universitas Pembangunan Nasional “Veteran” Jakarta yang beralamat di Jalan RS. Fatmawati nomor 1, Pondok Labu, Cilandak, Jakarta Selatan (12450). Waktu yang dibutuhkan untuk penelitian ini 6 bulan sejak Juli 2025\. Jadwal pelaksanaan penelitian disusun untuk memastikan setiap tahap dilakukan dengan terencana. Berikut tahapan waktu penelitian beserta waktu pelaksanaannya. 

\<\!-- Start of picture text \--\>  
Pm\<br\>Alwr Penetiian \[Rawr \[Sepemer | Omoba \[November \[Deemer \[ Janari\_\[ Fra\<br\>fucirnsivosssrewwmrasnrus RABARARARARARAAARAAAAAAAAAEELETT| TET || TTT TT E T TT  TTT T T TT TTT TT TTT T TTT T |\<br\>recnemanxerooron| || | | TETTTT T TTT TTT TT TTT TT TT |\<br\>roomanemsicn | | TTT TTT LTT TPP TT\<br\>luce TTT ET TT ET EE PT\<br\>lomenenss | LET TT TT EEE EE\<br\>eeOe\<br\>oncom\<br\>EET PEE TEE EET EEE\<br\>loowmenos LETTTT\<br\>\<\!-- End of picture text \--\>

Gambar 1.1 Timeline Penelitian 

6 

**Bimasetyo H. Y.: Website Akreditasi Prodi, Kriteria 7–9 LAM-INFOKOM FIK**  
\# \*\*BAB I\*\* 

\# \*\*PENDAHULUAN\*\* 

\# \*\*1.1 Latar Belakang\*\* 

Perkembangan teknologi yang semakin canggih sangat berpengaruh pada kehidupan masyarakat sekarang. Hal ini dibuktikan dari hasil survei Asosiasi Pengguna Jasa Internet Indonesia (APJII) tahun 2018 yang dikutip dari laman \_gurudikdas.kemdikbud.go.id\_ , menunjukan bahwa di Indonesia ada sebanyak 355 juta pengguna handphone dan sebanyak 171 juta jiwa pengguna internet. Teknologi sudah menjadi sebuah bagian dari kehidupan masyarakat untuk menjalani kegiatan sehari-hari. Berkembangnya teknologi saat ini mempengaruhi banyak kegiatan yang akhirnya membutuhkan konsep digitalisasi. Berkembangnya digitalisasi saat ini tidak terlepas dari kebutuhan teknologi informasi. Digitalisasi sudah menjadi kebutuhan utama untuk meningkatkan kinerja operasional di berbagai bidang. 

Perkembangan  dunia  digital  terjadi  begitu  dinamis,  cepat  atau lambat  bukan  hanya mempengaruhi  namun  mengubah  gaya hidup masyarakat  yang  tidak  dapat  dihindari. Digitalisasi merupakan proses pengimplementasian sistem digital. Hal ini berarti, terdapat penggunaan teknologi digital dalam suatu model bisnis. Digitalisasi merupakan salah satu proses dalam membuat dan memperbaiki sebuah proses bisnis dengan menggunakan bantuan teknologi digital. 

Digitalisasi sudah merambat ke berbagai sektor, salah satunya sektor pendidikan. Digitalisasi Pendidikan merupakan pengelolaan sistem yang menggunakan teknologi sebagai alat dalam mencapai pemindahannya (Ma’rufah, 2022). Perkembangan digitalisasi pendidikan tidak lepas dari tiga faktor yaitu regulasi dari pemerintah, pendidik, dan peserta didik serta diperlukan juga infrastruktur yang memadai. Digitalisasi dalam pendidikan 

1 

telah membawa perubahan besar dalam cara pembelajaran, pengelolaan administrasi, serta penyampaian informasi. 

Digitalisasi sangat membantu dalam hal persiapan data di sebuah institusi pendidikan. Salah satu yang terpengaruh adalah terkait akreditasi sebuah perguruan tinggi. Sistem akreditasi merupakan salah satu bentuk penilaian (evaluasi) mutu dan kelayakan institusi perguruan tinggi atau program studi yang dilakukan oleh organisasi atau badan mandiri di luar perguruan tinggi (Yani S., Ali F., Rohmat T., Mayang A., 2019). Akreditasi adalah kegiatan penilaian sesuai dengan kriteria yang telah ditetapkan berdasarkan Standar Nasional Pendidikan Tinggi (Pasal 55 (1) Undangundang Nomor 12 Tahun 2012\) (Pedoman Asesmen Lapangan BAN-PT Jakarta, 2019). Akreditasi menjadi salah satu penanda mutu pendidikan dari sebuah program studi dan perguruan tinggi. Akreditasi program studi adalah sebuah penilaian terkait kelayakan sebuah program studi di sebuah perguruan tinggi. Akreditasi program studi maupun perguruan tinggi biasanya memiliki masa berlaku selama 5 tahun. Berdasarkan Panduan Pelaksanaan Akreditasi Perguruan Tinggi oleh BAN-PT, akreditasi dilakukan melalui beberapa tahapan, yaitu evaluasi data, penetapan peringkat, dan pemantauan serta evaluasi lanjutan (IPEPA-PT 2021). Hal ini menekankan bahwa pentingnya penyimpanan serta persiapan data akreditasi program studi dan perguruan tinggi agar proses akreditasi dapat dilakukan dengan terstruktur. 

Persiapan data yang baik sangat diperlukan untuk memudahkan proses akreditasi. Banyak perguruan tinggi yang masih mengelola data persiapan akreditasi program studi secara manual, salah satunya adalah Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta sendiri merupakan salah satu fakultas yang memperoleh akreditasi program studi dari LAM-INFOKOM, yaitu lembaga yang bertugas untuk memproses akreditasi program studi di bidang informasi dan komputer. Pada Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta, data akreditasi masih dikelola hanya 

2 

menggunakan spreadsheets dan \_google drive\_ . Hal ini dinilai kurang terstruktur karena data yang ada tidak tersimpan di \_database\_ yang dikelola sendiri oleh pihak kampus yang akan membuat data pasti lebih aman dan terstruktur. 

Pada penelitian yang berjudul “Rancang Bangun \_Website\_ Akreditasi Program Studi (Studi Kasus: Kriteria 7,8,9 LAM-INFOKOM Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta)” ini akan dikembangkan sebuah \_website\_ yang dapat memfasilitasi pihak prodi untuk menyimpan hal-hal yang terkait dengan akreditasi program studi di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta agar data dan dokumen sudah siap saat kegiatan akreditasi dilakukan.  dengan menggunakan bahasa pemrograman HTML, CSS, dan \_Javascript\_ untuk bagian frontend serta dipadukan dengan bahasa pemrograman PHP dengan database \_MySQL\_ untuk bagian backend, selain itu penelitian ini juga dibantu dengan \_framework Laravel\_ . \_Laravel\_ merupakan salah satu \_framework\_ web yang berbasis PHP dan dikembangkan secara \_open-source\_ , \_laravel\_ dikembangkan oleh Taylor Otwell dan digunakan untuk mengembangankan aplikasi berbasis web yang menerapkan sebuah pola yaitu MVC (Rima Y., Indyah H. S., Wahyu D. P., 2022). 

Penelitian ini bertujuan untuk mengembangkan sebuah \_website\_ yang berfokus pada penyimpanan dan persiapan akreditasi program studi Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. W \_ebsite\_ ini diharapkan dapat membantu dalam hal persiapan akreditasi program studi Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. Oleh karena itu, hasil dari penelitian ini diharapkan dapat memberi kontribusi kepada pihak Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta dalam mengelola dan menyimpan data akreditasi untuk meningkatkan kinerja dan akreditasi program studi di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. Dengan meningkatnya kinerja pihak Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta akan terdapat juga segi peningkatan akreditasi karena 

3 

dalam proses akreditasi akan dapat dilakukan lebih terstruktur dan cepat karena data dan dokumen telah disimpan dalam satu \_database\_ pusat, sehingga akreditasi program studi di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta akan cepat meningkat. 

\# \*\*1.2 Identifikasi Masalah\*\* 

Berdasarkan latar belakang yang telah dijabarkan, maka terdapat beberapa identifikasi masalah, yaitu sebagai berikut: 

\- a. Belum adanya sistem informasi yang mendukung fitur perhitungan otomatis, pengelompokan dokumen berdasarkan kriteria akreditasi, serta kontrol akses pengguna yang menyebabkan proses akreditasi cenderung berlangsung tanpa dukungan sistem yang terarah dan terpadu. 

\- b. Belum adanya sistem digital yang terpusat dalam pengelolaan dokumen akreditasi yang menyulitkan fakultas dalam mengakses, memperbarui, dan menjaga konsistensi informasi yang dibutuhkan dalam proses akreditasi. 

\# \*\*1.3 Batasan Masalah\*\* 

\- Untuk mencapai tujuan penelitian secara lebih terarah dan fokus 

\- dalam menerapkan solusi terhadap permasalahan, perlu ditetapkan batasan masalah penelitian sebagai berikut: a. Penelitian ini menggunakan bahasa pemrograman PHP dengan \_framework Laravel\_ serta sistem basis data MySQL untuk pengembangan \_website\_ . 

\- b. Penelitian ini difokuskan pada pembuatan \_website\_ akreditasi program studi untuk Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta yang bertujuan untuk sebagai sarana pendukung dalam hal penyimpanan data dan dokumen terkait proses persiapan akreditasi program studi di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. 

4 

\- c. Penelitian ini difokuskan dalam lingkup kriteria 7,8,9 dari LAMINFOKOM Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. 

\# \*\*1.4 Tujuan dan Manfaat Penelitian\*\* 

\# \*\*1.4.1 Tujuan Penelitian\*\* 

Terdapat beberapa tujuan dari penelitian ini yaitu sebagai berikut: 

\- a. Untuk merancang dan membangun sistem informasi yang mendukung fitur perhitungan otomatis, pengelompokan dokumen berdasarkan kriteria akreditasi, serta pengaturan hak akses pengguna yang akan mendukung proses akreditasi yang lebih terarah dan terpadu. 

\- b. Untuk mengembangkan sistem digital terpusat yang nantinya akan dapat memudahkan perihal pengelolaan dokumen akreditasi, khususnya dalam hal akses, pembaruan, dan menjaga konsistensi informasi yang dibutuhkan oleh fakultas selama proses persiapan akreditasi. 

\# \*\*1.4.2 Manfaat Penelitian\*\* 

Manfaat yang diperoleh dari penelitian ini yaitu sebagai berikut: 

1\. Manfaat bagi peneliti 

   \- a. Menerapkan pengetahuan yang diperoleh selama mengikuti perkuliahan. 

   \- b. Meningkatkan keterampilan dalam desain dan pengembangan situs web berbasis sistem informasi, khususnya situs yang membantu proses akreditasi. 

2\. Manfaat bagi Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta 

5 

   \- a. \_Website\_ yang dikembangkan akan membantu Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dalam menjalankan proses akreditasi secara lebih terstruktur dan aman. 

   \- b. Dengan adanya sistem ini, proses pencarian, pengunggahan, dan penyimpanan dokumen akreditasi dapat dilakukan secara terpusat dan terstruktur. 

3\. Manfaat bagi pembaca 

   \- a. Pembaca yang ingin mempelajari atau mengembangkan sistem serupa dapat menggunakan penelitian ini sebagai referensi. 

   \- b. Pembaca akan memperoleh wawasan mengenai bagaimana teknologi informasi dapat diterapkan untuk mempermudah proses administratif di instansi pendidikan. 

\# \*\*1.5 Jadwal Kegiatan\*\* 

\# \*\*1.5.1 Tempat dan Waktu Penelitian\*\* 

a. Tempat Penelitian : Fakultas Ilmu Komputer, Universitas 

Pembangunan Nasional "Veteran" Jakarta, Jalan RS. Fatmawati Raya, Pondok Labu, Cilandak, Jakarta Selatan, Jakarta 12450 b. Waktu Penelitian : Oktober 2024 \- Mei 2025 

\# \*\*1.5.2 Jadwal Pelaksanaan Penelitian\*\* 

Jadwal pelaksanaan penelitian disajikan dalam tabel bertujuan memberikan gambaran yang jelas untuk tahapan-tahapan penelitian dan waktu yang diperlukan. Jadwal ini berlangsung selama enam bulan dengan alokasi waktu yang tercantum dalam tabel di bawah ini: 

6 

Tabel 1.1 Jadwal Pelaksanaan Penelitian 

|\*\*No\*\*|\*\*Tahapan\*\*|\*\*Bu\*\*\<br\>\*\*k\*\*|\*\*lan\*\*\<br\>\*\*e-1\*\*|||\*\*Bul\*\*\<br\>\*\*ke\*\*|\*\*an\*\*\<br\>\*\*-2\*\*||\*\*Bul\*\*|\*\*an\*\*\<br\>\*\*3\*\*|\*\*ke-\*\*||\*\*J\*\*\<br\>\*\*B\*\*\<br\>\*\*k\*\*|\*\*ad\*\*\<br\>\*\*ul\*\*\<br\>\*\*e-\*\*|\*\*wal\*\*\<br\>\*\*an\*\*\<br\>\*\*4\*\*|\*\*Ke\*\*\<br\>\*\*B\*\*|\*\*gia\*\*\<br\>\*\*ula\*\*\<br\>|\*\*t\*\*\<br\>\*\*n\*\*\<br\>\*\*5\*\*|\*\*a\*\*\<br\>|\*\*n\*\*\<br\>\*\*ke-\*\*|\*\*B\*\*|\*\*ula\*\*|\*\*n\*\*\<br\>\*\*6\*\*|\*\*ke-\*\*|\*\*Bu\*\*|\*\*lan\*\*\<br\>\*\*7\*\*|\*\*k\*\*|\*\*e-\*\*|\*\*B\*\*|\*\*ul\*\*|\*\*a\*\*\<br\>|\*\*n\*\*\<br\>\*\*8\*\*|\*\*ke-\*\*|  
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|  
|||\*\*1\*\* \*\*2\*\*|\*\*3\*\*|\*\*4\*\*|\*\*1\*\*|\*\*2\*\*|\*\*3\*\*|\*\*4\*\*|\*\*1\*\* \*\*2\*\*||\*\*3\*\* \*\*4\*\*|\*\*1\*\*|\*\*2\*\*||\*\*3\*\* \*\*4\*\*|\*\*1\*\*|\*\*2\*\*||\*\*3\*\*|\*\*4\*\*|\*\*1\*\*|\*\*2\*\*|\*\*3\*\*|\*\*4\*\*|\*\*1\*\*|\*\*2\*\*|\*\*3\*\*|\*\*4\*\*|\*\*1\*\*|\*\*2\*\*|||\*\*3 4\*\*|  
|1|Pengumpulan\<br\>Data|||||||||||||||||||||||||||||||||  
|2|Perencanaan\<br\>Kebutuhan|||||||||||||||||||||||||||||||||  
|3|Desain Sistem|||||||||||||||||||||||||||||||||  
|4|Perancangan\<br\>\_Prototype\_|||||||||||||||||||||||||||||||||  
|5|Evaluasi\<br\>\_Prototype\_|||||||||||||||||||||||||||||||||  
|6|Pengembangan\<br\>sistem|||||||||||||||||||||||||||||||||  
|7|Pengujian\<br\>Sistem|||||||||||||||||||||||||||||||||  
|8|Evaluasi\<br\>Sistem|||||||||||||||||||||||||||||||||  
|9|Implementasi\<br\>Sistem|||||||||||||||||||||||||||||||||  
|10|Dokumentasi|||||||||||||||||||||||||||||||||

s 

7 

**Irfan Nada B. S.: Arsitektur Integrasi Aplikasi-aplikasi di FIK UPNVJ**

\# \*\*BAB 1\. PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Seiring berjalannya waktu, jumlah dari sistem informasi yang diterapkan juga mengalami peningkatan. Dalam suatu organisasi, dapat memiliki berbagai sistem informasi yang berbeda-beda, sehingga memungkinkan terjadinya proses perulangan antara sistem satu dengan lainnya, terutama dalam hal pemasukan dan pengelolaan data yang ada. 

Integrasi dari sistem informasi akan sangat membantu organisasi dalam mencapai tujuannya, baik itu dalam hal operasional, manajemen, maupun dukungan fungsi strategis (Subiyakto 2023). Suatu organisasi  dapat memproses hingga 2.3 juta \_event\_ per menit dalam sistem skala besar, organisasi yang menerapkan integrasi menunjukkan peningkatan kecepatan \_deployment\_ sistem sebesar 42% dan mengurangi biaya operasional sebesar 37% dibandingkan dengan penggunaan \_middleware\_ secara tradisional (Sannapureddy 2025). 

Penggunaan \_Change Data Capture\_ (CDC) untuk mengatasi masalah yang muncul akibat perbedaan teknologi yang digunakan antara sistem satu dengan yang lainnya, selain itu CDC juga menjadi salah satu tahapan awal untuk menuju \_event driven architecture\_ (EDA), dengan menyediakan \_event\_ yang dapat digunakan pada arsitektur ini. Analisis dari 342 organisasi menunjukkan bahwa EDA dapat mengurangi ketergantungan antar layanan sebesar 67% dan pada saat yang sama memperbaiki respons sistem sebesar 43%, dibandingkan dengan metode integrasi tradisional (Sannapureddy 2025). 

Hasil wawancara dengan pihak pengelola sistem pada Fakultas Ilmu Komputer menunjukkan bahwa saat ini terdapat setidaknya tiga sistem yang aktif, yaitu Lentera sebagai sistem layanan tugas akhir dari fakultas, Sipas sebagai sistem manajemen sarana dan prasarana, serta Sistem Pelayanan Minimal yang merupakan sistem kuesioner layanan. Ketiga sistem tersebut masih berdiri sendiri dan terisolasi satu sama dengan lainnya, serta proses sinkronisasi dan integrasi data yang ada masih dilakukan secara manual. Masalah sinkronisasi data yang saat ini ada dikarenakan cepatnya data berubah, sehingga proses yang saat ini masih manual 

1 

2 

membuat seseorang harus \_stand by\_ untuk menjaga data tersebut, serta terdapat kekurangan \_staff\_ untuk mengelola aplikasi yang ada. Saat terjadi kesalahan sinkronisasi atau integrasi, prosedur yang dilakukan adalah untuk menggunakan satu aplikasi sebagai patokan, yaitu Lentera, kemudian membandingkan data pada sistem lainnya dengan data yang ada pada Lentera, serta juga dilakukan perbandingan dengan data yang ada dari universitas. Pengelola sistem juga menyatakan bahwa ke depannya akan dilakukan \_deployment\_ untuk beberapa sistem lainnya, seperti SMO yang merupakan sistem \_tracking\_ tugas sehari-hari, \_Repository\_ yang merupakan sistem penyimpanan data \_monitoring\_ dan evaluasi, serta \_Digital Library\_ yang merupakan sistem perpustakaan untuk membaca buku secara daring. 

Berdasarkan masalah yang terdapat pada Fakultas Ilmu Komputer, diskusi dengan staf terkait, serta studi penelitian terdahulu yang telah dipelajari, maka penulis berpendapat bahwa perlunya dilakukan integrasi antara aplikasi-aplikasi yang ada di Fakultas Ilmu Komputer. Integrasi yang dilakukan tidak hanya mengelola sistem yang telah ada, namun juga memungkinkan penambahan sistem baru dalam arsitektur yang akan dibangun, sehingga meminimalkan kompleksitas yang diperlukan untuk integrasi lanjutan. Hasil akhir yang diharapkan dari penelitian ini adalah suatu rancangan desain arsitektur yang dapat mengintegrasikan sistem-sistem yang ada, serta suatu prototipe dengan menerapkan arsitektur yang telah dibuat. 

\# \*\*1.2. Rumusan Masalah\*\* 

Rumusan masalah dalam proposal skripsi adalah bagian penting yang merumuskan pertanyaan atau masalah yang akan dijawab oleh penelitian. Rumusan masalah berfungsi sebagai pedoman utama yang mengarahkan jalannya penelitian. Bagian ini harus disusun secara spesifik, jelas, dan fokus pada inti permasalahan yang ingin dipecahkan. Rumusan Masalah dalam penelitian ini adalah: 

1\. Bagaimana merancang suatu \_event driven architecture\_ yang dapat mengintegrasikan Lentera, Sipas, dan Sistem Pelayanan Minimal, serta memungkinkan penambahan sistem baru di masa mendatang? 

3 

2\. Bagaimana menerapkan rancangan arsitektur ke dalam bentuk prototipe fungsional berdasarkan sistem target, dan mampu menangani \_Change Data Capture\_ ? 

3\. Bagaimana menerapkan mekanisme \_monitoring\_ yang dapat mengawasi berjalannya arsitektur integrasi? 

\# \*\*1.3. Batasan Masalah\*\* 

Batasan masalah adalah penjabaran yang secara jelas menjelaskan ruang lingkup atau cakupan masalah yang akan dibahas dalam sebuah tugas akhir. Batasan ini digunakan untuk memperjelas fokus penelitian agar tidak melebar ke aspekaspek yang tidak relevan dan agar penelitian tetap terarah, efisien, dan sesuai dengan tujuan yang ingin dicapai. Batasan masalah dalam penelitian ini adalah: 

1\. Penelitian ini hanya membahas perancangan arsitektur dan pembuatan prototipe untuk integrasi sistem. 

2\. Penelitian hanya akan menghasilkan rancangan dari arsitektur dan prototipe integrasi dari ketiga sistem yang berjalan pada Fakultas Ilmu Komputer Universitas Pembangunan Nasional UPN Veteran Jakarta. 

3\. Ketiga sistem yang dijadikan sebagai model integrasi adalah Sistem Pelayanan Minimal, SIPAS, dan Lentera. 

\# \*\*1.4. Tujuan dan Manfaat Penelitian\*\* 

Tujuan penelitian dalam proposal skripsi adalah bagian yang menjelaskan secara jelas dan spesifik apa yang ingin dicapai melalui penelitian tersebut. Tujuan penelitian harus berhubungan langsung dengan rumusan masalah dan memberikan gambaran tentang hasil atau capaian yang diharapkan dari penelitian. Tujuan dari penelitian ini adalah: 

1\. Menghasilkan rancangan \_Event Driven Architecture\_ dengan metode \_Change Data Capture\_ yang mampu mengintegrasikan Lentera, Sipas, dan Sistem Pelayanan Minimal, serta dapat mengakomodasi penambahan sistem baru di masa mendatang. 

4 

2\. Mengembangkan prototipe fungsional dari arsitektur yang telah dirancang berdasarkan sistem target, dan dapat menangani \_Change Data Capture\_ secara \_real-time\_ . 

3\. Menerapkan mekanisme monitoring yang dapat mengawasi berjalannya arsitektur integrasi. 

Manfaat teoretis dalam penelitian ini adalah untuk mencoba menerapkan metode CDC sebagai alternatif dari metode berbasis API yang banyak digunakan dalam proses integrasi sistem informasi. CDC dapat menghubungkan berbagai sistem secara langsung pada tingkat data, sehingga tidak diperlukan perubahan pada aplikasi yang sudah ada dan tidak mengganggu jalannya sistem yang menggunakan data tersebut, hal ini dapat mengurangi potensi terjadinya \_error\_ pada saat pembaharuan sistem, serta membuat proses integrasi menjadi lebih efisien. Penelitian ini juga melibatkan penggunaan beberapa teknologi untuk sekaligus memonitor dari arsitektur integrasi yang diterapkan. 

Manfaat praktis dalam penelitian ini adalah peningkatan efisiensi dalam proses integrasi sistem informasi pada organisasi tanpa harus melakukan banyak perubahan pada sistem yang sudah ada, sehingga meminimalkan ruang \_error\_ , dan meningkatkan efisiensi dari penggunaan sistem informasi. Penggunaan CDC juga menjadi salah satu pilar menuju arsitektur berbasis \_event\_ ( \_Event driven architecture)\_ yang lebih fleksibel untuk menangani integrasi secara \_real-time\_ dan penambahan sistem di masa mendatang. 

\# \*\*1.5. Sistematika Penulisan\*\* 

Sistematika penulisan ini ditulis untuk memberikan kemudahan informasi bagi pembaca dan memberikan sedikit gambaran dalam “ \*\*Perancangan dan Pengembangan Arsitektur Integrasi Aplikasi-Aplikasi di Fakultas Ilmu Komputer Universitas Pembangunan Nasional Veteran Jakarta\*\* ”, berikut ini adalah sistematika penulisannya : 

BAB I PENDAHULUAN 

5 

Bab ini menjelaskan secara singkat dan jelas mengenai latar belakang masalah, rumusan masalah, batasan masalah, tujuan penelitian dan manfaat penelitian, dan sistematika penulisan. 

BAB II TINJAUAN PUSTAKA 

Bab ini menguraikan teori-teori yang mendasari pembahasan secara detail, dapat berupa definisi-definisi atau model matematis yang langsung berkaitan dengan ilmu atau masalah yang diteliti dan penelitian terdahulu. 

BAB III METODE PENELITIAN 

Bab ini menguraikan tentang tahapan penelitian, alat dan bahan serta jadwal penelitian. 

BAB IV HASIL DAN PEMBAHASAN 

Bab ini menguraikan tentang profil Perusahaan, analisis sistem berjalan, dan hasil serta rekomendasi. 

BAB V PENUTUP 

Bab ini menguraikan tentang kesimpulan dan saran penelitian berikutnya. 

**Agnes Kurnia Gulo: Konfigurasi & Kustomisasi Odoo, Inventori Puskesmas Pondok Labu**

\# \*\*BAB 1\*\* 

\# \*\*PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Transformasi digital mendorong berbagai sektor, termasuk kesehatan, untuk meningkatkan efektivitas, akurasi, dan akuntabilitas proses kerja melalui pemanfaatan teknologi informasi. Dalam pelayanan kesehatan primer, digitalisasi berperan penting dalam menciptakan proses yang lebih terintegrasi, terdokumentasi, dan mendukung pengambilan keputusan secara tepat waktu. 

Pusat Kesehatan Masyarakat (Puskesmas) merupakan fasilitas pelayanan kesehatan tingkat pertama yang berperan sebagai garda terdepan pelayanan kesehatan masyarakat (Kementerian Kesehatan Republik Indonesia 2025). Berdasarkan data Kemenkes RI (2024a), terdapat 10.212 Puskesmas yang tersebar di seluruh Indonesia. Oleh karena itu, keberlangsungan pelayanan Puskesmas sangat dipengaruhi oleh kesiapan sumber daya pendukung, termasuk ketersediaan obat dan bahan medis habis pakai (BMHP) yang dikelola secara tepat, akurat, dan berkesinambungan. Pengelolaan inventori yang kurang optimal tidak hanya berdampak pada aspek administratif, tetapi juga dapat memengaruhi kualitas dan kontinuitas pelayanan kesehatan kepada masyarakat. 

Penelitian yang dilakukan oleh Fanda \_et al.\_ (2024) pada 9.831 Puskesmas menunjukkan bahwa pengelolaan inventori masih banyak dilakukan secara manual atau semi-manual menggunakan kartu stok dan spreadsheet. Kondisi ini menyebabkan pekerjaan berulang, keterlambatan pembaruan data, ketidaksesuaian stok, serta kurang optimalnya pemantauan pergerakan barang, nomor batch, dan tanggal kedaluwarsa yang berpotensi menurunkan kualitas pelayanan kesehatan. Akibatnya, fasilitas kesehatan lebih rentan mengalami kekosongan stok untuk item yang dibutuhkan, penumpukan stok untuk item yang kurang terpakai, hingga kerugian akibat barang kedaluwarsa. Hal ini berkontribusi secara langsung terhadap penurunan kualitas pelayanan kesehatan dan efisiensi pemanfaatan anggaran di fasilitas kesehatan tersebut. 

Permasalahan serupa ditemukan di Puskesmas Pondok Labu fasilitas pelayanan kesehatan tingkat pertama yang berdiri sejak tahun 1986 dan melayani kurang lebih 63.337 jiwa di Jakarta Selatan. Berdasarkan hasil observasi dan wawancara dengan petugas pengelola inventori, proses pengelolaan stok masih dilakukan secara semi-manual melalui pencatatan pada kartu stok yang kemudian dipindahkan kembali ke spreadsheet. Proses tersebut menyebabkan terjadinya pekerjaan berulang dan meningkatkan potensi terjadinya selisih antara stok fisik dan data administrasi. Selain itu, proses pengecekan dan pencocokan data stok memerlukan waktu sekitar 30 menit setiap hari, terutama ketika jumlah item 

1 

inventori yang dikelola cukup banyak. Permasalahan juga ditemukan pada proses Penyusunan LPLPO masih dilakukan secara manual dengan mengompilasi data dari berbagai dokumen sehingga membutuhkan waktu sekitar tiga hari. LPLPO juga masih harus melalui proses persetujuan dan pengiriman secara manual kepada Puskesmas induk. Kondisi tersebut menyebabkan proses administrasi menjadi lebih lama dan berpotensi menimbulkan keterlambatan informasi. 

Berdasarkan hasil analisis proses bisnis inventori, ditemukan bahwa permasalahan utama tidak hanya terletak pada pencatatan stok, tetapi juga pada belum terintegrasinya seluruh proses inventori. Proses permintaan barang dari poli, pencatatan pemakaian obat, pemantauan nomor batch dan tanggal kedaluwarsa, penyusunan LPLPO, persetujuan dokumen, hingga proses pengadaan masih berjalan secara terpisah. Akibatnya, informasi menjadi tersebar, ketertelusuran dokumen menjadi kurang optimal, serta proses pengambilan keputusan menjadi lebih lambat. 

Hasil kajian Handayani \_et al\_ . (2024) juga menunjukkan bahwa sekitar 60% fasilitas kesehatan masih menggunakan pencatatan manual dalam pengelolaan inventori, sedangkan 40% lainnya telah mulai mengadopsi sistem informasi inventori yang mampu meningkatkan efisiensi operasional dan akurasi data. Temuan tersebut menunjukkan bahwa digitalisasi pengelolaan inventori menjadi kebutuhan yang penting bagi fasilitas pelayanan kesehatan, termasuk Puskesmas. 

Salah satu pendekatan yang dapat digunakan untuk mengatasi permasalahan tersebut adalah \_Enterprise Resource Planning\_ (ERP). ERP memungkinkan berbagai proses bisnis terintegrasi dalam satu platform sehingga informasi dapat diakses secara lebih cepat, akurat, dan konsisten. Salah satu platform ERP yang banyak digunakan adalah Odoo karena bersifat open-source, modular, dan dapat dikonfigurasi maupun dikustomisasi sesuai kebutuhan organisasi. Berbagai penelitian menunjukkan bahwa penerapan Odoo mampu meningkatkan akurasi data inventori, mempercepat proses operasional, dan mendukung pengambilan keputusan melalui informasi yang tersedia secara real-time. 

Meskipun demikian, sebagian besar penelitian terdahulu dilakukan pada perusahaan, UMKM, dan apotek, sedangkan penelitian mengenai implementasi Odoo pada fasilitas pelayanan kesehatan primer masih relatif terbatas. Selain itu, kebutuhan operasional Puskesmas memiliki karakteristik yang berbeda karena melibatkan pengelolaan obat dan BMHP, proses permintaan dari poli, penyusunan LPLPO, persetujuan berjenjang, serta integrasi dengan proses pengadaan barang. 

Berdasarkan kondisi tersebut, penelitian ini dilakukan dengan mengimplementasikan sistem pengelolaan inventori berbasis Odoo melalui proses konfigurasi dan kustomisasi yang disesuaikan dengan kebutuhan operasional Puskesmas Pondok Labu. Pengembangan sistem dilakukan menggunakan metode Water-Scrum-Fall agar proses implementasi dapat dilakukan secara terstruktur 

2 

namun tetap fleksibel terhadap perubahan kebutuhan pengguna. Melalui penelitian ini diharapkan dapat dihasilkan sistem inventori yang lebih terintegrasi, akurat, terdokumentasi, mampu mendukung efektivitas pengelolaan inventori di lingkungan Puskesmas, dan dapat mendukung kebijakan Kemenkes RI HK.01.07/MENKES/1559/2022 terkait Penerapan Sistem Pemerintahan Berbasis Elektronik (SPBE) di sektor kesehatan. 

\# \*\*1.2. Rumusan Masalah\*\* 

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah pada penelitian ini adalah sebagai berikut : 

1\. Bagaimana permasalahan dalam sistem pengelolan inventori yang saat ini terjadi di Puskesmas Pondok Labu? 

2\. Bagaimana Konfigurasi Dan Kustomisasi Odoo Untuk Pengelolaan Inventori Di Puskesmas Pondok Labu? 

\# \*\*1.3. Batasan Masalah\*\* 

Batasan masalah yang diterapkan pada penelitian ini untuk mencapai tujuan yang telah ditetapkan yaitu sebagai berikut: 

1\. Penelitian ini dilakukan di Puskesmas Kelurahan Pondok Labu. 

2\. Penelitian berfokus hanya pada inventori Obat dan Bahan Medis Habis Pakai (BMHP) di Puskesmas Pondok Labu. 

3\. Penelitian terbatas hanya pada konfigurasi dan kustomisasi Odoo 17 dengan fokus pada pengelolaan inventori pada puskesmas Pondok Labu. 

4\. Modul utama yang dikaji dan diterapkan pada penelitian ini adalah modul \_inventory\_ (namun tidak terbatas pada modul tersebut jika berdasarkan analisis dibutuhkan modul pendukung lainnya). 

5\. Metode pengembangan yang diadaptasi dalam penelitian ini adalah \_Water-Scrum-Fall\_ , pendekatan \_hybrid\_ yang mengintegrasikan struktur \_Waterfall\_ dengan Scrum dipilih karena kombinasi metode ini dinilai sesuai untuk proyek ERP berskala kecil-menengah dengan kebutuhan adaptif. 

6\. Penelitian dilakukan dari September 2025 sampai dengan April 2026\. 

\# \*\*1.4. Tujuan dan Manfaat Penelitian\*\* 

Berdasarkan rumusan masalah yang telah diidentifkasi, maka tujuan dilakukan nya penelitian ini adalah sebagai berikut: 

1\. Mengidentifikasi permasalahan dalam sistem pengelolaan inventori yang saat ini digunakan di Puskesmas Pondok Labu. 

2\. Melakukan konfigurasi dan kustomisasi modul \_Inventory\_ pada Odoo untuk mendukung pengelolaan inventori di Puskesmas Pondok Labu. 

3 

Penelitian ini diharapkan bisa memiliki kontribusi dan manfaat sebagai berikut: 

\- a. Manfaat teoretis 

Penelitian ini diharapkan dapat memberikan kontribusi dalam pengembangan ilmu di bidang sistem informasi kesehatan, khususnya terkait dengan penerapan \_Enterprise Resource Planning\_ (ERP) pada fasilitas pelayanan kesehatan tingkat pertama. Selain itu, penelitian ini juga diharapkan dapat menambah referensi mengenai pemanfaatan Odoo dalam lingkungan Puskesmas yang memiliki karakteristik berbeda dengan sektor bisnis, terutama dalam hal pengelolaan dokumen, pembagian wewenang, serta pengendalian persediaan yang disesuaikan dengan kebutuhan layanan publik. Hasil dari penelitian ini diharapkan juga dapat menjadi dasar dalam pengembangan model implementasi ERP, khususnya pada pengelolaan inventori, agar lebih sesuai dengan kondisi dan kebutuhan fasilitas kesehatan primer di Indonesia. 

\- b. Manfaat praktis 

   1\. Bagi Puskesmas 

      \- Memberikan solusi operasional berupa sistem inventori terintegrasi yang membantu meningkatkan akurasi data stok, mempercepat proses kerja, memudahkan pemantauan ketersediaan dan kedaluwarsa, serta memperkuat ketertelusuran dokumen inventori dari permintaan hingga pengadaan. 

   2\. Bagi Pemerintah dan Pemangku Kebijakan Penelitian ini mendukung kebijakan transformasi digital kesehatan sebagaimana diatur dalam Permenkes RI Nomor HK.01.07/MENKES/1559/2022 tentang Sistem Pemerintahan Berbasis Elektronik (SPBE). Dengan adanya model konfigurasi dan kustomisasi ERP Odoo di Puskesmas Pondok Labu, penelitian ini diharapkan dapat menjadi salah satu contoh sehingga dapat menjadi bahan pertimbangan replikasi kebijakan di fasilitas sejenis. 

   3\. Bagi Penelitian Selanjutnya 

      \- Penelitian ini diharapkan dapat menjadi referensi bagi akademisi maupun peneliti berikutnya yang tertarik mengembangkan kajian terkait penerapan ERP di fasilitas pelayanan kesehatan dengan lingkup dan karakteristik yang berbeda. 

\# \*\*1.5. Sistematika Penulisan\*\* 

Sistematika penulisan disusun untuk memberikan gambaran umum mengenai alur pembahasan dalam penelitian yang berjudul “ \*\*Konfigurasi dan Kustomisasi Odoo untuk Pengelolaan Inventori di Puskesmas Pondok Labu\*\* ”, sehingga 

4 

memudahkan pembaca dalam memahami isi penelitian. Adapun sistematika penulisan dalam penelitian ini adalah sebagai berikut: 

\# BAB I PENDAHULUAN 

Bab ini berisi uraian mengenai latar belakang yang melandasi dilakukannya penelitian, rumusan masalah, batasan masalah, tujuan penelitian, manfaat penelitian, serta sistematika penulisan. 

\# BAB II TINJAUAN PUSTAKA 

Bab ini membahas landasan teori yang mendukung penelitian, meliputi konsepkonsep yang relevan dengan topik yang diangkat serta hasil penelitian terdahulu yang menjadi acuan dalam penelitian ini. 

BAB III METODE PENELITIAN 

Bab ini menjelaskan tahapan-tahapan yang dilakukan dalam penelitian, termasuk metode yang digunakan, alat dan bahan penelitian, serta jadwal pelaksanaan penelitian. 

BAB IV HASIL DAN PEMBAHASAN 

Bab ini menguraikan hasil penelitian yang telah dilakukan, meliputi profil instansi, struktur organisasi, analisis sistem yang sedang berjalan, rancangan sistem usulan, hasil implementasi sistem, serta pengujian sistem menggunakan metode \_black box testing\_ dan \_user acceptance testing\_ (UAT). 

\# BAB V PENUTUP 

Bab ini berisi kesimpulan dari hasil penelitian yang telah dilakukan serta saran yang dapat digunakan sebagai pertimbangan untuk penelitian selanjutnya. 

5 

**Deni Permana: Field Service Management berbasis Odoo, PT TMD**  
\# \*\*BAB 1\. PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Perkembangan teknologi informasi dan komunikasi pada era digital saat ini telah membawa perubahan besar dalam sistem layanan dan pengelolaan bisnis di berbagai sektor, termasuk industri telekomunikasi. Internet tidak hanya berfungsi sebagai sarana komunikasi, tetapi juga telah menjadi tulang punggung utama bagi kegiatan ekonomi, pendidikan, hiburan, dan pemerintahan. Ketergantungan yang semakin tinggi terhadap internet menjadikannya infrastruktur digital global yang esensial bagi individu maupun organisasi dalam menunjang aktivitas sehari-hari (Arifin 2023\) . Dalam era transformasi digital saat ini, konektivitas internet yang cepat, stabil, dan andal tidak lagi dipandang sebagai fasilitas tambahan, melainkan sebagai fondasi utama bagi keberlangsungan aktivitas sehari-hari. Keadaan ini menjadikan kualitas layanan internet sebagai faktor strategis yang menentukan tingkat kepuasan dan produktivitas pengguna. 

Dalam konteks industri telekomunikasi, penyedia layanan internet menghadapi tantangan signifikan untuk mempertahankan keandalan jaringan. Gangguan internet, termasuk perlambatan akses, terputusnya koneksi, dan kerusakan fisik infrastruktur, dapat menyebabkan dampak signifikan terhadap aktivitas pelanggan. Penyebab gangguan dapat berasal dari kerusakan perangkat keras seperti kabel atau \_router\_ , kesalahan konfigurasi perangkat lunak, serta faktor \_eksternal\_ seperti cuaca ekstrem dan bencana alam (Candra Laili 2023\) . Masalah ini tidak hanya menghalangi produktivitas pengguna, tetapi juga berpotensi merusak kepercayaan pelanggan terhadap penyedia layanan. 

PT. Tunggal Media Data (TMD), sebagai penyedia layanan internet, menghadapi masalah gangguan jaringan internet. Penanganan gangguan yang masih didominasi oleh metode \_manual\_ atau \_semi-digital\_ sering kali menimbulkan masalah, seperti keterlambatan \_respons\_ , duplikasi pelaporan, kesulitan dalam pencatatan riwayat gangguan, serta kurangnya transparansi informasi kepada pelanggan. Akibatnya, proses layanan menjadi kurang efisien, tingkat kepuasan pelanggan menurun, dan perusahaan berisiko melanggar standar \_Service Level Agreement\_ (SLA) yang ditetapkan oleh pemerintah (KEMENKOMINFO 2021\) . Pemenuhan metrik SLA ini membutuhkan sistem operasional yang terotomatisasi dengan jejak \_audit\_ ( \_audit trail\_ ) yang kuat, guna mencegah terjadinya manipulasi waktu perbaikan secara manual oleh pihak lapangan. Seiring dengan pertumbuhan jumlah pelanggan, kebutuhan akan sistem yang dapat mendukung pengelolaan layanan secara efisien, tepat, dan terintegrasi semakin mendesak. 

Sesuai dengan ketentuan yang diatur dalam Permenko No. 5 Tahun 2021 mengenai penataan jaringan dan untuk menjaga kualitas layanan, PT. Tunggal Media Data (TMD) telah menetapkan \_Service Level Agreement\_ (SLA) \_internal\_ . SLA ini difokuskan secara spesifik pada metrik Waktu Penyelesaian ( \_Resolution Time\_ ), yang berfungsi sebagai komitmen penyelesaian kendala jaringan bagi pelanggan sekaligus alat ukur evaluasi kinerja teknisi. Standar waktu penyelesaian 

1 

2 

ini dikategorikan secara tegas berdasarkan jenis langganan, yakni batas waktu penyelesaian maksimum 6 jam untuk pelanggan korporat, dan waktu penyelesaian maksimum 8 jam untuk pelanggan rumah tangga (ritel). 

Pemenuhan standar waktu penyelesaian ini sangat penting untuk mempertahankan ketersediaan layanan jaringan serta menghindari sanksi kompensasi atau pemutusan layanan dari pelanggan ( \_churn rate\_ ). Selanjutnya, untuk memastikan evaluasi kinerja tim lapangan berlangsung secara adil dan objektif, sistem pengukuran durasi penyelesaian masalah tidak mengadopsi skema 24 jam penuh. Waktu dihitung berdasarkan jam operasional yang memungkinkan fungsi \_On\_ / \_Off\_ (jeda), sehingga penghitungan batas waktu perbaikan 6 jam atau 8 jam tersebut akan otomatis terhenti di luar jam kerja atau ketika proses perbaikan terhambat oleh kendala yang berasal dari pihak pelanggan. 

Beberapa solusi digital telah diterapkan oleh penyedia layanan lain, seperti sistem tiket masalah berbasis aplikasi internal atau pemantauan jaringan menggunakan \_Digital Twin Network\_ s (Sun \_et al.\_ 2021\) . Namun, pendekatan tersebut umumnya masih memiliki keterbatasan, tidak sepenuhnya terintegrasi dengan modul bisnis lainnya, sulit untuk menyediakan analitik waktu nyata, dan kurang ramah bagi teknisi lapangan yang beroperasi di lokasi dengan infrastruktur terbatas. Penelitian ini menunjukkan kebutuhan akan \_platform\_ manajemen layanan lapangan yang lebih adaptif, terintegrasi, dan mendukung transformasi digital secara menyeluruh. 

Untuk mengatasi permasalahan tersebut, penelitian ini mengusulkan pengembangan sistem Manajemen Layanan Lapangan berbasis Odoo. Modul FSM di Odoo memiliki kemampuan untuk mengelola seluruh siklus layanan lapangan, mulai dari pembuatan tiket gangguan, penjadwalan teknisi, pelacakan status pekerjaan secara \_real-time\_ , hingga integrasi dengan modul lain (Hermanto \_et al.\_ 2023). Odoo juga menyediakan akses berbasis \_cloud\_ dan perangkat \_mobile\_ , memungkinkan teknisi untuk memperbarui status pekerjaan di lapangan secara langsung, meskipun terdapat kendala jaringan. Lebih lanjut, integrasi \_dashboard\_ analitik memungkinkan manajemen untuk secara transparan memantau durasi penyelesaian, serta kepatuhan terhadap SLA. 

Penelitian ini berjudul “ \_Field Service Management\_ Berbasis Odoo untuk Penanganan Gangguan Jaringan Internet Pelanggan pada PT. Tunggal Media Data (TMD)”. Tujuannya adalah merancang dan mengimplementasikan sistem terintegrasi yang dapat meningkatkan kecepatan penanganan gangguan, efisiensi operasional, serta kepatuhan terhadap SLA. Penelitian ini mengusung metodologi \_hybrid Water-Scrum-Fall\_ untuk mengintegrasikan logika \_Agile\_ ( \_Scrum\_ ) pada sistem ERP Odoo yang umumnya bersifat \_waterfall\_ , sehingga lebih adaptif terhadap iterasi data lapangan. Penelitian ini diharapkan tidak hanya memberikan kontribusi praktis bagi PT. TMD dalam meningkatkan kualitas layanan pelanggan, tetapi juga berkontribusi pada pengembangan pengetahuan mengenai penerapan ERP di sektor telekomunikasi. 

3 

Oleh karena itu, hasil dari penelitian ini akan memberikan manfaat yang signifikan. Secara praktis, PT. TMD mengimplementasikan solusi digital untuk meningkatkan kepuasan pelanggan dan memastikan kualitas layanan sesuai dengan regulasi. Secara akademik, penelitian ini dapat berfungsi sebagai referensi dan model implementasi \_Enterprise Resource Planning\_ berbasis Odoo dalam sektor telekomunikasi Indonesia, khususnya dalam manajemen layanan lapangan. 

\# \*\*1.2. Rumusan Masalah\*\* 

Berdasarkan latar belakang yang telah diuraikan, permasalahan yang dihadapi oleh PT Tunggal Media Data (TMD) dalam penanganan gangguan jaringan internet pelanggan adalah belum tersedianya sistem yang mampu mengelola dan mengukur kinerja layanan secara terstruktur dan terintegrasi. 

Pada kondisi sebelum sistem diterapkan, proses pencatatan gangguan dan penanganannya masih belum terdokumentasi secara sistematis, sehingga perusahaan mengalami kesulitan dalam mengetahui waktu respons, waktu penyelesaian, serta tingkat kepatuhan terhadap \_Service Level Agreement\_ (SLA). Hal ini berdampak pada keterbatasan perusahaan dalam memantau kinerja layanan secara objektif dan berkelanjutan. 

Berdasarkan permasalahan tersebut, maka rumusan masalah dalam penelitian ini adalah sebagai berikut: 

1\. Bagaimana merancang dan mengimplementasikan sistem \_Field Service Management\_ berbasis Odoo yang dilengkapi dengan \_dashboard analitik\_ menggunakan metodologi \_Water-Scrum-Fall\_ untuk mengelola tiket gangguan internet pelanggan di PT. Tunggal Media Data? 

2\. Bagaimana sistem \_Field Service Management\_ berbasis Odoo dapat digunakan untuk mengukur parameter SLA, seperti waktu respons dan waktu penyelesaian gangguan? 

3\. Bagaimana perbandingan kondisi penanganan gangguan jaringan internet sebelum dan sesudah penerapan sistem, khususnya terkait aspek \_usability\_ , ketepatan durasi penyelesaian gangguan, serta kepatuhan terhadap standar \_Service Level Agreement\_ (SLA)? 

\# \*\*1.3. Batasan Penelitian\*\* 

Terdapat beberapa batasan dalam penelitian ini, yaitu: 

1\. Objek dan Skala Implementasi: Penelitian ini menjadikan PT. Tunggal Media Data (TMD) sebagai objek studi kasus. Perancangan dan penerapan sistem \_Field Service Management\_ berbasis Odoo dalam pengelolaan tiket gangguan ini dibatasi hanya sampai pada tahap \_user testing\_ terbatas, dan tidak dilakukan \_full deployment\_ karena adanya keterbatasan akses perusahaan. 

2\. Ruang Lingkup Data dan Teknis Kustomisasi: Data operasional yang dianalisis meliputi data karyawan, pelanggan, dan riwayat penanganan gangguan pada rentang tahun 2024-2025. Secara teknis, pengembangan 

4 

sistem tidak hanya sebatas konfigurasi antarmuka bawaan (UI), melainkan mencakup kustomisasi \_source code\_ menggunakan bahasa pemrograman Python dan arsitektur XML untuk mengunci aturan hak akses, logika bisnis \_Service Level Agreement\_ (SLA), serta pembuatan \_dashboard\_ analitik. 

3\. Parameter Evaluasi: Evaluasi kinerja sistem dibatasi pada pengukuran dan perbandingan kondisi operasional dengan UAT. Parameter yang dinilai difokuskan pada aspek kegunaan sistem ( \_usability\_ ), ketepatan durasi penyelesaian gangguan berdasarkan pemenuhan SLA, serta relevansi \_dashboard\_ analitik dalam mendukung pengambilan keputusan manajerial. 

\# \*\*1.4. Tujuan Penelitian\*\* 

Berdasarkan poin-poin rumusan masalah yang telah dikemukakan, tujuan dilakukannya penelitian ini adalah sebagai berikut: 

   1\. Mengembangkan sistem \_Field Service Management\_ berbasis Odoo yang dapat digunakan PT. Tunggal Media Data untuk menangani tiket gangguan pelanggan secara terintegrasi, yang dilengkapi dengan \_dashboard\_ analitik guna memantau kinerja layanan secara \_real-time\_ . 

   2\. Mengembangkan fitur pengukuran parameter \_Service Level Agreement\_ (SLA), khususnya waktu respons dan waktu penyelesaian gangguan, melalui sistem \_Field Service Management\_ berbasis Odoo. 

   3\. Membandingkan kondisi penanganan gangguan jaringan internet pelanggan sebelum dan sesudah penerapan sistem sebagai bentuk pembuktian manfaat sistem yang dikembangkan. 

\- \*\*1.5. Manfaat Penelitian\*\* 

\- Dengan merujuk pada tujuan yang telah dijelaskan sebelumnya, diharapkan 

\- hasil dari penelitian ini dapat memberikan manfaat sebagai berikut: 1\. Manfaat Praktis 

      \- a. Bagi PT. Tunggal Media Data (TMD): Membantu perusahaan mempercepat penanganan gangguan pelanggan, meningkatkan transparansi proses layanan, serta menyediakan data akurat untuk kepatuhan SLA. 

      \- b. Bagi Pelanggan: Memberikan layanan yang lebih cepat, terukur, dan transparan, sehingga meningkatkan tingkat kepuasan dan kepercayaan terhadap layanan internet yang diberikan PT. TMD. 

   2\. Manfaat Akademis 

      \- a. Menjadi kontribusi ilmiah dalam penerapan metode \_WaterScrum-Fall\_ pada sistem \_Enterprise Resource Planning\_ (ERP) khususnya modul FSM berbasis Odoo pada bidang telekomunikasi. 

5 

\- b. Memberikan referensi kajian dan implementasi bagi penelitian selanjutnya terkait integrasi ERP, \_dashboard\_ analitik, maupun pengelolaan SLA di industri berbasis layanan digital. 

\# \*\*1.6. Luaran yang Diharapkan\*\* 

Hasil yang diharapkan dari penelitian ini adalah implementasi sistem bisnis berbasis Odoo yang dapat mengelola tiket gangguan internet pelanggan secara efektif dan efisien untuk PT. Tunggal Media Data (TMD). Sistem ini berfungsi sebagai alat pencatatan laporan gangguan dan dilengkapi dengan \_dashboard\_ analitik yang menampilkan visualisasi data secara \_real-time,\_ durasi penyelesaian, serta pencapaian kinerja berdasarkan indikator \_Service Level Agreement\_ (SLA). Dengan adanya \_dashboard\_ tersebut, manajemen PT. TMD dapat lebih efisien dalam melakukan pemantauan, evaluasi kinerja teknisi, serta pengambilan keputusan strategis yang cepat dan berbasis data. Selain itu, penelitian ini menghasilkan dokumentasi komprehensif yang mencakup analisis kebutuhan, desain sistem (UML dan analisis GAP), konfigurasi serta kustomisasi modul Odoo, hingga hasil pengujian dan evaluasi bersama pengguna. Hasil ini diharapkan memberikan kontribusi nyata tidak hanya untuk peningkatan kualitas layanan di PT. TMD dan kepuasan pelanggan, tetapi juga sebagai referensi akademik dan implementasi praktis sistem Manajemen Layanan Lapangan berbasis ERP di industri telekomunikasi di Indonesia. 

\# \*\*1.7. Sistematika Penulisan\*\* 

Penyusunan skripsi ini diuraikan secara sistematis ke dalam lima bab utama, ditambah dengan bagian pelengkap berupa daftar pustaka dan lampiran. Sistematika penulisan ini bertujuan untuk memberikan gambaran yang jelas dan terstruktur mengenai alur pembahasan penelitian. Adapun rincian isi dari masingmasing bagian adalah sebagai berikut: BAB I PENDAHULUAN Bab ini menguraikan landasan fundamental penelitian yang mencakup latar belakang masalah, perumusan masalah, batasan penelitian, tujuan yang ingin dicapai, serta manfaat penelitian. Selain itu, bab ini juga menjelaskan luaran yang diharapkan dan sistematika penulisan untuk memberikan panduan terkait arah dan alur penyusunan skripsi. 

BAB II TINJAUAN PUSTAKA 

Bab ini menyajikan kajian literatur dan landasan teori yang relevan sebagai pijakan dalam penelitian. Pembahasan difokuskan pada konsep dasar \_Field Service Management\_ (FSM) dan \_Helpdesk\_ berbasis Odoo, \_Dashboard\_ Analitik, Gangguan Jaringan Internet, dan Manajemen Layanan Teknologi Informasi. Lebih lanjut, bab ini mengkaji teori teknis yang mencakup metodologi \_Water-Scrum-Fall Project Management\_ , \_Arsitektur Three-Tier\_ , Sistem Basis Data, \_Unified Modeling Language\_ 

6 

(UML), \_Black Box Testing\_ , \_User Acceptance Testing\_ (UAT), serta komparasi dengan penelitian-penelitian terdahulu yang relevan. 

BAB III METODE PENELITIAN 

Bab ini menjabarkan pendekatan dan tahapan metodologi \_Water-ScrumFall\_ yang diterapkan untuk menyelesaikan masalah penelitian. Alur kerja diuraikan secara komprehensif ke dalam tiga fase utama, yakni Fase Perencanaan ( \_Waterfall\_ Awal), Fase Pengembangan Iteratif ( \_Scrum\_ ), dan Fase Penyelesaian ( \_Waterfall\_ Akhir). Selain itu, bab ini juga merincikan spesifikasi alat bantu penelitian yang digunakan beserta jadwal rencana pelaksanaan kegiatan. 

BAB IV HASIL DAN PEMBAHASAN 

Bab ini memaparkan implementasi sistem dan hasil pengujian berdasarkan tahapan metodologi yang telah dirancang. Pembahasan diawali dengan tinjauan perusahaan (PT. Tunggal Media Data), dilanjutkan dengan proses analisis dan perencanaan sistem, tahapan pengembangan iteratif (mencakup konfigurasi dan kustomisasi Odoo), hingga proses rilis dan validasi akhir untuk mengevaluasi sejauh mana sistem FSM yang dikembangkan mampu memenuhi kebutuhan operasional perusahaan. 

\- BAB V PENUTUP 

Bab ini berisi kesimpulan komprehensif yang ditarik dari seluruh rangkaian analisis, perancangan, dan implementasi sistem. Pada bab ini juga diberikan saran-saran konstruktif yang dapat dijadikan acuan untuk perbaikan, optimalisasi, maupun pengembangan sistem lebih lanjut pada penelitian di masa mendatang. 

DAFTAR PUSTAKA 

Bagian ini memuat daftar keseluruhan sumber referensi atau rujukan berupa buku teks, jurnal ilmiah, artikel, serta dokumen regulasi yang digunakan secara sah sebagai landasan teori dan acuan selama proses penelitian berlangsung. 

\# LAMPIRAN. 

Bagian ini melampirkan seluruh dokumen pendukung yang melengkapi penelitian, seperti instrumen pengumpulan data, transkrip hasil wawancara, kuesioner, dokumentasi implementasi dan pengujian sistem, serta suratsurat administratif terkait. 

**Muhammad Durmuji: Kustomisasi Modul Inventory Odoo, PT Chemindo Ekatama (2026)**  
1 

\# \*\*BAB 1\. PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Perkembangan teknologi informasi mendorong transformasi digital dalam manajemen rantai pasok, khususnya pada perusahaan distribusi dengan kompleksitas pengelolaan stok dan frekuensi transaksi yang tinggi. Dalam kegiatan distribusi, pengelolaan persediaan memiliki peran penting karena berkaitan dengan ketersediaan barang, kesesuaian data stok, dan kelancaran proses operasional perusahaan. Pengelolaan persediaan yang masih dilakukan secara terpisah berpotensi menyebabkan ketidaksesuaian data, keterlambatan pembaruan data stok, serta menurunkan efisiensi kerja. 

Untuk mengatasi permasalahan tersebut, perusahaan memerlukan sistem yang mampu mengintegrasikan proses bisnis secara terpusat. Salah satu solusi yang dapat digunakan adalah \_Enterprise Resource Planning\_ (ERP), yaitu sistem yang memungkinkan sinkronisasi data antar bagian secara langsung tanpa pencatatan ulang sehingga mendukung kesesuaian data stok dan efektivitas pengelolaan persediaan (Alan Dennis \_et al.\_ 2022). 

PT. Chemindo Ekatama merupakan perusahaan distribusi dengan variasi produk dan tingkat perputaran persediaan yang beragam. Berdasarkan hasil observasi dan wawancara, pengelolaan persediaan pada perusahaan masih dilakukan secara konvensional dan belum terintegrasi dalam satu sistem. Kondisi tersebut menyebabkan ketidaksesuaian antara stok fisik dan pencatatan administratif, terutama pada aktivitas dengan frekuensi transaksi tinggi. 

Data persediaan belum diperbarui secara langsung pada saat transaksi berlangsung, melainkan melalui pencatatan berkala menggunakan media yang berbeda, seperti buku stok dan \_spreadsheet\_ . Kondisi tersebut menyebabkan keterlambatan aliran informasi pada divisi gudang dan divisi \_Purchasing\_ , meningkatkan risiko duplikasi data, kesalahan administrasi, serta menyulitkan proses penelusuran data persediaan. Selain itu, perusahaan belum memiliki mekanisme pengendalian stok, seperti peringatan stok minimum, untuk meminimalkan risiko kekurangan maupun kelebihan persediaan. 

Penelitian terdahulu oleh (Novita 2023\) menunjukkan bahwa implementasi ERP dapat mendukung peningkatan kesesuaian data stok dan efisiensi proses bisnis. Namun, penelitian tersebut belum membahas secara spesifik konfigurasi modul, integrasi proses pengadaan terhadap pembaruan data stok, serta evaluasi operasional pada perusahaan distribusi skala meneng ah. 

\# \*\*1.2. Rumusan Masalah\*\* 

Berdasarkan latar belakang yang telah diuraikan, penelitian ini merumuskan pertanyaan penelitian yang berfokus pada implementasi sistem serta dampaknya 

2 

terhadap pengelolaan persediaan berdasarkan kondisi operasional perusahaan sebagai berikut: 

1\. Bagaimana kondisi awal pengelolaan persediaan di PT. Chemindo Ekatama ditinjau dari aspek kesesuaian data stok, kecepatan pembaruan data stok, dan integrasi proses operasional? 

2\. Bagaimana konfigurasi dan implementasi modul \_Inventory\_ pada sistem Odoo yang disesuaikan dengan kebutuhan operasional perusahaan? 

3\. Bagaimana tingkat penerimaan pengguna terhadap sistem yang diimplementasikan melalui \_User Acceptance Testing\_ (UAT) berdasarkan persepsi kemudahan penggunaan dan kemanfaatan sistem? 

\# \*\*1.3. Batasan Masalah\*\* 

Agar penelitian ini terarah dan sesuai dengan tujuan yang telah ditetapkan, maka ruang lingkup penelitian dibatasi pada hal-hal berikut: 

1\. Penelitian difokuskan pada proses pengelolaan persediaan yang meliputi pengadaan barang, penerimaan barang, penyimpanan, dan pengiriman barang. 

2\. Penelitian dibatasi pada analisis operasional pengelolaan persediaan berdasarkan hasil observasi, wawancara semi-terstruktur dan studi literatur 

3\. Implementasi sistem menggunakan Odoo \_Community Edition\_ versi 17\. 

4\. Penelitian difokuskan pada implementasi dan konfigurasi modul \_Inventory\_ , sedangkan modul \_Purchase\_ digunakan sebagai modul pendukung integrasi proses pengadaan dan pembaruan data stok. 

5\. Kustomisasi sistem dilakukan secara terbatas dalam bentuk pengembangan modul tambahan tanpa melakukan modifikasi terhadap kode inti Odoo. 

6\. Evaluasi sistem dilakukan berdasarkan skenario operasional pengelolaan persediaan dan pengujian pengguna. 

7\. Sistem dikonfigurasi dan diuji pada lingkungan lokal untuk menjaga konsistensi proses implementasi dan pengujian. 

8\. Penelitian ini tidak mencakup proses pengembalian barang kepada vendor. 

\# \*\*1.4. Tujuan dan Manfaat Penelitian\*\* 

Tujuan penelitian ini disusun untuk menganalisis perubahan pengelolaan persediaan berdasarkan indikator operasional sebelum dan sesudah implementasi sistem secara sistematis, sehingga hasil yang diperoleh tidak hanya bersifat teknis, tetapi juga dapat dianalisis secara terstruktur. 

Adapun tujuan dari penelitian ini adalah sebagai berikut: 

3 

1\. Mengidentifikasi kondisi awal pengelolaan persediaan di PT. Chemindo Ekatama berdasarkan aspek kesesuaian data stok, kecepatan pembaruan data stok, dan integrasi proses operasional. 

2\. Melakukan konfigurasi dan implementasi modul \_Inventory\_ pada Odoo sesuai dengan kebutuhan operasional perusahaan. 

3\. Menganalisis tingkat penerimaan pengguna terhadap sistem melalui \_User Acceptance Testing\_ (UAT) berdasarkan persepsi kemudahan penggunaan dan kemanfaatan sistem. 

Secara teoretis, penelitian ini diharapkan dapat memberikan kontribusi dalam bidang Sistem Informasi, khususnya pada implementasi, konfigurasi, dan kustomisasi Odoo sebagai ERP berbasis \_open source\_ untuk mendukung pengelolaan persediaan pada perusahaan distribusi. Selain itu, penelitian ini juga diharapkan dapat memberikan kajian mengenai integrasi modul \_Inventory\_ dan \_Purchase\_ dalam mendukung pembaruan data stok. 

Secara praktis, penelitian ini diharapkan dapat membantu perusahaan dalam meningkatkan pengelolaan persediaan melalui penerapan sistem yang terintegrasi. Sistem yang diimplementasikan mendukung pencatatan transaksi dan pembaruan data stok berdasarkan validasi transaksi sehingga informasi persediaan dapat diperbarui secara lebih cepat, terstruktur, dan konsisten antar bagian. Selain itu, penelitian ini diharapkan dapat menjadi referensi dalam implementasi Odoo pada perusahaan distribusi dengan karakteristik operasional yang serupa. 

\# \*\*1.5. Sistematika Penulisan\*\* 

Sistematika penulisan ini ditulis untuk memberikan kemudahan informasi bagi pembaca dan memberikan sedikit gambaran dalam "Konfigurasi dan kustomisasi modul \_Inventory\_ pada aplikasi Odoo studi kasus PT. Chemindo Ekatama", berikut ini adalah sistematika penulisannya: 

BAB I PENDAHULUAN 

Bab I Pendahuluan berisi latar belakang penelitian, rumusan masalah, batasan masalah, tujuan dan manfaat penelitian, serta sistematika penulisan yang menjadi dasar dan arah penelitian. 

BAB II TINJAUAN PUSTAKA 

Bab II Tinjauan Pustaka membahas teori-teori yang mendukung penelitian, meliputi konsep \_Enterprise Resource Planning\_ (ERP), Odoo, sistem pengelolaan persediaan, konfigurasi dan kustomisasi sistem ERP, \_User Acceptance Testing\_ (UAT), metode \_Water Scrum Fall\_ , Diagram \_Unified Modeling Language\_ (UML), serta penelitian terdahulu yang digunakan sebagai dasar teori dan identifikasi kesenjangan penelitian. 

4 

\# BAB III METODE PENELITIAN 

Bab III Metode Penelitian menjelaskan tahapan penelitian yang dilakukan menggunakan pendekatan \_Water Scrum Fall\_ , mulai dari identifikasi masalah, analisis kebutuhan sistem, perancangan sistem, pelaksanaan \_Sprint\_ pengembangan, hingga tahap pengujian dan evaluasi sistem. Selain itu, bab ini juga menjelaskan teknik pengumpulan data, proses implementasi sistem, dan metode pengujian yang digunakan dalam penelitian. 

\# BAB IV HASIL DAN PEMBAHASAN 

Bab IV Hasil dan Pembahasan menyajikan hasil analisis sistem berjalan, perancangan sistem usulan, implementasi dan kustomisasi sistem Odoo, pengujian integrasi sistem, \_Black Box Testing\_ , \_User Acceptance Testing\_ (UAT), serta pembahasan hasil implementasi berdasarkan permasalahan dan tujuan penelitian. 

BAB V PENUTUP 

Bab V Penutup berisi kesimpulan penelitian berdasarkan hasil implementasi dan pengujian sistem, serta saran untuk pengembangan dan implementasi sistem pada penelitian selanjutnya. 

**Haikal Rafif A. S.: Migrasi Data menuju Single Source of Truth**  
\# \*\*BAB I\*\* 

\# \*\*PENDAHULUAN\*\* 

\# \*\*1.1.   Latar Belakang\*\* 

Perkembangan  teknologi  informasi  telah  mendorong  transformasi  digital  di  berbagai sektor  industri,  termasuk  industri  otomotif  dan  jasa  perbengkelan.  Dalam  era  digital,  data menjadi  aset  strategis  yang  berperan  penting  dalam  mendukung  proses  bisnis  dan pengambilan  keputusan  organisasi.  Pengelolaan  data  yang  baik  memungkinkan  organisasi meningkatkan  efisiensi  operasional  serta  menghasilkan  informasi  yang  akurat  dan  relevan. Hal  ini  sejalan  dengan  penelitian  oleh  Matondang  dan  Nasution  (2025)  yang  menyatakan bahwa  pengelolaan  master  data  merupakan  komponen  krusial  dalam  sistem  informasi  modern karena berpengaruh langsung terhadap kualitas pengambilan keputusan. 

Akan  tetapi,  dalam  praktiknya,  banyak  organisasi  menghadapi  permasalahan  berupa sistem  yang  terisolasi  ( \_data  silo\_ )  akibat  pengembangan  aplikasi  yang  dilakukan  secara terpisah.  Kondisi  ini  menyebabkan  data  tersebar  di  berbagai  sistem  dengan  struktur  yang berbeda,  sehingga  menimbulkan  permasalahan  seperti  duplikasi  data,  inkonsistensi,  serta rendahnya  kualitas  data.  Albetdron  dan  Hidayanto  (2023)  menjelaskan  bahwa  rendahnya kualitas  pengelolaan  master  data  dapat  menyebabkan  terjadinya  silo  data,  duplikasi,  dan inkonsistensi yang berdampak pada menurunnya kualitas sistem informasi secara keseluruhan. 

Selain  itu,  integrasi  data  dari  berbagai  sumber  heterogen  juga  menjadi  tantangan  teknis yang  kompleks.  Setiap  sistem  biasanya  memiliki  struktur,  format,  dan  mekanisme penyimpanan  data  yang  berbeda  sehingga  memerlukan  pendekatan  khusus  untuk mengintegrasikannya.  Dalam  konteks  ini,  proses  integrasi  data  tidak  hanya  melibatkan penggabungan  data,  tetapi  juga  transformasi  dan  pembersihan  data  agar  dapat  digunakan secara konsisten. 

Permasalahan  tersebut  juga  dialami  oleh  platform  eBengkelku.com,  sebuah  ekosistem digital  berbasis  aplikasi  yang  berperan  sebagai \_platform  aggregator\_ yang  menghubungkan pelanggan  bengkel  ( \_customer\_ )  dengan  penyedia  layanan  bengkel  ( \_merchant\_ )  dalam  satu sistem  terpadu.  Berbeda  dengan  model  bisnis  bengkel  konvensional,  eBengkelku.com  tidak beroperasi  sebagai  penyedia  layanan  secara  langsung,  melainkan  sebagai  fasilitator  yang menghubungkan  berbagai  bengkel  sebagai  mitra  dalam  satu  ekosistem  digital.  Platform  ini dikembangkan  dalam  dua  sistem  yang  berbeda,  yaitu  platform  web  berbasis  Laravel  dengan basis  data  MySQL,  serta  platform  mobile  berbasis  Flutter  dengan  Supabase  sebagai  basis datanya.  Pengembangan  yang  dilakukan  secara  divergen  menyebabkan  kedua  platform memiliki  struktur  dan  sumber  data  yang  berbeda.  Kondisi  ini  menyebabkan  tidak  terdapat sumber kebenaran tunggal ( \_single source of truth\_ ). 

Dampak  dari  kondisi  tersebut  terlihat  pada  terjadinya  inkonsistensi  data  antar  platform. Fenomena  ini  sejalan  dengan  penelitian  oleh  Purwanto  dan  Rasyid  (2023)  yang  menyatakan bahwa  sistem  yang  tidak  terintegrasi  dengan  baik  akan  menyebabkan  proses  sinkronisasi  data 

1 

menjadi  tidak  optimal  serta  meningkatkan  potensi  inkonsistensi  data  antar  sistem.  Akibatnya, informasi  yang  dihasilkan  menjadi  tidak  konsisten  dan  berpotensi  menurunkan  kualitas layanan  serta  kepercayaan  pengguna.  Oleh  karena  itu,  diperlukan  suatu  pendekatan  yang mampu mengintegrasikan sistem serta mengelola data secara terpusat. 

Dalam  mengatasi  permasalahan  tersebut,  diperlukan  pendekatan  yang  tidak  hanya berfokus  pada  integrasi  komunikasi  antar  sistem,  tetapi  juga  pada  pengelolaan  dan  konsolidasi data  secara  menyeluruh.  Integrasi  sistem  tanpa  pengelolaan  data  yang  baik  tetap  berpotensi menghasilkan  inkonsistensi,  sehingga  diperlukan  mekanisme  yang  mampu  memastikan keseragaman dan keandalan data yang digunakan. 

Pendekatan  Master  Data  Management  (MDM)  berperan  penting  dalam  memastikan bahwa  data  utama  dikelola  secara  terpusat  dan  konsisten,  sehingga  dapat  digunakan  sebagai acuan  bersama  antar  sistem.  Lestari  dan  Nasution  (2025)  menjelaskan  bahwa  MDM  mampu meningkatkan  kualitas  informasi  bisnis  dengan  mengatasi  permasalahan  duplikasi, inkonsistensi,  dan  penyebaran  data  di  berbagai  sistem  yang  terpisah.  Dengan  demikian,  MDM menjadi  landasan  konseptual  dalam  membangun \_single  source  of  truth\_ pada  sistem  yang terintegrasi.  Dalam  implementasinya,  konsolidasi  data  tersebut  umumnya  dilakukan  melalui proses \_Extract\_ , \_Transform\_ , \_Load\_ (ETL),  yang  memungkinkan  pengambilan  data  dari  berbagai sumber,  transformasi  ke  dalam  format  yang  seragam,  serta  pemuatan  ke  dalam  sistem terpusat.  Dengan  adanya  proses  ETL,  organisasi  dapat  memastikan  bahwa  data  yang digunakan telah melalui proses integrasi dan validasi sebelum digunakan oleh sistem lain. 

Di  sisi  lain,  untuk  mendukung  komunikasi  dan  pertukaran  data  antar  sistem  secara terintegrasi,  diperlukan  mekanisme  integrasi  berbasis  layanan  seperti  REST  API.  Simbulan dan  Aryanto  (2024)  menjelaskan  bahwa  implementasi  REST  API  mampu  meningkatkan efisiensi  pengelolaan  data  serta  mempermudah  komunikasi  antar  sistem  yang  berbeda. Pangestu  et  al.  (2022)  juga  menyatakan  bahwa  REST  API  memungkinkan  pertukaran  data secara  terintegrasi  antar  sistem  yang  berbeda  sehingga  mendukung  integrasi  yang  lebih fleksibel  dan  efisien.  Dengan  demikian,  kombinasi  antara  ETL  sebagai  mekanisme konsolidasi  data  dan  REST  API  sebagai  media  integrasi  sistem  menjadi  solusi  yang komprehensif dalam mengatasi permasalahan fragmentasi data. 

Berdasarkan  uraian  tersebut,  penelitian  ini  bertujuan  untuk  merancang  dan mengimplementasikan  solusi  integrasi  sistem  menggunakan  pendekatan  ETL  dan  REST  API guna  mengatasi  permasalahan  fragmentasi  data  pada  ekosistem  digital  eBengkelku.com. Solusi  ini  diharapkan  mampu  mewujudkan  sistem  yang  terintegrasi  serta  meningkatkan konsistensi dan kualitas data dalam mendukung proses bisnis secara berkelanjutan. 

2 

\# \*\*1.2.   Rumusan Masalah\*\* 

Berdasarkan  latar  belakang  yang  telah  diuraikan,  maka  rumusan  masalah  dalam penelitian ini adalah sebagai berikut: 

1\.  Bagaimana  mengatasi  permasalahan  fragmentasi  data  akibat  sistem  yang  terisolasi pada platform eBengkelku.com? 

2\.  Bagaimana  merancang  dan  mengimplementasikan  mekanisme  konsolidasi  dan integrasi  data  untuk  mewujudkan \_single  source  of  truth\_ menggunakan  pendekatan  ETL dan REST API? 

3\.  Bagaimana  mengevaluasi  efektivitas  solusi  integrasi  sistem  dalam  meningkatkan konsistensi dan kualitas data? 

\# \*\*1.3.   Batasan Masalah\*\* 

\- Untuk  menjaga  fokus  penelitian  agar  tidak  melebar,  maka  penelitian  ini  memiliki 

\- batasan sebagai berikut: 

   1\.  Penelitian  difokuskan  pada  integrasi  sistem  antara  platform  web  dan  mobile  pada ekosistem digital eBengkelku.com yang sebelumnya berjalan secara terpisah. 

   2\.  Penelitian  tidak  mencakup  perubahan  atau  penambahan  fitur  pada  masing-masing platform,  serta  tidak  melakukan  perubahan  signifikan  pada  struktur  basis  data  yang telah ada. 

   3\.  Proses  konsolidasi  data  dilakukan  menggunakan  pendekatan \_Extract\_ , \_Transform\_ , \_Load\_ (ETL) untuk mengintegrasikan data dari berbagai sumber ke dalam sistem utama. 

   4\.  Integrasi  antar  sistem  dilakukan  menggunakan  REST  API  sebagai  media  komunikasi data antar platform. 

   5\.  Penelitian  berfokus  pada  konsolidasi  data  untuk  mewujudkan  sumber  kebenaran tunggal ( \_single source of truth\_ ) pada sistem yang terintegrasi. 

   6\.  Evaluasi  dalam  penelitian  ini  dibatasi  pada  aspek  konsistensi  dan  kualitas  data,  serta tidak mencakup pengujian performa sistem secara mendalam. 

\# \*\*1.4.   Tujuan Penelitian\*\* 

\- Berdasarkan  rumusan  masalah  yang  telah  dirumuskan,  maka  tujuan  dari  penelitian  ini 

\- adalah sebagai berikut: 

   1\.  Mengatasi  permasalahan  fragmentasi  data  akibat  sistem  yang  terisolasi  pada  platform eBengkelku.com. 

   2\.  Merancang  dan  mengimplementasikan  mekanisme  konsolidasi  dan  integrasi  data untuk  mewujudkan \_single  source  of  truth\_ menggunakan  pendekatan  ETL  dan  REST API. 

   3\.  Mengevaluasi  efektivitas  solusi  integrasi  sistem  dalam  meningkatkan  konsistensi  dan kualitas data pada platform eBengkelku.com. 

3 

\# \*\*1.5.   Manfaat Penelitian\*\* 

Penelitian  ini  diharapkan  dapat  memberikan  manfaat  baik  secara  teoritis  maupun  praktis sebagai berikut: 

\# \*\*1.5.1.   Manfaat Teoretis\*\* 

1\.  Penelitian  ini  diharapkan  dapat  memberikan  kontribusi  dalam  pengembangan kajian  di  bidang  sistem  informasi,  khususnya  terkait  integrasi  sistem  dan pengelolaan data menggunakan pendekatan Master Data Management (MDM). 

2\.  Penelitian  ini  dapat  menjadi  referensi  tambahan  dalam  penerapan  konsep \_single source  of  truth\_ melalui  mekanisme  konsolidasi  data  menggunakan  ETL  dan integrasi sistem menggunakan REST API. 

3\.  Penelitian  ini  dapat  menjadi  studi  kasus  empiris  dalam  penerapan  metodologi Design  Science  Research  (DSR)  untuk  menyelesaikan  permasalahan  nyata  terkait fragmentasi data pada sistem yang terisolasi. 

\# \*\*1.5.2.   Manfaat Praktis\*\* 

1\.  Memberikan  solusi  implementatif  bagi  eBengkelku.com  dalam  mengatasi permasalahan fragmentasi dan inkonsistensi data antar platform. 

2\.  Membantu  meningkatkan  konsistensi,  kualitas,  dan  keandalan  data  yang  digunakan dalam proses operasional dan pengambilan keputusan. 

3\.  Mendukung  terciptanya  sistem  yang  terintegrasi  melalui  penerapan  ETL  dan REST API sebagai mekanisme konsolidasi dan pertukaran data antar platform. 

4\.  Menjadi  acuan  bagi  pengembang  sistem  dalam  mengintegrasikan  sistem  yang terpisah  melalui  pendekatan  konsolidasi  data  dan  penyediaan  layanan  terpusat, dengan  tetap  mempertimbangkan  keterbatasan  sistem  eksisting  dan  kebutuhan penyesuaian pada sisi aplikasi. 

\# \*\*1.6.   Sistematika Penulisan\*\* 

Sistematika  penulisan  dalam  penelitian  ini  disusun  untuk  memberikan  gambaran mengenai  alur  pembahasan  yang  dilakukan,  yang  terbagi  ke  dalam  beberapa  bab  sebagai berikut: 

\# \*\*BAB I PENDAHULUAN\*\* 

Bab  ini  berisi  latar  belakang  yang  menjelaskan  permasalahan  fragmentasi  data  akibat  sistem yang  terisolasi  pada  platform  eBengkelku.com,  rumusan  masalah,  batasan  masalah,  tujuan penelitian, manfaat penelitian, serta sistematika penulisan. 

\# \*\*BAB II TINJAUAN PUSTAKA\*\* 

Bab  ini  menguraikan  landasan  teori  yang  mendukung  penelitian,  meliputi  konsep  sistem informasi,  integrasi  sistem,  Master  Data  Management  (MDM), \_single  source  of  truth\_ ,  ETL ( \_Extract\_ , \_Transform\_ , \_Load\_ ),  REST  API,  serta  konsep  Adapter  Pattern.  Selain  itu,  bab  ini  juga memuat penelitian terdahulu yang relevan sebagai dasar dalam perancangan solusi. 

4 

\# \*\*BAB III METODE PENELITIAN\*\* 

Bab  ini  menjelaskan  metodologi  yang  digunakan  dalam  penelitian,  yaitu  Design  Science Research  (DSR),  yang  mencakup  tahapan  identifikasi  masalah,  perancangan  solusi, pengembangan  artefak,  serta  evaluasi.  Pada  bab  ini  juga  dijelaskan  pendekatan  perancangan integrasi sistem dan konsolidasi data yang digunakan dalam penelitian. 

\# \*\*BAB IV HASIL DAN PEMBAHASAN\*\* 

Bab  ini  menguraikan  hasil  penelitian  yang  meliputi  analisis  sistem  berjalan  pada  platform eBengkelku.com,  identifikasi  permasalahan  fragmentasi  data,  serta  perancangan  dan implementasi  solusi  integrasi  sistem  menggunakan  ETL  dan  REST  API.  Selain  itu,  bab  ini juga  menyajikan  evaluasi  hasil  implementasi  berdasarkan  konsistensi  dan  kualitas  data  setelah integrasi sistem dilakukan. 

\# \*\*BAB V PENUTUP\*\* 

Bab  ini  berisi  kesimpulan  dari  hasil  penelitian  yang  telah  dilakukan  serta  saran  untuk pengembangan  penelitian  selanjutnya,  khususnya  dalam  pengembangan  integrasi  sistem  dan pengelolaan data pada ekosistem digital. 

5 

**Mahdiyyah Febrinazahra: Evaluasi Tata Kelola SPBE (2026) dan Lisa Febriyanti: Kapabilitas Tata Kelola TI COBIT 2019 (2026). Rujukan pengukuran tingkat kematangan untuk ©**  
\# \*\*BAB I\*\* 

\# \*\*PENDAHULUAN\*\* 

Bab ini menjelaskan dasar penyusunan penelitian yang meliputi latar belakang, rumusan masalah, batasan masalah, tujuan penelitian, manfaat penelitian, serta sistematika penulisan. 

\#\# \*\*1.1 Latar Belakang\*\* 

Perkembangan teknologi digital telah mendorong transformasi tata kelola pemerintahan menuju layanan publik yang lebih efektif, efisien, dan terintegrasi. Dalam konteks pemerintahan, pemanfaatan teknologi informasi tidak lagi terbatas pada digitalisasi administrasi, tetapi telah berkembang menjadi instrumen strategis untuk memperkuat transparansi, akuntabilitas, serta kualitas pengambilan keputusan (Sangaji dan Irianto 2025). Kondisi ini sejalan dengan meningkatnya ekspektasi masyarakat terhadap layanan publik yang efisien dan berbasis data, sehingga pemerintah dituntut untuk mengelola teknologi informasi secara optimal (Prihartono 2023). Di Indonesia, arah transformasi ini dipertegas melalui Peraturan Presiden Nomor 95 Tahun 2018 tentang Sistem Pemerintahan Berbasis Elektronik (SPBE), yang kemudian diperkuat dengan Peraturan Presiden Nomor 132 Tahun 2022 tentang Arsitektur SPBE. Berdasarkan Laporan Evaluasi SPBE Tahun 2024, Indeks SPBE Nasional mencapai 3,12 dengan kategori baik, dengan rerata tingkat kematangan instansi pusat sebesar 3,71 dan pemerintah daerah sebesar 3,08 (Kementerian PANRB 2025). Capaian ini menunjukkan perkembangan positif dalam implementasi SPBE secara nasional. 

Meskipun demikian, capaian tersebut belum sepenuhnya mencerminkan efektivitas tata kelola SPBE pada setiap instansi atau unit kerja. Keberhasilan implementasi SPBE tidak hanya bergantung pada ketersediaan kebijakan dan sistem, tetapi juga pada kemampuan organisasi dalam mengelola proses, risiko, keamanan informasi, keberlanjutan layanan, serta sumber daya pendukung secara konsisten dan terukur (Ilham \_et al.\_ 2025). Oleh karena itu, diperlukan tata kelola yang memadai agar implementasi SPBE dapat berjalan secara terarah dan selaras dengan tujuan organisasi (Kraugusteeliana \_et al.\_ 2024). Tata kelola yang baik juga menjadi faktor penting agar transformasi digital tidak hanya bersifat administratif, tetapi mampu mendukung pencapaian tujuan organisasi secara berkelanjutan (Sulila dan Mozin 2025). 

Kondisi tersebut relevan pada Kementerian Pekerjaan Umum, khususnya pada Sekretariat Badan Pengembangan Infrastruktur Wilayah (BPIW) yang berperan dalam pengelolaan tata kelola SPBE pada level unit kerja. Berdasarkan hasil observasi dan wawancara, implementasi SPBE di lingkungan BPIW masih menghadapi sejumlah permasalahan pada aspek tata kelola. Meskipun secara kelembagaan telah terdapat berbagai regulasi internal, kondisi tersebut belum 

1   
 

sepenuhnya mencerminkan efektivitas tata kelola pada tingkat operasional. Beberapa permasalahan yang teridentifikasi antara lain potensi tumpang tindih aplikasi, keterbatasan kesiapan SDM, serta ketergantungan pada pengembangan berbasis proyek tanpa perencanaan pemeliharaan jangka panjang. 

Selain itu, dari aspek keamanan informasi, meskipun telah diterapkan mekanisme pengamanan seperti pembentukan \_Computer Security Incident Response Team\_ (CSIRT) dan penggunaan \_Endpoint Detection and Response\_ (EDR), risiko insiden keamanan masih tetap ada dan memerlukan pengelolaan yang lebih sistematis. Dokumen manajemen risiko internal menunjukkan adanya risiko terkait tidak tersedianya mekanisme \_backup\_ pada sistem akibat serangan siber, yang berpotensi mengganggu keberlangsungan layanan SPBE. Kondisi ini menunjukkan adanya kesenjangan antara kebijakan yang telah ditetapkan dengan penerapan di lapangan, yang apabila tidak segera ditangani dapat berdampak pada terganggunya layanan, menurunnya kualitas pengambilan keputusan, serta meningkatnya risiko operasional organisasi. 

Untuk mengatasi permasalahan tersebut, diperlukan pendekatan evaluasi tata kelola yang mampu mengidentifikasi area perbaikan secara sistematis dan sesuai dengan kondisi organisasi (Hidayah \_et al.\_ 2024). Salah satu kerangka kerja yang dapat digunakan adalah \_Control Objectives for Information and Related Technologies\_ (COBIT) 2019 yang dikembangkan oleh \_Information Systems Audit and Control Association\_ (ISACA). COBIT 2019 menyediakan pendekatan terstruktur dalam tata kelola dan manajemen informasi dan teknologi yang dapat disesuaikan dengan kebutuhan organisasi (ISACA 2019a). Penyesuaian tersebut dilakukan melalui mekanisme \_goals cascade\_ untuk menerjemahkan tujuan organisasi ke dalam tujuan layanan SPBE, serta \_design factors\_ yang digunakan dalam menentukan prioritas tata kelola sesuai karakteristik organisasi. Selain itu, COBIT 2019 juga menyediakan model pengukuran kapabilitas untuk menilai kesenjangan antara kondisi saat ini ( \_as-is\_ ) dan kondisi yang diharapkan ( \_to-be\_ ). Dalam penelitian ini, evaluasi difokuskan pada analisis tingkat kapabilitas tata kelola sebagai pendukung implementasi SPBE menggunakan COBIT 2019, bukan sebagai pengganti penilaian SPBE nasional. 

Sejumlah penelitian sebelumnya menunjukkan bahwa COBIT 2019 dapat digunakan untuk mengevaluasi tata kelola pada sektor publik serta menghasilkan identifikasi domain prioritas, tingkat kapabilitas, dan rekomendasi perbaikan. Namun, sebagian penelitian belum mengintegrasikan secara komprehensif mekanisme \_goals cascade\_ , \_design factors\_ , dan analisis kesenjangan dalam satu kerangka evaluasi yang utuh. Selain itu, penelitian yang secara khusus mengkaji tata kelola SPBE pada level unit kerja pemerintah dengan pendekatan yang disesuaikan terhadap karakteristik organisasi masih terbatas. 

2 

Berdasarkan hal tersebut, penelitian ini bertujuan untuk menilai tingkat kapabilitas tata kelola SPBE pada Sekretariat BPIW dengan menggunakan kerangka kerja COBIT 2019, serta menganalisis kesenjangan antara kondisi saat ini ( \_as-is\_ ) dan kondisi yang diharapkan ( \_to-be\_ ). Hasil penelitian diharapkan dapat memberikan rekomendasi peningkatan yang relevan dan sesuai dengan kebutuhan organisasi. Dengan demikian, penelitian ini mengangkat judul “Evaluasi Tata Kelola Sistem Pemerintahan Berbasis Elektronik (SPBE) Menggunakan Kerangka Kerja COBIT 2019 (Studi Kasus: Kementerian Pekerjaan Umum)”. 

\#\# \*\*1.2 Rumusan Masalah\*\* 

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah dalam penelitian ini adalah sebagai berikut: 

1\. Bagaimana menentukan \_governance and management objectives\_ yang menjadi prioritas evaluasi sesuai kebutuhan tata kelola SPBE pada Sekretariat BPIW? 

2\. Bagaimana menganalisis tingkat kapabilitas tata kelola SPBE berdasarkan \_governance and management objectives\_ prioritas untuk menggambarkan kondisi saat ini ( \_as-is\_ ) dan kondisi yang diharapkan ( \_tobe\_ ) sesuai dengan kebutuhan organisasi? 

3\. Bagaimana merumuskan rekomendasi peningkatan tata kelola SPBE yang terarah berdasarkan hasil analisis kesenjangan (gap) kapabilitas pada masing-masing \_governance and management objectives\_ prioritas? 

\#\# \*\*1.3 Batasan Masalah\*\* 

Agar penelitian lebih terarah dan fokus, maka batasan masalah penelitian ini ditetapkan sebagai berikut: 

1\. Objek penelitian dibatasi pada Sekretariat BPIW di lingkungan Kementerian Pekerjaan Umum, sehingga hasil penelitian hanya merepresentasikan kondisi tata kelola SPBE pada unit tersebut. 

2\. Evaluasi dilakukan dengan menggunakan kerangka kerja COBIT 2019, dengan ruang lingkup penilaian difokuskan pada \_governance and management objectives\_ yang diprioritaskan berdasarkan hasil analisis \_design factors\_ dengan nilai kepentingan ≥50. 

3\. Penelitian ini tidak membahas aspek teknis secara rinci, seperti pengembangan perangkat lunak, konfigurasi infrastruktur jaringan, maupun penerapan kontrol keamanan secara teknis, melainkan berfokus pada evaluasi tata kelola dan manajemen informasi dan teknologi. 

3 

\#\# \*\*1.4 Tujuan dan Manfaat Penelitian\*\* 

Tujuan dari penelitian ini adalah sebagai berikut: 

1\. Menentukan \_governance and management objectives\_ yang menjadi prioritas evaluasi sesuai kebutuhan tata kelola SPBE pada Sekretariat BPIW. 

2\. Menganalisis tingkat kapabilitas tata kelola SPBE berdasarkan \_governance and management objectives\_ prioritas untuk menggambarkan kondisi saat ini ( \_as-is\_ ) dan kondisi yang diharapkan ( \_to-be\_ ) sesuai dengan kebutuhan organisasi. 

3\. Merumuskan rekomendasi peningkatan tata kelola SPBE yang terarah berdasarkan hasil analisis kesenjangan (gap) kapabilitas pada masingmasing \_governance and management objectives\_ prioritas. 

Adapun penelitian ini memberikan manfaat yang dapat ditinjau dari sisi teoritis maupun praktis sebagai berikut: 

1\. Manfaat Teoretis 

   \- a. Memberikan kontribusi dalam pengembangan kajian tata kelola SPBE di sektor publik melalui penerapan kerangka kerja COBIT 2019 yang disesuaikan menggunakan pendekatan \_design factors\_ , sehingga memberikan pendekatan evaluasi yang lebih kontekstual dan terukur. 

   \- b. Menyediakan referensi empiris mengenai penerapan COBIT 2019 dalam evaluasi tata kelola SPBE pada tingkat unit organisasi pemerintah yang masih terbatas dalam penelitian sebelumnya. 

2\. Manfaat Praktis 

   \- a. Memberikan gambaran yang terstruktur mengenai kondisi saat ini ( \_asis\_ ) tata kelola SPBE pada Sekretariat BPIW berdasarkan hasil pengukuran tingkat kapabilitas menggunakan COBIT 2019\. 

   \- b. Mengidentifikasi kesenjangan antara kondisi saat ini ( \_as-is\_ ) dan kondisi yang diharapkan ( \_to-be\_ ) pada setiap \_governance and management objectives\_ yang diprioritaskan, sehingga dapat menjadi dasar dalam penentuan prioritas peningkatan tata kelola. 

   \- c. Menghasilkan rekomendasi peningkatan tata kelola SPBE yang lebih terarah dan kontekstual, khususnya pada aspek keamanan informasi, keberlangsungan layanan, dan manajemen risiko sesuai dengan kebutuhan organisasi. 

   \- d. Mendukung Sekretariat BPIW dalam meningkatkan efektivitas implementasi SPBE melalui penguatan tata kelola manajemen 

4 

informasi dan teknologi informasi yang selaras dengan kebijakan nasional dan kebutuhan organisasi. 

\#\# \*\*1.5 Sistematika Penulisan\*\* 

Sistematika penulisan dalam penelitian ini disusun untuk memberikan gambaran menyeluruh mengenai isi penelitian serta membantu pembaca dalam memahami alur pembahasan. Penelitian ini berjudul \_“Evaluasi Tata Kelola Sistem Pemerintahan Berbasis Elektronik (SPBE) Menggunakan Kerangka Kerja COBIT 2019 (Studi Kasus: Kementerian Pekerjaan Umum)”\_ . Adapun susunan sistematika penulisan dijelaskan sebagai berikut: 

\#\# BAB I PENDAHULUAN 

Bab ini menjelaskan dasar penyusunan penelitian yang meliputi latar belakang, rumusan masalah, batasan masalah, tujuan penelitian, manfaat penelitian, serta sistematika penulisan. 

BAB II TINJAUAN PUSTAKA 

Bab ini menguraikan kajian teori, konsep, serta penelitian terdahulu sebagai landasan penelitian. Pembahasan meliputi Sistem Pemerintahan Berbasis Elektronik (SPBE), termasuk konsep, kebijakan dan regulasi di Indonesia, arsitektur SPBE nasional, serta implementasinya di Kementerian Pekerjaan Umum. Selain itu, dibahas pula tata kelola SPBE serta kerangka kerja COBIT 2019 yang meliputi prinsip dasar, \_Goals Cascade\_ , \_Governance System Design Workflow\_ , \_Design Factors\_ , \_Governance and Management Objectives\_ , \_Capability Level\_ , RACI \_Chart\_ , serta \_Gap Analysis\_ . Bab ini juga memuat metode pengumpulan data, instrumen penelitian, serta pengujian instrumen, yang kemudian ditutup dengan uraian penelitian terdahulu sebagai referensi pendukung. 

\#\# BAB III METODE PENELITIAN 

Bab ini menjelaskan metode yang digunakan dalam penelitian, termasuk kerangka dan tahapan penelitian. Tahapan tersebut meliputi identifikasi masalah, identifikasi \_Goals Cascade\_ , analisis \_Design Factors\_ , pemetaan RACI \_Chart\_ , penyebaran kuesioner, pengujian validitas dan reliabilitas, analisis tingkat kapabilitas, analisis kesenjangan (gap), serta penyusunan rekomendasi peningkatan. Selain itu, dijelaskan pula lokasi dan waktu penelitian, alat dan bahan yang digunakan, serta jadwal pelaksanaan penelitian. 

\#\# BAB IV HASIL DAN PEMBAHASAN 

Bab ini menyajikan hasil penelitian dan pembahasan berdasarkan metode yang telah digunakan, diawali dengan gambaran umum instansi penelitian. Selanjutnya dibahas hasil identifikasi \_Goals Cascade\_ dan analisis \_Design Factors\_ untuk menentukan \_governance and management objectives\_ COBIT 2019 yang diprioritaskan, pemetaan RACI \_Chart\_ untuk penentuan responden, serta hasil uji 

\*\*Mahdiyyah Febrinazahra, 2026\*\* \*\*\_EVALUASI TATA KELOLA SISTEM PEMERINTAHAN BERBASIS ELEKTRONIK (SPBE) MENGGUNAKAN KERANGKA KERJA COBIT 2019 (STUDI KASUS: KEMENTERIAN PEKERJAAN UMUM)\_\*\* 

5 

instrumen. Bab ini juga memuat analisis tingkat kapabilitas untuk menggambarkan kondisi saat ini ( \_as-is\_ ), analisis kesenjangan (gap) terhadap kondisi yang diharapkan ( \_to-be\_ ), serta rekomendasi peningkatan tata kelola SPBE. 

BAB V PENUTUP 

Bab ini berisi kesimpulan dan saran yang dirumuskan berdasarkan hasil penelitian. Kesimpulan memuat jawaban atas rumusan masalah serta temuan utama terkait tingkat kapabilitas dan kesenjangan tata kelola SPBE, sedangkan saran berisi rekomendasi bagi pihak terkait serta pengembangan penelitian selanjutnya. 

DAFTAR PUSTAKA 

Bagian ini memuat seluruh sumber referensi yang digunakan dalam penelitian yang disusun secara sistematis. 

DAFTAR RIWAYAT HIDUP 

Bagian ini memuat informasi singkat mengenai identitas dan riwayat hidup penulis. 

LAMPIRAN 

Bagian ini memuat dokumen pendukung penelitian sebagai pelengkap data dan bukti administratif yang mendukung keabsahan hasil penelitian. 

6 

**Rizky Arya Putra Razaan: Modul SKP dan Role-Based Access Control (2026). Untuk argumen hak akses (masalah no. 4).**

\# \*\*BAB I.  PENDAHULUAN\*\* 

\# \*\*1.1. Latar Belakang\*\* 

Di tengah arus globalisasi yang semakin deras, penguasaan bahasa asing telah menjadi sebuah kebutuhan. Minat masyarakat untuk mempelajari bahasa banyak didorong oleh fenomena budaya global seperti musik, drama, dan film, dan juga juga oleh motivasi yang lebih formal untuk meningkatkan prospek karier dan pendidikan. Menurut Yue dkk. (2022), faktor ketertarikan pada budaya memang berperan dalam menumbuhkan minat belajar bahasa, namun dorongan lain seperti kebutuhan pendidikan dan peluang karier menjadi salah satu pendorong utama yang memperkuat motivasi tersebut. Dorongan untuk bersaing di panggung dunia memacu banyak individu untuk mencari kesempatan baru seperti melanjutkan studi di luar negeri. Hal ini tercermin dari data yang menunjukkan bahwa hingga bulan desember tahun 2024, terdapat 18.126 mahasiswa penerima beasiswa LPDP, dengan 40,23% di antaranya atau sekitar 7.292 orang menempuh studi di luar negeri. 

Khrufai merupakan salah satu kursus bahasa asing yang berdiri sejak Desember 2024 yang berlokasi di Ciputat Timur, Tangerang Selatan, sebagai respons terhadap meningkatnya kebutuhan masyarakat akan penguasaan bahasa asing. Kursus ini menyediakan program pembelajaran Bahasa Inggris, Bahasa Korea, dan Bahasa Tailan yang dapat diikuti oleh berbagai kalangan, baik melalui kelas umum maupun kelas privat. 

Agar pembelajaran lebih terarah, setiap program bahasa di Khrufai telah disusun berdasarkan tingkat kemahiran peserta. Untuk Bahasa Inggris, kurikulum mengacu pada standar CEFR yang terbagi menjadi level pemula (A1–A2), dan menengah (B1–B2). Program Bahasa Korea mengadaptasi acuan topik, dimulai dari tingkat dasar (Level 1–2) hingga menengah lanjutan (Level 3–4) yang berfokus pada penguasaan kosakata harian dan struktur kalimat dasar. Adapun Bahasa Tailan dibagi menjadi dua jenjang, yaitu dasar , dan menengah, dengan penekanan pada kemampuan komunikasi sederhana. Pembagian level ini bertujuan agar materi yang diterima peserta benar-benar sesuai dengan kemampuan awal, sekaligus memudahkan pengajar dalam menyusun target evaluasi yang terukur. 

Berdasarkan hasil wawancara dengan salah satu pengajar Khrufai yaitu Bapak Faiz Taufikri, Khrufai menggunakan beragam \_platform\_ yang terpisah. Pendaftaran siswa dilakukan melalui Google Form, kemudian data dipindahkan ke Microsoft Excel untuk kebutuhan administrasi seperti rapor, absensi, dan sertifikat. Materi disampaikan lewat WhatsApp atau Google Drive. Tugas maupun kuis juga masih menggunakan metode sederhana, seperti menulis tangan lalu difoto dan dikirimkan melalui WhatsApp, atau dilakukan secara langsung saat sesi kelas berlangsung. 

Pengelolaan nilai, absensi, dan progres belajar siswa juga masih dilakukan secara manual menggunakan Excel. Data kemudian diolah untuk 

1 

menghasilkan laporan nilai maupun sertifikat. Cara ini sangat menyita waktu dan berisiko tinggi terhadap kesalahan input. Kondisi ini sejalan dengan temuan penelitian yang menunjukkan bahwa sistem manual kurang efisien serta dapat menghambat kualitas evaluasi pembelajaran (Mursalin dkk, 2022). 

Selain itu, proses penyampaian informasi akademik masih kurang efisien. Jika siswa ingin melihat perkembangan nilainya, pengajar harus menyalin data dari Excel ke Google Sheets sebelum membagikannya. Hal ini memperlambat komunikasi antara pengajar dan siswa. Evaluasi progres belajar juga sulit dilakukan secara objektif, karena penilaian lebih banyak bergantung pada respons siswa selama sesi online, bukan pada data terukur. 

Keterbatasan ini berpotensi menjadi hambatan besar bagi Khrufai, khususnya ketika jumlah siswa semakin bertambah. Pengelolaan nilai, absensi, dan materi dengan sistem manual akan semakin sulit dikendalikan, sehingga dapat berdampak pada menurunnya kepuasan siswa. 

Untuk mengatasi berbagai kendala tersebut, implementasi \_Learning Management System\_ (LMS) menjadi solusi yang strategis. LMS merupakan \_platform\_ perangkat lunak terintegrasi yang dirancang untuk mengelola, mendokumentasikan, melacak, dan menyampaikan konten pembelajaran secara daring. Menurut Depari dkk. (2021), penggunaan LMS terbukti dapat meningkatkan kemandirian dan motivasi belajar mahasiswa karena memberikan akses materi tanpa batas, fleksibilitas waktu belajar, serta forum interaksi yang mendorong pembelajaran kolaboratif. 

Beberapa LMS populer seperti Moodle, dan Google Classroom sebenarnya sudah banyak digunakan oleh banyak lembaga pendidikan. Namun, sistem-sistem tersebut memiliki keterbatasan ketika diterapkan di lembaga kursus seperti Khrufai. Google Classroom, misalnya, tidak menyediakan fitur pelaporan nilai otomatis sesuai kebutuhan lembaga. Oleh karena itu, penelitian ini berfokus pada pengembangan LMS yang menyesuaikan kebutuhan spesifik Khrufai. 

Selain itu, belum adanya sistem terintegrasi berbasis \_web\_ yang mampu mengelola seluruh proses pembelajaran menjadi celah penelitian yang perlu diselesaikan. Celah ini menunjukkan adanya kebutuhan terhadap sistem yang tidak hanya berfungsi sebagai media distribusi materi, tetapi juga mampu mengintegrasikan proses administrasi akademik dan evaluasi pembelajaran dalam satu \_platform\_ . 

Pemilihan \_platform\_ LMS berbasis \_web\_ didasari oleh tingkat aksesibilitasnya yang tinggi. Baik peserta maupun pengajar dapat menggunakan sistem ini melalui berbagai perangkat yang terhubung ke internet, seperti laptop, tablet, maupun ponsel pintar, tanpa perlu memasang aplikasi tambahan. Dengan kepraktisan tersebut, kegiatan belajar mengajar dapat dilakukan secara fleksibel, kapan pun dan di mana pun. 

2 

Penerapan LMS di Khrufai diharapkan dapat memberikan dampak positif yang signifikan bagi semua pihak. Bagi siswa, mereka akan mendapatkan pengalaman belajar yang lebih terstruktur, interaktif, dan transparan. Bagi pengajar, beban kerja administratif akan berkurang , sehingga mereka dapat lebih fokus pada kualitas pengajaran dan pendampingan siswa. Sementara itu, bagi pihak manajemen, LMS akan menyediakan data yang akurat untuk evaluasi, meningkatkan citra profesional lembaga, serta membangun fondasi yang kuat untuk pertumbuhan jumlah siswa di masa yang akan datang. 

\# \*\*1.2. Rumusan Masalah\*\* 

Dengan mempertimbangkan latar belakang yang telah dipaparkan, maka rumusan masalah dalam penelitian ini dirumuskan sebagai berikut: 

1\. Bagaimana merancang arsitektur dan fungsionalitas \_Learning Management System\_ (LMS) berbasis \_web\_ yang dapat mengotomatisasi dan mengintegrasikan proses pengelolaan nilai, absensi, dan distribusi materi di Kursus Khrufai? 

2\. Bagaimana menerapkan metode \_Rapid Application Development\_ (RAD) untuk membangun LMS yang sesuai dengan kebutuhan fungsional dan non-fungsional pengguna di Kursus Khrufai? 

\# \*\*1.3. Batasan Masalah\*\* 

Batasan penelitian ini mencakup beberapa poin, antara lain: 

1\. Pengembangan LMS ini dilakukan dengan menerapkan metode \_Rapid Application Development\_ (RAD), yaitu pendekatan yang menekankan pada proses pengulangan (iteratif) serta kerja sama antara tim pengembang dan pengguna untuk mempercepat siklus pengembangan sistem. 

2\. Kegiatan penelitian dan pengembangan diarahkan pada pembuatan serta penerapan LMS berbasis \_web\_ yang dapat diakses secara langsung oleh siswa, pengajar, maupun administrator di lingkungan Kursus Khrufai. 

\# \*\*1.4. Tujuan Penelitian\*\* 

Penelitian ini bertujuan untuk: 

1\. Menghasilkan \_Learning Management System\_ (LMS) berbasis \_web\_ yang mengintegrasikan fungsionalitas pengelolaan nilai, absensi, dan distribusi materi. 

2\. Mengembangkan dan mengimplementasikan sistem LMS dengan metode \_Rapid Application Development\_ (RAD) sesuai dengan rancangan yang telah dibuat. 

3 

\# \*\*1.5. Manfaat Penelitian\*\* 

Hasil dari penelitian ini diharapkan dapat memberikan manfaat yang nyata bagi berbagai pihak yang terlibat di Kursus Khrufai, serta bagi peneliti lain di bidang serupa. 

1\. Bagi Siswa 

   1\. Siswa mendapatkan kemudahan untuk mengakses semua materi pelajaran, tugas, dan informasi nilai dalam satu \_platform\_ . 

   2\. Proses belajar menjadi lebih transparan, karena siswa dapat melihat sendiri catatan kehadiran (absensi) dan perkembangan nilai mereka kapan saja. 

   3\. Mempermudah siswa dalam mengumpulkan tugas dan mengikuti kuis tanpa perlu berganti-ganti \_platform\_ . 

2\. Bagi Pengajar 

   1\. Mengurangi beban kerja administrasi yang sebelumnya dilakukan manual, seperti merekap absensi dan nilai di Excel. 

   2\. Pengajar dapat lebih mudah mengelola dan membagikan materi pelajaran kepada siswa secara terpusat. 

   3\. Waktu yang sebelumnya habis untuk administrasi kini bisa dialihkan untuk lebih fokus pada  proses pengajaran dan membimbing siswa. 

\# \*\*1.6. Sistematika Penulisan\*\* 

Sistematika penulisan ini ditulis untuk memberikan kemudahan informasi bagi pembaca dan memberikan sedikit gambaran dalam “Rancang Bangun \_Learning Management System\_ (LMS) Pada Kursus Bahasa Asing Khrufai Berbasis Web”, berikut ini adalah sistematika penulisannya : 

\# \*\*BAB I PENDAHULUAN\*\* 

Bab ini menjelaskan secara singkat dan jelas mengenai latar belakang masalah, rumusan masalah, batasan masalah, tujuan penelitian dan manfaat penelitian, dan sistematika penulisan. 

\# \*\*BAB II TINJAUAN PUSTAKA\*\* 

Bab ini menguraikan teori-teori yang mendasari pembahasan secara detail, dapat berupa definisi-definisi atau model matematis yang langsung berkaitan dengan ilmu atau masalah yang diteliti dan penelitian terdahulu. 

4 

\# \*\*BAB III METODE PENELITIAN\*\* 

Bab ini menguraikan tentang tahapan penelitian, alat dan bahan serta jadwal penelitian. 

\# \*\*BAB IV HASIL DAN PEMBAHASAN\*\* 

Bab ini menguraikan tentang profil lembaga, analisis sistem berjalan, perancanangan sistem usulan dan hasil. 

\# \*\*BAB V PENUTUP\*\* 

Bab ini menguraikan tentang kesimpulan dan saran penelitian berikutnya. 

5 

