# LabFIK Compliance: panduan bersama untuk Claude Code

Panduan ini berlaku untuk **semua anggota** proyek LabFIK Compliance dan semua branch. Isinya: konteks proyek, alur merancang modul TO-BE dari awal sampai design class diagram, dan konvensi dokumen serta diagram. Alur dan konvensi ini sudah dijalankan penuh untuk modul **Tata Kelola & Dokumen** (Febriyan, November 2026). Modul itu menjadi **contoh referensi**; hasilnya diharapkan setara untuk modul lain.

Bahasa kerja: **Indonesia**.

## 0. Langkah pertama setiap sesi

1. Tentukan **modul** yang sedang dikerjakan. Lihat nama branch (`<nama>-skripsi`) atau tanya pengguna. Jangan menebak.
2. Baca [projek-fiklab/brief/brief-seluruh-projek.md](projek-fiklab/brief/brief-seluruh-projek.md) (proyek, modul, Core, keputusan, pertanyaan terbuka).
3. Cek apakah brief modul (`projek-fiklab/brief/brief-<slug>.md`) dan analisis **setiap** PKG modul sudah ada. Bila sudah, baca. **Bila belum, jalankan Langkah 0 (bagian 4) dan jangan lanjut ke rancangan.**
4. Periksa langkah rancangan mana yang sudah selesai (bagian 4). Lanjutkan dari langkah berikutnya; jangan lompat.
5. Bila ada file konteks pribadi pemilik branch (contoh: `tatkel-CLAUDE.md` di branch `febriyan-skripsi`), baca juga.

## 1. Proyek ringkas

- **Apa:** sistem berbasis **Odoo 17 Community** untuk Laboratorium FIK UPN "Veteran" Jakarta (LabFIK). Sistem mengelola kegiatan lab dan sekaligus menghasilkan bukti untuk **Instrumen Monev Laboratorium UPNVJ 2026 v1.1**, yang antara lain mengacu ke **SNI ISO/IEC 17025:2017**.
- **Cakupan:** 21 indikator. **1 package = 1 indikator.** Nomor PKG (PKG-01–21) adalah identitas resmi indikator, karena penomoran di sheet instrumen tidak rapi.
- **Pembagian kerja:** per modul fungsional → package → entitas. Satu skripsi memegang satu modul. Master bersama ada di Core.
- **Pembimbing:** Pak Widi. Proposal mengikuti Pedoman TA FIK 2025 jenis **Prototipe/Proyek**.
- **Penting dari pembimbing (bimbingan November 2026):**
  - Prioritaskan rancangan **TO-BE** (Bab II 2.3) sebelum Bab I dan 2.1 Observasi.
  - Pendekatan **UML** yang cocok dengan Odoo.
  - Class Odoo dirancang memakai **inheritance**, supaya field dan perilaku tidak ditulis berulang.
  - Proses pendokumentasian di FIK banyak yang belum ada; observasi *as-is* boleh dari studi dokumen dan ISO selama wawancara belum ada.

### Prinsip utama: cari *sweet spot*, bukan sistem selengkap mungkin

Tujuan rancangan **bukan** sistem yang selengkap dan serumit mungkin. Yang dicari adalah titik tengah antara dua ujung:

| MVP | **Sweet spot (target)** | Rancangan lengkap |
|---|---|---|
| Minimum, sederhana, cakupan rendah. Ada kriteria instrumen yang tidak bisa dibuktikan | Semua kebutuhan awal (kriteria instrumen) terpenuhi, dan rancangannya tetap mudah dipahami pengguna, pembimbing, dan penguji | Lengkap, sangat detail, rumit. Sulit dipahami dan terlalu besar untuk dibangun dalam satu skripsi |

Cara menerapkannya di setiap modul:
- **Lantai ditentukan instrumen.** Setiap kriteria (K1–K4 / S1–Sn) harus punya kebutuhan dan rekaman bukti. Itu batas bawah yang tidak boleh dipangkas.
- **Langit-langit ditentukan kejelasan.** Fitur yang tidak dibutuhkan untuk membuktikan kriteria dan menambah kerumitan (varian alur, master tambahan, otomatisasi, pengingat, tahap persetujuan berlapis) **tidak dirancang**; cukup dicatat di batasan masalah sebagai saran pengembangan.
- **Dua lapis cakupan:** **Inti** (tanpa ini ada kriteria yang tidak terbukti atau alur putus; prioritas W) dan **Pelengkap** (memperkuat rancangan dengan biaya kecil; prioritas O). Keduanya dirancang dan digambar; selain itu tidak.
- **Pilihan sederhana didahulukan:** satu jalur utama sebelum jalur alternatif, teks bebas sebelum master baru, unggah berkas sebelum form isian, nilai yang dihitung dari data sebelum penjadwal/pengingat.
- **Yang menunjukkan desain tetap dipertahankan** bila murah: inheritance (mixin), riwayat kejadian penting, Template Method. Ini yang diminta pembimbing.
- Ragu apakah sesuatu masuk? Tanyakan: "kriteria instrumen mana yang gagal bila ini tidak ada?" Bila tidak ada jawabannya, jangan dirancang.

