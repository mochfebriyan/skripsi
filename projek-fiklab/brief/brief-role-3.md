# Brief Role 3: Pelaksanaan, Evaluasi & Dashboard Skor

26 Oktober 2026 (revisi dari 17 Oktober 2026: scope kelompok berubah) · Febriyan · Bagian dari proyek LabFIK Compliance (lihat [brief-seluruh-projek.md](brief-seluruh-projek.md))

## Ringkasan

- **Apa:** modul Odoo yang mencatat pelaksanaan setiap sesi praktikum LabFIK pada saat sesi berlangsung dan menautkan bukti penilaian praktikan ke sesi tersebut. Modul ini juga menyediakan mesin skor dan *dashboard* untuk kedelapan indikator kelompok, yang bisa ditelusuri sampai ke unit yang belum memenuhi.
- **Indikator yang dipegang:**
  - **Proses 18:** sesi terlaksana sesuai jadwal, modul, dan waktu. Unitnya sesi, levelnya otomatis.
  - **Evaluasi 19:** kompetensi praktikan dinilai secara individual dengan rubrik. Unitnya praktikan, levelnya bukti tertaut.
- ***Dashboard*:** menampilkan skor kedelapan indikator kelompok, yaitu Pengelolaan 4, 10, Pengembangan 13, 14, Persiapan 15, 17, Proses 18, dan Evaluasi 19. Data dan aturan untuk indikator milik Role 1 dan Role 2 berasal dari role masing-masing.
- **Masalah utama:**
  - Persentase Proses 18 saat ini tidak bisa dihitung ataupun diverifikasi. Lebih dari separuh kelas praktikum tidak punya rekaman sama sekali, dan rekaman yang ada dibuat untuk honor, bukan sebagai bukti mutu.
  - Bukti penilaian praktikan ada di LeADS dan presensi rinci ada di SIMPEL, tetapi keduanya tidak terhubung ke rekaman sesi.
- **Posisi sistem:** alat pencatatan, pembuktian, dan pemantauan. Sistem **tidak menjamin** skor naik. Skor tetap ditentukan oleh apakah sesi benar-benar terlaksana dan praktikan benar-benar dinilai.
- **Usulan judul:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan dan Evaluasi Sesi Praktikum serta *Dashboard* Skor Indikator Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

### Perubahan dari versi 17 Oktober

| | Sebelumnya | Sekarang |
|---|---|---|
| Indikator Role 3 | Proses 18 | Proses 18 + **Evaluasi 19** |
| *Dashboard* | 5 indikator, semuanya persentase berunit sesi | 8 indikator dengan unit campuran (sesi, personel–tugas/alat, praktikan, paket dokumen) dan dua jenis skor |
| Mesin skor | Persentase saja | Persentase **dan** kriteria berurutan 1–4 |
| Persiapan 16 | Ditampilkan di *dashboard* | Dikeluarkan dari scope kelompok |
| Judul | "... Perhitungan **Otomatis** Skor ..." | "... *Dashboard* Skor ...", karena tidak semua indikator dihitung otomatis |

## Posisi dalam proyek

| Role | Modul | Indikator | Hubungan dengan Role 3 |
|---|---|---|---|
| Role 1 | Personel: Kompetensi, Penugasan & Otorisasi | Pengelolaan 4, 10 | Memberi petugas per sesi dan data otorisasi personel–tugas/alat. Role 3 mengirim presensi asisten sebagai dasar honor |
| Role 2 | Perencanaan: Pengembangan Lab & Sesi | Pengembangan 13, 14; Persiapan 15, 17 | Memberi master data, sesi rencana, modul berversi, dan data bahan. **Sesi rencana adalah pembagi Proses 18.** Role 3 memberi hasil *dashboard* sebagai data analisis gap Pengembangan 13 |
| **Role 3** | Pelaksanaan, Evaluasi & Dashboard | Proses 18, Evaluasi 19, *dashboard* 8 indikator | Mencatat realisasi, perubahan, sesi pengganti, dan tautan bukti penilaian. Pemilik registri indikator, mesin skor, dan model bukti. Tugas lintas modul: *black box* dan UAT |

Role 3 berada **paling hilir** di putaran per sesi, sekaligus menjadi **titik balik** siklus: hasil *dashboard* kembali menjadi masukan Pengembangan 13. Semua role memakai satu model data sesi praktikum, jadi model ini harus disepakati di awal (lihat *Kontrak data dengan Role 1 & 2*).

## Indikator Proses 18

Isi rubrik dari Instrumen Monev Laboratorium UPNVJ 2026 v1.1:

