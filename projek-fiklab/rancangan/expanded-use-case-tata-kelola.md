# Expanded Use Case dan Aturan Bisnis Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 7 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Bahan kerja**, bukan diagram. Dipakai untuk SSD (langkah 8), conceptual model (langkah 9), pemetaan aturan ke mekanisme Odoo (langkah 10), dan Rencana Pengujian Bab II 2.4. Tabel deskripsi use case (bagian 3) bisa dimasukkan ke 2.3 bila diminta pembimbing.

Sumber: [use-case-tata-kelola.md](use-case-tata-kelola.md) (UC-01–28), [kebutuhan-tata-kelola.md](kebutuhan-tata-kelola.md) (KF *hidden* dan KNF), [proses-bisnis-tata-kelola.md](proses-bisnis-tata-kelola.md) (S1, S2), analisis PKG-01, 02, 03, 13 (aturan "memenuhi"), dan keputusan di brief.

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Alur utama = urutan transaksi aktor → sistem, lurus, tanpa *if* atau perulangan | §6.2, §6.4 | Bagian 4 |
| Varian (V) = cara lain mencapai tujuan; eksepsi (E) = hambatan. Setiap alternatif berakhir jelas: berhasil, gagal, atau kembali ke langkah *n* | §6.3.2–6.3.3 | Bagian 4 |
| Setiap aturan bisnis biasanya melahirkan satu eksepsi | §6.3.3 | Eksepsi merujuk kode AB |
| *Essential*: tanpa tombol, layar, atau menu. Identifikasi dan pemilihan ditulis generik ("memilih dokumen") | §6.4.1, §6.4.3 | Semua alur |
| Data yang dipertukarkan disebut eksplisit | §6.4.2 | Semua langkah aktor dan sistem |
| Hanya langkah wajib (*system event* dan *system return*). Langkah "sistem menyimpan ke basis data" tidak ditulis | §6.4.4 | Langkah sistem hanya berisi informasi yang dikembalikan ke aktor dan perubahan status yang terlihat |
| Prakondisi = fakta yang dianggap benar sebelum mulai; yang baru bisa dicek di tengah alur = eksepsi | §6.6.2 | Bagian 3 |
| Use case berpola («CRUDL», «report») cukup satu pola bersama | §6.7 | Bagian 5 |

---

## 2. Katalog aturan bisnis

Kode AB dipakai oleh eksepsi di bagian 3–5. Kolom **Lapis**: W = Inti, O = Pelengkap (berlaku hanya bila KF Pelengkapnya dibangun). Pemetaan ke mekanisme Odoo (`@api.constrains`, *hook*, `compute`, `ir.cron`, *record rule*) dilakukan di langkah 10.

### 2.1 Pengesahan (semua dokumen)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-01 | Dokumen hanya dapat diubah dan diajukan selama berstatus **Draf**. Dokumen Draf yang belum pernah diajukan boleh dihapus; selebihnya tidak | S1 (sel 7, transisi hapus) | UC-01, 10, 15, 22, 23 | W |
| AB-02 | Dokumen hanya dapat diajukan bila **isinya lengkap** menurut jenisnya:<br>• **Versi SOP/IK**: berkas, nomor revisi, tanggal efektif; untuk revisi kedua dan seterusnya juga bagian yang diubah, ringkasan, dan alasan perubahan<br>• **Renstra**: judul, periode, berkas<br>• **Rencana tahunan**: minimal satu item; setiap item punya kegiatan, KPI, target, satuan, PIC, jadwal, anggaran, dan rujukan Renstra<br>• **Rencana pengembangan**: keempat aspek gap (tridharma, kompetensi, sarana, layanan) masing-masing punya minimal satu temuan, atau dinyatakan "tidak ada gap" dengan alasan; minimal satu item; setiap item menunjuk minimal satu temuan gap dan punya nilai risiko, nilai manfaat, prioritas, biaya, target, PIC, dan jadwal<br>• **SK penetapan**: nomor SK, periode, minimal satu baris penetapan (personel, jabatan) | KF-01, KF-30; PKG-01 K2, PKG-13 K2, PKG-03 K1; ISO 8.3.2 | UC-01 | W |
| AB-03 | Berkas bertanda tangan hanya dapat diunggah atau diganti selama dokumen berstatus **Diajukan** | S1 | UC-03 | W |
| AB-04 | Dokumen hanya dapat disahkan bila **berkas bertanda tangan** sudah diunggah | KF-05 | UC-05 | W |
| AB-05 | **Pengesah tercatat** harus Personel yang jabatannya punya wewenang *mengesahkan* untuk jenis dokumen itu. Jabatan seseorang dibaca dari data Personel **[ASUMSI]** | KF-05; PKG-02 S2; ISO 8.3.2a | UC-05 | W |
| AB-06 | Hanya **KaLab** yang dapat mengembalikan, mengesahkan, dan mencabut dokumen. KaLab dicatat sebagai **pencatat** | Keputusan 14 Nov 2026; KNF-04 | UC-04, 05, 06 | W |
| AB-07 | Mengembalikan dan mencabut dokumen wajib disertai **alasan** | KF-03, KF-06 | UC-04, 06 | W |
| AB-08 | Saat dokumen disahkan, dokumen yang digantikannya menjadi **Diganti**: versi sebelumnya dari Dokumen Induk yang sama, atau rencana/SK/Renstra yang direvisinya. Dalam satu Dokumen Induk hanya ada satu versi Disahkan | KF-08; ISO 8.3.2c | UC-05 | W |
| AB-09 | Setiap kejadian pengesahan (diajukan, dikembalikan, berkas diunggah atau diganti, disahkan, diganti, dicabut, kedaluwarsa) dicatat sebagai **riwayat** berisi waktu, pelaku, pengesah tercatat, alasan, dan berkas. Riwayat tidak dapat diubah atau dihapus | KF-07; KNF-05 | UC-01, 03–07 | W |
| AB-10 | Dokumen berperiode (Renstra, rencana, SK) yang Disahkan menjadi **Kedaluwarsa** sehari setelah tanggal akhir periodenya | KF-09 | UC-07 | O |
| AB-11 | Hanya ada satu rencana **Disahkan** per jenis dan periode yang sama, kecuali revisi yang menggantikannya | KF-38 | UC-05 | O |

