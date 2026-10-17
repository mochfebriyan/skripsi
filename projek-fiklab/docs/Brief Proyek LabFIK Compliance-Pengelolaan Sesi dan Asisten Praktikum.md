# Brief Proyek LabFIK Compliance: Sesi & Asisten Praktikum

Oct 17, 2026 · @Febriyan

## Proyek ini

Kami membangun modul Odoo yang mengelola **asisten praktikum dan sesi praktikum** LabFIK UPN "Veteran" Jakarta dalam satu alur, sehingga skor 5 indikator monev bisa dihitung otomatis dari data operasional.

- **Yang dicatat:** rekrutmen dan seleksi asprak sesuai kompetensi minimum, penugasan laboran dan asisten ke setiap sesi, jadwal, kesiapan alat dan bahan, pelaksanaan, sesi pengganti, dan honor asprak.
- **Yang dihasilkan:** persentase dan skor 1–4 per indikator, bisa ditelusuri sampai ke sesi yang belum memenuhi beserta alasannya.
- **Pengguna:** KaLab, laboran/PLP, dosen pengampu, asisten praktikum, mahasiswa pendaftar asprak, dan GKM (hanya baca).
- **Posisi:** bagian dari proyek besar **LabFIK Compliance** (beberapa kelompok, tiap kelompok memegang sebagian indikator). Modul ini melanjutkan modul perencanaan dan pendaftaran asisten berbasis Odoo OpenEduCat dari skripsi Rafika Anandar (2026), bukan membangun dari nol.

## Urgensi

Mulai 2026 LabFIK diaudit dengan **Instrumen Monev Laboratorium UPNVJ 2026**, yang mengacu antara lain ke SNI ISO/IEC 17025:2017. Tuntutannya baru datang, jadi cara pencatatan lab belum disiapkan untuk menghasilkan bukti.

- Instrumen berisi 64 indikator, masing-masing skor 1–4; 36 di antaranya dinilai dari **persentase unit yang memenuhi** (100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1).
- **Bukti tidak bisa diverifikasi = skor 1**, walaupun kegiatannya sudah dilakukan dengan benar.
- Saat ini data asprak dan praktikum tersebar di Google Form dan Google Sheets yang tidak terhubung, sehingga bukti harus dikumpulkan dan persentasenya dihitung manual menjelang monev.

Belum ada sumber resmi tertulis yang menyebut audit ini mengarah ke ISO 17025 (lihat Pertanyaan terbuka).

## Penilaian yang dikerjakan

Kelima indikator memakai **sesi praktikum** sebagai unit hitung, dan semuanya dinilai dengan persentase, jadi skornya bisa dihitung sistem. Nomor di instrumen tidak unik, jadi selalu sebut aspeknya ("Pengelolaan 4", "Proses 18").

| Indikator | Bunyi singkat | Pembagi (populasi) | Sesi dianggap memenuhi bila | Bukti dukung utama |
| --- | --- | --- | --- | --- |
| Pengelolaan 4 | Seluruh sesi punya laboran/PLP dan asisten (bila perlu) yang ditugaskan sesuai kompetensi minimum | Sesi yang dilaksanakan | Kebutuhan petugas terpenuhi, penugasan sah, kompetensi terverifikasi, asisten memenuhi syarat internal | Daftar sesi dan petugas, surat tugas, matriks kompetensi, sertifikat/pelatihan, uji keterampilan, KHS asisten (nilai MK terkait ≥ 70), bukti orientasi dan supervisi |
| Persiapan 15 | Jadwal dan modul praktikum tersedia sebelum kegiatan | Sesi yang direncanakan | Jadwal sah tanpa bentrok dan sesuai kapasitas, modul versi berlaku tersedia sebelum sesi | Jadwal terpadu, persetujuan pemakaian, modul berversi, bukti publikasi, rekaman konflik jadwal |
| Persiapan 16 | Alat, software, dan utilitas siap sebelum sesi | Sesi yang dilaksanakan | Semua alat/software wajib siap dan diterima sebelum mulai | Checklist sebelum sesi, uji fungsi, versi/lisensi software, keputusan siap/tunda |
| Persiapan 17 *(bersyarat)* | Bahan praktikum tersedia sebelum sesi | Sesi yang memakai bahan | Bahan wajib cukup, layak, dan diterima sebelum mulai | Daftar kebutuhan bahan per sesi, stok, checklist dan catatan substitusi |
| Proses 18 | Sesi terlaksana sesuai jadwal, modul, dan waktu | Sesi yang direncanakan | Terlaksana sesuai rencana, atau diganti dengan sesi pengganti yang sudah selesai | Jadwal, jurnal sesi, presensi praktikan/asisten/laboran/dosen, modul yang dipakai, perubahan dan penggantian sesi |

