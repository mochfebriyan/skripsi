# Analisis Data Indikator Pengelolaan 4 (penugasan petugas sesuai kompetensi)

14 November 2026 · Zahir · PKG-04 · Bagian dari proyek LabFIK Compliance · Modul: SDM & Kompetensi (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (prasyarat rancangan); bahan Bab I dan 2.2. Belum ada hasil wawancara: pertanyaan untuk KaLab dan laboran sudah disiapkan di lembar "Wawancara FIKLAB Compliance" (Drive proyek, bagian SDM & Kompetensi no. 1–15), tetapi belum dijawab.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2: **target → aturan memenuhi → luaran → transaksi → master → dependensi → ditunda → pertanyaan narasumber**. Package lain di modul ini: PKG-10 Pengelolaan 10 (otorisasi) dan PKG-14 Pengembangan 14 (pelatihan PLP/laboran), dianalisis terpisah.

---

## 0. Sumber yang dipakai

| Sumber | Sifat | Dipakai untuk |
|---|---|---|
| Instrumen Monev Laboratorium UPNVJ 2026 v1.1, tab *Analysis* baris ID 4 | **Acuan resmi** | Target, kriteria, bukti dukung, usulan entitas awal |
| SNI ISO/IEC 17025:2017 klausul 6.2 ([docs](../docs/SNI%20ISO-IEC%2017025-2017_ID.md)) | **Acuan resmi** | Persyaratan kompetensi, seleksi, supervisi, otorisasi |
| `LABFIK_POB_Praktikum.pdf`: POB Manajemen Praktikum dan Asistensi FIK 2025 (Drive proyek) | **Nyata**, belum bernomor dan belum disahkan (kolom nomor, tanggal efektif, dan pengesahan kosong) | Alur as-is: alokasi, rekrutmen, seleksi, kontrak, alokasi jadwal asisten; formulir yang ada |
| Spreadsheet "Alokasi Pertemuan Asisten Praktikum" dan "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ (Responses)" (milik akun LabFIK) | **Data nyata**, berisi data pribadi: hanya struktur dan jumlah yang dikutip | Dibedah dan dihitung penuh di [bedah-dokumen-sdm.md](bedah-dokumen-sdm.md) (D2, D3; temuan A6–A9, A11–A12, A18–A19) |
| Slide PKKMB FIK dan SK SOTK FIK 2025 (baris 8–9 `ISO_LAB_SI`) | **Nyata** | Laboran per ruang (A10); jabatan lab di SK (A17). Lihat bedah dokumen D8a, D8b |
| [kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md) | Draf Langkah 3 | Pemakaian Core; Surat Tugas bergaris (K-6); Kelas/MK/Sesi di Core (K-5) |
| Paket Manajemen Praktikum LABFIK 2026 (STD-PRK-03, FRM-PRK-02, RUB-PRK-01, FRM-PRK-09, FRM-PRK-10) | **Draf** (README: "DRAFT", pengembangan dari POB 2025); diduga hasil GPT **[VALIDASI]** | Contoh format saja |
| Paket Dokumen Monev `07_SOP_Kompetensi_Penugasan_Otorisasi`, `09_Formulir_…`, `10_Workbook_…` (folder DOCUMENTS) | **Draf GPT** (status "Templat contoh") | Contoh format saja; tidak menjadi sumber kebutuhan |
| Draf pendahuluan penulis ("[SKRIPSI] Pendahuluan Zahir", 11 November 2026) | Tulisan penulis, sebagian klaim masih bertanda konfirmasi | Masalah, batasan, temuan as-is |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Seluruh sesi praktikum memiliki laboran/PLP dan asisten bila diperlukan yang ditugaskan sesuai kompetensi minimum |
| Penerapan / PJ | Umum / KaLab; Koor Prodi |
| Unit | **1 sesi praktikum** yang dilaksanakan pada periode monev |
| Jenis skor | **Persentase** (100% unit yang memenuhi) |
| Skor | 4: 100% sesi memenuhi dan bukti dapat diverifikasi · 3: 90% sampai <100% · 2: 70% sampai <90% · 1: <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan |
| Level cakupan (usulan) | **Otomatis** untuk persentase; keabsahan bukti tetap diperiksa penilai |
| Acuan | SNI ISO/IEC 17025:2017 6.2 · Pedoman Diklatfung PLP 2022 (kompetensi teknis) · usulan internal nilai asisten |

Bukti dukung: (1) daftar sesi dan petugas, (2) surat tugas, (3) matriks kompetensi, (4) ijazah/pelatihan/sertifikat relevan sesuai jabatan dan risiko, (5) hasil uji keterampilan, (6) KHS asisten (nilai mata kuliah terkait minimal 70 sebagai usulan kebijakan internal), (7) bukti orientasi dan supervisi.

**Rumus:** pembilang = jumlah sesi yang seluruh kebutuhan petugasnya terpenuhi dan kompetensinya terverifikasi; penyebut = seluruh sesi praktikum yang **dilaksanakan** pada periode monev.

## 2. Aturan "memenuhi"

Instrumen menyebut empat syarat per sesi. Sistem bisa memeriksa kelengkapan datanya; kebenaran isi bukti tetap diperiksa penilai.

| Syarat | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| S1 Kebutuhan ditetapkan | Jumlah dan jenis petugas yang dibutuhkan (laboran/PLP, asisten) ditetapkan menurut risiko/beban kerja | Kelas (atau sesi) punya **kebutuhan petugas**: jumlah minimal per peran | Apakah dasar penetapannya wajar |
| S2 Penugasan sah | Petugas ditugaskan oleh pihak berwenang | Setiap kebutuhan terisi oleh **baris Surat Tugas** yang suratnya berstatus *disahkan* dan rentang berlakunya mencakup tanggal sesi. Asisten dicocokkan lewat kelas sesi; laboran lewat **ruang** sesi | Keabsahan surat tugas |
| S3 Kompetensi terbukti | Kompetensi petugas dibuktikan dengan pendidikan, pelatihan, pengalaman, dan/atau demonstrasi | Setiap petugas punya **bukti kompetensi** untuk semua kompetensi yang disyaratkan peran/jabatannya, dan bukti masih berlaku pada tanggal sesi | Keaslian dan relevansi bukti |
| S4 Asisten memenuhi syarat internal | Asisten lolos seleksi untuk mata kuliah tersebut (mis. nilai MK minimal) | Asisten punya **hasil seleksi lulus** untuk mata kuliah kelas itu, **atau** pengecualian yang disetujui pihak berwenang | Kewajaran pengecualian |

Catatan:
- "Sertifikasi khusus wajib hanya jika dipersyaratkan untuk tugasnya." Jadi syarat kompetensi diatur per peran/jabatan, bukan seragam untuk semua orang.
- **Bukti 7 (orientasi dan supervisi)** tidak muncul di kalimat "unit dinyatakan memenuhi", tetapi diminta sebagai bukti dukung. **Keputusan sementara (Zahir, 14 November 2026):** dicatat sebagai rekaman pendukung (lapis Pelengkap) dan **tidak** menjadi syarat persentase **[KONFIRMASI pembimbing]**.
- Kelas yang memang tidak membutuhkan asisten: kebutuhan asisten = 0, sehingga sesi tetap bisa memenuhi. Ini menjawab masalah "42–56% kelas tanpa alokasi asisten tidak bisa dibedakan antara tidak butuh atau belum terpenuhi".

## 3. Luaran

| Luaran | Bukti ke- | Jenis | Keterangan |
|---|---|---|---|
| Daftar Sesi dan Petugas | 1 | [R] | Per sesi: kebutuhan, petugas, status S1–S4, memenuhi/tidak |
| Surat Tugas | 2 | **[T]** + berkas | Dokumen bergaris yang disahkan (keputusan 14 Nov 2026, kontrak Core K-6); berkas bertanda tangan diunggah. Sebelumnya ditulis [R] |
| Matriks Kompetensi | 3 | [R] | Personel × kompetensi, dihasilkan dari bukti kompetensi. Dipakai juga PKG-14 |
| Bukti kompetensi (ijazah/sertifikat/pelatihan) | 4 | Lampiran di [T] Bukti Kompetensi | — |
| Hasil uji keterampilan | 5 | Bagian dari [T] Seleksi Kompetensi | — |
| KHS asisten (nilai MK terkait) | 6 | Bagian dari [T] Seleksi Kompetensi | **Data pribadi**: cukup nilai yang dipersyaratkan + lampiran terbatas akses |
| Bukti orientasi dan supervisi | 7 | [T] Orientasi/Supervisi (lapis Pelengkap, lihat bagian 2) | — |
| Persentase PKG-04 per periode | — | [R] | Dihitung dari Daftar Sesi dan Petugas |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Kebutuhan Petugas** | 1 kelas × 1 peran per periode | kelas, peran (laboran/PLP, asisten), jumlah minimal, dasar penetapan (teks), penetap | Bisa juga anak dari Kelas. Lebih sederhana daripada per sesi **[ASUMSI]** |
| **Seleksi Kompetensi** | 1 asisten × 1 mata kuliah per periode | personel (asisten), mata kuliah, nilai MK, hasil uji keterampilan/wawancara (skor), keputusan (lulus / lulus dengan pengecualian), alasan pengecualian, penyetuju pengecualian, berkas | Per mata kuliah, karena asisten memilih MK saat mendaftar. Pendaftaran tidak dibangun ulang (batasan pendahuluan). **Hanya calon yang lulus** (termasuk dengan pengecualian) yang dicatat; Personel asisten dibuat saat itu (keputusan Zahir, 14 November 2026). **Dipisah** dari Asesmen Keterampilan PKG-10: unit, waktu, dan pesertanya berbeda. Keduanya boleh menghasilkan Bukti Kompetensi |
| **Bukti Kompetensi** | 1 bukti × 1 personel × 1 kompetensi | personel, kompetensi, jenis bukti (pendidikan/pelatihan/pengalaman/demonstrasi), nomor dokumen, berlaku sampai; tanggal, pelapor, berkas, keterangan diwarisi dari `labfik.evidence.mixin` | Sumber Matriks Kompetensi. Juga diisi oleh realisasi pelatihan PKG-14 dan asesmen PKG-10 |
| **Surat Tugas** | 1 surat per periode (atau per gelombang) | periode, nomor, berkas bertanda tangan; status, pengesah, riwayat dari `labfik.approval.mixin` | **Bergaris** (keputusan Zahir, 14 November 2026; kontrak Core K-6): disahkan sekali untuk semua barisnya. Pola sama dengan SK Penetapan Tata Kelola |
| **Penugasan Petugas** (baris Surat Tugas) | 1 personel × 1 sasaran × 1 peran | personel, peran (asisten/laboran), sasaran: **kelas** (asisten) atau **ruang** (laboran), `berlaku_mulai`, `berlaku_sampai` | Asisten **per kelas** (asisten memilih kelas setelah lulus seleksi MK). Laboran **per ruang** (bedah dokumen A10) **[KONFIRMASI K3]**. Rentang berlaku karena asisten tidak selalu mulai di pertemuan 1 (A6). Pengganti di tengah semester: revisi surat atau surat tambahan (Pelengkap). Siapa yang mengesahkan **[KONFIRMASI K7]** |
| **Komitmen Petugas** | 1 personel per periode | berkas pernyataan | Sheet: "Komitmen Petugas Praktikum"; POB 2025: "kontrak asisten". Cukup berkas lampiran di Surat Tugas (Pelengkap) |
| **Orientasi/Supervisi** | 1 kegiatan | jenis (orientasi/supervisi), personel, pelaksana, tanggal, catatan, bukti | Bukti 7. Lapis Pelengkap |

Sheet juga menyebut "Petugas (Master)" dan "Petugas (Transaksi)". Orangnya cukup master **Personel** (`hr.employee` di Core), sedangkan petugas per kelas/sesi menjadi **Penugasan Petugas [T]**, sesuai catatan di [pemetaan](pemetaan-package-instrumen.md).

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Personel | Petugas, asisten, penetap, penyetuju | Core: `hr.employee`. Asisten: `jenis_personel` = asisten, Jabatan = Asisten Praktikum; dibuat saat lulus seleksi. Laboran: `jenis_personel` = laboran_plp | Data contoh fiktif |
| Jabatan | Peran petugas dan syarat kompetensinya; siapa berwenang mengesahkan Surat Tugas | Core: `hr.job` diperluas | — |
| **Kompetensi** | Jenis kompetensi/sertifikasi yang disyaratkan | **Milik PKG-04** (dipakai 10 dan 14) | — |
| Syarat kompetensi per jabatan | Kompetensi minimum yang wajib dimiliki tiap jabatan. Untuk Asisten Praktikum hanya syarat umum; syarat per MK dicek lewat Seleksi | `syarat_kompetensi_ids` ditambahkan `labfik_sdm` ke `hr.job`, berdampingan dengan field teks Core `syarat_kompetensi` (kontrak Core K-1) | — |
| Ruang | Sasaran penugasan laboran; ruang sesi | Core: `labfik.ruang` | — |
| Mata Kuliah, Kelas | Kebutuhan petugas, seleksi asisten per MK, penugasan asisten | **Core** (keputusan Zahir, 14 Nov 2026; tanpa OpenEduCat) **[KONFIRMASI Herrens, Febriyan]** | Data contoh |
| Sesi | Unit penilaian | **Core** (satu-satunya transaksi di Core), dibangkitkan PKG-15 | Data contoh |
| Periode | Periode monev, semester | Core: `labfik.periode` | — |

**Struktur kompetensi (keputusan Zahir, 14 November 2026):** Kompetensi adalah **master sendiri**, bukan perluasan Jabatan atau Personel. Jabatan dan Personel hanya diberi tautan:

| Bagian | Jenis | Isi |
|---|---|---|
| Kompetensi | [M] baru | Jenis kompetensi/sertifikasi (mis. "Pemrograman Python", "Administrasi jaringan", "Diklatfung PLP") |
| Syarat kompetensi | Tautan di Jabatan | Kompetensi minimum yang wajib dimiliki pemegang jabatan/peran |
| Bukti Kompetensi | [T] milik Personel | Kompetensi yang dimiliki seseorang, beserta berkas dan masa berlakunya |
| Matriks Kompetensi | [R] | Bukti dibandingkan dengan syarat jabatan; tidak diinput |

Addon `hr_skills` (Odoo CE) tidak dipakai **[VALIDASI]**: setahu penulis addon ini memakai level keahlian dan tidak menyimpan berkas bukti maupun masa berlaku, padahal keduanya dibutuhkan untuk monev. Model sendiri yang mewarisi `labfik.evidence.mixin` lebih sederhana dan sekaligus menunjukkan inheritance.

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Sesi bertanggal (kelas, tanggal, pertemuan, ruang) | Model Sesi di Core, dibangkitkan PKG-15 (Herrens) | **Wajib** | Sesi contoh dibangkitkan dari data uji |
| Status "sesi terlaksana" (penyebut) | `state` Sesi di Core, diisi PKG-18 (Herrens) | **Wajib** untuk penyebut | Semua sesi terjadwal yang tanggalnya sudah lewat dianggap terlaksana **[ASUMSI]** |
| Personel, Jabatan, Ruang | Core | Wajib | Data contoh |
| Kompetensi hasil pelatihan | PKG-14 (modul sendiri) | Opsional | Bukti kompetensi diinput manual |
| Hasil pendaftaran asisten | Modul pendaftaran (acuan Anandar 2026, `skripsi_rafika/`) | Opsional | Asisten yang lulus seleksi diinput langsung sebagai Personel; calon yang tidak lulus tidak dicatat |

**Temuan dependensi baru:** [pemetaan](pemetaan-package-instrumen.md) mencatat 04 → 15 (wajib) dan 18 → 04 (opsional). Penyebut PKG-04 ("sesi yang dilaksanakan") ternyata juga membutuhkan **status pelaksanaan dari PKG-18**. Ini dependensi data, bukan dependensi addon, karena status sesi ada di model Sesi Core. Perlu disepakati dengan Herrens **[KONFIRMASI kelompok]**.

**Isu penempatan master Kompetensi [KONFIRMASI kelompok]:** CLAUDE.md bagian 6 menaruh "syarat kompetensi" di Jabatan (`hr.job`, addon `labfik_core`), sedangkan pemetaan menetapkan master Kompetensi milik PKG-04 (`labfik_sdm`). `labfik_core` tidak boleh bergantung ke `labfik_sdm`. Ada dua pilihan:
1. **Kompetensi ditaruh di Core** bersama Jabatan, lalu dikelola oleh modul SDM.
2. **Syarat kompetensi ditambahkan ke `hr.job` oleh `labfik_sdm`** (`_inherit = 'hr.job'`). Core tetap tidak mengenal Kompetensi.

**Dipilih pilihan 2** (Zahir, 14 November 2026). Dependensi tetap satu arah, dan Core tidak perlu diubah. `labfik_sdm` juga menambahkan daftar Bukti Kompetensi ke `hr.employee` agar terlihat di form personel.

**Koreksi (Langkah 3, 14 November 2026):** Core versi terbaru (branch `febriyan-skripsi`) ternyata sudah punya `hr.job.syarat_kompetensi` berupa **teks**. Field itu tetap dipakai Tata Kelola sebagai uraian; `labfik_sdm` menambah `syarat_kompetensi_ids` (Many2many ke Kompetensi) untuk perhitungan. Rinciannya di [kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md) K-1 **[KONFIRMASI Febriyan, KC-1]**.

## 7. Ditunda (tidak dirancang; saran pengembangan)

- Pendaftaran calon asisten (sudah dibahas Anandar 2026) dan perhitungan honor (batasan pendahuluan).
- Alokasi asisten otomatis (*minimum coverage*, *need first*, cek bentrok) dari draf STD-PRK-03.
- Bobot rubrik seleksi rinci (35/25/20/10/10) dari draf RUB-PRK-01. Cukup skor total + keputusan + berkas.
- Kebutuhan petugas per sesi dengan perhitungan risiko otomatis. Cukup ditetapkan per kelas.
- Pengingat bukti kompetensi kedaluwarsa (penjadwal). Cukup status "berlaku/tidak" yang dihitung saat dibaca.

## 8. Pertanyaan untuk narasumber

Sudah ada di lembar wawancara (SDM & Kompetensi no. 1–15), belum dijawab KaLab dan laboran. Yang paling menentukan rancangan PKG-04:

| No. wawancara | Pertanyaan inti | Menentukan |
|---|---|---|
| 2 | Siapa yang menetapkan dan menandatangani penugasan petugas? Ada SK? | Penetap penugasan, alur S2 |
| 3a, 4 | Kapan dan oleh siapa kebutuhan petugas per kelas ditentukan? Berapa jumlah minimal per sesi? Kelas tanpa asisten boleh? | Grain dan isi Kebutuhan Petugas (S1) |
| 5 | Syarat minimal laboran/PLP, asisten, dosen. Nilai minimal MK asisten (A? 70?) | Isi master Kompetensi dan syarat per jabatan (S3, S4) |
| 5, 6 | Bagaimana pengecualian syarat diputuskan dan dicatat? | Alur pengecualian (S4) |
| 7 | Ada pernyataan kesediaan, pembekalan, pendampingan? | Komitmen dan Orientasi/Supervisi (bukti 7) |
| 8 | Siapa menunjuk pengganti petugas? Kemampuannya diperiksa? | Penugasan per sesi untuk pengganti |
| 3c (tambahan) | Setelah asisten memilih kelas, siapa yang mengesahkan pilihan itu? Kapan surat tugas terbit? | Penetap Penugasan Petugas (S2) |
| 13, 14 | Di mana data petugas tersimpan? Siapa boleh melihat/mengubah? | Sumber data awal, hak akses |

Klaim as-is di pendahuluan yang masih menunggu wawancara: **syarat nilai A dapat dilonggarkan secara informal** **[KONFIRMASI KaLab/Koor Prodi]**.

## 9. Kompleksitas (perkiraan)

| T | M lokal | R |
|---|---|---|
| 5 inti (Kebutuhan Petugas, Seleksi Kompetensi, Bukti Kompetensi, Surat Tugas, Penugasan Petugas sebagai baris) + 1 pelengkap (Orientasi/Supervisi; Komitmen cukup berkas) | 1 (Kompetensi) + syarat per jabatan | 2 (Daftar Sesi dan Petugas, Matriks Kompetensi) + persentase |

Pemetaan lama mencatat 3 T / 0 M / 3 R. Selisihnya karena Bukti Kompetensi dan Kebutuhan Petugas dipisahkan, master Kompetensi dihitung sebagai milik package ini, dan Surat Tugas berubah dari [R] menjadi [T] bergaris (14 Nov 2026).
