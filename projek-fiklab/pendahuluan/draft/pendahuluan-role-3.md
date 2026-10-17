**Usulan judul:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan Sesi dan Perhitungan Otomatis Skor Indikator Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

*Role 3 proyek LabFIK Compliance. Cakupan indikator: Proses 18, ditambah dashboard skor Pengelolaan 4, Persiapan 15, 16, 17, dan Proses 18.*

# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Praktikum berperan penting dalam pembelajaran karena memperkuat pemahaman konsep dan keterampilan mahasiswa, tetapi pelaksanaannya sering kali belum optimal (Annam *et al.* 2026). Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta menyelenggarakan praktikum untuk lebih dari 70 kelas setiap semester (LabFIK UPNVJ 2026a). Mulai tahun 2026, LabFIK dinilai melalui Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026, yang memuat 64 indikator dengan skor 1 sampai 4. Indikator yang buktinya tidak dapat diverifikasi diberi skor terendah (UPN "Veteran" Jakarta 2026). Instrumen ini disusun dengan mengacu antara lain pada SNI ISO/IEC 17025:2017 **[KONFIRMASI: dasar resmi acuan ini]**. Standar tersebut mensyaratkan rekaman kegiatan laboratorium memuat tanggal dan identitas personel yang bertanggung jawab, dicatat pada saat kegiatan berlangsung, dan perubahannya dapat ditelusuri (Badan Standardisasi Nasional 2018). Akibatnya, kegiatan yang sudah dilaksanakan dengan benar tetap bernilai rendah apabila rekamannya tidak dapat ditunjukkan.

Salah satu indikator yang menilai setiap sesi praktikum adalah Proses 18, yaitu sesi praktikum terlaksana sesuai jadwal, modul, dan waktu kegiatan yang ditetapkan. Skornya dihitung dari persentase sesi yang memenuhi terhadap seluruh sesi yang direncanakan pada periode monev, sehingga sesi yang tidak tercatat tetap masuk ke dalam pembagi. Setiap perubahan harus disahkan, dan sesi yang tertunda baru dihitung memenuhi setelah sesi penggantinya selesai dalam periode pelaporan. Bukti yang diminta meliputi jadwal, jurnal sesi, presensi praktikan, asisten, laboran, dan dosen, modul yang dipakai, *log book*, serta rekaman perubahan dan penggantian sesi (UPN "Veteran" Jakarta 2026). Dengan demikian, Proses 18 hanya dapat dipenuhi apabila setiap sesi yang direncanakan dapat dipasangkan dengan rekaman pelaksanaannya.

Saat ini, rencana pertemuan praktikum disusun dalam *spreadsheet* alokasi asisten yang memuat nama asisten per kelas dan per pertemuan, tetapi tidak memuat hari dan jam pelaksanaan (LabFIK UPNVJ 2026a). Pelaksanaan sesi dilaporkan oleh asisten melalui Google Form Pelaksanaan Asistensi Praktikum, lalu direkap secara manual untuk menghitung honor asisten (LabFIK UPNVJ 2026b). Bersamaan dengan pengisian form, asisten juga mengisi lembar kegiatan kertas. Lembar ini hanya menjadi bukti fisik untuk pengajuan honor ke rektorat dan tidak memuat rincian kegiatan sesi, sehingga tidak dapat berfungsi sebagai *log book* praktikum. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: nama, jabatan, tanggal wawancara, dan alur pelaporan sesi.]** Karena seluruh pencatatan ini dirancang untuk keperluan honor, rekaman hanya tersedia untuk sesi yang memiliki asisten. Selain itu, belum ada rekaman presensi laboran maupun pengajuan perubahan dan sesi pengganti.

Analisis awal terhadap rekaman periode 2025/2026 Ganjil dan Genap menunjukkan tiga kesenjangan (LabFIK UPNVJ 2026a; 2026b). Pertama, 42–56% kelas praktikum tidak memiliki alokasi asisten, sehingga sesinya tidak tercatat sama sekali. Kedua, dari sesi berasisten yang direncanakan, hanya 64–74% yang memiliki laporan pelaksanaan. Ketiga, pada periode Genap, separuh laporan baru diisi 30 hari atau lebih setelah sesi berlangsung, sehingga tidak memenuhi syarat rekaman yang dicatat saat kegiatan (Badan Standardisasi Nasional 2018). Akibatnya, persentase Proses 18 tidak dapat dihitung maupun diverifikasi. Rekapitulasi pun baru dapat dilakukan menjelang monev, ketika kelas yang tertinggal sudah tidak dapat ditindaklanjuti.

Penelitian terdahulu telah mengembangkan sistem informasi laboratorium berbasis web untuk mencatat inventaris, peminjaman alat, jadwal, dan pemakaian laboratorium (Widyantoro *et al.* 2025). Di bidang penjaminan mutu, Ismail *et al.* (2026) membangun aplikasi E-SPMI untuk mengelola dokumen dan validasi audit mutu internal. Nurramadhona *et al.* (2025) kemudian menambahkan analisis ketercapaian standar secara otomatis beserta *dashboard*, tetapi ketercapaian tersebut masih bersumber dari hasil penilaian auditor, bukan dari rekaman kegiatan operasional. Di lingkungan FIK UPNVJ, Tiara (2026) mengembangkan modul monitoring Indikator Kinerja Utama yang realisasinya direkam oleh pengguna dan dihubungkan dengan Sistem *Repository*. Sementara itu, Anandar (2026) membangun modul Odoo OpenEduCat untuk pendaftaran asisten, validasi bentrok jadwal, dan pencatatan kesiapan sarana pada tahap perencanaan praktikum. Namun, belum ada penelitian yang menurunkan skor indikator mutu laboratorium secara otomatis dari rekaman pelaksanaan setiap sesi praktikum.

