**Proyek Payung: LabFIK Compliance — Pengembangan Sistem Pengelolaan dan Kepatuhan Laboratorium Berbasis Odoo pada Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta**

Proyek LabFIK Compliance dikerjakan oleh tiga mahasiswa dengan judul penelitian yang berbeda namun saling melengkapi:

| No | Judul | Kegiatan Utama | Keluaran bagi Proyek |
|---|---|---|---|
| A | Pemodelan Arsitektur Enterprise LabFIK Compliance Menggunakan TOGAF ADM dan ArchiMate | *Enterprise modeling* | Cetak biru arsitektur bisnis, data, aplikasi, dan teknologi |
| B | Kustomisasi Modul Odoo untuk Pengelolaan Layanan dan Pemantauan Kepatuhan Laboratorium | *Odoo module customization* | Modul Odoo yang berjalan |
| C | Perancangan Strategi Transformasi Digital Pengelolaan Laboratorium Berbasis Model Kematangan Digital | *Digital transformation* | Penilaian kematangan digital, peta jalan, dan evaluasi dampak |

Arsitektur pada Judul A menjadi acuan kebutuhan dan rancangan bagi Judul B. Judul C mengukur kondisi awal, merancang strategi perubahan, dan mengevaluasi dampak penerapan modul dari Judul B.

---

# JUDUL A

**Pemodelan Arsitektur Enterprise LabFIK Compliance Menggunakan TOGAF ADM dan ArchiMate pada Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta**

**1.1 Latar Belakang**

Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 53 Tahun 2023 mewajibkan perguruan tinggi menjalankan Sistem Penjaminan Mutu Internal (SPMI) melalui siklus Penetapan, Pelaksanaan, Evaluasi, Pengendalian, dan Peningkatan (PPEPP) pada seluruh kegiatan akademik maupun nonakademik (Kemendikbudristek 2023). Laboratorium termasuk unit yang dievaluasi dalam siklus tersebut. Di UPN "Veteran" Jakarta, evaluasi ini dilakukan melalui Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026, yang memuat 64 indikator dalam lima aspek, yaitu Pengelolaan Laboratorium, Pengembangan Laboratorium, Persiapan Praktikum, Proses Praktikum, dan Evaluasi Praktikum, dengan total 341 butir bukti dukung. Setiap indikator dinilai pada skala 1 sampai 4, dan skor terendah diberikan apabila bukti tidak dapat diverifikasi (UPNVJ 2026).

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta menyelenggarakan layanannya melalui Portal Layanan LabFIK. Portal ini memuat tujuh kelompok layanan, yaitu informasi profil, pelaporan kendala fasilitas, permintaan penggunaan sarana, permintaan penyediaan perangkat lunak, kegiatan praktikum, survei kepuasan layanan, dan kanal pertanyaan (LabFIK UPNVJ 2026). Seluruh layanan tersebut dijalankan melalui sembilan formulir Google Form dan satu dokumen Google Docs, sedangkan rekapitulasinya disajikan dalam sepuluh rangkuman terpisah, antara lain rangkuman peminjaman laboratorium, alokasi slot praktikum, pelaksanaan asistensi, dan survei praktikum. Pengolahan data kegiatan laboratorium masih dilakukan menggunakan Google Sheets dan belum didukung aplikasi pengelolaan yang terintegrasi. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: kendala yang dialami, misalnya data tersebar di banyak lembar kerja, rekap manual, dan kesulitan menyusun bukti monev.]**

Kondisi tersebut menunjukkan bahwa proses bisnis, data, dan layanan laboratorium belum terpetakan dalam satu kerangka yang utuh. Data yang dihasilkan layanan sebenarnya berkaitan langsung dengan indikator monev. Formulir peminjaman laboratorium berkaitan dengan indikator ketersediaan jadwal penggunaan laboratorium, lembar penggunaan sarana dengan indikator pencatatan pengoperasian alat oleh pengguna berwenang, pendaftaran dan seleksi asisten dengan indikator penugasan asisten sesuai kompetensi minimum, pelaporan kendala dengan indikator pengendalian alat rusak dan penanganan keluhan, serta survei praktikum dan survei layanan dengan indikator pengukuran kepuasan pengguna (UPNVJ 2026). Namun, keterkaitan antara layanan, data, penanggung jawab, dan indikator tersebut belum didokumentasikan. Di sisi lain, 60 dari 64 indikator memiliki lebih dari satu penanggung jawab, sehingga satu proses dapat melibatkan Kepala Laboratorium (KaLab), Pranata Laboratorium Pendidikan (PLP), dosen, asisten, dan Gugus Kendali Mutu (GKM) sekaligus. Tanpa pemetaan yang jelas, pengembangan aplikasi berisiko mengulang kondisi saat ini, yaitu sistem yang terpisah-pisah dan tidak selaras dengan kebutuhan pembuktian mutu.