Contoh penerapan: bagian "Cakupan rancangan" di brief Tata Kelola (branch `febriyan-skripsi`). Rancangan Tata Kelola di tag `rancangan-tatkel-v1` adalah contoh ujung **lengkap**: pakai sebagai contoh format dan cara berpikir, bukan sebagai ukuran cakupan.

## 2. Modul, pemegang, dan identitas

| Modul | Pemegang | Branch | Slug file | Addon (usulan) | Prefiks ID drawio | Prefiks kode KF/UC/AB | Warna (fill / stroke) |
|---|---|---|---|---|---|---|---|
| Tata Kelola & Dokumen (PKG-01, 02, 03, 13) | Febriyan | `febriyan-skripsi` | `tata-kelola` | `labfik_org` | `tk-` | **tanpa prefiks** (KF-01, UC-21, AB-03) | `#F5F0FF` / `#9673A6` |
| SDM & Kompetensi (PKG-04, 10, 14) | Zahir | `zahir-skripsi` **[KONFIRMASI]** | `sdm` | `labfik_sdm` | `sdm-` | `KF-SDM-01`, `UC-SDM-01`, `AB-SDM-01` | `#EEFAF3` / `#4E9A6B` |
| Pelaksanaan Praktikum (PKG-15–20) | Herrens | `herrens-skripsi` **[KONFIRMASI]** | `praktikum` | `labfik_praktikum` | `prk-` | `KF-PRK-01`, … | `#EEF6FF` / `#6C8EBF` |
| Asset Management (PKG-05, 07, 08, 12, 21) | Kelompok lain | — | `aset` | — | `ast-` | `KF-AST-01`, … | `#FFF8EC` / `#D79B00` |
| Safety Management (PKG-06, 09, 11) | Kelompok lain | — | `safety` | — | `saf-` | `KF-SAF-01`, … | `#FFF0F0` / `#B85450` |
| Core (master bersama) | Bersama | `main` | `core` | `labfik_core` | `core-` | `KF-CORE-01`, … | `#F2F2F2` / `#666666` |

- Warna diambil dari diagram bersama [pemetaan-package-instrumen.drawio](projek-fiklab/analisis/pemetaan-package-instrumen.drawio). Pakai warna modulmu untuk batas sistem, package, lajur, dan bingkai.
- Prefiks ID wajib untuk **semua** elemen drawio, supaya diagram semua orang bisa digabung ke satu file drawio tanpa bentrok.
- Modul Tata Kelola dikerjakan sebelum konvensi prefiks kode dibuat; kodenya tanpa prefiks. Modul lain **wajib** memakai prefiks agar tidak ada dua "UC-21" di dokumen gabungan.

## 3. Sumber kebenaran, penanda, dan larangan

**Urutan sumber kebenaran:** Instrumen Monev (xlsx) dan ISO/IEC 17025 → brief → analisis → rancangan → kode. Bila bertentangan, ikuti sumber yang lebih kiri, lalu sebutkan konfliknya ke pengguna.

**Penanda wajib** untuk hal yang belum pasti:

| Penanda | Dipakai bila |
|---|---|
| **[KONFIRMASI]** | Perlu jawaban pembimbing, KaLab, laboran, atau kelompok |
| **[VALIDASI]** | Perlu dicek ke dokumen asli atau data |
| **[ASUMSI]** | Dianggap benar sementara supaya pekerjaan bisa lanjut |
| **[USULAN PENULIS]** | Gagasan penulis, belum disetujui siapa pun |

**Konvensi umum:**
- Sebut indikator sebagai **PKG + aspek + nomor + kata kunci**, misalnya `PKG-10 Pengelolaan 10 (otorisasi)`.
- Pakai **nama master baku** dan label entitas **[T]** transaksi / **[M]** master / **[R]** report dari [pedoman-pengisian-sheet-analisis.md](projek-fiklab/analisis/pedoman-pengisian-sheet-analisis.md) bagian 4.
- Sebut **level cakupan** (otomatis / semi-otomatis / bukti tertaut). Jangan mengklaim skor "dihitung otomatis" untuk indikator kriteria berurutan K1–K4; sistem hanya menunjukkan kriteria tertinggi yang **lengkap secara data**, skor akhir ditetapkan penilai.
- Jangan menjanjikan kenaikan skor monev. Sistem adalah alat pencatatan, pembuktian, dan pemantauan.
- Klaim kondisi lab saat ini (as-is) harus punya sumber: wawancara, data, atau dokumen. Bukan dugaan.