### 2.2 Pengendalian dokumen SOP/IK (PKG-02)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-12 | Dalam satu Dokumen Induk hanya boleh ada satu versi **dalam proses** (Draf atau Diajukan) | KF-18 | UC-15, 01 | O |
| AB-13 | **Nomor revisi** unik dalam satu Dokumen Induk | ISO 8.3.2c (status revisi teridentifikasi) | UC-15 | W |
| AB-14 | **Tanggal tinjau berikutnya** = tanggal sah versi (atau tanggal tinjau ulang terakhir yang berhasil *tetap berlaku*) + siklus tinjau Dokumen Induk. Versi **perlu ditinjau** bila tanggal itu sudah lewat | KF-15; S2; PKG-02 S3 | UC-05, 18, 20, 28 | W |
| AB-15 | Distribusi, sosialisasi, dan tinjau ulang hanya dicatat untuk versi berstatus **Disahkan**. Sosialisasi memuat minimal satu peserta | PKG-02 S3–S5; A2 | UC-16, 17, 18 | W |
| AB-16 | Lokasi distribusi harus salah satu **lokasi penggunaan** Dokumen Induk | PKG-02 S4 ("lokasi yang ditetapkan") | UC-16 | W |
| AB-17 | Pengguna Lab hanya dapat melihat versi berstatus **Disahkan** | KF-17; KNF-04 | UC-19 | O |

### 2.3 Rencana (PKG-01, PKG-13)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-18 | Realisasi hanya dicatat untuk item dari rencana berstatus **Disahkan**, oleh **PIC item** atau KaLab, dan wajib melampirkan **bukti**. Satu item hanya punya satu realisasi per periode lapor | KF-31; PKG-01 K3, PKG-13 K3 | UC-25 | W |
| AB-19 | Tinjauan hanya dicatat untuk rencana yang pernah disahkan (Disahkan, Diganti, atau Kedaluwarsa). Rencana berikutnya yang ditautkan harus **berjenis sama** dan periodenya **sesudah** rencana yang ditinjau | KF-32; PKG-01 K4, PKG-13 K4 | UC-26 | W |
| AB-20 | Tinjauan rencana **pengembangan** wajib memuat **ukuran manfaat** (indikator, nilai sebelum, nilai sesudah, sumber) untuk setiap item yang punya realisasi **[USULAN PENULIS]** | KF-40; PKG-13 K4 | UC-26 | W |
| AB-21 | **Prioritas** item = nilai risiko × nilai manfaat (skala 1–3): skor 6–9 tinggi, 3–4 sedang, 1–2 rendah **[USULAN PENULIS]** | KF-42; PKG-13 K2 | UC-23 | O |

### 2.4 Umum

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-22 | **Rekaman bukti** (rapat koordinasi, evaluasi struktur, distribusi, sosialisasi, tinjau ulang, realisasi, tinjauan rencana) tidak dapat dihapus; hanya dapat dikoreksi, dan setiap koreksi terlacak. Tinjau ulang tidak dikoreksi; bila keliru, dicatat tinjau ulang baru | Keputusan 14 Nov 2026; KNF-05 | UC-11, 12, 16, 17, 18, 25, 26 | W |
| AB-23 | **Master** (Personel, Jabatan, Dokumen Induk, KPI) hanya dapat dihapus bila belum dirujuk data lain; selebihnya diarsipkan (tidak tampil sebagai pilihan baru) | Matriks CRUDL (use case bagian 6) | UC-08, 09, 14, 21 | W |

