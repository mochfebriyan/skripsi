# Brief Modul Pelaksanaan Praktikum

14 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20 · Bagian dari proyek LabFIK Compliance (lihat [brief-seluruh-projek.md](brief-seluruh-projek.md))

**Status: DRAF.** Hasil Langkah 0 (prasyarat rancangan). Bahan Bab I dan 2.2. Belum dikonfirmasi ke Pak Widi dan KaLab.

## Ringkasan

- **Modul:** Pelaksanaan Praktikum (rencana nama addon Odoo: `labfik_praktikum`).
- **Indikator:** 6 dari 21 indikator proyek, satu package per indikator. Semuanya masuk lingkup (keputusan Herrens, 14 Nov 2026).
  - PKG-15 Persiapan 15 (jadwal dan modul)
  - PKG-16 Persiapan 16 (kesiapan alat dan *software*)
  - PKG-17 Persiapan 17 (bahan praktikum)
  - PKG-18 Proses 18 (sesi terlaksana)
  - PKG-19 Evaluasi 19 (penilaian individual praktikan)
  - PKG-20 Evaluasi 20 (kepuasan pengguna)
- **Peran di Core:** modul ini **membangkitkan Sesi**, satu-satunya transaksi di `labfik_core`, yang dipakai juga oleh PKG-04 (SDM) dan PKG-08 (kelompok Aset). Karena itu PKG-15 adalah hulu modul ini dan sebagian modul lain.
- **Benang merah:** setiap sesi praktikum bisa ditelusuri dari **rencana → kesiapan → pelaksanaan → penilaian**, direkam saat terjadi oleh orang yang bertugas, bukan dikumpulkan menjelang monev atau untuk keperluan honor saja.
- **Status:** keenam package sudah dianalisis (Langkah 0 selesai). Belum ada rancangan teknis maupun kode.
- **Usulan judul (draf, perlu persetujuan Pak Widi):** Kustomisasi Modul Odoo untuk Pengelolaan Pelaksanaan Praktikum Berbasis Instrumen Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta) **[KONFIRMASI]**

## Indikator yang dipegang

| Package | Bunyi singkat | PJ | Jenis skor · unit | Level cakupan | Kompleksitas | Analisis |
|---|---|---|---|---|---|---|
| **PKG-15** Persiapan 15 | Jadwal penggunaan lab dan modul praktikum tersedia sebelum setiap kegiatan | KaLab; dosen pengampu | Persentase · sesi rencana | Otomatis | 7 | [analisis-data-persiapan-15.md](../analisis/analisis-data-persiapan-15.md) |
| **PKG-16** Persiapan 16 | Alat, *software*, dan utilitas dinyatakan siap sebelum setiap sesi | PLP/laboran; dosen | Persentase · sesi dilaksanakan | Otomatis | 3 | [analisis-data-persiapan-16.md](../analisis/analisis-data-persiapan-16.md) |
| **PKG-17** Persiapan 17 | Bahan tersedia dalam jumlah, mutu, dan kondisi sesuai sebelum sesi (**bersyarat**) | PLP/laboran | Persentase · sesi berbahan | Otomatis | 5 | [analisis-data-persiapan-17.md](../analisis/analisis-data-persiapan-17.md) |
| **PKG-18** Proses 18 | Sesi terlaksana sesuai jadwal, modul, dan waktu | Dosen; KaLab | Persentase · sesi rencana | Otomatis | 6 | [analisis-data-proses-18.md](../analisis/analisis-data-proses-18.md) |
| **PKG-19** Evaluasi 19 | Praktikan dinilai individual dengan rubrik dan bukti unjuk kerja sesuai CPMK | Dosen; asisten | Persentase · praktikan (pendekatan dari sesi asesmen) | Bukti tertaut | 4 | [analisis-data-evaluasi-19.md](../analisis/analisis-data-evaluasi-19.md) |
| **PKG-20** Evaluasi 20 | Kepuasan pengguna diukur, dianalisis, dan dipakai untuk perbaikan | KaLab; GKM | **Kriteria K1–K4** · paket per periode | Semi-otomatis | 5 | [analisis-data-evaluasi-20.md](../analisis/analisis-data-evaluasi-20.md) |

Acuan ISO/IEC 17025 yang dirujuk instrumen: 6.4.4 (PKG-16), 6.4 dan 6.6 (PKG-17), 8.6.2 (PKG-20). Acuan pendukung dari analisis: 7.2.1 dan 8.3 (modul), 7.5.1 (rekaman sesi).

