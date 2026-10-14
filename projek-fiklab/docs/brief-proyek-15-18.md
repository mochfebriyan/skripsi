# Brief Proyek: LabFIK Compliance, Modul Persiapan & Proses Praktikum

**Status:** usulan kelompok ke Pak Widi (pembimbing). Belum final.
**Terakhir diperbarui:** 14 Oktober 2026
**Cakupan indikator:** Instrumen Monev Laboratorium UPNVJ 2026, aspek **Persiapan Praktikum 15, 16, 17** dan **Proses Praktikum 18**

> **Cara membaca dokumen ini**
> Bagian 1–3 menjelaskan konteks bagi pembaca yang belum tahu apa-apa. Bagian 4–7 berisi isi proyek: indikator, data, dan sistem. Bagian 8–11 berisi risiko, pertanyaan terbuka, dan langkah berikutnya. Istilah asing dijelaskan di **Lampiran A (Glosarium)**.

---

## Ringkasan Satu Paragraf

Laboratorium Fakultas Ilmu Komputer (LabFIK) UPN "Veteran" Jakarta setiap tahun dinilai melalui **Instrumen Monev Laboratorium UPNVJ 2026**. Instrumen ini berisi 64 indikator yang masing-masing diberi skor 1–4, dan skornya hanya diakui kalau ada bukti yang bisa diverifikasi. Saat ini kegiatan lab dicatat lewat banyak Google Form dan Google Sheets yang tidak saling terhubung, sehingga bukti monev harus dikumpulkan dan dihitung manual. Kami mengusulkan membangun modul berbasis **Odoo** yang menangani **jadwal dan pelaksanaan sesi praktikum**. Setiap sesi tercatat dari rencana, persiapan, sampai terlaksana, sehingga skor empat indikator (Persiapan 15–17 dan Proses 18) bisa **dihitung otomatis** dan ditelusuri sampai ke sesi asalnya. Proyek ini adalah bagian dari proyek besar **LabFIK Compliance** yang dikerjakan bersama kelompok lain.

---

## 1. Konteks: Apa itu LabFIK dan Monev?

### 1.1 LabFIK

LabFIK melayani praktikum dan penggunaan fasilitas lab untuk mahasiswa dan dosen FIK (D3 Sistem Informasi, S1 Sistem Informasi, S1 Informatika, S1 Sains Data). LabFIK punya **8 ruang lab**:

| Kode | Bidang |
|---|---|
| LABFIK 201 | Software Engineering |
| LABFIK 301 | Immersive dan Multimedia |
| LABFIK 302 | AI dan Robotics |
| LABFIK 303 | Big Data dan Data Science |
| LABFIK 304 | Cyber Security dan Networking |
| LABFIK 401 | Internet of Things (IoT) |
| LABFIK 402 | Enterprise System |
| LABFIK 403 | E-Governance |