### 2.5 Status monev

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-24 | **Persentase PKG-02** pada tanggal tutup periode monev:<br>• **Pembagi** = Dokumen Induk berstatus wajib yang tanggal ditetapkan wajibnya ≤ tanggal tutup<br>• **Pembilang** = dari pembagi itu, yang lolos kelima cek:<br>  S1 terdaftar: dasar kebutuhan terisi<br>  S2 disahkan: ada versi Disahkan dengan pengesah dan tanggal sah<br>  S3 mutakhir: versi itu tidak *perlu ditinjau* pada tanggal tutup (AB-14)<br>  S4 tersedia: setiap lokasi penggunaan punya distribusi untuk versi itu<br>  S5 disosialisasikan: ada minimal satu sosialisasi untuk versi itu<br>• **Skor**: 100% → 4; 90–<100% → 3; 70–<90% → 2; <70% → 1. Bila pembagi 0, skor tidak dihitung<br>• Untuk setiap dokumen yang tidak lolos, ditampilkan cek yang gagal | KF-43; analisis PKG-02 bagian 1–2 | UC-28 | W |
| AB-25 | **Kriteria tertinggi K1–K4** (PKG-01, 03, 13) pada tanggal acuan = *k* terbesar sehingga K1 sampai K*k* semuanya lolos (berurutan). Rincian cek pada tabel di bawah. Sistem menampilkan kriteria tertinggi, tautan ke rekaman buktinya, dan kriteria berikutnya yang belum lolos beserta sebabnya. **Skor akhir ditetapkan penilai** | KF-44; brief batasan 4 | UC-28 | W |

Rincian cek AB-25:

| PKG | K1 | K2 | K3 | K4 |
|---|---|---|---|---|
| **PKG-01** | Ada Renstra Disahkan dan rencana tahunan Disahkan yang periodenya mencakup tanggal acuan | Rencana tahunan itu memenuhi kelengkapan AB-02 | Setiap item yang jadwal mulainya ≤ tanggal acuan punya minimal satu realisasi berbukti | Ada tinjauan rencana tahunan (periode berjalan atau sebelumnya) yang tertaut ke rencana tahunan berikutnya **[USULAN PENULIS]** |
| **PKG-03** | Ada SK penetapan Disahkan yang periodenya mencakup tanggal acuan | Setiap jabatan pada baris SK itu punya minimal satu tugas, minimal satu wewenang, atasan, dan jabatan pengganti | Ada minimal satu rapat koordinasi dalam periode SK sampai tanggal acuan | Ada evaluasi struktur dalam periode SK. Bila keputusannya *struktur perlu diubah*, evaluasi tertaut ke SK atau jabatan yang direvisi **[USULAN PENULIS]** |
| **PKG-13** | Ada rencana pengembangan Disahkan yang periodenya mencakup tanggal acuan | Rencana itu memenuhi kelengkapan AB-02 | Sama dengan PKG-01 K3 | Ada tinjauan rencana pengembangan yang memenuhi AB-20 dan tertaut ke rencana berikutnya atau revisinya |

Catatan rincian AB-25:
- PKG-01 K1 memakai Renstra sebagai *roadmap* (Bukti 1). Apakah boleh begitu masih ditanyakan ke Pak Widi (brief, pertanyaan terbuka).
- PKG-01 K4: tinjauan atas rencana berjalan baru ada di akhir periode, padahal monev bisa terjadi di tengah tahun. Karena itu tinjauan periode sebelumnya juga dihitung.
- PKG-03 K4: instrumen berbunyi "struktur diperbaiki **bila perlu**". Jadi tautan ke revisi hanya diwajibkan bila keputusan evaluasi adalah perubahan. Ini lebih longgar dari analisis PKG-03 versi awal; analisis sudah disesuaikan (disetujui Febriyan, 14 November 2026).

---

## 3. Tabel deskripsi use case

Semua use case selain «CRUDL» dan «report». Use case yang diberi tanda ★ dirinci alurnya di bagian 4. Prakondisi umum semua use case: aktor sudah teridentifikasi oleh sistem dan memegang grup akses yang sesuai (tidak diulang di tabel).

