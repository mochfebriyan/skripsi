# Analisis Data Indikator Evaluasi 20 (Kepuasan Pengguna)

14 November 2026 · Herrens · PKG-20 Evaluasi 20 (kepuasan pengguna) · Modul: Pelaksanaan Praktikum (ditetapkan 1 Nov 2026; di sheet belum bermodul)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab; wawancara bagian Pelaksanaan Praktikum belum dijawab.

PIC analisis awal di sheet adalah Patih dari kelompok lain (tab *Analysis* baris 55: Rencana Survei, Respons Survei, Keluhan Terbuka, Analisis Hasil, Rencana Tindak Lanjut [T]; Rekap per Aspek dan Perbandingan Antarperiode [R]; master aspek, instrumen, dan butir survei, ruang lab, mata kuliah). Dokumen ini melanjutkannya. Alasan PKG-20 masuk modul Praktikum ada di [pemetaan](pemetaan-package-instrumen.md#2d-kenapa-pkg-20-masuk-pelaksanaan-praktikum) bagian 2d.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2. Contoh format untuk indikator kriteria berurutan: analisis Pengelolaan 1 dan 3 di tag `rancangan-tatkel-v1`.

---

## Ringkasan

| | Evaluasi 20 |
|---|---|
| Inti | Kepuasan pengguna lab diukur dengan survei yang direncanakan, dianalisis, ditindaklanjuti, dan efektivitas tindak lanjutnya dibandingkan pada periode berikutnya |
| PJ (instrumen) | KaLab; GKM |
| Jenis skor | **Kriteria berurutan K1–K4** (satu-satunya di modul Praktikum; PKG-15 s.d. 19 memakai persentase) |
| Unit | 1 paket dokumen dan rekaman (per periode survei) |
| Level cakupan (usulan) | **Semi-otomatis**. Sistem menunjukkan kriteria tertinggi yang lengkap secara data; skor akhir ditetapkan penilai |
| Posisi dalam dependensi | Berdiri sendiri; hanya butuh Core. Tidak bergantung pada package lain |
| Acuan ISO/IEC 17025 | 8.6.2 (mencari umpan balik pelanggan, menganalisis, dan memakainya untuk perbaikan; dirujuk instrumen) · 7.9 (pengaduan) |
| Kompleksitas (kasar) | **5** (rincian di bagian 8) |

**Temuan utama:**
1. **Tidak ada bukti survei kepuasan pernah dijalankan.** POB 2025 punya kuesioner peserta, tetapi tidak ditemukan data respons atau laporan evaluasinya (A1, A5).
2. **Kuesioner yang ada belum memenuhi K2.** Butirnya tidak mencakup aspek keselamatan dan akses, alat dan bahan digabung dalam satu butir, tidak ada target respons maupun populasi, dan responden hanya praktikan (A2, A6).
3. **Pola tindak lanjut sudah ada di dokumen nyata.** Lembar Evaluasi Kendala dan Tindak Lanjut POB 2025 berisi analisis penyebab, solusi, PIC, dan tanggal (A4). Pola ini cocok untuk Rencana Tindak Lanjut (K4).
4. Odoo 17 Community sudah menyediakan addon **`survey`** (LGPL-3). Addon ini di-*extend*, sehingga PKG-20 tidak perlu membuat sendiri master instrumen, master butir, dan transaksi respons.

**Keputusan (Herrens, 14 November 2026):** survei memakai addon `survey` bawaan Odoo, karena paling sederhana untuk dibangun (kuesioner, tautan isi, dan statistik jawaban sudah tersedia). Google Form + impor menjadi jalan pengganti saja.

---

## 0. Sumber dan temuan *as-is*

### Dokumen dan data yang dipakai

| Sumber | Sifat | Tanggal | Yang relevan untuk PKG-20 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`) | **Nyata**, belum disahkan | 2025 | Langkah 11 dan 13; Formulir Kuesioner Peserta Praktikum; Lembar Evaluasi Kendala Praktikum dan Tindak Lanjut |
| Pencarian Drive LabFIK ("Kuesioner", "Kepuasan", "Survei", "Evaluasi Praktikum", "Feedback") | Hasil pencarian | 14 Nov 2026 | Ada tidaknya data survei nyata |
| Google Form "Pelaksanaan Asistensi Praktikum" (Responses) | **Data nyata** (tidak dikutip per baris) | Diolah 14 Nov 2026 | Kendala yang dilaporkan asisten |
| Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (FRM-PRK-06 Kuesioner Evaluasi Praktikum Mahasiswa, FRM-PRK-05 Evaluasi Tengah Semester dan Tindak Lanjut) | **Draf**, kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep 2026 | Contoh format saja |
| Paket Dokumen Monev `DOCUMENTS/23_SOP_Kepuasan_Keluhan`, `24_SOP_Evaluasi_Tindakan_Korektif_Inovasi` | **Draf GPT** | Okt 2026 | Contoh format saja |

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | POB 2025 langkah 11: praktikan mengisi kuesioner kepuasan setelah sesi praktikum. Langkah 13: KaLab dan asisten mengevaluasi hasil kuesioner, dengan hasil "Laporan Evaluasi Kuesioner Praktikum" | POB 2025 |
| A2 | Formulir Kuesioner Peserta POB 2025: identitas (periode, MK, kelas, ruang, pertemuan ke-, **nama praktikan**), 15 butir skala 1–5, dan 1 pertanyaan saran terbuka. Butir 1–8 dan 14 tentang asisten, 9 tentang alat **dan** bahan (satu butir), 10 waktu, 11 modul, 12 lingkungan lab, 13 pemahaman materi, 15 keseluruhan. **Tidak ada butir keselamatan dan akses**; alat dan bahan tidak bisa dipisahkan | POB 2025 lampiran |
| A3 | Kuesioner meminta nama praktikan, sehingga tidak anonim. Ini berisiko membuat jawaban bias dan menambah data pribadi yang harus dijaga | POB 2025 lampiran |
| A4 | Lembar Evaluasi Kendala Praktikum dan Tindak Lanjut POB 2025: tanggal evaluasi; pengaduan (deskripsi, sumber laporan, obyek kendala); analisis (kemungkinan penyebab, potensi solusi); tindak lanjut (PIC, tanggal mulai, tanggal selesai, keterangan); ditandatangani Koordinator Prodi, Dosen Koordinator, dan KaLab | POB 2025 lampiran |
| A5 | Pencarian Drive LabFIK tidak menemukan data respons kuesioner kepuasan maupun laporan evaluasinya; yang ditemukan hanya draf (FRM-PRK-06, FRM-PRK-10, DOC 23). Apakah kuesioner POB pernah dijalankan belum diketahui **[KONFIRMASI wawancara P16]** | Pencarian Drive (14 Nov 2026) |
| A6 | Kuesioner POB hanya menyasar praktikan. Instrumen menyebut "pengguna laboratorium", yang juga bisa mencakup dosen, asisten, dan pemakai lab di luar praktikum (PKG-15 A5); populasi sasaran harus ditetapkan (K1) | POB 2025; instrumen |
| A7 | Satu-satunya saluran keluhan yang terekam adalah kolom kendala di laporan sesi asisten (163 dari 1.147 laporan, PKG-16 A4). Itu keluhan asisten tentang sarana, bukan umpan balik pengguna. Saluran keluhan pengguna belum diketahui **[KONFIRMASI wawancara P16]** | Google Form (diolah 14 Nov 2026) |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Kepuasan pengguna laboratorium diukur, dianalisis, dan digunakan untuk perbaikan layanan |
| Penerapan / PJ | Umum / KaLab; GKM |
| Unit | 1 paket dokumen dan rekaman |
| Skor | 4: kriteria 1–4 terpenuhi berurutan · 3: kriteria 1–3, kriteria 4 belum · 2: hanya kriteria 1 atau 1–2, pelaksanaan belum terbukti · 1: kriteria 1 belum terpenuhi atau bukti tidak dapat diverifikasi |
| Referensi instrumen | Pedoman Diklatfung PLP 2022 (pelayanan prima/pengevaluasian), SNI ISO/IEC 17025:2017 8.6.2, Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

Bukti dukung: (1) instrumen survei, (2) populasi/jumlah responden dan *response rate*, (3) rekap hasil, (4) analisis per aspek, (5) keluhan terbuka, (6) RTL.

## 2. Aturan "memenuhi"

Kriteria diperiksa **berurutan** per periode survei. Kriteria berikutnya tidak dihitung bila kriteria sebelumnya belum berbukti. Pola ini memakai `labfik.criteria.mixin` dari Core (`kriteria_tertinggi` {compute}, `get_kriteria(tanggal_acuan)`, `_cek_k1()`–`_cek_k4()`).

| Kriteria | Arti (instrumen) | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| K1 Rencana ditetapkan | Instrumen dan waktu survei serta populasi sasaran ditetapkan | Survei periode ini berstatus *ditetapkan* (penetap, tanggal tetap), punya tanggal buka–tutup, jenis responden sasaran, dan jumlah populasi; tanggal tetap < tanggal buka | Kelayakan instrumen |
| K2 Cakupan dan target | Pertanyaan mencakup alat, bahan, layanan, keselamatan, akses, dan pengalaman belajar; target respons ditetapkan sebelum survei | Setiap aspek dari enam aspek punya ≥1 butir; ada ≥1 butir terbuka (keluhan/saran); target *response rate* terisi sebelum tanggal buka | Kualitas butir |
| K3 Dilaksanakan dan dianalisis | Survei dilaksanakan dan hasil dianalisis dengan jumlah/tingkat respons dilaporkan | Ada respons; jumlah responden dan *response rate* (= responden ÷ populasi) dihitung; rerata per aspek dihitung; kesimpulan analisis terisi | Mutu analisis |
| K4 Ditindaklanjuti dan dibandingkan | Prioritas perbaikan ditetapkan dan efektivitasnya dibandingkan pada periode berikutnya | Ada ≥1 Rencana Tindak Lanjut berprioritas (aspek, tindakan, PIC, tenggat); survei periode berikutnya sudah dianalisis dan setiap RTL diberi penilaian efektivitas berdasarkan perbandingan rerata aspeknya | Kewajaran keputusan efektivitas |

Catatan aturan:
- **K4 baru bisa lengkap pada periode berikutnya.** Pada periode survei pertama, sistem paling tinggi menunjukkan K3 lengkap. Ini sesuai bunyi instrumen, bukan kekurangan sistem.
- **Enam aspek adalah pilihan tetap** (alat, bahan, layanan, keselamatan, akses, pengalaman belajar), bukan master, karena bunyinya ditetapkan instrumen.
- **Respons anonim**: survei tidak meminta nama responden (memperbaiki A3). Identitas cukup jenis responden, MK, dan kelas bila relevan **[USULAN PENULIS]**.
- **Keluhan terbuka** (bukti 5) diambil dari jawaban butir terbuka di survei. Saluran pengaduan tersendiri (ISO 7.9) tidak dirancang, kecuali wawancara menunjukkan lab sudah punya saluran yang perlu direkam **[KONFIRMASI wawancara P16]**.
- **Bahan** tetap ditanyakan walau PKG-17 hanya berlaku terbatas; responden boleh menjawab "tidak relevan" **[USULAN PENULIS]**.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Instrumen survei | 1 | Survei beserta butirnya (dengan aspek), status penetapan |
| Populasi, jumlah responden, *response rate* | 2 | Populasi dan target diisi di survei; responden dan *rate* dihitung |
| Rekap hasil | 3 | Rerata per butir, dihitung |
| Analisis per aspek | 4 | Rerata per aspek dihitung + kesimpulan di Evaluasi Survei |
| Keluhan terbuka | 5 | Jawaban butir terbuka |
| RTL | 6 | Rencana Tindak Lanjut di Evaluasi Survei, termasuk penilaian efektivitasnya |
| Status K1–K4 | — | Dihitung, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Survei** | [T] *extend* `survey.survey` (Odoo CE `survey`, LGPL-3) | 1 survei per periode (bisa per jenis responden) | Bawaan: judul, butir, tanggal, tautan isi. Tambahan: periode, jenis responden sasaran, jumlah populasi, target *response rate*, status penetapan (draf → ditetapkan), penetap, tanggal tetap | Menggantikan Rencana Survei, master Instrumen Survei, dan master Butir Pertanyaan usulan sheet (keputusan 14 Nov 2026) |
| Butir survei | Bawaan `survey.question`, ditambah **aspek** | 1 butir | Teks, tipe jawaban (skala 1–5 / teks), aspek (pilihan tetap enam aspek) | — |
| Respons | Bawaan `survey.user_input` | 1 respons | Jawaban per butir; tanpa nama | Menggantikan Respons Survei di sheet; tidak dihitung sebagai tabel baru |
| **Evaluasi Survei** | [T] | 1 per Survei | Kesimpulan analisis per aspek, tanggal, pengisi (KaLab/GKM). Anak: **Rencana Tindak Lanjut** (aspek, prioritas, tindakan, PIC, tenggat, status, penilaian efektivitas: efektif / belum efektif / belum dinilai, dasar penilaian) | Menggabungkan Analisis Hasil dan Rencana Tindak Lanjut di sheet. Polanya mengikuti Lembar Evaluasi Kendala dan Tindak Lanjut POB 2025 (A4) |
| **Rekap Hasil per Aspek** | [R] | — | Responden, *response rate*, rerata per aspek dan per butir | Bukti 2–4 |
| **Perbandingan Antarperiode** | [R] | — | Rerata per aspek periode ini vs sebelumnya, beserta RTL yang menyasar aspek itu | Dasar penilaian efektivitas (K4) |
| **Status K1–K4** | [R] | — | Kriteria tertinggi yang lengkap secara data | Dari `labfik.criteria.mixin` |

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo.

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-20--evaluasi-20-kepuasan-pengguna) (T 5, M 3, R 2): Rencana Survei, Respons, dan ketiga master digantikan addon `survey`; Analisis Hasil dan RTL digabung menjadi Evaluasi Survei; Keluhan Terbuka diambil dari butir terbuka. RTL tetap kandidat entitas bersama "Tindak Lanjut" (pemetaan bagian 7); bila kelompok menyepakatinya, anak RTL di sini bisa dipindah ke Core.

## 5. Master data

PKG-20 **tidak punya master lokal**.

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Periode | Periode survei dan perbandingan antarperiode | `labfik.periode` (Core) | — |
| Mata Kuliah, Kelas, Ruang Lab | Identitas opsional di respons praktikan | Core | Tidak ditanyakan |
| Personel, Jabatan | Penetap survei, pengisi evaluasi, PIC RTL | `hr.employee`, `hr.job` diperluas | — |
| Aspek | Enam aspek instrumen | **Pilihan tetap**, bukan master | — |

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Periode, Personel, Jabatan | Core | Wajib | — |
| Addon `survey` | Odoo 17 CE (LGPL-3) | Wajib (keputusan 14 Nov 2026) | Survei dijalankan di Google Form; respons diimpor atau dilampirkan, dan rekap dihitung dari impor |
| Jumlah populasi | KaLab (mis. jumlah praktikan per periode dari Kelas di Core) | Wajib untuk *response rate* | Diinput manual |

Tidak bergantung pada package lain. **Keluar:** tidak dipakai package lain.

`labfik_praktikum` akan bergantung pada `survey` selain `labfik_core`. Ini menambah satu dependensi addon bawaan Odoo CE, bukan addon kelompok lain **[KONFIRMASI kelompok]**.

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan K1–K4, jadi tidak dirancang (calon isi batasan masalah):
- Saluran pengaduan tersendiri dengan alur penanganan (ISO 7.9), kecuali wawancara menunjukkan perlu.
- Survei per sesi setelah setiap pertemuan (POB 2025 langkah 11). Cukup satu survei per periode, karena instrumen menilai paket per periode.
- Integrasi dengan survei fakultas atau EDOM.
- Pengingat ke responden dan penutupan survei otomatis.
- Entitas bersama "Tindak Lanjut" lintas indikator (keputusan kelompok).

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 2 (Survei *extend*, Evaluasi Survei) | 0 | 0 | 0 | 1 (penetapan survei) | +2 (Belum ada, A5) | **5** |

Dihitung ulang dari pemetaan (T 5, M 3): tiga master dan dua transaksi ditanggung addon `survey`, dua transaksi digabung.

Ringkasan untuk kolom sheet: Modul `Pelaksanaan Praktikum` · Jenis Skor `Kriteria berurutan` · Unit `paket dokumen per periode` · Sumber `Belum ada` · Status `Belum ada` · Dependensi ID `—` · Eksternal `—` · Level `Semi-otomatis` · Kompleksitas `5`.

## 9. Pertanyaan untuk narasumber

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P16 (KaLab) | A5, A7, keluhan terbuka | Pernah tidaknya mengukur kepuasan (mahasiswa, dosen, asisten); instrumen, waktu, jumlah responden, pemakaian hasil; saluran keluhan dan penanganannya |
| P17 (KaLab) | K1, K2, K4 | Waktu survei, responden, penggabungan dengan survei fakultas/EDOM, dan siapa menindaklanjuti |
| P19 (KaLab) | Rekap | Rekap kepuasan per semester yang dibutuhkan |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] Apakah kuesioner boleh anonim (tanpa nama praktikan)?
- [ ] Berapa target *response rate* yang wajar menurut KaLab?
- [ ] Apakah GKM ikut menganalisis atau menindaklanjuti hasil survei? (GKM disebut sebagai PJ di instrumen)