**Larangan:**
- **Data pribadi tidak boleh masuk repo:** nama asisten/mahasiswa/staf dari dokumen nyata, NIM, nomor HP, rekening/KTP, nilai. Sebut jabatan dan nomor dokumen saja. Data demo dan seed wajib fiktif. Periksa file baru dengan `grep` sebelum commit.
- **Paket Dokumen Monev di Drive LabFIK** (M01–M21) dan sebagian dokumen di sheet `ISO_LAB_SI` adalah **draf hasil GPT**. Pakai hanya sebagai contoh format, bukan sumber kebutuhan atau bukti kondisi nyata. Tandai mana dokumen nyata dan mana draf GPT setiap kali membedah dokumen.
- `skripsi_rafika/` (modul `PendaftaranAsisten`, OpenEduCat) **hanya acuan**; jangan diubah dan jangan di-*extend*.
- File bersama (`brief-seluruh-projek.md`, `pedoman-pengisian-sheet-analisis.md`, `pemetaan-package-instrumen.*`, `docs/`, file ini) dipakai semua anggota. Perubahan di sana disampaikan ke anggota lain.

## 4. Alur rancangan TO-BE (langkah 1–10)

Alur ini mengikuti **Wazlawick, R. S. (2024). *Object-Oriented Analysis and Design for Information Systems* (2nd ed.). Morgan Kaufmann/Elsevier.** Ringkasan per bab ada di [projek-fiklab/docs/OOAD_Wazlawick_2024_Knowledge_Pack/](projek-fiklab/docs/OOAD_Wazlawick_2024_Knowledge_Pack/); mulai dari `00_INDEX_README.md`. **Baca bab yang relevan sebelum mengerjakan setiap langkah**, jangan dari ingatan.

Setiap langkah memakai hasil langkah sebelumnya. Jangan membuat use case atau class diagram langsung tanpa langkah sebelumnya: itu kesalahan yang sudah pernah terjadi (bagian 8).

| # | Langkah | Output (`projek-fiklab/…`) | Bab Wazlawick | Masuk proposal |
|---|---|---|---|---|
| 0 | **Prasyarat:** brief modul dan analisis per PKG | `brief/brief-<slug>.md`, `analisis/analisis-*.md` | — | Bahan Bab I dan 2.2 |
| 1 | Kumpulkan keputusan pembimbing dan scope | Brief modul diperbarui | — | (Bab I 1.3) |
| 2 | Studi dokumen (bedah dokumen lab) | `analisis/bedah-dokumen-<slug>.md` | — | Bahan 2.1 |
| 3 | Kontrak Core dengan modul lain | Catatan di brief / dokumen DCD | — | — |
| 4 | Kebutuhan sistem | `rancangan/kebutuhan-<slug>.md` | 4.7 | Bahan 2.2 |
| 5 | Proses bisnis TO-BE: activity + state machine | `rancangan/proses-bisnis-<slug>.md` + `activity-state-<slug>.drawio` | 3, 9.3 | **Ya** (2.3) |
| 6 | Use case diturunkan dari proses bisnis | `rancangan/use-case-<slug>.md` + `.drawio` | 4 | **Ya** (2.3) |
| 7 | Expanded use case + aturan bisnis | `rancangan/expanded-use-case-<slug>.md` | 6 | Bahan kerja (bahan 2.4) |
| 8 | System sequence diagram + katalog operasi | `rancangan/ssd-<slug>.md` + `.drawio` | 7 | **Ya** (2.3, "sequence diagram") |
| 9 | Conceptual model | `rancangan/conceptual-model-<slug>.md` + `.drawio` | 8–11 | Bahan kerja |
| 10 | Design class diagram (Odoo + inheritance) | `rancangan/design-class-<slug>.md` + `class-<slug>.drawio` | 13 | **Ya** (2.3) |

Kontrak OCL (Bab 12) **dilewati** untuk proposal; aturan bisnis cukup ditulis sebagai AB-xx dan dipetakan ke mekanisme Odoo di langkah 10.

### Langkah 0: Prasyarat (wajib dicek sebelum langkah 1)
Rancangan tidak boleh dimulai tanpa brief modul dan analisis setiap PKG-nya. Keduanya adalah dasar semua langkah berikutnya.

