# Analisis Data Indikator Proses 18 (Sesi Terlaksana)

14 November 2026 · Herrens · PKG-18 Proses 18 (sesi terlaksana) · Modul: Pelaksanaan Praktikum (di sheet: Practicum Management)

**Status: DRAF.** Bahan kerja Langkah 0 (bahan Bab I dan 2.2). Belum dikonfirmasi ke KaLab; wawancara bagian Pelaksanaan Praktikum belum dijawab.

Dokumen ini **menggantikan** analisis awal Proses 18 oleh Febriyan (24 Oktober 2026, `git show 62e50ce:projek-fiklab/analisis/analisis-data-proses-18.md`). Perubahannya: istilah "Role 1/2/3" dan "MVP" diganti dengan modul dan Core yang berlaku sejak 1 dan 14 November 2026, Sesi kini milik `labfik_core`, dan temuan *as-is* dihitung ulang dari data terbaru.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2. Package hulunya dianalisis di [analisis-data-persiapan-15.md](analisis-data-persiapan-15.md); rujukan "PKG-15 A1" berarti temuan A1 di dokumen itu.

---

## Ringkasan

| | Proses 18 |
|---|---|
| Inti | Setiap sesi praktikum yang direncanakan benar-benar terlaksana sesuai jadwal, modul, dan durasi, atau diganti lewat perubahan yang sah |
| PJ (instrumen) | Dosen; KaLab |
| Jenis skor | **Persentase** |
| Unit | 1 sesi praktikum yang direncanakan pada periode monev |
| Level cakupan (usulan) | **Otomatis**. Kesesuaian tujuan sesi tetap dinilai penilai |
| Posisi dalam dependensi | Tengah: butuh Sesi dan Versi Modul dari PKG-15; tidak dipakai package lain (PKG-19 kini memakai tautan LeADS per kelas, bukan Jurnal Sesi) |
| Acuan ISO/IEC 17025 | 7.5.1 (rekaman teknis dibuat pada saat kegiatan) · 7.2.1.3 (versi metode yang berlaku) · 8.4 (pengendalian rekaman) |
| Kompleksitas (kasar) | **6** (rincian di bagian 8) |

**Temuan utama:**
1. **Kelas tanpa asisten tidak punya rekaman apa pun.** Pencatatan saat ini dibuat untuk honor asisten, jadi 42–56% kelas per periode tidak punya rencana sesi maupun laporan (A1). Skor indikator untuk seluruh sesi rencana praktis tidak dapat diverifikasi.
2. **Untuk sesi berasisten pun, cakupan laporannya hanya 64–75%** (A2), setara skor 1–2, dan kualitas rekamannya rendah: laporan ganda, durasi tidak valid, dan pengisian yang terlambat sampai lebih dari 30 hari (A4–A7).
3. **Perubahan sesi tidak tercatat.** Ada 55 laporan yang menyebut sesi daring tanpa catatan persetujuan, dan asisten yang melapor berbeda dari rencana di 70 laporan (A3, A9).

---

## 0. Sumber dan temuan *as-is*

### Dokumen dan data yang dipakai

| Sumber | Sifat | Tanggal | Yang relevan untuk PKG-18 |
|---|---|---|---|
| POB Manajemen Praktikum dan Asistensi FIK (`LABFIK_POB_Praktikum.pdf`) | **Nyata**, belum disahkan | 2025 | Langkah 9–10 (asistensi, presensi dan kendala), 12 (evaluasi kendala), 14 (penyesuaian jadwal), 17 (rekapitulasi); Lembar Pelaksanaan Asistensi; Monitoring Alokasi dan Pelaksanaan Asisten |
| Google Form "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ" (Responses) | **Data nyata** (berisi data pribadi, tidak dikutip) | Diolah penuh 14 Nov 2026: 1.147 laporan, 4 periode, data sampai 10 Nov 2026. Yang dikutip hanya angka agregat | Seluruh kolom laporan sesi |
| Sheet "Alokasi Pertemuan Asisten Praktikum" | **Data nyata** (berisi data pribadi, tidak dikutip) | Diunduh dan diolah penuh 14 Nov 2026 | Rencana sesi berasisten per kelas per pertemuan |
| `brief-role-3.md` (commit `d6fcc5c`) dan brief bersama, bagian Kondisi saat ini | Catatan kelompok | 17–26 Okt 2026 | Presensi rinci di SIMPEL, penilaian di LeADS, lembar kegiatan kertas untuk honor |
| Paket `LABFIK_Paket_Manajemen_Praktikum_2026` (FRM-PRK-03, STD-PRK-01, STD-PRK-05, IK-PRK-01, REG-PRK-01) | **Draf**, kemungkinan hasil GPT **[VALIDASI ke KaLab]** | Sep–Okt 2026 | Contoh format saja |
| Paket Dokumen Monev `DOCUMENTS/19_SOP_Pelaksanaan_Supervisi_Penutupan_Praktikum` | **Draf GPT** | Okt 2026 | Contoh format saja |

