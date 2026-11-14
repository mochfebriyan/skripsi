# Analisis Data Indikator Evaluasi 19 (Penilaian Individual Praktikan)

14 November 2026 · Herrens · PKG-19 Evaluasi 19 (penilaian individual praktikan) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab atau dosen; wawancara bagian Pelaksanaan Praktikum belum dijawab.

Analisis awal ada di bagian "Indikator Evaluasi 19" pada `brief-role-3.md` (Febriyan, 26 Oktober 2026, `git show d6fcc5c:projek-fiklab/brief/brief-role-3.md`) dan isian tab *Analysis* baris 54. Dokumen ini melanjutkan pendekatannya, yaitu bukti penilaian ditempel **per sesi** di Jurnal Sesi PKG-18, lalu menambah dua hal: rubrik diambil dari Versi Modul PKG-15, dan cara menghitung unit praktikan dari data per sesi.

**Keputusan (Herrens, 14 November 2026):** penilaian dicatat **per sesi**, bukan rekap per kelas di akhir periode. Alasannya: dosen tidak realistis mengisi rekap di akhir semester, sedangkan jurnal sesi sudah diisi di setiap sesi.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2. Rujukan "PKG-18 A8" berarti temuan A8 di [analisis-data-proses-18.md](analisis-data-proses-18.md).

---

## Ringkasan

| | Evaluasi 19 |
|---|---|
| Inti | Setiap praktikan dinilai secara individual dengan rubrik, mendapat umpan balik, dan mendapat remediasi bila perlu |
| PJ (instrumen) | Dosen; asisten |
| Jenis skor | **Persentase** |
| Unit | 1 **praktikan** yang dinilai pada periode monev (berbeda dari PKG-15 dan PKG-18 yang menghitung sesi) |
| Level cakupan (usulan) | **Bukti tertaut**. Sistem menghitung persentase **pendekatan** dari catatan penilaian per sesi; kebenarannya diverifikasi penilai lewat tautan bukti. Skor **tidak** diklaim dihitung otomatis |
| Posisi dalam dependensi | Paling hilir; butuh Jurnal Sesi (PKG-18) dan Versi Modul (PKG-15) |
| Acuan | Standar SPMI UPNVJ 2025 (dukungan capaian pembelajaran). ISO/IEC 17025 tidak mengatur penilaian mahasiswa secara langsung |
| Kompleksitas (kasar) | **4** (rincian di bagian 8) |

**Temuan utama:**
1. **Lab tidak memegang data penilaian sama sekali.** Penilaian dikerjakan dosen di LeADS; formulir asistensi tidak punya kolom nilai, rubrik, atau umpan balik (A1, A2).
2. **Dokumen nyata belum mengatur rubrik, remediasi, maupun moderasi antarpenilai.** Yang ada hanya bobot komponen nilai di template modul (A4).
3. **Data per praktikan adalah data pribadi.** Sistem lab cukup mencatat **jumlah** praktikan per sesi asesmen beserta tautan buktinya, bukan nilai per mahasiswa. Konsekuensinya, persentase per praktikan hanya bisa didekati (bagian 2).

---

## 0. Sumber dan temuan *as-is*

### Dokumen dan data yang dipakai