1. **Cek keberadaan**, jangan hanya di branch aktif:
   - `projek-fiklab/brief/brief-<slug>.md` dan analisis untuk **setiap** PKG modul (`projek-fiklab/analisis/`).
   - Branch lain dan riwayat git: `git log --all --oneline -- 'projek-fiklab/analisis/*' 'projek-fiklab/brief/*'`, lalu `git show <branch atau commit>:<path>`. Sebagian PKG pernah dianalisis anggota lain (lihat catatan di brief bersama, bagian "Modul dan pemegangnya"; contoh: analisis awal PKG-18/19 ada di commit `62e50ce`).
   - Bahan yang sudah ada di `main`: [pemetaan-package-instrumen.md](projek-fiklab/analisis/pemetaan-package-instrumen.md) (entitas milik, *import*, dan pemakai tiap package) dan tab *Analysis* di Instrumen xlsx.
2. **Laporkan hasilnya** ke pengguna dalam tabel: PKG → analisis ada / sebagian / belum → lokasinya; brief ada / belum.
3. **Bila ada yang belum ada: berhenti.** Ajak pengguna menyusunnya dulu. Jangan lanjut ke langkah 1–10 dan jangan mengarang isi analisis.
4. **Cara menyusun** (sebagai diskusi dengan pengguna, satu PKG demi satu PKG):
   - **Analisis per PKG:** ikuti [pedoman-pengisian-sheet-analisis.md](projek-fiklab/analisis/pedoman-pengisian-sheet-analisis.md) bagian 2: target → aturan "memenuhi" (K1–K4 atau S1–Sn, dengan kolom cek oleh sistem / cek oleh penilai) → luaran (bukti dukung) → data transaksi → master data → dependensi dan jalan pengganti → yang ditunda → pertanyaan untuk narasumber. Sumber utama: bunyi indikator, kriteria, dan bukti dukung di Instrumen xlsx. Contoh format: `analisis-data-pengelolaan-1-3.md` dan `analisis-data-pengembangan-13.md` di tag `rancangan-tatkel-v1`.
   - **Brief modul:** tiru struktur `brief-tata-kelola-dokumen.md` (tag `rancangan-tatkel-v1`): ringkasan, indikator yang dipegang (PKG, PJ, jenis skor, level cakupan, acuan), pola bersama di dalam modul, lingkup kebutuhan, kontrak dengan modul lain (disediakan / dipakai), batasan masalah, tabel masalah → tujuan → fitur, risiko dan mitigasi, pertanyaan terbuka.
   - **Tanyakan** hal yang hanya diketahui pengguna: scope yang sudah disetujui pembimbing, kondisi lab yang diketahui, narasumber yang tersedia, dokumen lab yang dimiliki. Yang belum terjawab ditandai **[KONFIRMASI]**; klaim kondisi lab tanpa sumber ditandai dan tidak dikarang.
5. Setelah brief dan semua analisis ada, lanjut ke langkah 1.

### Langkah 1: Keputusan pembimbing dan scope
- Catat arahan bimbingan terbaru di brief modul. Bila bertentangan dengan brief lama, tandai dan perbarui brief (bagian batasan masalah).
- Brief dan analisis sudah dipastikan ada di Langkah 0; di sini cukup diperbarui sesuai arahan terbaru.
- Tetapkan **cakupan rancangan** di brief (prinsip *sweet spot*, bagian 1): tabel per area dengan lapis Inti dan Pelengkap, plus daftar "tidak dirancang" di batasan masalah. Semua langkah berikutnya tidak boleh keluar dari cakupan ini tanpa persetujuan pengguna.

### Langkah 2: Studi dokumen
- Bedah setiap dokumen lab yang relevan: bagian dokumen → field → model → PKG/kriteria → **Dasar** (Instrumen / ISO / Format saja).
- Tandai sifat tiap dokumen: **nyata** atau **draf GPT**, tanggal, PKG.
- Hasilkan **temuan as-is** bernomor (A1, A2, …) yang hanya bersumber dari isi dokumen. Ini bahan 2.1 Observasi.
- Field dari draf GPT hanya dipakai bila juga didukung instrumen atau analisis.

### Langkah 3: Kontrak Core
- Master bersama dan mixin **sudah dirancang** di modul Tata Kelola (bagian 6). Pakai yang ada. Bila butuh perubahan, usulkan ke pemiliknya; jangan membuat versi sendiri.

### Langkah 4: Kebutuhan
- Tabel aktor (peran, grup akses usulan) dan kebutuhan fungsional `KF-<P>-nn` dengan kolom: kebutuhan, aktor, model, kriteria instrumen, prioritas (W = lapis Inti, O = lapis Pelengkap). Kebutuhan di luar cakupan brief tidak ditulis sebagai KF. Ditambah kebutuhan nonfungsional dan tabel keterlacakan **masalah → tujuan → KF**.

