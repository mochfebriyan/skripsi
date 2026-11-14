# Brief Proyek LabFIK Compliance

1 November 2026 · Febriyan · Menggantikan versi 26 Oktober 2026. Pembagian "Role 1–3" dan scope "8 indikator siklus mutu praktikum" di versi itu **sudah tidak berlaku**.

Dokumen ini menjelaskan proyek secara keseluruhan. Brief dan analisis per modul disimpan di branch pemegangnya. Untuk Tata Kelola & Dokumen: [brief-tata-kelola-dokumen.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/brief/brief-tata-kelola-dokumen.md) di branch `febriyan-skripsi`.

## Ringkasan

- **Apa:** sistem berbasis Odoo untuk Laboratorium FIK UPN "Veteran" Jakarta (LabFIK). Sistem ini mengelola kegiatan lab dan sekaligus menghasilkan bukti untuk **Instrumen Monev Laboratorium UPNVJ 2026 v1.1**.
- **Siapa:** beberapa kelompok skripsi yang dibimbing Pak Widi. Arahan beliau: cakup indikator sebanyak mungkin. Indikator yang tidak tercakup menjadi bahan skripsi tahun berikutnya.
- **Indikator proyek:** **21 indikator**, satu per package (PKG-01 sampai PKG-21). **1 package = 1 indikator.**
- **Cara membagi kerja:** per **modul fungsional**, bukan per aspek monev. Hierarkinya **modul → package (indikator) → entitas**. Satu skripsi memegang satu modul.
- **Kelompok kita:** Febriyan (Tata Kelola & Dokumen), Zahir (SDM & Kompetensi), Herrens (Pelaksanaan Praktikum). Kelompok lain yang sudah tercatat: Wisnu dan Patih (Asset Management dan Safety Management).
- **Status (1 Nov 2026):**
  - Analisis per instrumen dan pemetaan package sudah ada.
  - Belum ada modul yang dibangun.

## Urgensi

- Mulai 2026 LabFIK dinilai dengan Instrumen Monev Laboratorium UPNVJ 2026. Instrumen ini antara lain mengacu ke SNI ISO/IEC 17025:2017. Dasar resmi bahwa audit mengarah ke ISO 17025 belum ditemukan **[KONFIRMASI]**.
- Setiap indikator diberi skor 1–4. **Bukti yang tidak bisa diverifikasi = skor 1**, walaupun kegiatannya sudah dilakukan.
- Saat ini bukti tersebar di Google Form/Sheets, LeADS (LMS kampus), SIMPEL (presensi), dan kertas, atau bahkan belum ada sama sekali. Bukti dikumpulkan manual menjelang monev.

## Indikator proyek

Proyek mencakup **21 indikator**, satu per package. **Nomor PKG adalah identitas resmi indikator di proyek ini.**

**Kenapa memakai nomor PKG?** Sheet instrumen ([docs/Instrumen Monev Laboratorium UPNVJ 2026 v1.1 - PIC dan Data.xlsx](../docs/), tab *Analysis*) berisi 64 baris, tetapi penomorannya tidak rapi:
- Nomor dipakai ganda. Contohnya ada tiga baris "Pengelolaan 10" dan dua baris "Evaluasi 19".
- Sebagian baris tidak punya aspek.
- Sebagian baris berkode Q/E.

Karena itu nomor baris di sheet **jangan dipakai sebagai identitas**. Selalu tulis **PKG-xx + aspek, nomor, dan kata kunci**, misalnya `PKG-10 Pengelolaan 10 (otorisasi)`.

Baris sheet di luar ke-21 indikator ini **tidak dicakup** proyek saat ini. Baris-baris itu kandidat skripsi berikutnya; dugaan package tempelnya ada di [pemetaan package](../analisis/pemetaan-package-instrumen.md) bagian 9.