| Sumber | Sifat | Tanggal | Yang relevan untuk PKG-19 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`) | **Nyata**, belum disahkan | 2025 | Kualifikasi pelaksana, langkah 10, daftar pencatatan, Template Modul bagian 9–10 |
| Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" (Responses) | **Data nyata** (tidak dikutip per baris) | Diolah 14 Nov 2026 (1.147 laporan) | Ada tidaknya data penilaian |
| `brief-role-3.md` (commit `d6fcc5c`) dan brief bersama | Catatan kelompok | 17–26 Okt 2026 | Penilaian di LeADS, presensi rinci di SIMPEL |
| Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (TPL-PRK-02 Template Laporan Praktikum Mahasiswa) | **Draf**, kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep–Okt 2026 | Contoh format saja |
| Paket Dokumen Monev `DOCUMENTS/20_Pedoman_Penilaian_CPMK_Remediasi`, `21_Formulir_Data_Praktikum_Penilaian`, `22_Workbook_Data_Praktikum_CPMK` | **Draf GPT** | Okt 2026 | Contoh format saja |

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | Penilaian praktikan (tugas, nilai, umpan balik) dikerjakan dosen di **LeADS**; presensi rinci per praktikan di **SIMPEL**. Keduanya tidak terhubung ke rekaman sesi lab. Fitur rubrik LeADS, tautan per aktivitas, dan hak akses KaLab belum diketahui | Brief bersama dan `brief-role-3.md` **[KONFIRMASI wawancara P14, P15]** |
| A2 | Formulir asistensi **tidak punya kolom** nilai, rubrik, atau umpan balik. Hanya 58 dari 1.147 laporan yang topiknya menyebut asesmen (kuis 48, tugas 6, ujian/responsi 4), dan tidak satu pun menyebut remedial | Google Form (diolah 14 Nov 2026) |
| A3 | POB 2025 menetapkan dosen pengampu "menilai hasil akhir mahasiswa"; asisten "membantu pelaksanaan praktikum, termasuk pembimbingan". Daftar pencatatan POB memuat "Laporan Hasil Praktikum" (hasil pekerjaan atau penilaian mahasiswa) | POB 2025, kualifikasi pelaksana dan pencatatan |
| A4 | Template Modul POB 2025 bagian 10 hanya memuat bobot komponen: keaktifan dan partisipasi 20%, hasil praktikum 30%, laporan praktikum 50%, nilai lulus minimal 60. **Tidak ada rubrik per kriteria, ketentuan remediasi, maupun moderasi antarpenilai.** Bagian 9 meminta laporan per mahasiswa (berkas bernama NIM dan nama), jadi laporan bersifat individual | POB 2025, lampiran Template Modul |
| A5 | Langkah 10 POB 2025 tidak konsisten: di diagram berbunyi "Melakukan penilaian praktikum" (dokumen: Formulir Evaluasi Asistensi Praktikum), tetapi di penjelasan berbunyi "Melakukan evaluasi praktikum: asisten mengisikan presensi pelaksanaan dan kendala". Tidak ada formulir penilaian praktikan yang dilampirkan | POB 2025 langkah 10 |
| A6 | Kuesioner peserta POB 2025 butir 7 menanyakan apakah asisten "memberikan umpan balik yang membangun setelah praktikum". Ini satu-satunya jejak umpan balik di dokumen nyata, dan sifatnya persepsi praktikan, bukan rekaman umpan balik | POB 2025, Formulir Kuesioner Peserta Praktikum |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Kompetensi praktikan dinilai secara individual melalui rubrik dan bukti unjuk kerja yang sesuai CPMK |
| Penerapan / PJ | Umum / Dosen; asisten |
| Unit | 1 praktikan |
| Pembilang | Jumlah praktikan yang memiliki penilaian individual lengkap sesuai rubrik dan umpan balik |
| Pembagi | Seluruh praktikan yang dinilai pada periode monev |
| Memenuhi bila | Bukti menunjukkan kemampuan individu; skor dapat ditelusuri ke rubrik; remediasi tersedia bila diperlukan; nilai kelompok tidak menjadi satu-satunya bukti kompetensi individu |
| Skor | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan → 1 |
| Referensi instrumen | Standar SPMI UPNVJ 2025 (dukungan capaian pembelajaran), usulan akademik internal, Dokumen ISO UPNVJ |

Bukti dukung: (1) rubrik keterampilan/produk, (2) hasil observasi individual, (3) portofolio, (4) umpan balik dan remediasi, (5) moderasi penilaian antarpenilai.

**Bukan lingkup PKG-19:** baris instrumen lain yang juga bernomor Evaluasi 19, "Ketercapaian CPMK praktikum dianalisis untuk seluruh mata kuliah" (PJ: Dosen, Koor Prodi, GKM). Baris itu tidak termasuk 21 indikator proyek.

## 2. Aturan "memenuhi"

### Cara mencatat

Penilaian dicatat **di sesi tempat asesmen terjadi**, sebagai bagian dari Jurnal Sesi PKG-18. Pengisi jurnal yang sama (asisten, dosen, atau laboran; lihat PKG-18) menambahkan satu **catatan penilaian** bila sesi itu berisi asesmen. Rubrik tidak diunggah ulang di setiap sesi, tetapi diambil dari **Versi Modul** yang dipakai sesi itu (PKG-15), karena template modul sudah punya bagian penilaian (A4).

### Syarat per sesi asesmen

| Syarat | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| P1 Individual | Asesmen menghasilkan bukti unjuk kerja per individu, bukan hanya nilai kelompok | Bentuk asesmen = individual, atau kelompok **dengan** komponen individual | Contoh bukti di tautan |
| P2 Tertelusur ke rubrik | Skor diberikan dengan rubrik | Versi Modul yang dipakai sesi itu punya rubrik terlampir | Isi rubrik selaras CPMK |
| P3 Umpan balik | Praktikan menerima umpan balik atas hasil kerjanya | Jumlah praktikan menerima umpan balik terisi | Contoh umpan balik di tautan |
| P4 Remediasi bila perlu | Praktikan di bawah batas lulus mendapat kesempatan remediasi | Bila jumlah "perlu remediasi" > 0, jumlah "diremediasi" terisi sebelum periode ditutup | Bukti remediasi |

Bila penilai lebih dari satu orang (dosen dan asisten), catatan **moderasi** wajib terisi (bukti 5).

### Cara menghitung persentase (pendekatan)

Data per sesi berupa **jumlah**, bukan daftar nama. Karena itu sistem tidak bisa memastikan bahwa praktikan yang sama sudah lengkap di semua asesmen. Persentase indikator didekati dengan:

**Persentase PKG-19 ≈ Σ praktikan dinilai lengkap (P1–P4) ÷ Σ praktikan hadir**, dijumlahkan atas semua sesi asesmen pada periode monev.

- Jumlah hadir diambil dari Jurnal Sesi PKG-18; praktikan yang tidak hadir di sesi asesmen tidak terhitung di sesi itu.
- **Ini bukan hitungan per praktikan yang tepat.** Hitungan tepat butuh presensi dan status penilaian per nama, yang ditunda (bagian 7). Penggunaan pendekatan ini perlu disetujui pembimbing **[KONFIRMASI pembimbing]**.
- Kelas yang tidak punya satu pun sesi asesmen ditampilkan di Daftar Kelas Tanpa Bukti Penilaian, karena praktikannya tidak terhitung sama sekali.

Catatan aturan:
- Sistem **tidak** memeriksa kebenaran angka; penilai memverifikasi lewat tautan bukti. Ini alasan level cakupannya **bukti tertaut**.
- Batas lulus mengikuti template modul (60) sampai ada ketentuan prodi **[KONFIRMASI wawancara P14d]**.
- Tautan LeADS butuh akses penilai ke *course* terkait **[KONFIRMASI]**; berkas unggahan disediakan sebagai cadangan.
- Sesi mana yang wajib berisi asesmen ditentukan dosen di modul. Sistem tidak memaksakannya.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Rubrik | 1 | Lampiran di Versi Modul (PKG-15) |
| Catatan penilaian per sesi asesmen | 2, 3 | Jenis dan bentuk asesmen, jumlah dinilai dan lengkap, tautan bukti (observasi, laporan, portofolio) |
| Umpan balik dan remediasi | 4 | Jumlah menerima umpan balik, perlu remediasi, dan diremediasi |
| Moderasi antarpenilai | 5 | Catatan moderasi bila penilai lebih dari satu |
| Persentase PKG-19 dan daftar kelas tanpa bukti penilaian | — | Dihitung dari catatan penilaian, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Catatan Penilaian Sesi** | [T] anak Jurnal Sesi (PKG-18) | 1 per asesmen dalam satu sesi | Jenis asesmen (kuis, tugas, observasi, laporan, ujian praktik), bentuk (individual / kelompok dengan komponen individual / kelompok saja), penilai, jumlah praktikan dinilai, jumlah lengkap (P1–P4), jumlah menerima umpan balik, jumlah perlu remediasi, jumlah diremediasi, tautan atau berkas bukti, catatan moderasi | Ditulis di dalam induknya (pedoman bagian 4a), jadi tidak dihitung sebagai tabel terpisah. Tidak menyimpan nilai per mahasiswa |
| Rubrik pada **Versi Modul** | Atribut [T] milik PKG-15 | — | Berkas rubrik | Tambahan kecil pada Versi Modul PKG-15 |
| **Daftar Kelas Tanpa Bukti Penilaian** | [R] | — | Kelas tanpa sesi asesmen, sesi asesmen tanpa rubrik, atau dengan remediasi tertunda | Dasar tindak lanjut |
| **Rekap PKG-19 per Periode** | [R] | — | Persentase pendekatan per kelas, per MK, dan total | Persentase indikator |

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo.

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-19--evaluasi-19-penilaian-individual-praktikan): pendekatannya sama ("«extend» Jurnal Sesi: tautan bukti penilaian"), diperinci menjadi catatan penilaian berisi jumlah dan syarat P1–P4, ditambah rubrik di Versi Modul dan cara menghitung praktikan.

## 5. Master data

Semua master **di-*import* dari Core** (melalui Sesi dan Jurnal Sesi). PKG-19 tidak punya master lokal.

| Master | Dipakai untuk | Sumber (Core) | Bila belum tersedia |
|---|---|---|---|
| Periode | Batas periode monev | `labfik.periode` | Periode monev = semester **[ASUMSI]** |
| Mata Kuliah, Kelas | Pengelompokan rekap | `labfik.mata.kuliah`, `labfik.kelas` | — |
| Personel | Penilai (dosen, asisten) | `hr.employee` diperluas | — |

Mahasiswa **tidak** dipakai, karena catatan penilaian tidak menyimpan data per praktikan.

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Jurnal Sesi dan jumlah praktikan hadir | PKG-18 Proses 18 (sesi terlaksana) | **Wajib** | Tidak ada tempat mencatat penilaian |
| Rubrik di Versi Modul | PKG-15 Persiapan 15 (jadwal dan modul) | Wajib untuk P2 | Rubrik diunggah di catatan penilaian sesi |
| Nilai, umpan balik, bukti kerja | LeADS (eksternal), dosen pengampu | Wajib untuk verifikasi | Berkas diunggah langsung |

**Keluar:** tidak dipakai package lain.

**Risiko:** pengisi catatan penilaian sama dengan pengisi Jurnal Sesi. Bila jurnal diisi asisten, kelas tanpa asisten (42–56% kelas; PKG-18 A1) tidak punya pengisi, sehingga PKG-19 ikut bergantung pada jawaban "siapa mengisi jurnal kelas tanpa asisten" **[KONFIRMASI wawancara P10, P13]**.

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan P1–P4 dengan level bukti tertaut, jadi tidak dirancang (calon isi batasan masalah):
- Presensi dan status penilaian **per praktikan** (yang membuat hitungan per praktikan menjadi tepat).
- Penyimpanan nilai, rubrik terstruktur per kriteria, dan perhitungan nilai di Odoo.
- Integrasi atau impor otomatis dari LeADS (API atau ekspor *gradebook*).
- Rekap penilaian per kelas di akhir periode oleh dosen (alternatif yang ditolak, 14 Nov 2026).
- Analisis ketercapaian CPMK per MK (baris Evaluasi 19 yang lain; bukan lingkup proyek).
- Alur remediasi (penjadwalan dan penilaian ulang). Cukup jumlah dan bukti.

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 0 (catatan penilaian adalah anak Jurnal Sesi) | 0 | 1 (PKG-18) | 1 (LeADS) | 0 | +2 (Belum ada di lab) | **4** |

Analisis awal menghitung 3 karena status data dianggap "ada" (LeADS). Dari sisi lab, data penilaian ternyata belum ada sama sekali (A1, A2).

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `praktikan` · Sumber `LeADS (dosen)` · Status `Belum ada` (di lab) · Dependensi ID `Proses 18 (sesi)` · Eksternal `LeADS` · Level `Bukti tertaut` · Kompleksitas `4`.

## 9. Pertanyaan untuk narasumber

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P14a–d (KaLab) | P1–P4 | Komponen nilai dan ada tidaknya rubrik per CPMK; siapa penilai dan cara menyamakan penilaian; di mana nilai dicatat; nilai individu vs kelompok; remediasi |
| P15 (KaLab) | Tautan bukti, pengisi | Bukti apa yang realistis disimpan sistem lab; siapa mengunggah dan kapan |
| P10, P13 (KaLab, laboran) | Pengisi catatan penilaian | Siapa mengisi jurnal sesi, termasuk kelas tanpa asisten |
| P19 (KaLab) | Akses | Siapa boleh melihat data penilaian |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] Apakah asisten ikut memberi nilai atau umpan balik? Bila ya, bagaimana penilaiannya disamakan dengan dosen (moderasi)?
- [ ] Apakah KaLab atau penilai monev bisa membuka *course* praktikum di LeADS? Apakah ada tautan per tugas/kuis yang bisa disalin ke jurnal sesi?
- [ ] Apakah dosen bersedia melampirkan rubrik saat menerbitkan modul?

Pertanyaan untuk **pembimbing**: apakah persentase pendekatan (jumlah penilaian lengkap ÷ jumlah praktikan hadir di sesi asesmen) dapat diterima sebagai bukti untuk unit "praktikan"? **[KONFIRMASI pembimbing]**