### Langkah 5: Proses bisnis (activity + state machine)
- **Activity** hanya untuk proses nontrivial (multi-aktor, bercabang, beraturan). Konsep yang hanya dikelola (CRUDL) tidak digambar (§3.4).
- **State machine** untuk objek bisnis yang berganti status (§3.3). Buat **tabel status × transisi** (Tabel 3–1) dan tanyakan setiap sel kosong: transisi baru yang ditemukan menjadi kebutuhan/use case baru.
- Satukan status yang tidak konsisten antar-analisis di state machine.
- Bagian proses yang dipakai banyak proses digambar sekali dan dipanggil dengan **«call behavior»**.

### Langkah 6: Use case
- Turunkan dari tugas **«user»** di activity (§4.5) dan **event** di state machine (§4.6). Tugas yang berurutan tanpa jeda = satu use case; yang bisa ditunda (beda hari atau aktor) = terpisah.
- Kriteria §4.3: satu sesi, interaktif, hasil konsisten, **essential** (tanpa "cetak", "ekspor PDF", "login", "buka layar"), tanpa fragmen.
- Hindari «include»/«extend» kecuali benar-benar use case utuh yang dipakai bersama. Konsep sederhana diberi stereotype **«CRUDL»**; laporan **«report»**.
- Lengkapi dengan **matriks Konsep × CRUDL** (§4.8.2): setiap konsep yang dibuat harus ada yang membacanya.
- Peran yang diperankan beberapa jabatan dijadikan **aktor abstrak** dengan generalisasi. Pemicu waktu = aktor «system» Penjadwal.
- Use case diagram boleh dipecah per area (beberapa halaman) agar terbaca.

### Langkah 7: Expanded use case
- Katalog **aturan bisnis** `AB-<P>-nn` lebih dulu; eksepsi merujuk ke kode AB.
- **Tabel deskripsi** semua use case non-CRUDL/non-report (tujuan, aktor, prakondisi, pascakondisi, eksepsi).
- **Alur lengkap** untuk use case kunci (yang akan dibuat SSD): pasangan transaksi aktor ↔ sistem, lurus tanpa *if*, data disebut eksplisit, varian V dan eksepsi E dengan akhir jelas (berhasil / gagal / kembali ke langkah n) (§6.2–6.4).
- Satu pola bersama untuk «CRUDL» dan «report» (§6.7).

### Langkah 8: System sequence diagram
- Satu SSD per use case kunci. Lifeline `:Aktor`, `:Antarmuka` (boundary), `:Kontroler` (control); aktor kedua di kanan bila ada pemberitahuan.
- Pisahkan **command** `op(args)` (mengubah data, tanpa nilai balik) dan **query** `dto = op(args)` (hanya membaca) (CQS, §7.1). **Stateless**: `user_id` dikirim ke setiap operasi (§7.5).
- Alur alternatif sebagai `opt «exception»` / `opt «variant»`; `ref` ke SSD lain (§7.6).
- Hasil utama: **katalog operasi** (command, query) + **kamus DTO**. Satukan operasi berpola sama dengan parameter `filter`.

### Langkah 9: Conceptual model
- Hanya konsep, atribut **primitif**, dan asosiasi bernama peran. **Tanpa method, tanpa Odoo, tanpa atribut bertipe kelas atau `*_id`** (§8, §10.4).
- Atribut turunan `/nama`, «unique», komposisi hanya untuk bagian–keseluruhan sungguhan (§8.4.5).
- Data yang baru muncul saat status berubah dimodelkan sebagai **konsep kejadian**, bukan atribut opsional (*modal class*, §9.3.2).
- Pakai pola Bab 11 bila cocok: organizational hierarchy, effectivity, history, superseding, specification class.
- Cek kelengkapan: setiap isi kamus DTO harus punya tempat di model.

### Langkah 10: Design class diagram
- Mulai dari salinan conceptual model, lalu (§13.6): tambah **method** dari katalog operasi, beri **arah** asosiasi, perinci **tipe field Odoo**, ubah struktur bila perlu (mixin, model log).
- **Inheritance:** pakai mixin `AbstractModel` untuk perilaku bersama; `_inherit` model baru ke mixin. Method `{abstract}` diisi model turunan (polimorfisme). Urutan baku yang tidak boleh terlewat ditulis sebagai **Template Method** dengan **hook** untuk turunan.
- Petakan **setiap** operasi SSD ke method atau ORM standar, dan **setiap** AB ke mekanisme Odoo (`@api.constrains`, `_sql_constraints`, hook, `compute`, `ir.cron`).
- Dokumen pendamping wajib memuat tabel "perubahan dibanding versi sebelumnya" bila ada versi lama.

