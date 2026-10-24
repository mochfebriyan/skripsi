**Usulan judul:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan Sesi dan Perhitungan Otomatis Skor Indikator Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

*Role 3 proyek LabFIK Compliance. Cakupan indikator: Proses 18, ditambah dashboard skor Pengelolaan 4, Persiapan 15, 16, 17, dan Proses 18.*

# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta menyelenggarakan praktikum untuk lebih dari 70 kelas setiap semester (LabFIK UPNVJ 2026a). Mulai tahun 2026, LabFIK dinilai melalui Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026, yang memuat 64 indikator dengan skor 1 sampai 4. Indikator yang buktinya tidak dapat diverifikasi diberi skor terendah (UPN "Veteran" Jakarta 2026). Instrumen ini mengacu antara lain pada SNI ISO/IEC 17025:2017 **[KONFIRMASI: dasar resmi acuan ini]**, yang mensyaratkan rekaman kegiatan laboratorium dicatat pada saat kegiatan berlangsung, memuat identitas personel yang bertanggung jawab, dan perubahannya dapat ditelusuri (Badan Standardisasi Nasional 2018). Lima indikator di antaranya menjadikan sesi praktikum sebagai unit yang dihitung, yaitu setiap sesi memiliki laboran dan asisten yang ditugaskan sesuai kompetensi minimum (Pengelolaan 4), jadwal dan modul tersedia sebelum sesi (Persiapan 15), alat dan perangkat lunak siap sebelum sesi (Persiapan 16), bahan praktikum tersedia sebelum sesi (Persiapan 17), dan sesi terlaksana sesuai jadwal, modul, dan waktu (Proses 18). Skor kelima indikator dihitung dari persentase sesi yang memenuhi, sehingga sesi yang sudah dilaksanakan dengan benar tetap bernilai rendah apabila rekamannya tidak dapat ditunjukkan.

Namun, pencatatan praktikum di LabFIK saat ini tersebar di beberapa Google Form dan *spreadsheet* yang tidak saling terhubung dan dirancang untuk keperluan honor asisten, bukan sebagai bukti mutu (LabFIK UPNVJ 2026a; 2026b). Penugasan asisten belum terhubung dengan bukti kompetensinya, dan bukti kompetensi laboran belum terdokumentasi. Rencana pertemuan tidak memuat hari dan jam pelaksanaan, modul diunggah asisten pada saat atau setelah sesi tanpa versi, dan kesiapan sarana hanya dilaporkan asisten melalui satu pilihan pada form, bukan melalui *checklist* oleh laboran. Pada tahap pelaksanaan, analisis rekaman periode 2025/2026 Ganjil dan Genap menunjukkan bahwa 42–56% kelas praktikum tidak memiliki asisten sehingga sesinya tidak tercatat sama sekali, hanya 64–74% sesi berasisten yang memiliki laporan, dan pada periode Genap separuh laporan baru diisi 30 hari atau lebih setelah sesi berlangsung. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: nama, jabatan, tanggal wawancara, alur penugasan asisten dan laboran, serta alur pelaporan sesi.]** Akibatnya, persentase kelima indikator tidak dapat dihitung maupun diverifikasi, dan rekapitulasi baru dilakukan secara manual menjelang monev, ketika kelas yang tertinggal sudah tidak dapat ditindaklanjuti.

Penelitian terdahulu menunjukkan bahwa sistem informasi dapat menggantikan pencatatan manual di laboratorium maupun penjaminan mutu. Widyantoro *et al.* (2025) mengembangkan sistem informasi laboratorium berbasis web untuk mencatat inventaris, peminjaman alat, jadwal, dan pemakaian laboratorium. Ismail *et al.* (2026) membangun aplikasi E-SPMI untuk mengelola dokumen dan validasi audit mutu internal, dan pada aplikasi yang sama Nurramadhona *et al.* (2025) menambahkan analisis ketercapaian standar secara otomatis beserta *dashboard*. Di FIK UPNVJ, Tiara (2026) mengembangkan modul monitoring Indikator Kinerja Utama, sedangkan Anandar (2026) membangun modul Odoo OpenEduCat untuk perencanaan dan pendaftaran asisten praktikum di LabFIK dengan skor *System Usability Scale* 81,88. Namun, ketercapaian pada penelitian-penelitian tersebut masih bersumber dari penilaian auditor atau realisasi yang direkam pengguna, dan modul Anandar (2026) belum menghubungkan asisten dengan sesi yang benar-benar dilaksanakan. Belum ada penelitian yang menurunkan skor indikator mutu laboratorium secara otomatis dari rekaman operasional setiap sesi praktikum.

