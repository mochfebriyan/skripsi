# Brief Proyek: LabFIK Compliance berbasis Odoo

*Draf awal, akan disesuaikan setelah wawancara dengan pengelola LabFIK.*

**Anggota & judul:**
- **[Nama 1]**: Pemodelan Arsitektur Enterprise LabFIK Compliance menggunakan ArchiMate
- **[Nama 2]**: Kustomisasi Modul Odoo untuk Pengelolaan Layanan dan Kepatuhan Laboratorium FIK
- **[Nama 3]**: Transformasi Digital Pengelolaan Laboratorium FIK UPN "Veteran" Jakarta

---

## 1. Sedikit latar belakang LabFIK

Laboratorium FIK UPN "Veteran" Jakarta (LabFIK) melayani kegiatan praktikum dan penggunaan fasilitas lab untuk mahasiswa dan dosen FIK. Layanannya saat ini diakses lewat Portal Layanan LabFIK (lab.fik.upnvj.ac.id), yang isinya antara lain:

- Pelaporan kendala/kerusakan fasilitas
- Peminjaman ruang laboratorium dan peminjaman 3D printer
- Lembar penggunaan sarana
- Permintaan penyediaan software untuk praktikum
- Pendaftaran, seleksi, dan pelaksanaan asistensi praktikum
- Survei praktikum dan survei kepuasan layanan

Semua layanan di atas berjalan pakai **Google Form** (ada 9 form + 1 Google Doc). Rekap datanya diolah di **Google Sheets**, dan di portal tersedia sekitar 10 "rangkuman" terpisah, misalnya rangkuman peminjaman, alokasi slot praktikum, dan pelaksanaan asistensi. Artinya, proses manajemen dan pengolahan data kegiatan lab **belum didukung aplikasi**.

Di sisi lain, lab juga dinilai lewat **Instrumen Monev Laboratorium UPNVJ 2026**. Isinya 64 indikator dalam 5 aspek: pengelolaan lab, pengembangan lab, persiapan praktikum, proses praktikum, dan evaluasi praktikum. Setiap indikator diberi skor 1–4 dan butuh bukti dukung, totalnya 341 butir bukti. Banyak indikator dinilai dari **persentase unit yang memenuhi** (misalnya berapa persen sesi praktikum yang tercatat lengkap), dan skornya otomatis 1 kalau buktinya tidak bisa diverifikasi.

## 2. Masalahnya apa

1. **Data tersebar.** Setiap layanan punya form dan sheet sendiri yang tidak saling terhubung. Untuk tahu kondisi lab secara utuh, datanya harus digabung manual.
2. **Form cuma mencatat pengajuan, bukan alurnya.** Status pengajuan (sudah disetujui atau belum, sudah dilaksanakan atau belum) dilacak manual di sheet. Bentrok jadwal juga tidak dicek otomatis.
3. **Tidak nyambung ke monev.** Data yang ada sebenarnya bukti untuk indikator monev:
   - peminjaman lab → jadwal penggunaan lab
   - lembar penggunaan sarana → log penggunaan alat oleh pengguna berwenang
   - seleksi asisten → asisten sesuai kompetensi
   - pelaporan kendala → pengendalian alat rusak dan penanganan keluhan
   - survei → kepuasan pengguna

   Tapi karena tidak terhubung, bukti monev harus disusun ulang manual menjelang penilaian, dan persentasenya dihitung manual juga.
4. **Google Sheets sendiri jadi temuan.** Instrumen monev punya indikator pengendalian data lab: hak akses, backup, jejak perubahan, dan validasi spreadsheet. Pengelolaan data di Sheets bebas edit justru sulit memenuhi indikator ini.
5. **Belum ada gambaran besar.** Belum ada peta yang menghubungkan proses bisnis, data, aplikasi, dan indikator mutu lab, jadi digitalisasinya jalan sepotong-sepotong.

*(Detail kendala nyata, seperti berapa lama rekap, contoh kasus bentrok, dan data hilang, akan dilengkapi dari wawancara dengan KaLab/laboran.)*