### Cek silang sebelum lanjut ke langkah berikutnya
- Setiap KF punya use case, atau dicatat sebagai perilaku sistem.
- Setiap use case non-CRUDL punya sumber (tugas activity atau event state machine).
- Setiap kriteria instrumen (K1–K4 / S1–Sn) punya kebutuhan dan rekaman buktinya.
- Setiap transisi state machine punya use case atau tugas Penjadwal.
- Status dan nama konsep sama di semua dokumen.
- Rujukan nomor (KF, UC, AB) di dokumen lain masih valid setelah perubahan.

## 5. Konvensi diagram draw.io

**Umum**
- Semua diagram berupa file **`.drawio`** di `projek-fiklab/rancangan/`, satu file per jenis diagram, beberapa halaman per file bila perlu.
- Hanya shape **UML** (atau Archimate). Bukan BPMN, bukan flowchart bebas.
- Nama halaman: `<Jenis> TO-BE (n-m) - <isi>`, misalnya `UC TO-BE (1-3) - Pengesahan Dokumen`.
- **Semua** ID berawalan prefiks modul + jenis diagram, misalnya `sdm-uc1-…`, `sdm-act-a2-…`, `sdm-ssd3-…`, `sdm-cm2-…`, `sdm-dcd1-…`.
- Setiap halaman punya: judul, **catatan legenda notasi** (kotak kuning `shape=note`, `#FFF2CC` / `#D6B656`), catatan sumber (dari dokumen mana, tanggal, nama penyusun), dan [KONFIRMASI] yang relevan.
- Buat diagram lewat **skrip Python** (contoh di [projek-fiklab/tools/drawio/](projek-fiklab/tools/drawio/)), lalu jalankan `validate.py` dengan prefiks modul. Laporkan ke pengguna bahwa tampilan visual belum dicek bila draw.io tidak tersedia.

**Activity diagram**
- Swimlane per aktor + lajur **Sistem**. Tugas: **«user»** (putih), **«service»** (abu-abu `#EEEEEE`, otomatis), **«manual»** (krem `#FFF8E7`, putus-putus, di luar sistem), **«call behavior»** (ungu, memanggil activity lain).
- Nama tugas = kata kerja + objek domain, tanpa "dan/atau". Keputusan ◇ tanpa nama; kondisi `[guard]` di panah. Menunggu waktu ⧗ (`shape=collate`). Paralel = bar hitam.

**State machine**
- Transisi `event [guard] / efek`. Status akhir abu-abu. Transisi yang baru ditemukan lewat tabel status × transisi ditandai garis merah (`#9B2C44`) dan dicatat.

**Use case**
- Batas sistem bergaris warna modul; use case dikelompokkan dalam **package** (`shape=folder`). Label use case: stereotype (bila ada), kode tebal, nama.
- Aktor abstrak bernama miring dengan generalisasi segitiga kosong; aktor «system» abu-abu.

**System sequence diagram**
- `shape=umlLifeline` dengan `participant=umlActor / umlBoundary / umlControl`. Event: panah penuh hitam; return: putus-putus; command/query: panah ungu kepala segitiga. Fragmen `shape=umlFrame` (`opt`, `ref`).

**Conceptual model**
- Kelas tanpa kompartemen method. Asosiasi tanpa arah, label peran + multiplisitas di ujung. Komposisi belah ketupat hitam; generalisasi segitiga kosong; enumerasi «enumeration» abu-abu; kelas yang dirinci di halaman lain = kotak putus-putus.

**Design class diagram**
- Mixin «AbstractModel» ungu (`#E1D5E7` / `#9673A6`), nama miring. Model Odoo bawaan «Odoo» abu-abu; Core «Core» abu-abu putus-putus; model baru hasil desain bertepi merah.
- Header kelas: nama teknis, nama manusiawi + [M]/[T], dan `{inherit: …}` bila mewarisi mixin. Field warisan **tidak** ditulis ulang.
- Asosiasi **berarah** (Many2one/Many2many) dengan label nama field + multiplisitas; komposisi = One2many + Many2one; turunan = garis putus-putus `{compute}`. Hanya model bawaan Odoo yang boleh ditulis sebagai atribut bertipe.
- Method: `+` publik (`action_*`, `get_*`), `#` internal (`_cek_*`, `_compute_*`), `@model`, `«override»`, `{abstract}`, `{hook}`.

## 6. Kontrak Core dan model yang sudah ada

Dirancang di modul Tata Kelola (design class diagram di tag `rancangan-tatkel-v1`). Modul lain **memakai**, bukan membuat ulang.

