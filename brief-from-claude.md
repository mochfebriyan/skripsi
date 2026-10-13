Saya sudah baca keempat bahan: pendahuluan BEM, kode MVP `lab_booking`, dan **Instrumen Monev Laboratorium UPNVJ 2026** (xlsx di folder fiklab). File xlsx itu ternyata kunci untuk memahami brief Fiklab.

## 1. Projek BEM: platform orientasi mahasiswa yang bisa dikonfigurasi

**Masalahnya:** PKKMB-FIK (~500 maba/tahun) masih dikelola pakai Google Form, Spreadsheet, dan LINE yang tidak saling terhubung. Akibatnya tugas fisik hilang, info terlewat, rekap dikerjakan manual, dan pengumuman kelulusan telat. SIERA hanya mencakup tingkat universitas.

**Solusinya:** web app tempat panitia menyusun program sendiri (tahapan, kelompok/mentor, tugas, komponen nilai, syarat lulus). Isinya presensi, penugasan, pusat informasi, dan dashboard peserta yang berisiko tidak lulus. Klaim kebaruannya ada di sifat *configurable*: satu platform untuk PKKMB, LDKMM, dan MABIM. Dikembangkan dengan Agile, diuji dengan UAT.

**Penilaian saya:**
- **Scope jelas dan masalahnya nyata** (berbasis wawancara). Rumusan masalah dan research gap juga sudah tertulis. Ini modal besar.
- **Bagian tersulitnya ada di Role 1.** "Aturan penilaian dan syarat kelulusan yang bisa dikonfigurasi" pada dasarnya adalah *rule engine* kecil: bobot komponen, ambang nilai, syarat kehadiran minimal, dan status "lulus dengan tugas tambahan". Kalau desain skemanya salah, Role 2 dan 3 ikut kena, karena keduanya membaca struktur data dari Role 1. Skema ini harus disepakati bertiga **di sprint pertama**.
- **Ada celah dalam pembagian role.** Autentikasi, RBAC (panitia/mentor/peserta/dekanat), import data peserta, dan manajemen kelompok/mentor belum dipegang siapa pun. Semuanya dibangun dari nol karena tidak ada framework seperti Odoo yang menyediakannya.
- **⚠️ Risiko jadwal UAT.** Rumusan masalah no. 3 meminta UAT "pada pelaksanaan PKKMB-FIK". Sekarang Oktober 2026, jadi PKKMB 2026 sudah lewat dan berikutnya sekitar Agustus 2027. Kalau target lulus kalian sebelum itu, UAT harus memakai LDKMM/MABIM (cek jadwalnya) atau simulasi bersama panitia lama. Redaksi rumusan masalah juga perlu disesuaikan. Ini perlu diputuskan sekarang, jangan menunggu Bab 4.

## 2. Projek Fiklab: kemungkinan besar digitalisasi instrumen monev lab

Saya rasa "LabFIK Compliance" artinya **kepatuhan lab terhadap Instrumen Monev Laboratorium UPNVJ 2026**. Ini masih dugaan saya dan perlu dikonfirmasi ke Pak Widi. Isi instrumennya:

- Sekitar **60 indikator** dalam 5 kelompok: Pengelolaan, Pengembangan, Persiapan Praktikum, Proses Praktikum, dan Evaluasi Praktikum.
- Setiap indikator punya PIC, **bukti dukung**, dan skor 1–4. Ada dua cara menghitung skor:
  - **"1 paket dokumen"**: kriteria 1–4 diperiksa berurutan. Contohnya indikator 1 (rencana kerja tahunan) dan E04 (keluhan).
  - **"100% unit yang memenuhi"**: dihitung dari persentase unit yang memenuhi syarat (100% = 4, 90 sampai <100% = 3, 70 sampai <90% = 2, <70% = 1). Contohnya Q04: "pengoperasian alat tercatat oleh pengguna berwenang".

Jadi sistemnya kemungkinan bertugas **menghasilkan bukti dukung secara otomatis dari operasional lab sehari-hari**: log alat, jadwal, presensi sesi, inspeksi K3, inventaris, keluhan, dan tindak lanjut temuan. Dari data itu, skor monev bisa dihitung, tidak lagi mengumpulkan dokumen secara manual menjelang audit. Odoo cocok untuk ini karena user, groups, record rules, chatter/audit trail (`mail.thread`), dan lampiran sudah tersedia. Ini juga yang dimaksud dosen dengan "permission security-nya udah ada di Odoo".

**Soal MVP kalian:** isinya sudah melebihi permintaan "manajemen user". Sudah ada 3 role bertingkat, record rules, workflow persetujuan, validasi bentrok jadwal dan kapasitas, serta unit test. Arahnya juga relevan dengan monev: booking/jadwal menyentuh indikator jadwal penggunaan lab ("rekaman konflik jadwal"), kapasitas sesi, dan sebagian Q04. Untuk pembuktian kemampuan teknis, ini sudah lebih dari cukup.

