# Bedah Dokumen Tata Kelola (Studi Dokumen)

13 November 2026, diselaraskan dengan cakupan rancangan 14 November 2026 · Febriyan · Bagian dari proyek LabFIK Compliance · Modul: Tata Kelola & Dokumen (PKG-01, 02, 03, 13)

**Status: DRAF.** Bahan kerja (temuan as-is masuk 2.1 Observasi). Semua usulan model dan field masih **[USULAN PENULIS]** sampai ditetapkan di rancangan (Bab II), dalam batas [cakupan rancangan](../brief/brief-tata-kelola-dokumen.md#cakupan-rancangan) di brief.

## Tujuan

Dokumen ini membedah enam dokumen lab yang diunggah FIKLAB ke web iso.upnvj. Daftarnya ada di sheet `ISO_LAB_SI`, baris 1, 4, 6, 7, 8, dan 9. Setiap bagian dokumen diterjemahkan menjadi **field dan model Odoo** untuk rancangan TO-BE.

Hasilnya dipakai di:

| Bagian proposal | Yang dipakai |
|---|---|
| 2.1 Observasi (studi dokumen) | [Bagian 2: Temuan as-is](#2-temuan-as-is-bahan-21-observasi) |
| 2.2 Usulan Solusi | Pembagian jenis dokumen ([bagian 1](#1-dokumen-yang-dibedah)) |
| 2.3 Rancangan: class diagram | [Bagian 4: Pola berulang → inheritance](#4-pola-berulang--inheritance) dan [bagian 5: Daftar model](#5-daftar-model-to-be-konsolidasi) |
| 2.3 Rancangan: rancangan keluaran | [Bagian 6: Laporan dan ekspor](#6-laporan-dan-ekspor-r) |
| Lampiran | Seluruh dokumen ini sebagai hasil studi dokumen |

## Aturan baca

- **Urutan sumber kebenaran tetap berlaku:** Instrumen Monev dan ISO 17025 → brief → analisis → dokumen ini. Kalau format dokumen lab bertentangan dengan kriteria instrumen, instrumen yang diikuti.
- **Draf GPT hanya acuan format**, bukan sumber kebutuhan dan bukan bukti kondisi nyata. Field dari draf GPT dipakai **hanya bila** juga didukung instrumen atau analisis. Kolom "Dasar" di tiap tabel menunjukkan dukungannya.
- **Dokumen nyata memuat nama orang.** Nama tidak disalin ke sini. Yang dicatat hanya jabatan, nomor dokumen, dan struktur.
- Label entitas `[T]`/`[M]`/`[R]` dan nama master mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md#4-konvensi-penamaan) bagian 4.
- Nama model memakai prefiks `labfik.` (addon `labfik_org`). Nama teknis field ditulis dalam bahasa Indonesia agar mudah ditelusuri ke dokumen sumber **[USULAN PENULIS]**.

---

## 1. Dokumen yang dibedah

| ID | Dokumen | Baris sheet | Sifat | Tanggal / periode | PKG | Jenis di TO-BE |
|---|---|---|---|---|---|---|
| D1 | Renstra 2027–2031 dan RKT 2027 Lab Informatika (kode FIK-LI-RENSTRA-RKT-001) | 1 | Draf GPT, belum disahkan | Renstra 2027–2031, RKT 2027 | 01, sebagian 13 | **Renstra: jarang berubah** (berlaku 5 tahun), diunggah dan disahkan. **RKT: rutin**, diisi lewat sistem, diekspor |
| D2 | Sasaran Kerja dan IKU Lab Informatika (FIK-LI-IKU-001) | 4 | Draf GPT, belum disahkan | 2027 | 01 | Bukan dokumen tersendiri: definisi indikator masuk master KPI, target per periode masuk item RKT |
| D3 | Kumpulan POB Lab FIK (pemeliharaan alat, peminjaman ruang, pengajuan layanan server) dan POB K-004 fakultas (peminjaman sarpras kampus) | 6 | **Nyata** | 2023–2024 | 02 | **Jarang berubah**: diunggah, dikendalikan versinya |
| D4 | Instruksi Kerja Lab Informatika (FIK-LI-IK-001) | 7 | Draf GPT, belum disahkan | Dibuat 20 Okt 2026 | 02 | **Jarang berubah**: diunggah, dikendalikan versinya |
| D5 | Slide Laboratorium PKKMB FIK | 8 | **Nyata** (bahan presentasi) | 2025 | 03 | Bukan dokumen tata kelola; hanya sumber data jabatan dan ruang |
| D6 | SK Dekan No. 3258/UN61/KP.04.00/2025 tentang Struktur Organisasi dan Tata Kerja FIK | 9 | **Nyata**, ditetapkan Dekan | September 2025 | 03 | Dokumen eksternal (fakultas): diunggah sebagai dasar. SK pengelola lab tersendiri: **rutin per periode [KONFIRMASI]** |

Pembagian jenis mengikuti keputusan 13 November 2026 dan 14 November 2026 (lihat [brief batasan masalah](../brief/brief-tata-kelola-dokumen.md#batasan-masalah) nomor 2–3).

**Tidak ada dokumen khusus untuk PKG-13.** Satu-satunya jejak ada di D1: program P8 "Pengembangan fasilitas" (analisis kebutuhan berbasis utilisasi, risiko, kondisi, dan arah kurikulum). Kebutuhan PKG-13 tetap diturunkan dari instrumen lewat [analisis Pengembangan 13](analisis-data-pengembangan-13.md).

---

## 2. Temuan as-is (bahan 2.1 Observasi)

Temuan di bawah hanya berasal dari isi dokumen. Klaim tentang praktik sehari-hari tetap harus dikonfirmasi lewat wawancara.

| No | Temuan | Sumber | Dampak ke indikator | Status |
|---|---|---|---|---|
| A1 | SOP/POB lab **sudah ada sejak 2023–2024**, minimal tiga POB lab dan satu POB fakultas | D3 | PKG-02: SOP tersedia, jadi masalahnya bukan "tidak ada SOP" | Fakta dokumen |
| A2 | Pada POB lab, kolom **Nomor POB, Tanggal Revisi, dan Tanggal Efektif kosong atau "-"**. Hanya POB K-004 (fakultas) yang lengkap nomor, tanggal, dan pengesahannya | D3 | PKG-02 S2 (disahkan) dan S3 (mutakhir) tidak bisa dibuktikan. Sesuai ISO 17025 8.3.2: status revisi harus teridentifikasi | Fakta dokumen. Ada tidaknya tanda tangan di PDF asli **[VALIDASI]** |
| A3 | Pihak "Disusun/Direview/Disetujui" berbeda antar-POB: ada yang disusun teknisi dan direview KaLab, ada yang disusun dan disetujui KaLab, dan POB fakultas disahkan Dekan | D3 | Pengesah bergantung pada jenis dokumen. Wewenang mengesahkan harus diatur **per jenis dokumen**, bukan satu pengesah tetap | Fakta dokumen |
| A4 | Tidak ditemukan **daftar induk** SOP, jadwal tinjau ulang, maupun rekaman distribusi dan sosialisasi | D3, D4 | PKG-02 S1, S4, S5 belum berbukti | Tidak ditemukan di dokumen yang dibagikan. Belum tentu tidak ada **[KONFIRMASI]** |
| A5 | Proses yang dijalankan memakai **Google Form dan Google Sheets** (peminjaman ruang, jadwal lab, konfirmasi) | D3, D5 | Mendukung pernyataan di brief bahwa bukti tersebar di GForm/Sheets. Proses ini milik modul lain (Praktikum, Aset) | Fakta dokumen |
| A6 | SK SOTK FIK 2025 menetapkan **satu kotak "Kepala Laboratorium"** di bawah Dekan, dengan 11 rincian tugas (a–k), termasuk "menyusun rencana operasional dan pengembangan laboratorium" dan "melaporkan kegiatan sekurang-kurangnya setiap semester kepada Ketua Jurusan" | D6 | PKG-03: tugas KaLab sudah punya dasar resmi. PKG-01/13: kewajiban menyusun rencana dan melapor per semester punya dasar hukum | Fakta dokumen |
| A7 | SK SOTK **tidak mengatur** laboran/PLP, teknisi, asisten, petugas K3, petugas pengganti, maupun matriks kewenangan di dalam lab | D6 | PKG-03 K1–K2: struktur internal lab belum ditetapkan | Fakta dokumen |
| A8 | Struktur internal lab hanya muncul di **slide PKKMB**: 2 KaLab (per prodi: Informatika dan Sistem Informasi), 1 teknisi jaringan, 4 laboran yang dibagi per ruang, dan staf kebersihan | D5 | PKG-03: ada struktur *de facto*, tetapi tidak ada penetapan resmi. Slide bukan bukti yang sah | Fakta dokumen |
| A9 | Ada **dua KaLab** (per prodi), sedangkan SK SOTK hanya menyebut satu "Kepala Laboratorium" | D5, D6 | Model Jabatan harus bisa membedakan jabatan yang sama untuk unit berbeda | Perlu penjelasan **[KONFIRMASI]** |
| A10 | Renstra, RKT, IKU, dan IK masih **draf berstatus "untuk validasi dan pengesahan"**. Tabel baseline dan anggarannya kosong (". . .") | D1, D2, D4 | PKG-01 K1 dan PKG-13 K1 belum terpenuhi | Fakta dokumen |
| A11 | Draf D1–D4 ditulis untuk **"Laboratorium Informatika"** (kode FIK-LI-…), padahal sheet bernama ISO_LAB_SI dan lab dikelola dua prodi | D1–D4 | Perlu diputuskan apakah sistem melayani satu lab FIK atau per lab prodi | **[KONFIRMASI]** |
| A12 | Status "Terverifikasi 100%" di web iso.upnvj tercantum pada semua 23 dokumen, termasuk yang masih draf | Sheet | Status di web tidak bisa dipakai sebagai bukti pengesahan | Fakta dokumen |

**Rumusan as-is ringkas:** dokumen tata kelola LabFIK *ada*, tetapi **tidak terkendali**. SOP lama tidak bernomor dan tidak bertanggal efektif. Struktur lab tidak ditetapkan resmi. Rencana kerja dan IKU masih draf yang belum disahkan. Belum ada daftar induk maupun siklus tinjau ulang. Proses pendokumentasian formal baru mulai dibangun bersamaan dengan monev 2026 (pernyataan Pak Widi saat bimbingan, November 2026).

---

## 3. Bedah per dokumen

Kolom tabel:
- **Bagian:** bagian dokumen sumber.
- **Field (usulan):** nama field di sistem.
- **Model:** model Odoo tujuan.
- **Dasar:** dukungan dari instrumen atau analisis. `Instr` = kriteria/bukti di Instrumen Monev, `ISO` = ISO/IEC 17025, `Format` = hanya untuk kebutuhan layout ekspor.

### 3.1 D1: Renstra dan RKT

D1 menggabungkan rencana strategis (multi-tahun) dan rencana kerja tahunan dalam **satu dokumen**. Di TO-BE keduanya dipisah sesuai sifatnya:
- **Renstra** berlaku 5 tahun, jadi disusun di luar sistem lalu **diunggah dan disahkan**. Sistem hanya menyimpan kepala dokumen (kode, revisi, periode, pengesahan) dan PDF-nya. Bagian isi Renstra (visi, misi, sasaran, program, baseline) tidak dijadikan field.
- **RKT** diisi lewat sistem dan diekspor. RKT dan rencana pengembangan (PKG-13) memakai satu model rencana yang dibedakan `jenis`-nya; Renstra adalah rencana `jenis = strategis` yang hanya berisi unggahan.

**Sampul dan lembar pengendalian**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Nama dokumen | `name` | `labfik.plan` | Format |
| Kode dokumen (FIK-LI-RENSTRA-RKT-001) | `kode_dokumen` | mixin kendali | ISO 8.3.2 |
| Revisi (00) | `revisi` | mixin kendali | ISO 8.3.2 |
| Periode Renstra (2027–2031) | `periode_mulai`, `periode_selesai` | mixin periode | Instr PKG-01 K1 (masih berlaku) |
| Periode RKT (2027) | Rencana `jenis = tahunan` dengan periodenya sendiri | `labfik.plan` | Instr PKG-01 Bukti 2 |
| Tanggal berlaku | `tanggal_berlaku` | mixin kendali | Instr PKG-01 K1 |
| Pemilik dokumen | `unit_pemilik` | mixin kendali | ISO 8.3 |
| Status | `state` | mixin pengesahan | Instr K1 |
| Disusun / Ditinjau / Disahkan (jabatan, nama, tanggal) | `penyusun_id`, `pengesah_id` + tanggal masing-masing. Kolom "Ditinjau" tetap ada di kertas, tidak dicatat sistem (pemeriksaan menyatu dengan pengesahan) | mixin pengesahan | Instr K1, ISO 8.3.2a |
| Tabel riwayat revisi (revisi, tanggal, uraian, disetujui) | Dihasilkan dari rantai revisi | `[R]` | ISO 8.3.2c |

**Isi naratif**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Ringkasan eksekutif | `ringkasan` (Html) | `labfik.plan` | Format |
| Bab I Pendahuluan: latar belakang, tujuan, ruang lingkup | `latar_belakang`, `tujuan`, `ruang_lingkup` (Html) | `labfik.plan` | Format |
| Bab I Referensi; Bab II Landasan tata kelola dan profil unit | **Tidak diambil.** Teks tetap di template ekspor | — | Format |
| Bab II 2.2 Daftar ruang dan fungsi | Diambil dari master **Ruang Lab** | `[R]` dari `labfik.ruang` (Core) | Format |
| Bab III Pendekatan ISO dan PPEPP | Teks tetap di template laporan, tidak diinput | — | Format |
| Bab IV Visi dan misi | **Tidak diambil.** Bagian isi Renstra; ada di PDF unggahan | — | Instr PKG-01 Bukti 1 dipenuhi oleh Renstra yang diunggah dan disahkan |
| Bab X Penutup | **Tidak diambil.** Teks tetap di template ekspor | — | Format |

Bagian naratif RKT cukup empat field teks berformat (Html): ringkasan, latar belakang, tujuan, ruang lingkup. Sistem tidak menilai isinya. Yang dinilai sistem hanya kelengkapan tabel terstruktur di bawah.

**Tabel terstruktur**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| 2.3 Profil dan baseline (data, nilai awal, sumber/verifikasi, PIC) | **Tidak diambil sebagai tabel tersendiri.** Kondisi saat ini untuk PKG-13 dicatat di temuan gap (`kondisi_saat_ini`); nilai awal per indikator di `baseline` item rencana | `labfik.plan.gap`, `labfik.plan.line` | Instr PKG-13 K2 (analisis gap) |
| 4.3 Sasaran strategis (kode S1–S9, sasaran, indikator, target akhir periode) | **Tidak diambil.** Bagian isi Renstra (PDF unggahan). Item RKT merujuknya lewat teks `rujukan_renstra` | — | Instr PKG-01 K2 (tertaut ke Renstra) dipenuhi lewat rujukan teks |
| Bab V Program strategis (P1–P8: kegiatan utama, luaran/bukti, tahapan) | **Tidak diambil.** Bagian isi Renstra (PDF unggahan) | — | Instr PKG-01 Bukti 1 |
| Bab VI RKT (no, kegiatan, target/indikator, waktu, PIC, bukti objektif) | `kegiatan`, `kpi_id`, `target`, `satuan`, `jadwal_mulai`, `jadwal_selesai`, `pic_id`, `bukti_diharapkan`, `anggaran`, `rujukan_renstra` (teks) | `labfik.plan.line` | Instr PKG-01 K2 (sasaran, KPI, target, PIC, jadwal, anggaran, tautan Renstra) |
| 6.1 Jadwal ringkas per triwulan | Dihasilkan dari `jadwal_mulai`/`jadwal_selesai` | `[R]` | Format |
| Bab VII Kebutuhan sumber daya dan anggaran (komponen, contoh kebutuhan, dasar prioritas, estimasi) | `komponen_anggaran` (pilihan) di item rencana. Rekap per komponen dihasilkan | `labfik.plan.line` + `[R]` | Instr PKG-01 K2 (anggaran). D1 merekap per komponen, instrumen meminta anggaran per item. **Keduanya bisa dipenuhi** dengan anggaran per item yang dikelompokkan per komponen |
| 8.1 Definisi indikator (indikator, cara hitung, frekuensi, sumber data) | Diambil dari master **KPI** | `[R]` dari `labfik.kpi` | Instr PKG-01 Bukti 4 |
| 8.2 Register risiko awal | **Tidak diambil.** Register risiko milik baris sheet 2 (di luar 21 indikator; kandidat Pengembangan 23) | — | — |
| 8.3 Evaluasi dan tindak lanjut (tinjauan triwulan, laporan semester, tinjauan manajemen) | Alur, bukan field. Menjadi dasar `labfik.realisasi` dan `labfik.tinjauan` | — | Instr PKG-01 K3–K4 |
| Bab IX Dokumen dan rekaman minimum (kode, dokumen, tujuan, pemilik) | Isi awal (*seed*) **Dokumen Induk** | `labfik.document` | Instr PKG-02 Bukti 1 |
| Lampiran D Format laporan kinerja semester (indikator/program, target, capaian, status, analisis gap, tindak lanjut) | Dihasilkan dari realisasi | `[R]` dari `labfik.realisasi` | Instr PKG-01 Bukti 5 |
| Lampiran E Matriks Renstra–RKT–ISO–AMI | Dihasilkan dari `rujukan_renstra` item rencana (daftar item per rujukan) | `[R]` | Instr PKG-01 Bukti 3 (matriks keterkaitan Renstra) |
| Lampiran F Checklist sebelum pengesahan | Validasi saat tombol "Ajukan" ditekan (field wajib terisi) | Logika di `labfik.plan` | Instr PKG-01 K2 |
| Lampiran A–C Formulir permohonan, serah-terima, ketidaksesuaian | **Tidak diambil.** Milik modul Praktikum, Aset, dan Safety | — | — |

### 3.2 D2: Sasaran Kerja dan IKU

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Kepala dokumen (kode FIK-LI-IKU-001, revisi, status, periode 2027) | **Tidak diambil.** IKU bukan dokumen tersendiri (lihat keputusan di bawah) | — | — |
| 1–3 Tujuan, ruang lingkup, acuan | **Tidak diambil** | — | Format |
| 4 Definisi operasional | Teks tetap di template | — | Format |
| 5 Tabel IKU: sasaran kerja, IKU/indikator, rumus, target, frekuensi, PIC, bukti/rekaman, acuan ISO | **Definisi** (indikator, rumus, frekuensi, PIC, bukti, acuan ISO) masuk master **KPI**. **Target per periode** masuk item rencana | `labfik.kpi` + `labfik.plan.line` | Instr PKG-01 Bukti 4 (KPI dengan definisi, sumber data, target) |
| 6 Indikator prioritas per unit lab | **Tidak diambil** | — | Format saja, tanpa dasar instrumen |
| 7 Tata cara pengukuran: baseline, data "belum tersedia" tidak boleh dianggap tercapai | Field `baseline` di item rencana. Status realisasi punya nilai "belum tersedia" | `labfik.plan.line`, `labfik.realisasi` | Instr PKG-01 K3 |
| 8 Skala status capaian (tercapai, perlu perhatian, tidak tercapai, tidak relevan dengan alasan) | `status_capaian` (pilihan), `alasan_tidak_relevan` | `labfik.realisasi` | Instr PKG-01 K3 |
| 9 Format rekap capaian triwulanan (kode IKU, target periode, capaian, status, analisis/tindakan, PIC & tenggat) | Field realisasi | `labfik.realisasi` | Instr PKG-01 K3 |
| 10–11 Persetujuan dan riwayat revisi | Mengikuti pengesahan RKT | — | ISO 8.3.2 |

**Keputusan model [USULAN PENULIS]:** isi D2 beririsan dengan RKT (keduanya punya indikator, target, dan PIC), jadi D2 tidak dijadikan dokumen tersendiri:
- **Definisi KPI** disimpan sekali di master `labfik.kpi` (memenuhi PKG-01 Bukti 4).
- **Target per periode** ada di item RKT, yang merujuk KPI lewat `kpi_id`.

Instrumen tidak meminta dokumen IKU terpisah, jadi keputusan ini tidak mengurangi bukti.

### 3.3 D3: SOP/POB (nyata)

Isi prosedur **tidak** dimodelkan, karena SOP diunggah sebagai file. Yang diambil hanya **kepala dokumen**, karena itu yang dibutuhkan untuk pengendalian versi.

**Kepala POB lab (format 2024)**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Judul POB | `name` | `labfik.document` (Dokumen Induk) | Instr PKG-02 Bukti 1 |
| Nomor POB | `kode_dokumen` | `labfik.document` | ISO 8.3.2c. **As-is: kosong** (A2) |
| Tanggal pembuatan | `tanggal_dibuat` | `labfik.document.version` | ISO 8.3.2 |
| Tanggal revisi | `tanggal_revisi` | `labfik.document.version` | ISO 8.3.2c. **As-is: "-"** |
| Tanggal efektif | `tanggal_berlaku` | mixin kendali | Instr PKG-02 S2. **As-is: kosong** |
| Direview oleh | `pemeriksa_id` | mixin pengesahan | ISO 8.3.2a |
| Dasar hukum | — (isi file) | — | — |
| Tujuan | `ringkasan` (opsional, untuk pencarian) | `labfik.document` | Format |
| Kualifikasi pelaksana | — (isi file). Kandidat tautan ke syarat kompetensi jabatan **ditunda** | — | Beririsan dengan PKG-04/10 (Zahir) |
| Keterkaitan (POB lain yang terkait) | `dokumen_terkait_ids` (Many2many ke Dokumen Induk) | `labfik.document` | ISO 8.3 (dokumen saling merujuk) |
| Peralatan/perlengkapan | — (isi file) | — | — |
| Peringatan | — (isi file) | — | — |
| Pencatatan dan pendataan (rekaman yang dihasilkan) | `rekaman_dihasilkan` (teks) | `labfik.document` | ISO 8.4. Kandidat tautan ke Dokumen Induk jenis formulir |
| Diagram alur dan uraian prosedur | — (isi file) | — | — |
| Disusun / Direview / Disetujui (jabatan, nama) | `penyusun_id`, `pemeriksa_id`, `pengesah_id` | mixin pengesahan | Instr PKG-02 S2 |

**Kepala POB fakultas (POB K-004)** memakai format lain: nomor POB, tanggal pembuatan, tanggal revisi, tanggal efektif, "Disahkan oleh Dekan". Field-nya sudah tercakup di tabel atas. Ini menunjukkan bahwa **Dokumen Induk juga perlu menampung dokumen fakultas** yang dirujuk lab, dengan `asal = fakultas` dan pengesah eksternal.

**Field tambahan dari instrumen (tidak ada di D3)**

| Field (usulan) | Model | Dasar |
|---|---|---|
| `jenis` (POB/SOP, IK, formulir, dokumen eksternal) | `labfik.document` | Instr PKG-02 |
| `kategori` (tata tertib, praktikum, operasi/manajemen, K3, alat, peminjaman, kedaruratan, limbah) | `labfik.document` | Instr PKG-02 Bukti 2 |
| `dasar_kebutuhan` (kegiatan/risiko yang mewajibkan SOP ini) | `labfik.document` | Instr PKG-02 Bukti 1, S1 |
| `is_wajib` | `labfik.document` | Instr PKG-02 (pembagi persentase) |
| `lokasi_penggunaan_ids` (Ruang Lab, portal) | `labfik.document` | Instr PKG-02 S4 |
| `periode_tinjau_bulan`, `tanggal_tinjau_berikutnya` | mixin kendali | Instr PKG-02 S3 |
| `file_ttd` (PDF bertanda tangan) | mixin pengesahan | Brief batasan 3 |
| Distribusi (versi × lokasi, tanggal, petugas) | `labfik.document.distribution` | Instr PKG-02 S4 |
| Sosialisasi (versi, tanggal, metode, bukti, peserta) | `labfik.document.socialization` | Instr PKG-02 S5 |
| Tinjau ulang (versi, tanggal, peninjau, hasil: tetap berlaku / perlu revisi, catatan) | `labfik.document.review` | Instr PKG-02 S3, ISO 8.3.2b. Tanpa rekaman ini, SOP yang ditinjau tetapi tidak diubah tidak bisa dibuktikan mutakhir |

### 3.4 D4: Instruksi Kerja

Sama seperti SOP, isi IK tidak dimodelkan. Lembar pengendaliannya **lebih lengkap** daripada POB 2024 dan menambah dua hal:

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Kode, revisi, tanggal pembuatan, tanggal efektif ("setelah disahkan"), status | Sama dengan D3 | mixin kendali, pengesahan | ISO 8.3.2 |
| **Unit pemilik** | `unit_pemilik` | mixin kendali | ISO 8.3 |
| **Periode tinjauan** ("minimal tahunan atau saat ada perubahan signifikan") | `periode_tinjau_bulan` + `alasan_revisi` (pilihan: tinjauan berkala, perubahan alat, perubahan metode, perubahan fasilitas, perubahan risiko, perubahan lingkup) | mixin kendali, `labfik.document.version` | Instr PKG-02 S3, ISO 8.3.2b |
| Riwayat revisi (revisi, tanggal, **bagian yang diubah**, uraian, pengesahan) | `bagian_diubah`, `ringkasan_perubahan` | `labfik.document.version` | ISO 8.3.2c |
| 5 Tanggung jawab (pelaku × tanggung jawab) | **Tidak diambil sebagai field.** Menjadi masukan isi **tugas Jabatan** saat menyusun SK pengelola (PKG-03) | Masukan `hr.job` | Instr PKG-03 Bukti 3 |
| 9 Rekaman yang harus dipelihara (rekaman, PJ, lokasi/retensi) | `rekaman_dihasilkan`; kandidat isi awal Dokumen Induk jenis formulir/rekaman | `labfik.document` | ISO 8.4 |
| 6–8, 10–13 Instruksi, darurat, ketidaksesuaian, lampiran | — (isi file) | — | — |

### 3.5 D5: Slide PKKMB

Slide ini bukan dokumen tata kelola. Isinya dipakai sebagai **contoh data** untuk master Jabatan, Personel, dan Ruang Lab.

| Bagian | Yang diambil | Model | Dasar |
|---|---|---|---|
| Daftar ruang (Sekretariat, FIK-Lab 201, 301–304, 401–403) beserta jumlah dan spesifikasi PC | Isi awal master Ruang Lab (kode, nama, fungsi, kapasitas) | `labfik.ruang` (Core) | Master bersama |
| Kepala Laboratorium per prodi (Informatika, Sistem Informasi) | Jabatan "Kepala Laboratorium" dengan `unit` berbeda | `hr.job` | Instr PKG-03. Lihat A9 |
| Teknisi jaringan, laboran per ruang (mis. "Laboran 302–304") | Jabatan "Laboran" dan "Teknisi"; penugasan per ruang di baris SK pengelola (`ruang_ids`) | `hr.job`, `labfik.assignment.line` | Instr PKG-03 Bukti 3 |
| Staf kebersihan | Tidak dimodelkan. Bukan pengelola lab **[ASUMSI]** | — | — |
| Hak dan kewajiban pengguna | Tidak dimodelkan. Isi tata tertib, dokumen terpisah (Dokumen Induk kategori tata tertib) | `labfik.document` | Instr PKG-02 |
| Tautan layanan (lapor kendala, pinjam ruangan, survei, instal software, pinjam 3D printer) | Tidak diambil. Milik modul lain. Dicatat sebagai bukti A5 | — | — |

Nama personel di slide **tidak** dipakai. Data uji memakai nama fiktif.

### 3.6 D6: SK SOTK FIK 2025

D6 adalah dokumen fakultas, bukan dokumen lab. Perannya dua:
1. Sebagai **dokumen eksternal** di Dokumen Induk, yaitu dasar hukum struktur lab.
2. Sebagai **contoh format SK** untuk ekspor SK penetapan pengelola lab (PKG-03 K1).

**Format SK → layout ekspor SK pengelola lab**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Kop (kementerian, universitas, fakultas, alamat) | Teks tetap di template laporan | — | Format |
| Nomor SK | `nomor_sk` | `labfik.assignment` | Instr PKG-03 K1 |
| Tentang (judul) | `name` | `labfik.assignment` | Format |
| Menimbang | `menimbang` (Html) | `labfik.assignment` | Format |
| Mengingat (daftar dasar hukum) | `dasar_hukum_ids` (Many2many ke Dokumen Induk jenis eksternal) + `mengingat` (Html) | `labfik.assignment` | Format; menautkan ke D6 sebagai dasar |
| Memutuskan, KESATU–KEEMPAT | `diktum` (Html). Diktum pencabutan SK lama dihasilkan dari `revisi_dari_id` | `labfik.assignment` | Instr PKG-03 K4 (struktur diperbaiki) |
| Ditetapkan di, tanggal | `tanggal_sah` | mixin pengesahan | Instr PKG-03 K1 |
| Penandatangan (Dekan) | `pengesah_id` | mixin pengesahan | Instr PKG-03 K1 (PJ: Dekan) |
| Tembusan | `tembusan` (teks) | `labfik.assignment` | Format |
| Lampiran I: bagan struktur (garis instruksi dan garis koordinasi) | Dihasilkan dari Jabatan → `atasan_id` (garis instruksi), sebagai daftar hierarki. Garis koordinasi tidak dicatat | `[R]` Bagan organisasi | Instr PKG-03 Bukti 2 |
| Lampiran II: tugas pokok dan fungsi per jabatan (daftar berhuruf a, b, c, …) | `labfik.jabatan.tugas` (anak: urutan, uraian) | `hr.job` | Instr PKG-03 Bukti 3, K2 |

**Isi D6 yang langsung relevan**

| Isi | Dipakai sebagai | Model | Dasar |
|---|---|---|---|
| Rincian tugas Kepala Laboratorium (a–k) | Isi awal tugas jabatan "Kepala Laboratorium". Sumber: D6 | `labfik.jabatan.tugas` | Instr PKG-03 Bukti 3 |
| Garis pelaporan: KaLab melapor tiap semester ke Ketua Jurusan; KaLab di bawah Dekan pada bagan | `atasan_id` pada jabatan KaLab. Jabatan fakultas (Dekan, Ketua Jurusan) dicatat sebagai jabatan **eksternal** (`is_eksternal`) | `hr.job` | Instr PKG-03 K2 (alur pelaporan), ISO 5.5 (posisi lab dalam organisasi induk) |
| Tugas a–b KaLab ("merencanakan kegiatan…", "menyusun rencana operasional dan pengembangan") | Dasar wewenang KaLab sebagai **penyusun** rencana PKG-01 dan PKG-13 | `labfik.jabatan.wewenang` | Instr PKG-01, PKG-13 |
| Tugas j KaLab ("melaporkan kegiatan sekurang-kurangnya setiap semester") | Dasar frekuensi laporan realisasi semesteran | Pengaturan periode lapor | Instr PKG-01 K3 |

**Field tambahan dari instrumen untuk PKG-03 (tidak ada di D6)**

| Field (usulan) | Model | Dasar |
|---|---|---|
| `wewenang_ids` (wewenang × jenis dokumen/tindakan: menyusun, mengesahkan) | `hr.job` | Instr PKG-03 Bukti 4 (matriks kewenangan) |
| `pengganti_id` (jabatan pengganti saat berhalangan) | `hr.job` | Instr PKG-03 K2 (pengganti petugas) |
| `syarat_kompetensi` | `hr.job` | Dipakai PKG-04/14. Pengelolanya disepakati dengan Zahir **[KONFIRMASI]** |
| Rapat koordinasi (tanggal, peserta, agenda, keputusan, notulen) | `labfik.meeting` | Instr PKG-03 K3, Bukti 5 |
| Evaluasi struktur (temuan beban kerja, efektivitas koordinasi, keputusan, tautan ke SK/jabatan yang direvisi) | `labfik.org.evaluation` | Instr PKG-03 K4 |

---

## 4. Pola berulang → inheritance

> Bagian 4 dan 5 adalah **usulan awal** dari studi dokumen. Rancangan final ditetapkan lewat alur Wazlawick (proses bisnis → use case → SSD → conceptual model → design class diagram).

Blok yang sama muncul berkali-kali di dokumen sumber:

| Blok | Muncul di | Jadi |
|---|---|---|
| Kode, revisi, tanggal berlaku, unit pemilik, periode tinjauan | D1, D2, D3, D4 | ~~`labfik.controlled.mixin`~~ tidak dipakai (keputusan 14 November 2026): kode dan siklus tinjau di Dokumen Induk, revisi dan tanggal tinjau di Versi Dokumen |
| Disusun / Disahkan (jabatan, nama, tanggal) + status draf → disahkan. Kolom "Diperiksa" hanya di kertas | D1, D2, D3, D4, D6 | `labfik.approval.mixin` |
| Riwayat revisi (revisi, tanggal, uraian, pengesahan) | D1, D2, D4 | `revisi_dari_id` di tiap model + laporan `[R]` |
| Periode berlaku (2027, 2027–2031, masa SK) | D1, D2, D6 | `labfik.period.mixin` |
| PIC + bukti objektif + tanggal | D1 (RKT), D2 (tabel IKU), instrumen (rapat, sosialisasi, realisasi) | `labfik.evidence.mixin` |
| Status kriteria berurutan K1–K4 | Instrumen PKG-01, 03, 13 | `labfik.criteria.mixin` |

### 4.1 Mixin yang diusulkan [USULAN PENULIS]

Semua mixin adalah `models.AbstractModel` (tidak membuat tabel sendiri). Model konkret memakainya lewat `_inherit = [...]`.

**Catatan (14 November 2026):** tabel ini usulan awal hasil studi dokumen. Rancangan final ada di [design-class-tata-kelola.md](../rancangan/design-class-tata-kelola.md). `labfik.controlled.mixin` **tidak dipakai**, karena kode dan revisi hanya ada di Dokumen Induk/Versi dan SK dengan makna berbeda. Tanggal tinjau pindah ke `labfik.document.version`, dan `mail.activity.mixin` tidak dipakai (tanpa pengingat terjadwal).

| Mixin | Field | Method | Dipakai oleh |
|---|---|---|---|
| ~~`labfik.controlled.mixin`~~ (tidak dipakai) | `kode_dokumen`, `revisi`, `tanggal_berlaku`, `unit_pemilik`, `periode_tinjau_bulan`, `tanggal_tinjau_berikutnya` (compute), `is_perlu_tinjau` (compute) | `_compute_tanggal_tinjau()` | `labfik.document.version`, `labfik.plan`, `labfik.assignment` |
| `labfik.approval.mixin` (turunan `mail.thread`, `mail.activity.mixin`) | `state` (draf, diajukan, disahkan, diganti, dicabut, kedaluwarsa), `penyusun_id`, `pengesah_id`, `tanggal_ajukan`, `tanggal_sah`, `file_ttd` | `action_ajukan()`, `action_kembalikan()`, `action_sahkan()` (memeriksa wewenang jabatan dan keberadaan `file_ttd`), `action_cabut()`, `_cek_kelengkapan()` (di-*override* per model) | `labfik.document.version`, `labfik.plan`, `labfik.assignment` |
| `labfik.period.mixin` | `periode_id` (Periode, Core), `tanggal_mulai`, `tanggal_selesai`, `is_berlaku` (compute) | `_compute_is_berlaku()` | `labfik.plan`, `labfik.assignment`, `labfik.tinjauan` |
| `labfik.evidence.mixin` | `tanggal`, `pelapor_id`, `bukti_ids` (lampiran), `keterangan` | — | `labfik.realisasi`, `labfik.tinjauan`, `labfik.meeting`, `labfik.org.evaluation`, distribusi, sosialisasi, tinjau ulang dokumen |
| `labfik.criteria.mixin` | `kriteria_tertinggi` (compute, 0–4), `status_k1`–`status_k4` (compute) | `_cek_k1()`–`_cek_k4()` (abstrak, di-*override* tiap model) | `labfik.plan` (PKG-01, 13), `labfik.assignment` (PKG-03) |

**Contoh polimorfisme (bahan class diagram dan sequence diagram):** `labfik.criteria.mixin` hanya mendefinisikan *bahwa* ada K1–K4 dan cara menghitung kriteria tertinggi secara berurutan. **Isi** cek K1–K4 berbeda di `labfik.plan` dan `labfik.assignment`, sehingga tiap model meng-*override* `_cek_k1()`–`_cek_k4()`. Hal yang sama berlaku untuk `_cek_kelengkapan()` di mixin pengesahan.

### 4.2 Tiga jenis inheritance Odoo yang relevan

| Jenis | Sintaks | Di modul ini |
|---|---|---|
| **Mixin / abstrak** | `_inherit = ['labfik.approval.mixin', ...]` pada model baru | Semua mixin di 4.1 |
| **Ekstensi model yang sudah ada** (*classical*) | `_inherit = 'hr.employee'` tanpa `_name` baru | Personel (`hr.employee`) dan Jabatan (`hr.job`) diperluas di addon `labfik_core` (keputusan 14 November 2026) |
| **Delegasi** | `_inherits = {'res.partner': 'partner_id'}` | Tidak dipakai. Opsi Personel sebagai model sendiri sudah gugur (keputusan 14 November 2026) |

### 4.3 Satu tahap pengesahan

Semua dokumen sumber memakai tiga kolom tanda tangan: **disusun → diperiksa → disahkan**.

Keputusan (14 November 2026): sistem hanya mencatat **disusun** dan **disahkan**. Pejabat yang mengesahkan dianggap sudah memeriksa isi dokumen, dan catatan pengesahan menjadi buktinya. Kolom "Diperiksa" tetap ada di blok tanda tangan dokumen cetak, tetapi tidak dicatat sebagai tahap atau field. Pejabat penanda tangan (mis. Dekan) tidak memakai sistem; KaLab mencatat pengesahannya.

---

## 5. Daftar model TO-BE (konsolidasi)

Tabel ini menggabungkan hasil bedah dengan entitas di [analisis Pengelolaan 1–3](analisis-data-pengelolaan-1-3.md) dan [analisis Pengembangan 13](analisis-data-pengembangan-13.md). Kolom "Dari dokumen" menunjukkan apakah dokumen sumber memberi masukan baru.

### 5.1 Master

| Model | Label | Nama baku | Field inti | Mixin | PKG | Dari dokumen |
|---|---|---|---|---|---|---|
| `hr.employee` (diperluas di `labfik_core`) | [M] | Personel | Bawaan `hr`: nama, `user_id`, `job_id`, `parent_id`. Tambahan: jenis (dosen, laboran/PLP, teknisi, asisten, petugas K3), unit/prodi. Pihak eksternal tidak dicatat (keputusan 14 November 2026) | — | 03 (dipakai semua) | D5 (jenis teknisi). Asisten lab (mahasiswa) dicatat sebagai `hr.employee` dengan jenis personel *asisten* dan jabatan (`hr.job`) **Asisten Praktikum** (keputusan Febriyan, 14 November 2026) |
| `hr.job` (diperluas di `labfik_core`) + `labfik.jabatan.tugas`, `labfik.jabatan.wewenang` | [M] | Jabatan | nama, kode, `unit` (lab FIK, prodi Informatika, prodi SI, fakultas), `is_eksternal`, `atasan_id`, `pengganti_id`, `syarat_kompetensi`, `dasar_dokumen_id`. Anak: **tugas** (urutan, uraian), **wewenang** (tindakan × jenis dokumen) | — | 03 | D5 (KaLab per prodi), D6 (tugas a–k, garis instruksi, format daftar berhuruf) |
| `labfik.document` | [M] | Dokumen Induk | kode, judul, `jenis`, `kategori`, `asal` (lab/fakultas/universitas), `dasar_kebutuhan`, `is_wajib`, `lokasi_penggunaan_ids`, `dokumen_terkait_ids`, `rekaman_dihasilkan`, `versi_berlaku_id` (compute) | — | 02 | D3 (keterkaitan, pencatatan, POB fakultas), D1 Bab IX (isi awal) |
| `labfik.kpi` | [M] | KPI | kode, nama, sasaran kerja, rumus (pembilang, penyebut), satuan, frekuensi, PIC (jabatan), sumber data/bukti, acuan ISO | — | 01 (dipakai 13, 21) | D2 Bagian 5 |
| `labfik.ruang` | [M] | Ruang Lab | kode, nama, fungsi, kapasitas | — | Core | D1 2.2, D5 |
| `labfik.periode` | [M] | Periode | nama, jenis (tahun anggaran, semester, multi-tahun), mulai, selesai | — | Core | D1, D2 |

### 5.2 Transaksi

| Model | Label | Field inti | Mixin | PKG / kriteria | Dari dokumen |
|---|---|---|---|---|---|
| `labfik.document.version` | [T] | `document_id`, `revisi`, `file`, `tanggal_dibuat`, `tanggal_revisi`, `bagian_diubah`, `ringkasan_perubahan`, `alasan_revisi`, `revisi_dari_id` | controlled, approval | 02 S2, S3 | D3, D4 |
| `labfik.document.distribution` | [T] | versi, lokasi, tanggal, petugas | evidence | 02 S4 | Instrumen |
| `labfik.document.socialization` | [T] | versi, tanggal, metode; anak: peserta | evidence | 02 S5 | Instrumen |
| `labfik.document.review` | [T] | versi, peninjau, `hasil` (tetap berlaku / perlu revisi), catatan. Bila *tetap berlaku*, `tanggal_tinjau_berikutnya` pada versi dihitung ulang dari tanggal tinjauan ini | evidence | 02 S3 | Instrumen, D4 (periode tinjauan) |
| `labfik.plan` | [T] | `jenis` (tahunan, pengembangan), narasi (Html: ringkasan, latar belakang, tujuan, ruang lingkup), `revisi_dari_id`. Renstra menjadi model terpisah `labfik.renstra` (lihat baris berikut). Anak: item, temuan gap | controlled, approval, period, criteria | 01 K1–K2, 13 K1–K2 | D1, D2 |
| `labfik.plan.line` | [T] anak | kegiatan, `kpi_id`, `baseline`, `target`, `satuan`, jadwal mulai/selesai, `pic_id`, `bukti_diharapkan`, `anggaran`, `komponen_anggaran`, `rujukan_renstra` (teks). Khusus pengembangan: `gap_ids`, `nilai_risiko`, `nilai_manfaat`, `prioritas` | — | 01 K2, 13 K2 | D1 Bab VI–VII, D2 Bagian 5 |
| `labfik.plan.gap` | [T] anak | aspek (tridharma, kompetensi, sarana, layanan), kondisi saat ini, kebutuhan/standar, sumber data, uraian gap, lampiran | — | 13 K2 | Tidak ada di dokumen. Dari instrumen |
| `labfik.realisasi` | [T] | `line_id`, periode lapor (triwulan/semester), capaian aktual, anggaran terpakai, `status_capaian` (tercapai, perlu perhatian, tidak tercapai, belum tersedia, tidak relevan), `alasan_tidak_relevan`, analisis/tindakan, PIC tindak lanjut, tenggat | evidence | 01 K3, 13 K3 | D2 Bagian 7–9, D1 Lampiran D |
| `labfik.tinjauan` | [T] | `plan_id`, peserta, ringkasan capaian, keputusan, `rencana_berikut_id`. Anak (pengembangan): ukuran manfaat (indikator, nilai sebelum, nilai sesudah, sumber) | evidence, period | 01 K4, 13 K4 | D1 8.3 (tinjauan manajemen tahunan) |
| `labfik.assignment` | [T] | `nomor_sk`, `name`, `menimbang`, `mengingat`, `dasar_hukum_ids`, `diktum`, `tembusan`, `revisi_dari_id`. Anak: **baris penetapan** (personel, jabatan, `ruang_ids`, mulai, selesai) | controlled, approval, period, criteria | 03 K1 | D6 (format SK), D5 (penugasan per ruang) |
| `labfik.meeting` | [T] | agenda, peserta, keputusan, notulen | evidence | 03 K3 | Instrumen |
| `labfik.org.evaluation` | [T] | temuan beban kerja, efektivitas koordinasi, keputusan, `assignment_baru_id`, `jabatan_direvisi_ids` | evidence | 03 K4 | Instrumen |

### 5.3 Perubahan terhadap analisis sebelumnya

| Perubahan | Alasan | Sumber |
|---|---|---|
| Renstra = model terpisah `labfik.renstra` (approval, period) berisi judul, periode, dan berkas unggahan saja (semula direncanakan sebagai `labfik.plan` jenis strategis; dipisah di langkah 9–10 karena tidak punya item, gap, maupun kriteria); RKT merujuknya lewat teks | Renstra berlaku 5 tahun, cukup diunggah dan disahkan. Analisis Pengelolaan 1 sudah menyediakan jalan pengganti "tautan berupa teks bebas" | Keputusan 14 Nov 2026 |
| Isi D2 (IKU) dibagi ke master KPI dan item RKT | Instrumen tidak meminta dokumen IKU terpisah | D2 |
| Empat field narasi (Html) di rencana | Dokumen rutin diekspor dari sistem, jadi narasi minimalnya disimpan di sistem | Keputusan 13 Nov 2026 |
| Status realisasi bertambah "belum tersedia" dan "tidak relevan (dengan alasan)" | Cegah data kosong dianggap tercapai | D2 Bagian 7–8 |
| Jabatan mendapat `unit`, `is_eksternal`, dan anak `tugas` serta `wewenang` | Ada dua KaLab per prodi. Jabatan fakultas perlu dirujuk sebagai atasan. Format tugas mengikuti SK | D5, D6 |
| Dokumen Induk mendapat `asal`, `dokumen_terkait_ids`, `rekaman_dihasilkan` | POB saling merujuk. Dokumen fakultas ikut dikendalikan | D3 |
| Pengesahan menyimpan dua peran (penyusun, pengesah) + pencatat | Kolom "Diperiksa" di dokumen sumber tidak dijadikan tahap (keputusan 14 Nov 2026) | D1–D4, D6 |
| Wewenang mengesahkan diatur per jenis dokumen | Pengesah berbeda antar-POB | D3 (A3) |
| Ditambahkan di langkah 9–10 (tidak ada di tabel 5.1–5.2): `labfik.approval.log` (riwayat pengesahan), `labfik.tinjauan.manfaat` (ukuran manfaat), `labfik.org.monev` (layanan status monev, tanpa tabel) | Konsep kejadian dan hasil hitung muncul saat conceptual model dan DCD | design-class-tata-kelola.md |

---

## 6. Laporan dan ekspor [R]

Semua laporan dihasilkan sebagai QWeb report (PDF) dari data T dan M. Tidak ada yang diinput ulang.

| Laporan | Isi | Dihasilkan dari | Meniru format | PKG / bukti |
|---|---|---|---|---|
| **Dokumen RKT** | Sampul, lembar pengendalian, narasi, tabel RKT, jadwal triwulan, anggaran per komponen, definisi KPI, riwayat revisi | `labfik.plan` (tahunan) + `labfik.kpi` | D1 Bab VI–VIII | 01 Bukti 2, 4 |
| **Dokumen Rencana Pengembangan** | Analisis gap per aspek, program dengan prioritas, biaya, target, PIC, jadwal | `labfik.plan` (pengembangan) | D1 (struktur umum) | 13 Bukti 1–4 |
| **Laporan capaian triwulan/semester** | Target, capaian, status, analisis, tindak lanjut | `labfik.realisasi` | D2 Bagian 9, D1 Lampiran D | 01 Bukti 5, 13 Bukti 5 |
| **Matriks keterkaitan Renstra** | Rujukan Renstra × item RKT | `labfik.plan.line` | D1 Lampiran E | 01 Bukti 3 |
| **SK Penetapan Pengelola Lab** | Format SK + Lampiran I (bagan) + Lampiran II (tugas per jabatan) | `labfik.assignment` + `hr.job` | D6 | 03 Bukti 1–3 |
| **Bagan organisasi** | Garis instruksi (daftar hierarki) | `hr.job` | D6 Lampiran I | 03 Bukti 2 |
| **Matriks kewenangan** | Jabatan × wewenang | `hr.job` | Instrumen | 03 Bukti 4 |
| **Daftar Induk Dokumen** | Kode, judul, jenis, revisi berlaku, tanggal berlaku, pemilik, tinjau berikutnya, lokasi | `labfik.document` + versi | D1 Bab IX (kolom), ISO 8.3 | 02 Bukti 1 |
| **Riwayat revisi** | Revisi, tanggal, bagian diubah, uraian, pengesah | Rantai `revisi_dari_id` | D1, D2, D4 | 02 Bukti 3 |
| **Status monev** | Persentase SOP wajib yang memenuhi (PKG-02); kriteria tertinggi K1–K4 beserta tautan bukti (PKG-01, 03, 13) | Semua model di atas | Instrumen | Semua |

**Alur ekspor dan pengesahan** (batasan 3 di brief): isi form → *Ajukan* → **ekspor PDF** → tanda tangan manual (KaLab atau Dekan, di luar sistem) → unggah `file_ttd` → KaLab menekan *Sahkan* atau *Kembalikan*. Tombol *Sahkan* hanya aktif bila `file_ttd` ada, dan pengesah yang dicatat harus memegang jabatan yang berwenang untuk jenis dokumen itu. Renstra dan SOP/IK melewati alur yang sama tanpa langkah ekspor.

---

## 7. Yang tidak diambil

| Isi | Dokumen | Alasan |
|---|---|---|
| Register risiko awal | D1 8.2 | Baris sheet 2–3 (risk register) di luar 21 indikator; kandidat Pengembangan 23 |
| Formulir permohonan penggunaan, serah-terima, ketidaksesuaian/insiden | D1 Lampiran A–C, D4 Lampiran A–B | Milik modul Praktikum, Aset, dan Safety |
| Isi prosedur POB dan IK (alur, langkah, mutu baku) | D3, D4 | SOP/IK diunggah, bukan diisi lewat form (keputusan 13 Nov 2026) |
| Instruksi pengujian/kalibrasi, ketertelusuran metrologi | D4 Bagian 7 | Bukan scope modul ini; relevansinya untuk lab komputer pun terbatas |
| Tugas jabatan fakultas selain KaLab (Senat, Dekan, Wakil Dekan, dan lainnya) | D6 Lampiran II | Cukup dicatat sebagai jabatan eksternal tanpa rincian tugas |
| Hak/kewajiban pengguna, tautan layanan | D5 | Isi tata tertib (dokumen tersendiri) dan layanan modul lain |
| Isi Renstra: visi, misi, sasaran strategis, program, baseline | D1 Bab II–V | Renstra berlaku 5 tahun, cukup diunggah dan disahkan (keputusan 14 Nov 2026) |
| Dokumen IKU tersendiri, indikator prioritas per unit | D2 | Definisi masuk master KPI, target masuk item RKT; instrumen tidak meminta dokumen terpisah |
| Tahap "Diperiksa" | D1–D4, D6 | Pemeriksaan menyatu dengan pengesahan (keputusan 14 Nov 2026) |
| Garis koordinasi antarjabatan | D6 Lampiran I | Bagan cukup garis instruksi; koordinasi dibuktikan lewat rapat koordinasi |

---

## 8. Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Renstra yang diunggah boleh dipakai sebagai roadmap PKG-01 sekaligus PKG-13? (Sama dengan pertanyaan di brief.)
- [ ] Sistem melayani **satu lab FIK** atau **per lab prodi** (Informatika, SI)? Draf D1–D4 hanya untuk Lab Informatika. (A11)
- [ ] SK penetapan pengelola lab (PKG-03) termasuk dokumen rutin yang diisi lewat sistem dan diekspor?

**Untuk KaLab/laboran (wawancara)**
- [ ] Apakah POB 2024 di D3 sudah ditandatangani? Mengapa nomor dan tanggal efektifnya kosong? (A2)
- [ ] Apakah ada daftar SOP lain selain yang ada di D3? (A4)
- [ ] Dokumen mana yang disahkan KaLab dan mana yang ditandatangani Dekan? (A3)
- [ ] Bagaimana pembagian tugas kedua KaLab? Siapa pengganti bila KaLab atau laboran berhalangan? (A8, A9)

**Untuk kelompok (Zahir, Herrens)**
- [x] Opsi model Personel: **diputuskan** `hr.employee` dan `hr.job` diperluas di `labfik_core` (14 November 2026). Persetujuan kelompok masih ditunggu. (4.2)
- [x] Asisten lab dicatat sebagai `hr.employee` dengan jenis personel *asisten* dan jabatan (`hr.job`) **Asisten Praktikum**; pihak eksternal tidak dicatat (keputusan 14 November 2026).
- [ ] Mixin di bagian 4.1 ditempatkan di `labfik_core` supaya bisa dipakai modul lain (misalnya pengesahan rencana pelatihan PKG-14)?
