# Kerangka Bab II Rancangan Proyek: Modul Pelaksanaan Praktikum

18 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20
**Status: DRAF**, garis besar. Mengikuti pola [kerangka Bab II Tata Kelola](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/penulisan-skripsi/draft/kerangka-bab-2-tata-kelola.md) (Febriyan, 16 Nov 2026) supaya Bab II anggota kelompok seragam. Isi paragraf ada di [bab-2-praktikum.md](bab-2-praktikum.md); naskah yang sama sudah dimasukkan ke tab "BAB 2" Google Docs proposal.

Acuan format: Pedoman TA FIK 2025 bagian 4.2.2 (Prototipe/Proyek, pendekatan UML): 2.1 Observasi, 2.2 Usulan Solusi, 2.3 Rancangan Proyek, 2.4 Rencana Pengujian.

**Perubahan 18 Nov 2026 (versi kedua):** struktur 2.3 diubah menjadi tujuh subbab A–G (arsitektur, proses bisnis, *use case*, *expanded use case* + aturan bisnis, SSD, *conceptual model*, DCD) mengikuti misi penulisan Bab II. SSD dan *conceptual model* yang sebelumnya dikeluarkan dari naskah dimasukkan kembali. Bila pembimbing meminta naskah tanpa SSD, hapus 2.3.5 beserta Gambar 2.12–2.16 dan Tabel 2.20, lalu nomori ulang.

---

## 1. Patokan beban

Patokan dari 13 Bab II skripsi terdahulu ([bab-2-references.md](../reference/bab-2-references.md)) sudah diukur di kerangka Tata Kelola: median ±58 halaman, ±34 gambar, dan 0,5–1,5 halaman penjelasan per gambar.

**Naskah modul ini: ±15.000 kata (±50 halaman), 25 gambar, 25 tabel.** Masih di bawah median gambar karena tidak ada diagram CRUD dan rancangan halaman.

---

## 2. Kerangka

Kolom **Sumber** menunjuk artefak yang sudah ada. Bab ini menarasikan artefak itu; tidak ada rancangan baru.

### 2.1 Observasi (*as-is*)

| Subbab | Isi | Sumber | Tabel |
|---|---|---|---|
| 2.1.1 Metode Observasi | Studi dokumen D1–D5 (sifat nyata/draf ditandai), telaah Instrumen Monev 2026 dan ISO/IEC 17025. Wawancara KaLab dan laboran **[KONFIRMASI: belum dilakukan]** | [bedah-dokumen-praktikum.md](../../analisis/bedah-dokumen-praktikum.md) §1, brief | 2.1 |
| 2.1.2 Kondisi Saat Ini | Temuan *as-is* per area: prosedur, jadwal, modul, kesiapan, bahan, pelaksanaan, penilaian, kepuasan | bedah-dokumen, brief | 2.2 |
| 2.1.3 Kesenjangan terhadap Instrumen | PKG → kriteria → kondisi saat ini → kesenjangan | analisis PKG-15–20 | 2.3 |
| 2.1.4 Pelaku dan Perannya Saat Ini | Pelaku *as-is* dan posisinya terhadap sistem usulan | bedah-dokumen §2 | 2.4 |

- **Tanpa activity *as-is*:** proses di POB tidak dijalankan seperti tertulis; cukup tabel kesenjangan (sama dengan keputusan Tata Kelola).
- **Data nyata hanya sebagai angka agregat** (CLAUDE.md bagian 3).

### 2.2 Usulan Solusi

| Subbab | Isi | Sumber | Tabel |
|---|---|---|---|
| 2.2.1 Gambaran Solusi | Posisi modul di LabFIK Compliance, Odoo 17 Community | brief | — |
| 2.2.2 Fitur Utama | Fitur per area (Inti/Pelengkap) dan **matriks Masalah → Kebutuhan → Usulan Solusi → Fitur → Package** (M1–M8) | brief "Cakupan rancangan", kebutuhan §4 | 2.5, 2.6 |
| 2.2.3 Kebutuhan Sistem | 52 KF diringkas per kelompok, 15 KNF, keterlacakan kriteria → KF | kebutuhan §2–5 | 2.7, 2.8, 2.9 |
| 2.2.4 Metode Pengembangan dan Perancangan | Metode pengembangan **[KONFIRMASI pembimbing, sama dengan kelompok]**; langkah OOAD Wazlawick (2024), termasuk SSD | CLAUDE.md §4 | 2.10 |
| 2.2.5 Platform dan Modul yang Diperluas | `hr`, `mail`, `survey` (LGPL-3); alasan tidak memakai OpenEduCat | brief | — |

### 2.3 Rancangan Proyek (25 gambar)