- **Bunyi:** sesi praktikum terlaksana sesuai jadwal, modul, dan waktu kegiatan yang ditetapkan. Penerapan umum. Penanggung jawab: Dosen dan KaLab.
- **Pembagi:** seluruh sesi praktikum yang **direncanakan** pada periode monev.
- **Pembilang:** sesi rencana yang terlaksana sesuai ketentuan, atau yang diubah secara sah dengan tujuan dan waktu setara.
- **Syarat memenuhi:** kegiatan, durasi, dan tujuan sesuai; perubahan sah; sesi tertunda baru dihitung memenuhi **setelah sesi penggantinya selesai dalam periode pelaporan**.
- **Bukti:** (1) jadwal, (2) jurnal sesi, (3) presensi praktikan, asisten, laboran, dan dosen, (4) modul yang dipakai, (5) *log book* praktikum, (6) perubahan yang disetujui, (7) penggantian sesi.
- **Skor:** dihitung dari persentase. 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1. Bukti yang tidak bisa diverifikasi → 1.

Instrumen mengacu antara lain pada **SNI ISO/IEC 17025:2017**. Butir yang relevan:

- **7.5.1:** rekaman teknis memuat tanggal dan identitas personel, dan "harus direkam pada saat dibuat".
- **7.5.2:** perubahan rekaman harus dapat ditelusuri ke versi sebelumnya, beserta tanggal dan personel yang mengubah.

Dasar resmi bahwa monev 2026 mengarah ke ISO 17025 belum ada; lihat Pertanyaan terbuka.

**Penerjemahan rubrik ke aturan sistem (draf):**

| Kondisi sesi rencana | Hasil |
|---|---|
| Terlaksana pada tanggal dan jam rencana, durasi ≥ ambang, topik sesuai modul pertemuan ke-n, jurnal dan presensi lengkap | Memenuhi |
| Dibatalkan → perubahan disetujui → pengganti selesai dalam periode, dengan durasi dan tujuan setara | Memenuhi |
| Pengganti belum selesai saat periode ditutup | Tidak memenuhi |
| Batal tanpa pengganti, tidak ada jurnal atau presensi, atau durasi kurang | Tidak memenuhi, dengan alasan tercatat |

Dua ambang **belum ditetapkan** oleh instrumen dan perlu diputuskan KaLab: toleransi keterlambatan mulai dan durasi minimal sesi.

## Indikator Evaluasi 19

Nomor 19 di aspek Evaluasi Praktikum dipakai dua baris. Yang dipegang Role 3 adalah baris **penilaian individual**. Baris "ketercapaian CPMK praktikum dianalisis untuk seluruh mata kuliah" **bukan** scope kita.

Isi rubrik dari Instrumen Monev Laboratorium UPNVJ 2026 v1.1:

- **Bunyi:** kompetensi praktikan dinilai secara individual melalui rubrik dan bukti unjuk kerja yang sesuai CPMK. Penerapan umum. Penanggung jawab: Dosen dan asisten.
- **Pembagi:** seluruh **praktikan** yang dinilai pada periode monev. Unitnya berbeda dari Proses 18, yang menghitung sesi.
- **Pembilang:** praktikan yang memiliki penilaian individual lengkap sesuai rubrik dan umpan balik.
- **Syarat memenuhi:**
  - Bukti menunjukkan kemampuan individu.
  - Skor dapat ditelusuri ke rubrik.
  - Remediasi tersedia bila diperlukan.
  - Nilai kelompok tidak menjadi satu-satunya bukti kompetensi individu.
- **Bukti:** (1) rubrik keterampilan/produk, (2) hasil observasi individual, (3) portofolio, (4) umpan balik dan remediasi, (5) moderasi penilaian antarpenilai.
- **Skor:** sama dengan Proses 18 (persentase → 1–4).

**Pendekatan: tautan bukti, bukan input ulang.**

- Penilaian, hasil kerja, dan umpan balik **sudah dikerjakan dosen di LeADS** (LMS kampus).
- Presensi per praktikan per pertemuan **sudah dicatat dosen di SIMPEL**.
- Membangun ulang fitur penilaian di Odoo akan membuat dosen menginput dua kali dan datanya tidak sinkron. Karena itu, pada tahap MVP:

| Aspek | Keputusan MVP |
|---|---|
| Sistem sumber | LeADS (bukti penilaian) dan SIMPEL (presensi rinci) tetap menjadi sumber data |
| Peran Odoo | Menautkan bukti dari kedua sistem ke jurnal sesi (Proses 18), sebagai atribut sesi |
| Presensi tingkat kelas | Tetap dicatat di jurnal sesi Odoo, misalnya 36/40 hadir (Proses 18) |
| Level cakupan | **Bukti tertaut.** Sistem menunjukkan sesi mana yang punya bukti penilaian. Persentase praktikan yang memenuhi tetap diverifikasi penilai dengan membuka tautan |
| Pengembangan berikutnya | Impor ekspor *gradebook* LeADS, lalu integrasi API bila diizinkan UPT TIK. Masuk saran / penelitian selanjutnya |

Hal yang perlu diperhatikan:

- **Beda unit.** Tautan menempel di sesi, sedangkan indikator menghitung praktikan. Jangan mengklaim Evaluasi 19 "dihitung otomatis".
- **Tidak semua sesi ada asesmen.** Perlu disepakati sesi mana yang wajib punya tautan bukti, misalnya dari rencana modul (Persiapan 15, Role 2).
- **Akses.** Tautan LeADS dan SIMPEL kemungkinan butuh login SSO dan hak akses ke *course*. Pastikan KaLab/penilai bisa membukanya, dan siapkan cadangan berupa unggahan file.
- **Tampilan role dosen di LeADS dan SIMPEL belum diketahui.** Belum jelas apakah ada URL per aktivitas atau per pertemuan, apakah penilaian memakai fitur rubrik, dan apakah *course* praktikum terpisah dari teori **[KONFIRMASI]**.
- Rincian atribut dan kolom dibahas saat perancangan (Bab II), tidak perlu dibahas sekarang.

## Kondisi saat ini (*as-is*)

1. **Rencana:** sheet "Alokasi Pertemuan Asisten Praktikum" berisi satu baris per kelas, dengan kolom pertemuan 1–15 + UTS/UAS yang diisi nama asisten. **Kolom Hari dan Jam kosong di semua periode.** Kelas tanpa asisten tetap tercantum, tapi kolom pertemuannya kosong.
2. **Realisasi:** asisten mengisi Google Form "Pelaksanaan Asistensi Praktikum". Isinya tanggal, jam, ruang, pertemuan ke-, jumlah mahasiswa hadir, dosen hadir (ya/tidak), topik, kesiapan sarana, kendala, link modul, dan foto.
3. **Lembar kegiatan kertas:** diisi bersamaan dengan form, hanya sebagai **bukti fisik untuk pengajuan honor ke rektorat**. Isinya tidak memuat rincian kegiatan, dan KaLab sebenarnya tidak terlalu membutuhkannya. Lembar ini **tidak bisa dipakai sebagai *log book* praktikum**.
4. **Rekap:** dilakukan manual di sheet jawaban form. Ada sheet per asisten, per mata kuliah, cek jumlah di kertas, rekap honor (Rp25.000 per sesi), status rekening dan KTP, serta "Ketercakupan Praktikum" (jumlah pertemuan dibagi 16). Sheet ketercakupan itu pada dasarnya **versi manual dari *dashboard* Role 3**.
5. **Penilaian praktikan:** dikerjakan dosen di **LeADS** (tugas, nilai, umpan balik). Tidak ada hubungannya dengan rekaman sesi di Form/Sheets **[KONFIRMASI: fitur rubrik, URL per aktivitas]**.
6. **Presensi rinci praktikan:** dicatat dosen per pertemuan di **SIMPEL**. Form Asistensi hanya mencatat jumlah hadir **[KONFIRMASI: tampilan dan hak akses role dosen/KaLab]**.

Seluruh pencatatan di Form/Sheets dirancang untuk **honor**, sehingga hanya sesi yang punya asisten yang tercatat. Bukti penilaian dan presensi rinci sebenarnya sudah ada, tetapi tersebar di sistem lain dan tidak terhubung ke sesi.

## Temuan data

Sumber: kedua sheet di atas, dibaca penuh pada 17 Oktober 2026. Form berisi 1.103 respons dari 4 periode: 2024/2025 Genap (312), 2025/2026 Ganjil (286), 2025/2026 Genap (466), dan 2026/2027 Ganjil (39, masih berjalan, data sampai 14 Okt 2026). Ada 8 ruang: FIKLAB-201, 301–304, 401–403. Rencana dicocokkan dengan laporan berdasarkan kode MK + kelas + pertemuan ke-.

### Cakupan rencana ↔ realisasi (temuan utama)

| Periode | Kelas praktikum | Kelas tanpa asisten | Sesi berasisten direncanakan | Punya laporan |
|---|---|---|---|---|
| 2025/2026 Ganjil | 71 | 40 (56%) | 351 | 260 (**74%**) |
| 2025/2026 Genap | 79 | 33 (42%) | 644 | 415 (**64%**) |
| 2026/2027 Ganjil* | 72 | 40 (56%) | 303 | 34 (11%) |

\* Masih berjalan, jadi bukan baseline.

- Kelas tanpa asisten **tidak punya rekaman apa pun**. Pembagi Proses 18 mencakup kelas-kelas ini, sehingga skor saat ini praktis tidak dapat diverifikasi.
- Untuk sesi berasisten saja, cakupannya 64–74%, setara skor 1–2.
- Ada 30 laporan (15 per periode) yang tidak ada di rencana.

### Kualitas rekaman

