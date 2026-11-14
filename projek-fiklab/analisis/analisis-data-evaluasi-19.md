# Analisis Data Indikator Evaluasi 19 (Penilaian Individual Praktikan)

14 November 2026 · Herrens · PKG-19 Evaluasi 19 (penilaian individual praktikan) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab atau dosen; wawancara bagian Pelaksanaan Praktikum belum dijawab.

Analisis awal ada di bagian "Indikator Evaluasi 19" pada `brief-role-3.md` (Febriyan, 26 Oktober 2026, `git show d6fcc5c:projek-fiklab/brief/brief-role-3.md`) dan isian tab *Analysis* baris 54.

**Riwayat keputusan:**
1. Rekap per kelas yang diisi dosen di akhir periode: **ditolak** (dosen tidak realistis mengisinya).
2. Catatan penilaian per sesi di Jurnal Sesi: **diganti**, karena satu sesi belum tentu ada tugas dan tenggat tugas bisa seminggu atau lebih.
3. **Berlaku (Herrens, 14 November 2026):** penilaian praktikan dilihat lewat **tautan eksternal ke LeADS** per kelas (lapis Inti). Bila LeADS punya opsi **ekspor ke Excel**, nilai kelas dapat **diimpor** ke Odoo (lapis Pelengkap) **[ASUMSI: tanpa API]**.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2.

---

## Ringkasan

| | Evaluasi 19 |
|---|---|
| Inti | Setiap praktikan dinilai secara individual dengan rubrik, mendapat umpan balik, dan mendapat remediasi bila perlu |
| PJ (instrumen) | Dosen; asisten |
| Jenis skor | **Persentase** |
| Unit | 1 **praktikan** dalam satu kelas yang dinilai pada periode monev |
| Level cakupan (usulan) | **Bukti tertaut** (Inti): sistem menunjukkan kelas mana yang punya tautan penilaian LeADS dan rubrik; persentase per praktikan ditetapkan penilai setelah membuka LeADS. **Semi-otomatis** bila nilai kelas diimpor (Pelengkap): sistem menghitung persentase per praktikan |
| Posisi dalam dependensi | Hilir; butuh Kelas (Core) dan rubrik di Versi Modul (PKG-15). Tidak bergantung pada Jurnal Sesi |
| Acuan | Standar SPMI UPNVJ 2025 (dukungan capaian pembelajaran). ISO/IEC 17025 tidak mengatur penilaian mahasiswa secara langsung |
| Kompleksitas (kasar) | **5** (rincian di bagian 8) |

**Temuan utama:**
1. **Lab tidak memegang data penilaian sama sekali.** Penilaian dikerjakan dosen di LeADS; formulir asistensi tidak punya kolom nilai, rubrik, atau umpan balik (A1, A2).
2. **Dokumen nyata belum mengatur rubrik, remediasi, maupun moderasi antarpenilai.** Yang ada hanya bobot komponen nilai di template modul (A4).
3. **Penilaian tidak terikat pada satu sesi.** Tugas punya tenggat sendiri dan tidak setiap pertemuan ada tugas, jadi bukti penilaian paling tepat diambil dari tempat nilai disimpan (LeADS), per kelas.
4. **Data per praktikan adalah data pribadi.** Pada lapis Inti sistem tidak menyimpannya sama sekali (cukup tautan). Bila impor dipakai, yang disimpan dibatasi: NIM (tanpa nama) dan status/nilai, dengan akses terbatas.

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

**Lapis Inti: tautan eksternal.** Untuk setiap kelas, dosen (atau laboran) mencatat **Penilaian Kelas**: tautan ke *course* atau *gradebook* LeADS kelas itu, dan catatan moderasi bila penilai lebih dari satu orang. Rubrik diambil dari **Versi Modul** MK itu (PKG-15). Nilai tidak disalin ke Odoo; penilai membuka LeADS lewat tautan.