| Subbab (bagian misi) | Isi | Sumber | Gambar | Tabel |
|---|---|---|---|---|
| 2.3.1 Arsitektur dan Batas Modul (A) | Susunan addon `labfik_core` → `labfik_sdm` → `labfik_praktikum` + `survey`; pembagian tanggung jawab data dengan modul lain | brief, kontrak Core | — | 2.11, 2.12 |
| 2.3.2 Proses Bisnis (B) | Activity A1–A5, state machine S1–S3, tabel status × transisi Sesi | [proses-bisnis-praktikum.md](../../rancangan/proses-bisnis-praktikum.md) | 2.1–2.8 | 2.13, 2.14 |
| 2.3.3 *Use Case* (C) | Deskripsi aktor, 3 diagram per paket, deskripsi UC non-CRUDL, pola «CRUDL» dan «report» | [use-case-praktikum.md](../../rancangan/use-case-praktikum.md) | 2.9–2.11 | 2.15, 2.16, 2.17 |
| 2.3.4 *Expanded Use Case* dan Aturan Bisnis (D) | Satu alur lengkap (UC-PRK-13) sebagai contoh; katalog AB-PRK diringkas | [expanded-use-case-praktikum.md](../../rancangan/expanded-use-case-praktikum.md) | — | 2.18, 2.19 |
| 2.3.5 *System Sequence Diagram* (E) | SSD lima UC kunci; operasi sistem utama (*command*/*query*) | [ssd-praktikum.md](../../rancangan/ssd-praktikum.md) | 2.12–2.16 | 2.20 |
| 2.3.6 *Conceptual Model* (F) | CM-1 s.d. CM-4; konsep utama | [conceptual-model-praktikum.md](../../rancangan/conceptual-model-praktikum.md) | 2.17–2.20 | 2.21 |
| 2.3.7 *Design Class Diagram* (G) | DCD-1 s.d. DCD-5; *mixin* Core, Template Method + *hook* pengajuan, perluasan `labfik.sesi` dan `survey.survey` | [design-class-praktikum.md](../../rancangan/design-class-praktikum.md) | 2.21–2.25 | 2.22, 2.23 |

- **Urutan subbab = urutan penurunan** (proses bisnis → *use case* → aturan → SSD → CM → DCD), supaya keterlacakan terlihat.
- **DCD jadi puncak bab:** *inheritance* adalah permintaan eksplisit Pak Widi.
- **Tanpa rancangan antarmuka:** modul memakai tampilan standar Odoo (sama dengan keputusan Tata Kelola).
- **Gambar di Google Docs masih berupa penanda** (sorotan kuning) karena API Docs hanya menerima gambar dari URL publik. Gambar siap sisip ada di `gambar-bab-2-praktikum.docx` (folder ini, tidak di-*commit*), urut Gambar 2.1–2.25 dengan judulnya.

**Tidak dimasukkan ke badan bab** (cukup di lampiran): daftar lengkap 52 KF, katalog operasi dan kamus DTO lengkap, pemetaan AB → mekanisme Odoo, ERD (Odoo membangkitkan tabel dari model).

### 2.4 Rencana Pengujian

| Subbab | Isi | Sumber | Tabel |
|---|---|---|---|
| 2.4.1 Pengujian *Black Box* | Kolom: ID, Fitur/*Use Case*, Skenario Pengujian, Kondisi Awal, Input/Tindakan, Hasil yang Diharapkan. Alur utama, varian, dan eksepsi UC kunci + skenario per AB | expanded-use-case §2, §4 | 2.24 |
| 2.4.2 Pengujian Kecocokan Status Monev | Persentase PKG-15–19 dan kriteria tertinggi PKG-20 dibandingkan hitungan manual pada data uji fiktif | KF-PRK-39–41 | 2.25 |
| 2.4.3 *User Acceptance Testing* | Responden dan instrumen **[KONFIRMASI: sama dengan kelompok, mis. SUS]** | brief | — |

Semua skenario berstatus **rencana**; belum ada pengujian yang dijalankan.

---

## 3. Ringkasan isi

| Subbab | Gambar | Tabel |
|---|---|---|
| 2.1 | 0 | 2.1–2.4 |
| 2.2 | 0 | 2.5–2.10 |
| 2.3 | 2.1–2.25 | 2.11–2.23 |
| 2.4 | 0 | 2.24–2.25 |
| **Total** | **25** | **25** |

## 4. Status penulisan

Urutan kerja sama dengan Tata Kelola: **2.3 → 2.2 → 2.4 → 2.1** (arahan Pak Widi: TO-BE dulu; 2.1 menunggu wawancara).

| Bagian | Status |
|---|---|
| 2.1 Observasi | Draf dari studi dokumen saja; dilengkapi setelah wawancara |
| 2.2 Usulan Solusi | Draf. Metode pengembangan masih [KONFIRMASI] |
| 2.3 Rancangan Proyek | Draf lengkap A–G |
| 2.4 Rencana Pengujian | Draf. Responden dan instrumen UAT masih [KONFIRMASI] |
| Google Docs tab "BAB 2" | Teks dan 25 tabel terisi (18 Nov 2026); gambar belum disisipkan |

## 5. Gaya penulisan

- Setiap gambar: kalimat pengantar → gambar → judul dan sumber → paragraf "Berdasarkan Gambar 2.n, …".
- Setiap teknik dibuka dengan definisi singkat bersitasi; rujukan utama Wazlawick (2024).
- Kalimat formal; istilah asing dicetak miring.
- Nama teknis Odoo terutama muncul di 2.3.1 dan 2.3.7; di subbab lain dipakai nama domain.
- Narasumber disebut dengan jabatan. Tidak ada data pribadi.
- Gambar diambil dari halaman diagram (bukan halaman "Catatan … (bahan kerja)") lewat ekspor draw.io.

## 6. Yang perlu diputuskan

| # | Hal | Dampak |
|---|---|---|
| 1 | Metode pengembangan **[KONFIRMASI pembimbing; sebaiknya sama untuk satu kelompok]** | Isi 2.2.4 |
| 2 | Wawancara KaLab dan laboran | 2.1.1–2.1.2, dan asumsi yang ditandai di 2.3 |
| 3 | Judul **[KONFIRMASI Pak Widi]** | Halaman judul; tidak mengubah isi Bab II |
| 4 | SSD dan *conceptual model* tetap di badan bab atau dipindah ke lampiran **[KONFIRMASI pembimbing]** | ±9 gambar dan 2 tabel di 2.3 |