| Temuan | Angka | Kaitan |
|---|---|---|
| Keterlambatan pengisian (median) | 1 hari (2024/2025 Genap, 2025/2026 Ganjil); **30 hari** (2025/2026 Genap) | ISO 7.5.1: "direkam pada saat dibuat" |
| Laporan > 30 hari setelah sesi | 25% / 11% / **50%** (2024/2025 Genap / 2025/2026 Ganjil / 2025/2026 Genap) | Sama |
| Durasi tidak valid (jam selesai < jam mulai, salah AM/PM) | 140 laporan (13%) | Perlu validasi input |
| Tanggal salah tahun (2005/2006) | 5 | Perlu validasi input |
| Hari tidak cocok dengan tanggal | 55 | Perlu validasi input |
| Laporan ganda (MK, kelas, pertemuan sama) | 48 | Perlu constraint unik per sesi |
| Sesi dilaporkan asisten berbeda dari rencana | 35 (2025/2026 Genap), 1 (2025/2026 Ganjil) | Penggantian asisten tidak tercatat |
| Sesi "online/Zoom/GMeet" tanpa catatan persetujuan | ±50 | Perubahan sesi tidak tercatat |
| Durasi median | 100 menit (Ganjil) vs 50 menit (2025/2026 Genap) | Tidak ada durasi rencana, jadi syarat "durasi sesuai" tidak bisa dinilai |
| Format nama MK | Berubah tiap periode (tanpa kode, kode di belakang, kode di depan) | Perlu master MK (Role 2) |
| Presensi laboran | Tidak ada | Bukti (3) tidak lengkap |
| Presensi praktikan | Hanya jumlah, tidak per nama | Bukti (3) lemah |
| Dosen hadir "Ya" | 50% / 38% / 88% / 95% per periode | — |
| Field rinci "Kehadiran Dosen Praktikum" | Baru terisi 3,5% (field baru) | — |
| Link modul terisi | 92% secara keseluruhan; 27% kosong di 2024/2025 Genap | Modul diunggah saat atau setelah sesi, tanpa versi (Persiapan 15, Role 2) |
| Kesiapan sarana | Siap 998, Dapat disesuaikan 84, Belum siap 11 | Diisi asisten, bukan laboran (Persiapan 16, kini di luar scope kelompok) |
| Rekap honor form vs lembar kegiatan | Selisih pada 7 dari 21 asisten yang punya data | Data untuk Role 1 |

**Catatan privasi:** kedua sheet memuat nama, NIM, nomor HP, dan status rekening/KTP asisten. Data seed, demo, dan lampiran wajib dianonimkan. Minta izin KaLab sebelum angka-angka ini dikutip di proposal.

## Temuan dari kode yang ada (modul Rafika + OpenEduCat)

- **Platform:** Odoo 17 (`'version': '17.0.1.0'`). Modul `PendaftaranAsisten` bergantung pada `openeducat_core`, `openeducat_admission`, `openeducat_attendance`, dan `openeducat_timetable`.
- **`op.session` sudah dipakai Rafika** sebagai sesi bertanggal, dengan `start_datetime`, `end_datetime`, dan state `draft/confirm/done/cancel`. Lihat `asprak_allocation.py` (alokasi) dan `self_allocation.py` (cek bentrok). Model ini sebaiknya di-*inherit* menjadi sesi praktikum, bukan membuat model baru.
- **`jadwal.praktikum` hanya template mingguan** (hari + jam), bukan sesi bertanggal.
- **Presensi OpenEduCat** (`op.attendance.sheet`/`op.attendance.line`) terhubung ke `op.session`, tetapi **hanya untuk mahasiswa** (`op.student`). Presensi asisten, laboran, dan dosen harus ditambahkan.
- **`lab.readiness.checklist`** terhubung ke fasilitas, bukan ke sesi. Model ini dulu disiapkan untuk Persiapan 16, yang sekarang **dikeluarkan dari scope kelompok**, jadi tidak perlu dihubungkan ke *dashboard*. Kalau Persiapan 16 dipegang kelompok lain, cukup dipastikan datanya bisa merujuk ke sesi yang sama.
- **Ada dua set master data:** `mst_*` milik Rafika (`mst_coursesemt`, `mst_dosen`, `mst_kodekelas`, `mst_periodesemt`) dan `op.course`/`op.faculty`/`op.batch` milik OpenEduCat. **Pilihan ini harus disepakati dengan Role 2.**
- **Field yang belum ada:** waktu aktual, topik dan pertemuan ke-, modul yang dipakai, *log book*, relasi sesi asal ↔ pengganti, dan status perubahan.

## Lingkup modul Role 3