| Model / mixin | Isi | Pakai untuk |
|---|---|---|
| Personel = `hr.employee` (Odoo CE `hr`, LGPL-3) diperluas dengan `_inherit` | Semua orang yang punya peran di lab (dosen, laboran/PLP, teknisi, asisten, petugas K3, eksternal) | Semua rujukan ke orang (PIC, peserta, petugas). Cara mencatat asisten (mahasiswa) dan pihak eksternal sebagai `hr.employee` masih **[KONFIRMASI kelompok]** |
| Jabatan = `hr.job` diperluas (+ `labfik.jabatan.tugas`, `labfik.jabatan.wewenang`) | Jabatan, unit, atasan, pengganti, wewenang per jenis dokumen, syarat kompetensi | Siapa berwenang melakukan apa. `cari_pemegang_berwenang(tindakan, jenis)` |
| `labfik.ruang`, `labfik.periode` | Master Core | Lokasi dan periode |
| `labfik.approval.mixin` + `labfik.approval.log` | Siklus status draf → diajukan → disahkan → diganti/dicabut/kedaluwarsa (tanpa tahap pemeriksaan), cek wewenang, berkas bertanda tangan, riwayat pengesahan, hook `_setelah_disahkan()` | Setiap dokumen yang perlu disahkan (mis. rencana pelatihan PKG-14) |
| `labfik.controlled.mixin` | Kode, revisi, unit pemilik | Dokumen terkendali |
| `labfik.period.mixin` | Periode berlaku + penjadwal kedaluwarsa | Dokumen berperiode |
| `labfik.criteria.mixin` | `status_k1`–`k4`, `kriteria_tertinggi`; `_cek_k1()`–`_cek_k4()` {abstract} | Indikator kriteria berurutan K1–K4 |
| `labfik.evidence.mixin` | Tanggal, pelapor, bukti, keterangan | Setiap rekaman kegiatan yang menjadi bukti |

**Nama model yang sudah dipakai Tata Kelola** (jangan dipakai ulang untuk hal lain): `labfik.plan*`, `labfik.document*`, `labfik.assignment*`, `labfik.meeting`, `labfik.org.evaluation`, `labfik.realisasi`, `labfik.tinjauan*`, `labfik.kpi`, `labfik.approval.log`. Untuk modul baru, pakai pola `labfik.<slug>.<objek>`, misalnya `labfik.sdm.kompetensi`.

**Penempatan (keputusan Febriyan, 14 November 2026; [KONFIRMASI kelompok]):** master bersama, perluasan `hr`, dan semua mixin di atas ditempatkan di addon **`labfik_core`** (`depends: ['hr', 'mail']`), terpisah dari `labfik_org`. Setiap modul fungsional cukup `depends: ['labfik_core']`. DCD di tag `rancangan-tatkel-v1` masih memakai model `labfik.personel` dan tahap *diperiksa*; tabel ini yang berlaku.

## 7. Konvensi dokumen Markdown

- Baris kedua setiap dokumen: `tanggal · penulis · PKG yang dicakup`. Lalu baris **Status: DRAF** dan keterangan apakah dokumen masuk proposal atau bahan kerja.
- Dokumen pendamping diagram memuat: aturan/pedoman yang dipakai (dengan nomor bab Wazlawick), isi diagram, keputusan dan alasannya, temuan untuk langkah berikutnya, isu terbuka.
- Kode bernomor tidak digeser setelah dipakai; bila ada yang dihapus, biarkan nomornya kosong dan catat alasannya.
- Tulis lugas dalam bahasa Indonesia; istilah teknis Inggris dicetak miring bila perlu (*use case*, *mixin*).

## 8. Kesalahan yang sudah pernah terjadi (hindari)

| Kesalahan | Akibat | Yang benar |
|---|---|---|
| Use case dan class diagram dibuat sebelum proses bisnis | Use case tidak punya sumber; transisi status terlewat | Ikuti urutan langkah 5 → 10 |
| «include» untuk langkah yang dilakukan aktor berbeda atau di hari berbeda | Melanggar kriteria satu sesi | Use case terpisah; urutan digambar di activity |
| Use case "Cetak Laporan", "Ekspor PDF" | Tidak *essential* | "Lihat Laporan …" «report», "Terbitkan Dokumen Resmi" |
| Nama use case dengan "dan" ("Catat Distribusi & Sosialisasi") | Dua tugas digabung | Pecah menjadi dua |
| `pic_id: Personel` di conceptual model | Relasi tersembunyi, multiplisitas tidak diperiksa | Asosiasi bernama peran |
| Pengesahan hanya disimpan sebagai field keadaan terakhir | Riwayat (dikembalikan berkali-kali, berkas diganti) hilang | Konsep kejadian di CM → model log di DCD |
| Status dokumen berbeda di tiap analisis | Rancangan tidak konsisten | Satukan di state machine |
| Override `action_sahkan()` langsung di model turunan | Cek wewenang bisa terlewat | Template Method + hook |
| Field dari draf GPT dipakai tanpa dasar instrumen | Kebutuhan palsu | Kolom "Dasar" di bedah dokumen |
| Konteks pribadi satu anggota di CLAUDE.md bersama | Claude anggota lain salah konteks | Konteks pribadi di brief modul atau file konteks per branch |
| Rancangan dimulai tanpa brief dan analisis PKG | Kebutuhan tidak berdasar instrumen | Langkah 0: cek, laporkan, susun dulu |
| Rancangan dibuat selengkap mungkin (semua varian, master, pengingat, tahap persetujuan) | Terlalu rumit dipahami dan dibangun; harus dipangkas ulang (Tata Kelola, November 2026) | Tetapkan cakupan Inti + Pelengkap di brief sebelum langkah 4 (bagian 1, prinsip *sweet spot*) |