| PKG | Indikator | Modul | Pemegang |
|---|---|---|---|
| 01 | Pengelolaan 1 (rencana kerja tahunan) | Tata Kelola & Dokumen | Febriyan |
| 02 | Pengelolaan 2 (SOP dan IK) | Tata Kelola & Dokumen | Febriyan |
| 03 | Pengelolaan 3 (struktur organisasi) | Tata Kelola & Dokumen | Febriyan |
| 04 | Pengelolaan 4 (penugasan petugas sesuai kompetensi) | SDM & Kompetensi | Zahir |
| 05 | Pengelolaan 5 (kalibrasi alat ukur) | Asset Management | Kelompok lain |
| 06 | Pengelolaan 6 (sarana keselamatan) | Safety Management | Kelompok lain |
| 07 | Pengelolaan 7 (inventaris alat dan bahan) | Asset Management | Kelompok lain |
| 08 | Pengelolaan 8 (kapasitas sesi) | Asset Management | Kelompok lain |
| 09 | Pengelolaan 9 (limbah) | Safety Management | Kelompok lain |
| 10 | Pengelolaan 10 (otorisasi personel) | SDM & Kompetensi | Zahir |
| 11 | Pengelolaan 11 (penyimpanan bahan) | Safety Management | Kelompok lain |
| 12 | Pengelolaan 12 (pemeliharaan preventif alat) | Asset Management | Kelompok lain |
| 13 | Pengembangan 13 (rencana pengembangan lab) | Tata Kelola & Dokumen | Febriyan |
| 14 | Pengembangan 14 (pelatihan PLP/laboran) | SDM & Kompetensi | Zahir |
| 15 | Persiapan 15 (jadwal dan modul) | Pelaksanaan Praktikum | Herrens |
| 16 | Persiapan 16 (kesiapan alat dan *software*) | Pelaksanaan Praktikum | Herrens |
| 17 | Persiapan 17 (bahan praktikum) | Pelaksanaan Praktikum | Herrens |
| 18 | Proses 18 (sesi terlaksana) | Pelaksanaan Praktikum | Herrens |
| 19 | Evaluasi 19 (penilaian individual praktikan) | Pelaksanaan Praktikum | Herrens |
| 20 | Evaluasi 20 (kepuasan pengguna) | Pelaksanaan Praktikum | Herrens (PIC analisis awal Patih) |
| 21 | Evaluasi 21 (kinerja pemeliharaan) | Asset Management | Kelompok lain (PIC analisis awal Herrens) |

Untuk kelompok kita: Febriyan 4 indikator, Zahir 3, Herrens 6.

**Dua jenis skor:**

| Jenis | Aturan |
|---|---|
| Persentase unit yang memenuhi | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70% → 1 |
| Kriteria berurutan K1–K4 | Skor naik hanya bila kriteria sebelumnya terpenuhi. 4 = K1–K4 · 3 = K1–K3 · 2 = K1 atau K1–K2 · 1 = K1 belum terpenuhi |

**Level cakupan sistem** dipakai supaya klaim tiap skripsi jujur:

| Level | Arti |
|---|---|
| Otomatis | Skor dihitung dari data operasional yang dicatat di Odoo |
| Semi-otomatis | Sistem mengelola alur dan bukti per kriteria. Skor akhir ditetapkan penilai |
| Bukti tertaut | Data utama ada di sistem lain. Odoo hanya menyimpan tautan atau lampiran |

## Modul dan pemegangnya

| Modul | Pemegang | Package (instrumen) | Objek utama |
|---|---|---|---|
| **Core** | Disepakati bersama | PKG-00: master bersama + Sesi | — |
| **Tata Kelola & Dokumen** | **Febriyan** (final, 1 Nov 2026) | 01 rencana kerja · 02 SOP · 03 struktur organisasi · 13 rencana pengembangan | Rencana, dokumen, organisasi |
| **SDM & Kompetensi** | **Zahir** | 04 penugasan petugas · 10 otorisasi · 14 pelatihan | Personel dan kompetensinya |
| **Pelaksanaan Praktikum** | **Herrens** | 15 jadwal & modul · 16 kesiapan alat · 17 bahan · 18 sesi terlaksana · 19 penilaian individual · 20 kepuasan pengguna | Sesi dan kelas |
| Asset Management | Kelompok lain | 05 kalibrasi · 07 inventaris · 08 kapasitas · 12 pemeliharaan · 21 kinerja pemeliharaan | Alat dan bahan |
| Safety Management | Kelompok lain | 06 sarana K3 · 09 limbah · 11 penyimpanan bahan | Bahaya dan keselamatan |

Catatan:
- PIC analisis di sheet tidak selalu sama dengan pemegang modul. Contohnya PKG-16/17 dianalisis Zahir tetapi dipegang Herrens, dan PKG-14 dianalisis Herrens tetapi dipegang Zahir.
- PKG-18 dan PKG-19 dianalisis awal oleh Febriyan, tetapi sekarang dipegang Herrens. Analisis awalnya ada di riwayat git: `git show 62e50ce:projek-fiklab/analisis/analisis-data-proses-18.md`.
- PKG-20 (kepuasan pengguna) masuk Pelaksanaan Praktikum (ditetapkan 1 Nov 2026). PIC analisis awalnya Patih dari kelompok lain.
- Isi tiap package (entitas milik, *import*, dipakai oleh) ada di [pemetaan-package-instrumen.md](../analisis/pemetaan-package-instrumen.md).

