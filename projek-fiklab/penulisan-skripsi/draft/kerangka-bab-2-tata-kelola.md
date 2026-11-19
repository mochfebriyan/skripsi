# Kerangka Bab II Rancangan Proyek: Modul Tata Kelola & Dokumen

16 November 2026 · Febriyan · PKG-01, 02, 03, 13
**Status: DRAF**, garis besar. Isi paragraf belum ditulis.

---

## 1. Patokan beban dari skripsi terdahulu

Diukur dari 13 Bab II di [bab-2-references.md](../reference/bab-2-references.md). Angka halaman dihitung dari nomor halaman, jadi perkiraan.

| Ukuran | Rentang | Tengah (median) | Catatan |
|---|---|---|---|
| Panjang Bab II | 29–126 hal | ±58 hal | Yang >100 hal membengkak karena CRUD dan halaman UI digambar satu per satu |
| 2.1 Observasi | 1–5 hal | ±3 hal | Kecuali yang memakai wawancara atau prototipe panjang (30+ hal) |
| 2.2 + 2.3 (diagram) | 20–90 hal | ±40 hal | Bagian terbesar |
| 2.4 Pengujian | 1–12 hal | ±3 hal | Satu tabel skenario *black box* |
| Jumlah gambar | 22–110 | ±34 | |
| Penjelasan per gambar | 0,5–1,5 hal | — | Pengantar → gambar → "Berdasarkan Gambar 2.n, …" |

**Target modul ini: ±40–50 halaman dan ±20–25 gambar.** Jumlah ini di sekitar median, tetapi tanpa diagram CRUD dan UI per halaman yang membuat beberapa skripsi terdahulu membengkak.

---

## 2. Kerangka

Kolom **Sumber** menunjuk artefak yang sudah ada, jadi isi bab ini disalin dan dinarasikan, bukan dibuat ulang.

### 2.1 Observasi (±6 hal)

| Subbab | Isi | Sumber | Beban |
|---|---|---|---|
| 2.1.1 Metode Observasi | Tiga metode: studi dokumen lab (D1–D6, ditandai **nyata** atau **draf**), telaah Instrumen Monev 2026 dan ISO/IEC 17025, wawancara KaLab **[KONFIRMASI: jadwal]** | bedah-dokumen §1, brief | 1 hal, 1 tabel dokumen |
| 2.1.2 Kondisi Saat Ini | Temuan A1–A12, dikelompokkan per indikator (struktur, SOP/IK, rencana kerja, rencana pengembangan) | bedah-dokumen §2 | 2 hal |
| 2.1.3 Kesenjangan terhadap Instrumen | Tabel: PKG → kriteria (K1–K4 / S1–S5) → kondisi saat ini → kesenjangan | analisis PKG, bedah-dokumen | 2 hal, 1 tabel |
| 2.1.4 Pengguna dan Kebutuhannya | Tabel aktor (Pengguna Lab, Laboran/PLP, KaLab) dan kebutuhan masing-masing | kebutuhan §1 | 1 hal, 1 tabel |

**Alasan:**
- **Lebih panjang dari median (±3 hal):** sistemnya belum ada, jadi bukti masalah sepenuhnya bergantung pada observasi. Rubrik "masalah jelas" berbobot 20.
- **Studi dokumen jadi metode utama:** sesuai arahan pembimbing 13 Nov 2026. Wawancara masuk bila sudah dilakukan.
- **Tabel kesenjangan menggantikan PIECES:** PIECES cocok untuk membandingkan sistem lama dengan sistem baru (dipakai skripsi HRM dan Fisioterapi). Di sini sistem lamanya tidak ada; patokannya instrumen monev.
- **Tanpa activity diagram as-is:** prosesnya memang belum ada (temuan A4: tidak ada daftar induk, tinjau ulang, distribusi). Menggambar alur yang tidak ada berarti mengarang.

### 2.2 Usulan Solusi (±9 hal)

| Subbab | Isi | Sumber | Beban |
|---|---|---|---|
| 2.2.1 Gambaran Solusi | Posisi modul dalam FIKLAB Compliance, Odoo 17 Community, dan addon `labfik_core` + `labfik_org` (1 gambar arsitektur addon) | brief, kontrak-core §1 | 1,5 hal, 1 gambar |
| 2.2.2 Fitur Utama | Empat area (struktur, pengendalian dokumen, rencana, status monev) + mekanisme pengesahan bersama; ditandai Inti/Pelengkap. Ditutup tabel **masalah → tujuan → fitur** (M1–M4) | brief "Cakupan rancangan", kebutuhan §4.1 | 2,5 hal, 1 tabel |
| 2.2.3 Kebutuhan Sistem | Kebutuhan fungsional diringkas per area (bukan 45 baris KF), kebutuhan nonfungsional, tabel kriteria instrumen → kebutuhan | kebutuhan §2–4.2 | 3 hal, 2–3 tabel |
| 2.2.4 Metode Pengembangan dan Perancangan | Metode pengembangan **[KONFIRMASI: belum diputuskan]**; metode rancangan OOAD Wazlawick (2024) dengan urutan langkahnya (1 gambar alur) | brief, CLAUDE.md §4 | 1,5 hal, 1 gambar |
| 2.2.5 Platform dan Modul yang Diperluas | `hr`, `mail` (LGPL-3); alasan memperluas, bukan membuat dari nol | brief "Platform dan addon" | 0,5 hal |