Arsitektur enterprise menyediakan pendekatan untuk menyelaraskan tujuan organisasi, proses bisnis, data, aplikasi, dan teknologi sebelum sistem dibangun. TOGAF Standard menyediakan metode pengembangan arsitektur (*Architecture Development Method*/ADM) yang bertahap (The Open Group 2022), sedangkan ArchiMate 3.2 menyediakan bahasa pemodelan untuk menggambarkan keterkaitan antarlapisan arsitektur, mulai dari motivasi dan strategi hingga lapisan bisnis, aplikasi, dan teknologi (The Open Group 2023). Nindyaistia et al. (2026) memodelkan arsitektur enterprise rumah sakit menggunakan lapisan TOGAF dan ArchiMate, dan menunjukkan bahwa arsitektur tersebut membantu mengidentifikasi kelemahan sistem yang ada, menyelaraskan strategi dengan proses bisnis dan sistem informasi, serta mendukung integrasi data untuk kebutuhan akreditasi. Pada konteks penjaminan mutu perguruan tinggi, Ismail et al. (2026) dan Nadia dan Subrata (2026) membangun sistem informasi SPMI untuk pengelolaan dokumen dan audit mutu internal, tetapi pengembangannya langsung berfokus pada aplikasi tanpa pemodelan arsitektur yang menghubungkan proses operasional dengan indikator mutu. Hingga saat ini, belum ditemukan penelitian yang memodelkan arsitektur enterprise pengelolaan laboratorium perguruan tinggi yang menelusuri keterkaitan antara layanan, data operasional, dan indikator monev laboratorium.

Berdasarkan permasalahan tersebut, penelitian ini memodelkan arsitektur enterprise LabFIK Compliance menggunakan TOGAF ADM dan ArchiMate 3.2. Penelitian memetakan arsitektur saat ini (*as-is*) dari layanan LabFIK yang berjalan menggunakan Google Form dan Google Sheets, merancang arsitektur target (*to-be*) yang menghubungkan setiap layanan dengan data dan indikator monev yang dibuktikannya, serta menyusun analisis kesenjangan dan peta jalan implementasi. Arsitektur target tersebut menjadi acuan pengembangan modul Odoo dalam proyek LabFIK Compliance dan divalidasi bersama pengelola laboratorium.

**1.2 Rumusan Masalah**

1. Bagaimana memodelkan arsitektur saat ini (*as-is*) pengelolaan layanan dan data kegiatan LabFIK UPN "Veteran" Jakarta beserta keterkaitannya dengan indikator Instrumen Monev Laboratorium UPNVJ 2026 menggunakan ArchiMate?
2. Bagaimana merancang arsitektur target (*to-be*) bisnis, data, aplikasi, dan teknologi LabFIK Compliance menggunakan TOGAF ADM sebagai acuan pengembangan sistem berbasis Odoo?
3. Bagaimana kesenjangan antara arsitektur saat ini dan arsitektur target, serta peta jalan implementasi yang diperlukan untuk menutup kesenjangan tersebut?

**Daftar Pustaka**

Ismail, A., Arief, S.N. dan Pramudya, H.A. (2026) 'Pengembangan Aplikasi E-SPMI (Sistem Penjaminan Mutu Internal) Audit Berbasis Web Politeknik Negeri Malang', *Jurnal Informatika Polinema*, 12(3), hlm. 519–528.

Kemendikbudristek (2023) *Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 53 Tahun 2023 tentang Penjaminan Mutu Pendidikan Tinggi*. Jakarta: Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.

LabFIK UPNVJ (2026) *Portal Layanan LabFIK UPNVJ*. Tersedia di: https://lab.fik.upnvj.ac.id (Diakses: 12 Oktober 2026).