### Rencana addon Odoo

Usulannya **1 modul fungsional = 1 addon**, supaya `depends` di manifest sama dengan panah dependensi antarmodul. Status: belum dikonfirmasi ke Pak Widi.

```
labfik_core                  master bersama + Sesi
 ├─ labfik_org               Tata Kelola & Dokumen
 ├─ labfik_sdm               SDM & Kompetensi
 └─ labfik_praktikum         Pelaksanaan Praktikum (depends: sdm)
      └─ labfik_praktikum_aset   jembatan ke addon kelompok Aset
```

**Usulan keputusan (Febriyan, 14 November 2026) [KONFIRMASI kelompok]:** master bersama (Personel, Jabatan, Periode, Ruang) dan mixin bersama ditempatkan di addon **`labfik_core`** tersendiri, terpisah dari `labfik_org`. Personel dan Jabatan meng-*extend* `hr.employee` dan `hr.job` dari Odoo CE `hr` (LGPL-3), mengikuti arahan Pak Widi untuk memperluas addon berlisensi LGPL. Jadi `labfik_core` bergantung pada `hr` dan `mail`, dan modul fungsional cukup bergantung pada `labfik_core`.

## Master bersama (Core) dan dependensi kunci

| Master | Dikelola oleh | Dipakai oleh (package) |
|---|---|---|
| Personel | **PKG-03** (Tata Kelola) | 01, 02, 03, 04, 06, 07, 10, 13, 14, 15, 18, 21 |
| Jabatan (tugas, kewenangan, atasan, pengganti, syarat kompetensi) | **PKG-03** (Tata Kelola) | 01, 02, 03, 04, 13, 14, 18 |
| Dokumen Induk (daftar dokumen terkendali) | **PKG-02** (Tata Kelola) | 02, 03, 09 |
| KPI | **PKG-01** (Tata Kelola) | 01, 21 |
| Kompetensi | PKG-04 (SDM) | 04, 10, 14 |
| Alat, Bahan | PKG-07 (Aset) | 05, 07, 08, 10, 11, 12, 16, 17, 21 |
| Periode, Mata Kuliah, Kelas, Ruang Lab, Mahasiswa | Core | Banyak package |
| Lokasi Penyimpanan, Mitra Eksternal, Indikator Monev | Core (usulan, belum disetujui) | Aset, Safety, *dashboard* |
| **Sesi** (satu-satunya transaksi di Core, *inherit* `op.session`) | Dibangkitkan PKG-15 | 04, 08, 15, 16, 17, 18, 19 |

Hal yang terlihat dari peta dependensi:
- **PKG-03 adalah yang paling hulu.** Personel dan Jabatan dipakai hampir semua package, termasuk milik kelompok lain. Modelnya harus disepakati paling awal.
- **PKG-15 adalah hulu modul praktikum**, karena Sesi yang dibangkitkannya menjadi pembagi PKG-04, 08, dan 18.
- **Interface dengan kelompok lain:**
  - 17 → 07 (stok bahan)
  - 16 → 05 (status kalibrasi)
  - 08 → 15 (Sesi)
  - 08 → 04 (jumlah petugas)
  - 09 → 02 (SOP limbah)

## Kondisi saat ini (ringkas)

| Area | Kondisi | Status |
|---|---|---|
| Tata kelola | FIKLAB **belum punya** SK pengelola lab, SOP yang disahkan, rencana kerja, maupun format baku rencana kerja | Disampaikan lisan 26 Okt 2026; perlu dicatat sebagai hasil wawancara KaLab |
| Pelaksanaan praktikum | Realisasi sesi dilaporkan asisten lewat Google Form "Pelaksanaan Asistensi Praktikum" (±1.100 respons, 4 periode). Rencana ada di sheet "Alokasi Pertemuan Asisten Praktikum" (kolom hari dan jam kosong). Pencatatan dibuat untuk **honor**, jadi kelas tanpa asisten (42–56% kelas) tidak punya rekaman. Cakupan laporan sesi berasisten 64–74% | Dibaca penuh 17 Okt 2026 |
| Penilaian dan presensi praktikan | Penilaian ada di **LeADS**, presensi rinci per praktikan di **SIMPEL**. Keduanya tidak terhubung ke rekaman sesi | Tampilan role dosen belum diketahui |
| Ruang | 8 ruang: FIKLAB-201, 301–304, 401–403 | — |
| Aset | KaLab punya templat *Integrated_Kalibrasi_Inventory_LabFIK_UPNVJ* yang menyiapkan ekspor ke CMDBuild/openMAINT. Bisa beririsan dengan rencana Odoo | Perlu dicek kelompok Aset |