Layanan diakses lewat **Portal Layanan LabFIK** (https://lab.fik.upnvj.ac.id). Hampir semua layanannya berupa tautan ke Google Form.

### 1.2 Monev Laboratorium

**Monev** (monitoring dan evaluasi) adalah penilaian mutu lab oleh universitas. Acuannya file **Instrumen Monev Laboratorium UPNVJ 2026 v1.1** (ada di folder `docs/`). Isinya:

- **64 indikator** dalam **5 aspek**:

  | Aspek | Jumlah indikator |
  |---|---|
  | Pengelolaan Laboratorium | 21 |
  | Pengembangan Laboratorium | 8 |
  | Persiapan Praktikum | 11 |
  | Proses Praktikum | 11 |
  | Evaluasi Praktikum | 13 |

- Total **341 butir bukti dukung** yang diminta.
- Setiap indikator diberi **skor 1–4**, dengan dua cara penilaian:
  - **"1 paket dokumen dan rekaman"** (28 indikator): kriteria 1–4 diperiksa berurutan. Contoh: ada SOP, struktur organisasi.
  - **"100% unit yang memenuhi"** (36 indikator): skor ditentukan dari **persentase unit yang memenuhi syarat**.

    | Persentase unit memenuhi | Skor |
    |---|---|
    | 100% dan bukti dapat diverifikasi | 4 |
    | 90% sampai < 100% | 3 |
    | 70% sampai < 90% | 2 |
    | < 70%, **atau bukti tidak dapat diverifikasi** | 1 |

> **Poin kunci:** walaupun kegiatannya sudah dilakukan dengan benar, **kalau buktinya tidak bisa ditunjukkan, skornya otomatis 1**. Jadi pencatatan yang rapi sama pentingnya dengan kegiatannya sendiri.

Instrumen ini disusun dengan acuan antara lain **SNI ISO/IEC 17025:2017** (standar lab pengujian dan kalibrasi), Pedoman Diklatfung PLP 2022, dan Standar SPMI UPNVJ 2025. Karena acuannya standar lab pengujian, sebagian indikator (kalibrasi, bahan kimia, limbah B3, dan sejenisnya) kemungkinan **tidak berlaku** untuk lab komputer.

### 1.3 Proyek besar: LabFIK Compliance

**LabFIK Compliance** adalah inisiatif untuk memindahkan pengelolaan LabFIK dari Google Form/Sheets ke **satu sistem berbasis Odoo**, supaya data operasional lab **otomatis menjadi bukti monev**. Itu sebabnya disebut "Compliance": patuh terhadap instrumen monev.

- Dikerjakan oleh **beberapa kelompok skripsi**. Setiap kelompok memegang sebagian indikator.
- Arahan pembimbing (Pak Widi): **cover indikator sebanyak mungkin**. Yang tidak tercover tahun ini dilanjutkan skripsi tahun depan.
- **Kelompok kami mengusulkan indikator Persiapan 15–17 dan Proses 18.**

---

## 2. Masalah yang Ingin Diselesaikan

1. **Data tersebar.** Setiap layanan punya form dan sheet sendiri. Jadwal praktikum, peminjaman lab, pelaksanaan asistensi, dan permintaan software tidak saling terhubung.
2. **Tidak ada satu daftar "sesi praktikum" yang utuh.** Rencana sesi ada di rangkuman alokasi slot. Pelaksanaan sesi dicatat lewat form asistensi, tapi **hanya untuk sesi yang punya asisten**. Tidak ada yang mencocokkan rencana dengan realisasi.
3. **Form hanya mencatat pengajuan, bukan alurnya.** Form peminjaman lab tidak punya status persetujuan dan **tidak mengecek bentrok jadwal**.
4. **Bukti monev disusun manual.** Untuk menghitung "berapa persen sesi yang terlaksana sesuai jadwal", seseorang harus menggabungkan beberapa sheet dan menghitung sendiri menjelang monev.
5. **Data tidak konsisten.** Contohnya penamaan ruang: "LABFIK 201" di form peminjaman, tapi "FIKLAB-201" di form asistensi.
6. **Sebagian bukti masih di kertas.** Lembar Penggunaan Sarana adalah dokumen cetak berisi paraf, sehingga tidak bisa dihitung otomatis.

> *Catatan:* poin di atas berasal dari analisis form dan dokumen yang tersedia. Detail dampaknya (berapa lama rekap, contoh kasus bentrok, data hilang) **perlu dikonfirmasi lewat wawancara** dengan KaLab/laboran.

---

## 3. Kenapa Indikator 15–18?

> ⚠️ **Hati-hati dengan nomor.** Nomor ID di file instrumen **tidak unik**. Nomor 15 muncul tiga kali, dan nomor 17 serta 18 juga muncul di aspek lain. Selalu sebut **aspeknya** (misalnya "Persiapan 15", "Proses 18") atau kutip teks indikatornya.

Alasan memilih empat indikator ini:

1. **Saling berurutan dan membentuk satu alur:** *direncanakan* (15) → *disiapkan* (16, 17) → *dilaksanakan* (18). Satu modul bisa melayani keempatnya.
2. **Semuanya dinilai dengan persentase**, jadi skornya bisa dihitung otomatis oleh sistem.
3. **Datanya sebagian sudah ada**, terutama di Form Pelaksanaan Asistensi dan Form Peminjaman Lab, sehingga tidak mulai dari nol.
4. **"Sesi praktikum" adalah fondasi bagi indikator lain.** Sekitar 8 indikator lain juga menghitung "÷ seluruh sesi praktikum", misalnya petugas sesuai kompetensi (Pengelolaan 4), kapasitas sesi (Pengelolaan 8), supervisi (Proses Q02), dan penutupan sesi (Proses Q10). Kalau modul sesi sudah ada, kelompok lain atau angkatan berikutnya tinggal menambahkan datanya.
5. **Ada bonus:** dari data jadwal, laporan utilisasi ruang (jam tersedia vs terpakai) bisa langsung dibuat sebagai bukti untuk indikator Pengembangan "pemanfaatan kapasitas dan waktu dievaluasi".

---

## 4. Rincian Indikator

Keempat indikator memakai **sesi praktikum** sebagai unit yang dihitung.

### 4.1 Persiapan 15: Jadwal & modul tersedia sebelum kegiatan

| | |
|---|---|
| **Bunyi indikator** | Jadwal penggunaan laboratorium dan modul praktikum tersedia sebelum setiap kegiatan. |
| **Penanggung jawab** | KaLab; dosen pengampu |
| **Unit memenuhi** | Sesi praktikum dengan jadwal sah tanpa konflik, serta modul berlaku tersedia sebelum sesi |
| **Populasi (pembagi)** | Seluruh sesi praktikum yang **direncanakan** pada periode monev |
| **Syarat memenuhi** | Jadwal sesuai kapasitas; kegiatan lain tercatat; modul relevan tersedia dan dapat diakses sebelum pelaksanaan |
| **Bukti dukung** | (1) Jadwal terpadu praktikum dan kegiatan lain, (2) persetujuan pemakaian, (3) modul versi berlaku, (4) bukti publikasi sebelum sesi, (5) rekaman konflik jadwal |

### 4.2 Persiapan 16: Alat, software & utilitas siap sebelum sesi

| | |
|---|---|
| **Bunyi indikator** | Peralatan, perangkat lunak dan utilitas yang diperlukan dinyatakan siap sebelum setiap sesi praktikum. |
| **Penanggung jawab** | PLP/laboran; dosen |
| **Unit memenuhi** | Sesi dengan seluruh alat/software/utilitas wajib siap dan diterima sebelum dimulai |
| **Populasi** | Seluruh sesi praktikum yang **dilaksanakan** pada periode monev |
| **Syarat memenuhi** | Fungsi dan kelengkapan sesuai modul; keamanan terverifikasi; status kalibrasi berlaku bila perlu; software sah dan bekerja; ketidaksiapan diselesaikan sebelum sesi |
| **Bukti dukung** | (1) Checklist sebelum sesi, (2) uji fungsi, (3) status kalibrasi bila relevan, (4) versi/lisensi software sesuai penggunaan, (5) pemeriksaan listrik/gas/air, (6) keputusan siap/tunda |

### 4.3 Persiapan 17: Bahan praktikum tersedia sebelum sesi *(bersyarat)*

| | |
|---|---|
| **Bunyi indikator** | Bahan praktikum tersedia dalam jumlah, mutu dan kondisi yang sesuai sebelum setiap sesi. |
| **Penerapan** | **Bersyarat:** hanya jika praktikum menggunakan bahan fisik |
| **Penanggung jawab** | PLP/laboran |
| **Unit memenuhi** | Sesi yang seluruh kebutuhan bahan wajibnya terpenuhi dan diterima sebelum dimulai |
| **Populasi** | Seluruh sesi praktikum yang **menggunakan bahan** |
| **Syarat memenuhi** | Jumlah cukup; mutu dan masa pakai sesuai; bahan diberi label; substitusi disetujui |
| **Bukti dukung** | (1) Daftar kebutuhan per sesi, (2) stok/lot/kedaluwarsa, (3) persiapan larutan/media, (4) kriteria penerimaan, (5) checklist dan catatan substitusi |

> **Status:** kemungkinan **berlaku terbatas**. Sebagian besar praktikum FIK berbasis komputer (tanpa bahan), tetapi lab **401 IoT** (komponen habis pakai) dan **3D printer** (filamen) bisa terhitung. Template inventaris KaLab juga punya sheet *Sparepart & BHP*. **Perlu keputusan pembimbing:** dinyatakan N/A, atau dicakup hanya untuk lab/sesi yang memakai bahan.

### 4.4 Proses 18: Sesi praktikum terlaksana sesuai jadwal

| | |
|---|---|
| **Bunyi indikator** | Sesi praktikum terlaksana sesuai jadwal, modul dan waktu kegiatan yang ditetapkan. |
| **Penanggung jawab** | Dosen; KaLab |
| **Unit memenuhi** | Sesi rencana yang terlaksana sesuai ketentuan, atau dengan perubahan sah yang tujuan/waktunya setara |
| **Populasi** | Seluruh sesi praktikum yang **direncanakan** pada periode monev |
| **Syarat memenuhi** | Kegiatan, durasi dan tujuan sesuai; perubahan sah; **sesi tertunda baru dihitung memenuhi setelah sesi pengganti selesai** dalam periode pelaporan |
| **Bukti dukung** | (1) Jadwal, (2) jurnal sesi, (3) presensi praktikan, asisten, laboran, dosen pendamping, (4) modul yang dipakai, (5) log book praktikum, (6) perubahan yang disetujui, (7) penggantian sesi |

### 4.5 Contoh perhitungan

Misalnya dalam satu semester direncanakan **120 sesi** praktikum, dan **114 sesi** punya jadwal sah, tidak bentrok, dan modulnya tersedia sebelum sesi:

> Persiapan 15 = 114 ÷ 120 = **95%** → **skor 3**

Sistem menampilkan skor 3 dan **daftar 6 sesi yang tidak memenuhi beserta alasannya**, sehingga KaLab tahu persis apa yang perlu diperbaiki.

---

## 5. Kebutuhan Data

### 5.1 Data master (dipakai keempat indikator)

| Data | Isi |
|---|---|
| Periode | Tahun ajaran dan semester (contoh: 2026/2027 Ganjil) |
| Ruang lab | Kode, nama, **kapasitas** (jumlah PC/stasiun yang berfungsi) |
| Mata kuliah praktikum | Kode, nama, prodi |
| Kelas praktikum | Kelas (A–F, PBI), jumlah peserta, dosen pengampu, asisten |
| Personel & peran | Dosen, laboran/PLP, asisten, praktikan, KaLab |
| Kebutuhan per mata kuliah | Software (dengan versi/lisensi), alat, bahan (bila ada) |
| Modul praktikum | File, versi, tanggal berlaku, per mata kuliah |

### 5.2 Data per sesi

| Data | Untuk indikator |
|---|---|
| Rencana sesi: tanggal, jam, ruang, kelas, pertemuan ke- | 15, 18 |
| Status persetujuan jadwal dan penyetujunya | 15 |
| Rekaman konflik jadwal dan penyelesaiannya | 15 |
| Waktu publikasi jadwal dan modul (harus sebelum sesi) | 15 |
| Checklist kesiapan: PC, jaringan, proyektor, software, listrik/AC; petugas; waktu cek | 16 |
| Keputusan siap / tunda, dan tindak lanjut kalau tidak siap | 16 |
| Kebutuhan dan ketersediaan bahan per sesi (bila berlaku) | 17 |
| Jurnal sesi: waktu mulai/selesai aktual, topik | 18 |
| Presensi praktikan, asisten, laboran, dosen | 18 |
| Modul yang dipakai | 18 |
| Perubahan jadwal beserta persetujuannya; sesi pengganti | 18 |

---

## 6. Kondisi Data Saat Ini (As-Is)

### 6.1 Sumber data yang ditemukan

| Sumber | Bentuk | Isi penting |
|---|---|---|
| **Form Peminjaman Lab** | Google Form | Kelompok (mahasiswa/dosen), nama, NIM/NIDN, ruang (8 lab), **jumlah unit komputer**, tanggal & jam mulai/akhir, kategori kegiatan (penelitian/pendidikan/pengabdian/kemahasiswaan), nama kegiatan, dosen PJ, dokumen pendukung. **Tidak ada status persetujuan atau cek bentrok.** |
| **Form Pelaksanaan Asistensi** | Google Form, diisi asisten **per pertemuan** | Mata kuliah (15 MK berkode), kelas, hari, tanggal, jam mulai/akhir, ruang, **pertemuan ke-** (1–14, tanpa 8), **jumlah kehadiran mahasiswa**, **dosen hadir?**, topik, **kesiapan sarana** (Siap / Belum Siap / Dapat Disesuaikan), keterangan kendala, **upload modul**, foto pelaksanaan |
| **Form Pendaftaran Asisten** | Google Form | Data calon asisten, mata kuliah target, nilai (A/A-), dosen pemberi rekomendasi, KHS |
| **Form Permintaan Software** | Google Form (dosen) | Nama & versi software, **jenis lisensi**, tanggal mulai/akhir pemakaian, ruang instalasi, nama kegiatan/mata kuliah |
| **Form Peminjaman 3D Printer** | Google Form | Tanggal & jam, dosen pembimbing, objek yang dicetak, **perkiraan panjang filamen** |
| **Lembar Penggunaan Sarana** | Google Doc, **dicetak dan diisi tangan** | Tanggal, nama kegiatan, kode ruang, acuan pengajuan; tabel nama, NIM/NIDN, alat, waktu mulai/selesai, **status akhir alat**, paraf; foto dokumentasi |
| **Rangkuman Alokasi Slot Praktikum** | Google Sheets (tertaut di portal) | Kemungkinan rencana jadwal praktikum per semester. **Belum bisa diakses.** |
| **Integrated_Kalibrasi_Inventory_LabFIK_UPNVJ** | Google Sheets milik KaLab (dibuat Juli 2026) | Sheet MASTER_ASET (sekitar 290 aset), STOCK_OPNAME, kategori Server/PC, Jaringan, IoT, Audio Visual, Kelistrikan/UPS, Sparepart & BHP, maintenance log, kalibrasi, dan **staging ekspor ke CMDBuild/openMAINT** |

Daftar lengkap isian form tersimpan di [`form.md`](form.md).

### 6.2 Perbandingan kebutuhan vs data yang ada

Legenda: 🟢 sudah ada · 🟡 ada sebagian / perlu dicek · 🔴 belum ada

| Kebutuhan | Sumber sekarang | Status |
|---|---|---|
| **Master data** | | |
| Daftar ruang | Semua form (8 lab) | 🟢 |
| Kapasitas ruang / jumlah PC | MASTER_ASET (kolom belum dicek) | 🟡 |
| Daftar mata kuliah praktikum | Form Asisten & Asistensi (15 MK berkode) | 🟢 |
| Kelas | Form Asistensi (A–F, PBI) | 🟢 |
| **Persiapan 15** | | |
| Rencana jadwal praktikum rutin | Rangkuman Alokasi Slot Praktikum | 🟡 Belum diakses |
| Kegiatan lain di jadwal yang sama | Form Peminjaman Lab | 🟢 |
| Persetujuan pemakaian | Tidak ada di form; mungkin dicatat manual | 🟡 |
| Rekaman konflik jadwal | — | 🔴 |
| Modul versi berlaku, tersedia **sebelum** sesi | Modul diunggah di Form Asistensi, tapi **saat/setelah** sesi dan tanpa versi | 🟡 Belum memenuhi syarat |
| Bukti publikasi jadwal | — | 🔴 |
| **Persiapan 16** | | |
| Status siap per sesi | Form Asistensi: "Kesiapan Sarana" | 🟡 Satu pilihan saja, bukan checklist; diisi asisten, bukan laboran |
| Software sesuai kebutuhan | Form Permintaan Software | 🟢 |
| Kondisi alat | MASTER_ASET / MAINTENANCE_LOG | 🟡 |
| **Persiapan 17** | | |
| Bahan per sesi | Form 3D Printer (filamen); sheet BHP KaLab | 🟡 Belum dikaitkan ke sesi praktikum |
| **Proses 18** | | |
| Jurnal sesi (topik, waktu, pertemuan ke-) | Form Asistensi | 🟢 |
| Presensi praktikan | Hanya **jumlah**, bukan per nama | 🟡 |
| Presensi asisten | Pengisi Form Asistensi | 🟢 |
| Presensi dosen | "Dosen hadir? Ya/Tidak" | 🟢 |
| Presensi laboran | — | 🔴 |
| Modul yang dipakai | Upload di Form Asistensi | 🟢 |
| Log book alat | Lembar Penggunaan Sarana (kertas) | 🟡 Tidak digital |
| Perubahan jadwal & sesi pengganti | — | 🔴 |

### 6.3 Temuan penting

1. **Form Pelaksanaan Asistensi sudah berfungsi sebagai jurnal sesi.** Ini sumber data terkuat untuk Proses 18 dan sebagian Persiapan 16.
2. **Tapi form itu hanya mencatat sesi yang punya asisten.** Padahal indikator menghitung **seluruh** sesi yang direncanakan. Rencana sesi harus diambil dari Alokasi Slot Praktikum lalu **dicocokkan** dengan realisasi.
3. **Pilihan pertemuan melompat dari 7 ke 9.** Pertemuan 8 kemungkinan UTS. Sistem harus bisa menandai sesi yang memang tidak dijadwalkan, supaya tidak dihitung "tidak terlaksana".
4. **Penamaan ruang tidak konsisten** (LABFIK 201 vs FIKLAB-201), jadi perlu satu master ruang.
5. **Peminjaman lab tidak punya alur persetujuan atau cek bentrok.** Ini celah paling jelas yang bisa diisi sistem baru untuk Persiapan 15.
6. **KaLab sudah menyiapkan template inventaris untuk diekspor ke CMDBuild/openMAINT** (platform manajemen aset lain). Perlu kejelasan apakah data aset tetap dikelola di sana atau dipindah ke Odoo (lihat Bagian 9).

---

## 7. Usulan Solusi (To-Be)

### 7.1 Gambaran umum

Satu modul Odoo, sementara dinamai **"Sesi Praktikum LabFIK"**, yang mencatat setiap sesi praktikum melalui empat tahap:

```
 [1] DIRENCANAKAN ──► [2] DISIAPKAN ──► [3] DILAKSANAKAN ──► [4] SELESAI / DIGANTI
   jadwal disetujui      checklist           jurnal & presensi      dihitung ke skor
   cek bentrok           kesiapan alat,      diisi asisten/         monev
   modul terpasang       software, bahan     dosen/laboran
     ▲                                                               │
     └────────── perubahan jadwal / sesi pengganti (disetujui) ◄─────┘
```

### 7.2 Fitur

| Fitur | Penjelasan | Indikator |
|---|---|---|
| **Master data** | Ruang + kapasitas, mata kuliah, kelas, periode, personel & peran | Semua |
| **Jadwal terpadu** | Sesi praktikum dan peminjaman lab dalam satu kalender per ruang | 15 |
| **Cek bentrok & kapasitas otomatis** | Sesi/peminjaman yang bentrok atau melebihi kapasitas ditolak atau ditandai, dan **konfliknya tercatat** | 15 |
| **Alur persetujuan** | Diajukan → disetujui KaLab/laboran → dipublikasikan, dengan waktu dan penyetuju tercatat | 15 |
| **Modul praktikum berversi** | Modul diunggah per mata kuliah dengan versi dan tanggal berlaku; sistem cek "tersedia sebelum sesi" | 15, 18 |
| **Checklist kesiapan sebelum sesi** | Diisi laboran: PC, jaringan, proyektor, software, listrik/AC; keputusan siap/tunda | 16 |
| **Kebutuhan bahan per sesi** *(bila berlaku)* | Daftar bahan dan konfirmasi ketersediaan | 17 |
| **Jurnal & presensi sesi** | Menggantikan Form Pelaksanaan Asistensi: waktu aktual, topik, presensi empat pihak, foto | 18 |
| **Perubahan & sesi pengganti** | Pengajuan perubahan dengan persetujuan; sesi pengganti terhubung ke sesi asalnya | 18 |
| **Dashboard skor** | Persentase dan skor 1–4 per indikator, bisa diklik sampai ke daftar sesi yang tidak memenuhi | 15–18 |
| **Hak akses per peran** | Memakai security bawaan Odoo (groups, access rights, record rules) | Pendukung |
| **Jejak perubahan** | Riwayat perubahan per record (chatter/audit trail Odoo) | Pendukung |

### 7.3 Peran pengguna

| Peran | Yang bisa dilakukan |
|---|---|
| **KaLab** | Menyetujui jadwal/perubahan, melihat dashboard skor, mengelola master data |
| **Laboran/PLP** | Mengelola jadwal ruang, mengisi checklist kesiapan, presensi laboran |
| **Dosen pengampu** | Mengunggah modul, mengajukan perubahan/sesi pengganti, konfirmasi kehadiran |
| **Asisten praktikum** | Mengisi jurnal sesi dan presensi |
| **Mahasiswa/dosen (peminjam)** | Mengajukan peminjaman lab |
| **GKM / penilai monev** | Melihat skor dan bukti (hanya baca) |

### 7.4 Rumus skor otomatis

| Indikator | Rumus |
|---|---|
| Persiapan 15 | sesi (jadwal disetujui ∧ tanpa konflik ∧ ≤ kapasitas ∧ modul tersedia sebelum sesi) ÷ sesi direncanakan |
| Persiapan 16 | sesi (checklist lengkap ∧ keputusan "siap" sebelum mulai) ÷ sesi dilaksanakan |
| Persiapan 17 | sesi (bahan wajib tersedia sebelum mulai) ÷ sesi yang memakai bahan |
| Proses 18 | sesi (terlaksana sesuai rencana ∨ diganti dengan pengganti yang sudah selesai) ÷ sesi direncanakan |

Hasil persentase dikonversi ke skor: 100% → 4, 90 sampai <100% → 3, 70 sampai <90% → 2, <70% → 1.

### 7.5 Yang **tidak** termasuk scope

- Indikator monev di luar Persiapan 15–17 dan Proses 18 (dipegang kelompok lain atau tahun depan).
- Pengelolaan inventaris, kalibrasi, dan maintenance (sudah ada template KaLab; kemungkinan modul/kelompok lain).
- Pendaftaran dan seleksi asisten, survei kepuasan, pelaporan kendala.
- Modul "rapor" monev untuk ke-64 indikator. Modul kami hanya **menyediakan angka** untuk empat indikatornya.
- Integrasi dengan SIAKAD (kecuali kalau aksesnya tersedia).

---

## 8. Keterkaitan dengan Kelompok Lain

Karena beberapa kelompok bekerja di satu sistem, perlu disepakati:

1. **Fondasi bersama:** master ruang, personel/peran, mata kuliah, dan periode harus **satu versi** untuk semua kelompok. Perlu ditentukan siapa yang memegangnya.
2. **Format "lapor ke rapor":** setiap modul menyediakan angka *unit memenuhi / total unit* per indikator ke modul rapor monev (kalau dibuat kelompok lain).
3. **Kesepakatan teknis:** versi Odoo, satu server/database bersama, dan aturan penamaan modul.
4. **Modul kami sebagai pondasi "sesi":** indikator lain yang menghitung per sesi (petugas kompeten, kapasitas, supervisi, penutupan sesi) bisa **menambahkan data ke sesi yang kami buat**, tanpa membuat tabel sesi sendiri.

---

## 9. Risiko & Hal yang Perlu Diwaspadai

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Data rencana jadwal (Alokasi Slot) tidak bisa diakses atau formatnya tidak per sesi | Pembagi (populasi) untuk 15 dan 18 tidak bisa dihitung | Minta akses sedini mungkin; kalau perlu, jadwal disusun ulang di sistem |
| Laboran belum terbiasa mengisi checklist kesiapan (proses baru) | Indikator 16 tetap rendah walaupun sistemnya ada | Checklist dibuat singkat (bisa dari HP); koordinasi dengan judul transformasi digital |
| Arah CMDBuild/openMAINT dari KaLab bertabrakan dengan Odoo | Data aset/kapasitas ganda | Klarifikasi ke KaLab; opsi Odoo hanya membaca data dari CMDBuild |
| Pembagian dengan kelompok lain belum jelas | Fitur dobel atau saling bergantung | Rapat kesepakatan fondasi bersama di awal |
| Nomor ID di instrumen dobel dan instrumen masih v1.1 | Salah rujuk, requirement berubah | Pakai kode indikator internal yang stabil; pantau revisi instrumen |
| Waktu UAT bergantung pada semester berjalan | Uji coba nyata terlambat | Rencanakan uji coba di semester Genap 2026/2027 atau dengan data semester lalu |
| Data pribadi (KTP, rekening asisten, NIM) | Risiko privasi | Tidak dimigrasikan kecuali perlu; batasi akses per peran |

---

## 10. Pertanyaan Terbuka

**Untuk Pak Widi**
1. Apakah scope Persiapan 15–17 dan Proses 18 disetujui untuk kelompok kami?
2. Persiapan 17 dinyatakan N/A, atau dicakup terbatas (lab IoT, 3D printer)?
3. Kelompok mana yang memegang fondasi bersama (master data) dan modul rapor monev?
4. Odoo versi berapa, dan apakah semua kelompok memakai satu server?
5. Bagaimana hubungan proyek ini dengan rencana CMDBuild/openMAINT di template KaLab?

**Untuk KaLab/laboran**
6. Bisakah sheet **Rangkuman Alokasi Slot Praktikum** dan sheet jawaban **Form Pelaksanaan Asistensi** serta **Form Peminjaman Lab** di-share (akses lihat)?
7. Jadwal praktikum disusun oleh siapa (lab atau prodi), dan apakah mengacu ke SIAKAD?
8. Kapasitas tiap lab (jumlah PC berfungsi): apakah tercatat di MASTER_ASET?
9. Peminjaman lab disetujui oleh siapa, dan dicatat di mana?
10. Apakah ada sesi praktikum **tanpa asisten**? Bagaimana pelaksanaannya dicatat?
11. Presensi praktikan per nama dicatat di mana (SIAKAD, kertas, atau tidak ada)?
12. Apakah laboran punya checklist sebelum/sesudah sesi, walaupun di kertas?
13. Bagaimana prosedur saat sesi batal atau diganti?
14. Kapan monev berikutnya berlangsung, dan berapa skor indikator-indikator ini pada monev sebelumnya (kalau ada)?

---

## 11. Rencana Langkah Berikutnya

| No | Langkah | Output |
|---|---|---|
| 1 | Konfirmasi scope ke Pak Widi (pertanyaan 1–5) | Scope final |
| 2 | Wawancara KaLab/laboran dan pengumpulan sheet (pertanyaan 6–14) | Catatan wawancara, data as-is |
| 3 | Lengkapi tabel perbandingan (Bagian 6.2) dengan data nyata | Analisis gap final |
| 4 | Rapat kesepakatan fondasi bersama dengan kelompok lain | Daftar master data dan pemilik modul |
| 5 | Desain model data dan alur (sesi, jadwal, checklist, jurnal) | Rancangan sistem |
| 6 | Pengembangan modul Odoo bertahap: jadwal (15) → jurnal (18) → checklist (16) → bahan (17) | Modul Odoo |
| 7 | Migrasi data semester berjalan dari Google Sheets | Data awal di sistem |
| 8 | Pengujian black box dan UAT dengan KaLab, laboran, dosen, asisten | Hasil pengujian |
| 9 | Hitung skor 15–18 sebelum vs sesudah sistem | Bukti dampak |

---

## Lampiran A. Glosarium

| Istilah | Arti |
|---|---|
| **LabFIK** | Laboratorium Fakultas Ilmu Komputer UPN "Veteran" Jakarta |
| **KaLab** | Kepala Laboratorium |
| **PLP / Laboran** | Pranata Laboratorium Pendidikan, staf teknis lab |
| **Asprak** | Asisten praktikum (mahasiswa yang membantu dosen di sesi praktikum) |
| **GKM** | Gugus Kendali Mutu, unit penjaminan mutu di fakultas |
| **Monev** | Monitoring dan evaluasi, penilaian mutu berkala |
| **Instrumen Monev** | Daftar indikator penilaian beserta kriteria skornya (file xlsx) |
| **Indikator** | Satu butir yang dinilai dalam monev, skornya 1–4 |
| **Bukti dukung** | Dokumen atau rekaman yang membuktikan indikator terpenuhi |
| **Unit** | Hal yang dihitung dalam indikator berbasis persentase; di scope ini adalah **sesi praktikum** |
| **Populasi** | Seluruh unit yang diperiksa (pembagi dalam persentase) |
| **Sesi praktikum** | Satu pertemuan praktikum: satu kelas, satu mata kuliah, satu waktu, satu ruang |
| **Modul praktikum** | Materi/panduan yang dipakai dalam sesi praktikum |
| **N/A** | Tidak berlaku (*not applicable*) |
| **BHP** | Bahan habis pakai |
| **Odoo** | Platform aplikasi bisnis open source (ERP) yang bisa dikustomisasi dengan modul sendiri |
| **CMDBuild / openMAINT** | Platform open source untuk manajemen aset dan pemeliharaan |
| **As-is / To-be** | Kondisi sekarang / kondisi yang dituju |
| **UAT** | *User Acceptance Testing*, uji coba oleh pengguna nyata |
| **SIAKAD** | Sistem Informasi Akademik kampus |
| **SNI ISO/IEC 17025** | Standar nasional/internasional untuk kompetensi laboratorium pengujian dan kalibrasi |

## Lampiran B. Dokumen Rujukan

| Dokumen | Lokasi |
|---|---|
| Instrumen Monev Laboratorium UPNVJ 2026 v1.1 | `docs/Instrumen Monev Laboratorium UPNVJ 2026 v1.1.xlsx` |
| SNI ISO/IEC 17025:2017 | `docs/SNI ISO-IEC 17025-2017_ID.md` |
| Isian lengkap form LabFIK | `docs/form.md` |
| Template inventaris KaLab | Google Sheets "Integrated_Kalibrasi_Inventory_LabFIK_UPNVJ" (milik lab_fik@upnvj.ac.id) |
| Portal Layanan LabFIK | https://lab.fik.upnvj.ac.id |
| Brief awal LabFIK Compliance (3 judul) | `brief labfik compliance.md` |