**Bukan lingkup modul ini:** baris instrumen lain yang juga bernomor Evaluasi 19, "Ketercapaian CPMK praktikum dianalisis untuk seluruh mata kuliah" (PJ Dosen, Koor Prodi, GKM).

## Pola bersama di dalam modul

Keenam package bertumpu pada **dua objek** dan **dua cara menumpang**, sehingga jumlah tabel baru kecil: 8 transaksi milik modul (PKG-15: 3, PKG-16: 1, PKG-18: 2, PKG-20: 2, salah satunya perluasan `survey.survey`), 0 master lokal.

| Pola | Dipakai oleh | Isi |
|---|---|---|
| **A. Sesi sebagai tulang punggung** | 15, 16, 17, 18, 19 | Sesi bertanggal (Core) dibangkitkan PKG-15, diperiksa kesiapannya (16, 17), dilaporkan pelaksanaannya (18), dan menjadi tempat catatan penilaian (19). Indikator 15, 16, 17, dan 18 adalah **persentase sesi** |
| **B. Versi Modul sebagai daftar kebutuhan** | 15, 16, 17, 19 | Dosen menerbitkan modul berversi (tanpa pengesahan) yang memuat berkas modul, **daftar *software***, **daftar bahan per pertemuan**, dan **rubrik**. Pemeriksaan dan penilaian merujuk ke daftar ini, bukan ke master baru |
| **C. Menumpang sebagai tabel anak** | 17 → 16, 19 → 18 | Bahan menjadi kategori butir di Pemeriksaan Kesiapan (16); penilaian menjadi catatan di Jurnal Sesi (18). Satu package = satu indikator tetap terpenuhi tanpa tabel sendiri |
| **D. Paket bertangga K1–K4** | 20 | Survei (addon `survey` Odoo) + Evaluasi Survei dengan Rencana Tindak Lanjut, memakai `labfik.criteria.mixin` dari Core |

```
PKG-15 ─ bangkitkan Sesi (Core) + terbitkan Versi Modul (software, bahan, rubrik)
   │
   ├─▶ PKG-16 Pemeriksaan Kesiapan per sesi ◀── PKG-17 butir "bahan"
   │        └─ keputusan tunda ─▶ Perubahan Sesi (PKG-18)
   │
   └─▶ PKG-18 Jurnal Sesi + Perubahan Sesi ◀── PKG-19 catatan penilaian
PKG-20 Survei + Evaluasi Survei (berdiri sendiri, hanya Core)
```

## Kondisi saat ini (ringkas)

Rincian lengkap (22 temuan, pelaku, dan bedah per bagian dokumen) ada di [studi dokumen](../analisis/bedah-dokumen-praktikum.md).

**Rumusan *as-is* ringkas:** LabFIK sudah punya prosedur praktikum dan lebih dari seribu laporan pelaksanaan, tetapi rekaman itu dibuat untuk honor asisten, bukan sebagai bukti mutu. Jadwal tidak bertanggal, modul tidak berversi, kesiapan dinilai asisten sesudah sesi, perubahan sesi tidak tercatat, kelas tanpa asisten tidak terekam, bukti penilaian dan kepuasan tidak ada di lab, dan prosedurnya belum disahkan.

Sumber: POB Manajemen Praktikum dan Asistensi FIK 2025 (nyata, belum disahkan), sheet "Alokasi Pertemuan Asisten Praktikum", dan Google Form "Pelaksanaan Asistensi Praktikum" (1.147 laporan, 4 periode; diolah 14 Nov 2026, hanya angka agregat). Paket dokumen praktikum 2026 dan Paket Dokumen Monev di Drive LabFIK adalah **draf** (kemungkinan GPT) dan hanya dipakai sebagai contoh format.

