# PRD: MVP Organization Management LabFIK (Pengelolaan 1, 2, 3)

26 Oktober 2026 · Febriyan · Status: **Draf v0.3**

| Versi | Tanggal | Perubahan |
|---|---|---|
| v0.1 | 26 Okt 2026 | Draf awal |
| v0.2 | 26 Okt 2026 | Keputusan platform, master personel, format, periode, dan kondisi FIKLAB dimasukkan |
| v0.3 | 26 Okt 2026 | Struktur ulang: pernyataan masalah, tujuan berpasangan metrik, FR/NFR bernomor, alur mulai dari nol, matriks keterlacakan, matriks hak akses, dataset uji, kriteria rilis. Detail teknis dipindah ke [spesifikasi teknis](spesifikasi-teknis-mvp-pengelolaan-1-3.md) |

**Penanda:** ⚠️ **[VALIDASI]** = butuh keputusan atau konfirmasi · 🔎 **[ASUMSI]** = dipakai sementara agar MVP bisa jalan · **[USULAN PENULIS]** = nilai yang ditetapkan penulis, bukan oleh KaLab atau instrumen.

**Sumber kebutuhan:** hanya Instrumen Monev Laboratorium UPNVJ 2026 v1.1 (kolom Target, Kriteria, Bukti Dukung) dan SNI ISO/IEC 17025:2017. Paket dokumen contoh hasil generate di Drive **tidak** dipakai sebagai sumber kebutuhan. Setiap kebutuhan fungsional bisa ditelusuri ke instrumen lewat [Lampiran A](#lampiran-a-matriks-keterlacakan).

**Dokumen terkait:** [spesifikasi teknis](spesifikasi-teknis-mvp-pengelolaan-1-3.md) · [analisis Pengelolaan 1–3](../analisis/analisis-data-pengelolaan-1-3.md) · [pedoman pengisian sheet](../analisis/pedoman-pengisian-sheet-analisis.md)

---

## 1. Pernyataan masalah

Mulai 2026 LabFIK dinilai dengan Instrumen Monev Laboratorium UPNVJ. Tiga indikator tata kelolanya meminta lab membuktikan bahwa ia punya **struktur, aturan, dan rencana** yang disahkan, dijalankan, dan dievaluasi:

| Indikator | Tuntutan | Jenis skor |
|---|---|---|
| **Pengelolaan 1** | Rencana kerja tahunan memuat sasaran, KPI, target, anggaran, dan PIC | Kriteria berurutan K1–K4 |
| **Pengelolaan 2** | Seluruh SOP dan instruksi kerja yang diperlukan tersedia, disahkan, mutakhir, dan dapat diakses | Persentase SOP wajib yang memenuhi |
| **Pengelolaan 3** | Struktur organisasi, tugas, wewenang, dan pengganti petugas ditetapkan dan dijalankan | Kriteria berurutan K1–K4 |

**Kondisi saat ini (dikonfirmasi 26 Oktober 2026):** FIKLAB **belum punya** SK pengelola lab, SOP yang disahkan, maupun rencana kerja, dan belum ada format baku rencana kerja. Bila monev dilakukan sekarang, ketiga indikator mendapat **skor 1** karena kriteria pertamanya belum terpenuhi.

**Masalah intinya** bukan bukti yang tersebar, tetapi **belum ada titik awal dan alat yang menuntun lab** menyusun, mengesahkan, menjalankan, dan meninjau ketiga hal tersebut dengan cara yang menghasilkan bukti. Selain itu, dua indikator berbentuk kriteria berurutan, dan kriteria K3 (dijalankan) serta K4 (dievaluasi) hanya bisa dibuktikan dengan **rekaman kegiatan**. Dokumen yang hanya disimpan di folder tidak cukup.

⚠️ **[VALIDASI]** Pernyataan kondisi ini harus dicatat sebagai hasil wawancara KaLab (nama, jabatan, tanggal) agar bisa dikutip di proposal.

## 2. Tujuan, metrik, dan bukan tujuan

### Tujuan dan metrik

| # | Tujuan (hasil) | Metrik | Target |
|---|---|---|---|
| O1 | KaLab bisa membangun struktur, daftar SOP wajib, dan rencana kerja pertama **dari nol** tanpa pendampingan teknis | Tingkat keberhasilan tugas pada skenario UAT S-01 sampai S-06 | ≥ 90% tugas selesai tanpa bantuan |
| O2 | Hanya pemegang jabatan yang berwenang yang bisa mengesahkan dokumen dan rencana | Pengesahan tidak sah pada uji hak akses (TC-AKS) | 0 kasus |
| O3 | Status ketiga indikator selalu sesuai aturan instrumen | Kecocokan status sistem dengan *test oracle* dataset skenario ([Lampiran D](#lampiran-d-dataset-skenario-uji)) | 100% cocok |
| O4 | Bukti satu indikator bisa ditunjukkan kepada penilai dengan cepat | Waktu tugas "tunjukkan bukti Pengelolaan 2 untuk SOP X" saat UAT | ≤ 3 menit, median |
| O5 | Sistem layak dipakai pengguna lab | System Usability Scale | ≥ 70 (pembanding: Anandar 2026 = 81,88) |
| O6 | Sistem dipakai pada dokumen nyata, bukan hanya data uji | Jumlah dokumen nyata yang melewati alur sampai *berlaku* selama pilot | ≥ 1 SOP nyata dan 1 draf SK/struktur nyata |

Responden UAT ⚠️ **[VALIDASI]**: KaLab (1), laboran/PLP (minimal 2), asisten (minimal 3).

### Bukan tujuan

- Menjamin skor monev naik. Sistem adalah alat pencatatan, pembuktian, dan pemantauan.
- Menulis isi SOP di dalam Odoo. Isi SOP tetap ditulis di Word atau Docs.
- Penganggaran rinci dan integrasi keuangan.
- Integrasi dengan sistem kepegawaian universitas, LeADS, atau SIMPEL.
- Indikator lain. MVP hanya **menyediakan** master personel, jabatan, periode, dan ruang untuk dipakai indikator lain nanti.
- Tanda tangan digital. Pengesahan dibuktikan dengan PDF bertanda tangan yang di-*upload* dan catatan siapa yang menekan "Sahkan".
- Menilai kualitas isi (misalnya "KPI terukur", "SOP sesuai risiko"). Itu tetap tugas penilai.

## 3. Pengguna dan peran

| Peran | Login? | Yang dilakukan |
|---|---|---|
| **Admin LabFIK** | Ya | Instalasi, master awal, impor personel, pemetaan jabatan → grup akses, pengaturan |
| **KaLab** | Ya | Menetapkan daftar SOP wajib, mengesahkan atau menolak SOP dan rencana kerja, memimpin rapat dan tinjauan |
| **Laboran/PLP** | Ya | Menyusun draf SOP, mencatat distribusi dan sosialisasi, melaporkan realisasi |
| **Pengguna Lab** (asisten, dosen) | Ya | Membaca dokumen berlaku; menjadi peserta sosialisasi dan rapat |
| **Penilai** (GKM, asesor monev) | Ya | Melihat status kepatuhan dan bukti; mengisi skor akhir indikator kriteria berurutan |
| **Dekan/Dekanat** | 🔎 **[ASUMSI]** Tidak | Menandatangani SK dan rencana kerja di luar sistem. Dicatat sebagai personel tanpa akun; PDF bertanda tangannya di-*upload* KaLab atau Admin |

## 4. Ruang lingkup

| Masuk MVP | Di luar MVP (ditunda) |
|---|---|
| Alur mulai dari nol (*checklist* awal, jabatan standar, kerangka SOP) | Delegasi wewenang otomatis saat petugas berhalangan |
| Master personel, jabatan, periode, ruang | Analisis beban kerja rinci (jam kerja, FTE) |
| SK penetapan berperiode dan sinkronisasi hak akses | Persetujuan bertingkat (penyusun → pemeriksa → pengesah) |
| Register dokumen dengan versi, pengesahan satu tingkat, penolakan | Kuis pemahaman setelah sosialisasi |
| Distribusi, sosialisasi, dan pengingat tinjau ulang | Retensi dan pemusnahan arsip |
| Rencana kerja: form, cetak baku, revisi, realisasi, tinjauan | Realisasi KPI otomatis dari indikator lain (hanya *hook*) |
| Rapat koordinasi dan evaluasi struktur | Bagan organisasi interaktif |
| Halaman status kepatuhan ketiga indikator dan *snapshot* periode monev | *Dashboard* lintas indikator kelompok; *deployment* ke server kampus |

## 5. Kebutuhan fungsional

Prioritas: **M** = Must · **S** = Should · **C** = Could. Kolom "Instrumen" menunjuk butir yang dipenuhi (rinciannya di [Lampiran A](#lampiran-a-matriks-keterlacakan)).

### FR-E · Umum dan mulai dari nol

| ID | Kebutuhan | Prio | Instrumen |
|---|---|---|---|
| FR-E1 | **Checklist mulai**: halaman yang menuntun urutan pengisian (jabatan → personel → SK → daftar SOP wajib → rencana kerja) dengan tanda selesai/belum | M | Pendukung semua |
| FR-E2 | **Jabatan standar** terpasang saat instalasi: KaLab, Laboran/PLP, Dosen, Asisten Praktikum, Petugas K3, masing-masing dengan uraian tugas kosong yang wajib dilengkapi | M | P3 Bukti 3 |
| FR-E3 | **Kerangka SOP baku** (sampul: kode, judul, versi, pengesah, tanggal berlaku; bab: tujuan, ruang lingkup, langkah, rekaman) tersedia untuk diunduh | S | P2 Bukti 2 |
| FR-E4 | **Impor personel** dari CSV | M | Pendukung |
| FR-E5 | **Master Periode**: tahun akademik dengan semester Ganjil/Genap, tanggal mulai dan selesai | M | P1 K1–K4, P3 K3–K4 |
| FR-E6 | **Master Ruang**: kode, nama, lokasi; ditambah entri non-ruang (misalnya "Portal LabFIK") untuk distribusi | M | P2 S4 |
| FR-E7 | **Pengaturan ambang** yang bisa diubah KaLab (lihat §8.3) | M | Pendukung |

### FR-A · Struktur dan akses (Pengelolaan 3)

| ID | Kebutuhan | Prio | Instrumen |
|---|---|---|---|
| FR-A1 | **Master Personel**: nama, jenis (dosen/tendik/mahasiswa/eksternal), NIP/NIM, akun login (opsional), aktif | M | Fondasi |
| FR-A2 | **Master Jabatan**: nama, uraian tugas, kewenangan, jabatan atasan, jabatan pengganti, grup akses | M | P3 Bukti 3–4, K2 |
| FR-A3 | **SK Penetapan**: nomor, tanggal, pengesah (personel), masa berlaku, status, **tautan ke entri register dokumen** (file tidak disimpan dua kali); baris personel–jabatan dengan tanggal mulai dan selesai | M | P3 Bukti 1, K1 |
| FR-A4 | **Sinkronisasi akses**: saat baris personel–jabatan aktif dan personel punya akun, pengguna masuk grup jabatan; saat periode berakhir atau SK dicabut, ia dikeluarkan. Setiap perubahan grup tercatat | M | P3 K3 |
| FR-A5 | **Laporan cetak**: bagan organisasi (hierarki jabatan dan pemangkunya) dan matriks kewenangan | M | P3 Bukti 2, 4, K2 |
| FR-A6 | **Rapat koordinasi**: periode, tanggal, agenda, peserta, keputusan, notulen | M | P3 Bukti 5, K3 |
| FR-A7 | **Evaluasi struktur**: periode, temuan beban kerja dan koordinasi, keputusan, tautan ke SK atau jabatan yang direvisi | M | P3 K4 |
| FR-A8 | **Aturan konsistensi**: jabatan tidak boleh menjadi penggantinya sendiri; jabatan aktif tanpa pemangku ditandai; personel nonaktif tidak bisa ditetapkan | M | P3 K2 |
| FR-A9 | Rekap beban kerja per personel | C | P3 K4 |

### FR-B · Pengendalian dokumen (Pengelolaan 2)

| ID | Kebutuhan | Prio | Instrumen |
|---|---|---|---|
| FR-B1 | **Daftar Induk Dokumen**: kode, judul, jenis (SOP/IK/formulir/dokumen eksternal), kategori, dasar kebutuhan, lokasi penggunaan (ruang), wajib ya/tidak, pemilik | M | P2 Bukti 1, S1 |
| FR-B2 | **Versi dokumen**: nomor revisi, file, ringkasan perubahan, status `draf → diajukan → berlaku → dicabut`, plus **`ditolak`** (kembali ke draf dengan alasan wajib); pengesah, tanggal sah, tanggal tinjau berikutnya | M | P2 Bukti 2–3, S2–S3 |
| FR-B3 | **Aturan versi**: hanya satu versi *berlaku* per dokumen; mengesahkan versi baru otomatis mencabut versi lama; file versi *berlaku* terkunci | M | P2 Bukti 3, S2 |
| FR-B4 | **Distribusi**: versi × lokasi, tanggal, petugas | M | P2 Bukti 3, S4 |
| FR-B5 | **Sosialisasi**: versi, tanggal, metode, bukti; daftar peserta | M | P2 Bukti 3, S5 |
| FR-B6 | **Halaman dokumen berlaku**, bisa difilter per ruang dan kategori, terbuka untuk semua pengguna internal | M | P2 S4 |
| FR-B7 | **Pengingat tinjau ulang** untuk pemilik dokumen menjelang tanggal tinjau | S | P2 S3 |
| FR-B8 | **Dokumen eksternal** (SK Dekan, rencana kerja bertanda tangan) disimpan di register yang sama | M | P1 Bukti 2, P3 Bukti 1 |
| FR-B9 | **Kunci daftar wajib** per periode monev: setelah tanggal kunci, daftar SOP wajib tidak bisa diubah untuk periode itu | S | P2 (pembagi "ditetapkan sebelum monev") |

### FR-C · Rencana kerja (Pengelolaan 1)

| ID | Kebutuhan | Prio | Instrumen |
|---|---|---|---|
| FR-C1 | **Master KPI**: kode, nama, definisi, pembilang, penyebut, satuan, sumber data | M | P1 Bukti 4 |
| FR-C2 | **Sasaran Renstra**: tingkat (UPNVJ/UPPS/prodi), kode, uraian, dokumen sumber. Bila belum ada data, cukup teks bebas di item | M | P1 Bukti 3, K2 |
| FR-C3 | **Rencana kerja**: jenis (strategis/tahunan), periode, pemilik, narasi, status `draf → diajukan → disahkan → selesai` plus `ditolak`; pengesah; tautan ke PDF bertanda tangan di register | M | P1 Bukti 1–2, K1 |
| FR-C4 | **Item rencana**: sasaran, tautan Renstra, KPI, target, satuan, PIC (personel), jadwal, anggaran | M | P1 Bukti 3–4, K2 |
| FR-C5 | **Cetak rencana kerja** dengan format usulan baku, termasuk matriks keterkaitan Renstra | M | P1 Bukti 2–3 |
| FR-C6 | **Revisi rencana yang sudah disahkan**: membuat versi baru (salinan) yang harus disahkan ulang; versi lama berstatus *diganti* dan tetap tersimpan | M | P1 K1 |
| FR-C7 | **Realisasi**: per item per semester; nilai capaian, anggaran terpakai, bukti, pelapor | M | P1 Bukti 5, K3 |
| FR-C8 | **Laporan pelaksanaan**: target vs realisasi per item | M | P1 Bukti 5, K3 |
| FR-C9 | **Tinjauan**: tanggal, peserta, ringkasan, keputusan; keputusan bisa ditautkan ke item rencana periode berikutnya | M | P1 K4 |
| FR-C10 | *Hook* realisasi otomatis dari modul lain | C | P1 K3 |

### FR-D · Status kepatuhan

| ID | Kebutuhan | Prio | Instrumen |
|---|---|---|---|
| FR-D1 | **Pengelolaan 2**: persentase SOP wajib yang lolos S1–S5, skor 1–4, daftar SOP yang belum memenuhi beserta cek yang gagal | M | P2 Kriteria |
| FR-D2 | **Pengelolaan 1 dan 3**: tangga K1–K4 per periode. Tiap kriteria berlabel **"Lengkap secara data"** atau **"Belum"**, dengan tautan ke rekamannya. Kolom terpisah **"Skor penilai"** diisi oleh Penilai | M | P1, P3 Kriteria |
| FR-D3 | Satu menu "Status Monev Tata Kelola" yang menampilkan ketiga indikator | M | — |
| FR-D4 | **Snapshot periode monev**: membekukan status dan daftar bukti pada tanggal tertentu, sehingga perubahan setelahnya tidak mengubah hasil monev | S | — |

## 6. Kebutuhan non-fungsional

| ID | Kebutuhan |
|---|---|
| NFR-01 | Antarmuka dalam Bahasa Indonesia |
| NFR-02 | **Jejak audit**: semua transaksi mencatat siapa mengubah apa dan kapan; file versi *berlaku* tidak bisa diganti (ISO/IEC 17025 7.5.2, 8.3.2) |
| NFR-03 | **Privasi**: NIP/NIM hanya terlihat oleh Admin dan KaLab; data demo dan repositori hanya berisi data fiktif |
| NFR-04 | **Backup**: prosedur backup basis data dan *filestore* terdokumentasi, dan pemulihan diuji minimal satu kali |
| NFR-05 | **Lingkungan dapat direproduksi**: satu perintah `docker compose up`; versi image dikunci |
| NFR-06 | **Kinerja**: halaman status terbuka < 3 detik pada dataset uji (≤ 100 dokumen, ≤ 50 personel) |
| NFR-07 | **Peramban**: Chrome dan Firefox versi terbaru di desktop. Di HP cukup untuk membaca dokumen berlaku |
| NFR-08 | **Modular**: modul berprefiks `labfik_`, tanpa ketergantungan ke modul Rafika atau OpenEduCat |
| NFR-09 | **Teruji**: setiap aturan di §8 punya unit test |
| NFR-10 | **Cetak PDF** menampilkan karakter dan format tanggal Indonesia dengan benar |

## 7. User stories

Format: *Sebagai [peran], saya ingin [aksi], supaya [manfaat].* Story kritis memakai kriteria penerimaan Given/When/Then.

### Mulai dari nol

**US-01** (FR-E1, E2, E4) · Sebagai **Admin**, saya ingin mengikuti *checklist* mulai dan mengimpor personel dari CSV, supaya lab bisa mulai tanpa input satu per satu.
- *Given* modul baru terpasang, *when* Admin membuka menu LabFIK, *then* tampil *checklist* dengan 5 langkah dan semuanya berstatus "belum".
- *Given* file CSV berisi 10 personel valid, *when* diimpor, *then* 10 personel tercipta dan langkah "personel" bertanda selesai.

### Struktur dan akses

**US-02** (FR-A1, A2, A8) · Sebagai **Admin**, saya ingin melengkapi jabatan dengan tugas, wewenang, atasan, dan pengganti, supaya struktur jelas.
- Jabatan yang menunjuk dirinya sendiri sebagai pengganti ditolak dengan pesan kesalahan.

**US-03** (FR-A3, B8) · Sebagai **KaLab**, saya ingin mencatat SK penetapan beserta daftar personel–jabatan, supaya struktur resmi tersimpan dengan riwayatnya.
- SK tidak bisa *berlaku* tanpa tautan ke PDF di register dan tanggal sah.

**US-04** (FR-A4) · Sebagai **KaLab**, saya ingin hak akses mengikuti jabatan secara otomatis.
- *Given* personel A punya akun dan ditetapkan sebagai KaLab mulai hari ini, *when* SK disahkan, *then* A masuk grup KaLab dan tombol "Sahkan" terlihat olehnya.
- *Given* periode jabatan A berakhir kemarin, *when* sinkronisasi harian berjalan, *then* A keluar dari grup KaLab dan perubahan tercatat.

**US-05** (FR-A5) · Sebagai **Penilai**, saya ingin mencetak bagan organisasi dan matriks kewenangan.

**US-06** (FR-A6, A7) · Sebagai **KaLab**, saya ingin mencatat rapat koordinasi dan evaluasi struktur, supaya bukti K3 dan K4 tersedia.

### Pengendalian dokumen

**US-07** (FR-B1, B9) · Sebagai **KaLab**, saya ingin menetapkan daftar SOP wajib untuk periode monev, supaya penyebut skor jelas dan tidak berubah setelah dikunci.

**US-08** (FR-B2) · Sebagai **Laboran**, saya ingin meng-*upload* draf SOP dan mengajukannya.

**US-09** (FR-B2, B3) · Sebagai **KaLab**, saya ingin mengesahkan atau menolak versi SOP.
- *Given* SOP X punya versi 1.0 *berlaku* dan versi 1.1 *diajukan*, *when* KaLab menekan "Sahkan" pada 1.1, *then* 1.1 menjadi *berlaku*, 1.0 menjadi *dicabut*, dan tanggal tinjau 1.1 = tanggal sah + siklus tinjau.
- *Given* versi 1.1 *diajukan*, *when* KaLab menekan "Tolak" tanpa alasan, *then* sistem meminta alasan; dengan alasan, status kembali ke *draf*.
- *Given* versi *berlaku*, *when* siapa pun mencoba mengganti file, *then* sistem menolak.
- *Given* pengguna tanpa grup KaLab, *then* tombol "Sahkan" dan "Tolak" tidak tampil.

**US-10** (FR-B4, B5) · Sebagai **Laboran**, saya ingin mencatat distribusi dan sosialisasi SOP.

**US-11** (FR-B6) · Sebagai **asisten**, saya ingin melihat SOP berlaku untuk ruang tempat saya bertugas.

**US-12** (FR-B7) · Sebagai **pemilik dokumen**, saya ingin diingatkan menjelang tanggal tinjau ulang. *(Should)*

### Rencana kerja

**US-13** (FR-C1–C4) · Sebagai **KaLab**, saya ingin menyusun rencana kerja tahunan lewat form.
- Rencana tidak bisa diajukan bila ada item tanpa KPI, target, PIC, jadwal, anggaran, atau sasaran Renstra (teks bebas pun boleh).

**US-14** (FR-C3, C5, B8) · Sebagai **KaLab**, saya ingin mencetak rencana kerja dengan format baku, lalu meng-*upload* versi bertanda tangan.
- Status *disahkan* membutuhkan tautan ke PDF bertanda tangan di register.

**US-15** (FR-C6) · Sebagai **KaLab**, saya ingin merevisi rencana yang sudah disahkan, supaya perubahan di tengah tahun tetap tercatat.
- Revisi membuat versi baru berstatus *draf*; versi lama tetap *disahkan* sampai versi baru disahkan, lalu menjadi *diganti*.

**US-16** (FR-C7, C8) · Sebagai **PIC item**, saya ingin melaporkan realisasi per semester beserta buktinya.

**US-17** (FR-C9) · Sebagai **KaLab**, saya ingin mencatat tinjauan akhir tahun dan menautkan keputusannya ke rencana tahun depan.

### Status kepatuhan

**US-18** (FR-D1) · Sebagai **KaLab atau Penilai**, saya ingin melihat skor Pengelolaan 2.
- *Given* dataset skenario D-1 ([Lampiran D](#lampiran-d-dataset-skenario-uji)), *when* halaman status dibuka, *then* tampil 6/10 = 60%, skor 1, dan empat SOP gagal beserta ceknya (S2, S3, S4, S5).

**US-19** (FR-D2) · Sebagai **Penilai**, saya ingin melihat tangga K1–K4 Pengelolaan 1 dan 3, lalu mengisi skor akhir.
- *Given* K1 dan K2 lengkap tetapi K3 belum, *then* K4 ditampilkan "tidak dihitung" walaupun datanya ada.
- Label yang tampil adalah "Lengkap secara data", bukan "Memenuhi".

**US-20** (FR-D4) · Sebagai **KaLab**, saya ingin membekukan status pada tanggal monev. *(Should)*

## 8. Aturan bisnis

### 8.1 Pengelolaan 2: satu SOP wajib memenuhi bila lolos semua cek

| Cek | Aturan |
|---|---|
| S1 Terdaftar | Ada di daftar induk dengan `wajib = ya` untuk periode monev |
| S2 Disahkan | Punya versi *berlaku* dengan pengesah dan tanggal sah |
| S3 Mutakhir | `tanggal tinjau berikutnya ≥ tanggal penilaian` |
| S4 Tersedia | Versi berlaku terdistribusi ke **semua** lokasi penggunaan di daftar induk |
| S5 Tersosialisasi | Ada minimal satu sosialisasi untuk versi berlaku |

**Skor:** `% = SOP wajib memenuhi ÷ seluruh SOP wajib`. 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70% → 1. Bila penyebut 0, tampil **N/A**, bukan 100%.

### 8.2 Pengelolaan 1 dan 3: kriteria berurutan

| | Pengelolaan 1 | Pengelolaan 3 |
|---|---|---|
| K1 | Ada rencana *disahkan* (dengan PDF bertanda tangan) yang periodenya mencakup tanggal penilaian | Ada SK *berlaku* (dengan PDF) yang punya minimal satu baris personel–jabatan aktif |
| K2 | Semua item punya KPI, target, PIC, jadwal, anggaran, dan sasaran Renstra | Semua jabatan aktif punya uraian tugas, kewenangan, atasan (kecuali puncak), pengganti, dan minimal satu pemangku |
| K3 | Setiap item punya realisasi berbukti sesuai ambang §8.3 | Rapat koordinasi sesuai ambang §8.3 |
| K4 | Ada tinjauan di periode itu, dan minimal satu keputusan tertaut ke rencana berikutnya | Ada evaluasi struktur di periode itu |

- Kriteria berikutnya **tidak dihitung** bila kriteria sebelumnya belum lengkap.
- Sistem menampilkan **kriteria tertinggi yang lengkap secara data**.
- **Skor akhir diisi Penilai**, karena kualitas isi tidak bisa dinilai mesin.

### 8.3 Periode dan ambang

**Periode = tahun akademik** (keputusan 26 Okt), dibagi Ganjil dan Genap.

⚠️ **[VALIDASI]** Anggaran kampus umumnya mengikuti tahun anggaran (Januari–Desember). Bila Dekanat menyusun anggaran per tahun anggaran, rencana kerja berbasis tahun akademik bisa tidak sinkron. Master Periode dibuat mendukung kedua jenis, supaya perubahan keputusan murah.

Ambang berikut adalah **[USULAN PENULIS]** dan disimpan sebagai pengaturan yang bisa diubah KaLab:

| Ambang | Nilai awal |
|---|---|
| P1 · K3 | Setiap item punya minimal 1 realisasi berbukti pada setiap semester yang sudah berjalan |
| P3 · K3 | Minimal 1 rapat koordinasi per semester yang sudah berjalan |
| P1 · K4, P3 · K4 | Minimal 1 tinjauan/evaluasi per tahun akademik |
| P2 · S3 | Siklus tinjau ulang SOP 12 bulan |
| Pengingat tinjau | 30 hari sebelum tanggal tinjau |

### 8.4 Kasus pinggir

| Kasus | Perilaku |
|---|---|
| Personel dinonaktifkan | Baris jabatan aktifnya diakhiri hari itu; aksesnya dicabut saat sinkronisasi |
| Satu orang memegang dua jabatan | Mendapat gabungan grup kedua jabatan |
| Jabatan aktif tanpa pemangku | Ditandai; P3 K2 belum lengkap |
| Admin mengubah grup pengguna secara manual | Sinkronisasi hanya mengelola grup yang dipetakan dari jabatan; grup lain tidak disentuh |
| SOP dihapus dari daftar wajib setelah dikunci | Ditolak untuk periode yang terkunci |
| Rencana tanpa item | Tidak bisa diajukan |

## 9. Risiko dan dependensi

| Risiko / dependensi | Dampak | Mitigasi |
|---|---|---|
| **Adopsi**: tidak ada yang menyusun dokumen nyata selama pilot | UAT hanya memakai data fiktif; argumen manfaat lemah | Target O6: minimal 1 SOP nyata dan 1 draf struktur nyata, disusun bersama laboran |
| **KaLab satu-satunya pengesah** | Titik sempit; proses berhenti bila KaLab berganti atau sibuk | Jabatan pengganti dipakai sebagai pengesah cadangan (ditunda); catat sebagai keterbatasan |
| FIKLAB belum punya SK, SOP, rencana (dikonfirmasi) | Status awal semua indikator skor 1; masalah harus dibuktikan wawancara | Wawancara KaLab terdokumentasi; dataset skenario |
| Master personel belum disepakati kelompok | Bentrok dengan Pengelolaan 4, 10, 14, Proses 18 | Model `labfik.personel` sebagai kontrak; sepakati sebelum indikator lain mulai |
| **Integrasi dengan modul Rafika nanti** | Data personel ganda; biaya migrasi | NIP/NIM sebagai kunci unik; field mengacu master Rafika |
| Tahun akademik vs tahun anggaran | Rencana dan anggaran tidak sinkron | Master Periode mendukung kedua jenis (§8.3) |
| Format rencana kerja usulan ditolak Dekanat | Template cetak diganti | Template terpisah; minta masukan KaLab saat UAT |
| Sinkronisasi akses salah | Orang tidak berwenang bisa mengesahkan | Unit test TC-AKS; log perubahan grup |
| Tumpang tindih dengan Pengelolaan 10 (KPI) dan 13 (dokumen mutu), belum ada PIC | Klaim atau pekerjaan ganda | Nyatakan di batasan: komponen KPI dan register dokumen milik MVP ini dan boleh dipakai ulang |
| **Risiko akademik**: dinilai "sekadar CRUD" | Kontribusi dipertanyakan | Bingkai kontribusi sebagai keterlacakan instrumen → bukti → status, dengan Lampiran A sebagai bukti |
| Hal teknis Docker (tag image bergeser, font PDF, volume) | Lingkungan tidak bisa direproduksi | Lihat spesifikasi teknis |
| Paket dokumen hasil generate dipakai sebagai acuan | Fitur berlebihan, tidak bisa dipertanggungjawabkan | Setiap FR wajib punya rujukan instrumen (kolom "Instrumen") |
| Tenggat proposal minggu ke-10 | MVP belum siap sebelum proposal | Proposal cukup memuat rancangan; MVP mengikuti tahapan §12 |

## 10. Log keputusan

| # | Tanggal | Keputusan | Oleh |
|---|---|---|---|
| D1 | 26 Okt 2026 | Platform Odoo 17 **Community** | Febriyan |
| D2 | 26 Okt 2026 | Master personel **dibuat sendiri**, mengacu ke master Rafika | Febriyan (perlu disepakati kelompok) |
| D3 | 26 Okt 2026 | Belum ada format baku rencana kerja; MVP mengusulkan format | Febriyan |
| D4 | 26 Okt 2026 | Periode = **tahun akademik**; ambang memakai batas wajar | Febriyan |
| D5 | 26 Okt 2026 | SK, SOP, dan rencana kerja FIKLAB **belum ada** | Febriyan (perlu dicatat sebagai hasil wawancara) |
| D6 | 26 Okt 2026 | Sumber kebutuhan hanya instrumen dan ISO 17025; paket dokumen hasil generate bukan acuan | Febriyan |
| D7 | 26 Okt 2026 | Master ruang dibuat sendiri (minimal), mengacu `lab.master.ruangan` Rafika | Usulan penulis |
| D8 | 26 Okt 2026 | Skor akhir indikator kriteria berurutan diisi Penilai (semi-otomatis) | Usulan penulis ⚠️ **[VALIDASI]** dosen |

## 11. Pertanyaan terbuka

**Untuk KaLab**
- [ ] Siapa yang akan menyusun dan mengesahkan SK, SOP, dan rencana kerja pertama?
- [ ] SOP apa saja yang menurut KaLab wajib ada?
- [ ] Apakah ada rapat koordinasi rutin?
- [ ] Apakah anggaran lab disusun per tahun anggaran atau tahun akademik?
- [ ] Bersediakah KaLab dan laboran menyusun 1 SOP nyata selama pilot?

**Untuk dosen dan kelompok**
- [ ] Apakah skor akhir indikator kriteria berurutan boleh diisi penilai (D8)?
- [ ] Satu server Odoo untuk semua kelompok?
- [ ] Kesepakatan model `labfik.personel`, `labfik.jabatan`, `labfik.periode`, `labfik.ruang` dengan Zahir dan Herrens
- [ ] Kapan daftar SOP wajib dikunci sebelum monev (FR-B9)?

## 12. Kriteria rilis dan tahapan

### Kriteria rilis MVP (*Definition of Done*)

- [ ] Semua FR berprioritas **M** lolos *black box testing*
- [ ] Unit test semua aturan §8 lolos
- [ ] Status sistem cocok 100% dengan *test oracle* dataset D-1 sampai D-3
- [ ] UAT selesai dengan responden minimal (KaLab 1, laboran 2, asisten 3) dan SUS terhitung
- [ ] Prosedur backup dan pemulihan diuji sekali
- [ ] `docker compose up` dari repositori bersih menghasilkan Odoo dengan modul dan data demo terpasang

### Tahapan

| Tahap | Isi | Estimasi |
|---|---|---|
| 0 | Docker Compose, kerangka modul, grup akses, master Periode dan Ruang, pengaturan | 1 minggu |
| 1 | FR-A1–A5, A8, FR-E1, E2, E4 (struktur, akses, mulai dari nol) | 2 minggu |
| 2 | FR-B1–B6, B8, FR-D1 (dokumen dan skor Pengelolaan 2) | 2 minggu |
| 3 | FR-C1–C9 (rencana kerja) | 2 minggu |
| 4 | FR-A6–A7, D2–D3, data demo, unit test, dataset skenario | 1–2 minggu |
| 5 | *Should*: FR-B7, B9, D4, E3; black box; UAT | 1–2 minggu |

Estimasi untuk satu orang dan ⚠️ **[VALIDASI]** terhadap jadwal skripsi.

---

## Lampiran A. Matriks keterlacakan

Rantai: **butir instrumen → FR → user story → test case**.

### Pengelolaan 1

| Butir instrumen | FR | US | TC |
|---|---|---|---|
| Bukti 1: roadmap lab | C3 (jenis strategis) | US-13 | TC-P1-01 |
| Bukti 2: rencana kerja tahunan disahkan | C3, C5, B8 | US-14 | TC-P1-02 |
| Bukti 3: matriks keterkaitan Renstra | C2, C4, C5 | US-13, US-14 | TC-P1-03 |
| Bukti 4: KPI dengan definisi, sumber data, target, anggaran | C1, C4 | US-13 | TC-P1-04 |
| Bukti 5: laporan pelaksanaan | C7, C8 | US-16 | TC-P1-05 |
| K1 disahkan dan berlaku | C3, C6 | US-14, US-15 | TC-P1-06 |
| K2 lengkap dan selaras | C4, D2 | US-13, US-19 | TC-P1-07 |
| K3 dijalankan dan tertelusur | C7, D2 | US-16, US-19 | TC-P1-08 |
| K4 ditinjau dan diperbaiki | C9, D2 | US-17, US-19 | TC-P1-09 |

### Pengelolaan 2

| Butir instrumen | FR | US | TC |
|---|---|---|---|
| Bukti 1: daftar induk kebutuhan SOP | B1, B9 | US-07 | TC-P2-01 |
| Bukti 2: SOP per kategori | B1, B2, E3 | US-08 | TC-P2-02 |
| Bukti 3: pengesahan, revisi, distribusi, sosialisasi | B2, B3, B4, B5 | US-09, US-10 | TC-P2-03 |
| Kriteria: disahkan (S2) | B2, B3 | US-09 | TC-P2-04 |
| Kriteria: mutakhir (S3) | B2, B7 | US-12 | TC-P2-05 |
| Kriteria: tersedia di titik penggunaan (S4) | B4, B6 | US-10, US-11 | TC-P2-06 |
| Kriteria: disosialisasikan (S5) | B5 | US-10 | TC-P2-07 |
| Skor persentase | D1 | US-18 | TC-P2-08 |

### Pengelolaan 3

| Butir instrumen | FR | US | TC |
|---|---|---|---|
| Bukti 1: SK/penetapan pengelola | A3, B8 | US-03 | TC-P3-01 |
| Bukti 2: bagan organisasi | A5 | US-05 | TC-P3-02 |
| Bukti 3: uraian tugas KaLab, PLP, dosen, asisten, petugas K3 | A2, E2 | US-02 | TC-P3-03 |
| Bukti 4: matriks kewenangan | A2, A5 | US-05 | TC-P3-04 |
| Bukti 5: bukti koordinasi | A6 | US-06 | TC-P3-05 |
| K1 struktur dan pengangkatan disahkan | A3 | US-03 | TC-P3-06 |
| K2 tugas, wewenang, pelaporan, pengganti lengkap | A2, A8, D2 | US-02, US-19 | TC-P3-07 |
| K3 penugasan dan koordinasi mengikuti struktur | A4, A6, D2 | US-04, US-06 | TC-P3-08, TC-AKS |
| K4 beban kerja dan koordinasi dievaluasi | A7, D2 | US-06, US-19 | TC-P3-09 |

## Lampiran B. Matriks hak akses

C = buat · R = baca · U = ubah · D = hapus · ✔ = aksi khusus · — = tidak ada akses

| Objek | Admin | KaLab | Laboran | Pengguna Lab | Penilai |
|---|---|---|---|---|---|
| Personel (termasuk NIP/NIM) | CRUD | CRU | R (tanpa NIP/NIM) | R (tanpa NIP/NIM) | R (tanpa NIP/NIM) |
| Jabatan | CRUD | CRU | R | R | R |
| SK Penetapan | CRUD | CRU, ✔ Sahkan | R | R | R |
| Daftar Induk Dokumen | CRUD | CRU, ✔ Kunci daftar wajib | CRU (bukan field "wajib") | R | R |
| Versi Dokumen | CRUD | CRU, ✔ Sahkan/Tolak | CRU (status draf), ✔ Ajukan | R (hanya *berlaku*) | R |
| Distribusi, Sosialisasi | CRUD | CRU | CRU | R | R |
| KPI, Sasaran Renstra | CRUD | CRU | R | — | R |
| Rencana dan Item | CRUD | CRU, ✔ Ajukan/Sahkan/Tolak/Revisi | R | — | R |
| Realisasi | CRUD | CRU | CRU (item yang ia PIC-i) | — | R |
| Tinjauan, Rapat, Evaluasi | CRUD | CRU | R | R (rapat yang ia ikuti) | R |
| Status kepatuhan | R | R, ✔ Snapshot | R | — | R, ✔ Isi skor akhir |
| Pengaturan | RU | RU | — | — | — |

Hapus (D) untuk KaLab ke bawah sengaja tidak diberikan. Rekaman dibatalkan lewat status, bukan dihapus, agar jejak audit utuh.

## Lampiran C. Glosarium

| Istilah | Arti |
|---|---|
| **SOP / IK** | Standar Operasional Prosedur / Instruksi Kerja: dokumen berisi langkah melakukan suatu kegiatan |
| **Personel** | Orang yang berperan di lab (siapa) |
| **Jabatan** | Peran atau kursi di struktur lab, beserta tugas dan wewenangnya |
| **SK Penetapan** | Keputusan yang menetapkan personel pada jabatan untuk periode tertentu |
| **Versi berlaku** | Satu-satunya versi dokumen yang sah dipakai saat ini |
| **K1–K4** | Kriteria berurutan Pengelolaan 1 dan 3: ditetapkan → lengkap → dijalankan → dievaluasi |
| **S1–S5** | Cek pemenuhan satu SOP wajib: terdaftar, disahkan, mutakhir, tersedia, tersosialisasi |
| **Lengkap secara data** | Status yang dihitung sistem: data dan bukti yang diminta sudah ada. Bukan penilaian kualitas |
| **Skor penilai** | Skor 1–4 yang ditetapkan penilai setelah memeriksa kualitas bukti |
| **Snapshot** | Status dan daftar bukti yang dibekukan pada tanggal monev |
| **Test oracle** | Hasil yang seharusnya, dihitung manual sebelum pengujian, untuk dibandingkan dengan hasil sistem |

## Lampiran D. Dataset skenario uji

Semua data **fiktif**. Hasil yang diharapkan dihitung manual sebelum pengujian (*test oracle*).

### D-1 · Pengelolaan 2, kondisi campuran

10 SOP wajib, tanggal penilaian 1 Juni 2027:

| SOP | Kondisi yang dibuat | Cek gagal |
|---|---|---|
| SOP-01 sampai SOP-06 | Disahkan, tinjau 2028, terdistribusi ke semua lokasi, tersosialisasi | — |
| SOP-07 | Versi masih *diajukan* | S2 |
| SOP-08 | Tanggal tinjau 1 Mei 2027 | S3 |
| SOP-09 | Lokasi penggunaan ruang 301 dan 302, hanya terdistribusi ke 301 | S4 |
| SOP-10 | Belum ada sosialisasi | S5 |

**Hasil yang diharapkan:** 6/10 = 60% → **skor 1**.

### D-2 · Pengelolaan 2, setelah perbaikan

D-1 ditambah: SOP-07 disahkan, SOP-09 didistribusikan ke 302, SOP-10 disosialisasikan.
**Hasil yang diharapkan:** 9/10 = 90% → **skor 3**. Penyebut 0 (tanpa SOP wajib) → **N/A**.

### D-3 · Pengelolaan 1 dan 3, tangga kriteria

| Skenario | Kondisi | Hasil yang diharapkan |
|---|---|---|
| D-3a | Rencana disahkan dengan PDF; 1 dari 5 item tanpa PIC | P1: K1 lengkap, K2 belum → kriteria tertinggi K1 |
| D-3b | D-3a dengan PIC dilengkapi; realisasi semester Ganjil ada untuk 5 item; belum ada tinjauan | P1: kriteria tertinggi K3 |
| D-3c | SK berlaku; jabatan Petugas K3 tanpa pemangku; ada evaluasi struktur | P3: kriteria tertinggi K1 (K4 tidak dihitung karena K2 belum) |
| D-3d | D-3c dengan Petugas K3 diisi; 1 rapat per semester; evaluasi ada | P3: kriteria tertinggi K4 |

### D-4 · Hak akses (TC-AKS)

| Skenario | Hasil yang diharapkan |
|---|---|
| Laboran mencoba mengesahkan SOP | Tombol tidak tampil; panggilan langsung ditolak |
| Periode jabatan KaLab A berakhir | Setelah sinkronisasi, A tidak bisa mengesahkan |
| Personel B memegang Laboran dan Petugas K3 | B mendapat gabungan grup kedua jabatan |