1. **Jurnal sesi:** waktu mulai dan selesai aktual, topik, pertemuan ke-, modul yang dipakai (ditautkan ke modul berversi milik Role 2), kendala, dan foto. Jurnal hanya dibuka pada hari sesi dan dikunci setelah batas waktu. Ini menjawab masalah keterlambatan.
2. **Presensi empat pihak:** asisten, laboran, dan dosen dicatat di Odoo. Praktikan dicatat **di tingkat kelas** (jumlah hadir per sesi), sedangkan presensi rinci per praktikan **ditautkan dari SIMPEL** dan tidak diinput ulang. Pemakaian `op.attendance` untuk presensi per nama ditunda sampai ada impor/integrasi SIMPEL.
3. ***Log book* praktikum digital:** isi kegiatan per sesi, menggantikan fungsi bukti yang tidak bisa dipenuhi lembar kertas. *Opsional:* mencetak rekap sebagai bukti fisik honor untuk rektorat, supaya asisten tidak mengisi dua kali (koordinasi dengan Role 1).
4. **Perubahan dan sesi pengganti:** pengajuan perubahan, persetujuan KaLab, sesi pengganti yang terhubung ke sesi asal, dan status yang mengikuti aturan "dihitung setelah pengganti selesai".
5. ***Audit trail*:** riwayat perubahan rekaman (*tracking* `mail.thread`), sesuai ISO 7.5.2.
6. **Tautan bukti Evaluasi 19:** pada jurnal sesi, tautan ke bukti penilaian di LeADS dan presensi rinci di SIMPEL, dengan status verifikasi oleh KaLab/penilai. Lihat bagian *Indikator Evaluasi 19*.
7. **Registri indikator dan mesin skor:**
   - **Registri** berisi kode aspek + nomor + bunyi singkat (karena nomor di instrumen tidak unik), unit hitung, jenis skor, aturan memenuhi, alasan gagal, dan level cakupan (otomatis / semi-otomatis / bukti tertaut).
   - **Mesin skor mendukung dua jenis skor:**
     - **Persentase:** untuk Pengelolaan 4, 10, Persiapan 15, 17, Proses 18, dan Evaluasi 19. Unitnya bisa sesi, personel–tugas/alat, atau praktikan. Ambangnya 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1.
     - **Kriteria berurutan 1–4:** untuk Pengembangan 13 dan 14. Skor naik hanya bila kriteria sebelumnya sudah berbukti. Sistem menunjukkan sampai kriteria ke berapa buktinya ada, lalu skor akhirnya ditetapkan penilai.
   - Skor dihitung per periode monev. Setiap role menyumbang aturan indikatornya sendiri, dan kelompok lain atau kelompok tahun depan bisa menambah indikator tanpa mengubah mesinnya.
8. **Model bukti:** lampiran file atau tautan eksternal per unit atau per kriteria, dengan status verifikasi. Dipakai bersama oleh semua role, terutama untuk Pengembangan 13, 14 (Role 2) dan Evaluasi 19.
9. ***Dashboard*:** skor 8 indikator per periode, dengan level cakupannya ditampilkan.
   - **Indikator persentase:** bisa diklik sampai ke daftar unit yang tidak memenuhi beserta alasannya.
   - **Indikator kriteria berurutan:** menampilkan kriteria yang sudah dan belum berbukti.
   - **Ekspor data:** daftar unit yang tidak memenuhi bisa diekspor sebagai bahan analisis gap Pengembangan 13 (Role 2).
10. **Importer data historis:** sheet Alokasi menjadi sesi rencana, dan form Pelaksanaan menjadi jurnal. Gunanya ada dua: data uji nyata tanpa menunggu modul Role 1/2, dan baseline untuk membandingkan skor manual dengan skor sistem.

## Batasan masalah (usulan)

1. Mitra: praktikum terjadwal di LabFIK UPNVJ (8 ruang). Peminjaman lab untuk kegiatan lain tidak termasuk.
2. Pencatatan dibangun untuk Proses 18, dan penautan bukti untuk Evaluasi 19. *Dashboard* menampilkan 8 indikator kelompok. Data dan aturan Pengelolaan 4, 10, Pengembangan 13, 14, dan Persiapan 15, 17 berasal dari Role 1 dan 2. Persiapan 16 dan 56 indikator monev lainnya tidak dicakup.
3. Tahapan yang dicakup: pelaksanaan sesi, penautan bukti penilaian praktikan, sampai penutupan periode. Rekrutmen, penugasan, otorisasi, penjadwalan, pengembangan lab, pelatihan laboran, dan honor berada di penelitian lain.
4. LeADS dan SIMPEL tetap menjadi sistem sumber untuk penilaian dan presensi rinci praktikan. Penelitian ini tidak membangun fitur penilaian dan tidak mengintegrasikan API keduanya, melainkan hanya menautkan bukti. Persentase praktikan yang memenuhi Evaluasi 19 tetap diverifikasi penilai.
5. Platform Odoo 17 + OpenEduCat, melanjutkan modul Anandar (2026).
6. Data: data historis 2025/2026 Ganjil–Genap yang dianonimkan. **[Putuskan: apakah ada uji coba di semester berjalan?]**
7. Sistem adalah alat pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin indikator terpenuhi dan tidak menggantikan verifikasi asesor monev. Skor otomatis hanya untuk indikator berbasis rekaman operasional di Odoo. Ambang aturan mengikuti ketetapan KaLab.
8. Pengujian: black box dan UAT.

## Kontrak data dengan Role 1 & 2

Field minimum pada sesi praktikum (*inherit* `op.session`) yang perlu disepakati bersama:

| Field | Diisi oleh | Dipakai untuk |
|---|---|---|
| Periode, MK, kelas, ruang, pertemuan ke- | Role 2 | Kunci sesi, pembagi |
| Tanggal dan jam rencana, durasi rencana | Role 2 | "Sesuai jadwal/waktu" |
| Modul berversi untuk pertemuan ke-n | Role 2 | "Sesuai modul", Persiapan 15 |
| Status persetujuan jadwal | Role 2 | Persiapan 15 |
| Kebutuhan dan penerimaan bahan per sesi (bila berlaku) | Role 2 | Persiapan 17 |
| Sesi yang wajib memiliki asesmen | Role 2 (rencana modul), disepakati dengan Role 3 | Pembanding tautan bukti Evaluasi 19 |
| Laboran dan asisten yang ditugaskan, surat tugas | Role 1 | Pengelolaan 4, pembanding presensi |
| Jurnal, waktu aktual, presensi 4 pihak, *log book* | **Role 3** | Proses 18 |
| Status pelaksanaan, perubahan, sesi asal/pengganti | **Role 3** | Proses 18 |
| Tautan bukti LeADS dan SIMPEL, status verifikasi | **Role 3** | Evaluasi 19 |
| Presensi asisten pada sesi terlaksana | Role 3 → Role 1 | Honor |

Selain field sesi, ada kontrak di luar sesi:

| Data | Dari | Ke Role 3 untuk |
|---|---|---|
| Register kompetensi dan otorisasi personel–tugas/alat | Role 1 | Skor Pengelolaan 10 (unitnya pasangan personel–tugas/alat, bukan sesi) |
| Rencana, realisasi, dan bukti per kriteria Pengembangan 13, 14 | Role 2 | Tampilan kriteria berurutan di *dashboard*, memakai model bukti bersama |
| Aturan indikator (unit, pembagi, syarat memenuhi, alasan gagal) | Role 1, Role 2 | Didaftarkan ke registri indikator |
| Daftar unit tidak memenuhi dan tren skor | **Role 3** → Role 2 | Data analisis gap Pengembangan 13 |

## Metode dan pengujian

- **Usulan metode: Water-Scrum-Fall.**
  - *Water*: analisis *as-is*, wawancara, dan desain model data bersama ketiga role.
  - *Scrum*: sprint fitur dengan demo ke KaLab, karena aturan seperti ambang dan prosedur ganti sesi baru akan jelas setelah ada prototipe.
  - *Fall*: black box, UAT, dan *deployment*.
- Ada preseden di UPNVJ 2026: Gulo (Odoo, inventori Puskesmas) dan Permana (Odoo FSM, PT TMD).
- Sebaiknya ketiga role memakai metode yang sama.
- Rujukan metode yang terbit ≥2022 belum diverifikasi. Rujukan asli, West (Forrester, 2011), terlalu tua untuk batas 2022.
- **Evaluasi:** black box, UAT, dan perbandingan skor Proses 18 hitungan manual vs hitungan sistem pada data 2025/2026 Genap. **Kenaikan skor tidak dipakai sebagai ukuran**, karena di luar kendali sistem.

## Struktur proposal (Pedoman TA FIK 2025, jenis Prototipe/Proyek)

- **Bab I:**
  - 1.1 Latar Belakang
  - 1.2 **Identifikasi Masalah** (bukan Rumusan Masalah)
  - 1.3 Batasan Masalah
  - 1.4 Tujuan dan Manfaat
  - 1.5 Jadwal Kegiatan
- **Bab II Rancangan Proyek:**
  - 2.1 Observasi: temuan data detail masuk di sini
  - 2.2 Usulan Solusi: rubrik Proses 18 dan metode
  - 2.3 Rancangan
  - 2.4 Rencana Pengujian
- **Tidak ada bab Tinjauan Pustaka.** Rubrik tetap memberi bobot 20% untuk penguasaan studi terkait, jadi paragraf penelitian terdahulu di Latar Belakang harus kuat.
- **Rubrik penilaian:** kesesuaian judul 15, penerapan teknologi 15, masalah jelas 20, studi terkait 20, **kesesuaian metode 30**.
- **Proposal ditolak** antara lain bila solusi tidak menyelesaikan masalah (3.4c). Karena itu masalah, tujuan, dan fitur dipetakan satu lawan satu (lihat tabel di bawah).
- **Lampiran wajib:** dokumen observasi dan wawancara, serta Surat Keterangan Riset dari LabFIK.
- **Batas waktu:** pengajuan seminar proposal paling lambat minggu ke-10 perkuliahan; similarity maksimal 25%.

**Peta masalah, tujuan, dan fitur:**