Oleh karena itu, penelitian ini mengembangkan modul Odoo yang mencatat pelaksanaan sesi praktikum pada saat sesi berlangsung. Cakupannya meliputi jurnal sesi, presensi praktikan, asisten, laboran, dan dosen, *log book*, serta pengajuan perubahan dan sesi pengganti yang terhubung ke sesi asalnya. Dari rekaman tersebut, modul menghitung persentase dan skor indikator secara otomatis, lalu menyajikannya dalam *dashboard* yang dapat ditelusuri sampai ke sesi yang belum memenuhi beserta alasannya. Odoo dipilih karena tiga alasan. Pertama, modul ini melanjutkan modul OpenEduCat yang telah dibangun oleh Anandar (2026). Kedua, Odoo bersifat *open source* dan dapat dikustomisasi (Nurrohmah dan Wiratama 2022). Ketiga, Odoo menyediakan hak akses dan *record rule* per kelompok pengguna (Odoo S.A. 2023), sehingga setiap rekaman dapat dikaitkan dengan personel yang bertanggung jawab.

Penelitian ini merupakan bagian dari proyek LabFIK Compliance, yang dikerjakan oleh beberapa kelompok dan masing-masing memegang sebagian indikator Instrumen Monev. Kelompok penulis mencakup indikator Pengelolaan 4, Persiapan 15–17, dan Proses 18. Penugasan asisten dan laboran serta perencanaan dan kesiapan sesi dibahas pada penelitian yang terpisah. Penelitian ini sendiri membahas pencatatan pelaksanaan sesi untuk Proses 18 dan *dashboard* skor kelima indikator tersebut. Pengembangan dilakukan dengan metode **[KONFIRMASI: metode pengembangan]**. Melalui penelitian ini, setiap sesi praktikum di LabFIK diharapkan memiliki rekaman yang sah dan dapat diverifikasi, sehingga KaLab dapat memantau skor indikator sepanjang semester, bukan hanya menjelang monev.

## Daftar Pustaka

Anandar, R. (2026) *Pengembangan Modul Perencanaan Asisten Praktikum Berbasis Odoo OpenEduCat (Studi Kasus: Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta)*. Skripsi. Jakarta: UPN "Veteran" Jakarta. Tersedia di: http://repository.upnvj.ac.id/51635/.

Annam, S., Muhiddin, N.H., Fatkhulloh, S., Sangkala, N.R. dan Hasanuddin (2026) 'Pelatihan Unit Praktikum (Fisika) Mata Kuliah IPA Sekolah II bagi Asisten Praktikum Laboratorium IPA', *Jurnal Pengabdian Pendidikan IPA Kontekstual*, 4(2), hlm. 34–43. doi: 10.29303/jppik.v4i2.1602.

Badan Standardisasi Nasional (2018) *SNI ISO/IEC 17025:2017 Persyaratan Umum Kompetensi Laboratorium Pengujian dan Kalibrasi*. Jakarta: BSN.

Ismail, A., Arief, S.N. dan Pramudya, H.A. (2026) 'Pengembangan Aplikasi E-SPMI (Sistem Penjaminan Mutu Internal) Audit Berbasis Web Politeknik Negeri Malang', *Jurnal Informatika Polinema*, 12(3), hlm. 519–528. doi: 10.33795/jip.v12i3.9580.

LabFIK UPNVJ (2026a) *Alokasi Pertemuan Asisten Praktikum* [*spreadsheet*]. Data internal, tidak dipublikasikan. Jakarta: Laboratorium FIK UPN "Veteran" Jakarta.

LabFIK UPNVJ (2026b) *Pelaksanaan Asistensi Praktikum LABFIK UPNVJ (Responses)* [*spreadsheet*]. Data internal, tidak dipublikasikan. Jakarta: Laboratorium FIK UPN "Veteran" Jakarta.

Nurramadhona, R.D., Ismail, A. dan Arief, S.N. (2025) 'Integrasi Fitur Analisis Ketercapaian Standar dalam Aplikasi E-SPMI', *Jurnal Informatika Polinema*, 12(1), hlm. 9–18. doi: 10.33795/jip.v12i1.8432.

Nurrohmah, W.M. dan Wiratama, J. (2022) 'Enterprise Resource Planning (ERP) SAP Business One Evaluation and Improvement Recommendation using Customized Odoo', *Ultima InfoSys: Jurnal Ilmu Sistem Informasi*, 13(2), hlm. 77–84. doi: 10.31937/si.v13i2.2802.

Odoo S.A. (2023) *Security in Odoo — Odoo 17.0 Documentation*. Tersedia di: https://www.odoo.com/documentation/17.0/developer/reference/backend/security.html (Diakses: 17 Oktober 2026).

Tiara, F. (2026) *Pengembangan Modul Perencanaan dan Monitoring Indikator Kinerja Utama dan Perjanjian Kinerja pada Fakultas Ilmu Komputer UPN "Veteran" Jakarta*. Skripsi. Jakarta: UPN "Veteran" Jakarta. Tersedia di: http://repository.upnvj.ac.id/51983/.

UPN "Veteran" Jakarta (2026) *Instrumen Monitoring dan Evaluasi Laboratorium UPNVJ 2026 Versi 1.1*. Dokumen internal. Jakarta: UPN "Veteran" Jakarta.

Widyantoro, W., Sya'diyah, S. dan Fathonah, A.K. (2025) 'Pengembangan Sistem Informasi Laboratorium Pendidikan Jurusan Kesehatan Lingkungan Poltekkes Kemenkes Yogyakarta', *Health Education Laboratory*, 1(1), hlm. 33–40. doi: 10.29238/helab.v1i1.2165.