Persiapan 17 kemungkinan hanya berlaku untuk lab 401 IoT (komponen habis pakai) dan 3D printer (filamen); sisanya praktikum berbasis komputer tanpa bahan.

## Alur sistem

Setiap asisten dan sesi melewati tahap berikut; tiap tahap menghasilkan bukti untuk indikator tertentu.

1. **Rekrutmen dan seleksi asprak** — pendaftaran, cek syarat kompetensi (KHS, rekomendasi dosen), penetapan asisten per mata kuliah. *(Pengelolaan 4)*
2. **Perencanaan sesi** — jadwal disusun, dicek bentrok dan kapasitas, disetujui, dipublikasikan bersama modul berversi. *(Persiapan 15)*
3. **Penugasan petugas** — laboran dan asisten ditugaskan ke setiap sesi, dengan surat tugas. *(Pengelolaan 4)*
4. **Persiapan sesi** — laboran mengisi checklist alat, software, dan bahan, lalu memutuskan siap atau tunda. *(Persiapan 16, 17)*
5. **Pelaksanaan sesi** — jurnal, waktu aktual, presensi empat pihak, modul yang dipakai. Sesi yang batal diajukan perubahannya dan dihubungkan ke sesi pengganti. *(Proses 18)*
6. **Rekap honor asprak** — dihitung dari kehadiran asisten pada sesi yang terlaksana.
7. **Dashboard skor** — persentase dan skor 1–4 per indikator, bisa diklik sampai ke daftar sesi yang belum memenuhi.

## Kebutuhan data

Sebagian data sudah ada di Google Form/Sheets, tetapi celah terbesarnya adalah rencana jadwal, bukti kompetensi, dan semua rekaman persetujuan/perubahan.

| Data | Isi | Sumber saat ini | Status | Role |
| --- | --- | --- | --- | --- |
| Master ruang lab | 8 ruang, kode, kapasitas PC berfungsi | Semua form; kapasitas di MASTER\_ASET KaLab | Ada sebagian (kapasitas belum dicek; penamaan tidak seragam) | 2 |
| Master akademik | Periode, mata kuliah praktikum, kelas, dosen pengampu | Form Asistensi (15 MK, kelas A–F, PBI) | Ada | 2 |
| Data pendaftar asprak | Identitas, MK target, nilai, rekomendasi dosen, KHS | Form Pendaftaran Asisten; modul Rafika | Ada | 1 |
| Bukti kompetensi petugas | Matriks kompetensi, sertifikat/pelatihan laboran, uji keterampilan, orientasi, supervisi | — | Belum ada | 1 |
| Surat tugas | Penugasan laboran dan asisten per MK/sesi | Kemungkinan dokumen manual | Perlu dicek | 1 |
| Tarif dan rekening honor | Tarif per pertemuan, aturan potongan, rekening asisten | Form Pendaftaran Asisten (rekening); tarif belum diketahui | Ada sebagian | 1 |
| Rencana jadwal praktikum | Tanggal, jam, ruang, kelas, pertemuan ke- | Rangkuman Alokasi Slot Praktikum | Belum bisa diakses | 2 |
| Peminjaman lab | Kegiatan lain di ruang yang sama | Form Peminjaman Lab | Ada (tanpa status persetujuan dan cek bentrok) | 2 |
| Modul praktikum | File, versi, tanggal berlaku | Diunggah di Form Asistensi saat/setelah sesi | Belum memenuhi syarat "sebelum sesi" | 2 |
| Kebutuhan software | Nama, versi, lisensi, ruang | Form Permintaan Software | Ada | 2 |
| Checklist kesiapan | PC, jaringan, proyektor, software, listrik/AC, keputusan siap/tunda | Form Asistensi: satu pilihan "Kesiapan Sarana" oleh asisten | Belum memenuhi (bukan checklist, bukan laboran) | 2 |
| Bahan per sesi | Komponen IoT, filamen 3D printer, stok BHP | Form 3D Printer; sheet BHP KaLab | Belum dikaitkan ke sesi | 2 |
| Jurnal sesi | Waktu aktual, topik, pertemuan ke-, foto | Form Pelaksanaan Asistensi | Ada (hanya sesi yang punya asisten) | 3 |
| Presensi | Praktikan per nama, asisten, laboran, dosen | Form Asistensi: jumlah praktikan, dosen hadir ya/tidak | Ada sebagian (laboran belum dicatat) | 3 |
| Perubahan dan sesi pengganti | Pengajuan, persetujuan, sesi asal | — | Belum ada | 3 |
| Log penggunaan alat | Alat, waktu, status akhir alat | Lembar Penggunaan Sarana (kertas) | Belum digital | 3 |