Nadia, K.P. dan Subrata, J. (2026) 'Sistem Informasi Penjaminan Mutu Internal pada Prodi D3 Manajemen Informatika Universitas Teknologi Digital PSDKU Tegal', *JATI (Jurnal Mahasiswa Teknik Informatika)*, 10(4), hlm. 6081–6088.

Nindyaistia, Widodo, A.P., Nugraheni, D.M.K. dan Widodo, K. (2026) 'Transformasi Digital dengan Pengembangan Enterprise Architecture pada Layanan Kesehatan', *Joutica: Journal of Informatic Unisla*, 11(1), hlm. 99–112. doi: 10.30736/jti.v11i1.1643.

The Open Group (2022) *The TOGAF Standard, 10th Edition*. Reading: The Open Group.

The Open Group (2023) *ArchiMate 3.2 Specification*. 's-Hertogenbosch: Van Haren Publishing.

UPN "Veteran" Jakarta (2026) *Instrumen Monitoring dan Evaluasi Laboratorium UPNVJ 2026 Versi 1.1*. Dokumen internal. Jakarta: UPN "Veteran" Jakarta.

---

# JUDUL B

**Kustomisasi Modul Odoo untuk Pengelolaan Layanan dan Pemantauan Kepatuhan Laboratorium pada Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta**

**1.1 Latar Belakang**

Laboratorium merupakan sarana utama pelaksanaan praktikum, penelitian, dan pengabdian kepada masyarakat, sehingga pengelolaannya termasuk dalam cakupan Sistem Penjaminan Mutu Internal (SPMI) yang diwajibkan bagi perguruan tinggi (Kemendikbudristek 2023). UPN "Veteran" Jakarta menjabarkan penjaminan mutu laboratorium ke dalam Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026 yang memuat 64 indikator. Sebanyak 36 indikator dinilai berdasarkan persentase unit yang memenuhi: skor 4 untuk 100% unit, skor 3 untuk 90% hingga kurang dari 100%, skor 2 untuk 70% hingga kurang dari 90%, dan skor 1 untuk kurang dari 70%. Sebanyak 28 indikator lainnya dinilai sebagai paket dokumen dengan kriteria yang diperiksa secara berurutan (UPNVJ 2026). Penilaian berbasis persentase menuntut setiap unit kegiatan, seperti sesi praktikum, penggunaan alat, dan penugasan asisten, tercatat secara individual agar dapat dihitung dan diverifikasi.

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta saat ini melayani pengguna melalui Portal Layanan LabFIK, yang menyediakan layanan pelaporan kendala fasilitas, peminjaman laboratorium, peminjaman sarana 3D printer, permintaan penyediaan perangkat lunak, pendaftaran dan seleksi asisten, pelaksanaan asistensi, survei praktikum, dan survei kepuasan layanan (LabFIK UPNVJ 2026). Seluruh layanan tersebut dijalankan menggunakan Google Form dan Google Docs, sedangkan pengolahan datanya dilakukan di Google Sheets. Belum terdapat aplikasi yang mengelola alur layanan secara utuh, mulai dari pengajuan, persetujuan, pelaksanaan, hingga pelaporan. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: bagaimana permintaan diproses dan disetujui saat ini, berapa lama rekapitulasi dilakukan, dan kendala yang muncul, misalnya bentrok jadwal, data ganda, atau status permintaan yang tidak terlacak.]**

Penggunaan formulir terpisah menimbulkan dua keterbatasan. Pertama, formulir hanya mencatat pengajuan, tidak mengelola alur kerja berikutnya, sehingga status persetujuan, pelaksanaan, dan penyelesaian layanan harus dilacak secara manual di lembar kerja. Kedua, data setiap layanan tersimpan terpisah dan tidak terhubung dengan indikator monev yang dibuktikannya, padahal data tersebut merupakan bukti dukung langsung. Data peminjaman laboratorium membuktikan ketersediaan jadwal penggunaan, lembar penggunaan sarana membuktikan pencatatan pengoperasian alat, data pendaftaran dan seleksi asisten membuktikan penugasan sesuai kompetensi minimum, dan data survei membuktikan pengukuran kepuasan pengguna (UPNVJ 2026). Akibatnya, perhitungan persentase unit yang memenuhi dan penyusunan bukti dukung harus dilakukan ulang secara manual menjelang monev.