Oleh karena itu, proyek LabFIK Compliance mengembangkan modul Odoo yang melanjutkan modul Anandar (2026) dan mengelola asisten serta sesi praktikum dalam satu alur, mulai dari rekrutmen dan penugasan petugas berdasarkan kompetensi minimum, perencanaan jadwal dan modul berversi, pemeriksaan kesiapan sarana, hingga pelaksanaan sesi. Seluruh tahap tersebut tercatat pada satu data sesi praktikum yang sama, sehingga skor kelima indikator dapat dihitung secara otomatis dan ditelusuri sampai ke sesi asalnya. Odoo dipilih karena bersifat *open source* dan dapat dikustomisasi (Nurrohmah dan Wiratama 2022), serta menyediakan hak akses dan *record rule* per kelompok pengguna sehingga setiap rekaman dapat dikaitkan dengan personel yang bertanggung jawab (Odoo S.A. 2023).

Proyek ini dikerjakan oleh beberapa kelompok yang masing-masing memegang sebagian indikator Instrumen Monev. Kelompok penulis mencakup lima indikator di atas, dengan penugasan asisten dan laboran serta perencanaan dan kesiapan sesi dibahas pada penelitian terpisah. Penelitian ini membahas tahap pelaksanaan untuk indikator Proses 18, yaitu jurnal sesi, presensi praktikan, asisten, laboran, dan dosen, *log book*, serta pengajuan perubahan dan sesi pengganti yang terhubung ke sesi asalnya, yang dicatat pada saat sesi berlangsung. Penelitian ini juga membangun perhitungan skor dan *dashboard* kelima indikator yang dapat ditelusuri sampai ke sesi yang belum memenuhi beserta alasannya. Pengembangan dilakukan dengan metode **[KONFIRMASI: metode pengembangan]**. Melalui penelitian ini, KaLab diharapkan dapat memantau skor indikator sepanjang semester berdasarkan rekaman yang dapat diverifikasi, bukan hanya menjelang monev.

## 1.2 Identifikasi Masalah

Berdasarkan latar belakang yang telah diuraikan, masalah yang diidentifikasi dalam penelitian ini adalah sebagai berikut:

1. Pencatatan pelaksanaan sesi praktikum hanya berupa laporan asisten melalui Google Form, sedangkan rencana pertemuan tidak memuat hari dan jam pelaksanaan. Akibatnya, sesi pada kelas tanpa asisten tidak tercatat, dan sesi yang direncanakan tidak dapat dipasangkan dengan pelaksanaannya.
2. Rekaman pelaksanaan yang ada belum memenuhi syarat bukti indikator Proses 18. Rekaman diisi setelah sesi berlangsung, tidak mencatat presensi laboran maupun rincian kegiatan dalam *log book*, dan tidak merekam perubahan jadwal serta sesi pengganti. Akibatnya, keterlaksanaan sesi tidak dapat diverifikasi.
3. Persentase dan skor indikator dihitung secara manual menjelang monev dan tidak dapat ditelusuri sampai ke sesi asalnya. Akibatnya, KaLab tidak dapat mengetahui dan menindaklanjuti kelas yang tertinggal selama semester berjalan.

## 1.3 Batasan Masalah

Agar penelitian ini lebih terarah, ruang lingkup masalah dibatasi sebagai berikut:

1. Penelitian dilakukan di LabFIK UPN "Veteran" Jakarta dan mencakup sesi praktikum terjadwal pada delapan ruang laboratorium. Peminjaman laboratorium untuk kegiatan di luar praktikum tidak dibahas.
2. Penelitian berfokus pada fase *Execute* dalam Prosedur Operasional Baku (POB) Manajemen Praktikum FIK **[KONFIRMASI: nama fase pada dokumen POB]**, yaitu pencatatan sesi sejak pelaksanaan hingga penutupan periode monev. Rekrutmen dan penugasan asisten, penjadwalan, pemeriksaan kesiapan sarana, serta perhitungan honor asisten dibahas pada penelitian terpisah dalam proyek LabFIK Compliance.
3. Pencatatan pelaksanaan dibangun untuk indikator Proses 18. *Dashboard* menampilkan skor indikator Pengelolaan 4, Persiapan 15, 16, 17, dan Proses 18. Data dan aturan penilaian keempat indikator selain Proses 18 berasal dari modul penelitian lain dalam proyek yang sama. Indikator lain pada Instrumen Monev tidak dicakup.
4. Sistem berfungsi sebagai alat pencatatan, pembuktian, dan pemantauan, sehingga tidak menjamin terpenuhinya indikator dan tidak menggantikan verifikasi oleh asesor monev. Ambang penilaian yang belum ditetapkan oleh instrumen, seperti toleransi keterlambatan dan durasi minimal sesi, mengikuti ketetapan KaLab.
5. Pengembangan menggunakan Odoo *Community Edition* versi 17.0 dengan modul OpenEduCat, melanjutkan modul yang dibangun oleh Anandar (2026). Penelitian ini tidak membandingkan Odoo dengan *platform* lain.
6. Data uji berasal dari rekaman pelaksanaan praktikum periode 2025/2026 Ganjil dan Genap yang telah dianonimkan **[KONFIRMASI: apakah ada uji coba pada semester berjalan]**.
7. Pengembangan menggunakan metode **[KONFIRMASI: Water-Scrum-Fall]**. Pengujian dilakukan dengan *black box testing* dan *User Acceptance Testing* (UAT), dengan responden KaLab, laboran/PLP, dosen pengampu, dan asisten praktikum.

## 1.4 Tujuan dan Manfaat

Berdasarkan identifikasi masalah di atas, tujuan penelitian ini adalah sebagai berikut:

1. Membangun fitur pencatatan pelaksanaan sesi praktikum yang terhubung ke sesi yang direncanakan, termasuk pengajuan perubahan jadwal dan sesi pengganti yang terhubung ke sesi asalnya.
2. Menghasilkan rekaman pelaksanaan yang memenuhi syarat bukti indikator Proses 18. Rekaman tersebut dicatat pada saat sesi berlangsung, memuat identitas personel, mencakup presensi praktikan, asisten, laboran, dan dosen beserta *log book*, serta menyimpan riwayat perubahannya.
3. Membangun perhitungan skor indikator Proses 18 secara otomatis beserta *dashboard* skor kelima indikator yang dapat ditelusuri sampai ke sesi yang belum memenuhi dan alasannya.
4. Menguji modul melalui *black box testing* dan UAT, serta membandingkan skor Proses 18 hasil perhitungan sistem dengan hasil perhitungan manual pada data periode 2025/2026 Genap.

Penelitian ini diharapkan memberikan manfaat sebagai berikut:

1. Manfaat Praktis
   - a. Bagi LabFIK UPNVJ: menyediakan rekaman pelaksanaan sesi yang siap diverifikasi saat monev, memungkinkan KaLab memantau kelas yang tertinggal sepanjang semester, serta mengurangi rekapitulasi manual menjelang monev.
   - b. Bagi asisten praktikum, laboran, dan dosen: pencatatan sesi cukup dilakukan satu kali pada saat sesi berlangsung, menggantikan pengisian form dan rekap yang terpisah.
2. Manfaat Akademis
   - a. Bagi proyek LabFIK Compliance dan penelitian selanjutnya: mekanisme perhitungan skor dapat diperluas ke indikator lain pada Instrumen Monev tanpa mengubah rancangan dasarnya.
   - b. Bagi komunitas akademik: menjadi referensi penerapan Odoo untuk pembuktian mutu laboratorium yang bersumber dari rekaman operasional.
   - c. Bagi penulis: menerapkan pengetahuan perkuliahan dalam kustomisasi dan pewarisan (*inheritance*) modul pada *framework* Odoo.

## Daftar Pustaka

Anandar, R. (2026) *Pengembangan Modul Perencanaan Asisten Praktikum Berbasis Odoo OpenEduCat (Studi Kasus: Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta)*. Skripsi. Jakarta: UPN "Veteran" Jakarta. Tersedia di: http://repository.upnvj.ac.id/51635/.

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