Periode 2024/2025 Genap tidak punya tab alokasi, jadi pencocokan rencana ↔ laporan hanya untuk tiga periode. Periode 2026/2027 Ganjil masih berjalan, jadi angkanya bukan *baseline*.

### Temuan *as-is*

| # | Temuan | Sumber |
|---|---|---|
| A1 | Tidak ada sesi bertanggal (PKG-15 A1). Rencana hanya memuat pertemuan **berasisten**: 344 (2025/2026 Ganjil), 644 (2025/2026 Genap), 303 (2026/2027 Ganjil). Kelas tanpa asisten (40 dari 71, 33 dari 79, 40 dari 72) tidak punya rencana per pertemuan maupun laporan, padahal tetap termasuk pembagi indikator | Sheet Alokasi dan Google Form (diolah 14 Nov 2026) |
| A2 | Dari pertemuan berasisten yang direncanakan, yang punya laporan: **258 dari 344 (75%)**, **415 dari 644 (64%)**, dan 76 dari 303 (25%, periode berjalan). Kunci pencocokan: MK + kelas + pertemuan ke- | Sheet Alokasi × Google Form |
| A3 | Ada laporan yang tidak ada di rencana (17, 16, 5 per periode) dan laporan yang asisten pelapornya berbeda dari asisten rencana (3, 47, 20). Penggantian asisten tidak tercatat di mana pun | Sheet Alokasi × Google Form |
| A4 | Laporan ganda untuk MK, kelas, dan pertemuan yang sama: 12 (2024/2025 Genap), 11, 36, 3. Formulir tidak mencegah satu sesi dilaporkan dua kali | Google Form |
| A5 | Durasi tidak valid (jam selesai ≤ jam mulai atau format salah): 38, 26, 69, 15 laporan (148 dari 1.147, 13%). Median durasi 100 menit di 2024/2025 Genap dan 2025/2026 Ganjil, tetapi **50 menit** di 2025/2026 Genap dan 2026/2027 Ganjil. Durasi rencana tidak tercatat, jadi syarat "durasi sesuai" tidak bisa dinilai | Google Form |
| A6 | Keterlambatan pengisian (tanggal kirim − tanggal sesi): median 1, 1, **29,5**, dan 2 hari. Laporan yang dikirim >30 hari setelah sesi: 77, 32, **230**, 5 | Google Form (kolom Timestamp dan Tanggal) |
| A7 | Tanggal tidak konsisten: tahun salah 3, 1, 0, 0; hari tidak cocok dengan tanggal 9, 9, 27, 2. Jam di laporan juga bisa salah isi, sehingga tampak tumpang tindih ruang (PKG-15 A11) | Google Form |
| A8 | Presensi: praktikan hanya **jumlah hadir** (selalu terisi). Dosen hanya ya/tidak (hadir: 50%, 38%, 88%, 89%); rincian "hadir penuh / hadir awal / tidak hadir" baru ada sejak 2026/2027 Ganjil. **Presensi laboran tidak ada sama sekali** | Google Form |
| A9 | 55 laporan menyebut sesi daring/online (24, 3, 26, 2) tanpa catatan persetujuan. POB 2025 langkah 14 menyerahkan penyesuaian jadwal kepada asisten; "Formulir Penyesuaian Jadwal Praktikum" disebut tetapi tidak dilampirkan | Google Form (kolom topik dan kendala); POB 2025 |
| A9a | Jadwal kelas praktikum tetap selama satu semester (hari dan jam yang sama untuk 16 pertemuan), kecuali ada **perubahan dari dosen pengampu**, misalnya kelas menjadi daring atau jadwal dipindah. Jadi dalam praktik pengaju perubahan adalah dosen, bukan asisten seperti tertulis di POB langkah 14 | Keterangan Herrens, 14 Nov 2026 **[KONFIRMASI wawancara P12]** |
| A10 | Kolom "Status" berisi TRUE/FALSE (18 FALSE di 2024/2025 Genap, sisanya TRUE atau kosong). Diduga tanda verifikasi untuk rekap honor **[VALIDASI ke laboran]** | Google Form |
| A11 | Penomoran pertemuan tidak konsisten: rencana memakai 8 = UTS dan 16 = UAS, tetapi ada laporan "pertemuan 8" (14 dan 4 laporan) dan "pertemuan 16" (1 dan 1) | Sheet Alokasi × Google Form |
| A11a | Pertemuan 8 (UTS) dan 16 (UAS) **tetap berlangsung di kelas** pada jadwal yang sama, berupa ujian atau presentasi proyek. Laporan "pertemuan 8" dan "16" di A11 adalah sesi UTS/UAS, bukan salah nomor. Karena itu pembagi PKG-18 mencakup 16 sesi per kelas, dan Sesi diberi jenis pertemuan (praktikum / UTS / UAS) | Keterangan Herrens, 14 Nov 2026 |
| A12 | Topik dan jumlah hadir selalu terisi; foto terisi di semua laporan kecuali 2024/2025 Genap (210 dari 312); kendala diisi di 66, 55, 62, 14 laporan | Google Form |
| A13 | Lembar Pelaksanaan Asistensi POB 2025 memuat: pertemuan, hari/tanggal, nama dosen, nama asisten, paraf dosen, paraf asisten, topik, modul, waktu mulai, ruang, jumlah, kendala; ditandatangani Koordinator Prodi, Dosen Koordinator, dan KaLab. Lembar Monitoring Alokasi dan Pelaksanaan mencatat A (alokasi) dan L (laporan) per pertemuan, diparaf laboran | POB 2025 lampiran |
| A14 | Presensi rinci per praktikan dicatat dosen di **SIMPEL**; penilaian di **LeADS**. Keduanya tidak terhubung ke laporan sesi | Brief bersama, Kondisi saat ini **[KONFIRMASI: tampilan dan hak akses role dosen/KaLab]** |
| A15 | Lembar kegiatan kertas diisi bersamaan dengan formulir, hanya sebagai bukti fisik pengajuan honor; isinya tidak memuat rincian kegiatan sehingga tidak bisa dipakai sebagai *log book* | `brief-role-3.md` (commit `d6fcc5c`) **[KONFIRMASI: sumber pernyataan]** |
| A16 | Lembar Pelaksanaan Asistensi POB 2025 hanya punya kolom **waktu mulai**, tanpa waktu selesai, sehingga durasi tidak bisa dihitung dari lembar itu | POB 2025 lampiran (studi dokumen, [bedah-dokumen-praktikum.md](bedah-dokumen-praktikum.md) A15) |
| A17 | Rekap keterlaksanaan sudah dibutuhkan tetapi dibuat manual: lembar Monitoring Alokasi dan Pelaksanaan (A vs L per pertemuan, diparaf laboran) dan tab rekap "Per Pertemuan", "Per Asisten", "Per Mata Kuliah" di sheet respons formulir | POB 2025 lampiran; Google Form (studi dokumen A16) |

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Sesi praktikum terlaksana sesuai jadwal, modul, dan waktu kegiatan yang ditetapkan |
| Penerapan / PJ | Umum / Dosen; KaLab |
| Unit | 1 sesi praktikum |
| Pembilang | Jumlah sesi rencana yang terlaksana sesuai ketentuan atau perubahan sah dengan tujuan/waktu setara |
| Pembagi | Seluruh sesi praktikum yang direncanakan pada periode monev |
| Memenuhi bila | Kegiatan, durasi, dan tujuan sesuai; perubahan sah; sesi tertunda hanya dihitung memenuhi setelah pengganti selesai dalam periode pelaporan |
| Skor | 100% → 4 · 90–<100% → 3 · 70–<90% → 2 · <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan → 1 |
| Referensi instrumen | Pedoman Diklatfung PLP 2022 (pengoperasian/metode), Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