**Alasan:**
- **Urutan solusi → fitur → kebutuhan → metode → teknologi** mengikuti pola mayoritas skripsi terdahulu, jadi mudah diikuti penguji.
- **Tabel masalah → tujuan → fitur wajib ada:** proposal ditolak bila solusi tidak menjawab masalah (Pedoman TA).
- **KF diringkas:** daftar 45 KF lengkap terlalu panjang untuk badan bab. Daftar lengkapnya masuk lampiran.
- **Metode rancangan dijelaskan di sini:** penguji perlu tahu mengapa diagram di 2.3 berbeda dari skripsi lain (ada state machine dan SSD, tidak ada use case Login atau CRUD per menu). Rubrik "kesesuaian metode" berbobot 30, terbesar.

### 2.3 Rancangan Proyek (±28 hal)

| Subbab | Isi | Sumber | Gambar |
|---|---|---|---|
| 2.3.1 Proses Bisnis | **Activity:** A1 Pengesahan Dokumen, A2 Siklus SOP/IK, A3 Siklus Rencana, A4 Siklus Struktur. **State machine:** S1 status dokumen disahkan, S2 kemutakhiran versi SOP/IK, + tabel status × transisi S1 | proses-bisnis | 6 |
| 2.3.2 *Use Case* | Tabel aktor (dengan aktor abstrak dan Penjadwal); 3 diagram per paket; **tabel deskripsi use case** untuk 19 UC non-CRUDL/non-report; satu paragraf pola «CRUDL» dan «report» | use-case, expanded-use-case §3, §5 | 3 |
| 2.3.3 Aturan Bisnis | Katalog AB ringkas per kelompok (pengesahan, SOP/IK, rencana, umum) | expanded-use-case §2 | 0 |
| 2.3.4 *System Sequence Diagram* | SSD-1 s.d. SSD-8 (UC-01, 03, 05, 15, 18, 23, 25, 28), tiap gambar dengan eksepsi yang merujuk AB | ssd §2 | 8 |
| 2.3.5 *Design Class Diagram* | (a) mixin Core dan inheritance; (b) model `labfik_org` per area; penjelasan Template Method pengesahan + hook; tabel model → `_inherit` → label [M]/[T] | design-class §2, §4 | 3–4 |

**Alasan:**
- **Isi 2.3 = empat diagram yang diminta di Pedoman/CLAUDE.md §9** (activity + state machine, use case, SSD, DCD). Semuanya sudah jadi, jadi bab ini tinggal narasi.
- **Proses bisnis didahulukan:** use case diturunkan dari activity dan state machine. Urutan bab mengikuti urutan penurunan supaya keterlacakannya terlihat.
- **Tabel deskripsi use case** adalah praktik umum di skripsi terdahulu (Santoso, Natasha) dan mudah dibaca penguji. Alur lengkap expanded use case terlalu rinci untuk badan bab; dipakai sebagai dasar SSD dan 2.4.
- **Aturan bisnis diberi subbab sendiri:** eksepsi SSD dan skenario uji 2.4 merujuk kode AB, jadi pembaca perlu katalognya lebih dulu.
- **Hanya 8 SSD, bukan satu per fitur:** SSD dibuat untuk use case kunci (Wazlawick Bab 7). Skripsi terdahulu yang membuat SSD untuk Login dan setiap CRUD menghabiskan 20–40 halaman tanpa informasi baru.
- **DCD jadi puncak bab:** inheritance adalah permintaan eksplisit pembimbing. Penjelasan per kelas cukup lewat tabel model ditambah narasi mixin, tidak perlu satu paragraf per kelas (cara Aura memakan ±5 hal untuk 13 kelas).
- **Tanpa rancangan antarmuka** (arahan Pak Widi): proyek memodifikasi modul Odoo yang memakai tampilan standar (form, list, kanban). Skripsi terdahulu yang menggambar semua halaman (Raihan 59 hal, Nurul 94 hal) membangun antarmuka dari nol; modul ini tidak.

**Tidak dimasukkan ke badan bab** (bahan kerja, cukup di lampiran atau tidak sama sekali):
- *Conceptual model*: tahap antara menuju DCD; isinya sudah tercermin di DCD.
- Katalog operasi dan kamus DTO: rincian teknis SSD.
- Pemetaan AB → mekanisme Odoo: bahan Bab implementasi (skripsi), bukan proposal.
- Diagram ERD: Odoo membangkitkan tabel dari model, jadi DCD sudah mencukupi.