**Risiko Fiklab:**
- **Scope belum ada.** Tidak ada rumusan masalah, belum jelas bagian mana milik kalian, dan "digabung dengan grup lain" berarti ada ketergantungan ke instance Odoo, dependency antar-modul, dan jadwal kelompok lain.
- **Instrumennya sendiri masih v1.1 dan belum stabil.** Nomor ID-nya dobel (ada dua indikator 8, 10, 12, 13, 15, 19) dan formatnya campur angka dengan Q/E. Requirement kemungkinan masih berubah.
- **Kebaruan akademis.** Skripsi berbasis Odoo rawan dinilai penguji sebagai "cuma konfigurasi ERP". Kalian perlu argumen kontribusi yang kuat, misalnya mesin skoring monev otomatis berbasis data operasional.
- **Learning curve Odoo** (ORM, XML views, OWL kalau butuh UI custom) menanjak saat keluar dari CRUD standar.

## 3. Mana yang lebih sulit?

Tingkat kesulitannya berbeda jenis:

| | BEM Website | Fiklab (Odoo) |
|---|---|---|
| Volume coding | **Lebih berat**, semua dari nol (auth, RBAC, UI, notifikasi) | Lebih ringan, banyak fitur gratis dari Odoo |
| Kejelasan scope | **Jelas**, pendahuluan sudah jadi | **Kabur**, brief masih via chat |
| Ketergantungan eksternal | Panitia BEM (untuk UAT) | Dosen, grup lain, instrumen yang masih berubah |
| Risiko terbesar | Jadwal UAT dan desain rule engine (Role 1) | Scope melebar, integrasi lintas grup, kebaruan |
| Kendali tim | Penuh | Sebagian |

**Kesimpulan saya:** dari sisi teknis murni, **BEM lebih berat**. Tapi secara keseluruhan untuk skripsi, **Fiklab lebih sulit dan berisiko**, karena skripsi lebih sering tertunda akibat scope yang tidak jelas dan ketergantungan ke pihak lain daripada akibat banyaknya coding. Kerja berat bisa direncanakan, sedangkan ketidakpastian tidak.

Fiklab bisa menyusul jadi pilihan yang setara atau bahkan lebih baik **kalau** Pak Widi segera menjawab soal scope dan pembagian grup. Kelebihannya: dosen sendiri yang jadi sponsor (biasanya dukungan pembimbing kuat), ada dokumen requirement yang formal (xlsx monev), dan MVP-nya sudah terbukti jalan.

## 4. Usulan pembagian role Fiklab (sementara)

Saya ikuti pola tiga role di BEM dan petakan ke kelompok indikator monev:

- **Role 1, Aset & Sarana Lab:** inventaris alat/bahan, kalibrasi, pemeliharaan preventif, alat rusak/karantina, dan inspeksi sarana K3 (indikator 5, 6, 7, 12, 18, 19, 21).
- **Role 2, Operasional Praktikum:** jadwal/booking (lanjutan dari MVP), sesi praktikum dan presensi petugas/praktikan, log penggunaan alat, checklist sebelum dan sesudah sesi, safety induction, serta laporan insiden (15, 16, 18, 37, Q01–Q10).
- **Role 3, Compliance & Monev:** register indikator, upload dan verifikasi bukti, **kalkulasi skor 1–4 otomatis** dari data Role 1 dan 2, register temuan/RTL, keluhan, dan dashboard (10, 13, E04, E08). Bagian ini kemungkinan besar inti "Compliance".

## 5. Pertanyaan untuk Pak Widi sebelum memutuskan

1. Apakah "LabFIK Compliance" memang digitalisasi instrumen monev ini?
2. Indikator atau kelompok indikator mana yang menjadi bagian grup kami, dan mana bagian grup lain?
3. Apakah semua grup memakai satu instance/database Odoo? Siapa yang memegang modul inti (master lab, user)?
4. Versi Odoo yang dipakai? MVP kami memakai Odoo 17.
5. Siapa user nyata untuk UAT (KaLab, PLP/laboran, GKM?), dan kapan monev berikutnya berjalan?
6. Apakah output akhirnya hanya skor internal atau juga harus menghasilkan dokumen laporan monev?

Kalau jawaban nomor 1–3 belum jelas dalam 1–2 minggu, saran saya lanjutkan BEM. Tapi segera putuskan strategi UAT-nya karena PKKMB 2026 sudah lewat.

Kalau mau dibagikan ke tim atau dibawa ke bimbingan, analisis ini bisa saya jadikan halaman ringkas.