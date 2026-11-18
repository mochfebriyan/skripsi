# PROYEK PEMBANGUNAN SISTEM INFORMASI KEGIATAN KEMAHASISWAAN BERBASIS WEBSITE DENGAN FRAMEWORK LARAVEL (STUDI KASUS BEASISWA FAKULTAS ILMU KOMPUTER UNIVERSITAS PEMBANGUNAN NASIONAL”VETERAN” JAKARTA)

# **BAB II**

# **RANCANGAN PRODUK**

# **2.1 Deskripsi Aktor**

Penetapan peran yang jelas bagi setiap aktor dalam sistem informasi beasiswa Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta merupakan kunci untuk memastikan kelancaran dan efisiensi pengelolaan dan pelaksanaan beasiswa. Identifikasi peran yang tepat membantu memastikan setiap pengguna sistem hanya memiliki akses dan kewenangan yang sesuai dengan tugasnya. Dengan mengidentifikasi peran secara jelas, dapat meminimalisir risiko penyalahgunaan sistem dan memastikan akuntabilitas dalam pengelolaan beasiswa. Tabel berikut ini memberikan deskripsi rinci tentang peran masingmasing aktor dalam sistem informasi beasiswa.

Tabel 2.1 Deskripsi Aktor

|**Aktor**|**Deskripsi**|
|---|---|
|Mahasiswa|1. Dapat mengakses informasi beasiswa.<br>2. Dapat melakukan pendaftaran beasiswa.<br>3. Dapat melihat buku panduan (guidebook)<br>beasiswa.<br>4. Dapat melakukan pendataan mandiri saat<br>mendaftar beasiswa.<br>5. Dapat mengunggah surat bukti penerima<br>beasiswa dan melakukan konfirmasi penerima<br>beasiswa.|
|Badan Eksekutif|1. Dapat melihat dan mengakses informasi|
|Mahasiswa (BEM)|beasiswa.|
|Fakultas Ilmu|2. Dapat menambahkan informasi beasiswa.|
|Komputer Universitas|3. Dapat menghapus informasi beasiswa yang|
|Pembangunan|telah ditambahkan oleh BEM.|

|Nasional “Veteran”<br>Jakarta|4. Dapat memperbarui atau mengedit informasi<br>beasiswa yang telah ditambahkan oleh BEM.|
|---|---|
|Kelompok Studi|1. Dapat melihat dan mengakses informasi|
|Mahasiswa (KSM)|beasiswa.|
|Fakultas Ilmu|2. Dapat menambahkan informasi beasiswa.|
|Komputer Universitas<br>Pembangunan|3. Dapat menghapus informasi beasiswa yang<br>telah ditambahkan oleh KSM.|
|Nasional “Veteran”<br>Jakarta|4. Dapat memperbarui atau mengedit informasi<br>beasiswa yang telah ditambahkan oleh KSM.|
|Wakil Dekan 3|1. Dapat melihat dan mengakses informasi<br>beasiswa.<br>2. Dapat mengakses laporan pendataan<br>mahasiswa yang mendaftar beasiswa.<br>3. Dapat mengakses laporan  pendataan<br>mahasiswa penerima beasiswa.|
|Koordinator<br>Program Studi|1. Dapat melihat dan mengakses informasi<br>beasiswa.<br>2. Dapat melakukan pencarian beasiswa.<br>3. Dapat mengakses laporan pendataan<br>mahasiswa yang mendaftar beasiswa.<br>4. Dapat mengakses laporan pendataan<br>mahasiswa penerima beasiswa.|
|Dosen|1. Dapat melihat dan mengakses informasi<br>beasiswa.<br>2. Dapat menambahkan informasi beasiswa.<br>3. Dapat menghapus informasi beasiswa yang<br>telah ditambahkan oleh Dosen.|

||4.|Dapat memperbarui atau mengedit informasi<br>beasiswa yang telah ditambahkan oleh Dosen.|
|---|---|---|
|Staf Tata Usaha|1.|Dapat melihat dan mengakses informasi<br>beasiswa.|
||2.|Dapat membuat, membaca, memperbarui, dan<br>menghapus (CRUD) semua informasi yang|
|||tersedia dalam sistem.|
||3.|Dapat mengakses pendataan mahasiswa yang|
|||mendaftar beasiswa.|
||4.|Dapat mengakses pendataan mahasiswa|
|||penerima beasiswa.|
||5.|Dapat memvalidasi data penerima beasiswa.|

# **2.2 Kerangka Pikir**

Berdasarkan deskripsi aktor yang sudah dijelaskan, langkah selanjutnya adalah merumuskan kerangka pikir. Kerangka pikir merupakan panduan penting dalam perencanaan proyek pembangunan sistem informasi kegiatan kemahasiswaan berbasis website. Dengan kerangka pikir yang terstruktur, proyek ini dapat dijalankan secara sistematis, mulai dari perancangan hingga implementasi. Hal ini memungkinkan semua pihak yang terlibat, baik pengembang maupun pengguna, untuk memiliki pemahaman yang sama tentang alur kerja dan interaksi antar elemen dalam sistem. Berikut adalah gambar yang menjelaskan kerangka pikir proyek pembangunan sistem informasi beasiswa Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta.

<!-- Start of picture text -->
A=<br>-2 |<br>‘— al<br><!-- End of picture text -->

Gambar 2.3 Kerangka Pikir

Sistem informasi kegiatan kemahasiswaan ini dirancang untuk mempermudah pengguna dalam mengakses informasi serta melakukan proses pendaftaran beasiswa di Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Seperti yang tergambarkan pada ilustrasi sebelumnya, sistem ini melibatkan sejumlah aktor, yaitu mahasiswa, Badan Eksekutif Mahasiswa (BEM), Kelompok Studi Mahasiswa (KSM), Wakil Dekan 3, Koordinator Program Studi, Dosen, serta Staf Tata Usaha (Admin).

Semua aktor yang terlibat dapat melakukan _login_ untuk dapat mengakses informasi kegiatan kemahasiswa pada _website_ . Badan Eksekutif Mahasiswa (BEM), Kelompok Studi Mahasiswa (KSM), dan Staf Tata Usaha dapat melakukan _Create, Read, Update, Delete_ (CRUD) informasi terkait Beasiswa yang diunggahnya, lalu data ini akan tersimpan di database informasi beasiswa yang kemudian informasi tersebut dapat dilihat oleh mahasiswa.

Mahasiswa, setelah melakukan login dapat mencari beasiswa, melihat berbagai informasi beasiswa yang tersedia, dan melihat buku panduan (guidebook) beasiswa. Lalu, mahasiswa dapat mengklik tautan dan mengisi form pendaftaran yang tersedia serta mencantumkan dokumen persyaratan yang dibutuhkan untuk mendaftar beasiswa. Kemudian, mahasiswa diminta untuk melakukan pengisian form pendataan pendaftar beasiswa fakultas. Form tersebut dapat diakses oleh Wakil Dekan 3,  Koordinator Program Studi, dan Staf Tata Usaha.

Jika ada mahasiswa yang keterima beasiswa maka mahasiswa melakukan konfirmasi pada _website_ yang dimana data mahasiswa tersebut akan terisi otomatis dari data pendaftar beasiswa dan data ini juga dapat diakses oleh Wakil Dekan 3, Koordinator Program Studi, dan Staf Tata Usaha. Lalu, Staf Tata Usaha akan membuatkan surat keterangan penerima beasiswa dan bisa diunduh oleh mahasiswa.

# **2.3** **_Low-Fidelity_**

Mengacu pada kerangka pikir yang telah disusun sebelumnya, dirancang beberapa desain low-fidelity sebagai representasi awal dari konsep yang berkaitan dengan beasiswa di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. Desain ini berperan sebagai prototipe awal yang menggambarkan tampilan antarmuka pengguna serta jalur interaksi dalam sistem, dengan penekanan pada struktur dasar dan fungsionalitas utama. Tujuannya adalah untuk memvisualisasikan ide desain secara umum serta mengidentifikasi kebutuhan tambahan sebelum masuk ke tahap pengembangan yang lebih rinci.

<!-- Start of picture text -->
Masuk<br><!-- End of picture text -->

Gambar 2.4 Tampilan Login

Pada halaman login, pengguna memiliki opsi untuk memasukkan username (nama pengguna) dan kata sandi. Terdapat juga tombol "Masuk" yang dapat diklik oleh pengguna untuk memulai proses login ke dalam sistem.

<!-- Start of picture text -->
Form Penyebaran Informasi Beasiswa<br>Poster Beasiswa<br>= =<br><!-- End of picture text -->

Gambar 2.5 Tampilan Form Penyebaran Informasi Beasiswa

Pada halaman formulir penyebaran informasi beasiswa, Badan Eksekutif Mahasiswa (BEM), Kelompok Studi Mahasiswa (KSM), dan Staf Tata Usaha Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta memiliki akses untuk mengisi detail informasi beasiswa. Informasi yang dapat dimasukkan meliputi nama beasiswa, deskripsi beasiswa, penyelenggara, batas waktu pendaftaran, buku panduan (guidebook), tautan pendaftaran, dan poster beasiswa. Selain itu, mereka juga dapat melakukan tindakan seperti mengedit, menyimpan perubahan, atau membatalkan perubahan yang telah dilakukan pada Formulir Penyebaran Informasi Beasiswa.

<!-- Start of picture text -->
Informasi Beasiswa Uploaded<br>by BEM/KSM/STAFTU<br>Nama Beasiewa<br>Deadline Pendattaran<br>Penyelenggara<br>pubvinersednislid<br>tlementum mattisnune.amet. Lotem Fermentum tincidundolor s it euamet plapsum c eratonsectetur alquet Est vitaeAmet du<br>elementum matis nunc<br><!-- End of picture text -->

Gambar 2.6 Tampilan Informasi Beasiswa

Pada halaman informasi beasiswa, pengguna dapat melihat detail beasiswa seperti nama beasiswa, batas waktu pendaftaran, penyelenggara, deskripsi singkat, serta poster terkait beasiswa yang akan dilaksanakan. Pengguna juga memiliki opsi untuk mendaftar beasiswa dengan menekan tombol “Daftar” dan melihat buku panduan (guidebook) beasiswa dengan mengklik tombol “Lihat Guidebook”.

<!-- Start of picture text -->
Form Pendataan Pendaftar Beasiswa<br>NamaLengkep<br>Nim<br>Program Studi {<br>Angkatan {<br>NamaBeasiswa<br>( )<br><!-- End of picture text -->

Gambar 2.7 Tampilan Form Pendataan Pendaftar Beasiswa

Pada halaman formulir pendataan pendaftar beasiswa, pengguna dapat mengisi data yang diperlukan, seperti nama, nomor induk mahasiswa (NIM), program studi, angkatan, nama beasiswa, jenis beasiswa, dan penyelenggara beasiswa. Setelah mengisi formulir, pengguna dapat mengirimkan data dengan menekan tombol “Submit” atau membatalkan pendaftaran dengan mengklik tombol “Batal”.

<!-- Start of picture text -->
Informasi Pendataan Beasiswa<br>°<br><!-- End of picture text -->

Gambar 2.8 Tampilan Informasi Pendataan Beasiswa

Pada halaman informasi pendataan beasiswa, terdapat data pendaftar dan penerima beasiswa yang mencakup nama, nomor induk mahasiswa (NIM), program studi, angkatan, nama beasiswa, jenis beasiswa, dan penyelenggara beasiswa. Halaman ini hanya dapat diakses oleh Wakil Dekan 3, Koordinator Program Studi, dan Staf Tata Usaha Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta.

<!-- Start of picture text -->
Konfirmasi Penerima Beasiswa<br>= =<br><!-- End of picture text -->

Gambar 2.9 Tampilan Konfirmasi Penerima Beasiswa

Pada halaman konfirmasi penerima beasiswa, pengguna yang telah mendaftar dan dinyatakan diterima diminta untuk mengunggah surat bukti penerimaan beasiswa dari penyelenggara. Setelah mengunggah, pengguna dapat menekan tombol “Kirim”. Jika belum diterima, pengguna dapat memilih tombol “Belum Diterima” untuk melakukan konfirmasi.

<!-- Start of picture text -->
Informasi Pendataan Beasiswa<br>==<br>°<br><!-- End of picture text -->

Gambar 2.10 Tampilan Data Pendaftar dan Penerima Beasiswa

Pada halaman data pendaftar dan penerima beasiswa, terdapat informasi mengenai mahasiswa yang telah mengisi formulir pendaftaran dan melakukan konfirmasi penerimaan beasiswa. Informasi tersebut meliputi NIM, nama, program studi, angkatan, nama beasiswa, jenis beasiswa, dan penyelenggara. Halaman ini hanya dapat diakses oleh Wakil Dekan 3, Koordinator Program Studi, dan Staf Tata Usaha.

# **2.4 Teknologi Proyek**

Dalam mengembangkan sistem ini, diperlukan pemilihan teknologi yang sesuai. Hal ini meliputi perangkat keras dan perangkat lunak yang spesifik guna memastikan sistem beroperasi secara optimal dan mendukung seluruh tahap pengembangan dengan efisien. Berikut adalah detail kebutuhan perangkat keras, perangkat lunak, serta perangkat lunak pendukung lainnya.

# **2.4.1 Kebutuhan** **_Hardware_**

Proyek ini menggunakan perangkat keras Laptop HP Pavilion 14-ec0014AU dengan spesifikasi sebagai berikut:

1) Processor : AMD Ryzen 5 5500U with Radeon Graphics 2) Installed RAM  : DDR4-3200 MHz 16 GB 3) Storage : SSD 512 GB

# **2.4.2 Kebutuhan** **_Software_**

Perangkat lunak yang dimanfaatkan dalam proses pengembangan antara lain:

- 1) Operating System : Microsoft Windows 11 HSL

- 2) Programming Language  : PHP

- 3) Framework : Laravel, ReactJS, dan Tailwind CSS

- 4) Database Management    : PostgreSQL

- 5) Code Editor : VS Code

# **2.5 Rencana Pengujian Proyek**

Dalam tahap pengujian aplikasi, digunakan pendekatan Black-Box Testing, yang berfokus pada evaluasi fungsionalitas sistem tanpa melihat struktur internal atau kode sumbernya. Tujuan dari pengujian ini adalah untuk memastikan bahwa sistem berjalan sesuai dengan spesifikasi yang telah ditetapkan dan mampu memenuhi kebutuhan pengguna dengan baik.

# **2.5.1 Skenario Pengujian**

Skenario pengujian merupakan langkah penting dalam proses validasi sistem, yang bertujuan untuk memastikan bahwa seluruh fitur yang dikembangkan berjalan sesuai dengan harapan dan dapat memenuhi kebutuhan pengguna.

Tabel 2.2 Skenario _Black-Box Testing_ Akun Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>Pengguna dapat dengan mudah<br>mengakses informasi mengenai<br>dashboard yang menampilkan keaktifan<br>serta berbagai pencapaian mahasiswa.|

|2|Login<br>Fitur Da|Pengguna dapat mengakses dashboard<br>mahasiswa apabila NIM dan kata sandi<br>yang dimasukkan valid. Jika tidak, akan<br>muncul pesan kesalahan.<br>shboard|
|---|---|---|
|3|Akses informasi pada<br>dashboard|Informasi terkait kegiatan lomba,<br>beasiswa, pengabdian kepada<br>masyarakat, dan penelitian dapat<br>ditampilkan secara akurat dan benar.<br>Mahasiswa dapat mengakses menu<br>FAQ, yang berisi prosedur kegiatan.|
|4|Akses informasi beasiswa|Pengguna dapat memilih dan melihat<br>informasi beasiswa yang tersedia<br>melalui dashboard.|
|5|Akses detail informasi beasiswa|Informasi detail mengenai beasiswa<br>yang dipilih akan ditampilkan,<br>mencakup nama beasiswa, deskripsi,<br>jadwal, serta persyaratan.|
|6|Akses buku panduan beasiswa|Buku panduan beasiswa dapat diakses<br>langsung melalui browser atau diunduh<br>untuk dibaca nanti.|
|7|Mendaftar beasiswa|Pengguna dapat mengklik tautan<br>pendaftaran beasiswa, yang akan<br>mengarahkan mereka ke halaman<br>eksternal untuk proses pendaftaran.|
||Fitur|FAQ|

|8|Melihat prosedur pendaftaran<br>beasiswa|Petunjuk mengenai proses daftar<br>beasiswa disampaikan dalam format<br>yang ringkas, jelas, dan mudah<br>dimengerti oleh pengguna.|
|---|---|---|
|9|Melihat prosedur pendataan<br>penerima beasiswa<br>Fitur P|Prosedur pendataan penerima beasiswa<br>ditampilkan sesuai dengan ketentuan<br>yang berlaku di universitas.<br>endataan<br>|
|11|Melakukan pendataan<br>partisipasi beasiswa|Sistem mencatat data partisipasi<br>beasiswa dengan akurat dan<br>mengarahkan pengguna ke halaman<br>profil pada bagian riwayat pendataan.|
|12|Melakukan pendataan penerima<br>beasiswa<br>Fitur|<br>Sistem menyimpan data penerima<br>beasiswa dengan tepat dan mengalihkan<br>pengguna ke halaman profil pada<br>bagian riwayat pendataan.<br>Profile<br>|
|13|Menampilkan data mahasiswa|Informasi data mahasiswa, termasuk<br>NIM, nama, angkatan, dan program<br>studi ditampilkan dengan akurat.|
|14|Menyajikan ringkasan data<br>statistik terkait tingkat keaktifan<br>mahasiswa.|<br>Ringkasan data statistik disajikan<br>secara numerik sebagai rangkuman dari<br>berbagai aktivitas yang telah dilakukan.|
|15|Menampilkan riwayat<br>pendataan partisipasi kegiatan<br>beasiswa|Riwayat partisipasi beasiswa<br>ditampilkan dalam format daftar kartu.|

|16|Menampilkan riwayat<br>pendataan penerima beasiswa|Riwayat penerima beasiswa<br>ditampilkan dengan informasi yang<br>lengkap dan terperinci.|
|---|---|---|

Tabel 2.3 Skenario _Black-Box Testing_ Akun Admin Tata Usaha

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>Admin dapat dengan mudah mengakses<br>informasi mengenai dashboard yang<br>menampilkan keaktifan serta berbagai<br>pencapaian mahasiswa.|
|2<br>3|Login<br>Fitur Da<br>Akses informasi pada<br>dashboard admin|Admin dapat mengakses dashboard<br>mahasiswa apabila username dan kata<br>sandi yang dimasukkan valid. Jika<br>tidak, akan muncul pesan kesalahan.<br>shboard<br>Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time<br>Fitur L|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.<br>aporan|
|5|Menampilkan laporan<br>partisipasi beasiswa secara real-<br>time|Data mahasiswa yang berpartisipasi<br>beasiswa disajikan secara lengkap dan<br>terkini.|

|6|Menampilkan laporan penerima<br>beasiswa secara real-time|<br>Data mahasiswa penerima beasiswa<br>disajikan secara lengkap dan terkini.|
|---|---|---|
|7|Menampilkan data berdasarkan<br>filter|Sistem menyaring dan menampilkan<br>data sesuai dengan tahun pelaksanaan,<br>angkatan, prodi, jenis beasiswa yang<br>dipilih.|
|8|Menampilkan data nama<br>mahasiswa berdasarkan hasil<br>pencarian|Data mahasiswa ditampilkan sesuai<br>dengan nama yang dicari.|
|9|Melakukan validasi data<br>penerima beasiswa yang diisi<br>mahasiswa|Admin memverifikasi dan menyimpan<br>data penerima beasiswa yang diunggah<br>mahasiswa.|
|10|Membuka file bukti penerima<br>beasiswa|File bukti, seperti sertifikat, surat<br>keterangan dapat diakses dalam format<br>.jpg, .jpeg, .png, atau .pdf.|
|11|Membuka file screenshot/foto<br>beasiswa|Screenshot/foto dapat dibuka dalam<br>format .png, .jpg, atau .jpeg.|
|12|Mengunduh file laporan<br>kegiatan beasiswa|Laporan kegiatan dapat diakses dalam<br>format .xlsx|
||<br>Fitur Pusa|t Informasi<br>|
|13|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|14|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam<br>sistem.|

|15|Memperbarui informasi<br>beasiswa|Informasi beasiswa yang sudah ada<br>dapat diperbarui sesuai kebutuhan.|
|---|---|---|
|16|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|17|Validasi informasi beasiswa<br>Fitur Mana|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.<br>jemen User<br>|
|18|Mengakses manajemen user<br>Tabel 2.4 Skenario_Black-Bo_<br>|Admin super dapat mengubah atau<br>mengganti akses pengguna siapa saja<br>yang dapat masuk ke dashboard admin.<br>_x Testing_Akun Wakil Dekan<br>|
|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>Wakil Dekan dapat dengan mudah<br>mengakses informasi mengenai<br>dashboard yang menampilkan keaktifan<br>serta berbagai pencapaian mahasiswa.|
|2|Login<br>Fitur D|Wakil Dekan dapat mengakses<br>dashboard mahasiswa apabila username<br>(NIDN) dan kata sandi yang<br>dimasukkan valid. Jika tidak, akan<br>muncul pesan kesalahan.<br>ashboard|

|3|Akses informasi pada<br>dashboard admin|Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|---|---|---|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time<br>Fitur L<br>|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.<br>aporan<br>|
|5|Menampilkan laporan<br>partisipasi beasiswa secara real-<br>time|Data mahasiswa yang berpartisipasi<br>beasiswa disajikan secara lengkap dan<br>terkini.|
|6|Menampilkan laporan penerima<br>beasiswa secara real-time|Data mahasiswa penerima beasiswa<br>disajikan secara lengkap dan terkini.|
|7|Menampilkan data berdasarkan<br>filter|Sistem menyaring dan menampilkan<br>data sesuai dengan tahun pelaksanaan,<br>angkatan, prodi, jenis beasiswa yang<br>dipilih.|
|8|Menampilkan data nama<br>mahasiswa berdasarkan hasil<br>pencarian|Data mahasiswa ditampilkan sesuai<br>dengan nama yang dicari.|
|9|Membuka file bukti penerima<br>beasiswa|File bukti, seperti sertifikat, surat<br>keterangan dapat diakses dalam format<br>.jpg, .jpeg, .png, atau .pdf.|
|10|Membuka file screenshot/foto<br>beasiswa|Screenshot/foto dapat dibuka dalam<br>format .png, .jpg, atau .jpeg.|
|11|Mengunduh file laporan<br>kegiatan beasiswa<br>Fitur Pusa|Laporan kegiatan dapat diakses dalam<br>format .xlsx<br>t Informasi|

|12|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|---|---|---|
|13|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam<br>sistem.|
|14|Memperbarui informasi<br>beasiswa|Informasi beasiswa yang sudah ada<br>dapat diperbarui sesuai kebutuhan.|
|15|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|16|Validasi informasi beasiswa|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.|

Tabel 2.5 Skenario _Black-Box Testing_ Akun Koordinator Program Studi

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>Koordinator Program Studi dapat<br>dengan mudah mengakses informasi<br>mengenai dashboard yang<br>menampilkan keaktifan serta berbagai<br>pencapaian mahasiswa.|
|2|Login|Koordinator Program Studi dapat<br>mengakses dashboard mahasiswa<br>apabila username (NIDN) dan kata<br>sandi yang dimasukkan valid. Jika|

||Fitur Da|tidak, akan muncul pesan kesalahan.<br>shboard<br>|
|---|---|---|
|3|Akses informasi pada<br>dashboard admin|Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time<br>Fitur L<br>|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.<br>aporan<br>|
|5|Menampilkan laporan<br>partisipasi beasiswa secara real-<br>time|Data mahasiswa yang berpartisipasi<br>beasiswa disajikan secara lengkap dan<br>terkini.|
|6|Menampilkan laporan penerima<br>beasiswa secara real-time|Data mahasiswa penerima beasiswa<br>disajikan secara lengkap dan terkini.|
|7|Menampilkan data berdasarkan<br>filter|Sistem menyaring dan menampilkan<br>data sesuai dengan tahun pelaksanaan,<br>angkatan, prodi, jenis beasiswa yang<br>dipilih.|
|8|Menampilkan data nama<br>mahasiswa berdasarkan hasil<br>pencarian|Data mahasiswa ditampilkan sesuai<br>dengan nama yang dicari.|
|9|Membuka file bukti penerima<br>beasiswa|File bukti, seperti sertifikat, surat<br>keterangan dapat diakses dalam format<br>.jpg, .jpeg, .png, atau .pdf.|
|10|Membuka file screenshot/foto<br>beasiswa|Screenshot/foto dapat dibuka dalam<br>format .png, .jpg, atau .jpeg.|
|11|Mengunduh file laporan|Laporan kegiatan dapat diakses dalam|

||kegiatan beasiswa<br>Fitur Pusa|format .xlsx<br>t Informasi|
|---|---|---|
|12|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|13|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam<br>sistem.|
|14|Memperbarui informasi<br>beasiswa|Informasi beasiswa yang sudah ada<br>dapat diperbarui sesuai kebutuhan.|
|15|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|16|Validasi informasi beasiswa|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.|

Tabel 2.6 Skenario _Black-Box Testing_ Akun Dosen

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>Dosen dapat dengan mudah mengakses<br>informasi mengenai dashboard yang<br>menampilkan keaktifan serta berbagai<br>pencapaian mahasiswa.|
|2|Login|Dosen dapat mengakses dashboard<br>mahasiswa apabila username dan kata<br>sandi yang dimasukkan valid. Jika|

||Fitur Da|tidak, akan muncul pesan kesalahan.<br>shboard<br>|
|---|---|---|
|3|Akses informasi pada<br>dashboard admin|Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.|
||Fitur Pusa|t Informasi|
|5|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|6|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam<br>sistem.|
|7|Memperbarui informasi<br>beasiswa|Informasi beasiswa yang sudah ada<br>dapat diperbarui sesuai kebutuhan.|
|8|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|9|Validasi informasi beasiswa|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.|

Tabel 2.7 Skenario _Black-Box Testing_ Akun Badan Eksekutif Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>BEMF-IK dapat dengan mudah<br>mengakses informasi mengenai<br>dashboard yang menampilkan keaktifan<br>serta berbagai pencapaian mahasiswa.|
|2<br>3|Login<br>Fitur Da<br>Akses informasi pada<br>dashboard admin|BEMF-IK dapat mengakses dashboard<br>mahasiswa apabila username (NIM)<br>dan kata sandi yang dimasukkan valid.<br>Jika tidak, akan muncul pesan<br>kesalahan.<br>shboard<br>Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.|
||Fitur Pusat|Informasi|
|5|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|6|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam|

|||sistem.|
|---|---|---|
|7|Memperbarui informasi|Informasi beasiswa yang sudah ada|
||beasiswa|dapat diperbarui sesuai kebutuhan.|
|8|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|9|Validasi informasi beasiswa|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.|

Tabel 2.8 Skenario _Black-Box Testing_ Akun Kelompok Studi Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Akses tampilan utama website<br>Techfo|Tampilan utama website dirancang<br>dengan susunan yang teratur dan<br>elemen-elemen yang berfungsi optimal.<br>KSMF-IK dapat dengan mudah<br>mengakses informasi mengenai<br>dashboard yang menampilkan keaktifan<br>serta berbagai pencapaian mahasiswa.|
|2|Login<br>Fitur Da|KSMF-IK dapat mengakses dashboard<br>mahasiswa apabila username dan kata<br>sandi yang dimasukkan valid. Jika<br>tidak, akan muncul pesan kesalahan.<br>shboard|
|3|Akses informasi pada<br>dashboard admin|Dashboard menyajikan data mengenai<br>keaktifan mahasiswa serta ringkasan<br>laporan dalam bentuk grafik.|
|4|Menampilkan laporan keaktifan<br>mahasiswa secara real-time|Data terkini mengenai keaktifan<br>mahasiswa disajikan dalam format tabel<br>atau grafik.|

||Fitur Pusa|t Informasi|
|---|---|---|
|5|Mengakses pusat informasi<br>beasiswa|Pusat informasi dapat dibuka,<br>menampilkan daftar beasiswa yang<br>telah diunggah sebelumnya (jika<br>tersedia).|
|6|Menambahkan informasi<br>beasiswa|Informasi beasiswa baru berhasil<br>ditambahkan dan tersimpan dalam<br>sistem.|
|7|Memperbarui informasi<br>beasiswa|Informasi beasiswa yang sudah ada<br>dapat diperbarui sesuai kebutuhan.|
|8|Menghapus informasi beasiswa|Informasi beasiswa dihapus dari sistem<br>dan tidak lagi ditampilkan.|
|9|Validasi informasi beasiswa|Informasi beasiswa divalidasi dan<br>tersedia untuk diakses oleh mahasiswa.|


# PROYEK PENGEMBANGAN SISTEM INFORMASI MBKM PADA FAKULTAS ILMU KOMPUTER UPN “VETERAN” JAKARTA

# **BAB II**

# **RANCANGAN PROYEK**

# **2.1 Observasi**

Peneliti melakukan observasi dengan terjun langsung ke tempat penelitian yakni di Fakultas Ilmu Komputer UPN “Veteran” Jakarta, untuk mengamati secara langsung berbagai fenomena dan aktivitas yang terjadi. Tahapan ini merupakan langkah penting dalam metode penelitian karena membantu peneliti untuk mendapatkan pemahaman yang mendalam tentang konteks dan dinamika yang ada di lingkungan tersebut. Dengan terlibat secara langsung, peneliti dapat mengumpulkan data yang lebih akurat dan mendapatkan wawasan yang lebih dalam mengenai topik yang sedang diteliti. Observasi juga membantu peneliti untuk melihat secara langsung interaksi antara individu, kebijakan dan lingkungan, yang dapat memberikan wawasan yang mendalam untuk proses penelitian.

# **2.1.1 Diagram Sistem Berjalan**

Diagram berikut merupakan diagram sistem berjalan pada Sistem Informasi MBKM Pada Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Sistem berjalan ditunjukkan pada gambar dibawah ini.

Gambar 2.1 Proses Bisnis MBKM Sistem Saat Ini

Diagram proses bisnis pada gambar 2.1 menggambarkan alur pengelolaan kegiatan MBKM yang terdiri dari admin, PIC MBKM, dan mahasiswa. Proses dimulai dari admin yang membuat _form_ pengajuan surat rekomendasi (SR), kemudian mahasiswa mengisi form tersebut. Setelah data pengajuan diterima, admin menyimpan data ke dalam _Google Drive_ untuk mempermudah pengelolaan dan penyimpanan.

Selanjutnya, admin membuat _form_ pendaftaran MBKM, yang kemudian disebarkan oleh PIC MBKM melalui _link_ kepada mahasiswa. Mahasiswa mengisi form pendaftaran MBKM dan menunggu pengumuman hasil seleksi, termasuk informasi mengenai dosen pembimbing.

Setelah mahasiswa diterima, proses berlanjut ke tahap pendaftaran ulang di mana admin membuat _form_ pendaftaran ulang kemudian PIC MBKM menyebarkan _link form_ tersebut. Mahasiswa kembali mengisi _form_ pendaftaran ulang sebagai bagian dari kelengkapan administrasi. Admin juga membuat form pelaporan kegiatan yang disebarkan oleh PIC MBKM, dan mahasiswa mengisinya untuk menyampaikan laporan kegiatan MBKM. Semua data, mulai dari pengajuan hingga laporan, dikelola dan disimpan oleh admin ke dalam _Google Drive_ . Tahapan terakhir melibatkan mahasiswa yang menunggu proses konversi SKS sebagai hasil dari kegiatan MBKM yang telah dilakukan. Diagram ini mencerminkan alur kerja yang terstruktur dan mendukung koordinasi antara berbagai pihak untuk memastikan keberhasilan program MBKM.

# **2.2 Usulan Solusi (DFD)**

Pada tahapan ini, diusulkan solusi berupa Data Flow Diagram (DFD) yang menggambarkan alur data dalam sistem secara terstruktur dan jelas. DFD digunakan untuk memvisualisasikan bagaimana data mengalir antara proses-proses utama, sumber data eksternal, dan penyimpanan data dalam sistem yang diusulkan. Solusi ini dirancang untuk mempermudah pemahaman alur kerja sistem serta membantu dalam identifikasi kebutuhan sistem secara lebih detail. Dengan adanya DFD, pengembangan sistem dapat dilakukan secara lebih efektif dan efisien, karena proses-proses dan hubungan antar komponen sistem telah terdefinisi dengan baik. Berikut merupakan penjelasan DFD terkait dengan Sistem Informasi MBKM Pada Fakultas Ilmu Komputer UPN “Veteran” Jakarta.

**2.2.1** **_Diagram Context_**

<!-- Start of picture text -->
fs 2<br>baie &2F<br>B52 E5555<br>BEEZE EEEES<br>Dosen Pembimbing sEEeefeb cegazegigeg<br>€ 346<br>4 i<br>Data Keiatan olla Kept<br>‘Bimbingan € ‘Data Pendaftarar<br>Seleksi Pend<br>Pengaivan SR- . j <Aeimbingan<br>Data tengetota Data Keoiatar<br>Pendatara Kegiatar SistemMBKM InformasiFIK Info-VerifikasiPengaivanKegiatar<br>Daftar Uang UPN "Veteran" Jakarta SR<br>Manasiswa etka PengahianSR.<br>nfo Dosen Pembibing Data Pendataran<br>Bimtingan Seleks Pendaftaran<br>‘Pelaporan- ‘Info Daftar ulang’<br>2 Seleksi<br>Dosen Pembimbing<br>£3£ &2 Detail LaraBimbingan<br>ZG2282 58<br>S328 83<br>2/33 2¢<br>BE]<br><!-- End of picture text -->

Gambar 2.2 _Diagram Context_

Gambar 2.2 diatas merupakan _Diagram Context_ untuk Sistem Informasi MBKM Fakultas Ilmu Komputer UPN "Veteran" Jakarta, yang menggambarkan aliran data antara sistem dengan berbagai entitas terkait. Entitas tersebut meliputi Mahasiswa, Kaprodi, PIC MBKM, Admin, Dosen Pembimbing, dan Mitra, yang masing-masing memiliki peran penting dalam proses pelaksanaan MBKM. Mahasiswa dapat melakukan pengajuan Surat Rekomendasi, pendaftaran, pendaftaran ulang, memilih dosen pembimbing, melakukan bimbingan, serta upload laporan kegiatan. Kaprodi bertanggungjawab dalam memverifikasi pengajuan SR, melakukan seleksi mitra, memvalidasi seleksi pendaftaran, mengelola kegiatan, seleksi dosen pembimbing, memonitor bimbingan, dan memeriksa laporan mahasiswa.

PIC MBKM bertanggung jawab dalam melakukan seleksi mitra, mengelola data kegiatan, seleksi pendaftaran MBKM, seleksi dosen pembimbing, memonitor bimbingan, dan mengecek laporan kegiatan. Admin berperan dalam melakukan seleksi mitra, mengelola data kegiatan, dan memverifikasi pengajuan SR. Dosen Pembimbing bertanggung jawab pada memberikan kepada bimbingan mahasiswa serta memeriksa laporan kegiatan mereka. Sementara itu, Mitra berperan dalam melakukan registrasi untuk melakukan kerjasama dengan Fakultas Ilmu Komputer UPN “Veteran” Jakarta, mengelola data kegiatan, menerima data pendaftaran mahasiswa, dan melakukan seleksi mitra. Sistem Informasi MBKM menjadi pusat koordinasi yang mengintegrasikan aliran data dari berbagai pihak untuk memastikan kelancaran pelaksanaan kegiatan MBKM. Diagram ini mencerminkan interaksi yang kompleks namun terstruktur antara aktor-aktor tersebut, mendukung proses administrasi dan pelaporan secara efektif.

# **2.2.2** **_Diagram Overview_**

<!-- Start of picture text -->
ee_ — =|<br>a —— TI Te .<br>TS eb<br>| eel ~<br>=o © i-—a— ——<br><!-- End of picture text -->

Gambar 2.3 _Diagram Overview_

Gambar 2.3 adalah _Diagram Overview_ yang menggambarkan alur data dalam sistem informasi yang melibatkan beberapa entitas, yaitu Mahasiswa, Kaprodi, PIC MBKM, Admin, Dosen Pembimbing, dan Mitra. Sistem dimulai dengan proses login (Proses 1), di mana setiap entitas mengakses sistem dengan otentikasi. Setelah berhasil login, masing-masing entitas memiliki fungsi spesifik. Mahasiswa dapat melihat informasi kegiatan, mengajukan surat rekomendasi (Proses 6), mendaftar kegiatan MBKM (Proses 9), melakukan daftar ulang, dan mengunggah laporan bimbingan serta laporan kegiatan (Proses 15). Data yang dimasukkan oleh Mahasiswa akan diteruskan ke proses-proses berikutnya untuk divalidasi oleh pihak yang berwenang, seperti Kaprodi atau PIC MBKM.

Kaprodi dan PIC MBKM memiliki peran penting dalam memastikan kelancaran proses administrasi. Mereka dapat meninjau dan menyetujui pengajuan surat rekomendasi, memilih Dosen Pembimbing (Proses 10), serta memantau laporan bimbingan Mahasiswa (Proses 11). Selain itu, Mitra juga memiliki akses untuk melihat data pendaftaran Mahasiswa, menyetujui pendaftaran, dan memberikan masukan terkait kegiatan. Admin mendukung sistem dengan mengelola data kegiatan, termasuk menambah, mengedit, dan menghapus informasi. Semua alur data ini saling terhubung, sehingga memungkinkan koordinasi yang efisien antara entitas yang terlibat.

Sistem ini dirancang untuk mengintegrasikan berbagai proses dalam kegiatan MBKM, mulai dari pengajuan surat rekomendasi, pendaftaran, hingga pelaporan. Setiap proses memiliki alur data yang jelas dan memastikan setiap aktor dapat melaksanakan tugasnya dengan baik. Diagram ini menunjukkan kompleksitas hubungan antar entitas dan proses yang dikelola melalui alur data yang terorganisir. Dengan memanfaatkan sistem ini, kolaborasi antar entitas dapat berjalan lancar dan transparansi data dapat terjaga untuk mendukung kelancaran kegiatan MBKM secara keseluruhan.

# **2.2.3 DFD Level 2 Login**

<!-- Start of picture text -->
‘data login<br>PIC MBKM isemmame & passwor¢-—> > User<br>data login<br>1.2 Validasi Data<br>Dosen Pembimbing sername & password<br>konfirmasi. login’ 1.3 KonfirmasiData ‘onfirmasi login<br><!-- End of picture text -->

Gambar 2.4 DFD Level 2 Login

Gambar 2.4 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses login pada Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana setiap entitas pengguna sistem seperti Mahasiswa, Kaprodi, PIC MBKM, Mitra, Admin, dan Dosen Pembimbing, dapat melakukan autentikasi untuk mengakses sistem menggunakan _username_ dan _password_ .

Proses dimulai dari entitas pengguna yang mengirimkan _username_ dan _password_ ke proses 1.1 Login. Data login yang diterima kemudian diteruskan ke proses 1.2 Validasi Data, sistem akan memeriksa keabsahan username dan password yang dikirimkan. Jika data login valid, sistem akan mengirimkan data pengguna ke entitas yang sesuai seperti Mahasiswa, Kaprodi, PIC MBKM, Admin, Dosen Pembimbing, dan Mitra sehingga mereka dapat mengakses fitur yang relevan sesuai dengan peran mereka di sistem. Setelah validasi selesai, proses 1.3 Konfirmasi Data memastikan bahwa login berhasil, dan sistem memberikan umpan balik ke pengguna terkait status autentikasi mereka.

# **2.2.4 DFD Level 2 Registrasi Mitra**

<!-- Start of picture text -->
registrasi. 2.1 Melakukan<br>Registrasi Mitra<br>data registrasi<br>Registrasi Mitra<br>data registrasi<br>2 Menampilkan<br>data registrasi data registrasi Admin<br>Mitra<br><!-- End of picture text -->

Gambar 2.5 DFD Level 2 Registrasi Mitra

Gambar 2.5 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses registrasi mitra dalam Sistem Informasi MBKM. Proses ini dimulai ketika Mitra melakukan registrasi ke dalam proses 2.1 yaitu Melakukan Registrasi Mitra. Data registrasi ini kemudian disimpan dalam _database_ Registrasi Mitra, yang berfungsi sebagai pusat penyimpanan data terkait mitra yang telah terdaftar. Kemudian pada proses 2.2 yaitu Menampilkan data registrasi Mitra, data yang sudah diajukan oleh Mitra akan ditampilkan di sistem Admin. Admin memiliki wewenang dalam memproses data registrasi yang telah dilakukan mitra yaitu melakukan seleksi.

Diagram ini menggambarkan alur data yang sistematis dalam proses registrasi mitra. Data registrasi mitra yang diterima dikelola dalam sistem untuk kemudian diseleksi oleh Admin. Hal ini memastikan bahwa informasi yang disampaikan oleh mitra dapat diakses secara tepat guna mendukung proses administrasi, pengawasan, dan pengambilan keputusan terkait kerja sama MBKM.

# **2.2.5 DFD Level 2 Seleksi Mitra**

<!-- Start of picture text -->
info verifikasi<br>‘data hasil<br>3.4 Validasi<br>registrasi<br>3.3 Cek<br>kelengkapan<br>data registrasi- data<br>3.2 Melakukan<br>seleksi<br>registrasi Mitra,<br>data registrasi<br>34<br>Menampilkan<br>Mitra<br><!-- End of picture text -->

Gambar 2.6 DFD Level 2 Seleksi Mitra

Gambar 2.6 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses seleksi mitra dalam Sistem Informasi MBKM. Proses ini dimulai ketika Mitra mengirimkan data registrasi ke dalam proses 3.1 Menampilkan data registrasi Mitra, sistem menampilkan data registrasi Mitra ke dalam sistem admin untuk melakukan registrasi. Pada proses 3.2 Melakukan Seleksi Registrasi Mitra. Data registrasi ini kemudian diterima oleh entitas Registrasi Mitra, yang berfungsi sebagai pusat penyimpanan data pendaftaran mitra yang akan diproses lebih lanjut.

Selanjutnya, data registrasi ini diteruskan ke pihak-pihak yang berwenang yaitu Admin untuk memverifikasi kelayakan kerja sama dengan mitra.. Setelah dilakukan seleksi, data diteruskan ke proses 3.3 Cek Kelengkapan Data untuk memastikan semua dokumen dan informasi telah terpenuhi.

Setelah kelengkapan data terverifikasi, proses dilanjutkan ke tahap 3.3 Validasi Registrasi untuk memastikan data yang diajukan valid dan sesuai dengan ketentuan. Hasil validasi berupa informasi verifikasi akan di infokan oleh Admin kepada Mitra melalui _whatsapp_ . Diagram ini menggambarkan alur data yang sistematis dan terstruktur, memastikan bahwa setiap tahap dalam proses registrasi mitra dilakukan dengan efisien dan terintegrasi untuk mendukung pelaksanaan program MBKM.

**2.2.6 DFD Level 2 Mengelola Data Kegiatan**

<!-- Start of picture text -->
pe | saankegsn<br>Kaprodi ‘detail kegiatan-<br>4.1 Mengelola -<br>data kegiatan data kegiatan<br>detail kegiatan<br>PIC MBKM detail kegiatan Dosen<br>Pembimbing<br>Kegiatan MBKM<br>Admin detail kegiatan-<br>data kegiatan<br>data kegiatan-. 4.2data Menampilan egiatan data kegiatan’<br><!-- End of picture text -->

Gambar 2.7 DFD Level 2 Mengelola Data Kegiatan

Gambar 2.7 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pengelolaan data kegiatan dalam Sistem Informasi MBKM. Proses ini dimulai dengan penginputan data yang dilakukan oleh Mitra kemudian diproses dalam tahap 4.1 Mengelola Data Kegiatan oleh Kaprodi, PIC MBKM, dan Admin. Detail kegiatan yang diterima selanjutnya disimpan dalam _database_ Kegiatan MBKM, yang berfungsi sebagai pusat penyimpanan data terkait kegiatan yang dikelola dalam sistem.

Data kegiatan yang telah diseleksi pada tahap tersebut dapat diakses dan ditampilakan oleh berbagai pihak seperti Mahasiswa dan Dosen Pembimbing, melalui tahap 4.2 Menampilkan Data Kegiatan. Pada tahap ini, data kegiatan ditampilkan sesuai dengan kebutuhan pengguna, baik untuk tujuan pemantauan, pelaporan, maupun pelaksanaan program MBKM.

# **2.2.7 DFD Level 2 Pengajuan Surat Rekomendasi**

<!-- Start of picture text -->
detail pengajuan.. Surat<br>Mahasiswa 5.1 Mengajukan<br>Rekomendasi<br>data pengajuan<br>5.2 Menampilkan<br>Data Pengajuan<br>‘Surat<br>Rekomendasi<br>data pengajuan<br>PIC MBKM data pengajuan—_——_ Surat Rekomendasi __data pengajua Kaprodi<br>MBKM<br>——<br>data pengajuan<br><!-- End of picture text -->

Gambar 2.8 DFD Level 2 Pengajuan Surat Rekomendasi

Gambar 2.8 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pengajuan surat rekomendasi dalam Sistem Informasi MBKM. Proses ini dimulai dengan Mahasiswa yang melakukan pengajuan surat rekomendasi ke tahap 5.1 Mengajukan Surat Rekomendasi. Data pengajuan tersebut kemudian disimpan dalam _database_ Surat Rekomendasi MBKM, yang berfungsi sebagai pusat penyimpanan informasi terkait pengajuan surat rekomendasi. Kemudian pada proses 5.2 Menampilkan Data Pengajuan Surat Rekomendasi. Data pengajuan ini diteruskan ke pihak-pihak terkait yaitu PIC MBKM, Kaprodi, dan Admin. Semua data pengajuan ini dikelola secara terpusat melalui _database_ Pengajuan SR untuk memastikan kelancaran proses pengajuan surat rekomendasi.

# **2.2.8 DFD Level 2 Seleksi Surat Rekomendasi**

<!-- Start of picture text -->
infoinfo venliverifi k : as 6.3 Validasi; <— data hasi<br>pengajuan surat<br>6.2 Cek<br>kelengkapan<br>data pengajua ‘surat<br>‘6.1 Menyeleksi<br>surat<br>rekomendasi /*<br>data pengajuan<br>data pengajuan<br>data pengajuan<br>Pic mek hain Pro<br>data pengajuan data pengajuan data pengajuan<br>Surat Rekomendasi<br>MBKM<br><!-- End of picture text -->

Gambar 2.9 DFD Level 2 Seleksi Surat Rekomendasi

Gambar 2.9 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses seleksi dan validasi surat rekomendasi dalam Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana alur data berjalan antara entitas pengguna (Mahasiswa, PIC MBKM, Admin, dan Kaprodi) dan prosesproses yang terlibat dalam pengajuan serta validasi surat rekomendasi.

Proses dimulai dari entitas Mahasiswa yang mengirimkan data pengajuan surat rekomendasi. Data tersebut kemudian masuk ke proses 6.1 Menyeleksi Surat Rekomendasi, yang berfungsi untuk melakukan seleksi awal terhadap surat yang diajukan. Proses ini melibatkan tiga pihak utama, yaitu PIC MBKM, Admin, dan Kaprodi, yang masing-masing memberikan data pengajuan sesuai dengan perannya dalam sistem.

Setelah seleksi surat rekomendasi selesai, data pengajuan diteruskan ke proses 6.2 Cek Kelengkapan Surat, di mana sistem memeriksa apakah semua persyaratan dan dokumen pendukung telah lengkap. Jika dokumen dianggap lengkap, proses dilanjutkan ke 6.3 Validasi Pengajuan Surat, yang memastikan bahwa surat tersebut memenuhi standar yang ditetapkan. Hasil validasi ini kemudian dikembalikan ke entitas Mahasiswa sebagai informasi terkait status pengajuan mereka.

Diagram ini menggambarkan alur kerja yang sistematis dalam pengelolaan pengajuan surat rekomendasi, mulai dari proses seleksi hingga validasi akhir yang bertujuan untuk memastikan bahwa setiap surat yang diajukan memenuhi kriteria dan persyaratan yang berlaku di Sistem Informasi MBKM.

# **2.2.9 DFD Level 2 Pendaftaran MBKM Mandiri Kerjasama**

<!-- Start of picture text -->
7.2 Validasi<br>Data<br>detail pendaftaran MBKM<br>detailPelpendaftaran MBKM 7.1 Melakukan\ detail pendaftaran MBKM<br>pendaftaran<br>MBKM<br>7.3 Menyimpan<br>Data detail pendaftaran MBKM<br>MBKM Enroliment<br>data pendaftaran MBKM<br>“mesamenues<br>Pendaftaran<br>[mf — a 74<br>data pendaftaran MBKM<br>PIC MBKM<br><!-- End of picture text -->

Gambar 2.10 DFD Level 2 Pendaftaran MBKM Mandiri Kerjasama

Gambar 2.10 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pendaftaran MBKM dalam Sistem Informasi MBKM. Proses ini dimulai ketika mahasiswa melakukan pendaftaran MBKM melalui proses 7.1 yaitu melakukan pendaftaran MBKM. Data yang dikirimkan mahasiswa kemudian melewati proses 7.2 yaitu Validasi Data, dimana sistem memverifikasi kelengkapan dan kebenaran data pendaftaran yang telah diinput oleh mahasiswa. Setelah data tervalidasi, proses 7.3 Menyimpan Data dilakukan untuk menyimpan data pendaftaran tersebut ke dalam _database_ MBKM _Enrollment_ sebagai pusat penyimpanan informasi terkait pendaftaran. Kemudian proses 7.4 Menampilkan Data Pendaftaran dari Mahasiswa yang telah melakukan pendaftaran MBKM Mandiri Kerjasama sistem Kaprodi, PIC MBKM, dan Mitra, Data yang tersimpan dalam _database_ pendaftaran MBKM selanjutnya dapat diakses oleh beberapa pihak yang berwenang seperti Mitra, Kaprodi, dan PIC MBKM. Mitra menerima data ini untuk melakukan seleksi sesuai dengan ketentuan dari program yang ditawarkan. Kaprodi dapat menggunakan data ini untuk memverifikasi dan memberikan persetujuan atas pendaftaran mahasiswa. Sementara itu, PIC MBKM menggunakan data ini untuk memantau dan mengelola proses pendaftaran secara keseluruhan.

# **2.2.10 DFD Level 2 Seleksi Pendaftaran MBKM Mandiri Kerjasama**

Gambar 2.11 DFD Level 2 Seleksi MBKM Mandiri Kerjasama

Gambar 2.11 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses seleksi dan validasi pendaftaran MBKM dalam Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana alur data berjalan antara entitas pengguna (Kaprodi, PIC MBKM, Mitra, dan Mahasiswa) dan prosesproses yang terlibat dalam pendaftaran serta seleksi program MBKM.

Proses dimulai dari entitas Kaprodi, PIC MBKM, dan Mitra yang mengirimkan data pendaftaran MBKM. Data tersebut kemudian masuk ke proses 8.1 Menampilkan Data Pendaftaran dari Data Mahasiswa yang telah melakukan pendaftaran ke dalam sistem Kaprodi, PIC MBKM, dan Mitra untuk di seleksi. Kemudian pada proses 8.2 Menyeleksi Pendaftaran MBKM, yang berfungsi untuk melakukan seleksi awal terhadap data pendaftaran yang diajukan. Dalam proses ini, ketiga pihak tersebut memberikan data sesuai dengan perannya dalam sistem.

Setelah seleksi pendaftaran selesai, data diteruskan ke proses 8.3 Validasi Data, dimana sistem memeriksa apakah data pendaftaran yang diajukan memenuhi persyaratan yang telah ditentukan. Jika data dianggap valid, proses dilanjutkan ke 8.4 Menampilkan Hasil Seleksi yaitu untuk memberikan hasil seleksi kepada entitas Mahasiswa sebagai informasi terkait status pendaftaran mahasiswa.

Diagram ini menggambarkan alur kerja yang sistematis dalam pengelolaan pendaftaran program MBKM, mulai dari proses seleksi hingga validasi dan penampilan hasil, untuk memastikan bahwa setiap data pendaftaran yang diajukan sesuai dengan kriteria yang berlaku di Sistem Informasi MBKM.

# **2.2.11 DFD Level 2 Pendaftaran Ulang**

<!-- Start of picture text -->
Mahasiswa —|—detal pendataran—o{ 9.11HelaninanMelakukan | tandetail Kelengkapan9.2DataCek<br>detail pendattaran<br>MBKM 9.3 Menyimpan<br>Participants“ #etat pendaaran—| “pata data<br><!-- End of picture text -->

Gambar 2.12 DFD Level 2 Pendaftaran Ulang

Gambar 2.12 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan alur proses pendaftaran ulang oleh mahasiswa dalam sistem informasi MBKM. Diagram ini menunjukkan bagaimana data pendaftaran ulang dikelola melalui beberapa proses utama untuk memastikan kelengkapan dan penyimpanan data.

Proses dimulai dari entitas Mahasiswa yang mengirimkan detail pendaftaran ulang ke sistem. Data tersebut masuk ke proses 9.1 Melakukan Daftar Ulang, yang berfungsi untuk mengelola pengisian data pendaftaran ulang oleh mahasiswa. Setelah itu, data yang diisi diteruskan ke proses 9.2 Cek Kelengkapan Data untuk memastikan bahwa seluruh data yang diperlukan telah terisi dan sesuai dengan persyaratan.

Apabila data dinyatakan lengkap, proses selanjutnya adalah 9.3 Menyimpan Data-data, di mana detail pendaftaran yang telah diverifikasi akan disimpan ke dalam sistem. Hasil penyimpanan ini kemudian dikembalikan ke entitas pendaftaran ulang sebagai data yang telah berhasil disimpan.

Diagram ini menunjukkan alur kerja sistematis dalam pengelolaan data pendaftaran ulang, mulai dari pengisian hingga penyimpanan, untuk memastikan bahwa seluruh data mahasiswa dikelola dengan baik dan terverifikasi dalam sistem MBKM.

# **2.2.12 DFD Level 2 Seleksi Dosen Pembimbing**

<!-- Start of picture text -->
[ meee} doeeating<br>Fivot Pembimbing .<br>Fembimbing gata dos<br>a ho.2 menyimpan 104<br>MBKM 4101 Memiin Data Dosen Ienampikan List<br>Participants ——éslamahasiowa—> Dosen ‘nfo dosen—>\Pembimbing Dosen<br>er" 9 Pembimbing<br>data dosen<br>Pic MBKM ata dosen<br>data dosen<br>10,3 Vaidasi<br>Kaprodi Data Dosen<br>" Pembimbing<br><!-- End of picture text -->

Gambar 2.13 DFD Level 2 Seleksi Dosen Pembimbing

Gambar 2.13 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses seleksi dosen pembimbing pada Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana entitas seperti Mahasiswa, Dosen Pembimbing, PIC MBKM, dan Kaprodi berinteraksi dengan sistem untuk memilih dan memvalidasi dosen pembimbing.

Proses dimulai ketika Mahasiswa melakukan pendaftaran ulang yang kemudian dikirimkan ke proses 10.1 Memilih Dosen Pembimbing. Dalam proses ini, data dosen yang diperoleh dari Dosen Pembimbing, PIC MBKM, dan Kaprodi akan diproses untuk menentukan dosen pembimbing yang sesuai. Hasil dari proses ini berupa informasi dosen pembimbing yang akan diteruskan kembali kepada Mahasiswa.

Setelah dosen pembimbing dipilih, sistem akan meneruskan informasi tersebut ke proses 10.2 Menyimpan Data Dosen Pembimbing. Data ini kemudian dikirim ke proses 10.3 Validasi Data Dosen Pembimbing, di mana sistem memeriksa kelengkapan dan keabsahan data dosen pembimbing. Jika data telah divalidasi, proses 10.4 Menampilkan List Dosen Pembimbing akan menyediakan daftar dosen pembimbing yang dapat diakses oleh Mahasiswa atau entitas terkait.

Diagram ini menjelaskan bagaimana alur data dirancang untuk memastikan proses seleksi dosen pembimbing berjalan dengan baik. Setiap langkah, mulai dari pemilihan hingga validasi dan penyimpanan data, dirancang untuk mendukung efisiensi dan akurasi dalam sistem, serta memastikan data dapat digunakan dengan benar oleh pihak yang berkepentingan.

# **2.2.13 DFD Level 2 Jadwal Bimbingan**

<!-- Start of picture text -->
11.2 Monitor<br>Jadwal Bimbingan<br>MBKM<br>11.1 Membuat ta bimbi Dosen<br>jadwal Bimbingan/ gata bimbingarr Pembimbing<br><!-- End of picture text -->

Gambar 2.14 DFD Level 2 Jadwal Bimbingan

Gambar 2.14 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses bimbingan dalam Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana entitas seperti Kaprodi, PIC MBKM, dan Dosen

Pembimbing berinteraksi dengan sistem untuk membuat jadwal dan memantau bimbingan.

Proses dimulai ketika Dosen Pembimbing membuat jadwal bimbingan yang kemudian dikirimkan ke proses 11.1 Membuat Jadwal Bimbingan. Dalam proses ini, data bimbingan diolah untuk membuat jadwal yang sesuai, dan hasilnya akan diteruskan ke dalam proses 11.2 Monitor Bimbingan. Proses monitoring ini berfungsi untuk memastikan pelaksanaan bimbingan berjalan sesuai jadwal yang telah dibuat.

Selanjutnya, data bimbingan yang telah dimonitor akan diteruskan ke Kaprodi dan PIC MBKM untuk dilakukan evaluasi atau tindakan lebih lanjut jika diperlukan. Kedua entitas ini menerima data bimbingan untuk memastikan kelancaran pelaksanaan bimbingan dan memberikan catatan. Diagram ini menjelaskan bagaimana alur data dalam proses bimbingan dirancang untuk memastikan pelaksanaan bimbingan berjalan secara efisien dan terpantau dengan baik.

# **2.2.14 DFD Level 2 Mengisi** **_Form_ Bimbingan**

<!-- Start of picture text -->
-<br>[ meses sneneen 12.1 Melakukan!<br>detail bimbingan<br>Kehadiran Bimbingan < . 12.2 Validasi<br>MBKM ‘detail bimbingan’ bimbingan<br><!-- End of picture text -->

Gambar 2.15 DFD Level 2 Mengisi Form Bimbingan

Gambar 2.15 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pelaksanaan bimbingan pada Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana Mahasiswa dan entitas Bimbingan berinteraksi dalam sistem untuk melaksanakan dan memvalidasi kegiatan bimbingan.

Proses dimulai ketika Mahasiswa mengisi _form_ bimbingan yang kemudian dikirimkan ke proses 12.1 Melakukan Bimbingan. Dalam proses ini, detail bimbingan yang diberikan Mahasiswa akan dikelola oleh sistem untuk memastikan bahwa bimbingan dapat berjalan dengan baik.

Setelah proses bimbingan selesai dilakukan, detail bimbingan tersebut diteruskan ke proses 12.2 Validasi Bimbingan. Pada tahap ini, sistem memeriksa dan memvalidasi data yang telah diinput untuk memastikan kebenaran dan kelengkapan data bimbingan. Hasil dari proses validasi ini akan disimpan dalam entitas Bimbingan untuk keperluan pencatatan dan pelaporan.

Diagram ini menjelaskan bagaimana alur data dirancang untuk mendukung pelaksanaan dan validasi bimbingan secara efisien. Setiap langkah dalam proses ini dirancang untuk memastikan bahwa kegiatan bimbingan dapat dilakukan dengan lancar, data yang dihasilkan akurat, dan seluruh informasi tercatat dengan baik dalam sistem.

# **2.2.15 DFD Level 2 Catatan Bimbingan**

<!-- Start of picture text -->
Sima 13.1 Melakukan’<br>_Simbingan WEN—data bimbingan->{ pengecekanbimbingan<br>data bimbingan<br>Dosen data bimbis 13.2 Validasi<br>Pembimbing “oa bimbingan<br>data bimbingan<br>13.3<br>Menampilkan — 7<br>rin “me<br>Bimbingan<br>data bimbingar PIC MBKM<br><!-- End of picture text -->

Gambar 2.16 DFD Level 2 Catatan Bimbingan

Gambar 2.16 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses memberikan catatan bimbingan untuk mahasiswa pada Sistem Informasi MBKM. Diagram ini menunjukkan alur data yang terjadi dalam proses pengecekan, validasi, hingga memberikan catatan dari bimbingan yang telah dilakukan.

Proses dimulai dari proses 13.1 Melakukan Pengecekan Bimbingan, di mana data bimbingan diperiksa untuk memastikan kelengkapan atau kesesuaiannya. Setelah data diperiksa, proses dilanjutkan ke 13.2 Validasi Bimbingan, di mana validasi dilakukan untuk menentukan apakah data tersebut memenuhi kriteria yang telah ditentukan.

Setelah proses validasi selesai, data bimbingan diteruskan ke proses 13.3 catatan bimbingan. Dalam proses ini, dosen pembimbing memberikan catatan berdasarkan data yang telah divalidasi. Data bimbingan yang telah menerima catatan kemudian diteruskan ke Kaprodi dan PIC MBKM untuk melakukan monitor proses bimbingan.

Diagram ini menjelaskan bagaimana alur data dirancang untuk memastikan proses bimbingan berjalan dengan baik, mulai dari pengecekan hingga pemberian catatan. Proses ini penting untuk menjaga kualitas bimbingan dan memastikan semua pihak yang terlibat mendapatkan informasi yang diperlukan secara efisien.

# **2.2.16 DFD Level 2 Pelaporan Bulanan**

<!-- Start of picture text -->
4.1 Melakuka<br>Mahasiswa detail laporan bulanan- Pelaporan<br>Bulanan<br>detail laporan bulanan<br>14.2 Validasi<br>Monthly Report <—detail laporan bulanan- Laporan<br>—————_ Bulanan<br><!-- End of picture text -->

Gambar 2.17 DFD Level 2 Pelaporan Bulanan

Gambar 2.17 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pelaporan bulanan pada Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana mahasiswa melakukan pelaporan hingga proses validasi laporan oleh sistem.

Proses dimulai ketika mahasiswa input detail laporan bulanan ke dalam proses 14.1 Melakukan Pelaporan Bulanan. Data laporan bulanan yang dimasukkan kemudian dikirimkan ke proses 14.2 Validasi Laporan Bulanan, di mana sistem memeriksa apakah laporan tersebut sesuai dengan format dan ketentuan yang telah ditentukan. Setelah laporan divalidasi, detail laporan yang diterima akan disimpan ke dalam _database Monthly Report_ untuk dikirimkan ke sistem mahasiswa.

Diagram ini menjelaskan bagaimana alur data dalam proses pelaporan bulanan dirancang untuk memastikan laporan yang dibuat oleh mahasiswa dapat diterima dan diproses dengan baik. Proses ini penting untuk menjaga kelengkapan dan validitas data laporan bulanan yang diterima oleh sistem.

# **2.2.17 DFD Level 2 Pengecekan Pelaporan Bulanan**

<!-- Start of picture text -->
——“— 5.1 Melakukal<br>Monthly Pengecekan<br>Bulanan<br>_—_—__ Report —data laporan bulanar- Laporan<br>data laporan bulanan<br>pense 9 data laporan bulanan- 15.2Laporan Validasi<br>Bulanan<br>data laporan bulanan<br>| 15.3<br>Manampilkan<br>Monthly Report. —data laporan bulana Data data laporan bulanan- Kaprodi<br>—________ Laporan<br>Bulanan<br>data laporan bulanan<br>PIC MBKM<br><!-- End of picture text -->

Gambar 2.18 DFD Level 2 Pengecekan Pelaporan Bulanan

Gambar 2.18 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pengecekan dan validasi laporan bulanan pada Sistem Informasi MBKM. Diagram ini menunjukkan alur data dari proses pengecekan laporan hingga validasi oleh pihak-pihak terkait.

Proses dimulai dari _database Monthly Report_ yang mengirimkan data laporan bulanan mahasiswa ke proses 15.1 Melakukan Pengecekan Laporan Bulanan. Pada tahap ini, data laporan diperiksa untuk memastikan kelengkapan dan kesesuaiannya dengan _form_ . Setelah proses pengecekan selesai, data laporan diteruskan ke proses 15.2 Validasi Laporan Bulanan.

Diagram ini menjelaskan bagaimana alur data dirancang untuk memastikan proses pengecekan dan validasi laporan dapat berjalan secara terstruktur dan melibatkan pihak-pihak yang berkepentingan. Proses ini penting untuk menjaga akurasi data laporan dan mendukung pengambilan keputusan yang tepat.

# **2.2.18 DFD Level 2 Pelaporan Akhir**

<!-- Start of picture text -->
detail laporan akhir 16.1 Melakukan<br>Pelaporan Akhir,<br>detail laporan akhir<br>Final Report <—detail laporan akhir-- 16.2 Validasi<br><!-- End of picture text -->

Gambar 2.19 DFD Level 2 Pelaporan Akhir

Gambar 2.19 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pelaporan akhir pada Sistem Informasi MBKM. Diagram ini menunjukkan bagaimana mahasiswa melakukan pelaporan hingga proses validasi laporan oleh sistem.

Proses dimulai ketika mahasiswa input detail laporan bulanan ke dalam proses 16.1 Melakukan Pelaporan Akhir. Data laporan akhir yang dimasukkan kemudian dikirimkan ke proses 16.2 Validasi Laporan Akhir, di mana sistem memeriksa apakah laporan tersebut sesuai dengan format dan ketentuan yang telah ditentukan. Setelah laporan divalidasi, detail laporan yang diterima akan disimpan ke dalam _database Final Report_ untuk dikirimkan ke sistem mahasiswa.

Diagram ini menjelaskan bagaimana alur data dalam proses pelaporan akhir dirancang untuk memastikan laporan yang dibuat oleh mahasiswa dapat diterima dan diproses dengan baik. Proses ini penting untuk menjaga kelengkapan dan validitas data laporan akhir yang diterima oleh sistem.

# **2.2.19 DFD Level 2 Pengecekan Pelaporan Akhir**

<!-- Start of picture text -->
17.1 Melakukan’<br>Monthly Report ——data laporan akhir- Pengecekan<br>Laporan Akhir<br>data laporan akhir<br>Dosen data laporan akhir: 17.2 Validasi<br>Pembimbing ape Laporan Akh<br>data laporan akhir<br>| 17.3<br>Manampilkan<br>Final Report +——data laporan akhir- Data data laporan akhir- Kaprodi<br>Laporan<br>Akhir<br>data laporan akhir<br>PIC MBKM<br><!-- End of picture text -->

Gambar 2.20 DFD Level 2 Pengecekan Pelaporan

Gambar 2.20 di atas adalah _Data Flow Diagram_ (DFD) Level 2 yang menggambarkan proses pengecekan dan validasi laporan akhir pada Sistem Informasi MBKM. Diagram ini menunjukkan alur data dari proses pengecekan laporan hingga validasi oleh pihak-pihak terkait.

Proses dimulai dari _database Final Report_ yang mengirimkan data laporan akhir mahasiswa ke proses 17.1 Melakukan Pengecekan Laporan Akhir. Pada tahap ini, data laporan akhir diperiksa untuk memastikan kelengkapan dan kesesuaiannya dengan _form_ . Setelah proses pengecekan selesai, data laporan diteruskan ke proses 17.2 Validasi Laporan Akhir.

Diagram ini menjelaskan bagaimana alur data dirancang untuk memastikan proses pengecekan dan validasi laporan dapat berjalan secara terstruktur dan melibatkan pihak-pihak yang berkepentingan. Proses ini penting untuk menjaga akurasi data laporan dan mendukung pengambilan keputusan yang tepat.

# **2.3 Rancangan Proyek**

Pada tahap rancangan proyek akan menjelaskan tentang bagaimana kebutuhan analisis dari sistem yang akan diusulkan. Rancangan proyek mencakup _need analysis_ pada _User Interface (UI)_ dan _User Experience_ serta _design dari user interface_ . Tahap ini bertujuan untuk memastikan bahwa rancangan sistem dapat memenuhi kebutuhan pengguna sehingga memudahkan pengembang dalam tahap implementasi dan memastikan bahwa rancangan tersebut sesuai dengan kebutuhan pengguna. Penjelasan terkait rancangan proyek akan dijelaskan pada penjelasan berikut.

# **2.3.1** **_Need Analysis User Interface_ (UI) MBKM**

Bagian ini berfokus pada kebutuhan dari tampilan antarmuka yang akan digunakan dalam sistem MBKM. Analisis ini bertujuan untuk memastikan bahwa desain antarmuka mampu memenuhi kebutuhan pengguna dengan tampilan yang menarik dan mudah dipahami. Adapun komponen yang dibutuhkan akan dijelaskan pada tabel berikut.

Tabel 2.1 _Need Analysis_ pada _User Interface_ MBKM

|**Komponen****_User_**<br>**_Interface_**|**Fungsi**|**Desain yang**<br>**dibutuhkan**|**Contoh**<br>**Implementasi**|
|---|---|---|---|
|Dashboard|Menampilkan|Grafik_pie chart,_|Halaman<br>awal|
|MBKM (Layout)|ringkasan|diagram<br>batang,|yang menampilkan|
||informasi||informasi<br>secara|

||mengenai|pengumuman,|ringkas<br>kepada|
|---|---|---|---|
||MBKM.|_card_testimoni.|pengguna dengan<br>menyajikan<br>berbagai<br>komponen<br>yang<br>mudah diakses dan<br>dipahami.|
|Formulir (Form)|Mengumpulkan<br>data<br>dari<br>pengguna,|Formulir dengan<br>field yang jelas,<br>label yang mudah|Formulir registrasi<br>mitra dengan input<br>teks untuk nama|
||seperti<br>data|dipahami,<br>dan|perusahaan, sektor|
||registrasi mitra,|tombol<br>simpan|perusahaan,|
||data pengajuan<br>surat<br>rekomendasi,<br>data<br>pendaftaran|yang<br>mudah<br>diakses.|website,<br>nama<br>_contact_<br>_person_,<br>_phone_<br>_number_<br>_contact_<br>_person_,<br>dan_email contact_|
||MBKM,<br>data||_person_.<br>Textarea|
||input kegiatan,<br>data<br>pendaftaran||untuk<br>alamat<br>kantor utama, dan<br>dropdown<br>untuk|
||ulang,<br>data<br>bimbingan, dan<br>data pelaporan.||prodi yang dituju.|
|Tombol (Button)|Membantu<br>pengguna dalam|Tombol<br>yang<br>cukup<br>besar,|Tombol<br>dengan<br>warna<br>kontras,|
||mengumpulkan|dengan<br>warna|seperti "Simpan",|
||data<br>seperti|yang<br>mencolok|“Batal”,<br>“Cari”,|
||mengirim data|untuk<br>menarik|dengan efek hover|
||atau|perhatian,<br>dan|untuk|
||mengeksekusi|ukuran<br>yang|menunjukkan|
||perintah.|konsisten<br>di<br>seluruh halaman.|interaktivitas.|

|Navigasi|Membantu|Menu<br>navigasi|Sidebar<br>yang|
|---|---|---|---|
||pengguna dalam<br>berpindah antar<br>halaman<br>atau|yang<br>mudah<br>diakses<br>dan<br>dipahami,<br>baik|berada di sisi kiri<br>dan berisi menu<br>dari sistem dengan|
||menu<br>dalam|secara<br>vertikal|ikon<br>dan<br>teks|
||sistem<br>dengan<br>mudah.|(sidebar)<br>atau<br>horizontal<br>(navbar).|deskriptif<br>serta<br>navbar<br>yang<br>berada diatas layar<br>pada<br>halaman<br>_landing page._|
|Feedback|Memberikan|Pesan yang jelas,|Pesan<br>"Berhasil"|
|Pengguna|umpan<br>balik<br>langsung<br>kepada|dengan ikon atau<br>warna<br>yang<br>membedakan|setelah mengirim<br>formulir<br>atau<br>pesan<br>"Terjadi|
||pengguna|jenis<br>feedback.|Kesalahan"<br>jika|
||tentang<br>tindakan<br>mereka, seperti<br>konfirmasi atau<br>pesan error.|Pesan<br>berhasil<br>berwarna<br>hijau<br>dan eror dengan<br>merah.|ada<br>kesalahan<br>input.|

Tabel 2.1 diatas memberikan panduan yang untuk mendesain dan mengimplementasikan komponen-komponen antarmuka pengguna dalam sistem. Panduan ini mencakup berbagai aspek, seperti fungsi utama masing-masing komponen, desain yang diperlukan untuk memenuhi kebutuhan pengguna, dan contoh implementasi yang memudahkan pemahaman tentang bagaimana komponen tersebut dapat digunakan secara efektif dalam aplikasi. Dengan panduan dari tabel ini, pengembang dapat merancang antarmuka yang intuitif dan mudah diakses oleh pengguna dengan memperhatikan detail dan konsistensi dalam setiap elemen desain.

# **2.3.2** **_Need Analysis User Experience_ (UX) MBKM**

Bagian ini berisi analisis kebutuhan pengalaman pengguna (UX) untuk sistem MBKM. Analisis ini bertujuan untuk memahami kebutuhan, dan tantangan yang dihadapi oleh pengguna dalam berinteraksi dengan sistem MBKM. Dengan melakukan analisis ini, pengembang dapat merancang antarmuka dan fungsionalitas yang lebih sesuai dengan preferensi pengguna, meningkatkan kenyamanan, dan memastikan bahwa setiap interaksi dalam sistem berjalan lancar. Fokus utama dari analisis ini adalah untuk memastikan bahwa sistem tidak hanya fungsional tetapi juga mudah digunakan oleh pengguna. Adapun komponen-komponen yang dibutuhkan dapat dilihat pada penjelasan berikut.

Tabel 2.2 _Need Analysis_ pada _User Experience_ MBKM

|**Komponen****_User_**<br>**_Experience_**|**Tujuan****_U_**<br>**_Experie_**|**_ser_**<br>**_nce_**|**Kebutuhan**<br>**Pengguna**|**Desain**<br>**Pengalaman**<br>**yang Diusulkan**|
|---|---|---|---|---|
|Navigasi|Memudahka<br>pengguna|n|Menu yang jelas<br>dan<br>mudah|_Sidebar_<br>dengan<br>ikon<br>deskriptif|
||berpindah|antar|diakses<br>serta|dan<br>navbar<br>di|
||halaman<br>bagian<br>sistem.|atau<br>dalam|jalur<br>navigasi<br>yang logis.|bagian atas untuk<br>navigasi<br>yang<br>mudah.|
|Kemudahan|Mempermu|dah|Fungsi pencarian|Input<br>pencarian|
|dalam<br>mencari|pengguna|untuk|yang cepat dan|yang<br>mudah|
|informasi|menemukan<br>informasi<br>dibutuhkan<br>kesulitan.|<br>yang<br>tanpa|efisien.<br>Filter<br>data<br>yang<br>responsif<br>dan<br>mudah<br>digunakan.|digunakan dengan<br>opsi filter untuk<br>mempercepat<br>pencarian.|
|Konsistensi|Membantu||Elemen<br>visual|Menggunakan|
|Desain|pengguna<br>memahami|dan|yang seragam di<br>seluruh aplikasi|palet warna dan<br>ikon<br>yang|
||beradaptasi||(warna,<br>ikon,<br>layout).|konsisten<br>di<br>seluruh halaman.|

||dengan<br>sistem<br>lebih cepat.|||
|---|---|---|---|
|Visualisasi Data|Mempermudah<br>pengguna<br>dalam|Grafik<br>yang<br>informatif<br>dan|Menggunakan<br>diagram<br>batang,|
||memahami<br>data|mudah dipahami.|_pie chart_untuk|
||yang disajikan.||menampilkan<br>data.|

Tabel 2.2 di atas memberikan gambaran yang jelas tentang komponenkomponen _User Experience_ yang harus diperhatikan dalam merancang sistem atau aplikasi. Setiap komponen berfokus pada kebutuhan pengguna dan tujuan pengalaman pengguna yang ingin dicapai, dengan desain pengalaman yang diusulkan yang dapat memastikan interaksi pengguna berjalan dengan lancer dan efisien. Dengan melakukan analisis, sistem dapat lebih mudah diakses, dipahami, dan digunakan oleh berbagai jenis pengguna, menciptakan pengalaman yang positif, dan meningkatkan kepuasan pengguna.

Selain itu, pada website MBKM setiap tampilan dan elemen desain dirancang dengan mempertimbangkan konteks penggunaan dan kebutuhan penggunanya. Pengguna dapat dengan mudah menavigasi antara halamanhalaman penting, seperti pendaftaran kegiatan, pelaporan, dan pengajuan surat rekomendasi. Tampilan yang intuitif dengan elemen-elemen yang terorganisir dengan baik akan membantu pengguna fokus pada tugas yang sedang dikerjakan tanpa adanya kebingungan. Implementasi desain yang baik pada website MBKM tidak hanya akan meningkatkan kenyamanan pengguna, tetapi juga memastikan bahwa semua informasi penting mudah diakses, meminimalkan langkah-langkah yang membingungkan, serta mempercepat pencapaian tujuan pengguna. Adapun kebutuhan dan fungsinya dari rancangan sistem MBKM akan dijelaskan sebagai berikut.

- 1) Pada bagian halaman _landing page_ , keseluruhan aktor dapat mengakses halaman ini untuk melihat informasi yang terdapat di dalam sistem berupa informasi kegiatan, panduan, _form registrasi_ Mitra, dan untuk _login_ ke dalam sistem.

- 2) Pada bagian _login,_ keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk masuk ke dalam sistem.

- 3) Pada bagian _dashboard general,_ keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk memilih menu MBKM dari ketiga menu yang terdapat di dalam sistem.

- 4) Pada bagian _dashboard_ MBKM, keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk melihat informasi yang terdapat di dalam sistem berupa mahasiswa prodi yang mengikutti MBKM dalam bentuk _pie chart,_ program MBKM yang paling diminati dalam bentuk diagram batang, tipe perusahaan paling banyak dalam bentuk diagram batang. Kemudian terdapat grafik penerimaan MBKM Flagship, MBKM Mandiri Kerjasama, MBKM Mandiri dalam bentuk _pie chart,_ grafik jumlah keseluruhan peserta MBKM. Selain itu, terdapat informasi umum dan testimoni.

- 5) Pada bagian seleksi Mitra, halaman ini hanya bisa diakses oleh Kaprodi, PIC MBKM, dan Admin dengan tujuan untuk melakukan seleksi terhadap Mitra yang telah melakukan registrasi untuk bekerjasama dengan FIK.

- 6) Pada bagian informasi kegiatan, keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk melihat informasi kegiatan yang tersedia. Untuk Kaprodi, PIC MBKM, Admin, dan Mitra dapat mengelola data kegiatan yaitu input, edit, delete data kegiatan di halaman ini. Selain itu, di halaman ini juga Kaprodi, PIC MBKM, Admin dapat melakukan _approve_ data kegiatan yang di input oleh Mitra.

- 7) Pada bagian pengajuan surat rekomendasi, hanya Mahasiswa yang dapat mengakses halaman ini dengan tujuan untuk melakukan pengajuan surat rekomendasi magang.

- 8) Pada bagian seleksi surat rekomendasi, halaman ini hanya bisa diakses oleh Kaprodi, PIC MBKM, dan Admin dengan tujuan untuk melakukan seleksi surat rekomendasi yang telah diajukan oleh Mahasiswa.

- 9) Pada bagian pendaftaran, halaman ini terdapat dua menu yang berisi pendaftaran MBKM Mandiri Kerjasama dan pendaftaran ulang. Pada halaman ini, bisa diakses oleh Kaprodi, PIC MBKM, dan Mitra. Untuk Mahasiswa, halaman ini bertujuan untuk melakukan pendaftaran MBKM Mandiri Kerjasama, untuk melihat status pendaftaran, dan untuk melakukan

pendaftaran ulang. Sedangkan Kaprodi, PIC MBKM, dan Mitra halaman ini bertujuan untuk melakukan seleksi pendaftaran MBKM Mandiri Kerjasama, melihat status seleksi, melakukan pengecekan daftar ulang, dan melakukan seleksi dosen pembimbing.

- 10) Pada bagian _approve_ PKS, halaman ini hanya dapat diakses oleh Admin dengan tujuan untuk melakukan _approve_ PKS yang telah di input oleh Mahasiswa ketika melakukan pendaftaran ulang.

- 11) Pada bagian bimbingan, halaman ini dapat diakses oleh Mahasiswa, Kaprodi, PIC MBKM, dan Dosen Pembimbing. Untuk Mahasiswa, halaman ini bertujuan untuk melakukan bimbingan. Sedangkan untuk Dosen Pembimbing, halaman ini bertujuan untuk membuat jadwal bimbingan, melakukan bimbingan, melakukan pengecekan bimbingan, dan memberikan catatan bimbingan kepada mahasiswa terkait dengan kendala yang dihadapi selama magang. Untuk Kaprodi dan PIC MBKM, halaman ini bertujuan untuk melakukan monitor dari bimbingan yang telah dilakukan oleh Mahasiswa dan Dosen Pembimbing.

- 12) Pada bagian halaman daftar mahasiswa, halaman ini dapat diakses oleh Kaprodi, PIC MBKM, Admin, Dosen Pembimbing, dan Mitra. Untuk Kaprodi dan PIC MBKM halaman ini bertujuan untuk menampilkan daftar mahasiswa yang diterima MBKM beserta dengan dosen pembimbing, untuk Admin halaman ini bertujuan untuk menampilkan daftar mahasiswa yang mengajukan surat rekomendasi, sedangkan untuk Dosen Pembimbing halaman ini bertujuan untuk menampilkan daftar mahasiswa yang dibimbing, dan untuk Mitra halaman ini bertujuan untuk menampilkan daftar mahasiswa yang melakukan pendaftaran MBKM Mandiri Kerjasama di Mitra yang bersangkutan.

- 13) Pada bagian _logout,_ keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk keluar dari sistem.

# **2.3.3 Design** **_User Interface_ (UI) MBKM**

Pada bagian ini akan menampilkan dan menjelaskan terkait dengan tampilan antarmuka yang dirancang dengan tujuan untuk memberikan gambaran terkait rancangan _user interface_ yang diusulkan. Rancangan ini dibuat berdasarkan _need analysis_ pada _user interface_ dan _user experience_ yang telah dijelaskan sebelumnya. Rancangan untuk tampilan _design user interface_ dapat dilihat pada gambar berikut.

# **2.3.3.1 Halaman** **_Landing Page_**

<!-- Start of picture text -->
nding Page ><br>=<br>| } |<br>Seles colon overt GOMASTHC2024 InternshipOpportuntyPTSorasuttech-WW. Opening Summercamp Exchange<br>a a a<br>Seles colon overt GOMASTIC2024 InternshipOpportunityPT Sorasuttech- UW. Opening Surmercamp Exchange<br>@(2) Fakultastimuun verenan saxarraKomputer vereka lor tempus erika student tchange Manajemen Falenta<br><!-- End of picture text -->

Gambar 2.21 _Landing Page_

Pada halaman _landing page,_ seluruh _user_ dapat mengakses halaman tersebut untuk melakukan _login_ ke dalam sistem. Untuk Mitra jika ingin melakukan kerjasama dengan FIK UPN “Veteran” Jakarta dapat mengakses menu MBKM yang berada di header _landing page._ Ketika header MBKM di klik maka akan menampilkan menu _form_ registrasi mitra. Mitra juga dapat melakukan registrasi

ketika mengakses halaman _login._ Jika mitra klik button _sign up,_ maka sistem akan mengarahkan mitra ke dalam halaman _form_ registrasi mitra.

# **2.3.3.2 Halaman Registrasi Mitra**

<!-- Start of picture text -->
i<br>Gy Fakultas IImu Komputer<br>=") UPN VETERAN JAKARTA.<br>Register<br>asuk<br>Sudah punya as aku?  Partner MBKM<br>Noma Perusahaan *<br>{_prasco<br>sektor Perusahaan *<br>{_totnetogormost<br>‘Alamat Kantor Utomo *<br>Website<br>{ww ptabedcam<br>Noma contact person * Phone Number contact person *<br>ee cerasseres0<br>{Email contact person * Tipe Perusahaan<br>chmamuzoki@gmaitcom | stort up<br>Password * Konfirmasi Password *<br>” my<br>vd th<br>| f- -<br><!-- End of picture text -->

Gambar 2.22 _Form_ Registrasi Mitra

Tampilan _form_ registrasi mitra bertujuan untuk membantu mitra dalam melakukan registrasi ketika ingin melakukan kerjasama dengan Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Pada _form_ tersebut mitra diminta untuk menginputkan data-data kegiatan seperti nama perusahaan, sektor perusahaan, alamat kantor utama, website, nama _contact person, phone number contact person,_ email _contact person,_ tipe perusahaan, _password,_ konfirmasi _password,_ dan _upload_

surat perjanjian kerjasama (PKS). Mitra yang diterima maupun ditolak registrasinya akan dihubungi oleh admin melalui _whatsapp_ pada _contact person_ yang telah di daftarkan.

# **2.3.3.3 Halaman** **_Login_**

<!-- Start of picture text -->
fj(< a y]* FakultasUPN VETERAN IImu JAKARTA Komputer<br>Login to your account<br>Username<br>= Password<br>a 2 a. ma<br>oetowe<br>. registrasi terlebin dahulu. Sign up<br><!-- End of picture text -->

Gambar 2.23 _Login_

Halaman _login_ merupakan halaman digunakan oleh _user_ untuk mengakses sistem dengan username dan password. Halaman ini merupakan proses dalam memastikan bahwa hanya pengguna yang terdaftar dan memiliki izin yang dapat melanjutkan ke halaman berikutnya. Proses login juga bertujuan untuk menjaga keamanan data dan memberikan akses yang sesuai dengan peran atau hak pengguna dalam sistem.

# **2.3.3.4 Halaman** **_Dashboard General_**

<!-- Start of picture text -->
O) Fakultas llmu Komputer<br>Goig/ UPN VETERAN JAKARTA<br>= Samet drag octane<br>Mj Dashboard<br>silahkan pith salah satu program yang tersedia !<br>@ mBkm<br>@ student exchange somatn ta el [co<br>@_Manajemen Talenta<br>4)<br>‘Terdir cariMe p r ogram MBKMdeka BelajarFlagship, KampusMKM ManaliMerdeka(Kerja Sama),(MBKM) MBKM Mandi<br>4)<br>Terdi dari program exchangStud e ntSMA, ExchangePMM, dan Kerja Sama Universitas<br>es 2<br>Azka Lailatul Hana Losour Manajemen Talenta<br>Yohasiowa<br>= Terdii dari program pendataan talenta, informasi lomba, dan pendaftaran lomba<br><!-- End of picture text -->

Gambar 2.24 _Dashboard General_

_Dashboard general_ merupakan tampilan _dashboard_ ketika _user_ berhasil melakukan _login._ Pada _dashboard general_ terdapat tiga menu untuk _login_ ke dalam masing-masing sistem. Tiga menu tersebut terdapat MBKM, _Student Exchange_ , dan Manajemen Talenta. Pada halaman ini, _user_ dapat memilih menu dari ketiga sistem tersebut untuk mengakses sistem yang dituju. Jika _user_ memilih MBKM maka sistem akan menampilkan _dashboard_ MBKM. Untuk halaman _dashboard general_ dapat diakses oleh Mahasiswa, Kaprodi, PIC MBKM, Admin, dan Dosen Pembimbing. Dikarenakan peran Mitra hanya untuk sistem MBKM, maka _dashboard general_ tidak ditampilkan di sistem Mitra. Ketika Mitra berhasil melakukan _login_ maka sistem akan menampilkan _dashboard_ MBKM untuk Mitra mengakses sistem.

# **2.3.3.5 Halaman** **_Dashboard_ MBKM**

<!-- Start of picture text -->
= Dashboard<br>Selamat datang, AzkaLailatulHana , -.<br>(Me sressiegi tae es eoine<br>=<br>\<br>B Pengajuansr im<br>3 Pendaftaran<br>peanairass arcs :<br>(I Petaporan Kegiatan<br>B Logout «<br>paqgancinan<br>B avait eva 8 oma<br>moore Pendaftaran MBKM di PT Savas. Pendattaran lang bagi Pelaporan logbook mingguon<br>Multitech Integra sudah dibuka rmahasiswa yang diterima <opat clakukon<br>Read more > Read more > Read more ><br>Testimoni<br>“ 1 y<br><!-- End of picture text -->

Gambar 2.25 _Dashboard_ MBKM

Halaman _dashboard_ MBKM merupakan halaman pertama ketika _user_ mengakses sistem MBKM. Pada halaman ini, _user_ dapat melihat berbagai informasi yang tersedia. Informasi yang tersedia pada halaman ini diantaranya chart mengenai sistem MBKM, informasi umum mengenai MBKM, dan testimoni. Halaman _dashboard_ MBKM untuk masing-masing _user_ memiliki tampilan yang sama dan tidak ada perbedaan diantara _user._

# **2.3.3.6 Halaman Seleksi Mitra**

<!-- Start of picture text -->
i) Seleksi Mitra MBKM ;<br>8} Dashboard<br>© wermaiopron ganna soos stiptsn vo<br>_ 2 ies a soos mcpanoenains aan a<br>5 emma co seo smn soca<br>~<br>B togout<br>samc<br><!-- End of picture text -->

Gambar 2.26 Seleksi Mitra

Halaman seleksi Mitra merupakan halaman untuk melakukan penerimaan atau penolakan terhadap Mitra yang ingin melakukan kerjasama dengan Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Pada halaman ini akan menampilkan data-data Mitra yang melakukan registrasi. Jika Mitra diterima maupun ditolak, maka admin akan menghubungi Mitra tersebut melalui _whatsapp_ pada _contact person_ yang sudah di daftarkan. Halaman ini juga dapat berisi _history_ terkait dengan seleksi Mitra yang sudah dilakukan.

# **2.3.3.6.1 Terima Seleksi Mitra**

<!-- Start of picture text -->
Penerimaan Mitra MBKM FIK UPN “Veteran” Jakarta<br>Pr ABco<br>Teknologi informasi<br>‘www,ptabed.com<br>‘chmdmuzaki@gmallcom Ahmdmuzakil2_<br>Ea<br><!-- End of picture text -->

Gambar 2.27 Terima Mitra

Halaman terima seleksi Mitra merupakan halaman yang akan ditampilkan oleh sistem ketika Admin melakukan mengklik button “Terima”. Halaman ini menampilkan data-data yang diinputkan oleh Mitra pada saat melakukan registrasi. Data-data tersebut sudah _autofill_ dari data registrasi Mitra. Admin dapat melihat _password_ yang diinputkan oleh Mitra untuk memastikan bahwa _password_ tersebut sudah sesuai dengan ketentuan.

# **2.3.3.6.2 Tolak Seleksi Mitra**

<!-- Start of picture text -->
Penolakan Mitra MBKM FIK UPN “Veteran” Jakarta<br>pr reo aul<br>Teknologi Informasi<br>vpn<br>=a<br><!-- End of picture text -->

Gambar 2.28 Tolak Mitra

Halaman tolak seleksi Mitra merupakan halaman yang akan ditampilkan oleh sistem ketika Admin melakukan mengklik button “Tolak”. Halaman ini menampilkan data-data yang diinputkan oleh Mitra pada saat melakukan registrasi. Data-data tersebut sudah _autofill_ dari data registrasi Mitra. Kemudian Admin dapat menginputkan alasan penolakan dari registrasi yang telah di daftarkan oleh Mitra.

# **2.3.3.7 Halaman Informasi Kegiatan Mahasiswa**

<!-- Start of picture text -->
PR<br>(Q) neigeeet a<br>j Informasi Kegiatan<br>BB vashboard ##MBKM FIK BERAGAM ake<br>ew<br>B Pengojuon se 5 pe<br>182 Pendattoron<br>@ status Kegiaton °<br>— Ket manor ato serve -  epracepa-notctenect SE<br>2) Pelaporan kegiatan ro rs<br>s =<br>to<br>Data ntaigence internship Program tmemooxonsgnPr sretuttech megs ota Ants<br>P<br><!-- End of picture text -->

Gambar 2.29 Informasi Kegiatan Mahasiswa

Halaman Informasi Kegiatan pada sistem Mahsiswa merupakan halaman yang menampilkan informasi mengenai lowongan magang yang sedang tersedia. Pada halaman ini terdapat berbagai macam informasi magang dari masing-masing MBKM. Informasi tersebut terdapat informasi dari MBKM Flagship, MBKM Mandiri Kerjasama, dan MBKM Mandiri. Mahasiswa dapat mencari informasi seputar magang pada halaman ini dan dapat melakukan pendaftaran sesuai dengan bakat dan minat yang dimiliki oleh Mahasiswa. Jika Mahasiswa ingin melakukan pendaftaran pada informasi MBKM Flagship dan MBKM Mandiri maka sistem hanya akan menampilkan informasinya saja, tanpa bisa melakukan pendaftaran pada sistem. Mahasiswa dapat melakukan pendaftaran pada platform yang terdapat pada deskripsi kegiatan. Jika Mahasiswa melakukan pendaftaran pada MBKM Mandiri Kerjasama, maka sistem ini dapat membantu Mahasiswa dalam melakukan pendaftaran. Ketika Mahasiswa mengklik button “Ikut Kegiatan” pada halaman _detail_ informasi kegiatan, maka sistem akan menampilkan _form_ pendaftaran MBKM Mandiri Kerjasama.

# **2.3.3.7.1 Tampilan** **_Detail_ Infomasi Kegiatan MBKM Flagship**

<!-- Start of picture text -->
} < Kembali ke halaman utama cay<br>Detail Pendaftaran MBKM Flagship<br>3. bashboard<br>Q=== = EEF vata intelligence internship Kampus Merdeka<br>Bi rengojuanse ae 18esembar 2024<br>AA Pendattaran a<br>@ status Kegiatan<br>Deskeipsi Keglatan<br>1 Bimbingan MBKM [Data inteligence Internship Kampus Merdeka Is Open For Registration)<br>Ue} ania ato Young Tlts!<br>etl cre “Sip Unt Mere Daria Data?<br>B Logout ergaburfahkro PaqatamanDenganLangsung Asa OstPecarannigeneTantangon iteraDuniaKaus eta Merdeka!Dan KembangtonKteemoln Daten ©<br>Smal formas Program Requirement Den Recruitment Posesny Bork hi<br>MoKe FeoFelakanraanPedal:Progr 086 Jana Desemiber2025-25 2024-1Apr Desmber2025  2024<br>LoseLn endtreBItLy/ADUP248_ReglstrationJakarta Uta<br>‘Astracareer<br>Poche $0 You Son Younginternship Talent #Oatanetgence #Oata<br><!-- End of picture text -->

Gambar 2.30 _Detail_ Informasi Kegiatan MBKM Flagship

Halaman _detail_ informasi kegiatan MBKM Flagship merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa memilih salah satu informasi kegiatan MBKM Flagship. Tampilan ini menampilkan _detail_ informasi dari kegiatan MBKM Flagship, Mahasiswa dapat melihat deskripsi kegiatan apakah informasi yang tertera pada informasi tersebut sesuai dengan bakat dan minat. Mahasiswa juga dapat melihat waktu pendaftaran hingga penutupan. Namun untuk informasi kegiatan MBKM Flagship tidak bisa melakukan pendaftaran pada sistem MBKM dikarenakan untuk pendaftaran dapat dilakukan pada _website_ Kampus Merdeka. Pada sistem MBKM, informasi tersebut hanya bisa menampilkan saja tanpa melakukan pendaftaran. Halaman ini bertujuan untuk membantu Mahasiswa dalam melakukan pencarian informasi yang sesuai dengan cepat dan mudah.

# **2.3.3.7.2 Tampilan** **_Detail_ Informasi Kegiatan MBKM Mandiri Kerjasama**

<!-- Start of picture text -->
$ < Kembali ke halaman utama fay<br>Detail Pendaftaran MBKM Mandiri Kerjasama<br>3. bashboard<br>COE=E=D Intorn Data Engineer PT Saras Multitech Intogra<br>M2 Pendattaran ‘KUTIKEGIATAN<br>@ status Kegiatan DeskripsiKegiatan<br>1 Bimbingan MBKM {intern Data Engineer is Open For Registration]<br>C) Polaporan Kegiatan +otoSiop Future untu eaders MengombangkanSill Don Bokotrmu?<br>Siege: Bergabunglah<br>moti PengciomanDenganLangeung. intern Data toaEngineer Tontongan Program! Duna =Nyota, Can Kembongkan Keteramyplon Protesenaim.<br>Simak informa! Program, Persyaraton<br>Can roses Rotrutmenny Bertin<br>MeKM rP\okos: e laksanaansteJoka Pendtoran:Program:setton08 06 besember Jenuari 2025 202418- 28 Maret Oesember 2025 2028<br>00 You Soon Future Leoder!<br>‘#rsorsmulttechintegra_corertinersnp<br>#Octaengneer #Stildeveloprent<br><!-- End of picture text -->

Gambar 2.31 _Detail_ Informasi Kegiatan MBKM Mandiri Kerjasama

Halaman _detail_ informasi kegiatan MBKM Mandiri Kerjasama merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa memilih salah satu informasi kegiatan MBKM Mandiri Kerjasama. Tampilan ini menampilkan _detail_ informasi dari kegiatan, Mahasiswa dapat melihat deskripsi kegiatan apakah informasi yang tertera pada informasi tersebut sesuai dengan bakat dan minat. Mahasiswa juga dapat melihat waktu pendaftaran hingga penutupan. Mahasiswa dapat melakukan pendaftaran di dalam sistem pada jenis MBKM ini, ketika Mahasiswa mengklik button “Ikut Kegiatan” maka sistem akan menampilkan _form_ pendaftaran MBKM Mandiri Kerjasama. Halaman ini bertujuan untuk membantu Mahasiswa dalam melakukan pencarian informasi dan melakukan pendaftaran yang sesuai dengan cepat dan mudah.

# **2.3.3.7.3 Tampilan** **_Form_ Pendaftaran MBKM Mandiri Kerjasama**

<!-- Start of picture text -->
; << Kembali ke halaman detail kegiatan a<br>Form Pendaftaran MBKM Mandiri Kerjasama<br>J Mohon isikan data-data dibawah ini dengan benar dan teliti!<br>== ee<br>B rengajuanse Cae)<br>@ status Kegiotan Email<br>a 2nosno\semahosewaupevjackd<br>By | tomortoneprene<br>Bene oesns70 }<br>Apatoh Perch Meng Mle?<br>— “Moe—CSSS—S—SSSSSSCi<br>aa<br>—G<br>8<br>Jum 88 Yong Soh otempsh<br>wea )<br>raioge<br>24/2025 Gon )<br>Keterangan (Opsional)<br>C }<br>Kartu Hasil Studi (KHS)<br>enam]<br>aKartu Rencana Studi (kRS)<br>carter oe<br>[2amnanetotsinsvenatex |<br>=a<br><!-- End of picture text -->

Gambar 2.32 _Form_ Pendaftaran MBKM Mandiri Kerjasama

Halaman _form_ pendaftaran MBKM Mandiri Kerjasama merupakan halaman yang ditampilkan oleh sistem ketika Mahasiswa mengklik button “Ikut Kegiatan” yang terdapat di dalam halaman _detail_ informasi kegiatan MBKM Mandiri Kerjasama. Pada halaman ini, Mahasiswa dapat mengisi data-data yang dibutuhkan yang terdapat di dalam sistem. Halaman ini bertujuan untuk memfasilitasi proses pendaftaran kegiatan MBKM secara terstruktur dan memastikan bahwa data yang diperlukan terkumpul dengan lengkap dan akurat.

# **2.3.3.7.4 Tampilan** **_Detail_ Informasi Kegiatan MBKM Mandiri**

<!-- Start of picture text -->
é < Kembali ke halaman utama ‘O)<br>Detail Pendaftaran MBKM Mandiri<br>8G Dashboard<br>[@ informasixegiatan se ig Data Intelligence Internship Program<br>BB rengejuanse SRNR CMIEED | :<vesomoor 2024<br>BA Pendattaran fa<br>@ status kegiatan<br>Deskripsi Kegiatan<br>© imbingan mek {beta tigonce ntarship Program Open For Rogistaton}<br>ie eigweroe owe 4 Siop Untuk MeroleobiDura Dota?<br>B Logout ‘egebungla‘NtatargplamenDengan argnin Ate Daantigence Pecan Trtargan neiDunia Progr Nat, Dan KembengtanKeterrpan Osta. ©<br>‘Sma formas! Program, Requirement Dan Recrutment Poses Bert i<br>axm ride Ponta: 08 Detonbor 2024-4 Desmber 2024<br>‘laaaraan Progra @ Januar 2028-28 Agr 2025<br>Las:Unk Pentonekarte UraBLy/ADIP240_Rogitation<br>oe tte See YouSoon Young Tl<br>one<br><!-- End of picture text -->

Gambar 2.33 _Detail_ Informasi Kegiatan MBKM Mandiri

Halaman _detail_ informasi kegiatan MBKM Mandiri merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa memilih salah satu informasi kegiatan MBKM Mandiri. Tampilan ini menampilkan _detail_ informasi dari kegiatan MBKM Mandiri, Mahasiswa dapat melihat deskripsi kegiatan apakah informasi yang tertera pada informasi tersebut sesuai dengan bakat dan minat. Mahasiswa juga dapat melihat waktu pendaftaran hingga penutupan. Namun untuk informasi kegiatan MBKM Mandiri tidak bisa melakukan pendaftaran pada sistem MBKM dikarenakan untuk pendaftaran dapat dilakukan pada _website_ yang tertera pada deskripsi kegiatan. Pada sistem MBKM, informasi tersebut hanya bisa menampilkan saja tanpa melakukan pendaftaran. Halaman ini bertujuan untuk membantu Mahasiswa dalam melakukan pencarian informasi yang sesuai dengan cepat dan mudah.

# **2.3.3.8 Halaman Informasi Kegiatan Kaprodi dan PIC MBKM**

<!-- Start of picture text -->
@<br>© Informasi Kegiatan<br>BB solexsisn<br>1 teneanmone- Hogg Neetepmona tone —eeemegien conn vento<br>@ Soloksi axa<br>@ Pendattaran Uiang<br>& Bimbingan MEKM<br>Dice 2 ccna teenie civrontennetegraicm exes sense<br>B Logout<br>MoKm<br>seat<br><!-- End of picture text -->

Gambar 2.34 Informasi Kegiatan Kaprodi dan PIC MBKM

Halaman informasi kegiatan pada sistem Kaprodi dan PIC MBKM merupakan halaman yang bertujuan untuk melakukan pengelolaan data kegiatan seperi _input_ , _edit,_ dan _delete_ data kegiatan. Pada halaman ini, Kaprodi dan PIC MBKM hanya bisa menginputkan data-data untuk MBKM Flagship dan MBKM Mandiri. Selain itu, halaman ini juga dapat menampilkan data-data kegiatan yang diinputkan oleh Mitra untuk melakukan seleksi dari data-data tersebut. Jika datadata kegiatan yang diinputkan oleh Mitra diterima oleh Kaprodi dan PIC MBKM, maka data tersebut akan berstatus “Diterima” dan akan ditampilkan di halaman seluruh _user_ termasuk Mahasiswa untuk melakukan pendaftaran MBKM Mandiri Kerjasama. Tetapi jika data tersebut ditolak, maka data tersebut akan berstatus “Ditolak” dan Mitra akan melakukan input data kegiatan kembali. Informasi Kegiatan dapat dikelola oleh Kaprodi, PIC MBKM, dan Admin. Ketiga aktor tersebut dapat melakukan _input_ , _edit,_ dan _delete_ data kegiatan serta dapat melakukan seleksi dari input data kegiatan yang diinputkan oleh Mitra. Untuk tampilan informasi kegiatan dari ketiga aktor tersebut memiliki tampilan yang sama dan tidak ada perbedaan diantara masing-masing aktor.

<!-- Start of picture text -->
fo} << Kerbol ke halaman informs! kegiatan<br>ed Form Menambahkan Data Kegiatan<br>Bi omeiceers Mohon isikan data-data dibawah ini dengan benar dan teliti<br>QD ier<br>Bnei 81 Sistornformos v|<br>“+ ponstoran Namoeeinstansi<br>ong eee<br>Prantam ]<br>‘© mings Nama Kegiatan<br>1 operankaton eK Monee ]<br>Boone Email<br>edekopuri@gmolicom ]<br>NomorTelepon<br>ar 081234567600 ]<br>Poss<br>Intern u/Ux design |<br>Kvota Pendottaran<br>20 |<br>Tanggal endoftoran<br>of)w/26/2024 |<br>Tonga! Beroknir<br>| teloeinong12/06/2024 |<br>JonisKegictan<br>eEM Manat- Mayong v]<br>Destripsi<br>(rot mr mo emer<br>‘ransengranongingts ferangan no ota Sansereargun etorgon Peers<br>Foster Pendoftaran<br><!-- End of picture text -->

Gambar 2.35 _Form_ Tambah Data Kegiatan (Kaprodi dan PIC MBKM)

Halaman _form_ tambah data kegiatan merupakan halaman yang akan ditampilkan oleh sistem ketika Kaprodi, PIC MBKM, dan Admin klik button “+” pada halaman informasi kegiatan. Halaman ini digunakan untuk menginputkan data-data kegiatan yang akan ditampilkan pada halaman informasi kegiatan di seluruh sistem _user._ Tampilan _form_ tambah data kegiatan memiliki tampilan yang sama diantara ketiga aktor. Perbedaannya hanya

terletak pada program studi. Admin dapat memilih program studi sedangkan Kaprodi dan PIC MBKM tidak dapat memilih karena program studi kedua aktor sudah disesuaikan dengan tugas dari masing-masing aktor pada program studi. Misalnya seperti Bapak Novi Trisman Hadi, S.Pd., M.Kom. yang merupakan PIC MBKM dari program studi S1 Informatika. Maka pada saat input data kegiatan, program studi yang terdapat pada _form_ tambah data kegiatan pada sistem Pak Hadi hanya program studi S1 Informatika karena sesuai dengan tugas yang saat ini sedang dijalankan.

# **2.3.3.9 Halaman Informasi Kegiatan Dosen Pembimbing**

<!-- Start of picture text -->
(Q)@) Informasi Kegiatan9) :<br>15 basnboard #MBKM FIK BERAGAM ate<br>—).<br>Cari berbaga’ informasi magang yang.<br> Mahasiswa Bimbingan Magang? Stupen? ADAAA LOHHH™ aif, MN<br>‘© Bimbingan MoxM 7<br>Cy Petaperon Kegicton et wet encore serio Sc es |<br>@ status Petaporan<br>B Logout s s<br>fa] mel rf<br>axm ig ig fl<br>Dat lttigenc ntorahi Program nagettc age betas<br>= 2<br>tate P<br><!-- End of picture text -->

Gambar 2.36 Informasi Kegiatan Dosen Pembimbing

Halaman informasi kegiatan dosen pembimbing menampilkan berbagai macam informasi kegiatan dari masing-masing jenis MBKM. Pada halaman ini menampilkan informasi kegiatan dari MBKM Flagship, MBKM Mandiri Kerjasama, dan MBKM Mandiri. Tampilannya sama seperti tampilan Mahasiswa, perbedaannya hanya jika di dosen pembimbing tidak dapat melihat _detail_ dari masing-masing informasi kegiatan dan tidak dapat melakukan pendaftaran. Dosen pembimbing hanya dapat melihat informasi kegiatan dari masing-masing jenis MBKM.

# **2.3.3.10 Halaman Informasi Kegiatan Mitra**

<!-- Start of picture text -->
5<br>oO Informasij Kegiatani ‘)<br>Hy vosnboora 2 Ket unk mencar egioton servo © Taup Tercpot= KuotaTere - Ba<br>4 O crmasiescton No Joris Kegicton Namaegiotan stan emit Telepon resis<br>@ Scloksimekm | senisoweapmona-tnay Teen con sou cctrtunnggritan seni vention<br>B Logout<br>2 senusegmore-hogonyrrsoesea som ——e oan vom<br>meKM<br>ee cae soo ccyorvanosoyraton — comsesn vont<br>Arma uzki<br><!-- End of picture text -->

Gambar 2.37 Informasi Kegiatan Mitra

Halaman informasi kegiatan Mitra merupakan halaman yang bertujuan untuk membantu Mitra dalam melakukan pengelolaan data kegiatan seperti _input, edit,_ dan _delete_ data kegiatan. Pada halaman ini, Mitra juga dapat melihat status seleksi yang dilakukan oleh Kaprodi, PIC MBKM, dan Admin. Jika data-data kegiatan yang diinputkan oleh Mitra diterima oleh Kaprodi dan PIC MBKM, maka data tersebut akan berstatus “Diterima” dan akan ditampilkan di halaman seluruh user termasuk Mahasiswa untuk melakukan pendaftaran MBKM Mandiri Kerjasama. Tetapi jika data ditolak, maka data tersebut akan berstatus “Ditolak” dan Mitra akan melakukan input data kegiatan kembali.

<!-- Start of picture text -->
= Form Menambahkan Data Kegiatan Mitra<br>Beene. Mohon isikan data-data dibawah ini dengan benar dan teliti!<br>OD i<br>2 enlion 51 Sistem informs wal<br>btn!<br>Nama Instansi<br>Noma Kegiatan<br>PT soras Career ]<br>Email<br>‘ahmdmuzaki@gmaiicom<br>Nomor Telepon<br>—: 081294567800 ]<br>Posisi<br>Intern Fullstack Developer<br>uote Pendoftaran<br>6 ]<br>Tanggal Pendaftaran<br>1/28/2024 a]<br>Tanggal Berakhir<br>12/08/2024 a|<br>Jenis Kegiatan<br>[mex<br>manaKeqosoma<br>- Mogang v]<br>Deskripsi<br>enn haat nme op ern<br>‘Se ngucra rgnnosToncngon esac aborgon apn Mer<br>ra srt ete ehcp tenet<br>PostereSPendattaran<br>(se<br><!-- End of picture text -->

Gambar 2.38 _Form_ Tambah Data Kegiatan (Mitra)

Halaman _form_ tambah data kegiatan merupakan halaman yang bertujuan untuk membantu Mitra dalam melakukan input data kegiatan yang akan ditampilkan pada halaman informasi kegiatan. Pada halaman ini, Mitra diminta untuk menginpukan data-data yang dibutuhkan.

# **2.3.3.11 Halaman Seleksi Informasi Kegiatan Data Mitra**

# **2.3.3.11.1 Terima Data Kegiatan MBKM Mandiri Kerjasama dari Mitra**

<!-- Start of picture text -->
Penerimaan Kegiatan MBKM FIK UPN “Veteran” Jakarta<br>Aditya Muhammad edithyamuhammad@gmailcom<br>Pr soras<br>26 November 2024 08 Desember 2024<br>20 orang<br>[tern bata ingineeropen For Regt]<br>volo+ SoprareUneLeaders engembangton Si on Batali?<br>bergabunglan<br>Tentangon DuniaDengan nya itran Kembangkonbata ngineetPogiam! KeteramponPoesonaim.- _ Nkmat PengaamnanLangsungAas<br>=s<br><!-- End of picture text -->

Gambar 2.39 Terima Data Kegiatan Mitra (Kaprodi dan PIC MBKM)

Tampilan terima data kegiatan Mitra merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi, PIC MBKM, dan Admin mengklik button “Terima” pada data kegiatan yang diinputkan oleh Mitra. Pada tampilan ini, data-data tersebut sudah _autofill_ dan ketiga aktor tersebut dapat memastikan bahwa data tersebut sudah sesuai dengan ketentuan. Tampilan seleksi input data kegiatan di masing-masing aktor menampilkan tampilan yang sama, perbedaannya hanya terletak pada program studi. Admin dapat melakukan seleksi dari Mitra yang melakukan input data kegiatan pada seluruh program studi. Sedangkan Kaprodi dan PIC MBKM hanya dapat melakukan seleksi pada program studi yang sesuai dengan tugas yang saat ini sedang dijalankan. Jika data kegiatan yang diinputkan oleh Mitra diterima, maka akan menampilkan status “Diterima” di sistem Kaprodi, PIC MBKM, Admin, dan Mitra dan data tersebut akan ditampilkan di halaman informasi kegiatan seluruh _user._

# **2.3.3.11.2 Tolak Data Kegiatan MBKM Mandiri Kerjasama dari Mitra**

<!-- Start of picture text -->
Penolakan Kegiatan MBKM FIK UPN “Veteran” Jakarta<br>Aditya Muhammad ‘adithyamunammad@gmai.com<br>Prsoras<br>26 November 2024 08 Desember 2024<br>20 orang<br>[rtrn bat nginoeri Open ForRegion}<br>' Sop UntMergembangton slioan Blot?<br>Sergabungjch<br>‘Tortangan DuneDengon Wyte nim Dan KembangionKeterampton Data Engin Program!  FotsenaasNkmatPangloman ongsing Aas<br>@ Informasi yang dlinputkan tidak lengkap<br>@e kt faran t<br>ex aftarar c i<br>@ Lain<br><!-- End of picture text -->

Gambar 2.40 Tolak Data Kegiatan Mitra (Kaprodi dan PIC MBKM)

Tampilan tolak data kegiatan Mitra merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi, PIC MBKM, dan Admin mengklik button “Tolak” pada data kegiatan yang diinputkan oleh Mitra. Pada tampilan ini, data-data tersebut sudah _autofill_ dan ketiga aktor tersebut dapat memastikan bahwa data tersebut sudah sesuai dengan ketentuan. Tampilan seleksi input data kegiatan di masing-masing aktor menampilkan tampilan yang sama, perbedaannya hanya terletak pada program studi. Admin dapat melakukan seleksi dari Mitra yang melakukan input data kegiatan pada seluruh program studi. Sedangkan Kaprodi dan PIC MBKM hanya dapat melakukan seleksi pada program studi yang sesuai dengan tugas yang saat ini sedang dijalankan. Kaprodi, PIC MBKM, dan Admin dapat menginputkan alasan penolakan. Jika data tersebut ditolak maka akan berstatus “Ditolak” dan menampilkan alasan penolakan, kemudian Mitra dapat melakukan input data kegiatan kembali.

# **2.3.3.12 Halaman Pengajuan Surat Rekomendasi**

<!-- Start of picture text -->
SF Pengajuan Surat Rekomendasi<br>HE bashboard Dont Strait<br>© Noro Kepiaton (No Tanggal Pengajuan —Jenis Kegiatan © Nama Kegiotan_ instansi Posisi Perior<br>RA Pondattaran 2 svn234 ane score rect emt oon mats<br>OCI 2 awe nas sega nme nee sous<br>.<br>1 Bimbingan MBKM<br>C2) Petoporan Kegiatan<br>B Logout<br>MaKm<br><!-- End of picture text -->

Gambar 2.41 Pengajuan Surat Rekomendasi

Halaman pengajuan surat rekomendasi merupakan halaman yang terdapat di dalam sistem Mahasiswa untuk melakukan pengajuan surat rekomendasi sebagai syarat dalam proses pendaftaran magang. Pada halaman ini, Mahasiswa dapat melihat perkembangan dari pengajuan yang dilakukan. Jika Mahasiswa tidak memilih pengambilan surat melalui pengambilan ke fakultas maka pengajuan surat yang diterima akan dikirimkan ke _email_ yang telah dicantumkan pada saat melakukan pengajuan. Tetapi jika Mahasiswa memilih pengambilan surat melalui fakultas, maka ketika pengajuan surat tersebut diterima maka Admin akan menginfokan melalui _whatsapp_ mengenai waktu pengambilan. Ketika pengajuan surat tersebut ditolak maka akan menampilkan status “Ditolak” beserta alasan penolak, kemudian Mahasiswa dapat melakukan pengajuan surat rekomendasi kembali. Ketika Mahasiswa mengklik button “Buat Surat Kegiatan” maka sistem akan menampilkan _form_ pengajuan surat rekomendasi.

<!-- Start of picture text -->
S Form Pengajuan Surat Rekomendasi @<br>Li Mohon isikan data-data dibawah ini dengan benar dan teliti!<br>© serermescopeton email<br>LB resschenss ) 2020'S @mahasiswaupnvjacic<br>18 rendtiron<br>Nomor Handphone<br>© erenge tot (eesnoneser06710846870<br>© Peaporn eglton Jenis© Surat Rekomendos! |<br>1B Logout ekm Mandlint v<br>|Apakah sebelumnya sudah pemah mengikuti MBKM?<br>_ Tidak v<br>Semester<br><= rs<br>PK<br>|<br>392<br>JJumlah SKS yang sudah ditempun<br>4<br>Noma instans!<br>| pr sucofindo )<br>Nama Kegiatan<br>MokM Mandir<br>Posisi yang ingin dilamar (bersifat opsional)<br>Intern Ul/UX Design<br>Periods<br>2023/2024 Ganji<br>-Apakh ingin melakukan pengambilan surat i Fakutas?<br>Tidak v<br>xKeterongan (bersfot opsioncl)<br><!-- End of picture text -->

Gambar 2.42 _Form_ Pengajuan Surat Rekomendasi

Halaman _form_ pengajuan surat rekomendasi merupakan halaman yang ditampilkan oleh sistem ketika Mahasiswa mengklik button ”Buat Surat Kegiatan” pada halaman pengajuan surat rekomendasi. Pada halaman ini, Mahasiswa diminta untuk mengisi data-data yang dibutuhkan. Halaman ini bertujuan untuk mempermudah Mahasiswa dalam proses pengajuan surat rekomendasi secara terstruktur dan memastikan bahwa semua data yang diperlukan untuk pengajuan surat telah terisi dengan benar.

# **2.3.3.13 Halaman Seleksi Surat Rekomendasi**

<!-- Start of picture text -->
. : @<br>iw) Pengajuan Surat Rekomendasi =<br>NE Dashboard Kati untuk mencor mahosiswa [aconJ<br>Seleksi Mitra (NO NAMA, EMAIL (NO.HP JENIS SURAT REKOMENDAS! ‘SUDAH PERNAH MBK<br>© informasikegiatan 1 aaron ‘monainemerosenavenyacid _sesoeane enna am<br>B logout 2 cecummneeire: — notaagertmaipmion cece ou —_<br>exo<br>Tanda Put<br><!-- End of picture text -->

Gambar 2.43 Seleksi Surat Rekomendasi (Admin)

Halaman seleksi surat rekomendasi merupakan halaman yang berisi data-data pengajuan surat rekomendasi yang diajukan oleh Mahasiswa. Aktor yang dapat melakukan seleksi surat rekomendasi adalah Kaprodi, PIC MBKM, dan Admin. Pada halaman ini, ketiga aktor tersebut dapat melakukan seleksi berdasarkan kelengkapan dan kesesuaian data yang diajukan oleh Mahasiswa. Halaman ini bertujuan untuk membantu dalam proses seleksi secara efisien dan transparan serta memastikan bahwa pengajuan surat rekomendasi diproses sesuai dengan prosedur yang berlaku sehingga dapat memberikan keputusan yang tepat berdasarkan data yang telah diajukan.

# **2.3.3.13.1 Terima Pengajuan Surat Rekomendasi**

<!-- Start of picture text -->
a} Pengajuan., Surat Rekomendasi: ‘Q)~<br>Setekel eater: NO NAMA ewan NO. HP _JENIS SURAT REKOMENDAS! |SUDAH PERNAH MBK<br>@ intormasi kegiatan 1 asetesvonn ‘masccegmataimaugeyeclt —cesnenaaro serene som<br>Ws tones 2 tte cimusetouine simangs ——«NEIAIpmanedmaeryacs ca MSATBOD cu ene eum<br>2 ena pesciererameseniot sansa a ray<br>MoKm<br>_ © betesSurat Rekomendasi.Menesa Pengojven<br><!-- End of picture text -->

Gambar 2.44 Terima Pengajuan Surat Rekomendasi (Admin)

Tampilan terima pengajuan surat rekomendasi merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi, PIC MBKM, dan Admin mengklik tombol “Terima” pada data pengajuan surat rekomendasi yang diajukan oleh Mahasiswa. Pada tampilan ini, data-data pengajuan tersebut sudah _autofill_ . Ketiga aktor tersebut dapat memastikan bahwa informasi yang diajukan telah sesuai dengan ketentuan. Tampilan seleksi pengajuan surat rekomendasi di masing-masing aktor menampilkan tampilan yang sama, dengan perbedaan terletak pada cakupan program studi. Admin dapat memproses pengajuan dari seluruh program studi, sedangkan Kaprodi dan PIC MBKM hanya memproses pengajuan yang sesuai dengan program studi masing-masing. Jika pengajuan surat rekomendasi diterima, status “Diterima” akan ditampilkan di sistem Kaprodi, PIC MBKM, Admin, dan Mahasiswa.

# **2.3.3.13.2 Tolak Pengajuan Surat Rekomendasi**

<!-- Start of picture text -->
Penolakan Surat Rekomendasi<br>“na Lollatul Hana<br>a<br>$1 Sistem informasi<br>=_<br><!-- End of picture text -->

Gambar 2.45 Tolak Pengajuan Surat Rekomendasi (Admin)

Tampilan tolak pengajuan surat rekomendasi merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi, PIC MBKM, dan Admin mengklik tombol “Tolak” pada data pengajuan surat rekomendasi yang diajukan oleh Mahasiswa. Pada tampilan ini, data-data pengajuan sudah autofill, dan ketiga aktor tersebut dapat memastikan bahwa informasi yang ditolak sesuai dengan ketentuan yang berlaku. Tampilan seleksi pengajuan surat rekomendasi di masing-masing aktor menampilkan tampilan yang sama, dengan perbedaan terletak pada cakupan program studi. Admin dapat memproses pengajuan dari seluruh program studi, sedangkan Kaprodi dan PIC MBKM hanya memproses pengajuan yang sesuai dengan program studi masing-masing. Kaprodi, PIC MBKM, dan Admin juga dapat menginputkan alasan penolakan. Jika pengajuan ditolak, status “Ditolak” akan ditampilkan disertai dengan alasan penolakan. Kemudian Mahasiswa dapat melakukan pengajuan kembali.

# **2.3.3.14 Halaman Pendaftaran MBKM Mandiri Kerjasama (Mahasiswa)**

<!-- Start of picture text -->
‘ Pendaftaran MBKM Kerjasama a)<br>HE vashboard oo<br>Pendaftaran MBKM Mandiri Kerjasama Pendaftaran Ulang<br>© ntormasixegiatan<br>BB rengojuanse NO. NAMAKEGUATAN ——_INSTANS TANGOALPENOAFTARAN —STATUSPENERMAANMITRA STATUS PENERMA<br>CES 1 seanantamone prac some an freoanaJ<br>@ status Kegiatan " : , eo<br>1 Bimbingan MBKM . 2 hart sens some as [seiJ .<br>C) Petoporan Kegiatan<br>B Logout<br>MoKm<br><!-- End of picture text -->

Gambar 2.46 Pendaftaran MBKM Mandiri Kerjasama

Halaman Pendaftaran MBKM Mandiri Kerjasama adalah halaman yang bertujuan untuk melihat status perkembangan dari pendaftaran MBKM Mandiri Kerjasama yang telah di daftarkan oleh Mahasiswa. Pada halaman ini, Mahasiswa dapat melihat dan mengetahui apakah pendaftaran yang dilakukan masih berstatus “Pending”, “Diterima”, atau ditolak. Jika penerimaan dari Mitra dan Prodi berstatus “Diterima” maka langkah selanjutnya yang dapat dilakukan oleh Mahasiswa adalah melakukan pendaftaran ulang. Tetapi jika penerimaan dari Mitra dan prodi berstatus “Ditolak” maka sistem akan menampilkan alasan penolakan dari pendaftaran yang telah dilakukan oleh Mahasiswa dan Mahasiswa tidak dapat melakukan pendaftaran kembali.

# **2.3.3.15 Halaman Seleksi MBKM Kaprodi dan PIC MBKM**

<!-- Start of picture text -->
a Seleksi Pendaftaran MBKM Mandiri Kerjasama Q)<br>$5 peatiboord PT Saras Multitech Integra PT ABCD<br>@ informasikegiatan<br>Cs como) Penta Pender<br>@ Pendattaran Viang<br>sh eerbingca me<br>(NO NAMA NAMA KEGIATAN INSTANS! eMail NOMOR HANDPHON!<br>CO) Petaporan kegiatan 1 tsar Rime rttoceikanecnviege —PTSaonIKMeCrMge ——_ORemnesmaupacts cesronsa7<br>B togout<br>— <2 encodetirosings —tootraytntmrico aD meamentoimcionot jean) =<br>dairaomni 2 cm nena = mecienseincenjen sero<br><!-- End of picture text -->

Gambar 2.47 Seleksi Pendaftaran MBKM Mandiri Kerjasama

Halaman seleksi pendaftaran MBKM Mandiri Kerjasama merupakan halaman yang berisi data-data pendaftaran kegiatan MBKM Mandiri Kerjasama yang diajukan oleh Mahasiswa. Seleksi Pendaftaran MBKM Mandiri Kerjasama dapat dilakukan ketika Mitra sudah melakukan seleksi. Aktor yang dapat melakukan seleksi pendaftaran adalah Kaprodi dan PIC MBKM. Pada halaman ini, kedua aktor tersebut dapat melakukan seleksi berdasarkan kelengkapan dan kesesuaian data pendaftaran yang diajukan oleh Mahasiswa. Halaman ini dapat menampilkan keseluruhan pendaftar dari masing-masing Mitra. Halaman ini bertujuan untuk memfasilitasi proses seleksi secara efisien dan transparan serta memastikan bahwa pendaftaran kegiatan diproses sesuai dengan prosedur sehingga dapat menghasilkan keputusan yang tepat.

# **2.3.3.15.1 Terima MBKM Mandiri Kerjasama (Kaprodi dan PIC MBKM)**

<!-- Start of picture text -->
Penerimaan Pendaftaran MBKM<br>Penerimaan Pendaftaran MBKM berhasil dilakukan!<br><!-- End of picture text -->

Gambar 2.48 Terima Pendaftaran MBKM Mandiri Kerjasama

Tampilan terima seleksi pendaftaran MBKM Mandiri Kerjasama merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi dan PIC MBKM mengklik button “Terima” pada data pendaftaran MBKM Mandiri Kerjasama yang diajukan oleh Mahasiswa. Pada tampilan ini, data-data pendaftaran sudah _autofill_ , dan kedua aktor tersebut dapat memastikan bahwa data yang didaftarkan telah sesuai dengan ketentuan. Jika pendaftaran diterima, maka status “Diterima” akan ditampilkan di sistem Kaprodi, PIC MBKM, dan Mahasiswa. Data seleksi pendaftaran akan tercatat sebagai data pendaftaran resmi yang ditampilkan di halaman pendaftaran MBKM Mandiri Kerjasama pada sistem Mahasiswa.

# **2.3.3.15.2 Tolak MBKM Mandiri Kerjasama (Kaprodi dan PIC MBKM)**

<!-- Start of picture text -->
Penolakan Kegiatan MBKM FIK UPN “Veteran” Jakarta<br>sanyo tuners cinyomnarmadegiaiiem<br>2001009<br>(montero ophpa)<br>‘Foe Gergen Sen ona?<br>Sepnagantngn<br>(igre as ieorungatoreantmarasnaa gra hagangacrenge<br>@t c<br>e<br>e<br><!-- End of picture text -->

Gambar 2.49 Tolak Pendaftaran MBKM Mandiri Kerjasama

Tampilan tolak pendaftaran MBKM Mandiri Kerjasama merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi dan PIC MBKM mengklik button “Tolak” pada data pendaftaran yang diajukan oleh Mahasiswa. Pada tampilan ini, data-data pendaftaran sudah autofill. Pada saat melakukan penolakan, Kaprodi dan PIC MBKM dapat menginputkan alasan penolakan. Jika pendaftaran ditolak, maka status “Ditolak” akan ditampilkan di sistem Kaprodi, PIC MBKM, dan Mahasiswa beserta alasan penolakannya. Mahasiswa tidak dapat melakukan pendaftaran kembali.

# **2.3.3.16 Halaman Seleksi MBKM Mitra**

<!-- Start of picture text -->
Oo Seleksi Pendaftaran MBKM Mandiri Kerjasama vay<br>Ey vashboard PT ABCD<br>@ intormast xegiatan 3<br>Pendaftor<br>B Logout<br>No NaMa, NAMA EOULTAN InsTaNst wa NoMoR HANOPHON:<br><2 mmcmcatasosterge<br>oadAD mo amoszeagmanateoinoeit omen ><br>\pitembenmin 2 Dian Rkiyort wlontern PT ABCD praacD ‘moBROOVeManasiewaUpIM}OCId basn0e4070_<br><!-- End of picture text -->

Gambar 2.50 Seleksi MBKM Mandiri Kerjasama (Mitra)

Halaman seleksi pendaftaran MBKM Mandiri Kerjasama pada sistem Mitra merupakan halaman yang berisi data-data pendaftaran yang diajukan oleh Mahasiswa untuk kegiatan yang diselenggarakan oleh Mitra. Aktor yang dapat melakukan seleksi pendaftaran adalah Mitra. Pada halaman ini, Mitra hanya dapat melihat dan melakukan seleksi terhadap pendaftaran Mahasiswa yang mengajukan pendaftaran untuk kegiatan yang diselenggarakan oleh perusahaan atau instansi yang bersangkutan. Pendaftaran dari perusahaan lain tidak akan ditampilkan di halaman ini. Halaman ini bertujuan untuk memfasilitasi proses seleksi secara efisien dan memastikan bahwa pendaftaran yang diterima sesuai dengan ketentuan.

# **2.3.3.16.1 Terima MBKM Mandiri Kerjasama (Mitra)**

<!-- Start of picture text -->
Penerimaan Pendaftaran MBKM<br>Penerimaan Pendaftaran MBKM berhasil dilakukan!<br><!-- End of picture text -->

Gambar 2.51 Terima Pendaftaran MBKM Mandiri Kerjasama (Mitra)

Tampilan terima seleksi pendaftaran MBKM Mandiri Kerjasama pada sistem Mitra merupakan tampilan yang ditampilkan oleh sistem ketika Mitra mengklik button “Terima” pada pendaftaran yang diajukan oleh Mahasiswa untuk kegiatan yang diselenggarakan oleh perusahaan atau instansi yang bersangkutan. Pada tampilan ini, data-data pendaftaran sudah _autofill_ dan Mitra dapat memastikan bahwa data yang diajukan telah sesuai dengan ketentuan. Halaman seleksi pendaftaran hanya menampilkan pendaftaran dari Mahasiswa yang melakukan pendaftaran untuk kegiatan di perusahaan yang bersangkutan, sementara pendaftaran dari perusahaan lain tidak akan ditampilkan. Jika pendaftaran diterima, maka status “Diterima” akan ditampilkan di sistem Mitra, Mahasiswa, Kaprodi, dan PIC MBKM.

# **2.3.3.16.2 Tolak MBKM Mandiri Kerjasama (Mitra)**

<!-- Start of picture text -->
Penolakan Pendaftaran<br>aka tallatul Hone.<br>2m0812015<br>@« an tidak se<br>ea2<br>@Tidak I MBK<br>@ Kuota sudah melebini<br>@ Laine<br><!-- End of picture text -->

Gambar 2.52 Tolak Pendaftaran MBKM Mandiri Kerjasama (Mitra)

Tampilan tolak seleksi pendaftaran MBKM Mandiri Kerjasama pada sistem Mitra merupakan tampilan yang ditampilkan oleh sistem ketika Mitra mengklik button “Tolak” pada pendaftaran yang diajukan oleh Mahasiswa untuk kegiatan yang dilakukan oleh perusahaan atau instansi yang bersangkutan. Pada tampilan ini, data pendaftaran sudah autofill, dan Mitra dapat memastikan bahwa data yang diajukan tidak sesuai dengan ketentuan yang berlaku. Halaman seleksi pendaftaran hanya menampilkan pendaftaran dari Mahasiswa yang mengajukan diri untuk kegiatan di perusahaan yang bersangkutan, sementara pendaftaran dari perusahaan lain tidak akan ditampilkan. Mitra juga dapat menginputkan alasan penolakan. Jika pendaftaran ditolak, maka status “Ditolak” akan ditampilkan di sistem Mitra, Mahasiswa, Kaprodi, dan PIC MBKM beserta alasan penolakannya.

# **2.3.3.17 Halaman Pendaftaran Ulang MBKM Flagship**

<!-- Start of picture text -->
“S Pendaftaran Ulang MBKM fay<br>BE voshboara Pendaftaran MBKM Mandiri Kerjasama Pendaftaran Ulang MBKM<br>@ informasikegiatan<br>Bi Pengojuan se<br>CED Informasi mengenai Pendaftaran Ulang MBKM Flagship)<br>Pendattaran ulang merupakan pendattaran yang dilakukan untuk mahasiswa yang telah diterima,<br>,g status Kegiatan'<br>pendattaran ulang bertujuan untuk melokukan pendataan. Dengan adanya pendataan in fokultas<br>1 Bimbingan MBKM ‘dapat melakukan pengecekan dan pemantauan pada kegiatan mahasiswa dalam pelaksanaan<br>C) Pelaporan kegiatan BKM yang ckan dilaksanakan. Untuk mahasiswa yang diterima melalui MBKM Flagship (MSIB dan<br>B logout ‘Studi Independent) serta MBKM Mandiri yang terdapat informasi pendaftaran melalui website MBKM<br>dapat metakukan pendattaran ulang dengan klk button pendaftaran ulang dibawah in<br>‘MBKM Pendaftaran Ulang MBKM Flagship<br>_ Informasi mengenai Pendaftaran Ulang MBKM Mandiri (Mencari Sendiri)<br>Pandiaftaran lana marunakan nandaftaran vane dilakukan untuk mahasiswa vana telah atari<br><!-- End of picture text -->

Gambar 2.53 Pendaftaran Ulang MBKM

Halaman Pendaftaran Ulang MBKM merupakan halaman yang diperuntukkan bagi Mahasiswa yang telah diterima dalam program MBKM melalui jalur MBKM Flagship maupun MBKM Mandiri. Pada halaman ini, Mahasiswa dapat memilih antara MBKM Flagship atau MBKM Mandiri sesuai dengan program yang telah mereka pilih sebelumnya. Halaman ini bertujuan untuk memastikan bahwa Mahasiswa melengkapi data yang diperlukan untuk pendaftaran ulang termasuk mengunggah dokumen pendukung seperti LoA _(Letter of Acceptance)_ dan data lain yang relevan sehingga proses administrasi dapat berjalan dengan lancar dan terintegrasi dalam sistem.

<!-- Start of picture text -->
Data Peserta Lolos MBKM Flagship<br>u ‘Mohon iskan data-dote dibawah ini dengon benar dan titi<br>Omen<br>Booms roma<br>——) TTT<br>roast<br>ne © ern suppor<br>rc tegaton<br>2 oot<br>ree Support Arto<br>_ _mwstasseronasiswauprwocles<br>omer tanapone<br>— 9670646870<br>soris worn<br>worst rogsip- Mogang<br>‘spokan Pema Meng Mae?<br>5<br>me v<br>302<br>Jmioh 88 Yang Such otempun<br>20<br>Poros<br>(_zo2u)079 ]<br>008<br>zonalza2s Gort<br>or Host su (6)<br>onRorcone<br>su (8)<br> penaaung nny (Opsona)<br>=z<br><!-- End of picture text -->

Gambar 2.54 _Form_ Pendaftaran Ulang MBKM Flagship

Halaman _form_ pendaftaran ulang MBKM Flagship merupakan halaman yang dapat membantu Mahasiswa dalam melakukan konfirmasi pendataan penerimaan pada program MBKM Flagship. Pada halaman ini, Mahasiswa diminta untuk mengisi _form_ dengan data-data yang dibutuhkan. Halaman ini bertujuan untuk memastikan bahwa data Mahasiswa tercatat dengan lengkap dan valid dalam sistem, sehingga proses administrasi dan pelaksanaan program MBKM Flagship dapat berjalan dengan baik dan sesuai prosedur.

# **2.3.3.18 Halaman Pendaftaran Ulang MBKM Mandiri Kerjasama**

<!-- Start of picture text -->
bed Pendaftaran MBKM Kerjasama a)<br>Pendaftaran Ulang MBKM Mandiri Kerjasama Pendaftaran Ulang<br>© rtormasixegiatan [=a<br>[ick asst! (NO NAMAKEGIATAN INSTANSI_ TANGGAL PENDAFTARAN STATUS PENERIMAAN MITRA |STATUS PENERIN<br>[Aa rendataran [halaman ed ‘nee a co<br>@ status Kegiatan + someon ett == an<br>© Bimbingan MBKM 2 eee aaa seaeccttoet co cs<br>(1) Pelaporan Kegiatan .<br>B Logout<br>ow<br><!-- End of picture text -->

Gambar 2.55 Pendafaran Ulang MBKM Mandiri Kerjasama

Halaman pendaftaran ulang MBKM Mandiri Kerjasama merupakan halaman yang dapat digunakan untuk memantau status perkembangan penerimaan pendaftaran MBKM Mandiri Kerjasama. Pada halaman ini, Mahasiswa dapat melihat status penerimaan dari mitra dan prodi. Jika Mitra dan Prodi menerima pendaftaran maka langkah selanjutnya yang dapat dilakukan oleh Mahasiswa adalah daftar ulang, tetapi jika pendaftaran Mahasiswa ditolak maka sistem akan menampilkan alasan penolakan dari pendaftaran Mahasiswa.

<!-- Start of picture text -->
-) < Kembalike halamandetail kegiatan a<br>Form Pendaftaran MBKM Mandiri Kerjasama<br>a Mohon isikan data-data dibawah ini dengan benar dan teliti!<br>Ce rer<br>Bi rongoluon st i skstem informos!<br>18 Pendtoron<br>2 statue Kepiaton Email<br>oe 20512015@mahasiswaupnyjacid<br>1) Petoporen egiaton Nomor Handphone<br>‘Apakah Pernah Mengikuti MKM?<br>= [tor —“—C‘(Y‘SS<br>Semester<br>Pk<br>(ae—<—sCSCSCSCSC‘i‘(SW<br>.Jumiah SKS Yang Sudah Ditempuh<br>134<br>Poriode<br>{ 2024/2025 Ganji ]<br>Keterangan((opsionol)<br>Kartu Hosil Studi (KHS)<br>Kartu Rencana Studi (kRS)<br>Curriculum vitae<br>Bukti Pendukung Lainnya (Opsionsl)<br>[2Sneisosninninnee|<br>=)<br><!-- End of picture text -->

Gambar 2.56 _Form_ Pendaftaran Ulang MBKM Mandiri Kerjasama

Halaman _form_ pendaftaran ulang MBKM Mandiri Kerjasama merupakana halaman yang diperuntukkan untuk Mahasiswa yang diterima melalui jalur MBKM Mandiri Kerjasama sebagai data konfirmasi penerimaan. Pada halaman ini, data-data Mahasiswa sudah _autofill_ karena mengambil data dari pendaftaran dan Mahasiswa hanya diminta untuk mengupload bukti penerimaan magang (LoA).

# **2.3.3.18.1 Halaman Pendaftaran Ulang MBKM Mandiri**

<!-- Start of picture text -->
Data Peserta Lolos MBKM Mandiri<br>ne heaiat ‘Mohon isikan data-data dibawah ini dengan benar dan teliti<br>Sens Nama instansi<br>Bruen ~~<br>Cr<br>— int Data nginer<br>———— ened<br>2 hom [oetasnginermiemerate SSS<br>mai<br>~ -MOSI201@mahasiswaupryj.ocid<br>omer Hancphone<br>oa Mone Mogong<br>-Apakoh Perah Meng MBE?<br>a<br>“belch 8 Yang Susoh temp<br>2ovafaazs cory<br>xetorangan (peor<br>2o2a/2028 cart<br>aru ost stu (8)<br>are Rencona uc (8)<br>su Penermaon Mager (oH)<br>surat Pomononan Krjasama (Hs) Download Template Ps<br>=z<br><!-- End of picture text -->

Gambar 2.57 _Form_ Pendaftaran Ulang MBKM Mandiri

_Form_ pendaftaran ulang MBKM Mandiri merupakan halaman yang dapat membantu Mahasiswa dalam melakukan konfirmasi pendataan penerimaan pada program MBKM Mandiri. Perbedaan antara _form_ pendaftaran ulang MBKM Flagship dan MBKM Mandiri terletak pada Perjanjian Kerjasama (PKS). Jika Mahasiswa diterima melalui jalur MBKM Flagship maka tidak perlu mengupload PKS tetapi jika Mahasiswa diterima melalui jalur MBKM Mandiri maka Mahasiswa diminta untuk mengupload PKS pada saat melakukan pendaftaran ulang.

# **2.3.3.19 Halaman Pendaftaran Ulang dan Seleksi Dosen Pembimbing**

<!-- Start of picture text -->
Le) Seleksi Pendaftaran Ulang MBKM fay<br>—— ati untuk mencor mahosiswa [i can |<br>@ informasi kegiatan no NAMA, NAMA KEGIATAN INSTANS! Posist ewan<br>B seteksisa 1 ‘to Laer Hore "rte PY Soros Mathech tego 9 Sore Makan gr | inten ‘mosuospmorosen<br>3 Seleksimaxn<br>2 tectonic cs von en entotencretue<br>2, Dattar Mahasiswa<br>‘& Bimbingan MBKM<br>©) Pelaporankegiatan 2 (Dion yore Uf een Pr ABCD rawco what mommrcrosw<br>B logout<br>wake<br>detonate<br><!-- End of picture text -->

Gambar 2.58 Seleksi Pendaftaran Ulang MBKM

Halaman seleksi pendaftaran ulang MBKM adalah halaman yang dapat digunakan untuk melakukan seleksi pendaftaran ulang MBKM dari Mahasiswa. Aktor yang dapat melakukan seleksi pendaftaran ulang adalah Kaprodi dan PIC MBKM. Pada halaman ini dapat menampilkan data-data pendaftaran ulang dari masing-masing MBKM seperti MBKM Flagship, MBKM Mandiri Kerjasama, dan MBKM Manidri. Selain itu, halaman ini juga berfungsi sebagai riwayat _(history)_ untuk mencatat status dan hasil seleksi pendaftaran ulang yang telah dilakukan. Halaman ini bertujuan untuk mempermudah Kaprodi dan PIC MBKM dalam memantau, meninjau, dan memastikan bahwa proses pendaftaran ulang berjalan sesuai prosedur yang berlaku.

# **2.3.3.19.1 Terima Mahasiswa (Konfirmasi Seleksi Dosen Pembimbing)**

<!-- Start of picture text -->
Terima Pendaftaran<br>Es Ey<br><!-- End of picture text -->

Gambar 2.59 Seleksi Dosen Pembimbing (Pendaftaran Ulang)

Halaman seleksi dosen pembimbing merupakan halaman yang akan ditampilkan oleh sistem ketika Kaprodi dan PIC MBKM mengklik button “Terima” pada data pendaftaran ulang Mahasiswa. Pada saat melakukan penerimaan, Kaprodi dan PIC MBKM akan melakukan seleksi dosen pembimbing yang sesuai untuk Mahasiswa. Jika Kaprodi dan PIC MBKM telah melakukan seleksi dosen pembimbing, maka data akan tersimpan di dalam _database_ dan akan ditampilkan di sistem Mahasiswa pada menu “Status Kegiatan” yang berisi status kegiatan dan dosen pembimbing.

# **2.3.3.19.2 Tolak Mahasiswa**

<!-- Start of picture text -->
Penolakan Pendaftaran<br>-2ka tollatul Hana<br>2nosr2015,<br>@ tis yang diinputkan tidak sesuai<br>@ Rs yar kan tidak sesuai<br>@ tia ari x<br>@. elebit<br>@ Lair<br><!-- End of picture text -->

Gambar 2.60 Tolak Pendaftaran Ulang

Tampilan tolak seleksi pendaftaran ulang MBKM merupakan tampilan yang ditampilkan oleh sistem ketika Kaprodi dan PIC MBKM mengklik button "Tolak" pada data pendaftaran ulang yang diajukan oleh Mahasiswa. Kaprodi dan PIC MBKM juga dapat memberikan alasan penolakan pada data yang tidak memenuhi syarat. Jika data pendaftaran ulang ditolak, maka statusnya akan berubah menjadi "Ditolak" dengan alasan penolakan yang ditampilkan di sistem, dan Mahasiswa dapat melakukan pendaftaran ulang kembali setelah menerima penolakan dari Kaprodi dan PIC MBKM.

# **2.3.3.20 Halaman Status Kegiatan (Mahasiswa)**

<!-- Start of picture text -->
bs Status Kegiatan MBKM a)<br>© rtormasixegiatan wo AMAREOATAN TANS one enn asavroouss<br>B Pengajuansr 2 wmmoateergreetasco ABCD tren atatrgroer course -<br>3 Pendattaran 2 ‘eterDota Engraer PARED FAKED. “reer bata tage bom 0 at<br>1 Bimbingan MBKM<br>©) Pelaporan Kegiatan<br>B Logout<br>ox<br><!-- End of picture text -->

Gambar 2.61 Status Kegiatan Mahasiswa

Halaman status kegiatan mahasiswa merupakan halaman yang berisi status perkembangan terkait dengan pendaftaran ulang. Pada halaman ini. Mahasiswa dapat melihat dan mengetahui status perkembangan daftar ulangnya. Jika Kaprodi dan PIC MBKM menerima daftar ulang yang diajukan oleh Mahasiswa, maka akan menampilkan status “Diterima” dan menampilkan nama dosen pembimbing yang sesuai dengan Mahasiswa. Tetapi, jika Kaprodi dan PIC MBKM menolak daftar ulang yang diajukan oleh Mahasiswa maka akan menampilkan status “Ditolak” dan akan terdapat alasan penolakan. Jika Mahasiswa pendaftaran ulangnya ditolak, maka Mahasiswa dapat melakukan pendaftaran ulang kembali.

# **2.3.3.21 Halaman Jadwal Bimbingan (Mahasiswa)**

<!-- Start of picture text -->
3 oe )<br>nis Jadwal Bimbingan MBKM<br>8 Dashboard Paling Boru . =<br>© informasixegiatan<br>ee Bimbingan Bulanan<br>B Penggjuansr a (B18 september2024<br>BA Pendaftaran nee<br>@ status Kegiaton ‘Online https://z00m-fik.com<br>C2 Pelaporan Kegiatan<br>B Logout<br>MoKn<br>sa atone<br><!-- End of picture text -->

Gambar 2.62 Belum Mengisi Kehadiran Bimbingan

Tampilan status belum mengisi kehadiran bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing sudah membuat jadwal bimbingan dan sudah melaksanakan bimbingan dengan Mahasiswa. Pada tampilan ini, Mahasiswa diharuskan untuk mengisi kehadiran bimbingan. Tampilan ini berfungsi sebagai pengingat bagi Mahasiswa yang belum mengisi kehadiran dan memastikan bahwa setiap sesi bimbingan terdokumentasi dengan baik dalam sistem.

<!-- Start of picture text -->
MS Form Kehadiran Bimbingan Q)<br>Ee Dosntoord Bimbingan Bulanan<br>© itormasi egiatan rwseptomber2004oni 1200snap son- corn<br>Bi Pengojuanse Nama<br>BY pendattoran ‘2ka Loilatul Hana<br>@ status egiatan av<br>Gu Baa<br>7 Pelaporan Kegiatan Prodi<br>B togout 51 Sistem informasi<br>Tonggal Pelaksonaan<br>MK 18 September 2024 0<br>Topik simbingan<br>peeteny chorion<br><!-- End of picture text -->

Gambar 2.63 _Form_ Kehadiran Bimbingan

Halaman _form_ kehadiran bimbingan merupakan halaman yang ditampilkan oleh sistem ketika Mahasiswa mengklik button “Isi Kehadiran” yang terdapat pada halaman jadwal bimbingan MBKM. Pada halaman ini, Mahasiswa diminta untuk mengisi data-data yang dibutuhkan sebagai bukti bahwa mereka telah mengisi _form_ kehadiran bimbingan. Setelah Mahasiswa mengisi _form_ ini, data tersebut akan disimpan dalam _database_ dan akan dikirimkan ke sistem Dosen Pembimbing untuk validasi serta memberikan catatan bimbingan.

# **2.3.3.21.1 Pending Kehadiran Bimbingan**

<!-- Start of picture text -->
- ¢0 Jadwal Bimbingan— MBKM vay‘i<br>BB oashboard ating Boru -— =<br>© informasixegiatan =— — Bimbingan Bulanan mB<br>BB rengojuanse : | (2 seprroee2024<br>BB Pendattaran: Swat<br>@ statue Kegiatan ‘ening tpfsoomn-fiecom<br>cprmemrerans<br>C1 Peloporan Kegiatan<br>B Logout<br>oxo<br><!-- End of picture text -->

Gambar 2.64 Pending Kehadiran Bimbingan

Tampilan pending kehadiran bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa telah berhasil mengisi _form_ kehadiran. Pada tampilan ini. Mahasiswa diharapkan untuk menunggu penerimaan atau penolakan dari dosen pembimbing terkait dengan _form_ kehadiran yang telah diisi. Halaman ini berfungsi sebagai pemberitahuan status kehadiran bimbingan yang masih dalam proses validasi oleh Dosen Pembimbing.

# **2.3.3.21.2 Diterima Kehadiran MBKM**

<!-- Start of picture text -->
J " ., vay<br>as Jadwal Bimbingan MBKM<br>HE Dashboord Foling Baru - =<br>@ informasikegiatan<br>2 Bimbingan Bulanan<br>BB rengsjuanse es.| {3 sapmber2024<br>BD Pendattaran geo<br>@ status Kegiaton nine iipsfsom-com<br>(2) Peloporan Kegiatan<br>B togout<br>on<br><!-- End of picture text -->

Gambar 2.65 Diterima Kehadiran Bimbingan

Tampilan diterima kehadiran bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa telah diterima _form_ kehadiran. Pada tampilan ini. Mahasiswa dapat melihat catatan bimbingan yang diberikan oleh Dosen pembimbing. Halaman ini berfungsi sebagai media untuk mengonfirmasi bahwa kehadiran bimbingan telah diverifikasi dan diterima oleh Dosen Pembimbing. Selain itu, tampilan ini membantu Mahasiswa untuk mengakses catatan penting yang dibuat oleh Dosen Pembimbing terkait dengan kendala yang dihadapi selama pelaksanaan MBKM.

# **2.3.3.21.3 Ditolak Kehadiran**

<!-- Start of picture text -->
es7; Jadwal Bimbingan— MBKM vay<br>BE Dashboard Paling aru - =<br>© rformasikegiatan<br>B Pengojuanse 2“) £2Bimbingan 8 september Bulanan2028<br>89 ondattaran a<br>‘onine _ntpefzoom-flecom<br>@ statue Kegiaton<br>C3 Petaporan kegiatan<br>B Logout<br>wenn<br><!-- End of picture text -->

Gambar 2.66 Ditolak Kehadiran Bimbingan

Tampilan ditolak kehadiran bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa ditolak _form_ kehadiran. Pada tampilan ini. Mahasiswa dapat melihat alasan penolakan dari dosen pembimbing. Mahasiswa diminta untuk mengisi kehadiran kembali. Halaman ini berfungsi sebagai media untuk memberikan informasi kepada Mahasiswa terkait alasan penolakan form kehadiran, sehingga Mahasiswa dapat memperbaiki atau melengkapi data yang diperlukan sesuai dengan arahan Dosen Pembimbing.

# **2.3.3.21.4** **_Form_ Kehadiran setelah diberikan catatan bimbingan**

<!-- Start of picture text -->
ao Catatan Bimbingan MBKM (a)<br>83 osttboora SEE Bimbingan Bulanan<br>© intormasi kegiatan < ‘Ontinereseptember2024 1300intps:|/z00m-fk.com<br>B Pengajuansk Noma<br>AY Pendattaran ‘ka Loilotul Hana<br>@ status Kogiatan Nm<br>C1 Petaporan kegiatan Prodi<br>B togout SI Sistom informasi<br>TTonggol Petoksonaon<br>mows 18 September 2024 a<br>Topik simbingan<br>Progress Kegiatan<br>— xonodivan<br>Hodir v<br>UUnagah Loporan Bulanan<br>is) 2110512015 _AzkaLoilatul Hana_Laporan Magang Bulananpal<br>Kendala yang dihadapi selome MakM<br>Kendalanya sult dalam mengerjakan task<br>Laporan<br>Saye mendapatkan role sebagai trontend developer<br>Catatan simbingan<br><iskusikanKalau ada denganbagian tugas saya yang atau temansult, coba untuk dipisahkan duly mencari solusi mana bersama, yangAturpalingwoktususah.denganBisa<br>bik dan kerjokan tugos sedikt-sediktbior nggak terasa beratKalau butuh bantuan<br>tambahan, saya siop membantu atau memberikan materi yang bisa dipelajari<br>Kombat<br><!-- End of picture text -->

Gambar 2.67 _Form_ Kehadiran Setelah Diberikan Catatan Bimbingan

Tampilan _form_ kehadiran setelah diberikan catatan bimbingan merupakan tampilkan yang ditampilkan oleh sistem ketika _form_ kehadiran bimbingan Mahasiswa diterima oleh Dosen Pembmbing dan Mahasiswa mengklik button “Cek Catatan Bimbingan” pada halaman jadwal bimbingan. Pada halaman ini, Mahasiswa dapat melihat secara _detail_ catatan bimbingan yang diberikan oleh Dosen Pembimbing. Catatan bimbingan ini berfungsi sebagai penjelasan atau tanggapan dari Dosen Pembimbing terkait kendala yang sedang dihadapi oleh Mahasiswa.

# **2.3.3.22 Halaman Jadwal Bimbingan (Dosen Pembimbing)**

<!-- Start of picture text -->
a) Jadwal Bimbingan MBKM<br>Bg Dashboard ating Baru . [a cus |[+ |<br>© snformasixegiatan D G<br>22 Mahasiawa Bimbingon<br>@ status Pelaporan<br>B Logout<br>ac<br><!-- End of picture text -->

Gambar 2.68 Jadwal Bimbingan MBKM (Dosen Pembimbing)

Halaman jadwal bimbingan MBKM pada Dosen Pembimbing merupakan halaman untuk Dosen Pembimbing melakukan pengelolaan data kegiatan jadwal bimbingan seperti _input, edit,_ dan _delete_ . Pada halaman ini, Dosen Pembimbing dapat melakukan pengecekan kehadiran dari Mahasiswa terkait dengan pelaksanaan bimbingan yang telah dilakukan.

# **2.3.3.22.1 Tambah Jadwal Bimbingan**

<!-- Start of picture text -->
Form Tambah Jadwal Pelaksanaan Bimbingan<br>ane TS amine<br>“os<br><!-- End of picture text -->

Gambar 2.69 _Form_ Tambah Jadwal Bimbingan

Halaman _form_ tambah jadwal bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “+” yang terdapat pada halaman jadwal bimbingan MBKM. Pada halaman ini, Dosen Pembimbing dapat melakukan penambahan jadwal pelaksanaan bimbingan yang akan dilaksanakan dengan Mahasiswa.

# **2.3.3.22.2** **_Edit_ Jadwal Bimbingan**

<!-- Start of picture text -->
Form Ubah Jadwal Pelaksanaan Bimbingan<br>®ulonan :<br>ri a 09/18/2024 a<br>~<br>ae 02:00 PM -<br>oniine :<br><!-- End of picture text -->

Gambar 2.70 _Form Edit_ Jadwal Bimbingan

Halaman _edit_ jadwal bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing memilih salah satu informasi bimbingan dan mengklik button “edit” yang terdapat pada halaman jadwal bimbingan MBKM. Pada halaman ini, Dosen Pembimbing dapat melakukan pengeditan pada jadwal bimbingan seperti mengubah _cover_ bimbingan, jenis bimbingan, tanggal bimbingan, jam bimbingan, pelaksanaan, dan deskripsi.

# **2.3.3.22.3** **_Delete_ Jadwal Bimbingan**

<!-- Start of picture text -->
@) Jadwal Bimbingan MBKM<br>Hy vashboard erate _aa<br>@ intormasi kegiatan ) (<br>2 Mahasiewa Bimbingan<br>C7) Petaporan Kegiatan<br>@ status Petoporan<br>B Logout<br>ox<br>== © erhcatmenghopusjawed bimbingan,<br><!-- End of picture text -->

Gambar 2.71 Berhasil _Delete_ Jadwal Bimbingan

Tampilan berhasil _delete_ jadwal bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing berhasil menghapus jadwal bimbingan yang telah dibuat sebelumnya. Pada tampilan ini, sistem akan menampilkan notifikasi atau pesan konfirmasi bahwa jadwal bimbingan telah berhasil dihapus. Halaman ini berfungsi untuk memberikan informasi kepada Dosen Pembimbing bahwa tindakan penghapusan jadwal telah berhasil dilakukan. Selain itu, tampilan ini memastikan bahwa data jadwal yang dihapus tidak lagi muncul di daftar jadwal bimbingan, sehingga sistem tetap terorganisir dan hanya menampilkan jadwal-jadwal yang masih berlaku.

# **2.3.3.22.4 Pengecekan Bimbingan**

<!-- Start of picture text -->
; Pengecekan Bimbingan Bulanan - 18 September 2024 Q)<br>By bashboora<br>© informasixegiatan No nana TANGOALPELAKSANAAN TORE BNUBHVOAN venaoinan aronansuanan<br>2. Mahosiswa Bimbingan — o— we =z —<br>C Petaporan Kegiatan 9 mectanoaranangs ar pete = =<br>@ status Pelaporan “een<br>B Logout<br>axe<br><!-- End of picture text -->

Gambar 2.72 Pengecekan Bimbingan (Dosen Pembimbing)

Halaman pengecekan bimbingan merupakan halaman yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Lihat Kehadiran Bimbingan” pada halaman jadwal bimbingan MBKM. Halaman ini berfungsi sebagai sarana bagi Dosen Pembimbing untuk memantau dan memverifikasi kehadiran bimbingan yang telah diisi oleh Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat detail informasi kehadiran, termasuk kendala pelaksanaan bimbingan yang diinputkan oleh Mahasiswa. Halaman ini juga memungkinkan Dosen Pembimbing untuk memberikan keputusan berupa penerimaan dan catatan bimbingan serta penolakan beserta dengan alasan penolakan.

# **2.3.3.22.5 Terima Bimbingan (Memberikan Catatan Bimbingan)**

<!-- Start of picture text -->
Terima Pengecekan Bimbingan<br>‘zka Loilatul Hane<br>20512015,<br>SI Sistem informa!<br>Kalau ada bagian tugas yang sult, oba dipisahkan dulu mana yang paling<br>susah, Bisa diskusikan dengan saya atau teman untuk mencari solusi<br>bersama. Atur waktu dengan balk dan kerjakan tugas sedikit-sedikit bior<br>‘nggak terasa berat. Kalau butuh bantuan tambahan, saya siap membantu<br>‘atau memberikan materi yang bisa dipelajar<br><!-- End of picture text -->

Gambar 2.73 _Form_ Catatan Bimbingan (Terima Bimbingan)

Tampilan _form_ catatan bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Terima” pada data _form_ kehadiran bimbingan yang diajukan oleh Mahasiswa. Pada halaman ini, Dosen Pembimbing melakukan penerimaan _form_ kehadiran bimbingan Mahasiswa dengan memberikan catatan bimbingan untuk memberikan solusi atau arahan mengenai kendala yang mungkin menghambat proses pelaksanaan MBKM pada Mahasiswa.

# **2.3.3.22.6 Tolak Bimbingan**

<!-- Start of picture text -->
Penolakan Pengecekan Bimbingan<br>‘2ka Lalatul Hane<br>2n0st2015<br>Si sistem informast<br>@ Loporan yang diinputkantidak sesuai<br>@ Lainnya:<br>Es<br><!-- End of picture text -->

Gambar 2.74 Tolak Bimbingan

Tampilan tolak bimbingan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Tolak” pada data _form_ kehadiran bimbingan yang diajukan oleh Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat memberikan alasan penolakan terkait dengan _form_ kehadiran bimbingan yang telah diajukan oleh Mahasiswa. Jika kehadiran bimbingan ditolak oleh Dosen Pembimbing, maka Mahasiswa dapat mengisi _form_ kehadiran bimbingan kembali.

# **2.3.3.23 Tampilan Bimbingan Kaprodi dan PIC MBKM**

<!-- Start of picture text -->
Ce) Pelaporan Mahasiswa MBKM @<br>1 Ket unt manson mahasewa semua Prods - ao<br>Hii Dashboard<br>© informasikegiatan no naw cS NoMon TEPON ens aKa NAMA KEOIATAN<br>B seietsisn ‘coe emesis ees<br>3 Seleksi MBKM<br>@ Pendattaran vlang 2 —seceaterednasitege Eee eee Mooeroaee unt rucaro ire<br>(2. Daftar Mahasiswa<br>LD ia Seems oe omen ene<br>Sere<br>(e) ese<br>B logout<br>Max<br>Acer<br><!-- End of picture text -->

Gambar 2.75 Pengecekan Bimbingan (Kaprodi dan PIC MBKM)

Tampilan pengecekan bimbingan pada sistem Kaprodi dan PIC MBKM merupakan tampilan yang ditampilkan oleh sistem untuk menampilkan data-data bimbingan yang dilakukan oleh Mahasiswa dengan Dosen Pembimbing. Pada halaman ini, Kaprodi dan PIC MBKM hanya bisa melakukan monitor tanpa melakukan penerimaan atau penolakan dari _form_ kehadiran bimbingan Mahasiswa. Halaman ini juga dapat di _export_ ke dalam file _excel_ sebagai bukti dari pelaksanaan bimbingan Mahasiswa dengan Dosen Pembimbing.

# **2.3.3.24 Halaman Daftar Mahasiswa Kaprodi dan PIC MBKM**

<!-- Start of picture text -->
@ Daftar Mahasiswa MBKM :<br>Dattar Mahasiswa yang melokukan pendaftaran MEKM<br>By Dashboard . : mo<br>© informasikegiatan<br>B Soloksise NosetaeNAMA nena ‘mestanomenmioosgnjocitean NoMoRO87 TELEFON ens sensrn ergerra MoO Mogarg etnNAMAKEOIATANmanga<br>3 Soloksi MBKM Semen nora<br>@ Pendattaran ulang<br>2 emcinttndnatmenge —"EAEOchmaengocs GADD secure sean ru conpasite<br>© Bimbingan MBKM<br>C1 Peloporan kegiatan 5 nsenue nosmmencaimognect — cmiasem sects seamen tagote<br>B Logout<br>MeKM<br>Ada rus<br><!-- End of picture text -->

Gambar 2.76 Daftar Mahasiswa (Kaprodi dan PIC MBKM)

Halaman daftar mahasiswa pada sistem Kaprodi dan PIC MBKM merupakan tampilan yang ditampilkan oleh sistem untuk menampilkan daftar Mahasiswa yang sedang melaksanakan MBKM. Pada tampilan ini, menampilkan data Mahasiswa secara keseluruhan namun tetap terbatas sesuai dengan program studi dari Kaprodi dan PIC MBKM. Jadi daftar Mahasiswa yang ditampilkan hanya Mahasiswa dari program studi yang sesuai dengan Kaprodi dan PIC MBKM. Halaman ini juga dapat di _export_ ke dalam file _excel_ sebagai rekap mengenai daftar Mahasiswa yang sedang melaksanakan MBKM.

# **2.3.3.25 Halaman Daftar Mahasiswa Dosen Pembimbing**

<!-- Start of picture text -->
. ee fay<br>} Mahasiswa Bimbingan MBKM =<br>OSTBF bashboard Nowa naa ses Moe ana xeouaTaN wnsransi<br>1 press ‘as tons Mare se Marc terme = Mogang ‘ete oa ngewe ABCD prac<br>‘© Bimbingan MBKM 2 msm rms ote Ago secure sees omigtonp ere irene<br>7 Pelaporan kegiatan<br>@ ‘status Pelaporan<br>B togout 3 momo sepasovergra seven ota inreennen<br>axe<br>ut ata<br><!-- End of picture text -->

Gambar 2.77 Daftar Mahasiswa (Dosen Pembimbing)

Halaman daftar mahasiswa pada sistem Dosen Pembimbing merupakan halaman yang menampilkan data-data mahasiswa bimbingan yang terdaftar sebagai Mahasiswa bimbingan pada pelaksanaan MBKM. Halaman ini membantu Dosen Pembimbing untuk melihat informasi lengkap Mahasiswa seperti nama, program studi, jenis MBKM dari masing-masing Mahasiswa, nama kegiatan, dan nama instansi. Halaman ini berfungsi untuk memudahkan Dosen Pembimbing dalam memantau perkembangan Mahasiswa selama pelaksanaan MBKM.

# **2.3.3.26 Halaman Pelaporan Bulanan (Mahasiswa)**

<!-- Start of picture text -->
vs Pelaporan Kegiatan Bulanan MBKM<br>3 Dashboard { sarurcon)<br>Otte No JoB068c/Posis) _RIKAPLOOBOOKBULAN soo#00K ewan save ase<br>BB Pengajuan sk _ — “<br>2 mtn toi om oe.)<br>A Pendattaran<br>@ status Kegiatan L 2 naman AA Sagan os oom a;<br>© Bimbingan MaKM<br>3 Laporan aknie<br>B Logout<br>oxo<br><!-- End of picture text -->

Gambar 2.78 Pelaporan Bulanan (Mahasiswa)

Halaman pelaporan bulanan MBKM merupakan halaman yang dapat digunakan untuk memantau dan mengelola pelaporan kegiatan bulanan Mahasiswa selama pelaksanaan MBKM. Pada halaman ini, Mahasiswa dapat mengunggah laporan bulanan yang berisi progres kegiatan yang telah dilakukan. Jika laporan diterima, maka sistem akan mencatat laporan tersebut sebagai bagian dari dokumentasi kegiatan MBKM. Jika laporan ditolak, sistem akan menampilkan alasan penolakan, sehingga Mahasiswa dapat melakukan revisi dan mengunggah laporan bulanan kembali. Halaman ini dirancang untuk mendukung transparansi dan efisiensi dalam proses pelaporan bulanan MBKM.

<!-- Start of picture text -->
es Form Pelaporan Kegiatan Bulanan MBKM<br>8 Dashboard Mohon isikan data-data dibawah ini dengan benar dan teliti!<br>@ informasikegiatan Nama<br>B Pengajuan sr CSL Ee era<br>AY Pendattaran Ni<br>@ Status Kegiatan ‘2NOSI2018<br>1 Bimbingan MaKM Program Studi<br>Gx eae<br>3 Laporan aknie Instonsi<br>B logout Prasco a<br>Dosen Pembimbing<br>ox<br>Novi Trisman Hadi, S.Pd, M.Kom.<br>Email<br>snaMenacetabtattane (2N10512015@mahasiswa.upnvj.ac.id-<br>Nomor Handphone:<br>ret<br>085710846870<br>Rekap Logbook Bulan<br>24 September 2024 - 24 Noverber 2024<br>Unggah Logbook (.paf) Download Template Logbook<br>2110512015_Azka Lallatul Hona_toporan Magang @ulanan pat<br>Kendola seloma MBkM<br>— ]<br><!-- End of picture text -->

Gambar 2.79 _Form_ Pelaporan Bulanan

Tampilan _form_ pelaporan bulanan merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa mengklik button “Buat Laporan”pada halaman pelaporan bulanan. Halaman ini berfungsi sebagai sarana bagi Mahasiswa untuk mengisi data laporan bulanan seperti rekap logbook bulan, unggah _logbook_ , dan kendala selama pelaksanaan MBKM. Halaman ini dirancang untuk memastikan laporan bulanan yang diunggah oleh Mahasiswa sesuai dengan format dan ketentuan.

# **2.3.3.27 Halaman Pelaporan Bulanan (Kaprodi dan PIC MBKM)**

<!-- Start of picture text -->
Oo Pelaporan Kegiatan Bulanan ~<br>3 varhboard<br>@ weet teciton wo manta ua oon rsrow ses moo naa ouaTan<br>sce ttermatmmsgmtss seu seavienateepora-tay<br>BB soloksise wee —rntnatgrean<br>& Sotoxsi exe<br>EE 5 tacoma Sitrnmnns seosroare voitntoroatete<br>2. Dotter Mahasiswa<br>Soon ennai conerwowegnict) seam oer en acm tgs<br>B togout<br>on<br>air<br><!-- End of picture text -->

Gambar 2.80 Pelaporan Bulanan (Kaprodi dan PIC MBKM)

Halaman pelaporan bulanan pada sistem Kaprodi dan PIC MBKM merupakan halaman yang ditampilkan oleh sistem untuk menampilkan data laporan bulanan yang diajukan oleh Mahasiswa selama pelaksanaan MBKM. Pada halaman ini, Kaprodi dan PIC MBKM hanya dapat memantau laporan tanpa melakukan penerimaan atau penolakan terhadap laporan bulanan Mahasiswa. Halaman ini juga dapat di _export_ ke dalam file _excel_ sebagai dokumentasi dan bukti pelaksanaan pelaporan bulanan Mahasiswa selama program MBKM berlangsung.

# **2.3.3.28 Halaman Pelaporan Bulanan (Dosen Pembimbing)**

<!-- Start of picture text -->
. ‘Q)<br>(@) Pelaporan Kegiatan Bulanan MBKM -<br>© informasi kegiatan No NAMA JoBDESC/POSIS! __REKAPLOGBOOK BULAN. 106800 KENDALA statu<br>Ap —=_— evonetrgne Sean a t 2emner matte swoon GEE<br>a 2 rem esomtane —aegunmt eqanee at ote<br>2 SEES nents arate seni it eotnace =<br>@ status elaporan<br>B Logout<br>eK<br><!-- End of picture text -->

Gambar 2.81 Pelaporan Bulanan (Dosen Pembimbing)

Halaman pelaporan bulanan pada sistem Dosen Pembimbing merupakan halaman yang bertujuan untuk memudahkan Dosen Pembimbing dalam melakukan pengecekan laporan bulanan yang telah diajukan oleh Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data-data pelaporan bulanan dengan Mahasiswa bimbingan yang diampuh. Pada halaman ini, Dosen Pembimbing dapat melakukan penerimaan atau penolakan pelaporan bulanan. Jika pelaporan bulanan Mahasiswa ditolak, maka alasan penolakan akan ditampilkan pada halaman ini.

# **2.3.3.28.1 Terima Pelaporan Bulanan**

<!-- Start of picture text -->
Penerimaan Pelaporan Bulanan Berhasil<br>Penerimaan pelaporan bulanan berhasil dilakukan!<br><!-- End of picture text -->

Gambar 2.82 Terima Pelaporan Bulanan

Tampilan terima pelaporan bulanan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Terima” pada data pelaporan bulanan Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data laporan bulanan yang telah diajukan oleh Mahasiswa serta memastikan bahwa laporan tersebut telah sesuai dengan ketentuan yang berlaku. Jika laporan bulanan diterima, status laporan akan berubah menjadi "Diterima" dan akan dikirimkan pada sistem Mahasiswa. Halaman ini berfungsi untuk memudahkan Dosen Pembimbing dalam memantau pelaksanaan MBKM oleh Mahasiswa.

# **2.3.3.28.2 Tolak Pelaporan Bulanan**

<!-- Start of picture text -->
Penolakan Pengecekan Laporan Bulanan<br>sects era<br>=a<br><!-- End of picture text -->

Gambar 2.83 Tolak Pelaporan Bulanan

Tampilan tolak pelaporan bulaan merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Tolak” pada data pelaporan bulanan Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data laporan bulanan yang diajukan oleh Mahasiswa. Dosen Pembimbing juga dapat menginputkan alasan penolakan yang akan ditampilkan pada sistem Mahasiswa. Jika laporan bulanan ditolak maka status laporan akan berubah menjadi "Ditolak" dan alasan penolakan akan dikirimkan ke sistem Mahasiswa untuk pemberitahuan. Halaman ini berfungsi untuk memberi kesempatan pada Mahasiswa untuk melakukan perbaikan atau revisi pada laporan bulanan sesuai dengan alasan penolakan yang telah diberikan oleh Dosen Pembimbing.

# **2.3.3.29 Halaman Pelaporan Akhir (Mahasiswa)**

<!-- Start of picture text -->
@ 7 : xe)<br>as Pelaporan Kegiatan Akhir MBKM -<br>Bq Dashboard sr ron)<br>© informasi kegiatan No JUDULKEGIATANMBKM, es kes toa LOGBOOK ——LAPORANAKKIRMBKM ——_SERTIE<br>B. Pongojuanse 1 mio opttennkes) inte Pore arers om a<br>: :<br>2 Pendattaran<br>@ status kegiatan<br>1© Bimbingan MBKM.<br>1 Laporan Akhir<br>B Logout<br>ox<br>sotona<br><!-- End of picture text -->

Gambar 2.84 Pelaporan Akhir (Mahasiswa)

Halaman pelaporan akhir MBKM merupakan halaman yang dapat digunakan untuk memantau dan mengelola pelaporan kegiatan akhir Mahasiswa pada pelaksanaan akhir MBKM. Pada halaman ini, Mahasiswa dapat mengunggah data-data yang dibutuhkan untuk proses konversi SKS. Jika laporan diterima, maka sistem akan mencatat laporan tersebut sebagai bagian dari dokumentasi kegiatan MBKM dan sebagai proses konversi SKS. Jika laporan ditolak, sistem akan menampilkan alasan penolakan, sehingga Mahasiswa dapat melakukan revisi dan mengunggah laporan akhir kembali. Halaman ini dirancang untuk mendukung transparansi dan efisiensi dalam proses pelaporan akhir MBKM.

<!-- Start of picture text -->
© Form PelaporanKegiatan Akhir MBKM<br>a<br>~ aaa<br>aacme saa<br>— —<br>semen<br>anon — 7<br>ad mosaeemerereweipenaeis<br>see<br>sehen sso<br>safc<br>seneenersnnini anil<br>===)<br><!-- End of picture text -->

Gambar 2.85 _Form_ Pelaporan Akhir

Tampilan _form_ pelaporan akhir merupakan tampilan yang ditampilkan oleh sistem ketika Mahasiswa mengklik button “Buat Laporan”pada halaman pelaporan akhir. Halaman ini berfungsi sebagai sarana bagi Mahasiswa untuk mengunggah data-data yang dibutuhkan untuk proses konversi SKS selama pelaksanaan MBKM.

# **2.3.3.30 Halaman Pelaporan Akhir (Kaprodi dan PIC MBKM)**

<!-- Start of picture text -->
Oo Pelaporan Kegiatan Akhir S<br>Hii Dashboard<br>© ‘formas kegiatan no naa oan oworrusron or cr<br>@ Soloksi sxe<br>@ Pendattoran viong 2 mecententeetm Zemetereminmemins on sro vnonea<br>—<br>& Daftar Mahasiswa<br>‘& Bimbingan MBKM > mane mosseomerrerameaunrarss acne sams tomo<br>Sse rones<br>B logout<br>MoKm<br>deta Put<br><!-- End of picture text -->

Gambar 2.86 Pelaporan Akhir (Kaprodi dan PIC MBKM)

Halaman pelaporan akhir pada sistem Kaprodi dan PIC MBKM merupakan halaman yang ditampilkan oleh sistem untuk menampilkan data laporan akhir yang diajukan oleh Mahasiswa sebagai bukti pendukung dalam pelaksanaan MBKM dan sebagai pengambilan keputusan dalam proses konversi SKS. Pada halaman ini, Kaprodi dan PIC MBKM hanya dapat memantau laporan tanpa melakukan penerimaan atau penolakan terhadap laporan akhir Mahasiswa. Halaman ini juga dapat di _export_ ke dalam file _excel_ sebagai dokumentasi dan bukti pelaksanaan pelaporan akhir Mahasiswa selama program MBKM berlangsung.

# **2.3.3.31 Halaman Pelaporan Akhir (Dosen Pembimbing)**

<!-- Start of picture text -->
@) Pelaporan Kegiatan Akhir MBKM<br>Oi TED No NAMA JUDUL KEGIATAN MBKM ens Rs. oA ‘LooB00K LAPORAN<br>& Mahasiswa Bimbingan a — mer Cc ghar ac ht pory =<br>‘© bimbingan MoKM =<br>GEEEE=D 2 Yepemmocynye —waoeruencon meen por ‘at<br>@ status etoporan<br>B Logout<br>ox<br><!-- End of picture text -->

Gambar 2.87 Pelaporan Akhir (Dosen Pembimbing)

Halaman pelaporan akhir pada sistem Dosen Pembimbing merupakan halaman yang bertujuan untuk memudahkan Dosen Pembimbing dalam melakukan pengecekan laporan akhir yang telah diajukan oleh Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data-data pelaporan akhir dengan Mahasiswa bimbingan yang diampuh. Pada halaman ini, Dosen Pembimbing dapat melakukan penerimaan atau penolakan pelaporan akhir. Jika pelaporan bulanan Mahasiswa ditolak, maka alasan penolakan akan ditampilkan pada halaman ini. Pelaporan akhir ini berfungsi sebagai pengambilan keputusan dalam proses konversi SKS Mahasiswa.

# **2.3.3.31.1 Terima Pelaporan Akhir**

<!-- Start of picture text -->
Penerimaan Pelaporan Akhir Berhasil<br>Penerimaan pelaporan akhir berhasil dilakukan!<br><!-- End of picture text -->

Gambar 2.88 Terima Pelaporan Akhir (Dosen Pembimbing)

Tampilan terima pelaporan akhir merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Terima” pada data pelaporan akhir Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data laporan akhir yang telah diajukan oleh Mahasiswa serta memastikan bahwa laporan tersebut telah sesuai dengan ketentuan yang berlaku. Jika laporan akhir diterima, status laporan akan berubah menjadi "Diterima" dan akan dikirimkan pada sistem Mahasiswa. Halaman ini berfungsi untuk memudahkan Dosen Pembimbing dalam mengambil keputusan pada proses konversi SKS Mahasiswa.

# **2.3.3.31.2 Tolak Pelaporan Akhir**

<!-- Start of picture text -->
Penolakan Pengecekan Laporan Akhir<br>ska tolot Hana<br>anosta015<br>SI Sistem informs<br>Logbook tidak sesuai |<br>cs<br><!-- End of picture text -->

Gambar 2.89 Tolak Pelaporan Akhir (Dosen Pembimbing)

Tampilan tolak pelaporan akhir merupakan tampilan yang ditampilkan oleh sistem ketika Dosen Pembimbing mengklik button “Tolak” pada data pelaporan akhir Mahasiswa. Pada halaman ini, Dosen Pembimbing dapat melihat data laporan akhir yang diajukan oleh Mahasiswa. Dosen Pembimbing juga dapat menginputkan alasan penolakan yang akan ditampilkan pada sistem Mahasiswa. Jika laporan akhir ditolak maka status laporan akan berubah menjadi "Ditolak" dan alasan penolakan akan dikirimkan ke sistem Mahasiswa untuk pemberitahuan. Halaman ini berfungsi untuk memberi kesempatan pada Mahasiswa untuk melakukan perbaikan atau revisi pada laporan akhir sesuai dengan alasan penolakan yang telah diberikan oleh Dosen Pembimbing.

# **2.3.3.32 Halaman** **_Logout_**

Halaman _logout_ pada seluruh sistem dirancang untuk memberikan pengalaman pengguna yang sederhana. Ketika pengguna mengklik menu _logout_ , sistem akan segera mengeluarkan pengguna dari aplikasi tanpa menampilkan _pop up_ konfirmasi. Setelah _logout_ , pengguna akan diarahkan ke halaman _landing page_ , yang berfungsi sebagai halaman pertama yang dapat diakses oleh _user_ untuk melakukan login kembali.

# **2.4 Rencana Pengujian Proyek**

Rencana pengujian proyek pada Proyek Pengembangan Sistem Informasi MBKM di Fakultas Ilmu Komputer UPN “Veteran” Jakarta adalah menggunakan metode _black box testing_ . _Black box testing_ merupakan sebuah teknik pengujian perangkat lunak yang berfokus pada fungsi sistem tanpa memeriksa struktur internal atau kode programnya. Pengujian ini dilakukan dengan memeriksa input dan output sistem untuk memastikan bahwa setiap fungsi berjalan sesuai dengan spesifikasi yang telah ditentukan. Pengujian ini dilakukan bertujuan untuk memastikan bahwa sistem informasi MBKM dapat memenuhi kebutuhan pengguna dengan baik dan berfungsi secara optimal. Adapun skenario dari _black box testing_ pada penelitian ini dapat dilihat pada tabel berikut.

Tabel 2.3 Rencana Pengujian Proyek

|**No**|**Aktor**|**Skenario Pengujian**|**Hasil yang Dih**|**arapkan**|
|---|---|---|---|---|
|||1) Mengakses_landing page._|1) Mahasiswa|dapat|
|||2) Melakukan_login_dengan<br>menggunakan<br>akun<br>SIAKAD.|mengakses_la_<br>2) Mahasiswa<br>melakukan_lo_|_nding page._<br>dapat<br>_gin._|
|||3) Masuk<br>ke<br>dalam|3) Mahasiswa|dapat|
|||_dashboard general._|mengakses|_dashboard_|
|||4) Memilih menu MBKM|_general._||
|||pada_sidebar dashboard_|4) Mahasiswa|dapat|
|1.|Mahasiswa|_general._<br>5) Mengakses<br>_dashboard_<br>MBKM.|memilih me<br>pada_sidebar_<br>_general._|nu MBKM<br>_dashboard_|
|||6) Mengakses<br>informasi|5) Mahasiswa|dapat|
|||kegiatan.|mengakses|_dashboard_|
|||7) Mengajukan<br>Surat|MBKM.||
|||Rekomendasi (SR).|6) Mahasiswa|dapat|
|||8) Melakukan<br>pendaftaran|mengakses|informasi|
|||MBKM<br>Mandiri|kegiatan.||
|||Kerjasama.|||

||9) Melakukan<br>pendaftaran<br>ulang.|7) Mahasiswa<br>mengajukan|dapat<br> <br>Surat|
|---|---|---|---|
||10) Melakukan<br>bimbingan|Rekomenda|si (SR).|
||bulanan dan akhir.|8) Mahasiswa|dapat|
||11) Melakukan<br>pelaporan|melakukan|pendaftaran|
||bulanan dan akhir.|MBKM|Mandiri|
||12) _Logout_|Kerjasama.||
|||9) Mahsiswa<br>melakukan<br>ulang.|dapat<br>pendaftaran|
|||10) Mahasiswa|dapat|
|||melakukan<br>bulanan dan|bimbingan<br>akhir.|
|||11) Mahasiswa<br>melakukan<br>bulanan dan<br>12) Mahasiswa<br>melakukan_l_|dapat<br>pelaporan<br>akhir.<br>dapat<br>_ogout._|
||1) Mengakses_landing page._|1) Kaprodi|dapat|
||2) Melakukan_login_dengan|mengakses_l_|_anding page._|
||menggunakan akun yang|2) Kaprodi|dapat|
||telah di daftarkan oleh<br>admin.|melakukan<br>menggunak|_login_dengan<br>an akun yang|
||3) Masuk<br>ke<br>dalam|telah di da|ftarkan oleh|
|2.<br>Kaprodi|_dashboard general._<br>4) Memilih menu MBKM|admin.<br>3) Kaprodi|dapat|
||pada_sidebar dashboard_<br>_general._|mengakses<br>_general._|_dashboard_|
||5) Mengakses<br>_dashboard_|4) Kaprodi da|pat memilih|
||MBKM.|menu<br>M|BKM<br>pada|
||6) Mengakses<br>halaman|_sidebar_|_dashboard_|
||informasi kegiatan.|_general._||

|7) _Input, edit,_dan_delete_data|5) Kaprodi<br>dapat|
|---|---|
|kegiatan MBKM Flagship|mengakses<br>_dashboard_|
|dan MBKM Mandiri pada|MBKM.|
|halaman<br>informasi|6) Kaprodi<br>dapat|
|kegiatan.|mengakses<br>informasi|
|8) _Approve_<br>data<br>kegiatan|kegiatan.|
|MBKM<br>Mandiri|7) Kaprodi<br>dapat|
|Kerjasama<br>yang|melakukan_input, edit,_|
|diinputkan oleh Mitra pada|dan_delete_pada data|
|halaman<br>informasi|kegiatan<br>MBKM|
|kegiatan.|Flagship<br>dan<br>MBKM|
|9) Melakukan seleksi surat|Mandiri pada halaman|
|rekomendasi pada halaman|informasi kegiatan.|
|seleksi SR.|8) Kaprodi<br>dapat|
|10) Melakukan<br>seleksi|mengapprove<br>data|
|pendaftaran<br>MBKM|kegiatan MBKM Mandiri|
|Mandiri Kerjasama yang|Kerjasama<br>diinputkan|
|telah diseleksi oleh Mitra|oleh Mitra pada halaman|
|pada halaman pendaftaran.|informasi kegiatan.|
|11) Melakukan seleksi dosen|9) Kaprodi<br>dapat|
|pembimbing<br>bagi|melakukan seleksi surat|
|mahasiswa<br>yang<br>telah|rekomendasi<br>pada|
|melakukan daftar ulang|halaman seleksi SR.|
|pada pendaftaran ulang.|10) Kaprodi<br>dapat|
|12) Melihat daftar mahasiswa|melakukan<br>seleksi|
|dari masing-masing dosen|pendaftaran<br>MBKM|
|pembimbing pada halaman|Mandiri Kerjasama yang|
|daftar mahasiswa.|telah diseleksi oleh Mitra|
|13) Melakukan<br>monitor|pada<br>halaman|
|bimbingan yang dilakukan|pendaftaran.|
|oleh Dosen Pembimbing|11) Kaprodi<br>dapat|
|dengan Mahasiswa.|melakukan seleksi dosen<br>pembimbing<br>bagi|

||14) Melakukan<br>pengecekan|mahasiswa yang telah|
|---|---|---|
||pelaporan yang telah di<br>input oleh Mahasiswa.|melakukan daftar ulang<br>pada pendaftaran ulang.|
||15) _Logout._|12) Kaprodi dapat melihat|
|||daftar mahasiswa dari|
|||masing-masing<br>dosen|
|||pembimbing<br>pada|
|||halaman<br>daftar<br>mahasiswa.|
|||13) Kaprodi<br>dapat|
|||melakukan<br>monitor|
|||bimbingan<br>yang|
|||dilakukan oleh Dosen|
|||Pembimbing<br>dengan<br>Mahasiswa.<br>14) Kaprodi<br>dapat|
|||melakukan<br>pengecekan<br>pelaporan yang telah di<br>input oleh Mahasiswa.|
|||15) Kaprodi<br>dapat<br>melakukan_logout._|
||1) Mengakses_landing page._|1) PIC<br>MBKM<br>dapat|
||2) Melakukan_login_dengan|mengakses_landing page._|
||menggunakan akun yang|2) PIC<br>MBKM<br>dapat|
||telah di daftarkan oleh|melakukan_login_dengan|
||admin.|menggunakan akun yang|
|3.<br>PIC MBKM|3) Masuk<br>ke<br>dalam<br>_dashboard general._|telah di daftarkan oleh<br>admin.|
||4) Memilih menu MBKM|3) PIC<br>MBKM<br>dapat|
||pada_sidebar dashboard_|mengakses<br>_dashboard_|
||_general._|_general._|
||5) Mengakses<br>_dashboard_<br>MBKM.|4) PIC<br>MBKM<br>dapat<br>memilih menu MBKM|

|6) Mengakses<br>halaman|pada_sidebar dashboard_|
|---|---|
|informasi kegiatan.|_general._|
|7) _Input_,_edit_, dan_delete_data|5) PIC<br>MBKM<br>dapat|
|kegiatan MBKM Flagship|mengakses<br>_dashboard_|
|dan MBKM Mandiri pada|MBKM.|
|halaman<br>informasi|6) PIC<br>MBKM<br>dapat|
|kegiatan.|mengakses<br>informasi|
|8) _Approve_<br>data<br>kegiatan|kegiatan.|
|MBKM<br>Mandiri|7) PIC<br>MBKM<br>dapat|
|Kerjasama<br>yang|melakukan_input_,_edit_,|
|diinputkan oleh Mitra pada|dan_delete_pada data|
|halaman<br>informasi|kegiatan<br>MBKM|
|kegiatan.|Flagship<br>dan<br>MBKM|
|9) Melakukan seleksi surat|Mandiri pada halaman|
|rekomendasi pada halaman|informasi kegiatan.|
|seleksi SR.|8) PIC<br>MBKM<br>dapat|
|10) Melakukan<br>seleksi|mengapprove<br>data|
|pendaftaran<br>MBKM|kegiatan MBKM Mandiri|
|Mandiri Kerjasama yang|Kerjasama<br>diinputkan|
|telah diseleksi oleh Mitra|oleh Mitra pada halaman|
|pada halaman pendaftaran.|informasi kegiatan.|
|11) Melakukan seleksi dosen|9) PIC<br>MBKM<br>dapat|
|pembimbing<br>bagi|melakukan seleksi surat|
|mahasiswa<br>yang<br>telah|rekomendasi<br>pada|
|melakukan daftar ulang|halaman seleksi SR.|
|pada pendaftaran ulang.|10) PIC<br>MBKM<br>dapat|
|12) Melihat daftar mahasiswa|melakukan<br>seleksi|
|dari masing-masing dosen|pendaftaran<br>MBKM|
|pembimbing pada halaman|Mandiri Kerjasama yang|
|daftar mahasiswa.|telah diseleksi oleh Mitra|
|13) Melakukan<br>monitor|pada<br>halaman|
|bimbingan yang dilakukan|pendaftaran.|

||oleh Dosen Pembimbing|11) PIC<br>MBKM|dapat|
|---|---|---|---|
||dengan Mahasiswa.|melakukan seleks|i dosen|
||14) Melakukan<br>pengecekan|pembimbing|bagi|
||pelaporan yang telah di<br>input oleh Mahasiswa.<br>15) _Logout._|mahasiswa yang<br>melakukan daftar<br>pada pendaftaran<br>12) PIC<br>MBKM<br>melihat daftar mah<br>dari<br>masing-<br>dosen pembimbin<br>halaman<br>mahasiswa.|telah<br>ulang<br>ulang.<br>dapat<br>asiswa<br>masing<br>g pada<br>daftar|
|||13) PIC<br>MBKM|dapat|
|||melakukan<br> <br>bimbingan<br>dilakukan oleh<br>Pembimbing<br>Mahasiswa.<br>14) PIC<br>MBKM|monitor<br>yang<br>Dosen<br>dengan<br>dapat|
|||melakukan<br>peng<br>pelaporan yang t<br>input oleh Mahasi|ecekan<br>elah di<br>swa.|
|||15) PIC<br>MBKM|dapat|
|||melakukan_logout_|_._|
||1) Mengakses_landing page._<br>2) Melakukan_login_dengan<br>menggunakan akun yang|1) Admin dapat men<br>_landing page._<br>2) Admin dapat mel|gakses<br>akukan|
|4.<br>Admin|telah di daftarkan oleh<br>admin_general_.<br>3) Masuk<br>ke<br>dalam<br>_dashboard general._|_login_akun yang t<br>daftarkan<br>oleh<br>_general._<br>3) Admin dapat men<br>_dashboard genera_|elah di<br>admin<br>gakses<br>_l._|

|4) Memilih menu MBKM|4) Admin dapat memilih|
|---|---|
|pada_sidebar dashboard_|menu<br>MBKM<br>pada|
|_general._|_sidebar_<br>_dashboard_|
|5) Mengakses<br>_dashboard_|_general._|
|MBKM.|5) Admin dapat mengakses|
|6) Melakukan seleksi Mitra|_dashboard_MBKM.|
|yang<br>ingin<br>melakukan|6) Admin dapat melakukan|
|kerjasama<br>dengan<br>FIK|seleksi Mitra yang ingin|
|pada<br>halaman<br>seleksi|melakukan<br>kerjasama|
|Mitra.|dengan<br>FIK<br>pada|
|7) Mengakses<br>halaman|halaman seleksi Mitra.|
|informasi kegiatan.|7) Admin dapat mengakses|
|8) _Input_,_edit,_dan_delete_data|informasi kegiatan.|
|kegiatan MBKM Flagship|8) Admin dapat melakukan|
|dan MBKM Mandiri pada|_input, edit,_dan_delete_|
|halaman<br>informasi|pada<br>data<br>kegiatan|
|kegiatan.|MBKM<br>Flagship<br>dan|
|9) _Approve_<br>data<br>kegiatan|MBKM Mandiri pada|
|MBKM<br>Mandiri|halaman<br>informasi|
|Kerjasama<br>yang|kegiatan.|
|diinputkan oleh Mitra pada|9) Admin<br>dapat|
|halaman<br>informasi|mengapprove<br>data|
|kegiatan.|kegiatan MBKM Mandiri|
|10) Melakukan seleksi surat|Kerjasama<br>diinputkan|
|rekomendasi pada halaman|oleh Mitra pada halaman|
|seleksi SR.|informasi kegiatan.|
|11) _Logout._|10) Admin dapat melakukan<br>seleksi surat rekomendasi<br>pada halaman seleksi SR.|
||11) Admin<br>melakukan<br>_logout._|

||1) Mengakses_landing page._|1) Dosen<br>Pembimbing|
|---|---|---|
||2) Melakukan_login_dengan|dapat mengakses_landing_|
||menggunakan akun yang|_page._|
||telah di daftarkan oleh|2) Dosen<br>Pembimbing|
||admin.|dapat melakukan_login_|
||3) Masuk<br>ke<br>dalam|dengan<br>menggunakan|
||_dashboard general._|akun<br>yang<br>telah<br>di|
||4) Memilih menu MBKM|daftarkan oleh admin_._|
||pada_sidebar dashboard_|3) Dosen<br>Pembimbing|
||_general._|dapat<br>mengakses|
||5) Mengakses<br>_dashboard_|_dashboard general._|
||MBKM.|4) Dosen<br>Pembimbing|
||6) Mengakses<br>informasi|dapat<br>memilih<br>menu|
||kegiatan.|MBKM<br>pada<br>_sidebar_|
||7) Melihat daftar mahasiswa|_dashboard general._|
|Dosen|yang<br>dibimbing<br>pada|5) Dosen<br>Pembimbing|
|5.<br> <br>Pbibi|halaman daftar mahasiswa.|dapat<br>mengakses|
|emmng|8) Membuat<br>jadwal|_dashboard_MBKM.|
||bimbingan bulanan dan|6) Dosen<br>Pembimbing|
||akhir<br>pada<br>halaman|dapat<br>mengakses|
||bimbingan.|informasi kegiatan.|
||9) Melakukan<br>pengecekan|7) Dosen<br>Pembimbing|
||pelaporan<br>bulanan<br>dan|dapat<br>melihat<br>daftar|
||akhir<br>pada<br>halaman|mahasiswa<br>yang|
||pelaporan.|dibimbing pada halaman|
||10) _Logout._|daftar mahasiswa.|
|||8) Dosen<br>Pembimbing|
|||dapat membuat jadwal|
|||bimbingan bulanan dan|
|||akhir<br>pada<br>halaman|
|||bimbingan.|
|||9) Dosen<br>Pembimbing|
|||dapat<br>melakukan|

|||pengecekan<br>pelaporan<br>bulanan dan akhir pada<br>halaman pelaporan.<br>10) Dosen<br>Pembimbing<br>dapat melakukan_logout._|
|---|---|---|
||1) Mengakses_landing page._<br>2) Melakukan registrasi Mitra<br>untuk bekerjasama dengan<br>FIK pada_sidebar_MBKM|1) Mitra dapat mengakses<br>_landing page._<br>2) Mitra dapat melakukan<br>registrasi Mitra untuk|
||pada<br>halaman<br>_landing_|bekerjasama dengan FIK|
||_page_.|pada<br>_sidebar_<br>MBKM|
||3) Melakukan_login_dengan<br>menggunakan akun yang<br>telah didaftarkan.|pada halaman_landing_<br>_page_.<br>3) Mitra dapat melakukan|
||4) Masuk<br>ke<br>dalam<br>_dashboard_MBKM.<br>5) Mengakses<br>halaman|_login_<br>dengan<br>menggunakan akun yang<br>telah didaftarkan._._|
||informasi kegiatan.|4) Mitra dapat mengakses|
|6.<br>Mitra|6) _Input_,_edit_, dan_delete_data<br>kegiatan MBKM Mandiri<br>Kerjasama pada halaman|_dashboard_MBKM.<br>5) Mitra dapat mengakses<br>informasi kegiatan.|
||informasi kegiatan.|6) Mitra dapat melakukan|
||7) Melakukan<br>seleksi|input, edit, dan delete|
||pendaftaran<br>MBKM|pada<br>data<br>kegiatan|
||Mandiri Kerjasama pada|MBKM<br>Mandiri|
||halaman seleksi MBKM.|Kerjasama pada halaman|
||8) Melihat daftar mahasiswa|informasi kegiatan.|
||yang mendaftar di Mitra|7) Mitra dapat melakukan|
||yang bersangkutan.|seleksi<br>pendaftaran|
||9) _Logout._|MBKM<br>Mandiri<br>Kerjasama pada halaman<br>seleksi MBKM.|

|8)|Mitra<br>dapat<br>melihat|
|---|---|
||daftar mahasiswa yang|
||mendaftar di Mitra yang|
||bersangkutan.|
|9)|Mitra dapat melakukan|
||_logout._|


# PROYEK: PENGEMBANGAN DASHBOARD BUSINESS INTELLIGENCE PADA FAKULTAS ILMU KOMPUTER UNIVERSITAS PEMBANGUNAN NASIONAL VETERAN JAKARTA

# **BAB II**

# **RANCANGAN PROYEK**

# **2.1 Observasi**

Pada bagian observasi ini akan menjelaskan bagaimana sistem yang selama ini berjalan pada Fakultas Ilmu Komputer dalam memahami alur kerja, data yang digunakan, serta aktor yang berperan dalam pengelolaan data untuk mencapai sebuah hasil keputusan bisnis bagi fakultas. Selain itu, dilakukan identifikasi masalah berdasarkan analisis sistem yang berjalan yang akan menjadi dasar pengembangan _dashboard business intelligence_ untuk solusi yang lebih efisien. Adapun penjelasannya, dijelaskan pada bagian berikut.

# **2.1.1 Diagram Sistem Berjalan**

Pada tahapan ini dilakukan penggambaran skema terkait dengan sistem pengambilan keputusan yang dilakukan oleh Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Penggambaran ini dilakukan dikarenakan fakultas saat ini belum memiliki alur resmi terkait dengan pengambilan keputusan bisnisnya. Dengan demikian, berdasarkan hasil wawancara yang dilakukan dengan koordinator akademik dan kemahasiswaan, Fakultas Ilmu Komputer masih menggunakan sistem yang memakai data statis untuk melakukan pengambilan keputusan. Adapun penggambaran alur pengambilan keputusan yang dimiliki oleh Fakultas Ilmu Komputer tergambar pada gambar 2.1 berikut.

<!-- Start of picture text -->
+<br><!-- End of picture text -->

Gambar 2. 1 _Flowchart_ Sistem Berjalan

Gambar 2.1 di atas menunjukkan alur kerja dalam pengumpulan, pengelolaan, dan pelaporan data akademik di Fakutas Ilmu Komputer UPN “Veteran” Jakarta. Proses dimulai dengan pengumpulan data mahasiswa oleh Staf Administrasi Kemahasiswaan yang kemudian dikirimkan ke Staf Akademik. Staf Akademik bertanggung jawab untuk mengumpulkan data akademik, melakukan proses pembersihan data, dan mengelola data mahasiswa serta akademik secara manual. Setelah data diolah, Staf Akademik akan menyusun laporan performa mahasiswa dalam bentuk dokumen dan menyerahkannya kepada Koordinator Program Studi. Koordinator Program Studi kemudian melakukan evaluasi terhadap data yang telah dilaporkan dan menyampaikan hasil evaluasi tersebut kepada Pimpinan Fakultas yaitu Dekan dan Wakil Dekan. Di tingkat Pimpinan Fakultas, hasil evaluasi digunakan untuk melakukan evaluasi lebih lanjut dan membentuk keputusan bisnis terkait pengelolaan program studi dan mahasiswa.

# **2.1.1.1 Identifikasi Masalah**

Dalam melakukan identifikasi masalah terhadap sistem pengambilan keputusan untuk _Business Intelligence_ bagi Fakultas Ilmu Komputer UPN “Veteran” Jakarta, penulis menggunakan analisis metode PIECES yang sebagaimana hasilnya terdapat pada tabel 2.1 berikut.

Tabel 2. 1 Identifikasi Masalah dengan Metode PIECES

|**Aspek PIECES**|**Proses**|**Identifikasi**<br>**Masalah**|**Deskripsi**|**Masalah**|
|---|---|---|---|---|
|**_Performance_**|Pengumpulan|Kinerja lambat|Pengumpulan|<br>data|
||Data|akibat|mahasiswa s|ecara manual|
||Mahasiswa|ketergantungan|menghambat|kinerja staf|
|||pada<br>proses<br>manual|dan mengura<br>proses input|ngi kecepatan<br>data. Hal ini|
||||dikarenakan|staf<br>harus|
||||mengekstraks|i<br>data|
||||mentah dari b|erbagai tabel|
||||sistem,|melakukan|
||||pembersihan|<br>data,<br>dan|

|menyusun laporan tanpa|
|---|
|bantuan<br>alat<br>otomatis.|
|Proses<br>ini<br>melibatkan|
|banyak langkah manual|
|seperti melakukan_query_|
|berulang,<br>memeriksa|
|format<br>data,<br>dan|
|mengkompilasi data ke|
|dalam<br>bentuk<br>laporan|
|yang<br>dapat<br>dimengerti|
|pimpinan. Selain itu, staf|
|akademik juga mengalami|
|kesulitan<br>dalam|
|pemahaman<br>terhadap|
|tabel-tabel<br>yang<br>tidak|
|familiar<br>sehingga|
|menyebabkan<br>pekerjaan|
|sering<br>tertunda.|
|Berdasarkan pengalaman,|
|penyusunan laporan data|
|mahasiswa<br>untuk|
|pengambilan<br>keputusan|
|biasanya<br>membutuhkan|
|waktu sekitar 2–3 hari|
|kerja untuk satu laporan|
|bulanan,<br>padahal|
|seharusnya<br>bisa|
|diselesaikan dalam 1 hari|
|jika sistem lebih efisien.|
|Indikasi<br>bahwa<br>proses|
|input<br>menjadi<br>lambat|
|terlihat dari banyaknya|

||||laporan yang baru selesai<br>mendekati tenggat rapat<br>bulanan<br>dan<br>adanya<br>keluhan pimpinan yang<br>harus<br>menunggu<br>data<br>selesai<br>diolah<br>sebelum<br>dapat<br>mengambil<br>keputusan.|
|---|---|---|---|
|**_Information_**|Pengelolaan<br>Data<br>Akademik<br>dan<br>Mahasiswa<br>serta<br>data<br>pembayaran<br>UKT|Keterbatasan<br>informasi yang<br>dapat<br>diakses<br>_real-time_|Data<br>akademik<br>dan<br>mahasiswa dikelola secara<br>manual,<br>sehingga<br>informasi_real-time_tidak<br>tersedia untuk keperluan<br>evaluasi dan pengambilan<br>keputusan. Sementara data<br>pembayaran UKT yang<br>tidak bisa sepenuhnya bisa<br>diakses oleh Koordinator<br>Tata Usaha menyebabkan<br>informasi<br>mengenai<br>pembayaran UKT tidak<br>tersedia secara_real-time_<br>untuk dievaluasi karena<br>diperlukan<br>pengambilan<br>data dari sistem keuangan<br>universitas.|
|**_Economy_**|Penyusunan<br>Laporan|Biaya<br>waktu<br>dan<br>tenaga<br>tinggi<br>untuk<br>penyusunan<br>laporan manual|Proses<br>penyusunan<br>laporan<br>secara<br>manual<br>membutuhkan waktu lama<br>dan sumber daya staf yang<br>lebih<br>banyak,<br>mengakibatkan inefisiensi|

||||biaya. Inefisiensi biaya ini|
|---|---|---|---|
||||terjadi<br>karena<br>proses<br>manual<br>membutuhkan|
||||lebih banyak tenaga dan<br>waktu kerja staf untuk|
||||menyusun<br>laporan,|
||||sehingga<br>biaya|
||||operasional<br>meningkat|
||||dibanding<br>jika|
||||menggunakan sistem yang|
||||lebih<br>cepat.<br>Hal<br>ini|
||||diketahui dari banyaknya|
||||jam kerja yang terpakai|
||||hanya<br>untuk<br>tugas|
||||pengolahan<br>data,<br>yang|
||||seharusnya<br>bisa|
||||dialokasikan ke pekerjaan|
||||lain jika proses sudah|
||||otomatis. Beban waktu|
||||kerja yang panjang untuk|
||||menyelesaikan<br>laporan<br>juga menunjukkan adanya<br>pemborosan biaya tenaga<br>kerja.|
|**_Control_**|Proses|Minim kontrol|Proses pembersihan data|
||Pembersihan|untuk menjaga|manual kurang terstandar,|
||Data|kualitas<br>dan|meningkatkan<br>risiko|
|||konsistensi|kesalahan<br>dan|
|||data|inkonsistensi data yang|
||||berpotensi mempengaruhi|
||||laporan<br>akhir.|
||||Inkonsistensi data yang|

||||dimaksud terjadi ketika|
|---|---|---|---|
||||hasil pembersihan data|
||||manual<br>menghasilkan|
||||nilai atau format yang<br>berbeda-beda untuk data<br>yang seharusnya seragam.<br>Sebagai contoh, dalam|
||||satu laporan ditemukan<br>perbedaan penulisan status<br>mahasiswa<br>(“Aktif”,<br>“aktif”, atau “AKTIF”).|
||||Hal ini disebabkan oleh|
||||kurangnya standar baku|
||||dan kontrol yang ketat|
||||dalam<br>proses<br>pembersihan,<br>sehingga<br>data akhir tidak konsisten<br>dan<br>berpotensi<br>menyesatkan pengambilan<br>keputusan.|
|**_Efficiency_**|Pengiriman|Proses|Pengiriman data antar staf|
||Data|pengiriman|dilakukan secara manual,|
||Mahasiswa|data<br>antar|yang<br>memperlambat|
|||divisi<br>tidak|waktu<br>proses<br>dan|
|||efisien|menambah<br>potensi|
||||keterlambatan<br>dalam<br>evaluasi data. Lambatnya<br>pengiriman data antar staf<br>pada umumnya memakan<br>waktu 1–2 hari karena data|
||||harus dikompilasi, dicek|
||||ulang,<br>lalu<br>dikirimkan|

||||melalui<br>_email_<br>atau|
|---|---|---|---|
||||dokumen<br>cetak<br>secara|
||||bergantian.<br>Hal<br>ini|
||||memperlambat<br>karena|
||||sering<br>terjadi<br>antrean|
||||pekerjaan, kesalahan saat|
||||pengecekan yang perlu<br>diperbaiki,<br>dan<br>keterbatasan waktu staf<br>yang harus membagi fokus<br>dengan tugas lain. Selain<br>itu,<br>apabila<br>terdapat<br>koreksi atau revisi, proses<br>pengiriman ulang semakin<br>menambah durasi hingga<br>laporan<br>akhir<br>siap<br>dievaluasi.|
|**_Service_**|Evaluasi oleh|Keterbatasan|Pimpinan Fakultas dan|
||Koordinator|layanan|Koordinator<br>Program|
||Program|evaluasi<br>dan|Studi<br>membutuhkan|
||Studi<br>dan|pengambilan|evaluasi data yang cepat|
||Pimpinan|keputusan|dan<br>akurat<br>untuk|
||Fakultas|berbasis<br>data|bimbingan<br>akademik,|
|||_real-time_|namun saat ini hanya|
||||tersedia<br>laporan<br>statis.|
||||Laporan statis ini dapat<br>berdampak pada kualitas<br>layanan (_service_) karena<br>pimpinan hanya menerima<br>data dalam bentuk tabel|
||||atau dokumen tetap yang|
||||tidak<br>dapat<br>langsung|

|diolah atau|difilter sesuai|
|---|---|
|kebutuhan|saat rapat atau|
|bimbingan.|<br>Hal<br>ini|
|membuat p|roses evaluasi|
|menjadi|lambat<br>dan|
|kurang resp|onsif terhadap|
|pertanyaan|atau analisis|
|mendalam|yang|
|diperlukan,|<br>sehingga|
|layanan|bimbingan|
|akademik|yang|
|seharusnya|cepat dan tepat|
|justru terha|mbat.|

Tabel 2.1 di atas menggambarkan berbagai masalah dalam proses yang ada berdasarkan analisis PIECES. Setiap aspek menunjukkan area yang memerlukan perbaikan, seperti meningkatkan kecepatan kinerja _(Performance)_ , menyediakan akses informasi _real-time (Information)_ , serta mengurangi ketergantungan pada input manual yang memakan waktu _(Efficiency)_ .

# **2.1.2 Solusi Penyelesaian Masalah**

Berdasarkan identifikasi permasalahan pada sistem pengambilan keputusan yang sedang berjalan pada Fakultas Ilmu Komputer UPN “Veteran” Jakarta yang dianalisis dengan menggunakan metode PIECES, dapat disimpulkan bahwa diperlukan sebuah pengembangan dan penerapan sistem _dashboard Business Intelligence_ yang terintegrasi. _Dashboard_ ini nantinya akan dirancang untuk meningkatkan kinerja pemantauan, menyediakan akses informasi yang _real-time_ , mengurangi biaya operasional, mempercepat proses penyusunan laporan, dan memberikan layanan yang lebih efektif kepada pimpinan fakultas dalam pengambilan keputusan. Solusi ini merupakan rekomendasi yang diajukan berdasarkan hasil identifikasi masalah dan belum diimplementasikan pada penelitian ini. Diharapkan rekomendasi ini dapat memaksimalkan efisiensi dan efektivitas pengelolaan data, serta memberikan nilai tambah dalam proses evaluasi

akademik dan manajemen fakultas secara keseluruhan. Detail dari rekomendasi solusi tersebut terdapat pada Tabel 2.2 berikut.

Tabel 2. 2 Tabel Solusi Penyelesaian Masalah

|**Aspek PIECES**|**Identifikasi**<br>**Masalah**|**Solusi**|**Deskripsi**|**Solusi**|
|---|---|---|---|---|
|**_Performance_**|Tidak<br>ada<br>pemantauan_real-_|Mengembangkan<br>fitur<br>pemantauan|Sistem BI<br>memiliki|akan<br>fitur|
||_time_<br>terhadap<br>status<br>keaktifan<br>mahasiswa|_real-time_<br>dalam<br>dashboard BI|pemantauan<br>status mah<br>secara_rea_<br>sehingga<br> <br>pemantauan<br>responsif.|<br>asiswa<br>_l-time_,<br>proses<br>lebih|
|**_Information_**|Informasi terkait<br>data mahasiswa,<br>status akademik,<br>dan<br>data<br>pembayaran UKT<br>tidak_up-to-date_|Mengintegrasikan<br>sistem BI dengan<br>sumber<br>data<br>internal<br>fakultas<br>yang<br>diperbarui<br>secara berkala|Sistem BI<br>menarik dat<br>berbagai s<br>secara<br>ot<br>untuk<br>memastikan<br>informasi<br>tersedia<br>terkini.|akan<br>a dari<br>umber<br>omatis<br> <br>yang<br>selalu|
|**_Economy_**|Penggunaan<br>biaya lebih tinggi<br>karena<br>pengelolaan data<br>manual|Mengotomatisasi<br>proses<br>pengumpulan dan<br>pengelolaan<br>data<br>melalui sistem BI|Sistem BI<br>mengurangi<br>kebutuhan<br>manual<br>pengumpul<br>data,<br>se<br>menekan<br>operasional<br>waktu.|akan<br> <br>tenaga<br>untuk<br>an<br>hingga<br>biaya<br> <br>dan|

|**_Control_**|Terbatasnya|Menambahkan|Sistem<br>akan|
|---|---|---|---|
||kontrol<br>akses|fitur kontrol akses|memiliki sistem|
||pada data sensitif|yang<br>terstruktur<br>dalam<br>_dashboard_<br>BI|login dan kontrol<br>akses<br>berbasis<br>peran<br>_(role-_<br>_based),_sehingga<br>data hanya dapat<br>diakses<br>oleh<br>pihak<br>yang<br>berwenang.|
|**_Efficiency_**|Penyusunan<br>laporan<br>yang|Menyediakan fitur<br>penyusunan|Sistem<br>akan<br>menghasilkan|
||memakan waktu<br>lama karena tidak<br>terotomatisasi|laporan<br>otomatis<br>dalam<br>_dashboard_<br>BI|laporan<br>secara<br>otomatis<br>berdasarkan data<br>yang<br>masuk,<br>mengurangi<br>waktu<br>yang<br>diperlukan untuk<br>laporan manual.|
|**_Service_**|Layanan laporan<br>yang terbatas dan|Mengembangkan<br>dashboard<br>yang|_Dashboard_akan<br>memberikan|
||tidak mendukung<br>pengambilan|interaktif<br>dan<br>dilengkapi|visualisasi<br>data<br>yang<br>mudah|
||keputusan<br>yang|visualisasi<br>data|dipahami<br>dan|
||cepat|untuk pimpinan|mendukung<br>pengambilan|
||||keputusan<br>yang<br>cepat<br>dan<br>informatif.|

# **2.2 Usulan Solusi**

Pada bagian ini penulis mengusulkan solusi berupa diagram alur _(data flow diagram)_ yang mampu memberikan gambaran terkait dengan bagaimana alur data dalam sistem secara terstruktur. Seperti yang dijelaskan dalam buku yang berjudul _“Data Flow Diagrams”_ , _Data Flow Diagram_ (DFD) merupakan sebuah model logikal data dalam sebuah sistem yang menunjukkan bagaimana batasan, proses, entitas data dalam suatu sistem saling berkaitan secara logika sehingga mampu memberikan detail ringkasan dan susunan informasi terkait dengan sistem tersebut (Davis, 2020). Selain itu menurut jurnal yang berjudul _“Detecting violations of access control and information flow policies in data flow diagrams”_ , DFD menjadi sebuah notasi model yang berfokus pada esensial dan aspek fungsionalitas yang biasanya ditemukan dalam perancangan awal desain pada suatu _software_ (Seifermann et al., 2022). Dengan demikian, _data flow diagram_ menjadi suatu komponen penting yang diperlukan dalam suatu perancangan sistem agar memberikan gambaran alur terhadap data yang mengalir dalam sistem secara sistematis, jelas, dan terarah.

Bagian ini akan memberikan penggambaran usulan solusi melalui _data flow diagram_ 0 dan _data flow diagram_ 1 yang dibentuk sesuai dengan kebutuhan dari sistem. Adapun penjelasan dari masing-masing bagian tersebut tertera pada penjelasan berikut.

# **2.2.1** **_Data Flow Diagram_**

Bagian ini merupakan bagian yang menggambarkan aliran data di dalam sistem melalui alat visual. _Data Flow Diagram_ akan menampilkan bagaimana data bergerak dari satu proses ke proses lainnya, interaksi antar entitas, baik pengguna maupun sistem eksternal, serta penyimpanan data yang digunakan dalam sistem. Pada pengembangan _dashboard_ , DFD akan membantu memetakan alur informasi dari input data hingga pengelolaannya menjadi sebuah _output_ visualisasi yang ditampilkan dalam _dashboard_ , serta memastikan bahwa setiap proses data terstruktur dan efisien. Dalam penelitian ini, digunakan dua _data flow diagram_ , yaitu DFD 0 dan DFD 1, dimana diagram ini akan menjelaskan bagaimana alur data yang diperoleh berjalan dalam sistem. Adapun DFD 0 dan DFD 1 dalam proyek

pengembangan _dashboard business intelligence_ pada Fakultas Ilmu Komputer UPN "Veteran" Jakarta ini dapat dilihat pada penjelasan berikut.

# **2.2.1.1.** **_Data Flow Diagram 0_**

<!-- Start of picture text -->
DataKemahasiswaanAkademikdan<br>c<br>3<br>:<br>era|id<br>pele 2) ———,<br>Beseg¢68 8 g@Gs Data Keuangan19% ‘4<br>g2533 242 Mahasiswa :<br>23442 288 5<br>eiahz @ Date uxt H<br>ze Eas 2| 8<br>asale ee |e<br>oaR| 2 7z3?<br>FAH eS —>|oastooar8 ee<br>Lsa Data Mentah —Datapata Status uxMahasisw eeeR55e<br>g83<br>if —_ 2a 2<br>Bee<br>Sub Kocedinator Bidang VisuaisasiLaporan DashboardHasil | VisualsasiDachboardLaporan Hasi | PinpinanFlutas saeaa8<br>Akademi dan Kemabasinvaanat Oneant ‘2 a=;<br>Laporan Hasil Laporan Hasil =:<br>i LL<br><!-- End of picture text -->

Gambar 2. 2 _Data Flow Diagram 0_

Pada _Data Flow Diagram_ (DFD) Level 0 di atas, tergambar secara menyeluruh bagaimana alur data dalam sistem _Dashboard Business Intelligence_ (BI) dikembangkan dan dikelola. Proses dimulai dari pengumpulan berbagai jenis data mentah yang berasal dari dua sumber utama, yaitu Data Akademik dan Kemahasiswaan serta Data Keuangan Mahasiswa. Data akademik dan kemahasiswaan mencakup informasi-informasi data seperti data mahasiswa belum isi KRS, data perolehan nilai mahasiswa, data mahasiswa melebihi periode studi, data mahasiswa cuti, dan data status mahasiswa (aktif, nonaktif, cuti, lulus, keluar, dan _drop out_ ) yang nantinya data ini akan ditampung pada _data store_ Data Mentah. Di sisi lain, data keuangan mahasiswa mencakup informasi tentang data tunggakan UKT, data mahasiswa mengajukan KIPK dan KJMU, data distribusi golongan UKT Mahasiswa, dan data mahasiswa mengajukan cicilan UKT, penurunan UKT,

maupun pemotongan 50% yang nantinya juga data-data ini akan ditampung pada _data store_ Data Mentah.

Seluruh data mentah tersebut terlebih dahulu diolah ke dalam sistem _Dashboard_ BI. Dalam sistem ini, data akan diolah, dianalisis, dan divisualisasikan agar bisa disajikan dalam bentuk laporan yang informatif. Visualisasi ini mencakup berbagai jenis data yang diantaranya berupa data nilai, data KRS, data UKT, dan data status mahasiswa. Selanjutnya, hasil dari proses visualisasi tersebut dikemas menjadi Laporan Hasil Visualisasi _Dashboard_ , yang didistribusikan kepada berbagai pemangku kepentingan di lingkungan fakultas. Pihak-pihak yang menjadi pengguna utama dari laporan ini meliputi Pimpinan Fakultas (Dekan dan Wakil Dekan), Koordinator Program Studi, Sub Koordinator Bidang Akademik dan Kemahasiswaan, serta Koordinator Tata Usaha. Melalui akses terhadap _dashboard_ ini, mereka dapat memantau kondisi akademik dan keuangan mahasiswa secara lebih menyeluruh, sehingga dapat digunakan sebagai dasar pertimbangan dalam pengambilan keputusan strategis di tingkat fakultas.

# **2.2.1.2.** **_Data Flow Diagram 1_**

<!-- Start of picture text -->
‘ata Status Mahaiowa (Akt Non Akt Luts, Kalua, Drop Out<br>Data Mahasiowa<br>Nis Mabaso<br>Data Belum Is KRS-<br>‘tsMahasiosWels Pode<br>ata ManasionaC<br>‘Sub Koordinator Bidang_ Dats Status Mahasinwa<br>‘Alslemkda © Data Akademik STAT<br>Kemahasiswaan dan Mahasiswa eT<br>5H << ont vit —<br>7 1 Dass Ks<br>Ha 1. PengumpulanData aData Ni Data Mentah<br>ava: as uxt<br>ie CGoeknamnData Keuangan SY<—————3<br>Data Mentah Mahasiswa $———z 3x<br>z gla5 aia:<br>3 Beeg SE& a<br>a 238 2. Pembersihan c2sis<br>A : dan Pengolahan oe a<br>i a — BE Ess<br>3 g Daa egies<br>z t gage<br>&5 gabea 48:<br>Daa Beh qiae<br>a Koordinator Tata a<br>Cleaned Data ‘Usaha<br>bata Bosh |<br>Leporan Viualeai Dashboard<br>3. Penyajian Data<br>Laporan Visuaisasi Dashboard<br>Laporan Visualisasi Dashboard Pimpinan Fakultas<br>Koordinator‘StudiProgram (DekanDekan)dan Wakil<br><!-- End of picture text -->

Gambar 2. 3 _Data Flow Diagram 1_

_Data Flow Diagram_ (DFD) Level 1 di atas merupakan perluasan dari DFD Level 0, yang menggambarkan bagaimana proses pengolahan data berjalan secara sistematis dalam pengembangan _dashboard Business Intelligence_ (BI). Proses dimulai dari Sub Koordinator Bidang Akademik dan Kemahasiswaan yang menyediakan berbagai jenis data terkait mahasiswa, seperti data status mahasiswa (aktif, nonaktif, lulus, keluar, drop out), data mahasiswa cuti, data mahasiswa belum isi KRS, data mahasiswa melebihi masa periode studi, serta data perolehan nilai mahasiswa. Di sisi lain, data keuangan mahasiswa seperti data tunggakan UKT, data mahasiswa mengajukan KIPK dan KJMU, data distribusi golongan UKT

mahasiswa, serta data mahasiswa mengajukan cicilan UKT, penurunan UKT, dan Pemotongan 50%. Semua data yang diterima akan dikategorikan sebagai data mentah, yang kemudian masuk ke tahap pertama dalam sistem, yaitu Pengumpulan Data. Dalam tahap ini, sistem akan mengintegrasikan data dari berbagai sumber menjadi satu kesatuan. Data yang telah terkumpul kemudian diteruskan ke proses kedua, yaitu Pembersihan dan Pengolahan Data. Melalui tahapan pembersihan dan pengolaan data ini, data mentah yang sebelumnya masih campur aduk akan dibersihkan dari duplikasi, ketidaksesuaian, atau kesalahan entri, lalu diolah agar menjadi data bersih _(cleaned data)_ yang siap digunakan.

Setelah melalui proses pembersihan, data bersih masuk ke tahap ketiga, yaitu Penyajian Data. Di tahap inilah data divisualisasikan ke dalam bentuk laporan interaktif yang disusun dalam _dashboard_ BI. Laporan visualisasi _dashboard_ ini selanjutnya didistribusikan kepada para pemangku kepentingan, seperti Pimpinan Fakultas (Dekan dan Wakil Dekan), Koordinator Program Studi, Koordinator Tata Usaha, serta kembali ke Sub Koordinator Bidang Akademik dan Kemahasiswaan. Laporan ini berfungsi sebagai bahan analisis dan evaluasi untuk mendukung proses pengambilan keputusan strategis berbasis data di tingkat fakultas.

# **2.2.2 Arsitektur** **_Dashboard_**

Pada bagian ini akan dijelaskan terkait dengan bagaimana rancangan arsitektur _dashboard_ yang akan dibentuk. Rancangan arsitektur ini mencakup pada lapisan-lapisan terkait dengan pengumpulan data, pemrosesan ETL pada data, penyimpanan data, serta visualisasinya. Adapun gambaran terkait dengan arsitektur _dashboard_ ini dapat dilihat pada gambar 2.4 berikut.

<!-- Start of picture text -->
Crarsaranes] | Frontena”<br>—<br>Data Visualization & Business Rules Layer<br>unt aan<br>: Bi Data Mart Layer :<br>: Ut aan : —_<br>:4 eS |janesiswe : Postgresql)Database<br>:: |g Data Layer & |“comoencomponan<br>: UKT dan i<br>:py [Sanemetasora][Dwaaesive] | aweungatin | [ers] :<br>: :<br>encpnt csv<br>rs extn)<br><!-- End of picture text -->

Gambar 2. 4 Arsitektur _Dashboard_

Gambar 2.4 menunjukkan arsitektur _dashboard_ yang dirancang untuk mengembangkan _dashboard business intelligence_ pada Fakultas Ilmu Komputer. Terdapat berbagai lapisan _(layer)_ yang memiliki fungsi dan proses yang berbeda. Pada lapisan pertama yaitu _Curation Layer_ yang dimana bertanggung jawab untuk mengumpulkan, membersihkan, dan memvalidasi data mentah dari berbagai sumber sebelum digunakan lebih lanjut. Data diambil dari dua sumber utama yaitu _Endpoint_ yang berasal UPA TIK dan _file_ CSV (sebagai _backup_ atau data manual dari Koordinator Akademik dan Kemahasiswaan). Pada bagian ini, data dikumpulkan secara periodik, diperiksa konsistensinya, disesuaikan formatnya, dan dipersiapkan untuk dimasukkan ke dalam layer berikutnya. Hal ini bertujuan untuk memastikan bahwa data yang masuk sudah layak pakai, lengkap, dan tidak cacat.

Setelah melalui proses kurasi, data disimpan terlebih dahulu di _Core Data Layer_ . _Layer_ ini berfungsi sebagai gudang data yang menyimpan data mentah namun sudah bersih ( _cleaned_ ), masih lengkap dan detail, serta belum dioptimalkan untuk analitik. Data di sini masih berbentuk _normalized_ dan mirip dengan database operasional, tetapi sudah konsisten dan aman untuk dijadikan basis bagi transformasi lebih lanjut. Selain itu, terdapat proses _Extract, Transform,_ dan _Load_

(ETL) yang terjadi ketika data telah divalidasi dan disiapkan untuk disimpan di _Core Data  Layer_ . Tahapan ETL ini menjadikan data yang berasal dari berbagai sumber diekstrak dari _staging area_ atau hasil kurasi, lalu ditransformasikan ke dalam bentuk yang seragam dan terstruktur. Data hasil dari ETL ini berperan sebagai _single source of truth_ , aman untuk audit, pelacakan histori transaksi, serta menjadi dasar bagi transformasi lebih lanjut ke layer analitik seperti _BI Data Mart Layer_ . Dengan demikian, proses ETL pada _Core Data Layer_ memastikan data yang tersimpan tidak hanya bersih dan konsisten, tetapi juga tetap lengkap dan dapat ditelusuri hingga ke detail terkecil.

Selanjutnya data diproses menjadi lebih sederhana, ringkas, dan agregatif di _BI Data Mart Layer_ . Di lapisan ini data sudah diolah untuk siap pakai oleh _dashboard_ dengan _query_ yang cepat dan ringan. Data pada _layer_ ini menunjukkan tabel yang berisi rekapitulasi seperti total mahasiswa aktif per prodi, rata-rata IPK per angkatan, jumlah tunggakan UKT per semester, dan lain-lain. Proses di _layer_ ini biasanya dijalankan oleh _store procedure_ yang dijadwalkan, seperti mingguan atau bulanan, untuk memastikan data tetap segar sesuai kebutuhan pemangku kepentingan.

Lapisan berikutnya adalah _Data Visualization & Business Rules Layer_ , yang merupakan jembatan antara data dan pengguna. Lapisan ini mengambil data dari _BI Data Mart_ yang kemudian menerapkan aturan bisnis _(business rules)_ seperti definisi mahasiswa aktif atau cuti, dan memformat data sesuai kebutuhan tampilan. Pada lapisan ini data sudah dipecah-pecah menjadi komponen visual yang lebih spesifik seperti Status Mahasiswa, Nilai Mahasiswa, UKT & Tunggakan Mahasiswa, dan KRS. Proses ini penting untuk memastikan bahwa data yang ditampilkan di _dashboard_ konsisten dengan kebijakan kampus dan mudah dipahami.

Lapisan paling atas adalah _Front-end/UI Component_ , yang merupakan lapisan yang berinteraksi langsung dengan pengguna melalui _web browser_ . Komponen ini terdiri dari _Control Panel_ yang berfungsi untuk memilih _filter_ , periode, dan parameter lainnya _, Information Panel_ yang berfungsi untuk _insight_ cepat dan ringkasan _statistik_ , serta _Charts & Tables Panel_ yang berfungsi untuk grafik, tabel, dan detail data. Data yang sudah diformat oleh _business rules layer_ ditampilkan di sini secara interaktif, dengan kemampuan _drill-down_ , _filter dinamis_ ,

dan _update real-time/semi real-time_ . Fungsi utama lapisan ini adalah menyajikan informasi yang relevan, tepat, dan menarik bagi pemangku kepentingan untuk mendukung proses pengambilan keputusan.

# **2.3 Rancangan Proyek**

Bagian rancangan proyek ini akan menjelaskan terkait dengan analisis kebutuhan yang diperlukan selama pengembangan sistem _dashboard_ yang dimana berhubungan dengan bagaimana kebutuhan pengguna terkait pengalaman dan antarmuka pengguna diidentifikasi, dianalisis, dan diterjemahkan menjadi sebuah desain sistem yang efektif. Hal-hal yang diperlukan dalam analisis kebutuhan ini diantaranya berupa kebutuhan analisis pada komponen interaksi antara sistem dengan pengguna yang meliputi _Need Analysis User Interface_ , _Need Analysis User Experience_ , serta tampilan UI/UX _Design_ . Tahapan ini diperlukan untuk memudahkan pengembang sistem dalam memastikan rancangan sistem telah sesuai dengan apa yang dibutuhkan oleh pengguna dan mencakup fitur yang mampu membantu pengguna nantinya selama berinteraksi dengan _website_ . Adapun penjelasan terkait dengan kebutuhan analisis rancangan proyek ini adalah sebagai berikut.

# **2.3.1** **_Need Analysis User Interface_**

Bagian ini berfokus pada aspek visual dan interaktif dari _dashboard business intelligence_ . Melalui analisis kebutuhan ini, penulis nantinya dapat membuat antarmuka yang intuitif, mudah digunakan, serta menarik secara visual untuk seluruh  aktor. Adapun komponen yang dibutuhkan tergambar pada tabel 2.3 berikut.

Tabel 2. 3 Tabel _Need Analysis_ pada _User Interface_

|**Komponen**<br>**_User Interface_**|**Fungsi**|**Desain yang**<br>**Dibutuhkan**|**Conto**<br>**Impleme**|**h**<br>**ntasi**|
|---|---|---|---|---|
|Dashboard|Menampilkan|_Summary_<br>_cards_,|Halaman|awal|
|Utama|informasi<br>ringkasan|grafik pie/bar, dan|dengan||
||data.|diagram<br>garis|visualisasi||
|||untuk data status|ringkasan|<br>dan|

|||mahasiswa,<br>IPK,<br>dan<br>pembayaran<br>UKT.|navigas<br>lainnya|i ke fitur<br>.|
|---|---|---|---|---|
|Visualisasi Data|Membantu pengguna<br>memahami<br>data<br>dengan cepat melalui<br>grafik.|Grafik<br>interaktif<br>yang mendukung<br>filter berdasarkan<br>kriteria<br>tertentu<br>(prodi,<br>semester,<br>status).|Grafik<br>untuk d<br>mahasis<br>prodi<br>grafik<br>untuk<br>pembay<br>UKT.|batang<br>istribusi<br>wa per<br>atau<br>garis<br>tren<br>aran|
|Menu Navigasi|Memudahkan<br>akses<br>ke fitur dan halaman<br>lain.|_Sidebar_<br>dengan<br>menu<br>utama<br>(_Dashboard_UKT,<br>KRS, Nilai, Status<br>Mahasiswa).|_Sidebar_<br>sisi ki<br>dengan<br>dan<br>deskrip|tetap di<br>ri layar<br> <br>ikon<br>teks<br>tif.|
|Tabel Data|Menampilkan<br>data<br>detail<br>dengan<br>kemampuan<br>_drill-_<br>_down_dan filter.|Tabel<br>dengan<br>kolom yang dapat<br>diurutkan,<br>pencarian,<br>dan<br>tombol<br>detail<br>untuk<br>melihat<br>informasi<br>mahasiswa<br>lebih<br>lanjut.|Tabel<br>mahasis<br>belum<br>UKT<br>kolom<br>(prodi,<br>bayar).|wa<br>bayar<br>dengan<br>filter<br>status<br>|

Tabel 2.3 di atas memberikan panduan yang terstruktur untuk kebutuhan

desain antarmuka di setiap komponen sistem. Desain ini memastikan bahwa antarmuka tidak hanya menarik tetapi juga mendukung fungsi yang optimal untuk pengguna.

# **2.3.2** **_Need Analysis User Experience_**

Bagian ini berfokus pada pengalaman pengguna secara keseluruhan saat menggunakan sistem. Analisis kebutuhan yang dilakukan bertujuan untuk mengetahui bagaimana _dashboard business intelligence_ mampu membantu pengguna dari berbagai aspek seperti efesiensi, kemudahan akses data, mengambil keputusan bisnis yang lebih cepat, dan sebagainya. Dalam analisis kebutuhan ini terdapat beberapa poin analisis yang dilakukan, seperti kemudahan navigasi, efisiensi waktu, pengalaman interaktif, konsistensi desain, aksesibilitas data, serta kenyamanan penggunaan. Adapun poin-poin tersebut dijelaskan pada tabel 2.4 berikut.

Tabel 2. 4 Tabel _Need Analysis_ pada _User Experience_

|**Komponen**<br>**_User_**<br>**_Experience_**|**Tujuan****_User_**<br>**_Experience_**|**Kebutuh**<br>**Penggun**|**an**<br>**a**|**Desain**<br>**Pengalaman**<br>**yang**<br>**Diusulkan**|
|---|---|---|---|---|
|Navigasi Intuitif|Memudahkan<br>pengguna berpindah<br>dari satu halaman ke<br>halaman lain.|Menu yang<br>tombol<br>na<br>terlihat, dan<br>navigasi<br>logis.|jelas,<br>vigasi<br>jalur<br>yang|_Sidebar_dengan<br>menu<br>utama<br>dan<br>ikon<br>deskriptif.|
|Akses Informasi<br>Cepat|Membantu pengguna<br>menemukan<br>informasi<br>yang<br>dibutuhkan<br>tanpa<br>langkah yang rumit.|Pencarian<br>yang<br>cepat<br>efisien.|data<br>dan|_Filter_data yang<br>responsif<br>dan<br>mudah<br>digunakan.|
|Visualisasi Data|Menyajikan<br>data<br>dalam format yang<br>mudah dipahami.|Grafik dan<br>interaktif yan<br>menampilkan<br>detail.|tabel<br>g bisa<br>|Grafik batang,<br>pie, dan garis<br>dengan<br>interaktivitas,<br>seperti|

||||highlight<br>tertentu.|data|
|---|---|---|---|---|
|Konsistensi<br>Desain|Membantu pengguna<br>beradaptasi<br>dengan|Warna, ikon, dan<br>tata<br>letak<br>yang|Panduan<br>dengan|desain<br>palet|
||sistem lebih cepat.|seragam di seluruh|warna da|n ikon|
|||halaman.|standar|untuk|
||||semua el|emen.|

Tabel 2.4 ini mampu memberikan penjelasan mengenai kebutuhan UX yang dirancang untuk memberikan pengalaman yang lancar, intuitif, dan memuaskan bagi semua aktor sistem. Dengan demikian, desain pengalaman yang diusulkan dapat memastikan sistem mendukung tugas pengguna secara optimal.

Selain itu, pada _website dashboard business intelligence_ ini, setiap visualisasi data dalam bentuk diagram maupun grafik dapat dilihat oleh masing-masing aktor yang sesuai dengan kebutuhannya. Data-data visualisasi yang disajikan merupakan hasil analisis data yang telah diproses dimana masing-masing data tersebut diantaranya berupa data mahasiswa yang mengajukan cuti, data mahasiswa aktif dan nonaktif, data pembayaran UKT, serta data pengisian KRS. Terkait dengan _user experience_ -nya, adapun kebutuhan rancangan dan fungsinya dijelaskan sebagai berikut.

1. Pada bagian halaman _login_ , keseluruhan aktor dapat mengakses halaman ini dengan tujuan untuk melakukan _login,_

2. Pada bagian _home,_ aktor-aktor berupa Dekan, Wakil Dekan 1, Wakil Dekan 2, Wakil Dekan 3, Koordinator Tata Usaha, serta Koordinator Akademik dan Kemahasiswaan dapat mengakses semua _button_ (UKT, Status Mahasiswa, Pengisian KRS, dan Nilai Mahasiswa), kecuali Koordinator Program Studi yang hanya dapat mengakses 3 _button_ saja berupa Status Mahasiswa, Pengisian KRS, dan Nilai Mahasiswa) serta melihat grafik _update_ terkait dengan jumlah mahasiswa Fakultas Ilmu Komputer per-tanggal sistem di setiap program studi. Grafik ini berfungsi untuk memantau _update_ jumlah mahasiswa terkini,

3. Pada bagian halaman UKT, aktor berupa Dekan, Wakil Dekan 1, Wakil Dekan 2, Wakil Dekan 3, Koordinator Akademik dan Kemahasiswaan serta Koordinator Tata Usaha dapat melihat grafik-grafik berupa:

   - a. Grafik persentase mahasiswa yang belum bayar UKT diikuti dengan tabel detailnya yang berfungsi untuk mengetahui seberapa banyak persentase perbandingan antara mahasiswa yang sudah membayar UKT dengan mahasiswa yang belum membayar UKT beserta dengan detail dari mahasiswa-mahasiswa tersebut, sesuai dengan kebutuhan dari Koordinator Tata Usaha dan Wakil Dekan 2,

   - b. Grafik Total Mahasiswa yang Menunggak UKT sampai dengan tanggal sistem yang berfungsi untuk memantau grafik tunggakan UKT yang terjadi serta menganalisis dan memonitor status akademik dan keuangan mahasiswa secara menyeluruh pada setiap periodenya, sesuai dengan kebutuhan dari Wakil Dekan 2 dan Koordinator Tata Usaha,

   - c. Grafik perbandingan tunggakan mahasiswa aktif, nonaktif, cuti, lulus, keluar, dan _drop out_ per program studi dengan perbandingan beberapa garis beserta dengan _button_ detail untuk mahasiswa yang masih menunggak yang berfungsi untuk memantau banyaknya mahasiswa yang masih menunggak per tiap status akademiknya, sesuai dengan kebutuhan dari Wakil Dekan 2,

   - d. Diagram _pie_ persentase penggolongan banyak mahasiswa dalam golongan UKT di keseluruhan angkatan yang berfungsi untuk memberikan _insight_ berapa banyak total mahasiswa yang mendapatkan golongan ukt A, sesuai dengan kebutuhan Koordinator Tata Usaha,

   - e. Grafik banyak mahasiswa yang memperoleh KIPK beserta dengan _button_ detail yang mengarahkan ke halaman daftar mahasiswa yang memperoleh KIPK yang berfungsi untuk melihat perkembangan seberapa banyak mahasiswa per periode angkatannya yang mendapatkan KIPK, sesuai dengan kebutuhan dari Koordinator Tata Usaha

   - f. Grafik banyak mahasiswa yang mengajukan cicilan UKT, Penurunan UKT, dan pemotongan 50% beserta dengan _button_ detail terkait detai dari mahasiswa yang mengajukan yang berfungsi untuk memberikan _insight_ mengenai banyaknya mahasiswa yang mengajukan keringanan tersebut yang

dapat difilter berdasarkan periodenya, sesuai dengan kebutuhan dari Koordinator Tata Usaha dan Wakil Dekan 2.

4. Pada bagian halaman Status Mahasiswa, Dekan, Wakil Dekan 1, Wakil Dekan 2, Wakil Dekan 3, Koordinator Program Studi, Koordinator Akademik dan Kemahasiswaan serta Koordinator Tata Usaha dapat melihat grafik-grafik berupa:

   - a. Diagram batang bertumpuk yang menunjukkan perbandingan mahasiswa aktif dan nonaktif dengan persentasenya per program studi yang dapat difilter sesuai dengan angkatan, beserta dengan list tabel detail daftar mahasiswa nonaktif dan aktif yang berfungsi untuk mengetahui persentase banyaknya mahasiswa aktif dan nonaktif per angkatannya di setiap program studi, sesuai dengan kebutuhan dari Wakil Dekan 1, Koordinator Program Studi, serta Koordinator Tata Usaha,

   - b. Diagram batang yang menunjukkan perbandingan mahasiswa aktif, nonaktif, cuti, keluar, dan _drop out_ dimana diagram ini dapat difilter per tiap periodenya yang berfungsi untuk memantau dan menganalisis banyaknya mahasiswa aktif, nonaktif, cuti, keluar, dan _drop out_ di setiap angkatannya, sesuai dengan kebutuhan dari Koordinator Tata Usaha dan Koordinator Program Studi,

   - c. Grafik banyak mahasiswa yang mengajukan cuti per periode dan program studinya beserta dengan _button_ detail yang berisikan detail dari mahasiswa yang mengajukan cuti tersebut, yang berfungsi untuk menganalisis banyaknya mahasiswa yang mengajukan cuti di angkatan A pada angkatan B di setiap program studinya, sesuai dengan kebutuhan dari Wakil Dekan 1, Koordinator Program Studi, dan Koordinator Tata Usaha,

   - d. Diagram batang banyaknya mahasiswa yang telah melebihi masa periode di setiap program studi dan kategori semesternya yang dimana dapat difilter berdasarkan semester (ganjil maupun genap) dimana terhitung di waktu sistem beserta dengan _button_ detail mengenai detail dari mahasiswanya, yang berfungsi untuk mengetahui dan menganalisis banyak mahasiswa yang telah melebihi masa periode studi (khususnya yang sudah berada di akhir periode untuk ditindaklanjuti), sesuai dengan kebutuhan Wakil Dekan 1.

5. Pada bagian halaman Nilai Mahasiswa, Dekan, Wakil Dekan 1, Wakil Dekan 2, Wakil Dekan 3, Koordinator Program Studi, Koordinator Akademik dan Kemahasiswaan serta Koordinator Tata Usaha dapat melihat grafik-grafik berupa:

   - a. Terdapat 4 _button_ program studi yang akan mengarahkan ke halaman detail dari program studi dimana berisikan grafik _dashboard_ perolehan nilai mahasiswa per program studi yang dapat difilter berdasarkan tahun akademik, semester, dan mata kuliah beserta dengan detail mahasiswa per program studi yang berfungsi untuk memantau dan menganalisis distribusi jumlah perolehan nilai mahasiswa secara informatif yang mendukung evaluasi capaian pembelajaran, sesuai dengan kebutuhan dari Wakil Dekan 1,

   - b. Pada halaman detail program studi juga nantinya dapat melihat grafik IPS dan perolehan nilai dari mahasiswa ketika _button_ lihat selengkapnya dan _button_ detail mahasiswa ini ditekan yang befungsi untuk memberikan _insight_ dan menganalisis mahasiswa yang memerlukan perhatian, sesuai dengan kebutuhan dari Koordinator Program Studi dan Koordinator Akademik dan Kemahasiswaan,

6. Pada bagian halaman Pengisian KRS, Dekan, Wakil Dekan 1, Wakil Dekan 2, Wakil Dekan 3, Koordinator Program Studi, Koordinator Akademik dan Kemahasiswaan serta Koordinator Tata Usaha dapat melihat fitur berupa:

   - a. Tabel Jadwal Pengisian KRS yang berjalan pada Fakultas Ilmu Komputer yang berfungsi untuk mengetahui jadwal yang telah ditempuh oleh fakultas dalam melakukan pengisian KRS, sesuai dengan kebutuhan dari Koordinator Akademik dan Kemahasiswaan dan Koordinator Tata Usaha,

   - b. Grafik perbandingan banyak mahasiswa aktif, nonaktif, dan aktif tidak isi krs yang dapat difilter berdasarkan angkatan yang berfungsi untuk memberikan analisis terkait dengan perbandingan antara mahasiswa aktif, mahasiswa nonaktif, dan mahasiswa yang aktif namun menunggu isi krs, sesuai dengan kebutuhan dari Koordinator Tata Usaha dan Koordinator Program Studi,

   - c. Tabel mahasiswa aktif belum mengisikan KRS yang apabila menekan _button_ lihat selengkapnya, akan muncul halaman detail dari mahasiswa yang belum mengisikan KRS dengan tujuan untuk mengetahui mahasiswa yang belum

mengisikan KRS dan menindaklanjuti mahasiswa tersebut, sesuai dengan kebutuhan dari Koordinator Program Studi, Wakil Dekan 1, dan Koordinator Tata Usaha.

# **2.3.3** **_Design User Interface (UI/UX Design)_**

Bagian ini akan memberikan gambaran rancangan _user interface_ pada sistem _dashboard_ . Rancangan ini dibentuk sesuai dengan kebutuhan analisis dari _User Interface_ maupun _User Experience_ yang telah dijelaskan sebelumnya dengan memperhatika struktur halaman dan penempatan elemen penting seperti grafik dan tabel. Adapun rancangan _User Interface_ ini ditunjukkan pada gambar-gambar berikut.

# **2.3.3.1 Halaman** **_Login_**

Gambar 2. 5 Halaman _Login_

Pada gambar 2.5 menunjukkan halaman login bagi _user_ untuk menginputkan _username_ dan _password_ yang disediakan. Selanjutnya _user_ dapat menekan _button login_ untuk menuju halaman selanjutnya.

# **2.3.3.2 Halaman** **_Home_**

<!-- Start of picture text -->
@issesee""" Selamat Datang di Dashboard Business Intelligence @<br>vr ay ae)<br><!-- End of picture text -->

Gambar 2. 6 Halaman _Home_

Pada gambar 2.6 di atas merupakan tampilan halaman _home_ yang menjadi beranda utama pada sistem _dashboard business intelligence_ ini. Pada menu _home_ ditampilkan 4 menu dalam _dashboard_ menu yang menunjukkan fitur-fitur yang disediakan. Menu-menu tersebut diantaranya adalah menu UKT yang akan menampilkan visualisasi grafik berkaitan dengan pembayaran UKT, Status Mahasiswa yang akan menampilkan visualisasi grafik berkaitan dengan status mahasiswa di fakultas, Nilai Mahasiswa yang akan menampilkan visualisasi grafik berkaitan dengan nilai-nilai mahasiswa, dan Pengisian KRS yang akan menampilkan visualisasi grafik berkaitan dengan pengisian KRS mahasiswa. Terdapat _sidebar_ dengan menu serupa, tetapi ditambahkan menu About yang nantinya akan menampilkan _Guideline_ dari penggunaan _dashboard business intelligence_ berbasiskan _website_ ini. Selain itu, dalam menu _home_ ini akan menampilkan diagram garis yang menunjukkan visualisasi data terkait dengan banyaknya mahasiswa Fakultas Ilmu Komputer di setiap prodinya. Melalui visualisasi ini nantinya pemangku kepentingan mendapatkan _insight_ mengenai _update_ banyaknya mahasiswa di setiap program studi.

# **2.3.3.3 Halaman Menu** **_Dashboard UKT_**

<!-- Start of picture text -->
eum Dashboardct ®<br>ne annette _<br>_o<br>=-<br>a<br><!-- End of picture text -->

Gambar 2. 7 Halaman Menu _Dashboard_ UKT

Pada gambar 2.7 di atas menunjukkan halaman menu _dashboard_ UKT. Halaman ini akan muncul ketika menu UKT pada halaman _home_ ditekan. Halaman ini memuat visualisasi-visualisasi data dalam bentuk grafik maupun diagram.

Visualisasi pertama menunjukkan _pie diagram_ dari persentase pembayaran UKT. Diagram ini akan memberikan _insight_ mengenai persentase mahasiswa yang sudah membayar UKT maupun belum membayar UKT. Di bagian bawah diagram ini juga nantinya akan terdapat _button_ yang mengarah ke halaman detail mahasiswa belum membayar UKT. Kemudian, pada visualisasi kedua menunjukkan diagram

batang mengenai total mahasiswa yang menunggak UKT sampai dengan tanggal sistem hari ini. Diagram ini akan memberikan _insight_ total terkait seberapa banyak tunggakan UKT yang masih ditanggung oleh fakultas di setiap periodenya yang dapat difilter berdasarkan program studi.

Visualisasi ketiga menunjukkan diagram garis dari perbandingan tunggakan mahasiswa aktif, nonaktif, cuti, lulus, keluar, dan _drop out_ . Perbandingan ini ditunjukkan dari warna garis yang merepresentasikan masing-masing status mahasiswa (yaitu aktif, nonaktif, cuti, lulus, keluar, dan _drop out_ ) seperti yang ditunjukkan pada gambar. Dalam bagian visualisasi ini terdapat _button_ “Lihat Detail” yang dimana ketika ditekan, maka tampilan akan berpindah halaman menuju halaman Detail Tunggakan Mahasiswa. Kemudian terdapat visualisasi _pie diagram_ yang menunjukkan persentase mahasiswa berdasarkan golongan UKT yang dapat difilter berdasarkan angkatan.

Selanjutnya terdapat visualisasi yang menunjukkan banyak mahasiswa yang memperoleh KIPK dan KJMU per waktu saat ini dengan menggunakan diagram garis. Bagian visualisasi ini juga dilengkapi dengan _button_ “Lihat Detail” yang nantinya ketika _button_ ini ditekan akan menampilkan halaman yang berisikan daftar mahasiswa yang memperoleh KIPK dan KJMU. Kemudian visualisasi terakhir pada halaman ini menunjukkan banyak mahasiswa yang mengajukan cicilan UKT, Penurunan UKT, dan Pemotongan 50% yang digambarkan dengan menggunakan diagram garis. Perbandingan ini ditunjukkan dari warna garis yang merepresentasikan masing-masing program studi (S1 Sistem Informasi, S1 Informatika, D3 Sistem Informasi, dan S1 Sains Data) seperti yang ditunjukkan pada gambar. Visualisasi diagram ini nantinya dapat difilter berdasarkan periode. Bagian visualisasi ini juga dilengkapi dengan _button_ “Lihat Detail” yang nantinya ketika _button_ ini ditekan akan menampilkan halaman yang berisikan daftar mahasiswa yang mengajukan Cicilan UKT, Penurunan UKT, dan Pemotongan 50%.

# **2.3.3.4 Halaman Daftar Mahasiswa Belum Bayar UKT**

<!-- Start of picture text -->
@!SSSS"_ Dashboard UKT - Daftar Mahasiswa Belum Bayar UKT ®@<br><!-- End of picture text -->

Gambar 2. 8 Halaman Detail Mahasiswa Belum Bayar UKT

Pada gambar 2.8 ini menunjukkan daftar mahasiswa yang belum membayarkan UKT dimana daftar mahasiswa ini nantinya dapat difilter berdasarkan program studi dan tahun akademik. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu. Halaman ini menunjukkan detail mahasiswa terkait dengan tahun akademik, NIM, nama mahasiswa, program studi, status akademik, total tunggakan, dan _button_ detail mahasiswa. Ketika _button_ tersebut ditekan, maka akan muncul detail lebih lanjut dari mahasiswa tersebut.

<!-- Start of picture text -->
Detail Mahasiswa x<br><!-- End of picture text -->

Gambar 2. 9 Detail Mahasiswa Belum Bayar UKT

Pada gambar 2.9 di atas menunjukkan detail dari salah satu mahasiswa yang belum bayar UKT. Detail ini akan muncul ketika _button_ detail mahasiswa pada tabel daftar mahasiswa belum bayar UKT ditekan, sehingga menampilkan detail dari mahasiswa tersebut yang berupa nama mahasiswa, NIM, program studi,

semester, Alamat, _e-mail_ aktif, nomor telepon, status mahasiswa di akademik, golongan UKT, total bayar, dan status bayarnya.

# **2.3.3.5 Halaman Detail Tunggakan Mahasiswa**

<!-- Start of picture text -->
@ceuseesgowene Dashboard UKT - Detail Tunggakan Mahasiswa ®<br>2<br><!-- End of picture text -->

Gambar 2. 10 Halaman Detail Tunggakan Mahasiswa

Pada gambar 2.10 di atas menampilkan halaman detail tunggakan mahasiswa, baik mahasiswa aktif, nonaktif, cuti, lulus, keluar, maupun _drop out_ , yang dimana halaman ini nantinya dapat difilter berdasarkan program studi dan tahun akademik. Halaman ini akan muncul ketika _user_ menekan _button_ “Lihat Detail” pada bagian visualisasi diagram perbandingan tunggakan mahasiswa per program studi. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu. Pada halaman ini nantinya akan memunculkan tabel yang berisikan tahun akademik, NIM, nama mahasiswa, program studi, status akademik, total tunggakan, dan detail lebih rinci dari mahasiswa yang masuk ke dalam daftar mahasiswa yang masih menunggak.

<!-- Start of picture text -->
Detail Mahasiswa x<br><!-- End of picture text -->

Gambar 2. 11 Detail Mahasiswa yang Menunggak UKT

Pada gambar 2.11 di atas menunjukkan detail dari salah satu mahasiswa yang masih menunggak UKT. Detail ini akan muncul ketika _button_ detail mahasiswa pada tabel detail tunggakan UKT mahasiswa aktif dan mahasiswa nonaktif ditekan, sehingga menampilkan detail dari mahasiswa tersebut yang berupa nama mahasiswa, NIM, program studi, semester, Alamat, _e-mail_ aktif, nomor telepon, status mahasiswa di akademik, golongan UKT, total bayar, dan status bayarnya.

**2.3.3.6 Halaman Daftar Mahasiswa yang Memperoleh KIPK**

<!-- Start of picture text -->
—<br><!-- End of picture text -->

Gambar 2. 12 Halaman Daftar Mahasiswa yang Memperoleh KIPK

Pada gambar 2.12 di atas menunjukkan daftar mahasiswa yang memperoleh KIPK. Halaman ini muncul ketika _user_ menekan _button_ “Lihat Detail” pada bagian visualisasi “Banyak Mahasiswa yang Memperoleh KIPK” yang dimana setiap isinya dapat difilter berdasarkan program studi. Halaman ini akan menampilkan tabel yang berisikan NIM, nama mahasiswa, semester, dan program studi dari setiap mahasiswa yang memperoleh KIPK.

**2.3.3.7 Halaman Daftar Mahasiswa yang Mengajukan Cicilan UKT, Penurunan UKT, dan Pemotongan 50%**

<!-- Start of picture text -->
Penurunan UKT, dan Pemotongan 50%<br><!-- End of picture text -->

Gambar 2. 13 Daftar Mahasiswa yang Mengajukan Cicilan UKT, Penurunan UKT, dan Pemotongan 50%

Pada gambar 2.13 di atas menunjukkan daftar mahasiswa yang mengajukan cicilan UKT, penurunan UKT, dan pemotongan 50%. Halaman ini muncul ketika _user_ menekan _button_ “Lihat Detail” pada bagian visualisasi grafik “Banyak Mahasiswa yang mengajukan Cicilan UKT, Penurunan UKT, dan Pemotongan 50%” yang dimana setiap isinya dapat difilter berdasarkan program studi. Halaman ini akan menampilkan tabel yang berisikan NIM, nama mahasiswa, semester, program studi, golongan UKT, total UKT, status bayar, dan detail mahasiswa dari setiap mahasiswa yang mengajukan.

<!-- Start of picture text -->
Detail Mahasiswa x<br>NamaManasiowas :—TyeskKollsh<br>Program Stat 51 Sistem intormas!<br>Amat son Tunan Mengam, Blk HAN K2<br>Ema Act nayospanayoonalicom<br>No-Toepon ontaraeaz2sce<br>Status Manasiowa © Ale<br>olongan kT olongan<br>‘Total Boyar fp 9100000a<br>status Bayar Pemetengan 50%<br><!-- End of picture text -->

Gambar 2. 14 Detail Mahasiswa yang Mengajukan Pemotongan 50%

Pada gambar 2.14 di atas menunjukkan detail dari salah satu mahasiswa yang mengajukan pemotongan 50% dari UKT. Detail ini akan muncul ketika _button_

detail mahasiswa pada tabel Daftar Mahasiswa yang Mengajukan Cicilan UKT, Penurunan UKT, dan Pemotongan 50% ditekan, sehingga menampilkan detail dari mahasiswa tersebut yang berupa nama mahasiswa, NIM, program studi, semester, Alamat, _e-mail_ aktif, nomor telepon, status mahasiswa di akademik, golongan UKT, total bayar, dan status bayarnya.

**2.3.3.8 Halaman Menu** **_Dashboard_ Status Mahasiswa**

<!-- Start of picture text -->
@NEEAT™ DashboardStatus Mahasiswa @<br>sevtemeen =<br>bebe bch. =<br>=)<br>6S<br><!-- End of picture text -->

Gambar 2. 15 Halaman Menu _Dashboard_ Status Mahasiswa

Pada gambar 2.15 di atas menunjukkan halaman menu _dashboard_ Status Mahasiswa. Halaman ini akan muncul ketika menu Status Mahasiswa pada halaman _home_ ditekan. Halaman ini memuat visualisasi-visualisasi data dalam bentuk grafik maupun diagram.

Visualisasi pertama menunjukkan grafik batang bertumpuk atau yang sering disebut _stacked bar chart_ yang memperlihatkan perbandingan mahasiswa aktif dan nonaktif yang dapat difilter berdasarkan angkatannya. Grafik ini menampilkan persentase mahasiswa aktif dan nonaktif, serta jumlah mahasiswa per program studi yang diletakkan diatas diagram batang. Apabila salah satu tumpukkan diarahkan

oleh kursor, maka akan memunculkan _hover_ detail jumlah mahasiswa dari hasil perhitungan persentase tersebut. Selain itu, di bagian bawah diagram ini juga nantinya akan terdapat _button_ ‘Lihat Detail’ yang apabila ditekan maka akan mengarah ke halaman detail mahasiswa aktif dan nonaktif.

Visualisasi kedua menunjukkan grafik perbandingan mahasiswa aktif, mahasiswa nonaktif, mahasiswa cuti, mahasiswa lulus, mahasiswa keluar, dan mahasiswa _drop out_ di setiap program studinya yang dimana grafik ini nantinya bisa difilter berdasarkan angkatan. Perbandingan ini nantinya akan ditampilkan melalui _bar_ yang memiliki warna berbeda yang dimana warna ini merepresentasikan status mahasiswa tersebut (seperti contoh _bar_ dengan warna biru menunjukkan mahasiswa aktif, _bar_ dengan warna merah menunjukkan mahasiswa nonaktif, _bar_ dengan warna kuning menunjukkan mahasiswa cuti, _bar_ dengan warna abu-abu menunjukkan mahasiswa lulus, _bar_ dengan warna cokelat menunjukkan mahasiswa keluar, dan _bar_ dengan warna hitam menunjukkan mahasiswa _drop out_ ).

Visualisasi ketiga menunjukkan grafik banyak mahasiswa yang saat ini mengajukan cuti. Perbandingan ini akan ditampilkan melalui garis yang memiliki warna berbeda dimana garis ini menunjukkan jumlah dari mahasiswa yang mengajukan cuti per angkatan dan ditunjukkan dengan warna yang berbeda untuk membedakan setiap program studinya. Dalam bagian visualisasi ini terdapat _button_ “Lihat Detail” yang dimana ketika ditekan, maka tampilan akan berpindah halaman menuju halaman Detail Mahasiswa yang Mengajukan Cuti.

Visualisasi terakhir menunjukkan grafik perbandingan mengenai banyak mahasiswa yang telah melebihi masa periode saat ini. Di setiap program studinya akan menampilkan 3 _bar_ dengan berbeda warna yang dimana _bar_ ini menunjukkan masing-masing semester yang sudah melebihi masa periode (semester 9, semester 11, semester 13). Dalam bagian visualisasi ini terdapat _button_ “Lihat Detail” yang dimana ketika ditekan, maka tampilan akan berpindah halaman menuju halaman Detail Mahasiswa Melebihi Masa Periode.

# **2.3.3.9 Halaman Detail Mahasiswa Aktif dan Non Aktif**

<!-- Start of picture text -->
@SSMA"_ Dashboard Status Mahasiswa - Daftar Mahasiswa Aktif dan Non Aktif ©<br><!-- End of picture text -->

Gambar 2. 16 Halaman Detail Mahasiswa Non Aktif

Pada gambar 2.16 di atas menunjukkan halaman daftar mahasiswa aktif dan nonaktif. Halaman ini akan muncul ketika _button_ “Lihat Detail” pada bagian visualisasi perbandingan mahasiswa aktif dan nonaktif ditekan. Halaman ini dapat difilter berdasarkan status mahasiswa, angkatan, dan program studi. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu. Pada halaman ini akan menunjukkan tabel yang berisikan detail mahasiswa berupa NIM, Nama Mahasiswa, Program Studi, IPK, Status Mahasiswa serta _button link_ detail mahasiswa yang lebih lanjut.

<!-- Start of picture text -->
Detail Mahasiswa Non Aktif x<br>NamaMahasiwa = Juohoh<br>CD aoeProgram Stud 2 Sistem nermas<br>‘Atamat Perum Ak Lela No. 184<br>Ema At iulenanegmalicom<br>No. Telepon owosrszee724<br>status Akademi:<br>Perio o2ar2028<br><!-- End of picture text -->

Gambar 2. 17 Detail Mahasiswa Non Aktif

Pada gambar 2.17 di atas menunjukkan detail dari salah satu mahasiswa yang menunjukkan status nonaktif. Detail ini akan muncul ketika _button_ detail mahasiswa pada daftar mahasiswa nonaktif ditekan sehingga menampilkan detail lebih rinci dari mahasiswa tersebut yang berisikan data berupa nama mahasiswa,

NIM, program studi, semester yang ditempuh saat ini, Alamat, _e-mail_ aktif, nomor telepon, status akademik, dan periode mahasiswa dinyatakan tidak aktif.

# **2.3.3.10 Halaman Daftar Mahasiswa Mengajukan Cuti**

Gambar 2. 18 Halaman Daftar Mahasiswa yang Mengajukan Cuti

Pada gambar 2.18 di atas menunjukkan halaman yang berisikan daftar mahasiswa yang mengajukan cuti. Halaman ini akan muncul ketika _button_ “Lihat Detail” pada visualisasi grafik banyak mahasiswa yang mengajukan cuti ditekan, sehingga menampilkan tabel yang berisikan detail mahasiswa yang mengajukan cuti. Tabel ini berisikan detail mahasiswa berupa NIM, nama mahasiswa, program studi, IPK mahasiswa mengajukan cuti, dan detail pengajuan cuti dari mahasiswa tersebut.

<!-- Start of picture text -->
Detail Mahasiswa Cuti x<br>NamaManasiows : Conta Angola<br>Program Stuct ‘tieformatia<br>Alamat Jalan Tunan Past nar No.1<br>Email tit Angelcantka@gmaiicom<br>No. Telepon 081323456745<br>Status Akademi nutans<br>Periods 2023/2024<br><!-- End of picture text -->

Gambar 2. 19 Detail Mahasiswa Cuti

Pada gambar 2.19 di atas menunjukkan detail dari mahasiswa yang mengajukan cuti. Detail ini akan muncul ketika _button link_ detail cuti ditekan. Detail ini akan berisikan detail lebih rinci dari mahasiswa berupa nama mahasiswa,

NIM, program studi, semester, alamat, _e-mail_ aktif, nomor telepon, status akademik yang berupa “Mengajukan Cuti”, serta periode mengajukan cutinya.

# **2.3.3.11 Halaman Daftar Mahasiswa yang Telah Melebihi Masa Periode**

<!-- Start of picture text -->
@{8unsu"" Dashboard Status Mahasiswa - Daftar Mahasiswa Melebihi Periode ®<br>@<br><!-- End of picture text -->

Gambar 2. 20 Halaman Daftar Mahasiswa yang Telah Melebihi Masa Periode

Pada gambar 2.20 di atas menunjukkan halaman daftar mahasiswa yang telah melebihi masa periode yang dimana isinya nanti dapat difilter berdasarkan program studi dan tahun akademik. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu. Halaman ini akan muncul ketika _button_ “Lihat Detail” pada visualisasi diagram mahasiswa yang telah melebihi masa periode ditekan, sehingga menampilkan tabel daftar mahasiswa dengan detail berupa NIM, nama mahasiswa, program studi, semester, tahun akademik, IPK, dan detail mahasiswa yang lebih rinci.

<!-- Start of picture text -->
Detail Mahasiswa Melebihi Masa Periode x<br>Noma Mahasiswa : Jeremiah Doni<br>Program Studi S1Sistern nformasi<br>tamat Perum Labu Slam No 89<br>Email Akt Jeremiandoni@gmalicom<br>No. Telepon oagea24r63412<br>Status Akademik Ati<br>catatan MAHASISWA BERADA DI AKHIR PERIODE<br><!-- End of picture text -->

Gambar 2. 21 Detail Mahasiswa Melebihi Masa Periode

Pada gambar 2.21 di atas menampilkan detail dari salah satu mahasiswa yang telah melebihi masa periode yang dimana detail ini akan muncul ketika _button_ detail mahasiswa pada tabel mahasiswa yang telah melebihi masa periode ditekan. Detail ini akan menunjukkan detail lebih rinci dari mahasiswa yang diantaranya adalah nama mahasiswa, NIM, program studi, semester, alamat, _e-mail_ aktif, nomor telepon, status akademik, dan catatan (seperti contoh bahwa mahasiswa tersebut telah berada di akhir masa periode pada semester ganjil, maka akan ada peringatan dalam catatan tersebut).

# **2.3.3.12 Halaman Menu** **_Dashboard_ Nilai Mahasiswa**

<!-- Start of picture text -->
@sssseAe" Dashboard Nilai Mahasiswa ®<br>Beee Program$1 SeatemStuct ieformast ‘1intormates (D9 Sistem informa |S)Sains ute<br><!-- End of picture text -->

Gambar 2. 22 Halaman Menu _Dashboard_ Nilai Mahasiswa

Pada gambar 2.22 di atas menunjukkan halaman menu _dashboard_ Nilai Mahasiswa. Halaman ini akan muncul ketika menu Nilai Mahasiswa pada halaman _home_ ditekan. Halaman ini memuat visualisasi-visualisasi data dalam bentuk grafik maupun diagram.

Dalam halaman ini memuat 4 menu yang merupakan pilihan program studi berupa S1 Sistem Informasi, S1 Informatika, D3 Sistem Informasi, dan S1 Sains Data. Menu ini nantinya akan menampilkan halaman detail terkait dengan nilai yang diperoleh masing-masing kelas dari setiap program studinya.

Kemudian terdapat visualisasi yang digambarkan dengan grafik batang menunjukkan perbandingan IPK tertinggi dan terendah yang nantinya dapat difilter berdasarkan angkatan. Grafik ini ditunjukkan berdasarkan program studi yang tersedia di setiap angkatannya yang dimana perbandingan ini ditunjukkan par _bar_

dengan berbeda warna. _Bar_ ini merepresentasikan IPK tertinggi, IPK terendah, dan rata-rata IPK di setiap program studinya dengan warna yang berbeda.

# **2.3.3.13 Halaman** **_Dashboard_ Nilai Mahasiswa Per Program Studi**

<!-- Start of picture text -->
@\sueu"—" 4 Dashboard Nilai Mahasiswa S1 Sistem Informasi ®<br>a Detat Manasiswa 5 Sistem formas =><br>° — — one<br>Dota Manasiswa Perolshan Nia ce<br><!-- End of picture text -->

Gambar 2. 23 Halaman _Dashboard_ Nilai Mahasiswa Per Program Studi

Pada gambar 2.23 di atas menunjukkan halaman _dashboard_ nilai mahasiswa per program studi yang dimana halaman ini akan muncul ketika salah satu menu pada menu program studi ditekan. Seperti contoh pada gambar, ketika _button_ S1 Sistem Informasi ditekan, maka akan muncul halaman _dashboard_ nilai mahasiswa S1 Sistem Informasi. Dalam halaman ini akan muncul di bagian atas terkait dengan _button_ ‘Lihat Detail’ yang dimana _button_ ini merujuk pada detail mahasiswa S1 Sistem Informasi.

Di bagian bawah detail mahasiswa S1 Sistem Informasi terdapat visualisasi diagram batang yang berderet dimana menampilkan grafik distribusi perolehan nilai mata kuliah di setiap kelas. Visualisasi ini nantinya dapat memperlihatkan perolehan nilai setiap kelas yang dapat difilter berdasarkan angkatan, semester, dan mata kuliah yang tersedia pada angkatan dan semester tersebut. Visualisasi ini nantinya mampu membantu pemangku kepentingan dalam menilai kelas mana yang memiliki nilai yang bersifat anomali. Kemudian terdapat _button_ ‘Lihat Detail’ yang merujuk pada detail mahasiswa perolehan nilai dari program studi terpilih. Apabila _button_ ini ditekan, maka akan memunculkan halaman detail perolehan nilai mahasiswa berdasarkan mata kuliah terpilih.

<!-- Start of picture text -->
QL" Dashboard Nilai Mahasiswa - Perolehan Nilai Mahasiswa ®@<br><!-- End of picture text -->

Gambar 2. 24 Detail Perolehan Nilai Mahasiswa

Gambar 2.24 di atas menunjukkan tampilan halaman Perolehan Nilai Mahasiswa. Halaman ini akan muncul ketika _button_ ‘Lihat Detail’ yang terdapat di bawah diagram perolehan nilai diklik. Halaman ini merujuk berdasarkan program studi yang terpilih serta tahun akademik, semester, mata kuliah yang terpilih berdasarkan _dropdown filter_ pada diagram perolehan nilai sebelumnya sehingga akan memunculkan tabel yang berisikan NIM, Nama Mahasiswa, Kelas, Nilai, dan Dosen Pengampu dari mata kuliah terpilih. Terdapat _dropdown filter_ kelas yang mampu melakukan _filtering_ berdasarkan kelas yang dipilih. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu.

# **2.3.3.14 Halaman Daftar Mahasiswa Program Studi**

<!-- Start of picture text -->
OLS" Detail Mahasiswa $1 Sistem Informasi @<br>a Y roan -<br><!-- End of picture text -->

Gambar 2. 25 Detail Mahasiswa Program Studi

Pada gambar 2.25 di atas menunjukkan daftar detail mahasiswa dalam program studi yang dapat difilter berdasarkan angkatan. Dalam halaman ini akan berisikan tabel detail mahasiswa yang merupakan bagian dari program studi terkait dengan atribut berupa NIM, nama mahasiswa, semester tempuh, dan _button link_ detail mahasiswa. Halaman ini memuat fitur _search_ yang mampu membantu _user_ dalam mencari nama mahasiswa.

# **2.3.3.15 Halaman Detail Mahasiswa pada Nilai Mahasiswa**

<!-- Start of picture text -->
@ise=se" petal Nal Mahasiowa ®<br><!-- End of picture text -->

Gambar 2. 26 Halaman Detail Nilai Mahasiswa

Pada gambar 2.26 di atas menampilkan halaman detail nilai mahasiswa yang akan muncul ketika _button link_ detail mahasiswa pada tabel detail mahasiswa program studi ditekan. Dalam halaman ini akan ditampilkan nama mahasiswa, NIM, program studi, semester tempuh, alamat, status akademik, dan IPK dari mahasiswa yang dipilih. Selain itu, terdapat dua buah visualisasi grafik garis berupa grafik perolehan IPK per Semester dan perolehan banyak nilai dari individu mahasiswa.

**2.3.3.16 Halaman Menu** **_Dashboard_ Pengisian KRS**

<!-- Start of picture text -->
GSS" Dashboard Pengisian KRS 2<br>~ Tabel Jadwal Pengisian KRS_<br>o nom owe gt 328-382<br>ee<br>| . L.<br><!-- End of picture text -->

Gambar 2. 27 Halaman Menu _Dashboard_ Pengisian KRS

Pada gambar 2.27 di atas menunjukkan halaman menu _dashboard_ pengisian KRS. Halaman ini akan muncul ketika menu Pengisian KRS pada halaman _home_ ditekan. Halaman ini memuat visualisasi-visualisasi data dalam bentuk grafik maupun diagram.

Visualisasi pertama menunjukkan tabel jadwal pengisian KRS. Tabel ini nantinya akan menampilkan periode, semester (ganjil atau genap), serta tanggal pengisian KRS. Kemudian visualisasi kedua menunjukkan grafik batang berderet yang menampilkan perbandingan banyak mahasiswa aktif, mahasiswa nonaktif, dan mahasiswa aktif tidak isi KRS per program studinya. Grafik ini nantinya akan dapat difilter berdasarkan angkatan yang dimana _bar_ yang ditampilkan berjumlah tiga buah di masing-masing program studi dengan perbedaan warna yang menunjukkan perbedaan antara _bar_ jumlah mahasiswa aktif, mahasiswa nonaktif, dan mahasiswa berstatus aktif tidak isi krs. Fitur terakhir merupakan fitur detail

mahasiswa yang belum mengisi KRS yang untuk detailnya dapat dilihat pada halaman selanjutnya ketika _user_ menekan _button_ “Lihat Detail.”

# **2.3.3.17 Halaman Daftar Mahasiswa yang Belum Mengisi KRS**

<!-- Start of picture text -->
@pNsansar"™" Dashboard Pengisian KRS - Mahasiswa Aktif Belum Isi KRS 2}<br><!-- End of picture text -->

Gambar 2. 28 Halaman Daftar Mahasiswa yang Belum Mengisi KRS

Pada gambar 2.28 di atas menunjukkan halaman yang menampilkan tabel daftar mahasiswa yang belum mengisi KRS. Tabel ini akan berisikan detail mahasiswa berupa NIM, nama mahasiswa, IPK, program studi, serta _button link_ detail mahasiswa yang dimana data-data yang masuk akan dapat difilter berdasarkan program studi dan angkatan. Selain itu, terdapat _button export as pdf_ yang nantinya mampu memberikan hasil _file export_ dalam tipe dokumen pdf dimana dalam pdf tersebut akan menampilkan tabel berdasarkan hasil _filtering dropdown_ menu.

# **2.4 Rencana Pengujian Proyek**

Sesuai dengan penjelasan pada _testing_ dan _feedback_ pada _website dashboard_ , akan dilakukan rencana pengujian proyek dengan menggunakan metode _black box testing_ yang memungkinkan pengujian untuk mengamati hasil _input_ maupun _output_ dari _website_ yang dibentuk. Adapun skenario mengenai _black box testing_ yang terdapat pada penelitian ini terdapat pada tabel 2.5 berikut.

Tabel 2. 5 Skenario _Black Box Testing_

|**N**|**Aktor**|**Sken**|**ario**||**Hasil yang**|
|---|---|---|---|---|---|
|**o**||Positif|Nega|tif|**Diharapkan**|
|1|Pimpinan<br>Fakultas|- Melakukan<br>_Login_dengan|-<br>Pengg<br>mema|una<br>sukkan|- Pimpinan<br>dapat|
|||akun<br>yang|_usern_|_ame_|melakukan|
|||dibuatkan.|atau|yang|_Login_.|
|||- Mengakses|tidak||- Pimpinan|
|||menu status|terdaf|tar.|dapat melihat|
|||mahasiswa<br>(aktif/non-|-<br>Pengg<br>mema|una<br>sukkan|ringkasan<br>mengenai|
|||aktif), menu|_passw_|_ord_|pembayaran|
|||ukt,<br>menu|yang s|alah.|ukt,<br>status|
|||nilai<br>mahasiswa,<br>dan menu krs|-<br>Data<br>menu<br>mahas|pada<br>status<br>iswa|mahasiswa,<br>nilai<br>mahasiswa,|
|||pada website|tidak|dimuat|dan krs dalam|
|||_dashboard_|atau|muncul|bentuk<br>grafik|
|||_business_|_error_|_server_.|dan tabel yang|
|||_intelligence_.|-<br>Data|pada|akurat<br>dan|
||||menu<br>tidak<br>karen<br>UKT<br>_down._|<br>UKT<br>muncul<br>a_server_<br>sedang|diperbarui.|
||||-<br>_Filter_|pada||
||||menu<br>tidak<br>berfun<br>(misal<br>tidak<br>meny|<br>UKT<br>gsi<br>nya<br>aring||

|berdasarkan|
|---|
|angkatan).|
|-<br>Data<br>pada|
|menu<br>nilai|
|mahasiswa|
|tidak muncul.|
|-<br>Data<br>pada|
|menu<br>KRS|
|tidak dimuat|
|atau muncul.|
|-<br>Tombol atau|
|aksi<br>pada|
|menu<br>KRS|
|tidak<br>berfungsi<br>(misalnya|
|klik<br>“Isi|
|KRS”<br>tidak|
|ada respon).|
|-<br>Sistem|
|_logout_|
|otomatis saat|
|pengguna<br>sedang<br>mengakses|
|salah<br>satu|
|menu.|
|-<br>Data di salah|
|satu<br>menu|
|terlalu lama|
|untuk dimuat|
|(_loading_|

|||terus-<br>menerus).||
|---|---|---|---|
|2<br>Koordinator<br>Program Studi|- Melakukan<br>_Login_dengan<br>akun<br>yang<br>dibuatkan.<br>- Menampilka|-<br>Pengguna<br>memasukkan<br>_username_<br>yang<br>tidak<br>terdaftar.|- Koordinator<br>program studi<br>dapat<br>melakukan<br>_Login_.|
||n data IPK<br>dan<br>nilai<br>mahasiswa<br>per program|-<br>Pengguna<br>memasukkan<br>_password_<br>yang salah.|- Data nilai dan<br>IPK<br>mahasiswa<br>tampil lengkap,|
||studi<br>pada<br>menu<br>nilai<br>mahasiswa|-<br>_Server_<br>lambat<br>atau<br>tidak<br>merespons<br>saat<br>proses<br>_login_.<br>-<br>_Login_<br>berhasil<br>tetapi<br>diarahkan ke<br>halaman<br>yang<br>salah<br>atau kosong.<br>-<br>Login<br>berhasil<br>tetapi<br>hak<br>akses<br>pengguna<br>salah<br>(tidak|akurat,<br>dan<br>dapat<br>diakses<br>dengan<br>filter<br>program studi<br>dan<br>angkatan<br>tertentu.|

<!-- Start of picture text -->
sesuai<br>perannya).<br>- Data  IPK<br>mahasiswa<br>tidak muncul<br>pada  menu<br>nilai<br>mahasiswa.<br>- Data  nilai<br>mahasiswa<br>tidak lengkap<br>atau  salah<br>ditampilkan<br>(contoh: nilai<br>tidak sesuai<br>dengan<br>mahasiswa).<br>- Data  IPK<br>atau  nilai<br>yang<br>ditampilkan<br>bukan untuk<br>program<br>studi  yang<br>dipilih.<br>- Data  IPK<br>atau  nilai<br>tidak terurut<br>atau  tidak<br>sesuai  filter<br>program<br><!-- End of picture text -->

<!-- Start of picture text -->
studi  yang<br>dipilih.<br>- Data IPK dan<br>nilai  gagal<br>dimuat<br>karena  server<br>API  error .<br>- Data IPK dan<br>nilai  lama<br>sekali dimuat<br>( loading<br>terlalu lama<br>atau  timeout ).<br>- Data  yang<br>tampil  di<br>menu  nilai<br>mahasiswa<br>berasal  dari<br>program<br>studi  lain<br>( mismatch ).<br>- Hak  akses<br>pengguna<br>tidak sesuai<br>sehingga<br>menu  nilai<br>mahasiswa<br>tidak  bisa<br>diakses.<br>- Filter<br>program<br>studi  pada<br><!-- End of picture text -->

|||menu<br>nilai<br>mahasiswa<br>tidak bekerja<br>atau<br>menghasilka<br>n<br>data<br>kosong.|||
|---|---|---|---|---|
|3<br>Koordinator|- Melakukan|-<br>Pengguna|-|Koordinator|
|Tata Usaha|_Login_dengan|memasukkan||tata<br>usaha|
||akun<br>yang|_username_||dapat|
||dibuatkan.|yang<br>tidak||melakukan|
||- Mengakses|terdaftar.||_Login_.|
||dan|-<br>Pengguna|-|Informasi|
||menampilkan|memasukkan||mengenai|
||informasi|_password_||pembayaran|
||pembayaran|yang salah.||UKT<br>muncul|
||UKT|-<br>_Server_||dengan|
||mahasiswa,|lambat<br>atau||lengkap,|
||termasuk|tidak||termasuk|
||daftar<br>dan|merespons||daftar|
||persentase|saat<br>proses||mahasiswa|
||mengenai|_login_.||yang<br>belum|
||pembayaran|-<br>Pengguna||membayar,|
||UKT,<br>total|tidak||serta<br>dapat|
||mahasiswa|memiliki hak||diakses<br>dan|
||yang|akses untuk||difilter|
||menunggak|melihat||berdasarkan|
||UKT,|informasi||kebutuhan.|
||Perbandinga|pembayaran|||
||n Tunggakan|UKT.|||
||Mahasiswa|-<br>Data|||
||Aktif,<br>Non|pembayaran|||

|Aktif,<br>Cuti,|UKT<br>tidak|
|---|---|
|Lulus,|dapat dimuat|
|Keluar, dan|karena_server_|
|_Drop Out_.|sedang_down_.|
||-<br>Data|
||pembayaran|
||UKT<br>yang|
||muncul tidak|
||lengkap atau|
||kosong.|
||-<br>Data|
||pembayaran|
||UKT<br>yang|
||muncul salah|
||(misalnya|
||nominal atau<br>persentase|
||tidak sesuai).|
||-<br>Daftar|
||mahasiswa|
||yang|
||menunggak|
||UKT<br>tidak|
||muncul atau|
||hanya|
||sebagian|
||tampil.|
||-<br>_Filter_untuk|
||melihat data|
||pembayaran|
||UKT|
||(misalnya|

|berdasarkan|
|---|
|angkatan|
|atau<br>status)|
|tidak|
|berfungsi.|
|-<br>Perbandinga|
|n tunggakan|
|mahasiswa|
|(aktif,<br>non|
|aktif,<br>cuti,|
|lulus, keluar,|
|_drop_<br>_out_)|
|tidak tampil|
|atau<br>salah|
|perhitungan.|
|-<br>Grafik<br>atau|
|persentase|
|tunggakan|
|mahasiswa|
|tidak muncul|
|atau_error_.|
|-<br>Tombol atau|
|aksi<br>untuk|
|melihat detail|
|mahasiswa|
|penunggak|
|UKT<br>tidak|
|berfungsi.|
|-<br>Data<br>di|
|halaman|
|pembayaran|
|UKT terlalu|

|||lama<br>untuk<br>dimuat<br>(loading<br>terus-<br>menerus).<br>-<br>Sistem<br>menampilkan<br>data<br>mahasiswa<br>yang<br>tidak<br>relevan atau<br>tercampur<br>antar status.|||
|---|---|---|---|---|
|4<br>Koordinator|- Melakukan|-<br>Pengguna|-|Koordinator|
|Akademik dan|_Login_dengan|memasukkan||akademik dan|
|Kemahasiswaa|akun<br>yang|_username_||kemahasiswaa|
|n|dibuatkan.|yang<br>tidak||n<br>dapat|
||- Menampilka|terdaftar saat||melakukan|
||n<br>menu|_login_.||_Login_.|
||terkait|-<br>Pengguna|-|Grafik<br>dan|
||dengan status|memasukkan||tabel kehadiran|
||mahasiswa,|_password_||mahasiswa|
||nilai|yang<br>salah||tampil<br>sesuai|
||mahasiswa,|saat_login_.||_dropdown_|
||dan<br>krs|-<br>_Server_tidak||_filter_<br>yang|
||mahasiswa|merespons||dipilih, dengan|
|||atau koneksi||_filter_<br>yang|
|||terputus saat||memudahkan|
|||login.||pemantauan|
|||-<br>Setelah_login_,||keaktifan|
|||pengguna||mahasiswa|
|||tidak<br>dapat||secara akurat.|

|melihat menu|
|---|
|status|
|mahasiswa,|
|nilai|
|mahasiswa,|
|atau<br>KRS|
|karena tidak|
|memiliki hak<br>akses.|
|-<br>Menu status|
|mahasiswa|
|gagal dimuat|
|karena_error_|
|_server_<br>atau<br>API<br>tidak|
|merespons.|
|-<br>Menu<br>nilai|
|mahasiswa|
|gagal dimuat|
|<br>karena<br>masalah pada|
|<br>_database_<br>atau API.|
|-<br>Menu<br>KRS|
|tidak<br>bisa|
|diakses|
|karena<br>_role_|
|pengguna|
|tidak sesuai.|
|-<br>Menu<br>KRS|
|gagal|
|menampilkan|

<!-- Start of picture text -->
data<br>(misalnya<br>muncul<br>pesan  “data<br>tidak<br>ditemukan”<br>padahal ada).<br>- Tombol atau<br>fitur  pada<br>menu  KRS<br>tidak<br>merespons<br>saat  diklik<br>(misalnya<br>“Isi  KRS”<br>tidak<br>berfungsi).<br>- Halaman<br>menu  yang<br>dimaksud<br>hanya<br>menampilkan<br>loading<br>terus-<br>menerus<br>tanpa selesai.<br>- Sistem<br>logout<br>otomatis saat<br>sedang<br>membuka<br>salah  satu<br><!-- End of picture text -->

<!-- Start of picture text -->
menu karena<br>sesi habis.<br>- Filter pada<br>menu  (jika<br>ada)  tidak<br>berfungsi<br>atau  tidak<br>menyaring<br>data dengan<br>benar.<br><!-- End of picture text -->


# PROYEK PENGEMBANGAN SISTEM INFORMASI SISTEM PELAYANAN MINIMAL MENGGUNAKAN FRAMEWORK LARAVEL 11 (STUDI KASUS: FAKULTAS ILMU KOMPUTER UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN“ JAKARTA)

# **BAB II**

# **RANCANGAN PROYEK**

Bab ini menjelaskan rancangan produk yang akan dikembangkan sebagai solusi dari permasalahan yang telah diidentifikasi dalam bab pendahuluan. Rancangan ini bertujuan untuk memastikan setiap komponen sistem berjalan sesuai kebutuhan dan harapan pengguna. Bab ini akan memuat observasi (kondisi System berjalan), usulan solusi, rancangan proyek, dan rencana  pengujian proyek.

# **2.1. Observasi (kondisi** **_system_ berjalan)**

Sistem evaluasi pelayanan minimal yang saat ini berjalan di Fakultas Ilmu Komputer UPNVJ menggunakan _platform Google Forms_ sebagai media untuk pengumpulan data survei. Tautan formulir dibagikan melalui _website_ resmi fakultas atau langsung kepada responden. Meskipun sistem ini sederhana dan mudah diakses, terdapat beberapa kendala yang signifikan. Pengelolaan data masih dilakukan secara manual, sehingga memerlukan waktu yang cukup lama untuk mengolah dan menganalisis hasil survei. Sistem ini juga tidak memiliki mekanisme kontrol akses, sehingga memungkinkan pengisian formulir oleh pihak yang tidak relevan atau pengisian data yang berulang. Selain itu, hasil survei tidak dapat disajikan secara _real-time_ dalam format visual yang interaktif, yang menyebabkan keterbatasan dalam mendukung pengambilan keputusan cepat dan berbasis data. Hal ini menunjukkan bahwa sistem yang berjalan kurang efisien, kurang aman, dan tidak sepenuhnya memenuhi kebutuhan pengguna dalam proses evaluasi pelayanan minimal.

# **2.2. Usulan Solusi**

# **2.2.1. Kerangka berpikir**

Kerangka berpikir merupakan diagram yang menggambarkan alur logika penelitian yang sedang berjalan (Priadana & Sunarsi, 2021). Diagram ini menggambarkan alur logika pengembangan sistem yang diajukan untuk menyelesaikan permasalahan manual dalam pengumpulan kuesioner di Fakultas Ilmu Komputer. Kerangka berpikir pada system ini digambarkan dengan kerangka subsistem. Kerangka subsistem adalah kerangka berpikir yang digunakan untuk menjelaskan sistem atau komponen dari suatu sistem yang lebih besar. Menurut

Widarti et al. (2024), kerangka subsistem adalah struktur di mana dua atau lebih subsistem saling bergantung dan bekerja bersama untuk mencapai tujuan tertentu dalam sebuah sistem informasi. Setiap subsistem memiliki fungsi spesifik, namun tetap terintegrasi untuk mendukung kinerja sistem secara keseluruhan. Sistem ini akan terdiri dari beberapa subsistem yang saling berhubungan dan saling mendukung untuk mencapai tujuan pengembangan. Kerangka subsistem untuk sistem informasi digambarkan seperti pada Gambar 1 dibawah ini.

<!-- Start of picture text -->
ee<br><!-- End of picture text -->

Gambar 1. Kerangka Subsistem

Diagram kerangka subsistem Sistem Informasi Pelayanan Minimal (SPM) untuk studi kasus di Fakultas Ilmu Komputer UPNVJ menggambarkan berbagai peran pengguna dan alur pengelolaan data dalam sistem. Subsistem pengguna terdiri dari mahasiswa, dosen, tenaga kependidikan, alumni, pengguna lulusan, dan

mitra kerja sama, di mana masing-masing memiliki akses khusus. Mahasiswa dapat melihat grafik SPM, mengisi kuesioner evaluasi layanan oleh mahasiswa, tugas akhir, dan layanan fakultas, serta memantau riwayat pengisian kuesioner. Dosen memiliki akses serupa, dengan tambahan kuesioner kepuasan dosen dan evaluasi layanan fakultas. Tenaga kependidikan dapat mengisi kuesioner kepuasan tenaga kependidikan dan layanan fakultas serta melihat grafik dan riwayat pengisian kuesioner. Alumni, pengguna lulusan, dan mitra kerja sama masing-masing dapat melihat grafik SPM, mengisi kuesioner sesuai peran mereka, dan memantau riwayat pengisian.

Subsistem admin memiliki peran penting dalam mengelola seluruh data responden, mengakses dan memperbarui kuesioner, serta mengolah hasil kuesioner. Admin juga bertanggung jawab menyajikan laporan dalam bentuk _dashboard_ grafis yang interaktif dan _real-time_ , yang berguna bagi pihak fakultas dan program studi untuk pemantauan dan evaluasi. Proses alur utama dalam sistem meliputi registrasi akun dan _Login_ oleh responden, pengisian kuesioner, pengelolaan data oleh admin, dan penyajian hasil kuesioner dalam bentuk grafik yang dapat diakses oleh pihak terkait. Dengan menggunakan _framework_ Laravel 11, sistem ini diharapkan mampu mengatasi kendala yang ada dalam proses manual sebelumnya, seperti keterbatasan keamanan, risiko duplikasi data, serta kurangnya pemantauan dan analisis _realtime_ . Secara keseluruhan, sistem ini diharapkan dapat meningkatkan efektivitas dan efisiensi pelayanan minimal di Fakultas Ilmu Komputer UPNVJ serta membantu memenuhi standar pelayanan pendidikan yang ditetapkan.

# **2.2.2. Deskripsi Aktor**

Dalam pengembangan Sistem Informasi Pelayanan Minimal, identifikasi aktor menjadi aspek penting guna memastikan setiap pengguna sistem dapat menjalankan tugas sesuai dengan kewenangan dan fungsi sistem. Dalam sistem ini, setiap aktor memiliki hak akses yang berbeda dalam proses pengisian dan pengelolaan kuesioner, yang berperan dalam menjaga dan meningkatkan kualitas layanan di Fakultas Ilmu Komputer UPN “Veteran” Jakarta.

Beragam aktor yang terlibat, mulai dari mahasiswa hingga pimpinan fakultas, memerlukan pembagian peran yang jelas agar sistem berfungsi optimal.

Setiap aktor berkontribusi dalam pengumpulan data evaluasi dan pemantauan hasil kuesioner. Data ini akan digunakan sebagai bahan evaluasi untuk meningkatkan layanan di fakultas. Tabel 2. berikut berisi penjelasan deskripsi dan uraian aktivitas yang dapat dilakukan oleh masing-masing aktor pada system.

Tabel 2 _._ Deskripsi Aktor

|**No**|**Aktor**||**Deskripsi**|
|---|---|---|---|
|1.|Mahasiswa|1.|Dapat_Login_masuk ke sistem|
||FIK|2. <br>3. <br>4.|Dapat mengisi Kuesioner Evaluasi Layanan oleh<br>Mahasiswa (ELOM), Evaluasi Layanan Tugas Akhir<br>(ELTA),  dan Evaluasi Layanan Fakultas<br>Dapat memberikan umpan balik untuk peningkatan<br>standar pelayanan.<br>Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|2.|Dosen|1. <br>2. <br>3. <br>4.|Dapat_Login_masuk ke sistem<br>Dapat mengisi Kuesioner Evaluasi Kepuasan Dosen<br>dan Evaluasi Layanan Fakultas.<br>Dapat melihat grafik hasil semua kuesioner (SPM)<br>Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|3.|Tenaga<br>Kependidikan|1. <br>2. <br>3. <br>4.|Dapat_Login_masuk ke sistem<br>Dapat Mengelola dan memperbarui profil<br>Dapat mengisi Kuesioner evaluasi Kepuasan Tenaga<br>Kependidikan dan Evaluasi Layanan Fakultas.<br>Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|4.|Alumni|1. <br>2. <br>3. <br>4.|Dapat registrasi akun<br>Dapat mengelola dan memperbarui profil<br>Dapat mengisi Kuesioner Kepuasan Alumni.<br>Dapat menyampaikan saran terkait layanan yang<br>mendukung karir setelah lulus.|

|**No**|**Aktor**||**Deskripsi**|
|---|---|---|---|
|||5.|Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|5.|Pengguna<br>lulusan|1. <br>2. <br>3.|Dapat<br>mengisi<br>Kuesioner<br>Evaluasi<br>Kepuasan<br>Pengguna Lulusan untuk memberikan penilaian<br>terhadap lulusan yang bekerja di perusahaan mereka.<br>Dapat berkontribusi dalam peningkatan kualitas<br>pendidikan melalui masukan.<br>Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|6.|Mitra<br>Kerjasama|1. <br>2. <br>3.|Dapat mengisi Kuesioner Kepuasan Mitra Kerjasama.<br>Dapat menyampaikan umpan balik terkait pengalaman<br>bekerja sama dengan Fakultas.<br>Dapat melihat grafik (SPM) dan riwayat pengisian<br>kuesioner|
|7.|Administrator<br>Sistem|1. <br>2. <br>3. <br>4.|Dapat_Login_untuk masuk ke sistem<br>Dapat mengelola seluruh sistem, termasuk<br>menambahkan, mengedit, atau menghapus data<br>responden dan kuesioner.<br>Dapat menyediakan hak akses sesuai peran (admin,<br>dosen, mahasiswa, dll).<br>Dapat mengakses dan mengelola hasil laporan dan<br>analisis kepuasan|
|8.|Pimpinan<br>Fakultas|1. <br>2.|Dapat_Login_untuk masuk ke sistem<br>Dapat Mengakses grafik SPM dan laporan hasil<br>kuesioner|

# **2.2.3.** **_Use Case Diagram_**

<!-- Start of picture text -->
|efelnat DashboardRwayat PengisianSPM FIK—UPNV. |<br>Tengisi Kuesioner Evaluasi Mfengisi Kuesioner Evaluasr ie)<br>Dosen olen Mahasiswa ‘Kepuasan Dosen<br>fe) Mensisi Kuesioner Evalvast Dosen<br>Layanan Fakutas<br>oO<br>Mahasiswa ‘engiLayanan Kuesioneroleh Mahasiswa Evaluasi Tengisi Kuesioner Evaluast<br>Kepuasan Tenaga Kepenciikap ‘enaya Kependidikan<br>fengisi Kuesioner Layanan<br>Tugas Aki<br>Wfengisi Kuesioner Kepuas fe)<br>‘Mengelola Kategori Responden Fengguna Lulusan<br>Mengelola Kuesioner Pengguna Lulusan<br>fe) ‘Mengelola Pertanyaan {eRgisiMira KuesionerKenasama Kepuasan fe)<br>Admin Mengella Jacwal Kuesioner ‘engis Kuasioner mara Kesjasama<br>Kepuasan Alumni O<br>Mengella Data User<br>elakukan Regisras)<br>Mengimport Data Aur<br>Mengakses Dashboard<br>wrengalses<br>Data HasildanKuesione Menger fe)<br>encetak dan Mengelola Laporen Pimpinan<br>Fakultas<br>ilakuKan Logo<br><!-- End of picture text -->

Gambar 2. _Use Case Diagram_

_Use Case Diagram_ yang ditampilkan menggambarkan sistem informasi pengelolaan kuesioner untuk Sistem Pelayanan Minimal (SPM) di Fakultas Ilmu Komputer UPN "Veteran" Jakarta. Terdapat tiga aktor utama dalam sistem ini, yaitu responden (mahasiswa, dosen, tenaga kependidikan, alumni, mitra kerja), admin, dan pimpinan fakultas.

Responden memiliki peran untuk melakukan _login_ , melihat _dashboard_ , melihat riwayat pengisian kuesioner, serta mengisi berbagai jenis kuesioner sesuai dengan perannya. Mahasiswa dapat mengisi Kuesioner Evaluasi Dosen oleh Mahasiswa, Kuesioner Evaluasi Layanan Fakultas, Kuesioner Evaluasi Layanan oleh Mahasiswa, dan Kuesioner Evaluasi Layanan Tugas Akhir. Dosen dapat mengisi Kuesioner Kepuasan Dosen dan Kuesioner Evaluasi Layanan Fakultas. Tenaga Kependidikan dapat mengisi Kuesioner Kepuasan Tenaga Kependidikan dan Kuesioner Evaluasi Layanan Fakultas. Alumni perlu melakukan registrasi terlebih dahulu sebelum mengisi Kuesioner Kepuasan Alumni. Sementara itu,

Pengguna Lulusan dan Mitra Kerjasama diberi kemudahan dengan tidak melakukan registrasi untuk dapat mengisi Kuesioner Kepuasan masing-masing. Mekanisme ini dirancang agar proses pengumpulan data evaluasi berjalan efisien dan sesuai dengan peran responden.

Untuk masuk ke sistem, Admin perlu _login_ untuk mengelola seluruh elemen sistem, seperti kategori responden, kuesioner, pertanyaan, jadwal kuesioner, data _user_ , serta fitur mengimpor data. Admin juga memiliki akses terhadap _dashboard_ , data hasil kuesioner, serta fitur untuk mencetak dan mengelola laporan. Selain itu, admin juga dapat melakukan _logout_ setelah menyelesaikan tugasnya. Sementara itu, pimpinan fakultas dapat mengakses _dashboard_ , serta melihat dan mengelola data hasil kuesioner, termasuk mencetak laporan. Setelah menyelesaikan tugasnya pengguna yang telah _login_ dapat mengakhiri sesinya dengan _logout_ .

# **2.2.4.** **_Activity Diagram_**

1. _Activity Diagram_ Registrasi akun Alumni

<!-- Start of picture text -->
a<br>a<br>aos) aera<br>‘Melakukan Registrasi Ssoometen<br>tego Roa<br>(Mengklik “Dattar”) Menyimpan data )<br>meansenanplan sen<br>©<br><!-- End of picture text -->

Gambar 3 _. Activity Diagram_ Registrasi Akun Alumni

Berikut adalah _Activity Diagram_ registrasi alumni. Proses dimulai ketika alumni mengakses halaman _homepage_ , lalu memilih menu registrasi. Sistem kemudian menampilkan halaman form registrasi yang harus diisi oleh alumni. Setelah mengisi form, alumni mengklik tombol "Daftar", dan sistem akan menyimpan data user ke dalam _database_ . Jika proses berhasil, sistem menampilkan notifikasi bahwa registrasi berhasil.

# 2. _Activity Diagram Login_

<!-- Start of picture text -->
fact AaviyDagranLogn<br>[seStem atatase<br>Mengakses“homepagehalaman<br>password<br>=)<br>‘Mengkik "Login" Vasil Ema can<br>=asnbowd Manas<br>© ‘Wenampiian halaman |<br>vases<br>© enampikan plaman|__|sosen<br>© , papiiaaMboard‘dasnboard‘Kependiaian DosenTenagaalaman/<br>© enampikan‘dashboard  PalananAlum<br>© ——enampilkanasnboara  halamanAdmin ws,san)ere<br>vats<br>© ‘Menampikan halaman eran<br>i: ‘dashbor nulas a rd Pimpinan’ i [ya<br><!-- End of picture text -->

Gambar 4. _Activity Diagram Login_

_Activity Diagram_ login di atas menjelaskan alur proses autentikasi pengguna berdasarkan peran masing-masing. Proses dimulai saat pengguna mengakses _homepage_ dan memilih menu _login_ . Setelah memasukkan _email_ dan _password_ , sistem akan melakukan validasi ke _database_ . Jika data tidak valid, sistem menampilkan pesan error. Namun jika valid, pengguna akan diarahkan ke halaman _dashboard_ sesuai dengan perannya, seperti mahasiswa, dosen, tenaga kependidikan, alumni, admin, atau pimpinan fakultas.

3. _Activity Diagram_ Lihat _Dashboard_ SPM

<!-- Start of picture text -->
Mengakses MenampilkanSPM FIK UPNV) dashboard<br>Dashboard<br>Melihat Nilai SPM beserta<br>Dashboard Grafik Radar<br>Kuesioner SPM dan<br>detail nilai masing<br>masing kuesioner<br><!-- End of picture text -->

Gambar 5. _Activity Diagram_ Lihat _Dashboard_ SPM

_Activity Diagram_ di atas menggambarkan alur pengguna dalam melihat dashboard SPM FIK UPNVJ. Proses dimulai ketika pengguna mengakses menu dashboard. Sistem kemudian menampilkan halaman _dashboard_ yang memuat nilai SPM, grafik radar hasil kuesioner, serta detail nilai dari masing-masing kuesioner.

# 4. _Activity Diagram_ Isi Kuesioner

<!-- Start of picture text -->
Menampiian daar<br>ralgraneiandapat diisi sesuai gaatjenis<br>Menjawab Butir Pertanyaan / rms<br>Mengilk"Kirim- |__|Jawaban” |_| (Menampilkanace alertes  kuesionerfae Tenyinpan‘abannylmpan Daa<br>Tenanpiian<br>sachecar<br>aa a S Kk<br><!-- End of picture text -->

Gambar 6. _Activity Diagram_ Isi Kuesioner

_Activity Diagram_ di atas menjelaskan alur pengisian kuesioner oleh pengguna yang telah login, seperti mahasiswa, dosen, tenaga kependidikan, dan alumni. Proses dimulai saat pengguna memilih menu isi kuesioner. Sistem kemudian menampilkan daftar kuesioner yang tersedia sesuai dengan jenis responden. Setelah pengguna memilih salah satu kuesioner, sistem menampilkan butir pertanyaan yang harus dijawab. Setelah semua pertanyaan dijawab, pengguna mengklik tombol “Kirim Jawaban”. Sistem akan menyimpan jawaban ke dalam _database_ , lalu menampilkan notifikasi bahwa kuesioner berhasil diisi, dan mengarahkan kembali pengguna ke _dashboard_ SPM FIK UPNVJ.

# 5. _Activity Diagram_ Isi Kuesioner Publik

<!-- Start of picture text -->
Pengguna Lansan Wire<br>MemihPpuesmenu kuesionertersediaSianMenampikanrespondenot Saale daaryang<br>Restonsebagai pergoura<br>Mengform lan<br>—a sjenanginan ba wenanyaan<br>‘enjwab Bul Penanyaan —<br>‘Mengklik 5"Kirim —Kuesioner Wenyimpan Data Janaban Menyimpanenyimpan ke<br>penamplkan |<br>aumaal pengen<br>O<br>‘enampian){ Menampltan<br>“KemalKemmalixesene"|(ke |||] "Kembel“ggmbalMegan ke<br><!-- End of picture text -->

Gambar 7. _Activity Diagram_ Isi Kuesioner Publik

_Activity diagram_ di atas menggambarkan alur pengisian kuesioner publik oleh pengguna lulusan atau mitra kerja sama tanpa perlu _login_ . Proses dimulai ketika pengguna memilih menu isi kuesioner publik dan memilih jenis kuesioner yang tersedia sesuai kategorinya. Sistem kemudian menampilkan form isian identitas pengguna sebagai lulusan atau mitra kerja sama. Setelah form diisi dan pengguna mengklik “lanjut ke kuesioner”, sistem menampilkan butir pertanyaan yang harus dijawab. Setelah menjawab seluruh pertanyaan, pengguna mengklik “Kirim Kuesioner”, dan sistem menyimpan data jawaban ke dalam _database_ . Selanjutnya, sistem menampilkan informasi bahwa pengisian berhasil, serta menyediakan dua opsi navigasi: kembali ke halaman kuesioner atau kembali ke beranda.

# 6. _Activity Diagram_ Lihat Riwayat

<!-- Start of picture text -->
aet AciviyDiagramLinatRiwayatKuesioner<br>pilengaksesyi kuesionerMenampilkandiisi sebelumnya yang daftar sudah<br>Meri Lihat<br>KKoesioner yang Chat<br>‘ipl Data<br>Menampilkan<br>etal javvaban<br>pada kttestoner<br>Yang aipiin<br><!-- End of picture text -->

Gambar 8. _Activity Diagram_ Lihat Riwayat

_Activity diagram_ di atas menggambarkan proses pengguna dalam melihat riwayat pengisian kuesioner. Proses diawali ketika pengguna mengakses menu riwayat, kemudian sistem menampilkan daftar kuesioner yang telah diisi sebelumnya. Pengguna dapat memilih salah satu kuesioner dan memilih opsi untuk melihat detailnya. Jika pengguna memilih untuk melihat detail, sistem akan menampilkan isi jawaban dari kuesioner yang dipilih. Diagram ini menunjukkan kemudahan sistem dalam memberikan akses transparan terhadap riwayat pengisian kuesioner bagi pengguna.

7. _Activity Diagram_ Kelola Kategori Responden

<!-- Start of picture text -->
act ActivityDiagramKelolaKategoriResponden<br>KategoriMemilih RespondenMenu P KategoriMenampilkan Respondendaftar<br>Memilih Kategori Responden<br>Memilih Kuesioner yang<br>dapat diisi sesual kategori<br>Responden<br>Simpan‘Memilihperupenen tombol respondenMenampilkansukses kategoridiperbarui alert<br><!-- End of picture text -->

Gambar 9. _Activity Diagram_ Kelola Kategori Responden

_Activity diagram_ di atas menjelaskan alur kerja admin dalam mengelola kategori responden. Proses dimulai ketika admin memilih menu kategori responden, lalu sistem menampilkan daftar kategori yang tersedia. Selanjutnya, admin memilih salah satu kategori responden dan menentukan kuesioner yang dapat diisi oleh kategori tersebut. Setelah selesai, admin menekan tombol simpan perubahan. Sistem kemudian menampilkan notifikasi bahwa perubahan kategori responden telah berhasil diperbarui.

# 8. _Activity Diagram_ Kelola Kuesioner

<!-- Start of picture text -->
PES<br>[|<br>ea ana<br>aaReeTa Se | ing aan<br>SesStes sarectsieee, pf Taha? = Tea<br>poraryrss dieesttaceoner ‘emtonsr sat |__| murmaalasine<br>eo<br>a ee at<br>| MapesKussioner Baru| [wlan‘Bemnasi Diperbart<br>(SH|} | + <a><br>oS<br>‘Mengnapus Data eenInformaReapedata<br><!-- End of picture text -->

Gambar 10. _Activity Diagram_ Kelola Kuesioner

_Activity diagram_ di atas menjelaskan alur pengelolaan kuesioner oleh admin. Proses dimulai saat admin memilih menu kelola kuesioner, lalu sistem menampilkan daftar kuesioner yang tersedia. Untuk menambahkan kuesioner baru, admin mengisi informasi seperti nama, deskripsi, jenis, periode, dan kategori responden, kemudian memilih template pertanyaan dari kuesioner sebelumnya jika diperlukan. Setelah itu, sistem menyimpan data dan menampilkan informasi bahwa kuesioner berhasil ditambahkan. Admin juga dapat melihat atau mengedit kuesioner yang telah ada. Jika perubahan dilakukan, sistem akan memperbarui data dan menampilkan notifikasi keberhasilan. Selain itu, admin dapat menghapus kuesioner dengan melalui proses konfirmasi terlebih dahulu. Jika disetujui, sistem menghapus data dan menampilkan informasi bahwa kuesioner berhasil dihapus. Diagram ini mencerminkan proses manajemen kuesioner yang fleksibel, lengkap, dan aman dalam sistem.

# 9. _Activity Diagram_ Kelola Pertanyaan

<!-- Start of picture text -->
=)<br>(Galamn | aanCSAsaera<br>i yee a a<br>Pt | att<br>oom<br>==}— | &<br>Teagpsson) {penaTecanoiin<br>ay<br><!-- End of picture text -->

Gambar 11 _. Activity Diagram_ Kelola Pertanyaan

_Activity diagra_ m di atas menggambarkan proses pengelolaan pertanyaan kuesioner oleh admin. Proses dimulai ketika admin memilih menu kelola kuesioner dan memilih kuesioner tertentu. Sistem kemudian menampilkan daftar pertanyaan berdasarkan kuesioner yang dipilih. Untuk menambahkan pertanyaan, admin memasukkan data dan memilih opsi tambah pertanyaan. Jika disetujui, sistem menyimpan data dan menampilkan notifikasi bahwa pertanyaan berhasil ditambahkan. Admin juga dapat mengedit pertanyaan yang ada; sistem akan memperbarui data dan menampilkan notifikasi keberhasilan jika perubahan dilakukan. Selain itu, admin dapat menghapus pertanyaan setelah proses konfirmasi, dan sistem akan menampilkan pesan bahwa data berhasil dihapus.

# 10. _Activity Diagram_ Kelola Jadwal Kuesioner

<!-- Start of picture text -->
e<br>= ==<br>cod<br>O;<br><!-- End of picture text -->

Gambar 12. _Activity Diagram_ Kelola Jadwal Kuesioner

_Activity Diagram_ diatas menggambarkan proses Kelola Jadwal Kuesioner yang dilakukan oleh Admin dan sistem. Proses dimulai ketika admin memilih menu kelola jadwal kuesioner. Admin dapat menambahkan periode baru dengan memasukkan nama periode, tahun akademik, serta tanggal mulai dan selesai. Setelah memilih tombol tambah, sistem akan menyimpan data dan menampilkan notifikasi bahwa periode berhasil ditambahkan. Admin juga dapat mengedit data periode yang sudah ada dengan memasukkan data baru, lalu sistem akan memperbarui data dan menampilkan _alert_ jika berhasil. Selain itu, admin memiliki opsi untuk mengaktifkan periode tertentu. Jika pengaktifan berhasil, sistem memberikan notifikasi bahwa periode telah diaktifkan. Terakhir, admin dapat memilih untuk menghapus periode. Sebelum menghapus, sistem meminta konfirmasi. Jika disetujui, sistem akan menghapus periode dan menampilkan alert bahwa periode berhasil dihapus.

11. _Activity Diagram_ Kelola Hasil Kuesioner

Gambar 13. _Activity Diagram_ Kelola Hasil Kuesioner

_Activity diagram_ di atas menggambarkan alur proses admin dalam mengelola hasil kuesioner. Proses dimulai saat admin memilih menu hasil kuesioner, kemudian dapat melihat ringkasan evaluasi dan distribusi nilai per kategori serta per pertanyaan. Admin juga dapat melihat data responden yang telah mengisi kuesioner secara detail. Jika diperlukan, admin dapat menghapus data responden, dan sistem akan menampilkan informasi bahwa data berhasil dihapus.

12. _Activity Diagram_ Kelola Laporan

<!-- Start of picture text -->
‘act ActivityDiagramKelolalaporan<br>Memilih menu laporan ‘Menampilkan daftar laporan<br>‘Memilih lihat laporan<br>pada kuesioner yang i!<br>dipilih Ya Laporan Tidak<br>Menampillkan Laporan<br>kuesioner yang dipilih<br>Cetak<br>as,<br>LampiranCetak ‘Cetak<br>Ya Nkampiran Teak<br>me<br><!-- End of picture text -->

Gambar 14. _Activity Diagram_ Kelola Laporan

_Activity diagram_ di atas menggambarkan proses pengelolaan laporan kuesioner oleh pengguna. Pengguna memulai dengan memilih menu laporan, lalu sistem menampilkan daftar laporan yang tersedia. Setelah memilih laporan kuesioner yang diinginkan, sistem menampilkan isi laporan tersebut. Selanjutnya, pengguna memiliki opsi untuk mencetak laporan utama, mencetak lampiran, atau mengekspor data ke format Excel. Diagram ini menggambarkan alur sederhana namun lengkap dalam mengakses dan mengelola output laporan kuesioner.

13. _Activity Diagram_ Kelola _User_

<!-- Start of picture text -->
a |<br>eltonTenasiian are<br>tas apn<br>eerieen<br>eipasent % Ta<br>a<br>eet<br>en " <> Tes<br>Menghapus Data Usmuter borhactt<br><!-- End of picture text -->

Gambar 15. _Activity Diagram_ Kelola _User_

_Activity diagram_ di atas menjelaskan proses pengelolaan data _user_ oleh admin. Admin dapat menambahkan _user_ baru dengan mengisi data lengkap, kemudian sistem menyimpan data dan menampilkan notifikasi keberhasilan. Admin juga bisa mengedit data _user_ yang sudah ada, lalu menyimpan perubahan tersebut. Selain itu, admin dapat menghapus _user_ setelah konfirmasi, dan sistem akan menghapus data serta menampilkan notifikasi bahwa data berhasil dihapus.

14. _Activity Diagram Import_ Data

<!-- Start of picture text -->
act ActivityDiagramimpontData<br>Mengakses Menampilkan Halaman<br>Menu import Form Import Data<br>Data<br>Memilih Kuesioner yang<br>akan di import<br>Mendownload template<br>data kuesioner yang<br>dipilih<br>Mengupload Data hasil<br>kuesioner yang dipilih dalam<br>format excel dan csv<br>Klik Import Data Mengimport Data<br><!-- End of picture text -->

Gambar 16. _Activity Diagram Import_ Data _Activity diagram_ di atas menggambarkan proses _import_ data kuesioner oleh

_user_ . Proses dimulai saat user mengakses menu _import_ data, lalu sistem menampilkan form _import_ . _User_ kemudian memilih kuesioner yang akan diimpor, mengunduh template data, dan mengunggah hasil kuesioner dalam format Excel atau CSV. Setelah itu, user mengklik tombol _import_ dan sistem memproses data tersebut.

# 15. _Activity Diagram Logout_

<!-- Start of picture text -->
act ActivityDiagramLogout<br>Memilih Menu Profile<br>Mengklik tombol Logout Mena eae<br><!-- End of picture text -->

Gambar 17. _Activity Diagram Logout_

Activity diagram di atas menggambarkan proses _logout_ oleh _user_ . Proses dimulai ketika _user_ memilih menu profil, lalu mengklik tombol _logout_ . Setelah itu, sistem akan menampilkan halaman _homepage_ sebagai tanda bahwa _user_ telah berhasil keluar dari sistem.

# **2.3. Rancangan Proyek**

# **2.3.1. Desain Produk**

Tahap awal perancangan sistem informasi pelayanan minimal melibatkan pembuatan _wireframe low-fidelity_ untuk memvisualisasikan alur kerja dan antarmuka pengguna secara sederhana. Berikut merupakan desain produk pada sistem informasi sistem pelayanan minimal FIK UPNVJ

# **1. Halaman** **_Login_ dan** **_Sign up_ ,** **_Home_ dan** **_Dashboard_**

<!-- Start of picture text -->
|a<br>Sistem Pelayanan<br>Minimal a<br>el > gu<br>qa...<br>3.37 =—e<br>BSC3 Sree<br>GSS) Ge<br>= =e<br>a, =e<br>— = 5<br>one Ose ore<br>One oS one<br>ore ore Ores<br><!-- End of picture text -->

<!-- Start of picture text -->
w z a<br>iid ain iin ‘ip pn ai {te Doe<br>-=<br>9<br>posi spegp an<br>an2 —ae pico*<br>Bergabunglahdalam Peningkatan Mutu FIK UPNV)<br><!-- End of picture text -->

Gambar 18. Halaman _Home Website_ SPM FIK UPNVJ

Halaman ini memuat tiga menu utama: Registrasi, _Login_ , dan Kuesioner Publik, serta dua tombol utama, yaitu “ _Login_ ” dan “Isi Kuesioner” yang mengarahkan pengguna untuk masuk ke sistem atau langsung mengisi kuesioner. Di bawahnya ditampilkan nilai total SPM FIK UPNVJ sebagai rata-rata keseluruhan dari 9 grafik dengan indikator kategori penilaian dalam skala warna (Kurang, Cukup, Baik, Sangat Baik) berdasarkan periode, jumlah kuesioner, dan total responden. Halaman ini juga menampilkan grafik radar yang memvisualisasikan rata-rata hasil 9 kuesioner, seperti Evaluasi Layanan Fakultas, Evaluasi Dosen, dan Kepuasan Mahasiswa, serta grafik batang horizontal yang menampilkan nilai setiap aspek penilaian ( _Assurance, Empathy, Reliability, Responsiveness, Tangible_ ). Bagian “Hasil per Jenis Kuesioner” merinci

rata-rata nilai dari masing-masing kuesioner berdasarkan aspek penilaian, dan “Jenis Kuesioner” menampilkan daftar lengkap beserta deskripsi singkatnya.

<!-- Start of picture text -->
[SN stent nr me<br><!-- End of picture text -->

Gambar 19 _._ Halaman Registrasi

Jika _User_ dalam hal ini alumni belum memiliki akun dan memilih Registrasi pada navigasi atas _website_ maka sistem akan menampilkan formulir registrasi dan alumni dapat mengisi data yang dibutuhkan untuk membuat akun. alumni akan diminta untuk mengisi data diri seperti NIM, tahun lulus, kode program studi, nama lengkap, nomor telepon, _email_ , domisili, NIK, dan NPWP. Setelah mengisi data tersebut, alumni dapat mengklik tombol "Simpan". Setelah data tersimpan, alumni dapat melanjutkan untuk mengisi kuesioner evaluasi kepuasan.

<!-- Start of picture text -->
—<br>.<br><!-- End of picture text -->

Gambar 20 _._ Halaman _Login_

Pada halaman _Login_ , mahasiswa, dosen, tenaga kependidikan dan alumni dapat masuk ke sistem dengan memasukkan _Username_ (NIM, NIDN, NIK, _email_ terdaftar untuk alumni) dan _password_ sedangkan untuk mitra dan pengguna lulusan tanpa _Login_ untuk mengakses _website_ .

<!-- Start of picture text -->
a ry<br>x<br>pA 6<br>“ a=<br><!-- End of picture text -->

Gambar 21. Halaman Menu Kuesioner Publik

Halaman ini menyajikan informasi bagi pengguna publik seperti Pengguna Lulusan dan Mitra Kerjasama untuk langsung mengisi kuesioner sesuai kategori. Terdapat empat menu utama: Pengguna Lulusan, Mitra Kerjasama, Alumni, dan Informasi. Pengguna Lulusan dan Mitra dapat langsung mengisi kuesioner melalui tombol “Isi Kuesioner”, sementara Alumni diarahkan untuk _Login_ atau mendaftar terlebih dahulu. Bagian Informasi menjelaskan bahwa mahasiswa, dosen, dan tendik mengisi kuesioner melalui SIAKAD dengan tombol _Login_ yang tersedia.

<!-- Start of picture text -->
222<br>Oo Oo )<br><!-- End of picture text -->

<!-- Start of picture text -->
=~ @<br>——<br><!-- End of picture text -->

Gambar 22. Halaman _Dashboard_ SPM FIK UPNVJ

Halaman ini merupakan _Dashboard_ Sistem Pelayanan Minimal FIK UPNVJ yang menyajikan informasi hasil evaluasi layanan berdasarkan data kuesioner. Terdapat tiga menu utama: _Dashboard_ , Kuesioner dan Riwayat. Di bagian atas, terdapat sambutan dan tombol “Isi Kuesioner” untuk memulai survei. Grafik utama menampilkan nilai total SPM FIK UPNVJ sebagai rata-rata dari 9 jenis kuesioner, disertai kategori penilaian berwarna dari “Kurang” hingga “Sangat Baik”.

Terdapat grafik radar yang memperlihatkan rata-rata nilai dari seluruh jenis kuesioner Di bawahnya, grafik donat menunjukkan skor masingmasing jenis kuesioner beserta kategorinya.

Bagian bawah halaman memuat dua panel: “Kuesioner Tersedia” yang menampilkan daftar kuesioner aktif beserta batas waktunya, dan “Riwayat Pengisian” yang menunjukkan status pengisian kuesioner.

<!-- Start of picture text -->
====<br>—<br><!-- End of picture text -->

Gambar 23 _._ Halaman Detail _Dashboard_ Kuesioner

Jika _User_ memilih grafik kecil sebagai contoh Kuesioner Layanan oleh Fakultas pada halaman sebelumnya, sistem akan mengarahkan ke menu _dashboard_ dan menampilkan halaman detail _dashboard_ yang berisi grafik kuesioner tersebut per aspek, penjelasan terkait kuesioner, serta grafik kecil untuk masing-masing aspek _, yaitu reliability, responsiveness, assurance, empathy, dan tangible._

<!-- Start of picture text -->
@Daftar Kuesioner =<br>Evaluasi Layanan FIK UPNVJ<br>gen a eneesemraogca sone yng hems -<br>Ge B22 eo)<br>arm<br><!-- End of picture text -->

Gambar 24 _._ Halaman Pilih Isi Kuesioner

Jika _User_ memilih _button_ isi kuesioner pada halaman _home_ maka sistem akan menampilkan halaman Pilih Isi Kuesioner terlebih dahulu. Halaman ini berisi _button_ - _button_ nama kuesioner yang dapat dipilih sesuai hak akses _User_ . Di tampilan Mahasiswa terdapat 4 _button_ yaitu _button_ Kuesioner Evaluasi Layanan Fakultas, Kuesioner Evaluasi Dosen oleh Mahasiswa, Kuesioner Evaluasi Layanan oleh Mahasiswa, dan Kuesioner Layanan Tugas Akhir.  Untuk dosen terdapat 2 _button_ yaitu Kuesioner Evaluasi Layanan Fakultas dan Kuesioner Kepuasan Dosen. Sementara itu, tenaga kependidikan memiliki 2 _button_ yaitu _button_ Kuesioner Evaluasi Layanan Fakultas Dan Kuesioner Evaluasi Tenaga Kependidikan. Alumni, mitra dan pengguna lulusan masing - masing hanya 1 _button_ kuesioner yang sesuai dengan rolenya. Setiap _button_ akan mengarahkan _User_ ke halaman pengisian kuesioner sesuai dengan nama kuesionernya.

# **a. Halaman Isi Kuesioner Evaluasi Layanan Fakultas**

Gambar 25 _._ Halaman Isi Kuesioner Evaluasi Layanan Fakultas

Halaman Isi Kuesioner Evaluasi Layanan Fakultas merupakan halaman yang digunakan oleh Mahasiswa, Dosen, dan Tenaga Kependidikan untuk memberikan penilaian terhadap kualitas layanan di FIK UPNVJ. Disediakan petunjuk pengisian untuk memandu responden. Kuesioner disusun berdasarkan lima aspek utama yaitu _reliability, responsiveness, assurance, empathy_ , dan _tangible_ , yang masing-masing terdiri dari beberapa pertanyaan. Setiap pertanyaan menggunakan skala Likert 1–4 (Kurang hingga Sangat Baik) dan dilengkapi dengan opsi komentar. Di bagian bawah tersedia kolom

“Saran & Masukan” untuk memberikan masukan tambahan secara terbuka, serta tombol “ _Submit_ ” untuk mengirim hasil isian.

# **b. Halaman Isi Kuesioner Evaluasi Dosen oleh Mahasiswa**

<!-- Start of picture text -->
—. ;<br><!-- End of picture text -->

<!-- Start of picture text -->
8 mee rn<br>a= -- on —<br><!-- End of picture text -->

Gambar 26. Halaman Isi Kuesioner Evaluasi Dosen oleh Mahasiswa

Berikut adalah tampilan halaman isi kuesioner Evaluasi Dosen oleh Mahasiswa. Kuesioner ini dapat disii oleh Mahasiswa aktif FIK UPNVJ. Tampilan ini muncul setelah _button_ yang diklik oleh _User_ pada halaman sebelumnya. Tampilan ini bersifat seragam untuk semua jenis kuesioner, dengan perbedaan hanya pada isi pertanyaan yang disesuaikan dengan setiap  kuesioner. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

# **c. Halaman Isi Kuesioner Evaluasi Layanan Oleh Mahasiswa**

<!-- Start of picture text -->
=_———— ;<br>=<br>—— =<br><!-- End of picture text -->

<!-- Start of picture text -->
tai Kuesioner<br>[omnes<br>a= -- _ —<br><!-- End of picture text -->

Gambar 27. Halaman Isi Kuesioner Layanan oleh Mahasiswa

Berikut adalah tampilan halaman isi kuesioner Evaluasi Layanan oleh Mahasiswa. Kuesioner ini dapat disii oleh Mahasiswa aktif FIK UPNVJ. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

# **d. Halaman Isi Kuesioner Evaluasi Layanan Tugas Akhir**

Gambar 28. Halaman Isi Kuesioner Evaluasi Layanan Tugas Akhir

Berikut adalah tampilan halaman isi kuesioner Evaluasi Layanan Tugas Akhir. Kuesioner ini dapat disii oleh Mahasiswa FIK UPNVJ yang sedang menjalani tugas akhir. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

# **e. Halaman Isi Kuesioner Evaluasi Kepuasan Dosen**

Gambar 29. Halaman Isi Kuesioner Evaluasi Kepuasan Dosen

Berikut adalah tampilan halaman isi kuesioner Evaluasi Kepuasan Dosen. Kuesioner ini dapat disii oleh Dosen FIK UPNVJ. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

# **f. Halaman Isi Kuesioner Evaluasi Kepuasan Tenaga Kependidikan**

<!-- Start of picture text -->
 bikemioner<br>rc 7 oo on —<br>_———— aanans .<br><!-- End of picture text -->

<!-- Start of picture text -->
Seer<br>eee :<br>=<br><!-- End of picture text -->

Gambar 30. Halaman Isi Kuesioner Evaluasi Kepuasan Tenaga Kependidikan

Berikut adalah tampilan halaman isi kuesioner Evaluasi Kepuasan Tenaga Kependidikan. Kuesioner ini dapat disii oleh Tenaga Kependidikan FIK UPNVJ. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

# **g. Halaman Isi Kuesioner Evaluasi Kepuasan Alumni**

Gambar 31 _._ Halaman Isi Kuesioner Evaluasi Kepuasan Alumni

Berikut adalah tampilan halaman isi kuesioner Evaluasi Kepuasan Alumni. Kuesioner ini dapat disii oleh Alumni FIK UPNVJ _._ Tampilan ini bersifat seragam untuk semua jenis kuesioner, dengan perbedaan hanya pada isi pertanyaan yang disesuaikan dengan masing-masing kuesioner. Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, saran dan masukan dan tombol _Submit_ .

**h. Halaman Isi Kuesioner Evaluasi Kepuasan Pengguna Lulusan**

<!-- Start of picture text -->
i Kuesioner Kepuasan Pengguna Lulusan<br>© Pevnjuk Pengsan<br><!-- End of picture text -->

Gambar 32 _._ Halaman Formulir  Data Diri Pengguna Lulusan Sebelum Isi Kuesioner

Halaman ini merupakan formulir pengisian data diri bagi pengguna layanan yang ingin mengisi survei Kuesioner Evaluasi Kepuasan Pengguna Lulusan. Formulir ini dirancang untuk mempermudah pengguna yang tidak memiliki akun atau tidak perlu melakukan _Login_ atau registrasi. Pengguna diminta mengisi kolom data diri seperti nama responden, jabatan, dan nama perusahaan, serta data terkait alumni yang akan dinilai, yaitu nama alumni FIK UPNVJ, tahun lulus, dan program studi alumni. Setelah data diisi, pengguna dapat menyimpan informasi dengan menekan tombol "Simpan" yang terletak di bagian bawah.

<!-- Start of picture text -->
— it ote<br>iowa<br>=<<br><!-- End of picture text -->

<!-- Start of picture text -->
1 Kepuasan Pengguna Lulusan<br>=n - ES oo<br><!-- End of picture text -->

Gambar 33. Halaman Isi Kuesioner Evaluasi Kepuasan Pengguna Lulusan

Berikut adalah tampilan halaman isi kuesioner Evaluasi Kepuasan Pengguna Lulusan. Kuesioner ini dapat disii oleh Pengguna Lulusan FIK UPNVJ. Tampilan ini dihasilkan berdasarkan _button_ yang dipilih _User_ pada halaman sebelumnya _._ Terdapat petunjuk pengisian, tabel pertanyaan kuesioner, opsi komentar, Harapan dan Saran dari mitra atau pengguna terhadap lulusan FIK UPNVJ dan tombol _Submit_ .

# **i. Halaman Isi Kuesioner Evaluasi Kepuasan Mitra Kerjasama**

<!-- Start of picture text -->
© Kuesioner Kepuasan Mitra —<br><!-- End of picture text -->

Gambar 34. Halaman Formulir  Data Diri Mitra Kerjasama Sebelum Isi Kuesioner

Halaman ini adalah formulir pengisian data diri bagi pengguna yang ingin mengisi survei Kuesioner Evaluasi Kepuasan Mitra Kerjasama. Formulir ini dirancang untuk memudahkan pengguna yang tidak memiliki akun atau tidak perlu melakukan _Login_ atau registrasi. Pengguna diminta untuk mengisi kolom data diri seperti nama

responden, jabatan, nama perusahaan, jenis kerjasama dan mitra, lingkup kerjasama, periode kerjasama, alamat, dan nomor telepon. Setelah mengisi data tersebut, pengguna dapat menyimpan informasi yang telah diisi dengan menekan tombol "Simpan" yang terletak di bagian bawah halaman.

<!-- Start of picture text -->
= cs<br>—————— 3 18<br>a...<br><!-- End of picture text -->

<!-- Start of picture text -->
8 Kapa Mira Kajama o_|<br>© roar<br>EE Oe<br><!-- End of picture text -->

Gambar 35 _._ Halaman Isi Kuesioner Evaluasi Kepuasan Mitra Kerjasama

Berikut adalah tampilan halaman isi kuesioner Evaluasi Kepuasan Mitra Kerjasama. Kuesioner ini dapat disii oleh Mitra Kerjasama FIK UPNVJ. Tampilan ini dihasilkan berdasarkan _button_ yang dipilih _User_ pada halaman sebelumnya _._ Tampilan ini seragam untuk semua jenis kuesioner, dengan pembeda hanya pada isi pertanyaan yang sesuai dengan masing-masing kuesioner. Pada bagian bawah formulir, terdapat kolom untuk menuliskan Saran dari mitra dan Saran untuk kemajuan FIK.

<!-- Start of picture text -->
©) SPM FIKUPNVI outboe Konsoner = © Dr nga Hay Fay =<br>‘D-) RiwayatRi Kuesioner, & contac<br>8 Kuesioner yang Telah Dis<br>dul Kesoner dene Perede Wate Pengan A<br>vs aya Tope Ar (1A) o SevminrGoy ums MINIS. 0828 Oo<br>‘aus Don lhMasons CTD sereswcayiemuzns —watmasonz oom<br>Slaton lhMains 10M) o Senminrcap mums WM ImS.0826 © Oe<br>as aya alts ceric cops sues somes. cans «ot<br><!-- End of picture text -->

Gambar 36. Halaman Riwayat Pengisian Kuesioner

Berikut adalah tampilan halaman riwayat pengisian kuesioner. Halaman ini berisi informasi tanggal pengisian kuesioner yang sudah selesai diisi, dan dapat melakukan lihat detail untuk melihat jawaban kuesioner yang sudah diisi sebelumnya.

<!-- Start of picture text -->
2, Profil Saya a<br>==<br><!-- End of picture text -->

Gambar 37 _._ Halaman _Profile_

Pada halaman _profile_ , _User_ dapat mengubah profil, memasukkan informasi tambahan yang dibutuhkan serta mengubah _password_ . Jika _User_ ingin keluar dari sistem _User_ dapat memilih _User._

# **2. Halaman** **_Admin_**

Pada halaman admin terdapat 7 menu yaitu _dashboard_ , Kelola Kuesioner, Hasil Kuesioner, Kategori Responden, Jadwal Kuesioner, Laporan, _Import_ Data dan Kelola _User._

<!-- Start of picture text -->
~~ |: e |= ae |e &<br>es rine<br><!-- End of picture text -->

<!-- Start of picture text -->
= = =<br>3.25 3.35 3.42<br>Sw os<br>3.32 3.29 3.30<br>o @ o<br>3.42 3.39 3.63<br>= e =<br><!-- End of picture text -->

Gambar 38. Halaman _Dashboard_ Admin

Halaman _Dashboard_ Admin SPM FIK UPNVJ menyajikan ringkasan visual dan analisis data evaluasi kuesioner layanan dan kepuasan pengguna. Tersedia filter untuk memilih periode akademik dan program studi guna menyesuaikan tampilan data. Tiga kartu statistik utama menunjukkan total kuesioner, jumlah responden, dan nilai rata-rata SPM dari 9 kuesioner. _Dashboard_ utama menampilkan tren nilai SPM berdasarkan periode yang dipilih. Di bawahnya, ditampilkan visualisasi tiap aspek dan kategori evaluasi, termasuk kepuasan layanan fakultas, mahasiswa, dosen, tugas akhir, alumni, pengguna lulusan, dan mitra kerja sama.

<!-- Start of picture text -->
® semrixurnw fi © distor<br>tac Kammer KelolaTambo etKuesioner dnl hesner SPM iK — Semester Ganj 2024/2025 Gans zoa4ia0 | Yy<br>No Nama Kuesioner Semester Tahun Prods Status Revpondan Ak<br>B apo 1 ieluaeo)Uyanan Tages Gayl 25 oremroneot- ED<br>DOES 2 Kapusan Doan oy mazes 2aoyramrons ED ozo<br>2 Kapusan Tenge Gail 2420251098224 2 ozo<br>Keenan orn<br>4 Repunsan Ani Gant 20242085 onan100872024 = 8]<br>Repuisan Ferggune Gani 20242025 ora1908/2024 = =o<br>6 Kapuso ora =o<br>Kesama iva oy maurems. psp. o<br>7 Goku Lynanfolutas Gans mes ronson. EE CD | RY<br>zorzrnee oc<br>© aunMahanLynamOM) oleh Gani 20242085 zara1909/2008, c= seo<br>9 wai Dosenceh Gail 20242085 1009/2024 c= EO<br>Meson soyrozoze<br><!-- End of picture text -->

Gambar 39. Halaman Kelola Kuesioner

Pada menu Kelola Kuesioner pada sistem SPM FIK UPNVJ Admin dapat mengelola kuesioner berdasarkan semester dan tahun akademik yang dapat dipilih melalui dropdown di bagian atas. Tabel utama menampilkan daftar kuesioner dengan kolom nomor, nama kuesioner, semester, tahun akademik, periode, status kuesioner (Aktif, Non-Aktif, atau Selesai), kelompok responden, dan aksi. Bagian aksi menyediakan ikon untuk mengedit atau menghapus kuesioner. Tombol "Tambah Kuesioner" memungkinkan admin menambahkan kuesioner baru.

# **a. Halaman Kelola Kuesioner – Tambah Kuesioner**

<!-- Start of picture text -->
0) SPM FIK UPNVS = © Anitator<br>a rae Tambah Kuesioner Baru ce<br>BB Laporan Desks<br>eet © suinevyny o<br>Giustn Fearyut Kuwsone Seam<br>"ak mengpinatan template ut prayed ava .<br><!-- End of picture text -->

Gambar 40. Halaman Formulir Tambah Kuesioner

Halaman ini merupakan formulir untuk menambahkan kuesioner baru pada sistem SPM FIK UPNVJ, khususnya untuk evaluasi layanan fakultas. Admin diminta mengisi nama kuesioner, deskripsi, periode pelaksanaan (dengan tanggal mulai dan selesai), serta menentukan status aktif kuesioner. Pilihan responden dapat disesuaikan dengan mencentang kategori responden. Admin juga dapat memilih untuk menggunakan template pertanyaan dari periode sebelumnya atau membuat pertanyaan baru. Setelah selesai, kuesioner disimpan melalui tombol “Simpan & Lanjutkan”.

# **b. Halaman Lihat Detail - Kelola Kuesioner (Kuesioner layanan**

# **Fakultas)**

Gambar 41. Halaman Kelola Kuesioner – Lihat Detail

Jika admin memilih untuk lihat detail suatu kuesioner pada halaman sebelumnya, maka sistem akan membuka Halaman kelola Kuesioner  tersebut. Di bagian atas halaman, ditampilkan informasi umum kuesioner yang mencakup judul, deskripsi, periode pengisian, tanggal pelaksanaan, serta jenis dan kategori responden yang dapat mengisi kuesioner.Tombol aksi seperti “Duplikasi Kuesioner”, “Kembali”, dan “Edit Kuesioner” tersedia untuk memudahkan pengelolaan.

Selanjutnya, bagian utama halaman menampilkan daftar pertanyaan yang dikelompokkan berdasarkan lima aspek utama, yaitu _Reliability_ , _Responsiveness_ , _Assurance_ , _Empathy_ , dan _Tangible_ . Setiap pertanyaan disertai informasi terkait apakah pertanyaan tersebut wajib diisi, statusnya aktif atau tidak, serta tombol aksi untuk mengedit atau menghapus pertanyaan. Total terdapat 14 pertanyaan yang secara menyeluruh mengukur berbagai dimensi kepuasan pelanggan terhadap layanan fakultas. Fitur tambahan yang berguna pada halaman ini adalah kemampuan untuk mengubah urutan pertanyaan dengan cara _drag and drop,_ memberikan fleksibilitas bagi admin dalam menyusun kuesioner sesuai kebutuhan.

# • **Halaman Tambah Pertanyaan Baru**

<!-- Start of picture text -->
Tambh Pertanyaan Baru x<br>oc<br><!-- End of picture text -->

Gambar 42. Halaman Tambah Pertanyaan

Pada halaman Tambah Pertanyaan Baru, admin dapat menambahkan pertanyaan secara manual ke dalam kuesioner. Admin dapat memilih aspek pertanyaan yang sesuai dan mengisi isi pertanyaannya. Terdapat juga _toggle_ “Wajib Diisi” yang dapat diaktifkan atau dinonaktifkan sesuai kebutuhan. Setelah pertanyaan selesai dibuat, admin dapat menekan tombol “Simpan” untuk menyimpan pertanyaan tersebut atau memilih tombol “Batal” untuk membatalkan proses penambahan.

- **Halaman Edit Pertanyaan**

<!-- Start of picture text -->
kat Petayaan x<br>© as<br>oes<br><!-- End of picture text -->

Gambar 43. Halaman Edit Pertanyaan

Pada halaman Edit Pertanyaan, admin dapat mengedit pertanyaan Admin dapat memperbarui aspek pertanyaan yang sesuai dan isi pertanyaannya. Terdapat juga _toggle_ “Wajib Diisi” dan “Aktif”  yang dapat diaktifkan atau dinonaktifkan sesuai kebutuhan. Untuk menyimpan perubahan, admin dapat menekan

tombol “Simpan Perubahan” atau memilih tombol “Batal” untuk membatalkan proses perubahan.

**c. Halaman Kelola Kuesioner - Edit Kuesioner**

<!-- Start of picture text -->
©) SPMFIK UPNYJ = Oo<br>1B Laporen Decsipst<br>- hee ‘Jens Kuesioner* “Perode Akadernik:<br><!-- End of picture text -->

Gambar 44. Halaman Kelola Kuesioner - Edit Kuesioner

Jika admin memilih untuk mengedit kuesioner "Kuesioner Evaluasi Layanan Fakultas" pada halaman sebelumnya, maka sistem akan membuka Halaman kelola Kuesioner Layanan Fakultas. Formulir tersebut akan menampilkan detail kuesioner yang sudah ada, seperti nama kuesioner, deskripsi, jenis kuesioner, periode akademik, tanggal mulai tanggal selesai, _toggle_ status kuesioner (Aktif atau NonAktif), dan kelompok responden yang berhak mengisi. Admin dapat mengubah informasi tersebut, seperti mengganti semester, memperbarui periode, atau mengubah status kuesioner. Setelah selesai, admin dapat menyimpan perubahan dengan menekan tombol "Simpan Perubahan". Hal ini memungkinkan admin untuk memperbarui kuesioner yang sudah ada sesuai kebutuhan tanpa harus membuat kuesioner baru.

# **d. Halaman Kelola Kuesioner - Hapus Kuesioner**

<!-- Start of picture text -->
(<br>Konfirmasi Hapus<br><!-- End of picture text -->

Gambar 45. Halaman Kelola Kuesioner - Hapus Kuesioner

Jika admin ingin menghapus sebuah kuesioner, admin dapat memilih opsi hapus pada kuesioner yang diinginkan. Setelah itu, sistem akan menampilkan dialog konfirmasi untuk memastikan tindakan penghapusan. Dalam dialog tersebut, admin dapat menekan tombol “Ya, Hapus” untuk mengonfirmasi dan melanjutkan proses penghapusan kuesioner. Sebaliknya, jika admin memutuskan untuk tidak melanjutkan, tombol “Batal” dapat dipilih untuk membatalkan tindakan tersebut. Dialog konfirmasi ini bertujuan untuk mencegah penghapusan data secara tidak disengaja.

<!-- Start of picture text -->
4) SPM FIK UPN) = © Administer<br>© tetote Meecione [MenampakanHasil Kuesionerhasil pengisian kuesioner dalam bentuk tabel dan grafik<br>Hes Kuesioner rman<br>18 Kelle seal Kvesoner PevdeSemester Aadeik Ganil2024/ ¥ —JesSamunJensKone === StsSemmSttus Pengiion Semanrogram SuProgram sta<br>import<br>Oat<br>ata Has Kusone ==<br>ama Kusoner tide JiaRewponden—Penginstatue s—B luasi a t Ala<br>Evan Dosen lh Mahasiowe SstanaesGanj o = oe<br>values Layanan Fakutas SemesterananasGanji o @ ce<br>tan Lyon lh Mabon Semeter Ganj o = oe<br>cio anaes<br>[lunien) Layanan Tuga Abhi SemesteranaanasGanji oo e &<br>KeputenAbeot SemesteranaesGani o = oe<br>epussen Doton Semesteranaes Ganji o [eons<br>Kepuasan<br>Miva Keysama——_Semerteranaes Gary o = oe<br>epuesen Pengguna Lsusen | Semesteranaes Ganj o<br>Kepusan<br>Tenaga Kependitan Semesteranaaaas Gan o =<br>sseodune EB seyere-<br><!-- End of picture text -->

Gambar 46. Halaman Kelola Hasil Kuesioner - SPM

Halaman Kelola Hasil Kuesioner - SPM menampilkan data hasil semua kuesioner dalam tabel. Halaman ini memiliki filter pencarian berdasarkan periode akademik, jenis kuesioner, status pengisian, dan program studi. Tabel di bawahnya memuat informasi seperti nama kuesioner, periode, jumlah responden, status pengisian, status evaluasi, dan opsi aksi (ikon grafik untuk lihat lebih detail, edit dan hapus).

# **a. Halaman Detail hasil Kuesioner (Kuesioner Layanan Fakultas)**

<!-- Start of picture text -->
- : ~ Deel te useioner ===.<br>cis paaraorey a.|<br>j=" F = lz als: °<br>© }<br>sae =a es<br> —————— - ><br><!-- End of picture text -->

Gambar 47. Halaman Detail Hasil Kuesioner – Lihat Hasil

Halaman Detail Hasil Kuesioner – Lihat Hasil menyajikan data hasil kuesioner responden berdasarkan aspek kualitas layanan seperti _Reliability, Responsiveness, Assurance, Empathy,_ dan _Tangible_ . Disediakan fitur filter berdasarkan program studi. Hasil evaluasi ditampilkan dalam bentuk visual berupa nilai rata-rata, jumlah responden, periode, dan rentang tanggal pelaksanaan, lengkap dengan kategorinya. Grafik distribusi dan per kategori memberikan gambaran menyeluruh, serta tabel di bagian bawah merinci penilaian tiap pertanyaan beserta aspek, rata-rata nilai, dan kategori penilaiannya.

# **b. Halaman Detail Hasil Kuesioner – Daftar Responden**

<!-- Start of picture text -->
a Daftar Responden =<br>‘s =<br>7 =e ee eas<br>er= nor oo<br>cwanapattion nO stom ED<br>egg Cererr ee ree—y oo<br>a _=po<br>= =p)<br>a a oo<br>sam [accoume —|eeent meen — Teh oo<br><!-- End of picture text -->

Gambar 48. Halaman Detail Hasil Kuesioner – Daftar Responden

Halaman Detail Hasil Kuesioner – Daftar Responden menampilkan daftar responden yang sudah mengisi kuesioner layanan tersedia. Pada halaman ini terdapat informasi dari formulir kuesioner yang sudah diisi yaitu tanggal pengisian, nama pengisi, NIM, Program Studi dan Kategori Respondennya terdapat aksi untuk lihat data Responden untuk melihat hasil jawaban kuesioner masing-masing responden dan hapus data hasil kuesioner.

# **c. Halaman Daftar Responden – Detail Jawaban Responden**

<!-- Start of picture text -->
: Respond<br><!-- End of picture text -->

<!-- Start of picture text -->
a ne<br>=<br>tn<br>ta i =<br><!-- End of picture text -->

Gambar 49. Halaman Lihat Responden – Detail Jawaban Responden

Jika Admin memilih opsi Lihat Data Responden, sistem akan menampilkan halaman Detail Jawaban Responden yang berisi tanggapan lengkap dari satu responden terhadap kuesioner evaluasi layanan. Informasi responden seperti nama, NIM, _email_ , program studi, kategori, dan waktu pengisian ditampilkan secara ringkas di bagian atas. Di bawahnya, ditampilkan daftar pertanyaan yang dikelompokkan menurut dimensi layanan ( _Reliability, Responsiveness, Assurance, Empathy, Tangible_ ), lengkap dengan nilai skala 1–4 dan komentar jika tersedia. Warna pada nilai mempermudah identifikasi tingkat kepuasan: hijau (Sangat Baik), biru (Baik), kuning (Cukup), dan merah (Kurang). Di bagian bawah terdapat _Danger Zone_ bagi admin untuk menghapus data jawaban dengan tombol “Hapus Data Responden” beserta peringatan bahwa tindakan ini bersifat permanen.

<!-- Start of picture text -->
Cee = 2 canna<br>to Kategori Responden<br>18 ton tenn i oo or |<br>Kueioner yang Dap Dis leh Mahasswa c=)<br>’ © name anne ia ede se<br>© ccuactnncenitiens — Eadamacabttnens Sree cant<br>Xero Don Pannen a —-)<br>ers Towpteptton —tgasenyeenin Seve ant<br>pore ‘eno Ar an)<br>Nerumnegpeitan ——epamanengptannnn Seren<br>Aponte ‘ep ena an)<br><!-- End of picture text -->

Gambar 50. Halaman Kategori Responden

Pada halaman Kategori Responden, admin dapat mengatur kategori responden dan menentukan akses terhadap kuesioner berdasarkan peran pengguna dalam sistem. Terdapat tab yang mewakili masing-masing

kategori responden seperti Mahasiswa, Dosen, Tenaga Kependidikan, Alumni, Pengguna Lulusan, dan Mitra. Admin dapat memilih kuesioner mana saja yang dapat diisi oleh masing-masing kategori dengan mencentang kotak yang sesuai. Setelah melakukan perubahan, admin dapat menyimpan pengaturannya dengan memilih tombol “Simpan Perubahan”.

<!-- Start of picture text -->
a Kelola Jadwal Kuesioner =<br>—aene tet SE<br>© rere<br><!-- End of picture text -->

Gambar 51. Halaman Kelola Jadwal Kuesioner

Halaman ini adalah halaman kelola jadwal kuesioner di SPM FIK UPNVJ. Pada halaman ini, admin dapat melihat daftar jadwal kuesioner yang mencakup informasi seperti nomor, nama periode, semester, tahun akademik, tanggal mulai, tanggal selesai, status (aktif atau non-aktif). Tersedia tombol "Tambah Periode" untuk menambahkan jadwal baru, serta ikon untuk mengedit atau menghapus jadwal yang ada.

# **a. Halaman Tambah Periode**

<!-- Start of picture text -->
‘Tambah Periode Akademik x<br>dammeyry 1D eimeyyy<br>Athan Period<br><!-- End of picture text -->

Gambar 52. Halaman Tambah Periode

Pada halaman Kelola Jadwal Kuesioner, admin dapat menambahkan periode akademik baru sebagai acuan jadwal pengisian kuesioner. Saat tombol “Tambah Periode” diklik, sistem menampilkan formulir dalam bentuk dialog yang berisi isian nama periode, semester, tahun akademik, tanggal mulai dan selesai. Admin juga dapat memilih untuk menyalin kuesioner dari periode lain dan mengaktifkan periode secara langsung. Setelah data diisi, admin dapat menyimpan periode dengan tombol “Simpan” atau membatalkannya dengan tombol “Batal”

# **b. Halaman Edit Periode**

<!-- Start of picture text -->
os J monn<br><!-- End of picture text -->

Gambar 53. Halaman Edit Periode Akademik

Pada halaman Kelola Jadwal Kuesioner, admin juga dapat mengedit periode akademik yang telah ditambahkan sebelumnya. Ketika admin memilih ikon edit pada salah satu periode, sistem akan menampilkan formulir “Edit Periode Akademik” dalam bentuk dialog. Di dalam formulir ini, admin dapat memperbarui nama periode, memilih semester dan tahun akademik, serta menyesuaikan tanggal mulai dan tanggal selesai sesuai kebutuhan. Terdapat pula _toggle_ “Aktifkan Periode” yang bisa diaktifkan jika admin ingin menjadikan periode tersebut sebagai periode aktif. Setelah melakukan perubahan, admin dapat menyimpannya dengan menekan tombol “Simpan Perubahan” atau memilih “Batal” untuk membatalkan perubahan yang telah dilakukan.

# **c. Halaman Hapus Periode**

<!-- Start of picture text -->
Konfirmasi Hapus<br><!-- End of picture text -->

Gambar 54. Halaman Hapus Periode

Ketika admin ingin menghapus data periode akademik pada halaman Kelola Jadwal Kuesioner, sistem akan menampilkan _pop-up_ konfirmasi dengan judul “Konfirmasi Hapus”. _Pop-up_ ini berfungsi sebagai pengingat dan verifikasi untuk memastikan bahwa tindakan penghapusan benar-benar diinginkan. Di dalamnya terdapat ikon peringatan dan teks pertanyaan “Anda yakin ingin menghapus data ini?”. Admin dapat memilih tombol “Ya, Hapus” untuk melanjutkan proses penghapusan, atau menekan tombol “Batal” untuk membatalkan tindakan tersebut dan menutup _pop-up_ tanpa perubahan apa pun pada data.

<!-- Start of picture text -->
a=<br>=<br><!-- End of picture text -->

Gambar 55. Halaman Laporan

Pada halaman Laporan Kuesioner, admin dapat melihat daftar laporan dari seluruh kuesioner yang telah dibuat dan diisi oleh responden. Informasi yang ditampilkan meliputi nomor urut, judul kuesioner, deskripsi singkat, tanggal dibuat, jumlah responden yang telah mengisi, serta opsi aksi yang dapat dilakukan terhadap masing-masing kuesioner.

Tombol “Lihat” memungkinkan admin untuk melihat detail kuesioner. Sementara itu, tombol “Cetak Laporan” dapat digunakan untuk menghasilkan dokumen laporan hasil kuesioner dalam format PDF. Di bawahnya, tombol “Cetak Lampiran” disediakan untuk mencetak dokumen pendukung atau detail jawaban kuesioner sebagai bagian dari dokumentasi dalam format PDF. Lalu, tombol “ _Export to Excel_ ”  untuk mendapatkan data lampiran dalam format excel.

# **a. Lihat Laporan**

<!-- Start of picture text -->
— sone 5." wninass Tawa |S<br>straits take Sheet we a<br>‘ome snes hae aL -<br>=<br>a<br>bes cae<br><!-- End of picture text -->

<!-- Start of picture text -->
Drepsecran fautae<br>a oe els 2<br>=<br>~=]<br>o =]<br>=<br>:=<br>i s<br><!-- End of picture text -->

Gambar 56. Halaman Lihat Laporan

Halaman Lihat Laporan akan menampilkan ringkasan hasil dari satu kuesioner yang telah diisi oleh responden. Informasi dasar seperti judul, tipe, periode, tanggal pelaksanaan, dan deskripsi kuesioner ditampilkan di bagian atas. Empat indikator utama Total Responden, Skor Rata-Rata, Jumlah Pertanyaan, dan Penilaian Umum disajikan dalam bentuk kartu statistik untuk memberikan gambaran ringkas.

Grafik rata-rata per kategori ( _Reliability, Responsiveness, Assurance, Empathy, Tangible_ ) dan tabel detail pertanyaan disediakan untuk analisis lebih lanjut. Di bagian bawah, ditampilkan daftar responden lengkap dengan nama, kategori, program studi, waktu pengisian, dan nilai rata-rata. Admin dapat melihat jawaban detail tiap responden melalui tombol Detail.

Tersedia juga fitur Edit Konten Laporan untuk menambahkan analisis, kesimpulan, dan rencana tindak lanjut (RTL), yang dapat disimpan dengan menekan tombol Simpan Konten.

# **b. Cetak Laporan Analisis**

<!-- Start of picture text -->
i<br>=e<br>=<br>LAST SSS<br>SSEeEess<br>Se<br>SSeS<br><!-- End of picture text -->

<!-- Start of picture text -->
5 OO Ow uu<br>LAPORAN<br>‘outs ISIONER<br>evans<br>ee,<br>SS<br>FAKULTAS ILMU KOMPUTER<br>UPN “VETERAN” JAKARTA<br><!-- End of picture text -->

<!-- Start of picture text -->
—<br>SS<br>=<br>= :<br>a (<br><!-- End of picture text -->

<!-- Start of picture text -->
= Sa<br>-_.<br><!-- End of picture text -->

<!-- Start of picture text -->
El TTT |<br><!-- End of picture text -->

<!-- Start of picture text -->
=<br>—<br><!-- End of picture text -->

<!-- Start of picture text -->
=——s—<br><!-- End of picture text -->

<!-- Start of picture text -->
a<br>wnsennnn<br><!-- End of picture text -->

Gambar 57. Hasil Cetak Laporan

Sistem SPM FIK UPNVJ menyediakan fitur cetak laporan evaluasi layanan semua kuesioner yang memungkinkan admin menghasilkan dokumen resmi sesuai format standar fakultas. Laporan ini mencakup data kuantitatif seperti rata-rata per pertanyaan, per aspek layanan (Reliability, Responsiveness, Assurance, Empathy, dan Tangible), serta rata-rata keseluruhan kuesioner. Seluruh data yang ditampilkan telah diolah otomatis oleh sistem dan disajikan dalam bentuk tabel maupun grafik untuk memudahkan analisis dan interpretasi.

Admin dapat mencetak laporan dalam format dokumen resmi yang siap digunakan untuk keperluan analisis internal maupun pelaporan formal kepada pimpinan. Format laporan tersebut telah dilengkapi dengan struktur standar seperti: pendahuluan, metode pengumpulan data, hasil dan pembahasan, serta rencana tindak lanjut. Data kuantitatif disajikan dalam bentuk tabel dan grafik, termasuk distribusi skor, persentase kategori penilaian, dan agregat skor ratarata berdasarkan responden dan aspek yang dinilai.

Dengan adanya fitur cetak ini, proses dokumentasi hasil evaluasi menjadi lebih efisien dan terstruktur. Admin tidak perlu lagi melakukan pengolahan manual terhadap data kuesioner, karena sistem sudah menyusun dan menyajikannya secara otomatis dan akurat sesuai format laporan yang digunakan fakultas. Kemudahan ini mendukung upaya fakultas dalam meningkatkan akuntabilitas dan transparansi proses penjaminan mutu, serta mempermudah pengambilan keputusan berbasis data oleh pimpinan.

# **c. Cetak Lampiran**

<!-- Start of picture text -->
Ee=—— edia sce<br> ee<br>SS<br>erred<br><!-- End of picture text -->

<!-- Start of picture text -->
AT__=__ Sseal ial Re =)<br>Feeemeeetme tectecteteteecteel<br>a—=—————_T a el el ee a a<br>SeePeeeeeeee SSSERTSTESTES|<br><!-- End of picture text -->

Gambar 58. Hasil Cetak Lampiran

Fitur cetak lampiran pada sistem evaluasi layanan ini memungkinkan admin mencetak laporan lengkap berisi data kuantitatif hasil kuesioner dalam bentuk tabel terstruktur. Lampiran mencakup rincian setiap pertanyaan, kategori aspek layanan, distribusi skor (Sangat Baik, Baik, Cukup, Kurang), nilai rata-rata, serta keterangan mutu pelayanan. Selain itu, terdapat pula data tabulasi responden lengkap dengan identitas responden dan jawaban

terhadap masing-masing pertanyaan. Informasi ini sangat penting dalam mendukung transparansi dan validitas hasil evaluasi.

Dengan adanya fitur ini, admin dapat menghasilkan dokumen pendukung laporan evaluasi yang siap dicetak atau diarsipkan untuk kebutuhan pelaporan internal, dan  tindak lanjut peningkatan layanan. Format lampiran yang dicetak dalam bentuk PDF juga sudah disusun agar mudah dibaca dan dianalisis oleh pimpinan atau tim pengambil keputusan, serta memungkinkan visualisasi data secara menyeluruh dan akurat.

# **d.** **_Export To Excel_**

Gambar 59. Hasil _Export To Excel_

Fitur _Export ke Excel_ memungkinkan admin untuk mengunduh data hasil evaluasi kuesioner dalam format Microsoft Excel (.xlsx). Data yang diekspor mencakup seluruh hasil tanggapan responden terhadap setiap pertanyaan, lengkap dengan informasi kategori, program studi (jika ada), dan nilai jawaban berdasarkan skala Likert. Melalui format Excel ini, admin dapat dengan mudah melakukan olah data lanjutan, menyusun grafik, melakukan filter atau pengurutan, serta menyesuaikan format sesuai kebutuhan analisis internal fakultas.

Kemudahan akses data melalui Excel sangat berguna dalam proses rekapitulasi hasil, validasi manual, serta integrasi ke sistem pelaporan lainnya seperti dokumen akreditasi atau laporan pimpinan. Selain itu, file Excel ini dapat digunakan untuk menyusun lampiran tabulasi atau mendukung pelaporan evaluasi mutu dalam bentuk kuantitatif yang sistematis dan mudah dibaca.

<!-- Start of picture text -->
D somrxurnvs i O sue<br>_ Import Hasil Kuesioner<br>2<br>Staten ver © Petunjuk Format File<br>ne<br>o [2] o o<br>(Bevattonreed anne Sore ate brs<br><!-- End of picture text -->

Gambar 60. Halaman _Import_ Data

Gambar di atas menunjukkan antarmuka halaman _Import_ Hasil Kuesioner yang digunakan oleh admin untuk mengimpor data hasil pengisian kuesioner dari file eksternal, seperti _Google Form_ atau Excel. Pada bagian atas, terdapat formulir impor data yang terdiri dari dua elemen utama: _dropdown_ pemilihan jenis kuesioner dan ada data _exciting_ atau template sesuai struktur file serta tombol untuk mengunggah file Excel/CSV dengan format .xlsx, .xls, atau .csv maksimal 10MB. Setelah file dipilih, admin dapat menekan tombol “ _Import Data”_ untuk memulai proses unggah data.

<!-- Start of picture text -->
eee | = os es oe<br>eeeoe<br>re<br>a<br>geeoe<br>a<br>leeoe<br><!-- End of picture text -->

Gambar 61. Halaman Kelola _User_

Halaman _Kelola User_ memungkinkan admin untuk mengelola data pengguna sistem. Daftar pengguna ditampilkan dalam tabel berisi informasi seperti nama, email, kategori (Mahasiswa, Dosen, Tendik, atau Alumni), NIM, program studi, serta status akun yang ditandai label hijau “Aktif” jika akun aktif. Tersedia fitur pencarian dan filter berdasarkan kategori untuk memudahkan pencarian data. Admin dapat menambahkan pengguna baru melalui tombol _Tambah User Baru_ yang membuka formulir input lengkap. Setiap baris data dilengkapi tombol aksi: ikon pensil untuk mengedit dan ikon tempat sampah untuk menghapus akun.

# **a. Halaman Tambah** **_User_ Baru**

<!-- Start of picture text -->
1 Edit User c<br>i)<br><!-- End of picture text -->

Gambar 62 _._ Halaman Tambah _User_ Baru

Pada halaman Tambah _User_ Baru, admin dapat menambahkan pengguna ke sistem SPM FIK UPNVJ dengan mengisi formulir berisi nama, _email_ , _Username_ , kategori _User_ , _password_ , dan konfirmasi _password_ . Admin juga dapat mengunggah foto profil (JPG, PNG, JPEG, maks. 2MB) serta mengisi nomor telepon sebagai informasi tambahan. Terdapat opsi Status Akun untuk langsung mengaktifkan akun baru melalui tombol geser “Aktif”.

# **b. Halaman Edit** **_User_**

<!-- Start of picture text -->
ets = © soot<br>On Edit User x<br>2 sve vote toon<br>etc pn ang pt)<br><!-- End of picture text -->

Gambar 63 _._ Halaman Edit _User_

Halaman ini digunakan oleh admin untuk memperbarui informasi pengguna dalam sistem SPM. Admin dapat mengedit data seperti nama lengkap, _email_ , kategori _User_ (Mahasiswa, Dosen, Tendik, dll), status aktif/tidak aktif, serta informasi tambahan seperti NIM, program studi, dan nomor telepon. Admin juga dapat mengganti foto profil dan melakukan pengaturan ulang _password_ jika diperlukan. Seluruh perubahan disimpan melalui tombol “Simpan Perubahan” di bagian bawah halaman.

# **c. Halaman Pop Up Konfirmasi Hapus** **_User_**

<!-- Start of picture text -->
Konfirmasi Hapus<br><!-- End of picture text -->

Gambar 64. Halaman _Pop Up_ Konfirmasi Hapus _User_

Halaman ini ditampilkan saat admin mencoba menghapus data pengguna dari sistem. Sistem akan menampilkan dialog konfirmasi dengan pesan: _"Anda yakin ingin menghapus data ini?"_ untuk menghindari penghapusan data secara tidak sengaja. Admin dapat memilih tombol “Ya, Hapus” untuk melanjutkan proses penghapusan atau “Batal” untuk membatalkannya. Fungsi ini penting sebagai tindakan preventif dalam pengelolaan data pengguna.

# **3. Halaman Pimpinan Fakultas**

Pada halaman pimpinan fakultas terdapat 3 menu yaitu _dashboard_ , Hasil Kuesioner, dan Laporan

<!-- Start of picture text -->
—_—<br>325 335 3.42<br>— a<br>3.32 3.29 3.30<br>e o e<br>== o ==<br>3.42 3.39 3.63<br><!-- End of picture text -->

<!-- Start of picture text -->
|: e |= ce gt |i &<br>~ .<br>aaa<br>2<br><!-- End of picture text -->

Gambar 65 _._ Halaman _Dashboard_ Pimpinan Fakultas

Halaman _Dashboard_ Pimpinan menampilkan ringkasan evaluasi dan tingkat kepuasan layanan di lingkungan FIK UPNVJ. Pimpinan dapat memfilter data berdasarkan periode akademik untuk melihat indikator utama: total kuesioner, jumlah responden, dan nilai rata-rata SPM beserta kategorinya. Tersedia grafik tren nilai SPM antar semester dan diagram pie distribusi nilai per aspek layanan ( _Assurance, Empathy, Reliability, Responsiveness, Tangible_ ). Nilai rata-rata per kategori kuesioner seperti kepuasan alumni dan pengguna lulusan juga ditampilkan, dilengkapi dengan tabel aspek layanan, klasifikasi, dan grafik batang. _Dashboard_ ini membantu pimpinan melakukan evaluasi cepat, menentukan prioritas peningkatan, dan mendukung pengambilan keputusan berbasis data.

<!-- Start of picture text -->
& semrikueny) [iliaiaealao © beian x<br>© dashboard<br>Hasil Kuesioner<br>—<br>D&S Fier HaiKuesioner<br>evade Aaderic Jeni Kueioner status Pension Program Std<br>Semester<br>Ganj 2024) ¥ Sem ene © Semua status Seman Program Std ¥<br>Nama Juma Status Statue<br>EvalueKuesonerDosen oleh Mahassws PS mester Ganjran402s e vode Rexpondeno Pengivian EvalFenn) As<br>valu Layenan Fautas Semesteraana02s Gan o 2<br>omEva Layanan oleh Mahasisna_ 2a2402sSemester ani o =<br>EvsuasLayananTugas<br>cen Abie Semester2024025Ganji o<br>Kepussan Dosen Semester2a24r02sGanji o GE<br>Kepuasn<br>Tenaga Kependiian Semesterzan4r02s Ganj o ou<br>Kegan Aso Semesteraana02s nj o<br>‘onze zona<br>Kepuasan Pengguna Lulusan Semester2a24202s nj o<br>Kepuasan<br>Mir Kersama —_Sameter202472025 Ganji o<br><Sebetnnga [I seanuina<br><!-- End of picture text -->

Gambar 66 _._ Halaman Kelola Hasil Kuesioner – SPM (Pimpinan)

Halaman Kelola Hasil Kuesioner memungkinakan pimpinan fakultas untuk memantau hasil evaluasi layanan. Seperti admin, pimpinan dapat melihat rata-rata hasil seluruh kuesioner dalam bentuk tabel dan grafik interaktif berdasarkan periode dan program studi. Hasil evaluasi ditampilkan berdasarkan lima aspek kualitas layanan: _Reliability, Responsiveness, Assurance, Empathy,_ dan _Tangible,_ disertai nilai rata-rata, jumlah responden, periode pengisian, serta kategori penilaian.

Tersedia grafik distribusi penilaian dan grafik nilai per kategori untuk memberikan gambaran menyeluruh. Di bagian bawah, terdapat tabel detail per pertanyaan berisi aspek, isi pertanyaan, skor rata-rata, dan klasifikasi. Halaman ini membantu pimpinan melakukan evaluasi mendalam dalam rangka peningkatan mutu dan pengambilan keputusan berbasis data secara efisien.

# **a. Halaman Detail hasil Kuesioner – Kuesioner**

<!-- Start of picture text -->
pm ota<br>—_ Detail Hai Kuesioner ee<br>ns sa<br>Jee * |= * | “|= °<br>©<br>22 2 ee ste st<br>= ar)<br>wast roms | ac<br>incon iemvoneesniontitiinliniainisiviowed | sal |<br>= aac, | |e<br>—  RpNOAa CIT<br>Ee freed<br>ls Lapa eel » oo<br>=e ee<br>a Se ee<br>en |pmettnnap ar]<br>a 2 @<br><!-- End of picture text -->

Gambar 67. Halaman Kelola Hasil Kuesioner – Kuesioner

Halaman Detail Hasil Kuesioner menampilkan ringkasan pengisian kuesioner oleh responden selama periode evaluasi. Di bagian atas ditampilkan informasi dasar seperti nama kuesioner, jenis layanan, periode, jumlah responden, dan status pelaksanaan.

Rata-rata nilai keseluruhan disertai kategori penilaian dan grafik distribusi kepuasan (Sangat Baik hingga Kurang). Grafik batang horizontal menunjukkan nilai tiap aspek layanan: _Reliability, Responsiveness, Assurance, Empathy_ dan _Tangible_ , lengkap dengan skor rata-rata dan kategorinya.

Tabel detail mencantumkan pertanyaan per aspek, skor rata-rata, kategori, dan jumlah responden, memberikan gambaran spesifik persepsi pengguna. Tampilan visual dan ringkas ini memudahkan pimpinan dalam menganalisis data dan mengambil keputusan strategis untuk peningkatan layanan.

# **b. Halaman Detail hasil Kuesioner – Lihat Detail**

<!-- Start of picture text -->
paantk<br>pian tae ©<br>Daftar Responden rere<br>|<br>No Name Ketegr—tetn Program Sd Tagg engion Ab<br>ee ee ee ee |<br>ee ee re |<br>5 Mihai? CED vn amir sisimowe  tnovansiear<br>ee Ce ee |<br>eCce |<br><!-- End of picture text -->

Gambar 68. Halaman Detail Hasil Kuesioner – Lihat Detail

Halaman di atas adalah Halaman Kelola Hasil Kuesioner – Lihat Detail. Sama seperti admin, pimpinan fakultas dapat melihat daftar responden yang telah mengisi kuesioner.

c. **Halaman Detail Hasil Kuesioner – Responden**

<!-- Start of picture text -->
-<br><!-- End of picture text -->

<!-- Start of picture text -->
- =<br>Co<br><!-- End of picture text -->

Gambar 69. Halaman Detail Hasil Kuesioner – Responden

Halaman di atas adalah Halaman Kelola Hasil Kuesioner – Responden. Sama seperti admin, pimpinan fakultas dapat melihat dengan rinci hasil kuesioner yang diisi oleh responden.

<!-- Start of picture text -->
Laporan Kuesioner<br>st tte aioeAen Da oda poten A<br>rn °<br>+ .Sitios seer“Rte mgtpumps otnams gy a<br>2 Shimer “Ther” oye ans gy Se<br>> teenScie Tamar” Sige os o a<=<br>« Myannly “Tron” Sime tava gg<br>@ eyperentnceeh ec -<br>5 Spanni) Semel aioenan gas cocor<br>poor Cain<br>o eran)<br>a o<br>0s = S| 28<br>‘ce ES oot e= « GSS<br>9 Nap Sas nd ora<br>Dy moe Siete<br>os Scat<br><!-- End of picture text -->

Gambar 70. Halaman Laporan Pimpinan Fakultas

Halaman Laporan SPM FIK UPNVJ dirancang untuk menampilkan laporan kuesioner berdasarkan semester dan tahun akademik tertentu. Sama seperti Admin, Pimpinan fakultas dapat memilih periode waktu melalui menu dropdown untuk memfilter data laporan yang relevan. Tabel di bawahnya memuat informasi seperti nomor, semester, tahun akademik, nama kuesioner, dan opsi cetak untuk setiap laporan. Sama seperti admin, tombol “Lihat” memungkinkan pimpinan untuk melihat detail kuesioner. Sementara itu, tombol “Cetak Laporan” dapat digunakan untuk menghasilkan dokumen laporan hasil kuesioner dalam format PDF. Di

bawahnya, tombol “Cetak Lampiran” disediakan untuk mencetak dokumen pendukung atau detail jawaban kuesioner sebagai bagian dari dokumentasi dalam format PDF. Lalu, tombol “ _Export to Excel_ ”  untuk mendapatkan data lampiran dalam format excel. Halaman ini mempermudah pengelolaan, pencetakan, dan analisis hasil kuesioner secara terorganisir untuk mendukung evaluasi dan peningkatan layanan fakultas.

<!-- Start of picture text -->
te matigen tgp md<br>— ue =|" i<br>coSt n s a=. |on |<br>7 tenn sal 1 he 25 os<br>Aaa enh<br>inintenlionoae<br>aie<br>cn<br>Tid ani 0)<br>(era cae il apt dt<br><!-- End of picture text -->

<!-- Start of picture text -->
Det acces<br>—<br>|: 2 |=" * eam &<br>Se<br>= se _<br>ss<br>~ =<br>~ " =<br>—<br>~ =<br><!-- End of picture text -->

Gambar 71. Halaman Detail Laporan – Pimpinan

Halaman Detail Laporan – Pimpinan menyajikan ringkasan hasil evaluasi kuesioner pada periode akademik tertentu. Di bagian atas terdapat informasi utama seperti judul, tipe, periode, jumlah responden dan pertanyaan, status laporan, serta waktu pembuatan. Tersedia tombol untuk mencetak laporan, mencetak detail, dan mengunduh PDF.

Statistik utama ditampilkan secara visual, meliputi jumlah responden, skor rata-rata, dan kategori penilaian (skala 1–4). Distribusi nilai ditampilkan dalam grafik, sementara komposisi kategori responden divisualisasikan dalam pie chart.

Rata-rata per aspek layanan ( _Reliability, Responsiveness, Assurance, Empathy, Tangible_ ) ditampilkan dalam grafik dan tabel, lengkap dengan nilai

dan kategorinya. Detail per pertanyaan juga disediakan, termasuk skor ratarata dan jumlah responden.

Bagian akhir menampilkan tabel ringkasan responden serta kolom analisis, kesimpulan, dan rencana tindak lanjut (RTL) sebagai dokumentasi evaluasi dan rekomendasi perbaikan layanan.

**2.3.2. Fitur**

Tabel 3. Fitur _Website_ SPM FIK UPNVJ

|**No**|**Fitur**|**Deksripsi**|**Pengguna**|
|---|---|---|---|
|1.|Registrasi|Memungkinkan<br>Alumni<br>untuk<br>mendaftarkan akun baru dengan<br>mengisi informasi identitas diri<br>seperti nama,_email_, program<br>studi, nomor telepon, tahun lulus|Alumni|
|2.|_Login_|Memberikan izin akses masuk ke<br>system untuk pengguna SIAKAD<br>seperti Mahasiswa, Dosen, Tenaga<br>Kependidikan,<br>Admin,<br>dan|Mahasiswa,<br>Dosen, Tenaga<br>Kependidikan,<br>Admin,|
|||Pimpinan Fakultas serta juga<br>Alumni agar dapat menggunakan<br>fitur – fitur sesuai peran dan<br>kebutuhannya.|Pimpinan<br>Fakultas,<br>dan<br>Alumni|
|3.|Pengisian<br>Kuesioner|Pengguna dapat mengisi kuesioner<br>sesuai hak akses dan kategorinya.<br>Tersedia untuk 9 jenis kuesioner.|Mahasiswa,<br>Dosen, Tendik,<br>Alumni, Mitra,<br>Pengguna<br>Lulusan|
|4.|_Dashboard_<br>SPM<br>Interaktif|Menampilkan nilai SPM rata-rata,<br>grafik radar, grafik distribusi aspek<br>layanan, dan detail per kuesioner.|Semua<br>Pengguna|

|5.|Riwayat<br>Pengisian<br>Kuesioner|Memungkinkan pengguna melihat<br>daftar kuesioner yang telah diisi,<br>lengkap dengan tanggal pengisian,<br>serta dapat menampilkan kembali<br>tanggapan atau jawaban yang telah<br>diberikan.|Semua<br>responden<br>_Login_|
|---|---|---|---|
|6.|Kelola<br>Kuesioner|Membuat, mengedit, menghapus,<br>dan menduplikasi kuesioner serta<br>menambahkan<br>pertanyaan<br>berdasarkan aspek layanan.|Admin|
|7.|Hasil<br>Kuesioner|Menampilkan<br>hasil<br>kuesioner<br>dalam bentuk tabel, rata-rata nilai<br>per aspek dan kategori, grafik, dan<br>laporan detail per pertanyaan.|Admin,<br>Pimpinan|
|8.|Kelola<br>Kategori<br>Responden|Menentukan kuesioner mana yang<br>dapat<br>diakses<br>oleh<br>kategori<br>responden tertentu.|Admin|
|9.|Kelola<br>Jadwal<br>Kuesioner|Menambah,<br>mengedit,<br>menghapus,<br>dan<br>mengaktifkan<br>periode<br>akademik<br>untuk<br>pelaksanaan kuesioner.|Admin|
|10.|Laporan dan<br>Cetak PDF|Menyajikan<br>laporan<br>kuesioner<br>lengkap dengan fitur cetak hasil<br>laporan dan lampiran dalam format<br>PDF.|Admin,<br>Pimpinan|
|11.|Cetak<br>lampiran<br>PDF|Mencetak data hasil kuesioner<br>berupa statistik pertanyaan dan<br>tabulasi data responden dalam<br>format PDF.|Admin,<br>Pimpinan|
|12|_Export_<br>_To_<br>_Excel_|Mencetak data hasil kuesioner<br>berupa statistik pertanyaan dan|Admin,<br>Pimpinan|

|||tabulasi data responden dalam<br>format Excel.||
|---|---|---|---|
|13.|_Import_data|Meng_Import_hasil isian kuesioner<br>periode sebelumnya dari sumber<br>eksternal,<br>dalam<br>format|Admin|
|||Excel/CSV,<br>ke<br>dalam<br>sistem<br>secara otomatis.||
|14.|Kelola_User_|Menambah,<br>mengedit,<br>atau<br>menghapus data pengguna dan<br>mengatur hak akses berdasarkan<br>kategori.|Admin|
|15.|Grafik Hasil|Visualisasi<br>hasil<br>penilaian|Admin,|
||Evaluasi Per|berdasarkan<br>aspek<br>layanan|Pimpinan|
||Aspek dan|(_Reliability,_<br>_Responsiveness,_||
||Kategori|_Assurance, Empathy, Tangible_)<br>dan kategori kuesioner.||
|16.|Detail<br>Jawaban<br>Responden|Melihat jawaban individu lengkap<br>dari setiap responden, termasuk<br>komentar dan skor per pertanyaan.|Admin|
|17.|Manajemen|Mengizinkan<br>pengguna<br>untuk|Semua|
||Profil|memperbarui<br>informasi<br>profil<br>seperti foto dan lain-lain|Pengguna<br>_Login_|

# **2.3.3.  Perancangan Kategori Nilai dan Logika Perhitungan Evaluasi Layanan**

Untuk mendukung proses interpretasi hasil evaluasi layanan di lingkungan FIK UPN "Veteran" Jakarta, sistem dirancang dengan skema kategori nilai mutu pelayanan. Skema ini bertujuan untuk menyederhanakan pemaknaan data kuantitatif menjadi klasifikasi kualitatif yang lebih mudah dipahami oleh pimpinan, admin, maupun pengguna lain yang terlibat. Perancangan sistem evaluasi layanan tidak hanya menekankan pada proses pengumpulan data, tetapi juga pada bagaimana data tersebut diinterpretasikan dan disajikan secara informatif. Dalam konteks ini, diperlukan perumusan kategori nilai dan logika perhitungan yang dapat

digunakan sebagai dasar untuk menilai mutu layanan berdasarkan persepsi pengguna.

# **1. Perancangan Kategori Nilai**

Rentang kategori mutu pelayanan dalam sistem ini disusun berpedoman pada sistem pada fakultas sebelumnya yaitu berprinsip skala _Likert_ 4 poin, di mana setiap responden memberikan penilaian dari skor 1 hingga 4 untuk setiap pertanyaan dalam masing – masing kuesioner. Skor ini merepresentasikan persepsi mereka terhadap kualitas layanan yang diberikan. Setiap pertanyaan menggunakan skala Likert 4 poin, dengan rincian sebagai berikut:

Tabel 4. Skor Nilai Jawaban Kuesioner

|**Skor Liktert**|**Interpretasi**|
|---|---|
|1|Kurang|
|2|Cukup|
|3|Baik|
|4|Sangat Baik|

Karena nilai minimum adalah 1 dan maksimum adalah 4, maka perancangan rentang kategori dilakukan dengan membagi distribusi nilai rata-rata berdasarkan kecenderungan jawaban:

- **a. Rata-rata < 2.00**

   - Mengindikasikan mayoritas responden memilih skor rendah (1–2), yang berarti terdapat persepsi negatif terhadap layanan, Kategori: Kurang

- **b. Rata-rata ≥ 2.00 hingga < 3.00**

   - Mencerminkan dominasi jawaban netral hingga cukup puas, Kategori: Cukup

- **c. Rata-rata ≥ 3.00 hingga < 3.50**

   - Menggambarkan kecenderungan jawaban positif (nilai 3), Kategori: Baik

- **d. Rata-rata ≥ 3.50 hingga 4.00**

   - Menunjukkan dominasi penilaian sangat baik, Kategori: Sangat Baik

Dengan logika tersebut, sistem dapat mengubah data kuantitatif menjadi klasifikasi kualitatif yang lebih komunikatif dan mudah ditindaklanjuti. Untuk mendukung keterbacaan dan penyampaian informasi yang intuitif, setiap kategori nilai disajikan dalam warna berbeda yang telah dirancang secara psikologis dan fungsional:

- a. **Merah** untuk _Kurang_ , memberikan sinyal peringatan atau atensi tinggi terhadap masalah layanan.

- b. **Kuning** untuk _Cukup_ , menandakan area perhatian yang memerlukan perbaikan.

- c. **Biru** untuk _Baik_ , mencerminkan stabilitas, kepercayaan, dan kepuasan umum.

- d. **Hijau** untuk _Sangat Baik_ , menggambarkan keberhasilan, kualitas tinggi, dan kepuasan maksimal.

Pemilihan warna ini mengikuti prinsip psikologi warna dalam antarmuka pengguna ( _User_ interface), di mana setiap warna memiliki asosiasi emosional dan persepsi yang membantu pengguna memahami kondisi layanan dengan cepat tanpa membaca angka secara mendalam.

Sebagai penegasan dari logika perancangan kategori nilai mutu, berikut disajikan tabel rentang rata-rata, kategori penilaian, dan interpretasi mutu layanan:

Tabel 5. Tabel Rancangan Kategori Nilai SPM FIK UPNVJ

|**Kategori**<br>**Nilai**|**Rentang Nilai**<br>**Rata-Rata**|**Warna**|**Interpretasi Mutu**|
|---|---|---|---|
|Kurang|< 2.00|Merah|Persepsi<br>negatif<br>terhadap|
||||layanan|
|Cukup|≥ 2.00 – < 3.00|Kuning|Persepsi<br>cukup,<br>area<br>perlu<br>peningkatan|
|Baik|≥ 3.00 – < 3.50|Biru|Persepsi positif terhadap layanan|
|Sangat|≥ 3.50 – 4.00|Hijau|Kepuasan<br>tinggi,<br>persepsi|
|Baik|||layanan sangat baik|

# **2. Perancangan Logika Perhitungan Evaluasi Layanan**

Evaluasi layanan dilakukan melalui kuesioner yang terdiri dari beberapa pertanyaan yang mewakili lima aspek mutu layanan: _Reliability_ , _Responsiveness_ , _Assurance_ , _Empathy_ , dan _Tangible_ . Setiap pertanyaan dijawab dengan skala Likert (1 hingga 4), yang kemudian diolah secara sistematis.

- a. Rata – rata per pertanyaan

Sistem menghitung nilai rata – rata  per pertanyaan yang dinilai oleh sejumlah responden.

Rumus perhitungannya adalah:

# **Keterangan:**

- 𝑥̅𝑝𝑖 = rata-rata skor pada satu pertanyaan (P1, P2, ..., P10)

- 𝑥𝑖 = skor dari masing-masing responden pada pertanyaan tersebut

- 𝑛 = jumlah responden

- ∑𝑛𝑖=1 𝑥𝑖= jumlah semua skor dari seluruh responden

- b. Rata – rata per Aspek

Sistem menghitung nilai rata – rata  per aspek yang terdiri dari beberapa pertanyaan.

Rumus perhitungannya adalah:

# **Keterangan:**

- 𝑥̅𝑎𝑠𝑝𝑒𝑘 = rata-rata skor untuk satu kategori/aspek layanan (misalnya: Reliability, Responsiveness, dll)

- 𝑥𝑖𝑗 = skor dari responden ke-i pada pertanyaan ke-j dalam aspek tersebut

- 𝑚 = jumlah pertanyaan dalam aspek tersebut

- 𝑛 = jumlah responden

- ∑𝑚𝑗=1 ∑𝑛𝑖=1 𝑥𝑖𝑗= total skor seluruh pertanyaan dalam aspek

c. Rata – rata per Kuesioner

Sistem menghitung nilai rata-rata dari seluruh jawaban pada setiap kuesioner. Rumus perhitungannya adalah:

# **Keterangan:**

- 𝑥̅𝑘𝑢𝑒𝑠𝑖𝑜𝑛𝑒𝑟 = rata-rata skor seluruh pertanyaan dalam satu kuesioner

- 𝑥̅𝑝𝑗𝑖 = rata-rata skor dari pertanyaan ke-j

- 𝑚 = jumlah pertanyaan dalam satu kuesioner

- ∑𝑚𝑗=1 𝑥̅𝑝𝑗= total seluruh rata – rata dari setiap pertanyaan

# d. Nilai Total SPM FIK UPNVJ

Sistem juga menghitung nilai rata-rata dari seluruh kuesioner aktif pada suatu periode sebagai cerminan performa layanan secara institusional. Rumus yang digunakan:

# **Keterangan:**

- 𝑥̅𝑖 = nilai rata-rata dari kuesioner ke-i

- 9 = jumlah total kuesioner yang dinilai

Nilai tersebut kemudian diklasifikasikan ke dalam kategori mutu berdasarkan rentang yang telah dijelaskan, didapat jika nilai rata – rata = 3,8 maka termasuk dalam kategori sangat baik.

# **2.4. Rencana Pengujian Proyek**

Pengujian sistem dilakukan menggunakan metode _black-box Testing_ , yaitu pengujian yang berfokus pada fungsi sistem tanpa melihat struktur internal kode program. Dalam metode ini, penguji hanya mengamati input dan output dari setiap fitur yang ada, sesuai dengan skenario penggunaan yang telah dirancang. Tujuan dari pengujian ini adalah untuk memastikan bahwa seluruh fitur dapat berjalan sesuai dengan kebutuhan pengguna dan menghasilkan keluaran yang benar. Pengujian dilakukan terhadap semua peran pengguna dalam sistem, mulai dari mahasiswa, dosen, tenaga kependidikan, alumni, mitra kerja sama, pengguna lulusan, hingga admin dan pimpinan fakultas. Setiap aktor diuji berdasarkan fungsionalitas yang mereka akses, seperti proses _Login_ , pengisian kuesioner, melihat hasil, hingga pengelolaan data dan laporan evaluasi. Hasil yang diharapkan dari pengujian ini adalah semua fitur dapat dijalankan tanpa error, validasi berjalan sesuai aturan, dan data yang dihasilkan akurat. Jika ditemukan bug atau ketidaksesuaian, dilakukan perbaikan dan pengujian ulang hingga sistem berfungsi dengan baik pada seluruh skenario yang diuji.

# **2.4.1.** **_Blackbox Testing_ Akun Mahasiswa**

Tabel 6. _Scenario Blackbox Testing_ Akun Mahasiswa

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page_<br>_Website_|Mahasiswa dapat mengakses_Landing_<br>_Page Website_|
|2.|_Login_dengan_Username_(NIM)<br>dan_password_|Mahasiswa dapat masuk ke halaman<br>_Dashboard_Mahasiswa|
|3.|Mengakses<br>halaman<br>_Dashboard_utama|Mahasiswa dapat mengakses halaman<br>_Dashboard_utama dan semua elemen<br>tampil dengan benar|
||Fitur_D_|_ashboard_|
|4.|Mengakses<br>_Dashboard_|Mahasiswa<br>dapat<br>mengakses|
||Evaluasi Kepuasan Layanan<br>Fakultas|_Dashboard_Evaluasi Layanan  Fakultas|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|5.|Mengakses<br>_Dashboard_|Mahasiswa<br>dapat<br>mengakses|
||Evaluasi<br>Layanan<br>oleh<br>Mahasiswa|_Dashboard_Evaluasi Layanan oleh<br>Mahasiswa|
|6.|Mengakses<br>_Dashboard_|Mahasiswa<br>dapat<br>mengakses|
||Evaluasi<br>Dosen<br>oleh<br>Mahasiswa|_Dashboard_<br>Evaluasi<br>Dosen<br>oleh<br>Mahasiswa|
|7.|Mengakses<br>_Dashboard_<br>Evaluasi Layanan Tugas Akhir|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Layanan Tugas<br>Akhir|
|8.|Mengakses<br>_Dashboard_<br>Evaluasi Kepuasan Dosen|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Kepuasan Dosen|
|9.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Kepuasan<br>Tenaga<br>Kependidikan|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan<br>Tenaga<br>Kependidikan|
|10.|Mengakses<br>_Dashboard_<br>Kepuasan Alumni|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Alumni|
|11.|Mengakses<br>_Dashboard_<br>Kepuasan Pengguna Lulusan|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan<br>Pengguna<br>Lulusan|
|12.|Mengakses<br>_Dashboard_<br>Kepuasan Mitra Kerjasama|Mahasiswa<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Mitra Kerjasama|
||<br>Fitur Isi|<br>Kuesioner|
|13.|Navigasi<br>ke<br>halaman<br>Isi<br>Kuesioner dari_dashboard_|Mahasiswa dapat Klik “Isi Kuesioner”,<br>berhasil navigasi ke halaman Isi<br>Kuesioner dari_dashboard_|
|14.|Menampilkan daftar Kuesioner<br>Tersedia|Mahasiswa dapat mengakses kuesioner<br>tersedia|
|15.|Mengisi kuesioner Evaluasi<br>Kepuasan Layanan Fakultas|Mahasiswa dapat mengisi kuesioner<br>Evaluasi Kepuasan Layanan Fakultas,<br>dan jawaban berhasil tersimpan.|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|16.|Mengisi Kuesioner Evaluasi<br>Layanan oleh Mahasiswa|Mahasiswa dapat mengisi kuesioner<br>Evaluasi Layanan oleh Mahasiswa dan<br>jawaban berhasil tersimpan.|
|17.|Mengisi Kuesioner Evaluasi<br>Dosen oleh Mahasiswa|Mahasiswa dapat mengisi kuesioner<br>Evaluasi Dosen oleh Mahasiswa dan<br>jawaban berhasil tersimpan|
|18.<br>|Mengisi Kuesioner Evaluasi<br>Layanan Tugas Akhir<br>Fitur<br> <br>|Mahasiswa dapat  mengisi kuesioner<br>Evaluasi Layanan Tugas Akhir dan<br>jawaban berhasil tersimpan.<br>Riwayat<br>|
|19.|Mengakses<br>menu<br>Riwayat<br>Kuesioner|Mahasiswa dapat mengakses menu<br>Riwayat Kuesioner dan berhasil melihat<br>riwayat kuesioner.|
|20.|Klik<br>tombol<br>Detail<br>pada<br>riwayat kuesioner|Mahasiswa dapat melihat detail jawaban<br>kuesioner dengan mengklik tombol<br>Detail pada riwayat yang tersedia.|
||Fitu|<br>r Profil|
|21.|Melihat Profil|Mahasiswa dapat mengakses profil dan<br>berhasil<br>melihat<br>foto<br>profil<br>dan<br>informasi akun|
|21.|Melakukan Ubah_Profile_|Mahasiswa dapat mengubah foto profil<br>dan informasi akun dan berhasil<br>disimpan.|
|22.|Melakukan ubah_Password_|Mahasiswa dapat mengubah_password,_<br>dengan memasukkan_password_saat ini,<br>_password_baru dan konfirmasi_password_<br>baru|
|23.|Melakukan_logout_|Mahasiswa dapat melakukan_logout_dan<br>diarahkan kembali ke_landing page_|

# **2.4.2** **_. Blackbox Testing_ Akun Dosen**

Tabel 7. _Scenario Blackbox Testing_ Akun Dosen

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses_Landing Page_<br>_Website_|Dosen dapat mengakses_Landing Page_<br>_Website_|
|2.|_Login_dengan_Username_<br>(NIDN) dan_password_|Dosen dapat masuk ke halaman_Dashboard_<br>Dosen.|
|3.|Mengakses<br>halaman<br>_Dashboard_utama setelah<br>_Login_|Dosen dapat mengakses halaman_Dashboard_<br>utama dan semua elemen tampil dengan<br>benar|
||Fit|ur_Dashboard_|
|4.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Kepuasan<br>Layanan Fakultas|Dosen dapat mengakses_Dashboard_Evaluasi<br>Layanan  Fakultas|
|5.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Layanan<br>oleh<br>Mahasiswa|Dosen dapat mengakses_Dashboard_Evaluasi<br>Layanan oleh Mahasiswa|
|6.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Dosen<br>oleh<br>Mahasiswa|Dosen dapat mengakses_Dashboard_Evaluasi<br>Dosen oleh Mahasiswa|
|7.|Mengakses<br>_Dashboard_<br>Evaluasi Layanan Tugas<br>Akhir|Dosen dapat mengakses_Dashboard_Evaluasi<br>Layanan Tugas Akhir|
|8.|Mengakses<br>_Dashboard_<br>Evaluasi Kepuasan Dosen|Dosen dapat mengakses_Dashboard_Evaluasi<br>Kepuasan Dosen|
|9.|Mengakses<br>_Dashboard_<br>Evaluasi Kepuasan Tenaga<br>Kependidikan|Dosen<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan Tenaga Kependidikan|
|10.|Mengakses<br>_Dashboard_<br>Kepuasan Alumni|Dosen<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan Alumni|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|11.|Mengakses<br>_Dashboard_<br>Kepuasan<br>Pengguna<br>Lulusan|Dosen<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan Pengguna Lulusan|
|12.|Mengakses<br>_Dashboard_<br>Kepuasan Mitra Kerjasama|Dosen<br>dapat<br>mengakses<br>_Dashboard_<br>Kepuasan Mitra Kerjasama|
||<br>Fitu|<br>r Isi Kuesioner|
|13.|Navigasi ke halaman Isi<br>Kuesioner dari_dashboard_|Dosen dapat Klik “Isi Kuesioner”, berhasil<br>navigasi ke halaman Isi Kuesioner dari<br>_dashboard_|
|14.|Menampilkan<br>daftar<br>Kuesioner Tersedia|Dosen dapat mengakses kuesioner tersedia|
|16.|Mengisi<br>Kuesioner<br>Evaluasi Layanan Fakultas|Dosen dapat mengisi kuesioner Evaluasi<br>Kepuasan Layanan Fakultas, dan jawaban<br>berhasil tersimpan.|
|16.|Mengisi<br>Kuesioner<br>Evaluasi Kepuasan Dosen<br>F|Dosen dapat mengisi kuesioner Evaluasi<br>Kepuasan Dosen dan jawaban berhasil<br>tersimpan.<br>itur Riwayat|
|17.|Mengakses menu Riwayat<br>Kuesioner|Dosen dapat mengakses menu Riwayat<br>Kuesioner dan berhasil melihat riwayat<br>kuesioner.|
|18.|Klik tombol Detail pada<br>riwayat kuesioner|Dosen<br>dapat<br>melihat<br>detail<br>jawaban<br>kuesioner dengan mengklik tombol Detail<br>pada riwayat yang tersedia.<br>Fitur Profil|
|19.|Melihat Profil|Dosen dapat mengakses profil dan berhasil<br>melihat foto profil dan informasi akun|
|20.|Melakukan Ubah_Profile_|Dosen dapat mengubah foto profil dan<br>informasi akun dan berhasil disimpan.|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|21.|Melakukan ubah_Password_|Dosen dapat mengubah_password,_dengan|
|||memasukkan_password_saat ini,_password_|
|||baru dan konfirmasi_password_baru|
|22.|Melakukan_logout_|Dosen dapat melakukan_logout_dan diarahkan<br>kembali ke_landing page_|

# **2.4.3** **_. Blackbox Testing_ akun Tenaga Kependidikan**

Tabel 8. _Scenario Blackbox Testing Akun Tenaga Kependidikan_

|**No**|**Skenario Pengujian**|**Hasil Yang diharapk**|**an**|
|---|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page Website_|Tenaga<br>Kependidikan<br>dapat<br>_Landing Page Website_|mengakses|
|2.|_Login_dengan_Username_<br>(NIK) dan_password_|Tenaga Kependidikan dapat masu<br>_Dashboard_Tenaga Kependidikan|k ke halaman<br>|
|3.<br>|Mengakses<br>halaman<br>_Dashboard_<br>utama<br>setelah_Login_<br> <br>|Tenaga<br>Kependidikan<br>dapat<br>halaman_Dashboard_utama dan s<br>tampil dengan benar<br>Fitur_Dashboard_<br> <br> <br>|<br>mengakses<br>emua elemen<br>|
|4.|Mengakses_Dashboard_<br>Evaluasi<br>Kepuasan<br>Layanan Fakultas|Tenaga<br>Kependidikan<br>dapat<br>_Dashboard_Evaluasi Layanan  Fa|mengakses<br>kultas|
|5.|Mengakses_Dashboard_<br>Evaluasi Layanan oleh<br>Mahasiswa|Tenaga<br>Kependidikan<br>dapat<br>_Dashboard_Evaluasi Layanan<br>Kependidikan|mengakses<br>oleh Tenaga|
|6.|Mengakses_Dashboard_<br>Evaluasi<br>Dosen<br>oleh<br>Mahasiswa|Tenaga<br>Kependidikan<br>dapat<br>_Dashboard_Evaluasi Tenaga<br>oleh Tenaga Kependidikan|mengakses<br>Kependidikan|
|7.|Mengakses_Dashboard_<br>Evaluasi Layanan Tugas<br>Akhir|Tenaga<br>Kependidikan<br>dapat<br>_Dashboard_Evaluasi Layanan Tug|mengakses<br>as Akhir|

|**No**|**Skenario**|**Pengujian**||**Hasil Yang diharapk**|**an**|
|---|---|---|---|---|---|
|8.|Mengakses<br>Evaluasi<br>Dosen|_Dashboard_<br>Kepuasan|Tenaga<br>_Dashboa_|Kependidikan<br>dapat<br>_rd_Evaluasi Kepuasan Do|mengakses<br>sen|
|9.|Mengakses<br>Evaluasi<br>Tenaga Kepe|_Dashboard_<br>Kepuasan<br>ndidikan|Tenaga<br>_Dashboa_|Kependidikan<br>dapat<br>_rd_Kepuasan Tenaga Kep|mengakses<br>endidikan|
|10.|Mengakses<br>Kepuasan Al|_Dashboard_<br>umni|Tenaga<br>_Dashboa_|Kependidikan<br>dapat<br>_rd_Kepuasan Alumni|mengakses|
|11.|Mengakses<br>Kepuasan<br>Lulusan|_Dashboard_<br>Pengguna|Tenaga<br>_Dashboa_|Kependidikan<br>dapat<br>_rd_Kepuasan Pengguna L|mengakses<br>ulusan|
|12.|Mengakses<br>Kepuasan<br>Kerjasama|_Dashboard_<br>Mitra<br>F|Tenaga<br>_Dashboa_<br>itur Isi Ku|Kependidikan<br>dapat<br>_rd_Kepuasan Mitra Kerja<br>esioner|mengakses<br>sama|
|13.|Navigasi ke<br>Kuesioner<br>_dashboard_|halaman Isi<br>dari|Tenaga<br>Kuesione<br>Kuesione|Kependidikan<br>dapat<br>r”, berhasil navigasi ke<br>r dari_dashboard_|Klik<br>“Isi<br>halaman Isi|
|14.|Menampilka<br>Kuesioner T|n<br>daftar<br>ersedia|Tenaga<br>kuesioner|Kependidikan<br>dapat<br>tersedia|mengakses|
|15.|Mengisi<br>Evaluasi<br>Fakultas|Kuesioner<br>Layanan|Tenaga K<br>Evaluasi<br>jawaban|ependidikan dapat meng<br>Kepuasan Layanan F<br>berhasil tersimpan.|isi kuesioner<br>akultas, dan|
|16.|Mengisi<br>Evaluasi<br>Tenaga Kepe|Kuesioner<br>Kepuasan<br>ndidikan|Tenaga K<br>Evaluasi<br>jawaban<br>Fitur Riw|ependidikan dapat meng<br>Kepuasan Tenaga Kepe<br>berhasil tersimpan.<br>ayat|isi kuesioner<br>ndidikan dan|
|17.|Mengakses<br>Riwayat Kue|menu<br>sioner|Tenaga K<br>Riwayat<br>riwayat k|ependidikan dapat men<br>Kuesioner dan berh<br>uesioner.|gakses menu<br>asil melihat|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|18.|Klik tombol Detail pada<br>riwayat kuesioner|Tenaga Kependidikan dapat melihat detail<br>jawaban kuesioner dengan mengklik tombol<br>Detail pada riwayat yang tersedia.<br>Fitur Profil|
|19.|Melihat Profil|Tenaga Kependidikan dapat mengakses profil<br>dan berhasil melihat foto profil dan informasi<br>akun|
|20.|Melakukan Ubah_Profile_|Tenaga Kependidikan dapat mengubah foto<br>profil dan informasi akun dan berhasil<br>disimpan.|
|21.|Melakukan<br>ubah<br>_Password_|Tenaga<br>Kependidikan<br>dapat<br>mengubah<br>_password,_dengan memasukkan_password_saat<br>ini,_password_baru dan konfirmasi_password_<br>baru|
|22.|Melakukan_logout_|Tenaga Kependidikan dapat melakukan_logout_<br>dan diarahkan kembali ke_landing page_|

# **2.4.4.** **_Blackbox Testing_ akun Alumni**

Tabel 9. _Scenario Blackbox Testing_ Akun Alumni

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page Website_|Alumni dapat mengakses_Landing Page_<br>_Website_|
|2.|Registrasi akun alumni|Alumni dapat mengisi formulir registrasi<br>dengan lengkap dan valid, sistem melakukan<br>validasi data (seperti NIK,_email_, dan NPWP),<br>lalu akun berhasil dibuat dan alumni dapat<br>_Login_ke sistem menggunakan akun tersebut<br>tanpa error.|
|3.|_Login_dengan_Username_<br>(_email_) dan_password_|Alumni dapat Masuk ke halaman_Dashboard_<br>Alumni|

|**No**|**Skenario**|**Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|---|
|4.|Mengakses<br>_Dashboard_<br>setelah_Login_|halaman<br>utama<br>|Alumni dapat mengakses halaman_Dashboard_<br>utama dan semua elemen tampil dengan benar|
||||Fitur_Dashboard_|
|5.|Mengakses<br>Evaluasi<br>Layanan Fak|_Dashboard_<br>Kepuasan<br>ultas|Alumni dapat mengakses_Dashboard_Evaluasi<br>Layanan  Fakultas|
|6.|Mengakses<br>Evaluasi La<br>Mahasiswa|_Dashboard_<br>yanan oleh|Alumni dapat mengakses_Dashboard_Evaluasi<br>Layanan oleh Mahasiswa|
|7.|Mengakses<br>Evaluasi<br>D<br>Mahasiswa|_Dashboard_<br>osen<br>oleh|Alumni dapat mengakses_Dashboard_Evaluasi<br>Dosen oleh Mahasiswa|
|8.|Mengakses<br>Evaluasi Lay<br>Akhir|_Dashboard_<br>anan Tugas|Alumni dapat mengakses_Dashboard_Evaluasi<br>Layanan Tugas Akhir|
|9.|Mengakses<br>Evaluasi<br>Dosen|_Dashboard_<br>Kepuasan|Alumni dapat mengakses_Dashboard_Evaluasi<br>Kepuasan Tenaga Dosen|
|10.|Mengakses<br>Evaluasi<br>Tenaga Kepe|_Dashboard_<br>Kepuasan<br>ndidikan|Alumni dapat mengakses_Dashboard_Kepuasan<br>Tenaga Kependidikan|
|11.|Mengakses<br>Kepuasan Al|_Dashboard_<br>umni|Alumni dapat mengakses_Dashboard_Kepuasan<br>Alumni|
|12.|Mengakses<br>Kepuasan<br>Lulusan|_Dashboard_<br>Pengguna|Alumni dapat mengakses_Dashboard_Kepuasan<br>Pengguna Lulusan|
|13.|Mengakses<br>Kepuasan<br>Kerjasama|_Dashboard_<br>Mitra<br>F|Alumni dapat mengakses_Dashboard_Kepuasan<br>Mitra Kerjasama<br>itur Isi Kuesioner|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|14.|Navigasi ke halaman Isi|Alumni dapat Klik “Isi Kuesioner”, berhasil|
||Kuesioner<br>dari<br>_dashboard_|navigasi ke halaman Isi Kuesioner dari<br>_dashboard_|
|15.|Menampilkan<br>daftar<br>Kuesioner Tersedia|Alumni dapat mengakses kuesioner tersedia|
|16.|Mengisi<br>kuesioner<br>Kepuasan Alumni|Alumni dapat mengisi kuesioner Evaluasi<br>Kepuasan Alumni, dan jawaban berhasil<br>tersimpan.|
|||Fitur Riwayat|
|17.|Mengakses<br>menu<br>Riwayat Kuesioner|Alumni dapat mengakses menu Riwayat<br>Kuesioner dan berhasil melihat riwayat<br>kuesioner.|
|18.|Klik tombol Detail pada<br>riwayat kuesioner|Alumni dapat melihat detail jawaban kuesioner<br>dengan mengklik tombol Detail pada riwayat<br>yang tersedia.|
|||Fitur Profil|
|19.|Melihat Profil|Alumni dapat mengakses profil dan berhasil<br>melihat foto profil dan informasi akun|
|20.|Melakukan Ubah_Profile_|Alumni dapat mengubah foto profil dan<br>informasi akun dan berhasil disimpan.|
|21.|Melakukan<br>ubah<br>_Password_|Alumni dapat mengubah_password,_dengan<br>memasukkan_password_saat ini,_password_baru<br>dan konfirmasi_password_baru|
|22.|Melakukan_logout_|Alumni dapat melakukan_logout_dan diarahkan<br>kembali ke_landing page_|

# **2.4.5** **_. Blackbox Testing_ akun Pengguna Lulusan**

Tabel 10. _Scenario Blackbox Testing_ Akun Pengguna Lulusan

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page Website_|Pengguna Lulusan dapat  mengakses_Landing_<br>_Page Website_|
|2.|Mengakses<br>halaman<br>_Dashboard_publik|Pengguna Lulusan dapat mengakses halaman<br>_Dashboard_utama dan semua elemen tampil<br>dengan benar|
|||Fitur_Dashboard_|
|5.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Kepuasan<br>Layanan Fakultas|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Layanan  Fakultas|
|6.|Mengakses<br>_Dashboard_<br>Evaluasi Layanan oleh<br>Mahasiswa|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Layanan oleh Mahasiswa|
|7.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Dosen<br>oleh<br>Mahasiswa|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Dosen oleh Mahasiswa|
|8.|Mengakses<br>_Dashboard_<br>Evaluasi Layanan Tugas<br>Akhir|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Layanan Tugas Akhir|
|9.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Kepuasan<br>Dosen|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Evaluasi Kepuasan Dosen|
|10.|Mengakses<br>_Dashboard_<br>Evaluasi<br>Kepuasan<br>Tenaga Kependidikan|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Tenaga Kependidikan|
|11.|Mengakses<br>_Dashboard_<br>Kepuasan Alumni|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Alumni|

|**No**|**Skenario**|**Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|---|
|12.|Mengakses<br>Kepuasan<br>Lulusan|_Dashboard_<br>Pengguna|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Pengguna Lulusan|
|13.|Mengakses<br>Kepuasan<br>Kerjasama|_Dashboard_<br>Mitra<br>Fitur|Pengguna<br>Lulusan<br>dapat<br>mengakses<br>_Dashboard_Kepuasan Mitra Kerjasama<br>Isi Kuesioner Publik|
|14.|Navigasi ke<br>Kuesioner<br>_dashboard_|halaman Isi<br>dari|Pengguna Lulusan dapat Klik “Isi Kuesioner”,<br>berhasil navigasi ke halaman Isi Kuesioner dari<br>_dashboard._|
|15.|Menampilka<br>Kuesioner T|n<br>daftar<br>ersedia|Pengguna Lulusan dapat mengakses kuesioner<br>tersedia.|
|14.|Mengisi for<br>pengguna lul|mulir isian<br>usan|Pemgguna Lulusan dapat mengisi formulir<br>isian pengguna lulusan.|
|15.|Mengisi<br>Kepuasan<br>Lulusan|kuesioner<br>Pengguna|Pengguna Lulusan dapat mengisi Kuesioner<br>Kepuasan Pengguna Lulusan dan jawaban<br>berhasil tersimpan.|

**2.4.6.** **_Blackbox Testing_ akun Mitra Kerjasama**

Tabel 11. _Scenario Blackbox Testing_ Akun Mitra Kerjasama

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page Website_|Mitra Kerjasama dapat mengakses_Landing Page_<br>_Website_|
|2.|Mengakses<br>halaman<br>_Dashboard_Publik|Mitra Kerjasama dapat mengakses halaman<br>_Dashboard_utama dan semua elemen tampil<br>dengan benar|
|||Fitur_Dashboard_|
|3.|Mengakses_Dashboard_<br>Evaluasi<br>Kepuasan<br>Layanan Fakultas|Mitra Kerjasama dapat mengakses_Dashboard_<br>Evaluasi Layanan  Fakultas|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|4.|Mengakses_Dashboard_<br>Evaluasi Layanan oleh<br>Mahasiswa|Mitra Kerjasama dapat mengakses_Dashboard_<br>Evaluasi Layanan oleh Mahasiswa|
|5.|Mengakses_Dashboard_<br>Evaluasi Dosen oleh<br>Mahasiswa|Mitra Kerjasama dapat mengakses_Dashboard_<br>Evaluasi Dosen oleh Mahasiswa|
|6.|Mengakses_Dashboard_<br>Evaluasi<br>Layanan<br>Tugas Akhir|Mitra Kerjasama dapat mengakses_Dashboard_<br>Evaluasi Layanan Tugas Akhir|
|7.|Mengakses_Dashboard_<br>Evaluasi<br>Kepuasan<br>Tenaga Kependidikan|Mitra Kerjasama dapat mengakses_Dashboard_<br>Evaluasi Kepuasan Dosen|
|8.|Mengakses_Dashboard_<br>Kepuasan Alumni|Mitra Kerjasama dapat mengakses_Dashboard_<br>Kepuasan Tenaga Kependidikan|
|9.|Mengakses_Dashboard_<br>Kepuasan<br>Pengguna<br>Lulusan|Mitra Kerjasama dapat mengakses_Dashboard_<br>Kepuasan Alumni|
|10.|Mengakses_Dashboard_<br>Kepuasan<br>Mitra<br>Kerjasama|Mitra Kerjasama dapat mengakses_Dashboard_<br>Kepuasan Pengguna Lulusan|
||<br>Fitu|r Isi Kuesioner Publik|
|11.|Navigasi ke halaman Isi<br>Kuesioner<br>dari<br>_dashboard_|Mitra Kerjasama dapat Klik “Isi Kuesioner”,<br>berhasil navigasi ke halaman Isi Kuesioner dari<br>_dashboard._|
|12.|Menampilkan<br>daftar<br>Kuesioner Tersedia|Mitra Kerjasama dapat mengakses kuesioner<br>tersedia.|
|13.|Mengisi formulir isian<br>mitra kerjasama|Pemgguna Lulusan dapat mengisi formulir isian<br>pengguna lulusan.|
|14.|Mengisi<br>kuesioner<br>Kepuasan<br>mitra<br>kerjasama|Mitra Kerjasama dapat mengisi Kuesioner<br>Kepuasan Mitra Kerjasama dan jawaban berhasil<br>tersimpan.|

# **2.4.7.** **_Blackbox Testing_ Akun Admin**

Tabel 12. _Scenario Blackbox Testing_ Akun Admin

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|1.|Mengakses<br>_Landing_<br>_Page Website_|Admin dapat mengakses_Landing Page Website_|
|2.|_Login_<br>dengan<br>_Username_<br>dan<br>_password_|Admin dapat masuk ke halaman_Dashboard_<br>Admin<br>Fitur_Dashboard_|
|3.|Mengakses<br>halaman<br>_Dashboard_Admin|Admin dapat mengakses halaman_dashboard_<br>Admin|
|4.|Melakukan<br>_filter_<br>periode|Admin<br>dapat<br>mem_filter_<br>data<br>_dashboard_<br>berdasarkan periode|
||Fi|tur Kelola Kuesioner|
|5.|Mengakses<br>halaman<br>Kelola Kuesioner|Admin dapat melihat daftar kuesioner dengan<br>informasi lengkap.|
|6.|Melakukan_filter_daftar<br>kuesioner berdasarkan<br>periode akademik|Admin dapat memfilter kuesioner berdasarkan<br>periode.|
|7.|Memilih<br>Tambah<br>Kuesioner|Admin dapat membuka form penambahan<br>kuesioner baru dan menyimpan data|
|8.|Memilih tombol Edit<br>(ikon pensil) pada salah<br>satu kuesioner|Admin dapat membuka form edit data kuesioner<br>dan mengubah data.|
|9.|Memilih tombol Hapus<br>(ikon tempat sampah)<br>pada<br>salah<br>satu<br>kuesioner|Admin dapat menghapus kuesioner setelah<br>konfirmasi.|
||Fit|ur Kelola Pertanyaan|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|10.|Memilih tombol Lihat<br>(ikon mata) pada salah<br>satu kuesioner|Admin dapat melihat detail informasi dan daftar<br>pertanyaan.|
|11.|Memilih<br>Tambah<br>Pertanyaan|Admin dapat menambah pertanyaan dan<br>menyimpan ke sistem.|
|12.|Memilih tombol Edit<br>(ikon pensil) pada salah<br>satu pertanyaan|Admin dapat mengedit data pertanyaan.|
|13.|Memilih tombol Hapus<br>(ikon tempat sampah)<br>pada<br>salah<br>satu<br>pertanyaan<br> <br>|Admin dapat menghapus pertanyaan setelah<br>konfirmasi.<br>Fitur Kelola Hasil<br>|
|14.|Mengakses<br>halaman<br>Hasil Kuesioner|Admin dapat melihat semua daftar hasil<br>kuesioner|
|15.|Filter hasil kuesioner<br>berdasarkan<br>Periode<br>Akademik|Admin<br>dapat<br>memfilter<br>hasil<br>kuesioner<br>berdasarkan periode.|
|16.|Filter hasil kuesioner<br>berdasarkan<br>Jenis<br>Kuesioner|Admin dapat memfilter hasil berdasarkan jenis<br>kuesioner.|
|17.|Filter hasil berdasarkan<br>Status Pengisian|Admin dapat melihat data sesuai status<br>pengisian.|
|18|Filter hasil berdasarkan<br>Program Studi|Admin dapat memfilter data berdasarkan<br>program studi.|
|19.|Klik<br>tombol<br>Detail<br>Evaluasi (ikon grafik)|Admin dapat melihat grafik dan tabel evaluasi<br>lengkap|
|20.|Klik tombol "Kembali"|Admin kembali ke halaman sebelumnya.|
||Fitur D|etail Jawaban Responden|
|21.|Klik tombol "Daftar<br>Responden"|Admin<br>dapat<br>melihat<br>daftar<br>responden<br>kuesioner|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|22.|Filter daftar responden<br>berdasarkan<br>Program<br>Studi|Admin dapat memfilter responden berdasarkan<br>program studi|
|23.|Klik<br>tombol<br>Lihat<br>Detail (ikon mata) pada<br>responden|Admin dapat melihat detail jawaban responden|
|24.|Klik<br>tombol<br>Hapus<br>(ikon tempat sampah)<br>pada responden|Admin dapat menghapus data responden setelah<br>konfirmasi|
|25.|Klik tombol Kembali<br>ke Daftar|Admin kembali ke halaman daftar responden|
|26.<br>|Klik<br>tombol<br>Hapus<br>Data<br>Responden<br>di<br>_Danger Zone_<br>Fitu<br> <br>|Admin<br>dapat<br>menghapus<br>data<br>jawaban<br>responden secara permanen<br>r Kategori Responden<br>|
|27.|Mengakses<br>halaman<br>Kategori Responden|Menampilkan semua tab kategori responden dan<br>daftar nama kuesioner|
|28.|Memilih<br>atau<br>tidak<br>memilih<br>kuesioner<br>tertentu pada kategori|Admin dapat melakukan centang/uncentang<br>kuesioner yang dapat diakses oleh kategori<br>responden tersebut dan berhasil disimpan.|
|29.|Klik tombol Simpan<br>Perubahan<br>setelah<br>mengatur kuesioner<br>Fitur|Admin dapat melihat daftar periode akademik<br>Kelola Jadwal Kuesioner|
|30.|Mengakses<br>halaman<br>Kelola<br>Jadwal<br>Kuesioner|Admin dapat melihat semua tab kategori dan<br>daftar kuesioner|
|31.|Menambahkan periode<br>akademik baru|Admin dapat memilih atau menghapus akses<br>kuesioner|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|32.|Mengedit<br>periode<br>akademik (klik ikon<br>edit)|Admin dapat melihat daftar periode akademik|
|33.|Mengaktifkan periode<br>akademik tertentu|Admin dapat melihat semua tab kategori dan<br>daftar kuesioner|
|34.|Menghapus<br>periode<br>akademik|Admin dapat memilih atau menghapus akses<br>kuesioner|
|||<br>Fitur Laporan|
|35.|Mengakses<br>halaman<br>Laporan Kuesioner|Admin dapat mengakses halaman laporan dan<br>melihat daftar kuesioner.|
|36.|Klik<br>tombol<br>Lihat<br>laporan kuesioner|Admin dapat melihat detail evaluasi kuesioner<br>yang dipilih.|
|37.|Klik<br>tombol<br>Detail<br>pada<br>ringkasan<br>responden|Admin<br>dapat<br>membuka<br>detail<br>jawaban<br>responden.|
|38.|Mengisi<br>Analisa<br>&<br>Pembahasan,<br>Simpulan, dan Rencana<br>Tindak Lanjut (RTL)|Admin dapat mengisi dan menyimpan konten<br>laporan|
|39.|Klik tombol Simpan<br>Konten|Admin dapat menyimpan konten laporan dan<br>muncul notifikasi berhasil|
|40.|Klik<br>tombol<br>Cetak<br>Laporan<br>untuk<br>mencetak<br>laporan<br>evaluasi<br>kuesioner<br>yang dipilih|Admin dapat mencetak laporan evaluasi dalam<br>format PDF yang rapi|
|41.|Klik<br>tombol<br>Cetak<br>Lampiran<br>untuk<br>mencetak<br>lampiran<br>kuesioner|Admin dapat mencetak file lampiran jawaban<br>responden|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|42.|Klik tombol “_Export To_<br>_Excel_”|Admin dapat mencetak data tabulasi responden<br>dalam bentuk Excel|
|||Fitur_Import_Data|
|43.|Mengakses halaman<br>_Import_Data|Admin dapat mengakses halaman_Import_data|
|44.|Memilih<br>jenis<br>kuesioner<br>dari<br>dropdown|Admin dapat memilih jenis kuesioner ingin<br>di_Import_dan melihat template data_exciting_|
|45.|Mengunduh<br>template<br>data_exciting_|Admin dapat mengunduh template data yang<br>sesuai dengan struktur file|
|46.|Menggunggah<br>file<br>_excel_sesuai template|Admin dapat mengimpor data dari file, dan<br>sistem menyimpan ke_database_|
|||<br>Fitur Kelola_User_|
|46.|Mengakses<br>halaman<br>Kelola_User_|Admin dapat melihat daftar pengguna lengkap<br>dengan nama, email, kategori, dan status|
|47.|Menggunakan<br>filter<br>berdasarkan<br>kategori<br>_User_|Admin dapat memfilter pengguna berdasarkan<br>kategori (Mahasiswa, Dosen, Tendik, dll.)|
|48.|Menggunakan<br>fitur<br>pencarian berdasarkan<br>nama/_email_/NIM|Admin dapat menggunakan fitur perncarian<br>pencarian sesuai kata kunci yang dimasukkan|
|49.|Menambah_User_baru|Admin dapat membuka formulir tambah_User_<br>dan menyimpan data baru dengan sukses|
|50.|Mengedit data_User_|Admin dapat membuka membuka formulir edit<br>_User_dan menyimpan perubahan tanpa error|
|51.|Mengubah<br>status<br>aktif/nonaktif_User_|Admin dapat mengubah status aktif/nonaktif<br>pengguna secara langsung|
|52.|Menghapus_User_|Admin dapat menghapus_User_<br>Fitur Profil|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|53.|Melihat Profil|Admin dapat mengakses profil dan berhasil<br>melihat foto profil dan informasi akun|
|54.|Melakukan<br>Ubah<br>_Profile_|Admin dapat mengubah foto profil dan<br>informasi akun dan berhasil disimpan.|
|55.|Melakukan<br>ubah<br>_Password_|Admin dapat mengubah_password,_dengan<br>memasukkan_password_saat ini,_password_baru<br>dan konfirmasi_password_baru|
|56.|Melakukan_logout_|Admin dapat melakukan_logout_dan diarahkan<br>kembali ke_landing page_|

# **2.4.8** **_. Blackbox Testing_ Akun Pimpinan Fakultas**

Tabel 13. _Scenario Blackbox Testing_ Akun Pimpinan Fakultas

|**No**|**Skenario Pe**|**ngujian**||**Hasil Yang diharapkan**|
|---|---|---|---|---|
|1.|Mengakses<br>_Page Website_|_Landing_|Pimpinan<br>_Page Web_|Fakultas dapat mengakses_Landing_<br>_site_|
|2.|_Login_dengan <br>dan_password_|_Username_|Pimpinan<br>_Dashboar_|Fakultas dapat masuk ke halaman<br>_d_Pimpinan Fakultas|
||||Fitur_Das_|_hboard_|
|3.|Mengakses<br>_Dashboard_<br>Fakultas|halaman<br>Pimpinan|Pimpinan<br>Pimpinan|Fakultas dapat mengakses_Dashboard_<br>Fakultas|
|4.|Melakukan<br>periode|filter|Pimpinan<br>diinginkan<br>sesuai pili<br>Fitur Kelo|dapat memilih periode akademik yang<br>, lalu_dashboard_memperbarui data<br>han.<br>la Hasil|
|5.|Mengakses<br>Hasil Kuesion|halaman<br>er|Pimpinan<br>hasil kues|Fakultas dapat melihat semua daftar<br>ioner|
|6.|Filter hasil<br>berdasarkan<br>Akademik|kuesioner<br>Periode|Pimpinan<br>kuesioner|<br>Fakultas<br>dapat<br>memfilter<br>hasil<br>berdasarkan periode.|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|7.|Filter hasil kuesioner<br>berdasarkan<br>Jenis<br>Kuesioner|Pimpinan<br>Fakultas<br>dapat<br>memfilter<br>hasil<br>berdasarkan jenis kuesioner.|
|8.|Filter hasil berdasarkan<br>Status Pengisian|Pimpinan Fakultas dapat melihat data sesuai<br>status pengisian.|
|9.|Filter hasil berdasarkan<br>Program Studi|Pimpinan<br>Fakultas<br>dapat<br>memfilter<br>data<br>berdasarkan program studi.|
|10.|Klik<br>tombol<br>Detail<br>Evaluasi (ikon grafik)|Pimpinan Fakultas dapat melihat grafik dan tabel<br>evaluasi lengkap|
|11.|Klik tombol "Kembali"|Pimpinan Fakultas dapat melihat semua daftar<br>hasil kuesioner|
||Fitur D|etail Jawaban Responden|
|12.|Klik<br>tombol<br>"Daftar<br>Responden"|Pimpinan Fakultas dapat melihat daftar responden<br>kuesioner|
|13.|Filter daftar responden<br>berdasarkan<br>Program<br>Studi|Pimpinan Fakultas dapat memfilter responden<br>berdasarkan program studi|
|14.|Klik tombol Lihat Detail<br>(ikon<br>mata)<br>pada<br>responden|Pimpinan Fakultas dapat melihat detail jawaban<br>responden|
|15.|Klik<br>tombol<br>Hapus<br>(ikon tempat sampah)<br>pada responden|Pimpinan Fakultas kembali ke halaman daftar<br>responden<br>Fitur Laporan|
|16.|Mengakses<br>halaman<br>Laporan Kuesioner|Pimpinan Fakultas dapat mengakses halaman<br>laporan dan melihat daftar kuesioner.|
|17.|Klik<br>tombol<br>Lihat<br>laporan kuesioner|Pimpinan Fakultas dapat melihat detail evaluasi<br>kuesioner yang dipilih.|
|18.|Klik tombol Detail pada<br>ringkasan responden|Pimpinan Fakultas<br>dapat<br>membuka detail<br>jawaban responden.|

|**No**|**Skenario Pengujian**|**Hasil Yang diharapkan**|
|---|---|---|
|19.|Klik<br>tombol<br>Cetak<br>Laporan<br>untuk<br>mencetak<br>laporan<br>evaluasi kuesioner yang<br>dipilih|Pimpinan Fakultas dapat mencetak laporan<br>evaluasi dalam format PDF yang rapi|
|20.|Klik<br>tombol<br>Cetak<br>Lampiran<br>untuk<br>mencetak<br>lampiran<br>kuesioner|Pimpinan Fakultas dapat mencetak file lampiran<br>jawaban responden|
|21.|Klik tombol “_Export To_<br>_Excel_”|Pimpinan Fakultas dapat mencetak data tabulasi<br>responden dalam bentuk Excel|
|||Fitur Profil|
|22.|Melihat Profil|Pimpinan Fakultas dapat mengakses profil dan<br>berhasil melihat foto profil dan informasi akun|
|23.|Melakukan<br>Ubah<br>_Profile_|Pimpinan Fakultas dapat mengubah foto profil<br>dan informasi akun dan berhasil disimpan.|
|24.|Melakukan<br>ubah<br>_Password_|Pimpinan Fakultas dapat mengubah_password,_<br>dengan memasukkan_password_saat ini,_password_<br>baru dan konfirmasi_password_baru|
|25.|Melakukan_logout_|Pimpinan Fakultas dapat melakukan_logout_dan<br>diarahkan kembali ke_landing page_|


# PROYEK PENGEMBANGAN SISTEM INFORMASI STUDENT EXCHANGE PADA FAKULTAS ILMU KOMPUTER UPN “VETERAN” JAKARTA

# **BAB II**

# **RANCANGAN PRODUK**

# **2.1 Observasi**

Pada bagian observasi ini akan menjelaskan bagaimana sistem yang selama ini berjalan untuk mendukung program student exchange pada Fakultas Ilmu Komputer dalam memahami alur kerja, data yang dibutuhkan, serta aktor yang berperan dalam program student exchange untuk mencapai sebuah keberhasilan dalam menunjang program student exchange bagi Fakultas Ilmu Komputer. Selain itu, dilakukan identifikasi masalah berdasarkan analisis sistem yang berjalan yang akan menjadi dasar pengembangan sistem informasi program student exchange untuk solusi yang lebih efisien. Adapun penjelasannya sebagai berikut.

# **2.1.1 Diagram Sistem Berjalan**

Pada tahapan ini dilakukan penggambaran skema terkait dengan proses program _student exchange_ yang sudah berjalan pada Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Penggambaran ini dilakukan dikarenakan Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta saat ini belum memiliki alur proses yang resmi dan datadata yang dibutuhkan dalam program _student exchange_ ini belum terintegrasi. Untuk mencari informasi mengenai IISMA dan PMM, Mahasiswa melihat dari _website_ kampus merdeka. Untuk informasi mengenai program _mobility_ kerja sama antar universitas, hanya beberapa Mahasiswa yang mendapat informasi tersebut melalui Dosen. Data-data mahasiswa yang terdaftar, _logbook_ harian mahasiswa, sampai dengan laporan akhir kegiatan di _upload_ melalui _google form._ Dengan demikian, berdasarkan hasil wawancara penulis dengan Dosen PIC program _exchange_ , Fakultas Ilmu Komputer belum memiliki sistem informasi yang terintegrasi untuk mendukung program _student exchange_ . Adapun penggambaran alur program _student exchange_ yang dimiliki oleh Fakultas Ilmu Komputer tergambar pada gambar 2.1 berikut.

<!-- Start of picture text -->
{==)-<br><!-- End of picture text -->

Gambar 2.1 Diagram Sistem Berjalan

Pada gambar 2.1 diatas menunjukkan alur kerja dalam proses _student exchange_ Fakultas Ilmu Komputer UPN "Veteran" Jakarta. Alur proses pelaksanaan program _Student Exchange_ melibatkan tiga aktor utama, yaitu Mahasiswa, Admin, dan Dosen PIC _Student Exchange_ . Proses dimulai ketika mahasiswa mengisi _form_ pengajuan surat rekomendasi yang sebelumnya telah dibuat dan disiapkan oleh Admin. Setelah pengajuan dilakukan, Admin menyimpan data tersebut dalam _google drive_ sebagai bentuk dokumentasi.

Kemudian, Admin membuat _form_ pendaftaran program _Student Exchange_ dan membagikan _link_ -Nya kepada Mahasiswa. Mahasiswa mengisi _form_ pendaftaran tersebut, lalu data yang terkumpul digunakan oleh Dosen PIC untuk melakukan proses seleksi. Setelah seleksi selesai, Dosen PIC menyampaikan hasil seleksi kepada Admin, dan Admin menyebarkan informasi pengumuman kepada Mahasiswa yang lolos.

Bagi Mahasiswa yang dinyatakan lolos, proses dilanjutkan ke tahap pendataan ulang. Admin membuat form pendataan ulang dan membagikan _link_ -Nya kepada Mahasiswa. Setelah diisi oleh Mahasiswa, admin kembali menyimpan data pendataan ulang ke dalam _google drive_ . Selanjutnya, proses penentuan Dosen Pembimbing dilakukan oleh Dosen PIC. Setelah ditentukan, Admin menyebarkan informasi Dosen Pembimbing kepada Mahasiswa yang bersangkutan.

Setelah program _Student Exchange_ selesai dijalankan oleh Mahasiswa, Admin membuat _form_ pengumpulan laporan kegiatan dan menyebarkan _link_ -Nya. Mahasiswa mengisi _form_ laporan tersebut, dan Dosen PIC melakukan pengecekan serta validasi terhadap laporan yang dikumpulkan. Setelah laporan dinyatakan valid, proses konversi SKS dilakukan sebagai bentuk pengakuan akademik

terhadap kegiatan _Student Exchange_ yang telah dijalani. Sebagai tahapan akhir, admin menyimpan seluruh data laporan kegiatan ke dalam _google drive._

# **2.1.2 Identifikasi Masalah**

Proses identifikasi masalah diambil dari hasil observasi lingkungan penelitian dan diolah menjadi kebutuhan dari perancangan sistem informasi _Student Exchange_ pada Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta, serta dibuat tabel perbandingan sistem dengan menggunakan metode PIECES yang mempunyai 6 (enam) variabel evaluasi, antara lain _performance_ , _information_ , _economic, control, efficiency_ , dan _service._ Berikut adalah hasil analisis yang telah ditentukan.

|**Aspek**|**Proses**|**Identifikasi**|**Deskripsi Masalah**|
|---|---|---|---|
|**PIECES**||**Masalah**||
|**_Performance_**|Pengumpulan<br>data mahasiswa|Kinerja lambat<br>Akibat proses<br>pengumpulan data<br>masih dilakukan<br>secara manual|Pengumpulan data<br>mahasiswa secara<br>manual menghambat<br>kinerja aktor yang<br>terkait dan<br>mengurangi<br>kecepatan proses<br>input data.|
|**_Information_**|Penyebaran<br>informasi<br>mengenai<br>program student<br>exchange yang<br>tersedia|Keterbatasan<br>informasi yang<br>dapat diakses<br>secara_real-_<br>_time_|Pada sistem yang<br>berjalan saat ini<br>informasi yang<br>diberikan oleh pihak<br>fakultas<br>menggunakan_group_<br>_WhatsApp,_yang<br>menyebabkan<br>informasi mengenai|

||||program student<br>exchange yang<br>tersedia tidak dapat<br>diakses secara_real-_<br>_time_oleh mahasiswa.|
|---|---|---|---|
|**_Economy_**|Proses<br>pemantauan<br>program|Biaya waktu dan<br>tenaga tinggi untuk<br>pemantauan<br>keberhasilan<br>program secara<br>manual|Proses pemantauan<br>program secara<br>manual membutuhkan<br>waktu lama dan<br>sumber daya yang<br>lebih banyak,<br>mengakibatkan<br>inefisiensi biaya.<br>Oleh karena itu,<br>diperlukannya sistem<br>informasi yang<br>terintegrasi dalam<br>memantau<br>berjalannya program<br>dengan baik.|
|**_Control_**|Proses<br>penyimpanan<br>data|Data disimpan<br>dalam<br>penyimpanan yang<br>tidak aman dan<br>beresiko kehilangan<br>data|Pada sistem yang<br>berjalan saat ini<br>_control_dilakukan<br>secara manual<br>melalui_google form_<br>sehingga<br>memungkinkan<br>terjadinya kehilangan<br>data saat dibutuhkan|

|**_Efficiency_**|Proses pencarian<br>data|Proses pencarian<br>data masih<br>dilakukan secara<br>manual|Pada sistem yang<br>berjalan saat ini<br>proses pengumpulan<br>_logbook_kegiatan dan<br>laporan akhir masih<br>dilakukan dengan<br>_google form_, dan<br>untuk proses<br>pendaftaran pada<br>_student mobility_<br>_exchange_juga masih<br>melalui_google form_<br>sehingga<br>membutuhkan waktu<br>yang lama apabila<br>data tersebut<br>dibutuhkan|
|---|---|---|---|
|**_Service_**|Evaluasi oleh<br>Pemangku<br>kepentingan<br>Fakultas|Keterbatasan<br>layanan evaluasi<br>dan<br>pengambilan<br>keputusan secara<br>_real-time_|Pemangku<br>kepentingan<br>membutuhkan<br>evaluasi data yang<br>cepat dan akurat<br>untuk pengambilan<br>keputusan,  namun<br>saat ini hanya tersedia<br>dalam bentuk laporan<br>saja|

Tabel 2.1 Identifikasi Masalah

# **2.1.3 Solusi Penyelesaian Masalah**

Berdasarkan identifikasi permasalahan pada sistem pengambilan keputusan yang sedang berjalan pada Fakultas Ilmu Komputer UPN “Veteran” Jakarta yang dianalisis dengan menggunakan metode PIECES, dapat disimpulkan bahwa diperlukan sebuah pengembangan sistem informasi student exchange yang terintegrasi untuk meningkatkan kinerja dari berjalannya proses program exchange, seperti peningkatan layanan informasi program secara _real-time_ , menyediakan layanan pendaftaran, layanan pengajuan surat rekomendasi dan layanan bimbingan untuk mempermudah mahasiswa yang mengikuti program, mengurangi biaya oprasional, menampung data yang terintegrasi, dan memberikan layanan yang lebih efektif kepada mahasiswa serta para pemangku kepentingan Fakultas Ilmu Komputer dalam pengambilan keputusan. Setiap solusi yang penulis berikan, diharapkan dapat memaksimalkan efisiensi dari kinerja dalam setiap proses program student exchange secara menyeluruh. Detail dari solusi tersebut terdapat pada tabel 2.2 berikut.

|**Aspek PIECES**|**Identifikasi**<br>**Masalah**|**Solusi**|**Deskripsi**<br>**Solusi**|
|---|---|---|---|
|**_Performance_**|Tidak ada<br>pemantauan_real-_<br>_time_terhadap<br>data mahasiswa<br>yang mendaftar,<br>kelengkapan<br>dokumen, hingga<br>laporan|Mengembangkan<br>fitur pemantauan<br>_real-time_terhadap<br>data dalam sistem<br>informasi program<br>exchange|Sistem<br>informasi<br>program<br>exchange ini<br>akan memiliki<br>fitur<br>pemantauan<br>data secara_real-_<br>_time_, sehingga<br>data yang ada<br>_up-to-date_|

|**_Information_**|Informasi<br>mengenai<br>program<br>exchange yang<br>tersedia tidak_up-_<br>_to-date_|Mengintegrasikan<br>sistem informasi<br>student exchange<br>dengan sumber<br>data internal<br>fakultas yang<br>diperbarui secara<br>berkala|Sistem<br>informasi<br>student<br>exchange akan<br>mengambil data<br>dari berbagai<br>sumber secara<br>otomatis untuk<br>memastikan<br>informasi yang<br>tersedia selalu<br>_up-to-date._|
|---|---|---|---|
|**_Economy_**|Memerlukan<br>biaya lebih untuk<br>pemantauan<br>keberhasilan<br>program secara<br>manual|Mengotomatisasi<br>semua proses yang<br>ada pada program<br>student exchange<br>melalui sistem<br>informasi yang<br>terintegrasi|Sistem<br>informasi yang<br>terintegrasi ini<br>akan<br>mengurangi<br>kebutuhan<br>tenaga<br>manual untuk<br>pengumpulan<br>data,<br>sehingga<br>menekan<br>biaya<br>operasional<br>dan waktu.|
|**_Control_**|Terbatasnya<br>kontrol pada<br>penyimpanan|Menambahkan<br>fitur<br>kontrol akses yang|Sistem<br>informasi ini<br>akan memiliki|

||data, sehingga<br>beresiko<br>kehilangan dan<br>penyalahgunaan<br>data|terstruktur dalam<br>penyimpanan data|sistem control<br>pada<br>penyimpanan<br>data,<br>sehingga data<br>hanya<br>dapat diakses<br>oleh<br>pihak yang<br>berwenang dan<br>tidak terjadi<br>kehilangan data.|
|---|---|---|---|
|**_Efficiency_**|Proses pencarian<br>data memakan<br>waktu lama<br>karena masih<br>dilakukan secara<br>manual|Menyediakan fitur<br>pencarian dan<br>filter data untuk<br>mempermudah<br>proses pencarian<br>data yang<br>dibutuhkan|Sistem<br>informasi ini<br>akan<br>menampilkan<br>data<br>berdasarkan<br>filterisasi<br>maupun<br>_keyword_yang<br>telah diinputkan<br>untuk<br>mempercepat<br>pencarian data<br>yang<br>dibutuhkan|
|**_Service_**|Hasil dari<br>program dalam<br>bentuk laporan|Menyediakan<br>tampilan laporan<br>hasil program yang|Sistem<br>informasi ini|

|sangat terbatas,|dilengkapi|akan|
|---|---|---|
|sehingga tidak|visualisasi data|menampilkan|
|mendukung para|untuk|visualisasi data|
|pemangku|mempermudah|yang mudah|
|kepentingan|para kepentingan|dipahami oleh|
|dalam|dalam mengambil|para pemangku|
|pengambilan|keputusan|kepentingan|
|keputusan.||dan mendukung<br>pengambilan<br>keputusan.|

Tabel 2.2 Solusi Penyelesaian Masalah

# **2.2 Usulan Solusi**

Pada tahapan ini, penulis memberikan solusi dalam bentuk Data Flow Diagram (DFD) yang menggambarkan alur data dalam sistem secara terstruktur. Data Flow Diagram (DFD) digunakan oleh penulis untuk memvisualisasikan bagaimana aliran data pada proses-proses utama, sumber data, dan penyimpanan data yang diusulkan. Solusi ini dirancang untuk mempermudah pemahaman alur kerja sistem serta membantu dalam identifikasi kebutuhan sistem secara rinci. Dengan adanya Data Flow Diagram (DFD), perancangan sistem dapat dilakukan secara lebih efektif, karena proses-proses dan hubungan antar komponen sistem telah terdefinisikan dengan baik. Adapun penjelasan dari masing-masing bagian tersebut tertera pada penjelasan berikut.

# **2.2.1 Data Flow Diagram (DFD) Level 0**

<!-- Start of picture text -->
informest profs mengelola Informasi program<br>Daftar mahasiswa<br>informasi program<br>Pongajuan SA Verifikasi pendaftaran<br>Mahasiswa Mengisiisi kelengkapankelengkap: dokumen| Mengolola<br>pendaftaran (Kerjasama) dattar mahasiswa<br>Talus pendafaran<br>Ketiasam Informasi program<br>Pendataan (IISMA, PMN),<br>informasi dosen pembimbing Data mahasiswa bimbingannya<br>Upload laporanBimbingankegiatan Sistem ExchangeInformasi Student | Mengelola jadwal bimbingan Dosen Pembimbing<br>Mengelola laporan bimbingan<br>Informasi program<br>Data pengajuan SR Data mahasiswa program<br>Veriikasi pengajuan SR cata simbingan | osen Pic<br>Remark bimbingan<br>Daftar mahasiswa<br>Koordinator Prodi Approve Konversi SKS Verifkasi asi laporanlaporan mahasiswmahasiswa<br>‘Approve bukti pelaksanaan<br>inbound (iisma, kerjasama)<br><!-- End of picture text -->

Gambar 2.2 DFD Level 0

Sistem Informasi _Student Exchange_ dirancang untuk mendukung proses administrasi dan pengelolaan kegiatan pertukaran mahasiswa di lingkungan perguruan tinggi. Berdasarkan Diagram DFD Level 0, sistem ini memiliki lima entitas eksternal utama yang berinteraksi secara langsung, yaitu Mahasiswa, Admin, Koordinator Program Studi (Prodi), Dosen Pembimbing, dan Dosen PIC ( _Person In Charge)._ Proses dimulai dari Mahasiswa yang melakukan pendaftaran melalui sistem dengan mengisi formulir dan mengunggah dokumen persyaratan untuk mengikuti program pertukaran mahasiswa.

Data pendaftaran mahasiswa yang masuk kemudian diverifikasi oleh Admin. Admin memiliki peran penting dalam melakukan validasi awal terhadap kelengkapan data dan dokumen yang diunggah oleh mahasiswa. Selanjutnya, Koordinator Prodi akan menerima data pengajuan dari sistem untuk dilakukan proses verifikasi surat rekomendasi. Jika mahasiswa dinyatakan memenuhi syarat, maka Koordinator Prodi menyetujui pengajuan tersebut dan menyetujui penerbitan surat rekomendasi melalui sistem.

Sementara itu, Dosen Pembimbing memiliki peran sebagai pendamping akademik mahasiswa. Dosen Pembimbing dapat mengakses data mahasiswa untuk keperluan monitoring dan pemberian bimbingan selama program berlangsung. Di

sisi lain, Dosen PIC bertugas dalam proses pemantauan dan pelaporan kegiatan pertukaran mahasiswa. Dosen PIC dapat melihat data mahasiswa yang sudah disetujui untuk mengikuti program, serta turut melakukan pencatatan informasi penting terkait kegiatan tersebut.

Seluruh interaksi antar entitas dilakukan melalui satu proses utama dalam sistem, yaitu proses pengelolaan program _student exchange_ . Sistem ini dirancang untuk mengintegrasikan seluruh proses secara efisien dan terdokumentasi, sehingga mempermudah koordinasi antar peran serta mendukung transparansi dalam pelaksanaan program.

# **2.2.2 Data Flow Diagram (DFD) Level 1**

<!-- Start of picture text -->
_<br>=a<br>- a==><br><!-- End of picture text -->

Gambar 2.3 DFD Level 1

DFD Level 1 Sistem Informasi _Student Exchange_ menggambarkan prosesproses utama yang berlangsung dalam sistem pengelolaan program pertukaran mahasiswa. Diagram ini menguraikan alur interaksi antara entitas eksternal yaitu

Mahasiswa, Admin, Koordinator Program Studi (Koordinator Prodi), Dosen Pembimbing, dan Dosen PIC dengan subsistem yang ada, serta aliran data yang menyertainya.

Seluruh pengguna sistem memulai aktivitas dengan proses Login untuk memperoleh akses sesuai perannya. Mahasiswa, sebagai entitas utama yang menjalani program, dapat mengakses informasi melalui proses Informasi Program, yang memuat detail program pertukaran dan tersimpan dalam “informasi_exchanges”. Tahap awal program dimulai dengan proses Kelengkapan Dokumen, di mana mahasiswa mengunggah dokumen yang diperlukan dan disimpan dalam “document_exchanges”. Setelah dokumen dinyatakan lengkap, mahasiswa mengajukan Surat Rekomendasi (SR) melalui sistem, yang kemudian diverifikasi oleh Koordinator Prodi melalui proses Verifikasi Surat Rekomendasi. Jika disetujui, surat rekomendasi akan diterbitkan dan disimpan dalam “surat_rekomendasi_exchanges”.

Perbedaan alur terjadi pada tahap pendaftaran: untuk mahasiswa _inbound_ , proses pendaftaran dilakukan langsung di dalam sistem internal, dan hanya dapat dilakukan setelah surat rekomendasi disetujui. Proses ini diverifikasi oleh Admin, dan data peserta disimpan dalam “exchange_participants”. Sementara itu, untuk mahasiswa _outbound_ , pendaftaran dilakukan secara eksternal melalui _platform_ Kampus Merdeka, dan hanya dapat dilakukan setelah mahasiswa memperoleh surat rekomendasi dari Koordinator Prodi. Setelah diterima oleh pihak Kampus Merdeka, mahasiswa kembali ke sistem internal untuk melakukan Pendataan, sebagai dasar pelaksanaan proses selanjutnya.

Setelah proses pendaftaran atau pendataan selesai, Admin akan langsung menetapkan dosen pembimbing melalui proses Mengelola Daftar Dosen Pembimbing, yang datanya tercatat dalam “pivot_pembimbing_exchanges”. Dengan penetapan tersebut, Dosen Pembimbing dapat langsung mengatur waktu pertemuan melalui proses Mengelola Jadwal Bimbingan, dengan data jadwal disimpan dalam “jadwal_bimbingan_exchanges”. Selama kegiatan berlangsung, mahasiswa menjalani sesi Bimbingan dengan Dosen Pembimbing. Proses ini

dicatat ke dalam “kehadiran_bimbingan_exchanges”, dan Dosen Pembimbing dapat mengelola catatan melalui proses Mengelola Laporan Bimbingan.

Setelah proses bimbingan selesai, mahasiswa mengunggah Laporan Kegiatan melalui proses _Upload_ Laporan Kegiatan. Laporan yang diunggah akan diverifikasi oleh Admin atau Dosen PIC dalam proses Verifikasi Laporan Kegiatan, dan jika valid akan disimpan dalam “final_report_exchanges”. Bukti pelaksanaan kegiatan diperiksa melalui proses _Approve_ Bukti Pelaksanaan, dan kemudian diikuti dengan proses _Approve_ Konversi SKS, yang menjadi tanggung jawab Koordinator Prodi. Di sisi lain, Dosen PIC memiliki kewenangan khusus untuk memberikan _Remarks_ sebagai bentuk evaluasi tambahan terhadap proses dan hasil kegiatan mahasiswa. Admin dan Dosen PIC juga berperan dalam proses Mengelola Mahasiswa _Inbound_ , yakni peserta pertukaran dari luar institusi, yang datanya juga dikelola dalam sistem.

Dengan alur tersebut, sistem _Student Exchange_ secara menyeluruh mendukung kegiatan pertukaran mahasiswa mulai dari tahap awal administrasi hingga pelaporan hasil program, baik untuk skema _inbound_ maupun _outbound_ , secara terintegrasi dan ter-dokumentasi dengan baik.

# **2.2.3 Data Flow Diagram (DFD) Level 2 Login**

<!-- Start of picture text -->
username dan password<br>oo ata login mahasiswa_—————<br>[ann _| username dan password ata login admin cam<br>ata login<br>dosen :pic username dan password lmaoon 1.2 vatidastData \|,_dosen pic ——— —<br>data login<br>sen<br>dosen username dan password PEMBIMBIPG gosen pembimbing<br>pempimbing<br>data login<br>username dan password aprod vaproai<br>TT<br>fs kontirmas)<br>Kontirmasiiogin Login<br><!-- End of picture text -->

Gambar 2.4 DFD Level 2 Login

Pada proses login dalam sistem informasi student exchange, terdapat lima jenis pengguna yang memiliki akses ke sistem, yaitu mahasiswa, admin, dosen PIC, dosen pembimbing, dan koordinator prodi. Setiap pengguna memulai proses dengan memasukkan username dan password mereka ke dalam sistem melalui proses 1.1 Login. Data login yang dimasukkan oleh masing-masing pengguna kemudian diteruskan ke proses 1.2 Validasi Data.

Pada tahap ini, sistem melakukan pencocokan data login yang diterima dengan data login yang tersimpan di masing-masing basis data pengguna. Validasi dilakukan terhadap data login mahasiswa, data login admin, data login dosen PIC, data login dosen pembimbing, dan data login Koordinator Prodi. Jika data yang dimasukkan sesuai dan valid, maka proses dilanjutkan ke tahap 1.3 Konfirmasi Login. Sistem kemudian memberikan umpan balik berupa konfirmasi login kepada pengguna yang bersangkutan, yang menyatakan bahwa proses autentikasi berhasil dan pengguna dapat mengakses sistem sesuai dengan hak aksesnya.

Secara keseluruhan, proses login ini dirancang untuk menjamin keamanan akses serta memastikan bahwa setiap pengguna hanya bisa masuk dan mengakses fitur sesuai dengan hak dan tanggung jawab masing-masing dalam program pertukaran mahasiswa.

# **2.2.4 Data Flow Diagram (DFD) Level 2 Informasi Kegiatan**

<!-- Start of picture text -->
Informast<br>Admin informasi kegiatan | #1 MengelolaKegiatan<br>informasi kegiatan<br>22 -_—_<br>eranIntormast Informasi_exchan.Moral emhanace<br>pembimbingdosen Kegiatan_/9) informasi cagekegiatan<br>23<br>fenampiikan<br>informasi kegiatan Informasipai informasi kegiatan<br><!-- End of picture text -->

Gambar 2. 5 DFD Level 2 Informasi Kegiatan

Proses pengelolaan informasi kegiatan dalam sistem informasi _student exchange_ dimulai dari entitas Admin, yang memiliki kewenangan untuk menginput atau mengelola informasi kegiatan melalui proses 2.1 Mengelola Informasi Kegiatan. Informasi yang dimasukkan mencakup berbagai data terkait program pertukaran mahasiswa, seperti nama program, periode pelaksanaan, kuota peserta, tanggal penting, dan nama universitas. Informasi tersebut kemudian diteruskan ke proses 2.2 Menyimpan Informasi Kegiatan, yang bertanggung jawab menyimpan data tersebut ke dalam basis data “informasi_exchanges” secara permanen agar dapat diakses oleh pengguna lain.

Selanjutnya, sistem akan menampilkan informasi yang telah tersimpan melalui proses 2.3 Menampilkan Informasi Kegiatan. Pada tahap ini, data ditarik dari basis data dan disajikan kepada seluruh pengguna sistem, termasuk mahasiswa, dosen PIC, dosen pembimbing, dan koordinator prodi (Koordinator Prodi). Proses ini memastikan bahwa semua pihak yang berkepentingan dapat melihat informasi kegiatan terbaru secara _real-time_ dan terpusat dalam sistem. Dengan demikian, proses ini mendukung transparansi serta kemudahan akses terhadap informasi penting seputar program pertukaran mahasiswa.

**2.2.5 Data Flow Diagram (DFD) Level 2 Pengajuan Surat Rekomendasi**

<!-- Start of picture text -->
a2<br>6.1 Pengajuan) validasi<br>pengajuanrekomendasisurat SR rekomendasi}pengajuan™\surat PengajuanSR<br>pengajuan surat<br>rekomendasi<br>32<br>enema ‘surat_rekomendasi_exchanges<br>Pengajuan ' pengajuanrekomendasi surat<br>pengajuan surat -, pengajuan surat<br>Pengajuan<br>Senor rekomendasi _/renampilkanSR rekomendasi<br><!-- End of picture text -->

Gambar 2.6 DFD Level 2 Pengajuan Surat Rekomendasi

Proses pengajuan surat rekomendasi dalam sistem informasi student exchange diawali oleh entitas mahasiswa yang mengajukan permintaan surat rekomendasi melalui proses 3.1 Pengajuan Surat Rekomendasi. Data pengajuan yang dimasukkan oleh mahasiswa mencakup informasi yang diperlukan untuk mendukung permintaan surat tersebut. Setelah data diajukan, sistem akan memprosesnya melalui tahap 3.2 Validasi Pengajuan Surat Rekomendasi, di mana dilakukan pengecekan kelengkapan dan kebenaran data yang diinput oleh mahasiswa. Jika valid, maka data pengajuan surat rekomendasi akan dilanjutkan ke proses berikutnya.

Tahap selanjutnya adalah proses 3.2 Menyimpan Pengajuan Surat Rekomendasi, di mana sistem akan menyimpan data pengajuan surat rekomendasi ke dalam basis data "surat_rekomendasi_exchanges" untuk kemudian dapat diakses oleh pihak yang berwenang. Data yang telah tersimpan ini selanjutnya ditampilkan melalui proses 3.3 Menampilkan Pengajuan Surat Rekomendasi agar dapat dilihat oleh entitas Koordinator Program Studi. Koordinator Program Studi memiliki tanggung jawab untuk melakukan peninjauan dan persetujuan atas pengajuan surat rekomendasi yang diajukan mahasiswa. Dengan demikian, proses ini memastikan bahwa setiap permintaan surat rekomendasi berjalan sesuai prosedur yang ditetapkan dan mendapatkan validasi dari pihak akademik berwenang.

# **2.2.6 Data Flow Diagram (DFD) Level 2 Verifikasi Surat Rekomendasi**

<!-- Start of picture text -->
pengajuan surat 44 pengajuan surat<br>tekomendasi Menampitkan rekomendasi<br>Pengajuan<br>SR<br>sural_rekomendas|_exchanges<br>pengajuan surat<br>42 tekomendasi<br>Verifikasi SR<br>hasil verifikasi<br>43<br>Menyimpan<br>hasil verifikasi hasil<br>lerifikasi SB<br>44<br>hasil verifikasi Menamphas i llkan mahasiswa<br>ferifikasi SB hasil verifikasi<br><!-- End of picture text -->

Gambar 2.7 DFD Level 2 Verifikasi Surat Rekomendasi

Proses verifikasi surat rekomendasi diawali dari proses 4.1 Menampilkan Pengajuan Surat Rekomendasi, dimana sistem mengambil data pengajuan surat rekomendasi yang telah disimpan sebelumnya dan menampilkannya kepada Koordinator Program Studi. Setelah itu, pada proses 4.2 Verifikasi Surat Rekomendasi, Koordinator Program Studi melakukan pemeriksaan dan validasi terhadap isi dan kelengkapan surat rekomendasi yang diajukan oleh mahasiswa. Hasil dari verifikasi ini dapat berupa persetujuan atau penolakan pengajuan tersebut.

Selanjutnya, hasil verifikasi yang dilakukan oleh Koordinator Program Studi akan diproses lebih lanjut dalam proses 4.3 Menyimpan Hasil Verifikasi Surat Rekomendasi. Sistem akan mencatat hasil verifikasi tersebut dan menyimpannya ke dalam basis data "surat_rekomendasi_exchanges". Setelah data hasil verifikasi tersimpan, proses dilanjutkan ke tahap 4.4 Menampilkan Hasil Verifikasi Surat Rekomendasi, dimana sistem akan menampilkan hasil tersebut kepada mahasiswa.

Dengan demikian, mahasiswa dapat mengetahui status akhir dari pengajuan surat rekomendasi yang telah diajukan.

# **2.2.7 Data Flow Diagram (DFD) Level 2 Kelengkapan Dokumen**

<!-- Start of picture text -->
kelengkapan 5A<br>dokumen Mengupload<br>Kelengkapan<br>Dokumen<br>kelengkapan<br>dokumen<br>52 es<br>Menyimpan document_exchanges<br>Kelengkapan kelengkapan<br>Admin Dokumen J“ dokumen<br>53<br>Menampikan<br>kelengkapan Kelengkapan kelengkapan<br>dokumen Domine dokumen<br><!-- End of picture text -->

_G_ ambar 2.8 DFD Level 2 Kelengkapan Dokumen

Proses pengelolaan kelengkapan dokumen dimulai dari aktivitas 5.1 Mengupload Kelengkapan Dokumen, dimana mahasiswa mengunggah dokumendokumen yang diperlukan sebagai syarat untuk mengikuti program _student exchange._ Dokumen yang telah diunggah kemudian diproses dan disimpan melalui proses 5.2 Menyimpan Kelengkapan Dokumen, dimana sistem akan mencatat dan menyimpan data dokumen tersebut ke dalam basis data "document_exchanges".

Setelah disimpan, dokumen yang telah diunggah akan dapat diakses oleh pihak-pihak yang berkepentingan melalui proses 5.3 Menampilkan Kelengkapan Dokumen. Informasi kelengkapan dokumen akan ditampilkan kepada Admin dan Koordinator Prodi sebagai dasar untuk proses lebih lanjut, seperti verifikasi dokumen atau proses pengajuan surat rekomendasi.

# **2.2.8 Data Flow Diagram (DFD) Level 2 Pendaftaran Kerja Sama**

<!-- Start of picture text -->
detail pendaftaran 6.1<br>Melakukan<br>(Kerjasama)<br>detail pendattaran<br>62<br>Validasi<br>Pendaftaran<br>(Kerjasama)<br>detail pendattaran<br>Menyimpan63 —<br>Nenyimpan exchange_participants<br>Kerjasamay/ etail pendaftaran =<br><!-- End of picture text -->

Gambar 2.9 DFD Level 2 Pendaftaran Kerja Sama

Proses pengelolaan pendaftaran kerja ama dimulai dari aktivitas 6.1 Melakukan Pendaftaran Program _Exchange_ Kerja Sama, dimana mahasiswa melihat detail dari pendaftaran untuk mengikuti program _student exchange_ . Setelah mahasiswa melakukan pendaftaran, sistem akan melakukan proses 6.2 Validasi Pendaftaran Kerja Sama. Kemudian data pendaftaran akan diproses dan disimpan melalui proses 6.3 Menyimpan Pendaftaran Kerja Sama, dimana sistem akan mencatat dan menyimpan data pendaftaran program _exchange_ kerja sama tersebut ke dalam basis data "exchange_participants".

# **2.2.9 Data Flow Diagram (DFD) Level 2 Verifikasi Pendaftaran**

<!-- Start of picture text -->
71<br>Menampitkan<br>detail pendaftaran | Pendaftaran | detail pendaftaran<br>(Kerjasama)<br>72<br>Verifikasi<br>Pendattaran “~~ detail pendaftaran<br>exchange_participants (Kerjasama)<br>hasil verifikasi<br>73<br>Menyimpan<br>hasil verifikasi hasil<br>Verifikasi<br>74<br>Menampilkan’<br>hesilsil verifkasiverifica VerifikasiLana hasil verifikasi<br><!-- End of picture text -->

Gambar 2.10 DFD Level 2 Verifikasi Pendaftaran

Proses verifikasi pendaftaran kerja sama dimulai dari proses 7.1 Menampilkan Pendaftaran Program _Exchange_ Kerja Sama, dimana sistem akan menampilkan data pendaftar dari _databas_ e "exchange_participants" kepada Admin. Lalu, Admin akan melakukan proses 7.2 Verifikasi Pendaftaran Program Kerja Sama. Jika sudah verifikasi, sistem akan melakukan proses 7.3 Menyimpan Hasil Verifikasi, hasilnya akan disimpan ke dalam _database_ "exchange_participants". Kemudian, sistem akan melakukan proses 7.4 Menampilkan Hasil Verifikasi yang akan bisa diakses oleh mahasiswa.

# **2.2.10 Data Flow Diagram (DFD) Level 2 Pendataan IISMA dan PMM**

<!-- Start of picture text -->
data mahasiswa | PendataanMelakukan4 PendataanValidasi82<br>(lisMa, PM) / data mahasiswa \ (lISMA, PMM)<br>data mahasiswa<br>dosen pic 83 _—_=<br>Menyimpan exchange_participants<br>Pendataan | data mahasiswa oe pare<br>(lisMa, PMM)<br>dosen<br>pemibimbing<br>84<br>Menampitkan<br>data mahasiswa (lisa,PendataanPMM) data mahasiswa<br><!-- End of picture text -->

Gambar 2.11 DFD Level 2 Pendataan IISMA dan PMM

Berdasarkan DFD Level 2 untuk proses Pendataan IISMA dan PMM, proses dimulai dari mahasiswa yang memberikan data mahasiswa untuk dilakukan proses 8.1 Melakukan Pendataan (IISMA, PMM). Data mahasiswa yang telah didata akan dilanjutkan ke proses 8.2 Validasi Pendataan (IISMA, PMM). Proses ini bertujuan untuk memastikan kebenaran dan kelengkapan data yang diberikan oleh mahasiswa.

Setelah data tervalidasi, informasi tersebut diteruskan ke proses 8.3 Menyimpan Pendataan (IISMA, PMM). Pada tahap ini, data mahasiswa yang telah tervalidasi disimpan ke dalam basis data "exchange_participants". Penyimpanan data ini menjadi pusat referensi untuk proses-proses selanjutnya.

Beberapa aktor lain seperti Admin, Dosen PIC, Dosen Pembimbing, dan Koordinator Prodi berperan dalam mengakses data mahasiswa yang sudah tersimpan. Mereka berinteraksi dengan sistem melalui proses 8.4 Menampilkan Pendataan (IISMA, PMM), yang mengambil data dari penyimpanan dan menampilkannya sesuai kebutuhan masing-masing pengguna.

**2.2.11 Data Flow Diagram (DFD) Level 2 Memilih Dosen Pembimbing**

<!-- Start of picture text -->
a ot<br>exchange_participants fisaleincaal<br>ahasiswa<br>re data manasiswa data ‘ata manasiswa<br>92<br>Memilih<br>Dosen<br>;<br>embimbing pempmongdata dosen<br>data dosen<br>pempimbing<br>93<br>pivot_pembimbing_exchanges Menyimpan<br>data dosen Dosen<br>pempimbing  'Rembimbing<br>ata dosen /aenampikan—94 data dosen maisiswa<br>Pempimbing ng pempimbing<br><!-- End of picture text -->

Gambar 2.12 DFD Level 2 Memilih Dosen Pembimbing

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Memilih Dosen Pembimbing, proses dimulai dari Admin yang mengakses data mahasiswa yang tersimpan di dalam basis data "exchange_participants" melalui proses 9.1 Menampilkan Data Mahasiswa. Data ini ditampilkan agar admin dapat mengetahui mahasiswa mana saja yang perlu ditentukan dosen pembimbingnya.

Setelah data mahasiswa ditampilkan, proses dilanjutkan ke 9.2 Memilih Dosen Pembimbing, di mana admin menentukan dosen pembimbing yang sesuai untuk masing-masing mahasiswa. Data dosen pembimbing yang dipilih kemudian diteruskan ke proses 9.3 Menyimpan Dosen Pembimbing, di mana data tersebut disimpan ke dalam tabel "pivot_pembimbing_exchanges", yang berfungsi sebagai relasi antara mahasiswa dan dosen pembimbing.

Data dosen pembimbing yang telah tersimpan kemudian dapat diakses oleh mahasiswa melalui proses 9.4 Menampilkan Dosen Pembimbing, yang mengambil informasi dari "pivot_pembimbing_exchanges" dan menampilkan data dosen pembimbing kepada mahasiswa.

# **2.2.12 Data Flow Diagram (DFD) Level 2 Mengelola Jadwal Bimbingan**

<!-- Start of picture text -->
ee 10.1<br>exchange_participants haenampilkan dosen<br>SC ata manasiswar Gata data mahasiswa pembimbing<br>bimbingan lahasiswe bimbingan<br>102<br>Mengelola<br>Bimbingan,Jadwal jadwal bimbingan<br>jadwal bimbingan<br>— 103<br>jadwal_bimbingan_exchanges Menyimpanseen<br>jadwal bimbingan \ Bimbingan,<br>jadwal bimbingan haenampilkanJadwal104 _) —jadwal bimbingan aabianeaaa<br>Bimbingan,<br><!-- End of picture text -->

Gambar 2.13 DFD Level 2 Mengelola Jadwal Bimbingan

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Mengelola Jadwal Bimbingan, alur dimulai dari dosen pembimbing yang mengakses data mahasiswa bimbingan yang berasal dari basis data exchange_participants melalui proses 10.1 Menampilkan Data Mahasiswa. Data ini ditampilkan untuk membantu dosen mengetahui siapa saja mahasiswa yang berada di bawah bimbingannya.

Setelah itu, dosen pembimbing melakukan proses 10.2 Mengelola Jadwal Bimbingan, yaitu menyusun dan mengatur jadwal bimbingan sesuai dengan ketersediaan waktu dosen dan kebutuhan mahasiswa. Jadwal yang telah diatur kemudian dilanjutkan ke proses 10.3 Menyimpan Jadwal Bimbingan, yang akan menyimpan informasi jadwal tersebut ke dalam basis data "jadwal_bimbingan_exchanges".

Selanjutnya, jadwal bimbingan yang sudah tersimpan dapat ditampilkan kembali melalui proses 10.4 Menampilkan Jadwal Bimbingan. Proses ini menyediakan informasi jadwal bimbingan kepada mahasiswa agar mereka dapat mengetahui waktu bimbingan yang telah ditentukan.

# **2.2.13 Data Flow Diagram (DFD) Level 2 Melakukan Bimbingan**

<!-- Start of picture text -->
$$ $$ W414<br>jadwal_bimbingan_exchanges Menampikan'<br>bimbingan / jadwal bimbingan<br>12<br>Bimbingan kehadiran<br>bimbingan<br>kehadiran<br>bimbingan<br>ee, 13<br>kehadiran_bimbingan_exchanges Menyimpan<br>TT bimbingana — \Bimbingan,tae<br><!-- End of picture text -->

Gambar 2.14 DFD Level 2 Melakukan Bimbingan

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Melakukan Bimbingan, alur dimulai dari mahasiswa yang mengakses jadwal bimbingan yang berasal dari basis data "jadwal_bimbingan_exchange" melalui proses 11.1 Menampilkan Jadwal Bimbingan. Data ini ditampilkan untuk membantu mahasiswa maupun dosen dalam melaksanakan bimbingan.

Setiap melakukan bimbingan, mahasiswa wajib mengisi kehadiran bimbingan melalui proses 11.2 Kehadiran Bimbingan. Data kehadiran bimbingan mahasiswa tersebut akan disimpan melalui proses 11.3 Menyimpan Data Bimbingan yang akan disimpan ke dalam basis data "kehadiran_bimbingan_exchange".

# **2.2.14 Data Flow Diagram (DFD) Level 2 Mengelola Laporan Bimbingan**

<!-- Start of picture text -->
—_— 121<br>kehadiran_bimbingan_exchanges Menampilkan dosen<br>kehadiran Arclcal kehadiran pembimbing<br>bimbingan mbinga/_bimbingan<br>122<br>Mengelola<br>laporan<br>bimbingan data bimbingan<br>data bimbingan<br>122<br>Menyimpan<br>data bimbingan bimbingan,laporan<br><!-- End of picture text -->

Gambar 2.15 DFD Level 2 Mengelola Laporan Bimbingan

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Mengelola Laporan Bimbingan, alur dimulai dari dosen pembimbing yang mengakses data kehadiran bimbingan yang berasal dari basis data "kehadiran_bimbingan_exchanges" melalui proses 12.1 Menampilkan Kehadiran Bimbingan. Data ini ditampilkan untuk membantu dosen pembimbing melakukan proses 12.2 Mengelola Laporan Bimbingan, yang nantinya data laporan bimbingan tersebut akan disimpan melalui proses 12.3 Menyimpan Laporan bimbingan yang akan disimpan kembali kedalam data base "kehadiran_bimbingan_exchanges".

# **2.2.15 Data Flow Diagram (DFD) Level 2 Membuat Remark**

<!-- Start of picture text -->
a 13.1<br>kehadiran_bimbingan_exchanges kehadiran pomsarsstel kehadiran dosen pic<br>bimbingan pimbingan bimbingan<br>132<br>MemberikanRemark data remark<br>data remark<br>133<br>Menyimpan<br>data remark Remark<br>data remark MenampilkanRemark.)13.4 data remark pembimbingoe<br><!-- End of picture text -->

Gambar 2.16 DFD Level 2 Membuat _Remark_

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Membuat _Remark_ , alur dimulai dari dosen PIC yang mengakses data kehadiran bimbingan mahasiswa yang telah tersimpan di dalam basis data “kehadiran_bimbingan_exchanges”. Data ini ditampilkan melalui proses 13.1 Menampilkan Kehadiran Bimbingan, yang bertujuan untuk memberikan informasi kepada dosen PIC mengenai aktivitas bimbingan mahasiswa.

Setelah meninjau data kehadiran, dosen PIC dapat memberikan catatan atau tanggapan melalui proses 13.2 Memberikan _Remark_ , di mana _remark_ (tanggapan atau evaluasi) dibuat berdasarkan data kehadiran yang telah dilihat. _Remark_ tersebut kemudian dikirimkan ke proses 13.3 Menyimpan _Remark_ untuk disimpan ke dalam sistem.

_Remark_ yang telah tersimpan akan masuk ke dalam database, dan selanjutnya dapat diakses kembali melalui proses 13.4 Menampilkan _Remark,_ yang menyajikan data _remark_ tersebut kepada dosen pembimbing untuk menjadi bahan evaluasi atau tindak lanjut dalam proses bimbingan.

Proses ini memastikan bahwa kehadiran mahasiswa dalam bimbingan dipantau secara aktif dan diberikan evaluasi secara tertulis oleh dosen PIC, serta remark tersebut dapat dimanfaatkan oleh dosen pembimbing untuk mendukung kelancaran dan efektivitas proses pembimbingan.

# **2.2.16 Data Flow Diagram (DFD) Level 2 Mengupload Laporan Kegiatan**

<!-- Start of picture text -->
laporan kegiatan 14.1<br>Upload<br>vata<br>Kegiatan<br>laporan kegiatan<br>142<br>Validasi<br>Laporan<br>Kegiatan<br>laporan kegiatan<br>143 po<br>Menyimpan final_report_exchanges<br>Laporan laporan kegiatan =hae 2<br>Kegiatan TT<br><!-- End of picture text -->

Gambar 2.17 DFD Level 2 Laporan Kegiatan

Berdasarkan Data Flow Diagram (DFD) Level 2 untuk proses Mengupload Laporan Kegiatan, alur dimulai dari mahasiswa yang mengunggah laporan kegiatan melalui proses 14.1 Upload Laporan Kegiatan. Proses ini bertujuan untuk mengumpulkan laporan hasil kegiatan mahasiswa selama mengikuti program pertukaran.

Setelah laporan diunggah, sistem akan melanjutkan ke proses 14.2 Validasi Laporan Kegiatan. Validasi ini dilakukan untuk memastikan bahwa laporan yang diunggah oleh mahasiswa telah memenuhi ketentuan yang berlaku, baik dari segi format, isi, maupun kelengkapan data.

Laporan yang telah divalidasi kemudian dikirim ke proses 14.3 Menyimpan Laporan Kegiatan, di mana laporan tersebut disimpan secara permanen ke dalam basis data "final_report_exchanges". Basis data ini menjadi arsip resmi laporan kegiatan mahasiswa yang mengikuti program _student exchange_ .

**2.2.17 Data Flow Diagram (DFD) Level 2 Verifikasi Laporan Kegiatan**

<!-- Start of picture text -->
15.1<br>laporan kegiatan MenampilkanLaporan Taporan kegiatan pembimbingdosen<br>Kegiatan<br>15.2<br>Verifikasi laporan kegiatan<br>Laporan<br>final_report_exchanges Kegiatan<br>hasil verifikasi<br>153<br>Menyimpan<br>hasil verifikasi Laporan<br>Kegiatan<br>154<br>Menampilkanrat<br>hasil verifikasi Verifikasi hasil verifikasi<br><!-- End of picture text -->

Gambar 2.18 DFD Level 2 Verifikasi Laporan Kegiatan

Proses Verifikasi Laporan Kegiatan diawali dengan pengambilan data laporan kegiatan yang telah disimpan dalam basis data "final_report_exchanges". Laporan kegiatan tersebut ditampilkan melalui proses 15.1 Menampilkan Laporan Kegiatan untuk dapat diakses oleh dosen pembimbing, yang bertugas melakukan verifikasi terhadap isi laporan.

Selanjutnya, dosen pembimbing melakukan proses 15.2 Verifikasi Laporan Kegiatan untuk mengevaluasi apakah laporan yang diajukan oleh mahasiswa telah sesuai dengan ketentuan akademik dan administratif. Hasil dari verifikasi ini akan diteruskan ke proses 15.3 Menyimpan Laporan Kegiatan, yang menyimpan data hasil verifikasi ke dalam sistem.

Data hasil verifikasi yang telah disimpan kemudian dapat diakses kembali melalui proses 15.4 Menampilkan Hasil Verifikasi, yang menyediakan informasi hasil penilaian laporan kegiatan kepada pihak Koordinator Prodi sebagai bagian dari proses monitoring dan validasi akhir.

# **2.2.18 Data Flow Diagram (DFD) Level 2 Konversi SKS**

<!-- Start of picture text -->
fenampilkai<br>Hasil<br>hasil verifikasi Laporan— hasil verifikasi<br>laporan kegiatan egia laporan kegiatan<br>162 Approve Konversi<br>Approve as<br>conversi SK‘<br>final_report_exchanges<br>Approve Konversi<br>SKS<br>163<br>Menyimpan<br>Approve<br>Approve Konversi konversi<br>SKS SKS<br><!-- End of picture text -->

Gambar 2.19 DFD Level 2 Konversi SKS

Proses Konversi SKS dimulai dengan Koordinator Prodi yang mengakses data hasil verifikasi laporan kegiatan melalui proses 16.1 Menampilkan Hasil Verifikasi Laporan Kegiatan. Data ini berasal dari _database_ “final_report_exchanges” dan menjadi dasar pertimbangan untuk konversi SKS mahasiswa.

Setelah hasil verifikasi ditampilkan, Koordinator Prodi melakukan proses 16.2 _Approve_ Konversi SKS. Dalam tahap ini, Koordinator Prodi menilai apakah kegiatan mahasiswa selama program pertukaran dapat dikonversikan ke dalam bentuk SKS sesuai kebijakan akademik yang berlaku.

Apabila disetujui, data hasil approval konversi SKS tersebut akan diteruskan ke proses 16.3 Menyimpan Approve Konversi SKS, yang akan menyimpan hasil persetujuan konversi ke dalam sistem untuk keperluan dokumentasi dan pelaporan lebih lanjut.

# **2.2.19 Data Flow Diagram (DFD) Level 2 Verifikasi Bukti Pelaksanaan**

<!-- Start of picture text -->
17.4<br>Menampilkan Hasil<br>onBukti VerifikasiPelaksanaanBukti aS BuktiVETMIKAST<br>Pelaksanaan Pelaksanaan<br>172 Approve Bukti<br>Approve Bukti Pelaksanaan<br>Pelaksanaan<br>final_report_exchanges<br>Approve Bukti<br>Pelaksanaan<br>173<br>Menyimpan<br>Approve Bukti Approve Bukti<br>Pelaksanaan Pelaksanaan<br><!-- End of picture text -->

Gambar 2.20 DFD Level 2 Verifikasi Bukti Pelaksanaan

Proses Verifikasi Bukti Pelaksanaan dimulai ketika Koordinator Prodi mengakses hasil verifikasi bukti pelaksanaan melalui proses 17.1 Menampilkan Hasil Verifikasi Bukti Pelaksanaan. Data ini ditarik dari basis data “final_report_exchanges” dan ditampilkan agar Koordinator Prodi dapat meninjau kesesuaian bukti pelaksanaan kegiatan yang dilaporkan mahasiswa.

Setelah meninjau bukti tersebut, Koordinator Prodi melanjutkan dengan proses 17.2 _Approve_ Bukti Pelaksanaan untuk memberikan persetujuan atau validasi terhadap bukti yang telah dikumpulkan. Tahap ini penting untuk memastikan bahwa kegiatan benar-benar dilaksanakan sesuai dengan ketentuan program (seperti IISMA atau PMM).

Persetujuan tersebut kemudian diproses pada tahap 17.3 Menyimpan _Approve_ Bukti Pelaksanaan, yang bertugas menyimpan hasil persetujuan dari Koordinator Prodi ke dalam sistem. Data persetujuan ini juga diperbarui dalam _database “_ final_report_exchanges” sebagai bagian dari rekam jejak resmi pelaksanaan kegiatan mahasiswa.

# **2.2.20 Data Flow Diagram (DFD) Level 2 Mengelola Mahasiswa Inbound**

<!-- Start of picture text -->
18.1<br>Mahasiswa<br>mahasiswa Mengelola<br>inbound Inbound<br>mahasiswa<br>inbound<br>— 18.2<br>eeexchange_participants mahasiswa MenyimpanhiahaciewalInbound<br>inbound<br><!-- End of picture text -->

Gambar 2.21 DFD Level 2 Mengelola Mahasiswa _Inbound_

Data Flow Diagram (DFD) Level 2 Mengelola Mahasiswa _Inbound_ menggambarkan proses pengelolaan data mahasiswa yang mengikuti program pertukaran dari luar perguruan tinggi (mahasiswa _inbound_ ). Proses ini diawali oleh admin yang bertugas untuk memasukkan atau memperbarui data mahasiswa _inbound_ ke dalam sistem melalui proses 18.1 Mengelola Mahasiswa _Inbound_ . Data yang dikelola mencakup informasi pribadi dan akademik mahasiswa _inbound_ . Selanjutnya, data tersebut dikirimkan ke proses 18.2 Menyimpan Mahasiswa Inbound untuk disimpan ke dalam basis data “exchange_participants”. Penyimpanan ini bertujuan agar data mahasiswa _inbound_ dapat digunakan untuk keperluan administrasi, pelaporan, serta pemantauan aktivitas akademik mereka selama mengikuti program _student exchange_ di Fakultas Ilmu Komputer UPN “Veteran” Jakarta.

# **2.3 Rancangan Proyek (UI dan UX)**

Pada tahapan ini akan menjelaskan bagaimana kebutuhan analisis dari tampilan antarmuka yang akan diusulkan beserta dengan fungsionalitasnya. Penjelasan terkait kebutuhan dan tampilan tersebut akan dijelaskan pada penjelasan berikut ini.

# **2.3.1 Need Analysis User Interface dan User Experience**

Pada bagian need analysis ini, penulis menjelaskan bagaimana kebutuhan pengguna terkait pengalaman dan antarmuka pengguna yang dirancang berdasarkan komponen _User Experience_ (UX), tujuan UX, kebutuhan pengguna, dan desain pengalaman yang diusulkan dalam bentuk tabel berikut:

|**Komponen**<br>**_User_**|**Tujuan****_User_**<br>**_Experience_**|**Kebutuhan**<br>**Pengguna**|**Design Pengalaman**<br>**yang Dibutuhkan**|
|---|---|---|---|
|**_Experience_**||||
|**_Usability_**|Memastikan<br>sistem mudah<br>digunakan<br>oleh semua<br>pengguna|-<br>Navigasi<br>yang intuitif<br>-<br>Panduan<br>penggunaan<br>yang jelas<br>-<br>Design yang<br>responsif|-<br>Antarmuka<br>yang<br>sederhana dan<br>udah<br>digunakan<br>oleh pengguna<br>-<br>Menu navigasi<br>yang<br>tersturktur<br>-<br>Adanya buku<br>panduan untuk<br>bantuan para<br>pengguna|
|**_Functionality_**|Menyediakan<br>fitur yang<br>relevan untuk|-<br>Formulir<br>pendaftaran<br>berbasis|-<br>Sistem<br>menyediakan<br>antarmuka|
||proses|online|sederhana|
||pendaftaran|-<br>Informasi|dengan|
||dan|yang|formulir|
||manajemen|disajikan|pendaftaran|
|||mengenai|berbasis web.|

||student<br>exchange|-|program<br>lengkap dan<br>terkini<br>Semua<br>proses dari<br>awal hingga<br>pengumpulan<br>laporan<br>terfasilitasi|-<br>-|Sistem dapat<br>mengelola<br>informasi<br>secara terkini<br>dan lengkap<br>Sistem<br>menampilkan<br>tahapan proses<br>awal hingga<br>akhir secara<br>visual|
|---|---|---|---|---|---|
|**_Reliability_**|Menjamin<br>sistem bekerja<br>dengan baik<br>dan minim|-<br>-|Sistem yang<br>stabil<br>Semua<br>terproses|-<br>-|Infrastruktur<br>server yang<br>andal<br>Proses|
||gangguan||tanpa ada<br>kesalahan||validasi data<br>otomatis|
|||-|Penyimpanan|-|Pencadangan|
||||data yang<br>aman||data berkala|
|**_Engagement_**|Meningkatkan<br>minat|-|Tampilan<br>yang|-|Design visual<br>dengan|
||pengguna||menarik dan||elemen|
||untuk||professional||interaktif|
||menggunakan|-|Interaksi|-|Konten visual|
||sistem secara||yang||seperti|
||aktif||interaktif||testimonia tau|
|||-|Pemberian||galeri|
||||informasi<br>terkini||pengalaman<br>alumni|

|**_Personali-_**|Memberikan|-<br>Rekomendasi|-|Adanya fitur|
|---|---|---|---|---|
|**_zation_**|pengalaman<br>yang sesuai<br>dengan<br>preferensi<br>masing-<br>masing<br>pengguna|program<br>berdasarkan<br>minat dan<br>kebutuhan||filter untuk<br>memudahkan<br>para pengguna<br>dalam mencari<br>program<br>maupun<br>informasi<br>secara cepat|
|**_Security_**|Melindungi<br>data pengguna<br>dari resiko<br>keamanan|-<br>Privasi data<br>pribadi<br>-<br>Sistem<br>autentikasi<br>yang aman|-|Implementasi<br>sistem login<br>dengan<br>menginput<br>_username_dan<br>_password_para<br>pengguna<br>berdasarkan<br>API yang<br>tersedia|
||Tabel 2|.3 Anlysis UI UX|||

Berdasarkan tabel 2.3 di atas menggambarkan pentingnya perancangan sistem informasi Student Exchange yang berorientasi pada pengalaman pengguna (User Experience). Sistem ini dirancang dengan mempertimbangkan enam komponen utama UX, yaitu **_Usability, Functionality, Reliability, Engagement, Personalization,_** dan **_Security_ ,** yang masing-masing memiliki peran penting dalam menciptakan pengalaman yang optimal bagi pengguna.

Dari segi **_Usability_ ,** sistem dirancang agar mudah digunakan oleh semua pengguna, termasuk mahasiswa, dosen, dan staf administrasi. Untuk mencapai hal ini, navigasi yang intuitif menjadi salah satu prioritas, di mana setiap menu dan fitur diatur secara terstruktur untuk meminimalkan kebingungan. Selain itu, desain

responsif memastikan bahwa sistem dapat diakses dengan nyaman di berbagai perangkat, baik desktop maupun seluler. Adanya buku panduan atau fitur bantuan interaktif juga dirancang untuk mendukung pengguna yang mungkin mengalami kesulitan dalam mengoperasikan sistem.

Komponen **_Functionality_** menekankan pada penyediaan fitur yang relevan dengan kebutuhan pengguna. Sistem ini menyediakan formulir pendaftaran berbasis online yang dirancang dengan antarmuka yang sederhana, sehingga memudahkan proses pendaftaran. Selain itu, informasi program disajikan secara lengkap dan selalu diperbarui agar pengguna dapat mengakses data yang terkini, seperti syarat pendaftaran, jadwal kegiatan, dan detail program. Untuk mempermudah pengguna dalam memahami alur proses, sistem juga menampilkan tahapan kegiatan mulai dari pendaftaran hingga pengumpulan laporan akhir dalam bentuk visual yang mudah dipahami.

Keandalan sistem atau **_Reliability_** menjadi salah satu prioritas utama untuk menjamin sistem bekerja dengan baik dan minim gangguan. Sistem ini didukung oleh infrastruktur server yang andal, yang memastikan stabilitas operasional meskipun digunakan oleh banyak pengguna secara bersamaan. Selain itu, validasi data otomatis membantu mengurangi risiko kesalahan selama proses pengisian formulir atau pengunggahan dokumen. Pencadangan data secara berkala juga dilakukan untuk menjaga keamanan data pengguna dari kehilangan atau kerusakan.

Pada aspek **_Engagement,_** sistem dirancang untuk menarik minat pengguna agar lebih aktif menggunakannya. Tampilan yang menarik dan profesional menjadi salah satu elemen utama, didukung oleh desain visual yang interaktif. Selain itu, konten visual seperti galeri pengalaman alumni atau testimoni dari peserta program sebelumnya disediakan untuk memberikan gambaran yang inspiratif kepada pengguna baru. Informasi yang selalu diperbarui juga memastikan bahwa pengguna tetap terhubung dengan perkembangan terbaru.

Komponen **_Personalization_** bertujuan untuk memberikan pengalaman yang sesuai dengan preferensi individu pengguna. Fitur filter pencarian, misalnya, memudahkan pengguna dalam menemukan program yang sesuai dengan minat atau kebutuhan mereka, seperti lokasi, bidang studi, atau durasi kegiatan. Dengan

memberikan pengalaman yang lebih personal, sistem dapat meningkatkan efisiensi dan kepuasan pengguna dalam mengakses informasi.

Terakhir, aspek **_Security_** sangat penting untuk melindungi data pribadi pengguna. Sistem ini menggunakan autentikasi yang aman dengan login berbasis _username_ dan _password_ yang terintegrasi dengan API, sehingga data pengguna tetap terlindungi dari risiko kebocoran atau penyalahgunaan. Dengan pendekatan ini, sistem memberikan rasa aman kepada pengguna dalam berinteraksi dengan platform.

Secara keseluruhan, sistem informasi Student Exchange ini dirancang untuk memenuhi kebutuhan pengguna secara holistik dengan memastikan kemudahan penggunaan, fungsionalitas yang relevan, keandalan yang tinggi, pengalaman yang menarik, personalisasi yang sesuai, dan keamanan data yang terjamin. Implementasi sistem ini diharapkan tidak hanya mempermudah proses administrasi dan manajemen program, tetapi juga meningkatkan kepuasan dan kepercayaan pengguna.

# **2.3.2 Design User Interface**

Pada bagian ini akan menampilkan dan menjelaskan terkait dengan tampilan antarmuka yang dirancang dengan tujuan untuk memberikan gambaran terkait rancangan user interface yang diusulkan. Rancangan ini dibuat berdasarkan need analysis pada user interface dan user experience yang telah dijelaskan sebelumnya. Rancangan untuk tampilan design user interface dapat dilihat pada gambar berikut.

# **2.3.2.1 Halaman Landing Page**

<!-- Start of picture text -->
fo) @ becprentees Owens 64 eect entenge em<br>landing Page<br>in ia"<br><!-- End of picture text -->

Gambar 2.22 Halaman _Landing Page_

Pada halaman _landing page_ , seluruh user dapat melakukan klik login untuk masuk ke halaman login. _User_ juga dapat melihat semua informasi seputar MBKM, Manajemen Talenta, dan _Student Exchange_ . _User_ dapat menggunakan _filter search_ untuk mempermudah dalam mencari informasi yang dibutuhkan.

# **2.3.2.2 Halaman Login**

Gambar 2.23 Halaman Login

Pada halaman login, _user_ dapat memasukkan _username_ dan _password_ -Nya yang telah terdaftar. Apabila _user_ salah memasukkan _username_ atau _password_ , maka akan muncul pesan _error._ Proses login ini bertujuan untuk memberikan hak akses kepada pengguna sistem yang telah terdaftar untuk menjaga keamanan data

pada sistem.

# **2.3.2.3 Halaman Dashboard General**

<!-- Start of picture text -->
an<br>= eSus oSnora<br>Zs<br>——<br>noe ee<br><!-- End of picture text -->

Gambar 2.24 Halaman _Dashboard General_

Setelah _user_ berhasil melakukan login, maka akan masuk ke halaman _dashboard general_ . Pada tampilan _dashboard general_ terdapat tiga pilihan menu, yaitu MBKM, _Student Exchange_ , dan Manajemen Talenta. Apabila _user_ ingin masuk ke halaman program _student exchange_ , maka _user_ dapat mengklik menu _student exchange_ dan masuk ke halaman _dashboard_ program _student exchange_ . Halaman _dashboard general_ ini dapat diakses oleh aktor mahasiswa, admin, Koordinator Prodi, dosen PIC program, dan dosen pembimbing.

# **2.3.2.4 Halaman Dashboard Student Exchange Mahasiswa**

<!-- Start of picture text -->
Se a a a<br>2 Uptoad kegiatan @<br><!-- End of picture text -->

Gambar 2.25 Halaman _Dashboard Student Exchange_

Halaman _dashboard student exchange_ , mahasiswa dapat melihat daftar program yang tersedia, seperti IISMA, PMM, dan Kerja sama. Mahasiswa juga

dapat melihat statistik dari program _exchange_ pada bagian yang menampilkan jumlah total program _exchange_ yang tersedia.

# **2.3.2.5 Halaman Profil Mahasiswa**

<!-- Start of picture text -->
$) cvrwenncs<br>—_— semis setae nr<br>— teeth tne<br>|= Progam tactonae omen<br>1 surttomendon com<br>2 emeingen<br>poset ere<br>— ono<br>© ge va<br>come o<br><!-- End of picture text -->

Gambar 2.26 Halaman Profil Mahasiswa

Pada halaman profil, mahasiswa dapat melihat informasi indentitas-Nya, seperti Nama, NIM, Program Studi, Email, dan Nomor Telepon yang sudah ditampilkan otomatis dari sistem. Mahasiswa juga dapat melihat progress kegiatanNya pada tampilan _progress bar_ untuk mempermudah mahasiswa mengetahui mereka sudah berapa tahap dalam proses rangkain _student exchange_ yang terdiri dari tahapan pengajuan surat rekomendasi, penerimaan, bimbingan, membuat laporan bulanan, membuat laporan akhir, dan tahap penilaian.

# **2.3.2.6 Halaman Informasi Program Exchange**

<!-- Start of picture text -->
= —<br><— pn<br>_<br>=<br>= QW |PAIMIBKIDGE<br><!-- End of picture text -->

Gambar 2.27 Halaman Informasi Program _Exchange_

Pada halaman program _exchange,_ mahasiswa dapat melihat semua informasi seputar program _exchange_ yang tersedia. Mahasiswa dapat menggunakan menu filter dan _search_ untuk mempermudah mahasiswa dalam mencari informasi yang dibutuhkan. Pada filter terdapat pilihan filter kategori program, sehingga mempermudah mahasiswa untuk melihat informasi program sesuai dengan kategori program yang ingin mereka ikuti. Informasi yang akan ditampilkan pada halaman ini sudah berdasarkan program studi mahasiswa. Pada halaman ini, terdapat informasi tanggal mulai pendaftaran program dan tanggal batas akhir pendaftaran. Untuk melihat _detail_ dari setiap informasi, mahasiswa dapat klik “Lihat _Detail_ ” dan akan masuk ke halaman _detail_ dari informasi program tersebut.

# **2.3.2.7 Halaman Detail Informasi Program Exchange**

Gambar 2.28 Halaman Detail Informasi Program _Exchange_

Halaman detail program memuat informasi lengkap dari program tersebut. Lalu, terdapat informasi kebutuhan syarat yang harus dipersipakan oleh mahasiswa sebelum mendaftar pada program tersebut. Apabila mahasiswa ingin melakukan pendaftaran pada program tersebut, mahasiswa dapat mengklik _button_ “Daftar Sekarang” atau _button_ “Daftar di platform Kampus Merdeka” untuk mahasiswa yang ingin mendaftar program IISMA dan PMM.

# **2.3.2.8 Halaman Belum Mengajukan Surat Rekomendasi**

<!-- Start of picture text -->
ED easeen Surat Rekomendasi<br>suntan so atomendon utarmendotrprgram hermsmaton<br>kom mon dengan aman<br> osttoort va naw ‘aja verte<br>2 Prot<br>1 rogram bxonge (3)<br>BKelengtapan Dotumen mu bolum mengouttonsot retomendosh<br>storeFendtoon Perdatoron Lengtap! dotmu vt mengajttonsactretomends! J vcnca<br>1 |<br>1 aimingon<br><!-- End of picture text -->

Gambar 2.29 Halaman Belum Mengajukan Surat Rekomendasi

Pada halaman surat rekomendasi, mahasiswa dapat megajukan surat rekomendasi sesuai dengan kategori program yang ingin diikuti. Apabila mahasiswa belum pernah mengajukkan, maka akan muncul tampilan “Kamu belum pernah mengajukan surat rekomendasi” dan mahaiswa bisa mengklik _button_ “Lengkapi Data” untuk masuk ke halaman _input_ data yang dibuthkan sesuai dengan program yang ingin diikuti. Mahasiswa hanya dapat mengajukkan surat rekomendasi satu kali dan hanya dapat mengikuti satu program _exchange_ saja.

# **2.3.2.9 Halaman Ingin Mengajukan Surat Rekomendasi**

# **2.3.2.9.1 Halaman Pengajuan Surat Rekomendasi Program IISMA**

<!-- Start of picture text -->
‘Surat Rekomendasi lISMA,<br><<“<br>—<br>rena<br>tl(a)<br>1 setegtapon ote resspor (wei)<br>sm renoon suratatranganteat (naps)<br>sit ersesian (wa)<br><!-- End of picture text -->

Gambar 2.30 Halaman Pengajuan Surat Rekomendasi Program IISMA

Pada halaman pengajuan surat rekomendasi IISMA, mahasiswa dapat melakukan _upload_ untuk memenuhi persyaratan data yang dibutuhkan. Data yang dibutuhkan dalam program IISMA yaitu KTP, Transkip Nilai, Passport, Surat Keterangan Sehat, dan Surat Persetujuan. Untuk mendapat _template_ surat persetujuan, mahasiswa dapat melakukan _download_ pada bagian “Disini”. Setelah mengisi semua dokumen yang dibutuhkan, mahasiswa dapat klik “Ajukan surat rekomendasi” dan data pengajuan tersbeut akan tersimpan pada sistem.

# **2.3.2.9.2 Halaman Pengajuan Surat Rekomendasi Program PMM**

<!-- Start of picture text -->
eresaieene Surat Rekomendasi PMM<br>Lengkopl dokumenmu untuk mengalukan sure rekomendas.nfrmasimu akon kam simpan dengan oman<br>& boshboars (wows)<br>wei: \Unggah KTP kam dalom format POF dengan wun maimed 2M<br>| Program fxchonge ‘TronstipLnggah transbipnilatMill (Wojio)kama dolom format POF dengan ukuran maksima 2 MB<br>BB Ketongkapen Dokuren ‘SurotKeterangan<br>Sehat (Wojib)<br>Oe \Unggan fe kom dalam format POF dengan ukuran mekaimal2 MB<br>1m Pendotoon<br>er surat Persetujuon (Wojs)<br>Download format surat persetujuanOsi<br>tan oneeh<br><!-- End of picture text -->

Gambar 2.31 Halaman Pengajuan Surat Rekomendasi Program PMM

Pada halaman pengajuan surat rekomendasi PMM, mahasiswa dapat melakukan _upload_ untuk memenuhi persyaratan data yang dibutuhkan. Data yang dibutuhkan dalam program PMM yaitu KTP, Transkip Nilai, Surat Keterangan Sehat, dan Surat Persetujuan. Untuk mendapat _template_ surat persetujuan, mahasiswa dapat melakukan _download_ pada bagian “Disini”. Setelah mengisi semua dokumen yang dibutuhkan, mahasiswa dapat klik “Ajukan surat rekomendasi” dan data pengajuan tersbeut akan tersimpan pada sistem.

# **2.3.2.9.3 Halaman Pengajuan Surat Rekomendasi Kerja Sama**

<!-- Start of picture text -->
a<br>CORTE Surat Rekomendasi Kerja Sama Universitas<br>oc: commen unk mengojton ssc eked intros onto sinpan dengan mon<br>2 ma<br>pel)<br>B  Kelengkapan Dokumen ‘Passport (Was)<br>of caste<br>rose sectsrangin<br>st wo)<br>2 opectingnn seston (wa)<br><!-- End of picture text -->

Gambar 2.32 Halaman Pengajuan Surat Rekomendasi Program Kerja Sama

Pada halaman pengajuan surat rekomendasi Kerja Sama Universitas, mahasiswa dapat melakukan _upload_ untuk memenuhi persyaratan data yang dibutuhkan. Data yang dibutuhkan dalam program Kerja Sama Universitas yaitu KTP, Transkip Nilai, Passport, Surat Keterangan Sehat, dan Surat Persetujuan. Untuk mendapat _template_ surat persetujuan, mahasiswa dapat melakukan _download_ pada bagian “Disini”. Setelah mengisi semua dokumen yang dibutuhkan, mahasiswa dapat klik “Ajukan surat rekomendasi” dan data pengajuan tersbeut akan tersimpan pada sistem.

# **2.3.2.10 Halaman Surat Rekomendasi Diproses**

<!-- Start of picture text -->
Ocean = Surat Rekomendasi<br>natn nc etorendo remana rogram HNematimchantam sean dangan amon<br>2 rt<br>= rogembctonge Le]~<br>1 taanghopon turn<br>st Pendtoren engejnoemandotir sedans prone!<br>1 sintngen ‘ecorenonrn nosongSeronee Monon MOOV<br>2 poostageton<br>© tego<br><!-- End of picture text -->

Gambar 2.33 Halaman Surat Rekomendasi Diproses

Halaman ini menapilkan informasi status dari surat rekomendasi mahasiswa yang telah diajukkan oleh mahasiswa masih dalam proses.

# **2.3.2.11 Halaman Berhasil Mendapatkan Surat Rekomendasi**

<!-- Start of picture text -->
Oeeesereens = Surat Rekomendasi<br>symon st oreraoe trangia nlaaem onto! mean srgoneran<br>2 reat<br>1 siningon “euntanseremooto proton srt change! ==)<br>2 Upeodtagton [Srna monsoopn rn penguomen a pam Stet erage yngbar<br><!-- End of picture text -->

Gambar 2.34 Halaman Berhasil Mendapatkan Surat Rekomendasi

Halaman ini akan menampilkan informasi surat rekomendasi yang telah diberikan untuk mahasiswa. Jika sudah berhasil mendapatkan surat rekomendasi, mahasiswa mahasiswa dapat mengklik _button_ “Telusuri Program” untuk melihat informasi program _exchange_ yang tersedia dan dapat melakukan pendaftaran pada menu tersebut.

# **2.3.2.12 Halaman Mengisi Kelengkapan Dokumen Kerja Sama**

<!-- Start of picture text -->
_ Bree reng mein ropa cane waeetnn rang at rp angen ar<br>—— °<br>a =<br>ae °<br>Bess :<br>|<br>—— =<br><!-- End of picture text -->

Gambar 2.35 Halaman Mengisi Kelengkapan Dokumen

Halaman kelengkapan dokumen ini muncul apabila mahasiswa ingin mengikuti program _exchange_ kerja sama universitas. Mahasiswa dapat mengisi data-data yang dibutuhkan. Untuk data KTP, Transkip Nilai, Passport, dan Surat Persetujuan akan muncul secara otomatis karena sudah tersimpan oleh sistem saat mahasiswa mengajukan surat rekomendasi pada program _exchange_ kerja sama universitas. Kemudian, mahasiswa hanya mengisi dokumen seperti CV dan dokumen tambahan untuk mengisi kelengkapan dokumen. Apabila semua data sudah terisi, maka mahasiswa dapat mengklik _button_ “Submit” dan data kelengkapan dokumen ini akan tersimpan pada sistem.

# **2.3.2.13 Halaman Berhasil Melakukan Pendaftaran Kerja Sama**

<!-- Start of picture text -->
Bernasit<br><!-- End of picture text -->

Gambar 2.36 Halaman Berhasil Melakukan Pendaftaran

Pada halaman pendaftaran program kerja sama universitas, mahasiswa dapat melakukan pendaftaran pada sistem dengan mengklik _button_ “Daftar Sekarang” dan akan muncul _pop up_ berhasil. Apabila telah berhasil mendaftar, mahasiswa dapat men _download_ bukti pendaftaran dengan mengklik _button_ “Lihat bukti pendaftaran”. Untuk mahasiswa yang mengikuti program IISMA dan PMM, mahasiswa dapat melakukan pendaftaran di luar sistem ini, yaitu pada _website_ Kampus Merdeka.

# **2.3.2.14 Halaman Melihat Status Pendaftaran Program Kerja Sama**

<!-- Start of picture text -->
S))pereervene Status Pendaftaran<br>Damon<br>i rss tye<br>2 ropamucterae<br>1 Swoteetomendon<br>1B. telengrgpantotum<br>1. sibingon<br>2 Upoadkogitan<br>© toga<br><!-- End of picture text -->

Gambar 2.37 Halaman Melihat Status Pendaftaran

Halaman status pendaftaran ini memuat informasi status pendaftaran mahasiswa. Untuk mempermudah mahasiswa dalam melihat status pendaftaranNya, mahasiswa dapat melakukan _search_ untuk mempermudah menemukan status pendaftaran pada setiap universitas yang mereka daftar pada program kerja sama universitas. Untuk melihat _detail_ dari status pendaftaran, mahasiswa dapat mengklik _card_ informasi, lalu akan muncul tampilan _detail_ status pendaftaran.

# **2.3.2.15 Halaman Melakukan Pendataan Untuk Program PMM dan IISMA**

<!-- Start of picture text -->
Pendataan<br>————_ EE<br>oan vow<br>am Program Sut<br>AB Program Exchange eee<br>1 settee<br>:<br>‘eae<br>2 sng rey -<br>Upload Kegiton Fregeneschenge<br>: mine<br><!-- End of picture text -->

Gambar 2.38 Halaman Melakukan Pendataan (IISMA dan PMM)

Pada halaman pendataan, mahasiswa yang telah dinyatakan lolos program IISMA dan PMM pada _website_ Kampus Merdeka harus mengisi data-data yang dibutuhkan pada halaman ini, seperti Tanggal Lahir, Jenis Program _Exchange_ , Diterima di Universitas, dan Meng _upload_ Bukti Penerimaan. Setelah semua data yang dibutuhkan terisi, mahasiswa dapat mengklik _button_ “Submit” dan data mahasiswa yang lolos program IISMA atau PMM ini akan tersimpan pada sistem.

# **2.3.2.16 Halaman Bimbingan**

<!-- Start of picture text -->
OlReesarvag = Bimbingan<br>———_ ‘emuEtsmace nin nine gon een ne whan dou nig ounWi at gn ie en<br>— Kc sonata<br>0 masse<br>troponin on =<br>bs sent<br>— ae<br>—_—eee<br>— eee<br>tag  ——— =o<br>© tat<br><!-- End of picture text -->

Gambar 2.39 Halaman Bimbingan

Pada halaman bimbingan ini, mahasiswa dapat melihat informasi nama dosen pembimbing-Nya dan informasi jadwal bimbingan, seperti tanggal bimbingan, waktu bimbingan, dan lokasi bimbingan. Mahasiswa dapat mengklik _button_ “Lihat Detail” untuk melihat informasi _detail_ dari jadwal bimbingan.

# **2.3.2.17 Halaman Detail Bimbingan**

<!-- Start of picture text -->
=<br><!-- End of picture text -->

Gambar 2.40 Halaman Detail Bimbingan

Halaman _detail_ bimbingan ini memberikan informasi lengkap dari jadwal bimbingan mahasiswa. Lalu, mahaiswa dapat mengisi kehadiran dengan melakukan _upload_ bukti kehadiran dan mengisi kendala yang dihadapi. Setalah itu, mahasiswa dapat mengklik _button_ “Simpan” dan data kehadiran tersebut akan tersimpan oleh sistem.

# **2.3.2.18 Halaman** **_Upload_ Kegiatan**

# **2.3.2.18.1 Halaman Mengisi Logbook Harian**

<!-- Start of picture text -->
Ea<br><!-- End of picture text -->

Gambar 2.41 Halaman Mengisi Logbook Harian

Pada halaman _upload_ logbook harian, terdiri dari tanggal _upload_ logbook harian, deskripsi aktivitas mahasiswa, dan kendala yang dihadapi mahasiswa saat mengikuti kegiatan. Mahasiswa dapat mengisi logbook harian sebagai syarat konversi. Apabila sudah diisi, mahasiswa dapat mengklik _button_ “Simpan” dan data tersebut akan tersimpan pada sistem.

# **2.3.2.18.2 Halaman** **_Upload_ Laporan Akhir**

<!-- Start of picture text -->
iene Upload Kegiatan Kerjasama Universitas<br>1 rogremtachonge<br>1 sect eeemenson<br>1 comnnapo oon<br>Sex tendenocn<br>© toga<br><!-- End of picture text -->

Gambar 2.42 Halaman _Upload_ Laporan Akhir

Pada halaman _upload_ laporan akhir, mahasiswa dapat meng- _upload_ laporan akhir-Nya sebagai syarat konversi. Apabila sudah _upload_ , mahasiswa dapat mengklik _button_ “Simpan” dan data tersebut akan tersimpan pada sistem.

# **2.3.2.18.3 Halaman** **_Upload_ Transkrip Nilai**

<!-- Start of picture text -->
Giessen Upload Kegiatan Kerjasama Universitas<br>_2 rt oad TorampisterWbegl ae uta<br>2 regent<br>1B sretntorenden =o<br>1 ccrstopon cohen<br>1 SenurFensohrn<br><!-- End of picture text -->

Gambar 2. 43 Halaman _Upload_ Transkrip Nilai

Pada halaman _upload_ transkrip nilai, mahasiswa dapat meng- _upload_ transkrip nilai-Nya sebagai syarat konversi. Apabila sudah _upload_ , mahasiswa dapat mengklik _button_ “Simpan” dan data tersebut akan tersimpan pada sistem.

# **2.3.2.19 Halaman** **_Dashboard_ Admin**

Gambar 2.44 Halaman _Dashboard_ Admin

Halaman _dashboard_ admin menampilkan grafik dari keikutsertaan mahasiswa dalam program _exchange_ , seperti tampilan grafik pada program _exchange_ kerja sama universitas, IISMA, dan PMM. Pada grafik tersebut terlihat jumlah pendaftar dan jumlah peserta yang lolos program berdasarkan program studi. Pada _dashboard_ ini, admin dapat melakukan filter berdasrkan tahun dan akan muncul grafik keikutsertaan mahasiswa sesuai dengan tahun yang dibutuhkan.

# **2.3.2.20 Halaman Mengelola Data Informasi Program**

Gambar 2.45 Halaman Mengelola Data Informasi Program

Pada halaman informasi ini, admin dapat mengklik _button_ “+” untuk menambah informasi program. Setelah itu, admin dapat mengisi data-data yang dibutuhkan untuk menambah informasi, seperti memilih Program Studi, input Nama Instansi, Judul Informasi, Tanggal Pendaftaran, Tanggal Berakhir, Kategori Program, Deskripsi, dan Poster Pendaftaran. Setelah selesai, admin dapat mengklik _button_ “Simpan” dan data informasi program akan tersimpan pada sistem.

# **2.3.2.21 Halaman Melihat Daftar Mahasiswa**

# **2.3.2.21.1 Halaman Data Pendaftaran Program Kerjasama**

<!-- Start of picture text -->
©) men Daftar Mahasiswa<br>= saree st =) amen -|<br>© biome beter mens eg ene pa actos sa rhaok =<br>|B Doha Pembimbing ~ “ _ a — ~ ~~<br>senses int . .<br>tome<br>1 twee<br><!-- End of picture text -->

Gambar 2.46 Halaman Data Pendaftaran Program Kerjasama

Pada halaman ini, admin dapat melihat daftar mahasiswa yang telah mendaftar pada program kerja sama universitas. Admin dapat melakukan filter berdasarkan program studinya untuk mempermudah mencari mahasiswa yang dibutuhkan. Lalu, admin dapat mengklik _button_ “Download” untuk men _download_ data mahasiswa yang terdaftar dalam bentuk excel.

# **2.3.2.21.2 Halaman Data Mahasiswa Yang Mengikuti Program**

<!-- Start of picture text -->
) —— Daftar Mahasiswa<br>aa “Serrwa Program Stu Sera Program - [ccm J<br>_Doftar mahosiswa yang mengkut program exchange J somone<br><!-- End of picture text -->

Gambar 2.47 Halaman Data Mahasiswa Yang Mengikuti Program

Pada halaman ini, admin dapat melihat daftar mahasiswa yang mengikuti program exchange IISMA, PMM, dan Kerja Sama Universitas. Admin dapat melakukan filter berdasarkan program studi dan berdasarkan kategori program untuk mempermudah mencari mahasiswa yang dibutuhkan. Lalu, admin dapat mengklik _button_ “Download” untuk men _download_ data mahasiswa yang mengikuti program dalam bentuk excel.

# **2.3.2.22 Halaman Memverifikasi Status Pendaftaran Mahasiswa**

<!-- Start of picture text -->
©) Sects mere Status Pendaftaran<br>-<br>—_ — .<br>~ rexgputetanon — regente ” 6)<br>—<br>tower— _eto —Seenstomas -mae =<br>= —<br><!-- End of picture text -->

Gambar 2.48 Halaman Memverifikasi Status Pendaftaran Mahasiswa

Pada halaman status pendaftaran mahasiswa ini, admin dapat melihat _detail_ file-file yang sudah di _upload_ oleh mahasiswa dengan mengklik icon “eye”. Lalu, admin dapat melakukan aksi dengan mengklik icon “ceklis” untuk menerima mahasiswa dan icon “silang” untuk menolak mahasiswa. Apabila mahasiswa tidak diterima, maka statusnya akan “Ditolak”. Jika mahasiswa diterima, maka statusnya akan “Diterima”. Pada halaman ini admin dapat melakukan filter untuk menampilkan data dari paling lama hingga paling baru. Untuk mempermudah pencarian mahasiswa, admin dapat menggunakan fitur _search_ agar dapat menemukan mahasiswa yang dibutuhkan dan memverifikasi status pendaftaran mahasiswa tersebut.

# **2.3.2.23 Halaman Mengelola Daftar Dosen Pembimbing**

<!-- Start of picture text -->
eeseawene Daftar Dosen Pembimbing<br>—_— Topvonitaneyah ‘ajotare Unnverstos—_Unverstos Moya mound Khare Wot Gu,<br>© ape<br>16 torneo —<br><!-- End of picture text -->

Gambar 2.49 Halaman Mengelola Daftar Dosen Pembimbing

Pada halaman ini, admin dapat melihat data mahasiswa yang belum mendapatkan dosen pembimbing. Kemudian, admin dapat mengklik _button_ “Pilih Dosen” pada kolom aksi. Admin dapat memilih dosen pembimbing untuk mahasiswa tersebut dengan daftar dosen yang tersedia di Fakultas Ilmu Komputer. Admin dapat menggunakan fitur _search_ untuk mempermudah mencari mahasiswa yang sedang dibutuhkan.

# **2.3.2.24 Halaman Mengelola Daftar Mahasiswa** **_Inbound_**

<!-- Start of picture text -->
4) Gem<br>aa<br>©comme<br>B tating utnenne<br>Orn) amin<br>Beene<br>fel rns terorore<br><!-- End of picture text -->

Gambar 2.50 Halaman Mengelola Daftar Mahasiswa _Inbound_

Pada halaman mahasiswa _inbound_ ini, admin dapat mengklik _button_ “+” untuk menambah data mahasiswa _inbound_ . Selanjutnya, admin dapat mengisi datadata yang dibutuhkan seperti, Program Studi, Angkatan, Nama Mahasiswa, Gender, NIM/Username, Password Akun, Konfirmasi Password Akun, Email, No.Telepon, Kategori Exchange, Universitas Asal, Memilih Dosen Pembimbing, Mata Kuliah yang diambil. NIM/ _Username_ dan _Password_ yang telah dibuat oleh admin akan digunakan oleh mahasiswa _inbound_ untuk login ke dalam sistem _student exchange_ dalam melaksanakan bimbingan. Setelah semua data sudah terisi, admin dapat mengklik _button_ “Simpan” dan data mahasiswa _inbound_ ini akan tersimpan oleh sistem.

# **2.3.2.25 Halaman** **_Dashboard_ Koordinator Prodi**

<!-- Start of picture text -->
See<br>seers Cy<br>ors = =<br>Oc) masraomenn ot eternang on 8<br>tant so fnama tenton ae<br>oc . nea . a |<br><!-- End of picture text -->

Gambar 2.51 Halaman _Dashboard_ Koordinator Prodi

Halaman _dashboard_ Koordinator Prodi menampilkan grafik dari keikutsertaan mahasiswa dalam program _exchange_ , seperti tampilan grafik pada program _exchange_ kerja sama universitas, IISMA, dan PMM. Pada grafik tersebut terlihat jumlah pendaftar dan jumlah peserta yang lolos program berdasarkan program studi. Pada _dashboard_ ini, admin dapat melakukan filter berdasrkan tahun dan akan muncul grafik keikutsertaan mahasiswa sesuai dengan tahun yang dibutuhkan. Pada halaman ini juga menampilkan statistik jumlah mahasiswa yang masih membutuhkan _approve_ surat rekomendasi.

# **2.3.2.26 Halaman** **_Dashboard_ Koordinator Prodi**

<!-- Start of picture text -->
(ecm Program Exchange<br>ame ; 7a, ns<br>1 sepmmest oo: veg Sa = ; |e=| t<br>© voner tonone roveneee : ail a i =<br>onaiia a ato! unnes<br> etretomen OemmveemesCocman” || pipeancanpurenn psionic<br>ces vcein enn cintaan esot<br>et<br><!-- End of picture text -->

Gambar 2.52 Halaman _Dashboard_ Koordinator Prodi

Pada halaman program _exchange,_ Koordinator Prodi dapat melihat semua informasi seputar program _exchange_ yang tersedia. Koordinator Prodi dapat menggunakan menu filter dan _search_ untuk mempermudah Koordinator Prodi dalam mencari informasi yang dibutuhkan. Pada filter terdapat pilihan filter kategori program dan program studi, sehingga mempermudah Koordinator Prodi untuk melihat informasi program sesuai dengan program studi dan kategori program yang ingin mereka ikuti. Pada halaman ini, terdapat informasi tanggal mulai pendaftaran program dan tanggal batas akhir pendaftaran. Untuk melihat _detail_ dari setiap informasi, mahasiswa dapat klik “Lihat _Detail_ ” dan akan masuk ke halaman _detail_ dari informasi program tersebut.

# **2.3.2.27 Halaman** **_Approve_ Surat Rekomendasi**

<!-- Start of picture text -->
SRE |2pproveSurat Rekomendasi<br>— seen . F : 7 : oo<br><!-- End of picture text -->

Gambar 2.53 Halaman _Approve_ Surat Rekomendasi

Pada halaman _approve_ surat rekomendasi, Koordinator Prodi dapat melihat kelengkapan file-file yang terlah diinput oleh mahasiswa saat ingin mengajukan surat rekomendasi. Koordinator Prodi dapat mengklik _button_ “Terima” apabila ingin memberikan surat rekomendasi kepada mahasiswa pada kolom aksi. Jika Koordinator Prodi ingin menolak, maka Koordinator Prodi dapat mengklik _button_ “Tolak” pada kolom aksi dan Koordinator Prodi dapat menginput alasan penolakan pemberian surat rekoemndasi kepada mahasiswa tersebut. Pada halaman ini tersdapat fitur _search_ untuk mempermudah Koordinator Prodi dalam mencari mahasiswa yang sedang dibutuhkan.

# **2.3.2.28 Halaman Approve Surat Rekomendasi**

**2.3.2.28.1 Halaman Data Pendaftaran Program Kerjasama**

<!-- Start of picture text -->
0) Saecmmeoan Daftar Mahasiswa<br>— | —= i =<br><!-- End of picture text -->

Gambar 2.54 Halaman Data Pendaftaran Program Kerjasama

Pada halaman ini, Koordinator Prodi dapat melihat daftar mahasiswa yang telah mendaftar pada program kerja sama universitas. Koordinator Prodi dapat melakukan filter berdasarkan program studinya untuk mempermudah mencari mahasiswa yang dibutuhkan. Lalu, Koordinator Prodi dapat mengklik _button_ “ _Download_ ” untuk men _download_ data mahasiswa yang terdaftar dalam bentuk excel.

# **2.3.2.28.2 Halaman Data Mahasiswa Yang Mengikuti Program**

<!-- Start of picture text -->
Oieeeiene Daftar Mahasiswa<br>oo ‘Somua Program Sus Sema Progam za<br>omer& ponte cnermeinn arrohenpen =<br>+a<br>ere TT :<br><!-- End of picture text -->

Gambar 2.55 Halaman Data Mahasiswa Yang Mengikuti Program

Pada halaman ini, Koordinator Prodi dapat melihat daftar mahasiswa yang mengikuti program exchange IISMA, PMM, dan Kerja Sama Universitas. Koordinator Prodi dapat melakukan filter berdasarkan program studi dan berdasarkan kategori program untuk mempermudah mencari mahasiswa yang dibutuhkan. Lalu, Koordinator Prodi dapat mengklik _button_ “Download” untuk men _download_ data mahasiswa yang mengikuti program dalam bentuk excel.

# **2.3.2.29 Halaman** **_Approve_ Konversi SKS**

<!-- Start of picture text -->
C)pereee Approve KonversiSKS<br>— Parry sasoon vena een emu rnaioetoon—rumantene at<br>1B pps .<br>© togaut n ,<br>4 sense<br><!-- End of picture text -->

Gambar 2.56 Halaman _Approve_ Konversi SKS

Pada halaman _approve_ konversi sks, Koordinator Prodi dapat melihat kelengkapan file-file yang terlah diinput oleh mahasiswa untuk keperluan konversi sks, yaitu file logbook dan file transkip nilai. Jika file mahasiswa sudah memenuhi syarat, maka Koordinator Prodi dapat mengklik _button_ “Approved” Pada halaman ini tersdapat fitur _search_ untuk mempermudah Koordinator Prodi dalam mencari mahasiswa yang sedang dibutuhkan.

# **2.3.2.30 Halaman** **_Approve_ Bukti Pelaksanaan** **_Inbound_**

<!-- Start of picture text -->
F) beri Bukti Pelaksanaan Exchange Inbound<br>t vetbead Cee fase<br><!-- End of picture text -->

Gambar 2.57 Halaman _Approve_ Bukti Pelaksanaan Inbound

Pada halaman _approve_ bukti pelaksanaan inbound, Koordinator Prodi dapat melihat file bukti pelaksanaan kegiatan yang telah di _upload_ oleh dosen PIC untuk keperluan konversi sks. Jika file bukti pelaksanaan sudah memenuhi syarat, maka Koordinator Prodi dapat mengklik _button_ “Approved”. Pada halaman ini tersdapat fitur _search_ untuk mempermudah Koordinator Prodi dalam mencari mahasiswa yang sedang dibutuhkan.

# **2.3.2.31 Halaman** **_Dashboard_ Dosen Pembimbing**

<!-- Start of picture text -->
program Exchange<br>1 Progrom Exchange Program change MBRIL{ rogram txchonge is rogram txhange<br>© serceiewe Betingan<br>{8 cat simbingon<br>0, epoca =<br>Jadwal Bimbingan<br>& togout<br><!-- End of picture text -->

Gambar 2. 58 Halaman _Dashboard_ Dosen Pembimbing

Pada halaman _dashboard_ , dosen pembimbing dapat melihat melihat program exchange yang tersedia dan melihat statisistik jumlah mahasiswa bimbingan-Nya, jadwal bimbingan, dan laporan bimbingan.

# **2.3.2.32 Halaman Informasi Program** **_Exchange_**

<!-- Start of picture text -->
a Program Exchange<br>(FaNy student exchange<br>=<br> Dohboord forego rogram ;<br>__.. ns at ru<br>Onm oe Fs) Ne<br>Oram eo EH<br><oomenen  tejosoma ap ae = » || \<br>{8 Jodeci tentingan | © semeCV ~ ah* UNNES<br>0 item norman = =| *<br>BLeporonsimbingon Oa semeset ————— cee<br>+ 0 siromata Program Exchange Mehasswa rogram change Maas<br>‘S1Sistem informasi, ‘Dil Sistem informasi<br>& Logout Inrecent yeors UPN "Veteran Jakartahos sent over20 _Intecent years, PN Veteran’ Jakarta has set over 20<br>students abroad per yor to study for one students abroad pe yer to sty for one.<br><!-- End of picture text -->

Gambar 2.59 Halaman Informasi Program _Exchange_

Pada halaman program _exchange,_ dosen pembimbing dapat melihat semua informasi seputar program _exchange_ yang tersedia. Dosen pembimbing dapat menggunakan menu filter dan _search_ untuk mempermudah dosen pembimbing dalam mencari informasi yang dibutuhkan. Pada filter terdapat pilihan filter kategori program dan program studi, sehingga mempermudah dosen pembimbing untuk melihat informasi program sesuai dengan program studi dan kategori program yang ingin mereka ikuti. Pada halaman ini, terdapat informasi tanggal mulai pendaftaran program dan tanggal batas akhir pendaftaran. Untuk melihat _detail_ dari setiap informasi, dosen pembimbing dapat klik “Lihat _Detail_ ” dan akan masuk ke halaman _detail_ dari informasi program tersebut.

# **2.3.2.33 Halaman Daftar Mahasiswa Bimbingan**

<!-- Start of picture text -->
LJ) studentunm verERAn txchongeJAKARTA Daftar Mahasiswa Bimbingan<br>& oshboors<br>§& Program Exchange \Muhommed20h Momdoni Nt rversias Negeri Padang food 200612M@mahaxiowa.upmo<br>8 Loporan simbingan /<br>© Logout ~~<br>sera<br>Wt out $7,<br><!-- End of picture text -->

Gambar 2.60 Halaman Daftar Mahasiswa Bimbingan

Pada halaman mahasiswa bimbingan, dosen pembimbing dapat melihat daftar mahasiswa yang masuk ke dalam bimbingan-Nya. Dosen pembimbing dapat mengetahui progress dari setiap mahasiswa dengan mengklik _button_ “Lihat Progres” pada kolom aksi, yang nantinya akan muncul tampilan progress bar tahapan mahasiswa dalam mengikuti rangkaian program _exchange_ .

# **2.3.2.34 Halaman Membuat Jadwal Bimbingan**

<!-- Start of picture text -->
) aewee Cd<br>— BS<br>tate<br>me —<br>8 rogomincnege mein .<br>ome— onsron~~ 0s —-- 0<br>1 prt tes<br>~~ ets<br>© loge we: BIUN EEE<br>tame<br><!-- End of picture text -->

Gambar 2.61 Halaman Membuat Jadwal Bimbingan

Pada halaman membuat jadwal bimbingan, dosen pembimbing dapat mengklik button “+” untuk membuat jadwal. Kemudian, dosen pembimbing dapat memasukkan data-data yang dibutuhkan, seperti Nama Bimbingan, Tanggal Bimbingan, Waktu Bimbingan, Tempat, Deskripsi, dan Tambahkan Foto. Setelah semua data terisi, dosen pembimbing dapat mengklik button “Simpan” dan jadwal bimbingan mahasiswa tersebut dapat tersimpan oleh sistem.

# **2.3.2.35 Halaman Mengelola Jadwal Bimbingan**

<!-- Start of picture text -->
@) Eeeeeeen Jadwal Bimbingan<br>cea igen wa<br>1 cpr ngs<br>(toga<br><!-- End of picture text -->

Gambar 2.62 Halaman Mengelola Jadwal Bimbingan

Pada halaman jadwal bimbingan, dosen pembimbing dapat mengelola jadwal bimbingan-Nya. Dosen pembimbing dapat melakukan aksi “Edit” untuk mengubah data jadwal bimbingan dan juga dapat melakukan aksi “Hapus” untuk menghapus jadwal bimbingan yang telah dibuat. Dosen pembimbing dapat mengklik _button_ “+” untuk menambah jadwal bimbingan. Pada halaman ini terdapat fitur _search_ untuk mempermudah dosen pembimbing mencari data jadwal bimbingan dengan mudah.

# **2.3.2.36 Halaman Mengelola Laporan Bimbingan Mahasiswa**

<!-- Start of picture text -->
YESS ESRAME | Loporan Bimbingan Mahasiswa Exchange<br><!-- End of picture text -->

Gambar 2.63 Halaman Mengelola Laporan Bimbingan Mahasiswa

Pada halaman laporan bimbingan, dosen pembimbing dapat melihat hasil laporan bimbingan mahasiswa, seperti melihat kendala yang dihadapi oleh mahasiswa selama mengikuti program. Lalu, dosen pembimbing dapat mengklik _button_ “Edit” pada kolom aksi untuk mengubah data laporan mahasiswa apabila terdapat ketidaksesuaian. Dosen pembimbing dapat melakukan aksi untuk menghapus laporan mahasiswa dengan mengklik _button_ “Hapus”. Selain itu, dosen pembimbing dapat melihat catatan dari dosen PIC dengan mengklik “Lihat Remark”. Pada tampilan ini terdapat fitur _search_ untuk mempermudah dosen pembimbing dalam mencari laporan mahasiswa dan juga terdapat _button_ “Export” untuk men _download_ hasil laporan bimbingan dalam bentuk excel.

# **2.3.2.37 Halaman** **_Dashboard_ PIC Program PMM**

<!-- Start of picture text -->
—____ 7<br>~ Program Euchange Mahasiswa room ticnongenonosine 2 ‘Program Exchange Mahosiswa<br>j<br>om<br>=<br><!-- End of picture text -->

Gambar 2.64 Halaman _Dashboard_ PIC Program PMM

Pada halaman _dashboard_ , dosen PIC program PMM dapat melihat informasi program PMM yang tersediaa. Selain itu, dosen PIC PMM juga dapat melihat statistik daftar mahasiswa bimbingan, jadwal bimbingan, dan laporan bimbingan.

# **2.3.2.38 Halaman Daftar Mahasiswa Program PMM**

<!-- Start of picture text -->
Eee Daftar Mahasiswa Program PMM<br>QQ EE =o<br>1 roma<br><!-- End of picture text -->

Gambar 2.65 Halaman Daftar Mahasiswa Program PMM

Pada halaman daftar mahasiswa program PMM, dosen PIC program PMM dapat melihat mahasiswa yang terdaftar dalam program PMM. Dosen PIC dapat mengetahui progress mahasiswa dengan mengklik _button_ “Lihat Progress” dan nanti akan muncul tampilan progress bar mahasiswa yang menampilkan tahapan kegiatan mahasiswa dalam mengikuti program PMM. Dosen PIC dapat mengklik _button_ “ _Download_ ” untuk melakukan _download_ daftar mahasiswa yang mengikuti program PMM.

# **2.3.2.39 Halaman Laporan Bimbingan Program PMM**

<!-- Start of picture text -->
Oca | Loporan Bimbingan Program PMM<br>8 tapweninceiere<br>8 ron<br><!-- End of picture text -->

Gambar 2.66 Halaman Laporan Bimbingan Program PMM

Pada halaman laporan bimbingan program PMM, dosen PIC dapat melihat data laporan bimbingan mahasiswa. Apabila dosen PIC ingin menambahkan catatan pada mahasiswa tersebut, dosen PIC dapat mengklik _button_ “isi _remarks_ ” pada kolom aksi yang nantinya _remarks_ tersebut akan muncul ke tampilan dosen pembimbing untuk disampaikan kepada mahasiswa tersebut. Pada halaman ini, dosen PIC dapat melakukan _filter_ dari paling lama dan paling baru untuk melihat data laporan bimbingan mahasiswa. Dosen PIC dapat menggunakan fitur _search_ untuk mencari laporan bimbingan mahasiswa dengan cepat dan dosen PIC dapat mengklik _button_ ”Export” untuk men- _download_ hasil laporan bimbingan mahasiswa dalam format excel.

# **2.3.2.40 Halaman Laporan Mahasiswa Program PMM**

# **2.3.2.40.1 Halaman Melihat** **_Logbook_ Harian**

<!-- Start of picture text -->
ieeeeenven = Loporan Mahasiswa Program PMM<br> oshboars Loabot ran 7<br>es © Ketic untuk mencari mahasiswa fo |[ =<br>© Logout<br>2 borane<br>sey tomancen stom<br><!-- End of picture text -->

Gambar 2.67 Halaman Melihat _Logbook_ Harian

Pada halaman laporan mahasiswa, dosen PIC dapat melihat laporan logbook harian mahasiswa. Pada halaman ini terdapat fitur _search_ untuk mempermudah dosen PIC dalam menemukan laporan _logbook_ harian mahasiswa dengan cepat. Dosen PIC dapat mengklik button “ _Export_ ” untuk melakukan _download_ data _logbook_ harian mahasiswa program PMM.

# **2.3.2.40.2 Halaman Melihat Laporan Akhir**

<!-- Start of picture text -->
O))eeaeeven = Loporan Mahasiswa Program PMM.<br>Oca Q. Ketik untuk mencari mahasiswa. [ccm | ea<br>© topo<br>48 seranda<br><!-- End of picture text -->

Gambar 2.68 Halaman Melihat Laporan Akhir

Pada halaman laporan mahasiswa, dosen PIC dapat melihat laporan akhir mahasiswa. Dosen PIC dapat mengisi keberhasilan mahasiswa dengan mengklik _button_ “Isi Kebenrhasilan” pada kolom aksi untuk memverifikasi apakah mahasiswa tersebut berhasil atau tidak dalam melaksanakan program exchange PMM.  Pada halaman ini terdapat fitur _search_ untuk mempermudah dosen PIC dalam menemukan laporan akhir mahasiswa dengan cepat. Dosen PIC dapat mengklik _button_ “ _Export_ ” untuk melakukan _download_ data laporan akhir mahasiswa program PMM.

# **2.3.2.41 Halaman Daftar Mahasiswa Program IISMA dan Kerja Sama**

<!-- Start of picture text -->
ED) eeeeniean Daftar Mahasiswa Program IISMA, Kerjasama Universitas<br>——__,, EI =<br>1B Laporan Bimbingon / /<br>SS .<br>fe mtirsctsoncen<br>© toga<br><!-- End of picture text -->

Gambar 2. 69 Halaman Daftar Mahasiswa

Pada halaman daftar mahasiswa program IISMA dan Kerja Sama, dosen PIC program IISMA dan Kerja Sama dapat melihat mahasiswa yang terdaftar dalam program IISMA dan Kerja Sama. Dosen PIC dapat mengetahui progress mahasiswa dengan mengklik _button_ “Lihat Progress” dan nanti akan muncul tampilan progress bar mahasiswa yang menampilkan tahapan kegiatan mahasiswa dalam mengikuti program IISMA dan Kerja Sama. Dosen PIC dapat mengklik _button_ “ _Download_ ” untuk melakukan _download_ daftar mahasiswa yang mengikuti program IISMA dan Kerja Sama.

# **2.3.2.42 Halaman Laporan Bimbingan Program IISMA dan Kerja Sama**

<!-- Start of picture text -->
E)ieecaeeene Loporan Bimbingan Program IISMA, Kerjasama Universitas<br>oe 0. kota untuk mencor mahasiswa wou ~ ED Ey<br>1 regen bchange<br>Approves<br>© ootor ahosiona<br><!-- End of picture text -->

Gambar 2.70 Halaman Laporan Bimbingan Program

Pada halaman laporan bimbingan program IISMA dan Kerja Sama, dosen PIC dapat melihat data laporan bimbingan mahasiswa. Apabila dosen PIC ingin menambahkan catatan pada mahasiswa tersebut, dosen PIC dapat mengklik _button_ “isi remarks” pada kolom aksi yang nantinya _remarks_ tersebut akan muncul ke tampilan dosen pembimbing untuk disampaikan kepada mahasiswa tersebut. Pada halaman ini, dosen PIC dapat melakukan filter dari paling lama dan paling baru untuk melihat data laporan bimbingan mahasiswa. Dosen PIC dapat menggunakan fitur _search_ untuk mencari laporan bimbingan mahasiswa dengan cepat dan dosen PIC dapat mengklik _button “Export”_ untuk men- _download_ hasil laporan bimbingan mahasiswa dalam format excel.

# **2.3.2.43 Halaman Laporan Mahasiswa Program IISMA dan Kerja Sama**

# **2.3.2.43.1 Halaman Melihat** **_Logbook_ Harian**

<!-- Start of picture text -->
Laporan Mahasiswa Program SMA, Kerjasama Universitas<br><!-- End of picture text -->

Gambar 2.71 Halaman Melihat _Logbook_ Harian

Pada halaman laporan mahasiswa, dosen PIC dapat melihat laporan _logbook_ harian mahasiswa. Pada halaman ini terdapat fitur _search_ untuk mempermudah dosen PIC dalam menemukan laporan _logbook_ harian mahasiswa dengan cepat. Dosen PIC dapat mengklik button “ _Export_ ” untuk melakukan _download_ data _logbook_ harian mahasiswa program IISMA dan Kerjasama Universitas.

# **2.3.2.43.2 Halaman Melihat Laporan Akhir**

<!-- Start of picture text -->
G)) Sreverenneseeara Laporan Mahasiswa Program IISMA, Kerjasama Universitas<br><!-- End of picture text -->

Gambar 2.72 Halaman Melihat Laporan Akhir

Pada halaman laporan mahasiswa, dosen PIC dapat melihat laporan akhir mahasiswa. Dosen PIC dapat mengisi keberhasilan mahasiswa dengan mengklik _button_ “Isi Keberhasilan” pada kolom aksi untuk memverifikasi apakah mahasiswa tersebut berhasil atau tidak dalam melaksanakan program _exchange_ IISMA dan

Kerja Sama.  Pada halaman ini terdapat fitur _search_ untuk mempermudah dosen PIC dalam menemukan laporan akhir mahasiswa dengan cepat. Dosen PIC dapat mengklik _button_ “ _Export_ ” untuk melakukan _download_ data laporan akhir mahasiswa program IISMA dan Kerja Sama.

# **2.3.2.44 Halaman Bukti Pelaksanaan Program IISMA dan Kerja Sama**

<!-- Start of picture text -->
@) Sevennamener Bukti Pelaksanaan Exchange Inbound<br>rogram sk, eronoma iverson<br>operon simeingen . .<br>1 Loporen Monasiwe<br>48 verona<br><!-- End of picture text -->

Gambar 2.73 Halaman Bukti Pelaksanaan Program

Pada halaman bukti pelaksanaan program, dosen PIC dapat mengklik _button “Upload”_ pada kolom aksi untuk mengupload bukti pelaksanaan _exchange inbound_ . Jika dosen PIC sudah berhasil melakukan _upload_ bukti, maka data tersebut akan tersimpan pada sistem.

# **2.3.2.45 Halaman Mahasiswa** **_Inbound_**

<!-- Start of picture text -->
©) crete sara Profit<br>soannennaioyrtcom<br>© tome | nyt<br><!-- End of picture text -->

Gambar 2.74 Halaman Mahasiswa _Inbound_

Tampilan halaman untuk mahasiswa _inbound_ ada tampilan profil dan tampilan bimbingan. Untuk tampilan profil, memuat informasi identitas mahasiswa _inbound_ dan progress bar mahasiswa. Untuk tampilan bimbingan mahasiswa inbound sama seperti tampilan bimbingan mahasiswa _outbound_ yang menampilkan informasi dosen pembimbing dan jadwal bimbingan.

# **2.4 Rencana Pengujian Proyek**

Rencana pengujian proyek pada Proyek Pengembangan Sistem Informasi _Student Exchange_ di Fakultas Ilmu Komputer UPN “Veteran” Jakarta adalah menggunakan metode _black box testing_ . _Black box testing_ merupakan sebuah teknik pengujian perangkat lunak yang berfokus pada fungsi sistem tanpa memeriksa struktur internal atau kode programnya. Pengujian ini dilakukan dengan memeriksa _input_ dan _outpu_ t sistem untuk memastikan bahwa setiap fungsi berjalan sesuai dengan spesifikasi yang telah ditentukan. Pengujian ini dilakukan bertujuan untuk memastikan bahwa sistem informasi _student exchange_ dapat memenuhi kebutuhan pengguna dengan baik dan berfungsi secara optimal. Adapun skenario dari _black box testing_ pada penelitian ini dapat dilihat pada tabel berikut.

|**Aktor**|**Skenario Pengujian**|**Hasil yang Diharapkan**|
|---|---|---|
|**Mahasiswa**|-<br>Login dengan|-<br>Sistem berhasil|
||_username_dan|login dan|
||_password_yang|menampilkan|
||valid|halaman|
||-<br>Login dengan|_dashboard_utama|
||_username_atau|-<br>Muncul pesan|
||_password_yang|_error_|
||salah|-<br>Sistem berhasil|
||-<br>Logout dari sistem|logout dan|
|||menampilkan|
|||halaman login|

|-|Masuk menu|-|Sistem berhasil|
|---|---|---|---|
||“_Student_||menampilkan|
||_Exchange_”||_dashboard Student_|
|-|Melihat informasi||_Exchange_|
||program_exchange_|-|Sistem berhasil|
|-|Mengajukan surat||menampilkan|
||rekomendasi||informasi program|
||dengan data yang||IISMA, PMM, dan|
||lengkap||Kerja Sama|
|-|Mengajukan surat||Fakultas yang|
||rekomendasi||ditampilkan sesuai|
||dengan data yang||filter kategori|
||tidak lengkap||program dan filter|
|-|Melengkapi||program studi|
||dokumen untuk|-|Surat rekomendasi|
||mahasiswa yang||berhasil diajukan|
||mengikuti program||dan muncul status|
||kerja sama fakultas||“Sedang diproses”|
|-|Melihat status|-|Muncul pesan|
||pendaftaran untuk||_error_|
||mahasiswa|-|Dokumen berhasil|
||program kerja||tersimpan di sistem|
||sama fakultas|-|Status pendaftaran|
|-|Melakukan||muncul dengan|
||bimbingan||kategori “Sedang|
|-|_Upload_laporan||Diproses”,|
||kegiatan||“Disterima”, atau|
|-|Melihat profil||“Ditolak”|
|||-|Data kehadiran,|
||||kendala, dan bukti|
||||kehadiran berhasil|

|||-<br>-|disimpan dalam<br>sistem<br>File berhasil<br>diunggah dan<br>status “Terkirim”<br>ditampilkan<br>Sistem berhasil<br>menampilkan data<br>profil mahasiswa<br>(Nama, NIM,|
|---|---|---|---|
||||Email, No.tlp) serta|
||||progress bar|
||||tahapan kegiatan|
|**Admin**|-<br>Login dengan|-|Sistem berhasil|
||_username_dan||login dan|
||_password_yang||menampilkan|
||valid||halaman|
||-<br>Login dengan||_dashboard_utama|
||_username_atau|-|Muncul pesan error|
||_password_yang|-|Sistem berhasil|
||salah||logout dan|
||-<br>Logout dari sistem||menampilkan|
||-<br>Masuk menu||halaman login|
||“_Student_|-|Sistem berhasil|
||_Exchange_”||menampilkan|
||-<br>Melakukan CRUD||_dashboard Student_|
||informasi program||_Exchange_|
||_exchange_|-|Informasi program|
||-<br>Melihat daftar||berhasil|
||mahasiswa||ditambahkan,|
||||diubah, atau|

||-|Memperbarui|dihapus sesuai|
|---|---|---|---|
|||status pendaftaran|input|
|||program kerja|-<br>Sistem berhasil|
|||sama fakultas|menampilkan data|
||-|Membuat daftar|mahasiswa sesuai|
|||dosen pembimbing|kategori dan status|
||-|Melihat data|-<br>Status mehasiswa|
|||mahasiswa|berubah menjadi|
|||_inbound_|“Seleksi Berkas”,<br>“Diterima”, atau<br>“Ditolak”|
||||-<br>Daftar dosen|
||||pembimbing|
||||berhasil<br>ditambahkan<br>-<br>Sistem berhasil<br>menampilkan data<br>mahasiswa<br>_inbound_(NIM,<br>Nama, Kategori,|
||||dan Progress|
||||mahasiswa)|
|**Dosen PIC**|-|Login dengan|-<br>Sistem berhasil|
|||_username_dan|login dan|
|||_password_yang|menampilkan|
|||valid|halaman|
||-|Login dengan|_dashboard_utama|
|||_username_atau|-<br>Muncul pesan error|
|||_password_yang|-<br>Sistem berhasil|
||-|salah<br>Logout dari sistem|logout dan|

||-|Masuk menu<br>“_Student_||menampilkan<br>halaman login|
|---|---|---|---|---|
|||_Exchange_”|-|Sistem berhasil|
||-|Melihat informasi||menampilkan|
|||program_exchange_||_dashboard Student_|
||-|Melihat daftar||_Exchange_|
|||mahasiswa|-|Sistem berhasil|
||-|Melihat hasil||menampilkan|
|||laporan bimbingan||informasi program|
|||dan memberikan||IISMA, PMM, dan|
|||pesan kepada||Kerja Sama|
|||dosen pembimbing||Fakultas yang|
||-|Melakukan_upload_||ditampilkan sesuai|
|||bukti pelaksanaan||filter kategori|
|||program IISMA||program dan filter|
|||dan Kerja Sama||program studi|
|||Fakultas|-|Sistem berhasil<br>menampilkan hasil|
|||||laporan bimbingan<br>mahasiswa dan|
|||||pesan dari dosen<br>pic berhasil<br>terkirim dan|
|||||diterima oleh dosen<br>pembimbing|
|**Koordinator**|-|Login dengan|-|Sistem berhasil|
|**Prodi**||_username_dan||login dan|
|||_password_yang||menampilkan|
|||valid||halaman|
||-|Login dengan<br>_username_atau||_dashboard_utama|

|||_password_yang<br>salah|-<br>Muncul pesan<br>_error_|
|---|---|---|---|
||-|Logout dari sistem|-<br>Sistem berhasil|
||-|Masuk menu|logout dan|
|||“_Student_|menampilkan|
|||_Exchange_”|halaman login|
||-|Melihat informasi|-<br>Sistem berhasil|
|||program_exchange_|menampilkan|
||-|Melakukan|_dashboard Student_|
|||_approve_surat|_Exchange_|
|||rekomendasi|-<br>Sistem berhasil|
||-|Menolak surat|menampilkan|
|||rekomendasi|informasi program|
||-|Melakukan|IISMA, PMM, dan|
|||_approve_konversi|Kerja Sama|
||-|Melakukan|Fakultas yang|
|||_approve_bukti|ditampilkan sesuai|
|||pelaksanaan|filter kategori|
|||_inbound_|program dan filter|
||||program studi|
||||-<br>Status konversi|
||||berubah menjadi|
||||“Disetujui”|
||||-<br>Bukti pelaksanaan|
||||berubah status|
||||menjadi|
||||“Disetujui”|
|**Dosen**|-|Login dengan|-<br>Sistem berhasil|
|**Pembimbing**||_username_dan|login dan|
|||_password_yang<br>valid|menampilkan|

|-<br>Login dengan||halaman|
|---|---|---|
|_username_atau||_dashboard_utama|
|_password_yang|-|Muncul pesan|
|salah||_error_|
|-<br>Logout dari sistem|-|Sistem berhasil|
|-<br>Masuk menu||logout dan|
|“_Student_||menampilkan|
|_Exchange_”||halaman login|
|-<br>Melihat informasi|-|Sistem berhasil|
|program_exchange_||menampilkan|
|-<br>Melihat daftar||_dashboard Student_|
|mahasiswa yang||_Exchange_|
|dibimbing|-|Sistem berhasil|
|-<br>Membuat jadwal||menampilkan|
|bimbingan||informasi program|
|-<br>Melihat dan||IISMA, PMM, dan|
|melakukan_update_||Kerja Sama|
|pada laporan||Fakultas yang|
|bimbingan||ditampilkan sesuai|
|||filter kategori|
|||program dan filter|
|||program studi|
||-|Sistem berhasil|
|||menampilkan data|
|||mahasiswa yang|
|||termasuk dalam|
|||bimbingan|
||-|Jadwal bimbingan|
|||berhasil dibuat dan|
|||tersimpan dalam<br>sistem|

|-<br>Sistem berhasil|
|---|
|menampilkan|
|laporan mahasiswa|
|dengan tampilan|
|opsi_edit_dan_delete_|

Tabel 2.4 Rencana Pengujian Proyek


# PROYEK: PEMBANGUNAN SISTEM INFORMASI PENGAJUAN CUTI MAHASISWA PADA FAKULTAS ILMU KOMPUTER UPN “VETERAN” JAKARTA BERBASIS WEBSITE

# **BAB II**

# **RANCANGAN PROYEK**

# **2.1 Observasi**

# **2.1.1 Proses Bisnis Saat Ini**

Berdasarkan pengumpulan data yang telah dilakukan, alur pengajuan cuti akademik mahasiswa saat ini dapat digambarkan sebagai berikut.

Gambar 2.1 Alur Pengajuan Cuti Akademik Mahasiswa Saat Ini

Proses pengajuan cuti akademik diawali dari mahasiswa yang mengunduh, mencetak, dan mengisi form cuti akademik, lalu melapor ke Dosen Pembimbing Akademik (PA) untuk mendapatkan persetujuan melalui tanda tangan. Setelah mendapat persetujuan, mahasiswa mengisi _Google Form_ dan mengunggah dokumen persyaratan yang kemudian diperiksa oleh Staf Kemahasiswaan Fakultas. Staf Kemahasiswaan Fakultas mencetak form beserta dokumen persyaratan, membuat Surat Pengantar Cuti Akademik, lalu mengirimnya ke Koordinator Tata Usaha (TU) dan Koordinator Prodi untuk diparaf, kemudian kepada Dekan untuk ditandatangani. Setelah di paraf dan ditandatangani, Surat Pengantar akan diberikan nomor oleh Staf Kemahasiswaan Fakultas, baru kemudian Surat Pengantar yang hanya berisi tanda tangan Dekan dan dokumen pendukung dikirim ke Biro AKK, yang meneruskannya ke Kepala Bagian Akademik. Setelah disetujui, Kepala Bagian Akademik mendisposisikan berkas tersebut ke Konseptor untuk pembuatan Surat Keputusan Cuti Akademik dalam bentuk draft.

Draft Surat Keputusan Cuti Akademik ini dikirimkan untuk mendapat paraf dari Kepala Bagian Akademik, Koordinator UHT dan BMN, Kepala Biro AKK, Kepala Biro Umum dan Keuangan, dan Wakil Rektor Bidang Keuangan. Setelah semua paraf terkumpul, Konseptor membuat Surat Keputusan Cuti Akademik asli yang kemudian dikirim ke Wakil Rektor Bidang Akademik untuk ditandatangani. Setelah ditandatangani, Konseptor mengajukan Surat Permohonan Ijin Penomoran Keputusan kepada Kepala Bagian Akademik, yang setelah ditandatangani, nomor dikeluarkan oleh Biro AKK dan dikembalikan ke Konseptor.

Selanjutnya, Surat Keputusan Cuti Akademik baik yang draft maupun asli serta Surat Permohonan Ijin Penomoran Keputusan diserahkan kepada Rektor untuk disetujui dan didisposisikan ke Bagian Umum untuk diberi nomor pada Surat Keputusan Cuti Akademik asli. Setelah nomor diberikan, Konseptor memfotokopi Surat Keputusan asli dan mengirimkannya ke Staf Kemahasiswaan Fakultas. Staf Kemahasiswaan Fakultas menerima informasi dari Konseptor bahwa Surat Keputusan Cuti Akademik telah selesai, mengambilnya, dan menyerahkannya kepada Mahasiswa, serta melakukan pendokumentasian dan pencatatan dalam sistem.

# **2.1.2 Analisis PIECES**

Untuk mengevaluasi sistem pengajuan cuti akademik yang ada dan merencanakan perbaikan pada sistem baru, digunakan pendekatan analisis PIECES ( _Performance, Information, Economy, Control, Efficiency, Service_ ). PIECES adalah metode yang membantu mengidentifikasi masalah dalam sistem yang berjalan serta memberikan gambaran mengenai perbaikan yang dibutuhkan. Melalui analisis ini, area-area yang membutuhkan perbaikan dapat ditemukan, dan solusi yang tepat untuk meningkatkan efektivitas serta efisiensi sistem dapat dirumuskan. Tabel berikut menyajikan analisis tersebut untuk memberikan gambaran yang lebih jelas mengenai perbedaan dan perbaikan yang akan dilakukan pada sistem pengajuan cuti akademik.

Tabel 2.1 Analisis PIECES

|**Aspek**|**Sistem Lama**|**Sistem Baru**|
|---|---|---|
|_Performance_|Proses<br>persetujuan|Persetujuan dapat dilakukan|
|(Kinerja)|membutuhkan waktu lama<br>karena<br>harus<br>dilakukan<br>secara<br>manual<br>dan<br>melibatkan banyak pihak,<br>sehingga memakan waktu<br>hingga 1 bulan.|secara digital, mempercepat<br>waktu penyelesaian.|
|_Information_<br>(Informasi)|Mahasiswa sulit mengetahui<br>secara pasti status pengajuan<br>mereka karena hanya bisa|Sistem menyediakan fitur<br>untuk<br>memantau<br>status<br>secara<br>_real-time_,|
||mendapatkan<br>informasi|memungkinkan mahasiswa|
||dengan menghubungi staf|untuk<br>mengakses|
||kemahasiswaan<br>fakultas<br>melalui_WhatsApp_.|perkembangan<br>pengajuan<br>mereka secara_online_kapan<br>saja.|
|_Economy_|Dokumen seperti formulir<br>pengajuan dan surat-surat|Penggunaan dokumen dan<br>pengarsipan<br>digital|

|(Ekonomi)|yang harus dicetak untuk<br>keperluan persetujuan dan|membantu<br>mengurangi<br>biaya cetak.|
|---|---|---|
||arsip<br>menambah<br>biaya<br>operasional.||
|_Control_<br>(Kontrol)|Data disimpan di Excel dan<br>arsip manual tanpa adanya<br>pengaturan hak akses yang<br>terstruktur,<br>sehingga<br>berisiko data diakses oleh<br>pihak yang tidak berwenang.|Hak akses diatur sesuai<br>peran pengguna, dan data<br>disimpan<br>dalam<br>sistem<br>_database_terpusat dengan<br>keamanan yang lebih baik<br>dan lebih terstruktur.|
|_Efficiency_<br>(Efisiensi)|Mahasiswa harus mencetak<br>formulir, mengisinya secara<br>manual,<br>lalu<br>mengunggahnya kembali ke|Pengajuan dan persetujuan<br>dilakukan<br>secara<br>digital,<br>mempermudah proses dan<br>mengurangi<br>langkah-|
||_Google_<br>_Form_,<br>yang<br>membuat proses lebih rumit<br>dan memakan waktu. Selain<br>itu, proses menjadi lebih<br>lambat karena pengiriman|langkah<br>yang<br>memakan<br>waktu.|
||dokumen<br>fisik<br>untuk<br>persetujuan.||
|_Service_|Mahasiswa harus menunggu|Mahasiswa dapat memantau|
|(Pelayanan)|respons<br>dari<br>staf|status<br>pengajuan<br>cuti|
||kemahasiswaan<br>fakultas|mereka secara mandiri dan|
||untuk<br>mengetahui<br>status|_real-time_,<br>mengurangi|
||pengajuan, yang terkadang|ketergantungan<br>pada staf|
||memakan<br>waktu<br>lama|dan<br>meningkatkan|
||karena adanya koordinasi<br>antar pihak.|transparansi serta kualitas<br>layanan.|

# **2.2 Usulan Solusi**

# **2.2.1** **_Data Flow Diagram_**

_Data Flow Diagram_ (DFD) menggambarkan aliran data dalam usulan sistem informasi pengajuan cuti akademik mahasiswa Fakultas Ilmu Komputer UPN “Veteran” Jakarta. DFD terdiri dari beberapa tingkatan, yaitu Level 0, Level 1, dan Level 2. Pada DFD Level 0 disajikan gambaran umum sistem secara menyeluruh dengan menunjukkan entitas luar yang terlibat serta aliran data antara entitas tersebut dan sistem. Selanjutnya, pada DFD Level 1 diuraikan proses-proses utama yang terjadi di dalam sistem, lengkap dengan _data store_ yang digunakan serta alur data antar proses dan entitas. Kemudian, DFD Level 2 memberikan rincian lebih lanjut dari salah satu proses pada Level 1 dengan menggambarkan langkah-langkah yang lebih spesifik untuk memperjelas logika proses tertentu dalam sistem.

# **2.2.1.1 DFD Level 0**

<!-- Start of picture text -->
Data Logir ‘Sistem Pengajuan ‘Preview Surat Keputusan Cut ‘Bagian Umum<br>cout akedomik Mehasiwa<br>Fakuitas: “a<br>-Nomor Surat Pengantar Pai Losi<br>a<br><!-- End of picture text -->

Gambar 2.2 DFD Level 0

Pada DFD Level 0, terdapat tujuh aktor eksternal yang berinteraksi dengan sistem, yaitu Mahasiswa, Dosen Pembimbing Akademik (PA), Staf Kemahasiswaan Fakultas, Pihak Fakultas, Pihak Universitas, Bagian Umum, dan Super Admin. Setiap aktor dapat mengakses sistem dengan data _login_ masing-masing. Proses dimulai ketika Mahasiswa mengajukan data pengajuan cuti ke sistem. Setelah itu, sistem menginformasikan status pengajuan cuti kepada Mahasiswa. Selanjutnya, data pengajuan cuti dikirimkan ke Dosen PA, yang bertugas memberikan

persetujuan atas pengajuan tersebut. Proses ini kemudian berlanjut ke Staf Kemahasiswaan Fakultas, yang menerima data pengajuan cuti untuk melakukan verifikasi dan persetujuan. Setelah verifikasi, data tersebut diteruskan ke Pihak Fakultas, yang dapat melihat data pengajuan cuti dan _preview_ Surat Pengantar untuk memberikan persetujuan. Setelah disetujui oleh Pihak Fakultas, data kembali ke Staf Kemahasiswaan Fakultas untuk penginputan nomor Surat Pengantar. Selanjutnya, data pengajuan cuti beserta Surat Pengantar dan _preview_ Surat Keputusan Cuti dikirimkan ke Pihak Universitas untuk mendapatkan persetujuan akhir. Akhirnya, sistem mengirimkan data pengajuan cuti, Surat Pengantar, dan _preview_ Surat Keputusan Cuti kepada Bagian Umum, yang bertugas memberikan penomoran pada Surat Keputusan Cuti. Setelah diberikan nomor, Surat Keputusan Cuti yang telah selesai akan tersedia di sistem dan dapat diakses oleh Mahasiswa, Staf Kemahasiswaan Fakultas, dan Bagian Umum. Selain itu, terdapat Super Admin yang bertugas mengelola manajemen _user_ .

# **2.2.1.2 DFD Level 1**

<!-- Start of picture text -->
: * ve<br>=<br>Lo | Oa<br>ss<br>connor cise}Se — eo<br>—<br>ror —<br>al Pengantar<br>(te) —<br>—— \_ eee<br>coe —| rena ene =<br>—<br>—<br>[mm | ving =<br><!-- End of picture text -->

Gambar 2.3 DFD Level 1

Pada DFD Level 1, terdapat tujuh aktor eksternal, yaitu Mahasiswa, Dosen Pembimbing Akademik (PA), Staf Kemahasiswaan Fakultas, Pihak Fakultas, Pihak Universitas, Bagian Umum, dan Super Admin, serta sembilan proses utama. Proses pertama adalah _Login_ , di mana semua aktor mengirimkan data _login_ ke sistem, yang kemudian memverifikasi data tersebut melalui _data store_ “ _Login_ ” dan mengembalikan status _login_ serta hak akses kepada semua aktor. Setelah proses _Login_ , terdapat proses kedua, yaitu Manajemen _User_ , yang khusus dikelola oleh Super Admin. Pada proses ini, Super Admin dapat mengelola data _user_ , data _role_ , dan data _permission_ yang disimpan dalam _data store_ “ _Users_ ”, “ _Roles_ ”, dan “ _Permissions_ ”. Proses ketiga adalah Pengajuan Cuti, di mana Mahasiswa mengirimkan data pengajuan cuti ke sistem, yang disimpan dalam _data store_ “Pengajuan Cuti” dan memberikan status pengajuan kembali kepada Mahasiswa.

Selanjutnya, proses Persetujuan Dosen PA mengambil data pengajuan cuti dari _data store_ dan mengirimkannya ke Dosen PA untuk mendapatkan persetujuan, yang kemudian dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Proses Verifikasi dan Persetujuan Staf Kemahasiswaan Fakultas dimulai dengan pengambilan data pengajuan cuti dari _data store_ oleh sistem dan ditampilkan kepada Staf Kemahasiswaan Fakultas untuk diverifikasi dan disetujui. Persetujuan ini dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Selanjutnya, pada proses Persetujuan Pihak Fakultas, sistem menampilkan data pengajuan cuti beserta _preview_ Surat Pengantar kepada Pihak Fakultas, yang kemudian memberikan persetujuan, juga dicatat dalam “Log Status Pengajuan Cuti”. Setelah itu, proses Penomoran Surat Pengantar dilakukan oleh Staf Kemahasiswaan Fakultas, di mana sistem menampilkan _preview_ Surat Pengantar, lalu nomor Surat Pengantar dimasukkan dan disimpan ke dalam _data store_ “Pengajuan Cuti”.

Berikutnya, proses Persetujuan Universitas menampilkan data pengajuan cuti, Surat Pengantar, dan _preview_ Surat Keputusan Cuti kepada Pihak Universitas untuk disetujui, dan dicatat dalam “Log Status Pengajuan Cuti”. Proses terakhir adalah Penomoran Surat Keputusan oleh Bagian Umum, yang menerima data pengajuan cuti, Surat Pengantar, dan _preview_ Surat Keputusan Cuti, lalu memberikan nomor Surat Keputusan yang juga disimpan dalam _data store_ “Pengajuan Cuti”. Setelah diberikan nomor, sistem akan mengirimkan Surat

Keputusan Cuti yang sudah jadi kepada Mahasiswa, Staf Kemahasiswaan Fakultas dan Bagian Umum.

# **2.2.1.3 DFD Level 2** **_Login_**

<!-- Start of picture text -->
—<br>eras<br>PA dan Parone oor UT<br>Dosen an Pssnr dan Bt<br>eur Kenanasonaanmae Joram sencan asec raean Pastore<br>KeertatoeTU | -tsemanecin Pans ranecan Passe Kotanion<br>Keen Prost | serein Poses Int Ota1 °° Loin sores enemas —| Week Sang<br>a ee<br>Lear<br>en Paes<br>oiatog >] Users<br>Log in Ha Ate tr Log an Ha Ak<br>sag an aK 7 tt Lag din Ha A<br>Sit apn don Hk toe bea og Sit apn don kA<br>is Leg in Ake ts Leg in HA<br>Logsr ag ada ak Sr Logn in Hoke<br><!-- End of picture text -->

Gambar 2.4 DFD Level 2 _Login_

Pada DFD Level 2 untuk proses _Login_ , terdapat dua sub-proses yaitu Input Data _Login_ (1.1) dan Validasi Data _Login_ (1.2). Proses dimulai ketika semua aktor eksternal memasukkan _username_ dan _password_ mereka. Setelah data _login_ dimasukkan, informasi tersebut akan divalidasi dengan mengirimkannya ke _data store_ “ _User_ ”. Proses validasi ini memastikan bahwa _username_ dan _password_ yang dimasukkan sesuai dengan data yang ada di _data store_ . Setelah verifikasi dilakukan, hasil validasi akan dikembalikan kepada aktor eksternal, yang kemudian menerima status _login_ beserta hak akses mereka.

# **2.2.1.4 DFD Level 2 Manajemen** **_User_**

<!-- Start of picture text -->
Data Use Pengelolann24 Data User DalaUse——> Users<br>Data Use<br>Data User<br>Super Admin ataData Ra Ro Pengeoien,engel Data Role ‘DataData RoleRole ——> Roles<br>aia Perniesiet 23 Data Permissior—><br>Data Permission Pengelolaan Data Permissions<br>Permission ‘Data Permission<br><!-- End of picture text -->

Gambar 2.5 DFD Level 2 Manajemen _User_

Pada DFD Level 2 untuk proses Manajemen _User_ , terdapat tiga sub-proses utama, yaitu Pengelolaan Data _User_ (2.1), Pengelolaan Data _Role_ (2.2), dan Pengelolaan Data _Permission_ (2.3). Proses ini dimulai ketika Super Admin mengakses sistem untuk mengelola data _user_ , _role_ , dan _permission_ . Dalam pengelolaan data _user_ , Super Admin dapat menambah, mengubah, atau menghapus data _user_ , dan hasil perubahan tersebut akan disimpan dalam _data store_ “ _Users_ ”. Selanjutnya, pada sub-proses pengelolaan data _role_ , Super Admin dapat menambah, mengubah, atau menghapus data _role_ , dengan perubahan data tersebut tersimpan di _data store_ “ _Roles_ ”. Terakhir, dalam pengelolaan data _permission_ , Super Admin dapat menambah, mengubah, atau menghapus data _permission_ , dan hasil pengelolaan ini akan disimpan di _data store_ “ _Permissions_ ”.

# **2.2.1.5 DFD Level 2 Pengajuan Cuti**

<!-- Start of picture text -->
Data Pengajuan Cul Mengisi Form<br>Mahasiswa 34<br>Pengajuan Cutt<br>Data Pengajuan Cut<br>32<br>Validasi Data<br>Pengajuan Cut<br>Data Pengajuan Cuti Valid<br>33<br>‘Simpan Data Data Pengajuan Cut—> _Pengajuan Cut<br>Pengajuan Cut)<br>Data Pengajuan Cut 34<br>status Pengajuan"a Cut ‘MenampikanPengaiuan Cut DataPengejuan|<br><!-- End of picture text -->

Gambar 2.6 DFD Level 2 Pengajuan Cuti

Pada DFD Level 2 untuk proses Pengajuan Cuti, terdapat empat sub-proses yaitu Mengisi Form Pengajuan Cuti (3.1), Validasi Data Pengajuan Cuti (3.2), Simpan Data Pengajuan Cuti (3.3), dan Menampilkan Data Pengajuan Cuti (3.4). Proses dimulai ketika Mahasiswa mengirimkan data pengajuan cuti melalui form yang tersedia. Setelah form diisi, data tersebut divalidasi untuk memastikan kelengkapannya. Jika data dinyatakan valid, informasi tersebut akan disimpan dalam _data store_ “Pengajuan Cuti”. Data yang telah tersimpan ini kemudian dapat diakses kembali oleh Mahasiswa, sekaligus menampilkan status pengajuan cuti agar mereka dapat memantau perkembangan prosesnya.

**2.2.1.6 DFD Level 2 Persetujuan Dosen PA**

<!-- Start of picture text -->
a<br>Pagan2 an<br>—<br>[= | Kabag ace _<br>hoor UT dana<br>“a<br>Poesia<br>Kare Uru on<br><!-- End of picture text -->

Gambar 2.7 DFD Level 2 Persetujuan Dosen PA

Pada DFD Level 2 untuk proses Persetujuan Dosen PA, terdapat empat subproses yaitu Menerima Notifikasi (4.1), Menampilkan Pengajuan Cuti (4.2), Memberikan Persetujuan (4.3), dan Menampilkan Status Persetujuan (4.4). Proses dimulai dengan notifikasi yang dikirim kepada Dosen PA. Setelah menerima notifikasi, data pengajuan cuti diambil dari _data store_ dan ditampilkan kepada Dosen PA untuk ditinjau. Dosen PA kemudian memberikan persetujuan, yang hasilnya dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Akhirnya, status persetujuan diambil dari _data store_ dan diinformasikan kepada aktor-aktor terkait.

**2.2.1.7 DFD Level 2 Verifikasi dan Persetujuan Staf Kmhs Fakultas**

<!-- Start of picture text -->
:<br>wns<br>«s<br>are Umummae dan iatus Peresajuan Stat KemahatwaF a nk MenampikanPersetujuanStatus afar PereigquanStat Kerahatiwann Fakulne<br>ro<br><!-- End of picture text -->

Gambar 2.8 DFD Level 2 Verifikasi dan Persetujuan Staf Kmhs Fakultas

Pada DFD Level 2 untuk proses Verifikasi dan Persetujuan Staf Kemahasiswaan Fakultas, terdapat empat sub-proses yaitu Menerima Notifikasi (5.1), Menampilkan Pengajuan Cuti (5.2), Memberikan Persetujuan (5.3), dan Menampilkan Status Persetujuan (5.4). Proses dimulai dengan notifikasi yang dikirim kepada Staf Kemahasiswaan Fakultas. Setelah menerima notifikasi, data pengajuan cuti diambil dari _data store_ dan ditampilkan kepada Staf Kemahasiswaan Fakultas untuk ditinjau. Staf Kemahasiswaan Fakultas kemudian memberikan persetujuan, yang hasilnya dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Akhirnya, status persetujuan diambil dari _data store_ dan diinformasikan kepada aktor-aktor terkait.

# **2.2.1.8 DFD Level 2 Persetujuan Fakultas**

<!-- Start of picture text -->
Fe= we<br>it<br>fe a<br>oH vom a ae<br>a=<br>a<br>__<br>e. Ld § Log Stans<br>a enn po<br>ve| Se Denia Keone<br>LH Sais Vascr Ph<br>momen EY| ‘Status Persotiuan|<br>[== |a| [—IN ion daareeter t y a ngan Romana Pre<br><!-- End of picture text -->

Gambar 2.9 DFD Level 2 Persetujuan Fakultas

Pada DFD Level 2 untuk proses Persetujuan Fakultas, terdapat empat subproses yaitu Menerima Notifikasi (6.1), Menampilkan Pengajuan Cuti & _Preview_ Surat Pengantar (6.2), Memberikan Persetujuan (6.3), dan Menampilkan Status Persetujuan (6.4). Proses dimulai dengan notifikasi persetujuan yang dikirimkan kepada Koordinator TU, Koordinator Program Studi, dan Dekan. Setelah menerima notifikasi, data pengajuan cuti diambil dari _data store_ dan ditampilkan beserta dengan _preview_ Surat Pengantar kepada Koordinator TU, Koordinator Program Studi, dan Dekan untuk ditinjau. Koordinator TU, Koordinator Program Studi, dan Dekan kemudian memberikan persetujuan, yang hasilnya dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Akhirnya, status persetujuan diambil dari _data store_ dan diinformasikan kepada aktor-aktor terkait.

**2.2.1.9 DFD Level 2 Penomoran Surat Pengantar**

<!-- Start of picture text -->
2 ——<br>2<br>—<br>“Akaderik ™<br><!-- End of picture text -->

Gambar 2.10 DFD Level 2 Penomoran Surat Pengantar

Pada DFD Level 2 untuk proses Penomoran Surat Pengantar, terdapat empat sub-proses, yaitu Menerima Notifikasi (7.1), Menampilkan Pengajuan Cuti & _Preview_ Surat Pengantar (7.2), Memberikan Nomor Surat (7.3), dan _Generate_ Surat (7.4). Proses dimulai dengan dikirimkannya notifikasi kepada Staf Kemahasiswaan Fakultas. Setelah notifikasi diterima, sistem mengambil data pengajuan cuti dari _data store_ , lalu menampilkannya bersama _preview_ Surat Pengantar yang telah ditandatangani oleh Dekan untuk ditinjau oleh Staf Kemahasiswaan Fakultas. Setelah proses peninjauan, Staf Kemahasiswaan Fakultas memberikan nomor Surat Pengantar, yang hasilnya dicatat dalam _data store_ “Pengajuan Cuti”. Kemudian, data pengajuan cuti beserta tanda tangan Dekan diambil dari _data store_ untuk digunakan dalam pembuatan Surat Pengantar. Surat yang telah dihasilkan tersebut disimpan dalam _data store_ dan dapat diakses oleh aktor-aktor terkait.

# **2.2.1.10 DFD Level 2 Persetujuan Universitas**

<!-- Start of picture text -->
|fe— regeaeeeeeeeeeeterrae<br>Swe<br>aceite<br>Se aeeaaon<br>fe)PT |<br>FFEtpons unt aan an<br>ot<br>ize(FESSPett :=<br>oto<br>=== wis ne<br>izeeeoes: fie |<br>eet<br>| hieFSS[Aart "| _—_I<br>el<br>ott<br>FESS mee |<br>Pinan<br>i ey A<br>CY er srkoresna vane» Sees<br>a etait ees on<br>k—t+<br>=a<br>[ — allFT pnrestoresre ag —_aaawre Bag Adacems<br>Koowemorty ftssh aForet KoadORT da sas Ponta—— Kor<br>[ER UAT dn<br>LH —— =<br>[ om E55 —— — _ =ea<br><!-- End of picture text -->

Gambar 2.11 DFD Level 2 Persetujuan Universitas

Pada DFD Level 2 untuk proses Persetujuan Universitas, terdapat empat subproses, yaitu Menerima Notifikasi (8.1), Menampilkan Pengajuan Cuti, Surat Pengantar, & _Preview_ Surat Keputusan Cuti (8.2), Memberikan Persetujuan (8.3), dan Menampilkan Status Persetujuan (8.4). Proses dimulai dengan pengiriman notifikasi persetujuan kepada para pejabat terkait, yaitu Kepala Bagian Akademik, Koordinator UHT dan BMN, Kepala Biro AKK, Kepala Biro Umum dan Keuangan, dan Wakil Rektor Bidang Akademik. Setelah menerima notifikasi, data pengajuan cuti dan Surat Pengantar diambil dari _data store_ dan ditampilkan beserta dengan _preview_ Surat Keputusan Cuti kepada masing-masing pejabat untuk ditinjau. Setelah meninjau, para pejabat terkait kemudian memberikan persetujuan mereka, yang hasilnya dicatat dalam _data store_ “Log Status Pengajuan Cuti”. Akhirnya, status persetujuan diambil dari _data store_ dan diinformasikan kepada aktor-aktor terkait.

**2.2.1.11 DFD Level 2 Penomoran Surat Keputusan**

<!-- Start of picture text -->
22 —<br>nasiuan Cul Surat Penganiar. 81 Pengajuan Cuti, Surat ta Pengajuan Cut & Surat Pengantar—  Pengajuan Cut<br><!-- End of picture text -->

Gambar 2.12 DFD Level 2 Penomoran Surat Keputusan

Pada DFD Level 2 untuk proses Penomoran Surat Keputusan, terdapat empat sub-proses, yaitu Menerima Notifikasi (9.1), Menampilkan Pengajuan Cuti, Surat Pengantar, & _Preview_ Surat Keputusan Cuti (9.2), Memberikan Nomor Surat (9.3), dan _Generate_ Surat (9.4). Proses dimulai dengan dikirimkannya notifikasi kepada Bagian Umum. Setelah notifikasi diterima, sistem mengambil data pengajuan cuti dan Surat Pengantar dari _data store_ , lalu menampilkannya bersama _preview_ Surat Keputusan Cuti yang telah ditandatangani oleh Wakil Rektor Bidang Akademik untuk ditinjau oleh Bagian Umum. Setelah proses peninjauan, Bagian Umum memberikan nomor Surat Keputusan Cuti, yang hasilnya dicatat dalam _data store_ “Pengajuan Cuti”. Kemudian, data pengajuan cuti beserta tanda tangan Wakil Rektor Bidang Akademik diambil dari _data store_ untuk digunakan dalam pembuatan Surat Keputusan Cuti. Surat yang telah dihasilkan tersebut disimpan dalam _data store_ dan dapat diakses oleh Bagian Umum, Staf Kemahasiswaan Fakultas, dan Mahasiswa.

# **2.2.2** **_Entity Relationship Diagram_ (ERD)**

<!-- Start of picture text -->
~On oc<br>er © <2 >) - -<br>e\/ I \e) CC . — i<br>D~ CDoO Gen AW // —_<br>‘) Ee Os = WA IG<br>Oe yop SS ae OD<br>Ae —// | \\ \ ga<br>EH - a an)<br>< ~~ OT Oo<br>SNe)<br>COQ) QJ} CO})O—<br>—fpocsS o “(emf ——()<br><!-- End of picture text -->

Gambar 2.13 ERD

_Entity-Relationship Diagram_ (ERD) digunakan untuk merancang struktur basis data dalam pengembangan sistem informasi pengajuan cuti akademik bagi mahasiswa Fakultas Ilmu Komputer UPN “Veteran” Jakarta, sehingga keterkaitan antar data dapat tergambarkan dengan jelas. ERD untuk sistem ini terdiri dari beberapa entitas, yaitu _Users_ , _Roles_ , _Permissions_ , TandaTangan, PengajuanCuti, LogStatusPengajuanCuti, dan _Notifications_ . Relasi antar entitas dapat dijelaskan sebagai berikut:

- Entitas _Users_ dan _Roles_ memiliki relasi _many-to-many_ , yang berarti satu _user_ dapat memiliki banyak _role_ , dan satu _role_ dapat dimiliki oleh banyak _user_ .

- Entitas _Roles_ dan _Permissions_ memiliki relasi _many-to-many_ , yang berarti satu _role_ dapat memiliki banyak _permission_ , dan satu _permission_ dapat dimiliki oleh banyak _role_ .

- Entitas _Users_ dan TandaTangan memiliki relasi _one-to-one_ , yang berarti satu _user_ memiliki satu data tanda tangan digital, dan satu tanda tangan hanya dimiliki oleh satu _user_ .

- Entitas _Users_ dan PengajuanCuti memiliki relasi _one-to-many_ , yang berarti satu _user_ dapat membuat banyak pengajuan cuti, tetapi satu pengajuan cuti hanya dibuat oleh satu _user_ .

- Entitas _Users_ dan LogStatusPengajuanCuti memiliki relasi _one-to-many_ , yang berarti satu _user_ dapat memiliki banyak log status pengajuan, tetapi satu log status hanya dimiliki oleh satu _user_ .

- Entitas _Users_ dan _Notifications_ memiliki relasi _one-to-many_ , yang berarti satu _user_ dapat memiliki banyak notifikasi, tetapi satu notifikasi hanya dimiliki oleh satu _user_ .

- Entitas PengajuanCuti dan LogStatusPengajuanCuti memiliki relasi _one-tomany_ , yang berarti satu pengajuan cuti dapat memiliki banyak log status, tetapi satu log status hanya dimiliki oleh satu pengajuan cuti.

# **2.3 Rancangan Proyek**

# **2.3.1** **_Need Analysis User Interface_ dan** **_User Experience_**

Analisis kebutuhan antarmuka pengguna ( _User Interface_ ) dan pengalaman pengguna ( _User Experience_ ) dilakukan untuk memastikan sistem informasi pengajuan cuti akademik berbasis web dapat digunakan secara optimal oleh seluruh pengguna. Analisis ini bertujuan untuk mengidentifikasi elemen visual dan interaktif yang diperlukan dalam antarmuka serta merancang alur penggunaan yang efisien, mudah dipahami, dan sesuai dengan kebutuhan pengguna sistem.

# **2.3.1.1** **_Need Analysis User Interface_**

_User Interface_ (UI) merupakan bagian dari sistem yang menjadi titik interaksi langsung antara pengguna dengan aplikasi. Analisis kebutuhan UI dilakukan untuk merancang elemen-elemen antarmuka yang tidak hanya fungsional dan informatif, tetapi juga mendukung kemudahan penggunaan dan konsistensi tampilan. Tabel 2.2 menyajikan analisis kebutuhan komponen _user interface_ .

Tabel 2.2 _Need Analysis User Interface_

|**No.**|**Komponen UI**|**Fungsi**|**Desain yang**<br>**Dibutuhkan**|**Cont**<br>**Impleme**|**oh**<br>**ntasi**|
|---|---|---|---|---|---|
|1.|Tombol|Menjalankan<br>aksi<br>tertentu<br>seperti<br>menyetujui,<br>menolak,<br>menyimpan, dan<br>lainnya.|Desain<br>konsisten,<br>dengan<br>warna<br>sesuai makna.|Tombol<br>“Setujui”<br>berwarna<br>tombol “<br>berwarna|hijau,<br>Tolak”<br>merah.|
|2.|_Badge_Status|Menampilkan<br>status pengajuan<br>cuti<br>secara<br>visual<br>dan<br>informatif.|Warna<br>yang<br>membedakan<br>setiap<br>status<br>dengan<br>konsisten.|_Badge_ber<br>abu-abu<br>status<br>”Menungg<br>hijau bila<br>”Disetujui<br>merah bila<br>”Ditolak”.|warna<br>bila<br>masih<br>u”,<br>status<br>”, dan<br>status<br>|
|3.|Formulir|Media input data<br>pengajuan cuti.|Terdiri atas field<br>isian yang rapi<br>dan<br>jelas,<br>dilengkapi<br>validasi<br>input<br>serta_dropdown_<br>untuk<br>pilihan<br>tetap.|Formulir<br>pengajuan<br>dengan<br>teks,_drop_<br>dan<br>ung<br>file.|<br>cuti<br>input<br>_down_,<br>gahan|
|4.|Tabel|Menyajikan data<br>dalam<br>bentuk<br>terstruktur agar|_Header_<br>jelas,<br>terdapat<br>fitur<br>pencarian<br>dan<br>_filter_.|Tabel<br>pengajuan<br>yang terdi<br>kolom No|data<br> <br>cuti<br>ri atas<br>, NIM,|

|||mudah<br>dibaca<br>dan dikelola.||Nama, Program<br>Studi,<br>Tanggal<br>Pengajuan,<br>Periode<br>Akademik,<br>Semester,<br>Status, dan Aksi,<br>serta dilengkapi<br>fitur<br>_filter_<br>berdasarkan<br>semester<br>dan<br>periode<br>akademik.|
|---|---|---|---|---|
|5.|_Navbar_|Menyediakan<br>menu<br>navigasi<br>antar<br>halaman<br>dalam sistem.|Menampilkan<br>menu yang aktif<br>dengan penanda<br>visual, ikon, dan<br>teks deskriptif.|_Navbar_<br>berisi<br>menu<br>“_Dashboard_”,<br>“Pengajuan<br>Cuti”, notifikasi<br>dengan<br>ikon<br>bell, dan profil<br>dengan<br>ikon<br>orang.|
|6.|_Dashboard_<br>_Card_|Menampilkan<br>jumlah data cuti<br>yang<br>sedang<br>diproses,<br>disetujui,<br>dan<br>ditolak.|Warna dan ikon<br>berbeda<br>untuk<br>tiap<br>kategori,<br>jumlah<br>data<br>tertera jelas.|Kartu ringkasan<br>jumlah<br>cuti<br>“Diproses”,<br>“Disetujui”, dan<br>“Ditolak”|
|7.|Grafik|Menyajikan<br>visualisasi data<br>untuk|Grafik<br>batang<br>dan grafik garis|Grafik<br>jumlah<br>mahasiswa cuti|

|||mendukung<br>pemantauan dan<br>analisis.|dengan<br>label<br>yang jelas.|per<br>pro<br>studi.|gram|
|---|---|---|---|---|---|
|8.|_Modal_(_Pop-up_)|Menampilkan<br>formulir<br>tambahan<br>atau<br>dialog<br>konfirmasi.|Muncul<br>di<br>tengah<br>layar,<br>fokus<br>ke<br>isi,<br>dengan tombol<br>aksi yang jelas.|Modal<br> <br>menambah<br>mengubah<br>pengguna,<br>konfirmasi<br>persetujuan<br>pengisian a<br>penolakan.|untuk<br>atau<br>data<br>, dan<br>lasan<br>|

# **2.3.1.2** **_Need Analysis User Interface_**

_User Experience_ (UX) berfokus pada bagaimana pengalaman keseluruhan pengguna saat berinteraksi dengan sistem, mencakup aspek kenyamanan, kemudahan, serta kepuasan pengguna dalam menjalankan tugas-tugasnya. Analisis kebutuhan UX dilakukan untuk memastikan bahwa sistem pengajuan cuti akademik berbasis web tidak hanya berfungsi dengan baik, tetapi juga memberikan pengalaman penggunaan yang intuitif dan efisien. Tabel 2.3 menyajikan analisis kebutuhan komponen _user experience_ .

Tabel 2.3 _Need Analysis User Experience_

|**No.**|**Komponen UX**|**Tujuan**|**Kebutuhan**<br>**Pengguna**|**Desain**<br>**Pengalaman**<br>**yang**|
|---|---|---|---|---|
|||||**Diusulkan**|
|1.|Navigasi Sistem|Mempermudah<br>pengguna<br>berpindah<br>antar|Pengguna dapat<br>dengan mudah<br>menemukan|Navbar dengan<br>ikon dan label<br>teks konsisten,|
|||halaman dan fitur|fitur<br>seperti|indikator menu|
|||utama.|_dashboard_,|aktif, dan tata|

||||pengajuan<br>cuti<br>dan<br>profil<br>pengguna.|letak<br>familiar.|yang|
|---|---|---|---|---|---|
|2.|Konsistensi<br>Antar Halaman|Membantu<br>pengguna<br>memahami pola<br>interaksi<br>dan<br>tampilan<br>tanpa<br>harus<br>belajar<br>ulang di setiap<br>halaman.|Pengguna<br>menginginkan<br>elemen<br>antarmuka<br>seperti tombol,<br>warna<br>status,<br>dan_layout_yang<br>konsisten<br>di<br>semua halaman.|Menggun<br>_layout_,<br>tombol,<br>dan<br>tampilan<br>seragam<br>seluruh si|akan<br>warna<br>ikon,<br>gaya<br>yang<br>di<br>stem.|
|3.|Alur Pengajuan<br>Cuti|Memastikan<br>proses pengajuan<br>cuti<br>mudah<br>dipahami<br>dan<br>tidak<br>membingungkan.|Pengguna<br>membutuhkan<br>alur yang jelas<br>mulai dari awal<br>hingga<br>pengajuan<br>selesai.|Alur<br>d<br>secara<br>berurutan,<br>dengan<br>indikator<br>tahapan<br>sedang dij|isusun<br> <br>yang<br>alani.|

# **2.3.2** **_Desain User Interface_**

Perancangan tampilan _user interface_ dilakukan sebagai langkah awal untuk menggambarkan tampilan sistem secara visual sebelum memasuki tahap pembangunan sistem. Dalam proses perancangannya, peneliti menggunakan aplikasi Figma sebagai media desain antarmuka. Adapun rancangan tampilan antarmuka sistem informasi pengajuan cuti akademik adalah sebagai berikut.

# **2.3.2.1 Halaman** **_Login_**

Gambar 2.14 Halaman _Login_

Pada halaman _login_ , pengguna diminta untuk memasukkan _username_ dan _password_ mereka untuk mengakses sistem. Setelah mengisi kolom yang tersedia, pengguna dapat mengklik tombol “ _Login_ ” untuk melanjutkan proses.

# **2.3.2.2 Halaman** **_Dashboard_**

<!-- Start of picture text -->
DASHBOARD<br>TRACKING<br>STATUS PENGAJUAN<br>© meinggteeendeenre<br>© _serungg verte etamahalonoanoboe<br>© _terungputenetvenKoornterTs<br>©<br>seningguPsrenivoneerdnetorrot<br>© _MenungguPenendatangananSurat Pengantar oleh Dekon<br>© _teeungguPenemeran<br>tre Pengertr sh et amahasowoan Fon<br>© semingguPeeetiion<br>kag Akademi<br>© _wenungguPwsetsvon<br>oor UT SonBun<br>© temungguPeeetiion<br>kareAk<br>© | teungguPeteifonKare Umum denKevengen<br>© _tenunggutenandctengenenfret Pengontr sh Won eng Akademi<br>© _teungguPenemeran<br>fret Keputven le glen Umum<br>© sete<br><!-- End of picture text -->

Gambar 2.15 Halaman _Dashboard_ Mahasiswa

Pada halaman _dashboard_ mahasiswa, terdapat informasi mengenai jumlah pengajuan cuti yang sedang diproses, disetujui, dan ditolak. Selain itu, mahasiswa dapat melihat status pengajuan cuti terbaru yang sedang berjalan, sehingga mereka dapat memantau progres pengajuan cuti yang terakhir diajukan.

<!-- Start of picture text -->
DASHBOARD:<br>Bi: °<br>nn Pengen coer Stn Tan 2028<br>———<br>——<br>nt Pengen ot treet Aan on 2038<br>Perma yan Sap Ban Tn 2025<br>»/ ¥<br>Parte Laan et Ph Tan 2028<br>TL<br>_—_—<br>ey<br>—<br>—_————<br><!-- End of picture text -->

Gambar 2.16 Halaman _Dashboard_ Dosen/Pegawai

Pada halaman _dashboard_ dosen atau pegawai, ditampilkan informasi mengenai jumlah pengajuan cuti yang belum diproses dan yang sudah diproses. Selain itu, terdapat beberapa grafik yang berfungsi untuk membantu memantau dan menganalisis data pengajuan cuti. Grafik-grafik tersebut mencakup jumlah pengajuan cuti berdasarkan status dan alasan di tahun berjalan, jumlah mahasiswa yang cuti per program studi, performa layanan setiap bulan, serta performa layanan dari setiap pihak yang terlibat dalam proses persetujuan.

<!-- Start of picture text -->
DASHBOARD<br>100 20 40<br>ma Pongsn Cut tarasran Stata Tah 2025<br>VV<br>en<br>—— ST<br>|<br>a<br>eee<br>mia oogun Cut BeraasrkanAsan Tan 2025<br>_Aman Maasiws Cu Pe Poa saanoney<br>Performa ayanan Seip Bln Tatun 2025<br>Vi. aN A ~ <<br>PertormaLayann<br>ety Pn Tatu 2025<br>TS<br>sd<br>—<$<br>—$<br><!-- End of picture text -->

Gambar 2.17 Halaman _Dashboard_ Super Admin

Pada halaman _dashboard_ super admin, terdapat informasi mengenai total _user_ aktif, total _role_ , dan total _permission_ . Selain itu, terdapat beberapa grafik yang berfungsi untuk membantu memantau dan menganalisis data pengajuan cuti. Grafik-grafik tersebut mencakup jumlah pengajuan cuti berdasarkan status dan alasan di tahun berjalan, jumlah mahasiswa yang cuti per program studi, performa layanan setiap bulan, serta performa layanan dari setiap pihak yang terlibat dalam proses persetujuan.

# **2.3.2.3 Halaman Buat Pengajuan Cuti**

<!-- Start of picture text -->
FORM PENGAJUAN CUTI AKADEMIK MAHASISWA<br>eta Mosnwe DotarengojvanCat<br>sere tego Sea ser resort .<br>anaornod Sevoma eran rv aon ct .<br>serpato stra Dokumen endukung<br>rope ionr ‘enoveie 204 EE<br>sons oupon — ‘rotnennjvoncarg<br>senstnene socratojron sonata 6 ator ia Cheetachoosen Whenote chonenchon<br>stoptunesmenboyran<br>tat lausrsoeretexenupcelt Chotefin_ Hote chon<br><!-- End of picture text -->

Gambar 2.18 Halaman Buat Pengajuan Cuti

Pada halaman buat pengajuan cuti, terdapat form pengajuan cuti akademik dimana mahasiswa diminta untuk melengkapi data yang diperlukan guna mengajukan cuti. Data mahasiswa seperti NIM, nama lengkap, program studi, tempat dan tanggal lahir, nomor telepon, alamat rumah, _email_ , serta pembimbing akademik akan terisi secara otomatis oleh sistem, kecuali pada kolom nama orang tua yang perlu diisi secara manual. Selanjutnya, mahasiswa diminta mengisi data pengajuan cuti, yang mencakup periode tahun akademik, semester (ganjil atau genap), serta alasan cuti. Pada bagian akhir, mahasiswa diwajibkan mengunggah dokumen pendukung berupa surat persetujuan orang tua, KHS terbaru, rekap pelunasan pembayaran, dan bukti bayar semester. Tersedia tombol “Surat Persetujuan Orang Tua” yang dapat digunakan mahasiswa untuk mengunduh surat

persetujuan, mencetaknya, dan meminta tanda tangan orang tua sebelum diunggah kembali ke sistem sebagai dokumen pendukung.  Terdapat tombol “Batal” yang berfungsi untuk menghapus seluruh isian dalam formulir, dan tombol “Submit” yang digunakan untuk mengirimkan pengajuan cuti ke sistem setelah seluruh data telah lengkap.

# **2.3.2.4 Halaman Detail Pengajuan Cuti**

<!-- Start of picture text -->
© Detail Pengajuan Cuti<br>FORM PENGAJUAN CUTI AKADEMIK MAHASISWA<br>ota Monasewe otarengojvenCut<br>= rauserv0 ro t onea a t orse 28/38<br>snontno Seder seanct —<br>secoptenr ——— arent .<br>snonatnsnen carang as taoperonson tte by sree : 7<br>nat lasosoermosenoupnocls<br>rertineing Haden aoa<br>TRACKING<br>STATUS PENGAJUAN<br>© serungguPesetsjvan<br>Dosen PA<br>© erunggu verte! Stet KemahasiawaonFekatos<br>© _ wronunggu Persetujuan Keordinator TU<br>© HorungguPorsetjvonKeorintar<br>rot<br>© terungguPenandctangananSurat Pengantar ssh Deka<br>© _ Menungge Penemoran Surat Pengentar oleh Stat Kemahasiswoen Fakuttas<br>© HerungguPersetjzan<br>Kobog Akademi<br>© werungguPersetuon<br>Koon. NT don OM<br>© serunggurereetsjuonKoro Axx<br>© HerungguPorsetjuan<br>Koro Umum dan Kevengan<br>© serungguPenandatongananSurat Keputusan lah WarekBidang Akademi<br>© _ tterungguPenemorensurat Keputusan oleh Bagion Unum<br>© seiesai<br><!-- End of picture text -->

Gambar 2.19 Halaman Detail Pengajuan Cuti

Pada halaman detail pengajuan cuti terdapat form pengajuan cuti yang datanya telah diisi sebelumnya. Halaman ini juga menampilkan _tracking_ status

pengajuan, sehingga alur dan perkembangan dari pengajuan cuti dapat diketahui dengan jelas.

**2.3.2.5 Halaman Data Pengajuan Cuti**

<!-- Start of picture text -->
DATA PENGAJUAN CUTI AKADEMIK MAHASISWA<br>1 234867800 than omesSinfonotio 10-06-2008 2028/2028 cont ITY oe8o<br><!-- End of picture text -->

Gambar 2.20 Halaman Data Pengajuan Cuti Pemberi Persetujuan

Pada halaman data pengajuan cuti pemberi persetujuan ditampilkan tabel berisi informasi seperti nomor, NIM, nama mahasiswa, program studi, tanggal pengajuan, periode akademik, semester, status, dan aksi. Kolom status menunjukkan bahwa pengajuan masih menunggu persetujuan dari pihak terkait.

Kolom aksi memuat tombol yang disesuaikan dengan tahapan proses. Tombol kuning (ikon mata) digunakan untuk melihat detail pengajuan, dan tombol hijau (ikon pena) untuk memberikan persetujuan yang hanya muncul jika status pengajuan masih menunggu persetujuan dan akan hilang setelah disetujui.

Tersedia pula tombol biru muda (ikon dokumen) untuk melihat Surat Pengantar, mulai ditampilkan sejak tahap persetujuan Koordinator TU. Sedangkan tombol biru tua untuk melihat Surat Keputusan hanya muncul saat pengajuan telah mencapai tahap persetujuan Kepala Bagian Akademik. Halaman ini juga dilengkapi fitur pencarian dan _filter_ berdasarkan periode akademik dan semester.

<!-- Start of picture text -->
enema ten x<br>seit agsren<br>Ea<br><!-- End of picture text -->

Gambar 2.21 _Pop-Up_ Konfirmasi Persetujuan

Pada _pop-up_ konfirmasi persetujuan, pengguna akan ditanya apakah yakin ingin menyetujui pengajuan tersebut. Tersedia dua tombol yaitu ”Tolak” dan ”Setujui”. Jika memilih ”Tolak”, akan muncul _pop-up_ lanjutan untuk mengisi alasan penolakan. Jika memilih ”Setujui”, maka pengajuan akan langsung disetujui dan status akan diperbarui.

<!-- Start of picture text -->
‘net P<br>seniortoot<br>[r= a)<br><!-- End of picture text -->

Gambar 2.22 _Pop-Up_ Tujuan Surat

Pada _pop-up_ tujuan surat, pengguna diminta untuk mengisi pihak atau instansi tujuan dari Surat Pengantar. _Pop-up_ ini akan muncul setelah Staf Kemahasiswaan

Fakultas menekan tombol “Setujui” pada tahap verifikasi pengajuan cuti. Setelah tujuan diisi, pengguna dapat menekan tombol ”Simpan” untuk menyimpan data dan menyetujui pengajuan, atau tombol ”Batal” untuk menutup _pop-up_ tanpa menyimpan dan membatalkan proses persetujuan.

<!-- Start of picture text -->
ete ent x<br>sotaeraepeeanindenmri pera<br>a) =")<br><!-- End of picture text -->

Gambar 2.23 _Pop-Up_ Berikan Alasan Penolakan

Pada _pop-up_ berikan alasan penolakan, pengguna diminta untuk mengisi alasan mengapa pengajuan ditolak. Terdapat dua tombol ”Kembali” untuk membatalkan penolakan, dan ”Tolak” untuk menyimpan alasan yang telah diisi sekaligus menetapkan status pengajuan menjadi ditolak.

<!-- Start of picture text -->
DATA PENGAJUAN CUTI AKADEMIK MAHASISWA<br>1 234867800 hon Jomes —Siinlommetko 0-06-2005 sie ont TT ooso<br><!-- End of picture text -->

Gambar 2.24 Halaman Data Pengajuan Cuti Pemberi Nomor Surat

Pada halaman data pengajuan cuti pemberi nomor surat ditampilkan tabel berisi informasi seperti nomor, NIM, nama mahasiswa, program studi, tanggal pengajuan, periode akademik, semester, status, dan aksi. Kolom status menunjukkan bahwa pengajuan telah memasuki tahap pemberian nomor oleh pihak terkait.

Kolom aksi menampilkan tombol sesuai peran dan tahapan proses. Tombol kuning (ikon mata) digunakan untuk melihat detail pengajuan. Tombol hijau (ikon pena) digunakan untuk memberikan nomor surat, dan hanya muncul jika status pengajuan masih menunggu pemberian nomor. Untuk Staf Kemahasiswaan Fakultas, tombol ini digunakan untuk memberi nomor Surat Pengantar, sementara Bagian Umum menggunakannya untuk Surat Keputusan.

Tersedia pula tombol biru muda (ikon dokumen) untuk melihat Surat Pengantar, yang muncul sejak tahap persetujuan Koordinator TU hingga akhir, serta tombol biru tua untuk melihat Surat Keputusan yang tampil setelah persetujuan dari Kepala Bagian Akademik. Halaman ini dilengkapi fitur pencarian dan _filter_ berdasarkan periode akademik dan semester. Khusus untuk Staf Kemahasiswaan Fakultas, tersedia juga fitur ekspor data ke format CSV atau XLS untuk mempermudah dokumentasi dan pengolahan data.

Gambar 2.25 _Pop-Up_ Berikan Nomor Surat

Pada _pop-up_ berikan nomor surat, pengguna diminta untuk mengisi nomor surat sesuai dengan perannya. Staf Kemahasiswaan Fakultas mengisikan nomor untuk Surat Pengantar, sedangkan Bagian Umum mengisikan nomor untuk Surat Keputusan. Pengguna dapat menekan tombol ”Simpan” untuk menyimpan nomor surat, atau tombol ”Batal” untuk membatalkan pemberian nomor surat dan menutup _pop-up_ .

<!-- Start of picture text -->
DATA PROSES PENGAJUAN<br>teen [Bi ternenteUTI tetera © Peon»|<br>1 tuuse7e80 ron ores Stiveratta 08-2028 74/70 cont oso<br>osnttnonne rom i<br><!-- End of picture text -->

Gambar 2.26 Halaman Data Pengajuan Cuti Final

Pada halaman data pengajuan cuti final ditampilkan tabel berisi informasi penting seperti nomor, NIM, nama mahasiswa, program studi, tanggal pengajuan, periode akademik, semester, status pengajuan, dan aksi. Status ditampilkan sebagai _badge_ hijau bertuliskan ”Disetujui”, menandakan bahwa pengajuan telah selesai diproses.

Kolom aksi menampilkan tiga tombol sesuai peran pengguna. Tombol kuning dengan ikon mata digunakan untuk melihat detail pengajuan. Tombol biru muda dengan ikon dokumen menampilkan Surat Pengantar, hanya tersedia untuk akun Staf Kemahasiswaan Fakultas dan Bagian Umum. Sementara tombol biru tua dengan ikon dokumen untuk melihat Surat Keputusan, tersedia pada akun Mahasiswa, Staf Kemahasiswaan Fakultas, dan Bagian Umum. Karena proses telah selesai, tidak terdapat tombol hijau untuk persetujuan atau pemberian nomor surat.

Halaman ini juga dilengkapi fitur pencarian serta _filter_ berdasarkan periode akademik dan semester. Khusus bagi Staf Kemahasiswaan Fakultas, tersedia fitur ekspor data ke format CSV atau XLS untuk memudahkan pengolahan dan dokumentasi.

# **2.3.2.6 Halaman Data** **_User_**

<!-- Start of picture text -->
— oo<br>4 sero iotamaiten ettacnoinoen ag ea<br>a Oe) ao<br><!-- End of picture text -->

Gambar 2.27 Halaman Data _User_

Pada halaman data _user_ , ditampilkan tabel yang memuat informasi berupa nomor, _username_ , nama, role, status, dan kolom aksi. Pada kolom aksi, terdapat

tombol hijau dengan ikon pena untuk mengubah data _user_ , serta tombol merah dengan ikon tempat sampah untuk menghapus data _user_ . Halaman ini juga dilengkapi dengan fitur pencarian untuk memudahkan pengguna menemukan _user_ tertentu, serta tombol ”Tambah _User_ ” yang digunakan untuk menambahkan data _user_ baru.

<!-- Start of picture text -->
ete woroeews<br>om<br>oc<br><!-- End of picture text -->

Gambar 2.28 Tambah _User_

Pada _pop-up_ tambah _user_ , pengguna diminta untuk memilih tipe _user_ , lalu mengisi data seperti nama, _username_ , _email_ , _password_ , dan konfirmasi _password_ . Selain itu, tersedia daftar _checkbox_ untuk memilih _role_ yang sesuai, serta opsi status akun (aktif atau non-aktif). Setelah semua data diisi, pengguna dapat menekan tombol “Simpan” untuk menambahkan _user_ ke sistem, atau tombol “Batal” untuk menutup _pop-up_ tanpa menambahkan data.

<!-- Start of picture text -->
anuser x<br>‘erat<br>mot<br>“anynaoyxegratcon<br>onnton oberon merain<br>Super hain Monasiona<br>1BDosen Koornaor  PA 1 ‘sol cemahosoonFaeutos<br>ote<br>0Nonaitat<br><!-- End of picture text -->

Gambar 2.29 _Edit User_

Pada _pop-up edit user_ , pengguna dapat mengubah informasi seperti _username_ , nama, _email_ , dan _password_ (jika diperlukan). _Role_ ditampilkan dalam bentuk _checkbox_ untuk menyesuaikan peran pengguna, serta tersedia opsi status akun (aktif atau non-aktif). Setelah melakukan perubahan, pengguna dapat menekan tombol ”Simpan” untuk menyimpan perubahan, atau tombol ”Batal” untuk menutup _pop-up_ tanpa menyimpan perubahan.

<!-- Start of picture text -->
Kendemasivopun x<br>‘Apatoh Anda yin ing menghopus datani?<br><!-- End of picture text -->

Gambar 2.30 _Delete User_

Pada _pop-up_ konfirmasi hapus, pengguna diminta memastikan apakah data benar-benar ingin dihapus. Tersedia tombol ”Tidak” untuk membatalkan penghapusan dan menutup _pop-up_ , serta tombol ”Ya” untuk menghapus data secara permanen.

# **2.3.2.7 Halaman Data** **_Role_**

<!-- Start of picture text -->
DATAROLE<br>1 pers rronoge ve menoge codon ven. peroon.<br>2 wotavina vier_s0.pengsuon cneecao.paroouon vew.nx- 9 ED<br>2 comma veo. genasion cero otn.20 a<br>4 attain ion. ct0_pengsion pp tte.Ststn ou.<br><!-- End of picture text -->

Gambar 2.31 Halaman Data _Role_

Pada halaman data role, ditampilkan tabel yang memuat informasi berupa nomor, nama role, daftar _permissions_ yang dimiliki, dan kolom aksi. Pada kolom aksi, terdapat tombol hijau dengan ikon pena untuk mengubah data, serta tombol merah dengan ikon tempat sampah untuk menghapus data. Halaman ini juga dilengkapi dengan fitur pencarian untuk memudahkan pengguna menemukan _role_ tertentu, serta tombol ”Tambah _Role_ ” yang digunakan untuk menambahkan data _role_ baru.

<!-- Start of picture text -->
‘Tembah Role x<br>ara Role<br>manage usar menage kadai<br>‘Ye cate pengaluon reat data_pengaivon<br>Vien srot_pengortar ‘approve stt_kenhsfohustas<br>‘approve coven pa ‘opprove hoor<br>‘en sot beputuson<br><!-- End of picture text -->

Gambar 2.32 _Pop-Up_ Tambah _Role_

Pada _pop-up_ tambah _role_ , pengguna diminta untuk mengisi nama _role_ dan memilih hak akses ( _permissions_ ) yang relevan melalui daftar _checkbox_ . Setelah semua data terisi, pengguna dapat menekan tombol ”Simpan” untuk menambahkan _role_ ke sistem, atau tombol ”Batal” untuk menutup _pop-up_ tanpa menambahkan data.

<!-- Start of picture text -->
eltRole x<br>Nome tele<br>Bi1BPermiesions| view. viewsurot_pongantormaroge-userdota_pengojuen -manege-atodericreate‘opprove cata_pengaionstot kms tatutor<br>surat_keputuson<br>‘pprove.or0now pa 1 epprove.toord.ta<br><!-- End of picture text -->

Gambar 2.33 _Pop-Up Edit Role_

Pada _pop-up edit role_ , nama _role_ dapat diubah dan diatur hak aksesnya. Daftar _permissions_ ditampilkan dalam bentuk _checkbox_ yang dapat dicentang sesuai

kebutuhan. Tersedia tombol “Batal” untuk menutup _pop-up_ tanpa menyimpan perubahan, dan tombol “Simpan” untuk menyimpan perubahan yang telah dilakukan.

<!-- Start of picture text -->
senmeiepn x<br>spacoecyanihmergape<br>coche<br>St<br><!-- End of picture text -->

Gambar 2.34 _Pop-Up_ Konfirmasi Hapus

Pada _pop-up_ konfirmasi hapus, pengguna diminta memastikan apakah data benar-benar ingin dihapus. Tersedia tombol ”Tidak” untuk membatalkan penghapusan dan menutup _pop-up_ , serta tombol ”Ya” untuk menghapus data secara permanen.

# **2.3.2.8 Halaman Data** **_Permission_**

<!-- Start of picture text -->
DaraPenmision<br>— a ==<br>neo Perna oa<br>2 managestodern siesta meng doa chasers eo<br>2 nce pargeon nsx snot aaparent ea<br>4 create_date_pengajuon Ake unti& mernbuat pengapran cst ea<br>5 ews. pongonor aorta iminetaonmindomiont secre.<br>gp ttie oman aa<br>2 gpm tn sua stsssimonenrtasannewnne<br>® approve_koord_tu esos unt. staf eordnator ty member approKa ea<br>© esr seputson meres mnatconmsomina necransoonsn. EY<br><!-- End of picture text -->

Gambar 2.35 Halaman Data _Permission_

Pada halaman data _permission_ , ditampilkan tabel yang memuat informasi berupa nomor, nama _permission_ , keterangan, dan aksi. Pada kolom aksi, terdapat tombol hijau dengan ikon pena untuk mengubah data, serta tombol merah dengan ikon tempat sampah untuk menghapus data. Halaman ini juga dilengkapi dengan fitur pencarian untuk memudahkan pengguna menemukan _permission_ tertentu, serta tombol ”Tambah _Permission_ ” yang digunakan untuk menambahkan data _permission_ baru.

<!-- Start of picture text -->
‘ea omen x<br>toma henna<br>ttwoson<br><!-- End of picture text -->

Gambar 2.36 _Pop-Up_ Tambah _Permission_

Pada _pop-up_ tambah _permission_ , pengguna diminta untuk mengisi nama _permission_ dan keterangannya. Setelah data diisi, pengguna dapat menekan tombol ”Simpan” untuk menambahkan _permission_ ke sistem, atau tombol ”Batal” untuk menutup _pop-up_ tanpa menambahkan data.

<!-- Start of picture text -->
at Permieson x<br>Noma Permission<br>ow sutat_koputuson<br>koterongon-Akaos unt metat dan mendowmicad swat kept ct<br><!-- End of picture text -->

Gambar 2.37 _Pop-Up Edit Permission_

Pada _pop-up edit permission_ , pengguna dapat mengubah nama _permission_ dan keterangan yang menjelaskan fungsinya. Tersedia tombol “Batal” untuk menutup _pop-up_ tanpa menyimpan perubahan, serta tombol “Simpan” untuk menyimpan perubahan yang telah dilakukan.

<!-- Start of picture text -->
erties pe x<br>soar nya ngmergpopict<br>ees] =)<br><!-- End of picture text -->

Gambar 2.38 _Pop-Up_ Konfirmasi Hapus

Pada _pop-up_ konfirmasi hapus, pengguna diminta memastikan apakah data benar-benar ingin dihapus. Tersedia tombol ”Tidak” untuk membatalkan penghapusan dan menutup _pop-up_ , serta tombol ”Ya” untuk menghapus data secara permanen.

# **2.3.2.9 Halaman Data Prodi**

<!-- Start of picture text -->
Dara proot<br>—) @<br>GS<br><!-- End of picture text -->

Gambar 2.39 Halaman Data Prodi

Pada halaman data prodi, ditampilkan tabel yang memuat informasi berupa nomor, nama program studi, dan nama koordinator program studi. Halaman ini juga

dilengkapi dengan fitur pencarian untuk memudahkan pengguna dalam menemukan data prodi tertentu.

**2.3.2.10 Halaman Data Cuti Mahasiswa**

<!-- Start of picture text -->
DATACUTIMAHASISWA<br>femomes —-¥—ainatoasomnap Search [<br>1 maton ey ‘ute hormoss—anneanas np<br>2 Wye vasseret tomate naj noe<br>4 acts vaseraca sieetemitomoss ——anaanas ccna<br>8 ovansock vasseraee fiettemitomas ——anneanas ap<br><!-- End of picture text -->

Gambar 2.40 Halaman Data Cuti Mahasiswa

Pada halaman data cuti mahasiswa, ditampilkan tabel yang memuat informasi berupa nomor, nama mahasiswa, NIM, program studi, periode akademik, dan semester. Halaman ini dilengkapi dengan fitur pencarian serta _filter_ berdasarkan program studi dan periode akademik untuk memudahkan pengguna dalam menemukan data pengajuan cuti tertentu.

# **2.3.2.11 Halaman Data Mahasiswa**

<!-- Start of picture text -->
DATAMAHASISWA,<br>eae ¥) (sr f@<br>ry ‘cnvenorgen| ‘meter aman<br>rowing oot ents rious vee<br><!-- End of picture text -->

Gambar 2.41 Halaman Data Mahasiswa

Pada halaman data mahasiswa, ditampilkan tabel yang memuat informasi berupa nomor, NIM, nama mahasiswa, dan program studi. Halaman ini juga dilengkapi dengan fitur pencarian serta _filter_ berdasarkan tahun angkatan untuk memudahkan pengguna dalam menemukan data mahasiswa tertentu.

# **2.3.2.12 Halaman Data Dosen**

<!-- Start of picture text -->
DATADOSEN<br>ngNo Bo roe renei sx<br><!-- End of picture text -->

Gambar 2.42 Halaman Data Dosen

Pada halaman data dosen, ditampilkan tabel yang memuat informasi berupa nomor, NIDN, dan nama dosen. Halaman ini juga dilengkapi dengan fitur pencarian untuk memudahkan pengguna dalam menemukan data dosen tertentu.

**2.3.2.13 Halaman Data Pegawai**

<!-- Start of picture text -->
DATAPEGAWAI<br>1 sserana2 —Diotaraston —FakutortruKonpnter Tenaga Kependion<br>2° sasemeoe —aniotma —FatutontruKomputer coven ota eto<br>owing Notre rouse<br><!-- End of picture text -->

Gambar 2.43 Halaman Data Pegawai

Pada halaman data pegawai, ditampilkan tabel yang memuat informasi berupa nomor, NIP, nama pegawai, unit kerja, tipe pegawai, dan jabatan. Halaman ini juga dilengkapi dengan fitur pencarian untuk memudahkan pengguna dalam menemukan data pegawai tertentu.

# **2.3.2.14 Halaman Notifikasi**

<!-- Start of picture text -->
Pengojuon cut baru dar Ethan James. o<br><!-- End of picture text -->

Gambar 2.44 Halaman Notifikasi

Pada halaman notifikasi, terdapat seluruh notifikasi yang diterima oleh pengguna. Tersedia tombol ”Tandai Semua Dibaca” untuk memudahkan pengguna dalam menandai semua notifikasi sebagai telah dibaca.

# **2.3.2.15 Halaman Tanda Tangan Digital**

<!-- Start of picture text -->
‘TANDA TANGAN DIGITAL<br>onda Tongan Soya ‘0 fonda ongon<br><!-- End of picture text -->

Gambar 2.45 Halaman Tanda Tangan Digital

Pada halaman tanda tangan digital, pengguna dapat melihat dua bagian utama, yaitu “Tanda Tangan Saya” di sisi kiri dan “Buat Tanda Tangan” di sisi kanan. Pada

bagian “Tanda Tangan Saya”, apabila pengguna belum pernah membuat tanda tangan digital sebelumnya, akan ditampilkan keterangan “Anda belum memiliki tanda tangan”. Sementara itu, pada bagian “Buat Tanda Tangan”, tersedia kanvas yang dapat digunakan untuk menggambar tanda tangan secara manual. Jika tombol “Hapus” diklik, maka kanvas akan dikosongkan sehingga pengguna dapat menggambar ulang tanda tangan. Setelah selesai, pengguna dapat menekan tombol “Simpan” untuk menyimpan hasil tanda tangan tersebut. Tanda tangan yang telah disimpan kemudian akan ditampilkan dalam bentuk gambar pada bagian “Tanda Tangan Saya”.

# **2.3.2.16 Halaman Profil**

<!-- Start of picture text -->
prone<br>voters<br>tonsansp<br>—<br>ay<br>Ca<br>Sa SST<br>SS SN SOTO)<br><!-- End of picture text -->

Gambar 2.46 Halaman Profil Mahasiswa

Pada halaman profil mahasiswa, terdapat informasi terkait data diri mahasiswa, seperti nama lengkap, NIM, program studi, tempat lahir, tanggal lahir, _email_ , nomor telepon, dan alamat.

<!-- Start of picture text -->
prom<br>aaa<br><!-- End of picture text -->

Gambar 2.47 Halaman Profil Dosen

Pada halaman profil mahasiswa, terdapat informasi terkait data diri dosen, seperti nama lengkap, NIDN, dan _email_ .

<!-- Start of picture text -->
prom<br>_—<br><!-- End of picture text -->

Gambar 2.48 Halaman Profil Pegawai

Pada halaman profil pegawai, terdapat informasi terkait data diri pegawai, seperti nama lengkap, NIP, dan _email_ .

<!-- Start of picture text -->
vn<br>—<br><!-- End of picture text -->

Gambar 2.49 Halaman Profil Super Admin

Pada halaman profil super admin, terdapat informasi terkait data diri super admin, seperti nama lengkap dan _email_ .

# **2.4 Rencana Pengujian Proyek**

Untuk memastikan bahwa sistem informasi pengajuan cuti akademik yang dikembangkan berfungsi dengan baik dan sesuai dengan kebutuhan pengguna, pengujian akan dilakukan menggunakan metode _black box testing_ . _Black box testing_ adalah metode pengujian perangkat lunak yang berfokus pada fungsionalitas sistem dengan memeriksa apakah hasil yang diperoleh sudah sesuai dengan yang diharapkan. Pengujian dilakukan berdasarkan _test case_ yang mencakup berbagai skenario pengujian. Hasil dari pengujian ini akan digunakan untuk mengevaluasi apakah sistem telah berfungsi sesuai harapan atau masih memerlukan perbaikan. Berikut adalah tabel _black box testing_ dengan _test case_ yang akan diujikan:

Tabel 2.4 Rencana Pengujian Proyek

|**No.**|**Aktor**|**Skenario**|**Hasil yang Diharapkan**|
|---|---|---|---|
|1.|Mahasiswa|1) Pengguna mengakses|1) Sistem mengarahkan|
|||halaman<br>_login_<br>dan|pengguna ke_dashboard_|
||||sesuai perannya.|

|memasukkan_email_serta|2) Sistem menampilkan|
|---|---|
|_password_yang valid.|“Form Pengajuan Cuti|
|2) Pengguna membuka|Akademik Mahasiswa”|
|menu “Pengajuan Cuti”|dengan data diri yang|
|lalu klik submenu “Buat|sudah terisi otomatis.|
|Pengajuan Cuti”.|3) Sistem mengosongkan|
|3)<br>Pengguna mengisi|seluruh isian form yang|
|data pengajuan cuti, lalu|sudah dimasukkan (reset|
|klik tombol “Batal”.|form).|
|4)<br>Pengguna mengisi|4) Sistem menampilkan|
|data pengajuan cuti, lalu|notifikasi<br>toast|
|klik tombol “Submit”.|“Pengajuan cuti berhasil|
|5)<br>Pengguna<br>melihat|dikirim.”<br>dan|
|bagian “_Tracking_Status”|mengarahkan<br>ke|
|pada<br>halaman<br>detail|halaman<br>detail|
|pengajuan.|pengajuan.|
|6) Pengguna membuka|5) Sistem menampilkan|
|menu “Pengajuan Cuti”|tahapan persetujuan yang|
|lalu klik submenu “Data|telah dan akan dilalui|
|Pengajuan Cuti”.|oleh<br>pengajuan<br>cuti|
|7)<br>Pengguna|tersebut.|
|menggunakan<br>_filter_|6) Sistem menampilkan|
|untuk memilih periode|daftar seluruh pengajuan|
|atau semester tertentu.|cuti yang pernah dibuat.|
|8) Pengguna klik tombol|7) Sistem menampilkan|
|“Lihat<br>Detail|daftar<br>pengajuan<br>cuti|
|Pengajuan”.|sesuai_filter_yang dipilih.|
|9) Pengguna klik tombol|8) Sistem menampilkan|
|“Lihat<br>Surat|informasi<br>lengkap|
|Keputusan”.|formulir cuti dan histori|
|10) Pengguna menerima|_tracking_<br>status|
|notifikasi<br>ketika|sebelumnya.|

||pengajuan cuti disetujui<br>atau ditolak.<br>11) Pengguna klik ikon<br>profil di navbar dan pilih<br>submenu “_Logout_”.|9) Sistem menampilkan<br>dokumen<br>Surat<br>Keputusan.<br>10) Sistem menampilkan<br>notifikasi<br>yang|
|---|---|---|
|||mengarahkan pengguna<br>ke<br>halaman<br>detail<br>pengajuan.<br>11) Sistem mengakhiri<br>sesi dan mengarahkan<br>pengguna kembali<br>ke<br>halaman_login_.|
|2.<br>Dosen PA|1) Pengguna mengakses<br>halaman<br>_login_<br>dan<br>memasukkan_email_serta<br>_password_yang valid.|1) Sistem mengarahkan<br>pengguna ke_dashboard_<br>sesuai perannya.<br>2) Sistem menampilkan|
||2) Pengguna membuka<br>menu “Pengajuan Cuti”<br>lalu klik submenu “Data<br>Pengajuan Cuti”.|daftar<br>pengajuan<br>cuti<br>yang<br>memerlukan<br>persetujuan.<br>3) Sistem menampilkan|
||3)<br>Pengguna<br>menggunakan<br>_filter_<br>untuk memilih periode|daftar<br>pengajuan<br>cuti<br>sesuai_filter_yang dipilih.<br>4) Sistem menampilkan|
||atau semester tertentu.|informasi<br>lengkap|
||4) Pengguna klik tombol|formulir cuti dan histori|
||“Lihat<br>Detail|_tracking_<br>status|
||Pengajuan”.|sebelumnya.|
||5) Pengguna klik tombol|5) Sistem menampilkan|
||“Beri<br>Konfirmasi|_pop-up_<br>untuk<br>input|
||Persetujuan” dan pilih|alasan.<br>Jika<br>berhasil,|
||“Tolak”, lalu mengisi<br>alasan penolakan.|maka<br>sistem<br>akan<br>menampilkan notifikasi|

|6) Pengguna klik tombol|toast “Pengajuan telah|
|---|---|
|“Beri<br>Konfirmasi|ditolak.”<br>dan<br>status|
|Persetujuan” dan pilih|pengajuan akan berubah|
|“Setujui”,<br>lalu|menjadi “Ditolak”.|
|memasukkan_password_.|6)<br>Sistem<br>melakukan|
|7) Pengguna menerima|autentikasi. Jika valid,|
|notifikasi<br>ketika|maka<br>sistem<br>akan|
|pengajuan<br>masuk<br>ke|menampilkan notifikasi|
|tahapnya.|toast “Pengajuan berhasil|
|8) Pengguna klik tombol|diperbarui.” dan status|
|“Setujui” atau “Tolak”|akan berubah ke tahapan|
|dari halaman detail yang|selanjutnya.|
|diakses<br>melalui|7) Sistem menampilkan|
|notifikasi.|notifikasi<br>yang|
|9) Pengguna klik ikon|mengarahkan pengguna|
|profil di navbar dan pilih|ke<br>halaman<br>detail|
|submenu “_Logout_”.|pengajuan.|
||8) Sistem menampilkan<br>_pop-up_autentikasi atau|
||input<br>alasan<br>sesuai|
||tindakan yang dipilih.|
||Setelah<br>itu,<br>sistem|
||menampilkan notifikasi|
||toast “Pengajuan telah|
||ditolak.”<br>atau|
||“Pengajuan<br>berhasil|
||diperbarui.” sesuai aksi|
||<br>yang dilakukan.|
||9) Sistem<br>mengakhiri|
||sesi dan mengarahkan|
||pengguna kembali<br>ke|
||halaman_login_.|

|3.<br>Staf|1) Pengguna mengakses|1) Sistem mengarahkan|
|---|---|---|
|Kemahasiswaan|halaman<br>_login_<br>dan|pengguna ke_dashboard_|
|Fakultas|memasukkan_email_serta|sesuai perannya.|
||_password_yang valid.|2) Sistem menampilkan|
||2) Pengguna membuka|daftar<br>pengajuan<br>cuti|
||menu “Pengajuan Cuti”|yang<br>memerlukan|
||lalu klik submenu “Data<br>Pengajuan Cuti”.|verifikasi atau pemberian<br>nomor surat.|
||3)<br>Pengguna|3) Sistem menampilkan|
||menggunakan<br>_filter_|daftar<br>pengajuan<br>cuti|
||untuk memilih periode|sesuai_filter_yang dipilih.|
||atau semester tertentu.|4) Sistem menampilkan|
||4) Pengguna klik tombol|informasi<br>lengkap|
||“Lihat<br>Detail|formulir cuti dan histori|
||Pengajuan”.|_tracking_<br>status|
||5) Pengguna klik tombol|sebelumnya.|
||“Lihat Surat Pengantar”.|5) Sistem menampilkan|
||6) Pengguna klik tombol|dokumen<br>Surat|
||“Lihat<br>Surat|Pengantar.|
||Keputusan”.|6) Sistem menampilkan|
||7) Pengguna klik tombol|dokumen<br>Surat|
||“Beri<br>Konfirmasi|Keputusan.|
||Persetujuan” dan pilih|7) Sistem menampilkan|
||“Tolak”, lalu mengisi|_pop-up_<br>untuk<br>input|
||alasan penolakan.|alasan.<br>Jika<br>berhasil,|
||8) Pengguna klik tombol|maka<br>sistem<br>akan|
||“Beri<br>Konfirmasi|menampilkan notifikasi|
||Persetujuan” dan pilih|toast “Pengajuan telah|
||“Setujui”,<br>lalu|ditolak.”<br>dan<br>status|
||memasukkan_password_.|pengajuan akan berubah<br>menjadi “Ditolak”.|

|9) Pengguna klik tombol|8)<br>Sistem<br>akan|
|---|---|
|“Beri Nomor Surat”, lalu|menampilkan notifikasi|
|mengisi nomor surat.|toast “Pengajuan berhasil|
|10) Pengguna menerima|diperbarui.” dan status|
|notifikasi<br>ketika|akan berubah ke tahapan|
|pengajuan<br>masuk<br>ke|selanjutnya.|
|tahapnya.|9) Sistem menampilkan|
|11)<br>Pengguna<br>klik|_pop-up_<br>input<br>nomor|
|tombol “Setujui” atau|surat.<br>Jika<br>berhasil,|
|“Tolak” dari halaman|sistem<br>menampilkan|
|detail<br>yang<br>diakses|notifikasi toast “Nomor|
|melalui notifikasi.|Surat Pengantar berhasil|
|12) Pengguna klik ikon|diberikan.” dan nomor|
|profil di navbar dan pilih|surat tersimpan.|
|submenu “_Logout_”.|10) Sistem menampilkan<br>notifikasi<br>yang<br>mengarahkan pengguna|
||ke<br>halaman<br>detail|
||pengajuan.<br>11) Sistem menampilkan<br>_pop-up_autentikasi atau<br> <br> <br>|
||input<br>alasan<br>sesuai|
||tindakan yang dipilih.|
||Setelah<br>itu,<br>sistem|
||menampilkan notifikasi<br>“|
||toast Pengajuan telah|
||ditolak.”<br>atau|
||“Pengajuan<br>berhasil|
||diperbarui.” sesuai aksi|
||yang dilakukan.|
||12) Sistem mengakhiri|
||sesi dan mengarahkan|

|||pengguna kembali<br>ke<br>halaman_login_.|
|---|---|---|
|4.<br>Koordinator TU|1) Pengguna mengakses<br>halaman<br>_login_<br>dan<br>memasukkan_email_serta<br>_password_yang valid.|1) Sistem mengarahkan<br>pengguna ke_dashboard_<br>sesuai perannya.<br>2) Sistem menampilkan|
||2) Pengguna membuka|daftar<br>pengajuan<br>cuti|
||menu “Pengajuan Cuti”<br>lalu klik submenu “Data<br>Pengajuan Cuti”.|yang<br>memerlukan<br>persetujuan.<br>3) Sistem menampilkan|
||3)<br>Pengguna<br>menggunakan<br>_filter_<br>untuk memilih periode<br>atau semester tertentu.|daftar<br>pengajuan<br>cuti<br>sesuai_filter_yang dipilih.<br>4) Sistem menampilkan<br>informasi<br>lengkap|
||4) Pengguna klik tombol|formulir cuti dan histori|
||“Lihat<br>Detail|_tracking_<br>status|
||Pengajuan”.|sebelumnya.|
||5) Pengguna klik tombol|5) Sistem menampilkan|
||“Lihat Surat Pengantar”.<br>6) Pengguna klik tombol|dokumen<br>Surat<br>Pengantar.|
||“Beri<br>Konfirmasi|6) Sistem menampilkan|
||Persetujuan” dan pilih|_pop-up_<br>untuk<br>input|
||“Tolak”, lalu mengisi|alasan.<br>Jika<br>berhasil,|
||alasan penolakan.|maka<br>sistem<br>akan|
||7) Pengguna klik tombol|menampilkan notifikasi|
||“Beri<br>Konfirmasi|toast “Pengajuan telah|
||Persetujuan” dan pilih|ditolak.”<br>dan<br>status|
||“Setujui”,<br>lalu|pengajuan akan berubah|
||memasukkan_password_.|menjadi “Ditolak”.|
||8) Pengguna menerima|7)<br>Sistem<br>melakukan|
||notifikasi<br>ketika|autentikasi. Jika valid,<br>maka<br>sistem<br>akan|

|pengajuan<br>masuk<br>ke|menampilkan notifikasi|
|---|---|
|tahapnya.|toast “Pengajuan berhasil|
|9) Pengguna klik tombol|diperbarui.” dan status|
|“Setujui” atau “Tolak”|akan berubah ke tahapan|
|dari halaman detail yang|selanjutnya.|
|diakses<br>melalui|8) Sistem menampilkan|
|notifikasi.|notifikasi<br>yang|
|10) Pengguna membuka|mengarahkan pengguna|
|menu<br>“Manajemen|ke<br>halaman<br>detail|
|_User_” dan klik submenu|pengajuan.|
|“Data_User_”.|9) Sistem menampilkan|
|11)<br>Pengguna<br>klik|_pop-up_autentikasi atau|
|tombol “Tambah_User_”|input<br>alasan<br>sesuai|
|dan mengisi data dengan|tindakan yang dipilih.|
|benar.|Setelah<br>itu,<br>sistem|
|12)<br>Pengguna<br>klik|menampilkan notifikasi|
|tombol “_Edit_” pada salah|toast “Pengajuan telah|
|satu_user_dan mengubah|ditolak.”<br>atau|
|datanya.|“Pengajuan<br>berhasil|
|13)<br>Pengguna<br>klik|diperbarui.” sesuai aksi|
|tombol “Hapus” pada|yang dilakukan.|
|salah<br>satu<br>_user_<br>dan|10) Sistem menampilkan|
|melakukan konfirmasi.|daftar_user_yang terdaftar|
|14) Pengguna membuka|di sistem.|
|menu<br>“Manajemen|11) Sistem menyimpan|
|_User_” dan klik submenu|data<br>_user_<br>baru<br>dan|
|“Data_Role_”.|menampilkan notifikasi|
|15)<br>Pengguna<br>klik|toast<br>“_User_<br>berhasil|
|tombol “Tambah_Role_”|ditambahkan.”|
|dan mengisi data dengan|12) Sistem menyimpan|
|benar.|perubahan<br>dan|
||menampilkan notifikasi|

||16)<br>Pengguna<br>klik|toast<br>“_User_<br>berhasil|
|---|---|---|
||tombol “_Edit_” pada salah<br>satu_role_dan mengubah|diperbarui.”<br>13) Sistem menghapus|
||datanya.|data<br>_user_<br>dan|
||17)<br>Pengguna<br>klik<br>tombol “Hapus” pada<br>salah<br>satu<br>_role_<br>dan<br>melakukan konfirmasi.<br>18) Pengguna klik ikon<br>profil di navbar dan pilih<br>submenu “_Logout_”.|menampilkan notifikasi<br>toast<br>“_User_<br>berhasil<br>dihapus.”<br>14) Sistem menampilkan<br>daftar_role_yang tersedia<br>di sistem.<br>15) Sistem menyimpan<br>data<br>_role_<br>baru<br>dan<br>menampilkan notifikasi<br>toast<br>"_Role_<br>berhasil<br>ditambahkan."<br>16) Sistem menyimpan<br>perubahan<br>dan<br>menampilkan notifikasi<br>toast<br>"_Role_<br>berhasil<br>diperbarui."<br>17) Sistem menghapus<br>data<br>_role_<br>dan<br>menampilkan notifikasi<br>toast<br>"_Role_<br>berhasil<br>dihapus."<br>18) Sistem mengakhiri<br>sesi dan mengarahkan<br>pengguna kembali<br>ke<br>halaman_login_.|
|5.<br>Koordinator|1) Pengguna mengakses|1) Sistem mengarahkan|
|Prodi|halaman<br>_login_<br>dan|pengguna ke_dashboard_<br>sesuai perannya.|

|memasukkan_email_serta|2) Sistem menampilkan|
|---|---|
|_password_yang valid.|daftar<br>pengajuan<br>cuti|
|2) Pengguna membuka|yang<br>memerlukan|
|menu “Pengajuan Cuti”|persetujuan.|
|lalu klik submenu “Data|3) Sistem menampilkan|
|Pengajuan Cuti”.|daftar<br>pengajuan<br>cuti|
|3)<br>Pengguna|sesuai_filter_yang dipilih.|
|menggunakan<br>_filter_|4) Sistem menampilkan|
|untuk memilih periode|informasi<br>lengkap|
|atau semester tertentu.|formulir cuti dan histori|
|4) Pengguna klik tombol|_tracking_<br>status|
|“Lihat<br>Detail|sebelumnya.|
|Pengajuan”.|5) Sistem menampilkan|
|5) Pengguna klik tombol|dokumen<br>Surat|
|“Lihat Surat Pengantar”.|Pengantar.|
|6) Pengguna klik tombol|6) Sistem menampilkan|
|“Beri<br>Konfirmasi|_pop-up_<br>untuk<br>input|
|Persetujuan” dan pilih|alasan.<br>Jika<br>berhasil,|
|“Tolak”, lalu mengisi|maka<br>sistem<br>akan|
|alasan penolakan.|menampilkan notifikasi|
|7) Pengguna klik tombol|toast “Pengajuan telah|
|“Beri<br>Konfirmasi|ditolak.”<br>dan<br>status|
|Persetujuan” dan pilih|pengajuan akan berubah|
|“Setujui”,<br>lalu|menjadi “Ditolak”.|
|memasukkan_password_.|7)<br>Sistem<br>melakukan|
|8) Pengguna menerima|autentikasi. Jika valid,|
|notifikasi<br>ketika|maka<br>sistem<br>akan|
|pengajuan<br>masuk<br>ke|menampilkan notifikasi|
|tahapnya.|toast “Pengajuan berhasil|
|9) Pengguna klik tombol|diperbarui.” dan status|
|“Setujui” atau “Tolak”|akan berubah ke tahapan|
|dari halaman detail yang|selanjutnya.|

||diakses<br>melalui<br>notifikasi.|8) Sistem menampilkan<br>notifikasi<br>yang|
|---|---|---|
||10) Pengguna klik ikon<br>profil di navbar dan pilih<br>submenu “_Logout_”.|mengarahkan pengguna<br>ke<br>halaman<br>detail<br>pengajuan.<br>9) Sistem menampilkan<br>_pop-up_autentikasi atau<br>input<br>alasan<br>sesuai<br>tindakan yang dipilih.<br>Setelah<br>itu,<br>sistem<br>menampilkan notifikasi<br>toast “Pengajuan telah<br>ditolak.”<br>atau<br>“Pengajuan<br>berhasil<br>diperbarui.” sesuai aksi<br>yang dilakukan.<br>10) Sistem mengakhiri<br>sesi dan mengarahkan<br>pengguna kembali<br>ke<br>halaman_login_.|
|6.<br>Dekan|1) Pengguna mengakses<br>halaman<br>_login_<br>dan<br>memasukkan_email_serta<br>_password_yang valid.<br>2) Pengguna klik ikon<br>profil di navbar dan pilih<br>submenu “Tanda Tangan<br>Digital”.|1) Sistem mengarahkan<br>pengguna ke_dashboard_<br>sesuai perannya.<br>2) Sistem menampilkan<br>halaman untuk membuat<br>tanda tangan digital.<br>3) Sistem menyimpan<br>gambar tanda tangan dan|
||3) Pengguna membuat|menampilkannya<br>di|
||tanda<br>tangan<br>digital|halaman.|
||dengan menggambar di|4) Sistem menampilkan<br>daftar<br>pengajuan<br>cuti|

|kanvas<br>lalu|yang<br>memerlukan|
|---|---|
|menyimpannya.|persetujuan.|
|4) Pengguna membuka|5) Sistem menampilkan|
|menu “Pengajuan Cuti”|daftar<br>pengajuan<br>cuti|
|lalu klik submenu “Data|sesuai_filter_yang dipilih.|
|Pengajuan Cuti”.|6) Sistem menampilkan|
|5)<br>Pengguna|informasi<br>lengkap|
|menggunakan<br>_filter_|formulir cuti dan histori|
|untuk memilih periode|_tracking_<br>status|
|atau semester tertentu.|sebelumnya.|
|6) Pengguna klik tombol|7) Sistem menampilkan|
|“Lihat<br>Detail|dokumen<br>Surat|
|Pengajuan”.|Pengantar.|
|7) Pengguna klik tombol|8) Sistem menampilkan|
|“Lihat Surat Pengantar”.|_pop-up_<br>untuk<br>input|
|8) Pengguna klik tombol|alasan.<br>Jika<br>berhasil,|
|“Beri<br>Konfirmasi|maka<br>sistem<br>akan|
|Persetujuan” dan pilih|menampilkan notifikasi|
|“Tolak”, lalu mengisi|toast “Pengajuan telah|
|alasan penolakan.|ditolak.”<br>dan<br>status|
|9) Pengguna klik tombol|pengajuan akan berubah|
|“Beri<br>Konfirmasi|menjadi “Ditolak”.|
|Persetujuan” dan pilih|9)<br>Sistem<br>melakukan|
|“Setujui”,<br>lalu|autentikasi. Jika valid,|
|memasukkan_password_.|maka<br>sistem<br>akan|
|10) Pengguna menerima|menampilkan notifikasi|
|notifikasi<br>ketika|toast “Pengajuan berhasil|
|pengajuan<br>masuk<br>ke|diperbarui.” dan status|
|tahapnya.|akan berubah ke tahapan|
|11)<br>Pengguna<br>klik|selanjutnya.|
|tombol “Setujui” atau|10) Sistem menampilkan|
|“Tolak” dari halaman|notifikasi<br>yang|

||detail<br>yang<br>diakses<br>melalui notifikasi.<br>12) Pengguna klik ikon<br>profil di navbar dan pilih<br>submenu “_Logout_”.|mengarahkan pengguna<br>ke<br>halaman<br>detail<br>pengajuan.<br>11) Sistem menampilkan<br>_pop-up_autentikasi atau<br>input<br>alasan<br>sesuai<br>tindakan yang dipilih.<br>Setelah<br>itu,<br>sistem<br>menampilkan notifikasi<br>toast “Pengajuan telah<br>ditolak.”<br>atau<br>“Pengajuan<br>berhasil<br>diperbarui.” sesuai aksi<br>yang dilakukan.<br>12) Sistem mengakhiri<br>sesi dan mengarahkan<br>pengguna kembali<br>ke<br>halaman_login_.|
|---|---|---|
|7.<br>Karo AKK|1) Pengguna mengakses<br>halaman<br>_login_<br>dan<br>memasukkan_email_serta<br>_password_yang valid.<br>2) Pengguna membuka<br>menu “Pengajuan Cuti”<br>lalu klik submenu “Data<br>Pengajuan Cuti”.<br>3)<br>Pengguna<br>menggunakan<br>_filter_<br>untuk memilih periode<br>atau semester tertentu.|1) Sistem mengarahkan<br>pengguna ke_dashboard_<br>sesuai perannya.<br>2) Sistem menampilkan<br>daftar<br>pengajuan<br>cuti<br>yang<br>memerlukan<br>persetujuan.<br>3) Sistem menampilkan<br>daftar<br>pengajuan<br>cuti<br>sesuai_filter_yang dipilih.<br>4) Sistem menampilkan<br>informasi<br>lengkap<br>formulir cuti dan histori|

|4) Pengguna klik tombol|_tracking_<br>status|
|---|---|
|“Lihat<br>Detail|sebelumnya.|
|Pengajuan”.|5) Sistem menampilkan|
|5) Pengguna klik tombol|dokumen<br>Surat|
|“Lihat Surat Pengantar”.|Pengantar.|
|6) Pengguna klik tombol|6) Sistem menampilkan|
|“Lihat<br>Surat|dokumen<br>Surat|
|Keputusan”.|Keputusan.|
|7) Pengguna klik tombol|7) Sistem menampilkan|
|“Beri<br>Konfirmasi|_pop-up_<br>untuk<br>input|
|Persetujuan” dan pilih|alasan.<br>Jika<br>berhasil,|
|“Tolak”, lalu mengisi|maka<br>sistem<br>akan|
|alasan penolakan.|menampilkan notifikasi|
|8) Pengguna klik tombol|toast “Pengajuan telah|
|“Beri<br>Konfirmasi|ditolak.”<br>dan<br>status|
|Persetujuan” dan pilih|pengajuan akan berubah|
|“Setujui”,<br>lalu|menjadi “Ditolak”.|
|memasukkan_password_.|8)<br>Sistem<br>melakukan|
|9) Pengguna menerima|autentikasi. Jika valid,|
|notifikasi<br>ketika|maka<br>sistem<br>akan|
|pengajuan<br>masuk<br>ke|menampilkan notifikasi|
|tahapnya.|toast “Pengajuan berhasil|
|10)<br>Pengguna<br>klik|diperbarui.” dan status|
|tombol “Setujui” atau|akan berubah ke tahapan|
|“Tolak” dari halaman|selanjutnya.|
|detail<br>yang<br>diakses|9) Sistem menampilkan|
|melalui notifikasi.|notifikasi<br>yang|
|11) Pengguna klik ikon|mengarahkan pengguna|
|profil di navbar dan pilih|ke<br>halaman<br>detail|
|submenu “_Logout_”.|pengajuan.<br>10) Sistem menampilkan|
||_pop-up_autentikasi atau|

|input<br>alasan<br>sesuai|
|---|
|tindakan yang dipilih.|
|Setelah<br>itu,<br>sistem|
|menampilkan notifikasi|
|toast “Pengajuan telah|
|ditolak.”<br>atau|
|“Pengajuan<br>berhasil|
|diperbarui.” sesuai aksi|
|yang dilakukan.|
|11) Sistem mengakhiri|
|sesi dan mengarahkan|
|pengguna kembali<br>ke|
|halaman_login_.|


# PROYEK PEMBUATAN APLIKASI BACK OFFICE PADA DISKOUMPERINDAG KABUPATEN SERANG BERBASIS WEB

# **BAB II RANCANGAN PROYEK**

- 2.1 Observasi

Dalam rangka memahami alur kerja dan permasalahan yang dihadapi dalam proses pendataan UMKM di DISKOUMPERINDAG Kabupaten Serang, penulis telah melakukan observasi langsung ke lokasi. Observasi ini dilakukan untuk mengidentifikasi prosedur yang berjalan saat ini, mulai dari kedatangan pelaku UMKM, proses pengambilan antrian, penyerahan berkas, hingga pengecekan dan pencatatan data oleh petugas dinas, seperti pada diagram di bawah :

<!-- Start of picture text -->
a Pendataan UMKM<br>Datang ke<br>DISKOPPERINDAG<br>Kab, Serang<br>™ <><br>if<br>Input Data ke File<br>Excel<br><!-- End of picture text -->

Gambar 2.1. Diagram Proses Bisnis Pendataan UMKM

Dan berikut merupakan proses bisnis pemantauan UMKM yang saat ini sedang berjalan di DISKOUMPERINDAG Kabupaten Serang :

<!-- Start of picture text -->
Pemantauan dan Pengelolaan UMKM<br>|<br>Datang ke lokasi<br>UMKM<br>Memberikan<br>Informasi yang Memint informs<br>diperlukan yang dip<br>Melakukan<br>pencatatan informasi<br><!-- End of picture text -->

Gambar 2.2. Diagram Proses Bisnis Pemantauan dan Pengelolaan UMKM

# 2.2 Usulan Solusi

# a. Bisnis Proses

Berikut merupakan proses bisnis pendataan UMKM yang akan diterapkan di DISKOUMPERINDAG Kabupaten Serang :

<!-- Start of picture text -->
Nelokukan Registas conwa<br>rasarermen || paitoat ||| aserireas ||| oxtareosie<br>resvies Ure let>ane pron xeowstas, ||| psa Pecetaan kero Poa<br>I<br>, u<br><!-- End of picture text -->

Gambar 2.3. Proses Bisnis Usulan

Diagram tersebut menggambarkan alur proses bisnis aplikasi pengelolaan data UMKM yang melibatkan dua aktor utama, yaitu pelaku UMKM dan admin. Proses dimulai dari pelaku UMKM yang melakukan registrasi. Setelah registrasi dilakukan, admin akan melakukan login dan proses otentikasi untuk mengakses sistem. Jika login berhasil, admin dapat mengakses berbagai fitur seperti

pengelolaan pengajuan, transaksi, aplikasi, daftar pengguna, profil, dan peta persebaran.

Dalam pengelolaan pengajuan, admin memverifikasi apakah data yang diajukan sesuai atau tidak. Jika tidak sesuai, admin akan mengisi alasan penolakan dan pelaku UMKM diminta melakukan registrasi ulang. Namun jika sesuai, admin dapat menyetujui pengajuan tersebut sehingga data UMKM akan terintegrasi dengan seluruh bagian sistem lainnya. Diagram ini menunjukkan hubungan antarproses yang saling terintegrasi, mulai dari registrasi hingga pengelolaan data oleh admin.

# b. Kerangka Berpikir

Berikut merupakan kerangka berpikir dalam proyek pembuatan aplikasi _back office_ ini :

<!-- Start of picture text -->
rodesd<br>=<br>alitor4<br>a<br>snupgno4 isis. biowees4 lsdU<br>=<br>‘iba lesallgA slolen MMU witsie9<br>iedsensiT sloloX<br>MOIMU sole<br>‘snupgne4 nislginon<br>sisd 2iesa<br>yeeU .t<br>iesensiT .S<br>odoT .€<br>nisiqmon A<br>Aubord hopsisy .2<br>odoT 2insl .d<br><!-- End of picture text -->

Gambar 2.4. Kerangka Berpikir Perancangan Aplikasi

Kerangka berpikir perancangan aplikasi pendataan dan pengelolaan UMKM ini bertujuan untuk memberikan gambaran alur logis dari pengembangan sistem yang akan diterapkan di DISKOUMPERINDAG Kabupaten Serang. Aplikasi ini dirancang untuk melibatkan dua aktor utama, yaitu pelaku UMKM dan admin. Pelaku UMKM memulai interaksi dengan sistem melalui proses registrasi dan login, yang kemudian diarahkan ke halaman dasbor pengguna. Di sisi lain, admin juga melalui proses login dan memiliki akses yang lebih luas dibandingkan pelaku UMKM. Pelaku UMKM dapat mengakses fitur dasbor untuk melihat ringkasan aktivitas serta profil untuk mengelola data pribadi mereka. Sementara itu, admin memiliki wewenang untuk mengakses berbagai fitur seperti daftar pengguna, peta persebaran UMKM, kelola aplikasi, kelola transaksi, dan kelola UMKM.

Setiap aktivitas pengguna, baik dari pelaku UMKM maupun admin, akan berhubungan langsung dengan basis data yang menyimpan informasi penting dalam sistem. Basis data ini terdiri dari beberapa entitas utama, yaitu data user, transaksi, toko (UMKM), kategori produk, dan jenis toko. Integrasi sistem ini bertujuan untuk meningkatkan efisiensi dalam pendataan dan pemantauan UMKM, serta mendukung pengambilan keputusan berbasis data secara cepat dan akurat. Dengan sistem ini, proses yang sebelumnya dilakukan secara manual dapat disederhanakan dan dikelola secara digital, terpusat, dan _real-time_ .

# 2.3 Metode Pengembangan Sistem

Metode _Agile_ dipilih untuk pengembangan sistem informasi _back office_ UMKM di Kabupaten Serang karena fleksibilitasnya yang memungkinkan tim pengembang merespons perubahan dengan cepat, khususnya mengingat waktu pengembangan yang terbatas hanya tiga bulan. Dalam periode waktu yang singkat ini, sangat penting untuk bisa menghasilkan fitur yang siap digunakan secara bertahap, sembari tetap mengakomodasi kebutuhan yang mungkin berubah-ubah. _Agile_ mendorong kolaborasi intensif antara tim pengembang, DISKOUMPERINDAG, dan pelaku UMKM melalui iterasi singkat atau _sprint_ , sehingga memungkinkan penyesuaian dan perbaikan sistem berdasarkan umpan balik pengguna secara cepat. Pendekatan ini juga memprioritaskan pengembangan fitur yang paling penting terlebih dahulu, memastikan bahwa sistem bisa berfungsi

meskipun belum sepenuhnya lengkap. Dengan _Agile_ , setiap sprint menghasilkan peningkatan berkelanjutan yang membuat pengembangan lebih efisien dan memungkinkan sistem digunakan secara lebih dini, memberikan waktu bagi _stakeholder_ untuk menguji dan memberikan masukan. Selain itu, risiko pengembangan dapat diminimalkan karena _Agile_ membagi proyek menjadi bagianbagian kecil yang bisa dievaluasi dan disesuaikan dengan lebih mudah, sehingga fitur-fitur yang tidak sesuai atau kurang efektif bisa segera diubah.

- 2.4 Analisis Kebutuhan Sistem

a. Fungsional

Berikut merupakan kebutuhan fungsional yang dibutuhkan pada aplikasi Bisa UMKM :

- 1) Pendataan UMKM

Aplikasi menyediakan fitur registrasi untuk pengguna mendaftarkan usahanya yang kemudian akan diverifikasi oleh admin.

- 2) Otentikasi Pengguna

Aplikasi menyediakan halaman _login_ yang memungkinkan pengguna untuk memasukkan _email_ /nomor telepon dan _password_ untuk mengakses aplikasi.

- 3) Manajemen Profil Pengguna

Pengguna, baik admin maupun pelaku usaha, dapat mengelola dan memperbarui profil mereka melalui fitur yang disediakan

- 4) Manajemen Aplikasi

Admin memiliki fitur untuk mengelola jenis toko, kategori produk dan biaya admin di dalam aplikasi. Tersedia fitur untuk menambah, mengubah, atau menghapus data di masing-masing kategori untuk memastikan kebutuhan aplikasi terpenuhi.

- 5) Manajemen Transaksi

Menampilkan daftar transaksi yang terjadi dan daftar _top-up_ yang dilakukan oleh pengguna. Memberikan akses bagi admin untuk memantau dan mengelola transaksi yang terjadi di dalam aplikasi.

- 6) Manajemen UMKM

Aplikasi menyediakan daftar UMKM yang terdaftar, yang dapat dilihat dan dikelola oleh admin. Terdapat fitur persetujuan bagi admin untuk memvalidasi data pendaftaran yang telah dikirim oleh pelaku UMKM.

- 7) Manajemen Pengguna

Admin memiliki akses untuk melihat daftar pengguna yang ada di aplikasi _mobile_ .

- 8) Fitur _Maps Marker_ untuk UMKM

Menyediakan fitur untuk menampilkan lokasi UMKM di peta (m _arker maps_ ), yang memudahkan admin dalam memantau lokasi usaha secara geografis.

b. Non-fungsional

Berikut adalah beberapa kebutuhan non-fungsional untuk aplikasi Bisa UMKM :

- 1) Keamanan:

Aplikasi harus memiliki autentikasi yang aman dengan enkripsi data _login_ . Sistem verifikasi _email_ untuk memastikan keaslian identitas pengguna. Akses ke fitur-fitur tertentu dibatasi sesuai dengan peran (admin atau pelaku usaha).

- 2) Kinerja :

Aplikasi harus tetap responsif meskipun digunakan oleh banyak pengguna secara bersamaan. Pemrosesan data transaksi dan visualisasi harus berjalan lancar tanpa hambatan.

- 3) Reliabilitas :

Aplikasi harus memiliki _uptime_ yang tinggi untuk memastikan aksesibilitas, terutama bagi pengguna yang membutuhkan aplikasi untuk pelaporan harian.

- 4) Kemudahan Penggunaan :

Antarmuka aplikasi harus mudah dipahami dan digunakan oleh pengguna.

# 2.5 Rancangan Proyek

# a. Use Case Diagram

<!-- Start of picture text -->
E-commerceUse Case Backoffioe BisaUMKM (ma)<br>Buka Toko<br>Daftar<br>Pengguna<br>Peta<br>Persebaran<br>UMKM<br>Pengiriman dan<br>Komplain Pembayaran"<br>Pengguna<br>Kelola Ubah Password<br>Teextend?>Mende ose<eexterhSSEAplikasiZextend>> \\<br>Kelola Tipe Kelola Kategori \ /Kelola Kategori<br>Admin UMKM Produk Pengiriman Penjual<br>Kelola<br>Transaksi<br>Daftar Transaks! Kelola Top-up<br>_A Kelola UMKM )<br><cextepd5> <2extend>><br>a <<exipnd>><br>(«elola Pengajuan)<br><!-- End of picture text -->

Gambar 2.5. _Use case_ Diagram

Use case diagram tersebut menunjukkan interaksi antara Admin dan Penjual dalam sistem _back office_ . Keduanya dapat masuk, membuka toko, mengelola profil, melihat dasbor, dan keluar. Admin memiliki peran tambahan seperti mengelola pengguna, aplikasi, transaksi, UMKM, serta melihat peta persebaran UMKM. Beberapa fungsi seperti daftar transaksi dan pengajuan merupakan bagian dari proses yang lebih besar melalui relasi _extend_ . Diagram ini menggambarkan alur utama pengelolaan sistem oleh kedua aktor.

# b. Activity Diagram

<!-- Start of picture text -->
Akses situs web Menampilkan<br>Memasukkan | Mengirim Data<br>Username Verifikasi Data<br>—<br>Menampilkan:<br>Pesan Data Tidak<br>Menampilkan<br>Halaman<br>Dashboard<br><!-- End of picture text -->

Gambar 2.6. _Activity Login_

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas _login_ untuk masuk ke dalam aplikasi.

<!-- Start of picture text -->
ee<br>Membuka menu<br>“Profil”<br>Klik Button Menghapus<br>"Logout" / token<br>Menerima respons Mengirimberhasil responslogout<br><!-- End of picture text -->

Gambar 2.7. _Activity Logout_

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas _logout_ untuk keluar dari aplikasi _back office._

1) _User_

<!-- Start of picture text -->
Akses situs web Halaman login<br><!-- End of picture text -->

Gambar 2.8. _Activity_ Buka Toko

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas pelaku UMKM yang ingin mendaftarkan UMKM nya pada aplikasi.

<!-- Start of picture text -->
Back Office - Profil Penjual<br>eS<br>Klik Profil ; MenampilkanRequest DataData Profil Profil 7 Kirim Data Profil<br><!-- End of picture text -->

Gambar 2. 9 _Activity_ Profile _User_

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas untuk melihat profil pengguna yang telah terdaftar.

<!-- Start of picture text -->
—_—<br>Mengirim data password baru<br>Data<br><!-- End of picture text -->

Gambar 2.10. _Activity_ Ubah _Password_

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas untuk mengubah kata sandi.

<!-- Start of picture text -->
Back Office - Ubah Kurir<br>Memilih menu<br>=nnMengirim data kur pilihan<br>Menyimpan<br>Data<br><!-- End of picture text -->

Gambar 2.11. _Activity_ Ubah Kurir

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas untuk mengubah data kurir yang digunakan.

Gambar 2.12. _Activity_ Ubah Metode Pembayaran

Gambar di atas merupakan _Activity_ Diagram dari pengguna yang menjelaskan alur dari aktivitas untuk mengubah data metode pembayaran yang digunakan untuk transaksi.

2) Admin

<!-- Start of picture text -->
Klik Profil ; Request Data Profil + Kirim Data Profil<br>Menampilkan Data Profil<br><!-- End of picture text -->

Gambar 2.13. _Activity_ Profil Admin

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk melihat profil admin.

<!-- Start of picture text -->
a<br>Klik Daftar Pengguna ; Request Data Pengguna ; Kirim Data Pengguna<br>‘Tampil DataPengguna T<br><!-- End of picture text -->

Gambar 2.14 _Activity_ Daftar Pengguna

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari

aktivitas untuk melihat daftar pengguna yang ada di aplikasi _mobile._

<!-- Start of picture text -->
a<br>Klik Peta Persebaran UMKM. :Request PetaPersebaranData UMKM. UMKM | Kirim Data UMKM<br><!-- End of picture text -->

Gambar 2.15. _Activity_ Peta Persebaran UMKM

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari

aktivitas untuk melihat peta geografis persebaran UMKM yang telah terdaftar.

<!-- Start of picture text -->
Klik Daftar Pengajuan Request Data Pengajuan Kirim Data Pengajuan<br>Kirim status toko Ubah Status di<br>" var : TampilData Pengajuan |<br>isi Alasan Penolakan Kirim Alasan ‘Simpan Alasan<br>- Penolakan - Penolakan<br><!-- End of picture text -->

Gambar 2.16. _Activity_ Kelola Pengajuan

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk mengelola pendaftaran UMKM yang telah diajukan oleh pelaku UMKM.

<!-- Start of picture text -->
Klik Menu |<br>— | | y<br>pagirelnreil Jenis ba! Jenis Pengiriman yang<br>Mengisi Form | mabe Form<br><!-- End of picture text -->

Gambar 2.17. _Activity_ Kelola Jenis Toko

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk mengelola jenis toko yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
— |.Menampilkan Daftar<br>Keolola UNKM<br>pereneen ba hired KategoriMenampilkan: Produk<br>[Hapus Kategori<><br>{Perubahan Kategori<br>Produk<br>PengisianMengisi FormKategori LhePengisian Kategori Form<br>Menyimpan<br>Kategori Produk<br><!-- End of picture text -->

Gambar 2.18. _Activity_ Kelola Kategori Produk

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk mengelola kategori produk yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Moran manu Halaman tomplinpengune<br>*Komplain Pengguna” oo<br>— | Request<br>fate cet Komen —<br>Metinat detail ldata detail komplain|<br>folak soma’ SS<br>KKomplain ditolak komplain Mengirim data - Data<br><!-- End of picture text -->

Gambar 2.19. _Activity_ Kelola Komplain

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk mengelola komplain yang dilakukan pengguna pada saat transaksi. _._

<!-- Start of picture text -->
Gack Ofie Daftar Transakal<br>[Admin Sistem Database<br>Pilih FilterKlik Kelola UntukTransaksi Data , Request Data Transaksi iinKirim Data Transaksi<br>yang Ditampilkan Tampil Data Transaksi<br>Tampil Data Sesuai<br>Filter<br><!-- End of picture text -->

Gambar 2.20. _Activity_ Daftar Transaksi

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk melihat daftar transaksi yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Back Office - Kelola Top-Up<br>Memilin menu Halaman kelola|<br>"Kelola Aplikasi" | aplikasi<br>ne Request<br>"Kelola Top-Up" data topup x Mengirim data<br>Metakukan Menampilkan<br>kelola topup data topup<br>folak topup]<><br>Topup tidak Verif kasi topup Menyimpan<br>diterima diterima Mengirim data nym<br>ltopup tidakMengirim diterimapesan @<br><!-- End of picture text -->

Gambar 2.21. _Activity_ Kelola _Top-Up_

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk mengelola _top-up_ saldo yang telah dilakukan oleh pelaku UMKM.

<!-- Start of picture text -->
Tampil Data UMKM<br><!-- End of picture text -->

Gambar 2.22. _Activity_ Daftar UMKM

Gambar di atas merupakan _Activity_ Diagram dari admin yang menjelaskan alur dari aktivitas untuk melihat UMKM yang telah terdaftar dan terverifikasi oleh admin.

<!-- Start of picture text -->
a<br>Klik Halaman "UMKM Tidak Aktif" Request Data UMKM : Kirim Data UMKM<br>TampilData UMKM 7<br><!-- End of picture text -->

Gambar 2.23. _Activity_ Daftar UMKM Tidak Aktif

Gambar di atas merupakan _Activity_ Diagram dari admin untuk melihat UMKM yang

tidak melakukan transaksi dalam jangka waktu yang sudah ditentukan.

c. Sequence Diagram

<!-- Start of picture text -->
i<br>Pengguna H : :<br>H Membuka website! i : :<br>Menampilkan form login H :<br>Mengisi form login, ‘ : :<br>- Mengtim data i<br>: T Hi : validasi<br>; :L ‘ | data<br>| a)H : Data tidakH valid [data tidak valid]<br>! Menampilkan pesan error H<br>car cara ee H<br>H : Data valid (data valid]<br>: Mengarahkan ke dashboard :<br>le Menampilkan halaman dashboard :<br><!-- End of picture text -->

Gambar 2.24. _Sequence Login_

Gambar di atas merupakan gambar dari _Sequence Login_ yang menggambarkan interaksi antar objek pada saat pengguna melakukan _login._

<!-- Start of picture text -->
Klik button "Keluar” : H 3<br>H Mengirim data_ Pengguna :<br>ecccttmasimren AP i<br><!-- End of picture text -->

Gambar 2.25. _Sequence Logout_

Gambar di atas merupakan gambar dari _Sequence Logout_ yang menggambarkan interaksi antar objek pada saat pengguna akan keluar dari aplikasi _._

1) _User_

<!-- Start of picture text -->
3d Bika ToPr uma Hlamartoon FembtaTeko a Goon sofeovadta<br>2 Minta Dataivole) i<br>‘mega | i<br>_ aman ian :<br>5: Mengakses Men Baka Toko i<br>se tampered Sn<br>12 Kamba flonan too ro<br>(rt aprovea | tangata Sa<br>Teena eet Penge :<br>iva H<br>lL Pen Err Tmo<br><!-- End of picture text -->

Gambar 2.26. _Sequence_ Buka Toko

Gambar di atas merupakan gambar dari _Sequence_ buka toko yang menggambarkan interaksi antar objek pada saat pelaku UMKM melakukan pendaftaran pada aplikasi _._

<!-- Start of picture text -->
‘Pelaku UMKM<br>k<br>! Klik Halaman Profil i H<br>Request Data Profil, |<br>| <.- Fampil Data Profi <---Data Profil od<br><!-- End of picture text -->

Gambar 2.27. _Sequence_ Profil _User_

Gambar di atas merupakan gambar dari _Sequence_ Profil _User_ yang menggambarkan interaksi antar objek pada saat pengguna membuka halaman profil _._

<!-- Start of picture text -->
Pengguna<br>x “Ubah Password<br>{Klik Halaman Ubah Password _! :<br>Tampil Form Ubah Password '<br>Isi Form :<br>|<br>Password Simpan Password Baru +<br>lama<br>sesuai]<br>[Password<br>lama tidak Gagal Ubah Password<br>sesuai] Gonna eee Renan nee e eee es seen eens eee<br><!-- End of picture text -->

Gambar 2.28. _Sequence_ Ubah _Password_

Gambar di atas merupakan _Sequence_ Diagram dari pengguna yang menjelaskan interaksi antar objek saat pengguna mengubah kata sandi.

<!-- Start of picture text -->
Pengguna<br>K<br>|_Klik Halaman Pengiriman & Pembayaran } :<br>Request data kurir | +<br>eeoeeeee--JampilDaftar Kurir |<br>Ubah Data Daftar Kurir<br>H Simpan Data Baru<br><!-- End of picture text -->

Gambar 2.29. _Sequence_ Ubah Pengiriman

Gambar di atas merupakan _Sequence_ Diagram dari pengguna yang menjelaskan interaksi antar objek saat pengguna mengubah data kurir yang digunakan.

<!-- Start of picture text -->
Pengguna<br>k<br>'Klik Halaman Pengiriman & Pembayaran : H<br>eeeeeeee---Jampil Halaman<br>aeroPilih Menu Pembayaran |<br>Request Data Pembayaran<br>Data Pembayaran <--- Data Pembayaran<br>Ubah Data Pembayaran<br>H Simpan Data Baru<br>: EEOer Tet<br><!-- End of picture text -->

Gambar 2.30. _Sequence_ Ubah Metode Pembayaran

Gambar di atas merupakan _Sequence_ Diagram dari pengguna yang menjelaskan interaksi antar objek saat pengguna mengubah metode pembayaran yang digunakan.

2) Admin

<!-- Start of picture text -->
‘Admin<br>k<br>{Klik Halaman Profil! H<br>Request Data Profil |<br>Tampil Data Profil ;<br><!-- End of picture text -->

Gambar 2.31. _Sequence_ Profil Admin

Gambar di atas merupakan gambar dari _Sequence_ Profil _Admin_ yang menggambarkan interaksi antar objek pada saat admin membuka halaman profil _._

<!-- Start of picture text -->
‘Admin<br>K Pengguna<br>{Klik Halaman Daftar Pengguna. } :<br>Request Data Pengguna !<br>H<br>_....Fampil Data Pengguna <--Data Pengguna |<br><!-- End of picture text -->

Gambar 2.32. _Sequence_ Daftar Pengguna

Gambar di atas merupakan gambar dari _Sequence_ daftar pengguna yang menggambarkan interaksi antar objek pada saat admin membuka halaman daftar pengguna

<!-- Start of picture text -->
‘Admin<br>Peta :Database<br>Persebaran<br>! Klik Halaman Peta Persebaran | '<br>Request Data Koordinat |<br><-- Data Koordinat___<br>_ Fampil Peta Dengan Koordinat _ H<br><!-- End of picture text -->

Gambar 2.33. _Sequence_ Peta Persebaran UMKM

Gambar di atas merupakan gambar dari _Sequence_ peta persebaran UMKM yang menggambarkan interaksi antar objek pada saat admin membuka halaman peta persebaran UMKM.

<!-- Start of picture text -->
‘Admin<br>K Pengajuan<br>{Klik Halaman Daftar UMKM |} :<br>Request Data UMKM | |<br>J<.-.---Tampil jc... Data UMKM<br>[ *) Setujui DataPengajuan UMKM<br>[Sesuai Update Status Toko<br>Persyaratan] |<.-.-Data UMKM Terbaru Status Bary<br>{Tidak Alasan Penolakan ,<br>Sesuai : Simpan Alasan<br>Persyaratan] } Hi H<br><!-- End of picture text -->

Gambar 2.34. _Sequence_ Kelola Pengajuan

Gambar di atas merupakan gambar dari _Sequence_ kelola pengajuan yang menggambarkan interaksi antar objek pada saat admin membuka halaman kelola pengajuan.

<!-- Start of picture text -->
:Kelola Aplikasi Database<br>‘agin i<br>i 1. Mengkiik Menu Kelola Aplikasi t<br>2. Mengambil Data<br>return<br>3. Menampilkan Halaman<br>Kelola Aplikasi<br>4. Mengklik Jenis Toko a<br>||| 5. MenampilkanJeni TokoHalaman |:<br>- . 7. Menampitkan Form<br>Tanton =<br>“anushe 8, Mengisi Form <— 9. Menyimpan Jenis Toko<br>}__YangYang DitambahkanDitambahkan<br>return<br>Ubah<br>Jens<br>tut<br>oko 6. Mengklik Salah Satu Jenis Toko 7. Mengambil Data Jenis Toko (|<br>>) 8. Menampitkan Jenis: Toko<br><— Yang Dipilih<br>Conattion 9. ubah Jenis Toko Sesuai Kebutuhan 10. Menyimpan Perubahan |<br>sonsUbahToko < a.J enis st TokoToko<br>Hapus i<br>‘Jone 9. Hapus Jenis Toko Yang Diinginkan 10. Menyimpan Perubahan |<br>et<br>Ta denis Toko (|<br><!-- End of picture text -->

Gambar 2.35. _Sequence_ Kelola Jenis Toko

Gambar di atas merupakan gambar dari _Sequence_ kelola jenis toko yang menggambarkan interaksi antar objek pada saat admin membuka halaman kelola jenis toko untuk mengelola jenis toko yang ada _._

<!-- Start of picture text -->
:kelola Aplikasi Database<br>i 1. Mengidik Menu Kelola Aplikast H H<br>2. Mengambil Data :<br>return<br>3. Menampitkan Halaman {|<br>Kelola Aplikasi ;<br>4. Mengklik Kategori Produk i<br>| > 5 Merametian tatenan |<br>“ 5 7. Menampilkan Form<br>Condition _ Kategori Produk i<br>=_— Renoisian Kategori Produk<br>Tamban | :<br>‘Yang Ditambahkan ¢<br>return<br>Uban 7<br>Kategon i<br>Produk 6. Mengklik Salah Satu Kategori Produk |<br>7. Mengambil Data Kategori Produk<br>tur<br>Conan l-> MenampikanYang DipiihKategor Produk|<br>ean 9. ubah Kategor! Produk Sesuai Kebutuban 10. MenyimpanKategori Produk Perubahan A |<br>kategon|<br>KaneoonHapus 9. Hapus Kategori Produk Yang Diinginkan 10. Menyimpan Perubahan i|<br>Produk eT Kategori Produk :<br>return<br><!-- End of picture text -->

Gambar 2.36. _Sequence_ Kelola Kategori Produk

Gambar di atas merupakan gambar dari _Sequence_ kelola kategori produk yang menggambarkan interaksi antar objek pada saat admin membuka halaman kelola jenis toko untuk mengelola kategori produk yang ada _._

<!-- Start of picture text -->
‘Admin<br>:KomplainPengguna :Database<br>! Klik Halaman Komplain Pengguna H H<br>Request Data Komplain |<br>STTampil Data Komplain .<br>Data Komplain<br>Le<br>Klik Halaman Detail<br>Request Data Detail<br>oes<br>Tampil Data Detail Komplain Lata Detail Komplain<br>Simpan Solusi<br>[Sesuai Setujui Pengajuan Komplain | smpan sous _|<br>Persyaratan]<br>[Tidak Tolak Pengajuan Komplain . .<br>Sesuai ; 7 ‘Simpan Status Komplain|<br>Persyaratan] H H ‘<br><!-- End of picture text -->

Gambar 2.37. _Sequence_ Komplain Pengguna

Gambar di atas merupakan gambar dari _Sequence_ komplain yang dilakukan oleh pengguna saat transaksi, dimana admin dapat melakukan aksi sesuai dengan ketentuan yang berlaku.

<!-- Start of picture text -->
Admin<br>‘Daftar<br>i . :Database<br>Transaksi<br>| Klik Halaman Daftar Transaksi | | '<br>Request Data Transaksi |<br>Tampil Data Transaksi 1<br>le < Data Transaksi<br><!-- End of picture text -->

Gambar 2.38. _Sequence_ Daftar Transaksi

Gambar di atas merupakan gambar dari _Sequence_ daftar transaksi yang menggambarkan interaksi antar objek pada saat admin membuka halaman daftar transaksi.

<!-- Start of picture text -->
Admin i | i i<br>5 Memil kelolatransaksi | | H<br>Menampian kel \ : i<br>Memiln menu kelola topup - i i<br>! Request<br>j | dala éJafar top op of<br>i Mengitim data<br>Mem data open | i i<br>|_eauest pou kontemas<br>: ‘Menampikan konfirmasi topup diterima H<br>at) [topup tidak aterima) | i H i<br>| Mem opus<br>ak teria i<br>Menino<br>a es<br>[topup diterima) ' ‘ Hi ‘<br>: Memilih topup ditenma + - H<br>H Memin "Yar i i<br>1 i i Muarirpen dais!<br><!-- End of picture text -->

Gambar 2.39. _Sequence_ Kelola _Top-Up_

Gambar di atas merupakan gambar dari _Sequence_ kelola _top-up_ yang menggambarkan interaksi antar objek pada saat admin membuka halaman kelola _top-up_ saat admin ingin mengelola _top-up_ yang telah dilakukan oleh pelaku UMKM.

<!-- Start of picture text -->
‘Admin<br>{ Klik Halaman Daftar UMKM H H<br>Request Data UMKM | }<br>Data UMKM<br>Tampil Data UMKM Soren<br><!-- End of picture text -->

Gambar 2.40. _Sequence_ Daftar UMKM

Gambar di atas merupakan gambar dari _Sequence_ daftar UMKM yang menggambarkan interaksi antar objek pada saat admin membuka halaman daftar UMKM.

<!-- Start of picture text -->
:Admin<br>‘DaftarTidak peAktif<br>‘Klik Halaman UMKM Tidak Aktif — | ; oot<br>Request Data UMKM Tidak Aktif |}<br>g.---- Data UMKM Tidak AKUF_ |<br>_Tampil<br>Data UMKM Tidak Aktif<br><!-- End of picture text -->

Gambar 2.41. _Sequence_ UMKM Tidak Aktif

Gambar di atas merupakan gambar dari _Sequence_ daftar UMKM tidak aktif dimana admin dapat melihat daftar UMKM yang tidak melakukan transaksi dalam jangka waktu tertentu sesuai dengan ketentuan yang berlaku.

# d. Class Diagram

<!-- Start of picture text -->
ee<br>fet<br>+ cant<br>ict int sees 0 producti + userid: int<br>‘+ min_atance:double ‘+ quantity: int — ent + updatePriced) ‘+ review text String<br>‘+ addttemtoCan() + int oe ene<br>— [swore] ssoinaera bmesmpraimeemed<br>wir nen<br>‘+ reason ‘string me + receipt_num: String<br>+ updateProcuet) + sau: Sting evidence Sting<br>[eee | + storecreat at e it  tmestano ‘ addProduct) = doltestreType) * rice: double + uploaged_at: timestamp<br>srenran + requestapprovald ost a [___Pamentno | te String + order int<br>+ = [se sae '<br>calculateTotastem() * store_ta: int sid ot ‘+ bank_name: String<br>+ status: String ‘+ bank_num: String<br>+ adéCouter() + balance double + stored: sting iat ven<br>+ removeCourier() + Mp: String ‘+ is_active: String ++ created_at timestamp ~<br>+icroated_s + pcatePaymentintod ~ payment<br>+ description: String<br>+ status: String<br>sage Sing + adaress_i: int i<br>i<br>+ persetujuan: String:<br>sonea Sena [-sascraune “seasons — —<br>cm se [everson] | | [:ormstonn<br>+ user ++ store_Id: int am ores ‘+id: int<br>_splaynotication() ‘+ createChatRoom() ++ latitude: double: + created_at: timestamp.<br>‘+ getChatRoom() ‘+ longitude double aymentintes + order_id: int<br>smete soon Seng<br>cay eit 0 stats: Sing<br>ema Sting + created_at tmestamp +province_j¢: int v= i + evidence: String<br>+ id: int<br>‘+ birth_date: Date + userid String<br>oe + changed_at timestamp<br>+ image. String + addaddress() ‘+ field: String<br><!-- End of picture text -->

Gambar 2.42. _Class_ Diagram

Gambar di atas merupakan gambar dari _Class_ Diagram dari rancangan aplikasi, yang

di mana terdapat 29 tabel yang saling berelasi.

e. Deployment Diagram

<!-- Start of picture text -->
<<device>><br>API server <<device>><br>Computer<br>cAttifacts Oo Lo<br>PostgreSQL <<device>><br>Computer<br>cAstifacts Qo Rest API ia)<br>index.js «Artifact»<br>Website Bisa UMKM.<br>«Components ]<br>UserController<br>cconponens<br>AdminController<br>sconponons =]<br>AuthController<br>Rest API<br><<device>><br>RajaOngkir<br>«Artifacts<br>Shipment Services<br><!-- End of picture text -->

Gambar 2.43. _Deployment_ Diagram

Gambar di atas merupakan gambar dari _Deployment_ Diagram dari aplikasi _back_

_office_ yang menggambarkan penempatan perangkat lunak aplikasi pada perangkat keras yaitu _server_

# f. Arsitektur Sistem

<!-- Start of picture text -->
—_ l=<br>=<br>&<br><!-- End of picture text -->

Gambar 2.44. Arsitektur Sistem

Gambar sebelumnya merupakan gambar dari arsitektur sistem aplikasi _back office_ , Sistem ini dirancang untuk mendukung dua peran utama, yaitu Admin dan pelaku UMKM, dengan fungsi masing-masing. Proses diawali dari halamn _login_ atau registrasi dengan verifikasi _email_ dan nomor HP. Pelaku usaha dapat membuat toko melalui proses validasi dan konfirmasi. Admin memiliki akses ke dasbor dengan visualisasi _business intelligence_ , meliputi data pendapatan, transaksi, statistik toko, dan grafik UMKM. Admin juga dapat mengelola jenis toko, kategori produk, pengiriman, transaksi, pengguna, dan data UMKM, termasuk lokasi UMKM melalui _Maps Marker_ .

- g. Desain Antarmuka

<!-- Start of picture text -->
Login<br>1 womtensn<br><!-- End of picture text -->

Gambar 2.45. Halaman _Login_

Gambar di atas merupakan rancangan desain antarmuka dari halaman _login_ dimana user bisa memasukkan _email_ dan _password_ , terdapat juga tombol untuk beralih ke halaman buka toko jika _user_ belum mempunyai akun

<!-- Start of picture text -->
Register<br>a<br><2)<br>f<s}<br><3}<br><3)<br>Alomat<br>eetLTEAS Fees<br>= ee. a<br>ge he By Ze} cat:<br>GIS Bie<br><!-- End of picture text -->

Gambar 2.46. Halaman Buka Toko

Gambar di atas merupakan rancangan desain antarmuka dari halaman buka toko dimana _user_ harus mengisi formulir yang diperlukan.

# 1) _User_

<!-- Start of picture text -->
Misono Profile<br>ae | 7<br>iS)<br><!-- End of picture text -->

Gambar 2.47. Halaman Profil UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman profil pengguna yang berisi informasi data diri dari toko yang telah didaftarkan.

<!-- Start of picture text -->
iiceerenene Pengiriman & Pembayaran<br>GED<br>Daftar Pengiriman<br>INEve<br>O ormes Thi<br>CD BD revrnenesia<br><!-- End of picture text -->

Gambar 2.48. Halaman Pengiriman dan Pembayaran

Gambar di atas merupakan rancangan desain antarmuka dari halaman pengiriman dan pembayaran yang digunakan pengguna untuk mengatur kurir dan metode pembayaran yang digunakan.

<!-- Start of picture text -->
Bilasnonremmons Ubah Password<br>’<br>[ == J<br><!-- End of picture text -->

Gambar 2.49. Halaman Ubah _Password_

Gambar di atas merupakan rancangan desain antarmuka dari halaman ubah _password_ yang digunakan pengguna untuk mengganti kata sandi akunnya.

- 2) Admin

<!-- Start of picture text -->
(i )seeorcemnnne Kelola Transaksi<br><!-- End of picture text -->

Gambar 2.50. Halaman Daftar Transaksi

Gambar di atas merupakan rancangan desain antarmuka dari halaman daftar transaksi

yang berada di menu transaksi, halaman ini berisi informasi mengenai transaksi pada aplikasi _mobile_ .

<!-- Start of picture text -->
Bilesmoeremnens mnie<br>Kelola Transaksi<br>7 [casae)<br>— | DattarTopUp E<br>: eee seooae © ret egErTe7e<br>; ee — 2 tre GD<br>, asptamber 2028 Toone 0200000 © op a nana ep<br>( )<br><!-- End of picture text -->

Gambar 2.51. Halaman Daftar _Top-up_

Gambar di atas merupakan rancangan desain antarmuka dari halaman daftar _top-up_

dimana terdapat informasi mengenai _top-up_ saldo yang dilakukan oleh UMKM.

<!-- Start of picture text -->
(i )sceorcennnne Kelola Aplikasi<br>Kota Ata I<br>; denis Toko @ G=<br>' Cl ep<br>a ‘tw @<br>‘<br>“ somone ep «am<br>: _ eg<br>, te ep<br><!-- End of picture text -->

Gambar 2.52. Halaman Jenis Toko

Gambar di atas merupakan rancangan desain antarmuka dari halaman jenis toko yang berisi daftar jenis toko yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Bipssmgeremnons ns<br>Kelola Aplikasi<br>; denis Toko 5 = TambahJens Toko<br>2 tin ep bad<br>. ‘ ep<br>oi ag «ee<br>, ve ap «a><br>St ==<br>° ne Con<br><!-- End of picture text -->

Gambar 2.53. Halaman Tambah Jenis Toko

Gambar di atas merupakan rancangan desain antarmuka dari halaman jenis toko (tambah) yang digunakan untuk menambahkan jenis toko yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Misses ns<br>Kelola Aplikasi<br>F Jeni Toko a<br>. 2idie cum=J<br>. me ep «a><br>. tesco ep<br>. Sd ep<br>° sve ep «a><br><!-- End of picture text -->

Gambar 2.54. Halaman Edit Jenis Toko

Gambar di atas merupakan rancangan desain antarmuka dari halaman jenis toko(edit) yang digunakan untuk mengubah informasi jenis toko yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Bi ipisnoerercusorpennone Kategori Produk<br>=<br>rota att I rattan mena tpi<br>a ae ep a><br>mecentino sonar mse<br>ee ea a><br><!-- End of picture text -->

Gambar 2.55. Halaman Kategori Produk

Gambar di atas merupakan rancangan desain antarmuka dari halaman kategori produk yang digunakan untuk menambahkan kategori produk yang ada pada aplikasi _mobile._

<!-- Start of picture text -->
Micsscereeisxopreninoac Komplain Pengguna<br>Komplain Pengguna a<br>a<br><!-- End of picture text -->

Gambar 2.56. Halaman Komplain Pengguna

Gambar di atas merupakan rancangan desain antarmuka dari halaman complain

pengguna yang berisi daftar komplain yang terjadi saat transaksi _._

<!-- Start of picture text -->
Bi lasnorremnons UMKM Tidak Aktif<br>Minimal Tidak Aki Kategori<br>= Daftar UMKM Tidak Aktif (Kategori 1) a<br>a<br><!-- End of picture text -->

Gambar 2.57. Halaman UMKM Tidak Aktif

Gambar di atas merupakan rancangan desain antarmuka dari halaman UMKM tidak aktif, yang berisi daftar UMKM yang tidak melakukan transaksi dalam jangka waktu yang ditentukan _._

<!-- Start of picture text -->
Bi jnssnonenmons Kelola Aplikasi<br>es<br>es<br><!-- End of picture text -->

Gambar 2.58. Halaman Kelola Saldo

Gambar di atas merupakan rancangan desain antarmuka dari halaman Kelola saldo, yang berisi informasi minimal saldo dan biaya admin yang dapat diubah oleh admin.

<!-- Start of picture text -->
ec Peta PersebaranUMKM<br>*<br>Bb Map<br>° aay x Nagin<br>i +) a! °" ata Meets<br>\*] 5 odes<br>: Onley Ea Salsbury 5<br>. a Robertson<br>Me<br>»« $Z)<br>\<br>a \ vw Sunnybank -$.secu<br>soon 3<br>CD 3 Oy, re 4 %wey,<br>Me. ge<br>ry Lee a ihalay Durack Leaflet| Map data © OpenStreetiiapG) contributors, CC-BY-SA,is Imagery@WNMapbox<br><!-- End of picture text -->

Gambar 2.59. Halaman Peta Persebaran UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman peta persebaran, yang berisi informasi geografis dari persebaran UMKM yang terdaftar.

<!-- Start of picture text -->
Kelola UMKM<br>Kola UMKM ‘<br>. Maneipine “ tion AM Aeon sme o © risoh sane ld ><br>— o —  meeima a -<br>sweat | weesonen on tana tate at On peu ><br>* ai po= mampe re er Sa =a oe om >><br>ste—sne “me —— tneee Ope2 Gece Come =¥<br>— =~ ce < a om .<br>in a pe ee ee — 5<br>te “ Oe /<br><!-- End of picture text -->

Gambar 2.60. Halaman Kelola UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman kelola UMKM, yang berisi informasi UMKM yang terdaftar pada aplikasi.

<!-- Start of picture text -->
Biipisxorrenwons Detail UMKM<br>= Deskripsi<br>~<br>o8aiz3916241<br>=) | Atrat<br>ee ec»<br>ep ee»<br>we<br>ep<br>Datta Perubahan<br><!-- End of picture text -->

Gambar 2.61. Halaman Detail UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman detail UMKM, yang berisi informasi dari detail dari UMKM _._

<!-- Start of picture text -->
Mi pseorcenone Daftar Pengajuan<br>Kola UMKM &<br>rae rod Aerie A hogar A Aneareh sonesazasa cy ea»<br>se ~ ie)<br>eters = raen ase ater ne Py aD<br>vena FRO ews see eta neta aoe ™ ace<br>ee enn eran Angee Argent sanasnens es =D<br>venue ney Crem ap ane ecsea —< §==><br>onus 20 Aaet we acanthan kam eo serena “ ee<br><!-- End of picture text -->

Gambar 2.62. Halaman Pengajuan UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman pengajuan, yang berisi informasi dari UMKM yang telah mengajukan pendaftaran buka toko.

<!-- Start of picture text -->
Bi jnssnonenmons Detail Pengajuan<br>var vs Nama Peri<br>—_ Deskripsi<br>ws | Noocezsowe Telepon<br>wna<br>Kw Foto<br>ep GD<br>we soma<br>ea eG»<br>wwe<br>ea<br><!-- End of picture text -->

Gambar 2.63. Halaman Detail Pengajuan UMKM

Gambar di atas merupakan rancangan desain antarmuka dari halaman detail pengajuan, yang berisi informasi detail dari pengajuan buka toko.

<!-- Start of picture text -->
i [pisnonreninoac Daftar Pengguna<br>Daftar Pengguna ;<br><!-- End of picture text -->

Gambar 2.64. Halaman Daftar Pengguna

Gambar di atas merupakan rancangan desain antarmuka dari halaman daftar pengguna, yang berisi informasi daftar pengguna yang terdaftar pada aplikasi _mobile_ tetapi tidak memiliki toko.

<!-- Start of picture text -->
5 [Piswoprenwone Profile<br>ig<br><!-- End of picture text -->

Gambar 2.65. Halaman Profil Admin

Gambar di atas merupakan rancangan desain antarmuka dari halaman profil admin _,_ yang berisi informasi data diri admin.

# 2.6 Rencana Pengujian Proyek

Pengujian sistem dilakukan untuk memastikan bahwa seluruh fungsi dalam aplikasi back office UMKM Kabupaten Serang berjalan sesuai dengan kebutuhan pengguna dan spesifikasi yang telah dirancang. Metode pengujian yang digunakan adalah _Black Box Testing_ , yaitu pengujian yang berfokus pada fungsi dari sistem tanpa memperhatikan struktur internal program.

Pengujian dilakukan berdasarkan beberapa skenario utama yang mencakup interaksi antara aktor (admin dan user) dengan fitur-fitur sistem, mulai dari proses login hingga pengelolaan data. Berikut adalah daftar skenario pengujian yang digunakan:

Tabel 2.1. _Black Box Testing_

|No.|Aktor|Skenario|Hasil yang diharapkan|
|---|---|---|---|
|1|Admin,|Melakukan_login_|Berhasil login sesuai dengan|
||_User_||informasi yang di_input_pada|
||||form_login_|

|2|Admin,<br>_User_|Melakukan_logout_|Berhasil keluar dari ap<br>web setelah menekan to<br>logout|likasi<br>mbol|
|---|---|---|---|---|
|3|_User_|Melakukan<br>pendaftaran<br>UMKM|Berhasil menyimpan<br>UMKM<br>sesuai<br>de<br>informasi yang telah di|data<br>ngan<br>_input_|
|4|_User_|Melakukan<br>perbaikan data|Berhasil<br>melak<br>perbaikan data pendaf<br>yang salah|ukan<br>taran|
|5|Admin,<br>_User_|Membuka menu<br>profil|Berhasil<br>menamp<br>informasi akun sesuai<br>yang telah di_input_ <br>formulir_login_|ilkan<br>data<br>pada|
|6|Admin|Melihat<br>daftar<br>jenis UMKM|Berhasil menampilkan<br>jenis UMKM|data|
|7|Admin|Menambah<br>data<br>jenis UMKM|Berhasil<br>menambah<br>jenis UMKM|data|
|8|Admin|Menghapus jenis<br>UMKM|Berhasil menghapus<br>UMKM yang dipilih|jenis|
|9|Admin|Melihat<br>daftar<br>kategori produk|Berhasil menampilkan<br>kategori produk|data|
|10|Admin|Menambah<br>data<br>kategori produk|Berhasil<br>menambah<br>kategori produk|data|
|11|Admin|Menghapus data<br>kategori produk|Berhasil menghapus<br>kategori produk yang d|data<br>ipilih|
|12|Admin|Melihat<br>data<br>biaya<br>admin,|Berhasil melihat data<br>admin,<br>minimal|biaya<br>saldo|
|||minimal<br>saldo|pengguna<br>dan|batas|
|||pengguna<br>dan|maksimal<br>konfi|rmasi|
|||batas<br>maksimal<br>konfirmasi<br>pesanan diterima|pesanan diterima||

|13|Admin|Mengubah biaya<br>admin|Berhasil mengubah besaran<br>biaya admin|
|---|---|---|---|
|14|Admin|Mengubah<br>minimal<br>saldo<br>pengguna|Berhasil mengubah besaran<br>minimal saldo pengguna|
|15|Admin|Mengubah batas<br>maksimal<br>konfirmasi<br>pesanan diterima|Berhasil mengubah batas<br>maksimal<br>konfirmasi<br>penerimaan pesanan|
|16|Admin|Melihat<br>daftar<br>transaksi<br>pengguna|Berhasil menampilkan data<br>transaksi|
|17|Admin|Melihat<br>daftar<br>_top-up_UMKM|Berhasil menampilkan data<br>_top-up_UMKM|
|18|Admin|Menyetujui_top-_<br>_up_UMKM|Berhasil menyetujui_top-up_<br>UMKM|
|19|Admin|Menolak<br>_top-up_<br>UMKM|Berhasil<br>menolak<br>_top-up_<br>UMKM|
|20|Admin|Membuka menu<br>peta<br>persebaran<br>UMKM|Berhasil menampilkan titik –<br>titik lokasi UMKM yang<br>terdapat di peta|
|21|Admin|Menampilkan<br>data<br>pengajuan<br>pendaftaran<br>UMKM|Berhasil menampilkan data<br>pengajuan<br>pendaftaran<br>UMKM|
|22|Admin|Menyetujui data<br>pengajuan<br>pendaftaran<br>UMKM|Berhasil menyetujui data<br>pengajuan<br>pendaftaran<br>UMKM|
|23|Admin|Menolak<br>data<br>pengajuan<br>pendaftaran<br>UMKM|Berhasil<br>menolak<br>data<br>pengajuan<br>pendaftaran<br>UMKM|

|24|Admin|Menampilkan<br>daftar<br>UMKM<br>tidak aktif|Berhasil menampilkan daftar<br>UMKM tidak aktif|
|---|---|---|---|
|25|Admin|Menonaktifkan<br>UMKM<br>yang<br>sudah tidak aktif|Berhasil<br>menonaktifkan<br>UMKM yang tidak aktif|
|26|Admin|Membuka menu<br>daftar pengguna|Berhasil menampilkan daftar<br>pengguna<br>yang<br>telah<br>terdaftar pada aplikasi_e-_<br>_commerce mobile_|
|27|_User_|Menampilkan<br>data daftar kurir<br>yang digunakan|Berhasil Menampilkan data<br>daftar kurir yang digunakan|
|28|_User_|Mengubah daftar<br>kurir<br>yang<br>digunakan|Berhasil Mengubah daftar<br>kurir yang digunakan|
|29|_User_|Menampilkan<br>data<br>metode<br>pembayaran|Berhasil Menampilkan data<br>metode pembayaran|
|30|_User_|Menambahkan<br>data<br>metode<br>pembayaran|Berhasil Menambahkan data<br>metode pembayaran|
|31|_User_|Mengubah<br>data<br>metode<br>pembayaran|Berhasil<br>Mengubah<br>data<br>metode pembayaran|
|32|_User_|Mengubah profil<br>data UMKM|Berhasil Mengubah profil<br>data UMKM|
|33|_User_|Mengubah<br>_password_|Berhasil<br>mengubah<br>_password_akun|


# PROYEK PEMBUATAN DASHBOARD BUSINESS INTELLIGENCE DISKOUMPERINDAG KABUPATEN SERANG

# **BAB II RANCANGAN PROYEK**

# **2.1. Observasi**

Observasi dilakukan untuk memahami alur kerja sistem yang sedang berjalan pada pelaku UMKM, khususnya dalam proses pendaftaran dan validasi toko. Dengan melakukan observasi ini, diharapkan dapat diketahui titik-titik kritis, hambatan, serta potensi yang dapat dikembangkan lebih lanjut dalam sistem yang akan dirancang.

<!-- Start of picture text -->
Pelaku UMKM<br>Melakukan Registrasi<br>Toko<br>‘Admin Akan Mengecek<br>Validasi Data<br><> TIDAK VALID<br>VALID<br>Admin Dinas Melakukan<br>Pencatatan Data Manual<br>Pelaku UMKM<br>Melakukan Proses Jual<br>Beli<br>Pelaku UMKM<br>Melakukan Pencatatan<br>Transaksi Manual<br>Pelaku UMKM<br>Melakukan Analisis<br>Penjualan Manual<br>Pelaku UMKM<br>Melakukan Pengambilan<br>Keputusan<br><!-- End of picture text -->

Gambar 2.1 Proses Bisnis Sistem yang Berjalan Pelaku UMKM

Proses bisnis yang sedang berjalan untuk pelaku UMKM dimulai dengan tahap pendaftaran toko. Pelaku UMKM melakukan registrasi toko, kemudian admin

memeriksa validitas data yang diajukan. Jika data tersebut tidak valid, pelaku UMKM perlu memperbaiki data registrasi dan mengulang proses validasi. Apabila data dinyatakan valid, admin Dinas DISKOUMPERINDAG melakukan pencatatan data secara manual.

Setelah data registrasi dicatat, pelaku UMKM dapat melakukan proses jual beli di platform. Namun, pencatatan transaksi masih dilakukan secara manual oleh pelaku UMKM, sehingga setiap transaksi memerlukan pengolahan data yang terpisah dan nonterintegrasi. Tahap berikutnya, pelaku UMKM melakukan analisis penjualan secara manual berdasarkan data transaksi yang telah dicatat, yang memerlukan waktu dan usaha ekstra untuk menilai performa bisnis mereka.

<!-- Start of picture text -->
‘Admin Dinas Melakukan<br>Pencatatan Data Pelaku<br>UMKM Manual<br>Pelaku UMKM<br>Melakukan Proses Jual<br>Beli<br>‘Admin Dinas Menerima<br>Laporan Penjualan<br>Masing-Masing Toko<br>‘Admin Dinas Melakukan<br>Analisis Laporan<br>Penjualan Setiap Toko<br>‘Admin Melakukan<br>Pengambilan Keputusan<br><!-- End of picture text -->

Gambar 2.2 Proses Bisnis Sistem yang Berjalan Admin DISKOUMPERINDAG

Sistem pengelolaan data di DISKOUMPERINDAG Kabupaten Serang sebelumnya dilakukan secara manual dan terfragmentasi. Data terkait koperasi, UMKM, perindustrian, dan perdagangan disimpan dalam format yang berbeda-beda, tersebar di berbagai departemen, dan diolah secara terpisah. Setiap unit kerja memiliki cara masingmasing dalam mengumpulkan, menyimpan, dan menganalisis data, sehingga

menyulitkan proses konsolidasi dan integrasi data untuk pelaporan dan pengambilan keputusan.

Admin DISKOUMPERINDAG menerima laporan penjualan yang dikirimkan secara manual oleh masing-masing toko. Laporan ini dikumpulkan secara berkala dan kemudian diolah oleh admin. Proses ini melibatkan analisis laporan penjualan dari setiap toko untuk mengevaluasi performa dan tren penjualan.

Setelah menganalisis laporan penjualan, admin DISKOUMPERINDAG membuat keputusan terkait kebijakan atau strategi yang perlu diterapkan. Keputusan ini diambil berdasarkan hasil analisis data yang dikumpulkan, dengan tujuan meningkatkan performa sektor UMKM dan perdagangan di wilayah tersebut. Proses manual ini cukup memakan waktu dan rentan terhadap kesalahan, sehingga memperlambat respons dalam pengambilan keputusan strategis.

Berikut kelemahan pada sistem pengelolaan data di DISKOUMPERINDAG Kabupaten Serang berdasarkan metode PIECES (Performance, Information, Economy, Control, Efficiency, Service):

1. Performance (Kinerja)

Sistem manual yang berjalan saat ini memiliki kinerja yang rendah karena memerlukan banyak waktu untuk mengumpulkan, memproses, dan membuat laporan. Tidak adanya otomatisasi membuat kinerja sistem lambat, terutama ketika menangani data dalam jumlah besar.

2. Information (Informasi)

Kualitas informasi yang dihasilkan seringkali kurang akurat dan tidak realtime. Informasi yang dikumpulkan secara manual oleh masing-masing admin dinas menyebabkan inkonsistensi dan duplikasi data, yang mengurangi keakuratan laporan serta analisis.

3. Economy (Ekonomi)

Pengelolaan data manual membutuhkan biaya tambahan untuk sumber daya manusia dan infrastruktur pendukung serta biaya waktu yang dihabiskan untuk pengolahan data.

4. Control (Pengendalian)

Kontrol terhadap data sulit dilakukan karena data yang diperlukan harus dilakukan secara manual dengan meminta masing-masing pelaku UMKM. Hal

ini mengakibatkan sulitnya melacak sumber kesalahan atau memastikan validitas data.

5. Efficiency (Efisiensi)

Sistem manual menghabiskan banyak waktu dan tenaga. Proses pengolahan data, pembuatan laporan, dan analisis sangat lambat, sehingga menurunkan efisiensi operasional. Ketergantungan pada metode manual memperlambat respons terhadap kebutuhan informasi mendadak.

6. Service (Layanan)

Sistem yang berjalan sekarang menyulitkan DISKOUMPERINDAG dalam memberikan layanan yang cepat dan responsif. Pelaporan dan evaluasi kinerja memakan waktu yang lama, sehingga mengurangi kemampuan instansi untuk memberikan layanan yang tepat waktu kepada pelaku UMKM.

# **2.2. Usulan Solusi**

Sistem baru yang diusulkan adalah pengembangan _Dashboard Business Intelligence_ (BI) yang terintegrasi, yang mampu mengumpulkan dan menyajikan data secara real-time dari berbagai sumber yang ada di DISKOUMPERINDAG. _Dashboard_ ini dirancang untuk mengintegrasikan data yang berasal dari aplikasi _mobile E- Commerce_ yang sedang dikembangkan. Dengan _Dashboard Business Intelligence_ , data yang sebelumnya tersebar dapat dikumpulkan dalam satu platform yang terpusat, diolah secara otomatis, dan disajikan dalam bentuk visualisasi yang mudah dipahami oleh pelaku UMKM dan Dinas.

<!-- Start of picture text -->
Pelaku UMKM<br>Melakukan Registrasi<br>Te<br>Sistem Menerima Data<br>Toko<br>‘Admin Akan Mengecek<br>Valdas! Date<br><> THOAK VALID<br>m0<br>Pelaku UMKM Dapat<br>Melakukan Proses Jual<br>Beli pada Aplikasi E-<br>commerce<br>Pelaku UMKM dapat<br>Halfat Dea Anahi<br>Transaksi Pada Website<br>Pelaku UMKM Membuat<br>IKeputusan untuk Strategi<br>Penjualan<br><!-- End of picture text -->

Gambar 2.3 Proses Bisnis Usulan Solusi Pelaku UMKM

Dimulai dengan pelaku UMKM yang melakukan pendaftaran toko secara online. Sistem kemudian menerima data registrasi dari pelaku UMKM dan mencatatnya dalam basis data. Selanjutnya, admin akan memeriksa dan memvalidasi data yang telah dikirimkan oleh pelaku UMKM untuk memastikan kebenaran dan kelengkapan informasi. Jika data yang diperiksa oleh admin tidak valid, pelaku UMKM akan diminta untuk memperbaiki dan mengirimkan kembali data tersebut.

Apabila data dinyatakan valid, pelaku UMKM diizinkan untuk memulai proses jual beli di dalam aplikasi _E-Commerce_ . Setelah terdaftar dan aktif dalam ekosistem _ECommerce_ , pelaku UMKM memiliki akses ke data analitik transaksi yang tersedia di website _Dashboard Business Intelligence_ (BI). Data analitik ini mencakup berbagai

informasi penting, seperti tren penjualan, produk paling diminati, serta performa penjualan secara keseluruhan.

Dengan akses ke data analitik yang real-time dan terintegrasi, pelaku UMKM dapat memanfaatkan informasi tersebut untuk membuat keputusan strategis yang lebih tepat guna dalam upaya meningkatkan penjualan. Langkah ini diharapkan dapat membantu pelaku UMKM merumuskan strategi yang lebih efektif dan efisien dalam mengembangkan bisnis mereka di platform _E-Commerce_ . Proses ini berakhir ketika pelaku UMKM mampu mengambil keputusan yang mendukung pertumbuhan dan kesuksesan bisnis mereka.

<!-- Start of picture text -->
Pelaku UMKM<br>Melakukan Proses Jual<br>Beli pada Aplikasi E-<br>commerce<br>JAdmin Memonitor Proses|<br>Jual Beli<br>Admin dapat Melihat<br>Data Analitik Transaksi<br>Pada Website<br>‘Admin Melakukan<br>Pengambilan Keputusan<br><!-- End of picture text -->

Gambar 2.4 Proses Bisnis Usulan Solusi Admin DISKOUMPERINDAG

Selain pelaku UMKM, Dinas DISKOUMPERINDAG juga memiliki akses ke _Dashboard Business Intelligence_ (BI) yang dirancang untuk menampilkan data analitik komprehensif dari semua toko yang terdaftar di aplikasi _E-Commerce_ . Sistem baru ini memungkinkan pemantauan indikator kinerja utama secara real-time, memfasilitasi evaluasi kinerja secara berkala, dan menghasilkan laporan yang dapat diakses kapan saja oleh pengambil keputusan. Hal ini membantu DISKOUMPERINDAG untuk merespons perubahan dengan cepat, merencanakan strategi yang lebih efektif, dan meningkatkan transparansi serta akuntabilitas dalam pelaporan. Dengan adanya integrasi antara aplikasi _mobile E-Commerce_ dan _Dashboard Business Intelligence_ di _back office_ , sistem

ini dapat memberikan gambaran menyeluruh tentang kondisi koperasi, UMKM, perindustrian, dan perdagangan di Kabupaten Serang, sehingga pengambilan keputusan dapat didasarkan pada data yang akurat dan up-to-date.

# **2.3. Analisis Kebutuhan Sistem**

Analisis kebutuhan sistem dilakukan untuk merumuskan spesifikasi yang harus dipenuhi dalam pengembangan _Dashboard Business Intelligence_ (BI) yang akan digunakan oleh DISKOUMPERINDAG Kabupaten Serang. Analisis ini mencakup kebutuhan fungsional dan non-fungsional yang akan menjadi acuan dalam proses perancangan dan pengembangan sistem. Identifikasi kebutuhan dilakukan berdasarkan hasil observasi, wawancara, serta studi terhadap proses bisnis yang sedang berjalan.

# **2.2.1. Identifikasi Kebutuhan Fungsional**

Kebutuhan fungsional merujuk pada fitur dan kapabilitas yang harus dimiliki oleh _Dashboard Business Intelligence_ (BI) agar dapat memenuhi tujuan proyek di DISKOPUMPERINDAG Kabupaten Serang. Berikut adalah beberapa kebutuhan fungsional yang diidentifikasi:

1. _Dashboard_ harus dapat mengintegrasikan data dari berbagai sumber internal di DISKOPUMPERINDAG, termasuk data yang berasal dari aplikasi _mobile E- Commerce_ .

2. Sistem harus mampu menyajikan data secara real-time, sehingga pengguna dapat memantau perkembangan koperasi, UMKM, industri, dan perdagangan tanpa keterlambatan.

3. Menyediakan fitur visualisasi data seperti grafik, tabel, dan diagram yang mudah dipahami untuk membantu analisis kinerja.

4. Menyediakan fitur filter untuk memudahkan pengguna dalam menelusuri data tertentu.

5. Memungkinkan pengguna untuk mengekspor data atau laporan ke berbagai format seperti PDF atau Excel untuk kebutuhan pelaporan lebih lanjut.

# **2.2.2. Identifikasi Kebutuhan Non-Fungsional**

Kebutuhan non-fungsional berkaitan dengan aspek kualitas dan standar yang harus dipenuhi oleh sistem agar berfungsi dengan baik. Beberapa kebutuhan non-fungsional yang diidentifikasi antara lain:

1. Keamanan

Sistem harus dilengkapi dengan mekanisme keamanan yang mumpuni, termasuk autentikasi dan otorisasi pengguna, untuk memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses data sensitif.

2. Keandalan

_Dashboard_ harus mampu beroperasi secara stabil dan konsisten, tanpa gangguan atau penurunan performa yang signifikan, bahkan ketika menangani volume data yang besar.

3. Skalabilitas

Sistem harus dapat menangani peningkatan jumlah data atau pengguna di masa depan tanpa mempengaruhi kinerja.

4. Kemudahan Penggunaan

Antarmuka _Dashboard_ harus intuitif dan user-friendly, sehingga pengguna dari berbagai latar belakang teknis dapat menggunakannya dengan mudah.

5. Performa

Sistem harus mampu memproses dan menyajikan data dengan cepat, tanpa mengalami keterlambatan yang dapat mengganggu pengguna dalam melakukan analisis atau pengambilan keputusan.

# **2.2.3. Analisis Pengguna**

Pengguna _Dashboard Business Intelligence_ (BI) pada DISKOPUMPERINDAG Kabupaten Serang terdiri dari dua tipe, yaitu Admin Dinas dan Penjual UMKM. Masing-masing pengguna memiliki akses dan kebutuhan yang berbeda terhadap fitur-fitur yang disediakan dalam _dashboard_ , sesuai dengan peran dan tanggung jawab mereka.

# **1. Admin Dinas**

Admin bertanggung jawab atas pemantauan keseluruhan kinerja UMKM dan perdagangan di aplikasi _E-Commerce_ . Mereka memerlukan visualisasi data yang memberikan gambaran tentang performa aplikasi secara keseluruhan. Adapun informasi yang tersedia bagi Admin dalam _Dashboard Business Intelligence_ meliputi:

● **Total Pendapatan Masuk (harian, mingguan, bulanan)** Visualisasi ini membantu admin DISKOPPERINDAG dalam memantau pendapatan yang masuk ke dinas dari admin fee transaksi UMKM secara langsung dan aktual. Dengan informasi yang real-

time, dinas bisa mengetahui kondisi pemasukan setiap saat tanpa harus menunggu laporan manual.

- **Total Transaksi**

Memantau volume transaksi dalam berbagai periode waktu untuk menganalisis pertumbuhan dan tren penjualan. Visualisasi data ini membantu admin dalam memahami fluktuasi penjualan dan mengevaluasi performa aplikasi secara berkala.

- **Total Toko**

Menyajikan jumlah total toko aktif yang terdaftar dalam platform. Data ini berguna untuk mengetahui seberapa banyak pelaku usaha yang berpartisipasi aktif di aplikasi.

- **Total Pengguna Aktif**

Memantau jumlah pengguna yang aktif dalam periode tertentu untuk mengukur tingkat partisipasi.

- **Kategori Produk**

Memberikan informasi mengenai kategori produk yang paling banyak diminati oleh pengguna, sehingga membantu dalam memahami preferensi pasar.

- **Top 5 Toko Berdasarkan Penjualan**

   - Menunjukkan toko dengan performa penjualan terbaik, membantu admin dalam mengidentifikasi toko unggulan yang bisa dijadikan contoh atau direkomendasikan kepada pengguna lain.

- **Top 5 Barang Penjualan Terlaris**

Menampilkan barang yang paling laris di platform, membantu admin dalam memantau permintaan pasar dan menyediakan data penting untuk analisis tren penjualan.

- **Top 10 Pengguna**

Menampilkan daftar 10 pengguna yang paling aktif melakukan transaksi di aplikasi. Setiap pengguna dalam daftar ini memiliki opsi untuk melihat Detail Daftar Transaksi yang mencakup informasi lengkap mengenai aktivitas pembelian mereka. Visualisasi ini membantu admin dalam menganalisis perilaku pengguna aktif,

memahami tren pembelian, serta mengevaluasi kontribusi mereka terhadap peningkatan performa aplikasi.

- **Total Pendaftar UMKM**

   - Memberikan informasi mengenai jumlah UMKM baru yang terdaftar, membantu admin menilai perkembangan partisipasi UMKM.

- **Toko Tidak Aktif**

Memberikan informasi mengenai persentase toko tidak aktif yang dibagi menjadi beberapa kategori beserta daftar-daftar toko. Visualisasi ini dapat membantu admin dalam menganalisis terkait ketidakaktifan toko dan dapat melakukan observasi dan pelatihan untuk toko-toko yang tidak aktif.

# **2. Pelaku UMKM**

Pelaku UMKM adalah pelaku usaha yang menggunakan _Dashboard Business Intelligence_ untuk memantau perkembangan bisnis mereka. Mereka membutuhkan akses ke data yang lebih mendalam tentang performa toko dan produk mereka, meliputi:

- **Total Penjualan atau Transaksi (harian, mingguan, bulanan)** Menyediakan informasi tentang volume penjualan mereka dalam periode tertentu.

- **Total Pendapatan**

Menyajikan data total pendapatan untuk memudahkan pelaku usaha menilai keuntungan.

- **Total Barang Terjual** Memberikan informasi mengenai total barang yang telah terjual untuk melihat tingkat permintaan produk.

- **Top 5 Produk Berdasarkan Penjualan** Menunjukkan produk yang paling laris untuk membantu mereka dalam memfokuskan strategi pemasaran.

- **Top 10 Pembeli**

   - Menampilkan daftar 10 pembeli dengan jumlah transaksi terbanyak di toko UMKM tersebut. Setiap pembeli dalam daftar ini dilengkapi dengan opsi untuk melihat Detail Daftar Transaksi yang telah dilakukan di toko mereka. Fitur ini membantu pelaku UMKM dalam

menganalisis perilaku pelanggan setia, memahami preferensi produk yang mereka beli, dan membangun strategi pemasaran yang lebih efektif, seperti pemberian promo atau diskon khusus untuk pembeli terbaik.

- **Transaksi Terakhir**

   - Menyediakan riwayat penjualan yang detail untuk evaluasi dan analisis mendalam.

- **Pengelolaan Pesanan** Menampilkan status pesanan, termasuk barang yang harus dikirim dan yang sudah terkirim, untuk membantu penjual dalam pengelolaan logistik.

- **Partisipasi Pembeli**

   - Menampilkan total pembeli pada setiap bulannya dalam dashboard pelaku UMKM berfungsi sebagai alat analisis untuk memahami perilaku konsumen dari waktu ke waktu. Dengan visualisasi ini, pelaku UMKM dapat melihat tren peningkatan atau penurunan jumlah pembeli setiap bulan secara jelas dan cepat. Informasi ini sangat penting untuk mengevaluasi efektivitas strategi pemasaran dan penjualan yang telah diterapkan.

- **Kategori Produk**

   - Memberikan informasi mengenai kategori produk yang paling banyak diminati oleh pengguna, sehingga membantu dalam memahami preferensi pasar.

Dengan informasi ini, baik Admin maupun Pelaku UMKM dapat menjalankan tugasnya dengan lebih efektif, memanfaatkan data untuk mengambil keputusan yang strategis, serta meningkatkan kinerja dan produktivitas masingmasing.

# **2.4. Kerangka Berpikir**

Kerangka berpikir disusun untuk memberikan gambaran alur logis dari proses pengembangan sistem hingga tercapainya tujuan utama proyek. Melalui kerangka ini, dapat dilihat hubungan antara aktor pengguna, alur proses, serta output yang dihasilkan. Gambar 2.5 berikut menyajikan kerangka berpikir sistem yang akan dibangun, dengan

memperjelas peran masing-masing pengguna dan bagaimana data diproses serta disajikan melalui _Dashboard Business Intelligence_ (BI).

<!-- Start of picture text -->
TasiboaningenceBisbee Tashoardintgoncebisbess<br>o Top tare |[ Tor | Tercera Tobaaw || 0910 | sme O<br>Pavia || resber_|| “ani Ponkton_||_Pemvet es<br>pewumn | [Toa] To ]| Tor arora a ae<br>Pendapatan || Penjualan Terjual Masuk Transaksi Admin<br>Faispast || ram || Pangacioan Farispast || Pendatar ]| Kasson<br>ombot_|[Pengapaan || Pesonan Penesuna || “umon || Proau<br>Kategon<br>ose<br>Database<br>2. Transaksi 1.User<br>3. Toko<br>4. Kategori Produk<br>5. Produk<br>6. Review<br><!-- End of picture text -->

Gambar 2.5 Kerangka Berpikir

Sistem ini dirancang untuk melayani dua jenis pengguna utama yaitu pelaku UMKM dan Admin DISKOUMPERINDAG. Proses awal penggunaan dimulai dengan tahap pendaftaran (register) dan masuk (login), di mana pengguna harus terlebih dahulu mengautentikasi diri. Setelah masuk, pelaku UMKM akan dapat mengakses _dashboard_ yang menyediakan berbagai fitur seperti laporan total pendapatan, total penjualan, barang terjual, serta visualisasi data seperti grafik pendapatan dan partisipasi pembeli. Fitur-fitur lainnya termasuk top barang penjualan, daftar 10 pembeli utama, riwayat transaksi terakhir, serta pengelolaan pesanan. Di sisi lain, Admin memiliki akses langsung ke _dashboard_ tanpa melakukan registrasi yang memungkinkan mereka memantau data secara menyeluruh, seperti total transaksi, total toko, total pengguna aktif, kategori produk populer, dan pendaftar UMKM. Data dari kedua jenis pengguna ini dikumpulkan dalam database terpusat yang mencakup informasi penting seperti data pengguna, transaksi, toko, produk, kategori produk, dan ulasan. Alur data yang dihasilkan dari interaksi pengguna diproses dan divisualisasikan dalam bentuk _dashboard_ , memfasilitasi analisis dan pengambilan keputusan secara efektif. Dengan

kerangka ini, _Dashboard Business Intelligence_ dapat menjadi alat yang bermanfaat untuk meningkatkan efisiensi operasional dan menyediakan informasi yang relevan bagi para pelaku UMKM dan Admin DISKOUMPERINDAG.

# **2.5. Rancangan Proyek**

Rancangan proyek merupakan tahap penting dalam pengembangan sistem yang bertujuan untuk memastikan setiap komponen dirancang secara sistematis dan sesuai dengan kebutuhan pengguna. Pada bagian ini, dijelaskan metode pengembangan sistem yang digunakan, desain arsitektur informasi, pemodelan sistem, desain antarmuka pengguna, serta rencana pengujian proyek. Setiap sub bagian disusun untuk memberikan gambaran menyeluruh tentang bagaimana sistem akan dibangun, diimplementasikan, dan diuji sebelum digunakan secara penuh.

# **2.5.1. Metode Pengembangan Sistem**

Proyek pembuatan _Dashboard Business Intelligence_ (BI) di DISKOUMPERINDAG Kabupaten Serang menggunakan metode pengembangan Agile. Metode ini dipilih karena fleksibilitas dan kemampuannya dalam mengakomodasi perubahan kebutuhan secara cepat serta memungkinkan kolaborasi yang lebih baik di antara anggota tim. Agile memungkinkan kolaborasi yang intensif antar anggota tim yang berbeda tugas, yakni tim yang membuat aplikasi mobile E-Commerce dan tim yang mengembangkan backoffice website.

<!-- Start of picture text -->
SPRINT<br>RETROSPECTIVE<br>BACKLOGPRODUCT SCRUM,DAILY<br>ELARwnTeuloence UM =>) ptanninsSPRINT |=) sacktosSPRINT / SCRUM TEAM >K>nena REVIEWSPRINT<br>DASHBOARD<br>INTELLIGENCE<br>Au _<br><!-- End of picture text -->

Gambar 2.6 Metode Pengembangan Sistem _Agile_

Dengan metode ini, seluruh tim dapat terus berkoordinasi, saling berbagi progres, dan menyinkronkan pekerjaan mereka untuk memastikan bahwa pengambilan data dari aplikasi _mobile_ berjalan lancar dan terintegrasi

dengan _Dashboard Business Intelligence_ di _back office_ . Berikut ini penjelasan masing-masing elemen dalam metode _Agile_ yang digunakan pada proyek ini:

# **1. Product Backlog**

Product backlog adalah daftar prioritas kebutuhan yang harus dikembangkan dalam proyek. Pada proyek ini, product backlog mencakup:

- a. _Dashboard_ BI untuk Admin, dengan fitur seperti pendapatan masuk, total toko, total transaksi, total partisipasi pengguna, kategori produk populer, top toko berdasarkan penjualan, top 5 barang penjualan terlaris, top 10 pengguna dan total pendaftar UMKM.

- b. _Dashboard_ BI untuk Pelaku UMKM, dengan fitur seperti total pendapatan, total transaksi, total barang terjual, top produk berdasarkan penjualan, transaksi terakhir, kategori produk populer dan pengelolaan pesanan (barang yang harus dikirim dan sudah dikirim).

# **2. Sprint Planning**

Sprint Planning Sprint planning dilakukan di awal setiap sprint untuk merencanakan pekerjaan yang akan dikerjakan dalam sprint tersebut. Tim menentukan item dari product backlog yang akan dimasukkan ke dalam sprint backlog berdasarkan prioritas dan kapasitas tim. Fokusnya adalah memilih fitur yang dapat diselesaikan terlebih dahulu, untuk di _dashboard_ sendiri seperti pengembangan visualisasi data tertentu untuk _dashboard_ admin atau penjual UMKM.

# **3. Sprint Backlog**

Sprint Backlog Sprint backlog berisi daftar tugas yang dipilih dari product backlog dan akan diselesaikan dalam satu sprint. Tugas ini didefinisikan secara detail dan ditugaskan ke anggota tim yang sesuai. Pada _dashboard_ , dalam satu sprint, tim dapat mengerjakan visualisasi data total penjualan harian, mingguan, dan bulanan untuk _dashboard_ admin, serta riwayat penjualan untuk _dashboard_ UMKM.

# **4. Scrum Team (Daily Scrum)**

Scrum Team (Daily Scrum) Tim proyek ini terdiri dari lima anggota dengan dua orang untuk pengembangan aplikasi _mobile E-Commerce_ dan tiga orang untuk pengembangan backoffice website termasuk _dashboard_ BI. Setiap hari rabu dan minggu diadakan pertemuan singkat (daily scrum) selama 15 menit untuk membahas progres, hambatan, dan rencana hari itu. Setiap daily scrum dilakukan per sprint agar seluruh anggota tetap selaras dan fokus terhadap tujuan sprint.

# **5. Increment**

Increment adalah hasil kerja yang diselesaikan dalam satu sprint, yang dapat digunakan atau dipresentasikan kepada pemangku kepentingan. Setiap increment harus dalam kondisi siap untuk diuji dan memberikan nilai tambah. Dalam proyek ini yaitu _dashboard_ , increment dapat berupa penyelesaian visualisasi data total penjualan untuk admin, atau fitur pengelolaan pesanan untuk UMKM, yang sudah diuji dan bisa diakses oleh tim untuk feedback.

# **6. Sprint Review**

Sprint Review Sprint review dilakukan di akhir setiap sprint untuk meninjau hasil pekerjaan. Setiap anggota mempresentasikan increment kepada anggota lain untuk mendapatkan umpan balik. Feedback ini digunakan untuk memperbarui dan memprioritaskan kembali product backlog, memastikan bahwa proyek tetap relevan dan memenuhi kebutuhan pengguna.

# **7. Sprint Retrospective**

Sprint Retrospective Setelah sprint review, setiap anggota tim akan melakukan sprint retrospective untuk mengevaluasi proses kerja selama sprint tersebut. Dalam pertemuan ini, tim mendiskusikan apa yang berjalan dengan baik, apa yang perlu diperbaiki, dan langkah-langkah yang bisa diambil untuk meningkatkan efektivitas kerja di sprint berikutnya. Sprint retrospective membantu tim menjadi lebih produktif, efisien, dan mengurangi masalah yang dihadapi di sprint sebelumnya.

# **2.5.2. Desain Arsitektur Sistem**

Desain arsitektur sistem menggambarkan alur penggunaan _Dashboard Business Intelligence_ (BI) untuk admin dan pelaku UMKM. Proses dimulai dari login atau pendaftaran baru dengan verifikasi, dilanjutkan dengan akses ke dashboard sesuai peran pengguna.

<!-- Start of picture text -->
t=—T ts<br><!-- End of picture text -->

Gambar 2.7 Desain Arsitektur Sistem

Admin dapat melihat visualisasi data berupa cards (pendapatan, total transaksi), tabel (top toko, pengguna, barang), dan grafik (partisipasi pengguna, kategori produk, pendaftar UMKM). Sementara itu, pelaku UMKM mengakses data tentang total penjualan, pendapatan, barang terjual, serta visualisasi tabel produk terlaris, top pembeli, dan riwayat transaksi. Grafik tambahan mencakup partisipasi pembeli dan pengelolaan pesanan.

# **2.5.3. Pemodelan Sistem**

Pemodelan sistem dilakukan untuk menggambarkan alur kerja serta interaksi antara pengguna dengan sistem secara visual dan terstruktur. Pemodelan ini bertujuan untuk memberikan pemahaman yang jelas kepada pengembang dan pemangku kepentingan mengenai bagaimana sistem akan beroperasi.

# **2.4.3.1. Use Case Diagram**

Use case diagram _Dashboard Business Intelligence_ (BI) _E-Commerce_ ini menggambarkan interaksi antara admin dan pelaku UMKM dengan fitur-fitur utama sistem.

<!-- Start of picture text -->
=<br>Kategori),‘. Ko contend.Ss. || <seintend=> iomsxentend> Top 10<br>Produk x. be he Pembelt<br>Soecextente ‘Visualisasi Tabe!<br>Partsipasi 2 --s. ><br>O Pempet_)<ceidengs‘Visualisast ceodngns <cestonto>a<br>‘Admir <cextend>>7 N Pelaku<br>cea ste H ccaxtghc>> TS Resten>><br>Partisipasi i Pendaftar \ ‘Top 10<br>Pengguna UMKM Top 5 Toko Pengguna<br>Sageeat) <a (oa Tako<br><!-- End of picture text -->

Gambar 2.8 _Use Case_ Diagram _Dashboard_ BI

_Dashboard_ BI Admin mencakup visualisasi card, tabel, dan grafik yang menampilkan data seperti pendapatan, total transaksi, top 5 toko, partisipasi pengguna, kategori produk, dan pendaftar UMKM, serta fitur ekspor data ke PDF. _Dashboard_ BI UMKM menyediakan visualisasi card, tabel, dan grafik untuk memonitor total pendapatan, penjualan, barang terjual, serta fitur pengelolaan pesanan dan partisipasi pembeli. Visualisasi tabel di sini membantu UMKM melihat transaksi terakhir, top 5 barang, dan top 10 pembeli. Diagram ini menunjukkan bagaimana fitur-fitur tersebut mendukung analisis data dan pengambilan keputusan.

# **2.4.3.2. Activity Diagram**

_Activity_ diagram ini menggambarkan alur interaksi Admin dengan sistem _Dashboard Business Intelligence_ . 1) Admin

<!-- Start of picture text -->
|<br>Se |<br>iar<br>ss<br>Peceforner|<br>Sa =<br>ee<br>wae<br><!-- End of picture text -->

Gambar 2.9 _Activity_ Diagram _Dashboard_ BI Aktor Admin

Proses dimulai ketika Admin melakukan login, dan sistem memverifikasi kredensial melalui basis data. Jika berhasil, sistem menampilkan halaman dasbor dengan berbagai visualisasi data seperti kartu, grafik, dan tabel. Admin dapat memilih filter untuk menampilkan data yang lebih relevan. Berdasarkan filter tersebut, sistem mengambil data dari basis data dan menampilkan visualisasi yang sesuai, memudahkan Admin dalam menganalisis informasi yang telah difilter.

- 2) Pelaku UMKM

<!-- Start of picture text -->
weowian toon<br>“eaten =| ==<br><!-- End of picture text -->

Gambar 2.10 _Activity_ Diagram _Dashboard_ BI Aktor Pelaku UMKM

_Activity_ Diagram ini menggambarkan alur interaksi Pelaku UMKM dengan sistem _Dashboard Business Intelligence_ . Proses ini hampir sama dengan diagram aktivitas Admin, dimulai dengan proses ketika Pelaku UMKM melakukan login, dan sistem memverifikasi kredensial melalui basis data. Jika berhasil, sistem menampilkan halaman dasbor dengan berbagai visualisasi data seperti kartu, grafik, dan tabel. Pelaku UMKM dapat memilih filter untuk menampilkan data yang lebih relevan. Berdasarkan filter tersebut, sistem mengambil data dari basis data dan menampilkan visualisasi yang sesuai, memudahkan pelaku UMKM dalam menganalisis informasi yang telah difilter.

# **2.4.3.3. Sequence Diagram**

_Sequence_ diagram ini memiliki alur yang kurang lebih sama dengan _activity_ diagram sebelumnya, yaitu menggambarkan proses interaksi antara Admin dan sistem dalam mengakses _Dashboard Business Intelligence_ .

<!-- Start of picture text -->
1) Admin<br>ae<br>1. Melakukan Login H H<br>2. Melakukan Cek Data |<br>return<br>3. Menampilkan Dashboard acevesceeeu seen nal Lercecsentusnocnacrsctts<br>Business Intelligence<br><23. HenampiikanMenampilkan VisuaisasiVisualisasi Card_|Card HH<br><2Menampilkan3. Menampilkan VisvalsasiVisualisasi TabelTabel_| H<br><23. MenampilkanNenampikan VisualisasiVisualisasi GrafikGrafik _| HH<br>4. Memilih Filter H<br>5. Mengambil Data Sesupi Filter yang Dipilin |<br>5. Menampilkan Halaman j<br>‘Visualisasi berdasarkan<br>Filter yang Dipilih<br><!-- End of picture text -->

Gambar 2.11 _Sequence_ Diagram _Dashboard_ BI Aktor Admin

Proses _sequence_ diagram dimulai dengan Admin login, yang diverifikasi oleh sistem melalui Database. Jika berhasil, _Dashboard_ muncul dengan visualisasi data. Admin memilih filter, lalu _Dashboard_ mengambil data yang sesuai dari Database dan menampilkan visualisasi yang relevan untuk analisis lebih lanjut.

- 2) Pelaku UMKM

<!-- Start of picture text -->
t Halaman<br>H<br>Peniual DevoreT ——H<br>i 1. Melakukan Login i H<br>b| Metakukan Cek Data<br>3. Menampilkan Dashboard ee: -.\) Are |<br>Business Intelligence 7<br>2.3. MenampilkanMenampilkan VisualisasiVisualisasiCard_|Card H<br>—————3. Menampilkan esetVisualisasi Tabel HH<br>——_—3. MenampilkanrrrVisualisasi Grafik HH<br>4. Memil Filter H<br>5. Mengambil Data SesuailF}iter yang Dipilih<br>§. Menampilkan Halaman H<br>Visualisasi berdasarkan<br>Filter yang Dipilih<br><!-- End of picture text -->

Gambar 2.12 _Sequence_ Diagram _Dashboard_ BI Aktor Pelaku UMKM

_Sequence_ diagram ini memiliki alur yang kurang lebih sama dengan _activity_ diagram sebelumnya, yaitu menggambarkan proses interaksi antara pelaku UMKM dan sistem dalam mengakses _Dashboard Business Intelligence_ . Proses _sequence_ diagram dimulai dengan pelaku UMKM login, yang diverifikasi oleh sistem melalui Database. Jika berhasil, _Dashboard_ muncul dengan visualisasi data. Pelaku UMKM memilih filter, lalu _Dashboard_ mengambil data yang sesuai dari Database dan menampilkan visualisasi yang relevan untuk analisis lebih lanjut.

# **2.4.3.4. Class Diagram**

_Class_ diagram ini dirancang untuk aplikasi _E-Commerce_ DISKOUMPERINDAG Kabupaten Serang, Banten, yang bertujuan untuk memfasilitasi proses jual beli secara digital serta mendukung pelaku usaha kecil dan menengah (UMKM). Diagram ini memberikan gambaran menyeluruh tentang struktur sistem yang melibatkan berbagai entitas utama, termasuk pengguna, produk, toko, transaksi, pembayaran, serta fitur pendukung lainnya seperti ulasan dan pengiriman. Dengan adanya _class_ diagram ini, alur kerja aplikasi

menjadi lebih jelas, membantu dalam pengembangan dan implementasi sistem yang terintegrasi dan efisien.

<!-- Start of picture text -->
seme a eee dato rg pny eco<br>sey rer nse om set se a<br>srt He ce oe an teow tet =<br>+ acktoersoCarti) bnaaed + dolateCategory() man ae + use<br>+ wpdatecany rang nt + alateTomPrce) ee tom et<br>+ olor) cme omer [Preower _| voaevartiy ating et<br>sna:oe  tate rae epepeerensvee outer ot ae= + cate trata<br>—ne tte smn ig eat wae ee<br>ott sor tet [sewn | ‘eco nan:Sg a<br>crete9 testa pores pte:ce vee<br>=] oentiene)rasernace coresseowtea rs +aa enaCeasedte<br>——= —= ]om eersr a seater=<br>ema ig see<br>‘+namer String + store_ie nt suimieemed<br>[eee ee =— neseman<br>= + mtn 5<br>scm nee<br>eee e ape sheo<br>some tt see senSSton coca<br>‘+sremctitsom:message:ingSinng +6=.anSing‘sirng sitTamoune+ status: Stingoe coe ++tesaretanttrome voucheri int +++sone dence:vidence()ado Sng<br>stat ore eden erent ens<br>[emer] en se eeseeeben ype ee aoeee +perros edatetotAr =<br>~ ory conse ae te evere<br>an ener va sate<br>contre<br>reer me sasora tecite [wre]vee | |<br>eae eg enue eee oy<br>+ ank_num: Sting ++ subdir String ‘+ fmage: Sireg,<br>Ca [ee] | |eremap metspototon cnee Sg rg oa r en<br>‘+oeoe 0tp: Sing. ee+ ve Seng a “+asesera phone Stangboreto an ‘+enasienndi satus: Stingane<br>rere. nestine verse sere rete Sng onc ote =<br>SS / * + user itt String “+ min_onder: double stint<br>se rg nepeie ete soe<br>a + birth date: Date sata +max_ a at:<br>aa meso: Surg ee nn+ lioness) ‘advouchereapeniyers usedsemenat nee<br>seco Soe = pneaniy<br>see a rears eens<br>[-sewereacn | poriinyceserol<br><!-- End of picture text -->

Gambar 2.13 _Class_ Diagram

Dalam _Dashboard Business Intelligence_ (BI) yang ada pada aplikasi ini, digunakan berbagai tabel seperti _Product, Store, Category, User, Orders,_ dan _Review_ untuk mengumpulkan dan menampilkan data yang relevan. Tabel Product mencatat informasi tentang produk yang tersedia, termasuk nama, deskripsi, harga, dan

jumlah stok. Tabel Store menyimpan data terkait toko, termasuk status dan jenis toko. Tabel Category mengelompokkan produk ke dalam kategori yang sesuai untuk memudahkan pengelolaan dan pencarian. Tabel User berisi data pengguna, mencakup informasi pribadi dan kredensial. Tabel Orders atau transaksi menyimpan detail tentang pembelian yang dilakukan, termasuk status dan total jumlah transaksi. Terakhir, tabel Review digunakan untuk menyimpan ulasan pengguna mengenai produk yang telah dibeli, memberikan umpan balik yang berguna untuk penjual dan calon pembeli. Dengan penggunaan tabeltabel ini, _dashboard_ BI mampu menampilkan analisis data yang membantu dalam pengambilan keputusan strategis, seperti identifikasi produk terlaris, kinerja toko, serta preferensi pelanggan.

# **2.6. Desain Antarmuka**

Berikut merupakan desain antarmuka dari _Dashboard Business Intelligence_ DISKOUMPERINDAG Kabupaten Serang, Banten berdasarkan langkah-langkah yang telah dilakukan sebelumnya. Desain ini mencakup tampilan yang dirancang untuk memfasilitasi aksesibilitas data serta membantu Admin dan pelaku UMKM dalam menganalisis performa bisnis dengan lebih efektif. Elemen-elemen visual, seperti card, grafik, dan tabel, dipilih untuk menyajikan data secara informatif dan interaktif, memastikan pengguna dapat memahami pengukuran penting seperti total transaksi, pendapatan, partisipasi pengguna, dan penjualan produk secara mudah. Desain ini diharapkan mendukung pengambilan keputusan yang lebih baik dan meningkatkan efisiensi dalam operasional _E-Commerce_ .

1. _Dashboard Business Intelligence_ Admin

- _Dashboard Business Intelligence_ Admin DISKOUMPERINDAG Kabupaten

- Serang Banten dirancang dengan fokus pada kemudahan akses informasi, representasi data visual yang jelas, dan pengelompokan informasi yang efektif.

<!-- Start of picture text -->
B|EeeDISKOPPERINDAS Welcome, Admin!q Gi [piskorrerDISKOPPERINDAG<br>S C—) =><br>Rpavrecs = 37 @ t6<br>Top 5 Toko Partisipasi Pengguna =p<br>aig<br>TotoToko AyaZa s8 Candctande A<br>Kecantikan Lestari 4 Lengkong Gudang “| Pp<br>i apr isa 3 oi mI<br>: fu Tent 2 — ,<br>Top5 Barang EEE GED ots! Pendaftar umm =D<br>7<br>Blouse Wanita Pakaian Wanita 36<br>Kero Snghone Mokananfingan 4<br>Bie be Raw Super Biit dan Tonamantis 18<br>bros Handmade Fae! asso B<br>Tea eae<br>‘Toko Tidak Aktif [ ves |<br>1 yu Wand 2760000<br>2 suites Ress000 SD<br>3 et resco GD :<br>4 Rudi Setiawan Rpssscoo | GD<br>6 Adina ute rez «| «GD<br>6 Siti Arisa rsccoo | GD<br>z Budi Sentoso resco GD © atego 1258<br>tate<br>8 250<br>Nina Rahmawati 2p 58000 @ aa<br>° Roosyidah Aya fea2000 @D<br>0 Dodi Pratama mp3s000 SD<br>Kategori Produk =<br>c= =><br><!-- End of picture text -->

Gambar 2.14 _User Interface Dashboard_ BI Admin

Pada halaman ini terdapat logo dan identitas instansi, yaitu DISKOUMPERINDAG Kabupaten Serang, yang memberikan kesan profesional

dan resmi. Selain itu, tersedia tombol Unduh PDF yang mempermudah admin untuk mencetak atau mengunduh laporan dalam format PDF.

Pada bagian atas _dashboard_ , terdapat tiga Visualisasi _Card_ , yaitu Pendapatan Masuk, Total Transaksi, dan Total Toko, yang memberikan akses cepat kepada admin terhadap data penting secara real-time. Menu navigasi di sisi kiri (Sidebar) menampilkan opsi seperti _Dashboard_ , Kelola Aplikasi, Transaksi, Kelola Pengguna, Peta Persebaran UMKM, Kelola UMKM, Daftar Pengguna, dan Profil. Setiap menu dilengkapi dengan ikon yang mempermudah pengguna dalam navigasi aplikasi.

Di bagian tengah _dashboard_ , visualisasi data disajikan secara informatif melalui grafik dan tabel. Grafik garis pada bagian Partisipasi Pengguna menampilkan tren jumlah pengguna yang mendaftar setiap bulan, dengan lonjakan tertinggi terjadi pada bulan April. Tabel Top 5 Toko menunjukkan lima toko dengan total penjualan tertinggi, lengkap dengan informasi lokasi kecamatannya. Tabel ini dilengkapi filter untuk menyesuaikan data berdasarkan waktu. Tabel Top 5 Barang menampilkan lima produk dengan total penjualan tertinggi, disertai kategori masing-masing produk. Tabel ini juga dilengkapi filter untuk mempermudah admin dalam melihat performa produk berdasarkan kategori dan waktu.

Grafik batang pada bagian Total Pendaftar UMKM memperlihatkan jumlah pendaftar UMKM yang disetujui ( _approved_ ) setiap bulan, dengan puncak pendaftaran terjadi pada bulan Mei. Tabel Top 10 Pengguna menampilkan daftar pembeli dengan total belanja tertinggi. Tabel ini dilengkapi tombol Detail untuk melihat informasi lebih lanjut tentang setiap pengguna, serta filter untuk memilih rentang tahun. Diagram lingkaran pada bagian Toko Tidak Aktif memberikan informasi mengenai distribusi toko yang tidak aktif berdasarkan kategori produk.

Terakhir, Grafik Kategori Produk menampilkan tren penjualan berbagai kategori produk dari tahun 2024 hingga 2025, memudahkan admin untuk membandingkan performa antar kategori produk secara tahunan.

2. _Dashboard Business Intelligence_ Pelaku UMKM

Pada _Dashboard_ Pelaku UMKM DISKOUMPERINDAG Kabupaten Serang Banten dirancang untuk memberikan gambaran menyeluruh tentang performa usaha bagi pelaku UMKM. Untuk isinya kurang lebih sama seperti Admin.

<!-- Start of picture text -->
EE ipisxorrerinoas == Welcome, Toko Zulfa! Gi |piskoprerinpas<br>Blass Pendapotar ce 4, Total _ Total Perjualan { unaun 0 J<br>S Rpasszso = 15 ® 62 ‘<br>- ‘Ths Bait a=am=pca Partisipasi* Pembeli<br>Kerik Singhong “ 43 . A<br>KacangBavang Guth 7 a 40 A<br>Makan rsp aun dr 2 #30<br>Total Pendapatan UMKM SEED iransatsi terathir atsea ts<br>- acang Bang Guth ———_—Rp20000<br>=<br>i | ecient Singhong 959.000<br>Pengelolaan Pesanan<br>1 Fk fp 218000<br>2 Sit Aion resco GD<br>3 bud Santoro fpescoo | SD<br>4 Nina Rahmawat mpss000<br>5 foceydah Aya ma000 | GD ax. 1%<br>° od Pratame mssooo DC .<br>Kategori Produk<br><!-- End of picture text -->

Gambar 2.15 _User Interface Dashboard_ BI Pelaku UMKM

Pada bagian atas halaman _dashboard_ , terdapat informasi identitas pelaku usaha berupa ucapan selamat datang yang dipersonalisasi, seperti “Welcome, Toko Zulfa!” Disediakan juga tiga indikator utama yang menampilkan total pendapatan, total transaksi, dan total penjualan secara ringkas dan real-time. Selain itu, tersedia tombol Unduh PDF yang memudahkan pengguna untuk mengunduh laporan dalam format dokumen. Panel navigasi di sisi kiri (Sidebar) menampilkan menu yang

sederhana dan mudah diakses, seperti _Dashboard_ , Pengiriman & Pembayaran, Ubah Password, dan Profil, sehingga mempermudah pelaku UMKM dalam mengelola akun mereka.

Di bagian utama, _dashboard_ menyajikan berbagai visualisasi dan tabel informatif. Pada Top 5 Barang, ditampilkan produk dengan penjualan tertinggi beserta total terjual dan ratingnya, yang memudahkan pelaku usaha memantau performa produk mereka. Grafik garis pada bagian Partisipasi Pembeli memberikan wawasan mengenai tren jumlah pembeli setiap bulan sepanjang tahun. Bagian Total Pendapatan UMKM disajikan dalam grafik batang yang menggambarkan perkembangan pendapatan setiap bulan, sehingga pelaku usaha dapat memantau kinerja keuangan mereka secara berkala.

Tabel Transaksi Terakhir menampilkan tiga transaksi terbaru beserta statusnya (dibatalkan, selesai, dalam proses), lengkap dengan rincian produk dan tanggal transaksi. Pengguna juga dapat mengakses seluruh riwayat transaksi melalui tautan yang tersedia. Diagram lingkaran pada bagian Pengelolaan Pesanan menunjukkan persentase pesanan yang sudah dikirim dan yang masih perlu dikirim, memberikan gambaran tentang efektivitas pengelolaan pesanan toko. Tabel Top 10 Pembeli menampilkan daftar pembeli dengan total belanja tertinggi, dilengkapi dengan tombol Detail untuk melihat informasi lebih lanjut serta filter untuk menyesuaikan data berdasarkan tahun.

Terakhir, Grafik Kategori Produk memperlihatkan tren penjualan dari berbagai kategori produk berdasarkan tahun 2024 dan 2025, sehingga pelaku UMKM dapat menganalisis performa kategori produk secara strategis dan menyusun rencana bisnis yang lebih tepat sasaran.

3. Detail Pengguna untuk _Dashboard Business Intelligence_ Admin Halaman Detail Pengguna ini dirancang untuk menampilkan informasi lengkap

mengenai riwayat transaksi dari pengguna tertentu yang dipilih oleh admin, misalnya dari daftar Top 10 Pengguna di _dashboard_ utama.

<!-- Start of picture text -->
BE pisxonrerinoac Ayu Wulandari<br>ry<br>Daftar Transaksi . a<br>1 18Februari2025 Ayu Wulandari spur Arisa fp 85000 Nasi Liwot Instan Komp<br>2 0Desember 2024 Ayu Wulandar Toko Ala fp 30000 Bros Handmade lane!<br>38 November 2024 AyuWulandari—_ Kecantikan Lestari Rp 65000 Partum Mawar<br>46 November 2024 Ayu Wulandari———Dapur Arisa Rp 155000 Nasi Livetistan Kompiit<br>5 1ONovember 2024 Ayu Wulandari Toko Ala Rp 50.000 Bros Handmade Fane!<br>© oktober 2028 Ayu Wulandar Toko Alya Rp910000 Blouse Wanita<br>7 WWokteber 2024 Ayu Wulandar Toko Alya Rp 30000 Bros Handmade Fae!<br>8 T7September2024 Ayu Wulandari_KacantkanLestari Rp 95000 Partum Mawar<br>© September 2024 Ayu Wulandari Toko Ale p85000 Kaos Fria KatunLengan Pendek<br>1 WAguetus 2024 Ayu Wulandari Toko Aya fp160000 Kaos PriaKatun Lengan Pendek<br>a<br>ass)<br><!-- End of picture text -->

Gambar 2.16 _User Interface_ Detail Pengguna _Dashboard_ BI Admin

Pada bagian header halaman, ditampilkan nama pengguna seperti “Ayu Wulandari” sebagai identitas utama, dengan judul Daftar Transaksi yang menjelaskan fokus halaman ini. Tersedia fitur Unduh untuk mempermudah pengambilan data transaksi dalam bentuk dokumen, serta kolom pencarian untuk memfilter transaksi berdasarkan kata kunci seperti nama toko atau produk.

Seluruh transaksi disajikan dalam tabel yang rapi dengan kolom: nomor urut, tanggal transaksi, nama pembeli, nama toko, total transaksi, dan nama produk yang dibeli. Desain tabel ini mempermudah admin untuk menganalisis riwayat belanja pengguna, seperti produk yang sering dibeli dan toko yang sering dikunjungi.

Jika jumlah data melebihi kapasitas satu halaman, admin dapat menggunakan navigasi halaman di bagian bawah tabel untuk berpindah ke halaman berikutnya. Tersedia juga tombol Kembali di bagian bawah halaman untuk mempermudah admin kembali ke halaman sebelumnya.

4. Detail Pembeli untuk _Dashboard Business Intelligence_ Pelaku UMKM

Halaman detail pembeli pada _Dashboard Business Intelligence_ untuk Pelaku UMKM dirancang untuk menampilkan informasi lengkap mengenai transaksi yang dilakukan oleh pembeli tertentu di toko yang dikelola Pelaku UMKM. Akses ke halaman ini dimulai ketika Pelaku UMKM mengklik salah satu nama pembeli dari daftar Top 10 Pembeli yang tersedia di _dashboard_ utama. Tujuan dari fitur ini adalah untuk membantu Pelaku UMKM memahami kebiasaan dan pola pembelian pelanggan mereka, serta menganalisis transaksi dengan lebih rinci.

<!-- Start of picture text -->
Bi pisnonreninoac Fikri<br>Daftar Transaksi a<br>1 16 Februar2025 Fat Toko 2a p32000 Kerpk Singtong<br>2 26 Desember 2024 Ft Toko Zita fp 37000 Kerik Singkong<br>3 16 Desember 2024 Ft Toko Zula Rp 59000 Kerik Singkong<br>‘ 10 Desember 2024 Fit Toko Zula fp 37000 Kern Singkong<br>5 1 Desember 2028 Fit Toko Zuta fp 45000 Kacang Bawang Gurih<br>6 28 Noveber 2024 Fit Toko Zula fp 30.000 Kacang Bawang Gurih<br>7 1B November 2024 Fit Toko Zula fp 45000 Kacang Bawang Guin<br>8 16 November 2024 Fei TokoZufa——_-Rp 186000 erp Singkong<br>° 2 November 2024 Fie Toko Zula fp 30000 Kacang Bawang Guin<br>” 2oKtober 2024 Fie Toko Zuta fp 45000 Kacang Bawang Guin<br>a<br><!-- End of picture text -->

Gambar 2.17 _User Interface_ Detail Pembeli _Dashboard_ BI Pelaku UMKM Pada bagian header halaman, nama pembeli pada toko yang sedang _login_ seperti “Fikri” yang merupakan pembeli dari toko tersebut. Halaman ini ditampilkan dengan jelas sebagai identitas utama, menandakan bahwa pelaku UMKM sedang mengakses detail transaksi pembeli tersebut. Seluruh riwayat transaksi disajikan dalam tabel yang terstruktur, memuat informasi seperti nomor urut, tanggal transaksi, nama pembeli, nama toko, total transaksi, dan nama produk yang dibeli. Tabel ini mempermudah pelaku UMKM dalam memantau dan melacak transaksi secara kronologis dan rinci.

Tersedia fitur Unduh untuk mempermudah pengambilan data, serta kolom pencarian untuk menemukan transaksi tertentu berdasarkan kata kunci seperti produk atau nama toko. Jika jumlah transaksi melebihi kapasitas satu halaman, tersedia navigasi halaman (pagination) di bagian bawah tabel untuk memudahkan perpindahan antar halaman. Tombol Kembali di bagian bawah halaman mempermudah pengguna untuk kembali ke halaman _dashboard_ utama tanpa kesulitan.

5. Semua Daftar Transaksi Terakhir untuk _Dashboard Business Intelligence_ Pelaku UMKM

Halaman detail transaksi pada _Dashboard Business Intelligence_ dirancang untuk memberikan informasi lengkap mengenai semua transaksi yang terjadi di toko yang dikelola oleh Pelaku UMKM. Halaman ini dapat diakses dengan mengklik tombol Lihat Semua Transaksi yang terdapat pada tabel transaksi terakhir

di _dashboard_ utama. Tujuannya adalah agar Pelaku UMKM memiliki pandangan menyeluruh terhadap riwayat transaksi mereka dan dapat melakukan analisis yang lebih mendalam terkait penjualan.

<!-- Start of picture text -->
Bi ipisxorreninoac Nina Rahmawati<br>- Detail Transaksi<br>@ 2 seeriine<br><!-- End of picture text -->

Gambar 2.18 _User Interface_ Transaksi Terakhir _Dashboard_ BI Pelaku UMKM

Pada halaman ini menampilkan tabel yang merinci informasi transaksi secara komprehensif, meliputi nomor urut, tanggal transaksi, nama pembeli, nama produk, metode pembayaran, total harga, persentase biaya administrasi, serta status transaksi seperti completed, canceled, paid, atau pending. Setiap kolom dalam tabel memberikan visibilitas penuh terhadap detail penjualan, sehingga memudahkan Pelaku UMKM dalam memantau aktivitas transaksi secara transparan.

Di sisi kanan atas tabel, terdapat fitur pencarian yang memungkinkan pengguna untuk menemukan transaksi tertentu secara cepat berdasarkan nama pembeli, produk, atau metode pembayaran. Selain itu, tombol "Unduh" menyediakan opsi untuk mengunduh data transaksi dalam format CSV, mendukung kebutuhan dokumentasi dan analisis data secara offline.

Navigasi pagination di bagian bawah tabel memungkinkan pengguna menjelajahi data transaksi secara terstruktur apabila jumlah entri melebihi batas tampilan satu halaman. Terakhir, tombol "Kembali" di pojok kanan bawah memudahkan pengguna untuk kembali ke halaman utama Dashboard UMKM.

# **2.7. Rencana Pengujian Proyek**

Pengujian proyek sangat penting untuk memastikan bahwa aplikasi yang dikembangkan memenuhi standar kualitas dan berfungsi sesuai dengan yang diharapkan. Dalam proyek pengembangan _Dashboard Business Intelligence_ (BI) untuk Pelaku UMKM dan DISKOUMPERINDAG Kabupaten Serang, pengujian dilakukan dengan metode _black box_ .

Pengujian _black box_ adalah metode pengujian yang memfokuskan pada pengujian fungsionalitas aplikasi tanpa melihat ke dalam struktur kode. Fokus Pengujian _black box_ pada proyek _Dashboard Business Intelligence_ (BI) untuk Pelaku UMKM dan DISKOUMPERINDAG Kabupaten Serang adalah menguji fungsionalitas aplikasi dari sudut pandang pengguna akhir, mencakup pengolahan data dan interaksi pengguna dengan antarmuka.

|**No**|**Fitur yang Diuji**|**Deskripsi**|**Hasil yang Diharapkan**|
|---|---|---|---|
|1|Login|Memastikan pengguna<br>dapat login sebagai<br>admin maupun pelaku<br>UMKM|Sistem berhasil masuk dan<br>menampilkan halaman<br>_dashboard_berdasarkan<br>penggunanya|
|2|Tampilan<br>_Dashboard_<br>_Business_<br>_Intelligence_|Akses Website untuk<br>Melihat_Dashboard_<br>_Business Intelligence_|Data dan Grafik yang<br>ditampilkan sesuai dengan<br>kondisi sebenarnya|
|3|Filter Pada<br>_Dashboard_<br>_Business_<br>_Intelligence_|Filter untuk memilih<br>berdasarkan rating,<br>kategori produk, total<br>penjualan, dan time<br>series|Ketika diklik, data yang<br>ditampilkan sesuai dengan<br>filter yang dipilih|
|4|Ekspor PDF|Memastikan bahwa<br>pengguna dapat<br>melakukan ekspor PDF<br>untuk pengambilan<br>keputusan|Pengguna dapat melakukan<br>ekspor atau download PDF|

Tabel 2.1 Pengujian Proyek dengan Metode _Black Box_


# PROYEK: PENGEMBANGAN SISTEM INFORMASI PENGAJUAN CUTI PEGAWAI PADA FAKULTAS ILMU KOMPUTER UPN “VETERAN” JAKARTA

# **BAB II**

# **RANCANGAN PROYEK**

# **2.1. Observasi**

Proses observasi dilakukan penulis dengan cara mengamati dan mengunjungi Fakultas Ilmu Komputer di UPN “Veteran” Jakarta serta mengumpulkan informasi terkait dengan proses pengajuan cuti. Observasi ini mencakup pemahaman mengenai alur kerja pengajuan cuti dan peran masing-masing aktor yang terlibat. Melalui observasi ini, penulis dapat memperoleh gambaran menyeluruh mengenai kendala dan kebutuhan pengguna dalam pengajuan cuti di Fakultas Ilmu Komputer UPN “Veteran” Jakarta.

# **2.1.1. Prosedur Sistem Berjalan**

Proses pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta saat ini masih dilakukan secara manual. Berikut ini tahapan-tahapan proses pengajuan cuti:

1. Pemohon cuti meminta formulir pengajuan cuti kepada staf admin tata usaha.

2. Staf admin tata usaha memberikan formulir pengajuan cuti kepada pemohon.

3. Pemohon mengisi formulir pengajuan cuti dengan lengkap.

4. Pemohon menyerahkan formulir yang sudah diisi kepada staf admin tata usaha.

5. Staf admin tata usaha menerima formulir dan memeriksa kelengkapan isinya.

6. Staf admin tata usaha menyerahkan formulir kepada atasan langsung pemohon. Jika pemohon adalah dosen, atasan langsungnya adalah koordinator program studi. Apabila pemohon cuti adalah tenaga kependidikan, atasan langsungnya adalah koordinator tata usaha. Sementara itu, jika pemohon cuti adalah koordinator prodi atau ketua laboratorium, atasan langsungnya adalah wakil dekan 1.

7. Atasan langsung memeriksa kelengkapan dan kebenaran isi formulir. Jika sudah sesuai, atasan langsung memberikan paraf pada formulir dan mengembalikannya ke staf admin tata usaha.

8. Staf admin tata usaha menerima formulir dan menyerahkannya kepada wakil dekan 2.

9. Wakil dekan 2 memeriksa formulir, memberikan tanda tangan, dan mengembalikan formulir kepada staf admin tata usaha.

10. Staf admin tata usaha menerima formulir dan menyerahkannya kepada sekretaris dekan.

11. Sekretaris dekan menerima formulir dan menyerahkannya kepada dekan.

12. Dekan memeriksa formulir, memberikan tanda tangan persetujuan, dan mengembalikannya ke sekretaris dekan.

13. Sekretaris dekan menerima formulir dan mengembalikannya ke staf admin tata usaha.

14. Staf admin tata usaha menerima formulir dan mengirimkannya ke staf kepegawaian.

15. Staf kepegawaian menerima formulir, memeriksa ketersediaan jatah cuti pemohon, lalu menyerahkan formulir tersebut ke plt. kepala biro perencanaan, keuangan, dan umum.

16. Plt. kepala biro memeriksa formulir, memberikan tanda tangan persetujuan, dan mengembalikannya ke staf kepegawaian.

17. Staf kepegawaian menerima formulir, kemudian membuat surat izin cuti dalam bentuk draf dan asli. Setelah itu, staf kepegawaian memberikan draf surat izin cuti kepada ketua tim kerja kepegawaian.

18. Ketua tim kerja kepegawaian memeriksa draf surat, memberikan paraf jika sudah sesuai, dan mengembalikannya ke staf kepegawaian.

19. Staf kepegawaian memberikan draf surat kepada kepala bagian umum.

20. Kepala bagian umum memeriksa draf surat, memberikan paraf jika sudah sesuai, dan mengembalikannya ke staf kepegawaian.

21. Staf kepegawaian menerima draf surat dan menyerahkan surat izin cuti, berbentuk draf dan asli, kepada plt. kepala biro perencanaan, keuangan, dan umum.

22. Plt. kepala biro perencanaan, keuangan, dan umum memeriksa dan memberikan tanda tangan pada draf dan surat asli, kemudian mengembalikannya ke staf kepegawaian.

23. Staf kepegawaian memberikan nomor surat, tanggal, dan stempel pada surat izin cuti, lalu mengunggahnya ke aplikasi. Setelah itu, staf kepegawaian

mengirimkan surat izin cuti yang telah disahkan plt. kepala biro perencanaan,

keuangan, dan umum ke staf admin tata usaha FIK.

24. Staf admin tata usaha FIK menerima surat izin cuti dan menyerahkannya kepada dekan dan pemohon cuti.

25. Dekan dan pemohon cuti masing-masing menerima surat izin cuti tersebut.

Untuk memperjelas prosesnya, dapat dilihat pada Gambar 2.1 yang menggambarkan alur pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta yang sedang berjalan.

<!-- Start of picture text -->
files) ee)<br>| & Seca Pease ee<br>a —<br><!-- End of picture text -->

<!-- Start of picture text -->
ji]SSGeese ee<br>,esereerew== |<br>fl]eeeee<br><!-- End of picture text -->

Gambar 2.1. Alur Sistem Berjalan

# **2.2. Usulan Solusi**

# **2.2.1.** **_Data Flow Diagram_**

_Data Flow Diagram_ (DFD) digunakan untuk menggambarkan aliran data dalam sistem informasi pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta yang diusulkan. Terdapat DFD Level 0, yang memberikan gambaran umum mengenai sistem secara keseluruhan, menunjukkan entitas eksternal dan interaksi dasar yang terjadi antara pengguna dan sistem. Selanjutnya, penulis menyusun DFD level 1, yang merinci proses utama dalam sistem. Setelah menyusun DFD level 1, penulis menyusun DFD level 2 untuk menggambarkan sub proses dari setiap proses di DFD level 1, yang memberikan detail tentang aliran data, interaksi antar proses, dan penyimpanan data yang terlibat.

# **2.2.1.1. DFD Level 0**

<!-- Start of picture text -->
Data Login t<br>Data Cu gle3<br>#18<br>apran 3g Morais Pein,<br>Koor<br>Tata Usaha FIK 5] 8 Mengelaa Roe<br>‘Mengelola Cuti Tahunan- i ata Logi<br>lengetla Batasan Cu longella Data Pegava<br>ata Cut<br>JstasanLangsung (Koor Prt Sai Admin Kepegawaian<br>Wadek 1) ” aporan Cut<br>KonfemasiPengakan cut->/ Sistem Informasi<br>aporan cuw—__|_ PegawaiPengajuanPadaCutiFIK asi Pengaivan Cut<br>UPN "Veteran" ata Loge<br>Wadek 2 KonfemasiDataPengaivan Login») Cut» Jakarta Data OatData Surat LoginCu Tan Veritas Surat<br>aporan Cue ——><br>Konfrmasi Pengecekan Dra Surat Ca<br>ata Log<br>Data Login, esahan Surat C<br>si asap Jt. Kepala Biro Perencanaan<br>‘one cues Keuangan, dan Umum<br>aporan Cut Laporan Cut<br><!-- End of picture text -->

Gambar 2.2. DFD Level 0

Dalam Gambar 2.2. menampilkan DFD Level 0 pada sistem informasi pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Pada DFD Level 0 sistem pengajuan cuti ini, terdapat sembilan entitas eksternal, diantaranya adalah _user_ , koordinator tata usaha FIK, atasan langsung, wadek 2, dekan, super admin, admin kepegawaian, tim verifikasi surat, dan plt. kepala biro

perencanaan, keuangan, dan umum. _User_ , sebagai pemohon cuti, memberikan input berupa _login_ dan data pengajuan cuti, serta menerima _output_ berupa surat cuti dan status cuti sebagai hasil proses pengajuan. Atasan langsung, wakil dekan 2, dan dekan melakukan _login_ untuk melakukan konfirmasi pengajuan cuti dan memperoleh laporan cuti. Sementara koordinator tata usaha FIK melakukan _login_ untuk melihat data pengajuan cuti, input hari noncuti, input batasan cuti, input cuti tahunan, serta menerima laporan cuti. Super admin memberikan input data _login_ untuk mengelola _permission, role,_ dan data _user_ sedangkan admin kepegawaian memberikan validasi pengajuan cuti, serta menerima laporan cuti. Sementara itu, tim verifikasi surat memberikan input data _login_ untuk memperoleh data draf surat cuti dan memberikan konfirmasi pengecekan draf surat cuti. Sementara itu, plt. kepala biro perencanaan, umum, dan keuangan memberikan input data _login_ untuk konfirmasi surat cuti dan menerima laporan cuti.

# **2.2.1.2. DFD Level 1**

<!-- Start of picture text -->
rT Sa i: =<br><!-- End of picture text -->

Gambar 2.3. DFD Level 1

Pada DFD Level 1 sistem informasi pengajuan cuti yang ditampilkan dalam Gambar 2.3, terdapat delapan proses dan sembilan _data store_ dengan entitas eksternal yang telah dijelaskan pada DFD Level 0. Proses-proses yang terdapat pada DFD Level 1 ini meliputi _login_ , manajemen _user_ dan _role_ , pengelolaan kebijakan cuti, pengajuan cuti, konfirmasi pengajuan cuti oleh atasan langsung, konfirmasi pengajuan cuti oleh wakil dekan 2, konfirmasi pengajuan cuti oleh dekan, dan pengelolaan surat cuti. Setiap proses ini terhubung dengan beberapa

_data store_ , yaitu data _role_ , data _user_ , data _permission_ , data sub unit, data hari noncuti, data batasan cuti, data cuti tahunan, data cuti, dan data _history_ .

# **2.2.1.3. DFD Level 2 Login**

<!-- Start of picture text -->
Konia: Log can Ha<br>onferasi Loge dan Hak<br>Konfiasi Log dan Hak As<br>F : _— woe—| pinonemasi Loge dan[tanHak<br>‘Asan Langsung + nout Data Lon Kevangan.Peroncanaan.PE KepaladanBroUmum ents Login dan Hak Akses<br>en ieon A—veename<br>dan Paswe<br>Wadek 2 Kerteasi tog<br>= fenton 1.2 Kontas\ Ota<br>_— ae san PasoTL sweee foto tein<br>oe een tnt —9 Kontasi Log dan Hak<br>Kontmas\ Logn dan Hak Aisa<br><!-- End of picture text -->

Gambar 2.4. DFD Level 2 _Login_

Gambar 2.4. menunjukkan DFD Level 2 untuk proses _login_ yang terdiri dari dua proses. Proses pertama adalah input data _login_ , yang menerima data _login_ berupa _username_ dan _password_ dari pengguna. Proses kedua adalah konfirmasi data _login_ , yang memverifikasi data _login_ yang dimasukkan dan menentukan hak akses pengguna.

**2.2.1.4. DFD Level 2 Manajemen** **_User_ dan** **_Role_**

<!-- Start of picture text -->
Data Permission Data——<br>info Permissio 1 PengelolaanPorisaa Data info Petsnideiee— Permission<br>Data Role ——» =,i,<br>Super Admin Info Ro 2 PengelolaanRole Datal¢ info Role Role<br>Data Use Data =——, |.<br>Info User. 3 PengelolaanUser Datal fo User— Use 1<br><!-- End of picture text -->

Gambar 2.5. DFD Level 2 Manajemen _User_ dan _Role_

Gambar 2.5. menunjukkan DFD Level 2 untuk proses manajemen _user_ dan _role_ yang terdiri dari tiga proses, yaitu proses mengolah data _permission_ , mengolah data _role_ , dan mengolah data _user_ . Ketiga proses tersebut dilakukan oleh super admin.

# **2.2.1.5. DFD Level 2 Pengelolaan Kebijakan Cuti**

<!-- Start of picture text -->
Date Sub U<br>Data Sub Unit<br>3.4Sub UntMengelolaKerja.Data Supsa Unit<br>Informasi Sup Un Informs! Suba)<br>Data Has Non.7]<br>bataata HanHar tion-cus—p{22 Penetapanener Hart Harisit Non-Cutiwok<br>Jnformasi Hari|<br>tnformasi Har Non-Cul<br>Data Batasan|7<br>Koor Tata Usaha Fik 3!Data Batasan_,/83 Acti3.3 Penetapan penaaitl Batasan h Cut<br>lformasi Batasana<br>informa Batasan Cut<br>Data Sisa Cu“7<br>Data Sisa 3.4 Pengelolaan<br>Cu Tahun Cut Tanunan oanfahunan<br>formasi Sisa Cut Tahuns aoe Ss Cowo!<br><!-- End of picture text -->

Gambar 2.6. DFD Level 2 Pengelolaan Kebijakan Cuti

Gambar 2.6. menunjukkan DFD Level 2 untuk proses pengelolaan kebijakan cuti, yang terdiri empat proses, yaitu mengelola data sub unit kerja, penetapan hari noncuti, penetapan batasan cuti bulanan, dan pengelolaan cuti tahunan. Proses 3.1 digunakan untuk mengelola data sub unit kerja yang terdapat pada unit kerja fakultas ilmu komputer. Proses 3.2 digunakan untuk menetapkan hari-hari tertentu yang tidak dapat diambil oleh _user_ saat mengajukan cuti tahunan. Proses 3.3 digunakan untuk mengatur batas maksimal cuti yang dapat diambil setiap bulan oleh _user_ , yang dibedakan berdasarkan jenis cuti dan jenis pegawai. Sementara itu, proses 3.4 untuk mengatur data cuti tahunan setiap _user_ sehingga mereka dapat memantau hak cuti tahunan yang tersedia. Ketiga proses tersebut dilakukan oleh koordinator tata usaha FIK.

# **2.2.1.6. DFD Level 2 Pengajuan Cuti**

<!-- Start of picture text -->
sanattae<br>[ = | Data Pengajuan Cutr Informasi Batazan Cub<br>cusmanan<br><!-- End of picture text -->

Gambar 2.7. DFD Level 2 Pengajuan Cuti

Gambar 2.7. menunjukkan DFD Level 2 untuk proses pengajuan cuti, yang terdiri lima proses, yaitu proses 4.1 untuk menampilkan form pengajuan cuti, proses 4.2 untuk input data pengajuan cuti, proses 4.3 untuk mengecek kebijakan cuti, proses 4.4 untuk menyimpan pengajuan cuti, dan proses 4.5 untuk melihat status pengajuan cuti. Kelima proses tersebut dilakukan oleh _user_ sebagai pemohon cuti.

**2.2.1.7. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Atasan Langsung**

<!-- Start of picture text -->
a<br>scm ca<br>noo<br>[fest "<br>[seman Jin reno “ ss<br>ee ee riereonmce—[ won|<br><!-- End of picture text -->

Gambar 2.8. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Atasan Langsung

Gambar 2.8. menunjukkan DFD Level 2 untuk proses konfirmasi pengajuan cuti oleh atasan langsung, yang terdiri tiga proses, yaitu proses 5.1 untuk menampilkan daftar pengajuan cuti kepada atasan langsung, proses 5.2 untuk input keputusan pengajuan cuti yang dilakukan oleh atasan langsung, dan proses 5.3 untuk menampilkan status pengajuan cuti kepada _user_ , koordinator tata usaha FIK, wadek 2, dekan, admin kepegawaian, tim verifikasi surat, dan plt. kepala biro perencanaan, umum, dan keuangan.

# **2.2.1.8. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Wakil Dekan 2**

<!-- Start of picture text -->
‘Daflar pengajuan cut<br>6.1 Menampilkan<br>‘Status Pengajuan<br>Cut Daftar CutiPengajuan }¢—Daftar pengajuan ci<br>Pengajuan Cuti<br>Konfirmasi Pengajuan Cut ————<br>Status Pengajuan —<br>B.2PengajvanInput Keputusar Cut J —Kentrmasi Pengajuan Cuti—> History7<br>[fm Pengavan ca Status Pengajuan<br>ee ee <——suss Fenn ca<br>6.3 Menampilkan<br>‘Status Pengajuan Tim Verifikasi Surat<br>‘Admin Kepegawaian_}€-Status Pengajuan Cut Cutt<br>Pit. Kepala Biro<br>Status Pengajuan Cut->| Perencanaan, Keuangan,<br>dan Umum<br>fatus Pengajuan Cutr<br>a Pena cf amino |<br><!-- End of picture text -->

Gambar 2.9. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Wadek 2

Gambar 2.9. menunjukkan DFD Level 2 untuk proses konfirmasi pengajuan cuti oleh wakil dekan 2, yang terdiri tiga proses, yaitu proses 6.1 untuk menampilkan daftar pengajuan cuti kepada wakil dekan 2, proses 6.2 untuk input keputusan pengajuan cuti yang dilakukan oleh wakil dekan 2, dan proses 6.3 untuk menampilkan status pengajuan cuti kepada _user_ , koordinator tata usaha FIK, atasan langsung, dekan, admin kepegawaian, tim verifikasi surat, dan plt. kepala biro perencanaan, umum, dan keuangan.

# **2.2.1.9. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Dekan**

<!-- Start of picture text -->
—<br>[om | status Pengauan cut— Daftar Pengajan }€—D a tr pengsan<br>ea an<br>— —7<br>merece]<br>ame tema<br>= — _y~<br>oa<br>a<br><!-- End of picture text -->

Gambar 2.10. DFD Level 2 Konfirmasi Pengajuan Cuti Oleh Dekan

Gambar 2.10. menunjukkan DFD Level 2 untuk proses konfirmasi pengajuan cuti oleh dekan, yang terdiri tiga proses, yaitu proses 7.1 untuk menampilkan daftar pengajuan cuti kepada dekan, proses 7.2 untuk input keputusan pengajuan cuti yang dilakukan oleh dekan, dan proses 7.3 untuk menampilkan status pengajuan cuti kepada _user_ , koordinator tata usaha FIK, atasan langsung, wadek 2, admin kepegawaian, tim verifikasi surat, dan plt. kepala biro perencanaan, umum, dan keuangan.

# **2.2.1.10. DFD Level 2 Pengelolaan Surat Cuti**

<!-- Start of picture text -->
:J] =<br>_ ‘| wef er]<br>: ok.<br>=e ~<br>=a<br><!-- End of picture text -->

Gambar 2.11. DFD Level 2 Pengelolaan Surat Cuti

Gambar 2.11. menunjukkan DFD Level 2 untuk proses pengelolaan surat cuti, yang terdiri tujuh proses, yaitu proses 8.1 untuk _generate_ surat cuti, proses 8.2 untuk validasi surat yang dilakukan oleh admin kepegawaian, proses 8.3 untuk pengecekan draf surat oleh ketua tim kerja kepegawaian, proses 8.4 untuk pengecekan draf surat oleh kepala bagian umum, proses 8.5 untuk pengesahan surat oleh plt. kepala biro perencanaan, umum, dan keuangan, dan proses 8.6 untuk menampilkan laporan cuti kepada koordinator tata usaha FIK, atasan langsung, wadek 2, dekan, admin kepegawaian, dan plt. kepala biro perencanaan, umum, dan keuangan, serta menampilkan surat cuti kepada _user_ .

# **2.2.2. Desain** **_Database_**

Pada tahap desain _database_ , penulis menggunakan _Entity Relationship Diagram_ (ERD) untuk merancang struktur basis data yang mendukung sistem informasi pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta. Rancangan ini bertujuan untuk menggambarkan entitas yang terlibat, atribut masing-masing entitas, serta hubungan antar entitas secara jelas dan terstruktur. Berikut adalah ERD sistem yang diusulkan:

<!-- Start of picture text -->
Qe SRS SVS alP<br>So SG (|S nee RS<br>ee Ses FES S\FS5 _2<br>a kaa a SS me KD<br>eo SS Se = eS = “ot<br>Sel ££ 2ZES es<br>Sos, a CEMEX. oe<br>to _§S3— EE /\S DIS.<br>RS> BX Ze 1} 22D KS<br>eo em SS<br><!-- End of picture text -->

Gambar 2.12. ERD

ERD pada Gambar 2.12. menunjukkan beberapa entitas, diantaranya, yaitu users, subunit, pegawai, permissions, roles, model_has_roles, role_has_permission, signature, batasan_cuti, hari_noncuti, setup_aplikasi, notifications, cuti_tahunan, foto, cuti, dan history. Relasi antara users dan pegawai bersifat _one-to-one_ , artinya

setiap _user_ hanya terkait dengan satu data pegawai, dan sebaliknya. Entitas pegawai memiliki relasi _many-to-one_ dengan entitas subunit, yang berarti banyak pegawai dapat berada dalam satu sub unit. Kemudian, users juga memiliki relasi _one-to-one_ dengan entitas signature, sehingga setiap user hanya memiliki satu tanda tangan digital. Relasi users dengan roles bersifat _many-to-many_ sehingga digunakan model pivot seperti model_has_roles. Lalu, roles dengan permissions juga membentuk relasi _many-to-many_ sehingga memerlukan pivot role_has_permissions. Sementara itu, users memiliki relasi _one-to-many_ dengan notifications, cuti_tahunan, dan cuti, yang berarti satu user dapat memiliki banyak notifikasi, data cuti tahunan, dan pengajuan cuti. Relasi cuti dengan foto bersifat _one-to-one_ , karena setiap pengajuan cuti hanya memiliki satu lampiran foto. Selanjutnya, entitas cuti memiliki relasi _many-to-one_ dengan beberapa entitas seperti hari_noncuti, setup_aplikasi, dan batasan_cuti, yang berarti banyak pengajuan cuti bisa mengacu pada data yang sama di masing-masing entitas tersebut.

# **2.3. Rancangan Proyek**

# **2.3.1.** **_Need Analysis User Interface_ dan** **_User Experience_**

Analisis ini bertujuan untuk mengidentifikasi kebutuhan visual dan interaksi pengguna terhadap sistem informasi pengajuan cuti. Dengan memahami elemen antarmuka dan pengalaman pengguna, sistem dapat dirancang agar lebih mudah digunakan, informatif, dan responsif terhadap kebutuhan pengguna.

# **2.3.1.1.** **_Need Analysis User Interface_**

Pada bagian ini, dilakukan analisis kebutuhan terhadap tampilan antarmuka pengguna atau _User Interface_ yang ada di dalam sistem. Tujuannya adalah agar tampilan sistem tidak hanya menarik secara visual, tetapi juga mudah digunakan oleh pengguna. Komponen-komponen UI yang dirancang mencakup tombol, _badge_ status, formulir, tabel, navigasi, hingga grafik visual. Masing-masing komponen dibuat untuk membantu pengguna menjalankan tugasnya dengan lebih cepat dan jelas. Tabel 2.1. menjelaskan setiap komponen UI yang digunakan, fungsinya di dalam sistem, seperti apa desain yang dibutuhkan, serta contoh implementasinya.

Tabel 2.1. _Need Analysis User Interface_

|**Komponen**<br>**_User Interface_**|**Fungsi**|**Desain yang**<br>**Dibutuhkan**|**Contoh**<br>**Implementasi**|
|---|---|---|---|
|Tombol|Memberikan<br>kontrol<br>aksi<br>kepada<br>pengguna seperti<br>menyimpan<br>data, menyetujui<br>cuti,<br>menolak,<br>menghapus, atau<br>menutup|Menggunakan dua<br>jenis tombol utama,<br>yaitu<br>tombol<br>_primary_<br>yang<br>menandai<br>aksi<br>utama pada suatu<br>form<br>seperti<br>simpan,<br>yang<br>menggunakan|Pada form pengajuan<br>cuti, tombol “_Save”_<br>ditampilkan dengan<br>warna oranye sebagai<br>tombol utama atau<br>_primary_, sedangkan<br>tombol<br>“_Close_”<br>menggunakan warna<br>abu-abu<br>sebagai|
||formulir.|warna<br>terang.<br>Selain<br>itu,<br>menggunakan<br>tombol<br>_secondary_<br>untuk<br>aksi<br>pendukung seperti<br>batal atau tutup,<br>dengan<br>desain<br>warna netral.|tombol sekunder.|
|_Badge_Status|Menampilkan<br>status pengajuan|Menggunakan<br>warna<br>berbeda|Ditampilkan<br>pada<br>kolom<br>status<br>di|
||cuti<br>secara|untuk setiap status,|halaman<br>daftar|
||visual.|merah<br>untuk|pengajuan<br>cuti.|
|||ditolak,<br>abu-abu<br>untuk<br>dibatalkan,<br>biru<br>untuk<br>menunggu,<br>dan<br>kuning<br>untuk<br>perubahan._Badge_<br>memiliki<br>bentuk|Setiap<br>status<br>memiliki warna yang<br>berbeda-beda, seperti<br>saat<br>pengajuan<br>ditolak maka_badge_<br>yang<br>ditampilkan<br>berwarna<br>merah,|

|||yang kecil dengan<br>sudut membulat.|disetujui<br>berwarna<br>hijau,<br>perubahan<br>berwarna<br>kuning,<br>menunggu diproses<br>berwarna biru, dan<br>dibatalkan berwarna<br>abu-abu.|
|---|---|---|---|
|Formulir|Menyimpan<br>input data atau<br>tindakan<br>pengguna tanpa<br>harus berpindah<br>halaman.|Ditampilkan dalam<br>bentuk modal_pop_<br>_up_. Form memiliki<br>struktur yang rapi,<br>disertai<br>validasi<br>input. Selain itu,<br>memiliki<br>pewarnaan tombol<br>yang berbeda antara<br>tombol simpan dan<br>tutup.|Pada<br>form<br>_permission_<br>yang<br>memiliki input teks<br>nama dan deskripsi,<br>beserta<br>dengan<br>tombol “_Save”_dan<br>“_Close_”_._|
|Tabel|Menyajikan data<br>secara<br>terstruktur<br>dan<br>mudah dibaca.|Tabel<br>responsif<br>dengan<br>fitur<br>pencarian,<br>pengurutan,<br>dan<br>halaman.<br>Kolom<br>aksi<br>menyediakan<br>tombol_edit_, hapus,<br>atau detail.|Pada halaman sub<br>unit<br>yang<br>menampilkan<br>tabel<br>sub unit, terdiri dari<br>kolom nomor, nama,<br>_created at_,_updated_<br>_at_, dan aksi. Tabel ini<br>disertai<br>dengan<br>kolom<br>pencarian.<br>Selain itu, pengguna<br>dapat<br>mengatur<br>jumlah data sesuai<br>kebutuhan<br>dan|

||||terdapat penomoran<br>halaman.|
|---|---|---|---|
|Navigasi<br>_Sidebar_|Memberikan<br>akses cepat ke<br>menu utama di<br>dalam sistem.|_Sidebar_<br>yang<br>terletak di sisi kiri<br>layar menampilkan<br>ikon<br>dan<br>nama<br>menu,<br>serta<br>memberikan warna<br>yang kontras untuk<br>menu yang aktif.|Akses ke halaman<br>_dashboard_,<br>menu<br>yang aktif diberikan<br>warna oranye.|
|_Card_|Menampilkan|Desain_card_dengan|Menampilkan<br>total|
|_Dashboard_|informasi<br>ringkasan<br>data<br>secara visual.|latar<br>warna<br>berbeda,<br>ikon<br>representatif,<br>dan<br>angka besar, serta<br>mudah dibaca oleh<br>pengguna.|pengajuan<br>cuti,<br>jumlah<br>yang<br>disetujui, ditolak, dan<br>sedang diproses pada<br>halaman_dashboard_<br>_user_.|
|Diagram<br>batang<br>dan|Menyajikan<br>informasi terkait|Grafik<br>dengan<br>warna yang kontras|Grafik<br>performa<br>bulanan dan waktu|
|diagram garis|rata-rata waktu<br>yang diperlukan<br>oleh setiap pihak<br>untuk<br>memproses<br>pengajuan cuti,<br>serta<br>rata-rata<br>waktu<br>yang<br>dibutuhkan<br>dalam<br>proses<br>persetujuan<br>pengajuan<br>cuti|terhadap<br>latar<br>belakang<br>untuk<br>memudahkan<br>pembacaan<br>serta<br>penamaan<br>yang<br>jelas.|penyelesaian<br>pengajuan cuti pada<br>_dashboard_ _user_.|

|setiap|bulan|
|---|---|
|pada|tahun|
|berjalan.||

# **2.3.1.2.** **_Need Analysis User Experience_**

Analisis kebutuhan pengalaman pengguna bertujuan untuk memastikan sistem informasi pengajuan cuti pegawai memberikan interaksi yang nyaman, efisien, dan mudah dipahami oleh seluruh pengguna. Komponen-komponen UX yang dirancang dalam sistem ini disesuaikan dengan kebutuhan pengguna berdasarkan peran dan aktivitas yang mereka lakukan di dalam sistem. Tabel 2.2. menjelaskan masing-masing komponen UX, tujuan utamanya, kebutuhan pengguna yang ingin dicapai, serta desain pengalaman yang diusulkan agar sistem lebih ramah dan fungsional.

Tabel 2.2. _Need Analysis User Experience_

|**Komponen**<br>**_User_**<br>**_Experience_**|**Tujuan****_User_**<br>**_Experience_**|**Kebutuhan**<br>**Pengguna**|**Desain Pengalaman**<br>**yang Diusulkan**|
|---|---|---|---|
|Navigasi Sistem|Mempermudah<br>pengguna<br>berpindah<br>antar halaman<br>dan<br>fitur<br>utama.|Menemukan<br>fitur<br>seperti cuti, laporan,<br>dan data pegawai<br>dengan cepat.|_Sidebar_dengan ikon<br>dan label teks yang<br>konsisten,<br>disertai<br>dengan<br>indikator<br>menu aktif.|
|_Feedback_<br>Visual|Memberikan<br>umpan<br>balik<br>langsung<br>setelah<br>interaksi<br>pengguna.|Pengguna<br>ingin<br>mengetahui apakah<br>aksi berhasil atau<br>gagal, serta status<br>terkini<br>dari<br>pengajuan cuti.|Menampilkan pesan<br>setelah<br>melakukan<br>penambahan,<br>perubahan,<br>atau<br>penghapusan<br>data.<br>Lalu,_badge_status<br>dengan<br>warna<br>berbeda untuk tiap|

||||status,<br>disetujui,<br>ditolak, menunggu,<br>serta pesan kesalahan<br>di bawah input jika<br>data tidak valid.|
|---|---|---|---|
|Konsistensi<br>Tampilan|Memastikan<br>pengalaman<br>antarmuka<br>seragam<br>di<br>seluruh sistem.|Pengguna<br>tidak<br>ingin<br>bingung<br>akibat<br>perbedaan<br>gaya desain atau<br>ikon.|Menggunakan warna<br>dan<br>tipografi<br>konsisten, ikon yang<br>familiar,<br>serta<br>elemen<br>UI<br>yang<br>seragam<br>di<br>setiap<br>halaman.|
|Visualisasi|Menyajikan<br>data<br>dengan<br>cara<br>yang<br>mudah<br>dipahami dan<br>dapat<br>digunakan<br>untuk<br>pengambilan<br>keputusan.|Melihat<br>ringkasan<br>cuti<br>dan<br>grafik<br>performa<br>layanan<br>pengajuan<br>cuti<br>dalam<br>bentuk<br>visual.|_Dashboard_<br>dengan<br>_card_informatif, dan<br>grafik batang atau<br>garis untuk performa<br>bulanan.|

# **2.3.2. Desain** **_User Interface_**

Rancangan Desain _User Interface_ (UI) dalam penelitian ini disusun untuk merancang tampilan dari sistem informasi pengajuan cuti pegawai pada Fakultas Ilmu Komputer UPN “Veteran” Jakarta yang akan dilakukan sebelum tahap pembangunan sistem. Dalam proses ini, peneliti menggunakan Figma sebagai alat desain. Berikut ini merupakan rancangan _user interface_ dari sistem informasi pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta.

# **2.3.2.1. Halaman** **_Login_**

<!-- Start of picture text -->
A> Sistem Informasi<br>©) FikPengajuanUPN “Veteran”Cuti PegawaiJakarta<br>ny Kompu<br>Peomaangien rasoe—<br>hadnt a<br>Sera ae<br>=—adtee ¢ ty we=<br><!-- End of picture text -->

Gambar 2.13. Halaman _Login_

Halaman _login_ digunakan oleh pengguna untuk memasukkan nomor pegawai dan _password_ . Setelah data diisi, pengguna menekan tombol “ _log in”_ untuk masuk ke dalam sistem. Di bawah tombol “ _log in_ ”, terdapat dua dokumen peraturan cuti, yaitu peraturan cuti PNS dan peraturan cuti PPPK. Kedua _file_ ini ditampilkan sebagai referensi bagi pengguna untuk memahami kebijakan cuti yang berlaku. Jika bagian dokumen ditekan maka pengguna akan diarahkan ke halaman baru yang menampilkan dokumen dalam format PDF agar mudah dibaca atau diunduh.

# **2.3.2.2. Halaman** **_Dashboard_**

<!-- Start of picture text -->
) hergoon ca ogo QD numayen<br>= “eEEDD"<br>& User Go Bo<br>Role<br>ae1 Set stotus Cuti yang Perlu Diproses Pegawalyang Akan Cutl<br>Manna Suda pon rs Te<br>8 cui Tehunan Qo Bo 80 80<br>® Konfiguasi<br>Cut<br>3. Har Noneut Performa Penyelesaian Cuti oleh Setiap Pinak Terkait di Tohun 2025<br>© Batasan cut :<br>& Tanda Tongan<br>Monojemen Cuti *<br>© ow 1}~e . . . : . : -<br>li Laporan cut [| ]<br>Performa Layanan Waktu Penyeiesaian Pengajuan Cutl Bulanan a Tahun 2025<br><!-- End of picture text -->

Gambar 2.14. Halaman _Dashboard_

Pada halaman _dashboard_ , pengguna yang memiliki akses untuk mengajukan cuti akan melihat empat kartu utama yang menampilkan informasi jumlah pengajuan cuti berdasarkan status, yaitu sedang diproses, disetujui, ditolak, dan perlu perubahan. Kartu-kartu ini memudahkan pengguna untuk mengetahui status pengajuan cuti mereka secara cepat dan ringkas. Selanjutnya, halaman _dashboard_ juga menampilkan dua grafik. Grafik pertama berbentuk _line chart_ yang memperlihatkan rata-rata waktu penyelesaian pengajuan cuti per bulan selama tahun berjalan. Waktu penyelesaian ini dihitung dalam satuan jam, sehingga pengguna bisa memahami seberapa cepat proses cuti diselesaikan dari waktu ke

waktu. Grafik kedua berupa _bar chart_ yang menampilkan rata-rata waktu penyelesaian cuti oleh setiap pemberi keputusan dalam satuan jam, sehingga dapat dilihat siapa saja yang menyelesaikan proses cuti dengan cepat atau lambat. Bagi pengguna yang berperan sebagai pemberi persetujuan, _dashboard_ akan menampilkan dua kartu tambahan yang menunjukkan total pengajuan cuti yang masih menunggu diproses dan total pengajuan yang sudah selesai diproses olehnya. Terakhir, terdapat kartu yang menunjukkan jumlah pegawai yang pengajuan cutinya telah disahkan, yang dibedakan antara dosen dan tenaga kependidikan. Informasi ini ditampilkan khusus untuk koordinator tata usaha FIK dan admin kepegawaian.

# **2.3.2.3. Halaman** **_User_**

<!-- Start of picture text -->
Cerner Qt<br>D Subunit<br>{® KonfigurasiCuti 3 oto Provetyo: oominkepeg. —<br>Hari Noncuti 4 Det testa “oomintUFMuser f acton wv |<br>© Batasan Cutt a<br>@ Tanda Tangan<br><!-- End of picture text -->

Gambar 2.15. Halaman _User_

Pada halaman ini, sistem menampilkan tabel yang memuat daftar _user_ dengan informasi seperti nama dan _role_ masing-masing pegawai. Di bagian atas halaman tersedia tombol “Tambah” untuk menambahkan _user_ baru, serta filter berdasarkan sub unit untuk mempermudah pencarian data pegawai. Pada setiap baris data dalam tabel, terdapat kolom aksi yang apabila diklik akan menampilkan tombol “ _Edit_ ” untuk memperbarui informasi _user_ , dan tombol “ _Delete_ ” untuk menghapus data

_user_ dari sistem. Halaman _user_ dapat diakses oleh koordinator tata usaha FIK dan admin kepegawaian.

<!-- Start of picture text -->
form User Pi<br>Pin Pagowat<br>[ram pean a<br>la regowo! arma gona<br>oxo Pease Fine roan<br>ES) EEE<br>Jeboton unit ker<br>en aE<br>Colongon JenisKelorin<br>EEE EEE<br>Tongget owt stot Pegowo!<br>nnhs<br>kmail foe<br>( J[ rime<br>Subunit porewordSt~CS<br>[rmeon Sv if<br><!-- End of picture text -->

Gambar 2.16. Halaman Form _User_

Form _user_ akan ditampilkan saat pengguna menekan tombol "Tambah". Pada form ini terdapat _dropdown_ untuk memilih pegawai dari daftar pegawai di lingkungan universitas. Setelah salah satu pegawai dipilih, sistem akan secara otomatis menampilkan data seperti id pegawai, nama, nomor pegawai, tipe pegawai, jabatan, unit kerja, golongan, jenis kelamin, tanggal masuk, email, dan status pegawai. Dengan demikian, pengguna tidak perlu mengisi data tersebut secara manual. Pengguna dapat menentukan sub unit dan _role_ dari pegawai yang dipilih.

<!-- Start of picture text -->
Form user z<br>ain agowal<br>[ 22-mamoyotnosonon<br>Foion im orp v]<br>1a[2NomorPegawotPegowo amamanayoutonnnPegow |<br>voc Tipe egowai<br>Joboten (sen)<br>oven Tete unitFotos keia komputer<br>cotongon Jane Keomin<br>Mosuk status Fogowo!<br>Tanggol |<br>[2015-02-01 mo<br>Emauhoytiouen cia rolewer al<br>subunit rosswora<br><!-- End of picture text -->

Gambar 2.17. Halaman Form _User_ Terisi

Gambar 2.17 memperlihatkan kondisi halaman form _user_ setelah data pegawai berhasil ditampilkan secara otomatis. Data-data pegawai yang relevan telah terisi di dalam form, sehingga pengguna hanya perlu melengkapi informasi tambahan seperti sub unit dan _role_ sebelum menyimpan data. Pada bagian bawah form _user_ , terdapat dua tombol, yaitu tombol " _Save_ " dan " _Close_ ". Tombol " _Save_ " berfungsi untuk menyimpan data _user_ yang telah diisi atau dipilih pada form ke dalam sistem. Setelah tombol ini ditekan, sistem akan memproses dan menyimpan informasi pegawai beserta sub unit dan _role_ yang telah ditentukan. Sementara itu, tombol " _Close_ " digunakan untuk menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
Apakah Anda Yokin?<br>‘ingoxan in oak dopet ototont<br><!-- End of picture text -->

Gambar 2.18. Hapus _User_

_Pop up delete_ menunjukkan tampilan konfirmasi saat pengguna menekan tombol " _Delete_ ". Sistem akan menampilkan _pop up_ konfirmasi yang berisi pertanyaan untuk memastikan apakah pengguna benar-benar ingin menghapus data _user_ yang dipilih. Pada _pop up_ ini terdapat dua tombol yaitu "Ya, Hapus" untuk melanjutkan proses penghapusan data, dan "Batal" untuk membatalkan aksi dan menutup _pop up_ tanpa menghapus data apapun.

# **2.3.2.4. Halaman** **_Role_**

<!-- Start of picture text -->
(®)‘Rengojuon‘Rein venCut  snaPegowot DQ wurmayors<br>@ Dasnooars seit<br>“ee oxi)<br>==8 User  ~ —_<br>Permission “ me crete epaateg at<br>1D) sium 1 cn sess wovaesien [scr|<br>8 cuiTahunan 2 wpm wenzesien wonsemien om<br>©<br>Kontguresict 2 own were ovsennien co<br>8 Har noneut 6 wot wevsemien onsenen oo<br>© atasan cut 5 tot weve wanaensien a<br>& Tnda Tongan pea seamen wonton oo<br>Monojemen cut 7 canmtneg were wovsensien oo<br>2 cw © amt ween worsen en [|<br>1 Laporan cut sronig to teen iB<br><!-- End of picture text -->

Gambar 2.19. Halaman _Role_

Halaman _role_ menampilkan daftar _role_ atau peran yang digunakan dalam sistem. Pada halaman ini, pengguna dapat melihat seluruh _role_ yang telah terdaftar beserta waktu dibuat dan diubah. Tersedia tombol “Tambah” untuk menambahkan _role_ baru, serta tombol “ _Edit_ ” dan “ _Delete_ ” di setiap baris data untuk memperbarui atau menghapus _role_ yang ada.

<!-- Start of picture text -->
Form Role «<br>Nama<br>Destrips!<br>Permissions,<br>road-users: teod-roles reod-permissions<br>reod-jabatan tead-cuti-tahunen | read-setup-<br>coplikasi<br>edit-hari-nencuti_— read-batasan- croote-hari-<br>cut roncuti<br>read-rignature read-cuti read-hari-noncuti<br>create-cuti read-laporan ‘opprove<br><!-- End of picture text -->

Gambar 2.20. Halaman Form _Role_

Form tambah _role_ menunjukkan tampilan form yang digunakan pengguna untuk menambahkan _role_ baru. Form ini memuat input untuk nama _role_ , deskripsi singkat mengenai _role_ tersebut, serta daftar _permission_ atau hak akses yang dapat dipilih melalui ceklis. Pengguna dapat menyesuaikan hak akses setiap _role_ dengan mencentang _permission_ yang sesuai. Hal ini memastikan bahwa setiap _role_ memiliki akses yang tepat dan sesuai tanggung jawabnya dalam sistem.

<!-- Start of picture text -->
Form Role *<br>Destripsi<br>-mengoboiokeseluunan sistem<br>Broad-users B reod-roies 8 reoa-permissions<br>@reac-javatan —_-@ raad-cuti-tahunan @ read-setup-<br>copikasi<br>Bodit-nari-noncuti @reod-batasen- _@ cteate-hari-<br>cut oneuti<br>Biroad-signature — @ rood-cut! 8 rooa-hari-noneuti<br>‘reate-cutl @ reod-taporan opprove<br><!-- End of picture text -->

Gambar 2.21. Halaman Form _Role_ Terisi

Form _role_ terisi menampilkan kondisi form setelah data _role_ dimasukkan. Nama _role_ , deskripsi, dan beberapa _permission_ telah dicentang sesuai kebutuhan. Di bagian bawah form terdapat dua tombol, yaitu “ _Save_ ” dan “ _Close_ ”. Tombol " _Save_ " digunakan untuk menyimpan data _role_ beserta _permission_ yang telah dipilih, sementara tombol " _Close_ " berfungsi untuk menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
Apakah Anda Yakin?<br>“Tindaton in tidok dapet alpatatkan!<br><!-- End of picture text -->

Gambar 2.22. Hapus _Role_

_Pop up delete role_ muncul saat pengguna menekan tombol “ _Delete_ ” pada salah satu _role_ . Sistem akan menampilkan _pop up_ konfirmasi untuk memastikan apakah pengguna benar-benar ingin menghapus _role_ tersebut. Di dalam _pop up_ terdapat dua tombol, yaitu “Ya, Hapus” untuk melanjutkan proses penghapusan, dan “Batal” untuk membatalkan dan menutup _pop up_ .

# **2.3.2.5. Halaman** **_Permission_**

<!-- Start of picture text -->
(3) Pengojuan Cuti Pegowa! D numrayart<br>@ Dasnboars List Permission<br>& User<br>pole<br>1 sununt a eons women oo<br>® Cuti Tahunan 2 read-soperan 15-09-2025 10.22 18-09-2028 1022 ~<br>{® Konfigurasi Cuti 3 create-cuth 18-03-2028 1022 18-02-2028 1022 aed<br>Monajemen Cuti wing 10 8016 oti a<br>© cw<br>ll Laporan Cuti<br><!-- End of picture text -->

Gambar 2.23. Halaman _Permission_

Halaman _permission_ menampilkan daftar data _permission_ yang tersedia dalam sistem. Setiap _permission_ ditampilkan dalam bentuk tabel dengan informasi seperti nama _permission_ , tanggal dibuat ( _Created At_ ), dan tanggal diperbarui ( _Updated At_ ). Di setiap baris tabel, tersedia tombol " _Edit_ " untuk memperbarui nama atau deskripsi _permission_ , serta tombol " _Delete_ " untuk menghapus _permission_ dari sistem.

<!-- Start of picture text -->
Form Porlson .<br>conte<br>a|<br><!-- End of picture text -->

Gambar 2.24. Halaman Form _Permission_

Form tambah _permission_ digunakan pengguna untuk menambahkan _permission_ baru ke dalam sistem. Form ini berisi _field_ untuk mengisi nama _permission_ dan deskripsi yang menjelaskan fungsi dari _permission_ tersebut. Di bagian bawah form, terdapat dua tombol, yaitu " _Save_ " untuk menyimpan data _permission_ baru dan " _Close_ " untuk menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
Form Peieion .<br>wee=<br>Se<br>8<br><!-- End of picture text -->

Gambar 2.25. Halaman Form _Permission_ Terisi

Form _permission_ terisi menampilkan kondisi form setelah data _permission_ dimasukkan oleh pengguna. _Field_ nama dan deskripsi _permission_ telah terisi, dan pengguna dapat memverifikasi informasi tersebut sebelum menyimpannya. Terdapat dua tombol yaitu " _Save_ ", yang akan menyimpan perubahan atau penambahan data ke dalam sistem, dan " _Close_ ", yang akan menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
Apakah Anda Yakin?<br>‘Tindokon in tidok dapet eibatotkant<br><!-- End of picture text -->

Gambar 2.26. Hapus _Permission_

_Pop up delete permission_ muncul saat pengguna menekan tombol " _Delete_ " pada salah satu _permission_ di tabel. Sistem akan menampilkan _pop up_ konfirmasi yang bertujuan untuk mencegah penghapusan data secara tidak sengaja. Di dalam _pop up_ terdapat dua tombol, yaitu "Ya, Hapus" untuk melanjutkan penghapusan _permission_ , dan "Batal" untuk membatalkan aksi dan menutup _pop up_ .

# **2.3.2.6. Halaman Sub Unit**

<!-- Start of picture text -->
= os<br>oases —<br>2, oa<br>meee : [<br>pac — a a i:<br>8 cw Tenunan 2 omen wensesien seramsien. -<br>®@ Kontigueasi<br>Cuti 3 rmogetepenaiton 00-2008 022, seen 20281022 [Rall|<br>© Hor none Sniigiicia ain ou<br>nike<br>seam<br>mains<br>aca<br>‘til Laporan Cutt<br><!-- End of picture text -->

Gambar 2.27. Halaman Sub Unit

Halaman sub unit menampilkan daftar sub unit kerja yang ada di fakultas ilmu komputer. Data ditampilkan dalam bentuk tabel dengan kolom nama, _created at_ atau tanggal dibuat, dan _updated at_ atau tanggal diperbarui. Di bagian atas halaman terdapat tombol “Tambah” untuk menambahkan sub unit baru. Setiap baris data dalam tabel juga dilengkapi dengan tombol “ _Edit_ ” untuk memperbarui informasi sub unit, serta tombol “ _Delete_ ” untuk menghapus sub unit dari sistem. Halaman sub unit dapat diakses oleh admin kepegawaian dan koordinator tata usaha FIK.

Gambar 2.28. Halaman Form Sub Unit

Form tambah sub unit digunakan untuk menambahkan data sub unit baru ke dalam sistem. Form ini berisi satu _field_ input untuk mengisi nama sub unit, dan dua tombol di bagian bawah yaitu " _Save_ " untuk menyimpan data dan " _Close_ " untuk menutup form tanpa menyimpan perubahan.

Gambar 2.29. Halaman Form Sub Unit Terisi

Form sub unit terisi memperlihatkan tampilan form setelah nama sub unit diisi oleh pengguna. Tombol " _Save_ " digunakan untuk menyimpan data ke sistem, sedangkan tombol " _Close_ " digunakan pengguna keluar dari form tanpa melakukan penyimpanan.

<!-- Start of picture text -->
‘Apakah<br>"ncokon in dexAn d apata Yakin? evotakan!<br><!-- End of picture text -->

Gambar 2.30. Hapus Sub Unit

_Pop up delete_ sub unit muncul saat pengguna menekan tombol " _Delete_ " pada salah satu data sub unit di tabel. Sistem akan menampilkan _pop up_ konfirmasi untuk memastikan tindakan penghapusan. Di dalam _pop up_ terdapat dua tombol, yaitu "Ya, Hapus" untuk menghapus data secara permanen, dan "Batal" untuk membatalkan tindakan dan menutup _pop up_ .

# **2.3.2.7. Halaman Cuti Tahunan**

<!-- Start of picture text -->
@ Dashboard Tahun Total<br>& User<br>B supunit show { 10v | énties seorete<br>™ ”<br>@ Konfigurasi<br>Cuti : sun sone .<br>1 Hace —_ _ : : worsen worn PY<br>rgemen ca 5 vont 2008 2 2 16-09-2028 1022 26-08-20281022<br><!-- End of picture text -->

Gambar 2.31. Halaman Cuti Tahunan

Halaman cuti tahunan menampilkan daftar cuti tahunan seluruh pegawai fakultas ilmu komputer, yang terdiri atas informasi nama pegawai, tahun, total, dan jumlah cuti yang telah digunakan. Terdapat tombol "Tambah" untuk menambahkan data tiap pegawai, serta opsi untuk mengubah atau menghapus masing-masing data pegawai. Pada bagian atas halaman, tersedia fitur " _Generate_ Cuti Tahunan Massal" yang akan secara otomatis membuat data cuti tahunan bagi seluruh pegawai berdasarkan input tahun dan total cuti yang ditentukan. Fitur tersebut dapat diakses oleh koordinator tata usaha FIK.

<!-- Start of picture text -->
Form Cut tahunan .<br>run Pegowst Digunaton<br>inten { ]<br><!-- End of picture text -->

Gambar 2.32. Halaman Form Cuti Tahunan

Pada form cuti tahunan, pengguna dapat mengisi data cuti tahunan untuk seorang pegawai. Tersedia input untuk tahun dan total cuti yang dialokasikan pada tahun tersebut. Untuk memilih pegawai, pengguna cukup menekan _field_ "Pilih Pegawai", yang akan memunculkan tabel berisi daftar pegawai. Dari tabel tersebut, pengguna dapat memilih salah satu pegawai, dan nama pegawai yang dipilih akan otomatis ditampilkan pada form. Setelah data dilengkapi, pengguna dapat menyimpannya melalui tombol yang tersedia. Kolom “Digunakan” hanya ditampilkan sebagai informasi dan tidak dapat diubah. Kolom ini akan terisi secara otomatis berdasarkan data pengajuan cuti yang telah disetujui.

<!-- Start of picture text -->
List user .<br>1 tase =]<br>coaster2 emtnnet ve a<br><!-- End of picture text -->

Gambar 2.33. Halaman List _User_

Pada tampilan ini, saat pengguna membuka form cuti tahunan dan menekan kolom pilih pegawai, sistem akan menampilkan daftar pegawai yang tersedia. Pengguna dapat memilih salah satu pegawai dari daftar tersebut. Setelah salah satu nama dipilih, maka nama pegawai secara otomatis akan ditampilkan di form sesuai pilihan pengguna.

<!-- Start of picture text -->
‘Apakah Anda Yakin?<br>Tindatan ini tidak dapat dibotoltant<br><!-- End of picture text -->

Gambar 2.34. Hapus Cuti Tahunan

_Pop up delete_ muncul ketika pengguna menekan tombol “ _Delete_ ” pada salah satu data cuti tahunan. Sistem akan menampilkan konfirmasi penghapusan untuk memastikan bahwa tindakan tersebut diinginkan. _Pop up_ ini berisi dua tombol, yaitu “Ya, Hapus” untuk melanjutkan proses penghapusan data, dan “Batal” untuk membatalkan dan menutup _pop up_ tanpa menghapus data.

# **2.3.2.8. Halaman Konfigurasi Cuti**

<!-- Start of picture text -->
Ore 0 wor<br>@ Desnnocee st Kontigurasi<br>=~ [eo] ae ~<br>rs Cuti<br>—& User “5 rare eee rar<br>i i er ee |<br>1D) subunit ‘showing 1101 of Vertres il ~<br>@ Cut Taunan<br>==ms<br>iS nae<br>emo<br>@ Tanda Tangan<br>pane<br>8 cw<br>lh Laporan Cutt<br><!-- End of picture text -->

Gambar 2.35. Halaman Konfigurasi Cuti

Halaman konfigurasi cuti digunakan untuk menentukan hari kerja yang akan digunakan sebagai dasar perhitungan jumlah hari cuti yang diajukan oleh pemohon. Data ditampilkan dalam bentuk tabel yang memuat kolom hari kerja, _created at_ , dan _updated at_ . Pada baris terdapat tombol “ _Edit_ ” yang dapat digunakan pengguna untuk memperbarui konfigurasi hari kerja sesuai kebijakan yang berlaku. Halaman ini dapat diakses oleh admin kepegawaian dan koordinator tata usaha FIK.

<!-- Start of picture text -->
i eit :<br>}<br>ces]--- ]<br><!-- End of picture text -->

Gambar 2.36. Halaman Form Konfigurasi Cuti

Saat pengguna menekan tombol “ _Edit_ ”, sistem akan menampilkan form konfigurasi cuti. Pada form ini, pengguna dapat memilih hari kerja melalui _dropdown_ yang berisi daftar nama hari, senin sampai minggu. Pengguna dapat memilih lebih dari satu hari sebagai hari kerja aktif.

<!-- Start of picture text -->
Form kontigrasCut -<br>eee<br>a|<br><!-- End of picture text -->

Gambar 2.37. Halaman Form Konfigurasi Cuti Terisi

Form konfigurasi cuti terisi menampilkan tampilan setelah pengguna memilih beberapa hari kerja dari _dropdown_ . Hari-hari yang telah dipilih akan terlihat di dalam _field_ sebagai indikator pilihan aktif. Setelah selesai, pengguna dapat menyimpan perubahan melalui tombol yang tersedia. Dengan tampilan ini, pengguna dapat meninjau kembali pilihan hari kerja sebelum menyimpannya, untuk memastikan perhitungan hari cuti berjalan sesuai kebijakan fakultas.

# **2.3.2.9. Halaman Hari Noncuti**

<!-- Start of picture text -->
6) bengahion cu Pepowa QD wroyet<br>1G Sachhnoend lst Hori Noneut<br>hy a May 2025 =<br>D) subunit<br><!-- End of picture text -->

Gambar 2.38. Halaman Hari Noncuti

Halaman hari noncuti menampilkan tampilan kalender yang dilengkapi dengan tombol navigasi berupa ikon “<” dan “>” untuk melihat bulan-bulan lain sesuai keinginan pengguna. Selain itu, terdapat tombol dengan teks “Hari Ini” yang berfungsi untuk menampilkan kembali bulan dan tahun saat ini. Jika terdapat hari noncuti yang telah didaftarkan, maka pada tanggal terkait akan ditampilkan label berwarna merah beserta keterangan teks sebagai penanda. Halaman ini dapat diakses oleh seluruh pengguna, tetapi yang memiliki akses untuk melakukan penambahan, perubahan, dan penghapusan data hari noncuti adalah koordinator tata usaha FIK, admin kepegawaian, dan plt. kepala biro perencanaan, keuangan, dan umum.

<!-- Start of picture text -->
Form Hari Noncuti x<br>Nome<br>]<br>Tonggot21-05-2008,Awol 1) |Tanggota+-08-2008 Ati 5]<br>© cwiorer<br><!-- End of picture text -->

Gambar 2.39. Halaman Form Hari Noncuti

Untuk menambahkan hari noncuti, pengguna dapat klik tanggal yang terdapat pada tampilan kalender. Setelah itu, sistem akan menampilkan form hari noncuti. Pengguna kemudian mengisi nama hari noncuti serta tanggal awal dan tanggal akhirnya, lalu menekan tombol “ _Save_ ” untuk menyimpan data tersebut ke dalam sistem.

<!-- Start of picture text -->
Form Hari Noncuti *<br>Nama<br>fopot Fk<br>Tanggol21-08-2025Awat | ‘Tengge[ 2-08-2025Athi C)<br>© vwiere?<br><!-- End of picture text -->

Gambar 2.40. Halaman Form Hari Noncuti Terisi

Untuk menghapus hari noncuti, pengguna dapat mengaktifkan tombol alih yang terletak di bawah input tanggal awal hari noncuti. Setelah tombol diaktifkan, pengguna dapat menekan tombol “ _Save_ ” untuk menyimpan perubahan dan data hari noncuti tersebut akan terhapus dari sistem.

# **2.3.2.10. Halaman Batasan Cuti**

<!-- Start of picture text -->
i) seca liao QD. nmayon<br>@ Dewnces Ust BatasanCut<br>& User<br>seee [wwe oun<br>© Roe<br>Cut Tahunan 2 a-2028 boven ‘ew tononan , 18-09-20280.. 28-03-2025 -<br>@ KonfigurasiCuti =<br>1 TandTangan<br>2 ow<br>ba Lapocan cs<br><!-- End of picture text -->

Gambar 2.41. Halaman Batasan Cuti

Halaman batasan cuti dirancang untuk mengatur batas jumlah pengajuan cuti berdasarkan kombinasi jenis cuti, jenis pegawai, dan periode waktu  dalam bulan dan tahun. Pengguna dapat menetapkan batasan berupa persentase dari total pegawai fakultas ilmu komputer. Misalnya, jika ditetapkan 10 pada bulan februari tahun 2025 untuk jenis cuti melahirkan dan jenis pegawai dosen, maka maksimal 10% dari total dosen di FIK dapat mengajukan cuti tersebut di bulan itu. Halaman ini menampilkan tabel berisi daftar batasan cuti yang sudah dibuat, dan dilengkapi tombol “Tambah” untuk menambahkan batasan baru. Pada kolom aksi, tersedia tombol “ _Edit_ ” untuk mengubah batasan yang ada, serta “ _Delete_ ” untuk menghapusnya. Halaman batasan cuti dapat diakses oleh koordinator tata usaha FIK, admin kepegawaian, ketua tim kerja kepegawaian, kepala bagian umum, dan plt. kepala biro perencanaan, keuangan, dan umum.

<!-- Start of picture text -->
Form ataron Cut :<br>eieitsm _eiet<br>|<br>[<br>a |<br><!-- End of picture text -->

Gambar 2.42. Halaman Form Batasan Cuti

Pada halaman form batasan cuti, pengguna dapat memasukkan informasi terkait batas cuti dengan mengisi bulan, tahun, jenis pegawai, jenis cuti, dan total batasan. Terdapat tombol “ _Save_ ” untuk menyimpan data yang telah diinput dan tombol “ _Close_ ” untuk kembali ke halaman batasan cuti.

<!-- Start of picture text -->
Form Botoson cut "<br>a|<br><!-- End of picture text -->

Gambar 2.43. Halaman Form Batasan Cuti Terisi

Tampilan ini menunjukkan kondisi form batasan cuti setelah seluruh data diisi oleh pengguna. _Field_ bulan, tahun, jenis cuti, jenis pegawai, dan total atau persentase telah terisi sesuai dengan kebutuhan. Misalnya, total diisi dengan nilai “10” yang berarti hanya maksimal 10% dari jumlah pegawai dengan jenis tersebut

di FIK yang dapat mengajukan cuti pada periode tersebut. Pengguna dapat menekan tombol " _Save_ " untuk menyimpan data, atau memilih tombol " _Close_ " untuk menutup form tanpa melakukan penyimpanan.

<!-- Start of picture text -->
‘Apakah<br>Tndokon in takAn d apata Y a lbotatian!kin?<br>_-~)<br><!-- End of picture text -->

Gambar 2.44. Hapus Batasan Cuti

Saat tombol " _Delete_ " diklik, sistem akan menampilkan _pop up_ konfirmasi dengan dua pilihan tombol, yaitu "Ya, Hapus" untuk melanjutkan penghapusan data, dan "Batal" untuk membatalkan tindakan tersebut

# **2.3.2.11. Halaman Tanda Tangan**

<!-- Start of picture text -->
© Pengakion‘eu vero cs Pagansare D. mumove<br>@ Dashboard ‘Tanda Tongan<br>Pengaturon ‘buat Tanda Tangon ‘Tendo Tongon Saya<br>3B veer<br>1seenRole tam tnd targon<br>Subunit<br>8 cut Tanunan<br>8 ontario oy |<br>8 Hari one<br>© batasan cut<br>=<br>Manojemen<br>Cutt<br>© ow<br>lit Laporan cut<br><!-- End of picture text -->

Gambar 2.45. Halaman Tanda Tangan

Saat pengguna menekan menu "Tanda Tangan", sistem akan menampilkan halaman khusus yang digunakan untuk mengatur paraf dan tanda tangan digital. Halaman ini hanya dapat diakses oleh ketua tim kerja kepegawaian dan kepala bagian umum untuk keperluan paraf, serta oleh plt. kepala biro perencanaan, keuangan, dan umum untuk keperluan tanda tangan. Pada area di sisi kanan jika data tanda tangan atau paraf belum pernah diunggah, maka akan muncul tulisan “Belum ada tanda tangan”. Namun, apabila data telah tersedia, maka gambar tanda tangan atau paraf pengguna akan langsung ditampilkan. Di bagian kiri terdapat kolom untuk menggambar paraf atau tanda tangan, serta tombol “Simpan” untuk menyimpan atau memperbarui data yang dimasukkan dan tombol “Hapus” untuk menghapus tanda tangan atau paraf yang telah digambar.

# **2.3.2.12. Halaman Cuti**

<!-- Start of picture text -->
@ rengejon Cut Pegawol Daye<br>@ astoors List PengojvanCut<br>& User<br> swune 1 rxeootee tgttoneo then ee SD EEE<br>8 cutiTehunan 2 Fe18020003 naMoring Yotunan os-ae-2005 oscanoes EES EES<br>©<br>Kootiguasicut 3 retowte2 omiietat theese eon) ED ED<br>© Hari Noncuti 4 remow00o1 simoemnon tonnen oases oases) SD EES<br>Tanda Tngon<br>[oo<br>id Loporan cut<br><!-- End of picture text -->

Gambar 2.46. Halaman Cuti

Halaman cuti menampilkan daftar pengajuan cuti pegawai dalam bentuk tabel yang berisi informasi lengkap, seperti nomor, nama pegawai, jenis cuti, tanggal awal cuti, tanggal akhir cuti, total atau lama cuti dalam satuan hari, serta status pengajuan cuti seperti dibatalkan yang diberi warna abu-abu, ditolak yang diberi warna merah, dan disahkan yang diberi warna hijau. Pada bagian atas halaman, tersedia tombol “Tambah” yang hanya akan muncul apabila pengguna memiliki

akses untuk membuat pengajuan cuti. Selain itu, halaman ini dilengkapi dengan dua filter utama untuk memudahkan pencarian dan penyaringan data. Filter pertama adalah _dropdown_ “Semua Pengajuan”, yang dapat digunakan pengguna untuk memilih antara “Semua Pengajuan” atau “Pengajuan Saya”. Filter tersebut hanya akan terlihat oleh pengguna yang memiliki akses untuk mengajukan cuti sekaligus memberikan persetujuan cuti. Filter kedua adalah filter berdasarkan status pengajuan, yang menyediakan opsi “Ditolak”, “Dibatalkan”, “Disahkan”, “Menunggu Diproses”, atau “Semua Status”.

<!-- Start of picture text -->
Form Cut “<br>woe Wo regawal<br> _<br>|<br>[[retutos tins Komp 3 =<br>status(REPepowel  (waive roe sre x v]<br>reagent renggol aie<br>Pilih Tanggat Pin Tanggat oe}<br>a |<br>ES |<br>as catsoncutem&<br>GLEs<br>No ep stoma cut<br>sone soca<br>omonaah<br>aEERE] me ctooon<br><!-- End of picture text -->

Gambar 2.47. Form Cuti

Halaman form pengajuan cuti dirancang untuk memudahkan pengguna dalam mengajukan cuti dengan menampilkan data pegawai yang akan terisi secara otomatis dan tidak dapat diubah, seperti nama, nomor pegawai, masa kerja, unit kerja, dan jabatan. Selain itu, di dalam form juga menampilkan informasi sisa cuti

tahunan, yang mencakup total sisa cuti yang dapat digunakan, hasil dari penjumlahan sisa cuti tahun berjalan, tahun sebelumnya, dan dua tahun sebelumnya. Sistem juga menampilkan catatan riwayat penggunaan cuti lainnya seperti cuti sakit, cuti melahirkan, cuti besar, dan cuti alasan penting. Selanjutnya, pengguna dapat memilih jenis cuti sesuai dengan kebutuhan. Pemohon juga memilih tanggal mulai dan tanggal selesai cuti, mengisi alamat tempat tinggal selama cuti, nomor telepon yang dapat dihubungi, dan keterangan atau alasan cuti. Selain itu, _user_ dapat mengunggah dokumen tambahan apabila memilih jenis cuti selain tahunan. Setelah semua data diisi, pemohon dapat memilih tombol “ _Save_ ” untuk mengajukan cuti atau “ _Close_ ” untuk menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
sone sores<br>sossnn a<br>e<br>so<br>Pain Tenege! 5]<br>sy<br>vsa<br><!-- End of picture text -->

Gambar 2.48. Form Cuti Memilih Jenis Cuti

Setelah menekan bagian pilih jenis cuti, _dropdown_ "Jenis Cuti" akan secara otomatis menampilkan daftar pilihan cuti yang sesuai dengan hubungan kerja atau

status kepegawaian yang dimiliki. Sistem menampilkan pilihan jenis cuti berdasarkan hubungan kerja pegawai yang sedang mengajukan cuti. Untuk pegawai dengan status PPPK, sistem menampilkan pilihan cuti seperti cuti tahunan, cuti sakit, dan cuti melahirkan. Sementara itu, untuk pegawai PNS atau Non ASN, _dropdown_ akan mencakup pilihan seperti cuti tahunan, cuti sakit, cuti melahirkan, cuti besar, dan cuti alasan penting. Adapun untuk pegawai kontrak, hanya ditampilkan opsi cuti tahunan dan cuti melahirkan.

<!-- Start of picture text -->
|.<br>= Se<br>Fokuitos timu Komputer | | Dosen j]<br>a<br>ven ue wed mu rt ot om |<br>Be Gd GT (1) Bl 5 sicocuvaon<br>suoune i<br>CGRBLGRTCURT SELIEII catatoncut Alosan Pent<br>LE<br>a<br>—<br><!-- End of picture text -->

Gambar 2.49. Form Cuti Memilih Tanggal

Saat pengguna menekan bagian pilih tanggal awal atau tanggal akhir cuti, akan muncul tampilan kalender yang memudahkan pemilihan tanggal. Namun, untuk jenis cuti tahunan, sistem memiliki aturan khusus yang tidak memperbolehkan tanggal cuti jatuh pada hari yang sudah terdaftar sebagai hari noncuti. Jika pengguna memilih tanggal yang termasuk hari noncuti, maka sistem akan

menampilkan notifikasi singkat berupa _toast message_ dengan pesan, “Tanggal yang dipilih merupakan hari noncuti”. Pesan tersebut muncul secara otomatis untuk memberi tahu pengguna agar memilih tanggal lain.

<!-- Start of picture text -->
Form Cuti *<br>rary areal<br>| __-<br>[omenteap di(Senate<br>[fentontu tnpew T) ( seein)<br>ston omen Jesu<br>a (ro — Z<br>12-08-2028 || 05-2025 Ey<br>i)<br>fia Gut 2028 ‘one<br>LE Eee<br>o 9<br>to Tp famaGu<br>—<br>Aomet salam Cut<br>“Mower Raya Neto<br>cmap<br>eT<br>—<br>Ls<br><!-- End of picture text -->

Gambar 2.50. Form Cuti Terisi

Setelah pengguna memasukkan tanggal awal dan tanggal akhir cuti, kolom total pengajuan cuti akan secara otomatis terisi dengan menghitung jumlah hari cuti berdasarkan rentang tanggal tersebut. Untuk jenis cuti tahunan dan cuti alasan penting, perhitungan dilakukan berdasarkan hari kerja, yaitu hanya menghitung hari senin hingga jumat. Sedangkan untuk jenis cuti sakit, melahirkan, dan cuti besar, perhitungan total cuti dihitung berdasarkan hari kalender.

<!-- Start of picture text -->
a) Pengaivan ut Pegowat DQ. sgeesomone<br>@ Dashoard Lise Pengoluancut<br>Har None<br><!-- End of picture text -->

Gambar 2.51. Halaman Cuti Menunggu Diproses

Tampilan halaman menu pengajuan cuti pada Gambar 2.51. menunjukkan daftar pengajuan yang telah dikirim oleh pengguna. Setelah pengajuan dikirim, data akan masuk ke dalam tabel dengan status menunggu diproses. Pada tombol “ _Action_ ” apabila diklik maka akan tampil tiga opsi aksi, yaitu tombol “Detail” untuk melihat detail dari pengajuan cuti, tombol “Batalkan” untuk membatalkan pengajuan yang masih dalam proses, dan tombol “ _Edit_ ” untuk melakukan perubahan pada data cuti. Pemohon dapat melakukan perubahan data cuti selama belum ada pihak yang memberikan konfirmasi persetujuan. Namun, apabila pihak lain melakukan konfirmasi berupa perubahan maka pemohon dapat melakukan perubahan pada data cuti.

<!-- Start of picture text -->
Form *<br>tone qvssonoms tts Yenanon 12<br>mmngontnia toe oto cunnoiten 8<br>imino sii oer Cutan ening: @<br>© Pereraan<br>Wott Penytesoan:12 40m<br>‘iwayat Approval<br>=<br>Pangojuon<br>‘tenurgguenurgge FestinaCuOpes lah Aan Pemonon fepegonnian Gow<br>enunggu<br>ace Ketua Tim kaya kepegawcion<br>enunggu<br>ace Kobog Umum<br>‘rengesonan<br>Surat le Pt. apa roParencaKauango no d n Umumon<br><!-- End of picture text -->

Gambar 2.52. Form Detail Pengajuan Cuti

Formulir detail cuti akan ditampilkan saat pengguna menekan tombol "Detail". Di dalam formulir ini terdapat informasi data pegawai dan data cuti yang diajukan. Pada bagian bawah, ditampilkan perkiraan waktu penyelesaian proses pengajuan cuti. Di bawahnya lagi terdapat riwayat persetujuan dalam bentuk _timeline_ , di mana proses terakhir yang telah dilakukan adalah pengajuan cuti oleh pemohon, yang disertai dengan tanggal pada bagian atas. Proses-proses selanjutnya yang masih menunggu persetujuan juga ditampilkan dalam urutan sesuai alur yang akan dilalui.

<!-- Start of picture text -->
Form Batalkan Cuti *<br>‘lazon<br><!-- End of picture text -->

Gambar 2.53. Form Pembatalan Cuti

Formulir pembatalan cuti akan ditampilkan saat pengguna menekan tombol "Batalkan" pada bagian aksi. Pemohon dapat mengisi alasan pembatalan cuti, kemudian menekan tombol " _Save_ " untuk menyimpan data atau “ _Close_ ” untuk menutup form tanpa menyimpan perubahan.

<!-- Start of picture text -->
a) argon ct regan QD. Aavsontoso<br>iS "Coated List Pengajuan Cut —<br>Rengetwon© Hari Noncuti ==] ‘Somua Status v<br>anojemen Cut<br><!-- End of picture text -->

Gambar 2.54. Halaman Cuti Telah Disahkan

Apabila pengajuan cuti telah disetujui hingga tahap akhir, maka status akan ditampilkan sebagai "Disetujui". Pemohon dapat klik tombol "Detail" untuk melihat rincian pengajuan cuti atau klik tombol "Surat" untuk melihat surat cuti yang telah diterbitkan. Selain perubahan status, sistem juga akan mengirimkan notifikasi di web kepada pemohon dengan pesan bahwa surat cuti telah disahkan. Pemohon juga akan menerima pemberitahuan melalui email, berisi informasi bahwa pengajuan cutinya telah disetujui.

<!-- Start of picture text -->
Form *<br>_ son tonone eta sua cut Taminan<br>outers Stonin20don — taaewiatominis<br>rier Fousonma fomputer Caatn viene °<br>anungon ajo ms comencuinmuninan — : 0<br>Toneglengonion 2025-105 oroncti =: Aeon<br>© Pentroan<br>iwayat Approvalwaktu Fenyeesaion 12 Jom<br>a=xrID<br>‘Pengojuan<br>Cut oleh remonen<br>Clamp<br>‘isto<br>On sina Dewt<br>GD aD<br>‘amin epegawaionTeton Mengecet Surat<br>DraG=IDanmD suet Dsetyu Ketus Tim Kaj Kepegowaion<br>Dra sroaDetl Kab09 Umum<br>‘isankanEDPl. Kepoi ro PerencanaonKevd an gonUmum<br><!-- End of picture text -->

Gambar 2.55. Detail Cuti Telah Disahkan

Tampilan pada Gambar 2.55. menunjukkan bahwa pengajuan cuti telah selesai diproses sampai tahap akhir. Pada bagian _timelin_ e, terlihat tahapan terakhir berwarna hijau yang menandakan bahwa proses pengajuan telah selesai. Setiap tahapan dalam _timeline_ menampilkan informasi berupa tanggal masuk dengan _badge_ berwarna biru, yaitu kapan masing-masing pihak menerima pengajuan untuk diproses, dan tanggal eksekusi dengan _badge_ berwarna hijau, yaitu waktu ketika pihak terkait memberikan persetujuan atau menindaklanjuti pengajuan cuti.

<!-- Start of picture text -->
Form *<br>=e tantonne ——toasnacutTonmen<br>© reroon<br>iwoyat Wott Penyeinoin 12 om<br>‘Fergavon<br>I Approval<br>ov‘bsa e  ren)ttercn on Femonon<br>ao Pemeton<br><!-- End of picture text -->

Gambar 2.56. Form Detail Pengajuan Cuti Dibatalkan

Ketika pengguna membatalkan cuti, maka pada halaman formulir detail, khususnya pada bagian riwayat persetujuan, akan ditampilkan informasi bahwa proses telah dibatalkan oleh pemohon, disertai dengan waktu pembatalannya.

<!-- Start of picture text -->
) ‘pangohionFRCUPN veteran Cu  soonPegowol QD sqeesonteee<br>‘eogoiuon<br>Pertbonanet Ando membutntan<br>@ touan eo Sta eu<br>vashooars Uist pengolvon cut Br wee<br>Pengaturan [rove J == L<br>SSManajemenHeenonca Cut! show|[ 10 v | enue swore:(<br><!-- End of picture text -->

Gambar 2.57. Notifikasi Perubahan Pengajuan Cuti

Apabila pemberi persetujuan melakukan perubahan, maka pada kolom “Status” di tabel pengajuan cuti akan tercantum keterangan perubahan. Selain itu, pemohon

cuti juga akan menerima notifikasi untuk melakukan perubahan data cuti. Dalam keadaan tersebut, pemohon dapat memilih untuk membatalkan pengajuan cuti atau melakukan perubahan pada data cuti terlebih dahulu agar proses persetujuan dapat dilanjutkan.

<!-- Start of picture text -->
@ ‘Pengojvon Cut Pegowa D sansonene<br>@ Deenooas<br>reogoturon ==<br>Hines<br>MorojmenCut<br>°° ooD<br>ee cl cD<br><!-- End of picture text -->

Gambar 2.58. Form Detail Pengajuan Cuti Ditolak

Pada form detail cuti menampilkan _timeline_ berwarna merah yang menunjukkan bahwa pengajuan cuti ditolak. Pada bagian tersebut juga disertakan keterangan berupa alasan penolakan dan waktu penolakan pengajuan cuti.

<!-- Start of picture text -->
KEMENTERIAN PENDIDIKAN, KERUDAYAAN,<br>TISET, DAN TERNOLOGI<br>+ aan when Tah 2 pa Pon Port ri Pern<br>{See gt Caerry ep<br>2 omnesSooo meteontop eateungaeeot et cet agri gine ig,<br>SoS wre tn<br>Seager anton<br>=<br>1 fate Bra Pann Karn re<br>1Sedeaeroameranor<br><!-- End of picture text -->

Gambar 2.59. Surat Cuti

Saat tombol "Surat" pada menu cuti diklik, sistem akan menampilkan surat cuti yang telah disahkan oleh plt. kepala biro perencanaan, keuangan, dan umum.

<!-- Start of picture text -->
Om tina<br>@ Dashboard List PengajuanCuti<br>li Laporan cut<br><!-- End of picture text -->

Gambar 2.60. Halaman Cuti Pemberi Persetujuan

Tombol " _Approve_ " akan secara otomatis ditampilkan pada halaman list pengajuan cuti  apabila pengguna memiliki peran sebagai pihak yang perlu memberikan persetujuan atas cuti tersebut. Tombol ini dapat digunakan pengguna untuk menyetujui pengajuan cuti secara langsung. Selain itu, notifikasi juga akan dikirimkan kepada pengguna yang berwenang sebagai pemberi persetujuan, baik melalui sistem maupun email, untuk memberitahukan bahwa terdapat pengajuan cuti yang menunggu tindak lanjut.

<!-- Start of picture text -->
Form x<br>ome. aun srt Tetacui toninon<br>oragowoi +: T0001 sin tan i 2<br>soso ere Stomin20ulon So et2tanenis °<br>aie + Fo t n osKomputer tatCu tvar °<br>rsangantane sms Catetoncatittaniten 0<br>TnggoPengajion 2028-108 soson cus: Acraxevorga<br>TenggotAwat + 2025-08 omer ower<br>Tonggsimine + aozeso8 no telapon ommazeasesse<br>emanyocis 1 Lemon<br>© Perkiraan Watt Penyotscion: 2 Jam<br>‘iwayat Approval<br>=D<br>FPengojan<br>Cut leh Perohon<br>Menunggu Perstujuon<br>Rina Dow<br>Menunggu Oiproses Admin Kepepawaion<br>Menunggu DiprotesKetua<br>Tim Keva epogawaion<br>MenungguOiprves bag Umum<br>Pengetohan Surat Oleh Pit Karo Ferencanaan Keuangan, dan Umum<br>Approval<br>© setuju © tolak O. Perudahon<br>Ketorangan<br><!-- End of picture text -->

Gambar 2.61. Form _Approve_ Cuti

Setelah tombol " _Approve_ " ditekan, sistem akan menampilkan sebuah form konfirmasi yang dirancang untuk memfasilitasi proses persetujuan pengajuan cuti. Pada form ini, pengguna dapat melihat secara lengkap data pegawai yang mengajukan cuti beserta rincian cuti yang diajukan, seperti jenis cuti, tanggal mulai, tanggal selesai, dan informasi terkait lainnya. Selain itu, sistem juga menampilkan perkiraan waktu penyelesaian pengajuan cuti berdasarkan alur persetujuan yang berlaku di sistem. Di bagian bawah form, pengguna dapat melihat riwayat persetujuan, yang mencatat siapa saja yang telah memproses atau memberikan keputusan atas pengajuan tersebut, termasuk tanggal dan catatan persetujuan sebelumnya. Tersedia tiga opsi konfirmasi yang dapat dipilih oleh pemberi persetujuan, yaitu setuju, tolak, dan perubahan. Pilihan “Perubahan” hanya akan tampil khusus pengguna yang merupakan pemberi persetujuan di lingkungan fakultas ilmu komputer. Setelah memilih salah satu opsi konfirmasi, pengguna dapat mengisi keterangan. Selanjutnya, pengguna dapat menekan tombol “ _Save_ ” untuk menyimpan keputusan, atau tombol “ _Close_ ” untuk menutup form tanpa melakukan perubahan.

<!-- Start of picture text -->
© Dro den<br>@ astooars<br>Uist Pengaivancut<br>1 reonno sonsonne tron erate ovata) SS um<br><!-- End of picture text -->

Gambar 2.62. Tombol _Approve_ Setelah Perubahan

Setelah pemohon cuti melakukan perubahan data cuti sesuai dengan permintaan perubahan, sistem akan memunculkan kembali tombol “ _Approve_ ” bagi pihak yang sebelumnya memberikan konfirmasi perubahan sehingga proses persetujuan dapat dilanjutkan tanpa harus memulai dari awal. Dengan munculnya kembali tombol tersebut, pemberi persetujuan dapat segera meninjau ulang pengajuan yang telah diperbarui dan memberikan keputusan akhir, baik itu menyetujui, menolak, atau kembali meminta perubahan.

<!-- Start of picture text -->
LD. weorone<br>@ Cesndowd Lust PengojuenCutt<br>ti Laporan cut<br>7<br>1 rere Agntone tone onetans ceo 1 SS EG<br><!-- End of picture text -->

Gambar 2.63. Tombol Draf Surat

Tombol “Draf Surat” akan muncul secara otomatis setelah dekan menyetujui pengajuan cuti. Sistem akan secara otomatis menghasilkan draf surat cuti berdasarkan data yang telah diisi oleh pemohon dalam formulir pengajuan, termasuk jenis cuti, tanggal cuti, dan informasi pegawai terkait. Akses terhadap tombol “Draf Surat” dibatasi hanya untuk peran tertentu, yaitu admin kepegawaian, ketua tim kerja kepegawaian, kepala bagian umum, dan plt. kepala biro perencanaan, keuangan, dan umum. Saat tombol “Draf Surat” ditekan, sistem akan membuka halaman baru yang menampilkan _preview_ draf surat cuti dalam format PDF. Sementara itu, tombol “Surat” akan muncul setelah plt. kepala biro perencanaan, keuangan, dan umum menyetujui pengajuan cuti. Tombol ini dapat diakses tidak hanya oleh pengguna yang memiliki akses pada tombol “Draf Surat”, tetapi juga oleh pegawai yang mengajukan cuti dan dekan.

# **2.3.2.13. Halaman Laporan**

<!-- Start of picture text -->
@ engajuan Cut Fegowat QD rina bem<br>@ Dashboard Laporon Cuti<br>Monajemen Cuti Tangge! Awol Cut | | Tenagataki cust a<br>© cw Tongga! Awol Pengojvon | | TonggatAkh Pengoivon }<br>125000004 namo toorpred. slinomata cwiTohnon 1 oso 08-200 ED<br>2 re2$o20003 noma dovent sinormatta cwTahunon 1 cxotams o.oo SD<br>3 remson082 nomedton sliomame cw wana wos SD<br>4 F2so0001 nomowodee? siento cwTonnon 1 onze ens ED<br><!-- End of picture text -->

Gambar 2.64. Halaman Laporan

Halaman laporan cuti menampilkan riwayat pengajuan cuti pegawai yang telah selesai diproses. Pada bagian status, terdapat tiga kondisi status, yaitu disetujui, ditolak, dan dibatalkan. Halaman ini dilengkapi dengan fitur filter berdasarkan tanggal awal dan akhir cuti, tanggal pengajuan cuti, jenis cuti, dan status pengajuan. Selain itu, data laporan dapat diekspor ke dalam format Excel dan CSV.

# **2.3.2.14. Halaman** **_Logout_**

<!-- Start of picture text -->
=<br>ae eaeneel (Cut Menunggu Cuti Disetuja Ps hs<br>© nine ©o Bo 3G<br>S cw Performa Penyelesaian Cuti oleh Setiop Pihak Terkait di Tahun 2025<br>.<br>a<br><!-- End of picture text -->

Gambar 2.65. Halaman _Logout_

Pada bagian _header_ , terdapat nama pengguna atau _username_ yang ditampilkan. Jika nama tersebut diklik maka akan muncul tombol “ _Logout_ ”. Saat tombol “ _Logout_ ” ditekan, sistem akan langsung mengakhiri sesi pengguna dan mengarahkan kembali ke halaman _login_ .

# **2.4. Rencana Pengujian Proyek**

Pada tahap pengujian sistem, penulis menggunakan metode _blackbox testing_ untuk memastikan bahwa sistem informasi pengajuan cuti pegawai di Fakultas Ilmu Komputer UPN “Veteran” Jakarta berfungsi sesuai dengan yang diharapkan. Pengujian akan difokuskan pada setiap alur yang melibatkan interaksi antara pengguna dan sistem, mulai dari pengajuan cuti hingga persetujuan oleh pihak terkait. Rincian skenario pengujian yang akan dilakukan dapat dilihat pada Tabel 2.3.

Tabel 2.3. Rancangan Pengujian Sistem

|No.|Aktor|Skenario|Hasil yang Diharapkan|
|---|---|---|---|
|1.|Pemohon<br>Cuti|1) Membuka<br>dokumen peraturan|1) Sistem<br>menampilkan<br>dokumen peraturan cuti PNS<br>dengan tampilan PDF.|

|cuti<br>PNS<br>dari|2) Sistem<br>menampilkan|
|---|---|
|halaman_login._|dokumen peraturan cuti PPPK|
|2) Membuka|dengan tampilan PDF.|
|dokumen peraturan|3) Sistem menampilkan halaman|
|cuti<br>PPPK<br>dari|_dashboard._|
|halaman_login_.|4) Sistem<br>mengarahkan|
|3) Melakukan_login_.|pengguna ke halaman_login_.|
|4) Melakukan_logout_.|5) Sistem menampilkan halaman|
|5) Memilih menu hari|hari noncuti.|
|noncuti<br>dari<br>_sidebar_.|6) Sistem menampilkan halaman<br>cuti.|
|6) Memilih menu cuti|7) Sistem menampilkan data cuti|
|dari_sidebar_.|sesuai<br>dengan<br>status|
|7) Melakukan<br>filter<br>data cuti.|pengajuan yang dipilih.<br>8) Sistem menyimpan data cuti.|
|8) Membuat<br>pengajuan cuti.|9) Sistem menampilkan form<br>detail pengajuan cuti.|
|9) Melihat<br>detail<br>pengajuan cuti.|10) Sistem<br>memperbarui<br>data<br>cuti.|
|10) Melakukan|11) Sistem menyimpan alasan|
|perubahan data|pembatalan.|
|11) Melakukan|12) Pemohon<br>cuti<br>menerima|
|pembatalan cuti.|notifikasi perubahan data.|
|12) Menerima|13) Pemohon<br>cuti<br>menerima|
|permintaan|notifikasi penolakan.|
|perubahan data.|14) Pemohon<br>cuti<br>menerima|
|13) Menerima|notifikasi<br>pengajuan<br>cuti|
|notifikasi|disahkan.|
|pengajuan<br>cuti|15) Sistem menampilkan surat|
|ditolak.|cuti dalam format PDF.|
|14) Menerima<br>notifikasi||

|||pengajuan<br>cuti<br>disahkan.<br>15) Melihat surat cuti.||
|---|---|---|---|
|||1) Melakukan_login_.<br>2) Melakukan_logout_.|1) Sistem menampilkan halaman<br>_dashboard_.|
|||3) Memilih menu hari|2) Sistem<br>mengarahkan|
|||noncuti<br>dari|pengguna ke halaman_login_.|
|||_sidebar_.|3) Sistem menampilkan halaman|
|||4) Memilih menu cuti|hari noncuti.|
|||tahunan<br>dari<br>_sidebar_.|4) Sistem menampilkan halaman<br>cuti tahunan.|
|||5) Memilih<br>menu|5) Sistem menampilkan halaman|
|||laporan<br>dari|laporan.|
|||_sidebar_.|6) Sistem<br>menampilkan<br>data|
|||6) Melakukan<br>filter<br>data laporan.|laporan sesuai dengan kriteria<br>filter yang dipilih.|
||Wakil Dekan|7) Mengekspor|7) Sistem<br>mengunduh<br>file|
|2.|2|laporan<br>dalam|laporan dalam format Excel.|
|||format Excel.|8) Sistem<br>mengunduh<br>file|
|||8) Mengekspor|laporan dalam format CSV.|
|||laporan<br>dalam|9) Sistem menampilkan halaman|
|||format CSV.|cuti.|
|||9) Memilih menu cuti|10) Sistem<br>menampilkan<br>data|
|||dari_sidebar._|pengajuan cuti sesuai dengan|
|||10) Melakukan<br>filter|kriteria filter yang dipilih.|
|||data pengajuan cuti.|11) Wakil Dekan 2 menerima|
|||11) Menerima|notifikasi<br>“Terdapat|
|||notifikasi pada web|pengajuan cuti” pada web dan|
|||dan email ketika|email.|
|||terdapat pengajuan<br>cuti yang masuk.|12) Wakil<br>Dekan<br>2<br>dapat<br>melakukan persetujuan cuti.|

|||12) Melakukan<br>persetujuan|13) Wakil<br>Dekan<br>2<br>dapat<br>melakukan penolakan cuti.|
|---|---|---|---|
|||pengajuan cuti.<br>13) Melakukan<br>penolakan<br>pengajuan cuti.<br>14) Melakukan|14) Wakil<br>Dekan<br>2<br>dapat<br>melakukan perubahan cuti.<br>15) Wakil Dekan 2 menerima<br>notifikasi setelah pemohon<br>merevisi pengajuan cuti.|
|||perubahan<br>pengajuan cuti.<br>15) Menerima<br>notifikasi<br>setelah<br>pemohon merevisi<br>pengajuan cuti.<br>16) Melakukan<br>persetujuan ulang.|16) Wakil<br>Dekan<br>2<br>dapat<br>melakukan persetujuan ulang.|
|||1) Melakukan_login_.<br>2) Melakukan_logout_.|1) Sistem menampilkan halaman<br>_dashboard_.|
|||3) Memilih menu hari|2) Sistem<br>mengarahkan|
|||noncuti<br>dari<br>_sidebar_.|pengguna ke halaman_login_.<br>3) Sistem menampilkan halaman|
|||4) Menambahkan hari|hari noncuti.|
|||noncuti.|4) Koordinator tata usaha FIK|
||Koordinator|5) Mengubah<br>hari|dapat<br>menambahkan<br>hari|
|3.|Tata Usaha|noncuti.|noncuti.|
||FIK|6) Menghapus<br>hari<br>noncuti.|5) Koordinator tata usaha FIK<br>dapat mengubah hari noncuti.|
|||7) Memilih<br>menu|6) Koordinator tata usaha FIK|
|||_users_dari_sidebar_.|dapat<br>menghapus<br>hari|
|||8) Menambahkan data|noncuti.|
|||_users_.|7) Sistem menampilkan halaman|
|||9) Mengubah<br>data<br>_users_.|users.|

|10) Menghapus|data|8) Koordinator tata usaha|FIK|
|---|---|---|---|
|_users_.||dapat<br>menambahkan|data|
|11) Melakukan<br>|filter|users.||
|data_user_.||9) Koordinator tata usaha|FIK|
|12) Memilih menu|_role_|dapat mengubah data use|rs.|
|dari_sidebar_.||10) Koordinator tata usaha|FIK|
|13) Menambahkan|data|dapat menghapus data us|ers.|
|_role_.||11) Sistem<br>menampilkan|data|
|14) Mengubah<br>_role_.|data|berdasarkan filter data us<br>12) Sistem menampilkan hala|er.<br>man|
|15) Menghapus|data|role.||
|_role_.||13) Koordinator tata usaha|FIK|
|16) Memilih menu|sub|dapat<br>menambahkan|data|
|unit dari_sideba_|_r_.|role.||
|17) Menambahkan<br>sub unit.|data|14) Koordinator tata usaha<br>dapat mengubah data rol|FIK<br>e.|
|18) Mengubah data|sub|15) Koordinator tata usaha|FIK|
|unit.||dapat menghapus data ro|le.|
|19) Menghapus<br>sub unit.|data|16) Sistem menampilkan hala<br>sub unit.|man|
|20) Memilih menu|cuti|17) Koordinator tata usaha|FIK|
|tahunan|dari|dapat menambahkan data|sub|
|_sidebar_.||unit.||
|21) Menambahkan|cuti|18) Koordinator tata usaha|FIK|
|tahunan<br>peg|awai|dapat mengubah data sub|unit.|
|secara massal.||19) Koordinator tata usaha|FIK|
|22) Menambahkan|data|dapat menghapus data|sub|
|cuti tahunan se|cara|unit.||
|individual.||20) Sistem menampilkan hala|man|
|23) Mengubah data|cuti|cuti tahunan.||
|tahunan.||21) Sistem menyimpan data<br>tahunan<br>untuk<br>sel|cuti<br>uruh|

|24) Menghapus<br>data|pegawai berdasarkan t|ahun|
|---|---|---|
|cuti tahunan.|dan jumlah yang diinput.||
|25) Memilih<br>menu|22) Koordinator tata usaha|FIK|
|konfigurasi cuti dari|dapat menambahkan data|cuti|
|_sidebar_.|tahunan secara individua|l.|
|26) Mengubah<br>data|23) Koordinator tata usaha|FIK|
|konfigurasi cuti.|dapat mengubah data|cuti|
|27) Memilih<br>menu|tahunan.||
|batasan cuti dari|24) Koordinator tata usaha|FIK|
|_sidebar_.|dapat menghapus data|cuti|
|28) Menambahkan data|tahunan.||
|batasan cuti.|25) Sistem menampilkan hal|aman|
|29) Mengubah<br>data|konfigurasi cuti.||
|batasan cuti .|26) Koordinator tata usaha|FIK|
|30) Menghapus<br>data|dapat<br>mengubah|data|
|batasan cuti.|konfigurasi cuti.||
|31) Memilih<br>menu|27) Sistem menampilkan hal|aman|
|laporan<br>dari|batasan cuti.||
|_sidebar_.|28) Koordinator tata usaha|FIK|
|32) Melakukan<br>filter|dapat<br>menambahkan|data|
|data laporan.|batasan cuti.||
|33) Mengekspor|29) Koordinator tata usaha|FIK|
|laporan<br>dalam|dapat mengubah data ba|tasan|
|format Excel.|cuti.||
|34) Mengekspor|30) Koordinator tata usaha|FIK|
|laporan<br>dalam|dapat menghapus data ba|tasan|
|format CSV.|cuti.||
|35) Memilih menu cuti|31) Sistem menampilkan hal|aman|
|dari_sidebar_.|laporan.||
|36) Melakukan<br>filter|32) Sistem<br>menampilkan|data|
|data pengajuan cuti.|laporan sesuai dengan kr<br>filter yang dipilih.|iteria|

|||37) Melihat<br>detail<br>pengajuan cuti.<br>38) Melihat surat cuti.|33) Sistem<br>laporan<br>34) Sistem<br>laporan<br>35) Sistem<br>cuti.<br>36) Sistem<br>pengaju<br>kriteria<br>37) Sistem<br>detail pe<br>38) Sistem<br>cuti dala|mengunduh<br>dalam format E<br>mengunduh<br>dalam format C<br>menampilkan ha<br>menampilkan<br>an cuti sesuai d<br>filter yang dipil<br>menampilkan<br>ngajuan cuti<br>menampilkan<br>m format PDF.|file<br>xcel.<br>file<br>SV.<br>laman<br> <br>data<br>engan<br>ih.<br>form<br>surat<br>|
|---|---|---|---|---|---|
|||1) Melakukan_login_.<br>2) Melakukan_logout_.<br>3) Memilih menu hari<br>noncuti<br>dari<br>_sidebar_.<br>4) Menambahkan hari<br>noncuti.<br>5) Mengubah<br>hari<br>noncuti.|1) Sistem<br>_dashboa_<br>2) Sistem<br>penggun<br>3) Sistem<br>hari non<br>4) Admin<br>menamb<br>5) Admin|menampilkan ha<br>_rd_.<br>menga<br>a ke halaman_l_<br>menampilkan ha<br>cuti.<br>kepegawaian<br>ahkan hari non<br>kepegawaian|laman<br>rahkan<br>_ogin_.<br>laman<br>dapat<br>cuti.<br>dapat|
|4.|Admin<br>Kepegawaian|6) Menghapus<br>hari<br>noncuti.<br>7) Memilih<br>menu<br>_users_dari_sidebar_.<br>8) Menambahkan data<br>_users_.<br>9) Mengubah<br>data<br>_users_.<br>10) Menghapus<br>data<br>_users_.|mengub<br>6) Admin<br>mengha<br>7) Sistem<br>_users_.<br>8) Admin<br>menamb<br>9) Admin<br>mengub|ah hari noncuti.<br>kepegawaian<br>pus hari noncut<br>menampilkan ha<br>kepegawaian<br>ahkan data_use_<br>kepegawaian<br>ah data_users_.|<br>dapat<br>i.<br>laman<br>dapat<br>_rs_.<br>dapat|

|11) Melakukan<br>f<br>data_user_.|ilter|10) Admin<br>mengha|kepegawaian<br>pus data_users._|dapat|
|---|---|---|---|---|
|12) Memilih menu<br>dari_sidebar_.|_role_|11) Sistem<br>berdasar|menampilkan<br>kan filter data_u_|<br>data<br>_ser_.|
|13) Menambahkan<br>_role_.|data|12) Sistem<br>_role_.|menampilkan ha|laman|
|14) Mengubah<br>_role_.|data|13) Admin<br>menamb|kepegawaian<br>ahkan data_role_|dapat<br>.|
|15) Menghapus<br>_role_.|data|14) Admin<br>mengub|kepegawaian<br>ah data_role_.|dapat|
|16) Memilih menu<br>unit dari_sideba_|sub<br>_r_.|15) Admin<br>mengha|kepegawaian<br>pus data_role._|dapat|
|17) Menambahkan<br>sub unit.|data|16) Sistem<br>sub unit|menampilkan ha<br>.|laman|
|18) Mengubah data<br>unit.|sub|17) Admin<br>menamb|kepegawaian<br>ahkan data sub|dapat<br>unit.|
|19) Menghapus<br>sub unit.|data|18) Admin<br>mengub|kepegawaian<br>ah data sub unit|dapat<br>.|
|20) Memilih menu|cuti|19) Admin|kepegawaian|dapat|
|tahunan|dari|mengha|pus data sub un|it_._|
|_sidebar_.||20) Sistem|menampilkan ha|laman|
|21) Menambahkan|data|cuti tahu|nan.||
|cuti tahunan.||21) Admin|kepegawaian|dapat|
|22) Mengubah data<br>tahunan.|cuti|menamb<br>tahunan|ahkan<br>data<br>.|cuti|
|23) Menghapus<br>cuti tahunan.|data|22) Admin<br>mengub|kepegawaian<br>ah data cuti tah|dapat<br>unan.|
|24) Memilih<br>m|enu|23) Admin|kepegawaian|dapat|
|konfigurasi cuti<br>_sidebar_.|dari|mengha<br>24) Sistem|pus data cuti tah<br>menampilkan ha|unan_._<br>laman|
|25) Mengubah<br>konfigurasi cuti|data<br>.|konfigu|rasi cuti.||

|26) Memilih<br>menu|25) Admin|kepegawaian dapat|
|---|---|---|
|batasan cuti dari|mengub|ah data konfigurasi|
|_sidebar_.|cuti.||
|27) Menambahkan data|26) Sistem|menampilkan halaman|
|batasan cuti.|batasan|cuti.|
|28) Mengubah<br>data|27) Admin|kepegawaian dapat|
|batasan cuti .|menamb|ahkan data batasan|
|29) Menghapus<br>data|cuti.||
|batasan cuti.|28) Admin|kepegawaian dapat|
|30) Memilih<br>menu|mengub|ah data batasan cuti.|
|laporan<br>dari|29) Admin|kepegawaian dapat|
|_sidebar_.|mengha|pus data batasan cuti_._|
|31) Melakukan<br>filter<br>data laporan.|30) Sistem<br>laporan.|menampilkan halaman<br>|
|32) Mengekspor|31) Sistem|menampilkan<br>data|
|laporan<br>dalam|laporan|sesuai dengan kriteria|
|format Excel.|filter ya|ng dipilih.|
|33) Mengekspor|32) Sistem|mengunduh<br>file|
|laporan<br>dalam|laporan|dalam format Excel.|
|format CSV.|33) Sistem|mengunduh<br>file|
|34) Memilih menu cuti|laporan|dalam format CSV.|
|dari_sidebar_.|34) Sistem|menampilkan halaman|
|35) Melakukan<br>filter|cuti.||
|data pengajuan cuti.|35) Sistem|menampilkan<br>data|
|36) Menerima notifikasi|pengaju|an cuti sesuai dengan|
|pada web dan email|kriteria|filter yang dipilih.|
|ketika<br>terdapat|36) Admin|kepegawaian|
|pengajuan cuti yang|menerim|a notifikasi saat ada|
|masuk.|pengaju|an cuti.|
|37) Melihat draf surat<br>cuti.|37) Sistem<br>surat cu|menampilkan<br>draf<br>ti dalam format PDF.|

|||38) Melakukan<br>persetujuan<br>38|) Admin kepegawaia<br>melakukan<br>pe|n dapat<br>rsetujuan|
|---|---|---|---|---|
|||pengajuan cuti.<br>39) Melakukan<br>penolakan<br>pengajuan cuti.<br>40) Melihat surat cuti.<br>39<br>40|pengajuan cuti.<br>) Admin kepegawaia<br>melakukan<br>p<br>pengajuan cuti.<br>) Sistem menampilk<br>cuti dalam format PD|n dapat<br>enolakan<br>an surat<br>F.|
|||1) Melakukan_login_.<br>2) Melakukan_logout_.|1) Sistem<br>men<br>halaman_dashboa_|ampilkan<br>_rd_.|
|||3) Memilih menu hari<br>noncuti dari_sidebar_.<br>4) Memilih menu cuti<br>tahunan dari_sidebar_.<br>5) Memilih menu batasan<br>cuti dari_sidebar_.<br>6) Menambahkan batasan<br>cuti.|2) Sistem<br>men<br>pengguna<br>ke<br>_login_.<br>3) Sistem<br>men<br>halaman hari nonc<br>4) Sistem<br>men<br>halaman cuti tahu<br>5) Sistem<br>men|garahkan<br>halaman<br>ampilkan<br>uti.<br>ampilkan<br>nan.<br>ampilkan|
||Ketua Tim|7) Mengubah<br>data|halaman batasan c|uti.|
|5.|<br>Kerja|batasan cuti.|6) Ketua<br>tim|kerja|
||Kepegawaian|8) Menghapus<br>data<br>batasan cuti.|kepegawaian<br>menambahkan|dapat<br>batasan|
|||9) Memilih menu tanda|cuti.||
|||tangan dari_sidebar_.|7) Ketua<br>tim|kerja|
|||10) Membuat paraf.|kepegawaian|dapat|
|||11) Menghapus<br>coretan<br>paraf.|mengubah data<br>cuti.|batasan|
|||12) Menghapus paraf yang<br>telah tersimpan.|8) Ketua<br>tim<br>kepegawaian|kerja<br>dapat|
|||13) Memilih menu laporan<br>dari_sidebar_.|menghapus data<br>cuti.|batasan|

|14) Melakukan filter data|9) Sistem<br>mena|mpilkan|
|---|---|---|
|laporan.|halaman tanda tan|gan.|
|15) Mengekspor<br>laporan|10) Ketua<br>tim|kerja|
|dalam format Excel.|kepegawaian|dapat|
|16) Mengekspor<br>laporan|membuat paraf.||
|dalam format CSV.|11) Ketua<br>tim|kerja|
|17) Memilih menu cuti|kepegawaian|dapat|
|dari_sidebar_.|menghapus coreta|n paraf.|
|18) Melakukan filter data|12) Ketua<br>tim|kerja|
|pengajuan cuti.|kepegawaian|dapat|
|19) Menerima<br>notifikasi|menghapus<br>para|f<br>yang|
|saat<br>admin|telah tersimpan.||
|kepegawaian<br>telah|13) Sistem<br>mena|mpilkan|
|menyetujui pengajuan<br>cuti.|halaman laporan.<br>14) Sistem menampil|kan data|
|20) Melihat draf surat cuti.|laporan<br>sesuai|dengan|
|21) Melakukan|filter.||
|persetujuan pengajuan|15) Sistem mengund|uh file|
|cuti.|laporan<br>dalam|format|
|22) Melakukan penolakan<br>pengajuan cuti.|Excel.<br>16) Sistem mengund|uh file|
|23) Melihat surat cuti.|laporan<br>dalam|format|
||CSV.<br>17) Sistem<br>mena<br>halaman cuti.<br>18) Sistem menampil<br>pengajuan<br>cuti|mpilkan<br>kan data<br>sesuai|
||dengan kriteria fil<br>dipilih.|ter yang|
||19) Ketua<br>tim|kerja|
||kepegawaian<br>m|enerima|
||notifikasi<br>saat|admin|

|kepegawaian<br>telah|
|---|
|menyetujui.|
|20) Sistem menampilkan draf|
|surat dalam format PDF.|
|21) Ketua<br>tim<br>kerja|
|kepegawaian<br>dapat|
|melakukan<br>persetujuan|
|pengajuan cuti.|
|22) Ketua<br>tim<br>kerja|
|kepegawaian<br>dapat|
|melakukan<br>penolakan|
|pengajuan cuti.|
|23) Sistem menampilkan surat|
|cuti dalam format PDF.|


# PROYEK PEMBANGUNAN SISTEM INFORMASI KEGIATAN KEMAHASISWAAN BERBASIS WEBSITE DENGAN FRAMEWORK LARAVEL (STUDI KASUS FAKULTAS ILMU KOMPUTER UNIVERSITAS PEMBANGUNAN NASIONAL”VETERAN” JAKARTA)

# **BAB II**

# **RANCANGAN PRODUK**

Berdasarkan latar belakang yang sudah dijelaskan sebelumnya, bab ini akan menguraikan rancangan produk berupa deskripsi aktor, kerangka pikir, dan _low-fidelity_ untuk memudahkan proses pembuatan proyek sistem informasi kegiatan kemahasiswaan berbasis _website_ terkait penelitian ataupun pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta agar pembuatan proyek ini dapat lebih terarah dan terstruktur.

# **2.1 Deskripsi Aktor**

Setiap aktor memiliki hak akses dalam sistem untuk memastikan penyebaran informasi dan proses pendaftaran mahasiswa dalam penelitian ataupun pengabdian masyarakat di Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta dapat berjalan dengan efektif dan efisien. Identifikasi peran setiap aktor ini sangat penting untuk memastikan bahwa setiap pengguna sistem dapat melakukan tugasnya sesuai dengan wewenangnya. Tabel berikut memuat batasan akses yang dapat dilakukan oleh setiap aktor dalam sistem ini untuk mengelola penelitian ataupun pengabdian masyarakat di Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta.

Tabel 2.1. Tabel Deskripsi Aktor

|**Aktor**|**Deskripsi**|
|---|---|
|Mahasiswa|1. Dapat melihat informasi penelitian ataupun|
||pengabdian masyarakat.|
||2. Dapat memilih penelitian ataupun|
||pengabdian masyarakat.|
||3. Dapat melakukan pendaftaran penelitian|
||ataupun pengabdian masyarakat.|
||4. Dapat melihat pengumuman hasil seleksi|
||mahasiswa untuk penelitian ataupun|
||pengabdian masyarakat.|

|5.|Dapat mengunduh surat tugas penelitian<br>ataupun pengabdian masyarakat.|
|---|---|
|Dosen<br>1.<br>2.<br>3.<br>4.<br>5.<br>6.|Dapat memasukkan informasi penelitian<br>ataupun pengabdian masyarakat.<br>Dapat melihat informasi penelitian ataupun<br>pengabdian masyarakat.<br>Dapat melakukan seleksi mahasiswa untuk<br>penelitian ataupun pengabdian masyarakat.<br>Dapat mengisi form pengumuman hasil<br>seleksi mahasiswa untuk penelitian ataupun<br>pengabdian masyarakat.<br>Dapat melakukan_edit_terhadap informasi<br>penelitian ataupun pengabdian masyarakat.<br>Dapat melihat pengumuman hasil seleksi<br>mahasiswa untuk penelitian ataupun<br>pengabdian masyarakat.|
|Koordinator<br>Program Studi<br>1.<br>2.|Dapat melihat informasi penelitian ataupun<br>pengabdian masyarakat.<br>Dapat mengecek dosen dan mahasiswa yang<br>mengikuti penelitian ataupun pengabdian<br>masyarakat melalui surat tugas.|
|Wakil Dekan 1<br>1.<br>2.|Dapat melihat informasi pengabdian<br>masyarakat penelitian ataupun pengabdian<br>masyarakat.<br>Dapat mengecek dosen dan mahasiswa yang<br>mengikuti penelitian ataupun pengabdian<br>masyarakat melalui surat tugas.|
|Staf Tata Usaha<br>1.|Dapat melihat informasi penelitian ataupun|

pengabdian masyarakat.

2. Dapat melihat pengumuman hasil seleksi penelitian ataupun pengabdian masyarakat.

3. Dapat membuat surat tugas penelitian ataupun pengabdian masyarakat.

4. Dapat melakukan _edit_ terhadap informasi penelitian ataupun pengabdian masyarakat.

Tabel 1. Deskripsi Aktor

# **2.2 Kerangka Pikir**

Berdasarkan tabel deskripsi aktor yang sudah dijelaskan sebelumnya, penulis membuat sebuah kerangka pikir agar lebih tergambar berbagai aktor dan aktivitas yang dilakukan dalam sistem informasi kegiatan kemahasiswaan berbasis _website_ terkait penelitian ataupun pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta ini. Dengan kerangka pikir ini, pembuatan proyek sistem informasi kegiatan kemahasiswaan berbasis _website_ terkait penelitian ataupun pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta dapat lebih terarah dan terstruktur.

<!-- Start of picture text -->
Informe Peneiton ataupun<br>Pengeian Masrrakat,<br>verges peretan<br>atapunpegetden manera a<br>—,—<———==i Database<br>[--———————— Kepataninom<br>g ‘Memasukcan informasi peneitian| xemanensraan<br>toon pengatdan mara<br>endaiarn Pveiian saupan<br>engaban Mesyarkat<br>erin pera augur<br>—<br>2 elhakn pendataran<br>ontabase<br>Percetarn<br>epaan<br>Mens fom pendtaran<br>eng okaen ya<br>ebeinan<br>Pope enka Sie<br>‘naBein MleRegt ge ean Frm<br>{eel a Kv a a<br>cepa Cates Penge<br>Naseer) Seles dan Pengumuman<br>Penitian tapun Penosbdan Masyarakat<br>Waban coat peretan<br>Lescun Donon macarnl a<br>Database<br>Tings fom pengouran set est Seats<br>seen stapuerasndan asyraat epatan<br>emanessraan<br>iol en aa<br>Peeltan ataupunSuratPengabaian Tones Masyarakat<br>fe)<br>soar<br>Progam St<br>fe)<br>Surat<br>senetn atavun pengabsan masa<br>fe)<br><!-- End of picture text -->

Gambar 2.1 Kerangka Pikir

Sistem informasi kegiatan kemahasiswaan berbasis _website_ terkait penelitian ataupun pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta ini dapat memudahkan user dalam menemukan informasi dan membantu user dalam  proses pendaftaran terkait kegiatan penelitian ataupun pengabdian masyarakat di lingkungan Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Seperti pada

gambar di atas, di dalam sistem ini terdapat beberapa aktor yang terdiri dari mahasiswa, dosen, Koordinator Program Studi, Wakil Dekan 1, dan Staf Tata Usaha (admin).

Dalam sistem ini, Dosen Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat menginputkan informasi penelitian ataupun pengabdian masyarakat. Data yang telah dimasukkan oleh dosen akan tersimpan ke dalam database informasi kegiatan kemahasiswaan. Dosen juga dapat melakukan _edit_ terhadap informasi penelitian ataupun pengabdian masyarakat.

Selanjutnya, mahasiswa Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat melihat berbagai informasi penelitian ataupun pengabdian masyarakat yang datanya diambil dari database informasi kegiatan kemahasiswaan. Mahasiswa juga dapat memilih penelitian ataupun pengabdian masyarakat mana yang akan mereka ikuti. Jika sudah, mereka dapat melakukan pendaftaran dengan mengisi form pendaftaran penelitian ataupun pengabdian masyarakat serta mencantumkan dokumen yang dibutuhkan dan datanya akan tersimpan ke dalam database pendaftaran kegiatan kemahasiswaan. Pada saat selesai proses seleksi mahasiswa yang telah dilakukan oleh dosen, mahasiswa dapat melihat pengumuman hasil seleksi penelitian ataupun pengabdian masyarakat yang data hasil seleksinya di ambil dari database hasil seleksi kegiatan kemahasiswaan. Jika dalam hasil tersebut mahasiswa ditolak, maka mahasiswa dapat melakukan pendaftaran penelitian ataupun pengabdian masyarakat yang lain, sedangkan jika mahasiswa diterima untuk penelitian ataupun pengabdian masyarakat maka akan dibuatkan surat tugas penelitian ataupun pengabdian masyarakat oleh Staf Tata Usaha Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta.

Ketika para dosen dan mahasiswa sudah terbentuk tim di masing-masing penelitian ataupun pengabdian masyarakatnya, mereka akan dibuatkan surat tugas oleh Staf Tata Usaha Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta. Data untuk surat tugas pengabdian masyarakat ini dapat diambil dari database hasil seleksi kegiatan kemahasiswaan. Selain itu, Staf Tata

Usaha juga dapat melakukan _edit_ terhadap informasi penelitian ataupun pengabdian masyarakat. Di dalam sistem ini juga, Koordinator Program Studi dan Wakil Dekan 1 Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat melihat berbagai informasi penelitian ataupun pengabdian masyarakat yang akan diadakan serta mengecek anggota tim yang ikut melalui surat tugas penelitian ataupun pengabdian masyarakat.

# **2.3** **_Low-Fidelity_**

Berdasarkan kerangka pikir yang sudah dibuatkan sebelumnya, penulis membuatkan _low-fidelity_ untuk proyek sistem informasi kegiatan kemahasiswaan berbasis _website_ terkait penelitian ataupun pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional “Veteran” Jakarta. Pembuatan _low-fidelity_ ini berfungsi sebagai representasi awal dari antarmuka pengguna dan alur interaksi dalam sistem, sehingga membantu dalam visualisasi konsep lebih lanjut sebelum tahap pengembangan yang lebih mendetail.

<!-- Start of picture text -->
Masuk<br><!-- End of picture text -->

Gambar 2.2. Tampilan Login

Pada tampilan login, user dapat memasukkan _nama pengguna_ (username)

dan kata sandi serta bisa klik _button_ masuk.

<!-- Start of picture text -->
Form Input Informasi<br>Topik Kegiatan<br>Jeniskegiatan >Peneitian © Pengabaian Masyarakat<br>Total Mahasiswa<br>yang Dibutuhkan<br>Nama Anggota Tim @®<br>Deskrips singket kegiatan<br>=_<br><!-- End of picture text -->

Gambar 2.3 Tampilan Form Input Informasi

Pada tampilan form input informasi, Dosen Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat memasukkan topik kegiatan, lalu memilih jenis kegiatan, mengisi lokasi kegiatan, total mahasiswa yang dibutuhkan, nama anggota tim (dosen), dan deskripsi singkat terkait kegiatan yang akan dilakukan. Dosen juga dapat melakukan edit, simpan dan batal pada form input informasi kegiatan. Di lain sisi, Staf Tata Usaha Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta juga dapat melakukan edit terhadap informasi kegiatan.

<!-- Start of picture text -->
Informasi Penelitian dan Pengabdian<br>Masyarakat<br>Topik Kegiatan<br>Jenis Kegiatan<br>LokasiKegiatan<br>Total Mahasiswa_<br>Nama Dosen<br>Nama Dosen<br>Nama Dosen<br>Deskripsi Singkat Kegiatan. Lorem ipsum dolor sit amet consectetur. Est<br>vitae pulvinar sed nisl id amet. Fermentum tincidunt eu placerat aliquet.<br>Ametodio elementum dui enim placeratmattis sed nunc. enim neque in nisi consequat. Convallis ornare<br>Topik Kegiatan<br>Jenis Kegiatan<br>LokasiKegiatan<br>Total Mahasiswa<br>NamaDosen<br>Nama Dosen<br>Nama Dosen<br>DeskripsiVitae Singkat Kegiatan, Loremipsumdolor sitamet consectetur. Est<br>‘Ametodio  duipulvinarelementumenim sed placeratmattisnisiid sedenimneque nunc.amet. Fermentuminnisiconsequat. tincidunt euplacerataliquet.Convalis ornare<br>Topik Kegiatan<br>Jenis Kegiatan<br>LokasiKegiatan<br>Total Mahasiswa<br>Nama Dosen<br>Nama Dosen<br>Nama Dosen<br>Deskrips! Singkat Kegiatan. Lorem ipsum dolor sitamet consectetur Est<br>vitae pulvinar sed nisl id amet. Fermentum tincidunt eu placerat aliquet.<br>Ametodio elementum dui enim placeratmattis sed nunc. enim neque in nisi consequat. Convallis ornare<br><!-- End of picture text -->

Gambar 2.4. Tampilan Informasi Penelitian dan Pengabdian Masyarakat

Pada tampilan informasi penelitian dan pengabdian masyarakat, terdapat berbagai kegiatan penelitian ataupun pengabdian masyarakat yang akan diadakan, dari masing-masing kegiatan terdapat informasi topik kegiatan, jenis kegiatan, lokasi kegiatan, total mahasiswa yang dibutuhkan, nama anggota tim (dosen), dan

deskripsi singkat terkait kegiatan yang akan dilakukan. Dalam setiap _card_ kegiatan terdapat _button_ untuk melakukan pendaftaran, melihat pengumuman, dan melihat surat tugas.

<!-- Start of picture text -->
Form Pendaftaran<br>°<br><!-- End of picture text -->

Gambar 2.5 Tampilan Form Pendaftaran

Pada tampilan form pendaftaran, mahasiswa Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat mengisi data yang dibutuhkan seperti nama lengkap, Nomor Induk Mahasiswa (NIM), email, nomor telepon/WA, program studi, angkatan, serta mencantumkan beberapa dokumen seperti Kartu Hasil Studi (KHS), CV, portofolio, dan foto 3x4. Lalu, mahasiswa bisa klik _button_ kirim, jika tidak jadi mendaftar mahasiswa bisa klik _button_ batal.

<!-- Start of picture text -->
Form Pendaftaran<br><!-- End of picture text -->

Gambar 2.6. Tampilan Form Pendaftaran (Dosen)

Pada tampilan form pendaftaran dari sisi dosen, Dosen Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat melihat data yang telah diisi oleh mahasiswa seperti nama lengkap, Nomor Induk Mahasiswa (NIM), email, nomor telepon/WA, program studi, angkatan, serta beberapa dokumen yang telah dicantumkan seperti Kartu Hasil Studi (KHS), CV, portofolio, dan foto 3x4. Jika sudah, dosen dapat menutup tampilannya dengan klik _button_ tutup.

<!-- Start of picture text -->
Form Pengumuman Kegiatan<br>Selamat, Anda tepith untuk mengikuti pengabdian masyarakat ini!<br> {<br>NamaMehasiswa ®<br>@<br><!-- End of picture text -->

Gambar 2.7. Tampilan Form Pengumuman Kegiatan

Pada tampilan form pengumuman kegiatan, Dosen Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat memasukkan nama-nama mahasiswa yang terpilih untuk mengikuti kegiatannya, lalu bisa klik _button_ kirim. Dosen juga dapat mengganti nama-nama mahasiswa yang sudah dicantumkan dengan klik _button edit_ .

<!-- Start of picture text -->
Pengumuman Kegiatan<br>Selamat, Anda terplih untuk mengikut kegiataninit<br>1. NamaMahasiswa<br>2. NamaMahasiswa<br>5. NamaMahasiswa<br><!-- End of picture text -->

Gambar 2.8. Tampilan Pengumuman Kegiatan

Pada tampilan pengumuman kegiatan, terdapat nama-nama mahasiswa yang terpilih untuk mengikuti penelitian ataupun pengabdian masyarakat.

<!-- Start of picture text -->
Surat Tugas<br>SuratTugas PilinFile<br><!-- End of picture text -->

Gambar 2.9. Tampilan Surat Tugas

Pada tampilan surat tugas dari sisi Staf Tata Usaha, Staf Tata Usaha dapat memasukkan file surat tugas penelitian ataupun pengabdian masyarakat.

<!-- Start of picture text -->
Surat Tugas<br><!-- End of picture text -->

Gambar 2.10. Tampilan Surat Tugas

Pada tampilan surat tugas di atas, mahasiswa, dosen, Koordinator Program

Studi, dan Wakil Dekan 1 Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta dapat melihat file surat tugas penelitian ataupun pengabdian masyarakat dengan mengunduh filenya.

# **2.4 Teknologi Proyek**

Dalam pembuatan proyek sistem informasi berbasis website terkait pengabdian masyarakat Fakultas Ilmu Komputer Universitas Pembangunan Nasional "Veteran" Jakarta, penulis mencantumkan kebutuhan perangkat keras dan perangkat lunak yang akan mendukung pembuatan proyek ini, termasuk perangkat keras untuk pengembangan serta perangkat lunak utama dan pendukung yang diperlukan untuk membangun dan merancang proyek ini.

# **2.4.1 Kebutuhan** **_Hardware_**

Perangkat keras (hardware) yang digunakan kami dalam proyek ini adalah Laptop Lenovo Ideapad Slim 5 Pro dengan spesifikasi laptop sebagai berikut:

- 1) Processor : AMD Ryzen 7 5800U

- 2) RAM       : 16 GB

- 3) Storage    : 512 GB

# **2.4.2 Kebutuhan** **_Software_**

Perangkat lunak (software) yang digunakan kami dalam proyek ini adalah sebagai

berikut:

- 1) Sistem Operasi : Microsoft Windows 11 Home Single Language

- 2) Bahasa Pemrograman : PHP

- 3) Framework : Laravel, Tailwind CSS, dan ReactJS 4) Basis Data : MySQL

- 5) Code Editor : Visual Studio Code

- **2.4.3 Kebutuhan** **_Software_ Pendukung**

Sarana pendukung  yang digunakan kami dalam proyek ini adalah sebagai berikut:

- 1) Draw.io    :  Pembuatan arsitektur jaringan aplikasi dan desain basis data.

- 2) Figma   : Pembuatan arsitektur informasi, diagram alur aplikasi, dan desain antarmuka pengguna.

# **2.5       Rencana Pengujian Proyek**

Pengujian pada proyek Pembangunan Sistem Informasi Kegiatan Kemahasiswaan Berbasis Website dengan Framework Laravel akan menggunakan metode Black Box

Testing. Metode ini dipilih karena fokusnya pada pengujian fungsionalitas sistem tanpa memeriksa kode sumber atau struktur internal aplikasi. Tujuan utama pengujian ini adalah untuk memastikan bahwa sistem dapat berfungsi sesuai dengan spesifikasi yang telah ditentukan.

# **2.5.1 Metodologi Pengujian**

Metode Black Box Testing akan dilakukan dengan langkah-langkah berikut:

1. Identifikasi Fitur: Mengidentifikasi fitur atau fungsi utama yang akan diuji, seperti pendaftaran kegiatan, pengelolaan data kegiatan, dan pelaporan hasil.

2. Pembuatan Skenario Uji: Membuat skenario pengujian berdasarkan kebutuhan pengguna dan spesifikasi sistem.

3. Pengujian Data Masukan dan Keluaran: Menguji sistem menggunakan berbagai kombinasi data masukan untuk memastikan bahwa keluaran yang dihasilkan sesuai dengan yang diharapkan.

4. Dokumentasi Hasil: Mencatat hasil pengujian, termasuk status lulus/gagal dari setiap skenario pengujian.

# **2.5.2    Skenario Pengujian**

Skenario pengujian akan disusun berdasarkan fitur-fitur utama sistem. Berikut adalah beberapa skenario uji yang direncanakan:

Skenario pengujian akan disusun berdasarkan fitur-fitur utama sistem. Berikut adalah beberapa skenario uji yang direncanakan:

- a. _Black Box Testing_ Akun Mahasiswa Fakultas Ilmu Komputer

Tabel 2.2. Skenario _Black Box Testing_ Akun Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka landing page website<br>Techfo|Landing page website Techfo ditampilkan<br>dengan tata letak yang benar dan elemen<br>yang berfungsi baik.<br>Pengguna bisa melihat informasi<br>dashboard keaktifan dan prestasi<br>mahasiswa Fakultas Ilmu Komputer|

|||Universitas Pembangunan Nasional<br>"Veteran" Jakarta.|
|---|---|---|
|2|Login dengan username (NIM)<br>dan password<br>Fitur D|Pengguna berhasil masuk ke dashboard<br>mahasiswa jika NIM dan password valid.<br>Jika tidak valid, muncul pesan error.<br>ashboard<br>|
|3|Melihat informasi pada<br>dashboard website Techfo|Informasi umum tentang kegiatan lomba,<br>beasiswa, pengabdian masyarakat, dan<br>penelitian ditampilkan dengan benar.<br>Mahasiswa bisa mengakses menu FAQ<br>melalui dashboard mahasiswa yang terdiri<br>dari prosedur lomba, prosedur beasiswa,<br>prosedur pengabdian masyarakat, dan<br>prosedur penelitian.|
|4|Memilih informasi pengabdian<br>masyarakat|Pengguna dapat memilih informasi<br>pengabdian masyarakat yang tersedia di<br>dashboard.|
|5|Melihat detail informasi<br>pengabdian masyarakat|Detail pengabdian masyarakat yang dipilih<br>ditampilkan, termasuk nama pengabdian<br>masyarakat, deskripsi, nama-nama dosen<br>yang terlibat, dan batas pendaftaran.|
|6|Melakukan pendaftaran<br>pengabdian masyarakat|Tombol daftar dapat diklik dan dapat<br>mengisi form pendaftaran pengabdian<br>masyarakat.|
|7|Memilih informasi penelitian|Pengguna dapat memilih informasi<br>penelitian yang tersedia di dashboard.|
|8|Melihat detail informasi<br>penelitian|Detail penelitian yang dipilih ditampilkan,<br>termasuk nama penelitian, deskripsi,|

|||nama-nama dosen yang terlibat, dan batas<br>pendaftaran.|
|---|---|---|
|9|Melakukan pendaftaran<br>penelitian|Tombol daftar dapat diklik dan dapat<br>mengisi form pendaftaran penelitian.|
||Fitu|r FAQ<br>|
|10|Melihat Prosedur Pendaftaran<br>Pengabdian Masyarakat|Informasi prosedur pendaftaran<br>pengabdian masyarakat ditampilkan<br>dengan format yang mudah dipahami.|
|11|Melihat Prosedur Pengumuman<br>Pengabdian Masyarakat|Prosedur pengumuman pengabdian<br>masyarakat ditampilkan dengan format<br>yang mudah dipahami.|
|12|Melihat Prosedur Pendaftaran<br>Penelitian|Informasi prosedur pendaftaran penelitian<br>ditampilkan dengan format yang mudah<br>dipahami.|
|13|Melihat Prosedur Pengumuman<br>Penelitian|Prosedur pengumuman penelitian<br>ditampilkan dengan format yang mudah<br>dipahami.|
||Fitur|Profile<br>|
|13|Melihat data pribadi mahasiswa|Informasi data pribadi mahasiswa (nama,<br>NIM, program studi, angkatan.)<br>ditampilkan dengan benar.|
|14|Melihat rekapitulasi statistik<br>keaktifan mahasiswa|Statistik keaktifan mahasiswa ditampilkan<br>dalam bentuk angka rekapitulasi keaktifan.|
|15|Melihat riwayat pengabdian<br>masyarakat|Riwayat pengabdian masyarakat<br>ditampilkan dalam bentuk list kartu.|
|16|Melihat riwayat penelitian|Riwayat penelitian ditampilkan dalam<br>bentuk list kartu.|

b. _Black Box Testing_ Akun Admin TU Fakultas Ilmu Komputer

Tabel 2.3. Skenario _Black Box Testing_ Akun Admin TU FIK

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka landing page website<br>Techfo|Landing page website Techfo untuk admin<br>TU ditampilkan dengan tata letak yang<br>benar.|
|2<br>3|Login dengan username (NIDN)<br>dan password<br>Fitur D<br>Melihat informasi pada<br>dashboard website admin Techfo|Admin berhasil masuk ke dashboard jika<br>username dan password valid. Jika tidak,<br>muncul pesan error.<br>ashboard<br>Dashboard menampilkan data statistik<br>keaktifan mahasiswa Fakultas Ilmu<br>Komputer Universitas Pembangunan<br>Nasional "Veteran" Jakarta dan laporan<br>ringkas berupa grafik.|
|4|Menampilkan data real-time<br>laporan keaktifan mahasiswa|Data real-time terkait keaktifan mahasiswa<br>ditampilkan dalam tabel atau grafik.|
|5|Menampilkan data real-time<br>rekap pengabdian masyarakat|Data real-time pengabdian masyarakat<br>ditampilkan berdasarkan lolos atau<br>tidaknya mahasiswa yang mendaftar.|
|6|Menampilkan data real-time<br>rekap penelitian<br>Fitur|Data real-time penelitian  ditampilkan<br>berdasarkan lolos atau tidaknya mahasiswa<br>yang mendaftar.<br>Laporan|
|7|Menampilkan data real-time<br>laporan partisipasi pengabdian<br>masyarakat|Data partisipasi mahasiswa pada<br>pengabdian masyarakat ditampilkan secara<br>lengkap.|
|8|Menampilkan data real-time|Data partisipasi mahasiswa pada penelitian|

||laporan partisipasi penelitian|ditampilkan secara lengkap.|
|---|---|---|
|9|Menampilkan data hasil filter<br>berdasarkan tahun pelaksanaan<br>kegiatan|Sistem menampilkan data sesuai tahun<br>pelaksanaan kegiatan yang dipilih.|
|10|Menampilkan data hasil filter<br>berdasarkan program studi|Sistem menampilkan data berdasarkan<br>program studi mahasiswa.|
|11|Menampilkan data hasil<br>pencarian berdasarkan NIM|Data mahasiswa berdasarkan NIM yang<br>dimasukkan ditampilkan.|
|12|Menampilkan data hasil<br>pencarian berdasarkan nama|Data mahasiswa berdasarkan nama yang<br>dimasukkan ditampilkan.|
|13|Menampilkan tabel pendaftar<br>pengabdian masyarakat yang<br>akan dilakukan seleksi|Data pendaftar pengabdian masyarakat<br>dapat dilakukan seleksi (lolos/tidak) oleh<br>admin.|
|14|Menampilkan tabel pendaftar<br>penelitian yang akan dilakukan<br>seleksi|Data pendaftar penelitian dapat dilakukan<br>seleksi (lolos/tidak) oleh admin.|
|15|Membuka file CV|File CV dapat dibuka dalam format .pdf.|
|16|Membuka file Portofolio|File Portofolio dapat dibuka dalam format<br>.jpg, .jpeg, atau .png.|
|17|Membuka file KHS|File KHS dapat dibuka dalam format .pdf.|
|18|Membuka file Foto|File foto dapat dibuka dalam format .jpg,<br>.jpeg, atau .png.|
|19|Membuka file Surat Pernyataan|File Surat Pernyataan dapat dibuka dalam<br>format .pdf.|
||Fitur Pus|at Informasi|

|20|Membuka fitur pusat informasi|Fitur pusat informasi terbuka dan<br>menampilkan data pengabdian masyarakat<br>dan penelitian yang sudah pernah diunggah<br>(jika ada).|
|---|---|---|
|21|Menambahkan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat baru<br>ditambahkan dan disimpan dalam sistem.|
|22|Melakukan pembaruan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat yang<br>sudah ada dapat diperbarui sesuai<br>kebutuhan.|
|23|Menghapus informasi pengabdian<br>masyarakat|Informasi lomba berhasil dihapus dan tidak<br>lagi ditampilkan.|
|24|Menambahkan informasi<br>penelitian|Informasi penelitian baru ditambahkan dan<br>disimpan dalam sistem.|
|25|Melakukan pembaruan informasi<br>penelitian|Informasi penelitian yang sudah ada dapat<br>diperbarui sesuai kebutuhan.|
|26|Menghapus informasi penelitian|Informasi penelitian berhasil dihapus dan<br>tidak lagi ditampilkan.|

- c. _Black Box Testing_ Akun Wakil Dekan Fakultas Ilmu Komputer

   - Tabel 2.4. Skenario _Black Box Testing_ Akun Wakil  Dekan FIK

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|||Landing page website Techfo untuk admin|
||Membuka landing page website|TU ditampilkan dengan tata letak yang|
|1|Techfo|benar.|
|||Admin berhasil masuk ke dashboard jika|
||Login dengan username (NIDN)|username dan password valid. Jika tidak,|
|2|dan password|muncul pesan error.|
||Fitur D|ashboard|

|3|Melihat informasi pada<br>dashboard website admin Techfo|Dashboard menampilkan data statistik<br>keaktifan mahasiswa Fakultas Ilmu<br>Komputer Universitas Pembangunan<br>Nasional "Veteran" Jakarta dan laporan<br>ringkas berupa grafik.|
|---|---|---|
||Menampilkan data real-time|Data real-time terkait keaktifan mahasiswa|
|4|laporan keaktifan mahasiswa|ditampilkan dalam tabel atau grafik.|
|5|Menampilkan data real-time<br>rekap pengabdian masyarakat|Data real-time pengabdian masyarakat<br>ditampilkan berdasarkan lolos atau<br>tidaknya mahasiswa yang mendaftar.|
|6|Menampilkan data real-time<br>rekap penelitian|Data real-time penelitian  ditampilkan<br>berdasarkan lolos atau tidaknya mahasiswa<br>yang mendaftar.|

||Fitur|Laporan|
|---|---|---|
|7|Menampilkan data real-time<br>laporan partisipasi pengabdian<br>masyarakat|Data partisipasi mahasiswa pada<br>pengabdian masyarakat ditampilkan secara<br>lengkap.|
|8|Menampilkan data real-time<br>laporan partisipasi penelitian|Data partisipasi mahasiswa pada penelitian<br>ditampilkan secara lengkap.|
|9|Menampilkan data hasil filter<br>berdasarkan tahun pelaksanaan<br>kegiatan|Sistem menampilkan data sesuai tahun<br>pelaksanaan kegiatan yang dipilih.|
|10|Menampilkan data hasil filter<br>berdasarkan program studi|Sistem menampilkan data berdasarkan<br>program studi mahasiswa.|
||Menampilkan data hasil|Data mahasiswa berdasarkan NIM yang|
|11|pencarian berdasarkan NIM|dimasukkan ditampilkan.|
||Menampilkan data hasil|Data mahasiswa berdasarkan nama yang|
|12|pencarian berdasarkan nama|dimasukkan ditampilkan.|

|13|Menampilkan tabel pendaftar<br>pengabdian masyarakat yang<br>akan dilakukan seleksi|Data pendaftar pengabdian masyarakat<br>dapat dilakukan seleksi (lolos/tidak) oleh<br>admin.|
|---|---|---|
|14|Menampilkan tabel pendaftar<br>penelitian yang akan dilakukan<br>seleksi|Data pendaftar penelitian dapat dilakukan<br>seleksi (lolos/tidak) oleh admin.|
|15|Membuka file CV|File CV dapat dibuka dalam format .pdf.|
|16|Membuka file Portofolio|File Portofolio dapat dibuka dalam format<br>.jpg, .jpeg, atau .png.|
|17|Membuka file KHS|File KHS dapat dibuka dalam format .pdf.|
|18|Membuka file Foto|File foto dapat dibuka dalam format .jpg,<br>.jpeg, atau .png.|
|19|Membuka file Surat Pernyataan|File Surat Pernyataan dapat dibuka dalam<br>format .pdf.|

|Fitur Pusat Informasi|
|---|

|20|Membuka fitur pusat informasi|Fitur pusat informasi terbuka dan<br>menampilkan data pengabdian masyarakat<br>dan penelitian yang sudah pernah diunggah<br>(jika ada).|
|---|---|---|
|21|Menambahkan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat baru<br>ditambahkan dan disimpan dalam sistem.|
|22|Melakukan pembaruan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat yang<br>sudah ada dapat diperbarui sesuai<br>kebutuhan.|
|23|Menghapus informasi pengabdian<br>masyarakat|Informasi lomba berhasil dihapus dan tidak<br>lagi ditampilkan.|

|24|Menambahkan informasi<br>penelitian|Informasi penelitian baru ditambahkan dan<br>disimpan dalam sistem.|
|---|---|---|
|25|Melakukan pembaruan informasi<br>penelitian|Informasi penelitian yang sudah ada dapat<br>diperbarui sesuai kebutuhan.|
|26|Menghapus informasi penelitian|Informasi penelitian berhasil dihapus dan<br>tidak lagi ditampilkan.|

d. _Black Box Testing_ Akun Koordinator Prodi Fakultas Ilmu Komputer

Tabel 2.5. Skenario _Black Box Testing_ Akun Koordinator Prodi FIK

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka landing page website<br>Techfo|Landing page website Techfo untuk admin<br>TU ditampilkan dengan tata letak yang<br>benar.|
|2|Login dengan username (NIDN)<br>dan password<br>Fitur D|Admin berhasil masuk ke dashboard jika<br>username dan password valid. Jika tidak,<br>muncul pesan error.<br>ashboard|
|3|Melihat informasi pada<br>dashboard website admin Techfo|Dashboard menampilkan data statistik<br>keaktifan mahasiswa Fakultas Ilmu<br>Komputer Universitas Pembangunan<br>Nasional "Veteran" Jakarta dan laporan<br>ringkas berupa grafik.|
|4|Menampilkan data real-time<br>laporan keaktifan mahasiswa|Data real-time terkait keaktifan mahasiswa<br>ditampilkan dalam tabel atau grafik.|
|5|Menampilkan data real-time<br>rekap pengabdian masyarakat|Data real-time pengabdian masyarakat<br>ditampilkan berdasarkan lolos atau<br>tidaknya mahasiswa yang mendaftar.|
|6|Menampilkan data real-time|Data real-time penelitian  ditampilkan|

||rekap penelitian<br>Fitur|berdasarkan lolos atau tidaknya mahasiswa<br>yang mendaftar.<br>Laporan|
|---|---|---|
||Menampilkan data real-time|Data partisipasi mahasiswa pada|
|7|laporan partisipasi pengabdian<br>masyarakat|pengabdian masyarakat ditampilkan secara<br>lengkap.|
|8|Menampilkan data real-time<br>laporan partisipasi penelitian|Data partisipasi mahasiswa pada penelitian<br>ditampilkan secara lengkap.|
|9|Menampilkan data hasil filter<br>berdasarkan tahun pelaksanaan<br>kegiatan|Sistem menampilkan data sesuai tahun<br>pelaksanaan kegiatan yang dipilih.|
|10|Menampilkan data hasil filter<br>berdasarkan program studi|Sistem menampilkan data berdasarkan<br>program studi mahasiswa.|
|11|Menampilkan data hasil<br>pencarian berdasarkan NIM|Data mahasiswa berdasarkan NIM yang<br>dimasukkan ditampilkan.|
|12|Menampilkan data hasil<br>pencarian berdasarkan nama|Data mahasiswa berdasarkan nama yang<br>dimasukkan ditampilkan.|
||Menampilkan tabel pendaftar|Data pendaftar pengabdian masyarakat|
|13|pengabdian masyarakat yang<br>akan dilakukan seleksi|dapat dilakukan seleksi (lolos/tidak) oleh<br>admin.|
|14|Menampilkan tabel pendaftar<br>penelitian yang akan dilakukan<br>seleksi|Data pendaftar penelitian dapat dilakukan<br>seleksi (lolos/tidak) oleh admin.|
|15|Membuka file CV|File CV dapat dibuka dalam format .pdf.|
|16|Membuka file Portofolio|File Portofolio dapat dibuka dalam format<br>.jpg, .jpeg, atau .png.|
|17|Membuka file KHS|File KHS dapat dibuka dalam format .pdf.|

|18|Membuka file Foto|File foto dapat dibuka dalam format .jpg,<br>.jpeg, atau .png.|
|---|---|---|
|19<br>20|Membuka file Surat Pernyataan<br>Fitur Pusa<br>Membuka fitur pusat informasi|File Surat Pernyataan dapat dibuka dalam<br>format .pdf.<br>t Informasi<br>Fitur pusat informasi terbuka dan<br>menampilkan data pengabdian masyarakat<br>dan penelitian yang sudah pernah diunggah<br>(jika ada).|
|21|Menambahkan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat baru<br>ditambahkan dan disimpan dalam sistem.|
|22|Melakukan pembaruan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat yang<br>sudah ada dapat diperbarui sesuai<br>kebutuhan.|
|23|Menghapus informasi pengabdian<br>masyarakat|<br>Informasi lomba berhasil dihapus dan tidak<br>lagi ditampilkan.|
|24|Menambahkan informasi<br>penelitian|Informasi penelitian baru ditambahkan dan<br>disimpan dalam sistem.|
|25|Melakukan pembaruan informasi<br>penelitian|Informasi penelitian yang sudah ada dapat<br>diperbarui sesuai kebutuhan.|
|26|Menghapus informasi penelitian|Informasi penelitian berhasil dihapus dan<br>tidak lagi ditampilkan.|

e. _Black Box Testing_ Akun Dosen Fakultas Ilmu Komputer

Tabel 2.6. Skenario _Black Box Testing_ Akun Dosen FIK

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
||Membuka landing page website|Landing page website Techfo untuk admin|
|1|Techfo|TU ditampilkan dengan tata letak yang|

|||benar.|
|---|---|---|
|2|Login dengan username (NIDN)<br>dan password|Admin berhasil masuk ke dashboard jika<br>username dan password valid. Jika tidak,<br>muncul pesan error.|
||Fitur D|ashboard<br>|
|3|Melihat informasi pada<br>dashboard website admin Techfo|Dashboard menampilkan data statistik<br>keaktifan mahasiswa Fakultas Ilmu<br>Komputer Universitas Pembangunan<br>Nasional "Veteran" Jakarta dan laporan<br>ringkas berupa grafik.|
|4|Menampilkan data real-time<br>laporan keaktifan mahasiswa|Data real-time terkait keaktifan mahasiswa<br>ditampilkan dalam tabel atau grafik.|
|5|Menampilkan data real-time<br>rekap pengabdian masyarakat|Data real-time pengabdian masyarakat<br>ditampilkan berdasarkan lolos atau<br>tidaknya mahasiswa yang mendaftar.|
|6|Menampilkan data real-time<br>rekap penelitian|Data real-time penelitian  ditampilkan<br>berdasarkan lolos atau tidaknya mahasiswa<br>yang mendaftar.|
||Fitur Pusa|t Informasi|
|7|Membuka fitur pusat informasi|Fitur pusat informasi terbuka dan<br>menampilkan data pengabdian masyarakat<br>dan penelitian yang sudah pernah diunggah<br>(jika ada).|
|8|Menambahkan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat baru<br>ditambahkan dan disimpan dalam sistem.|
|9|Melakukan pembaruan informasi<br>pengabdian masyarakat|Informasi pengabdian masyarakat yang<br>sudah ada dapat diperbarui sesuai<br>kebutuhan.|

|10|Menghapus informasi pengabdian<br>masyarakat|Informasi lomba berhasil dihapus dan tidak<br>lagi ditampilkan.|
|---|---|---|
|11|Menambahkan informasi<br>penelitian|Informasi penelitian baru ditambahkan dan<br>disimpan dalam sistem.|
|12|Melakukan pembaruan informasi<br>penelitian|Informasi penelitian yang sudah ada dapat<br>diperbarui sesuai kebutuhan.|
|13|Menghapus informasi penelitian|Informasi penelitian berhasil dihapus dan<br>tidak lagi ditampilkan.|


# PROYEK PENGEMBANGAN SISTEM INFORMASI MANAJEMEN TALENTA PADA FAKULTAS ILMU KOMPUTER UPN VETERAN JAKARTA

# **BAB II**

# **RANCANGAN PROYEK**

# **2.1. Observasi**

# **2.1.1. Proses Bisnis Saat Ini**

Berdasarkan pengumpulan data yang telah dilakukan, alur pengajuan manajemen talenta saat ini dengan menggunakan _activity diagram_ dapat digambarkan sebagai berikut.

<!-- Start of picture text -->
| a Ole<br><!-- End of picture text -->

Gambar 2.1 Activity Diagram Sistem Berjalan

Sumber: Dokumen Pribadi

# **2.1.2. Deskripsi Aktor Sistem Berjalan**

Beberapa aktor yang terlibat dalam sistem yang sedang berjalan dan kegiatan

yang dilakukan oleh aktor.

Tabel 2.1. Deskripsi Aktor Sistem yang Berjalan

|No.|Nama Aktor|Deskripsi|
|---|---|---|
|1|Mahasiswa|1. Melakukan Pendaftaran Kegiatan<br>2. Mengikuti Kegiatan<br>3. Mengisi kegiatan pada website Prestasi Mahasiswa|
|2|Wakil Dekan III (PIC<br>Manajemen Talenta)|1. Bertanggung jawab untuk proses seleksi kegiatan<br>2. Menjadi penghubung antara fakultas,  dosen<br>ormawa, dan mahasiswa.|

|3|Dekan|1. Bertanggung jawab<br>informasi masuk dari<br>mengirimkan informa<br>yang akan mengikuti k|hanya<br>untuk mendapat<br>penyelenggara kegiatan dan<br>si keluar terkait mahasiswa<br>egiatan tersebut.|
|---|---|---|---|
|4|Kaprodi|1. Bertanggung jawab<br>informasi masuk dari<br>mengirimkan informa<br>yang akan mengikuti k|hanya<br>untuk mendapat<br>penyelenggara kegiatan dan<br>si keluar terkait mahasiswa<br>egiatan tersebut.|
|5|Dosen Pembimbing|1. Bertanggung<br>jawab<br>Manajemen Talenta un<br>mahasiswa untuk men|untuk<br>membantu<br>PIC<br>tuk mencari dan memantau<br>gikuti kegiatan terkait.|
|6|BEMF-IK|1. Bertanggung<br>jawab<br>Manajemen Talenta<br>untuk mengikuti kegia|untuk<br>membantu<br>PIC<br>untuk mencari mahasiswa<br>tan terkait.|

# **2.1.3. Prosedur Sistem Berjalan**

Sistem pendataan yang diterapkan oleh Fakultas Ilmu Komputer UPN “Veteran” Jakarta memiliki tahapan yang sudah berjalan. Yaitu saat ini, Fakultas Ilmu Komputer (FIK) dan Universitas Pembangunan Nasional Veteran Jakarta (UPNVJ) belum memiliki sistem informasi berbasis website untuk manajemen talenta mahasiswa. Akibatnya, ketika ada kebutuhan untuk mencari mahasiswa yang akan mengikuti lomba atau kegiatan tertentu, pencarian dilakukan secara mendadak dan manual. Proses ini tidak efisien karena tidak ada data yang terdokumentasi dengan baik mengenai minat dan bakat mahasiswa.

Selama ini, pencarian talenta mahasiswa hanya dilakukan dengan cara mengumumkan lomba melalui Badan Eksekutif Mahasiswa (BEM) dan berharap mereka bisa menemukan mahasiswa berbakat yang sesuai untuk mengikuti kegiatan tersebut. Namun, karena tidak adanya sistem pendataan yang komprehensif, mahasiswa dengan talenta tertentu sering kali tidak teridentifikasi dengan baik. Ini menyebabkan kesulitan bagi bagian kemahasiswaan dalam menemukan dan merekomendasikan mahasiswa yang tepat untuk berbagai kegiatan.

Mahasiswa yang memiliki soft skills atau talenta khusus tidak terdata dengan baik dalam sistem yang berjalan saat ini. Hal ini mengakibatkan seringnya terjadi kesulitan dalam mencari mahasiswa berbakat untuk berpartisipasi dalam lomba atau kegiatan lainnya. Akibatnya, banyak potensi mahasiswa yang tidak teroptimalkan,

dan bagian kemahasiswaan sering kali mengandalkan mahasiswa yang sama berulang kali untuk mewakili universitas.

Oleh karena itu, diperlukan sekali sistem informasi berbasis website untuk manajemen talenta mahasiswa. Sistem ini akan membantu bagian kemahasiswaan dalam mendata dan mengidentifikasi mahasiswa yang memiliki soft skills dan talenta tertentu, sehingga proses pencarian dan rekomendasi mahasiswa untuk berbagai kegiatan menjadi lebih efisien dan terstruktur. Dengan adanya sistem ini, informasi mengenai minat dan bakat mahasiswa dapat terdokumentasi dengan baik, memudahkan pihak universitas dalam mengoptimalkan potensi mahasiswanya.

Untuk melihat dan menganalisis sistem yang sudah ada dan sistem yang akan diusulkan, bisa menggunakan analisis PIECES yang terdapat dilihat dalam tabel 1.

Tabel 2.2. Analisis Metode PIECES

|No.|PIECES|Sistem Saat Ini|Sistem Susulan|
|---|---|---|---|
|1.|_Performance_|Pada sistem yang berjalan saat ini<br>masih dilakukan manual seperti<br>pendataan dan pelaporan.|Pada sistem yang diusulkan,<br>data manajemen talenta, riwayat<br>mengikuti<br>perlombaan,<br>dan<br>pelaporan<br>dapat<br>dilakukan<br>dengan sistem.|
|2.|_Information_|● Mahasiswa<br>yang<br>memiliki<br>bakat atau keterampilan khusus<br>tidak terdata dengan baik,<br>sehingga mereka sering kali<br>tidak mendapat kesempatan<br>untuk<br>menunjukkan<br>atau<br>mengembangkan bakat mereka<br>dalam kegiatan yang sesuai.<br>● Mahasiswa<br>berbakat<br>tidak<br>mendapatkan informasi tentang<br>kegiatan atau lomba yang bisa<br>mereka ikuti, sehingga mereka<br>kehilangan kesempatan untuk<br>berprestasi<br>dan<br>mengembangkan kemampuan<br>mereka lebih lanjut.<br>● Mahasiswa dengan minat dan<br>bakat yang sama tidak memiliki<br>platform<br>untuk<br>saling<br>menemukan dan berkolaborasi,<br>yang membatasi peluang untuk<br>bekerja sama dalam proyek<br>atau<br>kegiatan<br>yang<br>dapat<br>memperkaya<br>pengalaman|● Sistem informasi manajemen<br>talenta akan menyediakan<br>data<br>yang<br>terpusat<br>dan<br>terstruktur tentang minat dan<br>bakat<br>mahasiswa,<br>memastikan bahwa semua<br>talenta teridentifikasi dengan<br>baik.<br>● Informasi terkait kegiatan<br>dan<br>lomba<br>akan<br>diintegrasikan dalam satu<br>platform yang mudah diakses<br>oleh<br>semua<br>mahasiswa,<br>memastikan bahwa mereka<br>tidak kehilangan kesempatan<br>untuk berpartisipasi.<br>● Sistem akan memfasilitasi<br>antar<br>mahasiswa<br>yang<br>memiliki minat dan bakat<br>yang sama, meningkatkan<br>peluang untuk kerja sama<br>dan pengembangan diri yang<br>lebih baik.|

|No.|PIECES|Sistem Saat Ini<br>belajar dan pengembangan diri<br>mereka.|Sistem Susulan|
|---|---|---|---|
|3.|_Economic_|Pada sistem yang berjalan saat ini<br>anggaran biaya diperlukan untuk<br>membeli kertas formulir.|Pada sistem yang diusulkan,<br>seluruh proses kerja disimpan<br>dalam sistem sehingga anggaran<br>biaya dapat berkurang.|
|4.|_Control_|● Pendataan<br>mahasiswa<br>yang<br>dilakukan secara manual rentan<br>terhadap<br>kebocoran<br>dan<br>penyalahgunaan<br>data.<br>Data<br>pribadi<br>mahasiswa<br>tidak<br>terlindungi dengan baik dan<br>bisa diakses oleh pihak yang<br>tidak berwenang.<br>● Sistem manual tidak memiliki<br>mekanisme<br>kontrol<br>yang<br>memadai untuk melindungi<br>privasi<br>mahasiswa.<br>Data<br>sensitif seperti minat, bakat,<br>dan informasi pribadi lainnya<br>bisa<br>tersebar<br>tanpa<br>sepengetahuan mahasiswa.<br>● Dengan<br>pendataan<br>manual,<br>sulit untuk mengatur siapa saja<br>yang memiliki akses ke data<br>mahasiswa. Ini meningkatkan<br>risiko<br>data<br>diakses<br>atau<br>disalahgunakan<br>oleh<br>pihak<br>yang tidak seharusnya.|● Sistem informasi manajemen<br>talenta yang berbasis website<br>akan menggunakan teknologi<br>untuk<br>melindungi<br>data<br>mahasiswa. Informasi yang<br>tersimpan dalam sistem akan<br>dienkripsi sehingga hanya<br>pihak yang berwenang yang<br>dapat<br>mengakses<br>dan<br>membacanya.<br>● Sistem baru akan memiliki<br>fitur kontrol akses yang ketat.<br>Hanya<br>pengguna<br>yang<br>memiliki izin khusus yang<br>dapat<br>mengakses<br>data<br>sensitif. Selain itu, sistem<br>akan<br>dilengkapi<br>dengan<br>mekanisme<br>audit<br>untuk<br>melacak siapa saja yang<br>mengakses data dan kapan<br>akses tersebut terjadi.<br>● Dengan<br>sistem<br>berbasis<br>website,<br>fakultas<br>dapat<br>dengan mudah mengatur dan<br>membatasi<br>akses<br>data<br>berdasarkan<br>peran<br>dan<br>tanggung jawab pengguna.<br>Misalnya, hanya staf tertentu<br>yang dapat mengakses data<br>pribadi<br>mahasiswa,<br>sementara mahasiswa hanya<br>dapat mengakses informasi<br>terkait diri mereka sendiri.|
|5.|_Efficiency_|Pada sistem yang berjalan saat ini<br>proses manajemen talenta karena<br>masih dilakukan secara manual,<br>sehingga membutuhkan waktu<br>untuk setiap pekerjaan.|Pada sistem yang diusulkan,<br>setiap proses seperti pencatatan<br>dan pelaporan dilakukan dengan<br>sistem<br>sehingga<br>dapat<br>meminimalisir waktu.|

|No.|PIECES|Sistem Saat Ini|Sistem Susulan|
|---|---|---|---|
|6.|_Service_|● Informasi<br>tentang<br>kegiatan,<br>lomba, dan kesempatan lainnya<br>disebarkan melalui pihak ketiga<br>seperti BEM atau dosen, yang<br>sering kali tidak efektif dan tidak<br>mencapai seluruh mahasiswa<br>yang relevan.<br>● Mahasiswa<br>dengan<br>talenta<br>khusus<br>sering<br>kali<br>tidak<br>mendapatkan dukungan yang<br>memadai<br>untuk<br>mengembangkan bakat mereka<br>karena kurangnya dokumentasi<br>dan sistem pengelolaan yang<br>terstruktur.<br>● Pengelolaan<br>data<br>talenta<br>mahasiswa<br>dilakukan<br>secara<br>manual, yang memakan waktu<br>dan sering kali tidak akurat. Hal<br>ini<br>memperlambat<br>respons<br>fakultas<br>dalam<br>memberikan<br>dukungan atau menindaklanjuti<br>kebutuhan mahasiswa berbakat.|● Sistem informasi manajemen<br>talenta yang berbasis website<br>akan<br>menyediakan<br>portal<br>terpusat<br>dimana<br>semua<br>informasi terkait kegiatan,<br>lomba,<br>dan<br>kesempatan<br>lainnya dapat diakses oleh<br>seluruh<br>mahasiswa.<br>Ini<br>memastikan bahwa semua<br>mahasiswa<br>mendapatkan<br>informasi<br>yang<br>mereka<br>butuhkan tepat waktu.<br>● Dengan data yang terstruktur<br>dan terpusat, fakultas dapat<br>dengan<br>mudah<br>mengidentifikasi mahasiswa<br>berbakat<br>dan<br>memberikan<br>dukungan<br>yang<br>mereka<br>butuhkan.<br>Ini<br>termasuk<br>bimbingan,<br>pelatihan,<br>dan<br>kesempatan untuk mengikuti<br>kegiatan yang relevan dengan<br>bakat mereka.<br>● Sistem<br>baru<br>akan<br>mengotomatisasi<br>banyak|
||||proses<br>yang<br>sebelumnya<br>dilakukan<br>secara<br>manual.|
||||Misalnya,<br>pendaftaran<br>kegiatan,<br>pemantauan<br>perkembangan talenta, dan<br>pengelolaan data mahasiswa.<br>Ini<br>akan<br>meningkatkan|
||||efisiensi<br>dan<br>akurasi<br>pengelolaan talenta.|

# **2.2. Usulan Solusi**

# **2.2.1.** **_Data Flow Diagram_ (DFD)**

Data Flow Diagram (DFD) digunakan untuk menggambarkan aliran informasi dan transformasi data dalam sebuah sistem secara visual. DFD membantu dalam memahami proses bisnis atau sistem informasi dengan cara yang lebih mudah dan terstruktur. Berikut merupakan gambar data flow diagram untuk sistem informasi ini.

- Diagram Konteks

Diagram konteks merupakan gambaran dasar dari keseluruhan sistem atau proses yang dianalisis atau dimodelkan. Diagram konteks merepresentasikan seluruh sistem sebagai gelembung tunggal dengan data input dan output yang ditunjukkan oleh panah masuk atau keluar. Berikut ini adalah alur proses dari diagram konteks:

<!-- Start of picture text -->
<= ——————<br>i a] a = en<br>Sane =o oe separ ra ty‘TI ae i ean Fors<br>‘Sistem Informasi === anes oes erp —<br>[Manajemen Talenta<br>Le pgm me OER \\, ueSakariFIKigan Arentrenner]eTrr sora|<br><!-- End of picture text -->

Gambar 2.2 Diagram Konteks

Sumber: Dokumen Pribadi

1. Mahasiswa

Alur diagram konteks untuk aktor mahasiswa diawali dengan mahasiswa mengirimkan isi data diri secara lengkap kepada sistem, kemudian mahasiswa akan mendapat informasi kegiatan dari sistem, kemudian mahasiswa akan mengirimkan isi form pendaftaran kepada sistem. Sistem akan memberikan info halaman pendaftaran, dan mahasiswa akan memberikan pendaftaran kepada sistem. Apabila sudah berhasil melakukan pendaftaran dan mengikuti kegiatan kepada sistem, sistem akan memberikan info status pendaftaran kepada mahasiswa.

2. PIC Manajemen Talenta

Alur diagram diagram konteks untuk aktor PIC manajemen talenta diawali dengan edit info kegiatan yang akan diberikan kepada sistem, kemudian sistem akan edit isi halaman pendaftaran. Apabila sudah ada

mahasiswa yang akan mengisi form pendaftaran, maka PIC manajemen talenta akan melakukan seleksi mahasiswa yang akan mengikuti kegiatan kepada sistem. Selanjutnya, PIC manajemen talenta akan membuat dan meminta laporan mahasiswa lolos kegiatan berdasarkan data dari detail laporan dari sistem kepada PIC manajemen talenta.

3. Kaprodi

Alur diagram diagram konteks untuk kaprodi diawali dengan sistem akan mendapat edit informasi dari kaprodi. Kemudian kaprodi akan menerima data informasi kegiatan dari sistem kepada kaprodi, kemudian sistem akan mengirimkan laporan lolos kegiatan kepada kaprodi.

4. Dosen Pembimbing

Alur diagram konteks untuk dosen pembimbing yaitu sistem memberikan informasi kegiatan kepada dosen pembimbing. Tujuan dimasukkannya dosen pembimbing pada tahapan manajemen talenta ini yaitu karena dosen pembimbing bisa menjadi penyalur informasi kepada mahasiswa dan apabila mahasiswa bertanya lebih lanjut seputar manajemen talenta, dosen pembimbing dapat menjelaskan dengan baik.

5. BEMF-IK

Alur diagram diagram konteks untuk BEMF-IK yaitu sistem memberikan informasi kegiatan kepada BEMF-IK. Tujuan dimasukkannya dosen pembimbing pada tahapan manajemen talenta ini yaitu karena BEMF-IK bisa menjadi penyalur informasi kepada mahasiswa dan apabila mahasiswa bertanya lebih lanjut seputar manajemen talenta, BEMF-IK dapat menjelaskan dengan baik.

6. Admin

Alur diagram konteks untuk aktor admin diawali dengan admin yang memberikan akses password kepada setiap _stakeholder_ kecuali mahasiswa. Selain itu admin sendiri memiliki akses yang hampir sama dengan PIC manajemen talenta. Hal ini disamakan dengan PIC Manajemen Talenta untuk memastikan kelancaran pembaruan informasi dan kegiatan. Dengan demikian, jika PIC Manajemen Talenta yang merupakan Wakil Dekan 3 sedang memiliki kesibukan lain, proses update tetap dapat dilakukan secara tepat waktu tanpa harus menunggu keterlibatan langsung dari PIC Manajemen Talenta. Seperti yang dapat dilihat, edit info kegiatan yang akan

diberikan kepada sistem, kemudian sistem akan edit isi halaman pendaftaran. Apabila sudah ada mahasiswa yang akan mengisi form pendaftaran, maka PIC manajemen talenta akan melakukan seleksi mahasiswa yang akan mengikuti kegiatan kepada sistem. Selanjutnya, PIC manajemen talenta akan membuat dan meminta laporan mahasiswa lolos kegiatan dan lolos kejuaraan berdasarkan data dari detail laporan dari sistem kepada PIC manajemen talenta.

# - DFD Level 0

Di level 0, diagram konteks dipisah menjadi beberapa gelembung atau proses. Maka dari itu, DFD level 0 memberikan pemecahan yang lebih rinci dari potongan-potongan diagram konteks. Melalui level ini, penulis akan membagikan secara rinci dari fungsi utama yang dilakukan oleh sistem. Berikut ini adalah alur proses dari DFD Level 0:

Gambar 2.3 DFD Level 0

Sumber: Dokumen Pribadi

# 1. Login

Mahasiswa, BEMF-IK, dosen pembimbing, admin, kaprodi, dan PIC manajemen talenta melakukan login pada sistem dengan menginput _Username_ (NIM untuk mahasiswa) dan NIDN (untuk dosen pembimbing, kaprodi,  PIC manajemen talenta) dan password yang sudah terdaftar pada database UPN Veteran Jakarta yang akan dimasukan oleh admin. Lalu, sistem akan melakukan pengecekan data didalam _database_ . Apabila data yang dikirimkan sudah sesuai, maka _database_ akan mengirim validasi data oleh admin dan sistem akan mengirimkan hasil validasi berupa berhasil login.

2. Data Diri Secara Lengkap

Pada _flow_ data diri secara lengkap merupakan bagian yang hanya diikuti oleh mahasiswa. Mahasiswa akan mengisi data diri mereka secara lengkap dengan nama “data_mahasiswa” dan data tersebut akan disimpan dengan nama “Data Talenta Mahasiswa”.

3. Mengelola Data Kegiatan

Pada bagian mengelola data kegiatan, sistem akan memberikan informasi kegiatan kepada mahasiswa, kaprodi, BEMF-IK, PIC manajemen talenta, dan dosen pembimbing. Selain itu juga kaprodi akan mengirim edit informasi kegiatan. Informasi kegiatan tersebut akan disimpan pada database program manajemen talenta.

4. Melakukan Pendaftaran

Pada bagian melakukan pendaftaran dimulai ketika mahasiswa mengirimkan data mahasiswa kepada sistem. Selanjutnya PIC manajemen talenta mengirimkan data form pendaftaran kepada sistem. Data form tersebut akan dikirimkan dari sistem kepada mahasiswa. Apabila sudah diisi oleh mahasiswa, maka data tersebut akan berubah menjadi data _input form_ pendaftaran, dan akan dikirimkan kepada sistem. Dan hasil akhirnya PIC manajemen talenta akan mendapat data _input form_ pendaftaran. Data input pendaftaran dan data _input form_ pendaftaran tersebut akan disimpan kedalam _database_ “Pendaftaran”.

5. Melakukan Seleksi Pendaftaran

Pada bagian melakukan seleksi pendaftaran dimulai ketika PIC manajemen talenta memberikan hasil seleksi pendaftaran kepada sistem. Hasil seleksi pendaftaran tersebut akan dikirim kepada mahasiswa dan kaprodi oleh sistem. Hasil seleksi pendaftaran akan disimpan pada _database_ “Pendaftaran”.

6. Membuat Laporan Lolos Pendaftaran

Pada tahapan ini dimulai ketika kaprodi dan PIC manajemen talenta memberikan data laporan lolos pendaftaran yang sudah pasti dan tidak ada perubahan data lagi kepada sistem. Kemudian data laporan lolos pendaftaran tersebut bisa dilakukan _export_ dengan format excel. Data laporan lolos pendaftaran akan disimpan pada database “Pelaporan”.

- DFD Level 1

DFD level 1 menyajikan detail yang lebih spesifik. Level ini pada satu kondisi memerlukan lebih banyak teks untuk mencapai tingkat detail yang diperlukan tentang fungsi sistem. Berikut tampilan DFD level 1.

1. DFD Level 1 - Login

Mahasiswa, dekan, BEMF-IK, dosen pembimbing, PIC manajemen talenta, dan kaprodi dapat melakukan login dengan menginput _username_ dan _password_ ke dalam sistem. Lalu, username dan password tersebut akan divalidasi oleh database yang dipegang oleh admin. Apabila username dan password berhasil dikonfirmasi, maka sistem akan menampilkan halaman dashboard utama.

<!-- Start of picture text -->
[ Mahasiowa | Usemame & Password:<br>Usemae & senor manasiwa<br>Data konfirmasi login<br><!-- End of picture text -->

Gambar 2.4 DFD Level 1 - Login

Sumber: Dokumen Pribadi

2. DFD Level 1 - Data Diri Lebih Lengkap

Pada bagian data diri secara lengkap diawali dengan sistem memberikan default informasi data diri kepada mahasiswa yang terdapat pada form pengisian data diri. Selanjutnya apabila mahasiswa sudah mengisi data diri tersebut, maka data tersebut menjadi detail data diri lebih rinci kepada sistem. Sistem akan menyimpan data detail diri lebih rinci kedalam _database_ data talenta mahasiswa.

<!-- Start of picture text -->
Data Talenta<br>Mahasiswa<br>detail data diri lebih rinci<br>default informasi data diri-<br>2.1 Data Diri r data d<br>Lebih Lengkap form pengisian data diri:<br><!-- End of picture text -->

Gambar 2.5 DFD Level 1 - Data Diri Lebih Lengkap

Sumber: Dokumen Pribadi

3. DFD Level 1 – Mengelola Data Kegiatan

Pada bagian mengelola data kegiatan dimana PIC manajemen talenta dapat melakukan proses _edit_ informasi kegiatan pada bagian mengelola data kegiatan dan menyimpannya kedalam “Program Manajemen Talenta”. Selanjutnya data yang sudah diolah tersebut akan ditampilkan dari sistem kepada mahasiswa, dosen pembimbing, kaprodi, BEMF-IK, dan PIC manajemen talenta menjadi informasi kegiatan.

<!-- Start of picture text -->
—Frrosram<br>Manajemen Talenta<br>informasi Kegiatan<br>PIC Manajamen 3.1 Mengelola<br>Talenta edit informasi Kegiatan data kegiatan<br>Mahasiswa<br>Kaprodi<br>3.2 Menampilan \_informasi Kegiatan<br>BEMF-IK data kegiatan Dosen<br>Pembimbing<br>informasi Kegiatan-<br><!-- End of picture text -->

Gambar 2.6 DFD Level 1 - Mengelola Data Kegiatan

Sumber: Dokumen Pribadi

4. DFD Level 1 – Melakukan Pendaftaran

Pada alur melakukan pendaftaran dimulai pada proses melakukan pendaftaran manajemen talenta, dimana PIC manajemen talenta memberikan data form pendaftaran kepada sistem, kemudian sistem akan memberikan data form pendaftaran tersebut kepada mahasiswa. Apabila mahasiswa sudah mengisi data input tersebut, maka data tersebut akan berubah nama menjadi data _input form_ pendaftaran dan akan diberikan kepada sistem. Data _input form_ pendaftaran akan masuk kedalam sistem dengan proses validasi data dan proses menyimpan data. Data _input form_ pendaftaran juga akan diberikan dari sistem kepada PIC manajemen talenta dan akan disimpan pada _database_ dengan nama Pendaftaran Manajemen Talenta.

<!-- Start of picture text -->
em<br>Manajemen Talon<br>alent /4.1ManajemenTeniaMelakukan\ aia input form pendaftaran<br>‘ta tom ender<br>42 valde<br>data<br>da pt em pence<br>input om pondtaran<br>[3menymoan]mmenyinpan aap om padatrar—> yhPendataran ta<br><!-- End of picture text -->

Gambar 2.7 DFD Level 1 - Melakukan Pendaftaran

Sumber: Dokumen Pribadi

5. DFD Level 1 – Melakukan Seleksi Pendaftaran

Pada proses melakukan seleksi pendaftaran dimulai ketika PIC manajemen talenta mengambil _data input form_ pendaftaran, apabila selesai melakukan seleksi maka akan terdapat data baru yaitu data hasil. Selanjutnya masuk ke proses validasi data, dan proses menampilkan hasil seleksi. Pada hasil seleksi akan terdapat data baru yaitu hasil seleksi yang diberikan oleh sistem kepada mahasiswa.

<!-- Start of picture text -->
Pendaftaran<br>Manajemen Talenta<br>data input form pendaftaran<br>5.2 Validasi data p 1MenyeleksManajemen PIC ManajamenTalenta<br>data hasil Talenta data inputIp form per pendaftaran|<br>ata hesi 5.3 Menampilkan hasil seleksi Mahasiswa<br>hasil seleksi<br>data hasil seleksi<br>Hasil Seleksi<br><!-- End of picture text -->

Gambar 2.8 DFD Level 1 - Melakukan Seleksi Pendaftaran

# Sumber: Dokumen Pribadi

6. DFD Level 1 – Membuat Laporan Lolos Seleksi Pendaftaran

Pada proses membuat laporan lolos seleksi pendaftaran dimulai dengan PIC manajemen data memberikan data laporan lolos pendaftaran kepada sistem. Data laporan lolos pendaftaran tersebut akan diberikan oleh sistem kepada kaprodi untuk proses pembuatan laporan lolos pendaftaran. Setelah selesai membuat dan menganalisis laporan lolos pendaftaran, maka PIC manajemen talenta dan kaprodi akan memberikan data laporan lolos pendaftaran kepada sistem. Data laporan lolos pendaftaran tersebut akan disimpan oleh sistem pada _database_ , dan masuk ke proses selanjutnya yaitu hasil laporan lolos pendaftaran.

<!-- Start of picture text -->
Hasil Seleksi<br>hasil seleksi<br>data laporan lolos pendaftaran,<br>laporan lolos pendaftaran —pelaporan<br>PIC Manajamen | aporan lolos pendaftaran)<br>Talenta 6.1 Membuat laporan lolos pendaftaran<br>Laporan Lolos<br>Seleksi<br>Pendaftaran<br>kaprodi data laporan lolos pendaftaran. BEMF-IK<br>Japoran lolos pendaftaran<br>[6.2 Hasil Laporan\—laporan lolos pendaftaran<br>olos Pendaftara<br><!-- End of picture text -->

Gambar 2.9 DFD Level 1 - Membuat Laporan Lolos Pendaftaran Sumber: Dokumen Pribadi

# **2.3. Rancangan Proyek**

Pada tahapan ini akan menjelaskan bagaimana kebutuhan analisis dari tampilan antarmuka yang akan diusulkan beserta dengan fungsionalitasnya. Penjelasan terkait kebutuhan dan tampilan tersebut akan dijelaskan pada penjelasan berikut ini.

# **2.3.1.** **_Need Analysis User Experience_ dan** **_User Interface_**

Pada bagian _need analysis_ ini, penulis menjelaskan bagaimana kebutuhan pengguna terkait pengalaman dan antarmuka pengguna yang sudah ditinjau, dianalisis, dan diterjemahkan menjadi sebuah desain sistem yang efektif. Penjabaran tersebut dijelaskan pada penjelasan berikut.

# **_2.3.1.1.Need Analysis_ pada** **_User Experience_**

Dalam pengembangan sistem manajemen talenta, penting untuk memahami kebutuhan pengguna. Hal ini bertujuan agar membantu pengguna dari berbagai aspek seperti  efisiensi, kemudahan akses data, mengambil keputusan bisnis yang lebih cepat, dan  sebagainya. Dalam analisis kebutuhan ini terdapat beberapa poin analisis yang dilakukan, seperti visualisasi data, aksesibilitas informasi, sistem pendaftaran _online_ , _dashboard_ pengelolaan data, serta laporan dan statistik otomatis.

Oleh karena itu, dilakukan analisis kebutuhan untuk mengidentifikasi hal-hal yang dibutuhkan oleh pengguna, sehingga sistem yang dibangun dapat memenuhi ekspektasi mereka dan meningkatkan efisiensi proses. Beberapa kebutuhan yang dapat diidentifikasi dari hasil analisis, antara lain:

Tabel 2.3. _Need Analysis_ pada _User Experience_

|**Komponen**<br>**_User Experience_**|**Tujuan****_User_**<br>**_Experience_**|**Tujuan****_User_**<br>**_Experience_**|**Desain  Pengalaman**<br>**yang  Diusulkan**|
|---|---|---|---|
||Menyajikan data|Grafik dan tabel interaktif|Grafik batang, pie, dan|
||secara<br>visual|yang dapat menampilkan|garis<br>dengan<br>fitur|
|Visualisasi Data|dalam<br>format<br>yang<br>mudah|detail data, seperti jumlah<br>mahasiswa<br>berbakat,|interaktif seperti_hover_<br>untuk detail data,_filter_|
||dipahami<br>dan<br>menarik.|jumlah<br>kegiatan,<br>dan<br>statistik prestasi.|kategori, dan opsi unduh<br>data.|
|Aksesibilitas|Memastikan|Informasi yang_up-to-date_|Antarmuka berbasis web|
|Informasi|informasi|tentang<br>kegiatan<br>yang|yang<br>responsif,|

||kegiatan<br>atau<br>lomba<br>dapat<br>diakses<br>dengan<br>cepat<br>oleh<br>pengguna.|relevan dengan mina<br>bakat<br>pengguna,<br>tersedia<br>kapan<br>melalui<br>perangkat<br>pun.|t dan<br>yang<br>saja<br> <br>apa|notifikas<br>untuk<br>kegiatan<br>kegiatan<br>kategori<br>terorgan|i<br>_re_<br>pengu<br>, dan h<br> <br> <br> <br>isir.|_al-time_<br>muman<br>alaman<br>dengan<br>yang|
|---|---|---|---|---|---|---|
|Sistem Pendaftaran<br>Online|Memudahkan<br>pengguna<br>untuk<br>mendaftar<br>kegiatan<br>atau<br>lomba<br>tanpa<br>proses manual.|Formulir pendaftaran<br>intuitif dengan konfi<br>instan dan kemam<br>untuk<br>melacak<br>pendaftaran.|yang<br>rmasi<br>puan<br>status|Formulir<br>_input_<br>konfirma<br>melalui<br>dan_da_<br>melihat<br>pendafta|_online_ <br>sed<br>si<br>o<br>email/not<br>_shboard_ <br>ran.|dengan<br>erhana,<br>tomatis<br>ifikasi,<br>untuk<br>status|
|Dashboard|Memberikan alat|_Dashboard_|yang|_Dashboa_|_rd_<br>|dengan|
|Pengelolaan Data|yang<br>intuitif<br>untuk memantau<br>dan<br>mengelola<br>data<br>mahasiswa<br>berbakat.|menampilkan<br>mahasiswa, prestasi<br>perkembangan<br>ke<br>secara lebih terorgan|data<br>, dan<br>giatan<br>isir.|tampilan<br>navigasi<br>tabel<br>_sorting/f_<br>grafik<br>monitori|<br>_clean_<br> <br>sed<br>dengan<br>_ilter_,<br>visual<br>ng.|dan<br>erhana,<br>fitur<br>serta<br>untuk|
||Mempermudah<br>pengelolaan|Laporan<br>yang<br>dihasilkan<br>s|dapat<br>ecara|Laporan<br>dan tab|berbasis<br>el denga|grafik<br>n fitur|
|Laporan<br>dan<br>Statistik Otomatis|laporan kegiatan<br>dan prestasi untuk<br>evaluasi<br>serta<br>akreditasi.|otomatis,<br>dengan<br>unduh dalam format<br>sesuai (_Excel_).|opsi<br>yang|ekspor<br>dashboar<br>untuk<br>data yan|langsun<br>d, serta<br>menyes<br>g ditampi|g dari<br>filter<br>uaikan<br>lkan.|

Tabel 2.3 ini mampu memberikan penjelasan mengenai kebutuhan UX yang dirancang  untuk memberikan pengalaman yang lancar, intuitif, dan memuaskan bagi semua aktor  sistem. Dengan demikian, desain pengalaman yang diusulkan dapat memastikan sistem  mendukung tugas pengguna secara optimal.

# **_2.3.1.2.Need Analysis_ pada** **_User Interface_**

Bagian ini berfokus pada aspek visual dan interaktif dari sistem informasi manajemen talenta. Melalui analisis kebutuhan ini, penulis nantinya dapat membuat antarmuka yang  intuitif, mudah digunakan, serta menarik secara visual untuk seluruh aktor. Adapun  komponen yang dibutuhkan tergambar pada tabel 2.4 berikut.

Tabel 2.4. _Need Analysis_ pada _User Interface_

|**Komponen**<br>**_User Interface_**|**Fungsi**|**Desain yang Dibutuhkan**|**Contoh**|**Implementasi**|
|---|---|---|---|---|
|Halaman<br>Data<br>Talenta<br>Mahasiswa|Menyediakan data<br>terorganisir<br>tentang<br>talenta<br>mahasiswa,<br>termasuk<br>minat,<br>bakat, dan prestasi<br>yang<br>telah<br>dicapai.|Halaman<br>ini<br>dirancang<br>dengan tabel interaktif yang<br>memungkinkan<br>pengguna<br>untuk melihat data mahasiswa<br>berbakat secara terorganisir.<br>Tabel<br>ini<br>memiliki<br>fitur<br>pencarian dan filter untuk<br>menyortir data berdasarkan<br>jurusan, minat, bakat, atau<br>tingkat prestasi. Selain itu,<br>setiap baris tabel dilengkapi<br>dengan tombol "Detail" yang<br>mengarahkan pengguna ke<br>profil lengkap mahasiswa,<br>yang mencakup informasi<br>diri, riwayat kegiatan, serta<br>grafik perkembangan prestasi<br>yang disajikan secara visual.|Halama<br>data<br>interakt<br>dengan<br>dapat<br>difilter.<br>"Detail<br>baris<br>penggu<br>khusus<br>profil<br>mahasi<br>grafik<br>perkem|n dengan tabel<br>talenta<br>yang<br>if,<br>dilengkapi<br>kolom yang<br>disortir<br>dan<br> <br>Tombol<br>" pada setiap<br>membawa<br>na ke halaman<br>untuk melihat<br>lengkap<br>swa, termasuk<br>visual tentang<br>bangan mereka.|

|Dashboard<br>Utama|Menampilkan<br>ringkasan<br>data<br>dan<br>status<br>mahasiswa<br>serta<br>kegiatan terkini.|_Dashboard_<br>utama<br>menampilkan ringkasan data<br>menggunakan_summary cards_<br>yang<br>memuat<br>jumlah<br>mahasiswa berbakat, jumlah<br>kegiatan aktif, dan jumlah<br>prestasi<br>terbaru.<br>Bagian<br>tengah_dashboard_dilengkapi<br>dengan grafik visual seperti<br>_pie chart_,_bar chart_untuk<br>menunjukkan distribusi dan<br>tren data. Di bagian bawah,<br>ditampilkan daftar kegiatan<br>terbaru atau pengumuman<br>penting yang dapat diakses<br>langsung oleh pengguna.|Halaman<br>utama<br>dengan<br>visualisasi<br>ringkasan (_cards_dan<br>grafik) di bagian atas,<br>diikuti dengan daftar<br>kegiatan<br>atau<br>pengumuman terbaru<br>di bagian bawah.|
|---|---|---|---|
|Formulir<br>Pendaftaran<br>Online|Memfasilitasi<br>mahasiswa untuk<br>mendaftar<br>kegiatan<br>secara<br>cepat dan efisien.|Formulir dirancang dengan<br>tata letak sederhana dan<br>intuitif, mencakup input field<br>untuk nama, NIM, kontak,<br>dan<br>pilihan<br>kegiatan.<br>_Dropdown_menu atau radio<br>button<br>digunakan<br>untuk<br>mempermudah<br>mahasiswa<br>memilih kategori kegiatan,<br>sementara_progress indicator_<br>menunjukkan status pengisian<br>formulir. Validasi otomatis<br>memastikan<br>data<br>yang<br>dimasukkan benar sebelum<br>formulir dapat dikirimkan,<br>dengan notifikasi konfirmasi|Formulir berbasis web<br>dengan<br>validasi<br>otomatis,<br>konfirmasi<br>pendaftaran langsung<br>di layar, dan opsi cetak<br>atau<br>unduh<br>bukti<br>pendaftaran.|

|||yang langsung terlihat setelah<br>pengiriman.||
|---|---|---|---|
||Memberikan|Halaman kegiatan di desain<br>dengan<br>_layout_<br>yang<br>menampilkan daftar kegiatan<br>dalam bentuk_grid_atau_card_<br>_view_. Setiap card memuat<br>informasi<br>penting<br>seperti||
|Halaman<br>Kegiatan|daftar<br>kegiatan<br>yang<br>relevan<br>dengan deskripsi<br>singkat<br>untuk<br>masing-masing<br>kegiatan.|nama kegiatan, tanggal,dan<br>deskripsi kegiatan. Di bagian<br>atas halaman, tersedia filter<br>kategori, tanggal, atau tingkat<br>kegiatan<br>untuk<br>mempermudah<br>pencarian.<br>Tombol "Detail" pada setiap<br>_card_<br>memungkinkan<br>pengguna<br>untuk<br>melihat<br>informasi lebih lengkap atau<br>langsung mendaftar.|Halaman dengan daftar<br>kegiatan dalam bentuk<br>_card grid_, disertai opsi<br>_filter_di_sidebar_atau<br>bagian atas halaman.|
||Menampilkan|Halaman<br>statistik<br>menampilkan grafik_pie_,_bar_,<br>dan_line_yang interaktif untuk<br>menggambarkan data prestasi<br>mahasiswa<br>berdasarkan|Halaman<br>khusus<br>dengan<br>grafik|
|Halaman Statistik<br>dan Laporan|data<br>statistik<br>kegiatan, prestasi<br>mahasiswa,<br>dan<br>laporan visual.|waktu,<br>kategori,<br>atau<br>kegiatan.<br>Bagian<br>bawah<br>halaman menampilkan tabel<br>detail dengan kemampuan<br>_sorting_dan_filtering_untuk<br>analisis lebih mendalam. Di<br>sudut kanan atas, terdapat<br>tombol ekspor laporan dalam|interaktif di bagian atas<br>dan tabel data detail di<br>bagian<br>bawah,<br>dilengkapi fitur unduh<br>di kanan atas|

|||format PDF atau Excel agar<br>data mudah dibagikan atau<br>disimpan.||
|---|---|---|---|
|Notifikasi<br>dan<br>Pengumuman|Memberikan<br>informasi terbaru<br>tentang kegiatan,<br>status<br>pendaftaran, atau<br>perubahan jadwal<br>kepada pengguna.|Notifikasi dirancang dengan<br>ikon di sudut kanan atas<br>halaman<br>yang<br>dilengkapi<br>_badge_untuk menunjukkan<br>jumlah<br>notifikasi<br>baru.<br>_Dropdown_menu muncul saat<br>ikon<br>diklik,<br>menampilkan<br>daftar pengumuman terbaru.<br>Setiap<br>notifikasi<br>dapat<br>ditandai<br>sebagai<br>"sudah<br>dibaca,"<br>dengan<br>tautan<br>langsung<br>ke<br>detail<br>pengumuman. Sistem juga<br>mendukung push notification<br>untuk informasi penting yang<br>membutuhkan respons cepat.|Notifikasi<br>yang<br>muncul di pojok kanan<br>atas_dashboard_dengan<br>opsi untuk menandai<br>sebagai sudah dibaca,<br>atau tautan langsung ke<br>detail pengumuman.|

Setelah merumuskan kebutuhan berdasarkan indikator _Need Analysis_ pada _User Experience_ dan _User Interface_ , langkah berikutnya adalah menerapkan kebutuhan ini ke dalam fitur yang relevan bagi setiap _role_ pengguna. Dengan mempertimbangkan peran dan tanggung jawab masing-masing, fitur-fitur dalam sistem dirancang untuk memberikan akses yang sesuai dan mendukung pengalaman pengguna yang optimal. Berikut adalah penjelasan fitur yang dirancang khusus untuk setiap _role_ pengguna dalam sistem manajemen talenta mahasiswa.

- a. Dashboard Utama

   - Dashboard utama menyediakan berbagai informasi penting yang relevan dengan manajemen talenta mahasiswa. Hal ini dirancang untuk memberikan ringkasan informasi secara visual dan interaktif sehingga memudahkan setiap aktor dalam sistem untuk mengakses data sesuai kebutuhan mereka.

Fungsi:

- Menampilkan ringkasan data talenta mahasiswa, kegiatan aktif, dan statistik prestasi.

- Memberikan akses cepat ke informasi kegiatan terkini atau pengumuman penting.

- Memantau tren perkembangan data talenta melalui visualisasi grafik.

Kebutuhan Racangan:

Pada halaman _dashboard_ utama, semua aktor (Mahasiswa, PIC ManajemenTalenta, Admin, Dosen Pembimbing, dan kaprodi) dapat mengakses data yang relevan. Dashboard menampilkan:

1. _Summary Card_ s: Menampilkan jumlah total mahasiswa berbakat, jumlah

   - kegiatan aktif, dan total prestasi mahasiswa.

2. Grafik Visualisasi Data:

   - _Line chart_ untuk menunjukkan jumlah partisipasi mahasiswa pada berbagai kegiatan.

3. Daftar Pengumuman Terbaru: Menampilkan kegiatan terkini yang membutuhkan perhatian pengguna.

Implementasi:

Halaman awal dirancang dengan layout grid. Bagian atas menampilkan _summary cards_ , bagian tengah untuk grafik interaktif, dan bagian bawah untuk daftar pengumuman. Navigasi intuitif memudahkan pengguna untuk langsung menuju halaman detail sesuai kebutuhan mereka.

Akses Role:

   - Mahasiswa, untuk melihat pengumuman terbaru dan ringkasan kegiatan yang relevan.

   - PIC Manajemen Talenta, untuk memantau jumlah mahasiswa berbakat, kegiatan aktif, dan statistik prestasi.

   - Admin, untuk memastikan dashboard berjalan sesuai kebutuhan semua pihak.

   - Dosen Pembimbing, untuk memantau progres mahasiswa yang dibimbing.

- b. Halaman Data Talenta Mahasiswa

Halaman ini dirancang untuk mengelola data talenta mahasiswa secara sistematis, memungkinkan pengguna untuk mencari, memfilter, dan melihat informasi detail dari setiap mahasiswa.

Fungsi:

> ● Mengorganisir data talenta mahasiswa berbasis minat, bakat, dan prestasi.

- Mempermudah pencarian dan pengelolaan data melalui fitur filter.

- Memberikan informasi detail mengenai mahasiswa berbakat.

Kebutuhan Rancangan:

1. Tabel Interaktif dan Menarik

   - Menampilkan kolom seperti nama mahasiswa, NIM, jurusan, minat/bakat, dan riwayat prestasi.

   - Fitur _sorting_ untuk mengatur data berdasarkan kebutuhan pengguna.

2. Filter dan Pencarian

   - Filter berbasis kategori seperti jurusan, tingkat kegiatan, atau rentang waktu prestasi.

   - _Search bar_ untuk mencari nama mahasiswa tertentu.

3. Halaman Detail Mahasiswa:

   - Grafik perkembangan prestasi yang menunjukkan kontribusi mahasiswa pada kegiatan tertentu.

   - Riwayat kegiatan mahasiswa yang mencakup deskripsi singkat tentang partisipasi mereka.

Implementasi:

Tabel dengan kolom interaktif dan filter dropdown ditempatkan di bagian atas halaman. Tombol “ _Detail_ ” pada setiap baris tabel membawa pengguna ke halaman khusus dengan profil mahasiswa lengkap.

Akses Role:

   - PIC Manajemen Talenta: Mengelola data talenta mahasiswa dan meninjau detail mereka.

   - Admin: Memastikan data tersimpan dengan benar dan mendukung integrasi dengan laporan.

- c. Halaman Kegiatan

Halaman ini menyediakan informasi lengkap tentang kegiatan atau lomba yang sedang berlangsung, akan datang, atau telah selesai. Fungsi:

- Memberikan akses kepada mahasiswa untuk melihat daftar kegiatan dan mendaftar.

- Mempermudah PIC Manajemen Talenta dalam memantau status kegiatan dan peserta.

Kebutuhan Rancangan:

1. _List View_ dengan _Card Layout_

   - Menampilkan informasi seperti nama kegiatan, waktu pelaksanaan, dan status pendaftaran.

   - Ikon status untuk menunjukkan apakah pendaftaran masih terbuka atau sudah ditutup.

2. _Filter_ dan Sortir

   - Filter berdasarkan kategori kegiatan, tanggal pelaksanaan, atau tingkat kegiatan.

   - _Sorting_ untuk menampilkan kegiatan terbaru di bagian atas.

3. Halaman Detail Kegiatan:

   - Deskripsi kegiatan, daftar peserta, dan kontak penyelenggara.

   - Tombol “Daftar” untuk mahasiswa yang ingin bergabung.

Implementasi:

Halaman utama kegiatan berbentuk grid dengan card view untuk tiap kegiatan. Filter berada di bagian atas halaman, dan tombol “ _Detail_ ” pada setiap _card_ membuka halaman khusus untuk informasi lebih lanjut.

Akses Role:

- Mahasiswa: Melihat kegiatan yang relevan dan mendaftar kegiatan tersebut.

- PIC Manajemen Talenta: Menambahkan dan memantau kegiatan, serta mengevaluasi hasilnya.

# **2.3.2.** **_Design User Interface_**

Bagian ini akan memberikan gambaran rancangan _user interface_ pada sistem _dashboard_ . Rancangan ini dibentuk sesuai dengan kebutuhan analisis dari _User Interface_ maupun _User Experience_ yang telah dijelaskan sebelumnya dengan memperhatikan struktur  halaman dan penempatan elemen penting seperti grafik dan tabel. Adapun rancangan _User  Interface_ ini ditunjukkan pada gambar-gambar berikut.

# 1. Halaman _Landing Page_

<!-- Start of picture text -->
(9) rene<br>Pengumuman bs<br>ec<br>Sots catan peso ceunstn 2024 Imereti opportunity PSoraeMuttech-UW. Openingsurmarcanp Exchange<br>y }<br>Seles colon Festa GEMASTI2024 ImranoppetuntyPrSoraeMuttach-Ul. Opening Sunmatcamp xchange<br><!-- End of picture text -->

Gambar 2.10 Design UI - _Landing Page_

Sumber: Dokumen Pribadi

Pada bagian ini merupakan tampilan _user interface_ dari halaman _landing page_ . Halaman _landing page_ sendiri merupakan tampilan awal ketika pengguna pertama kali membuka _website_ manajemen talenta. Pada bagian ini terdapat _button login_ , berbagai informasi, pengumuman, dan buku panduan yang disediakan oleh 3 bidang (manajemen talenta, MBKM, dan _student exchange_ ).

2. Halaman _Login_

   - _a._ Halaman _Login - Beginning_

<!-- Start of picture text -->
ify:<br>(aySua 4] ) FakultasUPN VETERAN Ilmu JAKARTA Komputer<br>Login to your account<br>Username<br>= (ipl Password<br>Y “. ne<br>2a oetows<br>ie hE<br>G refin  ai} J Untukdahulu. Mitra,sign silahkanup  melakukan registrasi terlebih<br><!-- End of picture text -->

Gambar 2.11 Design UI - Halaman _Login_ - _Beginning_

Sumber: Dokumen Pribadi

Pada halaman _login_ , pengguna diminta untuk memasukkan _username_ dan _password_ mereka untuk mengakses sistem. Pada halaman _login_ , pengguna juga dapat menggunakan fitur “ingat akun saya” tujuannya supaya ketika kembali ingin mengakses website ini, pengguna tidak perlu mengetik _username_ dan _password_ kembali, dan kolom _username_ dan _password_ akan otomatis fulfilled dengan data yang sebelumnya pernah diisi. Setelah mengisi kolom yang tersedia, pengguna dapat mengklik tombol “ _Login_ ” untuk melanjutkan proses.

# _b._ Halaman _Login - Wrong Filled_

<!-- Start of picture text -->
i ‘<br>( Cay«eee 2] ) FakultasUPN VETERAN IImuJAKARTA Komputer<br>mes 4<br>Login to your account<br>Username<br>These credentials do not match our records.<br>¢ £ Password<br>i<br>& as * |<br>i<br>a fee<br>H! Had ol iA dahulu.Untuk Mitra, Sign silahkan up  melakukan registrasi terlebih<br><!-- End of picture text -->

Gambar 2.12 Design UI - Halaman _Login_ - _Wrong Filled_

Sumber: Dokumen Pribadi

Pada halaman _login_ , terdapat tampilan ketika pengguna salah mengisi username dan password yang tidak sesuai dengan yang ada pada _database._ Seperti yang dapat dilihat pada desain antarmuka diatas, terdapat penambahan kalimat “ _These credentials do not match our records_ ” atau dalam kata lain kredensial input tidak sesuai dan tidak terbaca pada database yang ada.

# 3. Halaman _Dashboard General_

<!-- Start of picture text -->
o) ea _SsometsetongEuactewsiaRouinasitngst<br>‘28 Dashboard Sitahkanla pith solohsotu program program yangyang} terse!<br>vom 2<br>® student Exchange Merdeka Belajar Kampus Merdeka (MBKM)<br>xPa Teri dor program MaKM Flagship, MakM Mandi (Ker Sama), MaKM Mandi<br>© Logout 2<br>‘eri dor program exchange‘Student ISMA Exchange PM,don Kerja Soma Universitas<br>fe clos oun Manajemen Talenta<br>Sings (an } Terr er progam pendotcan alent formosiloma dan pendstron mba<br><!-- End of picture text -->

Gambar 2.13 Design UI - Halaman _Dashboard_ General

Sumber: Dokumen Pribadi

Pada _user interface_ halaman _dashboard general_ merupakan tampilan ketika user pertama kali berhasil untuk _login_ . Pada bagian sebelah kanan berisi _highlight_ informasi yang ada pada sistem ini (yang mencangkup manajemen talenta, MBKM, _student exchange_ ). Sedangkan pada bagian sebelah kiri terdapat sidebar dari setiap bidang yang sedang penulis dan rekan-rekan penulis lakukan (manajemen talenta, MBKM, _student exchange_ ). Sehingga apabila di pilih, akan diarahkan ke website masing-masing. Selain itu di bagian bawah terdapat informasi terkait nama pengguna yang sudah login dan role mereka.

4. Halaman Pembinaan

   - a. Halaman Pembinaan - Admin

<!-- Start of picture text -->
a<br>fF¥ Seminar<br>© informasi umum<br>NO JUDUL SEMINAR POSTER DESKRIPS! BIDANG TANGGAL SEMINAR ‘AKI<br>ae - os ae<br> Kegiatan en Sarvuneomie<br>ea pein aneRa<br>8 Pendattaran Kegiatan‘4 — aoe ae<br>@ LPs kegiatan jee Sow tenes aroma<br>4 Kembali ee orton erowcen<br>a so ——<br>ise Cauca eet Soarongn tapers<br><!-- End of picture text -->

Gambar 2.14 Design UI - Halaman Pembinaan - Admin

Sumber: Dokumen Pribadi

Pada _user interface_ halaman seminar untuk admin, PIC manajemen talenta, dan Kaprodi menampilkan data-data seminar yang sudah di tambahkan. Tampilan data yang disajikan berupa tabel yang memuat nomor _list_ seminar, judul seminar, poster seminar, deskripsi seminar, bidang, tanggal seminar, dan aksi. Aksi ini berupa ikon antara edit dan hapus. Selain itu pada bagian atas terdapat fitur search dan filter dari postingan terlama dan terbaru. Selain itu pada halaman ini juga berisi eksport data dengan tipe excel dan juga tambah data.

- b. Halaman Pembinaan - Admin  - Edit Pembinaan

<!-- Start of picture text -->
.<br>;<br>——<br>i Dashboard<br>© intormasiumum<br>— :<br>Ge ie<br>reSSi ar er re ce oot<br>ee eS<br>et<br>Sa nas eeeaes meereeeee eevee<br>Seance oe co op ee oe oo<br>nostra<br>_ et amy ao mm ee<br>SeteSee eersteSoe eee<br>wenn<br>— Sener<br>=paano aranaepeeNeer omve  reerrem res emoeen<br><!-- End of picture text -->

Gambar 2.15 Design UI - Halaman Pembinaan - Admin - Edit Seminar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan edit data seminar. Pada bagian edit data seminar, dapat dilihat data yang sebelumnya sudah dimasukan tidak terhapus karena sudah tercatat pada database. Dan pada bagian bawah terdapat

- 2 opsi _button_ yang dipilih yaitu “simpan” dan “batal”.

- c. Halaman Pembinaan - Admin  - Simpan Edit Pembinaan

<!-- Start of picture text -->
; ‘simpan Informasi umum<br><!-- End of picture text -->

Gambar 2.16 Design UI - Halaman Pembinaan - Admin - Simpan Edit Pembinaan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan menekan button “simpan” pada data seminar yang sedang di ubah ( _edit)_ . Pada bagian simpan edit seminar ini, tampilan yang diberikan berupa _pop up_ untuk meyakinkan pengguna dengan hasil informasi seminar yang akan diubah. Jika pengguna menekan tombol “batal” maka akan tetap bertahan pada halaman _edit_ seminar, tetapi jika pengguna menekan tombol “simpan” maka data hasil _edit_ informasi yang baru akan disimpan dan menggantikan data seminar yang sebelumnya.

d. Halaman Pembinaan - Admin  - Hapus Pembinaan

<!-- Start of picture text -->
=<br>-=<br>_s =.<br>Hapus Data .<br>-<br>oo<br>a<br>a om<br>a<br><!-- End of picture text -->

Gambar 2.17 Design UI - Halaman Pembinaan - Admin - Hapus Pembinaan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan menekan button “ _delete_ ” salah satu data seminar yang sudah dimasukan. Pada bagian hapus data seminar, akan menampilkan _pop up_ untuk memastikan pengguna ingin menghapus data seminar tersebut atau tidak. Jika menekan tombol “tidak”, maka akan kembali ke halaman data seminar, tetapi jika menekan tombol “simpan” maka akan menghapus data seminar yang sudah dipilih.

- e. Halaman Pembinaan - Admin  - Tambah Data

<!-- Start of picture text -->
:<br>;<br>= 3<br>© intormasiumum<br>= :<br>‘% Kembali<br><!-- End of picture text -->

Gambar 2.18 Design UI - Halaman Pembinaan - Admin - Tambah Data

Sumber: Dokumen Pribadi

Pada gambar _user interface_ diatas, merupakan tampilan ketika pengguna memilih button “tambah data”. Sama seperti halaman edit seminar yang ada pada admin, pada bagian ini, pengguna diwajibkan untuk mengisi judul seminar, tanggal dilaksanakan nya seminar, bidang yang termasuk, gambar/poster seminar, dan deskripsi seminar.

- f. Halaman Pembinaan - Admin  - Tambah Data

<!-- Start of picture text -->
5 ‘simpan Seminar<br><!-- End of picture text -->

Gambar 2.19 Design UI - Halaman Pembinaan - Admin - Tambah Data

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan menekan button “simpan” pada data seminar yang ingin ditambah. Pada bagian simpan seminar ini, tampilan yang diberikan berupa _pop up_ untuk meyakinkan pengguna dengan hasil informasi seminar yang akan diubah. Jika pengguna menekan tombol “batal” maka akan tetap bertahan pada halaman _form_ tambah seminar, tetapi jika pengguna menekan tombol “simpan” maka data hasil tambah data seminar akan disimpan.

g. Halaman Pembinaan - Admin  - Gagal Tambah Data

<!-- Start of picture text -->
8<br>’<br>~<br>Ef Dashboard<br>BB rmoonee<br>© + stony 3<br>informasi Umum isco -<br>© Kegiatan<br>i endattaran Kegiatan<br>@ wskegiatan<br>4% Kembali<br>[ Logout<br>—- ® Gagal Membuat Seminar.Undefined x<br>a a Variable $Filename<br><!-- End of picture text -->

Gambar 2.20 Design UI - Halaman Pembinaan - Admin - Gagal Tambah Data Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna sudah menekan tombol “simpan” tetapi data tersebut tidak tersimpan. _User interface Mockup_ yang ada akan menampilkan “Gagal Membuat Seminar”.

- h. Halaman Pembinaan - Mahasiswa - List Pembinaan

<!-- Start of picture text -->
(@) Seminar<br>© srtormastumum<br>* xegiotan<br>Bi rendatorKegiaton _<br> vraKegitan<br>& Logout<br>yp Scam<br>i, Jee<br><!-- End of picture text -->

Gambar 2.21 Design UI - Halaman Pembinaan - Mahasiswa- _List_ Pembinaan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna membuka menu seminar. Dapat dilihat pada halaman ini terdiri dari list seminar yang sudah di masukan oleh admin atau PIC manajemen talenta, ataupun kaprodi. Selain itu terdapat fitur search. filter postingan (terbaru dan terlama) serta filter berdasarkan kategori seminar bidang talenta. Untuk membuka salah satu seminar yang ingin dibuka, pengguna cukup memilih salah satu _card view_ seminar yang ingin dilihat.

- i. Halaman Pembinaan - Mahasiswa - Detail Pembinaan

<!-- Start of picture text -->
(@)<br>-$37 Dornvoars SIE openPariisataneynraonGeotouismMedon interatonl Conerence (Ole) 2023 ByPotten<br>AFAPy<br>© teres uum : ap:<br>Destripsttapetn<br>enn) a<br><!-- End of picture text -->

Gambar 2.22 Design UI - Halaman Pembinaan - Mahasiswa- _Detail_ Pembinaan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna membuka salah satu seminar dari tampilan _card view_ yang tersedia. Dapat dilihat pada halaman ini terdiri dari poster seminar, kategori seminar berdasarkan rekap bidang talenta, judul seminar, deskripsi seminar, tanggal dilaksanakannya seminar, sampai ke pendaftaran seminar.

j. Halaman Pembinaan - Mahasiswa - Berhasil Daftar Pembinaan

<!-- Start of picture text -->
Berhasit<br>Kamu berhasil mendattar seminar!<br><!-- End of picture text -->

Gambar 2.23 Design UI - Halaman Pembinaan - Mahasiswa- Berhasil Daftar

Pembinaan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna berhasil melakukan pendaftaran seminar. Dapat dilihat pada _mockup user interface_ diatas, bahwa apabila pengguna melakukan pendaftaran, akan muncul popup berhasil pendaftaran. Selanjutnya pengguna dapat menekan _button_ “OK” untuk kembali ke detail seminar sebelumnya.

- k. Halaman Pembinaan - Mahasiswa - Button Berhasil Daftar Pembinaan

<!-- Start of picture text -->
.<br>:<br>7<br>Bi Dashboard BI operRoweegistration:“ Gsotouram nternational Contarene (Ge) 2023 By Pots<br>arr<br>© swformasiv GRD 0 putes 200<br>earner censapien<br>eindan kis Kept<br>Bavoterkegiaten =.<br>© atin rondcheren a<br>oncjemen eenta =<br>_ Preece<br><!-- End of picture text -->

Gambar 2.24 Design UI - Halaman Pembinaan - Mahasiswa- Berhasil Daftar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna sudah berhasil melakukan pendaftaran seminar pada detail seminar. Dapat dilihat pada _mockup user interface_ diatas, bahwa _button_ “Daftar Seminar” yang sudah ada pada tabel sebelumnya, ketika berhasil melakukan pendaftaran akan berubah menjadi “Sudah Daftar” dan _button_ tersebut sudah tidak bisa lagi di pilih.

5. Halaman Informasi Umum

   - a. Halaman Informasi Umum - Admin

<!-- Start of picture text -->
53 Informasi Umum<br>|<br>ee sever aa, a<br>ee = _<br>© kegiton Zz. —<— —-=<br>Riese<br>a aa<br>@ trsxapaton<br>_ . == ‘ an<br>© tego<br><!-- End of picture text -->

Gambar 2.25 Design UI - Halaman Informasi Umum - Admin

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin atau pic manajemen talenta membuka bagian ‘informasi umum”. Pada bagian ini terdapat _list_ informasi umum yang sudah dimasukan oleh pengguna. Informasi ini mencangkup nomor _list_ informasi, judul informasi, deskripsi, tanggal dimasukkannya informasi dan aksi edit ataupun hapus. Selain itu terdapat fitur _filter_ yang memuat _filter_ postingan terbaru dan terlama beserta tambah data.

b. Halaman Informasi Umum - Admin - Edit Informasi Umum

<!-- Start of picture text -->
;<br>;<br>——==<br>wt up yn i se i<br>‘© Kegiatan [pengembangan soft sills menjod! semakin penting dalam menyempumakon kuaitas lulusan universitas dl indonesia.<br>oo EE ete<br>SUS eee eee<br>SS eres<br>mogsnceee sme<br><!-- End of picture text -->

Gambar 2.26 Design UI - Halaman  Informasi Umum- Admin - Berhasil Daftar Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin atau pic manajemen talenta membuka bagian “ _edit_ ” yang ada pada bagian aksi. Pada halaman ini terdapat kolom judul informasi, deskripsi informasi, dan poster informasi yang sudah dibuatkan sebelumnya. Apabila pengguna akan menyimpan hasil _edit_ informasi umum yang ingin diubah, dapat menekan button “simpan”. Tetapi jika tidak, dapat menekan button “Batal” untuk kembali ke halaman informasi umum untuk admin dan pic manajemen talenta.

- c. Halaman Informasi Umum - Admin - _Popup_ Simpan Informasi Umum

<!-- Start of picture text -->
‘impaninformasi Umum<br><!-- End of picture text -->

Gambar 2.27 Design UI - Halaman  Informasi - Admin- _Popup_ Simpan Informasi

Sumber: Dokumen Pribadi

Seperti pada keterangan _user interface_ sebelumnya, pada bagian ini merupakan tampilan ketika admin/pic manajemen talenta melakukan button “simpan”. Akan ada _popup_ tampilan untuk memastikan user atas pilihan yang sedang mereka ingin pilih. Apabila pengguna akan menyimpan hasil _edit_ informasi umum yang ingin diubah, dapat menekan button “simpan”. Tetapi jika tidak, dapat menekan button “Batal” untuk kembali ke halaman informasi umum untuk admin dan pic manajemen talenta.

d. Halaman Informasi Umum - Admin - Berhasil Edit Informasi Umum

<!-- Start of picture text -->
e<br>- Informasi Umum<br>roningontocon SE<br>[©siermesiomun<br> reslaton . Mos<br>Barendenorankegloton<br>—— Moses ose<br>© Kombo wm ca Fee ead _ oo<br>& ween<br>© werent<br><!-- End of picture text -->

Gambar 2.28 Design UI - Halaman  Informasi - Admin- Berhasil _Edit_ Informasi

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan proses lanjutan dari tampilan ketika pengguna berhasil menyimpan perubahan dari data informasi umum. Dapat dilihat bahwa ada popup

kecil dibagian bawah kanan yang menampilkan informasi berhasil menyimpan perubahan informasi umum yang telah diubah.

- e. Halaman Informasi Umum - Admin - _Popup_ Hapus Data Informasi Umum

<!-- Start of picture text -->
--<br>opus Dota —s -<br>Se -<br>_<br>- -<br><!-- End of picture text -->

Gambar 2.29 Design UI - Halaman  Informasi - Admin- _Popup_ Hapus Data

# Informasi

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan halaman ketik admin/pic manajemen talenta ingin menghapus salah satu informasi umum yang sudah tersedia.  Pada _user interface_ ini menampilkan popup notifikasi. Apabila menekan “Batal” maka akan kembali kepada halaman informasi umum, tetapi jika menekan tombol “Simpan” maka data informasi umum akan terhapus.

- f. Halaman Informasi Umum - Admin - Berhasil Hapus Data Informasi Umum

<!-- Start of picture text -->
:<br>= Informasi Umum<br>[© verwestvon roargentec ~ EEws<br>Brennen kaon bet =m baad<br>1 temoot za = ==<br>cago<br>_ Ferrers<br><!-- End of picture text -->

Gambar 2.30 Design UI - Halaman Seminar - Admin- Berhasil Hapus Informasi

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan proses lanjutan dari tampilan ketika pengguna berhasil

menyimpan menghapus data informasi umum. Dapat dilihat bahwa ada popup kecil dibagian bawah kanan yang menampilkan informasi berhasil dihapus informasi umum yang telah diubah.

- g. Halaman Informasi Umum - Admin - Tambah Data Informasi Umum

<!-- Start of picture text -->
(9)<br>_—<br>Bi Pendattaran Kegiatan<br>—<br>—<br>aaa = wn<br><!-- End of picture text -->

Gambar 2.31 Design UI - Halaman  Informasi - Admin- Berhasil Hapus Informasi

Sumber: Dokumen Pribadi

Pada gambar _user interface_ diatas, merupakan tampilan ketika pengguna memilih button “tambah data”. Sama seperti halaman edit informasi umum yang ada pada admin, pada bagian ini, pengguna diwajibkan untuk mengisi judul informasi umum, gambar/poster informasi umum, dan deskripsi informasi umum.

- h. Halaman Informasi Umum - Mahasiswa - _List_ Informasi Umum

<!-- Start of picture text -->
(Q) Informasi Umum<br>BG bosnboara © etc une encarSaminor roriegontocos EE<br>_—<br>B Pendattar kegiatan<br>G Logout:<br>=<br><!-- End of picture text -->

Gambar 2.32 Design UI - Halaman  Informasi - Mahasiswa - _List_ Informasi

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa membuka menu informasi umum pada sidebar. Dapat dilihat pada halaman ini terdiri dari list informasi umum yang sudah dimasukkan oleh admin atau PIC manajemen talenta. Selain itu terdapat fitur search dan _filter_ postingan (terbaru dan terlama). Untuk membuka salah satu informasi umum yang ingin dibuka, pengguna cukup memilih salah satu _card view_ informasi umum yang ingin dilihat.

i. Halaman Informasi Umum - Mahasiswa - _Detail_ Informasi Umum

<!-- Start of picture text -->
e<br>J Pentingnya Program Pengembangan Soft Skill bagi Mahasiswa<br>o ‘Admin Bang Kerjasama dan Kemahasiswoan<br>5 vashboard<br>Na 2 BU<br>(oi) 2,= corr<br> Kegiatan<br>Ferccon tng bukon log! setodar tempat mempsteeh pengetanvon okadomisramun jugosofon@ untuk mangembongtan<br>Rete ‘Semoun"eteromplon peningnok doom(so)menyerpurnokonyong Husa! wegaiomauzanmenghodap. unerstosenamia a ndoreb.duno tera, Pogfam pengembangon sof sits Mana.<br>oho gases sotSing‘top{etasete menysenggaroxan dengan perteribangonuga xe! yang Suse meri trketeramptonpogiom pengembangon ig tet! interpersonal, don rnsormos stepemimpinan ils igs yang pengueoh hts dan perecahan kak hanya masaich marca Clendkaren dengana pete pangetann bagi westen<br>4 Kombat "eraopatanapan‘ahapantrp Tanopontahoponrogram Fengembangon toheponni selommerStjsankonprogramis pangembongandengan festsat tsGon menyeust manosawe operunt dapmenyapkonmencapatjondinya dalamsecon mengresk!ere  duneBorst<br>{caso pernbonasanorgeaprva<br>oe dents Kabnton nas<br>‘embertan‘etaptecutunonmahosswonave wawotonmencesommeritMoses eunkonnyadapattentangcanutonmosing-masing teuotan danMl elmanonUntukkorsutos.tu program seeppersona manors pengembanganpenioin Gt sotdon ilsBanko horustesdulpekomet denganYONGKes!dapat<br>Qo ec eratimenced<br>‘ttl‘ating manosizwa Wnts tebutunon,longtohPrgiom in dopet mencakup poltnonslonkenya aah marancang teterompion progtm ierparenotyang personal kusus Kepemampinandon sesus dengan dantebutuhen prove ohomaxing<br>‘yong metboton manos dalam inghungon smu!dune er<br><!-- End of picture text -->

Gambar 2.33 Design UI - Halaman  Informasi - Mahasiswa - _Detail_ Informasi

# Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa membuka salah satu informasi umum dari tampilan _card view_ yang tersedia. Dapat dilihat pada halaman ini terdiri dari poster informasi umum, judul informasi umum, deskripsi informasi umum, yang memasukan informasi umum tersebut kedalam sistem manajemen talenta, sampai  tanggal diunggah informasi umum.

6. Halaman Kegiatan

   - a. Halaman Kegiatan - Admin

<!-- Start of picture text -->
@<br>osq Kegiatan-<br>Ef Dashboard<br>SS Ser posinganteou » EE<br>© irr<br>post bran NO JUOULKESITAN POSTER ese IOAN BOANG KUOTAPESERTATANGGALTUTUP ANS!<br>3 Seminar D eemeieoneespen tegatnten Gectou Fae SperoseLegend Kecamatan ” vrownowa<br>Mi teneetaicn tosis a Pe] on oe o<br>@ wi kegiatan Secret<br>4% Kombat 5 to had<br>pin ans raed te Seles<br>=<br>aexia as [rirralln diam<br><!-- End of picture text -->

Gambar 2.34 Design UI - Halaman Kegiatan - Admin- Berhasil Hapus Informasi Sumber: Dokumen Pribadi

Pada _user interface_ halaman kegiatan untuk admin, menampilkan data-data seminar yang sudah di tambahkan. Tampilan data yang disajikan berupa tabel yang memuat nomor _list_ kegiatan, judul kegiatan, poster kegiatan, deskripsi kegiatan, bidang, tanggal tutup kegiatan, kuota peserta dan aksi. Aksi ini berupa ikon antara edit dan hapus. Selain itu pada bagian atas terdapat fitur search dan filter dari postingan terlama dan terbaru. Selain itu pada halaman ini juga berisi eksport data dengan tipe excel dan juga tambah data.

- b. Halaman Kegiatan - Admin - Edit Kegiatan

<!-- Start of picture text -->
.<br>;<br>Bh petosert Pe — ®<br>— ssoe wn Seepe pn eo<br>SEE SASS<br>S EE ee eore meee eer<br>een oem<br>: me oe ee<br>oe<br>to<br>— Se SS eresee<br>See Sess<br>— SoSo rerenemo ncme nen e nnes<br>=e<br><!-- End of picture text -->

Gambar 2.35 Design UI - Halaman Kegiatan - Admin- Edit Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan edit data kegiatan. Pada bagian edit data kegiatan, dapat dilihat data yang sebelumnya sudah dimasukan tidak terhapus karena sudah tercatat pada database. Dan pada bagian bawah terdapat

- 2 opsi button yang dipilih yaitu “simpan” dan “batal”.

- c. Halaman Kegiatan - Admin - _Popup_ Simpan Kegiatan

<!-- Start of picture text -->
5 =<br><!-- End of picture text -->

Gambar 2.36 Design UI - Halaman Kegiatan - Admin- _Popup_ Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan menekan button “simpan” pada data seminar yang sedang di ubah ( _edit)_ . Pada bagian simpan edit

kegiatan ini, tampilan yang diberikan berupa _pop up_ untuk meyakinkan pengguna dengan hasil informasi kegiatan yang akan diubah. Jika pengguna menekan tombol “batal” maka akan tetap bertahan pada halaman _edit_ kegiatan, tetapi jika pengguna menekan tombol “simpan” maka data hasil _edit_ kegiatan yang baru akan disimpan dan menggantikan data kegiatan yang sebelumnya.

- d. Halaman Kegiatan - Admin - Berhasil Ubah Kegiatan

<!-- Start of picture text -->
& Kegiatan<br>© srormasl uum No -woUXtoarIN —posTeR oes 80M oan RUOTAPESETATANGGALTUTUP AS!<br>Lf tien) . jw . ao<br>Bi rendttoranKegiatan so<br>@ Ps kegiatan | eae<br>© teomoat fee fe " an<br>— Pa seat —~<br>‘ 2<br>i G) Berhasil Mengubah Kegiatan x<br><!-- End of picture text -->

Gambar 2.37 Design UI - Halaman Kegiatan - Admin- Berhasil Ubah Kegiatan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan proses lanjutan dari tampilan ketika pengguna berhasil menyimpan perubahan dari data kegiatan. Dapat dilihat bahwa ada _popup_ kecil dibagian bawah kanan yang menampilkan informasi berhasil menyimpan perubahan kegiatan yang telah diubah.

- e. Halaman Kegiatan - Admin - _Popup_ Hapus Kegiatan

<!-- Start of picture text -->
5 :<br><!-- End of picture text -->

Gambar 2.38 Design UI - Halaman Kegiatan - Admin- _Popup_ Hapus Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin melakukan menekan button “ _delete_ ” salah satu data kegiatan yang sudah dimasukan. Pada bagian hapus data seminar, akan menampilkan _pop up_ untuk memastikan pengguna ingin menghapus data kegiatan tersebut atau tidak. Jika menekan tombol “tidak”, maka akan kembali ke halaman data kegiatan, tetapi jika menekan tombol “simpan” maka akan menghapus data kegiatan yang sudah dipilih.

- f. Halaman Kegiatan - Admin - Berhasil Hapus Kegiatan

<!-- Start of picture text -->
9<br>- Kegiatan<br>meee Ea<br>© intormasiumum No JUDULKEGIKTAN POSTER SKIS! mans’ [eiihio SSTA aceTea RE<br>aseaer) | mer cen jz ected cecomtan os 1)<br>I@ NpwaxogiatanvndaftaronreaencteleKogiaton =— Pay SSeeraee ‘ovat owes<br>—— i ....-<br>SETS Bi Berhasil Menghapus Kegiatan x<br><!-- End of picture text -->

Gambar 2.39 Design UI - Halaman Kegiatan - Admin- Berhasil Hapus Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan proses lanjutan dari tampilan ketika pengguna berhasil menyimpan menghapus data kegiatan. Dapat dilihat bahwa ada popup kecil dibagian bawah kanan yang menampilkan informasi berhasil dihapus informasi umum yang telah diubah.

- g. Halaman Kegiatan - Admin - Tambah Data Kegiatan

<!-- Start of picture text -->
.<br>;<br>©informasi Umum veto resort<br>— .<br>[3 seiner)<br><!-- End of picture text -->

Gambar 2.40 Design UI - Halaman Kegiatan - Admin- Tambah Data Kegiatan

Sumber: Dokumen Pribadi

Pada gambar _user interface_ diatas, merupakan tampilan ketika pengguna memilih button “tambah data”. Sama seperti halaman edit kegiatan yang ada pada admin, pada bagian ini, pengguna diwajibkan untuk mengisi judul kegiatan, gambar/poster kegiatan, tanggal penutupan kegiatan, bidang kegiatan, kuota peserta, tingkat kejuaraan kegiatan dan deskripsi kegiatan.

- h. Halaman Kegiatan - Admin - Gagal Tambah Data Kegiatan

<!-- Start of picture text -->
(Q) 7<br>33 oasnvoora . sen ®<br>© tntormasivmum<br>© Kegioton<br>i rendatoran Kegitan<br> waKesgiatan<br>#8 Kembatt<br>© togout<br>a isa Cauca . a ® GagalVariable Membuat $Filename Kegiatan.Undefined x<br><!-- End of picture text -->

Gambar 2.41 Design UI - Halaman Kegiatan - Admin- Gagal Tambah Data Kegiatan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna sudah menekan tombol “simpan” tetapi data tersebut tidak tersimpan. _User interface Mockup_ yang ada akan menampilkan “Gagal Membuat Kegiatan”.

- i. Halaman Kegiatan - Mahasiswa- _List_ Kegiatan

<!-- Start of picture text -->
(Q) Kegiatan<br>© informasi umum<br>3 Seminar<br>Bi PendattarKegiatan Comnmagrsinccasartmiematons.ED= OpuntiaGEE Catatonia= OpenGE» arte Catan= eat<br>@ waxegiatan<br>Kembali y y<br>4 2p 8 ¢<br>© Logout => = =<br>Comntegatecasarimiemetond= _OpenettiCatotonaten. OpenattenOnto at<br>35, Sea cinadin = SSS IEEE SSS CESS<br><!-- End of picture text -->

Gambar 2.42 Design UI - Halaman Kegiatan - Mahasiswa- _List_ Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika pengguna membuka halaman kegiatan. Dapat dilihat pada halaman ini terdiri dari list kegiatan yang sudah di masukan oleh admin atau PIC manajemen talenta, dan filter berdasarkan kegiatan dari setiap bidang talenta. Untuk membuka salah satu kegiatan yang ingin dibuka, pengguna cukup memilih salah satu _card view_ kegiatan yang ingin dilihat.

- j. Halaman Kegiatan - Mahasiswa- _Detail_ Kegiatan

<!-- Start of picture text -->
=~ 7 IIE open Registration: Geotouiam international Conerence(Aie) 2023 By Polite<br>Pariwisata Madan<br>85 Dosnboara PAR<br>© toformasivmum<br>34 seminr Doskrps Kegiatan<br>Batter kegictan =<br>2 stots Fendataran ioe<br>Monajomen Tolenta =x,<br>y<br><!-- End of picture text -->

Gambar 2.43 Design UI - Halaman Kegiatan - Mahasiswa- _Detail_ Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa membuka salah satu kegiatan dari tampilan _card view_ yang tersedia. Dapat dilihat pada halaman ini terdiri dari poster kegiatan, kategori kegiatan berdasarkan rekap bidang talenta, judul kegiatan, deskripsi kegiatan, tanggal dilaksanakannya kegiatan, sampai ke pendaftaran kegiatan.

# k. Halaman Kegiatan - Mahasiswa- _Form_ Pendaftaran Kegiatan

<!-- Start of picture text -->
Ca) Dattar Kegiatan > Form Pendattaran > Mengiim tamaran<br>Open Registration: Geotourism International Conference (Gtic) 2023<br>Hi Dashboard Politeknik Pariwisata Medan<br>© sors mum heed<br>Nema terakee<br>3¢> Seminar<br>—-=<br>[ Bostarresioton ee<br>@ status Pendaftaran ee)<br>obi don Kelbinan<br>oven Pendomng<br>Alosan Meng Kegiaton<br>ort Hos tt<br>Uploads<br>‘cuir Vow<br>—<br><!-- End of picture text -->

Gambar 2.44 Design UI - Halaman Kegiatan - Mahasiswa- _Form_ Kegiatan

Sumber: Dokumen Pribadi

Pada tampilan _user interface mockup_ diatas, merupakan tahapan lanjutan ketika mahasiswa memilih _button_ “Ikut Kegiatan”. Pada _form_ ini terdapat beberapa file yang kolom yang wajib diisi dan sudah _autofilled_ hanya berupa data yang ditampilkan dari database yang sudah ada. Seperti bagian yang _autofilled_ yaitu nama lengkap, tanggal lahir, email, semester, dan hobi serta keahlian. Selain itu beberapa kolom yang wajib diisi _manual_ oleh mahasiswa seperti dosen pendamping, alasan mengikuti kegiatan, KHS, dan CV.

l. Halaman Kegiatan - Mahasiswa- _Popup_ Simpan Pendaftaran Kegiatan

<!-- Start of picture text -->
-<br>aoeat<br>ies,<br>eecmnecme<br>__simpan Data<br>5<br>eS<br><!-- End of picture text -->

Gambar 2.45 Design UI - Halaman Kegiatan - Mahasiswa- _Popup_ Simpan Kegiatan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa melakukan menekan button “daftar” pada _form_ pendaftaran kegiatan yang mereka ingin ikuti. Pada bagian simpan data untuk mendaftar kegiatan ini, tampilan yang diberikan berupa _pop up_ untuk meyakinkan pengguna dengan hasil informasi kegiatan yang akan diubah. Jika pengguna menekan tombol “batal” maka akan tetap bertahan pada halaman _edit form_ pendaftaran, tetapi jika pengguna menekan tombol “simpan” maka data pendaftaran tadi akan disimpan.

# m. Halaman Kegiatan - Mahasiswa- Berhasil Ikut Kegiatan

<!-- Start of picture text -->
a Berhasit eto<br>amu bemnasimendattarkegiatan!<br>2 |<br><!-- End of picture text -->

Gambar 2.46 Design UI - Halaman Kegiatan - Mahasiswa- Berhasil Ikut Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa berhasil melakukan pendaftaran kegiatan. Dapat dilihat pada _mockup user interface_ diatas, bahwa apabila pengguna melakukan pendaftaran, akan muncul popup berhasil pendaftaran. Selanjutnya pengguna dapat menekan _button_ “OK” untuk kembali ke detail kegiatan sebelumnya.

# n. Halaman Kegiatan - Mahasiswa- Gagal Ikut Kegiatan

<!-- Start of picture text -->
Open Registration: Geotourism International Conference (tic) 2023<br>13 poshboors Politeknik Pariwisata Medan<br>+al Sominar neneseaion(acinus<br>© egiton ze aaa orgs 5<br>CD<br>@ stot Pendataron (seme<br>onojemen Telenta <r<br>coarser<br>sorontangna nen<br>peso<br>Kesalahan Lainnya. Undefined Variable x<br>aa ® ‘scv_nameMohon Melengkapi Input Atau Perikse:<br><!-- End of picture text -->

Gambar 2.47 Design UI - Halaman Kegiatan - Mahasiswa- Berhasil Ikut Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa sudah menekan tombol “simpan” tetapi data tersebut tidak tersimpan. _User interface Mockup_ yang ada akan menampilkan “Mohon Melengkapi Input Atau Periksa Kesalahan Lainnya” dengan tetap berada pada halaman _form_ pendaftaran.

- o. Halaman Kegiatan - Mahasiswa - Sudah Berhasil Ikut Kegiatan

<!-- Start of picture text -->
2)<br>te — PurwiscteOpen Registration: Maden  Geotourism International Conference (Gtic) 2023 By Politeknik<br>1 voshboord ara<br>© intormasiumum<br>roarent Deskript egatan<br>BiveierKepton =<br>@ statue Pedtaran a<br>Merafpaen Tbiae ——<br><!-- End of picture text -->

Gambar 2.48 Design UI - Halaman Kegiatan - Mahasiswa- Berhasil Ikut Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa sudah berhasil mendaftar kegiatan yang mereka pilih. Pada bagian _button_ “ikut kegiatan” akan berubah menjadi “sudah daftar” sehingga mahasiswa tidak bisa lagi untuk mendaftar kegiatan yang sama lebih dari satu kali.

7. Halaman Pendaftaran Kegiatan

# a. Halaman Pendaftaran Kegiatan - Admin - _List_ Kegiatan

<!-- Start of picture text -->
6<br>2J<br>Pendaftaran Kegiatan<br>85 Dashboard<br>xagioton seminar<br>@ informasi umum<br>3 Seminar NO NAMAKEGIATAN —JENSKEGIATAN TNOKATKEGIATAN. OEADUNE PENUTUPAN JUMLAH PINDAFTAR. KS!<br>I CoESED<br>‘& Kegiatan erreur}<br>ed<br>e=== Beramproca}<br>@ wskegiatan Sp<br>Bosrenoarrany<br>4% Kembali GEEDfeurrecura}<br>© Logout c=<br>cmp<br>four rocartaal<br>ten cneia Bist rowoarran}<br><!-- End of picture text -->

Gambar 2.49 Design UI - Halaman Pendaftaran Kegiatan - Admin- Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin membuka halaman pendaftaran kegiatan. Pendaftaran kegiatan sendiri merupakan riwayat ( _history_ ) dari admin yang sudah membuat _list_ kegiatan dan juga _list_ seminar. Pada halaman ini terbagi menjadi 2 bagian nantinya untuk admin ataupun pic manajemen talenta untuk membuka. Untuk bagian halaman kegiatan admin ataupun pic manajemen talenta dapat melihat nomor kegiatan pendaftaran kegiatan, nama kegiatan, jenis kegiatan, tingkat kegiatan, _deadline_ penutupan, jumlah pendaftar, dan juga aksi untuk melihat pendaftar kegiatan tersebut. Selain itu pada bagian atas tabel, terdapat fitur search untuk mencari kegiatan, _filter_ untuk mengurutkan kegiatan dari yang terlama ataupun terbaru, dan juga _export_ kegiatan. _Export_ sendiri terdiri dari _export_ kegiatan dan _export_ seminar.

<!-- Start of picture text -->
Re |e kk |= =O | tengere = i ® ©) SRR |m- ty P|»<br>Gove-+<br>2 inp tet nnn yo a —— ome :<br><!-- End of picture text -->

Gambar 2.50 Design UI - Halaman Pendaftaran Kegiatan - Admin- Hasil _Export_

# Sumber: Dokumen Pribadi

Pada tampilan _excel_ diatas, merupakan hasil _export_ dari pendaftaran kegiatan untuk _list_ kegiatan. Pada hasil _export_ tersebut, terdapat nama kegiatan, jenis kegiatan, tingkat kegiatan, _deadline_ penutupan, dan jumlah pendaftar.

b. Halaman Pendaftaran Kegiatan - Admin - Mahasiswa Pendaftar Kegiatan

<!-- Start of picture text -->
s<br>Le)<br>otk untuk mencar kegiton. evo » EE) GEE<br>Hy vashboara NO NM NAMA PRODI MNATGAKAT ALASANMENGIKUTIKEGIATAN UPLOADCV UROADKHS AKI<br>1 Ute unatrie ENED<br>° Informasi Umum UotFle unatrie END<br>3¢ Seminar otUotFle Fle unatrieunatrie ENDEND<br>fe kogicean Ut Fle unatrie END<br>@ wa Kegiatan —_ =<br>& Kombat ee)Lnatrie unatrie ED<br>oc)<br>_A<br>Lorrie unatrie ED<br>Lnarrie unarrie ERD<br><!-- End of picture text -->

Gambar 2.51 Design UI - Halaman Pendaftaran Kegiatan - Admin- Mahasiswa

# Pendaftar Kegiatan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin membuka salah satu kegiatan untuk melihat mahasiswa yang mendaftar kegiatan tersebut. Pada halaman ini berisi nomor _list_ urutan mahasiswa yang mendaftar, NIM mahasiswa, nama mahasiswa, prodi mahasiswa, minat bakat mahasiswa, alasan mengikuti kegiatan, _upload_ CV, _upload_ KHS, dan aksi untuk menerima mahasiswa atau tidak.

Selain itu pada bagian atas tabel seperti fitur search untuk mencari mahasiswa, _filter_ untuk mengurutkan mahasiswa yang mendaftar dari yang terlama ataupun terbaru, dan juga _export_ mahasiswa pendaftar.

<!-- Start of picture text -->
a ene Lon = |] B® @ mle kel<br>wee | rue le Be ke | = = = 5 Eletmgttecmnin «|e% + 2 a | Maton oman Go| San an emt |" Ua<br>Boe:rent 6 v sl oe sl me sl 3 “ =<br>2 wale17051021ho wa  CtRane c od ° ‘Matos « ‘oan Meng tepatna —Upond«CV Upaod" HS Satef<br>Rol Songs SSitemisfoman! ean ra Pi lt roe asie —atse Ped<br><!-- End of picture text -->

Gambar 2.52 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Export_ Mahasiswa

# Pendaftar Kegiatan Pending

Sumber: Dokumen Pribadi

Pada tampilan _excel_ diatas, merupakan hasil _export_ dari pendaftaran kegiatan untuk mahasiswa yang mendaftar kegiatan tetapi status kegiatan mereka masih _pending_ atau belum ada aksi untuk diterima. Pada hasil _export_ tersebut, terdapat nomor _list_ mahasiswa, NIM mahasiswa, nama mahasiswa, prodi mahasiswa, minat bakat mahasiswa, alasan mengikuti kegiatan yang sudah di _input_ mahasiswa untuk kegiatan yang mereka ikuti tersebut, _file_ upload CV yang sudah di _input_ mahasiswa untuk kegiatan yang mereka ikuti tersebut, _file_ upload KHS, dan status _pending_ .

c. Halaman Pendaftaran Kegiatan - Admin - Mahasiswa Pendaftar Kegiatan

<!-- Start of picture text -->
Nama<br>sa Claudia Roulina Silitonga<br>NM<br>2110812021<br>Program studi<br>1 Sistem informasi<br>Minat Bakat<br>Puisi, Silat<br>‘Alasan Mengikuti Kegiatan<br>Saya ingin Menang Dan Mendapatkan Kejuaraan. Selain itu Saya<br>Ingin Mendapatkan SkIPI Untuk Syarat Sidang<br><!-- End of picture text -->

Gambar 2.53 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Popup Detail_ Mahasiswa Mendaftar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin mencoba memilin _button_ “terima” untuk salah satu mahasiswa. Setelah memilih _button_ mahasiswa tersebut,

maka akan muncul _popup_ detail mahasiswa yang terdiri dari nama mahasiswa, NIM mahasiswa, program studi, minat bakat, alasan mengikuti kegiatan, dan pada bagian bawah terdapat _button_ “batal” dan “terima mahasiswa”. Apabila _button_ “batal”, maka akan kembali ke halaman _list_ mahasiswa yang mendaftar, tetapi apabila memilih _button_ “terima mahasiswa” maka mahasiswa tersebut berhasil untuk diterima pada kegiatan yang mereka pilih.

- d. Halaman Pendaftaran Kegiatan - Admin - Berhasil Menerima Mahasiswa

<!-- Start of picture text -->
Borhasil<br>Berhasil Menyimpan Seleksi<br><!-- End of picture text -->

Gambar 2.54 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Popup Detail_

Mahasiswa Mendaftar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin berhasil menerima mahasiswa untuk masuk ke tahap selanjutnya. Disini terdapat _popup_ notifikasi apabila berhasil menyimpan seleksi.

# e. Halaman Pendaftaran Kegiatan - Admin - Kegiatan Aksi Diterima

<!-- Start of picture text -->
e<br>‘<br>5 poshboora<br>Oat km ATEACAT AASANMENGRUTEEQATAN UROADEY UROHDIOS As<br>2 wsxegiton . ad<br>{& kombat “ baad<br><!-- End of picture text -->

Gambar 2.55 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Popup Detail_

# Mahasiswa Mendaftar

# Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan dari tahapan sebelumnya yaitu berhasil menerima mahasiswa untuk mengikuti kegiatan yang sudah mahasiswa pilih. Dapat dilihat pada kolom aksi dari yang awalnya “terima” berhasil berubah ketika admin atau pic manajemen talenta sudah menerima mahasiswa tersebut, dan berubah menjadi “diterima”.

<!-- Start of picture text -->
7 er ar = Ep |e Rm Ee by<br>a Pears 2 © Bloneyatenom poe | bard Vee<br>BCecoD<br>mn<br>a me oo Seeger<br>i musta nando Simenbiomes ent Uae trendoS ee<br>at i Sane na oie<br><!-- End of picture text -->

Gambar 2.56 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Export_ Mahasiswa

# Pendaftar Kegiatan Diterima

Sumber: Dokumen Pribadi

Pada tampilan _excel_ diatas, merupakan hasil _export_ dari pendaftaran kegiatan untuk mahasiswa yang mendaftar kegiatan tetapi status kegiatan mereka sudah diterima. Pada hasil _export_ tersebut, terdapat nomor _list_ mahasiswa, NIM mahasiswa, nama mahasiswa, prodi mahasiswa, minat bakat mahasiswa, alasan mengikuti kegiatan yang sudah di _input_ mahasiswa untuk kegiatan yang mereka ikuti

tersebut, _file_ upload CV yang sudah di _input_ mahasiswa untuk kegiatan yang mereka ikuti tersebut, _file_ upload KHS, dan status diterima.

f. Halaman Pendaftaran Kegiatan - Admin - _List_ Pendaftaran Seminar

<!-- Start of picture text -->
e<br>©)<br>Pendaftaran Kegiatan<br>85 Dashboard<br>© ntormasi Umum<br>3 Seminar NO NaWaxEoIATAN BOANG SOANAR —_TANOGALSEMINAR SUMAN PENDAFTAR KS!<br>‘© Kegiatan f° Bsus roarra rt )<br>LEB rendattaranxopiaton] BsusLJ resoartar)<br>Bsus roar)<br>@ waKegiat —<br>_ “ Biss roar)<br>ee Bsus roar)<br>cm<br>G Bist roar)<br>Logout Bsus mara)<br>Bsus mara)<br>Bsus rsmarar)<br><!-- End of picture text -->

Gambar 2.57 Design UI - Halaman Pendaftaran Kegiatan - Admin- Seminar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin membuka halaman pendaftaran kegiatan. Pendaftaran kegiatan sendiri merupakan riwayat ( _history_ ) dari admin yang sudah membuat _list_ kegiatan dan juga _list_ seminar. Pada halaman ini terbagi menjadi 2 bagian nantinya untuk admin ataupun pic manajemen talenta untuk membuka. Untuk bagian halaman seminar, admin ataupun pic manajemen talenta dapat melihat nomor kegiatan pendaftaran seminar, nama kegiatan seminar, bidang seminar, tanggal seminar diadakan, jumlah pendaftar, dan juga aksi untuk melihat pendaftar kegiatan tersebut. Selain itu pada bagian atas tabel, terdapat fitur search untuk mencari seminar, _filter_ untuk mengurutkan kegiatan dari yang terlama ataupun terbaru, dan juga _export_ kegiatan. _Export_ sendiri terdiri dari _export_ kegiatan dan _export_ seminar.

<!-- Start of picture text -->
\ [eer kk | = Re teem [omen | & >» | & & m/e<br>pan)wy [ery Vs Q-Be  Av)Ae | == = = =2/88sm BletepatcengaionE © |B. 8988+ ah | MeemnromattnaeseeSo | Supan|epe Fat | Oocme<br>Gee<br>i2fio}nonaepitanrs"iwwormnenornsACDebet. Jenn kegatn « Torani° mish Peder© le aa<br>3) ass nono 30Deembur 202 1<br>2 Gateotontat Sin 21 Dente 2038 :<br><!-- End of picture text -->

Gambar 2.58 Design UI - Halaman Pendaftaran Kegiatan - Admin- Hasil _Export_

Seminar

Sumber: Dokumen Pribadi

Pada tampilan _excel_ diatas, merupakan hasil _export_ dari pendaftaran kegiatan untuk _list_ seminar. Pada hasil _export_ tersebut, terdapat nomor _list_ seminar yang ada, nama kegiatan seminar, jenis kegiatan, tanggal diadakannya seminar, dan jumlah pendaftar.

g. Halaman Pendaftaran Kegiatan - Admin - _List_ Pendaftaran Seminar

<!-- Start of picture text -->
(2)<br>8 Dashboard No me awa moot ar Bacar TANGGAL DAFTAR<br>© informasi umum<br>}¢ Seminar<br> xegiatan<br>@ ws kegiatan<br> Kembati<br>&Logout<br>fea cieae<br><!-- End of picture text -->

Gambar 2.59 Design UI - Halaman Pendaftaran Kegiatan - Admin- Mahasiswa Pendaftar Seminar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika admin membuka salah satu seminar untuk melihat mahasiswa yang mendaftar seminar tersebut. Pada halaman ini berisi nomor _list_ urutan mahasiswa yang mendaftar, NIM mahasiswa, nama mahasiswa,

prodi mahasiswa, minat bakat mahasiswa, dan tanggal mahasiswa tersebut mendaftar.

Selain itu pada bagian atas tabel seperti fitur search untuk mencari mahasiswa, _filter_ untuk mengurutkan mahasiswa yang mendaftar dari yang terlama ataupun terbaru, dan juga _export_ mahasiswa pendaftar.

<!-- Start of picture text -->
Bs | ame ce Coe mm | ih @ Ble<br>fe 4 3 5S covung<br>Te m etpe me +) ly De Ae | = = = Ba Eocovunpaccenpniona ketongahia «| > %% + 1 ch | FemvomatnoeFomatsedogt2 capeGee| St<br>freon 6 fo 5 ct Ste con<br>Gores<br>a 5 Si | Wo<br>aifvo}ne4K Nee c Prod o Minot Botat £ “angalattarF s ju<br>2/1 2110512021 esa Cauda Routine Sitongs $1 Sistem nformasi esaGratis,Pui St ‘4 Desember2024<br><!-- End of picture text -->

Gambar 2.60 Design UI - Halaman Pendaftaran Kegiatan - Admin- _Export_ Mahasiswa Pendaftar Seminar

# Sumber: Dokumen Pribadi

Pada tampilan _excel_ diatas, merupakan hasil _export_ dari pendaftaran kegiatan untuk mahasiswa yang mendaftar seminar. Pada hasil _export_ tersebut, terdapat nomor _list_ mahasiswa, NIM mahasiswa, nama mahasiswa, prodi mahasiswa, minat bakat mahasiswa, dan tanggal mahasiswa mendaftar.

h. Halaman Pendaftaran Kegiatan - Mahasiswa - Kegiatan

<!-- Start of picture text -->
(QO)<br>33 bashboard econ » GE<br>© evormasivmum SELEKSI NASIONAL MASTER OF CEREMONY DENGAN BAHASA INGGRIS KEGIATAN ICIMCIS<br>set = p=» =» t——<br> Kegiaton ———<br>SELEKSI NASIONAL MASTER OF CEREMONYDENGAN BAHASA INGGRIS KEGIATAN ICIMCIS<br>@ wakegiatan<br>4% Kembali SSELEKSI NASIONAL MASTER OF CEREMONY DENGAN BAHASA INGGRIS KEGIATAN ICIMCIS<br>© tant =Dk= ==> @ oo<br>scine :<br><!-- End of picture text -->

Gambar 2.61 Design UI - Halaman Pendaftaran Kegiatan - Mahasiswa - Kegiatan Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa membuka halaman pendaftaran kegiatan. Pendaftaran kegiatan sendiri merupakan riwayat ( _history_ ) dari mahasiswa yang sudah mengikuti kegiatan dan juga seminar. Pada halaman ini terbagi menjadi 2 bagian nantinya untuk mahasiswa buka, disebelah kiri terdapat pendaftaran kegiatan dan sebelah kanan terdapat pendaftaran kegiatan seminar. Untuk bagian halaman pendaftaran kegiatan, terdapat riwayat kegiatan yang telah mahasiswa ikuti. Seperti nama kegiatan, bidang kegiatan, skala tingkatan kegiatan, _update_ terakhir pendaftaran, sampai kepada tahap status pendaftaran yang terdiri dari “registrasi”, “administrasi”, “dan lolos pendaftaran”. Apabila mahasiswa sudah diterima untuk ikut pendaftaran, maka tahapan selanjutnya adalah mengunggah dokumen untuk laporan kegiatan lomba”. Selain itu juga terdapat _filter_ untuk mengurutkan pendaftaran kegiatan antara “terlama” dan “terbaru”.

i. Halaman Pendaftaran Kegiatan - Mahasiswa - Seminar

<!-- Start of picture text -->
s<br>Le<br>Ny bashboard recor » GREED<br>no ane sens TANOGAL DAFTAR asi<br>@ informasi Umum | p a K unar ocran seminar<br>; cxxx=D<br>3 Seminar " cCx==IID<br>DB Pendattaranxegiatn} ; =<br>; cxxx=ZD<br>& Kembali<br>; cmxxx=D<br>& Logout<br><!-- End of picture text -->

Gambar 2.62 Design UI - Halaman Pendaftaran Kegiatan - Mahasiswa - Seminar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan ketika mahasiswa membuka halaman pendaftaran kegiatan. Pendaftaran kegiatan sendiri merupakan riwayat ( _history_ ) dari mahasiswa yang sudah mengikuti kegiatan dan juga seminar. Pada halaman ini terbagi menjadi 2 bagian nantinya untuk mahasiswa buka, disebelah kiri terdapat pendaftaran kegiatan dan sebelah kanan terdapat pendaftaran kegiatan seminar.

Untuk bagian halaman pendaftaran seminar, terdapat riwayat seminar yang telah mahasiswa ikuti. Seperti nomor _list_ seminar, nama kegiatan seminar, tanggal daftar seminar, dan aksi untuk melihat detail seminar.

- j. Halaman Pendaftaran Kegiatan - Mahasiswa - _Detail_ Seminar

<!-- Start of picture text -->
‘ a<br>é<br>a<br>3 vasnboara AAPARYaM PariwisataOpen Registration:Modon Geotourism international Conference (Gtic) 2023 By Politeknik<br>© stern ena GRD 0 5112004<br>CD =<br>Sistoaan froDeskripstearmKegiatan cro nro common nd remem meen<br>BB vattarkegiatan ie —<br>@ status Pendattaran {pm toe<br>Manajemen Talenta ocean<br>rector<br>z=<br>5-2 an Fn<br><!-- End of picture text -->

Gambar 2.63 Design UI - Halaman Pendaftaran Kegiatan - Mahasiswa - _Detail_

Seminar

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tahapan lanjutan apabila mahasiswa ingin menekan aksi “lihat _detail_ seminar”. Sama seperti _detail_ seminar pada _sidebar_ seminar bagian _detail seminar,_ berikut ini merupakan tampilan ketika pengguna membuka salah satu seminar dari tampilan _card view_ yang tersedia. Dapat dilihat pada halaman ini terdiri dari poster seminar, kategori seminar berdasarkan rekap bidang talenta, judul seminar, deskripsi seminar, tanggal dilaksanakannya seminar, sampai ke pendaftaran seminar.

8. Halaman _Dashboard_

   - a. Halaman _Dashboard_ - Admin

<!-- Start of picture text -->
.<br>v Data Talenta Mahasiswa<br>[85 cosnocrs a ‘TralieSudeh Pengiaian<br>© intormasi Umum<br>Bi Pendattaran kegiaten<br>+4 Kembali Cteng tiene<br>— Fetacboootionlolow<br>ee<br>CTC HAR<br>cm<br>vas corsa)<br>cD<br>cmp<br>cm<br>om<br>cm<br>c=<br>cmp<br>cm<br>c=<br>iva cxraal<br>cmp<br>comm<br>Biv cxrasl<br>Hiv crvsal<br><!-- End of picture text -->

Gambar 2.64 Design UI - Halaman _Dashboard_ - Admin-

# Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman _dashboard_ dari sisi admin ataupun pic manajemen talenta. Terdapat _pie chart_ terkait pengisian antara mahasiswa yang sudah mengisi dan belum. Selain itu terdapat _traffic_ sudah mengisi dari angkatan 2020-2023. Selain itu terdapat _detail pie chart_ dari setiap angkatan antara yang sudah mengisi dan yang belum. Dilanjutkan pada bagian bawah terdapat tabel dari rincian mahasiswa yang sudah mengisi data talenta. Rincian tersebut tediri dari nomor, NIM

mahasiswa, nama mahasiswa, prodi, minat bakat, jenis kelamin, angkatan, nomor telepon, email, dan aksi “lihat detail”.

- b. Halaman _Dashboard_ - Admin - _Detail_ Mahasiswa Data Talenta

Gambar 2.65 Design UI - Halaman _Dashboard_ - Admin- _Detail_ Mahasiswa Data

Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman lanjutan dari _dashboard_ dari sisi admin ataupun pic manajemen talenta. Apabila pengguna menekan aksi “lihat detail” dari mahasiswa yang sudah meng _input_ data talenta yang pengguna pilih, maka dapat dilihat nama lengkap, tanggal lahir, nomor telepon, email, username, bidang keahlian yang dimiliki, dan pengalaman kejuaraan.

- c. Halaman _Dashboard_ - Mahasiswa

<!-- Start of picture text -->
(0) Seameromen Cuetn nega oy i 0 Aa ete or ee a<br>omenere<br>{th Dashboard Kegiatan dan Kejuaraan<br>—= egies<br>_ Fetacdacctiqelelow<br>+ caston<br>recente<br>2 taproot benePer ghten<br>_==<br>—<br>C3Tnnm “ao na<br>— InformasiUmum Terbaru<br>Seminar Terbaru<br>f Sener<br>Kegiatan Terbaru<br>=e EE<br>Sa<br><!-- End of picture text -->

Gambar 2.66 Design UI - Halaman _Dashboard_ - Admin- _Detail_ Mahasiswa Data

# Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman _dashboard_ dari sisi mahasiswa. Terdapat _bar chart_ terkait bidang talenta yang sudah diisi mahasiswa, selain itu terdapat _detail pie chart_ dari setiap angkatan antara yang sudah mengisi dan yang belum. Dilanjutkan dengan beberapa _card view_ dari informasi umum terbaru, seminar terbaru, dan kegiatan terbaru yang bisa mahasiswa lihat dan daftar.

Dilanjutkan pada bagian bawah terdapat tabel dari rincian mahasiswa yang sudah mengisi data talenta. Rincian tersebut tediri dari nomor, NIM mahasiswa, nama mahasiswa, prodi, minat bakat, jenis kelamin, angkatan, nomor telepon, email, dan aksi “lihat detail”.

9. Halaman Data Talenta

   - a. Halaman Data Talenta - Mahasiswa - _Preview_

<!-- Start of picture text -->
¥ {toma atong tka coud Retin itnge! sich gto dla tb don ut capt aac beartepeten yong a2<br>ota rbot<br>© eformasiumum ()<br>Nome ergtop ‘a Cauda Roun Song<br>3¢ Seminar Tonggo th 27-08-2003<br>somo Tlepon conrzes67000<br>as mai _mosttziemananewauonacid<br>Bipatter kegiatan<br>@ status Pendattoran onion yong nba SohotainggrisToskwondo, Menyony<br>Manejemen Tatenta 2 heropon debt boneve ng tngtt nota<br><!-- End of picture text -->

Gambar 2.67 Design UI - Halaman Data Talenta - Mahasiswa- _Detail_ Mahasiswa Data Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman data talenta dari sisi mahasiswa. Terdapat _preview_ data mahasiswa baik yang _autofilled_ berdasarkan data dari _database_ . Dan juga beberapa inputan yang mahasiswa diwajibkan untuk isi. Untuk mengubah dan mengisi data tersebut, mahasiswa dapat menekan tombol “ubah”.

- b. Halaman Data Talenta - Mahasiswa - _Edit_ Talenta

<!-- Start of picture text -->
2 sume onan moma ene tna we sb en ont spre aaneega nan 9059<br>5 ooshooors Data Pribod<br>O rvermes!<br>Biootartepoton Z) fo<br>somone<br>‘mops<br>ott<br>Monojemen Cetin J<br>Co. J<br>—_—<br>( rs]<br>omen nae owns cater meas<br>ver secon seoowen tone.)<br>secant 0-200 enn vine<br>od sem rerccabenatoma git<br>rmrasonantanaean us) 3)<br><!-- End of picture text -->

Gambar 2.68 Design UI - Halaman Data Talenta - Mahasiswa- _Detail_ Mahasiswa Data Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman _edit_ data talenta dari sisi mahasiswa. Terdapat nama lengkap dan email yang sudah _autofilled_ , tanggal lahir nomor telepon, semester saat ini, dan keahlian yang hanya bisa diisi sebanyak 3 bidang. Selain itu pada bagian bawah berisi pengalaman kejuaraan yang pernah diikuti mahasiswa dan maksimal diisi sebanyak 3 pengalaman.

- c. Halaman Data Talenta - Mahasiswa - Isi Data Talenta

<!-- Start of picture text -->
= ‘tema ntng ns hm tin tenga! htt ng a tain us rt pat meen erga hgten yng do<br>5 boshboord Date Pribadi<br>© votermasi<br>Ba aterkegiatan Z) fa,<br>a<br>@ status Pendattaran (ereeteeemoutne serge<br>Tengen<br>08-7003<br>cjomen Ttenta se<br>(cumaoneSSOSCSCSOSSOSOSCSCSSSSSSS~Sd;<br>(awstoaiemonosenavenoeia }<br>(ewes<br>G vowsn ae ret ton nga O) ewwet ona ineneia<br>Q== Pitme ritesraitente OCOemrorate<br>votly O) t0c0 quran Yorn D800 quran tote (1-10 4u2)<br>co avon<br>Te (29-30) spe mobi agen O eer uno<br>snrpor rot saryeyo C.O. conntromvece crctrprt anoint<br>><br>rengatomontjergan (optro) Mors)<br><!-- End of picture text -->

Gambar 2.69 Design UI - Halaman  Data Talenta - Mahasiswa- Isi Data Talenta

# Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman data talenta dari sisi mahasiswa apabila mahasiswa mencoba mengisi data. Terdapat tampilan nama lengkap dan email yang sudah _autofilled_ , tanggal lahir nomor telepon, semester saat ini, dan keahlian yang hanya bisa diisi sebanyak 3 bidang. Selain itu pada bagian bawah berisi pengalaman kejuaraan yang pernah diikuti mahasiswa dan maksimal diisi sebanyak 3 pengalaman. Pengalaman kejuaraan ini masih belum bisa diisi oleh mahasiswa apabila mahasiswa belum menyimpan data talenta tersebut.

- d. Halaman Data Talenta - Mahasiswa - _Popup_ Simpan Data Talenta

<!-- Start of picture text -->
—<br>=<br>simpan<br>Data Telenta<br>oft<br>—— —<br><!-- End of picture text -->

Gambar 2.70 Design UI - Halaman  Data Talenta - Mahasiswa- Isi Data Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan apabila mahasiswa mencoba untuk menyimpan data talenta yang telah mereka isi. Akan muncul _popup_ notifikasi untuk menyimpan data talenta tersebut. Apabila menekan tumbol “batal” maka akan kembali ke halaman _edit_ data talenta, dan apabila menekan tombol “simpan” maka perubahan isi data talenta akan tersimpan.

- e. Halaman Data Talenta - Mahasiswa - Berhasil Mengubah Data Talenta

<!-- Start of picture text -->
—<br>-<br>erhasit<br>Mengubah Data Totenta.<br>——_——-<br><!-- End of picture text -->

Gambar 2.71 Design UI - Halaman  Data Talenta - Mahasiswa- Isi Data Talenta

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan apabila mahasiswa sudah menekan tombol “simpan” untuk menyimpan perubahan isi data talenta. Akan ada _popup_ yang memberitahu mahasiswa bahwa data talenta berhasil diubah dan bisa masuk ke tahapan selanjutnya yaitu mengisi _history_ kejuaraan.

- f. Halaman Data Talenta - Mahasiswa - Mengisi Data Kejuaraan Data Talenta

<!-- Start of picture text -->
———<br>Tambah Pengalaman Kejuaraan<br>iano<br>a<br>ee a a a<br>Se a oe<br>pepe farted pto<br>fepeatemtarenarnyraatepef e ar<br>earmaa<br>areasaii—W______1__1_ 1,<br>Sana ——<br>(Bette >)<br>Se<br><!-- End of picture text -->

Gambar 2.72 Design UI - Halaman  Data Talenta - Mahasiswa- Isi Data Kejuaraan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman dari sisi mahasiswa apabila mahasiswa mencoba mengisi data kejuaraan. Terdapat tampilan _field_ nama kejuaraan, deskripsi kejuaraan, lembaga pembuat perlombaan, jenis perlombaan, tanggal perlombaan, dan unggah bukti perlombaan. Selain itu terdapat tombol “batal” untuk kembali ke halaman edit data talenta dan juga tombol “simpan” untuk menyimpan data kejuaraan tersebut.

- g. Halaman Data Talenta - Mahasiswa - Berhasil Simpan Data Kejuaraan

<!-- Start of picture text -->
——<br>-<br>|<br>‘sorhasit<br>MengubahData Kejuaraan<br>—-<-<br><!-- End of picture text -->

Gambar 2.73 Design UI - Halaman  Data Talenta - Mahasiswa- Berhasil Simpan Data Kejuaraan

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan tampilan apabila mahasiswa sudah menekan tombol “simpan” untuk menyimpan perubahan isi data kejuaraan. Akan ada _popup_ yang memberitahu mahasiswa bahwa data kejuaraan berhasil disimpan dan dapat dilihat pada halaman data talenta bagian pengalaman kejuaraan.

h. Halaman Data Talenta - Mahasiswa - Data Talenta _Full Filled_

<!-- Start of picture text -->
a<br>;<br>ona<br>85 Dashboard<br>Bi ooterkegiatan v4 ‘a<br>—_—<br>1 status Pendattaran | Bo Clava Rout Satorga,<br>eee eee<br>(_mos2o2iemanosiowaupe.ocid )<br>Sone — a<br>—— suxPt © esienietwat O eenorate<br>—=<br>—<br>== es<br>5 aieSeenseeepcve<br>Saeerieeecee eeneeme<br>ees<br>=<br>SessSe=eepee yee eerie ee i<br>aSe=e tiers en 7<br><!-- End of picture text -->

Gambar 2.74 Design UI - Halaman  Data Talenta - Mahasiswa- Data Talenta _Fulfilled_

Sumber: Dokumen Pribadi

Pada bagian ini, merupakan halaman data talenta dari sisi mahasiswa apabila mahasiswa sudah mengisi data. Terdapat tampilan nama lengkap dan email yang sudah _autofilled_ , tanggal lahir nomor telepon, semester saat ini, dan keahlian yang hanya bisa diisi sebanyak 3 bidang dan semua sudah terisi. Selain itu pada bagian bawah berisi pengalaman kejuaraan yang pernah diikuti mahasiswa dan maksimal diisi sebanyak 3 pengalaman yang berhasil mahasiswa isi pada tahapan _user interface_ sebelumnya.

# **2.4. Rencana Pengujian Proyek**

Untuk memastikan bahwa sistem informasi pengajuan cuti akademik yang dikembangkan berfungsi dengan baik dan sesuai dengan kebutuhan pengguna, pengujian akan dilakukan menggunakan metode _Black Box Testing_ . _Black Box Testing_ adalah metode pengujian perangkat lunak yang berfokus pada fungsionalitas sistem dengan memeriksa apakah hasil yang diperoleh sudah sesuai dengan yang diharapkan. Pengujian dilakukan berdasarkan _test case_ yang mencakup berbagai skenario pengujian. Hasil dari pengujian ini akan digunakan untuk mengevaluasi apakah sistem telah berfungsi sesuai harapan atau masih memerlukan perbaikan. Berikut adalah tabel _Black Box Testing_ dengan _test case_ yang akan diujikan:

- _a. Blackbox Testing_ Akun Mahasiswa

Tabel 2.5. _Scenario Blackbox Testing_ Akun Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka<br>_Landing_<br>_Page_<br>_Website_|Berhasil membuka_Landing Page Website._|
|2|_Login_dengan_username_(NIM)<br>dan_password_|Masuk ke halaman_dashboard general._|
|3|Memilih<br>bagian<br>manajemen<br>talenta|Masuk ke halaman_dasboard_manajemen<br>talenta dan menampilkan_bar chart_bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke_dashboard general_|Berhasil kembali_dashboard_general yang<br>ada pada_sidebar._|
|5|Melakukan_Logout_|Berhasil melakukan_logout_dan kembali ke<br>_landing page._|
||Mengisi|Data Talenta|
|6|Mengecek data talenta|Menampilkan<br>_preview_<br>data<br>talenta<br>_autofilled database._|
|7|Isi data talenta|Mengisi data talenta mulai dari tanggal<br>lahir, nomor telepon, semester saat ini,<br>keahlian.|
|8|Tambah data kejuaraan belum<br>simpan data talenta|Tidak<br>berhasil<br>menambahkan<br>data<br>kejuaraan yang belum mengisi data talenta|

|9|Tambah data kejuaraan sudah<br>simpan data talenta|Mengisi data kejuaraan mulai dari nama<br>kejuaraan, deskirpsi kejuaraan, lembaga<br>pembuat kejuaraan, memilih salah satu<br>jenis perlombaan, tanggal perlombaan, dan<br>unggah sertifikat.|
|---|---|---|
|10|_Edit_data talenta|Mengedit data talenta mulai dari tanggal<br>lahir, nomor telepon, semester saat ini, dan<br>keahlian.|
|11|Edit kejuaraan yang sudah di<br>submit|Mengubah data kejuaraan mulai dari nama<br>kejuaraan, deskripsi kejuaraan, lembaga<br>pembuat kejuaraan, memilih salah satu<br>jenis perlombaan, tanggal perlombaan, dan<br>unggah sertifikat ulang.|
|12|Hapus data kejuaraan<br>Melihat Inf|Berhasil menghapus data kejuaraan yang<br>sudah di submit.<br>ormasi Umum|
|13|Mencari informasi umum|Berhasil mencari informasi umum yang<br>ingin dilihat.|
|14|_Filter_<br>postingan<br>dari<br>yang<br>terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru.|
|15|Membuka halaman informasi<br>umum|Berhasil masuk ke halaman informasi<br>umum dan melihat kumpulan-kumpulan<br>informasi yang tersedia dan melihat judul<br>informasi, poster informasi, dan tanggal<br>dimasukan nya informasi.|
|16|Melihat detail informasi umum|Berhasil melihat detail informasi umum<br>yang dipilih. Terdiri dari judul informasi,<br>role yang memasukan informasi, tanggal<br>diunggah informasi, poster informasi, dan<br>deskripsi informasi.|

Fitur Seminar

|17|Membuka halaman seminar|Berhasil<br>melihat<br>_search_,<br>terbaru,|membuka halaman seminar dan<br>list seminar yang tersedia, fitur<br>_filter_postingan terlama atau<br>dan filter semua bidang.|
|---|---|---|---|
|18|Mencari seminar yang dipilih|Berhasil<br>dilihat.|mencari seminar yang ingin|
|19|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil<br>yang ter|melakukan_filter_postingan baik<br>lama dan terbaru.|

|20|Mencari seminar berdasarkan<br>filter bidang talenta|Berhasil menampilkan data berdasarkan<br>filter bidang talenta.|
|---|---|---|
|21|Menampilkan detail seminar<br>yang dipilih|Berhasil menampilkan detail seminar yang<br>dipilih beserta seminar tersebut masuk ke<br>bidang talenta apa, judul seminar, tanggal<br>dilaksanakannya seminar, poster seminar,<br>deskripsi kegiatan, dan tombol ikut<br>seminar.|
|22|Berhasil ikut kegiatan<br>Fitur|Berhasil<br>mengikuti<br>kegiatan<br>setelah<br>menekan tombol ikut pendaftaran dan<br>menampilkan_popup_berhasil daftar.<br>Kegiatan|
|23|Membuka halaman kegiatan|Berhasil membuka halaman kegiatan dan<br>melihat_list_kegiatan yang tersedia beserta<br>skala tingkat kegiatan, bidang kegiatan,<br>dan_button_ikut kegiatan_fitur search_,_filter_<br>postingan terlama atau terbaru, dan_filter_<br>semua bidang.|
|24|Mencari kegiatan yang dipilih|Berhasil mencari kegiatan yang ingin<br>dilihat.|
|25|Melakukan_filter_postingan dari<br>yang terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru.|
|26|Mencari kegiatan berdasarkan<br>filter bidang talenta|Berhasil<br>menampilkan<br>data<br>kegiatan<br>berdasarkan_filter_bidang talenta.|
|27|Menampilkan detail kegiatan<br>yang dipilih|Berhasil menampilkan detail kegiatan yang<br>dipilih beserta kegiatan tersebut masuk ke<br>bidang talenta apa, judul kegiatan, tanggal<br>dilaksanakannya kegiatan, poster kegiatan,<br>deskripsi kegiatan, dan tombol ikut<br>kegiatan.|
|28|Daftar Kegiatan|Berhasil<br>mengisi<br>mengisi<br>dosen<br>pendamping, alasan mengikuti kegiatan,<br>mengunggah KHS, mengunggah CV pada<br>kolom yang disediakan.|
|29|Popup simpan data ikut kegiatan|Berhasil<br>menampilkan<br>_popup_<br>untuk<br>menyimpan data untuk ikut kegiatan.|
|30|Berhasil ikut kegiatan|Menampilkan<br>notifikasi<br>berhasil<br>mengikuti kegiatan dan kolom ikut<br>kegiatan berubah menjadi sudah daftar.|

|Fitur Pendaftaran Kegiatan bagian kegiatan|
|---|

|31|Membuka halaman pendaftaran<br>bagian kegiatan|Berhasil membuka halaman pendaftaran<br>kegiatan dan melihat kolom kegiatan dan<br>menampilkan_history_kegiatan yang diikuti<br>mulai dari judul kegiatan, bidang talenta<br>kegiatan, skala tingkat kegiatan,_update_<br>terakhir kegiatan,_filter_kegiatan, dan status<br>pendaftaran kegiatan yaitu registrasi,<br>administrasi, dan lolos pendaftaran.|
|---|---|---|
|32|Melakukan_filter_postingan dari<br>yang terlama dan terbaru bagian<br>kegiatan|Berhasil melakukan filter pendaftaran<br>kegiatan baik yang terlama dan terbaru<br>pada bagian kegiatan.|
|33|Membuka halaman pendaftaran<br>bagian seminar|Berhasil membuka halaman pendaftaran<br>kegiatan bagian seminar dan melihat<br>kolom seminar dan menampilkan_history_<br>seminar yang diikuti mulai dari judul<br>seminar, tanggal daftar, dan aksi untuk<br>melihat detail seminar.|
|34|Membuka_detail_seminar|Berhasil masuk ke halaman detail seminar<br>dari pendaftaran kegiatan.|

- _b. Blackbox Testing_ Akun Admin

Tabel 2.6. _Scenario Blackbox Testing_ Akun Admin

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka<br>_Landing_<br>_Page_<br>_Website_|Berhasil membuka_Landing Page Website._|
|2|_Login_dengan_username_dan<br>_password_|Masuk ke halaman_dashboard general._|
|3|Memilih<br>bagian<br>manajemen<br>talenta|Masuk ke halaman_dashboard_manajemen<br>talenta dan menampilkan bar chart bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke_dashboard general_|Berhasil kembali_dashboard_ _general_yang<br>ada pada_sidebar._|
|5|Melakukan_Logout_|Berhasil melakukan_logout_dan kembali ke<br>_landing page._|

||Fitur D|ashboard|
|---|---|---|
|6|Mengecek_report_pengisian data<br>talenta pada_pie chart_|Menampilkan report mahasiswa yang<br>sudah mengisi data talenta dengan pie<br>chart. Antara lain_pie chart_keseluruhan<br>sudah mengisi dan belum,_pie chart traffic_<br>pengisian perangkatan,_pie chart_pengisian<br>perangkatan (angkatan 2020 s/d 2023)<br>antara yang sudah mengisi dan belum<br>mengisi,_bar chart_bidang talenta, detail<br>mahasiswa yang sudah mengisi data<br>talenta, dan_search bar_untuk mencari<br>mahasiswa.|
|7|Lihat_Detail_Mahasiswa|Berhasil menampilkan data mahasiswa<br>mulai<br>dari<br>NIM<br>mahasiswa,<br>nama<br>mahasiswa, jenis kelamin mahasiswa,<br>prodi mahasiswa, angkatan mahasiswa,<br>nomor telepon, email, minat bakat, dan list<br>kejuaraan yang sudah mereka isi.|
|8|Mencari mahasiswa yang dipilih|Berhasil mencari mahasiswa yang ingin<br>dilihat.|

Fitur Informasi Umum

|9|Membuka halaman informasi<br>umum|Berhasil membuka halaman informasi<br>umum dan menampilkan_button_tambah<br>data,_search bar_,_filter_postingan terlama<br>atau terbaru, dan list informasi umum yang<br>sudah di tambahkan yang terdiri dari<br>nomor informasi, judul informasi, poster,<br>deskripsi informasi, tanggal dimasukan<br>informasi, dan aksi edit atau hapus.|
|---|---|---|
|10|Melakukan_filter_postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada informasi<br>umum.|
|11|Mencari informasi umum|Berhasil menampilkan data informasi<br>umum yang sudah dicari.|
|12|Tambah data informasi umum|Berhasil menambahkan judul informasi,<br>deskripsi informasi, dan poster informasi<br>umum baru.|
|13|_Edit_data informasi umum|Berhasil mengubah atau melakukan edit<br>judul informasi, deskripsi informasi, dan<br>poster informasi umum yang telah di<br>tambahkan sebelumnya.|

|14|Hapus data informasi umum|Berhasil menghapus informasi umum yang<br>telah di tambahkan sebelumna|
|---|---|---|
||Fitur|y.<br>Seminar|
|15|Membuka_sidebar_seminar|Berhasil membuka halaman seminar dan<br>menampilkan_button_tambah data,_search_<br>_bar_,_filter_postingan terlama atau terbaru,<br>dan list seminar yang sudah di tambahkan<br>yang terdiri dari nomor seminar, judul<br>seminar, poster, deskripsi seminar, bidang<br>seminar, tanggal dilaksanakannya seminar,<br>dan aksi edit atau hapus.|
|16|Melakukan_filter_postingan dari<br>yang terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru pada seminar.|
|17|Mencari seminar|Berhasil menampilkan data seminar yang<br>sudah dicari.|
|18|Tambah data seminar|Berhasil menambahkan judul seminar,<br>deskripsi seminar, bidang seminar tanggal<br>dilaksanakannya seminar, dan poster<br>seminar.|
|19|Edit data seminar|Berhasil mengubah atau melakukan_edit_<br>judul seminar, deskripsi seminar, dan<br>poster seminar yang telah di tambahkan<br>sebelumnya.|
|20|Hapus data seminar|Berhasil menghapus seminar yang telah di<br>tambahkan sebelumnya.|
||Fitur|<br>Kegiatan|
|21|Membuka_sidebar_kegiatan|Berhasil membuka halaman kegiatan dan<br>menampilkan_button_tambah data,_search_<br>_bar_,_filter_postingan terlama atau terbaru,<br>dan list kegiatan yang sudah di tambahkan<br>yang terdiri dari nomor kegiatan, judul<br>kegiatan, poster, deskripsi kegiatan, bidang<br>kegiatan, tingkat skala kegiatan, kuota<br>peserta, tanggal ditutup kegiatan, dan aksi<br>_edit_atau hapus.|
|22|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru pada kegiatan.|
|23|Mencari kegiatan|Berhasil menampilkan data kegiatan yang<br>sudah dicari.|

|24|Tambah data kegiatan|Berhasil menambahkan judul kegiatan,<br>poster, deskripsi kegiatan, bidang kegiatan,<br>tingkat skala kegiatan, kuota peserta,<br>tanggal ditutup kegiatan.|
|---|---|---|
|25|_Edit_data kegiatan|Berhasil mengubah atau melakukan  judul<br>kegiatan, poster, deskripsi kegiatan, bidang<br>kegiatan, tingkat skala kegiatan, kuota<br>peserta, tanggal ditutup kegiatan yang telah<br>di tambahkan sebelumnya.|
|26|Hapus data kegiatan<br>Fitur Pendaftaran|Berhasil menghapus kegiatan yang telah di<br>tambahkan sebelumnya.<br>Kegiatan pada kegiatan|
|27|Menampilkan<br>pendaftaran<br>kegiatan bagian kegiatan|Berhasil menampilkan_search bar_, filter<br>postingan terlama atau terbaru,_export_<br>kegiatan, tabel_history_kegiatan mulai dari<br>nomor kegiatan, nama kegiatan, jenis<br>kegiatan,<br>tingkat<br>kegiatan,<br>_deadline_<br>penutupan, jumlah pendaftar, dan aksi<br>untuk melihat pendaftar|
|28|Melakukan_filter_postingan dari<br>yang terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian kegiatan|
|29|Mencari kegiatan|Berhasil menampilkan data kegiatan yang<br>sudah dicari|
|30|_Export_Kegiatan|Berhasil melakukan_export_dalam bentuk<br>excel yang menampilkan nomor kegiatan,<br>nama kegiatan, jenis kegiatan, tingkat<br>kegiatan,_deadline_penutupan, dan jumlah<br>pendaftar.|
|31|Detail pendaftar kegiatan yang<br>dipilih|Berhasil menampilkan nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, alasan<br>mengikuti<br>kegiatan<br>yang<br>diisi<br>oleh<br>pendaftar, CV pendaftar, KHS pendaftar,<br>aksi untuk menerima pendaftar,_filter_<br>pendaftar dari terlama dan terbaru, sampai<br>_export_pendaftar kegiatan.|
|32|Lihat_upload_CV|Berhasil membuka_file_yang telah diunggah<br>mahasiswa untuk mendaftar kegiatan yang<br>dipilih.|

|33|Lihat_upload_KHS|Berhasil membuka file KHS yang telah<br>diunggah mahasiswa untuk mendaftar<br>kegiatan yang dipilih.|
|---|---|---|
|34|_Export_Pendaftar|Berhasil melakukan export dalam bentuk<br>excel yang terdiri dari nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, alasan<br>mengikuti<br>kegiatan<br>yang<br>diisi<br>oleh<br>pendaftar, CV pendaftar, KHS pendaftar,<br>dan status pendaftaran antara pending dan<br>diterima..|
|35|Terima Mahasiswa|Berhasil menampilkan popup notifikasi<br>detail mahasiswa pendaftar yang terdiri<br>dari nama, NIM, program studi, alasan<br>mengikuti kegiatan, dan terima mahasiswa|
|36|Lihat_file_CV pada_excel_|Berhasil membuka_file_cv pada_excel_yang<br>telah di_export_|
|37|Lihat_file_KHS pada_excel_<br>Fitur Pendaftaran|Berhasil membuka_file_khs pada_excel_yang<br>telah di export<br>Kegiatan pada seminar|
|38|Menampilkan<br>pendaftaran<br>kegiatan bagian seminar|Berhasil menampilkan_search bar_,_filter_<br>postingan terlama atau terbaru,_export_<br>seminar, tabel_history_seminar mulai dari<br>nomor seminar, nama seminar, bidang<br>seminar,<br>tanggal<br>seminar,<br>jumlah<br>pendaftar, dan aksi untuk melihat pendaftar|
|39|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan_filter_postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian seminar.|
|40|Mencari seminar|Berhasil menampilkan data seminar yang<br>sudah dicari|
|41|Export seminar|Berhasil melakukan_export_dalam bentuk<br>excel yang menampilkan nomor seminar,<br>nama seminar, jenis kegiatan, tanggal<br>seminar, dan jumlah pendaftar.|
|42|Detail pendaftar seminar yang<br>dipilih|Berhasil menampilkan nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, tanggal<br>daftar seminar filter pendaftar dari terlama<br>dan<br>terbaru,<br>sampai<br>kepada<br>export<br>pendaftar seminar.|

|43|_Export_Pendaftar|Berhasil melakukan_export_dalam bentuk<br>excel yang terdiri dari nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, dan<br>tanggal daftar mahasiswa pada kegiatan<br>yang mereka pilih.|
|---|---|---|

_c. Blackbox Testing_ Akun PIC Manajemen Talenta

Tabel 2.7. _Scenario Blackbox Testing_ Akun PIC Manajemen Talenta

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka_Landing Page_<br>_Website_|Berhasil membuka_Landing Page Website._|
|2|_Login_dengan_username_dan<br>_password_|Masuk ke halaman_dashboard general._|
|3|Memilih bagian manajemen<br>talenta|Masuk ke halaman_dasboard_manajemen<br>talenta dan menampilkan bar chart bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke_dashboard general_|Berhasil kembali_dashboard general_yang<br>ada pada_sidebar_.|
|5|Melakukan_Logout_|Berhasil melakukan_logout_dan kembali ke<br>_landing page_.|
||Fitur|Dashboard|
|6|Mengecek_report_pengisian data<br>talenta pada_pie chart_|Menampilkan_report_mahasiswa yang<br>sudah mengisi data talenta dengan_pie_<br>_chart_. Antara lain pie chart keseluruhan<br>sudah mengisi dan belum, pie chart traffic<br>pengisian perangkatan,_pie chart_pengisian<br>perangkatan (angkatan 2020 s/d 2023)<br>antara yang sudah mengisi dan belum<br>mengisi,_bar chart_bidang talenta, detail<br>mahasiswa yang sudah mengisi data<br>talenta, dan search bar untuk mencari<br>mahasiswa.|
|7|Lihat Detail Mahasiswa|Berhasil menampilkan data mahasiswa<br>mulai<br>dari<br>NIM<br>mahasiswa,<br>nama<br>mahasiswa, jenis kelamin mahasiswa,<br>prodi mahasiswa, angkatan mahasiswa,|

|||nomor telepon, email, minat bakat, dan list<br>kejuaraan yang sudah mereka isi.|
|---|---|---|
|8|Mencari mahasiswa yang dipilih<br>Fitur Info|Berhasil mencari mahasiswa yang ingin<br>dilihat.<br>rmasi Umum|
|9|Membuka halaman informasi<br>umum|Berhasil membuka halaman informasi<br>umum dan menampilkan button tambah<br>data, search bar, filter  postingan terlama<br>atau terbaru, dan list informasi umum yang<br>sudah di tambahkan yang terdiri dari<br>nomor informasi, judul informasi, poster,<br>deskripsi informasi, tanggal dimasukan<br>informasi, dan aksi edit atau hapus|
|10|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada informasi<br>umum|
|11|Mencari informasi umum|Berhasil menampilkan data informasi<br>umum yang sudah dicari|
|12|Tambah data informasi umum|Berhasil menambahkan judul informasi,<br>deskripsi informasi, dan poster informasi<br>umum baru|
|13|Edit data informasi umum|Berhasil mengubah atau melakukan edit<br>judul informasi, deskripsi informasi, dan<br>poster informasi umum yang telah di<br>tambahkan sebelumnya|
|14|Hapus data informasi umum|Berhasil menghapus informasi umum yang<br>telah di tambahkan sebelumnya|
||Fitur|<br>Seminar|
|15|Membuka sidebar seminar|Berhasil membuka halaman seminar dan<br>menampilkan button tambah data, search<br>bar, filter  postingan terlama atau terbaru,<br>dan list seminar yang sudah di tambahkan<br>yang terdiri dari nomor seminar, judul<br>seminar, poster, deskripsi seminar, bidang<br>seminar, tanggal dilaksanakannya seminar,<br>dan aksi edit atau hapus|
|16|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada seminar|

|17|Mencari seminar|Berhasil menampilkan data seminar yang<br>sudah dicari|
|---|---|---|
|18|Tambah data seminar|Berhasil menambahkan judul seminar,<br>deskripsi seminar, bidang seminar tanggal<br>dilaksanakannya seminar, dan poster<br>seminar|
|19|Edit data seminar|Berhasil mengubah atau melakukan edit<br>judul seminar, deskripsi seminar, dan<br>poster seminar yang telah di tambahkan<br>sebelumnya|
|20|Hapus data seminar|Berhasil menghapus seminar yang telah di<br>tambahkan sebelumnya|
||Fitur|Kegiatan|
|21|Membuka sidebar kegiatan|Berhasil membuka halaman kegiatan dan<br>menampilkan button tambah data, search<br>bar, filter  postingan terlama atau terbaru,<br>dan list kegiatan yang sudah di tambahkan<br>yang terdiri dari nomor kegiatan, judul<br>kegiatan, poster, deskripsi kegiatan, bidang<br>kegiatan, tingkat skala kegiatan, kuota<br>peserta, tanggal ditutup kegiatan, dan aksi<br>edit atau hapus|
|22|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada kegiatan|
|23|Mencari kegiatan|Berhasil menampilkan data kegiatan yang<br>sudah dicari|
|24|Tambah data kegiatan|Berhasil menambahkan judul kegiatan,<br>poster, deskripsi kegiatan, bidang kegiatan,<br>tingkat skala kegiatan, kuota peserta,<br>tanggal ditutup kegiatan|
|25|Edit data kegiatan|Berhasil mengubah atau melakukan  judul<br>kegiatan, poster, deskripsi kegiatan, bidang<br>kegiatan, tingkat skala kegiatan, kuota<br>peserta, tanggal ditutup kegiatan<br>yang telah di tambahkan sebelumnya|
|26|Hapus data kegiatan|Berhasil menghapus kegiatanyang telah di<br>tambahkan sebelumnya|
||Fitur Pendaftaran|Kegiatan pada kegiatan|

|27|Menampilkan<br>pendaftaran<br>kegiatan bagian kegiatan|Berhasil menampilkan search bar, filter<br>postingan terlama atau terbaru, export<br>kegiatan, tabel history kegiatan mulai dari<br>nomor kegiatan, nama kegiatan, jenis<br>kegiatan,<br>tingkat<br>kegiatan,<br>deadline<br>penutupan, jumlah pendaftar, dan aksi<br>untuk melihat pendaftar|
|---|---|---|
|28|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian kegiatan|
|29|Mencari kegiatan|Berhasil menampilkan data kegiatan yang<br>sudah dicari|
|30|Export Kegiatan|Berhasil melakukan export dalam bentuk<br>excel yang menampilkan nomor kegiatan,<br>nama kegiatan, jenis kegiatan, tingkat<br>kegiatan, deadline penutupan, dan jumlah<br>pendaftar.|
|31|Detail pendaftar kegiatan yang<br>dipilih|Berhasil menampilkan nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, alasan<br>mengikuti<br>kegiatan<br>yang<br>diisi<br>oleh<br>pendaftar, CV pendaftar, KHS pendaftar,<br>aksi untuk menerima pendaftar, filter<br>pendaftar dari terlama dan terbaru, sampai<br>export pendaftar kegiatan|
|32|Lihat upload CV|Berhasil<br>membuka<br>file<br>yang<br>telah<br>diunggah mahasiswa untuk mendaftar<br>kegiatan yang dipilih|
|33|Lihat upload KHS|Berhasil membuka file KHS yang telah<br>diunggah mahasiswa untuk mendaftar<br>kegiatan yang dipilih|
|34|Export Pendaftar|Berhasil melakukan export dalam bentuk<br>excel yang terdiri dari nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, alasan<br>mengikuti<br>kegiatan<br>yang<br>diisi<br>oleh<br>pendaftar, CV pendaftar, KHS pendaftar,<br>dan status pendaftaran antara pending dan<br>diterima.|
|35|Terima Mahasiswa|Berhasil menampilkan popup notifikasi<br>detail mahasiswa pendaftar yang terdiri<br>dari nama, NIM, program studi, alasan<br>mengikuti kegiatan, dan terima mahasiswa|

|36|Lihat file CV pada excel|Berhasil membuka file cv pada excel yang<br>telah di export|
|---|---|---|
|37|Lihat file KHS pada excel<br>Fitur Pendaftaran|Berhasil membuka file khs pada excel yang<br>telah di export<br>Kegiatan pada seminar|
|38|Menampilkan<br>pendaftaran<br>kegiatan bagian seminar|Berhasil menampilkan search bar, filter<br>postingan terlama atau terbaru, export<br>seminar, tabel history seminar mulai dari<br>nomor seminar, nama seminar, bidang<br>seminar,<br>tanggal<br>seminar,<br>jumlah<br>pendaftar, dan aksi untuk melihat pendaftar|
|39|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian seminar|
|40|Mencari seminar|Berhasil menampilkan data seminaryang<br>sudah dicari|
|41|Export seminar|Berhasil melakukan export dalam bentuk<br>excel yang menampilkan nomor seminar,<br>nama seminar, jenis kegiatan, tanggal<br>seminar, dan jumlah pendaftar.|
|42|Detail pendaftar seminar yang<br>dipilih|Berhasil menampilkan nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, tanggal<br>daftar seminar filter pendaftar dari terlama<br>dan<br>terbaru,<br>sampai<br>kepada<br>export<br>pendaftar seminar|
|43|Export Pendaftar|Berhasil melakukan export dalam bentuk<br>excel yang terdiri dari nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, dan<br>tanggal daftar mahasiswa pada kegiatan<br>yang mereka pilih.|

# _d. Blackbox Testing_ Akun Kaprodi

Tabel 2.8. _Scenario Blackbox Testing_ Akun Kaprodi

|**No**||**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|---|
|1|Membuka<br>_Website_|_Landing_<br>_Page_|Berhasil membuka_Landing Page Website_|

|2|_Login_dengan_username_dan<br>_password_|Masuk ke halaman_dashboard general_|
|---|---|---|
|3|Memilih<br>bagian<br>manajemen<br>talenta|Masuk ke halaman_dasboard_manajemen<br>talenta dan menampilkan bar chart bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke dashboard general|Berhasil kembali dashboard general yang<br>ada pada sidebar|
|5|Melakukan Logout|Berhasil melakukan logout dan kembali ke<br>landing page|
||Fitur|<br>Seminar|
|6|Menampilkan<br>pendaftaran<br>kegiatan bagian seminar|Berhasil menampilkan search bar, filter<br>postingan terlama atau terbaru, export<br>seminar, tabel history seminar mulai dari<br>nomor seminar, nama seminar, bidang<br>seminar,<br>tanggal<br>seminar,<br>jumlah<br>pendaftar, dan aksi untuk melihat pendaftar|
|7|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian seminar|
|8|Mencari seminar|Berhasil menampilkan data seminaryang<br>sudah dicari|
|9|Export seminar|Berhasil melakukan export dalam bentuk<br>excel yang menampilkan nomor seminar,<br>nama seminar, jenis kegiatan, tanggal<br>seminar, dan jumlah pendaftar.|
|10|Detail pendaftar seminar yang<br>dipilih|Berhasil menampilkan nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, tanggal<br>daftar seminar filter pendaftar dari terlama<br>dan<br>terbaru,<br>sampai<br>kepada<br>export<br>pendaftar seminar|
|11|Export Pendaftar|Berhasil melakukan export dalam bentuk<br>excel yang terdiri dari nomor pendaftar,<br>NIM pendaftar, nama pendaftar, prodi<br>pendaftar, minat bakat pendaftar, dan<br>tanggal daftar mahasiswa pada kegiatan<br>yang mereka pilih.|

||Fitur Info|rmasi Umum|
|---|---|---|
|12|Membuka halaman informasi<br>umum|Berhasil membuka halaman informasi<br>umum dan menampilkan button tambah<br>data, search bar, filter  postingan terlama<br>atau terbaru, dan list informasi umum yang<br>sudah di tambahkan yang terdiri dari<br>nomor informasi, judul informasi, poster,<br>deskripsi informasi, tanggal dimasukan<br>informasi, dan aksi edit atau hapus|
|13|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada informasi<br>umum|
|14|Mencari informasi umum|Berhasil menampilkan data informasi<br>umum yang sudah dicari|
|15|Tambah data informasi umum|Berhasil menambahkan judul informasi,<br>deskripsi informasi, dan poster informasi<br>umum baru|
|16|Edit data informasi umum|Berhasil mengubah atau melakukan edit<br>judul informasi, deskripsi informasi, dan<br>poster informasi umum yang telah di<br>tambahkan sebelumnya|
|17|Hapus data informasi umum|Berhasil menghapus informasi umum yang<br>|
||Fitur|telah di tambahkan sebelumnya<br>Dashboard|
|18|Mengecek report pengisian data<br>talenta pada pie chart|Menampilkan report mahasiswa yang<br>sudah mengisi data talenta dengan pie<br>chart. Antara lain pie chart keseluruhan<br>sudah mengisi dan belum, pie chart traffic<br>pengisian perangkatan, pie chart pengisian<br>perangkatan (angkatan 2020 s/d 2023)<br>antara yang sudah mengisi dan belum<br>mengisi, bar chart bidang talenta, detail<br>mahasiswa yang sudah mengisi data<br>talenta, dan search bar untuk mencari<br>mahasiswa.|
|19|Lihat Detail Mahasiswa|Berhasil menampilkan data mahasiswa<br>mulai<br>dari<br>NIM<br>mahasiswa,<br>nama<br>mahasiswa, jenis kelamin mahasiswa,<br>prodi mahasiswa, angkatan mahasiswa,<br>nomor telepon, email, minat bakat, dan list<br>kejuaraan yang sudah mereka isi.|

|20<br>Mencari mahasiswa yang dipilih|Berhasil mencari mahasiswa yang ingin<br>dilihat|
|---|---|

- _e. Blackbox Testing_ Akun BEMF-IK

Tabel 2.9. _Scenario Blackbox Testing_ Akun BEMF-IK

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka<br>_Landing_<br>_Page_<br>_Website_|Berhasil membuka_Landing Page Website_|
|2|_Login_dengan_username_dan<br>_password_|Masuk ke halaman_dashboard general_|
|3|Memilih<br>bagian<br>manajemen<br>talenta|Masuk ke halaman_dasboard_manajemen<br>talenta dan menampilkan bar chart bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke dashboard general|Berhasil kembali dashboard general yang<br>ada pada sidebar|
|5|Melakukan Logout|Berhasil melakukan logout dan kembali ke<br>landing page|
||Fitur|Kegiatan|
|12|Menampilkan<br>pendaftaran<br>kegiatan bagian kegiatan|Berhasil menampilkan search bar, filter<br>postingan terlama atau terbaru, export<br>kegiatan, tabel history kegiatan mulai dari<br>nomor kegiatan, nama kegiatan, jenis<br>kegiatan,<br>tingkat<br>kegiatan,<br>deadline<br>penutupan, jumlah pendaftar, dan aksi<br>untuk melihat pendaftar|
|13|Melakukan filter postingan dari<br>yang terlama dan terbaru|Berhasil melakukan filter postingan baik<br>yang terlama dan terbaru pada pendaftaran<br>kegiatan bagian kegiatan|
|14|Mencari kegiatan|Berhasil menampilkan data kegiatan yang<br>sudah dicari|
|15|Export Kegiatan|Berhasil melakukan export dalam bentuk<br>excel yang menampilkan nomor kegiatan,<br>nama kegiatan, jenis kegiatan, tingkat<br>kegiatan, deadline penutupan, dan jumlah<br>pendaftar.|

|16|Detail pendaftar kegiatan yang<br>dipilih|Berhasil menampilkan<br>NIM pendaftar, nama<br>pendaftar, minat bakat<br>mengikuti<br>kegiatan<br> <br>pendaftar, CV pendafta<br>aksi untuk menerima<br>pendaftar dari terlama d<br>export pendaftar kegiata|nomor pen<br>pendaftar,<br>pendaftar,<br>yang<br>diisi<br>r, KHS pen<br>pendaftar,<br>an terbaru,<br>n|daftar,<br>prodi<br>alasan<br> <br>oleh<br>daftar,<br>filter<br>sampai|
|---|---|---|---|---|
|17|Lihat upload CV|Berhasil<br>membuka<br> <br>diunggah mahasiswa<br>kegiatan yang dipilih|file<br>yang<br>untuk me|telah<br>ndaftar|
|18|Lihat upload KHS|Berhasil membuka file<br>diunggah mahasiswa<br>kegiatan yang dipilih|KHS yan<br>untuk me|g telah<br>ndaftar|
|19|Export Pendaftar|Berhasil melakukan ex<br>excel yang terdiri dari<br>NIM pendaftar, nama<br>pendaftar, minat bakat<br>mengikuti<br>kegiatan<br> <br>pendaftar, CV pendafta<br>dan status pendaftaran a<br>diterima.|port dalam<br>nomor pen<br>pendaftar,<br>pendaftar,<br>yang<br>diisi<br>r, KHS pen<br>ntara pendi|bentuk<br>daftar,<br>prodi<br>alasan<br> <br>oleh<br>daftar,<br>ng dan|

# _f. Blackbox Testing_ Akun Dosen

Tabel 2.10. _Scenario Blackbox Testing_ Akun dosen

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Membuka<br>_Landing_<br>_Page_<br>_Website_|Berhasil membuka_Landing Page Website_|
|2|_Login_dengan_username_dan<br>_password_|Masuk ke halaman_dashboard general_|
|3|Memilih<br>bagian<br>manajemen<br>talenta|Masuk ke halaman_dasboard_manajemen<br>talenta dan menampilkan bar chart bidang<br>talenta yang sudah diisi mahasiswa,<br>pengisian per angkatan, informasi umum<br>terbaru, seminar terbaru, dan kegiatan<br>terbaru.|
|4|Kembali ke dashboard general|Berhasil kembali dashboard general yang<br>ada pada sidebar|
|5|Melakukan Logout|Berhasil melakukan logout dan kembali ke<br>landing page|

||Fitur Melakuka|n Input Data Talenta|
|---|---|---|
|6|Menampilkan halaman Talenta<br>Dosen|Berhasil menampilkan_preview_data talenta<br>dosen yang terdiri dari Nama Lengkap,<br>Username (yang berupa NIDN), dan<br>Bidang Data Talenta Dosen.|
|7|Melakukan Edit “Ubah” data<br>talenta|Berhasil<br>mengubah<br>dan<br>memasukan<br>maksimal<br>3<br>bidang<br>talenta<br>dosen<br>berdasarkan list yang sudah ada.|
|8|Menyimpan data talenta<br>Fitur Penda|Berhasil menekan dan menyimpan bidang<br>data talenta pilihan dosen dan perubahan<br>tersebut<br>ditampilkan<br>pada<br>_preview_<br>halaman data talenta kembali.<br>mpingan Lomba|
|10|Membuka<br>halaman<br>pendampingan lomba<br>Fitur|Berhasil<br>membuka<br>halaman<br>pendampingan lomba dan menampilkan<br>search<br>bar,<br>nomor<br>_list_<br>mahasiswa<br>bimbingan,<br>nama<br>mahasiswa,<br>nama<br>kejuaraan, alasan mengikuti, file cv, file<br>khs, prodi, dan aksi untuk melihat detail<br>_pop up_mahasiswa.<br>Dashboard|
|11|Mengecek report pengisian data<br>talenta pada pie chart|Menampilkan report mahasiswa yang<br>sudah mengisi data talenta dengan pie<br>chart. Antara lain pie chart keseluruhan<br>sudah mengisi dan belum, pie chart traffic<br>pengisian perangkatan, pie chart pengisian<br>perangkatan (angkatan 2020 s/d 2023)<br>antara yang sudah mengisi dan belum<br>mengisi, bar chart bidang talenta, detail<br>mahasiswa yang sudah mengisi data<br>talenta, dan search bar untuk mencari<br>mahasiswa.|
|12|Lihat Detail Mahasiswa|Berhasil menampilkan data mahasiswa<br>mulai<br>dari<br>NIM<br>mahasiswa,<br>nama<br>mahasiswa, jenis kelamin mahasiswa,<br>prodi mahasiswa, angkatan mahasiswa,<br>nomor telepon, email, minat bakat, dan list<br>kejuaraan yang sudah mereka isi.|
|20|Mencari mahasiswa yang dipilih|Berhasil mencari mahasiswa yang ingin<br>dilihat|


# PROYEK PEMBANGUNAN SISTEM INFORMASI KEGIATAN KEMAHASISWAAN BERBASIS WEBSITE DENGAN FRAMEWORK LARAVEL (STUDI KASUS KEGIATAN PERLOMBAAN FAKULTAS ILMU KOMPUTER UNIVERSITAS PEMBANGUNAN NASIONAL”VETERAN” JAKARTA)

# **BAB II**

# **RANCANGAN PRODUK**

Berdasarkan  penjelasan  pada  latar  belakang,  bab  ini  akan  menjelaskan perancangan  produk  yang  mencakup  deskripsi  aktor,  kerangka  pikir,  serta prototipe  aplikasi.  Perancangan  ini  bertujuan  untuk  memberikan  panduan  dalam proses  pembuatan  aplikasi,  sehingga  proses  pengembangannya  lebih  terarah  dan sistematis.  Dengan  rancangan  yang  jelas  dan  terstruktur,  diharapkan  sistem  ini dapat  dikembangkan  secara  efisien,  sesuai  dengan  kebutuhan  pengguna,  serta mendukung  kelancaran  pelaksanaan  kegiatan  kemahasiswaan,  khususnya  yang berkaitan dengan perlombaan.

# **2.1 Deskripsi Pengguna**

Setiap  pengguna  dalam  sistem  ini  memiliki  peran  spesifik  dengan hak  akses  serta  tanggung  jawab  yang  telah  ditentukan.  Hal  ini  bertujuan untuk  memastikan  pengelolaan  dan  pelaksanaan  kegiatan  perlombaan dapat  berjalan  dengan  lebih  terstruktur.  Menjelaskan  peran  tiap  pengguna menjadi  langkah  penting  dalam  memastikan  bahwa  mereka  dapat menjalankan fungsinya sesuai dengan otoritas yang diberikan.

Tabel  2.1  di  bawah  ini  merangkum  berbagai  peran  dalam  sistem, termasuk  hak  akses  serta  fungsionalitas  yang  dapat  dijalankan  oleh masing-masing  pengguna.  Deskripsi  ini  mencakup  tanggung  jawab  utama setiap pengguna dalam mengelola informasi perlombaan yang diselenggarakan  di  Fakultas  Ilmu  Komputer,  Universitas  Pembangunan Nasional “Veteran” Jakarta.

Tabel 2.1 Deskripsi Pengguna

|**Pengguna**|**Deskripsi**|
|---|---|
|Mahasiswa|1.  Mengakses serta melihat informasi perlombaan yang|
||tersedia.|

|2.<br>3.<br>4.<br>5.<br>6.|Melakukan pencarian lomba sesuai kebutuhan.<br>Mendaftarkan diri dalam perlombaan yang diminati.<br>Mengakses serta membaca buku panduan<br>perlombaan.<br>Melakukan pencatatan mandiri terkait keikutsertaan<br>dalam perlombaan.<br>Mencatat pencapaian sebagai pemenang lomba<br>secara mandiri.|
|---|---|
|Badan Eksekutif<br>1.|Mengakses serta melihat informasi terkait|
|Mahasiswa (BEM)|perlombaan.|
|Fakultas Ilmu<br>Komputer<br>2.|Menambahkan informasi lomba baru ke dalam<br>sistem.|
|Universitas<br>Pembangunan<br>3.|Menghapus informasi lomba yang sebelumnya telah<br>ditambahkan oleh BEM.|
|Nasional “Veteran”<br>Jakarta<br>4.|Memperbarui atau mengedit data lomba yang telah<br>dimasukkan oleh BEM.|
|Kelompok Studi<br>1.|- Mengakses serta melihat informasi perlombaan.|
|Mahasiswa (KSM)<br>Fakultas Ilmu<br>2.|Menambahkan informasi lomba baru yang berkaitan<br>dengan KSM.|
|Komputer<br>Universitas<br>3.|Menghapus informasi lomba yang telah ditambahkan<br>oleh KSM bersangkutan.|
|Pembangunan<br>4.|Memperbarui atau mengedit informasi lomba yang|
|Nasional “Veteran”<br>Jakarta|telah dimasukkan oleh KSM terkait.|
|Wakil Dekan 3<br>1.|Mengakses dan melihat informasi terkait<br>perlombaan.|

||2.  Melakukan pencarian data perlombaan sesuai<br>kebutuhan.<br>3.  Mengakses data mahasiswa yang mengikuti<br>perlombaan.<br>4.  Mengakses data pemenang perlombaan.|
|---|---|
|Staf Tata Usaha|1.  Mengakses serta melihat seluruh informasi lomba<br>yang tersedia.<br>2.  Melakukan pencarian informasi perlombaan dalam<br>sistem.|
||3.  Membaca, memperbarui, serta menghapus (CRUD)|
||seluruh informasi yang terdapat dalam sistem.|
||4.  Mengakses data mahasiswa yang berpartisipasi<br>dalam perlombaan.|
||5.  Mengakses informasi mengenai pemenang lomba.|

# **2.2 Kerangka Pikir**

Kerangka  pikir  merupakan  elemen  krusial  dalam  perencanaan proyek  pembangunan  sistem  informasi  kegiatan  kemahasiswaan  berbasis website  ini.  Dengan  kerangka  pikir  yang  terstruktur,  proyek  ini  dapat dipandu  secara  sistematis  dari  tahap  perancangan  hingga  implementasi. Hal  ini  memungkinkan  semua  pihak  yang  terlibat,  baik  pengembang maupun  pengguna,  untuk  memiliki  pemahaman  yang  sama  tentang  alur kerja dan interaksi antara elemen-elemen dalam sistem.

Gambar  2.3  di  bawah  ini  menampilkan  konsep  kerangka  pikir yang  diterapkan  dalam  proyek  website  informasi  kegiatan  perlombaan. Sistem  ini  dirancang  untuk  mempermudah  mahasiswa  dalam  mencari  dan mendaftar  lomba,  serta  mendukung  Badan  Eksekutif  Mahasiswa  (BEM), Kelompok  Studi  Mahasiswa  (KSM),  dan  pihak  fakultas  dalam

menyebarluaskan  informasi  terkait  perlombaan  yang  ada  di  lingkungan Fakultas  Ilmu  Komputer.  Dalam  sistem  ini,  terdapat  beberapa  aktor  yang memiliki  peran  spesifik,  di  antaranya  mahasiswa,  Badan  Eksekutif Mahasiswa  (BEM),  Kelompok  Studi  Mahasiswa  (KSM),  Wakil  Dekan  3,

serta Staf Tata Usaha.

<!-- Start of picture text -->
vilonns<br>sa<br><!-- End of picture text -->

Gambar 2.3 Kerangka Pikir

Sumber: Dokumen Pribadi

Sistem  informasi  berbasis  web  ini  dirancang  dengan  tujuan  utama untuk meningkatkan aksesibilitas mahasiswa  terhadap  informasi perlombaan  yang  tersedia  di  Fakultas  Ilmu  Komputer  Universitas Pembangunan  Nasional  "Veteran"  Jakarta.  Seperti  yang  digambarkan dalam  Gambar  2.3,  sistem  ini  melibatkan  beberapa  pemangku kepentingan,  di  antaranya  mahasiswa,  Badan  Eksekutif  Mahasiswa (BEM),  Kelompok  Studi  Mahasiswa  (KSM),  Wakil  Dekan  3,  dan  Staf Tata Usaha sebagai administrator sistem.

Semua  pemangku  kepentingan  dapat  melakukan _login_ untuk mengakses  informasi  kegiatan  kemahasiswaan  melalui _website_ .  Badan Eksekutif  Mahasiswa  (BEM),  Kelompok  Studi  Mahasiswa  (KSM),  dan Staf  Tata  Usaha  memiliki  kemampuan  untuk  membuat,  membaca, memperbarui,  dan  menghapus  (CRUD)  informasi  terkait  perlombaan yang  mereka  unggah.  Informasi  ini  mencakup  nama  lomba,  deskripsi lomba,  pihak  penyelenggara,  batas  waktu  pendaftaran,  buku  panduan (guidebook),  dan  tautan  pendaftaran,  yang  kemudian  dapat  dilihat  oleh mahasiswa.

Mahasiswa,  setelah  melakukan _login_ ,  dapat  mengakses  berbagai informasi  lomba  yang  tersedia  dan  memilih  lomba  yang  ingin  diikuti. Mereka  dapat  melihat  detail  informasi  dari  setiap  lomba,  seperti  nama lomba,  deskripsi  lomba,  pihak  penyelenggara,  batas  waktu  pendaftaran, panduan,  dan  tautan  pendaftaran.  Setelah  itu,  mereka  dapat  mengklik tautan  dan  mengisi  formulir  pendaftaran  yang  tersedia  serta  mengunggah dokumen  persyaratan  yang  diperlukan.  Selanjutnya,  mahasiswa  diminta untuk  mengisi  formulir  pendataan  pendaftaran  lomba  fakultas.  Jika  ada mahasiswa  yang  memenangkan  lomba,  mereka  dapat  melakukan konfirmasi  melalui  website,  di  mana  data  mahasiswa  tersebut  akan  terisi otomatis dari data pendaftar lomba.

Wakil  Dekan  3  memiliki  peran  pengawasan  dan  verifikasi  dalam sistem.  Wakil  Dekan  3  dapat  melihat  dan  mengakses  semua  informasi terkait  perlombaan  yang  tersedia.  Selain  itu,  Wakil  Dekan  3  juga  dapat melakukan  pencarian  lomba  berdasarkan  kriteria  tertentu.  Wakil  Dekan  3 memiliki  akses  untuk  melihat  pendataan  mahasiswa  yang  mengikuti lomba  serta  pendataan  pemenang  lomba,  sehingga  dapat  memantau  dan mengevaluasi  partisipasi  serta  prestasi  mahasiswa  dalam  berbagai perlombaan.

Staf  Tata  Usaha  memiliki  peran  administratif  yang  penting  dalam sistem.  Mereka  memiliki  akses  penuh  untuk  melihat  dan  mengakses semua  informasi  terkait  perlombaan  yang  tersedia  di  dalam  sistem.  Selain itu,  mereka  memiliki  wewenang  untuk  melihat  pendataan  mahasiswa yang  mengikuti  lomba  serta  pendataan  pemenang  lomba,  memastikan kelancaran proses administrasi dan dokumentasi kegiatan kemahasiswaan.  Selanjutnya,  Staf  Tata  Usaha  memiliki  kemampuan untuk  membuat,  membaca,  memperbarui,  dan  menghapus  (CRUD)  semua informasi  yang  tersedia  dalam  sistem,  memberikan  fleksibilitas  dan kontrol yang diperlukan untuk menjaga data tetap akurat dan terkini.

# **2.3 Sketsa Desain Aplikasi**

Sebagai  tindak  lanjut  dari  kerangka  pikir  yang  telah  dirancang, penulis  mengembangkan  beberapa  sketsa  desain  aplikasi  untuk mengilustrasikan  konsep  awa; _website_ yang  bertujuan  mendukung distribusi  informasi  kegiatan  perlombaan.  Sketsa  desain  ini  berfungsi sebagai gambaran awal dari _user interface_ pengguna.

<!-- Start of picture text -->
Masuk<br>ak<br><!-- End of picture text -->

# Gambar 2.4 Tampilan Masuk

# Sumber: Dokumen Pribadi

Pada  halaman  awal  atau  tampilan  masuk,  pengguna  diminta  untuk menginput  nama  pengguna  serta  kata  sandi.  Selain  itu,  terdapat  tombol "Masuk" yang dapat diklik untuk mengakses sistem.

<!-- Start of picture text -->
Form Penyebaran Informasi Lomba<br>NamaLomba SLASHNATIONAL COMPETITON 2024<br>DeskripsiLombe ‘BEMF-1KUPNV! Proudly Present<br>Keyboard berderak.debergerna<br>Diartara<br>KitabangunKage danAigortne<br>dina agtalyenggemilang<br>1)<br>MARK YOURCALENDER/<br>misckaraonm<br>Sendataran: 8-2<br>cae Ap 2028<br>ame ce<br>Namace2<br>kesempatanuntakmemenangkan<br>hadanya ©<br>Deacine Pendattaran —[ 8-21Apni2024<br>LnkPendattran tps /fnktee/slshcom2024<br>PosterLomos PBrpostersashcomae x<br><a)<br><!-- End of picture text -->

# Gambar 2.5 Tampilan Form Penyebaran Informasi Lomba

# Sumber: Dokumen Pribadi

Pada  tampilan  form  penyebaran  informasi  lomba,  Badan  Eksekutif Mahasiswa  (BEM),  Kelompok  Studi  Mahasiswa  (KSM),  dan  Staf  Tata Usaha diberikan kemampuan untuk memasukkan detail-detail perlombaan, termasuk nama lomba, deskripsi lomba, pihak

penyelenggara,  batas  waktu  pendaftaran,  buku  panduan  (guidebook),  dan tautan  pendaftaran.  Selain  itu,  mereka  juga  dapat  melakukan  aksi  edit, menyimpan  perubahan,  atau  membatalkan  perubahan  yang  dilakukan pada form Penyebaran Informasi Lomba.

<!-- Start of picture text -->
Informasi Lomba Uploadedtby BEM/KSM/STAFTU<br>Nama oma<br>Deadline Pendattaran<br>Penyolenausre<br><!-- End of picture text -->

Gambar 2.6 Tampilan Informasi Lomba

# Sumber: Dokumen Pribadi

Pada  tampilan  informasi  lomba, _user_ dapat  melihat  informasi  lomba berupa  nama  lomba,  tenggat  waktu  pendaftaran,  penyelenggara,  dan deskripsi  singkat  terkait  lomba  yang  akan  diselenggarakan. _User_ dapat melakukan  pendaftaran  lomba  dengan  cara  klik  tombol  daftar  dan _user_ juga  dapat  melihat  guidebook  lomba  dengan  cara  klik  tombol  lihat _guidebook._

<!-- Start of picture text -->
Form Pendataan Pendaftaran Lomba<br>=<br><!-- End of picture text -->

Gambar 2.7 Tampilan Form Pendataan Pendaftaran Lomba

Sumber: Dokumen Pribadi

Pada  tampilan  form  pendataan  pendaftaran  lomba, _user_ dapat  mengisi data  yang  dibutuhkan  seperti  nama  lengkap,  NIM,  program  studi, angkatan,  nama  lomba,  jenis  lomba,  penyelenggara  lomba,  dan  dosen pembimbing _._ Setelah  mengisi  form, _user_ dapat  mengklik  tombol _submit. User_ juga  dapat  melakukan  pembatalan  pada  pendaftaran  lomba  dengan cara klik tombol batal.

<!-- Start of picture text -->
Form Pendataan Pemenang Lomba<br>-<br>vo<br>Name tombe GDSCPHELS Chalenge 2028<br>Serunhat ae<br><!-- End of picture text -->

<!-- Start of picture text -->
x<br>Selamat<br>prestasinsudahmasukke<br>Data‘atatannernalFakfan,Yklonitendataandlwebsteatas Prestasimu! Presma!data<br><!-- End of picture text -->

Gambar 2.8 Tampilan Form Pendataan Pemenang Lomba

# Sumber: Dokumen Pribadi

Pada  tampilan  form  pendataan  pemenang  lomba, _user_ dapat  mengisi  data yang  dibutuhkan  seperti  nama  lengkap,  NIM,  program  studi,  angkatan, nama  lomba,  jenis  lomba,  penyelenggara  lomba,  dosen  pembimbing,  dan mengunggah  sertifikat  juara  atau  bukti  memenangkan  lomba _._ Setelah mengisi  form, _user_ dapat  mengklik  tombol _submit_ yang  kemudian  akan tampil  ucapan  selamat  untuk  pemenang  lomba _.  User_ juga  dapat melakukan  pembatalan  pada  form  pendataan  pemenang  lomba  dengan cara klik tombol batal.

<!-- Start of picture text -->
Informasi Pendataan Lomba<br>e<br><!-- End of picture text -->

# Gambar 2.9 Tampilan Data Pendaftar dan Pemenang Lomba

# Sumber: Dokumen Pribadi

Pada  tampilan  data  pendaftar  dan  pemenang  lomba,  terdapat  informasi terkait  mahasiswa  yang  telah  mengisi  form  pendaftaran  dan  pendataan pemenang  lomba  berupa  NIM,  Nama,  Program  studi,  angkatan,  nama lomba,  jenis  lomba,  penyelenggara,  dan  dosen  pembimbing.  Tampilan  ini hanya bisa diakses oleh Wakil Dekan 3 dan Staf Tata Usaha.

# **2.4 Teknologi Proyek**

Pengembangan _website_ distribusi  informasi  kegiatan  perlombaan membutuhkan  teknologi  yang  tepat.  Pemilihan  perangkat  keras  dan  perangkat lunak  menjadi  elemen  kunci  dalam  memastikan  keberhasilan  proyek  ini. Teknologi  yang  digunakan  meliputi  perangkat  keras  untuk  proses  pengembangan dan  perangkat  lunak  utama  serta  pendukung  yang  dirancang  untuk  mendukung efisiensi sistem. Berikut ini adalah rincian kebutuhan teknologinya:

# **2.4.1  Kebutuhan Perangkat Keras**

Proyek ini memanfaatkan sebuah laptop HP dengan spesifikasi sebagai berikut:

- 1)  Prosesor: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz 2.42 GHz

- 2)  RAM: 8 GB

- 3)  Penyimpanan: 512 GB SSD

# **2.4.2  Kebutuhan  Perangkat Lunak**

Perangkat lunak yang diterapkan dalam proyek ini meliputi:

- 1)  Sistem Operasi: Microsoft Windows 11 Home Single Language

- 2)  Bahasa Pemrograman: PHP

- 3)  Framework: Laravel, Tailwind CSS, dan ReactJS

- 4)  Basis Data: MySQL

- 5)  Editor Kode: Visual Studio Code

# **2.5 Rencana Pengujian Proyek**

Dalam  tahap  pengujian _website_ ,  metode  pengujian _Black  Box_ akan diterapkan.  Pengujian _Black  Box_ berfokus  pada  pengujian  fungsionalitas  sistem tanpa  perlu  melihat  struktur  internal  atau  kode  sumber  aplikasi.  Tujuan  utama dari  pengujian  ini  adalah  memastikan  bahwa  sistem  beroperasi  sesuai  dengan spesifikasi yang telah ditetapkan serta memenuhi kebutuhan pengguna.

# **2.5.1    Skenario Pengujian**

Skenario  pengujian  akan  disusun  berdasarkan  fitur  utama  yang  tersedia dalam  sistem.  Pengujian  ini  melibatkan  beberapa  kategori  pengguna,  yaitu Mahasiswa,  Admin  TU,  Wakil  Dekan,  dan  Koordinator  Program  Studi,  yang semuanya  merupakan  bagian  dari  Fakultas  Ilmu  Komputer  di  Universitas Pembangunan  Nasional  "Veteran"  Jakarta.  Tujuan  dari  pengujian  ini  adalah untuk  memastikan  bahwa  seluruh  fitur  dan  fungsionalitas  website  bekerja  dengan baik sesuai dengan kebutuhan dan peran pengguna masing-masing.

a.  Pengujian Akun Mahasiswa

Tabel 2.2 Skenario Pengujian Akun Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>website Techfo|Halaman utama_website_tampil dengan<br>layout yang benar dan semua elemen<br>berfungsi dengan baik. Pengguna dapat<br>melihat dashboard mengenai aktivitas dan<br>pencapaian mahasiswa.|
|2|Login menggunakan NIM dan<br>kata sandi|Pengguna masuk ke_dashboard_jika NIM<br>dan kata sandi yang dimasukkan valid. Jika<br>tidak, pesan error akan muncul.|
||Fitur|Dashboard|
|3|Melihat informasi pada<br>dashboard website Techfo|Informasi terkait lomba ditampilkan<br>dengan benar.|

|4|Mengakses data  informasi<br>lomba|Pengguna dapat mengakses informasi<br>lomba.|
|---|---|---|
|5|Melihat rincian informasi<br>lomba|Informasi lomba ditampilkan dengan<br>benar.|
|6|Mengakses buku panduan<br>lomba|Buku panduan lomba dapat diunduh atau<br>dilihat langsung melalui browser.|
|||Tautan untuk pendaftaran lomba dapat|
|7|Melakukan pendaftaran lomba|diklik dan berhasil mengarah ke halaman<br>eksternal untuk pendaftaran lomba.|

Fitur FAQ

|8|Melihat Prosedur Pendaftaran<br>Lomba|Informasi prosedur pendaftaran lomba<br>ditampilkan dengan format yang mudah<br>dipahami.|
|---|---|---|
|9|Melihat Prosedur Pendataan<br>Prestasi Lomba|Prosedur pendataan prestasi lomba<br>ditampilkan sesuai dengan kebijakan<br>universitas.|
|10|Prosedur Klaim Hadiah Prestasi<br>dari Universitas<br>Fitur|<br>Informasi langkah-langkah klaim hadiah<br>ditampilkan dengan jelas dan rinci.<br>Pendataan|
|11|Melakukan pendataan<br>partisipasi lomba|Sistem menyimpan data partisipasi lomba<br>dengan benar dan mengalihkan pengguna<br>ke halaman profile bagian riwayat<br>pendataan.|
|12|Melakukan pendataan prestasi<br>lomba|Sistem menyimpan data prestasi lomba<br>dengan benar dan mengalihkan pengguna<br>ke halaman profile bagian riwayat|

|||pendataan.|
|---|---|---|
||Fitu|r Profile|
|13|Data mahasiswa|Data mahasiswa ditampilkan sesuai<br>dengan akunnya.|
|14|Mengakses rangkuman data<br>laporan kegiatan yang diikuti<br>mahasiswa|Data ringkasan kegiatan yang telah diikuti<br>oleh mahasiswa.|
|15|Mengakses riwayat pendataan<br>partisipasi kegiatan lomba|Riwayat partisipasi kegiatan lomba<br>ditampilkan dalam bentuk jajaran kartu.|
|16|Mengakses histori pendataan<br>prestasi kegiatan lomba|Histori prestasi kegiatan lomba<br>ditampilkan dengan informasi detail.|

# b.  Pengujian Akun Admin Tata Usaha

Tabel 2.3 Skenario Pengujian Akun Admin Tata Usaha

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>tata letak yang sesuai, dan semua elemen<br>berfungsi dengan baik. Admin dapat<br>melihat dashboard yang menunjukkan<br>aktivitas dan pencapaian mahasiswa<br>Fakultas Ilmu Komputer UPN "Veteran"<br>Jakarta.|
|2|Masuk dengan nama pengguna<br>dan kata sandi|Admin bisa masuk ke aplikasi jika dengan<br>nama pengguna dan kata sandi yang<br>dimasukkan benar. Jika tidak, pesan gagal<br>akan muncul.|

|3|Fitur<br>Mengakses dashboard aplikasi|Dashboard<br>Dashboard menampilkan data laporan<br>dalam bentuk grafik.|
|---|---|---|
|4|Menampilkan data laporan<br>terkait perlombaan<br>Fitu<br>|Laporan ditampilkan dengan benar<br>r Laporan|
|5|Menampilkan data laporan<br>terkait perlombaan|Laporan ditampilkan dengan benar|
|6|Fitur filter|Data hasil filter tampil sesuai dengan jenis<br>filter yang dipilih mulai dari filter tahun,<br>program studi, jenis prestasi, dan bidang<br>prestasi yang dipilih.|
|7|Menampilkan data hasil<br>pencarian berdasarkan nama<br>atau NIM mahasiswa|Sistem menampilkan data mahasiswa<br>berdasarkan nama atau NIM yang<br>dimasukkan.|
|8|Melakukan validasi data<br>prestasi lomba yang diisi<br>mahasiswa|Data prestasi lomba divalidasi dan<br>disimpan oleh admin.|
|9|Mengakses dokumen bukti<br>kegiatan lomba|File bukti kegiatan (sertifikat) dapat dibuka<br>dalam format .jpg, .jpeg, .png, atau .pdf.|
|10|Membuka file foto kegiatan<br>lomba (.jpg, .jpeg, .png, .pdf)|Dokumen foto kegiatan dapat diakses<br>dalam format .jpg, .jpeg, atau .png.|
|11|Mengakses dokumen laporan<br>kegiatan lomba (.pdf)|Dokumen laporan kegiatan dapat diakses.|

Fitur Pusat Informasi

|12|Mengakses pusat kegiatan<br>lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|---|---|---|
|13|Menambahkan data kegiatan<br>lomba|Data lomba berhasil ditambahkan.|
|14|Melakukan pembaruan<br>informasi lomba|Data lomba bisa di-_update_.|
|15|Menghapus data lomba|Data lomba berhasil dihapus.|
|16|Melakukan validasi data<br>inputan lomba|Data lomba divalidasi, kemudian muncul<br>di_website_mahasiswa.|

# c.  Pengujian Akun Wakil Dekan Fakultas Ilmu Komputer

Tabel 2.4 Skenario Pengujian Akun Wakil Dekan

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>benar dan sesuai.|
|2|Masuk menggunakan NIDN<br>dan kata sandi|Jik NIDN dan kata sandi yang dimasukkan<br>benar, Wakil Dekan dapat masuk ke<br>dashboard_website_Techfo. Jika tidak,<br>pesan gagal akan muncul.|
||Fitu|r Dashboard|
|3|Mengakses data_dashboard_|_Dashboard_menampilkan data laporan<br>dengan benar.|
|4|Menampilkan laporan|Laporan perlombaan ditampilkan dengan|

||perlombaan mahasiswa|benar|
|---|---|---|
||Fitu<br>|r Laporan<br>|
|5|Menampilkan laporan<br>perlombaan mahasiswa|Laporan perlombaan ditampilkan dengan<br>benar|
|6|Menampilkan data hasil filter|Sistem menampilkan data hasil filter sesuai<br>dengan jenis filter yang dipilih mulai dari<br>filter tahun, program studi, jenis prestasi,<br>dan bidang prestasi yang dipilih.|
|7|Menampilkan data hasil<br>pencarian berdasarkan nama<br>atau NIM mahasiswa|Sistem menampilkan data mahasiswa<br>berdasarkan nama atau NIM yang<br>dimasukkan.|
|8|Melakukan validasi data<br>prestasi lomba yang diisi<br>mahasiswa|Data prestasi lomba divalidasi dan<br>disimpan oleh admin.|
|9|Mengakses dokumen bukti<br>kegiatan lomba|File bukti kegiatan (sertifikat) dapat dibuka<br>dalam format .jpg, .jpeg, .png, atau .pdf.|
|10|Membuka file foto kegiatan<br>lomba (.jpg, .jpeg, .png, .pdf)|Dokumen foto kegiatan dapat diakses<br>dalam format .jpg, .jpeg, atau .png.|
|11|Mengakses dokumen laporan<br>kegiatan lomba (.pdf)|Dokumen laporan kegiatan dapat diakses<br>dalam format .pdf.|
||<br>Fitur P|<br>usat Informasi<br>|
|12|Mengakses pusat lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|13|Menambahkan data lomba|Data lomba berhasil ditambahkan.|
|14|Melakukan pembaruan|Data lomba dapat diperbarui sesuai|

||informasi lomba|kebutuhan.|
|---|---|---|
|15|Menghapus data lomba|Data lomba berhasil dihilangkan.|
|16|Melakukan validasi data<br>inputan lomba|Data lomba divalidasi, kemudian muncul<br>di_website_mahasiswa.|

d.  Pengujian Akun Koordinator Program Studi Fakultas Ilmu Komputer

Tabel 2.5 Skenario Pengujian Akun Koordinator Program Studi

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>benar dan sesuai.|
|2|Masuk menggunakan NIDN<br>dan kata sandi<br>Fitu|Jik NIDN dan kata sandi yang dimasukkan<br>benar, Koordinator Program Studi dapat<br>masuk ke dashboard_website_. Jika tidak,<br>pesan gagal akan muncul.<br>r Dashboard|
|3|Mengakses data_dashboard_|_Dashboard_menampilkan data laporan<br>dengan benar.|
|4|Menampilkan laporan<br>perlombaan mahasiswa|Laporan perlombaan ditampilkan dengan<br>benar|
||Fitur P|usat Informasi|
|5|Mengakses pusat lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|6|Menambahkan data lomba|Data lomba berhasil ditambahkan.|

|7|Melakukan pembaruan<br>informasi lomba|Data lomba dapat diperbarui sesuai<br>kebutuhan.|
|---|---|---|
|8|Menghapus data lomba|Data lomba berhasil dihilangkan.|
|9|Melakukan validasi data<br>inputan lomba|Data lomba divalidasi, kemudian muncul<br>di_website_mahasiswa.|

# e.  Pengujian Akun Dosen Fakultas Ilmu Komputer

Tabel 2.5 Skenario Pengujian Akun Dosen

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>benar dan sesuai.|
|||Jik NIDN dan kata sandi yang dimasukkan|
|2|Masuk menggunakan NIDN<br>dan kata sandi|benar, Dosen dapat masuk ke dashboard<br>_website_. Jika tidak, pesan gagal akan<br>muncul.|

Fitur Dashboard

|3|Mengakses data_dashboard_|_Dashboard_menampilkan data laporan<br>dengan benar.|
|---|---|---|
|4|Menampilkan laporan<br>perlombaan mahasiswa|Laporan perlombaan ditampilkan dengan<br>benar|

Fitur Pusat Informasi

|5|Mengakses pusat lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|---|---|---|
|6|Menambahkan data lomba|Data lomba berhasil ditambahkan.|

|7|Melakukan pembaruan<br>informasi lomba|Data lomba dapat diperbarui sesuai<br>kebutuhan.|
|---|---|---|
|8|Menghapus data lomba|Data lomba berhasil dihilangkan.|
|9|Melakukan validasi data<br>inputan lomba|Data lomba divalidasi, kemudian muncul<br>di_website_mahasiswa.|

# f.  Pengujian Akun Badan Eksekutif Mahasiswa Fakultas Ilmu Komputer

Tabel 2.7 Skenario Pengujian Akun Badan Eksekutif Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>benar dan sesuai.|
|2|Masuk menggunakan NIM dan<br>kata sandi|Jik NIM dan kata sandi yang dimasukkan<br>benar maka bisa masuk ke aplikasi. Jika<br>tidak, pesan gagal akan muncul.|
||Fitur|Dashboard|
|3|Mengakses data_dashboard_|_Dashboard_menampilkan data laporan<br>dengan benar.|
|4|Menampilkan laporan<br>perlombaan mahasiswa|Laporan perlombaan ditampilkan dengan<br>benar|
||Fitur Pu|sat Informasi|
|5|Mengakses pusat lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|6|Menambahkan data lomba|Data lomba berhasil ditambahkan.|

|7|Melakukan pembaruan|Data lomba dapat diperbarui sesuai|
|---|---|---|
||informasi lomba|kebutuhan.|
|8|Menghapus data lomba|Data lomba berhasil dihilangkan.|

g.  Pengujian Akun Kelompok Studi Mahasiswa Fakultas Ilmu Komputer

Tabel 2.8 Skenario Pengujian Akun Kelompok Studi Mahasiswa

|**No**|**Skenario**|**Hasil Yang Diharapkan**|
|---|---|---|
|1|Mengakses halaman utama<br>situs Techfo|Halaman utama situs Techfo tampil dengan<br>benar dan sesuai.|
|2|Masuk menggunakan NIM dan<br>kata sandi|Jik NIM dan kata sandi yang dimasukkan<br>benar maka bisa masuk ke aplikasi. Jika<br>tidak, pesan gagal akan muncul.|
|3|Fitur<br>Mengakses data_dashboard_|Dashboard<br>_Dashboard_menampilkan data laporan<br>dengan benar.|
|4|Menampilkan laporan<br>perlombaan mahasiswa|Laporan perlombaan ditampilkan dengan<br>benar|
||Fitur Pu|sat Informasi|
|5|Mengakses pusat lomba|Sistem menampilkan data lomba yang<br>sudah pernah diunggah.|
|6|Menambahkan data lomba|Data lomba berhasil ditambahkan.|
|7|Melakukan pembaruan<br>informasi lomba|Data lomba dapat diperbarui sesuai<br>kebutuhan.|

8 Menghapus data lomba Data lomba berhasil dihilangkan.


# PROYEK PENGEMBANGAN SISTEM INFORMASI SURAT ELEKTRONIK PADA LAYANAN KEMAHASISWAAN FAKULTAS HUKUM UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN” JAKARTA

# **BAB II**

# **RANCANGAN PRODUK**

# **2.1 Observasi**

Peneliti melakukan observasi dengan terjun langsung ke tempat penelitian, yakni di Fakultas Hukum UPN "Veteran" Jakarta, untuk mengamati secara langsung berbagai fenomena dan aktivitas yang terjadi. Tahapan ini merupakan langkah penting karena membantu peneliti untuk mendapatkan pemahaman yang mendalam tentang konteks dan dinamika yang ada di lingkungan tersebut. Observasi ini bertujuan untuk mengenali masalah yang ada, memetakan proses kerja yang sedang berjalan, serta mengidentifikasi kendala-kendala yang dihadapi oleh fakultas dan mahasiswa dalam proses pengurusan surat. Selama observasi, peneliti mencatat berbagai aspek, seperti interaksi antara staf dan mahasiswa, penggunaan fasilitas, serta proses administrasi yang berlangsung. Peneliti juga mengamati bagaimana kebijakan-kebijakan yang ada diimplementasikan dalam praktik sehari-hari, dan bagaimana hal tersebut mempengaruhi efektivitas pengurusan surat-menyurat.

Dengan terlibat secara langsung, peneliti dapat mengumpulkan data yang lebih akurat dan mendapatkan wawasan yang mendalam mengenai topik yang sedang diteliti. Observasi juga membantu peneliti untuk melihat secara langsung interaksi antara individu, kebijakan, dan lingkungan, yang dapat memberikan wawasan yang mendalam untuk proses penelitian. Misalnya, peneliti dapat mengamati bagaimana mahasiswa berinteraksi dengan sistem pengurusan surat-menyurat, bagaimana mereka mencari informasi, dan bagaimana mereka mengatasi hambatan yang mungkin timbul. Selain itu, peneliti juga dapat mengamati bagaimana staf fakultas bekerja, bagaimana mereka berkoordinasi, dan bagaimana mereka menggunakan sumber daya yang tersedia. Dengan cara ini, peneliti dapat memperoleh pemahaman yang holistik tentang permasalahan yang ada dan mengidentifikasi potensi solusi yang dapat diterapkan.

# 2.1.1 Use case Sistem yang sedang berjalan.

<!-- Start of picture text -->
SISTEM BERJALAN - PENGAJUAN<br>Membuat form pendaftaran<br>menggunakan google form<br><<include>><br>{llemasukan link google form<br>kedalam web layanan FH<br>; I<br>O Admin kemahasiswaan<br>tersedia di web layanan FH<br>NY Mengisi google form yang<br>Mahasiswa<br>fengolah data dari googid<br>form<br>Menunggu email untuk<br>pengambilan surat<br><!-- End of picture text -->

gambar 2. 1 Use case sistem yang sedang berjalan

Pada sistem yang tengah beroperasi, yang diilustrasikan melalui diagram use case, menggambarkan alur proses pengajuan surat, proses dimulai dari admin yang membuat formulir pengajuan surat melalui google form, kemudian mahasiswa mengisi form tersebut. Setelah pengajuan data diterima, admin menyimpan data ke google drive untuk mempermudah pengelolaan dan penyimpanan, selanjutnya admin melakukan pengecekan Formulir dan melakukan proses administrasi dan meminta tanda tangan kepada pejabat fakultas sesuai dengan surat yang diajukan.

Setelah surat ditanda tangan oleh pejabat fakultas, maka admin akan mengirim pesan melalui email bahwa surat tersebut sudah jadi dan segera untuk diambil di layanan kemahasiswaan Fakultas Hukum UPN Veteran Jakarta, dan mahasiswa akan datang ke lokasi untuk pengambilan surat.

# 2.1.2 Dokumentasi Observasi dengan Wakil Dekan II Bidang Umum Fakultas Hukum

Kami mengawali observasi dengan mengadakan pertemuan bersama Wakil Dekan II Bidang Umum Fakultas Hukum, untuk membahas secara mendalam sistem yang sedang beroperasi. Pada pertemuan ini, kami mengidentifikasi area yang memerlukan perbaikan dan fitur-fitur baru yang dapat dikembangkan oleh peneliti untuk meningkatkan efisiensi dan efektivitas sistem tersebut.

gambar 2. 2 Observasi dengan Wakil Dekan Bidang umum FH

# 2.1.3 Dokumentasi dengan Kaprodi S1 Hukum

Kami turut melakukan observasi untuk memahami hubungan antara sistem program studi dengan sistem surat yang sedang dirancang. Selain itu, Kaprodi / Koordinator Program Studi berperan sebagai salah satu aktor penting dalam sistem yang akan dibuat, sehingga analisis perannya menjadi hal yang krusial. Proses observasi ini meliputi pengamatan interaksi Kaprodi dengan sistem yang ada, identifikasi kebutuhan spesifik program studi, serta pengumpulan masukan yang konstruktif guna memastikan bahwa sistem yang dikembangkan mampu memenuhi kebutuhan semua pihak terkait.

gambar 2. 3 Observasi dengan Kaprodi S1 Hukum

2.1.4 Dokumentasi dengan staff kemahasiswaan Fakultas Hukum Universitas Pembangunan Nasional “Veteran” Jakarta

Kami mengadakan pertemuan dengan Staff Kemahasiswaan Fakultas untuk mendiskusikan pengembangan sistem surat elektronik. Dalam pertemuan tersebut, kami meninjau kebutuhan dan harapan staf, mengidentifikasi masalah dalam pengelolaan suratmenyurat, serta mengumpulkan saran untuk peningkatan sistem. Tujuannya adalah memastikan sistem yang dikembangkan dapat memenuhi kebutuhan operasional.

<!-- Start of picture text -->
"pp. i. =n<br>ay | |<br>Se 4m<br><!-- End of picture text -->

gambar 2. 4 Observasi dengan Kemahasiswaan FH

# 2.1.5 Prosedur Sistem berjalan

Sistem layanan surat pada Fakultas Hukum UPNVJ memiliki sistem yang sudah berjalan. Yaitu saat ini Fakultas Hukum UPNVJ membuat google form yang tersedia di website Fakultas Hukum UPNVJ kemudian mahasiswa akan mengisi formulir tersebut untuk melakukan pengajuan surat, lalu data masuk ke admin kemahasiswaan, kemudian admin kemahasiswaan mencetak dan meminta tanda tangan pada pejabat fakultas terkait, lalu mahasiswa akan mengambilnya ditempat layanan kemahasiswaan Fakultas Hukum UPNVJ.

Oleh karena itu diperlukan sekali sistem inforrmasi layanan surat elektronik pada Fakultas Hukum UPNVJ. Sistem ini akan memudahkan mahasiswa dan juga pihak Fakultas Hukum UPNVJ. Dengan adanya sistem ini mahasiswa dapat melakukan pencetakan surat yang mudah, kemudian pihak Fakultas dapat bekerja lebih efisien ketimbang sistem yang lama.

# **Analisis PIECES**

tabel 2. 1 Analisis PIECES

|No|PIECES|Sistem saat ini|Sistem Usulan|
|---|---|---|---|
|1|Performance|Pada sistem yang berjalan|Pada sistem yang disulkan|
|||saat ini<br>masih dilakukan manual|proses pengajuan surat<br>akan dapat otomatis|
|||melalui gform yang|tercetak jika approval|
|||tersedia di website|pengajuan dari pejabat|
|||FakultasHukumUPNVJ|Fakultas diterima|

|2|Information|• Mahasiswa tidak dapat<br>melacak proses<br>pengajuan surat.<br>• Arsip surat fisik yang<br>banyak menyulitkan<br>Fakultas untuk<br>pencarian surat yang<br>lama.|• Pelacakan status surat:<br>Mahasiswa dan staf<br>dapat memantau status<br>proses surat.<br>• Semua surat tersimpan<br>secara digital dan dapat<br>diakses setiap saat..|
|---|---|---|---|
|3|Economic|Pada sistem berjalan saat<br>ini Fakultas memerlukan<br>anggaran membeli cap<br>stempel, pulpen, serta<br>kertas untuk print surat<br>yang akan diambil di<br>ruangan layanan<br>kemahasiswaan Fakultas<br>Hukum UPNVJ|Pada sistem yang akan<br>diusulkan Fakultas dapat<br>mengirim surat melalui<br>Sistem tanpa adanya<br>pengeluaran biaya|
|4|Control|• Mahasiswa hanya dapat<br>mengajukan Surat pada<br>saat jam kerja<br>• Dengan sistem saat ini,<br>surat kemungkinan<br>akan terjadi missing<br>(kehilangan surat)<br>• Dengan pendataan<br>melalui google form,<br>kemungkinan ada pihak<br>dari luar yang memakai<br>NIM orang lain untuk<br>spam pengajuan|• Sistem dapat terbuka<br>terus menerus oleh<br>Mahasiswa tanpa harus<br>menunggu jam kerja<br>• Dengan sistem yang<br>akan diusulkan, maka<br>surat terdata dengan<br>detail<br>• Dengan pendataan<br>sistem yang akan<br>diusulkan, pengajuan<br>hanya dapat diajukan<br>oleh mahasiswa<br>Fakultas Hukum<br>dnegan menggunakan<br>akun Siakadnya.|
|5|Efficiency|Pada sistem yang berlaku<br>saat ini, administrasi<br>pelayanan surat masih<br>dilakukan secara manual,<br>sehingga membutuhkan<br>lebih banyak waktu dan<br>tenaga.|Pada sistem yang<br>diusulkan, administrasi<br>pelayanan surat-menyurat<br>akan dilakukan secara<br>otomatis, sehingga tidak<br>membutuhkan waktu dan<br>tenaga ekstra.|
|6|Service|<br>Pengelolaan data<br>mahasiswa saat ini masih<br>dilakukan secara manual,<br>yang memakan waktu dan<br>sering kali tidak akurat.<br>Hal ini memperlambat<br>respons fakultas dalam|<br>Dengan sistem yang<br>diusulkan, sistem akan<br>mengelola data yang<br>mengajukan surat, lalu<br>hanya butuh approval dari<br>Fakultas dan surat akan<br>tercetak otomatis.|

|memberikan surat kepada<br>mahasiswa yang|
|---|
|membutuhkan waktu<br>cepat.|

# **2.2 Sistem usulan**

Dari observasi yang kami lakukan, kami menemukan sistem usulan yang mungkin dapat memenuhi kebutuhan sistem layanan surat Fakultas Hukum UPNVJ.

UML adalah sebuah metode visualisasi untuk merancang sistem berorientasi objek. UML telah menjadi standar untuk visualisasi, perancangan, dan pendokumentasian sistem perangkat lunak. UML juga berfungsi sebagai alat bantu dalam pengembangan sistem. Saat ini, UML dianggap sebagai bahasa standar dalam pembuatan blueprint perangkat lunak. Kelebihan UML mencakup kemampuannya sebagai blueprint yang sangat lengkap dan detail dalam perancangan, memberikan informasi mendetail tentang koding program, serta cocok untuk memodelkan sistem berorientasi objek, bukan hanya perangkat lunak.

Mengacu pada Riri Fitri Sari dan Ardiati (2021:107), UML merupakan bahasa yang berfungsi untuk menggambarkan, memvisualisasikan, merancang, serta mendokumentasikan berbagai artefak dalam sistem perangkat lunak, baik yang sedang dalam tahap perancangan maupun pengembangan.

Kemudian menurut Munawar (2021:49), Unified Modeling Language UML merupakan alat yang sangat bermanfaat dalam pengembangan sistem berbasis objek. Bahasa pemodelan visual ini memberikan pengembang kemampuan untuk menciptakan cetak biru dari visi mereka dalam format standar yang mudah dimengerti, sekaligus menyediakan mekanisme yang efisien untuk berbagi dan mengkomunikasikan rancangan tersebut.

Berdasarkan uraian tersebut, dapat disimpulkan bahwa UML merupakan standar yang digunakan untuk memvisualisasikan, merancang, serta mendokumentasikan sistem perangkat lunak. Dalam pembuatan diagram UML, terdapat berbagai jenis komponen, antara lain:

# • **Activity Diagram**

Activity Diagram adalah representasi visual yang menggambarkan alur aktivitas dalam program yang sedang dikembangkan. Diagram ini mencakup tahapan awal, kemungkinan keputusan yang diambil selama proses berlangsung, hingga mencapai tahap akhir dari sistem tersebut. Adapun

beberapa elemen yang terdapat dalam Activity Diagram meliputi:

<!-- Start of picture text -->
[No[  Simbol | Keeterangan |<br>Pe} Co] me |<br>4 Pilihan untuk pengambilan<br>keputusan<br>Fork ; digunakan untuk<br>menunjukkan kegiatan yang<br>5 dilakukan secara pararel atau untuk<br>menggabungkan dua kegiatan<br>pararel menjadi satu<br><!-- End of picture text -->

gambar 2. 5 Simbol activity diagram

- **Use case Diagram**

Use Case Diagram adalah sebuah model yang menggambarkan bagaimana sistem informasi yang akan dikembangkan berperilaku. Diagram ini bertujuan untuk mengenali berbagai fungsi dalam sistem informasi serta pihakpihak yang memiliki akses atau dapat menggunakan fungsi-fungsi tersebut. Beberapa simbol yang terdapat dalam Use Case Diagram di antaranya:

<!-- Start of picture text -->
es Mewakili peran orang, sistem yang lain,<br>atau alat ketika berkomunikasi dengan<br>use case<br><<include> > seluruhnyaMenunjukkanmerupakanbahwa suatufungsionalitas use case<br>dari use case lainnya<br><<Extend>> Menunjukkan bahwa suatu use case<br>seluruhnya merupakan tambahan<br><----- fungsional dari use case lainnya jika<br>suatu kondisi terpenuhi<br>|| Association] aktor dengan use case<br>Ss | ——> Menunjukkan penghubung antara<br>)+ {Co : stem Merupak“stem s care a n bagian ferpatss menspesifikast<br>Use Case | Merupakansistem dan abstraksiaktor dari interaksi antara<br><!-- End of picture text -->

gambar 2. 6 Simbol use case diagram

# • **Class diagram**

Class diagram merupakan diagram yang menunjukkan struktur dan hubungan antar kelas dalam suatu sistem. Diagram ini termasuk dalam bagian dari Unified Modeling Language (UML) yang diterapkan dalam pemrograman berorientasi objek (Object Oriented Programming). Beberapa elemen yang terdapat dalam class diagram antara lain:

<!-- Start of picture text -->
GAMBAR NAMA KETERANGAN<br>Hubungan dimana objek anak (descendent)<br>Generalization | berbagi perilaku dan struktur data dari objek<br>yang ada di atasnya objek induk (ancestor).<br>2 Nary Upaya untuk menghindari asosiasi dengan<br>Association lebih dari 2 objek.<br>atribut serta operasi yang sama.<br>>| eS] | va “re es2<br>ert Deskripsi dari urutan aksi-aksi yang<br>4 4 J Collaboration | ditampilkan sistem yang menghasilkan<br>Soe suatu hasil yang terukur bagi suatu actor<br>Operasi yang benar-benar dilakukan oleh<br>5 Realization | suatu objek.<br>Hubungan dimana perubahan yang terjadi<br>_ | pada suatu elemen mandini (independent)<br>------> Dependency akan mempegaruhi elemen yang bergantung<br>padanya elemen yang tidak mandiri<br>Apa yang menghubungkan antara objek satu<br>7 Association | dengan objek lainnya<br><!-- End of picture text -->

gambar 2. 7 Simbol class diagram

- **Sequence diagram**

Sequence diagram, atau diagram urutan, merupakan representasi visual yang digunakan untuk menggambarkan dan menjelaskan secara rinci interaksi antar objek dalam suatu sistem. Beberapa elemen yang terdapat dalam sequence diagram antara lain:

<!-- Start of picture text -->
ee<br>ee<br>Gambaran sistem sebagai<br>Entity Class landasan dalam menyusun<br>basis data<br>Boundary Class antar lingkungan sistem<br>re) Menangani komunikasi<br>Bertanggung jawab<br>Conic Class terhadap kelas-kelas.<br>terhadap objek yang berisi<br>logika<br>PL =| _—<br>a Mewakili proses durasi<br>tf—<br>Komponen yang<br>Life Line digambarkan garis putus<br>terhubung dengan objek<br><!-- End of picture text -->

gambar 2. 8 Simbol Sequence diagram

- 2.2.1 Use case Sistem usulan layanan surat

Berikut adalah use case diagram yang telah dibuat :

<!-- Start of picture text -->
‘oom enor Cooma X\h /<br>a4 \ VAY<br>_ \|\/<br>eau» L<br>vail J)<br>| \\<br>ay [HV<br>— ae iVi<br>‘uanasiena \\ consis ‘<cextonid> “eorend>> “eee . NfNf /| | \/\ 7ont<br>\ ‘ema perme (Penggantan Oospem) \ | |<br>\\ ™ \y |<br>\ | VY<br>\ / AJ<br>NN | TX —<br>a/<br>// /<br>: Since / / /<br>(YV///<br>Y/ / y \ ¢<br>Y/A _—<br>betan<br><!-- End of picture text -->

gambar 2. 9 Use case diagram sistem usulan

# 2.2.2 Activity Diagram login

Berikut adalah activity diagram login yang telah dibuat:

<!-- Start of picture text -->
[togin user Sistem | atabase<br>Isi NIP / NIK / NIM Cok database<br>dan password |<br>Sudah<br><!-- End of picture text -->

gambar 2. 10 Activity diagram login

- 2.2.2 Activity diagram pengajuan Surat keterangan Mahasiswa aktif

Berikut adalah activity diagram Surat keterangan mahasiswa aktif yang telah

dibuat :

<!-- Start of picture text -->
re | Sistem | atabase |<br>Pilih menu surat , .<br>keterangen mhe akti Menampilkan formulir<br>Mengisi formulir | Sudah<br>Submit pengajuan lengkap? Simpan Data<br><!-- End of picture text -->

gambar 2. 11 Activtiy diagram surat ket mhs aktif

2.2.3 Activity diagram surat pengantar riset

Berikut adalah activity diagram Surat pengantar riset yang telah dibuat :

<!-- Start of picture text -->
Pilih menu surat Menampilkan formulir<br>pengantar riset |<br>Mengisi formulir<br>Submit pengajuan; | lenglan?Sudah Simpan/ Data<br><!-- End of picture text -->

_gambar 2. 12 Activity diagram surat pengantar riset_

- 2.2.4 Activity diagram surat permohonan susulan UTS/UAS

Berikut adalah activity diagram Surat permohonan susulan ujian yang telah

dibuat :

<!-- Start of picture text -->
[Perera | Sistem | atabase |<br>Pilih menu surat<br>permohonan susulan Menampilkan formulir<br>UTS/UAS .<br>Mengisi formulir | Sudah<br>Submit pengajuan lengkap? Simpan Data<br><!-- End of picture text -->

gambar 2. 13 Activity diagram surat permohonan susulan ujian

- 2.2.5 Activity diagram pengajuan surat penggantian dospem TA

Berikut adalah activity diagram Surat penggantian dospem TA yang telah dibuat

:

<!-- Start of picture text -->
dospem TA<br>Pilih menu surat Menampilkan formulir<br>pengantar riset 5<br>Mengisi formulir | Sudah<br>Submit pengajuan lenatan? Simpan Data<br><!-- End of picture text -->

gambar 2. 14 Activity diagram surat penggantian dospem TA

- 2.2.6 Activity Diagram admin persuratan / kemahasiswaan

Berikut adalah activity diagram admin persuratan yang telah dibuat :

<!-- Start of picture text -->
Pilih menu surat a pengajuanMenampiikanSurat KetTa Mh,| Mengambil data<br>[Surat susulan ujian, Surat]<br>penagantian dospem<br>Memberikan aksi Memberikan aksi | Approval dit<br>Decline pt \pproval diterima<br>Simpan Data<br>Menampilkan alasan<br>~ oe<br><!-- End of picture text -->

gambar 2. 15 Activity diagram admin persuratan

- 2.2.7 Activity diagram Kaprodi

Berikut adalah activity diagram Kaprodi yang telah dibuat :

<!-- Start of picture text -->
Pilih menu surat 7 JpengajuanMenampikanSurat KetTs Mhs,| Mengambil data<br>surat pengantar riset,<br>Surat susulan ujian<br>Memberikan aksi Memberikan aksi | suratteroetok<br>Deeline Accept<br>Simpan Data<br>Menampilkan alasan<br>~ oe<br><!-- End of picture text -->

gambar 2. 16 Activity diagram Kaprodi

- 2.2.8 Activity diagram Wadek 1

Berikut adalah activity diagram Wakil dekan 1 yang telah dibuat :

<!-- Start of picture text -->
Pilih menu surat |7beeMenampilkanpengajuan dospemSurat list TA Mengambil data<br>Dapat membaca<br>data list pengajuan<br>surat<br><!-- End of picture text -->

gambar 2. 17 Activity diagram wadek 1

- 2.2.9 Activity diagram Dekan

Berikut adalah activity diagram Dekan yang telah dibuat :

<!-- Start of picture text -->
ee<br>Pilih menu surat - Monampiicen let Surat Mengambil data<br>ZZ pengantar riset.<br>Memberikan aksi Memberikan aksi | ‘Surat tercetak<br>Decline Accept<br>Simpan Data<br>Menampilkan alasan<br>~ oe<br><!-- End of picture text -->

gambar 2. 18 Activity diagram dekan

# 2.2.10 Sequence diagram Login

Berikut Sequence diagram Login yang telah dibuat:

<!-- Start of picture text -->
Halaman<br>| 1. Isi Form Login | H '<br>7 7 2. Data Login 3. isi NIM/NIP/NIK dan<br>' ' password<br>| | 8. Data Tidak Valid 4. Tidak Valid<br>: 9.PesanKesalahan = :<br>‘ | | 5. Data Valid ;<br>| 7. Dashboard Tampil H 6. Menampilkan Hi :<br>' Dashboard ' '<br><!-- End of picture text -->

gambar 2. 19 Sequence diagram Login

- 2.2.11 Sequence diagram pengajuan surat keterangan mahasiswa aktif

Berikut Sequence diagram Surat ket. Mahasiswa aktif yang telah dibuat :

<!-- Start of picture text -->
1. Buka Menu Surat ket mhs i<br>aktif :<br>2. Menampilkan 7<br>formulir 2<br>4. Simpan Data<br>H 3. Isi data form :<br>5. Pengajuan surat berhasill : H<br><!-- End of picture text -->

gambar 2. 20 Sequence diagram Surat ket mhs aktif

- 2.2.12 Sequence diagram surat pengantar riset

   - Berikut Sequence diagram Surat pengantar riset yang telah dibuat :

<!-- Start of picture text -->
41. Buka Menu Surat pengantar riset :<br>2. Menampilkan j<br>formulir :<br>4. Simpan Data<br>H 3. Isi data form ‘<br>5. Pengajuan surat berhasill : :<br><!-- End of picture text -->

gambar 2. 21  Sequence diagram surat pengantar riset

- 2.2.13 Sequence diagram pengajuan susulan uts/uas

   - Berikut Sequence diagram pengajuan susulan ujian yang telah dibuat :

<!-- Start of picture text -->
1. Buka Menu Surat permohonan susulan uts/uas :<br>2. Menampilkan 7<br>formulir<br>4. Simpan Data<br>H 3. Isi data form '<br>5. Pengajuan surat berhasill ' :<br><!-- End of picture text -->

gambar 2. 22 Sequence diagram surat permohonan ujian susulan

- 2.2.14 Sequence diagram pengajuan ganti dospem TA Berikut Sequence diagram pengajuan ganti dospem TA yang telah dibuat :

<!-- Start of picture text -->
1. Buka Menu Surat pengajuan ganti dospem TA j<br>2. Menampilkan j<br>formulir :<br>4. Simpan Data<br>H 3. Isi data form ‘<br>5. Pengajuan surat berhasill : :<br><!-- End of picture text -->

gambar 2. 23 Sequence diagram surat pengajuan ganti dospem TA

- 2.2.15 Sequence diagram admin persuratan

Berikut Sequence diagram admin persuratan yang telah dibuat :

<!-- Start of picture text -->
List pengajuan<br>‘2. Tampil Data Peserta H '<br>' ' 5. Simpan Data<br>! 3. Accept Peserta 4. Surat berhasildi approve: -<br>' 3.1 Tolak Peserta & ' 4. 1 Menampilkan<br>|” Masukan alasan ' notifikasi alasan 5.1 Simpan Data<br><!-- End of picture text -->

gambar 2. 24 Sequence diagram admin persuratan

- 2.2.16 Sequence diagram kaprodi

Berikut Sequence diagram Kaprodi yang telah dibuat :

<!-- Start of picture text -->
List pengajuan<br>1. Buka Menu Surat ket mhs ' : '<br>aktif, pengantar riset, ' :<br>permohonan susulan uts/uas ' '<br>2. Tampil Data Peserta H H<br>' ' 5. Simpan Data<br>! 3. Accept Peserta 4.’Surat berhasil dicetak ! -<br>' 3.1 Tolak Peserta & ' 4. 1 Menampilkan<br>|” Masukan alasan ' notifikasi alasan 5.1 Simpan Data<br><!-- End of picture text -->

gambar 2. 25 Sequence diagram Kaprodi

- 2.2.17 Sequence diagram Wadek 1

Berikut Sequence diagram Wadek 1 yang telah dibuat :

<!-- Start of picture text -->
Wadek 1 Halaman Sistem Database<br>List pengajuan<br>1, Buka Menu Surat : H :<br>permohonan susulan UTS/UAS : H :<br>:2. Tampil Data Peserta : H<br>' : 5. Simpan Data<br>‘3. Accept Peserta 4.’Surat berhasil dicetak -<br>+ 3.1 Tolak Peserta & ‘4. 1 Menampilkan =<br>|” Masukan alasan '  notifikasi alasan 5.1 Simpan Data<br><!-- End of picture text -->

gambar 2. 26 Sequence diagram Wadek  1

# 2.2.18 Sequence diagram Dekan

Berikut Sequence diagram Dekan yang telah dibuat :

<!-- Start of picture text -->
Halaman Sistem Database<br>List pengajuan<br>1. Buka Menu Surat pengantar : ' :<br>riset : : !<br>'2. Tampil Data Peserta : '<br>: : 5. Simpan Data<br>! 3. Accept Peserta 4.'Surat berhasil dicetak :<br>' 3.4 Tolak Peserta& ' 4. 1 Menampilkan<br>!Masukan alasan !  nofifikasi alasan 5.1 Simpan Data<br><!-- End of picture text -->

gambar 2. 27 Sequence diagram dekan

2.2.19 Class diagram

Diagram class ini memberikan gambaran yang cukup jelas tentang struktur data yang digunakan untuk mengelola berbagai jenis surat di Fakultas Hukum UPNVJ. Dengan melihat diagram ini, kita dapat memahami jenis data yang disimpan, hubungan antar data, dan bagaimana data tersebut dikelola dalam sistem.

Berikut Class diagram yang kami buat :

<!-- Start of picture text -->
[erste | kee<br>fa big fesuratsicine<br>lid_mahasiswa: bigint Jek = double<br>jens mat vera)<br>jeis_suratskadork try fomat:varenaflamat: text<br>id= bigint ro surat: varchar N is: anun(UTS, UAS)<br>isurat bint ecuereated-at:1d: chartimestamp plasenfret: watbt<br>IpkPhone : double varenar lupdated_at : timestamp lace.josen_pengampu admin  enum( : Pending.text ‘isetyu, “tol<br>Smt vere ferotakan admin text<br>gma vac fre: kaprod: enum( Pending, “isety, ‘oak<br>dosen_lama : varchar ppencianen. pepo: tent<br>flonan: text errand<br>judul_penelitian ; text vs_lampiran : varchar<br>fec_agmins enunt Pending fe_sspred: ign<br>Disetuju'’’Ditolak’) foreated_at : umestamp<br>penolakan_admin : text Pat: Sate<br>fice. wadek: enum( Pending<br>penolakan_wadekDisa Diolak) text [___Monasiova|<br>Createdat: timestamp la bin<br>Updated.at: timestamp haverim: varchariit<br>nama varenar<br>prod: varchar<br>angkatan:vrchar<br>ereate, at: tmostamp<br>Lpdated_at: timestamp<br>14 bigit<br>id_surat bint<br>ink doube,<br>phono varchar<br>tal: varchar<br>fama wnt<br>Denolakan_keperuan:oxtaceDistradmin:Dtolak) ain: enum( Pending ext idame{icmamebigntvarcharvarchar idi_suratipk bintdoubie.igi<br>ce kaprod enum Pending ‘ole: varchar pone varchar<br>Disetujur’’Ditolak’)perolakan_kaprod:F-kaprod ign unsignedext fomamber‘email_verified_atbassword varchartoken: varchar:timestamn¢ ‘emailSlamateperuan:toxt: varchartext<br>createdUpdated.at:at: timestamp timestamp Createdupdotod_at:at: timestamptmestamp juinatans: penetiantext :toxt<br>{ace_kaprodenum( Pending, "hse, ‘Doak)<br>[eee] Berolakan kaprod text<br>|| 'cz_dekanIddekan  :“big enum Pending ‘iseiju,‘iolak)<br>iaitor Bit bigint ponolakan_dekan: text<br>nipama varcharvorehar createdUpcated-at:at: timestamp timestamp<br>focesstreated varchar<br>Updatedat timestamp<br>at timestamp<br><!-- End of picture text -->

gambar 2. 28 Class Diagram

# **2.3 Desain dan fitur**

- 2.3.1 Tampilan login awal

Berikut tampilan login awal, mahasiswa akan login menggunakan akun siakad, sedangkan pejabat fakultas menggunakan akun yang dibuat oleh admin master.

<!-- Start of picture text -->
©)<br><!-- End of picture text -->

gambar 2. 29 Tampilan login

- 2.3.2 Tampilan Pengajuan surat untuk user Mahasiswa

Berikut tampilan menu layanan surat di akun mahasiswa dengan 4 menu pilihan pengajuan surat, mahasiswa akan memilih surat yang dibutuhkan untuk melakuan pengajuan kepada fakultas.

<!-- Start of picture text -->
Fakuitas Hukum<br>Layanan Surat<br>‘Surat Keterangen ‘Surat Permohonsn Susulan ‘Surat Usuian Penggantion<br><!-- End of picture text -->

gambar 2. 30 Tampilan dashboard mahasiswa

- 2.3.3 Tampilan pengajuan surat keterangan mahasiswa aktif

Berikut tampilan formulir pengajuan surat keterangan mahasiswa aktif, yang dimana mahasiswa perlu menyisipkan lampiran scan KHS dan bukti pembayaran terakhir agar mempermudah admin untuk proses pengecekan.

<!-- Start of picture text -->
Fakultas Hukum Layanan Surat<br>Surat Keterangan Mahasiswa Aktif<br><!-- End of picture text -->

gambar 2. 31 Tampilan formulir pengajuan surat ket mhs aktif

- 2.3.4  Tampilan pengajuan surat pengantar riset

   - Berikut tampilan formulir pengajuan surat pengantar riset.

<!-- Start of picture text -->
GG) Fatuttas Hokum Layanan Surat<br>(Oo<br>fs Penoshensunt Surat Pengantar Riset<br><!-- End of picture text -->

gambar 2. 32 Tampilan formulir surat pengantar riset

# 2.3.5 Tampilan formulir surat permohonan susulan UTS/UAS

Berikut tampilan formur pengajuan surat permohonan susulan UTS/UAS.

<!-- Start of picture text -->
Fakultas Hukum Layanan Surat<br>[i rossnonsint | Surat Permohonan UTS / UAS Susulan<br><!-- End of picture text -->

gambar 2. 33 Tampilan formulir permohonan susulan ujian

- 2.3.6 Tampilan formulir surat penggantian dospem TA

   - Berikut tampilan formulir pengajuan penggantian dospem TA.

<!-- Start of picture text -->
Fakultas Hukum Layanan Surat<br>= "Surat Permohonan Penggantian Dosen Pembimbing TA<br>© Riwayat Pengajuan Surat — wn :<br><!-- End of picture text -->

gambar 2. 34 Tampilan formulir penggantian dospem TA

# 2.3.7 Tampilan User Interface Riwayat pengajuan surat

Berikut tampilan riwayat pengajuan surat yang diajukan oleh akun mahasiswa,

akan ditampilkan status approval dari tiap masing-masing surat, dan jika surat sudah memenuhi approval maka surat akan bisa dicetak.

<!-- Start of picture text -->
—<br>Layanan Surat<br>f soess J f cos son)<br>[sions [cnt se]<br><!-- End of picture text -->

gambar 2. 35 Tampilan riwayat pengajuan surat mahasiswa

- 2.3.8 Output surat keterangan mahasiswa aktif

Dari pengajuan, jika sudah di approve oleh fakultas maka mahasiswa dapat mencetak surat seperti berikut:

<!-- Start of picture text -->
KEMENTERIAN PENDIDIKAN TINGGI, SAINS,<br>(fre DAN TEKNOLOGI<br>(; * ) UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN” JAKARTA<br>\2 Fy FAKULTAS HUKUM<br>\? 7 Jalan Rumah Sakit Fatmawati, Pondok Labu, Jakarta Selatan 12450<br>eS Telepon (021) 7656971, Fax. (021) 7656904<br>Laman: hukum.upnyj.ac.id , e-mail: fh@upnyj.ac.id<br>SURAT KETERANGAN<br>NOMOR: 002/UN61/FH/KM/2025<br>Yang bertanda tangan dibawah ini :<br>Nama : Dr. Muthia Sakti, S.H., M.H.<br>Jabatan : Koordinator Program Studi Hukum Program Sarjana<br>Menerangkan bahwa yang tersebut dibawah ini :<br>Nama : Leonardo Andreas Batubara<br>NIM 2 2010611258<br>Semester :9<br>IPK 23.9<br>E-mail 2 tess@gmail.com<br>No. Telp/HP 2 089727281192<br>Benar merupakan mahasiswa Fakultas Hukum UPN “Veteran” Jakarta terakreditasi “Baik<br>Sekali” berdasarkan Surat Keputusan Badan Akreditasi Nasional Nomor: 3850/SK/BAN-<br>PT/AK.KP/S/V/IX/2023 dan aktif kuliah pada Tahun Akademik 2024/2025<br>Demikian surat keterangan ini diberikan untuk dipergunakan sebagai kelengkapan<br>administrasi untuk melamar beasiswa.<br>Jakarta, 16 Januari 2025<br>Koordinator Program Studi Hukum Program Sarjana<br>Bygase see<br>Steet<br>pasha tras<br>fatecse seed<br>Dr. Muthia Sakti, S.H., M.H.<br>NIP. 0031129401<br><!-- End of picture text -->

gambar 2. 36 Output surat ket mhs aktif

# 2.3.9 Output surat pengantar riset

Dari pengajuan, jika sudah di approve oleh fakultas maka mahasiswa dapat

mencetak surat pengantar riset seperti berikut:

<!-- Start of picture text -->
2 KEMENTERIAN PENDIDIKAN TINGGI, SAINS,<br>Le DAN TEKNOLOGI<br>(2 ‘, ) UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN” JAKARTA<br>\e 3] FAKULTAS HUKUM<br>“ y Jalan Rumah Sakit Fatmawati, Pondok Labu, Jakarta Selatan 12450<br>ei Telepon (021) 7656971, Fax. (021) 7656904<br>Laman: hukum.upnyj.ac.id , e-mail: fh@upnyj.ac.id<br>Nomor : 004/UN61/FH/KM/2025 Jakarta, 17 Januari 2025<br>Lampiran : -<br>Perihal —: ‘Permohonan Penelitian<br>Kepada Yth.<br>Pengadilan Negeri Jakarta Selatan<br>di-<br>Jalan fatmawati no.8<br>Dengan Hormat.<br>Bersama ini kami hadapkan mahasiswa dari Fakultas Hukum UPN “Veteran” Jakarta:<br>Nama : Eli Marlina<br>NIM : 2210622031<br>Semester : 5 $2 Hukum<br>IPK 3.47<br>E-mail : tess@gmail.com<br>No. Telp/HP : 082114380390<br>Judul Tesis/Tugas Akhir : "Analisis Perkawinan Beda Agama"<br>Untuk melaksanakan penelitian di instansi Bapak/Ibu untuk keperluan Riset Tesis. Adapun<br>pelaksanaannya disesuaikan dengan jadwal yang ditentukan oleh instansi Bapak/Ibu.<br>Demikian permohonan ini kami sampaikan atas perhatian dan kerjasamanya kami ucapkan<br>terima kasih.<br>Jakarta, 17 Januari 2025<br>Dekan Fakultas Hukum<br>ear:<br>joo eos<br>O¥areut<br>Dr. Suherman, S.H., LL.M<br>NIP. 197006022021211004<br><!-- End of picture text -->

# gambar 2. 37 Output surat pengantar riset

# 2.3.10 Output surat permohonan susulan UTS/UAS

Dari pengajuan, jika sudah di approve oleh fakultas maka mahasiswa dapat mencetak surat permohonan ujian seperti berikut:

<!-- Start of picture text -->
KEMENTERIAN PENDIDIKAN TINGGI, SAINS,<br>Sgr \ DAN TEKNOLOGI<br>‘G *,) UNIVERSITAS PEMBANGUNAN NASIONAL “VETERAN” JAKARTA<br>\e if FAKULTAS HUKUM<br>* / Jalan Rumah Sakit Fatmawati, Pondok Labu, Jakarta Selatan 12450<br>etd Telepon (021) 7656971, Fax. (021) 7656904<br>Laman: hukum.upnyj.ac.id , e-mail: fh@upnyj.ac.id<br>Nomor : 001/UN61/FH/TU/2025 Jakarta, 16 Januari 2025<br>Lampiran : -<br>Perihal : Permohonan Pelaksanaan Ujian Susulan<br>Kepada Yth.<br>Bapak/Ibu Dr. abcd, S.H., M.H.<br>(Dosen Fakultas Hukum UPN “Veteran” Jakarta)<br>di tempat<br>Dengan Hormat.<br>Berdasarkan surat Mahasiswa atas nama Eli Marlina (2210622031) tanggal 16 Januari 2025<br>perihal Surat Permohonan Pelaksanaan Ujian Susulan.<br>Sehubungan dengan hal tersebut di atas, bersama ini disampaikan permohonan kepada<br>Bapak/Ibu agar berkenan dapat memberikan dispensasi/ijin kepada mahasiswa tersebut untuk<br>mengikuti ujian susulan/memberikan tugas sebagai pengganti Ujian Tengah Semester (UTS)<br>pada mata kuliah Pengantar IImu Hukum, karena pada saat UTS mata kuliah tersebut<br>mahasiswa yang bersangkutan sedang Karna sakit.<br>Berikut terlampir Surat Keterangan Sakit dari Dokter untuk menjadi acuan. Demikian surat<br>ini disampaikan, atas perkenan Bapak/Ibu diucapkan terima kasih.<br>Jakarta, 16 Januari 2025<br>Koordinator Program Studi Hukum Program Magister<br>[Oea ear]<br>Paraf Beas<br>: eStore 1p<br>- Kasubag Umum : peahoaes<br>ic OP oe<br>Dr. Atik Winanti, SH, MH<br>NIP. 0008066808<br>Tembusan :<br>1. Wadek I<br>1, Wadek III<br>Fakultas Hukum UPN “Veteran” Jakarta<br><!-- End of picture text -->

# gambar 2. 38 Output surat permohonan susulan ujian

- 2.3.11 Tampilan data usulan penggantian Dospem TA

Berikut tampilan list pengajuan penggantian dospem TA dari akun Wadek 1

gambar 2. 39 List pengajuan penggantian dospem TA

- 2.3.12 Tampilan hasil barcode validasi keaslian surat keterangan mahasiswa aktif

- Berikut tampilan jika barcode yang terdapat pada surat keterangan mahasiswa

- aktif di scan.

gambar 2. 40 Validasi surat ket mhs aktif

- 2.3.13 Tampilan hasil barcode validasi keaslian surat pengantar riset

Berikut tampilan jika barcode yang terdapat pada surat pengantar riset di scan.

gambar 2. 41 validasi surat pengantar riset

- 2.3.14 Tampilan hasil barcode validasi keaslian surat permohonan susulan UTS/UAS

Berikut tampilan jika barcode yang terdapat pada surat permohonan ujian

di scan.

gambar 2. 42 Surat permohonan susulan ujian

- 2.3.15 Tampilan dashboard admin user management

Berikut tampilan dashboard pada akun User management.

<!-- Start of picture text -->
Fakuitas Hukum Layanan Surat<br>e<br><!-- End of picture text -->

gambar 2. 43 Tampilan dashboard admin master

# 2.3.16 Tampilan manajemen user

Berikut tampilan management user, yang dimana admin master dapat menambahkan, menghapus, ataupun mengedit pengguna.

<!-- Start of picture text -->
Fakultes Hukum —-Manajemen Pengguna<br>ss<br>— =<br>(=<br>=<br>=<br>=<br><!-- End of picture text -->

<mark>gambar 2. 44 Tampilan management user</mark>

# 2.3.17 Tampilan penolakan surat

<!-- Start of picture text -->
Layanan Surat<br>Fakultas Hukum<br>Riwayat Pengajuen Surat<br>2 16 Januari 2025 Surat Permohonan jan Bolum Ada<br>4 6danvari202s Surat Keterangan Mahasswa Aki OovUNSVFHIKM/2025 [ soos} ax<br>516 Januari2025, Surat Keterangan Mahasiswa Atif oz/uNeWFHIKM/2025 ap a=<br><!-- End of picture text -->

gambar 2. 45 Tampilan penolakan surat

Berikut tampilan penolakan surat di akun mahasiswa jika terjadi penolakan dalam pengajuan.

# 2.3.18 Tampilan alasan penolakan

Berikut tampilan alasan penolakan jika terjadi penolakan saat pengajuan, alasan

dari fakultas akan dapat terlihat oleh mahasiswa

gambar 2. 46 Tampilan alasan penolakan

# **2. 4 Meta data**

Metadata merupakan informasi yang menjelaskan data lain, termasuk identifikasi, deskripsi, serta lokasi dari konten data tersebut. Metadata memainkan peran krusial dalam menjaga integritas, mengontrol, dan mengelola risiko yang berkaitan dengan konten digital. Oleh karena itu, pengelolaan metadata menjadi penting untuk memastikan perlindungan, identifikasi, dan kemudahan akses terhadap konten digital..

Metadata adalah informasi yang terorganisasi dengan baik yang berfungsi untuk menggambarkan, menjelaskan, dan mempermudah pelacakan data, sehingga memungkinkan data tersebut untuk diakses kembali, dimanfaatkan, serta dikelola dengan lebih efisien. Metadata sering diartikan sebagai data mengenai data atau informasi yang menjelaskan informasi lain. Metadata umumnya hadir dalam format digital, melekat langsung pada berkas tertentu, atau tersimpan dalam basis data dengan standar tertentu.

Berdasarkan pendapat Subli, Sugiantoro, dan Prayudi (2017), metadata dapat didefinisikan sebagai informasi yang terkandung dalam suatu file dan memberikan keterangan tentang file tersebut. Informasi ini mencakup detail mengenai konten data yang dimanfaatkan dalam pengelolaan file atau data pada sebuah basis data.

Sedangkan menurut pendapat Ii Sopiandi (2017), Metadata adalah informasi yang terorganisasi secara sistematis untuk menggambarkan, menjelaskan, menemukan, atau setidaknya mempermudah proses pencarian ulang suatu informasi, serta penggunaannya atau pengelolaannya. Metadata kerap diistilahkan sebagai data tentang data atau informasi yang menjelaskan informasi lain. Metadata ini mencakup rincian mengenai isi data yang dimanfaatkan dalam pengelolaan file atau data dalam sebuah basis data.

<!-- Start of picture text -->
pengpentan_sonpere<br>Eli) =r erat<br>2 i ign 1 bgin(20) unsigned<br>‘¢ id_surat - bigint(20)20) usignedunsigned r Wsdatipk: doubleai) wrsgniad<br>Ink:S double Mo marca 3phone : varchar(255)<br>email: varcher286)<br>© slamatphone“email : varchar(255)varhareesy alaeeerieeee) elo 2) alamat : text<br>» : text jen seat tat @ jenis :enum(UTS"UAS)<br>2 dosen_lamaae a : varchar(255) | See‘# akademik eee : tinyint(t) 9omuithalalasan : texttent<br>@.jatul_penetition text © No_surat: varchar(255) Fa GERLESE<br>seourity_id: char(36)<br>@»02_edminpenolakan_admin :enum(Pending’,DisetujutDitolox) : text ©ae 9aE a0e_sdmin : enum(Pending’,DisetujurDitolak)<br>@ acewadek|Gnum(Pending’DisetujutDitolak) Someta strasione, 0 ace_kaprodt : enum(Pending'/DisetujurDitlak)<br>ee= updated_st:panolaan_wadestimestamptet [SHGE4ie==. matasiowaea | 5peacelarierenieeal@ enis_lampirantmrpenn Zit : varchar255)<br>id_user : bigint(20) unsigned P) TH bacco gina) unolgned<br>updated.<br>Hie ; Ey | 2 at: timestamp J<br>isid bight2.20) unsignedsuratmahasiswa_aktits | 2© ceaied angkatanat: : varchar(255)timesiame i == eee<br>1 surat bigin20)unsignes f |e uedaied attimestep | 1 i bigin2o) unsigned<br>ipk: double | {#1d_surat: bigint20) unsigned<br>penal:ii aivechat2=5) , 1 pt: double<br>slams tex<br>© ognama etaeeaiaey Sineeal varchar)<br>=aca.penclatan_sdmintepeiuanadmin txtenamiPending ist OHia}; | elnanan, aeS eperuan txt<br>ext —_ 5 email veried_et: timestamp Sarl<br>Sy© penoltar_fapod: xt = sees Sper porate she<br>ts=  id_kaprodi : biginti20) unsigned e| pocsietcremate!att | /| 0» penolakan_kaprodiace Japrodl: enum : textPendlngOluiol)<br>ceated_st: timestamp eyes 0 scr detan enum Pend Deli-DAGIaA)<br>aaa teal penchant<br>—______| 1 dean igi 20) signed<br>Ho weit proties |) 3 ceated_at: tinea<br>1 bigint20) ulgned pare ier<br>|i. iser: baka) uated<br>2 lp: varchar36)<br>eee<br>5 acces: vrchri6)<br>|x3 Updated at: timestamp<br><!-- End of picture text -->

gambar 3. 1 Meta data

Dari gambar diatas, berikut ini adalah detail dari setiap rancangan tabel yang

sudah

dibuat, antara lain:

- 2.4.1  Tabel surat_penggantian_dospems

   - Berikut daftar tabel dari surat_penggantian_dospems

tabel 2. 2 tabel surat_penggantian_dospems

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|id|bigint(20)|Primary Key|
|Id_surat|bigint(20)|Foreign key|

|Ipk|double|Not null|
|---|---|---|
|Phone|varchar(255)|Not null|
|Email|varchar(255)|Not null|
|Alamat|text|Not null|
|dosen_lama|Varchar(255)|Not null|
|Alasan|text|Not null|
|judul_penelitian|text|Not null|
|Acc_admin|enum('Pending','Disetujui','Ditolak')|Null|
|penolakan_admin|text|Null|
|Acc_wadek|enum('Pending','Disetujui','Ditolak')|null|
|penolakan_wadek|text|null|
|created_at|timestamp|null|
|updated_at|timestamp|null|

# 2.4.2 Tabel surat_mahasiswa_aktifs

Berikut daftar tabel dari surat_mahasiswa_aktifs

tabel 2. 3 daftar tabel Surat_Mahasiswa_aktifs

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_surat|bigint(20)|Foreign key|
|Ipk|double|Not null|
|Phone|varchar(255)|Not null|
|Email|varchar(255)|Not null|
|Alamat|Text|Not null|
|Keperluan|text|null|
|Acc_admin|enum('Pending','Disetujui','Ditolak')|null|
|penolakan_admin|Text|null|
|Acc_kaprodi|enum('Pending','Disetujui','Ditolak')|null|
|penolakan_kaprodi|text|null|

|Id_kaprodi|bigint(20) unsigned|null|
|---|---|---|
|created_at|timestamp|null|
|Updated_at|timestamp|null|

# 2.4.3 Tabel surat_permohonan_ujians

Berikut daftar tabel dari surat_permohonan_ujians

tabel 2. 4 daftar tabel surat_permohonan_ujians

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_surat|bigint(20)|Foreign key|
|Ipk|double|Not null|
|Phone|varchar(255)|Not null|
|Email|varchar(255)|Not null|
|Alamat|Text|Not null|
|jenis|enum('UTS','UAS')|Not null|
|Alasan|Text|Not null|
|Matkul|text|Not null|
|Dosen_pengampu|text|Not null|
|Acc_admin|enum('Pending','Disetujui','Ditolak')|null|
|penolakan_admin|text|null|
|Acc_kaprodi|enum('Pending','Disetujui','Ditolak')|null|
|Penolakan_kaprodi|text|null|
|lampiran|text|Not null|
|Jenis_lampiran|varchar(255)|Not null|
|id_kaprodi|bigint(20) unsigned|null|
|created_at|timestamp|null|
|Updated_at|timestamp|null|

# 2.4.4 Tabel surat_pengantar_risets

Berikut daftar tabel dari surat_pengantar_risets

tabel 2. 5 daftar tabel surat_pengantar_risets

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_surat|bigint(20)|Foreign key|
|Ipk|double|Not null|
|Phone|varchar(255)|Not null|
|Email|varchar(255)|Not null|
|Alamat|text|Not null|
|Keperluan|text|Not null|
|Instansi|text|Not null|
|Judul_penelitian|text|Not null|
|Acc_kaprodi|enum('Pending','Disetujui','Ditolak')|null|
|penolakan_kaaprodi|text|Null|
|Acc_dekan|enum('Pending','Disetujui','Ditolak')|Null|
|penolakan_dekan|text|Null|
|id_dekan|bigint(20) unsigned|Null|
|created_at|timestamp|Null|
|Updated_at|timestamp|null|

# 2.4.5 Tabel surats

Berikut daftar tabel dari surats

tabel 2. 6 daftar tabel surats

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_mahasiswa|bigint(20)|Foreign key|
|Jenis_surat|text|Not null|

|Done|tinyint(1)|Not null|
|---|---|---|
|akademik|tinyint(1)|null|
|No_surat|varchar(255)|null|
|security_id|Char(36)|null|
|created_at|Timestamp|Null|
|updated_at|timestamp|null|

# 2.4.6 Tabel mahasiswas

# Berikut daftar dari tabel mahasiswa

tabel 2. 7 daftar tabel mahasiswas

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_user|bigint(20)|Foreign key|
|nim|varchar(255)|Not null|
|nama|varchar(255)|Not null|
|prodi|varchar(255)|Not null|
|angkatan|varchar(255)|Not null|
|created_at|Timestamp|Null|
|updated_at|timestamp|null|

# 2.4.7 Tabel users

# Berikut daftar dari tabel user

tabel 2. 8 daftar tabel users

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|id|bigint(20)|Primary key|
|name|varchar(255)|Foreign key|
|username|varchar(255)|Not null|
|role|varchar(255)|Null|
|Email_verfied_at|timestamp|Null|
|password|varchar(255)|Not null|
|Remember_token|varchar(100)|Null|
|Created_at|timestamp|Null|
|updated_at|timestamp|Null|

# 2.4.8 Tabel profiles

Berikut daftar dari tabel profiles

tabel 2. 9 daftar tabel profiles

|**Atribut**|**Tipe data**|**Keterangan**|
|---|---|---|
|Id|bigint(20)|Primary key|
|Id_user|bigint(20)|Foreign key|
|nip|varchar(255)|Not Null|
|nama|varchar(255)|not Null|
|access|varchar(16)|Null|
|created_at|Timestamp|Null|
|updated_at|timestamp|Null|