Penelitian terdahulu menunjukkan manfaat sistem informasi pada kedua sisi permasalahan ini. Harahap et al. (2024) menyimpulkan bahwa sistem informasi manajemen laboratorium pendidikan mendukung pengelolaan inventaris, penjadwalan, pemeliharaan peralatan, dan pelaporan, sedangkan Peniarsih et al. (2025) menerapkan sistem E-Laboratorium terpadu untuk meningkatkan efisiensi manajemen laboratorium perguruan tinggi. Pada sisi penjaminan mutu, Ismail et al. (2026) mengembangkan aplikasi E-SPMI audit berbasis web dengan hasil UAT sebesar 89,5%. Namun, sistem pengelolaan laboratorium tersebut tidak mengaitkan data operasional dengan indikator mutu, sedangkan sistem penjaminan mutu memperlakukan bukti sebagai dokumen yang diunggah secara manual. Untuk menjembatani keduanya, Odoo dapat digunakan sebagai platform. Odoo merupakan sistem *Enterprise Resource Planning* (ERP) bersifat *open source* yang dapat dikonfigurasi dan dikustomisasi sesuai kebutuhan organisasi (Nurrohmah dan Wiratama 2022). Odoo juga menyediakan mekanisme keamanan bawaan berupa grup pengguna, hak akses per model, dan aturan akses per rekaman (Odoo S.A. 2023). Mekanisme ini relevan dengan instrumen monev, yang mensyaratkan bahwa pengoperasian peralatan hanya dilakukan oleh pengguna berwenang dan bahwa akses sistem serta integritas data laboratorium dikendalikan (UPNVJ 2026).

Berdasarkan permasalahan tersebut, penelitian ini mengembangkan modul kustom Odoo untuk pengelolaan layanan dan pemantauan kepatuhan LabFIK UPN "Veteran" Jakarta. Modul menggantikan alur Google Form dan Google Sheets dengan alur kerja terintegrasi untuk layanan peminjaman laboratorium dan sarana, pencatatan penggunaan sarana, pelaporan kendala, permintaan perangkat lunak, serta pengelolaan asisten dan asistensi praktikum. Setiap rekaman layanan dipetakan ke indikator monev yang relevan, sehingga skor indikator berbasis persentase dapat dihitung secara otomatis dan ditelusuri hingga rekaman asalnya. Hak akses dikonfigurasi sesuai peran KaLab, PLP/laboran, dosen, asisten, dan mahasiswa. Modul dikembangkan menggunakan metode Agile dengan mengacu pada rancangan arsitektur proyek LabFIK Compliance, kemudian diuji melalui *Black Box Testing* dan *User Acceptance Testing* (UAT).

**1.2 Rumusan Masalah**

1. Bagaimana menganalisis kebutuhan fungsional dan hak akses layanan LabFIK UPN "Veteran" Jakarta yang saat ini berjalan menggunakan Google Form dan Google Sheets sebagai dasar kustomisasi modul Odoo?
2. Bagaimana merancang dan membangun modul kustom Odoo yang mengelola alur layanan laboratorium secara terintegrasi serta memetakan data layanan ke indikator Instrumen Monev Laboratorium UPNVJ 2026 untuk menghitung skor kepatuhan secara otomatis?
3. Bagaimana tingkat penerimaan pengguna terhadap modul yang dikembangkan berdasarkan *User Acceptance Testing*?

**Daftar Pustaka**

Harahap, A.H.J., Rukhaiyah, S. dan Harahap, N. (2024) 'Sistem Informasi Manajemen dalam Pengelolaan Laboratorium Pendidikan: Tinjauan Pustaka', *Jurnal Pendidikan Tambusai*, 8(2), hlm. 34899–34903. doi: 10.31004/jptam.v8i2.19069.

Ismail, A., Arief, S.N. dan Pramudya, H.A. (2026) 'Pengembangan Aplikasi E-SPMI (Sistem Penjaminan Mutu Internal) Audit Berbasis Web Politeknik Negeri Malang', *Jurnal Informatika Polinema*, 12(3), hlm. 519–528.

Kemendikbudristek (2023) *Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 53 Tahun 2023 tentang Penjaminan Mutu Pendidikan Tinggi*. Jakarta: Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.

LabFIK UPNVJ (2026) *Portal Layanan LabFIK UPNVJ*. Tersedia di: https://lab.fik.upnvj.ac.id (Diakses: 12 Oktober 2026).