| Masalah (1.2) | Tujuan (1.4) | Fitur |
|---|---|---|
| M1. Pelaksanaan sesi tidak terekam utuh dan tidak bisa dipasangkan dengan rencana | T1. Pencatatan pelaksanaan yang terhubung ke sesi rencana, termasuk perubahan dan pengganti | 1, 4, 8 |
| M2. Rekaman tidak memenuhi syarat bukti (terlambat, tanpa laboran, tanpa *log book*, perubahan tidak tercatat) | T2. Rekaman yang dicatat saat sesi, memuat identitas personel, presensi 4 pihak, dan perubahan yang tertelusur | 1, 2, 3, 5 |
| M3. Bukti penilaian individual (LeADS) dan presensi rinci praktikan (SIMPEL) tersebar dan tidak terhubung ke sesi | T3. Penautan bukti penilaian dan presensi rinci ke sesi yang terlaksana, dengan status verifikasi | 6, 8 |
| M4. Skor dihitung manual menjelang monev dan tidak tertelusur ke unit asalnya | T4. Skor Proses 18 dihitung otomatis, dan *dashboard* 8 indikator (persentase dan kriteria berurutan) bisa ditelusuri sampai ke unit yang belum memenuhi | 7, 9 |

**Manfaat:**
- KaLab: bukti siap saat monev, dan kelas tertinggal terpantau sepanjang semester.
- Asisten, laboran, dosen: cukup mencatat satu kali.
- Proyek: mesin skor bisa diperluas ke indikator lain.
- Akademik: contoh penerapan Odoo untuk pembuktian mutu laboratorium.

Jangan menjanjikan kenaikan skor.

## Status draf Bab I

- **26 Oktober 2026:** draf disesuaikan dengan scope baru, yaitu Evaluasi 19 ditambahkan, *dashboard* jadi 8 indikator, dan Persiapan 16 dikeluarkan. Klaim kondisi LeADS dan SIMPEL masih ditandai **[KONFIRMASI]**.
- [Latar Belakang](../pendahuluan/draft/pendahuluan-role-3.md): 5 paragraf (dipadatkan atas permintaan dosen; rincian as-is dan temuan data dipindah ke 2.1 Observasi), beserta daftar pustaka. Sisa placeholder: dasar resmi ISO 17025, data wawancara KaLab, dan metode (usulan Water-Scrum-Fall).
- 1.2 Identifikasi Masalah, 1.3 Batasan Masalah, 1.4 Tujuan dan Manfaat: draf sudah ditulis di file yang sama. Placeholder: nama fase POB (*Execute*), uji coba semester berjalan, dan metode.
- Jadwal Kegiatan: belum.

## Referensi yang sudah diverifikasi

Setiap referensi dicek ke halaman jurnal, PDF, atau abstrak repository.

| Referensi | Dipakai untuk | DOI / tautan | Catatan |
|---|---|---|---|
| Annam *et al.* (2026), JPPIK 4(2) 34–43 | Praktikum penting tapi pelaksanaannya sering belum optimal | 10.29303/jppik.v4i2.1602 | Konteksnya IPA; ganti dengan sumber bidang komputer bila ada |
| Widyantoro *et al.* (2025), *Health Education Laboratory* 1(1) 33–40 | SI lab: inventaris, peminjaman, jadwal, pemakaian | 10.29238/helab.v1i1.2165 | Draf lama salah tulis tahun (2024) |
| Ismail *et al.* (2026), JIP 12(3) 519–528 | E-SPMI: dokumen dan validasi audit mutu internal | 10.33795/jip.v12i3.9580 | Urutan penulis di PDF berbeda dengan di situs jurnal |
| Nurramadhona *et al.* (2025), JIP 12(1) 9–18 | Analisis ketercapaian otomatis + *dashboard*, sumbernya penilaian auditor | 10.33795/jip.v12i1.8432 | Penelitian paling dekat; celah penelitian kita dirumuskan dari sini |
| Nurrohmah & Wiratama (2022), Ultima InfoSys 13(2) 77–84 | Odoo *open source* dan bisa dikustomisasi | 10.31937/si.v13i2.2802 | Terbit online 31 Jan 2023, label volume 2022 |
| Tiara (2026), skripsi UPNVJ | Monitoring IKU, realisasi direkam dan ditautkan ke Repository | repository.upnvj.ac.id/51983 | — |
| Anandar (2026), skripsi UPNVJ | Modul Odoo OpenEduCat tahap perencanaan (Waterfall, SUS 81,88) | repository.upnvj.ac.id/51635 | Pendahulu langsung |
| Odoo S.A. (2023), Security in Odoo 17.0 | Hak akses dan *record rule* per grup | odoo.com/documentation/17.0 | 2023 adalah tahun rilis v17 |
| BSN (2018), SNI ISO/IEC 17025:2017 | 7.5.1–7.5.2 rekaman teknis | — | Lebih tua dari 2022, tapi dipakai karena standar acuan instrumen |
| UPNVJ (2026), Instrumen Monev v1.1 | Rubrik Proses 18, Evaluasi 19, dan 6 indikator kelompok lainnya | Dokumen internal | — |