| Area | Kondisi | Rujukan |
|---|---|---|
| Jadwal | Tidak ada sesi bertanggal: kolom hari dan jam kosong di seluruh 222 baris kelas (3 periode); tidak ada kolom ruang dan jumlah mahasiswa | PKG-15 A1, A10 |
| Modul | Diunggah ulang asisten di setiap laporan (1.062 berkas unik dari 1.064 laporan), tanpa versi, sesudah sesi | PKG-15 A9 |
| Pemakaian lab lain dan konflik | Tidak diatur di dokumen nyata; 24 tumpang tindih ruang di laporan akibat salah isi jam | PKG-15 A5, A11 |
| Kesiapan | Dicatat asisten, bukan laboran; 104 laporan "Siap" mencatat kendala; 11 sesi "Belum Siap" tetap berjalan | PKG-16 A3 |
| Bahan | Hampir tidak ada; jejak hanya sesi *crimping* kabel LAN dan kemungkinan praktikum IoT | PKG-17 A2, A3 |
| Pelaksanaan | Pencatatan dibuat untuk honor asisten; kelas tanpa asisten (42–56%) tidak punya rekaman; cakupan laporan sesi berasisten 64–75%; laporan ganda, durasi tidak valid (13%), keterlambatan sampai >30 hari; tidak ada presensi laboran; perubahan sesi tidak tercatat | PKG-18 A1–A9 |
| Penilaian | Dikerjakan dosen di LeADS; lab tidak memegang data penilaian; rubrik, remediasi, dan moderasi belum diatur | PKG-19 A1–A5 |
| Kepuasan | Kuesioner ada di POB, tetapi tidak ditemukan data respons; butir belum mencakup keselamatan dan akses | PKG-20 A1–A5 |

Wawancara KaLab dan laboran (sheet "Wawancara FIKLAB Compliance", bagian Pelaksanaan Praktikum P1–P19) **belum dijawab** per 14 Nov 2026.

## Lingkup kebutuhan

| Area | Yang harus bisa dibuktikan sistem |
|---|---|
| Jadwal dan modul (PKG-15) | Sesi bertanggal dibangkitkan dari kelas × pola mingguan; penetapan dan publikasi jadwal per periode; pemakaian lab di luar praktikum dengan persetujuan; cek konflik ruang dan kapasitas; versi modul berlaku sebelum sesi; jadwal terpadu dan rekaman konflik |
| Kesiapan (PKG-16, 17) | Pemeriksaan kesiapan oleh laboran sebelum sesi, dengan butir per kategori (PC, *software* sesuai modul, jaringan, listrik, proyektor, bahan bila ada), keputusan siap/tunda, dan substitusi bahan yang disetujui |
| Pelaksanaan (PKG-18) | Satu jurnal per sesi berisi jam aktual, modul yang dipakai, presensi petugas, jumlah praktikan hadir, *log book*; perubahan sesi dengan persetujuan dan sesi pengganti |
| Penilaian (PKG-19) | Catatan penilaian di sesi asesmen: bentuk individual, rubrik dari modul, jumlah dinilai/umpan balik/remediasi, tautan bukti LeADS |
| Kepuasan (PKG-20) | Survei per periode yang ditetapkan (populasi, target respons, enam aspek), respons anonim, rekap per aspek, evaluasi dan rencana tindak lanjut, perbandingan antarperiode |
| Status monev | Persentase PKG-15–19 beserta daftar unit yang tidak memenuhi; kriteria tertinggi K1–K4 PKG-20 |

## Cakupan rancangan (usulan awal)

Ditetapkan di Langkah 1 setelah arahan pembimbing; tabel ini usulan dari hasil analisis **[USULAN PENULIS]**. Prinsipnya mengikuti CLAUDE.md bagian 1: lantai ditentukan instrumen, langit-langit ditentukan kejelasan.

| Area | Inti (W) | Pelengkap (O) |
|---|---|---|
| PKG-15 | Bangkitkan Sesi; penetapan jadwal; rencana pemakaian lab + persetujuan; versi modul (berkas, *software*, bahan, rubrik); cek konflik dan kapasitas; persentase | Impor kelas dari sheet alokasi; jadwal terpadu per ruang per minggu |
| PKG-16, 17 | Pemeriksaan kesiapan per sesi dengan butir dan keputusan; butir bahan dengan substitusi; persentase | Rekap kesiapan per ruang |
| PKG-18 | Jurnal sesi (presensi petugas, jumlah hadir, *log book*); perubahan sesi + sesi pengganti; persentase | Rekap keterlaksanaan per kelas; peringatan keterlambatan pengisian |
| PKG-19 | Catatan penilaian di jurnal; rubrik di modul; persentase pendekatan | Daftar kelas tanpa bukti penilaian |
| PKG-20 | Survei (*extend* `survey`) dengan aspek, populasi, target; evaluasi + RTL; status K1–K4 | Perbandingan antarperiode dalam bentuk grafik |