Bukti dukung: (1) jadwal, (2) jurnal sesi, (3) presensi praktikan, asisten praktikum, laboran, dosen pendamping, (4) modul yang dipakai, (5) *log book* praktikum, (6) perubahan disetujui (bila ada), (7) penggantian sesi (bila ada).

## 2. Aturan "memenuhi"

Satu sesi rencana (Sesi dari PKG-15) dinyatakan **memenuhi** bila kelima cek lolos. Skor = jumlah sesi memenuhi ÷ seluruh sesi rencana pada periode monev.

| Cek | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| C1 Terlaksana | Ada jurnal sesi yang sudah dikirim | Jurnal sesi berstatus *terkirim* (nama status disamakan dengan rancangan, 16 Nov 2026) | — |
| C2 Sesuai jadwal | Dilaksanakan pada tanggal dan ruang rencana, atau ada perubahan yang disetujui | Tanggal dan ruang jurnal = Sesi, **atau** ada Perubahan Sesi berstatus *disetujui* | Keabsahan penyetuju |
| C3 Sesuai durasi | Durasi aktual tidak kurang dari ambang yang ditetapkan KaLab | Durasi aktual ≥ ambang × durasi rencana | — |
| C4 Sesuai modul dan tujuan | Modul yang dipakai adalah versi berlaku, dan topik sesuai pertemuan | Jurnal merujuk Versi Modul yang berlaku pada tanggal sesi (PKG-15); topik terisi; pertemuan ke- = Sesi | **Kesesuaian topik dengan tujuan sesi** |
| C5 Bukti lengkap | Presensi dan *log book* tercatat | Ada presensi dosen dan laboran, presensi asisten bila sesi berasisten, jumlah praktikan hadir, dan minimal satu entri *log book* | — |