Nurrohmah, W.M. dan Wiratama, J. (2022) 'Enterprise Resource Planning (ERP) SAP Business One Evaluation and Improvement Recommendation using Customized Odoo', *Ultima InfoSys: Jurnal Ilmu Sistem Informasi*, 13(2), hlm. 77–84. doi: 10.31937/si.v13i2.2802.

Odoo S.A. (2023) *Security in Odoo — Odoo 17.0 Documentation*. Tersedia di: https://www.odoo.com/documentation/17.0/developer/reference/backend/security.html (Diakses: 12 Oktober 2026).

Peniarsih, Sumitra, T., Ramadhnay, A., Setiadi, D. dan Iswandir (2025) 'Implementasi Teknologi E-Laboratorium Terpadu dalam Meningkatkan Efisiensi Manajemen Laboratorium Perguruan Tinggi', *JSI (Jurnal Sistem Informasi) Universitas Suryadarma*, 12(2), hlm. 52–57. doi: 10.35968/jsi.v12i2.1453.

UPN "Veteran" Jakarta (2026) *Instrumen Monitoring dan Evaluasi Laboratorium UPNVJ 2026 Versi 1.1*. Dokumen internal. Jakarta: UPN "Veteran" Jakarta.

---

# JUDUL C

**Perancangan Strategi Transformasi Digital Pengelolaan Laboratorium Berbasis Model Kematangan Digital pada Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta**

**1.1 Latar Belakang**

Transformasi digital di perguruan tinggi tidak sebatas penggunaan teknologi, tetapi mencakup perubahan proses, tata kelola data, serta kesiapan manusia dan budaya organisasi. Bravo-Jaico et al. (2025) merumuskan empat komponen kunci transformasi digital perguruan tinggi, yaitu teknologi digital, tata kelola data, manusia dan budaya digital, serta proses digital, yang diterapkan pada proses inti institusi, termasuk manajemen akademik dan administrasi. Pada tingkat laboratorium, Kammerlohr et al. (2023) mengembangkan model kematangan transformasi digital laboratorium pendidikan dan riset yang memungkinkan pengelola menilai posisi laboratorium saat ini, membandingkannya, dan menentukan langkah transformasi berikutnya. Kedua penelitian tersebut menunjukkan bahwa transformasi digital perlu diawali dengan pengukuran kematangan agar strategi yang disusun sesuai dengan kondisi organisasi.

Kebutuhan transformasi digital laboratorium di UPN "Veteran" Jakarta diperkuat oleh tuntutan penjaminan mutu. Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 53 Tahun 2023 mewajibkan perguruan tinggi menjalankan Sistem Penjaminan Mutu Internal melalui siklus PPEPP (Kemendikbudristek 2023), yang di tingkat laboratorium dijabarkan dalam Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026. Instrumen ini memuat 64 indikator dengan 341 butir bukti dukung, dan salah satu indikatornya secara eksplisit menuntut pengendalian data laboratorium, meliputi hak akses, pencadangan, jejak perubahan, serta validasi *spreadsheet* dan perangkat lunak yang kritis (UPNVJ 2026). Dengan demikian, cara laboratorium mengelola data kegiatannya turut menjadi objek penilaian mutu.

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta telah memulai digitalisasi layanannya melalui Portal Layanan LabFIK, yang menyediakan formulir daring untuk pelaporan kendala, peminjaman laboratorium dan sarana, permintaan perangkat lunak, kegiatan asistensi praktikum, serta survei praktikum dan kepuasan layanan (LabFIK UPNVJ 2026). Namun, digitalisasi tersebut masih berada pada tahap pemindahan formulir kertas ke Google Form. Pengolahan data dilakukan di Google Sheets, alur persetujuan dan tindak lanjut belum terotomasi, dan data setiap layanan tersimpan terpisah dalam sepuluh rangkuman yang berbeda. Proses manajemen dan pengolahan data kegiatan laboratorium belum didukung aplikasi yang terintegrasi. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: kesiapan dan kompetensi digital pengelola, kebiasaan kerja yang berlaku, dan hambatan yang dirasakan dalam pengelolaan data saat ini.]** Kondisi ini menunjukkan bahwa LabFIK berada pada tahap awal transformasi digital: teknologi telah digunakan, tetapi proses, tata kelola data, dan cara kerja pengelolanya belum berubah.