Yang **tidak dirancang** tercantum di batasan masalah.

## Kontrak dengan modul lain

**Yang disediakan modul ini:**

| Data | Dipakai oleh | Catatan |
|---|---|---|
| **Sesi** (dibangkitkan dan dipublikasikan) | PKG-04 (SDM), PKG-08 (kelompok Aset), 16, 17, 18, 19 | Model `labfik.sesi` di `labfik_core`, tidak mewarisi `op.session` (keputusan 14 Nov 2026) |
| Isi Mata Kuliah dan Kelas (impor dari alokasi, jumlah mahasiswa) | Semua pemakai Kelas | Model di Core; modul ini yang pertama mengisinya |
| Presensi petugas per sesi (Jurnal Sesi) | PKG-04 (opsional, untuk mencocokkan dengan penugasan) | — |

**Yang dipakai modul ini:**

| Data | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Periode, Ruang Lab, Mata Kuliah, Kelas, Personel, Jabatan | Core | Wajib | — |
| `labfik.criteria.mixin` | Core | Wajib (PKG-20) | — |
| `labfik.controlled.mixin` (kode, revisi) | Core | Wajib (Versi Modul) | — |
| `labfik.approval.mixin` + `labfik.approval.log` | Core | Wajib (Penetapan Jadwal; jadwal harus ditandatangani) | — |
| `labfik.evidence.mixin` | Core | Wajib (Pemeriksaan Kesiapan, Jurnal Sesi, Evaluasi Survei) | — |
| Addon `survey` | Odoo 17 CE (LGPL-3) | Wajib (PKG-20, keputusan 14 Nov 2026) | Google Form + impor |
| Penugasan petugas per sesi | PKG-04 (SDM) | Opsional | Presensi petugas tanpa pencocokan |
| Status kalibrasi alat | PKG-05 (kelompok Aset) | Opsional | Dianggap tidak berlaku untuk lab komputer |
| Kartu stok bahan | PKG-07 (kelompok Aset) | Opsional | Jumlah tersedia dicatat saat pemeriksaan |

### Kontrak Core (Langkah 3)

14 November 2026 · Herrens. Aturan CLAUDE.md Langkah 3: pakai master dan *mixin* yang sudah dirancang di Tata Kelola (tag `rancangan-tatkel-v1`, dengan penyesuaian CLAUDE.md bagian 6: Personel = `hr.employee`, Jabatan = `hr.job`, pengesahan tanpa tahap pemeriksaan). Bila butuh perubahan, **diusulkan ke pemiliknya**, tidak dibuat versi sendiri. Nama field di bawah masih **[USULAN PENULIS]**, ditetapkan di Langkah 10.

**a. Yang dipakai apa adanya**

| Model / *mixin* Core | Dipakai untuk | PKG |
|---|---|---|
| Personel (`hr.employee` diperluas) | Dosen, laboran, teknisi, asisten: pengisi jurnal, petugas hadir, pemeriksa kesiapan, penyusun modul, penyetuju, PIC RTL. **Praktikan tidak dicatat sebagai Personel** | 15–20 |
| Jabatan (`hr.job` diperluas) + `cari_pemegang_berwenang(tindakan, jenis)` | Jabatan yang dipakai: Kepala Laboratorium, Laboran/PLP, Teknisi, Dosen, **Asisten Praktikum**. Untuk menentukan siapa boleh mengesahkan jadwal, menyetujui pemakaian lab dan perubahan sesi, menetapkan survei, dan mengisi jurnal | 15, 18, 20 |
| `labfik.controlled.mixin` (kode, revisi, unit pemilik) | Versi Modul (revisi = nomor versi) | 15 |
| `labfik.approval.mixin` + `labfik.approval.log` (ajukan → kembalikan / unggah PDF bertanda tangan → sahkan → cabut; cek wewenang; riwayat; hook `_setelah_disahkan()`) | Penetapan Jadwal: **jadwal harus ditandatangani** (keputusan Herrens, 14 Nov 2026). Hook `_setelah_disahkan()` mengisi tanggal publikasi dan menandai Sesi periode itu sebagai terpublikasi | 15 |
| `labfik.evidence.mixin` (tanggal, pelapor, bukti, keterangan; rekaman tidak dihapus) | Pemeriksaan Kesiapan, Jurnal Sesi, Evaluasi Survei | 16, 18, 20 |
| `labfik.criteria.mixin` (`status_k1`–`k4`, `kriteria_tertinggi`, `_cek_k1()`–`_cek_k4()` {abstract}) | Perluasan `survey.survey` sebagai paket per periode | 20 |