Catatan aturan:
- **Sesi tertunda** baru dihitung memenuhi bila Sesi penggantinya lolos C1–C5 **sebelum** periode ditutup (bunyi instrumen).
- **Jam rencana diambil dari Sesi**, tidak diketik ulang pengisi jurnal. Pengisi hanya mencatat jam aktual. Ini menutup masalah salah isi tanggal dan jam (A5, A7).
- **Satu Sesi hanya punya satu jurnal.** Ini mencegah laporan ganda (A4).
- **Presensi praktikan cukup jumlah hadir**, ditambah tautan ke SIMPEL bila ada, seperti praktik sekarang (A8, A14). Presensi per nama ditunda **[USULAN PENULIS; KONFIRMASI wawancara P13]**.
- **Ambang durasi** dan sah tidaknya sesi daring adalah **pengaturan KaLab**, bukan data transaksi **[KONFIRMASI wawancara P12, P13]**.
- **Ketepatan waktu pengisian** tidak menjadi syarat memenuhi (instrumen tidak menyebutnya), tetapi ditampilkan sebagai peringatan dan jurnal dikunci setelah batas waktu tertentu **[USULAN PENULIS]**. Dasarnya ISO 7.5.1 dan temuan A6.
- **Kecocokan petugas yang hadir dengan penugasan** (A3) adalah urusan PKG-04 Pengelolaan 4 (penugasan). PKG-18 hanya mencatat siapa yang hadir.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Jadwal | 1 | Sesi dari PKG-15 (di-*import*, tidak dibuat ulang) |
| Jurnal sesi | 2, 4 | Satu per Sesi: jam aktual, pertemuan ke-, topik, Versi Modul yang dipakai, kendala, foto |
| Presensi | 3 | Baris presensi petugas di jurnal + jumlah praktikan hadir (+ tautan SIMPEL) |
| *Log book* | 5 | Entri *log book* di jurnal |
| Perubahan dan penggantian | 6, 7 | Perubahan Sesi beserta keputusan dan Sesi penggantinya |
| Persentase PKG-18 dan daftar sesi tidak memenuhi | — | Dihitung dari C1–C5, tidak disimpan sebagai tabel |

## 4. Data transaksi