**Privasi:** sheet asisten memuat nama, NIM, nomor HP, dan status rekening/KTP. Nilai mahasiswa juga data pribadi. Data seperti ini **tidak boleh masuk repo**. Data seed dan demo wajib fiktif atau dianonimkan.

## Platform dan kode yang sudah ada

| Kode | Isi | Status |
|---|---|---|
| [`skripsi_rafika/`](../../skripsi_rafika/README.md) | Modul `PendaftaranAsisten` (Rafika Anandar, 2026) di atas OpenEduCat, Odoo 17. Memakai `op.session` untuk sesi bertanggal dan master `mst_*` (dosen, MK, kelas, periode), `lab.master.ruangan` | **Acuan saja**, tidak di-*extend* dan tidak diubah |

## Keputusan yang sudah diambil

| Tanggal | Keputusan |
|---|---|
| Okt 2026 | Satu judul skripsi per orang |
| Okt 2026 | Modul Rafika dijadikan acuan, bukan di-*extend* |
| 26 Okt 2026 | Analisis per instrumen (modul, data, dependensi) dikerjakan **sebelum** pembagian kerja. Pembagian Role 1–3 versi 26 Okt dibatalkan |
| 26 Okt 2026 | Platform Odoo 17 **Community** |
| 26 Okt 2026 | Paket dokumen monev di Drive LabFIK adalah **draf hasil generate GPT**, bukan dokumen nyata FIKLAB. Paket ini bukan sumber kebutuhan |
| 28 Okt 2026 | Pemetaan package: 1 package = 1 instrumen; modul → package → entitas; master bersama di Core |
| 1 Nov 2026 | Pemegang modul: Febriyan = **Tata Kelola & Dokumen** (termasuk PKG-13, sebelumnya PIC analisis Herrens), Zahir = **SDM & Kompetensi**, Herrens = **Pelaksanaan Praktikum** |
| 1 Nov 2026 | PKG-20 (kepuasan pengguna) masuk Pelaksanaan Praktikum |
| 1 Nov 2026 | Proyek mencakup **21 indikator** dengan aturan 1 package = 1 indikator. Nomor PKG menjadi identitas indikator karena penomoran sheet tidak rapi |

## Permasalahan bersama untuk Bab 1

Arahan dosen: **permasalahan awal** di latar belakang semua skripsi FIKLAB Compliance harus selaras, baik kelompok Febriyan/Zahir/Herrens maupun kelompok Wisnu/Patih. Yang disamakan hanya **substansinya**. **Paragrafnya ditulis masing-masing** dari sudut modulnya sendiri, bukan disalin atau diparafrase dari tulisan anggota lain. Setelah paragraf ini, latar belakang tiap skripsi mengerucut ke modulnya.

**Klaim inti yang wajib ada** (boleh diurutkan dan ditekankan berbeda):

| # | Klaim | Sumber |
|---|---|---|
| 1 | Mulai 2026 laboratorium UPNVJ dinilai dengan Instrumen Monev Laboratorium UPNVJ 2026 v1.1, yang antara lain mengacu ke SNI ISO/IEC 17025:2017. Tiap indikator diberi skor 1–4 | Instrumen (dokumen internal UPNVJ); dasar resmi acuan ISO **[KONFIRMASI]** |
| 2 | Bukti yang tidak dapat diverifikasi diberi skor 1, walaupun kegiatannya dilakukan. Yang dinilai adalah bukti, bukan hanya kegiatan | Instrumen, kolom skor 1 |
| 3 | Data dan bukti LabFIK tersebar dan tidak terhubung (Google Form/Sheets, LeADS, SIMPEL, dokumen kertas, file perorangan), atau belum ada | Wawancara KaLab **[KONFIRMASI; saat ini masih keterangan lisan]** |
| 4 | Bukti dikumpulkan dan dihitung manual menjelang monev, sulit ditelusuri ke kegiatan asalnya, dan tidak terpantau sepanjang periode | Wawancara KaLab **[KONFIRMASI]** |
| 5 | Jawabannya adalah proyek bersama FIKLAB Compliance: satu sistem berbasis Odoo, 21 indikator, dibagi per modul fungsional dengan master data bersama | Brief ini |