| UC | Tujuan | Aktor | Prakondisi | Pascakondisi sukses | Eksepsi |
|---|---|---|---|---|---|
| UC-01 ★ Ajukan Dokumen | Menyerahkan dokumen yang sudah lengkap untuk ditandatangani dan disahkan | Pengelola Lab | Ada dokumen Draf yang disusun aktor | Dokumen berstatus Diajukan; riwayat "diajukan" tercatat | AB-01, AB-02, AB-12 (O) |
| UC-02 Terbitkan Dokumen Resmi | Mendapatkan dokumen resmi format lab dari isi rencana atau SK, untuk ditandatangani | Pengelola Lab | Rencana tahunan, rencana pengembangan (O), atau SK (O) berstatus Diajukan | Dokumen resmi tersedia bagi aktor. Tidak ada perubahan data | Dokumen bukan jenis yang bisa diterbitkan → gagal |
| UC-03 ★ Unggah Dokumen Bertanda Tangan | Melampirkan bukti tanda tangan pejabat | Pengelola Lab | Ada dokumen Diajukan | Berkas bertanda tangan terlampir; riwayat "berkas diunggah" tercatat | AB-03 |
| UC-04 Kembalikan Dokumen | Mengembalikan dokumen kepada penyusun untuk diperbaiki, termasuk bila pejabat menolak di atas kertas | KaLab | Ada dokumen Diajukan | Dokumen berstatus Draf; riwayat "dikembalikan" dengan alasan tercatat | AB-06, AB-07 |
| UC-05 ★ Sahkan Dokumen | Mencatat pengesahan dokumen yang sudah ditandatangani | KaLab | Ada dokumen Diajukan | Dokumen Disahkan dengan pengesah, pencatat, dan tanggal sah; dokumen lama Diganti; untuk versi SOP/IK, tanggal tinjau berikutnya terhitung; riwayat tercatat | AB-04, AB-05, AB-06, AB-11 (O) |
| UC-06 Cabut Dokumen | Menghentikan berlakunya dokumen yang tidak diperlukan lagi | KaLab | Ada dokumen Disahkan | Dokumen Dicabut; riwayat "dicabut" dengan alasan tercatat | AB-06, AB-07 |
| UC-07 Kedaluwarsakan Dokumen Berperiode (O) | Menandai dokumen yang periodenya sudah habis | Penjadwal | Tanggal berganti | Dokumen Disahkan yang periodenya habis berstatus Kedaluwarsa; riwayat tercatat | — |
| UC-10 Susun SK Penetapan Pengelola | Menyusun penetapan personel ke jabatan untuk satu periode | KaLab | Personel dan Jabatan terdaftar | SK berstatus Draf dengan baris penetapan; bila revisi, tertaut ke SK yang direvisi | AB-01 |
| UC-11 Catat Rapat Koordinasi | Merekam koordinasi sebagai bukti struktur dijalankan | KaLab | — | Rapat tercatat dengan tanggal, agenda, peserta, keputusan, notulen | AB-22 (koreksi) |
| UC-12 Catat Evaluasi Struktur | Merekam evaluasi beban kerja dan koordinasi | KaLab | Ada SK Disahkan | Evaluasi tercatat; bila keputusan *struktur perlu diubah*, tertaut ke SK atau jabatan yang direvisi (boleh diisi kemudian) | AB-22 |
| UC-15 ★ Unggah Versi Dokumen | Menambahkan versi baru SOP/IK | Laboran/PLP | Dokumen Induk terdaftar | Versi baru berstatus Draf | AB-12 (O), AB-13 |
| UC-16 Catat Distribusi Dokumen | Merekam bahwa versi berlaku sudah tersedia di lokasi penggunaan | Laboran/PLP | Ada versi Disahkan | Distribusi tercatat per lokasi, dengan tanggal dan petugas | AB-15, AB-16, AB-22 |
| UC-17 Catat Sosialisasi Dokumen | Merekam sosialisasi versi berlaku | Laboran/PLP | Ada versi Disahkan | Sosialisasi tercatat dengan tanggal, metode, peserta, bukti | AB-15, AB-22 |
| UC-18 ★ Tinjau Ulang Dokumen | Memastikan versi berlaku masih sesuai | Pengelola Lab | Ada versi Disahkan | Tinjau ulang tercatat; bila *tetap berlaku*, tanggal tinjau berikutnya diperbarui | AB-14, AB-15 |
| UC-19 Baca Dokumen Berlaku (O) | Membaca SOP/IK yang berlaku | Pengguna Lab | — | Tidak ada perubahan data | AB-17 |
| UC-23 ★ Susun Rencana | Menyusun rencana tahunan atau rencana pengembangan | KaLab | KPI dan Personel terdaftar | Rencana berstatus Draf dengan item (dan temuan gap untuk pengembangan) | AB-01, AB-21 (O) |
| UC-24 Buat Revisi Rencana (O) | Memperbarui rencana yang sudah disahkan | KaLab | Ada rencana Disahkan | Rencana baru berstatus Draf, salinan isi rencana lama, tertaut ke rencana yang direvisi. Rencana lama tetap Disahkan sampai revisi disahkan (AB-08) | — |
| UC-25 ★ Isi Realisasi Rencana | Melaporkan capaian item pada satu periode lapor | Pengelola Lab (PIC item) | Ada rencana Disahkan | Realisasi tercatat dengan pelapor, tanggal, dan bukti | AB-18, AB-22 |
| UC-26 Catat Tinjauan Rencana | Meninjau capaian rencana dan menetapkan keputusan perbaikan | KaLab | Ada rencana yang pernah disahkan | Tinjauan tercatat; untuk pengembangan, ukuran manfaat tercatat; tertaut ke rencana berikutnya bila sudah ada (boleh diisi kemudian) | AB-19, AB-20, AB-22 |

---

## 4. Alur lengkap use case kunci

Dipilih karena punya aturan bisnis atau mengubah status (use case bagian 9). Use case ini menjadi dasar SSD di langkah 8. UC-28 memakai pola «report» (bagian 5.2) dengan aturan AB-24 dan AB-25.

### UC-01 Ajukan Dokumen

**Alur utama**
1. Pengelola Lab meminta daftar dokumen Draf yang disusunnya.
2. Sistem menampilkan daftar dokumen Draf: jenis, judul atau nomor, periode, dan tanggal terakhir diubah.
3. Pengelola Lab memilih satu dokumen dan mengajukannya.
4. Sistem menampilkan dokumen dengan status Diajukan dan tanggal ajukan. [E1, E2, E3]

**Eksepsi**
- **E1 Isi belum lengkap (AB-02).** E1.1 Sistem menampilkan bagian isi yang belum lengkap, misalnya item tanpa PIC atau aspek gap yang kosong. E1.2 Use case gagal; dokumen tetap Draf.
- **E2 Dokumen tidak lagi berstatus Draf (AB-01)**, misalnya sudah diajukan dari sesi lain. E2.1 Sistem menampilkan status dokumen saat ini. E2.2 Use case gagal.
- **E3 (O) Ada versi lain dalam proses pada Dokumen Induk yang sama (AB-12).** E3.1 Sistem menampilkan versi yang sedang diproses. E3.2 Use case gagal.