**Lapis Pelengkap: impor Excel.** Bila LeADS punya opsi ekspor ke Excel, berkas ekspor kelas disusun ke **templat impor baku** lab lalu diimpor **[ASUMSI: tanpa API]**. Isinya satu baris per praktikan: NIM (tanpa nama), jumlah tugas individual dinilai, nilai akhir, ada umpan balik, diremediasi. Templat baku menghindari logika pemetaan kolom yang rumit **[USULAN PENULIS]**.

### Syarat per praktikan

Satu praktikan dihitung **lengkap** bila keempat syarat terpenuhi. **Persentase PKG-19 = Σ praktikan lengkap ÷ Σ praktikan yang dinilai**, untuk semua kelas pada periode monev.

| Syarat | Arti | Cek oleh sistem (Inti: tautan) | Cek oleh sistem (Pelengkap: impor) | Cek oleh penilai |
|---|---|---|---|---|
| P1 Individual | Ada bukti unjuk kerja individu, bukan hanya nilai kelompok | Kelas punya tautan penilaian | Jumlah tugas individual dinilai ≥ 1 | Nilai individual di LeADS |
| P2 Tertelusur ke rubrik | Skor diberikan dengan rubrik | Versi Modul punya berkas rubrik | Sama | Isi rubrik selaras CPMK |
| P3 Umpan balik | Praktikan menerima umpan balik | — | Kolom "ada umpan balik" = ya | Umpan balik di LeADS |
| P4 Remediasi bila perlu | Praktikan di bawah batas lulus mendapat remediasi | — | Bila nilai akhir < batas lulus, "diremediasi" = ya | Bukti remediasi |

Artinya:
- **Tanpa impor**, sistem hanya menghitung **persentase kelas berbukti** (kelas dengan tautan penilaian dan rubrik ÷ seluruh kelas). Persentase per praktikan untuk skor indikator **ditetapkan penilai** setelah memeriksa LeADS. Sistem tidak mengklaim skor PKG-19 dihitung otomatis.
- **Dengan impor**, sistem menghitung persentase per praktikan (P1–P4) untuk kelas yang datanya diimpor.