**Istilah baku:** "FIKLAB Compliance", "Instrumen Monev Laboratorium UPNVJ 2026 v1.1", "21 indikator", dan nama modul sesuai tabel [Modul dan pemegangnya](#modul-dan-pemegangnya).

**Sudut pandang per modul** (contoh, untuk membedakan tulisan):

| Modul | Masalah awal dilihat dari |
|---|---|
| Tata Kelola & Dokumen | Keputusan, dokumen, dan rencana lab yang tidak punya satu tempat terkendali |
| SDM & Kompetensi | Siapa yang ditugaskan dan berwenang, serta bukti kompetensinya |
| Pelaksanaan Praktikum | Sesi, jadwal, dan penilaian praktikan yang terekam di banyak tempat |
| Asset Management | Data alat, bahan, kalibrasi, dan pemeliharaan |
| Safety Management | Sarana keselamatan, limbah, dan penyimpanan bahan |

Hal lain:
- **Modul Anandar (2026)** disebut sebagai rujukan atau gambaran penerapan Odoo di LabFIK, **bukan** sebagai penelitian yang dilanjutkan.
- **Angka khusus satu modul** (misalnya cakupan laporan sesi praktikum) tidak dipakai di paragraf masalah awal. Angka seperti itu masuk paragraf modul masing-masing, dan hanya bila sudah diizinkan KaLab.

## Pertanyaan terbuka tingkat proyek

**Untuk Pak Widi**
- [ ] Apakah "modul" berarti addon Odoo (1 modul = 1 addon), atau cukup pengelompokan logis?
- [ ] Apakah master tambahan Lokasi Penyimpanan, Mitra Eksternal, dan Indikator Monev boleh masuk Core?
- [ ] Apa dasar resmi bahwa monev 2026 mengacu ke ISO/IEC 17025?
- [ ] Apakah semua kelompok memakai satu server Odoo?

**Untuk kelompok**
- [ ] Setuju Personel = `hr.employee` dan Jabatan = `hr.job` yang diperluas di `labfik_core`? (Keputusan Febriyan, 14 November 2026: asisten lab dicatat sebagai `hr.employee` dengan jenis personel *asisten* dan jabatan (`hr.job`) **Asisten Praktikum**; pihak eksternal tidak dicatat sebagai Personel dan bukan aktor.)
- [ ] Setuju `labfik_core` dipisah dari `labfik_org`?
- [ ] Apakah Sesi masuk Core dan dibangkitkan PKG-15?
- [ ] Apakah Persiapan 17 (bahan) dinyatakan N/A untuk lab FIK, atau dicakup terbatas (lab IoT, 3D printer)?

## Peta dokumen

| Dokumen | Isi | Milik |
|---|---|---|
| [brief-seluruh-projek.md](brief-seluruh-projek.md) | Dokumen ini | Bersama |
| [pedoman-pengisian-sheet-analisis.md](../analisis/pedoman-pengisian-sheet-analisis.md) | Cara mengisi sheet analisis, nama master baku, rumus kompleksitas | Bersama |
| [pemetaan-package-instrumen.md](../analisis/pemetaan-package-instrumen.md) + `.drawio` | Modul, package, Core, dependensi | Bersama |
| Brief dan analisis modul Tata Kelola & Dokumen ([brief](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/brief/brief-tata-kelola-dokumen.md), [analisis P1–3](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/analisis/analisis-data-pengelolaan-1-3.md), [analisis Pengembangan 13](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/analisis/analisis-data-pengembangan-13.md)) | Scope, kebutuhan, dan analisis data modul Febriyan | Febriyan (branch `febriyan-skripsi`) |
| [pendahuluan/reference/](../pendahuluan/reference/) | Rujukan Bab 1: Bab 1 skripsi Rafika dan daftar judul skripsi UPNVJ yang terkait proyek | Rujukan |
| [docs/](../docs/) | Instrumen (xlsx), SNI ISO/IEC 17025:2017, Pedoman TA FIK 2025, daftar dosen FIK | Rujukan |