### UC-03 Unggah Dokumen Bertanda Tangan

**Alur utama**
1. Pengelola Lab meminta daftar dokumen Diajukan.
2. Sistem menampilkan daftar dokumen Diajukan: jenis, judul, tanggal ajukan, dan keterangan ada atau belumnya berkas bertanda tangan.
3. Pengelola Lab memilih satu dokumen dan menyerahkan berkas bertanda tangan. [V1]
4. Sistem menampilkan dokumen dengan berkas bertanda tangan terlampir dan tanggal unggah. [E1]

**Varian**
- **V1 Berkas sudah pernah diunggah.** V1.1 Pengelola Lab menyerahkan berkas pengganti. V1.2 Sistem menampilkan berkas baru; riwayat mencatat penggantian berkas. V1.3 Use case berhasil.

**Eksepsi**
- **E1 Dokumen tidak lagi berstatus Diajukan (AB-03).** E1.1 Sistem menampilkan status dokumen saat ini. E1.2 Use case gagal.

### UC-05 Sahkan Dokumen

**Alur utama**
1. KaLab meminta daftar dokumen Diajukan.
2. Sistem menampilkan daftar dokumen Diajukan: jenis, judul, penyusun, tanggal ajukan, dan keterangan berkas bertanda tangan.
3. KaLab memilih satu dokumen.
4. Sistem menampilkan ringkasan isi dokumen, berkas bertanda tangan, riwayat pengesahan, dan daftar Personel yang jabatannya berwenang mengesahkan jenis dokumen itu.
5. KaLab menyerahkan pengesah tercatat (pejabat yang menandatangani) dan tanggal sah.
6. Sistem menampilkan dokumen dengan status Disahkan, pengesah, pencatat, tanggal sah, dokumen yang digantikan (bila ada), dan untuk versi SOP/IK tanggal tinjau berikutnya. [E1, E2, E3]

**Eksepsi**
- **E1 Berkas bertanda tangan belum ada (AB-04).** E1.1 Sistem menampilkan bahwa berkas belum diunggah. E1.2 Use case gagal; berkas diunggah lewat UC-03.
- **E2 Pengesah tidak berwenang (AB-05).** E2.1 Sistem menampilkan jabatan yang berwenang untuk jenis dokumen itu. E2.2 Kembali ke langkah 5. Bila berkas ternyata ditandatangani pejabat yang tidak berwenang, KaLab mengembalikan dokumen (UC-04).
- **E3 (O) Sudah ada rencana Disahkan dengan jenis dan periode yang sama, dan dokumen ini bukan revisinya (AB-11).** E3.1 Sistem menampilkan rencana yang sedang berlaku. E3.2 Use case gagal.

Catatan: perubahan dokumen lama menjadi Diganti (AB-08), perhitungan tanggal tinjau (AB-14), dan pencatatan riwayat (AB-09) adalah akibat langkah 6, tanpa interaksi tambahan (KF *hidden*, §4.7.2).

### UC-15 Unggah Versi Dokumen

**Alur utama**
1. Laboran meminta daftar Dokumen Induk.
2. Sistem menampilkan daftar Dokumen Induk: kode, judul, jenis, revisi berlaku, dan penanda perlu ditinjau.
3. Laboran memilih satu Dokumen Induk.
4. Sistem menampilkan revisi berlaku, riwayat revisi, dan nomor revisi berikutnya yang diusulkan.
5. Laboran menyerahkan berkas, nomor revisi, tanggal efektif, bagian yang diubah, ringkasan perubahan, dan alasan revisi. [V1]
6. Sistem menampilkan versi baru berstatus Draf. [E1, E2]

**Varian**
- **V1 Versi pertama dokumen.** V1.1 Laboran menyerahkan berkas, nomor revisi, dan tanggal efektif saja. V1.2 Kembali ke langkah 6.

**Eksepsi**
- **E1 Nomor revisi sudah dipakai (AB-13).** E1.1 Sistem menampilkan nomor revisi yang sudah ada. E1.2 Kembali ke langkah 5.
- **E2 (O) Ada versi lain dalam proses (AB-12).** E2.1 Sistem menampilkan versi yang sedang diproses. E2.2 Use case gagal.

### UC-18 Tinjau Ulang Dokumen

**Alur utama**
1. Pengelola Lab meminta daftar versi berlaku.
2. Sistem menampilkan daftar versi Disahkan: kode, judul, revisi, tanggal tinjau berikutnya, dan penanda perlu ditinjau, diurutkan dari yang paling lama terlewati.
3. Pengelola Lab memilih satu versi dan menyerahkan tanggal tinjau, hasil (*tetap berlaku*), dan catatan. [V1]
4. Sistem menampilkan tinjau ulang yang tercatat beserta peninjau dan tanggal tinjau berikutnya yang baru. [E1]

**Varian**
- **V1 Hasil *perlu revisi*.** V1.1 Pengelola Lab menyerahkan tanggal tinjau, hasil *perlu revisi*, dan catatan bagian yang perlu direvisi. V1.2 Sistem menampilkan tinjau ulang yang tercatat; tanggal tinjau berikutnya tidak berubah (S2). V1.3 Use case berhasil; versi baru disiapkan lewat UC-15.

