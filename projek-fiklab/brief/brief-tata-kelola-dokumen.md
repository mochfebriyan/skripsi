# Brief Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13. Bagian dari proyek LabFIK Compliance (lihat [brief-seluruh-projek.md](brief-seluruh-projek.md))

**Status: DRAF.** Scope skripsi final (1 November 2026); cakupan rancangan ditetapkan 14 November 2026. Bahan Bab I (1.2, 1.3, 1.4) dan dasar seluruh rancangan TO-BE.

## Ringkasan

- **Modul:** Tata Kelola & Dokumen (rencana nama addon Odoo: `labfik_org`, lihat [brief-seluruh-projek.md](brief-seluruh-projek.md#rencana-addon-odoo)).
- **Indikator:** 4 dari 21 indikator proyek. Di proyek ini 1 package = 1 indikator, dan nomor PKG menjadi identitasnya.
  - PKG-01 Pengelolaan 1 (rencana kerja tahunan)
  - PKG-02 Pengelolaan 2 (SOP dan IK)
  - PKG-03 Pengelolaan 3 (struktur organisasi)
  - PKG-13 Pengembangan 13 (rencana pengembangan lab)
- **Master bersama yang dikelola modul ini:**
  - **Personel** dan **Jabatan** (dari PKG-03)
  - **Dokumen Induk** (dari PKG-02)
  - **KPI** (dari PKG-01)

  Personel dan Jabatan dipakai hampir semua package lain, termasuk milik kelompok lain. Karena itu modul ini berada **paling hulu** di proyek.
- **Benang merah:** lab membuktikan bahwa ia punya **struktur, aturan, dan rencana** yang disahkan, dijalankan, dan dievaluasi. Bukti kegiatan direkam saat terjadi, bukan dikumpulkan menjelang monev.
- **Status:** keempat package sudah dianalisis dan dokumen lab sudah dibedah. Rancangan TO-BE disusun berikutnya mengikuti alur di [CLAUDE.md](../../CLAUDE.md) bagian 4 (langkah 4–10), dalam batas [cakupan rancangan](#cakupan-rancangan) di bawah.
- **Usulan judul (draf, perlu persetujuan Pak Widi):** Kustomisasi Modul Odoo untuk Tata Kelola dan Pengendalian Dokumen Laboratorium Berbasis Instrumen Monev (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

## Indikator yang dipegang

| Package | Bunyi singkat | PJ | Jenis skor · unit | Level cakupan | Acuan |
|---|---|---|---|---|---|
| **PKG-01** Pengelolaan 1 | Rencana kerja tahunan memuat sasaran, KPI, target, anggaran, dan penanggung jawab | KaLab; Dekanat | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | Pedoman Diklatfung PLP 2022, Standar SPMI UPNVJ 2025 |
| **PKG-02** Pengelolaan 2 | Seluruh SOP dan IK yang diperlukan tersedia, disahkan, mutakhir, dan dapat diakses pengguna | KaLab; PLP/laboran | Persentase · 1 SOP wajib | Otomatis | ISO/IEC 17025 8.3 |
| **PKG-03** Pengelolaan 3 | Struktur organisasi, tugas, tanggung jawab, wewenang, dan pengganti petugas ditetapkan dan dijalankan | Dekan; KaLab | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | ISO/IEC 17025 5 (5.5–5.6) |
| **PKG-13** Pengembangan 13 | Rencana pengembangan lab didasarkan pada analisis kesenjangan kebutuhan tridharma, kompetensi, sarana, dan layanan | KaLab; Dekanat | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | Pedoman Diklatfung PLP 2022, Standar SPMI UPNVJ 2025 |

Rincian kriteria, aturan memenuhi, entitas, dan dependensi ada di:
- [analisis-data-pengelolaan-1-3.md](../analisis/analisis-data-pengelolaan-1-3.md)
- [analisis-data-pengembangan-13.md](../analisis/analisis-data-pengembangan-13.md)

Temuan kondisi dokumen lab saat ini ada di [bedah-dokumen-tata-kelola.md](../analisis/bedah-dokumen-tata-kelola.md).

Baris lain dengan nomor yang sama **bukan** scope modul ini. Contohnya Pengelolaan 10 (KPI dipantau), Pengelolaan 10 (legalitas), dan Pengelolaan 13 (dokumen mutu dikendalikan). Baris-baris ini memang menempel ke komponen modul ini, jadi dicatat sebagai **kandidat perluasan** (lihat [Batasan masalah](#batasan-masalah)).

## Arahan pembimbing dan keputusan

| Tanggal | Sumber | Isi | Dampak |
|---|---|---|---|
| 13 Nov 2026 | Bimbingan Pak Widi | Dahulukan rancangan **TO-BE** (Bab II 2.3) dengan **UML**, sebelum Bab I dan 2.1 Observasi | Urutan kerja: rancangan dulu |
| 13 Nov 2026 | Bimbingan Pak Widi | Class Odoo dirancang dengan **inheritance**, supaya field dan perilaku tidak ditulis berulang | Perilaku bersama (pengesahan, dokumen terkendali, periode, kriteria, bukti) dirancang sekali lalu diwarisi |
| 13 Nov 2026 | Bimbingan Pak Widi | Proses pendokumentasian di FIK sebagian besar belum ada; observasi as-is boleh dari studi dokumen dan ISO 17025 selama wawancara belum ada | 2.1 Observasi memakai temuan bedah dokumen |
| 13 Nov 2026 | Febriyan | Dokumen rutin diisi di sistem lalu diekspor; SOP/IK diunggah. Pengesahan tanpa tanda tangan digital | Batasan masalah 2 dan 3 |
| 14 Nov 2026 | Febriyan | **Dekan tidak memakai sistem.** Dekan hanya menandatangani dokumen cetak. KaLab mencatat hasilnya di sistem: pengesah tercatat = Dekan, pencatat = KaLab | Dekan bukan aktor sistem |
| 14 Nov 2026 | Febriyan | **Memeriksa dan mengesahkan adalah satu kesatuan.** Pejabat yang mengesahkan dianggap sudah memeriksa isi dokumen; catatan pengesahan menjadi buktinya | Tidak ada tahap pemeriksaan terpisah. Kolom "Diperiksa" di blok tanda tangan dokumen cetak tetap di kertas saja |
| 14 Nov 2026 | Febriyan | **Renstra berlaku 5 tahun** (draf lab: 2027–2031), jadi cukup diunggah dan disahkan, tidak diisi lewat form | Rencana kerja tahunan merujuk Renstra lewat teks |
| 14 Nov 2026 | Febriyan | Cakupan rancangan proposal = lapis **Inti + Pelengkap** | Bagian [Cakupan rancangan](#cakupan-rancangan) |
| 14 Nov 2026 | Bimbingan Pak Widi | Lihat addon yang bisa di-*extend* (OCA, Cybro, OpenEduCat, dll.), utamakan lisensi LGPL | Bagian [Platform dan addon yang diperluas](#platform-dan-addon-yang-diperluas) |
| 14 Nov 2026 | Febriyan | Personel dan Jabatan meng-*extend* `hr.employee` dan `hr.job`; master bersama dan mixin di addon `labfik_core` yang **terpisah** dari `labfik_org` | Perlu disepakati kelompok **[KONFIRMASI]** |

## Pola bersama di dalam modul

Keempat package hanya memakai **dua pola**. Karena itu modulnya bisa dibangun sebagai komponen yang dipakai ulang, bukan empat fitur terpisah.

| Pola | Dipakai oleh | Alurnya |
|---|---|---|
| **A. Paket dokumen bertangga K1–K4** | PKG-01, PKG-03, PKG-13 | Ditetapkan/disahkan → isinya lengkap → dijalankan (rekaman) → dievaluasi dan diperbaiki |
| **B. Dokumen terkendali berversi** | PKG-02. Juga menyimpan PDF SK (PKG-03), rencana bertanda tangan (PKG-01, 13), dan Renstra | Draf → diajukan → disahkan (berlaku) → diganti / dicabut / kedaluwarsa, dengan distribusi, sosialisasi, dan tinjau ulang |

Kedua pola memakai **satu mekanisme pengesahan** yang sama:

```
Penyusun ajukan ─▶ cetak & tanda tangan di luar sistem ─▶ unggah PDF bertanda tangan ─▶ KaLab sahkan
                   (KaLab sendiri, atau Dekan)                                          atau kembalikan dengan alasan
```

Pengesahan dicek terhadap **wewenang jabatan** dan setiap kejadian (diajukan, dikembalikan, berkas diunggah, disahkan, dicabut, kedaluwarsa) **dicatat sebagai riwayat**, bukan hanya status terakhir.

PKG-01 dan PKG-13 polanya **sama persis**: rencana (+ item) → realisasi → tinjauan. Keduanya memakai satu konsep rencana yang dibedakan **jenis**-nya (tahunan / pengembangan). Pembedanya PKG-13: temuan gap per aspek, prioritas berbasis risiko dan manfaat, dan pengukuran manfaat di tinjauan. Renstra bukan rencana yang diisi di sistem, melainkan dokumen unggahan yang dirujuk.

Hubungan antar-package:

```
PKG-03 Struktur ──(Personel, Jabatan: PIC, pengesah, peserta, wewenang)──▶ PKG-01, PKG-02, PKG-13
PKG-02 Register dokumen ──(PDF SK, rencana bertanda tangan, Renstra)──▶ PKG-03, PKG-01, PKG-13
PKG-01 Renstra (unggahan) ◀──(dirujuk lewat teks)── item rencana tahunan dan pengembangan
PKG-01 Master KPI ──▶ dipakai juga PKG-21 (kelompok Aset)
```

## Lingkup kebutuhan

Kebutuhan berikut diturunkan dari bukti dukung dan kriteria di instrumen, lewat analisis.

| Area | Yang harus bisa dibuktikan sistem |
|---|---|
| Struktur (PKG-03) | Personel dan jabatan (tugas, wewenang, atasan, pengganti); penetapan pengelola (SK) berperiode; rapat koordinasi; evaluasi struktur; bagan organisasi dan matriks kewenangan sebagai laporan |
| Dokumen (PKG-02) | Daftar induk SOP/IK beserta dasar kebutuhan dan lokasi penggunaan; versi dengan pengesahan; distribusi ke titik penggunaan; sosialisasi; tinjau ulang; persentase SOP wajib yang memenuhi |
| Rencana kerja (PKG-01) | Renstra sebagai dokumen unggahan yang disahkan; rencana tahunan dengan item: KPI, target, PIC, jadwal, anggaran, rujukan Renstra; pengesahan; realisasi; tinjauan |
| Rencana pengembangan (PKG-13) | Temuan gap per aspek (tridharma, kompetensi, sarana, layanan); item dengan nilai risiko dan manfaat, biaya, target, PIC, jadwal; realisasi; tinjauan dengan pengukuran manfaat |
| Pengesahan (semua) | Ajukan dengan cek kelengkapan; kembalikan dengan alasan; unggah PDF bertanda tangan; sahkan dengan cek wewenang; cabut; riwayat pengesahan |
| Status monev | Skor persentase Pengelolaan 2; untuk Pengelolaan 1, 3, dan Pengembangan 13, kriteria K1–K4 yang sudah berbukti beserta tautan ke rekamannya |

## Cakupan rancangan

Rancangan proposal dibagi dua lapis. Keduanya dirancang penuh dan digambar di diagram Bab II.

| Lapis | Arti | Prioritas implementasi |
|---|---|---|
| **Inti** | Tanpa ini ada kriteria instrumen (K1–K4, S1–S5) yang tidak bisa dibuktikan, atau alur pengesahan putus | Wajib (W) |
| **Pelengkap** | Memperkuat rancangan (format dokumen lab, kelengkapan siklus) dengan biaya kecil | Opsional (O); dibangun bila waktu cukup |

Hal yang menambah kenyamanan atau kedalaman tetapi tidak dibutuhkan untuk membuktikan kriteria **tidak dirancang**; dicatat di [batasan masalah](#batasan-masalah) dan menjadi saran pengembangan.

**Prinsip pemilahan:**
1. **Lantai ditentukan instrumen.** Setiap kriteria K1–K4 dan S1–S5 harus punya kebutuhan dan rekaman bukti.
2. **Satu mekanisme, satu jalur utama.** Pengesahan cukup satu jalur: ajukan → kembalikan atau sahkan → cabut. Penolakan yang terjadi di atas kertas dicatat lewat aksi kembalikan yang sama.
3. **Teks dulu, master kemudian.** Bila analisis menyediakan jalan pengganti berupa teks bebas (rujukan Renstra), master khususnya tidak dibuat.
4. **Unggah dulu, form kemudian.** Dokumen yang jarang berubah (SOP/IK, Renstra) cukup diunggah lalu disahkan.
5. **Hitung, bukan jadwalkan.** Penanda yang bisa dihitung dari data (perlu ditinjau, masih berlaku, realisasi belum diisi) tidak butuh pengingat terjadwal.
6. **Tunjukkan desain.** Inheritance, riwayat pengesahan, dan urutan baku pengesahan yang tidak bisa dilewati tetap dirancang, karena biayanya kecil dan diminta pembimbing.

| Area | Inti | Pelengkap |
|---|---|---|
| **Pengesahan** | Ajukan (cek kelengkapan), kembalikan dengan alasan, unggah PDF bertanda tangan, sahkan (cek wewenang pengesah tercatat), cabut, riwayat pengesahan. Pengesah tercatat = pejabat penanda tangan; pencatat = KaLab | Dokumen berperiode otomatis kedaluwarsa saat periodenya habis (penjadwal harian) |
| **PKG-02 SOP/IK** | Dokumen induk, unggah versi (satu berlaku), distribusi, sosialisasi, tinjau ulang + penanda "perlu ditinjau", persentase memenuhi, daftar induk dan riwayat revisi | Pengguna lab membaca versi berlaku; hanya satu versi yang diproses per dokumen |
| **PKG-03 Struktur** | Personel, jabatan (tugas, wewenang, atasan, pengganti), SK + baris penetapan, rapat, evaluasi, bagan (daftar hierarki), matriks kewenangan (daftar) | Ekspor SK format fakultas |
| **PKG-01 Rencana** | Renstra sebagai dokumen unggahan yang disahkan; rencana tahunan: item dengan KPI, target, PIC, jadwal, anggaran, rujukan Renstra institusi berupa teks; matriks keterkaitan sebagai daftar item per rujukan Renstra; realisasi + bukti; tinjauan → rencana berikutnya; ekspor PDF rencana tahunan; master KPI | Narasi ringkas rencana (ringkasan, latar belakang, tujuan, ruang lingkup) untuk ekspor; revisi rencana; satu dokumen berlaku per jenis dan periode |
| **PKG-13 Pengembangan** | Rencana jenis pengembangan: temuan gap 4 aspek, item dengan nilai risiko dan manfaat, ukuran manfaat di tinjauan | Ekspor PDF rencana pengembangan (template sama dengan rencana tahunan); prioritas dihitung dari risiko × manfaat |
| **Status monev** | Persentase PKG-02; kriteria tertinggi K1–K4 PKG-01/03/13 dengan tautan bukti; akses baca penilai | — |

**Aktor sistem:** KaLab, Laboran/PLP, pengguna lab (asisten, dosen), penilai monev, dan penjadwal (pemicu waktu). Dekan dan pejabat lain yang hanya menandatangani dokumen cetak **bukan aktor sistem**; identitasnya tercatat sebagai pengesah.

## Kontrak dengan modul lain

**Yang disediakan modul ini:**

| Master / data | Dipakai oleh | Catatan |
|---|---|---|
| Personel | 01, 02, 03, 04, 06, 07, 10, 13, 14, 15, 18, 21 | Mencakup dosen, laboran/PLP, asisten (mahasiswa), petugas K3, pihak eksternal. NIP/NIM adalah data pribadi. Opsi modelnya ada di analisis Pengelolaan 3 |
| Jabatan | 01, 02, 03, 04, 13, 14, 18 | Termasuk **syarat kompetensi minimum** yang dibutuhkan PKG-04 dan PKG-14. Perlu disepakati dengan Zahir (SDM) |
| Wewenang dari jabatan | Semua modul | Siapa yang boleh mengesahkan atau menyetujui mengikuti jabatan aktif, bukan diatur terpisah per modul |
| Mekanisme pengesahan bersama | Semua dokumen yang perlu disahkan (mis. rencana pelatihan PKG-14) | Satu jalur: ajukan → kembalikan / sahkan → cabut, dengan riwayat. Tanpa tahap pemeriksaan terpisah |
| Dokumen Induk + versi | 02, 03, 09 (SOP limbah); kandidat Persiapan 15 (versi modul) | Pola versi sama dengan "modul berversi" di Persiapan 15 |
| KPI | 01, 21 | — |

**Yang dipakai modul ini dari modul lain (semuanya opsional, ada jalan pengganti):**

| Data | Dari | Untuk | Bila tidak ada |
|---|---|---|---|
| Penugasan petugas per sesi, presensi petugas | SDM (PKG-04), Praktikum (PKG-18) | Pengelolaan 3 K3 (penugasan mengikuti struktur), rekap beban kerja K4 | K3–K4 dari rapat dan evaluasi saja |
| Skor indikator monev | *Dashboard* / registri indikator (belum ada pemiliknya) | Realisasi KPI (Pengelolaan 1 K3) dan data gap layanan (Pengembangan 13) | Diinput manual |
| Gap kompetensi personel | SDM (PKG-04 matriks kompetensi, PKG-14) | Aspek kompetensi di temuan gap Pengembangan 13 | Diisi manual |
| Kondisi alat dan pemeliharaan | Aset (PKG-07, PKG-12, PKG-21) | Aspek sarana di temuan gap Pengembangan 13 | Diisi manual |

Sebaliknya, **gap kompetensi** dari Pengembangan 13 bisa menjadi masukan kebutuhan pelatihan di Pengembangan 14 (SDM). Hubungan ini opsional dan perlu disepakati.

## Platform dan addon yang diperluas

Arahan Pak Widi: lihat addon yang sudah ada (OCA, CybroAddons, OpenHRMS, EducationalERP, OpenEduCat, dll.) untuk di-*extend*, dengan mengutamakan lisensi **LGPL**.

Modul ini tetap berupa addon sendiri (`labfik_org`, `depends: ['labfik_core']`). Master bersama, perluasan `hr`, dan mixin bersama ada di addon **`labfik_core`** yang terpisah (keputusan 14 November 2026, [KONFIRMASI kelompok]). Kedua addon bergantung (`depends`) pada addon yang sudah ada dan memperluasnya lewat `_inherit`, tanpa mengubah kode addon lain. Model baru dibuat hanya untuk konsep yang tidak punya padanan.

Hasil survei awal (cabang 17.0, dicek 14 November 2026):

| Addon | Lisensi | Untuk | Keputusan |
|---|---|---|---|
| Odoo CE `mail` | LGPL-3 | Riwayat perubahan, aktivitas, notifikasi | **Dipakai** |
| Odoo CE `hr` (`hr.employee`, `hr.job`, `hr.department`) | LGPL-3 | Personel dan Jabatan | **Dipakai**, di-*extend* di `labfik_core`. Asisten (mahasiswa) dan pihak eksternal bukan pegawai; cara mencatatnya perlu disepakati kelompok **[KONFIRMASI]** |
| OCA `dms` | LGPL-3 | Penyimpanan berkas, folder, hak akses | **Opsional** untuk penyimpanan PDF. Versi berlaku, pengesahan, distribusi, dan tinjau ulang tetap dibuat sendiri **[USULAN PENULIS]** |
| OCA `base_tier_validation` | AGPL-3 | Persetujuan bertingkat | **Tidak dipakai** (AGPL; alur bertingkat tidak sesuai pengesahan satu tahap dengan PDF bertanda tangan). Pembanding di studi terkait |
| OCA `mgmtsystem`, `mgmtsystem_review`, `mgmtsystem_manual`, `document_page_approval` | AGPL-3 | Sistem manajemen ISO, tinjauan manajemen, prosedur | **Tidak dipakai** (AGPL). Pembanding di studi terkait |
| OpenEduCat `openeducat_core` | LGPL-3 | Data mahasiswa dan dosen | **Tidak dipakai** (batasan masalah 7: berdiri sendiri tanpa OpenEduCat) |
| Modul KPI OCA (`kpi`, `kpi_dashboard`, `mgmtsystem_objective`) | — | KPI | Tidak tersedia di 17.0; master KPI dibuat sendiri |

CybroAddons dan OpenHRMS belum diperiksa per modul. Lisensinya campuran (sebagian OPL/berbayar) **[VALIDASI]**.

## Batasan masalah

1. **Indikator yang dicakup:** Pengelolaan 1, 2, 3, dan Pengembangan 13. Baris lain tidak dicakup, termasuk Pengelolaan 10 (KPI dipantau), Pengelolaan 10 (legalitas), Pengelolaan 13 (dokumen mutu), dan Evaluasi E07/E10 (tinjauan). Namun komponen register dokumen, KPI, dan tinjauan bisa dipakai ulang untuk baris-baris itu.
2. **Dua jenis dokumen:**
   - **Dokumen rutin** yang isinya berganti tiap periode, yaitu rencana kerja tahunan (PKG-01) dan rencana pengembangan (PKG-13), **diisi lewat sistem lalu diekspor menjadi PDF** mengikuti format dokumen lab. Penetapan struktur/pengelola per periode (PKG-03) kemungkinan masuk jenis ini **[KONFIRMASI]**.
   - **Dokumen yang jarang berubah**, yaitu SOP dan IK (PKG-02) serta Renstra (berlaku 5 tahun), disusun di luar sistem. Sistem hanya mengelola versi, pengesahan, distribusi, sosialisasi, dan tinjau ulang (file diunggah).
3. **Pengesahan tanpa tanda tangan digital.** Dokumen diekspor atau disiapkan → ditandatangani manual → PDF bertanda tangan diunggah → KaLab menekan "Sahkan" (tercatat pengesah, pencatat, dan waktu). Pejabat penanda tangan (Dekan) tidak memakai sistem. Pemeriksaan isi dokumen menyatu dengan pengesahan, tidak dicatat sebagai tahap terpisah.
4. **Skor kriteria berurutan** (Pengelolaan 1, 3, Pengembangan 13): sistem menampilkan kriteria tertinggi yang "lengkap secara data", lalu skor akhir ditetapkan penilai. Skor Pengelolaan 2 dihitung otomatis.
5. **Tidak dirancang** (saran pengembangan):
   - form Renstra lengkap (visi, misi, sasaran, program, baseline) dan master sasaran Renstra institusi; rujukan Renstra cukup berupa teks di item rencana;
   - IKU sebagai dokumen tersendiri (target KPI per periode cukup di item rencana tahunan);
   - penarikan pengajuan oleh penyusun dan pengaturan modul;
   - pengingat terjadwal (tinjau ulang, realisasi); sistem cukup menampilkan penandanya;
   - koordinasi antarjabatan dan bagan organisasi visual;
   - grafik tren status monev antarperiode;
   - penarikan data gap otomatis dari modul lain.
6. **Tanpa integrasi** dengan sistem kepegawaian, keuangan, SIAKAD, LeADS, atau SIMPEL.
7. **Platform:** Odoo 17 Community, berdiri sendiri tanpa OpenEduCat. Integrasi dengan modul Rafika lewat modul jembatan menjadi saran pengembangan.
8. **Data:** data uji fiktif. Pilot memakai minimal satu dokumen nyata (1 SOP dan 1 draf struktur).
9. **Sistem adalah alat** pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin skor monev naik.

## Rancangan proposal

Mengikuti [Pedoman TA FIK 2025](../docs/Pedoman-TA-FIK-2025-23-29.md), jenis **Prototipe/Proyek**:
- **Bab I:** 1.1 Latar Belakang · 1.2 **Identifikasi Masalah** · 1.3 Batasan Masalah · 1.4 Tujuan dan Manfaat · 1.5 Jadwal Kegiatan
- **Bab II Rancangan Proyek:** 2.1 Observasi · 2.2 Usulan Solusi · 2.3 Rancangan Proyek · 2.4 Rencana Pengujian. Pendekatannya UML, dengan alur rancangan Wazlawick (2024).
- **Lampiran wajib:** dokumen observasi dan wawancara, serta Surat Keterangan Riset dari LabFIK.

| Bagian | Isi dari brief ini |
|---|---|
| 1.2 Identifikasi Masalah | M1–M4 di tabel bawah |
| 1.3 Batasan Masalah | Bagian [Batasan masalah](#batasan-masalah), termasuk butir 5 |
| 2.2 Usulan Solusi | Empat area fitur + mekanisme pengesahan bersama, dengan penanda Inti/Pelengkap |
| 2.3 Rancangan Proyek | Diagram untuk lapis Inti + Pelengkap |
| 2.4 Rencana Pengujian | Skenario *black box* lapis Inti; Pelengkap diuji bila dibangun |
| Saran pengembangan | Batasan masalah butir 5 |

Ketentuan penting:
- **Rubrik:** kesesuaian judul 15, penerapan teknologi 15, masalah jelas 20, studi terkait 20, kesesuaian metode 30.
- **Proposal ditolak** antara lain bila solusi tidak menyelesaikan masalah. Karena itu masalah, tujuan, dan fitur dipetakan satu lawan satu (tabel di bawah).
- **Batas waktu:** pengajuan seminar proposal paling lambat minggu ke-10. Similarity maksimal 25%.

| Masalah (1.2) | Tujuan (1.4) | Fitur |
|---|---|---|
| M1. LabFIK belum punya SK pengelola lab, rencana kerja, maupun rencana pengembangan yang disahkan (Renstra/RKT/IKU masih draf). SOP lab sudah ada sejak 2024, tetapi nomor, tanggal efektif, dan status pengesahannya tidak lengkap. Akibatnya kriteria pertama keempat indikator tidak terpenuhi atau tidak dapat dibuktikan (studi dokumen: [bedah-dokumen-tata-kelola.md](../analisis/bedah-dokumen-tata-kelola.md#2-temuan-as-is-bahan-21-observasi)) **[KONFIRMASI lewat wawancara]** | T1. Sistem yang menuntun lab menyusun dan mengesahkan struktur, SOP, rencana kerja, dan rencana pengembangan | Penetapan struktur, versi dokumen, rencana, pengesahan |
| M2. Kriteria "dijalankan" dan "dievaluasi" hanya bisa dibuktikan dengan rekaman kegiatan, dan rekaman itu belum ada | T2. Rekaman realisasi, rapat koordinasi, tinjauan, dan evaluasi yang tertaut ke dokumen asalnya | Realisasi, rapat, tinjauan, evaluasi |
| M3. Belum ada pengendalian dokumen (versi berlaku, pengesah berwenang, distribusi, tinjau ulang), sehingga SOP tidak bisa dibuktikan mutakhir dan tersedia | T3. Pengendalian dokumen berversi dengan pengesah yang mengikuti jabatan dan riwayat pengesahan | Register dokumen, pengesahan |
| M4. Status indikator dihitung manual dan tidak tertelusur ke buktinya | T4. Status monev: skor Pengelolaan 2 dihitung sistem, kriteria K1–K4 tertaut ke buktinya | Status monev |

Kolom "Fitur" masih tingkat kebutuhan. Rinciannya ditetapkan saat rancangan (Bab II).

**Metode rancangan:** OOAD Wazlawick (2024): kebutuhan → proses bisnis (activity, state machine) → use case → expanded use case → system sequence diagram → conceptual model → design class diagram Odoo dengan inheritance. **Metode pengembangan:** belum diputuskan; kandidat yang pernah diusulkan untuk kelompok adalah Water-Scrum-Fall.

**Evaluasi (usulan):**
- *black box* per kebutuhan;
- kecocokan status yang dihitung sistem dengan hitungan manual pada skenario uji;
- UAT dengan KaLab, laboran, dan asisten;
- SUS (pembanding: Anandar 2026 = 81,88);
- minimal satu dokumen nyata melewati alur sampai disahkan.

## Referensi

Daftar pustaka yang dipakai dan status verifikasinya ada di [draf latar belakang](../pendahuluan/draft/latar-belakang-tata-kelola.md#daftar-pustaka).

Kebijakannya:
- Utamakan jurnal (2022 ke atas), standar, dan regulasi.
- Skripsi dibatasi, saat ini hanya Anandar (2026) sebagai rujukan penerapan Odoo di LabFIK.
- Rancangan: Wazlawick, R. S. (2024). *Object-Oriented Analysis and Design for Information Systems* (2nd ed.). Morgan Kaufmann/Elsevier.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Dinilai "sekadar CRUD" | Bingkai kontribusinya sebagai **keterlacakan butir instrumen → kebutuhan → bukti → status**, tunjukkan lewat matriks keterlacakan; tunjukkan desain inheritance dan riwayat pengesahan |
| Model Personel/Jabatan dan mekanisme pengesahan tidak disepakati kelompok, lalu tiap modul membuat versinya sendiri | Sepakati sebagai kontrak bersama sebelum modul lain mulai |
| Data gap Pengembangan 13 bergantung pada modul lain yang belum jadi | Semua aspek gap diisi manual; penarikan otomatis menjadi saran pengembangan |
| KaLab satu-satunya pencatat pengesahan | Jabatan pengganti dipakai sebagai cadangan; dicatat sebagai keterbatasan |
| Pengesahan oleh Dekan tidak bisa diverifikasi sistem | PDF bertanda tangan wajib diunggah sebelum disahkan; pengesah tercatat dicek terhadap wewenang jabatan |
| Tidak ada dokumen nyata yang disusun selama pilot | Targetkan minimal 1 SOP nyata dan 1 draf struktur, disusun bersama laboran |
| Tumpang tindih dengan baris tanpa PIC (Pengelolaan 10 KPI, Pengelolaan 13 dokumen mutu) | Nyatakan di batasan; komponen boleh dipakai ulang |
| Klaim kondisi saat ini tanpa bukti | Wawancara KaLab terdokumentasi (nama, jabatan, tanggal) sebagai lampiran |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Apakah judul di atas disetujui?
- [ ] Apakah skor akhir indikator kriteria berurutan boleh ditetapkan penilai, sementara sistem hanya menunjukkan "lengkap secara data"?
- [ ] Apakah Renstra (berlaku 5 tahun) boleh dipakai sebagai roadmap Pengelolaan 1 (Bukti 1) sekaligus roadmap Pengembangan 13 (Bukti 3)?

**Untuk KaLab (wawancara, wajib sebagai lampiran)**
- [ ] Konfirmasi tertulis: SK pengelola, SOP disahkan, rencana kerja, dan rencana pengembangan belum ada.
- [ ] Siapa yang menyusun dokumen pertama? Dokumen mana yang ditandatangani Dekan dan mana yang cukup KaLab?
- [ ] SOP apa saja yang wajib menurut KaLab?
- [ ] Apakah ada rapat koordinasi rutin?
- [ ] Apakah anggaran disusun per tahun anggaran atau per tahun akademik?
- [ ] Data kebutuhan kurikulum/CPMK, riset, dan PkM untuk analisis gap didapat dari mana?

**Untuk kelompok (Zahir, Herrens)**
- [ ] Setuju Personel = `hr.employee` dan Jabatan = `hr.job` yang diperluas di `labfik_core` (lihat [Platform dan addon yang diperluas](#platform-dan-addon-yang-diperluas))? Bagaimana asisten (mahasiswa) dan pihak eksternal dicatat?
- [ ] Apakah setiap modul juga mensurvei addon LGPL yang bisa di-*extend* untuk modulnya (mis. `hr` untuk SDM)?
- [ ] Setuju master bersama dan mekanisme pengesahan ditempatkan di `labfik_core` yang terpisah dari `labfik_org`?
- [ ] Field syarat kompetensi minimum di Jabatan: dikelola di Tata Kelola atau di SDM?
- [ ] Apakah gap kompetensi Pengembangan 13 dipakai sebagai masukan Pengembangan 14?

## Langkah berikutnya

1. Susun rancangan TO-BE langkah 4–10 ([CLAUDE.md](../../CLAUDE.md) bagian 4) dalam batas cakupan Inti + Pelengkap.
2. Konfirmasi judul dan aturan skor penilai ke Pak Widi.
3. Wawancara KaLab untuk keempat indikator, didokumentasikan sebagai lampiran.
4. Sepakati kontrak master dan mekanisme pengesahan dengan Zahir dan Herrens.
5. Tulis ulang Bab I mengikuti scope ini.