## Pembagian role

Usulan: dibagi per modul supaya tiap orang punya indikator, judul, dan rumusan masalah sendiri. Model data "sesi praktikum" dirancang bersama di awal karena dipakai ketiga role.

| Role | Modul | Indikator | Tanggung jawab utama | Tugas lintas modul |
| --- | --- | --- | --- | --- |
| Role 1 | Asisten Praktikum | Pengelolaan 4 | Rekrutmen dan seleksi asprak berbasis kompetensi minimum, penugasan laboran dan asisten per sesi, surat tugas, rekap honor dari kehadiran | Integrasi dengan modul Rafika |
| Role 2 | Perencanaan & Persiapan Sesi | Persiapan 15, 16, 17 | Master data, jadwal terpadu dengan cek bentrok dan kapasitas, alur persetujuan, modul berversi, checklist kesiapan alat/software/bahan | Master data bersama dan koordinasi dengan kelompok lain |
| Role 3 | Pelaksanaan Sesi & Dashboard | Proses 18 | Jurnal dan presensi sesi, perubahan jadwal dan sesi pengganti, dashboard skor 5 indikator | Pengujian black box dan UAT |

**Usulan judul per role**

- **Role 1:** Kustomisasi Modul Odoo untuk Rekrutmen, Penugasan, dan Perhitungan Honor Asisten Praktikum Berbasis Kompetensi Minimum (Studi Kasus: LabFIK UPN "Veteran" Jakarta)
- **Role 2:** Kustomisasi Modul Odoo untuk Penjadwalan dan Pemeriksaan Kesiapan Sesi Laboratorium Berbasis Instrumen Monev (Studi Kasus: LabFIK UPN "Veteran" Jakarta)
- **Role 3:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan Sesi dan Perhitungan Otomatis Skor Indikator Monev Laboratorium (Studi Kasus: LabFIK UPN "Veteran" Jakarta)

## Pertanyaan terbuka

**Untuk Pak Widi**

- [ ] Apakah scope 5 indikator (Pengelolaan 4, Persiapan 15–17, Proses 18) disetujui untuk kelompok kami?
- [ ] Satu judul per orang, atau satu judul bersama?
- [ ] Modul Rafika di-*extend* langsung, atau hanya dijadikan acuan?
- [ ] Persiapan 17 dinyatakan N/A, atau dicakup terbatas (lab IoT, 3D printer)?
- [ ] Apa dasar resmi bahwa audit 2026 mengarah ke ISO/IEC 17025 (surat/SK) untuk dikutip di latar belakang?
- [ ] Odoo versi berapa, dan apakah semua kelompok memakai satu server?

**Untuk KaLab/laboran**

- [ ] Bisakah Rangkuman Alokasi Slot Praktikum dan sheet jawaban Form Asistensi, Form Peminjaman Lab, dan Form Pendaftaran Asisten di-*share*?
- [ ] Bagaimana alur seleksi dan penugasan asisten sekarang, dan siapa yang menerbitkan surat tugas?
- [ ] Bagaimana honor asprak dihitung (tarif per pertemuan, syarat, siapa yang menyetujui)?
- [ ] Apakah ada sesi praktikum tanpa asisten, dan bagaimana pelaksanaannya dicatat?
- [ ] Bukti kompetensi laboran apa yang sudah ada (ijazah, pelatihan, sertifikat)?
- [ ] Bagaimana prosedur saat sesi batal atau diganti?
