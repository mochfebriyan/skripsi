# Brief Modul SDM & Kompetensi

14 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Pemegang modul ditetapkan 1 November 2026. Cakupan rancangan ditetapkan 14 November 2026. Bahan Bab I (1.2, 1.3, 1.4) dan dasar seluruh rancangan TO-BE.

## Ringkasan

- **Modul:** SDM & Kompetensi (rencana addon Odoo: `labfik_sdm`, `depends: ['labfik_core']`).
- **Indikator:** 3 dari 21 indikator proyek.
  - PKG-04 Pengelolaan 4 (penugasan petugas sesuai kompetensi)
  - PKG-10 Pengelolaan 10 (otorisasi personel)
  - PKG-14 Pengembangan 14 (pelatihan PLP/laboran)
- **Master yang dikelola modul ini:** **Kompetensi** (dipakai ketiga package) dan **Tugas/Alat Berkewenangan Khusus** (PKG-10). Personel dan Jabatan dipakai dari Core; syarat kompetensi ditambahkan ke Jabatan oleh modul ini.
- **Benang merah:** satu data kompetensi dipakai tiga kali. **Syarat** kompetensi ada di jabatan, **bukti** kompetensi dimiliki personel, dan dari selisih keduanya lahir tiga hal: petugas sesi yang sah (PKG-04), izin tugas/alat (PKG-10), dan kebutuhan pelatihan (PKG-14). Pelatihan yang efektif menambah bukti kompetensi, sehingga siklusnya tertutup.
- **Status:** ketiga package sudah dianalisis (draf). Rancangan TO-BE disusun berikutnya mengikuti [CLAUDE.md](../../CLAUDE.md) bagian 4, dalam batas [cakupan rancangan](#cakupan-rancangan).
- **Usulan judul (dari draf pendahuluan, perlu persetujuan Pak Widi):** Kustomisasi Modul Odoo untuk Pengelolaan Kompetensi Personel Laboratorium Berbasis Instrumen Monev (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

## Indikator yang dipegang

| Package | Bunyi singkat | PJ | Jenis skor · unit | Level cakupan | Acuan |
|---|---|---|---|---|---|
| **PKG-04** Pengelolaan 4 | Seluruh sesi praktikum memiliki laboran/PLP dan asisten bila diperlukan yang ditugaskan sesuai kompetensi minimum | KaLab; Koor Prodi | Persentase · 1 sesi terlaksana | Otomatis | ISO/IEC 17025 6.2; Pedoman Diklatfung PLP 2022 |
| **PKG-10** Pengelolaan 10 | Personel yang menjalankan tugas/alat berkewenangan khusus memiliki otorisasi sesuai kompetensi | KaLab; PLP/laboran | Persentase · 1 pasangan personel × tugas/alat | Otomatis | ISO/IEC 17025 6.2.5–6.2.6 |
| **PKG-14** Pengembangan 14 | Kompetensi PLP/laboran dikembangkan melalui pelatihan yang relevan dan dievaluasi penerapannya | KaLab; Dekanat SDM | Kriteria K1–K4 · 1 paket per tahun | Semi-otomatis | ISO/IEC 17025 6.2.5; Pedoman Diklatfung PLP 2022 |

Rincian kriteria, aturan memenuhi, entitas, dan dependensi:
- [analisis-data-pengelolaan-4.md](../analisis/analisis-data-pengelolaan-4.md)
- [analisis-data-pengelolaan-10.md](../analisis/analisis-data-pengelolaan-10.md)
- [analisis-data-pengembangan-14.md](../analisis/analisis-data-pengembangan-14.md)

Dua baris "Pengelolaan 10" lainnya di sheet (capaian KPI, legalitas lab) **bukan** scope modul ini.

## Kondisi saat ini (as-is) dan sumbernya

| No | Temuan | Sumber | Status |
|---|---|---|---|
| A1 | Rencana pertemuan praktikum disusun di *spreadsheet* alokasi asisten (nama asisten per kelas per pertemuan) | Spreadsheet "Alokasi Pertemuan Asisten Praktikum" (akun LabFIK) | Data nyata; strukturnya dibedah di Langkah 2 **[VALIDASI]** |
| A2 | Pelaksanaan sesi dilaporkan asisten lewat Google Form dan direkap manual untuk honor; hanya mencakup asisten, laboran/PLP tidak tercatat | "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ (Responses)" | Data nyata **[VALIDASI]** |
| A3 | Pada 2025/2026 Ganjil dan Genap, 42–56% kelas praktikum tidak punya alokasi asisten, dan tidak bisa dibedakan antara tidak butuh atau belum terpenuhi | Analisis penulis atas A1 | Perlu dihitung ulang dan dicatat caranya di Langkah 2 **[VALIDASI]** |
| A4 | POB Manajemen Praktikum dan Asistensi 2025 mengatur alokasi → rekrutmen → seleksi (administrasi, wawancara, teknis) → kontrak → alokasi jadwal asisten. Dokumennya belum bernomor dan belum disahkan | `LABFIK_POB_Praktikum.pdf` (Drive proyek) | Dokumen nyata |
| A5 | Syarat nilai A untuk asisten dapat dilonggarkan secara informal bila pendaftar sedikit | Draf pendahuluan penulis | **[KONFIRMASI KaLab/Koor Prodi]** |
| A6 | Belum diketahui: alat/tugas yang dibatasi dan cara izinnya; cara penetapan dan pembuktian pelatihan PLP | Tidak ada dokumen nyata di Drive; wawancara belum dijawab | **[KONFIRMASI]** |

Paket Manajemen Praktikum 2026 dan Paket Dokumen Monev di Drive adalah **draf** (diduga hasil GPT) dan hanya dipakai sebagai contoh format.

## Arahan pembimbing dan keputusan

| Tanggal | Sumber | Isi | Dampak |
|---|---|---|---|
| 13 Nov 2026 | Bimbingan Pak Widi (kelompok) | Dahulukan rancangan TO-BE dengan UML; class Odoo memakai inheritance; observasi as-is boleh dari studi dokumen dan ISO selama wawancara belum ada | Urutan kerja dan gaya rancangan |
| 14 Nov 2026 | Keputusan kelompok (brief Tata Kelola) | Dekan dan penilai monev **bukan aktor sistem**; master bersama dan mixin di `labfik_core` | Dekanat SDM hanya penanda tangan; bukti untuk penilai berupa PDF |
| 14 Nov 2026 | Zahir | Pemegang modul: PKG-04, 10, 14 (final) | — |
| 14 Nov 2026 | Zahir | **Kompetensi = master sendiri.** Syarat kompetensi ditambahkan ke `hr.job` oleh `labfik_sdm` (Core tidak diubah). Bukti kompetensi = transaksi milik personel | Kontrak Core tetap |
| 14 Nov 2026 | Zahir | Penugasan asisten **per kelas** (asisten memilih MK saat mendaftar, lalu memilih kelas); seleksi per MK; pengganti per sesi = Pelengkap | Grain PKG-04 |
| 14 Nov 2026 | Zahir | Seleksi Kompetensi (PKG-04) **dipisah** dari Asesmen Keterampilan (PKG-10) | Dua transaksi |
| 14 Nov 2026 | Zahir | Orientasi/supervisi (bukti 7 PKG-04) dan pembatasan akses (bukti 4 PKG-10) = rekaman pendukung, bukan syarat persentase | **[KONFIRMASI pembimbing]** |
| 14 Nov 2026 | Zahir | PKG-14: peserta PLP/laboran dan teknisi; rencana per tahun; item pelatihan boleh *batal* dengan alasan dan tidak dihitung di K3 | — |
| 14 Nov 2026 | Zahir | PKG-10: hanya PLP/laboran (asisten, dosen, praktikan tidak dicakup); sistem tidak memblokir pemakaian alat | **[KONFIRMASI pembimbing]** |

## Pola bersama di dalam modul

| Pola | Dipakai oleh | Alurnya | Mekanisme Core |
|---|---|---|---|
| **A. Syarat vs bukti kompetensi** | PKG-04, 10, 14 | Jabatan/tugas mensyaratkan kompetensi → personel punya bukti → sistem membandingkan | — (milik modul ini) |
| **B. Keputusan yang disahkan** | Penugasan Petugas, Otorisasi, Rencana Pelatihan | Draf → diajukan → disahkan → diganti/dicabut/kedaluwarsa, dengan riwayat | `labfik.approval.mixin` (+ `labfik.period.mixin` untuk Otorisasi) |
| **C. Rekaman bukti** | Bukti Kompetensi, Realisasi Pelatihan | Tanggal, pelapor, berkas, keterangan | `labfik.evidence.mixin` |
| **D. Status monev** | PKG-04, 10 (persentase); PKG-14 (K1–K4) | Unit dihitung dari data; untuk K1–K4 ditampilkan kriteria tertinggi yang lengkap secara data | `labfik.criteria.mixin` (PKG-14) |

## Lingkup kebutuhan

| Area | Yang harus bisa dibuktikan sistem |
|---|---|
| Kompetensi (bersama) | Master kompetensi; syarat kompetensi per jabatan; bukti kompetensi per personel (jenis, berkas, masa berlaku); matriks kompetensi sebagai laporan |
| Penugasan (PKG-04) | Kebutuhan petugas per kelas; seleksi asisten per MK termasuk pengecualian dan penyetujunya; penugasan per kelas yang disahkan dengan surat tugas; daftar sesi dan petugas; persentase sesi memenuhi |
| Otorisasi (PKG-10) | Daftar tugas/alat berkewenangan khusus; asesmen keterampilan; otorisasi berlevel dan bermasa berlaku; evaluasi ulang saat ada pemicu; daftar operator sah; persentase pasangan memenuhi |
| Pelatihan (PKG-14) | Kebutuhan kompetensi PLP dari matriks; rencana pelatihan disahkan; realisasi dengan sertifikat dan bukti penerapan; evaluasi efektivitas yang menambah bukti kompetensi; status K1–K4 |
| Status monev | Persentase PKG-04 dan PKG-10; kriteria tertinggi PKG-14; daftar unit yang belum memenuhi beserta syarat yang gagal; laporan bukti sebagai PDF |

## Cakupan rancangan

Mengikuti prinsip *sweet spot* di [CLAUDE.md](../../CLAUDE.md) bagian 1. Lapis **Inti** (W) dan **Pelengkap** (O) dirancang dan digambar; selain itu tidak.

| Area | Inti | Pelengkap |
|---|---|---|
| **Kompetensi** | Master Kompetensi; syarat kompetensi di `hr.job`; Bukti Kompetensi (mewarisi `evidence.mixin`) dengan status berlaku dihitung dari tanggal; Matriks Kompetensi (daftar personel × kompetensi, penanda kurang) | — |
| **PKG-04 Penugasan** | Kebutuhan Petugas per kelas (jumlah minimal per peran; 0 = tidak butuh); Seleksi Kompetensi per MK (nilai, skor uji, keputusan, pengecualian + penyetuju); Penugasan Petugas per kelas (disahkan, berkas surat tugas); Daftar Sesi dan Petugas dengan status S1–S4; persentase | Pengganti per sesi; Komitmen petugas (berkas di penugasan); rekaman Orientasi/Supervisi (bukti 7); ekspor surat tugas PDF |
| **PKG-10 Otorisasi** | Master Tugas/Alat (kompetensi disyaratkan, masa berlaku standar); Asesmen Keterampilan (layak → Bukti Kompetensi); Otorisasi (level terbimbing/mandiri, supervisor, lingkup, masa berlaku; `approval.mixin` + `period.mixin`); Evaluasi Ulang (pemicu, keputusan, versi baru mengganti versi lama); Daftar Operator Sah; persentase | Cara pembatasan akses + berkas di master (bukti 4); kedaluwarsa otomatis lewat penjadwal `period.mixin` |
| **PKG-14 Pelatihan** | Rencana Pelatihan tahunan (kebutuhan dibekukan saat diajukan, item lengkap; `approval.mixin` + `criteria.mixin`); Realisasi per peserta (sertifikat, bukti penerapan); Evaluasi Efektivitas (skor sebelum/sesudah, kesimpulan, tindak lanjut; efektif → Bukti Kompetensi); status K1–K4 | Item *batal* dengan alasan; rekap pelatihan per personel; ekspor PDF rencana |
| **Status monev** | Persentase PKG-04/10 dan kriteria tertinggi PKG-14, masing-masing dengan daftar unit yang belum memenuhi dan tautan ke rekaman; laporan bukti diterbitkan sebagai PDF | — |

**Aktor sistem (usulan):** **KaLab** (menetapkan kebutuhan, mencatat pengesahan, menyetujui pengecualian, memantau status), **Laboran/PLP** (mencatat seleksi, bukti kompetensi, asesmen, realisasi), dan **Penjadwal** (kedaluwarsa otorisasi, Pelengkap). Dekan, Dekanat SDM, dan Koor Prodi yang hanya menandatangani dokumen cetak **bukan aktor sistem**; identitasnya tercatat sebagai pengesah. Penilai monev menerima bukti berupa PDF. Apakah asisten dan dosen perlu masuk sistem (mis. melihat surat tugas sendiri) **tidak dirancang** di proposal **[KONFIRMASI pembimbing]**.

## Kontrak dengan modul lain

**Yang disediakan modul ini:**

| Data | Dipakai oleh | Catatan |
|---|---|---|
| Kompetensi, syarat kompetensi jabatan, Bukti Kompetensi, Matriks Kompetensi | Opsional PKG-13 (gap aspek kompetensi) | Bila diotomatiskan, `labfik_org` yang bergantung ke `labfik_sdm` |
| Penugasan Petugas per kelas/sesi | Opsional PKG-18 (cocokkan presensi petugas), PKG-08 (jumlah petugas per sesi) | Alasan `labfik_praktikum` bergantung ke `labfik_sdm` (pemetaan bersama) |
| Daftar Operator Sah / cek berwenang | Peluang untuk modul Praktikum dan Aset | Tidak dirancang sekarang |

**Yang dipakai modul ini:**

| Data | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Personel (`hr.employee`), Jabatan (`hr.job`), Periode, mixin approval/period/criteria/evidence | Core (`labfik_core`) | Wajib | — |
| Mata Kuliah, Kelas, Sesi bertanggal | Core, dibangkitkan PKG-15 (Herrens) | Wajib | Data contoh dari skrip uji |
| Status sesi terlaksana (penyebut PKG-04) | PKG-18 (Herrens) | Wajib untuk penyebut | Sesi terjadwal yang tanggalnya sudah lewat dianggap terlaksana **[ASUMSI]** |
| Alat | Asset Management (kelompok lain) | Opsional | Nama alat sebagai teks di master Tugas/Alat |

## Platform dan addon yang diperluas

| Addon | Lisensi | Untuk | Keputusan |
|---|---|---|---|
| `labfik_core` (proyek) | — | Personel, Jabatan, Periode, mixin | **Dipakai**; `hr.job` dan `hr.employee` diperluas lagi oleh `labfik_sdm` lewat `_inherit` |
| Odoo CE `mail` | LGPL-3 | Riwayat perubahan | **Dipakai** (lewat Core) |
| Odoo CE `hr_skills` | LGPL-3 | Skill dan level per pegawai | **Tidak dipakai** **[VALIDASI]**: tidak menyimpan berkas bukti dan masa berlaku yang dibutuhkan monev |
| `skripsi_rafika/PendaftaranAsisten` (OpenEduCat) | — | Pendaftaran dan alokasi asisten | **Acuan saja**, tidak di-*extend* (CLAUDE.md bagian 3) |

## Batasan masalah

1. **Indikator yang dicakup:** Pengelolaan 4, Pengelolaan 10 (otorisasi), dan Pengembangan 14. Pencatatan pelaksanaan sesi (Proses 18) serta penjadwalan dan kesiapan sesi (Persiapan 15–17) dibahas di penelitian terpisah.
2. **Personel yang dicakup per indikator:** PKG-04 laboran/PLP dan asisten pada sesi praktikum terjadwal; PKG-10 hanya PLP/laboran; PKG-14 PLP/laboran dan teknisi.
3. **Data personel, jabatan, mata kuliah, kelas, dan sesi** diambil dari Core dan modul Praktikum. Bila belum tersedia saat pengujian, dipakai data contoh dengan struktur yang disepakati.
4. **Pengesahan tanpa tanda tangan digital:** dokumen (surat tugas, otorisasi, rencana pelatihan) ditandatangani manual, berkasnya diunggah, lalu KaLab mencatat pengesahan. Penanda tangan (Dekan, Dekanat SDM, Koor Prodi) tidak memakai sistem.
5. **Skor:** persentase PKG-04 dan PKG-10 dihitung sistem; untuk PKG-14 sistem menunjukkan kriteria tertinggi yang lengkap secara data, dan skor akhir ditetapkan penilai.
6. **Syarat kompetensi, ketentuan pengecualian, daftar tugas/alat berkewenangan khusus, dan masa berlaku otorisasi ditetapkan KaLab**, bukan oleh sistem.
7. **Tidak dirancang** (saran pengembangan):
   - pendaftaran calon asisten (Anandar 2026) dan perhitungan honor;
   - alokasi asisten otomatis (*minimum coverage*, cek bentrok) dan bobot rubrik seleksi rinci;
   - kebutuhan petugas per sesi berbasis perhitungan risiko;
   - otorisasi untuk asisten, dosen, dan mahasiswa praktikan; pemblokiran pemakaian alat oleh sistem; log supervisi harian;
   - penganggaran pelatihan rinci, angka kredit jabatan fungsional PLP, kuesioner reaksi peserta;
   - pengingat terjadwal (bukti kedaluwarsa, evaluasi pascapelatihan); penanda cukup dihitung saat dibaca;
   - *dashboard* grafik dan tren antarperiode (cukup daftar status dengan tautan bukti).
8. **Tanpa integrasi** dengan sistem kepegawaian universitas, SIAKAD, atau Google Form/Sheets yang dipakai sekarang.
9. **Data pribadi** (NIM, nilai/KHS, NIK, rekening) hanya disimpan sejauh diperlukan sebagai bukti, dengan akses terbatas. Data pengujian fiktif atau dianonimkan.
10. **Sistem adalah alat** pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin skor monev naik dan tidak menggantikan verifikasi penilai.

## Masalah → tujuan → fitur

| Masalah (draf pendahuluan 1.2) | Tujuan (1.4) | Fitur (lapis Inti) |
|---|---|---|
| M1 Syarat kompetensi asisten bisa dilonggarkan tanpa persetujuan tercatat; pencatatan petugas hanya asisten untuk honor; kesesuaian kompetensi petugas per sesi (PKG-04) tidak bisa dibuktikan | T1 Pengelolaan kompetensi dan penugasan petugas per sesi yang memeriksa kesesuaian kompetensi dan mencatat pengecualian | Master + syarat + bukti kompetensi; Kebutuhan Petugas; Seleksi dengan pengecualian; Penugasan per kelas; Daftar Sesi dan Petugas |
| M2 Belum ada rekaman tugas/alat berkewenangan khusus, asesmen, otorisasi, dan evaluasi ulangnya (PKG-10) **[KONFIRMASI]** | T2 Asesmen, otorisasi, dan evaluasi ulang otorisasi PLP/laboran | Master Tugas/Alat; Asesmen; Otorisasi; Evaluasi Ulang; Daftar Operator Sah |
| M3 Kebutuhan, pelaksanaan, dan efektivitas pelatihan PLP belum terhubung dengan kompetensi (PKG-14) **[KONFIRMASI]** | T3 Rencana, realisasi, dan evaluasi efektivitas pelatihan yang memperbarui matriks kompetensi | Rencana Pelatihan; Realisasi; Evaluasi Efektivitas → Bukti Kompetensi |
| M4 Skor dihitung manual menjelang monev dan tidak tertelusur ke bukti | T4 Status ketiga indikator yang tertelusur ke bukti, diuji dengan *black box* dan UAT | Status monev (persentase, K1–K4, daftar unit belum memenuhi, PDF bukti) |

**Yang perlu diubah di draf pendahuluan:** (a) Personel dan Jabatan berasal dari `labfik_core`, bukan modul Tata Kelola; (b) cakupan personel PKG-10 hanya PLP/laboran; (c) "*dashboard*" dipersempit menjadi daftar status dengan tautan bukti; (d) batasan masalah butir 1 menyebut praktikan sebagai kandidat, sekarang dinyatakan tidak dicakup.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Model Sesi/Kelas belum jelas (pemetaan: Sesi mewarisi `op.session`; brief Tata Kelola: tanpa OpenEduCat) | Sepakati dengan Herrens dan Febriyan sebelum Langkah 9; sementara modelkan Sesi sebagai konsep Core tanpa mengikat ke OpenEduCat |
| Wawancara KaLab/laboran belum dijawab | Rancangan memakai instrumen dan ISO sebagai dasar; klaim as-is ditandai; pertanyaan sudah disiapkan di lembar wawancara |
| Dinilai "sekadar CRUD" | Tunjukkan siklus syarat → bukti → penugasan/otorisasi/pelatihan → bukti baru, pewarisan mixin Core, dan keterlacakan kriteria → bukti |
| Data pribadi asisten (NIM, nilai) masuk sistem atau repo | Hanya nilai yang dipersyaratkan; lampiran KHS berakses terbatas; data uji fiktif; cek `grep` sebelum commit |
| Asisten (mahasiswa) dicatat sebagai `hr.employee` belum disepakati | Ikuti keputusan kelompok **[KONFIRMASI]**; rancangan SDM hanya merujuk "Personel" |
| Penyebut PKG-10 tidak menangkap orang yang belum berizin | Dibahas di Langkah 4 (usulan: pasangan aktif dari jabatan pelaksana) |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Judul di atas disetujui?
- [ ] Bukti orientasi/supervisi (PKG-04) dan pembatasan akses (PKG-10) cukup sebagai rekaman pendukung, bukan syarat persentase?
- [ ] Otorisasi PKG-10 dibatasi ke PLP/laboran saja, padahal instrumen menyebut "personel/pengguna"?
- [ ] Item pelatihan yang batal boleh dikecualikan dari K3 PKG-14?

**Untuk KaLab dan laboran (lembar wawancara SDM & Kompetensi no. 1–19, wajib sebagai lampiran)**
- [ ] Siapa yang menetapkan dan menandatangani penugasan petugas, izin alat/tugas khusus, dan rencana pelatihan?
- [ ] Syarat kompetensi minimal per peran; nilai minimal MK asisten; cara pengecualian dicatat
- [ ] Setelah asisten memilih kelas, siapa yang mengesahkan?
- [ ] Alat/tugas apa yang dibatasi, dan berapa lama izinnya berlaku?
- [ ] Apakah teknisi termasuk laboran? Berapa PLP/laboran aktif?
- [ ] Rencana pelatihan per tahun anggaran atau tahun kalender?

**Untuk kelompok (Febriyan, Herrens)**
- [ ] Febriyan: syarat kompetensi ditambahkan ke `hr.job` oleh `labfik_sdm`, bukan oleh Core. CLAUDE.md bagian 6 perlu disesuaikan
- [ ] Herrens: model Sesi, Kelas, Mata Kuliah di Core, dengan atau tanpa OpenEduCat? Status "terlaksana" dari PKG-18 dipakai sebagai penyebut PKG-04
- [ ] Bersama: cara mencatat asisten (mahasiswa) sebagai Personel

## Langkah berikutnya

1. Langkah 2: bedah dokumen (`analisis/bedah-dokumen-sdm.md`): POB 2025, struktur kolom spreadsheet alokasi dan Google Form (tanpa data pribadi), draf paket 2026 sebagai pembanding.
2. Langkah 3: sepakati kontrak Core dan Sesi dengan Febriyan dan Herrens.
3. Langkah 4–10 dalam batas cakupan Inti + Pelengkap di atas.
4. Wawancara KaLab dan laboran, didokumentasikan sebagai lampiran.
5. Revisi draf pendahuluan sesuai bagian "Yang perlu diubah".