## 3. Skenario proyek

Gambaran besarnya: **LabFIK pindah dari Google Form + Sheets ke satu sistem berbasis Odoo**. Semua layanan lab berjalan di sistem itu, dan datanya otomatis jadi bukti untuk indikator monev (makanya disebut "Compliance"). Proyek ini dikerjakan bertiga dengan pembagian sebagai berikut:

### (a) Enterprise Modeling dengan ArchiMate — [Nama 1]
**Ngerjain apa:**
- Memodelkan kondisi sekarang (*as-is*): aktor (KaLab, laboran, dosen, asisten, mahasiswa, GKM), proses layanan, data di form/sheet, dan aplikasi yang dipakai.
- Merancang kondisi target (*to-be*): proses, data, dan aplikasi setelah pindah ke Odoo, termasuk peta **layanan → data → indikator monev**.
- Analisis gap as-is vs to-be, lalu roadmap implementasinya.

**Masalah yang dijawab:** no. 5 (belum ada gambaran besar), sekaligus jadi dasar kebutuhan untuk (b).
**Output:** model ArchiMate (business, application, technology layer), matriks layanan–indikator, roadmap.

### (b) Odoo Module Customization — [Nama 2]
**Ngerjain apa:**
- Membuat modul kustom Odoo untuk layanan LabFIK: peminjaman lab & sarana (cek bentrok jadwal), log penggunaan sarana, pelaporan kendala, permintaan software, dan pengelolaan asisten/asistensi.
- Setiap layanan punya alur status (diajukan → disetujui → selesai) dan hak akses per peran memakai fitur security Odoo (groups, access rights, record rules).
- Data layanan dipetakan ke indikator monev, sehingga skor indikator berbasis persentase bisa dihitung otomatis dan ditelusuri sampai ke data asalnya (dashboard kepatuhan).

**Masalah yang dijawab:** no. 1–4.
**Output:** modul Odoo yang bisa dipakai, hasil pengujian (black box + UAT).

### (c) Digital Transformation — [Nama 3]
**Ngerjain apa:**
- Mengukur tingkat kematangan digital LabFIK sekarang memakai model kematangan transformasi digital laboratorium (proses, data, teknologi, manusia/budaya).
- Menyusun strategi transformasi: apa yang diubah dari cara kerja, aturan pengelolaan data, kesiapan pengelola, dan rencana migrasi dari Google Form/Sheets ke Odoo (termasuk *change management*).
- Mengevaluasi dampaknya setelah sistem dipakai, misalnya kematangan digital sebelum vs sesudah dan waktu penyusunan bukti monev sebelum vs sesudah.

**Masalah yang dijawab:** memastikan perpindahan ke sistem baru benar-benar diadopsi, bukan cuma ganti tools.
**Output:** hasil asesmen kematangan, roadmap transformasi digital, laporan evaluasi dampak.

### Keterkaitan ketiganya

```
 (c) ukur kondisi awal ──► (a) model as-is & to-be ──► (b) bangun modul Odoo
                                                              │
 (c) evaluasi dampak  ◄───────────────────────────────────────┘
```

## 4. Rencana kasar

1. Wawancara KaLab/laboran dan pengumpulan data form/sheet yang ada (bersama)
2. Asesmen kematangan awal (c) + pemodelan as-is (a)
3. Desain to-be dan pemetaan layanan–indikator (a), yang dipakai sebagai kebutuhan untuk (b)
4. Pengembangan modul Odoo bertahap per layanan (b)
5. Uji coba di LabFIK, UAT (b), dan evaluasi dampak (c)

## 5. Hal yang masih perlu dikonfirmasi

- Modul mana yang dikerjakan kelompok kami dan mana yang dikerjakan kelompok lain di proyek LabFIK Compliance
- Versi Odoo yang dipakai, dan apakah semua kelompok memakai satu server/database yang sama
- Narasumber dari LabFIK (KaLab/laboran) untuk wawancara dan UAT
- Akses ke data Google Sheets yang ada (untuk analisis as-is dan migrasi)