**b. Yang tidak dipakai, dan alasannya**

| Model / *mixin* | Alasan |
|---|---|
| `labfik.approval.mixin` untuk Versi Modul, Survei, Rencana Pemakaian Lab, Perubahan Sesi | Modul cukup diterbitkan (keputusan 14 Nov 2026); survei cukup "ditetapkan"; pemakaian lab dan perubahan sesi cukup disetujui. Ketiganya memakai status sederhana + cek wewenang lewat Jabatan, tanpa berkas bertanda tangan |
| `labfik.period.mixin` | Tidak ada objek Praktikum yang "kedaluwarsa" berdasarkan periode; cukup `periode_id` biasa |
| Mahasiswa (Core, di pemetaan) | Praktikum tidak menyimpan data per praktikan (batasan masalah 3) |

**c. Usulan perubahan ke Core (perlu disetujui pemiliknya)**

| Model | Usulan | Untuk | Kepada |
|---|---|---|---|
| `labfik.ruang` | Field `kode`, `name`, **`kapasitas`** (Integer). Isi awal 8 ruang: FIKLAB-201, 301–304, 401–403 | PKG-15 C3 (sesuai kapasitas); PKG-08 kelompok Aset juga memakainya | Kelompok (Core bersama) **[KONFIRMASI kelompok]** |
| `labfik.periode` | Field `name`, `jenis` (semester / tahun anggaran), **`tanggal_mulai`, `tanggal_selesai`** | Batas pembagi PKG-15–19; sesi pengganti harus selesai sebelum periode ditutup (PKG-18) | Kelompok (Core bersama) **[KONFIRMASI kelompok]** |
| `labfik.jabatan.wewenang` | Tambah pasangan (tindakan, jenis): (`mengesahkan`, `jadwal_praktikum`), (`menyetujui`, `pemakaian_lab`), (`menyetujui`, `perubahan_sesi`), (`menetapkan`, `survei_kepuasan`) | Cek wewenang PKG-15, 18, 20 | Febriyan (pemilik Jabatan) |
| Personel | Asisten (mahasiswa) dicatat sebagai `hr.employee` dengan Jabatan **Asisten Praktikum** (`hr.job`) — **diputuskan** (Herrens, 14 Nov 2026) dan dicatat di CLAUDE.md bagian 6. Alasannya: asisten perlu jabatan untuk cek wewenang dan syarat kompetensi (SDM), dan jabatan selalu menempel pada Personel. Pihak eksternal masih terbuka | Presensi asisten, pengisi jurnal | Kelompok (diberi tahu) |

**d. Model Core yang diisi modul ini** (keputusan 14 Nov 2026; kontraknya ditulis di sini karena Praktikum yang paling hulu)

| Model | Field (garis besar) | Aturan |
|---|---|---|
| `labfik.mata.kuliah` [M] | `kode` «unique», `name`, `prodi`, `semester` | Kode MK sebagai kunci impor (nama MK tidak seragam antarperiode) |
| `labfik.kelas` [M] | `mata_kuliah_id`, `periode_id`, `name`, `jumlah_mahasiswa`, `dosen_koordinator_id`, `dosen_ids` | Unik per (MK, periode, nama kelas) |
| `labfik.sesi` [T] | `kelas_id`, `pertemuan_ke`, `tanggal`, `jam_mulai`, `jam_selesai`, `ruang_id`, `state`, `sesi_asal_id` (bila pengganti) | Dibangkitkan hanya oleh PKG-15 (atau sebagai pengganti lewat Perubahan Sesi PKG-18). Satu Sesi asli per (kelas, pertemuan). Nama status ditetapkan di state machine (Langkah 5) |

**e. Aturan pakai bersama untuk Sesi** **[USULAN PENULIS; KONFIRMASI kelompok]**
- Modul lain (SDM PKG-04, Aset PKG-08) **tidak menambah field** ke `labfik.sesi`. Mereka membuat modelnya sendiri yang merujuk `sesi_id` (misalnya penugasan petugas per sesi), sehingga `labfik_core` tidak bergantung pada modul mana pun.
- Hanya Praktikum yang mengubah status Sesi.
- Sesi yang sudah punya jurnal atau penugasan tidak boleh dihapus; perubahan jadwal dilakukan lewat Perubahan Sesi.

