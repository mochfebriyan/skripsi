# Bedah Dokumen Pelaksanaan Praktikum (Studi Dokumen)

14 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20 · Modul: Pelaksanaan Praktikum

**Status: DRAF.** Bahan kerja Langkah 2 (temuan *as-is* masuk Bab II 2.1 Observasi). Semua usulan model dan field masih **[USULAN PENULIS]** sampai ditetapkan di rancangan (Langkah 10), dalam batas cakupan di [brief modul](../brief/brief-praktikum.md#cakupan-rancangan-usulan-awal).

## Tujuan

Dokumen ini membedah dokumen dan data nyata yang dipakai LabFIK untuk mengelola praktikum, lalu menerjemahkan setiap bagian menjadi **field dan model** untuk rancangan TO-BE. Input-nya adalah [brief modul](../brief/brief-praktikum.md) dan analisis keenam PKG (Langkah 0).

| Bagian proposal | Yang dipakai |
|---|---|
| 2.1 Observasi (studi dokumen) | [Bagian 3: Temuan *as-is*](#3-temuan-as-is-bahan-21-observasi) |
| 2.2 Usulan Solusi | [Bagian 2: Pelaku dan peluang otomasi](#2-pelaku-dan-peluang-otomasi) |
| Langkah 5 (activity) | Bagian 4.1, tabel langkah POB 2025 |
| Langkah 9–10 (model) | [Bagian 5: Pola berulang](#5-pola-berulang--kandidat-mixin) dan [bagian 6: Daftar model](#6-daftar-model-to-be-konsolidasi) |
| Lampiran | Seluruh dokumen ini sebagai hasil studi dokumen |

## Aturan baca

- **Urutan sumber kebenaran:** Instrumen Monev dan ISO 17025 → brief → analisis → dokumen ini. Bila format dokumen lab bertentangan dengan kriteria instrumen, instrumen yang diikuti.
- **Draf hanya acuan format.** Paket praktikum 2026 dan Paket Dokumen Monev di Drive LabFIK adalah draf (kemungkinan hasil GPT). Field dari draf dipakai **hanya bila** juga didukung instrumen atau analisis. Kolom **Dasar** menunjukkan dukungannya: `Instr` = kriteria/bukti instrumen, `ISO` = ISO/IEC 17025, `Analisis` = keputusan di analisis PKG, `Format` = hanya untuk tampilan atau ekspor.
- **Data nyata memuat data pribadi** (nama, NIM, nomor HP, email asisten; nama dosen). Tidak ada yang disalin ke sini; yang dicatat hanya nama kolom, struktur, dan angka agregat.
- **Aturan Wazlawick yang dipakai** (Langkah 2 tidak punya bab wajib di CLAUDE.md; yang dipakai adalah bab pemodelan bisnis):
  - **§3.1 Pengantar pemodelan bisnis:** tujuan studi ini adalah memahami struktur dan dinamika organisasi, masalah saat ini, dan perbaikan yang mungkin, lalu menurunkan kebutuhan. Juga: jangan merekam ulang data yang sudah ada di sistem lain (dasar keputusan tautan ke LeADS/SIMPEL).
  - **§2.6.1 *Business actor* dan *business worker*:** setiap pelaku di dokumen digolongkan sebagai *actor* (di luar kendali lab) atau *worker* (bagian dari lab). Hanya peran *worker* yang bisa digantikan sistem.
  - **§2.6.2 Peluang otomasi:** peran *worker* yang sekadar perantara (menyalin, merekap, mengetik ulang) adalah kandidat utama otomasi; batas sistem menunjukkan apa yang diotomasi dan apa yang tetap di luar.
- Label `[T]`/`[M]`/`[R]` dan nama master mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md#4-konvensi-penamaan). Nama model memakai pola `labfik.praktikum.<objek>` (CLAUDE.md bagian 6); model Core memakai nama di kontrak Core.

---

## 1. Dokumen yang dibedah

| ID | Dokumen | Sifat | Tanggal / periode | PKG | Perlakuan di TO-BE |
|---|---|---|---|---|---|
| **D1** | POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`), 17 langkah + 10 lampiran (L1–L10) | **Nyata**, belum disahkan (nomor dan tanggal pengesahan kosong) | 2025 | 15–20 (sebagian lampiran milik SDM) | Sumber alur (Langkah 5) dan field. POB-nya sendiri adalah dokumen terkendali milik PKG-02 Tata Kelola |
| **D2** | Sheet "Alokasi Pertemuan Asisten Praktikum" (tab per periode, LOV asisten, rekap) | **Data nyata** (data pribadi) | 2025/2026 Ganjil s.d. 2026/2027 Ganjil | 15, 18 (alokasi asisten milik PKG-04) | Sumber impor Mata Kuliah dan Kelas; digantikan Sesi |
| **D3** | Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" + sheet respons (tab Form Responses 1, Per Pertemuan, Per Asisten, Per Mata Kuliah, KONTAK_ASISTEN) | **Data nyata** (data pribadi) | 2024/2025 Genap s.d. 2026/2027 Ganjil (1.147 laporan) | 15, 16, 18 | Digantikan Jurnal Sesi dan Pemeriksaan Kesiapan |
| D4 | Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (23 dokumen: POB, 5 standar, rubrik, 10 formulir, 3 template, IK, matriks revisi, workbook) | **Draf**, berstatus "DRAFT 2026", kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep–Okt 2026 | 15–20 | Pembanding format saja (bagian 4.4) |
| D5 | Paket Dokumen Monev `DOCUMENTS/18`–`23` | **Draf GPT** (keputusan kelompok 26 Okt 2026) | Okt 2026 | 15–20 | Pembanding format saja |
| D6 | Sheet "Wawancara FIKLAB Compliance", bagian Pelaksanaan Praktikum (P1–P19) | Daftar pertanyaan, **belum dijawab** | Nov 2026 | 15–20 | Bukan sumber temuan; hanya rujukan pertanyaan |

**Tidak ditemukan dokumen nyata untuk:** jadwal kuliah praktikum bertanggal, daftar *software* dan lisensi, stok bahan, rubrik penilaian, rekap nilai, dan hasil survei kepuasan.

---

## 2. Pelaku dan peluang otomasi

Penggolongan mengikuti §2.6.1; kolom peluang otomasi mengikuti §2.6.2. Peran diambil dari D1 (kualifikasi pelaksana dan lajur diagram alur) dan D2–D3.

| Pelaku | Sumber | Jenis (§2.6.1) | Peran saat ini | Peluang otomasi (§2.6.2) |
|---|---|---|---|---|
| Kepala Laboratorium | D1 | *Worker* | Mengelola keseluruhan praktikum; meninjau alokasi; seleksi asisten; evaluasi kendala dan kuesioner | Tetap; dibantu status monev dan rekap |
| Laboran | D1 | *Worker* | Administrasi kepesertaan, penyiapan sarana (langkah 8, 16), monitoring alokasi-pelaksanaan (L5) dan kesiapan (L6) | Rekap manual L5/L6 diganti laporan [R]; pemeriksaan kesiapan dicatat langsung |
| Teknisi Laboratorium | D1 | *Worker* | Mengelola sarana dan prasarana | Ikut sebagai pemeriksa kesiapan **[KONFIRMASI]** |
| Asisten Praktikum | D1, D2, D3 | *Worker* (dikontrak fakultas, bekerja untuk lab) | Membantu sesi, mengembangkan soal modul, mengisi presensi dan kendala, **menyesuaikan jadwal dan modul** (langkah 14–15), melapor lewat D3 | **Perantara**: mengetik ulang MK, kelas, tanggal, jam, ruang, dan mengunggah ulang modul di setiap laporan → diambil dari Sesi dan Versi Modul |
| Dosen (koordinator, kelas, tandem) | D1, D2 | *Actor* (staf FIK, di luar struktur lab) | Memberi materi, memperbarui modul, menilai hasil akhir | Menerbitkan Versi Modul dan rubrik; penilaian tetap di LeADS |
| Praktikan | D1 | *Actor* | Mengikuti praktikum, mengisi kuesioner | Mengisi survei lewat tautan |
| Koordinator Program Studi | D1 | *Actor* | Mengajukan MK praktikum dan jumlah kelas (langkah 1, L1); menandatangani L7 dan L9 | Di luar batas sistem; hasilnya diimpor |
| Wakil Dekan Bidang Akademik | D1 | *Actor* | Menyetujui alokasi praktikum (L1) | Di luar batas sistem |
| Dekan | D1 | *Actor* | Mengesahkan POB; mengumumkan rekrutmen asisten | Di luar batas sistem |
| Bagian Tata Usaha | D1 | *Actor* | Lajur di diagram alur (administrasi, kontrak, honor) | Di luar batas sistem (rekap honor tidak dirancang) |
| Google Form + Sheets | D3 | *Worker* (sistem yang ada) | Wadah laporan sesi dan rekap honor | Digantikan Jurnal Sesi |
| Tim jadwal fakultas | D1 langkah 6 ("tabel jadwal kelas"); keterangan Herrens, 14 Nov 2026 | *Actor* (di luar lab) | Menyusun jadwal kelas praktikum; KaLab hanya menyetujui | Di luar batas; berkas jadwalnya diimpor laboran **[ASUMSI]** |
| LeADS, SIMPEL | Brief bersama | *Actor* (sistem luar) | Penilaian dan presensi rinci per praktikan | Di luar batas. SIMPEL ditautkan; penilaian LeADS ditautkan per kelas, diimpor bila ada ekspor Excel (PKG-19) |

**Batas sistem (usulan):** di dalam: KaLab, laboran, teknisi, asisten, dan peran Google Form. Di luar tetapi berinteraksi: dosen dan praktikan (mengisi lewat sistem). Di luar sepenuhnya: Koordinator Prodi, Wakil Dekan, Dekan, Tata Usaha, SIAKAD, LeADS, SIMPEL. Penilai monev bukan aktor sistem (mengikuti keputusan Tata Kelola).

---

## 3. Temuan *as-is* (bahan 2.1 Observasi)

Temuan hanya berasal dari isi dokumen dan data. Klaim tentang praktik sehari-hari tetap harus dikonfirmasi lewat wawancara. Kolom "Analisis" merujuk temuan yang sama di analisis PKG.

| No | Temuan | Sumber | Dampak ke indikator | Analisis | Status |
|---|---|---|---|---|---|
| A1 | POB praktikum **sudah ada (2025)**, mencakup persiapan, pelaksanaan, evaluasi, pengendalian, dan peningkatan, tetapi **belum disahkan**: nomor dokumen, tanggal pembuatan, revisi, efektif, dan pengesahan kosong; lembar pengesahan oleh Dekan belum diisi | D1 | Semua PKG praktikum: prosedur ada tetapi tidak terkendali (PKG-02 Tata Kelola) | — | Fakta dokumen |
| A2 | Alur POB memakai lima kelompok tahap: **Perencanaan** (langkah 1–8), **Pelaksanaan** (9–11), **Evaluasi** (12–13), **Pengendalian** (14–16), **Peningkatan** (17) | D1 | Bahan activity diagram (Langkah 5) | — | Fakta dokumen |
| A3 | Alokasi MK dan jumlah kelas diajukan Koordinator Prodi, ditinjau KaLab, disetujui Wakil Dekan, **4 minggu sebelum perkuliahan** (L1). Formulirnya tidak memuat hari, jam, atau ruang | D1 | PKG-15: jadwal sah belum punya formulir | PKG-15 A3 | Fakta dokumen |
| A4 | Langkah 6 POB menyebut asisten berkoordinasi dengan dosen "berdasarkan **tabel jadwal kelas** mata kuliah praktikum", jadi jadwal kelas ada di luar lab, tetapi tidak dilampirkan dan tidak masuk D2 | D1, D2 | PKG-15: sumber jadwal adalah sistem luar | **Baru** | Sumber jadwal **[KONFIRMASI wawancara P2]** |
| A5 | Kolom hari, jam mulai, dan jam selesai di D2 **kosong di seluruh 222 baris kelas** (3 periode); D2 tidak punya kolom ruang dan jumlah mahasiswa; susunan kolomnya berubah tiap periode | D2 | PKG-15, 18: tidak ada sesi bertanggal; pembagi tidak terbentuk | PKG-15 A1, A10 | Fakta data |
| A6 | Kelas tanpa asisten: 56%, 42%, 56% kelas per periode. Kelas ini tercantum di D2 tanpa alokasi, dan tidak punya laporan di D3 | D2, D3 | PKG-18, 19: sebagian besar kelas tanpa rekaman | PKG-18 A1 | Fakta data |
| A7 | Penyesuaian jadwal dan modul diserahkan kepada **asisten** (langkah 14–15). "Formulir Penyesuaian Jadwal Praktikum" disebut tetapi tidak dilampirkan | D1 | PKG-18: perubahan sesi tanpa persetujuan | PKG-15 A6, PKG-18 A9 | Fakta dokumen |
| A8 | POB tidak mengatur pemakaian lab di luar praktikum maupun penyelesaian bentrok jadwal | D1 | PKG-15 bukti 1, 2, 5 | PKG-15 A5 | Fakta dokumen |
| A9 | Template Modul (L10) punya kolom disusun (dosen), direviu (laboran), disetujui (KaLab), tanggal pengesahan, dan pertemuan ke-, tetapi **tidak punya nomor versi**. Bagian 5 "Alat dan Bahan" memuat *software* dan versinya; bagian 10 hanya bobot nilai (20/30/50, lulus 60) | D1 L10 | PKG-15 (versi), 16 (*software*), 17 (bahan), 19 (rubrik) | PKG-15 A7, PKG-16 A6, PKG-19 A4 | Fakta dokumen |
| A10 | Modul di laporan sesi diunggah ulang asisten setiap kali melapor: 1.062 berkas unik dari 1.064 laporan; kolom "Modul Praktikum" adalah unggah berkas | D3 | PKG-15 C4: tidak ada modul acuan | PKG-15 A9 | Fakta data + keterangan Herrens (14 Nov 2026) |
| A11 | Monitoring kesiapan sarana (L6) dirancang **berkala** oleh laboran, per MK-kelas × 8 ruang, kolom Alat/Bahan/Konektivitas (keterangan menyebut *Software* tetapi kolomnya tidak ada) | D1 L6 | PKG-16: bentuk *as-is* bukan per sesi | PKG-16 A2 | Fakta dokumen |
| A12 | Dalam praktik kesiapan dicatat **asisten** di D3: 104 laporan "Siap" mencatat kendala; 11 sesi "Belum Siap" tetap berjalan; tidak ada keputusan tunda | D3 | PKG-16 S1, S4 | PKG-16 A3 | Fakta data |
| A13 | Kendala sarana di 14% laporan: PC 31, jaringan 27, *software* 22, proyektor/audio 16, PC kurang 8 | D3 | PKG-16: kategori butir pemeriksaan | PKG-16 A4 | Fakta data (penggolongan kata kunci) |
| A14 | Jejak bahan fisik hanya di 3 laporan (*crimping* kabel LAN); MK Praktikum IoT tercantum di D2 tanpa satu laporan pun | D2, D3 | PKG-17 bersyarat, berlaku terbatas | PKG-17 A2, A3 | Fakta data; pemakaian komponen IoT **[KONFIRMASI P9]** |
| A15 | Lembar Pelaksanaan Asistensi (L7) mencatat **waktu mulai saja**, tanpa waktu selesai; D3 mencatat keduanya | D1 L7, D3 | PKG-18 C3: durasi tidak bisa dihitung dari L7 | **Baru** | Fakta dokumen |
| A16 | Monitoring Alokasi dan Pelaksanaan (L5) membandingkan A (alokasi) dan L (laporan) per pertemuan per kelas, diparaf laboran. D3 punya tab rekap "Per Pertemuan", "Per Asisten", "Per Mata Kuliah" yang dibuat manual | D1 L5, D3 | PKG-18: rekap keterlaksanaan sudah dibutuhkan, tetapi dikerjakan manual | **Baru** (sebagian di `brief-role-3.md`) | Fakta dokumen dan data |
| A17 | Kualitas laporan D3: cakupan sesi berasisten 75% dan 64%; 62 laporan ganda; 148 durasi tidak valid (13%); keterlambatan median sampai 29,5 hari; 55 sesi daring tanpa persetujuan; 70 laporan dengan asisten berbeda dari rencana; tidak ada presensi laboran; presensi praktikan berupa jumlah | D2, D3 | PKG-18 C1–C5 | PKG-18 A2–A9 | Fakta data |
| A18 | Kolom "Status" (TRUE/FALSE) di D3 belum diketahui fungsinya | D3 | PKG-18 (verifikasi) | PKG-18 A10 | **[KONFIRMASI P11]** |
| A19 | D3 dan L7 tidak punya kolom nilai, rubrik, atau umpan balik; POB langkah 10 tidak konsisten (diagram: "penilaian", penjelasan: presensi dan kendala) | D1, D3 | PKG-19: lab tidak memegang bukti penilaian | PKG-19 A2, A5 | Fakta dokumen |
| A20 | Kuesioner Peserta (L8): 15 butir skala 1–5 + 1 saran, meminta nama praktikan, tanpa butir keselamatan dan akses, tanpa populasi atau target respons. Tidak ditemukan data respons | D1 L8 | PKG-20 K1–K3 | PKG-20 A2, A3, A5 | Fakta dokumen; pernah dijalankan atau tidak **[KONFIRMASI P16]** |
| A21 | Lembar Evaluasi Kendala dan Tindak Lanjut (L9) sudah memuat pola analisis penyebab → solusi → PIC → tanggal mulai/selesai, ditandatangani Koorprodi, dosen koordinator, KaLab | D1 L9 | PKG-20 K4 (pola RTL) | PKG-20 A4 | Fakta dokumen |
| A22 | Pencatatan saat ini dirancang untuk **honor asisten**: D3 hanya diisi asisten, sheet rekap menghitung sesi per asisten, dan lampiran D2 berisi data kontak asisten | D2, D3 | Semua PKG: rekaman tidak dirancang sebagai bukti monev | Brief bersama | Fakta data |

**Rumusan *as-is* ringkas:** LabFIK sudah punya prosedur praktikum (POB 2025) dan rekaman pelaksanaan yang besar (lebih dari seribu laporan), tetapi **rekaman itu dibuat untuk honor asisten, bukan sebagai bukti mutu**. Jadwal tidak bertanggal, modul tidak berversi, kesiapan dinilai sendiri oleh asisten sesudah sesi, perubahan sesi tidak tercatat, kelas tanpa asisten tidak terekam, dan bukti penilaian serta kepuasan tidak ada di lab. Prosedur itu sendiri belum disahkan.

---

## 4. Bedah per dokumen

Kolom tabel: **Bagian** (sumber) · **Field (usulan)** · **Model** · **PKG/kriteria** · **Dasar**.

### 4.1 D1: POB Manajemen Praktikum dan Asistensi 2025

**Kepala dokumen dan identitas**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Nomor dokumen, tanggal pembuatan, revisi, efektif, jadwal reviu, pengesahan Dekan | **Tidak diambil di modul ini.** POB adalah dokumen terkendali milik PKG-02 (Tata Kelola) | `labfik.document` (Tata Kelola) | PKG-02 | Instr PKG-02 |
| Dasar hukum, tujuan, keterkaitan | Tidak diambil | — | — | Format |
| Kualifikasi pelaksana (KaLab, laboran, teknisi, dosen pengampu, asisten, praktikan) | Peran dan jabatan di Core | `hr.job` diperluas (Core) | Semua | Analisis (pelaku, bagian 2) |
| Peringatan (alat baik, keamanan, cek kesiapan sebelum setiap sesi, kerahasiaan data) | Dasar aturan Pemeriksaan Kesiapan per sesi | `labfik.praktikum.kesiapan` | PKG-16 S1 | Instr PKG-16, ISO 6.4.4 |
| Pencatatan (daftar peserta, kehadiran, laporan hasil, evaluasi kinerja asisten) | Kehadiran → Jurnal Sesi; daftar peserta dan laporan hasil tidak disimpan per mahasiswa; evaluasi kinerja asisten milik SDM | `labfik.praktikum.jurnal` | PKG-18 | Instr PKG-18 bukti 3; Analisis PKG-19 (tanpa data per praktikan) |

**Langkah prosedur → perlakuan TO-BE** (bahan activity diagram Langkah 5)

| No | Langkah (pelaksana) | Dokumen/hasil | PKG | TO-BE |
|---|---|---|---|---|
| 1 | Alokasi MK praktikum dengan asisten (Koorprodi, 4 minggu sebelum kuliah) | L1 | 15 | Di luar sistem; hasilnya diimpor menjadi Mata Kuliah dan Kelas |
| 2–5 | Pengumuman, pendaftaran, seleksi, kontrak asisten | L2–L4, surat | — | **Milik SDM** (PKG-04, 10). Tidak diambil |
| 6 | Alokasi jadwal asisten (asisten + dosen, berdasarkan tabel jadwal kelas) | D2 | 15, 04 | Sesi dibangkitkan dari jadwal kelas (15); penugasan asisten ke Sesi milik SDM (04) |
| 7 | Mengembangkan tugas di modul (asisten, dari pembaruan dosen) | Modul | 15 | Versi Modul diterbitkan dosen |
| 8 | Penyiapan sarana dan prasarana (laboran, 1 minggu) | Laporan Kesiapan Sarpras | 16, 17 | Pemeriksaan Kesiapan per sesi |
| 9 | Asistensi praktikum (asisten, 16 minggu) | L7 / D3 | 18 | Jurnal Sesi |
| 10 | "Penilaian" / evaluasi praktikum: presensi dan kendala (asisten) | L7 / D3 | 18, 19 | Jurnal Sesi (presensi, kendala); penilaian lewat tautan LeADS per kelas, impor Excel bila tersedia (PKG-19) |
| 11 | Kuesioner peserta (praktikan, setiap sesi) | L8 | 20 | Survei per periode (bukan per sesi) |
| 12 | Evaluasi kendala (KaLab, laboran) | L9 | — | Kendala tercatat di Jurnal Sesi; alur evaluasi kendala tersendiri **tidak dirancang** (tidak ada kriteria instrumen yang memintanya) |
| 13 | Evaluasi kuesioner (KaLab, asisten) | Laporan Evaluasi Kuesioner | 20 | Evaluasi Survei |
| 14 | Penyesuaian jadwal (asisten) | Formulir Penyesuaian Jadwal (tidak dilampirkan) | 18 | Perubahan Sesi dengan persetujuan |
| 15 | Penyesuaian modul (asisten) | Modul | 15 | Versi Modul baru diterbitkan dosen |
| 16 | Penyesuaian sarana (laboran) | Laporan Kesiapan Sarpras | 16 | Butir "diperbaiki sebelum sesi" atau keputusan tunda |
| 17 | Rekapitulasi dan arsip (laporan hasil, kehadiran, evaluasi asisten) | Laporan Rekapitulasi | 18 | Laporan [R] |

**L1 Formulir Alokasi Praktikum dengan Asisten**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Periode akademik | `periode_id` | `labfik.kelas` (Core) | 15 | Instr PKG-15 (pembagi per periode) |
| Program studi, kode MK, nama MK | `prodi`, `kode`, `name` | `labfik.mata.kuliah` (Core) | 15 | Analisis PKG-15 (kode sebagai kunci) |
| Jumlah kelas | Dihasilkan dari jumlah `labfik.kelas` per MK | [R] | 15 | Format |
| Diajukan Koorprodi / ditinjau KaLab / disetujui Wadek | **Tidak diambil.** Alokasi disetujui di luar sistem; yang ditetapkan di sistem adalah jadwal | — | — | Analisis (aktor di luar batas) |

**L2–L4 Pendaftaran, Berita Acara Penilaian, dan Daftar Nama Asisten** — **tidak diambil**; milik modul SDM (PKG-04, 10). Diteruskan ke Zahir.

**L5 Monitoring Alokasi dan Pelaksanaan Asisten**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Kode MK, kelas, pertemuan 1–15, A (alokasi) / L (laporan), ΣA, ΣL, paraf laboran | Dihasilkan: sesi rencana vs jurnal terkirim per kelas per pertemuan | [R] Rekap Keterlaksanaan per Kelas | 18 | Instr PKG-18 (pembilang/pembagi) |

**L6 Monitoring Kesiapan Sarana Prasarana**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Monitoring ke-, laboran, paraf | `pemeriksa_id`, `waktu_periksa` (per sesi, bukan per monitoring) | `labfik.praktikum.kesiapan` | 16 S1 | Instr PKG-16 ("sebelum setiap sesi") |
| Kode MK, kelas, lab (8 ruang) | Dari Sesi (`sesi_id` → kelas, ruang) | `labfik.praktikum.kesiapan` | 16 | Analisis PKG-16 |
| A Alat | Butir kategori "PC/stasiun kerja", `jumlah_stasiun_berfungsi` | `labfik.praktikum.kesiapan.butir` | 16 S2 | Instr PKG-16 bukti 1–2 |
| B Bahan | Butir kategori "bahan" | `labfik.praktikum.kesiapan.butir` | 17 B1–B3 | Instr PKG-17 |
| C Konektivitas | Butir kategori "jaringan" | `labfik.praktikum.kesiapan.butir` | 16 S2 | Instr PKG-16 (utilitas) |
| D *Software* (hanya di keterangan) | Butir kategori "*software*" dari daftar Versi Modul, tanda lisensi sah | `labfik.praktikum.kesiapan.butir` | 16 S3 | Instr PKG-16 bukti 4 |
| (tidak ada di L6) Listrik, proyektor, keputusan siap/tunda | Butir "listrik", "proyektor/audio"; `keputusan` | `labfik.praktikum.kesiapan` | 16 S2, S4 | Instr PKG-16 bukti 5–6 |

**L7 Lembar Pelaksanaan Asistensi Praktikum**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Periode, MK/kode, semester, prodi, dosen koordinator, kelas | Dari Sesi → Kelas (tidak diketik ulang) | `labfik.sesi` (Core) | 18 C2 | Analisis PKG-18 |
| Pertemuan, hari/tanggal, ruang | Dari Sesi (`pertemuan_ke`, `tanggal`, `ruang_id`) | `labfik.sesi` | 18 C2 | Instr PKG-18 bukti 1 |
| Waktu mulai | `jam_mulai_aktual` (+ `jam_selesai_aktual`, tidak ada di L7) | `labfik.praktikum.jurnal` | 18 C3 | Instr PKG-18 (durasi sesuai) |
| Nama dosen, nama asisten, paraf dosen, paraf asisten | Baris presensi petugas: `personel_id`, `peran`, `kehadiran` | `labfik.praktikum.jurnal.petugas` | 18 C5 | Instr PKG-18 bukti 3 |
| Topik, modul | `topik`, `modul_id` (Versi Modul) | `labfik.praktikum.jurnal` | 18 C4 | Instr PKG-18 bukti 4 |
| Jumlah (praktikan hadir) | `jumlah_hadir` | `labfik.praktikum.jurnal` | 18 C5, 19 | Instr PKG-18 bukti 3; Analisis (jumlah, bukan per nama) |
| Kendala | `kendala` | `labfik.praktikum.jurnal` | 18 | Instr PKG-18 bukti 5 (*log book*) |
| Tanda tangan Koorprodi, dosen koordinator, KaLab | **Tidak diambil.** Rekap per kelas dihasilkan sistem | [R] | — | Format |

**L8 Formulir Kuesioner Peserta Praktikum**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Periode | `periode_id` | `survey.survey` (*extend*) | 20 K1 | Instr PKG-20 |
| MK, kelas, ruang, pertemuan ke- | Butir identitas opsional (pilihan) | `survey.question` | 20 | Format |
| Nama praktikan | **Tidak diambil** (survei anonim) | — | — | Analisis PKG-20 (A3) |
| Butir 1–15 skala 1–5 | Butir bawaan + `aspek` (enam aspek instrumen) | `survey.question` | 20 K2 | Instr PKG-20 kriteria 2 |
| Butir 16 saran | Butir terbuka (keluhan/saran) | `survey.question` | 20 bukti 5 | Instr PKG-20 bukti 5 |
| (tidak ada) Populasi, target respons, waktu survei | `jumlah_populasi`, `target_response_rate`, tanggal buka/tutup | `survey.survey` (*extend*) | 20 K1–K2 | Instr PKG-20 kriteria 1–2 |

**L9 Lembar Evaluasi Kendala Praktikum dan Tindak Lanjut**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Tanggal evaluasi | `tanggal` | `labfik.praktikum.evaluasi.survei` | 20 K3 | Instr PKG-20 |
| Pengaduan (deskripsi, sumber, obyek kendala) | Tidak diambil sebagai field; keluhan terbuka dari survei, kendala dari Jurnal Sesi | — | 20 bukti 5 | Analisis PKG-20 |
| Analisis (kemungkinan penyebab, potensi solusi) | `kesimpulan` (per aspek) | `labfik.praktikum.evaluasi.survei` | 20 K3 | Instr PKG-20 bukti 4 |
| Tindak lanjut (PIC, tanggal mulai, tanggal selesai, keterangan) | Baris RTL: `aspek`, `prioritas`, `tindakan`, `pic_id`, `tenggat`, `status`, `efektivitas` | `labfik.praktikum.evaluasi.rtl` | 20 K4 | Instr PKG-20 bukti 6 |
| Tanda tangan | Tidak diambil | — | — | Format |

**L10 Template Modul Praktikum**

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Kode MK, nama MK, semester/tahun akademik, nama praktikum | `mata_kuliah_id`, `periode_id`, `name` | `labfik.praktikum.modul` | 15 C4 | Instr PKG-15 bukti 3 |
| Pertemuan ke- | Tidak dijadikan kunci; satu modul per MK per periode | — | 15 | Analisis PKG-15 **[KONFIRMASI P4]** |
| Disusun oleh (dosen) | `penyusun_id` | `labfik.praktikum.modul` | 15 | Instr PKG-15 (PJ dosen) |
| Direviu oleh, disetujui oleh, tanggal pengesahan | **Tidak diambil** (modul cukup diterbitkan, tanpa pengesahan) | — | — | Keputusan Herrens 14 Nov 2026 |
| (tidak ada) Nomor versi, tanggal terbit, status | `versi`, `tanggal_terbit`, `state` (draf/berlaku/diganti) | `labfik.praktikum.modul` | 15 C4 | Instr PKG-15 ("versi berlaku"), ISO 7.2.1.3 |
| Isi 1–4, 6–9, 11 (pendahuluan, tujuan, kompetensi, tempat, teori, langkah, tugas, format laporan, referensi) | Tetap di berkas PDF modul (`berkas`) | `labfik.praktikum.modul` | 15 | Format |
| 5 Alat dan Bahan: OS, RAM, *software* + versi, internet | Baris `software` (nama, versi minimal, bebas/berbayar); baris `bahan` (pertemuan ke-, nama, jumlah) | `labfik.praktikum.modul.software`, `labfik.praktikum.modul.bahan` | 16 S3, 17 B1 | Instr PKG-16 bukti 4, PKG-17 bukti 1 |
| 10 Penilaian (komponen dan bobot, nilai lulus) | `berkas_rubrik` | `labfik.praktikum.modul` | 19 P2 | Instr PKG-19 bukti 1 |

### 4.2 D2: Sheet Alokasi Pertemuan Asisten Praktikum

| Bagian | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Nama tab per periode (`ALOKASI_ASISTEN_PER_MINGGU_<periode>`) | `periode_id` | `labfik.periode` (Core) | 15 | Instr PKG-15 |
| Program studi, kode MK, nama MK, nama lengkap MK, semester | `labfik.mata.kuliah`: `kode`, `name`, `prodi`, `semester` | Core | 15 | Analisis PKG-15 (impor) |
| Kelas | `labfik.kelas`: `name`, `mata_kuliah_id`, `periode_id` | Core | 15 | Analisis PKG-15 |
| Hari, jam mulai, jam selesai (selalu kosong) | Masukan saat membangkitkan Sesi (pola mingguan), tidak disimpan | Wizard bangkitkan Sesi | 15 | Analisis PKG-15 |
| (tidak ada) Ruang, jumlah mahasiswa | `labfik.kelas.jumlah_mahasiswa`; ruang di pola mingguan | Core | 15 C3 | Instr PKG-15 ("sesuai kapasitas") |
| Dosen koordinator, dosen kelas, dosen tandem | `labfik.kelas`: `dosen_koordinator_id`, `dosen_ids` | Core | 15, 18 | Analisis (pengisi/penyetuju) |
| Pertemuan 1–7, UTS, 9–15, UAS (berisi nama asisten) | Nomor pertemuan Sesi (`pertemuan_ke`); nama asisten = **penugasan, milik SDM** (PKG-04) | `labfik.sesi` + SDM | 15, 04 | Analisis PKG-15, pemetaan |
| Jumlah alokasi per kelas, CEK | Dihasilkan | [R] | — | Format |
| Tab LOV Nama Asisten (NIM, nama, prodi, HP, email), Total Alokasi | **Tidak diambil di modul ini**; data pribadi; milik SDM (Personel) | — | — | Larangan data pribadi (CLAUDE.md bagian 3) |
| Tab Rekap per MK / per Asisten / per Prodi | Dihasilkan | [R] | 18 | Format |

### 4.3 D3: Google Form Pelaksanaan Asistensi dan sheet responsnya

| Kolom formulir | Field (usulan) | Model | PKG/kriteria | Dasar |
|---|---|---|---|---|
| Timestamp | `tanggal_kirim` (otomatis saat status → dikirim) | `labfik.praktikum.jurnal` | 18 (peringatan keterlambatan) | ISO 7.5.1 |
| Nama Asisten, NIM Asisten, Email Address | Pengisi = pengguna yang masuk (`create_uid` → Personel) | `labfik.praktikum.jurnal` | 18 | Analisis PKG-18 |
| Periode, Nama Mata Kuliah, Kelas, Tanggal, Hari, Ruang, Pertemuan Ke | **Tidak diketik ulang**: diambil dari Sesi (`sesi_id`) | `labfik.sesi` | 18 C2 | Analisis PKG-18 (A5, A7) |
| Waktu Mulai, Waktu Akhir | `jam_mulai_aktual`, `jam_selesai_aktual` dengan validasi akhir > mulai | `labfik.praktikum.jurnal` | 18 C3 | Instr PKG-18 (durasi) |
| Jumlah Kehadiran Mahasiswa | `jumlah_hadir` | `labfik.praktikum.jurnal` | 18 C5, 19 | Instr PKG-18 bukti 3 |
| Apakah dosen hadir?, Kehadiran Dosen Praktikum (hadir penuh/hadir awal/tidak hadir) | Baris presensi petugas peran dosen, `kehadiran` (penuh/sebagian/tidak) | `labfik.praktikum.jurnal.petugas` | 18 C5 | Instr PKG-18 bukti 3 |
| (tidak ada) Presensi laboran | Baris presensi petugas peran laboran | `labfik.praktikum.jurnal.petugas` | 18 C5 | Instr PKG-18 bukti 3 |
| Topik Kegiatan Praktikum | `topik` | `labfik.praktikum.jurnal` | 18 C4 | Instr PKG-18 bukti 2 |
| Kesiapan Sarana Praktikum (Siap/Dapat Disesuaikan/Belum Siap) | **Dipindah** ke Pemeriksaan Kesiapan oleh laboran sebelum sesi | `labfik.praktikum.kesiapan` | 16 | Instr PKG-16 (PJ laboran) |
| Keterangan Kendala Praktikum | `kendala`; entri *log book* | `labfik.praktikum.jurnal`, `.jurnal.logbook` | 18 bukti 5 | Instr PKG-18 bukti 5 |
| Modul Praktikum (unggah berkas) | `modul_id` → Versi Modul berlaku (tidak mengunggah ulang) | `labfik.praktikum.jurnal` | 18 C4 | Instr PKG-18 bukti 4 |
| Foto Pelaksanaan Praktikum | `foto` | `labfik.praktikum.jurnal` | 18 | Analisis (bukti pendukung) |
| Status (TRUE/FALSE) | Belum diambil | — | — | **[KONFIRMASI P11]** |
| Dosen Koordinator, Dosen Pengampu | Dari Kelas (Core) | `labfik.kelas` | — | Analisis |
| Tab Per Pertemuan, Per Asisten, Per Mata Kuliah | Dihasilkan | [R] Rekap Keterlaksanaan per Kelas | 18 | Format |
| Tab KONTAK_ASISTEN | Tidak diambil; data pribadi; milik SDM | — | — | Larangan data pribadi |

### 4.4 D4 dan D5: field draf yang ditimbang

Field berikut muncul di draf (terutama D4: FRM-PRK-03 Lembar Pelaksanaan dan Verifikasi Sesi, FRM-PRK-04, STD-PRK-01–05, IK-PRK-01, INDEX) dan **tidak ada di dokumen nyata**. Hanya yang punya dasar instrumen atau analisis yang diambil.

| Field/gagasan draf | Diambil? | Alasan / Dasar |
|---|---|---|
| *Session ID* per sesi | **Ya**, sebagai identitas Sesi | Analisis PKG-15/18 (Sesi bertanggal); bukan karena draf |
| *Module ID/Version* di lembar sesi | **Ya** (`modul_id`) | Instr PKG-15 bukti 3, PKG-18 bukti 4 |
| *Check-in/check-out* per petugas | Tidak; cukup tingkat kehadiran | Instrumen meminta presensi, bukan jam per orang |
| Status dosen FULL/SUPERVISED/PARTIAL/ABSENT/SUBSTITUTE | Sebagian: penuh/sebagian/tidak | D3 (nyata) sudah memakai hadir penuh/awal/tidak |
| Status sesi COMPLETED-PENDING/VERIFIED/RESCHEDULED/CANCELLED/NONCONFORMITY dan verifikasi laboran | Tidak (verifikasi menunggu P11); status sesi disatukan di state machine Langkah 5 | Analisis PKG-18 |
| *Incident ID*, register insiden, *workstation ID*, *cable control* | Tidak | Analisis PKG-16 (ditunda) |
| *Control gate* minggu 7/8 dengan KPI G/Y/R | Tidak | Tidak ada kriteria instrumen yang memintanya |
| *Module owner*, *dry-run*, *review cycle*, *improvement backlog* | Tidak | Analisis PKG-15 (ditunda) |
| Rekap honor, *Honor_Recap* | Tidak | Batasan masalah brief |
| Alokasi asisten terpusat, *minimum coverage* | Tidak di modul ini | Milik SDM (PKG-04) |

---

## 5. Pola berulang → kandidat *mixin*

Bahan untuk Langkah 10. Semua **[USULAN PENULIS]**.

| Pola | Muncul di | Kandidat |
|---|---|---|
| Rekaman "satu per Sesi" yang harus dibuat **sebelum** atau **sesudah** jam Sesi (cek waktu terhadap Sesi, satu rekaman per Sesi, ruang dan kelas ikut Sesi) | Pemeriksaan Kesiapan (16), Jurnal Sesi (18) | Mixin kecil `labfik.praktikum.sesi.mixin` (`sesi_id` unik, field *related*, `_cek_waktu_terhadap_sesi()` {hook}) |
| Rekaman kegiatan bertanggal dengan pelapor dan bukti | Pemeriksaan Kesiapan, Jurnal Sesi, Evaluasi Survei | `labfik.evidence.mixin` (Core) |
| Dokumen berversi tanpa pengesahan | Versi Modul (15) | Field `versi` biasa; `labfik.controlled.mixin` tidak dipakai lagi (kontrak Core terbaru, 14 Nov 2026) |
| Penetapan oleh pejabat berwenang | Penetapan Jadwal (15), penetapan Survei (20) | Jadwal: `labfik.approval.mixin` (Core), karena jadwal harus ditandatangani (keputusan 14 Nov 2026). Survei: status sederhana + cek wewenang (brief, Kontrak Core) |
| Persetujuan sederhana (diajukan → disetujui/ditolak) | Rencana Pemakaian Lab (15), Perubahan Sesi (18) | Satu pola status bersama di modul |
| Indikator kriteria berurutan | Evaluasi Survei (20) | `labfik.criteria.mixin` (Core) |
| Persentase sesi memenuhi | 15, 16, 17, 18 (19: kelas berbukti; per praktikan bila diimpor) | Satu cara hitung bersama (*compute* atau *report*); diputuskan di Langkah 10 |

---

## 6. Daftar model TO-BE (konsolidasi)

| Model | Label | Dari dokumen | PKG |
|---|---|---|---|
| `labfik.mata.kuliah`, `labfik.kelas`, `labfik.sesi` | [M], [M], [T] Core | D1 L1, D2 | 15 (diisi), semua |
| `labfik.praktikum.jadwal` (Penetapan Jadwal) | [T] | D1 langkah 1, 6 | 15 |
| `labfik.praktikum.pemakaian` (Rencana Pemakaian Lab) | [T] | — (tidak ada di dokumen; dari instrumen) | 15 |
| `labfik.praktikum.modul` (+ `.software`, `.bahan`) | [T] | D1 L10, D3 | 15, 16, 17, 19 |
| `labfik.praktikum.kesiapan` (+ `.butir`) | [T] | D1 L6, D3 | 16, 17 |
| `labfik.praktikum.jurnal` (+ `.petugas`, `.logbook`, `.penilaian`) | [T] | D1 L7, D3 | 18, 19 |
| `labfik.praktikum.perubahan` (Perubahan Sesi) | [T] | D1 langkah 14 | 18 |
| `survey.survey`, `survey.question` (*extend*) | [T] | D1 L8 | 20 |
| `labfik.praktikum.evaluasi.survei` (+ `.rtl`) | [T] | D1 L9 | 20 |
| Laporan: Jadwal Terpadu, Rekaman Konflik, Daftar Sesi Tidak Memenuhi (per PKG), Rekap Keterlaksanaan per Kelas, Rekap Kesiapan per Ruang, Rekap Hasil per Aspek, Perbandingan Antarperiode, Status K1–K4 | [R] | D1 L5, D3 tab rekap | 15–20 |

Total delapan transaksi milik modul, sama dengan brief. Nama model sementara; ditetapkan di Langkah 10.

---

## 7. Cek silang dan catatan penutup

### 7.1 Cek silang ke langkah sebelumnya

| Cek | Hasil |
|---|---|
| Setiap kriteria instrumen PKG-15–20 punya field dan sumber dokumen | Ya. Yang **tidak punya padanan di dokumen nyata** (diturunkan dari instrumen saja): Rencana Pemakaian Lab (15), konflik jadwal (15), versi modul (15), keputusan tunda (16), substitusi bahan (17), populasi dan target respons (20) |
| Field dari draf hanya dipakai bila didukung instrumen/analisis | Ya (bagian 4.4) |
| Entitas sama dengan analisis dan brief | Ya: 8 transaksi, 0 master lokal |
| Status dan nama konsep konsisten | Belum seluruhnya: status Sesi, Jurnal, Perubahan, dan Pemeriksaan baru disatukan di state machine (Langkah 5) |
| Langkah 1 | Baru sebagian: cakupan rancangan masih usulan di brief, arahan pembimbing belum dicatat |

### 7.2 Daftar [KONFIRMASI]

| Hal | Kepada | Rujukan |
|---|---|---|
| Sumber dan waktu penetapan "tabel jadwal kelas" | KaLab, laboran (P2) | A4 |
| Siapa mengisi jurnal kelas tanpa asisten | KaLab, laboran (P10, P13) | A6 |
| Fungsi kolom Status TRUE/FALSE | Laboran (P11) | A18 |
| Teknisi ikut memeriksa kesiapan | KaLab | Bagian 2 |
| Modul per MK atau per pertemuan | KaLab (P4) | L10 |
| Pemakaian komponen IoT | Laboran (P9) | A14 |
| Kuesioner pernah dijalankan | KaLab (P16) | A20 |
| Paket 2026 dibuat dengan GPT atau disusun lab | KaLab | D4 **[VALIDASI]** |
| Izin mengutip angka agregat D2/D3 di proposal | KaLab | Bagian 3 |

### 7.3 Dokumen lain yang perlu ikut berubah

| Dokumen | Perubahan | Pemilik |
|---|---|---|
| [analisis-data-persiapan-15.md](analisis-data-persiapan-15.md) | Tambah temuan A4 (jadwal kelas ada di luar lab, dari POB langkah 6) | Herrens — **sudah diterapkan** (PKG-15 A13) |
| [analisis-data-proses-18.md](analisis-data-proses-18.md) | Tambah temuan A15 (L7 tanpa waktu selesai) dan A16 (L5 + tab rekap manual) | Herrens — **sudah diterapkan** (PKG-18 A16, A17) |
| [brief-praktikum.md](../brief/brief-praktikum.md) | Tautan ke dokumen ini di bagian Kondisi saat ini; rumusan *as-is* ringkas | Herrens — **sudah diterapkan** |
| Modul SDM (Zahir) | Lampiran L2–L4 POB 2025 (pendaftaran, berita acara penilaian, daftar asisten) dan kolom pertemuan di D2 adalah bahan PKG-04/10 | Zahir |
| Modul Tata Kelola (Febriyan) | POB Praktikum 2025 adalah calon Dokumen Induk PKG-02 (belum bernomor dan belum disahkan) | Febriyan |

### 7.4 Kesalahan sendiri yang ditemukan

| Kesalahan | Di mana | Perbaikan |
|---|---|---|
| Analisis PKG-15 menyebut sumber jadwal kelas "belum punya sumber". POB langkah 6 sebenarnya sudah menyebut "tabel jadwal kelas", jadi keberadaannya punya dasar dokumen; yang belum diketahui hanya letaknya | Analisis PKG-15 bagian 0 | Tambahkan A4 dokumen ini ke analisis PKG-15 |
| Analisis PKG-18 A13 menyebut isi L7 tanpa menyadari bahwa L7 tidak punya waktu selesai | Analisis PKG-18 A13 | Tambahkan catatan A15 |
| Brief menyebut "kondisi saat ini" tanpa merujuk studi dokumen (belum ada saat itu) | Brief, bagian Kondisi saat ini | Tambah tautan ke dokumen ini |
| Analisis PKG-16 dan PKG-20 menyebut PJ dan penyetuju tanpa menggolongkan pelaku sebagai *actor*/*worker* | Analisis PKG-16, 20 | Penggolongan kini ada di bagian 2; dipakai di Langkah 4 (tabel aktor) |