**Tidak dipakai:** Fahrurrozi (2024), yang dirujuk Rafika, tidak dapat ditemukan.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Role 3 tertahan karena bergantung pada sesi rencana (Role 2) dan penugasan (Role 1) | Sepakati kontrak data di minggu awal. Pakai importer data historis agar bisa jalan sendiri |
| Penguji mempertanyakan klaim "*dashboard* 8 indikator" | Batasan no. 2: aturan 6 indikator lain milik Role 1/2, Role 3 membangun registri, mesin, dan tampilannya |
| Klaim "skor otomatis" dipakai untuk semua indikator | Tampilkan level cakupan per indikator. Yang otomatis hanya Proses 18 (dan indikator Role 1/2 yang berbasis rekaman Odoo). Evaluasi 19 = bukti tertaut, Pengembangan 13/14 = semi-otomatis |
| Tautan LeADS/SIMPEL tidak bisa dibuka penilai (SSO, hak akses, *course* di-*archive*) | Cek hak akses role KaLab sejak awal; siapkan cadangan unggahan file; catat tanggal tautan diinput |
| Mesin skor dirancang hanya untuk persentase berunit sesi | Rancang registri dengan unit dan jenis skor sebagai parameter sejak awal |
| Scope bertambah lagi | Indikator tambahan masuk level bukti tertaut lebih dulu |
| Klaim berlebihan "meningkatkan skor monev" | Pembingkaian sebagai alat bukti dan pemantauan. Evaluasi lewat akurasi skor dan UAT |
| Ambang aturan (telat, durasi) tidak pernah ditetapkan | Jadikan parameter yang bisa diatur KaLab, nilai awalnya hasil wawancara |
| Data pribadi bocor ke lampiran atau demo | Anonimkan saat import, dan jangan *commit* data mentah |
| Kebiasaan lapor terlambat tetap berlanjut | Jurnal dibuka hanya pada hari sesi, dengan notifikasi. Laporan yang telat ditandai sebagai "tidak memenuhi" |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Apa dasar resmi bahwa monev 2026 mengacu ke ISO/IEC 17025?
- [ ] Apakah *dashboard* sebagai mesin skor generik boleh menjadi kontribusi utama Role 3?
- [ ] Apakah ketiga role memakai Water-Scrum-Fall? Di proposal, metode diletakkan di mana?
- [ ] Apakah ada uji coba di semester berjalan, atau cukup data historis?
- [ ] Apakah MVP Evaluasi 19 berupa tautan bukti ke LeADS dan SIMPEL (tanpa input ulang) diterima?
- [ ] Apakah judul baru (tanpa kata "otomatis") disetujui?

**Untuk dosen/asisten (Evaluasi 19)**
- [ ] Di LeADS, apakah penilaian praktikum memakai fitur rubrik? Apakah ada URL per aktivitas yang menampilkan nilai dan umpan balik per mahasiswa?
- [ ] Apakah *course* praktikum di LeADS terpisah dari *course* teori?
- [ ] Di SIMPEL, apakah ada halaman presensi per pertemuan per praktikan? Siapa saja yang bisa membukanya?
- [ ] Untuk tugas kelompok, apakah ada komponen nilai individual?

**Untuk KaLab/PLP (wawancara, wajib sebagai lampiran)**
- [ ] Berapa toleransi keterlambatan mulai dan durasi minimal sesi?
- [ ] Bagaimana prosedur batal dan ganti sesi, dan siapa yang menyetujui? Apakah sesi online dianggap sah?
- [ ] Bagaimana sesi di kelas tanpa asisten berjalan dan dicatat?
- [ ] Di mana jadwal hari dan jam resminya ("Rangkuman Alokasi Slot Praktikum")?
- [ ] Apakah lembar kegiatan kertas juga diisi terlambat bersama form?
- [ ] Apa saja syarat bukti fisik honor dari rektorat?
- [ ] Bolehkah angka dari kedua sheet dikutip di proposal? Apakah LabFIK bisa menerbitkan Surat Keterangan Riset?

**Untuk Role 1 & 2**
- [ ] Master data mana yang dipakai: `mst_*` atau `op.*`?
- [ ] Field kontrak data di atas.
- [ ] Format modul berversi dan penanda sesi yang wajib memiliki asesmen.
- [ ] Format register kompetensi/otorisasi (Role 1) dan bukti per kriteria Pengembangan 13, 14 (Role 2) untuk *dashboard*.
- [ ] Alur presensi asisten → honor.

## Langkah berikutnya

1. Konfirmasi pertanyaan untuk Pak Widi, lalu kunci struktur Bab I dan metode.
2. Wawancara KaLab/PLP dan siapkan dokumen lampirannya.
3. Tulis prosa 1.2–1.4, lalu 1.5 Jadwal Kegiatan (mengacu ke batas minggu ke-10).
4. Rapat kontrak data dengan Role 1 dan 2.
5. Mulai Bab II: 2.1 Observasi dari temuan data di brief ini.