**Dampak ke rencana addon:** brief bersama mencatat `labfik_praktikum` bergantung pada `labfik_sdm`, ditambah jembatan `labfik_praktikum_aset` untuk PKG-16/17. Hasil analisis menunjukkan semua kaitan ke SDM dan Aset bersifat opsional. Usulan: `labfik_praktikum` cukup `depends: ['labfik_core', 'survey']`, dan addon jembatan tidak diperlukan **[KONFIRMASI kelompok]**.

## Batasan masalah (usulan)

1. **Indikator:** PKG-15 s.d. 20. Baris "Ketercapaian CPMK praktikum dianalisis" (Evaluasi 19 yang lain) tidak dicakup.
2. **Tanpa integrasi** dengan SIAKAD, SIMPEL, LeADS, atau sistem jadwal fakultas. Data kelas diimpor dari berkas; presensi rinci dan bukti penilaian berupa tautan.
3. **Tidak menyimpan data per praktikan** (presensi per nama, nilai). Presensi praktikan berupa jumlah; penilaian berupa jumlah per sesi asesmen. Konsekuensinya persentase PKG-19 adalah pendekatan **[KONFIRMASI pembimbing]**.
4. **Tanpa master baru** untuk *software* dan bahan: keduanya ditulis per modul. Master Alat, Bahan, dan stok adalah wilayah kelompok Aset.
5. **Rekap honor asisten** (tarif, rekening, pengajuan) tidak dirancang.
6. **Tidak dirancang:** penjadwalan otomatis, kalender libur, pengingat (modul, jurnal, lisensi, survei), pemeriksaan per unit PC, register insiden, saluran pengaduan tersendiri, alur remediasi, *snapshot* tren skor.
7. **PKG-17 bersyarat:** berlaku hanya untuk sesi yang modulnya mencantumkan bahan; N/A untuk periode tanpa sesi semacam itu.
8. **Skor:** persentase PKG-15–19 dihitung sistem (PKG-19 berupa pendekatan dengan bukti tertaut); PKG-20 hanya menunjukkan kriteria tertinggi yang lengkap secara data, skor akhir ditetapkan penilai.
9. **Platform:** Odoo 17 Community, tanpa OpenEduCat. Modul Rafika (`skripsi_rafika/`) hanya acuan.
10. **Data:** data uji fiktif. Data nyata (sheet alokasi dan formulir asistensi) hanya diolah menjadi angka agregat untuk observasi.
11. **Sistem adalah alat** pencatatan, pembuktian, dan pemantauan; tidak menjamin skor monev naik.

## Masalah → tujuan → fitur

| Masalah (1.2) | Tujuan (1.4) | Fitur |
|---|---|---|
| M1. Tidak ada jadwal sesi bertanggal yang ditetapkan sebelum semester; jam dan ruang diketik ulang asisten saat melapor, sehingga pembagi indikator tidak terbentuk dan konflik tidak terdeteksi (PKG-15 A1, A11) | T1. Jadwal sesi yang ditetapkan dan dipublikasikan sebelum sesi, dengan cek konflik dan kapasitas | Bangkitkan Sesi, penetapan jadwal, rencana pemakaian lab |
| M2. Modul tidak berversi dan tidak terbukti tersedia sebelum sesi (PKG-15 A9) | T2. Modul berversi yang terbit sebelum sesi dan menjadi acuan kebutuhan *software*, bahan, dan rubrik | Versi modul |
| M3. Kesiapan sarana dicatat asisten sesudah sesi, tidak konsisten, dan tanpa keputusan tunda (PKG-16 A3) | T3. Pemeriksaan kesiapan oleh laboran sebelum sesi dengan keputusan siap/tunda | Pemeriksaan kesiapan |
| M4. Pencatatan pelaksanaan dibuat untuk honor, sehingga kelas tanpa asisten tidak terekam dan kualitas rekaman rendah (PKG-18 A1–A9) | T4. Satu jurnal per sesi untuk semua kelas, dengan presensi petugas dan perubahan sesi yang disetujui | Jurnal sesi, perubahan sesi |
| M5. Bukti penilaian individual dan kepuasan pengguna tidak ada di lab (PKG-19 A1–A2, PKG-20 A5) | T5. Bukti penilaian per sesi asesmen dan survei kepuasan per periode beserta tindak lanjutnya | Catatan penilaian, survei, evaluasi survei |
| M6. Status indikator dihitung manual dan tidak tertelusur ke bukti | T6. Status monev: persentase per indikator dan K1–K4 PKG-20, tertaut ke bukti | Status monev |