Catatan aturan:
- Sesi berjenis **UTS** dan **UAS** (pertemuan 8 dan 16) adalah asesmen yang pasti ada; nilainya ada di LeADS, tidak dicatat di jurnal.
- **Batas lulus** mengikuti template modul (60) sampai ada ketentuan prodi; dijadikan pengaturan KaLab **[KONFIRMASI wawancara P14d]**.
- **Akses tautan:** penilai dan KaLab harus bisa membuka *course* LeADS lewat tautan itu **[KONFIRMASI wawancara P15]**; bila tidak bisa, berkas ekspor dilampirkan sebagai cadangan.
- **Data pribadi:** lapis Inti tidak menyimpan data praktikan. Bila impor dipakai, hanya NIM dan status/nilai, tanpa nama; akses: dosen kelas, KaLab, dan pengimpor. Data uji dan demo fiktif.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Rubrik | 1 | Berkas rubrik di Versi Modul (PKG-15) |
| Penilaian individual per kelas | 2, 3 | Tautan LeADS per kelas (Inti); baris nilai per praktikan dan berkas ekspor (Pelengkap) |
| Umpan balik dan remediasi | 4 | Di LeADS (Inti); kolom per praktikan (Pelengkap) |
| Moderasi antarpenilai | 5 | Catatan moderasi per kelas |
| Persentase kelas berbukti; persentase per praktikan (bila diimpor); daftar belum lengkap | — | Dihitung, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Penilaian Kelas** | [T] | 1 per kelas per periode | Kelas, **tautan LeADS** (*course*/*gradebook*), catatan moderasi, pengisi, tanggal; bila diimpor: sumber, berkas ekspor asli, tanggal impor. Anak (hanya bila diimpor): **nilai praktikan** (NIM, jumlah tugas individual dinilai, nilai akhir, ada umpan balik, diremediasi; status lengkap dihitung) | Model usulan `labfik.praktikum.penilaian` (+ `.baris`). Impor ulang mengganti baris kelas itu, dengan riwayat |
| **Daftar Belum Lengkap** | [R] | — | Kelas tanpa tautan penilaian, kelas tanpa rubrik; bila diimpor, praktikan yang gagal P1–P4 | Dasar tindak lanjut |
| **Rekap PKG-19 per Periode** | [R] | — | Persentase kelas berbukti; persentase per praktikan untuk kelas yang diimpor | — |

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo.

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-19--evaluasi-19-penilaian-individual-praktikan) ("«extend» Jurnal Sesi: tautan bukti penilaian (LeADS)"): pendekatan tautan LeADS dipertahankan, tetapi tautannya **per kelas**, bukan per sesi, dan ditambah impor sebagai lapis Pelengkap.

## 5. Master data

Semua master **di-*import* dari Core**. PKG-19 tidak punya master lokal.

| Master | Dipakai untuk | Sumber (Core) | Bila belum tersedia |
|---|---|---|---|
| Periode | Batas periode monev | `labfik.periode` | Periode monev = semester **[ASUMSI]** |
| Mata Kuliah, Kelas | Satuan penilaian; rubrik lewat Versi Modul | `labfik.mata.kuliah`, `labfik.kelas` | — |
| Personel | Pengisi tautan, pengimpor, dosen kelas | `hr.employee` diperluas | — |

Master **Mahasiswa tidak dipakai**. Bila impor dipakai, praktikan cukup dicatat dengan NIM pada baris nilai per kelas.

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Kelas | Core (diisi lewat PKG-15) | Wajib | — |
| Rubrik di Versi Modul | PKG-15 Persiapan 15 (modul) | Wajib untuk P2 | Rubrik diunggah di Penilaian Kelas |
| Tautan *course*/*gradebook* LeADS | LeADS (eksternal), dosen pengampu | Wajib (Inti) | Berkas ekspor dilampirkan |
| Ekspor Excel LeADS | LeADS (eksternal) | Opsional (Pelengkap) | Tetap memakai tautan saja |

Dependensi ke PKG-18 (Jurnal Sesi) **dilepas**. **Keluar:** tidak dipakai package lain.

**Risiko:** apakah penilai dan KaLab bisa membuka *course* LeADS lewat tautan, dan apakah LeADS punya opsi ekspor Excel, belum diketahui **[KONFIRMASI wawancara P15]**.

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan P1–P4, jadi tidak dirancang (calon isi batasan masalah):
- Integrasi API dengan LeADS atau SIAKAD; pemetaan kolom ekspor otomatis.
- Rincian nilai per tugas dan rubrik terstruktur per kriteria.
- Nama praktikan dan master Mahasiswa.
- Alur remediasi (penjadwalan dan penilaian ulang).
- Analisis ketercapaian CPMK per MK (baris Evaluasi 19 yang lain; bukan lingkup proyek).

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 1 (Penilaian Kelas) | 0 | 1 (PKG-15, rubrik) | 1 (LeADS) | 0 | +2 (Belum ada di lab) | **5** |

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `praktikan per kelas` · Sumber `LeADS (tautan; impor Excel bila ada)` · Status `Belum ada` (di lab) · Dependensi ID `Persiapan 15 (modul)` · Eksternal `LeADS` · Level `Bukti tertaut` (semi-otomatis bila diimpor) · Kompleksitas `5`.

## 9. Pertanyaan untuk narasumber

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P14a–d (KaLab) | P1–P4 | Komponen nilai dan rubrik; siapa penilai; di mana nilai dicatat; nilai individu vs kelompok; remediasi; batas lulus |
| P15 (KaLab) | Tautan dan impor | Bukti apa yang realistis disimpan sistem lab: tautan LeADS, atau ekspor nilai; siapa mengisi dan kapan |
| P19 (KaLab) | Akses | Siapa boleh melihat data nilai |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] Apakah LeADS punya opsi ekspor *gradebook* ke Excel? Apakah ekspor memuat kolom umpan balik dan item remedial?
- [ ] Apakah KaLab dan penilai monev bisa membuka *course* praktikum di LeADS lewat tautan?
- [ ] Apakah asisten ikut memberi nilai atau umpan balik (moderasi)?