| Entitas | Label | Grain | Isi (garis besar) | Catatan |
|---|---|---|---|---|
| **Sesi** | [T] Core | 1 sesi bertanggal | — | Dibangkitkan PKG-15. PKG-18 hanya memperbarui statusnya (mis. terlaksana, tertunda, diganti). Nama status disatukan di state machine (Langkah 5) |
| **Jurnal Sesi** | [T] | 1 per Sesi | Jam mulai dan selesai aktual, pertemuan ke-, topik, Versi Modul yang dipakai, jumlah praktikan hadir, tautan presensi SIMPEL (opsional), kendala, foto, pengisi, status (draf → dikirim). Anak: **presensi petugas** (`employee_id`: Many2one `hr.employee`, kontrak Core I-8; peran: dosen/asisten/laboran, kehadiran: penuh/sebagian/tidak), ***log book*** (waktu, uraian kegiatan) | Satu Sesi satu jurnal. Siapa pengisinya (asisten, dosen, atau laboran) **[KONFIRMASI wawancara P10, P13]** |
| **Perubahan Sesi** | [T] | 1 pengajuan perubahan | Sesi asal, jenis (pindah jadwal, pindah ruang, daring, batal dan diganti), alasan, pengaju, status (diajukan → disetujui/ditolak), penyetuju, Sesi pengganti | Bila disetujui dan ada pengganti, Sesi pengganti dibangkitkan dengan rujukan ke Sesi asal |
| **Daftar Sesi Tidak Memenuhi** | [R] | — | Sesi beserta cek C1–C5 yang gagal | Dasar persentase |
| **Rekap Keterlaksanaan per Kelas** (+) | [R] | — | Jumlah sesi rencana, terlaksana, memenuhi per kelas per periode | Pengganti rekap manual yang sekarang dibuat (A17) |

Riwayat perubahan memakai `mail.thread` + *tracking* bawaan Odoo. Tidak perlu tabel tambahan.