**Eksepsi**
- **E1 Versi tidak lagi berstatus Disahkan (AB-15)**, misalnya baru diganti. E1.1 Sistem menampilkan status versi saat ini. E1.2 Use case gagal.

### UC-23 Susun Rencana

**Alur utama** (rencana tahunan baru)
1. KaLab menyerahkan jenis rencana (*tahunan*), judul, periode, dan narasi ringkas (O, KF-36). [V1, V3]
2. Sistem menampilkan rencana berstatus Draf beserta daftar KPI dan daftar Personel yang dapat dipilih sebagai PIC.
3. KaLab menyerahkan item rencana: kegiatan, KPI, target, satuan, PIC, jadwal mulai dan selesai, anggaran, dan rujukan Renstra.
4. Sistem menampilkan rencana beserta item dan penanda kelengkapan setiap item terhadap AB-02. [V2]

**Varian**
- **V1 Rencana pengembangan.** V1.1 KaLab menyerahkan jenis *pengembangan*, judul, periode, dan narasi ringkas (O). V1.2 Sistem menampilkan rencana Draf dan keempat aspek gap. V1.3 KaLab menyerahkan temuan gap per aspek: aspek, kondisi saat ini, kebutuhan atau standar, sumber data, uraian gap, dan lampiran; atau pernyataan "tidak ada gap" dengan alasan. V1.4 Sistem menampilkan temuan per aspek beserta daftar KPI dan Personel. V1.5 KaLab menyerahkan item program: temuan gap yang dijawab, kegiatan, nilai risiko, nilai manfaat, prioritas, biaya, target, satuan, PIC, dan jadwal. V1.6 Sistem menampilkan item beserta prioritas hasil hitungan (O, AB-21) dan penanda kelengkapan. V1.7 Use case berhasil.
- **V2 Disimpan untuk dilanjutkan.** V2.1 KaLab menghentikan penyusunan. V2.2 Use case berhasil; rencana tetap Draf.
- **V3 Melanjutkan rencana Draf.** V3.1 KaLab memilih rencana Draf yang sudah ada. V3.2 Sistem menampilkan rencana dengan item dan temuan gapnya. V3.3 Kembali ke langkah 3 (atau V1.3 untuk rencana pengembangan). Bila rencana bukan Draf, berlaku E1.

**Eksepsi**
- **E1 Rencana tidak lagi berstatus Draf (AB-01).** E1.1 Sistem menampilkan status rencana. E1.2 Use case gagal.

Kelengkapan item tidak menghentikan penyimpanan; ia baru diwajibkan saat rencana diajukan (UC-01, AB-02). Dengan begitu KaLab bisa menyimpan rencana yang belum selesai (§4.3.1).

### UC-25 Isi Realisasi Rencana

**Alur utama**
1. Pengelola Lab meminta daftar item rencana yang menjadi tanggung jawabnya.
2. Sistem menampilkan daftar item dari rencana Disahkan: rencana, kegiatan, KPI, target, jadwal, dan realisasi terakhir.
3. Pengelola Lab memilih satu item dan menyerahkan periode lapor, capaian, anggaran atau biaya terpakai, status capaian, tindak lanjut, dan berkas bukti. [V1, V2]
4. Sistem menampilkan realisasi yang tercatat beserta pelapor, tanggal lapor, dan rekap capaian item terhadap target. [E1, E2]

**Varian**
- **V1 KaLab mengisi untuk item dengan PIC lain.** Langkahnya sama; pelapor tercatat sebagai KaLab (AB-18).
- **V2 Koreksi realisasi** (sudah ada realisasi untuk item dan periode lapor yang sama). V2.1 Sistem menampilkan realisasi yang ada. V2.2 Pengelola Lab menyerahkan nilai yang dikoreksi. V2.3 Sistem menampilkan realisasi terkoreksi; koreksinya terlacak (AB-22). V2.4 Use case berhasil.

**Eksepsi**
- **E1 Bukti tidak dilampirkan (AB-18).** E1.1 Sistem menampilkan bahwa bukti wajib. E1.2 Kembali ke langkah 3.
- **E2 Rencana tidak lagi berstatus Disahkan (AB-18)**, misalnya baru dicabut. E2.1 Sistem menampilkan status rencana. E2.2 Use case gagal.

---

## 5. Pola bersama «CRUDL» dan «report» (§6.7)

### 5.1 Pola «CRUDL»

**Create:** 1. Aktor menyerahkan data konsep. 2. Sistem menampilkan data yang tercatat. [E1]
**Retrieve:** 1. Aktor memilih satu rekaman. 2. Sistem menampilkan seluruh datanya beserta data terkait.
**Update:** 1. Aktor memilih satu rekaman dan menyerahkan data yang diubah. 2. Sistem menampilkan data terbaru. [E1, E3]
**Delete:** 1. Aktor memilih satu rekaman untuk dihapus. 2. Sistem menampilkan bahwa rekaman sudah tidak ada. [E2, E3]
**List:** 1. Aktor menyerahkan filter (opsional). 2. Sistem menampilkan daftar rekaman yang sesuai.

**Eksepsi bersama**
- **E1 Data wajib kosong atau tidak valid.** Sistem menampilkan field yang bermasalah; kembali ke langkah 1.
- **E2 Rekaman masih dirujuk data lain (AB-23).** Sistem menampilkan rujukannya dan menawarkan pengarsipan; use case gagal untuk penghapusan.
- **E3 Rekaman berstatus selain Draf (AB-01)**, khusus Renstra. Sistem menampilkan status; use case gagal.

