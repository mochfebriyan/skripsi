# Brief Proyek LabFIK Compliance: Siklus Mutu Praktikum

Oct 26, 2026 · @Febriyan · revisi dari versi Oct 17, 2026 (scope kelompok berubah, lihat [Perubahan scope](#perubahan-scope))

## Ringkasan

- **Apa:** modul Odoo yang mengelola **siklus mutu praktikum** LabFIK UPN "Veteran" Jakarta, mulai dari pengembangan lab dan kompetensi personel, lalu penugasan dan otorisasi petugas, penjadwalan, pelaksanaan sesi, sampai penilaian praktikan. Setiap tahap menghasilkan bukti untuk indikator Instrumen Monev Laboratorium UPNVJ 2026.
- **Scope kelompok (8 indikator):** Pengelolaan 4 dan 10, Pengembangan 13 dan 14, Persiapan 15 dan 17, Proses 18, Evaluasi 19. **Persiapan 16 tidak lagi dicakup.**
- **Hasil:** bukti tiap indikator terkumpul di satu sistem dan terhubung satu sama lain, dengan skor 1–4 per indikator di satu *dashboard*. Ada indikator yang skornya dihitung otomatis, ada juga yang hanya mengumpulkan bukti dan skornya ditetapkan oleh penilai (lihat [Level cakupan](#level-cakupan-per-indikator)).
- **Pengguna:** KaLab, laboran/PLP, dosen pengampu, asisten praktikum, mahasiswa pendaftar asprak, Dekanat (Pengembangan 13, 14), dan GKM (hanya baca).
- **Posisi:** bagian dari proyek besar **LabFIK Compliance**. Proyek ini melibatkan beberapa kelompok, dan tiap kelompok memegang sebagian dari 64 indikator.

## Perubahan scope

| | Versi Oct 17 | Versi sekarang (Oct 26, rencana awal) |
|---|---|---|
| Indikator | Pengelolaan 4, Persiapan 15, 16, 17, Proses 18 (5 indikator) | Pengelolaan 4, **10**, Pengembangan **13**, **14**, Persiapan 15, 17, Proses 18, Evaluasi **19** (8 indikator) |
| Dikeluarkan | — | **Persiapan 16** (alat, software, utilitas siap sebelum sesi) |
| Unit hitung | Semua per **sesi praktikum** | Campuran: per sesi, per personel–tugas/alat, per praktikan, dan per paket dokumen |
| Cara skor | Semua persentase, semua bisa otomatis | Dua jenis: persentase (6 indikator) dan kriteria berurutan (2 indikator) |
| Benang merah | "Skor 5 indikator dihitung otomatis dari rekaman sesi" | "Siklus mutu praktikum: lab dikembangkan → personel kompeten dan berwenang → sesi direncanakan → sesi terlaksana → praktikan dinilai → hasilnya kembali jadi masukan pengembangan" |

**Konsekuensinya:** narasi lama yang berbunyi "lima indikator berunit sesi, semuanya dihitung otomatis" sudah tidak berlaku. Judul, latar belakang, dan batasan masalah di draf Bab 1 tiap role perlu disesuaikan (lihat [Dampak ke Bab 1](#dampak-ke-bab-1-tiap-role)).

## Urgensi

Mulai 2026 LabFIK diaudit dengan **Instrumen Monev Laboratorium UPNVJ 2026**. Instrumen ini mengacu antara lain ke SNI ISO/IEC 17025:2017. Karena tuntutannya baru datang, cara pencatatan lab belum disiapkan untuk menghasilkan bukti.

- Instrumen berisi 64 indikator, masing-masing diberi skor 1–4. Ada dua cara penilaian:
  - **Persentase unit yang memenuhi:** 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1.
  - **Kriteria berurutan 1–4:** skor naik hanya jika kriteria sebelumnya sudah terpenuhi.
- **Bukti tidak bisa diverifikasi = skor 1**, walaupun kegiatannya sudah dilakukan dengan benar.
- Saat ini data asprak dan praktikum tersebar di beberapa tempat yang tidak terhubung: Google Form, Google Sheets, LeADS (LMS kampus), dan SIMPEL (presensi). Akibatnya bukti harus dikumpulkan dan persentasenya dihitung manual menjelang monev.

Belum ada sumber resmi tertulis yang menyebut audit ini mengarah ke ISO 17025 (lihat [Pertanyaan terbuka](#pertanyaan-terbuka)).

## Indikator yang dikerjakan

**Nomor di instrumen tidak unik.** Contohnya ada tiga baris "Pengelolaan 10" dan dua baris "Evaluasi 19". Karena itu, selalu sebut **aspek + nomor + bunyi singkat**. Berikut baris yang kami ambil:

| Sebutan | Baris yang dimaksud | Baris lain dengan nomor sama (**bukan** scope kami) |
|---|---|---|
| Pengelolaan 10 | *Seluruh personel/pengguna yang menjalankan tugas atau alat dengan kewenangan khusus memiliki **otorisasi sesuai kompetensi**.* | Capaian KPI laboratorium dipantau; Legalitas, identitas, fungsi, dan ruang lingkup layanan ditetapkan |
| Evaluasi 19 | *Kompetensi praktikan **dinilai secara individual** melalui rubrik dan bukti unjuk kerja yang sesuai CPMK.* | Ketercapaian CPMK praktikum dianalisis untuk seluruh mata kuliah |
| Pengembangan 13 | *Rencana pengembangan laboratorium didasarkan pada analisis kesenjangan.* | Pengelolaan 13 (dokumen dan rekaman mutu dikendalikan) ada di aspek lain |

### A. Indikator persentase (skor dihitung dari % unit yang memenuhi)

| Indikator | Bunyi singkat | PJ | Unit dan pembagi | Unit dianggap memenuhi bila | Bukti dukung utama |
|---|---|---|---|---|---|
| **Pengelolaan 4** | Seluruh sesi punya laboran/PLP dan asisten (bila perlu) yang ditugaskan sesuai kompetensi minimum | KaLab; Koor Prodi | **Sesi** yang dilaksanakan | Kebutuhan petugas terpenuhi, penugasan sah, kompetensi terverifikasi, asisten memenuhi syarat internal | Daftar sesi dan petugas, surat tugas, matriks kompetensi, ijazah/pelatihan/sertifikat, hasil uji keterampilan, KHS asisten (nilai MK terkait ≥ 70, usulan kebijakan internal), bukti orientasi dan supervisi |
| **Pengelolaan 10** | Personel/pengguna dengan tugas atau alat berkewenangan khusus memiliki otorisasi sesuai kompetensi | KaLab; PLP/laboran | **Pasangan personel–tugas/alat** yang memerlukan otorisasi dan aktif pada periode monev | Kompetensi dibuktikan, cakupan kewenangan spesifik ditetapkan, pengguna pemula disupervisi, otorisasi dievaluasi ulang bila ada perubahan | Matriks tugas/alat yang memerlukan otorisasi, asesmen keterampilan, daftar operator sah, pembatasan akses, evaluasi ulang |
| **Persiapan 15** | Jadwal dan modul praktikum tersedia sebelum kegiatan | KaLab; dosen pengampu | **Sesi** yang direncanakan | Jadwal sah, tanpa bentrok, sesuai kapasitas; modul versi berlaku tersedia sebelum sesi | Jadwal terpadu (praktikum + kegiatan lain), persetujuan pemakaian, modul berversi, bukti publikasi sebelum sesi, rekaman konflik jadwal |
| **Persiapan 17** *(bersyarat)* | Bahan praktikum tersedia dalam jumlah, mutu, dan kondisi yang sesuai sebelum sesi | PLP/laboran | **Sesi** yang memakai bahan fisik | Bahan wajib cukup, layak, dan diterima sebelum mulai | Daftar kebutuhan per sesi, stok/lot, kriteria penerimaan, checklist dan catatan substitusi |
| **Proses 18** | Sesi terlaksana sesuai jadwal, modul, dan waktu | Dosen; KaLab | **Sesi** yang direncanakan | Kegiatan, durasi, dan tujuan sesuai; perubahan sah; sesi tertunda baru dihitung memenuhi setelah penggantinya selesai dalam periode | Jadwal, jurnal sesi, presensi praktikan/asisten/laboran/dosen, modul yang dipakai, *log book*, perubahan yang disetujui, penggantian sesi |
| **Evaluasi 19** | Kompetensi praktikan dinilai individual dengan rubrik dan bukti unjuk kerja sesuai CPMK | Dosen; asisten | **Praktikan** yang dinilai pada periode monev | Bukti menunjukkan kemampuan individu, skor dapat ditelusuri ke rubrik, remediasi tersedia bila perlu, nilai kelompok bukan satu-satunya bukti | Rubrik keterampilan/produk, hasil observasi individual, portofolio, umpan balik dan remediasi, moderasi antarpenilai |

Catatan:

- Persiapan 17 kemungkinan hanya berlaku untuk lab 401 IoT (komponen habis pakai) dan 3D printer (filamen). Praktikum lain berbasis komputer dan tidak memakai bahan.
- Untuk Pengelolaan 10, belum diketahui tugas atau alat apa di LabFIK yang tergolong "berkewenangan khusus". Kemungkinannya antara lain 3D printer, perangkat IoT/solder, perangkat jaringan/server, dan akun admin lab. **[KONFIRMASI ke KaLab]**

### B. Indikator paket dokumen (kriteria berurutan)

Kedua indikator ini dinilai sebagai **1 paket dokumen dan rekaman**, dengan aturan skor yang sama:

- **4:** kriteria 1–4 terpenuhi berurutan.
- **3:** kriteria 1–3 terpenuhi.
- **2:** hanya kriteria 1, atau 1–2, yang terpenuhi.
- **1:** kriteria 1 belum terpenuhi, atau bukti tidak bisa diverifikasi.

| Indikator | Bunyi singkat | PJ | Kriteria 1 → 4 | Bukti dukung |
|---|---|---|---|---|
| **Pengembangan 13** | Rencana pengembangan lab didasarkan pada analisis kesenjangan kebutuhan tridharma, kompetensi, sarana, dan layanan | KaLab; Dekanat | (1) Analisis kebutuhan dan rencana pengembangan **disahkan**. (2) Gap, prioritas berbasis risiko/manfaat, biaya, target, dan PIC **lengkap**. (3) Program **berjalan** dan realisasinya bisa ditelusuri. (4) **Manfaat diukur** dan rencana diperbarui | Analisis gap; kebutuhan kurikulum/CPMK, riset, dan PkM; *roadmap*; prioritas, biaya, target, PIC, dan jadwal; realisasi |
| **Pengembangan 14** | Kompetensi PLP/laboran dikembangkan melalui pelatihan yang relevan dan dievaluasi penerapannya | KaLab; Dekanat SDM | (1) Kebutuhan kompetensi dan rencana pengembangan personel **ditetapkan**. (2) Materi, peserta, anggaran, jadwal, dan kriteria keberhasilan **sesuai gap tugas**. (3) Pelatihan **terlaksana** dan keterampilannya diterapkan. (4) **Efektivitas dibuktikan** lewat asesmen ulang/kinerja, lalu kebutuhan berikutnya diperbarui | Analisis kebutuhan kompetensi; rencana Diklatfung/bimtek/sertifikasi; sertifikat; praktik/demonstrasi pascapelatihan; rekaman peningkatan layanan |

Untuk kedua indikator ini, sistem **tidak bisa menghitung skornya sendiri**, karena pengesahan dan penilaian kualitas tetap dilakukan manusia. Peran sistem adalah:

- mengelola alur rencana → realisasi → evaluasi;
- menyimpan bukti di setiap kriteria;
- menunjukkan sampai kriteria ke berapa yang sudah ada buktinya.

### Persiapan 16 dikeluarkan

Persiapan 16 (alat, software, dan utilitas siap sebelum sesi) tidak lagi dicakup kelompok ini. Implikasinya:

- Alur sesi kami tidak lagi memuat *checklist* kesiapan alat dan software.
- Data Form Permintaan Software dan model `lab.readiness.checklist` di modul Rafika tidak lagi menjadi tanggung jawab kami.
- Batasan masalah tiap role perlu menyebut bahwa kesiapan sarana tidak dibahas.
- **[KONFIRMASI ke Pak Widi]** Apakah Persiapan 16 dipindah ke kelompok lain (misalnya kelompok inventaris/kalibrasi)? Kalau iya, data kesiapan sarananya perlu dihubungkan ke sesi milik kita.

## Benang merah: siklus mutu praktikum

Kedelapan indikator membentuk satu siklus tertutup yang terdiri dari dua putaran:

- **Putaran tahunan:** pengembangan lab dan personel.
- **Putaran per sesi:** operasional praktikum.

Kedua putaran terhubung lewat **data kompetensi personel** dan **hasil skor**.

```
            PUTARAN TAHUNAN (Pengembangan & Personel)
 ┌──────────────────────────────────────────────────────────────┐
 │  Pengembangan 13            Pengembangan 14                  │
 │  analisis gap lab   ──────▶ rencana & realisasi pelatihan    │
 │  + rencana pengembangan     laboran/PLP                      │
 │        ▲                          │ sertifikat, hasil        │
 │        │                          ▼ asesmen ulang            │
 │        │                    Register kompetensi personel     │
 │        │                          │                          │
 │        │                          ▼                          │
 │        │                    Pengelolaan 10                   │
 │        │                    otorisasi personel–tugas/alat    │
 └────────┼──────────────────────────┼──────────────────────────┘
          │                          │
          │          PUTARAN PER SESI (Operasional)
 ┌────────┼──────────────────────────▼──────────────────────────┐
 │        │   Persiapan 15  ──▶  Pengelolaan 4  ──▶ Persiapan 17│
 │        │   jadwal & modul     petugas kompeten    bahan siap │
 │        │                      & berwenang         (bersyarat)│
 │        │                           │                         │
 │        │                           ▼                         │
 │        │                     Proses 18                       │
 │        │                     sesi terlaksana                 │
 │        │                           │                         │
 │        │                           ▼                         │
 │        │                     Evaluasi 19                     │
 │        │                     praktikan dinilai individual    │
 └────────┼───────────────────────────┼─────────────────────────┘
          │                           ▼
          └──────────────────  Dashboard skor 8 indikator
                               (gap & tren jadi masukan Pengembangan 13)
```

Hubungan antarindikator:

1. **Pengembangan 13 → 14.** Salah satu dimensi analisis gap di Pengembangan 13 adalah *kompetensi*. Gap kompetensi laboran itulah yang menjadi kebutuhan pelatihan di Pengembangan 14.
2. **Pengembangan 14 → register kompetensi.** Sertifikat dan hasil asesmen pascapelatihan masuk ke register kompetensi personel.
3. **Register kompetensi → Pengelolaan 10 dan 4.**
   - Pengelolaan 10 memakai register untuk menerbitkan otorisasi per tugas/alat.
   - Pengelolaan 4 memakai register yang sama untuk menugaskan laboran dan asisten ke sesi.
   - Satu sumber data kompetensi, dua indikator.
4. **Pengelolaan 10 → Pengembangan 14 (kriteria 4).** Evaluasi ulang otorisasi sekaligus menjadi bukti efektivitas pelatihan, yaitu bahwa keterampilan diterapkan dan dinilai ulang.
5. **Persiapan 15 → Pengelolaan 4 → Proses 18.** Sesi rencana dari Persiapan 15 adalah pembagi Pengelolaan 4 dan Proses 18.
6. **Proses 18 → Evaluasi 19.** Penilaian praktikan terjadi di sesi yang terlaksana, dan presensi sesi menentukan siapa praktikan yang seharusnya dinilai.
7. **Dashboard → Pengembangan 13.**
   - Skor dan daftar unit yang tidak memenuhi di kedelapan indikator adalah data primer untuk analisis gap tahun berikutnya.
   - Contohnya: sesi tanpa laboran kompeten, praktikan tanpa penilaian individual, atau alat tanpa operator berwenang.
   - Dari sini siklusnya tertutup.

Dengan siklus ini, Pengembangan 13 dan 14 tidak berdiri sendiri sebagai "indikator dokumen". Bukti untuk kriteria 3 dan 4-nya (realisasi dan efektivitas) diambil dari data operasional role lain.

## Alur sistem

### Putaran tahunan (per tahun anggaran / periode monev)

1. **Analisis gap dan rencana pengembangan lab.** KaLab menyusun analisis kebutuhan dengan empat dimensi: tridharma, kompetensi, sarana, dan layanan. Analisis ini dibantu data *dashboard* periode sebelumnya. Rencana disahkan Dekanat, lalu realisasinya dipantau. *(Pengembangan 13)*
2. **Rencana dan realisasi pelatihan laboran.** Kebutuhan kompetensi diturunkan dari gap. Hasilnya adalah rencana pelatihan (Diklatfung/bimtek/sertifikasi), realisasi, sertifikat, praktik pascapelatihan, dan asesmen ulang. *(Pengembangan 14)*
3. **Register kompetensi dan otorisasi.** Kompetensi laboran dan asisten dicatat. Tugas atau alat yang memerlukan otorisasi ditetapkan, lalu otorisasi diterbitkan per personel. Pemula disupervisi, dan otorisasi dievaluasi ulang bila ada perubahan. *(Pengelolaan 10)*

### Putaran per semester / per sesi

4. **Rekrutmen dan seleksi asprak.** Pendaftaran, cek syarat kompetensi (KHS, rekomendasi dosen), dan penetapan asisten per mata kuliah. *(Pengelolaan 4)*
5. **Perencanaan sesi.** Jadwal disusun, dicek bentrok dan kapasitas, disetujui, lalu dipublikasikan bersama modul berversi. *(Persiapan 15)*
6. **Penugasan petugas.** Laboran dan asisten yang kompeten dan berwenang ditugaskan ke setiap sesi, dengan surat tugas. *(Pengelolaan 4, memakai data Pengelolaan 10)*
7. **Persiapan bahan (bersyarat).** Untuk sesi yang memakai bahan fisik, laboran mencatat kebutuhan, stok, dan penerimaan bahan. *(Persiapan 17)*
8. **Pelaksanaan sesi.** Isinya jurnal, waktu aktual, presensi empat pihak, modul yang dipakai, dan *log book*. Sesi yang batal diajukan perubahannya dan dihubungkan ke sesi pengganti. *(Proses 18)*
9. **Penilaian praktikan.** Penilaian tetap dilakukan di LeADS. Sistem menautkan bukti penilaian (LeADS) dan presensi rinci per praktikan (SIMPEL) ke sesi. *(Evaluasi 19)*
10. **Rekap honor asprak.** Dihitung dari kehadiran asisten pada sesi yang terlaksana. *(bukan indikator, tetapi kebutuhan operasional)*
11. ***Dashboard* skor.** Menampilkan skor 1–4 per indikator. Indikator persentase bisa diklik sampai ke unit yang belum memenuhi. Indikator paket dokumen menampilkan kriteria mana yang sudah berbukti.

## Level cakupan per indikator

Tidak semua indikator bisa dihitung otomatis. Supaya klaim tiap skripsi jujur, setiap indikator ditempatkan pada salah satu dari tiga level berikut:

| Level | Arti | Peran penilai |
|---|---|---|
| **Otomatis** | Skor dihitung sistem dari data operasional yang dicatat di Odoo | Memverifikasi sampel |
| **Semi-otomatis** | Sistem mengelola alur dan bukti, lalu menunjukkan kriteria mana yang sudah berbukti | Menilai kualitas bukti dan menetapkan skor akhir |
| **Bukti tertaut** | Data utama ada di sistem lain. Odoo hanya menyimpan tautan bukti per unit | Membuka tautan dan menilai |

| Indikator | Level (rencana awal) | Alasan |
|---|---|---|
| Pengelolaan 4 | Otomatis | Petugas per sesi dan kompetensinya tercatat di Odoo |
| Pengelolaan 10 | Otomatis | Pasangan personel–tugas/alat dan status otorisasinya tercatat di Odoo |
| Persiapan 15 | Otomatis | Jadwal, persetujuan, dan versi modul tercatat di Odoo |
| Persiapan 17 | Otomatis (bila berlaku) | Kebutuhan dan penerimaan bahan per sesi tercatat di Odoo |
| Proses 18 | Otomatis | Rencana vs realisasi sesi tercatat di Odoo |
| Pengembangan 13 | Semi-otomatis | Pengesahan dan pengukuran manfaat ditetapkan manusia. Data gap bisa diambil dari *dashboard* |
| Pengembangan 14 | Semi-otomatis | Rencana dan realisasi pelatihan tercatat. Efektivitasnya dibantu data asesmen ulang (Pengelolaan 10) |
| Evaluasi 19 | Bukti tertaut (MVP) | Penilaian, hasil kerja, dan *feedback* sudah ada di LeADS, dan presensi rinci ada di SIMPEL. Odoo tidak menginput ulang, cukup menautkan |

**Catatan Evaluasi 19:**

- Unit Evaluasi 19 adalah **praktikan**, sedangkan tautan bukti menempel di **sesi**. Akibatnya, pada tahap MVP sistem hanya bisa menunjukkan sesi mana yang punya bukti penilaian. Persentase praktikan yang memenuhi tetap diverifikasi penilai.
- Peningkatan ke level otomatis (impor *gradebook* LeADS, atau integrasi API) menjadi saran pengembangan.
- Tampilan role dosen di LeADS dan SIMPEL belum diketahui **[KONFIRMASI]**.

## Komponen bersama (*shared core*)

Empat komponen dipakai lebih dari satu role, jadi harus dirancang dan disepakati bersama **sebelum** tiap role membangun modulnya.

| Komponen | Isi | Pemilik | Dipakai oleh |
|---|---|---|---|
| **Sesi praktikum** (*inherit* `op.session`) | Periode, MK, kelas, ruang, pertemuan ke-, waktu rencana, status | Role 2 (membuat sesi rencana) | Role 1 (penugasan), Role 3 (realisasi, penilaian, skor) |
| **Register kompetensi personel** | Laboran, PLP, dan asisten; kompetensi, bukti (ijazah, sertifikat, uji keterampilan), masa berlaku | Role 1 | Role 1 (Pengelolaan 4, 10), Role 2 (Pengembangan 14 mengisi hasil pelatihan), Role 3 (*dashboard*) |
| **Registri indikator dan mesin skor** | Kode aspek + nomor + bunyi (karena nomor tidak unik), jenis skor (persentase / kriteria berurutan), unit, aturan memenuhi, alasan gagal | Role 3 | Semua role menyumbang aturan indikatornya |
| **Model bukti** | Lampiran file atau tautan eksternal per unit atau per kriteria, dengan status verifikasi | Role 3 | Semua role, terutama untuk Pengembangan 13, 14 dan Evaluasi 19 |

Prinsip desain:

- **Satu sumber data per fakta.** Contohnya, kompetensi laboran hanya dicatat di register, bukan di modul pelatihan dan modul penugasan secara terpisah.
- **Mesin skor generik.** Mesin harus mendukung dua jenis skor dan unit yang berbeda-beda, supaya kelompok lain atau kelompok tahun depan bisa menambah indikator tanpa mengubah mesinnya.
- **Data sistem lain tidak diinput ulang.** LeADS dan SIMPEL tetap menjadi sistem sumber.

## Kebutuhan data

Sebagian data sudah ada di Google Form/Sheets, LeADS, dan SIMPEL. Celah terbesarnya ada di empat hal: rencana jadwal, bukti kompetensi dan otorisasi, dokumen perencanaan pengembangan, dan semua rekaman persetujuan/perubahan.

| Data | Isi | Sumber saat ini | Status | Role |
|---|---|---|---|---|
| Master ruang lab | 8 ruang, kode, kapasitas PC berfungsi | Semua form; kapasitas di MASTER\_ASET KaLab | Ada sebagian (kapasitas belum dicek; penamaan tidak seragam) | 2 |
| Master akademik | Periode, mata kuliah praktikum, kelas, dosen pengampu | Form Asistensi (15 MK, kelas A–F, PBI) | Ada | 2 |
| Data pendaftar asprak | Identitas, MK target, nilai, rekomendasi dosen, KHS | Form Pendaftaran Asisten; modul Rafika | Ada | 1 |
| Register kompetensi personel | Matriks kompetensi, ijazah, sertifikat/pelatihan laboran, uji keterampilan, orientasi, supervisi | — | Belum ada | 1 |
| Daftar tugas/alat berkewenangan khusus | Tugas/alat yang memerlukan otorisasi, syarat kompetensinya | — | Belum ada **[KONFIRMASI]** | 1 |
| Otorisasi personel | Daftar operator sah, cakupan kewenangan, tanggal, evaluasi ulang | — | Belum ada | 1 |
| Surat tugas | Penugasan laboran dan asisten per MK/sesi | Kemungkinan dokumen manual | Perlu dicek | 1 |
| Tarif dan rekening honor | Tarif per pertemuan, aturan potongan, rekening asisten | Form Pendaftaran Asisten (rekening); rekap sheet (Rp25.000/sesi) | Ada sebagian | 1 |
| Analisis gap dan rencana pengembangan lab | Kebutuhan tridharma/kompetensi/sarana/layanan, prioritas, biaya, target, PIC, *roadmap* | Kemungkinan dokumen KaLab/Dekanat | Perlu dicek | 2 |
| Rencana dan realisasi pelatihan laboran | Kebutuhan kompetensi, rencana Diklatfung/bimtek, peserta, anggaran, jadwal, sertifikat, praktik pascapelatihan | Kemungkinan Dekanat SDM | Perlu dicek | 2 |
| Rencana jadwal praktikum | Tanggal, jam, ruang, kelas, pertemuan ke- | Sheet Alokasi Pertemuan Asisten Praktikum | Ada, tetapi kolom Hari dan Jam kosong | 2 |
| Peminjaman lab | Kegiatan lain di ruang yang sama | Form Peminjaman Lab | Ada (tanpa status persetujuan dan cek bentrok) | 2 |
| Modul praktikum | File, versi, tanggal berlaku | Diunggah di Form Asistensi saat/setelah sesi | Belum memenuhi syarat "sebelum sesi" | 2 |
| Bahan per sesi | Komponen IoT, filamen 3D printer, stok BHP | Form 3D Printer; sheet BHP KaLab | Belum dikaitkan ke sesi | 2 |
| Jurnal sesi | Waktu aktual, topik, pertemuan ke-, foto | Form Pelaksanaan Asistensi | Ada (hanya sesi yang punya asisten) | 3 |
| Presensi tingkat kelas | Jumlah praktikan hadir, asisten, laboran, dosen | Form Asistensi: jumlah praktikan, dosen hadir ya/tidak | Ada sebagian (laboran belum dicatat) | 3 |
| Presensi rinci per praktikan | Log presensi per pertemuan per praktikan | **SIMPEL** (diisi dosen) | Ada, di sistem lain | 3 (tautan) |
| Bukti penilaian praktikan | Rubrik, nilai, hasil kerja, *feedback* | **LeADS** | Ada, di sistem lain | 3 (tautan) |
| Perubahan dan sesi pengganti | Pengajuan, persetujuan, sesi asal | — | Belum ada | 3 |
| *Log book* praktikum | Isi kegiatan per sesi | Lembar kegiatan kertas (hanya untuk honor) | Belum memenuhi | 3 |
| ~~Kebutuhan software~~ | ~~Nama, versi, lisensi, ruang~~ | Form Permintaan Software | Tidak dicakup lagi (Persiapan 16) | — |
| ~~Checklist kesiapan sarana~~ | ~~PC, jaringan, proyektor, software~~ | Form Asistensi | Tidak dicakup lagi (Persiapan 16) | — |

**Privasi:** sheet asisten memuat nama, NIM, nomor HP, dan status rekening/KTP. Nilai mahasiswa dari LeADS juga data pribadi. Semua data seed, demo, dan lampiran proposal wajib dianonimkan.

## Pembagian role

Pembagian ini adalah rencana awal per Oct 26, 2026. Tiap role punya indikator, judul, dan rumusan masalah sendiri. Komponen bersama dirancang bersama di awal.

| Role | Modul | Indikator | Tanggung jawab utama | Tugas lintas modul |
|---|---|---|---|---|
| **Role 1** | Personel: Kompetensi, Penugasan & Otorisasi | Pengelolaan 4, 10 | Rekrutmen dan seleksi asprak berbasis kompetensi minimum; register kompetensi laboran dan asisten; daftar tugas/alat berkewenangan khusus dan penerbitan otorisasi; penugasan laboran dan asisten per sesi; surat tugas; rekap honor dari kehadiran | Integrasi dengan modul Rafika; pemilik **register kompetensi** |
| **Role 2** | Perencanaan: Pengembangan Lab & Sesi | Pengembangan 13, 14; Persiapan 15, 17 | Analisis gap dan rencana pengembangan lab beserta realisasinya; rencana, realisasi, dan evaluasi pelatihan laboran; master data; jadwal terpadu dengan cek bentrok dan kapasitas; modul berversi; kebutuhan dan penerimaan bahan per sesi | Pemilik **master data** dan **sesi rencana**; koordinasi dengan kelompok lain |
| **Role 3** | Pelaksanaan, Evaluasi & Dashboard | Proses 18, Evaluasi 19, *dashboard* 8 indikator | Jurnal dan presensi sesi; *log book*; perubahan jadwal dan sesi pengganti; tautan bukti penilaian (LeADS) dan presensi rinci (SIMPEL); registri indikator dan mesin skor; *dashboard* | Pemilik **registri indikator, mesin skor, dan model bukti**; pengujian *black box* dan UAT |

### Benang merah tiap role

- **Role 1: "orang yang tepat."** Memastikan setiap petugas kompeten (Pengelolaan 4) dan berwenang (Pengelolaan 10). Satu register kompetensi melayani dua indikator.
- **Role 2: "perencanaan di dua level."**
  - Level lab, tahunan: lab dan personelnya dikembangkan berdasarkan gap (Pengembangan 13, 14).
  - Level sesi, semesteran: setiap sesi direncanakan, lengkap dengan jadwal, modul, dan bahan (Persiapan 15, 17).
  - Narasi Role 2 perlu menekankan bahwa keduanya sama-sama *perencanaan*. Kalau tidak, scope-nya akan terlihat seperti kumpulan indikator sisa.
- **Role 3: "terlaksana, dinilai, dan terpantau."** Membuktikan sesi terlaksana (Proses 18), praktikan dinilai (Evaluasi 19), dan semua skor terpantau sepanjang periode (*dashboard*).

### Ketergantungan antar role

| Dari | Ke | Yang diserahkan |
|---|---|---|
| Role 2 | Role 1, Role 3 | Master data (periode, MK, kelas, ruang) dan sesi rencana, yang menjadi pembagi Pengelolaan 4 dan Proses 18 |
| Role 2 | Role 1 | Hasil pelatihan laboran (sertifikat, asesmen pascapelatihan), yang masuk ke register kompetensi |
| Role 1 | Role 2 | Data kompetensi dan hasil evaluasi ulang otorisasi, sebagai bukti efektivitas pelatihan (Pengembangan 14 kriteria 4) |
| Role 1 | Role 3 | Petugas per sesi, untuk presensi asisten/laboran dan skor Pengelolaan 4 |
| Role 3 | Role 1 | Presensi asisten pada sesi terlaksana, sebagai dasar honor |
| Role 3 | Role 2 | Hasil *dashboard* (unit yang tidak memenuhi, tren), sebagai data analisis gap Pengembangan 13 |
| Semua role | Role 3 | Aturan indikator masing-masing, untuk didaftarkan ke registri dan mesin skor |

**Urutan kerja yang disarankan:**

1. Sepakati komponen bersama terlebih dahulu: sesi, register kompetensi, registri indikator, dan model bukti.
2. Role 3 membangun importer data historis (sheet Alokasi dan Form Pelaksanaan), supaya punya data uji tanpa menunggu modul Role 1 dan 2 selesai.

### Usulan judul per role (draf, perlu disetujui Pak Widi)

- **Role 1:** Kustomisasi Modul Odoo untuk Penugasan dan Otorisasi Asisten Praktikum dan Laboran Berbasis Kompetensi (Studi Kasus: LabFIK UPN "Veteran" Jakarta)
- **Role 2:** Kustomisasi Modul Odoo untuk Perencanaan Pengembangan Laboratorium dan Penjadwalan Sesi Praktikum Berbasis Instrumen Monev (Studi Kasus: LabFIK UPN "Veteran" Jakarta)
- **Role 3:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan dan Evaluasi Sesi Praktikum serta *Dashboard* Skor Indikator Monev Laboratorium (Studi Kasus: LabFIK UPN "Veteran" Jakarta)

Perubahan dari versi Oct 17:

- Role 1 menambahkan *otorisasi*. Honor tetap dikerjakan, tetapi tidak lagi masuk judul.
- Role 2 mengganti *pemeriksaan kesiapan* (Persiapan 16, dikeluarkan) dengan *perencanaan pengembangan*.
- Role 3 mengganti "perhitungan **otomatis** skor" dengan "*dashboard* skor", karena tidak semua indikator dihitung otomatis.

## Dampak ke Bab 1 tiap role

Tidak semua hal di brief ini perlu masuk ke Pendahuluan. Panduannya:

**Masuk Bab 1:**

| Bagian | Isi |
|---|---|
| 1.1 Latar Belakang | Indikator yang dipegang beserta tuntutannya; kondisi saat ini, yaitu bukti tersebar di Form, Sheets, LeADS, dan SIMPEL dan tidak terhubung; arah solusi di tingkat konsep. Klaim kondisi saat ini wajib didukung wawancara/observasi **[KONFIRMASI]** |
| 1.2 Identifikasi Masalah | Masalah per indikator yang dipegang |
| 1.3 Batasan Masalah | Indikator yang dicakup dan level cakupannya; Persiapan 16 tidak dibahas; LeADS dan SIMPEL tetap sistem sumber (tidak dibangun fitur penilaian maupun integrasi API); indikator paket dokumen dan bukti tertaut tetap diverifikasi penilai |
| 1.4 Tujuan | Satu tujuan per kelompok fungsi yang dibangun |

**Jangan masuk Bab 1** (tempatnya Bab 2, 3, atau 5):

- Rancangan model, field, dan atribut → Bab 3.
- Rumus persentase, aturan skor, dan syarat "memenuhi" secara rinci → Bab 2 (landasan instrumen) atau Bab 3.
- Risiko teknis, misalnya tautan butuh login SSO atau *course* di-*archive* → Bab 3, atau Bab 5 bila terbukti jadi kendala.
- Opsi impor CSV dan integrasi API LeADS/SIMPEL → Bab 5 (saran / penelitian selanjutnya).
- Masalah nomor indikator yang tidak unik → cukup pakai sebutan aspek + nomor secara konsisten.

**Yang pasti bentrok dengan draf lama:**

- Kalimat "lima indikator menjadikan sesi praktikum sebagai unit yang dihitung" perlu diganti. Unitnya sekarang campuran.
- Klaim "skor dihitung otomatis" hanya berlaku untuk indikator level otomatis.
- Daftar indikator di Batasan Masalah perlu diganti mengikuti pembagian role baru.

## Risiko dan mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Role 2 terlihat tidak koheren (dokumen tahunan + operasional sesi) | Dipertanyakan di seminar proposal | Bingkai sebagai "perencanaan di dua level" dan tunjukkan alurnya (gap → pelatihan; jadwal → sesi) |
| Register kompetensi dibangun dua kali (Role 1 dan Role 2) | Data tidak sinkron, bukti Pengelolaan 4/10 dan Pengembangan 14 saling bertentangan | Register dimiliki Role 1; Role 2 hanya menulis hasil pelatihan ke register itu |
| Dokumen Pengembangan 13/14 tidak ada di FIK | Kriteria 1 tidak terpenuhi, skor 1, dan sistem tidak punya data nyata | Cek ke KaLab/Dekanat sejak awal; bila belum ada, sistem menjadi alat untuk *menyusunnya*, dan data uji memakai skenario |
| Daftar tugas/alat berkewenangan khusus belum ditetapkan | Pembagi Pengelolaan 10 tidak jelas | Tetapkan bersama KaLab sebagai bagian dari analisis kebutuhan Role 1 |
| Akses LeADS/SIMPEL terbatas (login SSO, hak akses role dosen) | Penilai tidak bisa membuka tautan bukti Evaluasi 19 | Cek tampilan dan hak akses role dosen dan KaLab; siapkan cadangan berupa unggahan file |
| Mesin skor hanya mendukung persentase | Pengembangan 13/14 tidak bisa tampil di *dashboard* | Rancang registri indikator dengan dua jenis skor sejak awal |
| Scope bertambah lagi | Beban kerja melebihi waktu skripsi | Pakai level cakupan: indikator tambahan cukup masuk level bukti tertaut lebih dulu |

## Pertanyaan terbuka

**Untuk Pak Widi**

- [x] ~~Apakah scope 5 indikator disetujui?~~ Scope diubah menjadi 8 indikator per Oct 26, 2026 (rencana awal).
- [x] ~~Apakah pembagian role di atas (Role 1: Pengelolaan 4, 10; Role 2: Pengembangan 13, 14, Persiapan 15, 17; Role 3: Proses 18, Evaluasi 19, *dashboard*) disetujui?~~ Ya, disetujui
- [ ] Persiapan 16 dikeluarkan karena apa? Apakah dipindah ke kelompok lain? Kalau iya, perlukah datanya terhubung ke sesi kami?
- [ ] Untuk Pengembangan 13 dan 14 (paket dokumen), apakah cukup di level semi-otomatis (alur + bukti per kriteria)?
- [ ] Untuk Evaluasi 19, apakah MVP berupa tautan bukti ke LeADS dan SIMPEL diterima?
- [x] ~~Satu judul per orang, atau satu judul bersama?~~ Satu judul per orang
- [x] ~~Modul Rafika di-*extend* langsung, atau hanya dijadikan acuan?~~ Acuan
- [ ] Persiapan 17 dinyatakan N/A, atau dicakup terbatas (lab IoT, 3D printer)?
- [ ] Apa dasar resmi bahwa audit 2026 mengarah ke ISO/IEC 17025 (surat/SK), untuk dikutip di latar belakang?
- [ ] Odoo versi berapa, dan apakah semua kelompok memakai satu server?

**Untuk KaLab/laboran**

- [x] ~~Bisakah Rangkuman Alokasi Slot Praktikum dan sheet jawaban Form Asistensi, Form Peminjaman Lab, dan Form Pendaftaran Asisten di-*share*?~~ shared
- [ ] Bagaimana alur seleksi dan penugasan asisten sekarang, dan siapa yang menerbitkan surat tugas?
- [x] ~~Bagaimana honor asprak dihitung (tarif per pertemuan, syarat, siapa yang menyetujui)?~~ Berdasarkan bukti submit jurnal sesi, dan pengisian bukti pada kertas.
- [ ] Apakah ada sesi praktikum tanpa asisten, dan bagaimana pelaksanaannya dicatat?
- [ ] Bukti kompetensi laboran apa yang sudah ada (ijazah, pelatihan, sertifikat)?
- [ ] Tugas atau alat apa saja di LabFIK yang hanya boleh dijalankan personel tertentu? Bagaimana izinnya diberikan sekarang?
- [ ] Apakah ada dokumen rencana pengembangan lab atau analisis kebutuhan (roadmap, renstra lab)? Siapa yang mengesahkan?
- [ ] Apakah ada rencana atau rekaman pelatihan laboran/PLP (Diklatfung, bimtek, sertifikasi)? Siapa yang mengelola di Dekanat SDM?
- [ ] Bagaimana prosedur saat sesi batal atau diganti?