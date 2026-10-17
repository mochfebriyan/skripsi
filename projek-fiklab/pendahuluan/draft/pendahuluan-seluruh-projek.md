**Usulan judul:** Kustomisasi Modul Odoo untuk Pengelolaan Sesi Praktikum dan Asisten Praktikum Berbasis Indikator Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

*Cakupan indikator Instrumen Monev Laboratorium UPNVJ 2026: Pengelolaan 4, Persiapan 15, 16, 17, dan Proses 18.*

# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Mulai tahun 2026, Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta dinilai melalui Instrumen Monitoring dan Evaluasi (Monev) Laboratorium UPNVJ 2026, yang disusun dengan acuan antara lain SNI ISO/IEC 17025:2017 sebagai arah menuju standar kompetensi laboratorium (UPNVJ 2026). **[KONFIRMASI: sumber/dasar resmi bahwa audit mengarah ke ISO 17025 mulai tahun ini.]** Instrumen ini memuat 64 indikator yang masing-masing diberi skor 1 sampai 4, dan skor terendah diberikan apabila bukti tidak dapat diverifikasi. Karena tuntutan ini baru berlaku, LabFIK belum memiliki cara pencatatan yang disiapkan untuk menghasilkan bukti tersebut, padahal kegiatan yang sudah dilaksanakan dengan benar tetap bernilai 1 apabila rekamannya tidak dapat ditunjukkan.

Lima indikator menjadikan sesi praktikum sebagai unit yang dihitung, yaitu setiap sesi memiliki laboran dan asisten yang ditugaskan sesuai kompetensi minimum (Pengelolaan 4), jadwal dan modul tersedia sebelum sesi (Persiapan 15), alat dan perangkat lunak siap sebelum sesi (Persiapan 16), bahan praktikum tersedia sebelum sesi (Persiapan 17), dan sesi terlaksana sesuai jadwal (Proses 18). Saat ini, pendaftaran asisten, pelaksanaan asistensi, peminjaman laboratorium, dan permintaan perangkat lunak dicatat melalui Google Form dan Google Sheets yang terpisah (LabFIK UPNVJ 2026). Pelaksanaan sesi hanya tercatat untuk sesi yang memiliki asisten, rencana jadwal tidak dicocokkan dengan realisasinya, dan penugasan asisten tidak terhubung dengan bukti kompetensinya, seperti nilai mata kuliah terkait yang menjadi syarat internal. Honor asisten pun baru dapat dihitung setelah rekapitulasi pelaksanaan asistensi dikumpulkan secara manual. Akibatnya, persentase sesi yang memenuhi kelima indikator harus dihitung manual menjelang monev, dan sebagian bukti tidak tersedia sama sekali. **[KONFIRMASI melalui wawancara dengan KaLab/PLP: alur seleksi dan penugasan asisten, cara perhitungan honor, serta adanya sesi tanpa asisten.]**

Penelitian terdahulu telah mengembangkan sistem pengelolaan laboratorium (Widyantoro *et al.* 2024) maupun sistem penjaminan mutu (Ismail *et al.* 2026), tetapi data operasional laboratorium belum dimanfaatkan langsung sebagai bukti indikator mutu. Di LabFIK sendiri, Anandar (2026) telah membangun modul Odoo untuk perencanaan kebutuhan dan pendaftaran asisten praktikum pada fase *Establish*, namun belum menghubungkan asisten dengan sesi yang benar-benar dilaksanakan, sehingga cakupan asisten per sesi dan honor berdasarkan kehadiran belum dapat diturunkan dari sistem.

Oleh karena itu, penelitian ini mengembangkan modul Odoo sebagai bagian dari proyek LabFIK Compliance yang melanjutkan modul Anandar (2026). Modul ini mencakup rekrutmen dan seleksi asisten berdasarkan kompetensi minimum, penugasan laboran dan asisten pada setiap sesi, pencatatan sesi dari jadwal yang disetujui, kesiapan sarana, hingga pelaksanaan dan sesi pengganti, serta perhitungan honor asisten dari kehadiran yang tercatat. Dari data tersebut, skor kelima indikator dihitung secara otomatis dan dapat ditelusuri sampai ke sesi asalnya. Odoo dipilih karena bersifat *open source*, dapat dikustomisasi (Nurrohmah dan Wiratama 2022), dan menyediakan pengaturan hak akses per peran pengguna (Odoo S.A. 2023).

## 1.2 Rumusan Masalah

1. Bagaimana kondisi pengelolaan sesi praktikum dan asisten praktikum di LabFIK saat ini, serta kesenjangannya terhadap bukti yang dipersyaratkan indikator Pengelolaan 4, Persiapan 15, 16, 17, dan Proses 18?
2. Bagaimana merancang dan membangun modul Odoo yang mengelola rekrutmen dan penugasan asisten, siklus sesi praktikum, serta perhitungan honor asisten?
3. Bagaimana modul tersebut menghitung skor kelima indikator secara otomatis, dan bagaimana tingkat penerimaan pengguna terhadapnya?

## Daftar Pustaka

Anandar, R. (2026) *[Lengkapi judul: Modul Perencanaan Asisten Praktikum berbasis Odoo OpenEduCat, Laboratorium FIK UPNVJ]*. Skripsi. Jakarta: UPN "Veteran" Jakarta. Tersedia di: http://repository.upnvj.ac.id/51635/.

Ismail, A., Arief, S.N. dan Pramudya, H.A. (2026) 'Pengembangan Aplikasi E-SPMI (Sistem Penjaminan Mutu Internal) Audit Berbasis Web Politeknik Negeri Malang', *Jurnal Informatika Polinema*, 12(3), hlm. 519–528.

LabFIK UPNVJ (2026) *Portal Layanan LabFIK UPNVJ*. Tersedia di: https://lab.fik.upnvj.ac.id (Diakses: 12 Oktober 2026).

Nurrohmah, W.M. dan Wiratama, J. (2022) 'Enterprise Resource Planning (ERP) SAP Business One Evaluation and Improvement Recommendation using Customized Odoo', *Ultima InfoSys: Jurnal Ilmu Sistem Informasi*, 13(2), hlm. 77–84. doi: 10.31937/si.v13i2.2802.

Odoo S.A. (2023) *Security in Odoo — Odoo 17.0 Documentation*. Tersedia di: https://www.odoo.com/documentation/17.0/developer/reference/backend/security.html (Diakses: 12 Oktober 2026).

UPN "Veteran" Jakarta (2026) *Instrumen Monitoring dan Evaluasi Laboratorium UPNVJ 2026 Versi 1.1*. Dokumen internal. Jakarta: UPN "Veteran" Jakarta.

Widyantoro, W., Sya'diyah, S. dan Fathonah, A.K. (2024) 'Pengembangan Sistem Informasi Laboratorium Pendidikan Jurusan Kesehatan Lingkungan Poltekkes Kemenkes Yogyakarta', *Health Educational Laboratory (HELAB)*, 1(1), hlm. 33–40. doi: 10.29238/helab.v1i1.2165.
