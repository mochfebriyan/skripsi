# Brief Modul Tata Kelola & Dokumen

1 November 2026 · Febriyan · Scope skripsi final. Bagian dari proyek LabFIK Compliance (lihat [brief-seluruh-projek.md](brief-seluruh-projek.md))

## Ringkasan

- **Modul:** Tata Kelola & Dokumen, dibangun sebagai addon Odoo `labfik_org`.
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
- **Status:**
  - Pengelolaan 1–3: MVP sudah jalan, 87 unit test lulus, belum UAT.
  - Pengembangan 13: baru dianalisis, belum dibangun.
- **Usulan judul (draf, perlu persetujuan Pak Widi):** Kustomisasi Modul Odoo untuk Tata Kelola dan Pengendalian Dokumen Laboratorium Berbasis Instrumen Monev (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

## Indikator yang dipegang

| Package | Bunyi singkat | PJ | Jenis skor · unit | Level cakupan | Acuan | Status |
|---|---|---|---|---|---|---|
| **PKG-01** Pengelolaan 1 | Rencana kerja tahunan memuat sasaran, KPI, target, anggaran, dan penanggung jawab | KaLab; Dekanat | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | Pedoman Diklatfung PLP 2022, Standar SPMI UPNVJ 2025 | MVP ✅ |
| **PKG-02** Pengelolaan 2 | Seluruh SOP dan IK yang diperlukan tersedia, disahkan, mutakhir, dan dapat diakses pengguna | KaLab; PLP/laboran | Persentase · 1 SOP wajib | Otomatis | ISO/IEC 17025 8.3 | MVP ✅ |
| **PKG-03** Pengelolaan 3 | Struktur organisasi, tugas, tanggung jawab, wewenang, dan pengganti petugas ditetapkan dan dijalankan | Dekan; KaLab | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | ISO/IEC 17025 5 (5.5–5.6) | MVP ✅ |
| **PKG-13** Pengembangan 13 | Rencana pengembangan lab didasarkan pada analisis kesenjangan kebutuhan tridharma, kompetensi, sarana, dan layanan | KaLab; Dekanat | Kriteria K1–K4 · 1 paket dokumen dan rekaman | Semi-otomatis | Pedoman Diklatfung PLP 2022, Standar SPMI UPNVJ 2025 | Analisis saja |

Rincian kriteria, aturan memenuhi, entitas, dan dependensi ada di:
- [analisis-data-pengelolaan-1-3.md](../analisis/analisis-data-pengelolaan-1-3.md)
- [analisis-data-pengembangan-13.md](../analisis/analisis-data-pengembangan-13.md)
- [PRD v0.3](../prd/prd-mvp-pengelolaan-1-3.md), untuk Pengelolaan 1–3

Baris lain dengan nomor yang sama **bukan** scope modul ini. Contohnya Pengelolaan 10 (KPI dipantau), Pengelolaan 10 (legalitas), dan Pengelolaan 13 (dokumen mutu dikendalikan). Baris-baris ini memang menempel ke komponen modul ini, jadi dicatat sebagai **kandidat perluasan** (lihat [Batasan masalah](#batasan-masalah-usulan)).

## Pola bersama di dalam modul

Keempat package hanya memakai **dua pola**. Karena itu modulnya bisa dibangun sebagai komponen yang dipakai ulang, bukan empat fitur terpisah.

| Pola | Dipakai oleh | Alurnya |
|---|---|---|
| **A. Paket dokumen bertangga K1–K4** | PKG-01, PKG-03, PKG-13 | Ditetapkan/disahkan → isinya lengkap → dijalankan (rekaman) → dievaluasi dan diperbaiki |
| **B. Dokumen terkendali berversi** | PKG-02. Juga menyimpan PDF SK (PKG-03) dan rencana bertanda tangan (PKG-01, 13) | Draf → diajukan → berlaku → dicabut, dengan distribusi, sosialisasi, dan tinjau ulang |

PKG-01 dan PKG-13 polanya **sama persis**: rencana (+ item) → realisasi → tinjauan. Usulannya, keduanya memakai satu model rencana generik yang dibedakan **jenis**-nya (strategis/tahunan/pengembangan). Pembedanya PKG-13 dibahas di analisisnya: analisis gap per aspek, prioritas berbasis risiko/manfaat, dan pengukuran manfaat.

Hubungan antar-package:

```
PKG-03 Struktur ──(Personel, Jabatan: PIC, pengesah, peserta)──▶ PKG-01, PKG-02, PKG-13
PKG-02 Register dokumen ──(PDF SK, rencana bertanda tangan)──▶ PKG-03, PKG-01, PKG-13
PKG-01 Roadmap / rencana strategis ◀──(keterkaitan, opsional)── PKG-13
PKG-01 Master KPI ──▶ dipakai juga PKG-21 (kelompok Aset)
```

## Lingkup fitur dan status

| Area | Fitur | Status |
|---|---|---|
| Mulai dari nol | *Checklist* mulai, jabatan standar, kerangka SOP, impor personel CSV | ✅ MVP |
| Struktur (PKG-03) | Personel, jabatan (tugas, kewenangan, atasan, pengganti), SK penetapan berperiode, sinkronisasi jabatan ke hak akses, rapat koordinasi, evaluasi struktur, cetak bagan organisasi dan matriks kewenangan | ✅ MVP |
| Dokumen (PKG-02) | Daftar induk, daftar SOP wajib per periode (bisa dikunci), versi dengan pengesahan dan penolakan, distribusi per ruang, sosialisasi, pengingat tinjau ulang, skor persentase | ✅ MVP |
| Rencana kerja (PKG-01) | Rencana dan item (sasaran, KPI, target, PIC, jadwal, anggaran, Renstra), cetak baku, PDF bertanda tangan, revisi, realisasi per semester, tinjauan | ✅ MVP |
| Status monev | Skor Pengelolaan 2, tangga K1–K4 Pengelolaan 1 dan 3 dengan tautan bukti, skor akhir oleh penilai, *snapshot* periode | ✅ MVP |
| Rencana pengembangan (PKG-13) | Analisis gap per aspek (tridharma, kompetensi, sarana, layanan), item program dengan prioritas risiko/manfaat, biaya, target, PIC, jadwal; realisasi; tinjauan dengan pengukuran manfaat; cetak dokumen; tangga K1–K4 di halaman status | ❌ Belum. Perlu PRD v0.4 |
| Integrasi | Modul jembatan ke master Rafika (`mst_dosen`, `op.student.assistant`); *hook* realisasi KPI otomatis dari modul lain | ❌ Ditunda |

Cara menjalankan MVP dan hasil validasinya ada di [odoo-pengelolaan-mvp/README.md](https://github.com/mochfebriyan/skripsi/tree/febriyan-skripsi/projek-fiklab/odoo-pengelolaan-mvp).

## Kontrak dengan modul lain

**Yang disediakan modul ini:**

| Master / data | Model di MVP | Dipakai oleh | Catatan |
|---|---|---|---|
| Personel | `labfik.personel` | 01, 02, 03, 04, 06, 07, 10, 13, 14, 15, 18, 21 | Jenis: dosen, tendik, mahasiswa (asisten), eksternal. NIP/NIM unik dan hanya terlihat oleh Admin/KaLab. Kandidat jembatan ke master Rafika |
| Jabatan | `labfik.jabatan` | 01, 02, 03, 04, 13, 14, 18 | Belum punya field **syarat kompetensi minimum**, padahal dibutuhkan PKG-04 dan PKG-14. Perlu disepakati dengan Zahir (SDM) |
| Hak akses dari jabatan | Sinkronisasi SK → `res.groups` | Semua modul | Modul lain cukup memakai grup LabFIK (KaLab, Laboran, Pengguna, Penilai) |
| Dokumen Induk + versi | `labfik.dokumen`, `labfik.dokumen.versi` | 02, 03, 09 (SOP limbah); kandidat Persiapan 15 (versi modul) | Pola versi sama dengan "modul berversi" di Persiapan 15 |
| KPI | `labfik.kpi` | 01, 21 | — |
| Periode, Ruang | `labfik.periode`, `labfik.ruang` | Banyak package | Di pemetaan, keduanya milik Core. **Perlu diputuskan** apakah dipindah ke `labfik_core` |

**Yang dipakai modul ini dari modul lain (semuanya opsional, ada jalan pengganti):**

| Data | Dari | Untuk | Bila tidak ada |
|---|---|---|---|
| Penugasan petugas per sesi, presensi petugas | SDM (PKG-04), Praktikum (PKG-18) | Pengelolaan 3 K3 (penugasan mengikuti struktur), rekap beban kerja K4 | K3–K4 dari rapat dan evaluasi saja |
| Skor indikator monev | *Dashboard* / registri indikator (belum ada pemiliknya) | Realisasi KPI otomatis (Pengelolaan 1 K3) dan data gap layanan (Pengembangan 13) | Diinput manual |
| Gap kompetensi personel | SDM (PKG-04 matriks kompetensi, PKG-14) | Aspek kompetensi di analisis gap Pengembangan 13 | Diisi manual |
| Kondisi alat dan pemeliharaan | Aset (PKG-07, PKG-12, PKG-21) | Aspek sarana di analisis gap Pengembangan 13 | Diisi manual |

Sebaliknya, **gap kompetensi** dari Pengembangan 13 bisa menjadi masukan kebutuhan pelatihan di Pengembangan 14 (SDM). Hubungan ini opsional dan perlu disepakati.

## Batasan masalah (usulan)

1. **Indikator yang dicakup:** Pengelolaan 1, 2, 3, dan Pengembangan 13. Baris lain tidak dicakup, termasuk Pengelolaan 10 (KPI dipantau), Pengelolaan 10 (legalitas), Pengelolaan 13 (dokumen mutu), dan Evaluasi E07/E10 (tinjauan). Namun komponen register dokumen, KPI, dan tinjauan bisa dipakai ulang untuk baris-baris itu.
2. **Isi dokumen tidak ditulis di Odoo.** SOP dan rencana disusun di Word/Docs. Sistem mengelola versi, pengesahan, distribusi, dan rekaman pelaksanaannya.
3. **Pengesahan** dibuktikan dengan PDF bertanda tangan yang diunggah dan catatan siapa yang menekan "Sahkan". Tidak ada tanda tangan digital.
4. **Skor kriteria berurutan** (Pengelolaan 1, 3, Pengembangan 13): sistem menampilkan kriteria tertinggi yang "lengkap secara data", lalu skor akhir ditetapkan penilai. Skor Pengelolaan 2 dihitung otomatis.
5. **Tanpa integrasi** dengan sistem kepegawaian, keuangan, SIAKAD, LeADS, atau SIMPEL.
6. **Platform:** Odoo 17 Community, berdiri sendiri tanpa OpenEduCat. Integrasi dengan modul Rafika lewat modul jembatan menjadi saran pengembangan.
7. **Data:** data uji fiktif. Pilot memakai minimal satu dokumen nyata (1 SOP dan 1 draf struktur).
8. **Sistem adalah alat** pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin skor monev naik.

## Rancangan proposal

Mengikuti [Pedoman TA FIK 2025](../docs/Pedoman-TA-FIK-2025-23-29.md), jenis **Prototipe/Proyek**:
- **Bab I:** 1.1 Latar Belakang · 1.2 **Identifikasi Masalah** · 1.3 Batasan Masalah · 1.4 Tujuan dan Manfaat · 1.5 Jadwal Kegiatan
- **Bab II Rancangan Proyek:** 2.1 Observasi · 2.2 Usulan Solusi · 2.3 Rancangan Proyek · 2.4 Rencana Pengujian. Pendekatannya terstruktur (DFD/ERD) atau UML.
- **Lampiran wajib:** dokumen observasi dan wawancara, serta Surat Keterangan Riset dari LabFIK.

Ketentuan penting:
- **Rubrik:** kesesuaian judul 15, penerapan teknologi 15, masalah jelas 20, studi terkait 20, kesesuaian metode 30.
- **Proposal ditolak** antara lain bila solusi tidak menyelesaikan masalah. Karena itu masalah, tujuan, dan fitur dipetakan satu lawan satu (tabel di bawah).
- **Batas waktu:** pengajuan seminar proposal paling lambat minggu ke-10. Similarity maksimal 25%.

| Masalah (1.2) | Tujuan (1.4) | Fitur |
|---|---|---|
| M1. LabFIK belum punya SK pengelola, SOP yang disahkan, rencana kerja, maupun rencana pengembangan, sehingga kriteria pertama keempat indikator tidak terpenuhi | T1. Alur yang menuntun lab menyusun dan mengesahkan struktur, SOP, rencana kerja, dan rencana pengembangan dari nol | *Checklist* mulai, SK, versi dokumen, rencana |
| M2. Kriteria "dijalankan" dan "dievaluasi" hanya bisa dibuktikan dengan rekaman kegiatan, dan rekaman itu belum ada | T2. Rekaman realisasi, rapat koordinasi, tinjauan, dan evaluasi yang tertaut ke dokumen asalnya | Realisasi, rapat, tinjauan, evaluasi struktur |
| M3. Belum ada pengendalian dokumen (versi berlaku, pengesah berwenang, distribusi, tinjau ulang), sehingga SOP tidak bisa dibuktikan mutakhir dan tersedia | T3. Register dokumen berversi dengan hak sahkan yang mengikuti jabatan | Register dokumen, sinkronisasi jabatan → akses |
| M4. Status indikator dihitung manual dan tidak tertelusur ke buktinya | T4. Halaman status monev: skor Pengelolaan 2 otomatis, tangga K1–K4 dengan tautan bukti, *snapshot* periode | Status kepatuhan |

**Metode:** belum diputuskan. Kandidat yang pernah diusulkan untuk kelompok adalah Water-Scrum-Fall. Tahapan pengembangan di PRD bersifat bertahap per kelompok fitur.

**Evaluasi:** mengikuti tujuan O1–O6 di PRD:
- unit test dan *black box* per kebutuhan fungsional;
- kecocokan status dengan *test oracle* dataset skenario;
- UAT dengan KaLab, laboran, dan asisten;
- SUS ≥ 70 (pembanding: Anandar 2026 = 81,88);
- minimal satu dokumen nyata melewati alur sampai *berlaku*.

## Referensi yang sudah diverifikasi dan relevan

| Referensi | Dipakai untuk | DOI / tautan |
|---|---|---|
| Ismail *et al.* (2026), JIP 12(3) 519–528 | E-SPMI: dokumen dan validasi audit mutu internal | 10.33795/jip.v12i3.9580 |
| Nurramadhona *et al.* (2025), JIP 12(1) 9–18 | Analisis ketercapaian otomatis + *dashboard* dari penilaian auditor | 10.33795/jip.v12i1.8432 |
| Tiara (2026), skripsi UPNVJ | Monitoring IKU: realisasi direkam dan ditautkan ke bukti (relevan untuk KPI Pengelolaan 1) | repository.upnvj.ac.id/51983 |
| Anandar (2026), skripsi UPNVJ | Pendahulu: modul Odoo OpenEduCat di LabFIK, SUS 81,88 | repository.upnvj.ac.id/51635 |
| Nurrohmah & Wiratama (2022), Ultima InfoSys 13(2) 77–84 | Odoo *open source* dan bisa dikustomisasi | 10.31937/si.v13i2.2802 |
| Odoo S.A. (2023), *Security in Odoo 17.0* | Grup akses dan *record rule* | odoo.com/documentation/17.0 |
| BSN (2018), SNI ISO/IEC 17025:2017 | 5 (struktur), 7.5 (rekaman), 8.3 (pengendalian dokumen) | [docs/](../docs/SNI%20ISO-IEC%2017025-2017_ID.md) |
| UPNVJ (2026), Instrumen Monev Laboratorium v1.1 | Rubrik keempat indikator | Dokumen internal |

**Masih perlu dicari:** rujukan ≥2022 tentang tata kelola atau pengendalian dokumen laboratorium perguruan tinggi, dan rujukan metode pengembangan.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Dinilai "sekadar CRUD" | Bingkai kontribusinya sebagai **keterlacakan butir instrumen → kebutuhan → bukti → status**. Matriks keterlacakan di PRD Lampiran A menjadi buktinya |
| Model Personel/Jabatan tidak disepakati kelompok, lalu tiap modul membuat versinya sendiri | `labfik.personel` dan `labfik.jabatan` ditawarkan sebagai kontrak; sepakati sebelum modul lain mulai |
| Data gap Pengembangan 13 bergantung pada modul lain yang belum jadi | Semua aspek gap bisa diisi manual dulu; tautan otomatis menyusul |
| KaLab satu-satunya pengesah | Jabatan pengganti dipakai sebagai cadangan (ditunda); dicatat sebagai keterbatasan |
| Tidak ada dokumen nyata yang disusun selama pilot | Target O6: susun 1 SOP nyata dan 1 draf struktur bersama laboran |
| Tumpang tindih dengan baris tanpa PIC (Pengelolaan 10 KPI, Pengelolaan 13 dokumen mutu) | Nyatakan di batasan; komponen boleh dipakai ulang |
| Klaim kondisi saat ini tanpa bukti | Wawancara KaLab terdokumentasi (nama, jabatan, tanggal) sebagai lampiran |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Apakah judul di atas disetujui?
- [ ] Apakah skor akhir indikator kriteria berurutan boleh ditetapkan penilai, sementara sistem hanya menunjukkan "lengkap secara data" (PRD D8)?
- [ ] Apakah roadmap Pengelolaan 1 (Bukti 1) dan roadmap Pengembangan 13 (Bukti 3) boleh satu dokumen?

**Untuk KaLab (wawancara, wajib sebagai lampiran)**
- [ ] Konfirmasi tertulis: SK pengelola, SOP disahkan, rencana kerja, dan rencana pengembangan belum ada.
- [ ] Siapa yang akan menyusun dan mengesahkan dokumen pertama? Apakah Dekan mengesahkan SK dan rencana?
- [ ] SOP apa saja yang wajib menurut KaLab?
- [ ] Apakah ada rapat koordinasi rutin?
- [ ] Apakah anggaran disusun per tahun anggaran atau per tahun akademik?
- [ ] Apakah pernah ada analisis kebutuhan, renstra, atau roadmap lab? Data kebutuhan kurikulum/CPMK, riset, dan PkM didapat dari mana?

**Untuk kelompok (Zahir, Herrens)**
- [ ] Apakah model `labfik.personel` dan `labfik.jabatan` disepakati sebagai master bersama?
- [ ] Apakah master bersama dipisah ke `labfik_core`?
- [ ] Field syarat kompetensi minimum di Jabatan: dikelola di Tata Kelola atau di SDM?
- [ ] Apakah gap kompetensi Pengembangan 13 dipakai sebagai masukan Pengembangan 14?

## Langkah berikutnya

1. Konfirmasi judul dan keputusan D8 ke Pak Widi.
2. Wawancara KaLab untuk keempat indikator, didokumentasikan sebagai lampiran.
3. Sepakati kontrak master (Personel, Jabatan, Periode, Ruang, Core) dengan Zahir dan Herrens.
4. PRD v0.4: tambahkan kebutuhan Pengembangan 13 (dari [analisisnya](../analisis/analisis-data-pengembangan-13.md)), lalu bangun di `labfik_org` di atas model rencana generik.
5. Tulis ulang Bab I mengikuti scope ini.