## 9. Pemetaan ke proposal (Pedoman TA FIK 2025, Prototipe/Proyek)

| Bagian | Isi dari alur ini |
|---|---|
| Bab I 1.2 Identifikasi Masalah | Masalah modul (selaras dengan "Permasalahan bersama untuk Bab 1" di brief bersama) + temuan as-is |
| Bab I 1.3 Batasan Masalah | Batasan di brief modul |
| Bab II 2.1 Observasi (as-is) | Temuan studi dokumen, hasil wawancara, ISO 17025. Activity as-is bila diperlukan. Dikerjakan setelah TO-BE |
| Bab II 2.2 Usulan Solusi | Fitur utama modul + mekanisme bersama (dari kebutuhan dan use case) |
| Bab II 2.3 Rancangan Proyek | Activity + state machine, use case, SSD, design class diagram, beserta penjelasannya. Tabel deskripsi use case bila diminta pembimbing |
| Bab II 2.4 Rencana Pengujian | Skenario *black box* dari alur utama dan eksepsi expanded use case; pengujian aturan bisnis AB |

## 10. Contoh referensi: modul Tata Kelola & Dokumen

Semua di tag `rancangan-tatkel-v1` (rancangan Tata Kelola yang lengkap, dibekukan 14 November 2026). Baca lokal dengan `git fetch --tags` lalu `git show rancangan-tatkel-v1:<path>`. Branch `febriyan-skripsi` sedang menyusun ulang rancangan dengan cakupan yang lebih kecil, jadi isinya belum lengkap; jangan jadikan contoh sampai tabel ini diperbarui.

| Langkah | File |
|---|---|
| 0 Analisis per PKG | [analisis-data-pengelolaan-1-3.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/analisis/analisis-data-pengelolaan-1-3.md), [analisis-data-pengembangan-13.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/analisis/analisis-data-pengembangan-13.md) |
| 0 · 1 Brief | [brief-tata-kelola-dokumen.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/brief/brief-tata-kelola-dokumen.md) |
| 2 Studi dokumen | [bedah-dokumen-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/analisis/bedah-dokumen-tata-kelola.md) |
| 4 Kebutuhan | [kebutuhan-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/kebutuhan-tata-kelola.md) |
| 5 Proses bisnis | [proses-bisnis-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/proses-bisnis-tata-kelola.md), `activity-state-tata-kelola.drawio` |
| 6 Use case | [use-case-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/use-case-tata-kelola.md), `use-case-tata-kelola.drawio` |
| 7 Expanded use case | [expanded-use-case-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/expanded-use-case-tata-kelola.md) |
| 8 SSD | [ssd-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/ssd-tata-kelola.md), `ssd-tata-kelola.drawio` |
| 9 Conceptual model | [conceptual-model-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/conceptual-model-tata-kelola.md), `conceptual-model-tata-kelola.drawio` |
| 10 Design class diagram | [design-class-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/rancangan-tatkel-v1/projek-fiklab/rancangan/design-class-tata-kelola.md), `class-tata-kelola.drawio` |
| Penjelasan untuk pemula (class diagram, inheritance) | Halaman artifact milik Febriyan; minta tautannya ke Febriyan |

## 11. Gaya kerja

- Sebelum membuat artefak, baca bab Wazlawick yang relevan dan sebutkan aturan yang dipakai. Setelah selesai, lakukan cek silang (bagian 4) dan laporkan temuannya, termasuk kesalahan sendiri yang ditemukan di langkah sebelumnya.
- Tanyakan keputusan yang benar-benar milik pengguna atau pembimbing; sisanya pilih default yang wajar dan sebutkan.
- Jelaskan dengan bahasa sederhana bila pengguna belum paham konsepnya (analogi, contoh dari modulnya sendiri).
- Jangan commit atau push tanpa diminta. Commit dikelompokkan per langkah dengan pesan berbahasa Indonesia huruf kecil.
- Cek data pribadi sebelum commit (bagian 3).