**Klaim kondisi** di M1–M6 bersumber dari dokumen dan data nyata; konfirmasi KaLab lewat wawancara tetap diperlukan sebelum dikutip di Bab I **[KONFIRMASI]**.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Siapa mengisi jurnal (dan catatan penilaian) untuk kelas tanpa asisten belum jelas; tanpa pengisi, PKG-18 dan 19 tidak terbukti untuk 42–56% kelas | Tanyakan di wawancara P10, P13; rancangan tidak mengikat peran pengisi (asisten, dosen, atau laboran) |
| Pemeriksaan kesiapan per sesi terlalu berat untuk laboran | Siapkan opsi satu pemeriksaan per ruang per hari (wawancara P8) |
| Persentase PKG-19 berupa pendekatan ditolak pembimbing | Ajukan sejak awal; alternatifnya presensi dan status penilaian per nama (lebih berat, data pribadi) |
| Dosen tidak menerbitkan modul berversi atau rubrik | Mulai dari satu MK pilot; jalan pengganti berupa tautan berkas di jurnal |
| Modul ini hulu bagi SDM dan Aset (Sesi); keterlambatan menghambat modul lain | Sepakati model Sesi lebih dulu (sudah di Core); bangun fitur bangkitkan Sesi paling awal |
| Data nyata berisi data pribadi asisten | Hanya angka agregat yang dikutip; data uji fiktif; minta izin KaLab sebelum angka dikutip di proposal |
| Klaim kondisi saat ini tanpa konfirmasi | Wawancara KaLab dan laboran terdokumentasi sebagai lampiran |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Apakah judul di atas disetujui?
- [ ] Apakah persentase PKG-19 berupa pendekatan dari sesi asesmen (tanpa data per praktikan) dapat diterima?
- [ ] Apakah skor akhir PKG-20 (kriteria berurutan) boleh ditetapkan penilai, sementara sistem menunjukkan kriteria yang lengkap secara data?

**Untuk KaLab dan laboran (wawancara P1–P19, wajib sebagai lampiran)** — rinciannya di bagian 9 tiap analisis. Yang paling menentukan rancangan:
- [ ] Sumber dan waktu penetapan jadwal; siapa membagi ruang (P2).
- [ ] Siapa mengisi catatan sesi, termasuk kelas tanpa asisten (P10, P13).
- [ ] Pemeriksaan kesiapan per sesi atau per hari; siapa berhak menunda (P8).
- [ ] Praktikum mana yang memakai bahan fisik (P9).
- [ ] Rubrik, penilai, dan remediasi (P14).
- [ ] Pernah tidaknya survei kepuasan dan saluran keluhan (P16).
- [ ] Fungsi kolom "Status" (TRUE/FALSE) di formulir asistensi (P11).

**Untuk kelompok (Febriyan, Zahir)**
- [ ] `labfik_praktikum` cukup `depends: ['labfik_core', 'survey']`, tanpa `labfik_sdm` dan tanpa addon jembatan Aset?
- [ ] Rencana Tindak Lanjut PKG-20 dijadikan entitas bersama "Tindak Lanjut" di Core, atau tetap di modul ini?
- [ ] PKG-17 dinyatakan "dicakup terbatas" (menutup pertanyaan terbuka di brief bersama setelah wawancara P9)?

## Langkah berikutnya

1. Wawancara KaLab dan laboran untuk bagian Pelaksanaan Praktikum; perbarui temuan *as-is* di setiap analisis.
2. Konfirmasi judul dan dua aturan skor (PKG-19, PKG-20) ke Pak Widi.
3. **Langkah 1:** catat arahan pembimbing dan tetapkan cakupan rancangan (Inti/Pelengkap) di brief ini.
4. **Langkah 2:** bedah dokumen (POB 2025, sheet alokasi, formulir asistensi, kuesioner) menjadi `bedah-dokumen-praktikum.md`.
5. **Langkah 4:** kebutuhan sistem `kebutuhan-praktikum.md` dengan kode `KF-PRK-nn`.