Penerapan aplikasi baru tanpa strategi transformasi berisiko tidak diadopsi secara berkelanjutan. Harahap et al. (2024) mencatat bahwa penerapan sistem informasi manajemen laboratorium pendidikan menghadapi tantangan berupa biaya implementasi dan resistensi terhadap perubahan. Nindyaistia et al. (2026) juga menunjukkan bahwa transformasi digital layanan memerlukan penyelarasan antara strategi, proses bisnis, dan sistem informasi, bukan sekadar pengadaan aplikasi. Penelitian transformasi digital yang ada umumnya berada pada tingkat institusi perguruan tinggi (Bravo-Jaico et al. 2025) atau laboratorium teknik dan manufaktur (Kammerlohr et al. 2023). Hingga saat ini, belum ditemukan penelitian yang merancang strategi transformasi digital laboratorium fakultas yang didorong oleh kebutuhan pemenuhan indikator monev laboratorium, sekaligus mengukur dampaknya terhadap pengelolaan data dan penyusunan bukti mutu.

Berdasarkan permasalahan tersebut, penelitian ini merancang strategi transformasi digital pengelolaan laboratorium bagi LabFIK UPN "Veteran" Jakarta. Penelitian mengukur tingkat kematangan digital LabFIK saat ini, merancang strategi dan peta jalan transformasi yang mencakup proses, data, teknologi, serta manusia dan budaya kerja, termasuk rencana pengelolaan perubahan bagi pengelola laboratorium. Selanjutnya, penelitian mengevaluasi dampak penerapan sistem LabFIK Compliance berbasis Odoo dengan membandingkan tingkat kematangan digital dan efisiensi penyusunan bukti monev sebelum dan sesudah penerapan.

**1.2 Rumusan Masalah**

1. Bagaimana tingkat kematangan digital pengelolaan LabFIK UPN "Veteran" Jakarta saat ini berdasarkan model kematangan transformasi digital laboratorium?
2. Bagaimana merancang strategi dan peta jalan transformasi digital pengelolaan LabFIK yang mencakup aspek proses, data, teknologi, serta manusia dan budaya kerja untuk mendukung pemenuhan indikator Instrumen Monev Laboratorium UPNVJ 2026?
3. Bagaimana dampak penerapan sistem LabFIK Compliance berbasis Odoo terhadap tingkat kematangan digital dan efisiensi penyusunan bukti monev laboratorium?

**Daftar Pustaka**

Bravo-Jaico, J., Alarcón, R., Valdivia, C., Germán, N., Aquino, J., Serquén, O., Guevara, L. dan Moreno Heredia, A. (2025) 'Model for Assessing the Maturity Level of Digital Transformation in Higher Education Institutions: A Theoretical-Methodological Approach', *Frontiers in Education*, 10. doi: 10.3389/feduc.2025.1581648.

Harahap, A.H.J., Rukhaiyah, S. dan Harahap, N. (2024) 'Sistem Informasi Manajemen dalam Pengelolaan Laboratorium Pendidikan: Tinjauan Pustaka', *Jurnal Pendidikan Tambusai*, 8(2), hlm. 34899–34903. doi: 10.31004/jptam.v8i2.19069.

Kammerlohr, V., Paradice, D. dan Uckelmann, D. (2023) 'A Maturity Model for the Effective Digital Transformation of Laboratories', *Journal of Manufacturing Technology Management*, 34(4), hlm. 621–643. doi: 10.1108/JMTM-01-2022-0050.

Kemendikbudristek (2023) *Peraturan Menteri Pendidikan, Kebudayaan, Riset, dan Teknologi Nomor 53 Tahun 2023 tentang Penjaminan Mutu Pendidikan Tinggi*. Jakarta: Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.

LabFIK UPNVJ (2026) *Portal Layanan LabFIK UPNVJ*. Tersedia di: https://lab.fik.upnvj.ac.id (Diakses: 12 Oktober 2026).

Nindyaistia, Widodo, A.P., Nugraheni, D.M.K. dan Widodo, K. (2026) 'Transformasi Digital dengan Pengembangan Enterprise Architecture pada Layanan Kesehatan', *Joutica: Journal of Informatic Unisla*, 11(1), hlm. 99–112. doi: 10.30736/jti.v11i1.1643.

UPN "Veteran" Jakarta (2026) *Instrumen Monitoring dan Evaluasi Laboratorium UPNVJ 2026 Versi 1.1*. Dokumen internal. Jakarta: UPN "Veteran" Jakarta.