| UC | Konsep | Data wajib | Aturan khusus |
|---|---|---|---|
| UC-08 Kelola Personel | Personel | Nama, jenis (dosen, laboran/PLP, teknisi, asisten, petugas K3), unit/prodi. Jabatan dan akun pengguna opsional (pejabat penanda tangan tidak punya akun) | AB-23. Pihak eksternal tidak dicatat |
| UC-09 Kelola Jabatan | Jabatan + tugas + wewenang | Nama, unit. Atasan, pengganti, tugas, dan wewenang tidak wajib saat disimpan, tetapi dibutuhkan untuk PKG-03 K2 (AB-25) | AB-23. Jabatan fakultas (Dekan, Ketua Jurusan) ditandai eksternal |
| UC-14 Kelola Dokumen Induk | Dokumen Induk | Kode (unik), judul, jenis, kategori, asal, status wajib, lokasi penggunaan, siklus tinjau. Bila wajib: dasar kebutuhan dan tanggal ditetapkan wajib | AB-23 (dihapus bila belum punya versi) |
| UC-21 Kelola KPI | KPI | Kode (unik), nama, definisi, rumus (pembilang, penyebut), satuan, frekuensi, sumber data | AB-23 (dihapus bila belum dirujuk item) |
| UC-22 Kelola Renstra | Renstra | Judul, periode, berkas | AB-01 (ubah dan hapus hanya saat Draf). Pengesahan lewat UC-01–05 |

### 5.2 Pola «report»

1. Aktor menyerahkan filter laporan.
2. Sistem menampilkan isi laporan.

Laporan tidak mengubah data. Bentuk keluarannya (layar atau PDF) adalah keputusan desain (§4.3.4, KNF-08).

| UC | Filter | Isi | Aturan |
|---|---|---|---|
| UC-13 Lihat Laporan Struktur Organisasi | Tanggal acuan | Bagan organisasi sebagai daftar hierarki jabatan (garis instruksi); uraian tugas per jabatan; matriks kewenangan (jabatan × tindakan × jenis dokumen); pemegang jabatan dari SK yang berlaku | — |
| UC-20 Lihat Laporan Pengendalian Dokumen | Jenis, kategori, status wajib | Daftar induk: kode, judul, jenis, revisi berlaku, tanggal sah, pengesah, tanggal tinjau berikutnya, penanda perlu ditinjau, lokasi penggunaan. Per dokumen: riwayat revisi, distribusi, sosialisasi, tinjau ulang | AB-14 |
| UC-27 Lihat Laporan Rencana | Rencana, periode lapor | Matriks keterkaitan (item per rujukan Renstra); laporan pelaksanaan (target, capaian, status, tindak lanjut per item); tinjauan dan ukuran manfaat | — |
| UC-28 Lihat Status Monev | Tanggal tutup / tanggal acuan | PKG-02: persentase, skor, daftar SOP wajib yang tidak memenuhi dan cek yang gagal. PKG-01, 03, 13: kriteria tertinggi, tautan bukti, kriteria berikutnya yang belum lolos dan sebabnya | AB-24, AB-25 |

---

## 6. Cek silang

### 6.1 AB → KF dan UC

| AB | KF | Eksepsi atau tempat dipakai |
|---|---|---|
| AB-01 | S1 | UC-01 E2, UC-23 E1, «CRUDL» E3 |
| AB-02 | KF-01, 30 | UC-01 E1 |
| AB-03 | — (S1) | UC-03 E1 |
| AB-04 | KF-05 | UC-05 E1 |
| AB-05 | KF-05 | UC-05 E2 |
| AB-06 | KNF-04 | Prakondisi grup akses UC-04, 05, 06 |
| AB-07 | KF-03, 06 | UC-04, UC-06 (alasan wajib) |
| AB-08 | KF-08 | UC-05 langkah 6 |
| AB-09 | KF-07 | UC-01, 03–07 |
| AB-10 | KF-09 | UC-07 |
| AB-11 | KF-38 | UC-05 E3 |
| AB-12 | KF-18 | UC-01 E3, UC-15 E2 |
| AB-13 | — (ISO 8.3.2c) | UC-15 E1 |
| AB-14 | KF-15 | UC-05 langkah 6, UC-18 langkah 4, UC-20, UC-28 |
| AB-15 | — (A2) | UC-16, 17, UC-18 E1 |
| AB-16 | — (PKG-02 S4) | UC-16 |
| AB-17 | KF-17 | UC-19 |
| AB-18 | KF-31 | UC-25 E1, E2, V1 |
| AB-19 | KF-32 | UC-26 |
| AB-20 | KF-40 | UC-26 |
| AB-21 | KF-42 | UC-23 V1.6 |
| AB-22 | Keputusan 14 Nov | UC-11, 12, 16, 17, 18, UC-25 V2, UC-26 |
| AB-23 | — (matriks CRUDL) | «CRUDL» E2 |
| AB-24 | KF-43 | UC-28 |
| AB-25 | KF-44 | UC-28 |