Dibanding [pemetaan](pemetaan-package-instrumen.md#pkg-18--proses-18-sesi-terlaksana): tidak ada entitas baru yang diinput; ditambah satu report (+) Rekap Keterlaksanaan per Kelas. Verifikasi jurnal oleh laboran (dugaan fungsi kolom "Status", A10) **tidak** dijadikan entitas atau tahap terpisah sampai fungsinya dipastikan **[KONFIRMASI wawancara P11]**.

## 5. Master data

Semua master **di-*import* dari Core**. PKG-18 tidak punya master lokal.

| Master | Dipakai untuk | Sumber (Core) | Bila belum tersedia |
|---|---|---|---|
| Periode | Batas pembagi dan tanggal tutup | `labfik.periode` | Periode monev = semester **[ASUMSI]** |
| Mata Kuliah, Kelas | Identitas sesi (melalui Sesi) | `labfik.mata.kuliah`, `labfik.kelas` | Diimpor dari tab alokasi (PKG-15) |
| Ruang Lab | Ruang aktual untuk C2 | `labfik.ruang` | — |
| Personel | Pengisi jurnal, petugas yang hadir, pengaju dan penyetuju perubahan | `hr.employee` diperluas | Laboran diinput manual (jumlahnya sedikit) |
| Jabatan | Siapa berwenang menyetujui perubahan sesi | `hr.job` diperluas | KaLab menyetujui semua perubahan **[ASUMSI]** |
| Mahasiswa | Tidak dipakai selama presensi praktikan berupa jumlah | `op.student` / Core | — |

Pilihan tetap: status jurnal, peran petugas, tingkat kehadiran, jenis perubahan, status perubahan, moda (luring/daring). Pengaturan KaLab: ambang durasi, batas hari pengisian jurnal, sah tidaknya sesi daring.

## 6. Dependensi dan jalan pengganti

**Masuk:**

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Sesi rencana bertanggal (pembagi) | PKG-15 Persiapan 15 (jadwal), lewat Core | **Wajib** | Tidak ada jalan pengganti yang sah. Tanpa Sesi, pembagi tidak terbentuk (A1) |
| Versi Modul berlaku | PKG-15 | Wajib untuk C4 | Jurnal menyimpan berkas modul yang dipakai, tanpa cek versi (seperti sekarang) |
| Penugasan petugas per sesi | PKG-04 Pengelolaan 4 (penugasan), addon `labfik_sdm` | Addon wajib (kontrak Core I-7); data opsional | Presensi petugas tetap diisi; pencocokan dengan penugasan dilakukan di Praktikum (KF-PRK-51) dan hanya tampil bila penugasan ada |
| Presensi rinci praktikan | SIMPEL (eksternal) | Opsional | Jumlah hadir saja |

**Keluar:**

| Dipakai oleh | Data |
|---|---|
| PKG-19 Evaluasi 19 (penilaian individual) | Tidak lagi (penilaian lewat tautan LeADS per kelas, keputusan 14 Nov 2026) |
| PKG-04 Pengelolaan 4 (penugasan) | Tidak dipakai langsung; pencocokan penugasan dengan presensi terjadi di Praktikum (kontrak Core I-7) |

## 7. Ditunda

Tidak dibutuhkan untuk membuktikan C1–C5, jadi tidak dirancang (calon isi batasan masalah):
- Presensi praktikan per nama dan integrasi langsung dengan SIMPEL atau SIAKAD.
- Rekap honor asisten (tarif, status rekening, pengajuan ke rektorat). Rekap jumlah sesi per asisten bisa dibaca dari jurnal bila diperlukan.
- Pencocokan otomatis presensi dengan penugasan PKG-04.
- Kesesuaian topik dengan RPS per pertemuan (cukup dinilai penilai).
- Pengingat ke pengisi jurnal; status keterlambatan cukup terlihat di daftar.
- *Snapshot* skor harian atau mingguan untuk grafik tren.
- Tanda bahaya kritis dari modul Safety.

## 8. Kompleksitas

| T | M | D | E | A | Status data | Total |
|---|---|---|---|---|---|---|
| 2 (Jurnal Sesi, Perubahan Sesi) | 0 | 1 (PKG-15) | 1 (SIMPEL, opsional tautan) | 1 (persetujuan perubahan) | +1 (Sebagian: hanya sesi berasisten, A1) | **6** |

Analisis awal menghitung 8 karena Sesi masih dihitung sebagai tabel milik PKG-18. Sekarang Sesi milik Core dan dibangkitkan PKG-15.

Ringkasan untuk kolom sheet: Jenis Skor `Persentase` · Unit `sesi rencana` · Sumber `Google Form + Google Sheets (hanya sesi berasisten)` · Status `Sebagian` · Dependensi ID `Persiapan 15 (jadwal)` · Eksternal `SIMPEL` · Level `Otomatis` · Kompleksitas `6`.

## 9. Pertanyaan untuk narasumber

Pertanyaan utamanya sudah ada di sheet "Wawancara FIKLAB Compliance" bagian Pelaksanaan Praktikum (belum dijawab per 14 Nov 2026).

| Wawancara | Untuk | Yang perlu didapat |
|---|---|---|
| P10 (KaLab, laboran) | Jurnal Sesi, C1 | Catatan apa saja yang dihasilkan, siapa mengisi dan kapan, dan **di mana rekaman kelas tanpa asisten** |
| P11 (laboran) | Kolom Status (A10), verifikasi | Siapa memeriksa laporan formulir, apa yang dicek, bagaimana menangani laporan ganda |
| P12 (KaLab) | Perubahan Sesi, C2 | Prosedur sesi batal, pindah, daring, atau diganti; siapa menyetujui; contoh kejadian terakhir |
| P13 (KaLab) | C1, C5, pengisi jurnal | Siapa mengisi catatan sesi; apakah formulir asistensi boleh digantikan sistem atau tetap untuk honor; apakah presensi cukup ditautkan dari SIAKAD/SIMPEL |
| P18b, P19 (KaLab) | Seluruh PKG-18 | Kendala merekam sesi; rekap yang paling dibutuhkan |

Pertanyaan tambahan yang **belum ada** di sheet wawancara (usulan):
- [ ] Berapa durasi rencana satu sesi praktikum (mis. 2 × 50 menit), dan berapa ambang minimal agar sesi dianggap terlaksana? (A5: median 100 vs 50 menit)
- [ ] Apakah sesi daring dianggap sah? Siapa yang boleh mengizinkannya?
- [ ] Apakah laboran hadir atau memantau di setiap sesi? Bila ya, bagaimana kehadirannya dicatat? (A8)
- [ ] Bagaimana pertemuan dinomori saat UTS/UAS, dan apakah pertemuan 8 dan 16 bisa berisi praktikum? (A11)