### 2.4 Rencana Pengujian (±5 hal)

| Subbab | Isi | Sumber | Beban |
|---|---|---|---|
| 2.4.1 Pengujian *Black Box* | Tabel skenario: No, Aktor, UC, Skenario, Data Masukan, Hasil Diharapkan. Alur utama + eksepsi dari 7 UC kunci, ±25 skenario, ditandai kode AB | expanded-use-case §4 | 3 hal, 1 tabel |
| 2.4.2 Pengujian Kecocokan Status Monev | Status hitungan sistem dibandingkan hitungan manual pada data uji | brief "Evaluasi" | 0,5 hal |
| 2.4.3 *User Acceptance Testing* | Uji penerimaan oleh KaLab, laboran, asisten; kuesioner SUS (pembanding Anandar 2026 = 81,88) | brief "Evaluasi" | 1 hal |
| 2.4.4 Uji Alur Dokumen Nyata | Minimal satu SOP lab nyata melewati alur sampai disahkan | brief "Evaluasi" | 0,5 hal |

**Alasan:**
- **Black box dengan pasangan berhasil/gagal** adalah pola tetap skripsi terdahulu. Di sini skenario gagal diambil dari eksepsi E dan kode AB, bukan dikarang, sehingga setiap aturan bisnis teruji.
- **Uji kecocokan status (2.4.2)** khas modul ini: klaim "sistem menunjukkan kriteria tertinggi" perlu dibuktikan.
- **Uji alur dokumen nyata (2.4.4)** menjawab temuan A2 (SOP ada tetapi tanpa nomor dan tanggal efektif).
- **Tanpa *white box*:** fokus proposal pada fungsi dan kesesuaian dengan instrumen, dan sebagian besar logika ditangani ORM Odoo.

---

## 3. Ringkasan beban

| Subbab | Halaman | Gambar | Tabel utama |
|---|---|---|---|
| 2.1 | ±6 | 0 | 3 |
| 2.2 | ±9 | 2 | 4 |
| 2.3 | ±24 | 20–21 | 4 |
| 2.4 | ±5 | 0 | 1–2 |
| **Total** | **±44** | **±22** | **±12** |

## 3a. Urutan penulisan

2.1 menunggu wawancara KaLab dan laboran, jadi urutannya: **2.3 → 2.2 → 2.4 → 2.1**. Sesuai arahan Pak Widi 13 Nov 2026 (TO-BE dulu).

| Urutan | Bagian | Bergantung pada wawancara? |
|---|---|---|
| 1 | 2.3 Rancangan Proyek | Tidak. Semua diagram sudah jadi |
| 2 | 2.2 Usulan Solusi | Sebagian. Tabel masalah → tujuan → fitur memakai M1–M4 dari studi dokumen; ditandai **[KONFIRMASI wawancara]** |
| 3 | 2.4 Rencana Pengujian | Tidak. Diturunkan dari expanded use case |
| 4 | 2.1 Observasi | Ya. 2.1.1 dan 2.1.3 bisa didraf dari studi dokumen; 2.1.2 dan 2.1.4 dilengkapi setelah wawancara |

Bila jawaban wawancara bertentangan dengan temuan studi dokumen, ubah dulu brief dan kebutuhan, baru 2.2–2.3 (urutan sumber kebenaran, CLAUDE.md §3).

## 4. Gaya yang dipakai (dari pola skripsi terdahulu)

- Setiap gambar: kalimat pengantar → gambar → paragraf "Berdasarkan Gambar 2.n, …" (0,5–1 hal).
- Sitasi hanya di kalimat definisi pembuka setiap teknik: **satu sitasi per teknik** (Wazlawick 2024 sebagai rujukan utama; ISO/IEC 17025 untuk pengendalian dokumen). Penjelasan diagram dan keputusan rancangan ditulis sebagai keputusan penulis, tanpa sitasi berulang (pola skripsi referensi FIK).
- Subjek "penulis", kalimat formal; istilah asing dicetak miring.
- Nomor gambar dan tabel per bab (Gambar 2.1, Tabel 2.1).
- Narasumber disebut dengan jabatan, tanpa nama dari dokumen nyata (CLAUDE.md §3).

## 5. Yang perlu diputuskan

| # | Hal | Dampak ke kerangka |
|---|---|---|
| 1 | Metode pengembangan (Scrum, prototipe, atau lainnya) **[KONFIRMASI pembimbing]** | Isi 2.2.4 |
| 2 | Wawancara KaLab sudah atau belum **[KONFIRMASI]** | 2.1.1–2.1.2: ada kutipan narasumber atau murni studi dokumen |
| 3 | ~~Rancangan antarmuka~~ | **Diputuskan:** tidak perlu (Pak Widi). 2.3.6 dihapus |
| 4 | Conceptual model dimasukkan atau cukup di lampiran **[USULAN PENULIS: lampiran]** | +2–3 hal di 2.3 |