Semua KF *hidden* (KF-05, 07, 08, 09, 15, 18, 30, 38, 42, 43, 44) punya AB. AB-03, 13, 15, 16, 22, 23 tidak punya KF khusus; sumbernya state machine, ISO, kriteria, atau keputusan, dan semuanya berada di dalam KF yang sudah ada (KF-02, 11, 12, 13, 14).

### 6.2 Kriteria instrumen → AB

| Kriteria | AB |
|---|---|
| PKG-02 S1–S5 | AB-24 (memakai AB-14, 15, 16) |
| PKG-01, 03, 13 K1 | AB-25 (memakai AB-04, 05, 08) |
| PKG-01, 13 K2 | AB-02, AB-25 |
| PKG-03 K2 | AB-25 |
| PKG-01, 13 K3 | AB-18, AB-25 |
| PKG-03 K3 | AB-25 |
| PKG-01, 13 K4 | AB-19, AB-20, AB-25 |
| PKG-03 K4 | AB-25 |

### 6.3 Temuan dan kesalahan di langkah sebelumnya

- **Pengesah tercatat dicatat KaLab saat mengesahkan (UC-05)**, bukan saat berkas diunggah (UC-03). Ini sesuai KF-04 dan A1. Akibatnya, pengunggah berkas tidak perlu tahu jabatan pengesah.
- **AB-05 butuh definisi "memegang jabatan".** Dipilih: jabatan pada data Personel, bukan baris SK. Alasannya, pejabat fakultas (Dekan) tidak muncul di SK pengelola lab, dan SK pertama pun harus bisa disahkan sebelum ada SK lain. Ini perlu tercermin di conceptual model (langkah 9).
- **Realisasi berbukti (AB-18)** sudah tersirat di KF-31 ("dan bukti") dan PKG-01 K3; di sini dijadikan wajib.
- **PKG-03 K4 dilonggarkan** menjadi "tautan bila struktur diubah" (catatan AB-25). Bila disetujui, analisis PKG-03 bagian 2 perlu disesuaikan.
- **UC-12 dan UC-26 boleh menautkan revisi atau rencana berikutnya kemudian**, karena revisi dan rencana berikutnya sering disusun setelah evaluasi atau tinjauan. Koreksi ini termasuk AB-22.

---

## 7. Perubahan dibanding versi sebelumnya

Versi sebelumnya ada di tag `rancangan-tatkel-v1` (AB-01–14). Dokumen ini **disusun ulang dengan penomoran baru**; nomor AB lama tidak berlaku.

| Versi lama | Versi ini | Alasan |
|---|---|---|
| Aturan tahap pemeriksaan dan tarik pengajuan | Dihapus | Tidak dirancang (keputusan 14 Nov 2026) |
| Pengesah harus pengguna yang login dengan jabatan berwenang | Pengesah tercatat (Personel, boleh tanpa akun) dicek wewenangnya; KaLab sebagai pencatat (AB-05, AB-06) | Dekan tidak login |
| Pengingat tinjau ulang dan realisasi | Dihapus; tanggal tinjau dan penanda dihitung (AB-14) | Prinsip "hitung, bukan jadwalkan" |
| — | Ditambah: rincian cek S1–S5 dan K1–K4 (AB-24, AB-25), rekaman bukti tidak dihapus (AB-22), penghapusan master (AB-23), pola «CRUDL» dan «report» | Keterlacakan ke kriteria dan matriks CRUDL |

---

## 8. Temuan untuk langkah 8 (SSD)

Kandidat operasi sistem dari alur bagian 4. Command mengubah data, query hanya membaca (CQS, §7.1). Nama final ditetapkan di langkah 8.

| UC | Query | Command |
|---|---|---|
| UC-01 | daftar dokumen Draf milik penyusun | ajukan dokumen |
| UC-03 | daftar dokumen Diajukan | unggah berkas bertanda tangan |
| UC-05 | daftar dokumen Diajukan; detail dokumen + pengesah berwenang | sahkan dokumen |
| UC-15 | daftar Dokumen Induk; detail Dokumen Induk + revisi berikutnya | buat versi |
| UC-18 | daftar versi berlaku | catat tinjau ulang |
| UC-23 | daftar KPI, daftar Personel; detail rencana | buat rencana, tambah item, tambah temuan gap |
| UC-25 | daftar item milik PIC | catat realisasi, koreksi realisasi |
| UC-28 | status monev | — |

Query daftar dokumen di UC-01, 03, 05 berpola sama dan bisa disatukan dengan parameter `filter` (status, penyusun).

## 9. Isu terbuka

- [ ] AB-05: jabatan pengesah dibaca dari data Personel, bukan dari SK **[ASUMSI]**
- [ ] AB-20: ukuran manfaat wajib untuk setiap item yang punya realisasi **[USULAN PENULIS]**
- [ ] AB-21: skala dan ambang prioritas **[USULAN PENULIS]**
- [ ] AB-25 PKG-01 K4: tinjauan periode sebelumnya ikut dihitung **[USULAN PENULIS]**
- [x] AB-25 PKG-03 K4: tautan ke revisi hanya bila struktur diubah. Disetujui Febriyan, 14 November 2026; analisis PKG-03 sudah disesuaikan
- [ ] AB-25 PKG-01 K1: Renstra sebagai *roadmap* **[KONFIRMASI Pak Widi]** (sudah di pertanyaan terbuka brief)
