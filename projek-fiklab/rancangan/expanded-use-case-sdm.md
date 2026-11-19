# Expanded Use Case dan Aturan Bisnis Modul SDM & Kompetensi

19 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 7 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Bahan kerja**, bukan diagram. Dipakai untuk SSD (langkah 8), conceptual model (langkah 9), pemetaan aturan ke mekanisme Odoo (langkah 10), dan Rencana Pengujian Bab II 2.4. Tabel deskripsi use case (bagian 3) dan katalog aturan bisnis (bagian 2) dimasukkan ke Bab II 2.3.

Sumber:
- [use-case-sdm.md](use-case-sdm.md): UC-SDM-01–28.
- [kebutuhan-sdm.md](kebutuhan-sdm.md): KF *hidden* dan KNF.
- [proses-bisnis-sdm.md](proses-bisnis-sdm.md): A1–A4, S1–S4 beserta tabel status × transisi.
- Analisis PKG-04, 10, 14: aturan "memenuhi" dan ambang skor.
- [kontrak-core-sdm.md](kontrak-core-sdm.md): model dan *hook*.

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Alur utama = urutan transaksi aktor → sistem, lurus, tanpa *if* atau perulangan | §6.2, §6.4 | Bagian 4 |
| Varian (V) = cara lain mencapai tujuan; eksepsi (E) = hambatan. Setiap alternatif berakhir jelas: berhasil, gagal, atau kembali ke langkah *n* | §6.3.2–6.3.3 | Bagian 4 |
| Setiap aturan bisnis biasanya melahirkan satu eksepsi | §6.3.3 | Eksepsi merujuk kode AB-SDM |
| *Essential*: tanpa tombol, layar, atau menu. Identifikasi dan pemilihan ditulis generik ("memilih otorisasi") | §6.4.1, §6.4.3 | Semua alur |
| Data yang dipertukarkan disebut eksplisit | §6.4.2 | Semua langkah |
| Hanya langkah wajib; "sistem menyimpan ke basis data" tidak ditulis | §6.4.4 | Langkah sistem berisi informasi yang dikembalikan dan perubahan yang terlihat |
| Prakondisi = fakta yang benar sebelum mulai; yang baru bisa dicek di tengah alur = eksepsi | §6.6.2 | Bagian 3 |
| Use case berpola («CRUDL», «report») cukup satu pola bersama | §6.7 | Bagian 5 |

---

## 2. Katalog aturan bisnis

Kolom **Lapis**: W = Inti, O = Pelengkap (berlaku hanya bila KF Pelengkapnya dibangun). Pemetaan ke mekanisme Odoo dilakukan di langkah 10.

### 2.1 Pengesahan dokumen SDM (Surat Tugas, Otorisasi, Rencana Pelatihan)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-01 | Dokumen SDM hanya dapat diubah dan diajukan selama berstatus **Draf**. Draf yang belum pernah diajukan boleh dihapus; selebihnya tidak | S1, S4 | UC-SDM-07, 08, 13, 17, 23 | W |
| AB-SDM-02 | **Surat Tugas** hanya dapat diajukan bila lengkap: minimal satu baris; setiap baris punya personel, peran, kelas (peran asisten) atau ruang (peran laboran), dan rentang berlaku di dalam periode surat; setiap asisten punya **seleksi lulus** (termasuk lulus dengan pengecualian) untuk mata kuliah kelasnya pada periode itu **[KONFIRMASI KB-3]** | KF-SDM-11; PKG-04 S2, S4 | UC-SDM-23 | W |
| AB-SDM-03 | **Otorisasi** hanya dapat diajukan bila: (a) kompetensi tugas/alat terbukti, yaitu ada asesmen *layak* untuk tugas/alat itu **atau** bukti kompetensi berlaku untuk semua kompetensi yang disyaratkannya; (b) lingkup terisi; (c) `berlaku_mulai` ≤ `berlaku_sampai` dan `berlaku_sampai` ≥ hari ini; (d) bila level *terbimbing*, supervisor terisi, bukan personel itu sendiri, dan punya otorisasi *mandiri* berlaku untuk tugas/alat yang sama | KF-SDM-23; PKG-10 S1, S3; S1 sel 3 | UC-SDM-23 | W |
| AB-SDM-04 | **Rencana Pelatihan** hanya dapat diajukan bila: setiap PLP/laboran dan teknisi aktif tercantum di kebutuhan (dengan kompetensi kurang, atau "tidak ada gap" beserta keterangan); setiap item punya kompetensi sasaran, jenis, materi, peserta, penyelenggara, anggaran, jadwal, dan kriteria keberhasilan; kompetensi sasaran item termasuk kebutuhan setiap pesertanya. Saat diajukan, daftar kebutuhan **dibekukan** | KF-SDM-32; PKG-14 K1, K2 | UC-SDM-23 | W |
| AB-SDM-05 | Berkas bertanda tangan hanya dapat diunggah atau diganti selama dokumen berstatus **Diajukan** | S1, S4 | UC-SDM-25 | W |
| AB-SDM-06 | Dokumen hanya dapat disahkan bila **berkas bertanda tangan** sudah diunggah | KF-SDM-06 | UC-SDM-27 | W |
| AB-SDM-07 | **Pengesah tercatat** harus Personel yang jabatannya berwenang *mengesahkan* jenis dokumen itu (`penugasan_petugas`, `otorisasi`, `rencana_pelatihan`) **[KONFIRMASI K7, K10]** | KF-SDM-43; PKG-04 S2, PKG-10 S2 | UC-SDM-27 | W |
| AB-SDM-08 | Hanya **KaLab** yang dapat mengembalikan, mengesahkan, dan mencabut dokumen SDM. KaLab dicatat sebagai **pencatat** | KNF-SDM-04 | UC-SDM-26, 27, 28 | W |
| AB-SDM-09 | Mengembalikan dan mencabut dokumen wajib disertai **alasan** | KF-SDM-06 | UC-SDM-26, 28 | W |
| AB-SDM-10 | Saat dokumen disahkan, dokumen yang digantikannya menjadi **Diganti**: surat tugas yang direvisi (O), atau otorisasi Disahkan lain untuk pasangan personel × tugas/alat yang sama. Untuk satu pasangan hanya ada satu otorisasi Disahkan | KF-SDM-14, 24; S1, S4 | UC-SDM-27 | W |
| AB-SDM-11 | Setiap kejadian pengesahan (diajukan, dikembalikan, berkas diunggah atau diganti, disahkan, diganti, dicabut) dicatat sebagai **riwayat** berisi waktu, pelaku, pengesah tercatat, alasan, dan berkas. Riwayat tidak dapat diubah atau dihapus | KF-SDM-06; KNF-SDM-05 | UC-SDM-23, 25–28 | W |
| AB-SDM-12 | Hanya ada satu **Rencana Pelatihan** Disahkan per periode tahunan | PKG-14 (1 paket per tahun) | UC-SDM-27 | W |

### 2.2 Kompetensi dan penugasan (PKG-04)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-13 | Bukti kompetensi **berlaku** pada tanggal T bila tanggal perolehannya ≤ T dan `berlaku_sampai` kosong atau ≥ T. Personel **memenuhi syarat jabatan** pada T bila setiap kompetensi wajib jabatannya punya bukti berlaku pada T | KF-SDM-04; PKG-04 S3 | UC-SDM-03, 04, 10, 17, 22 | W |
| AB-SDM-14 | Kebutuhan petugas ditetapkan **satu per kelas per peran** (asisten, laboran), jumlah minimal ≥ 0, dan wajib disertai dasar penetapan. Jumlah 0 berarti kelas itu memang tidak membutuhkan peran tersebut | KF-SDM-09; PKG-04 S1; A7 | UC-SDM-05 | W |
| AB-SDM-15 | Hasil seleksi hanya dicatat untuk calon yang **lulus** atau **lulus dengan pengecualian**. Pengecualian wajib mencatat **alasan** dan **penyetuju**. Satu personel punya paling banyak satu seleksi per mata kuliah per periode. Bila calon belum ada sebagai Personel, sistem membuatnya dengan jenis *asisten* dan jabatan Asisten Praktikum | KF-SDM-07, 08; PKG-04 S4 | UC-SDM-06 | W |
| AB-SDM-16 | Baris penugasan **berlaku** pada tanggal T bila suratnya Disahkan dan T berada di rentang berlakunya. Peran asisten wajib menunjuk kelas; peran laboran wajib menunjuk ruang | KF-SDM-10, 12; PKG-04 S2 | UC-SDM-07, 10, 22 | W |

### 2.3 Otorisasi (PKG-10)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-17 | Asesmen berkesimpulan *layak* membuat satu bukti kompetensi berjenis *demonstrasi* untuk setiap kompetensi yang disyaratkan tugas/alat itu. Masa berlakunya sama dengan masa berlaku standar tugas/alat **[USULAN PENULIS]** | KF-SDM-21 | UC-SDM-12 | W |
| AB-SDM-18 | Otorisasi **berlaku** pada tanggal T bila Disahkan dan T berada di antara `berlaku_mulai` dan `berlaku_sampai`. Nilai awal `berlaku_sampai` = `berlaku_mulai` + masa berlaku standar tugas/alat; KaLab boleh mengubahnya selama Draf | KF-SDM-22, 24; PKG-10 S2; K-3 | UC-SDM-13, 16, 22 | W |
| AB-SDM-19 | Pemicu evaluasi ulang hanya dicatat untuk otorisasi yang pernah disahkan dan belum Diganti atau Dicabut. Evaluasi hanya dapat diputuskan selama berstatus **Terbuka**; keputusan wajib disertai hasil dan penilai. Keputusan: diperpanjang, dibatasi, naik level, dicabut, atau tetap berlaku **[KONFIRMASI KP-1]** | KF-SDM-25; S2 | UC-SDM-14, 15 | W |

### 2.4 Pelatihan (PKG-14)

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-20 | Pengisian awal kebutuhan: untuk setiap PLP/laboran dan teknisi aktif, satu baris per kompetensi wajib jabatannya yang belum punya bukti berlaku pada tanggal mulai periode (AB-SDM-13); personel tanpa kekurangan dicatat "tidak ada gap" | KF-SDM-30; PKG-14 K1 | UC-SDM-17 | W |
| AB-SDM-21 | Realisasi hanya dicatat untuk item dari rencana **Disahkan** yang tidak batal, untuk peserta yang terdaftar di item itu. Satu realisasi per peserta per item. Realisasi pertama mengubah status item menjadi *terlaksana* | KF-SDM-33; S3 | UC-SDM-18 | W |
| AB-SDM-22 | Item hanya dapat dibatalkan selama berstatus *rencana* (belum ada realisasi), dengan alasan wajib. Item batal tidak dihitung di K3 | KF-SDM-37; S3 | UC-SDM-20 | O |
| AB-SDM-23 | Satu evaluasi efektivitas per realisasi. Evaluasi berkesimpulan *efektif* membuat bukti kompetensi berjenis *pelatihan* untuk kompetensi sasaran item, dengan sertifikat realisasi sebagai berkas | KF-SDM-34, 35; PKG-14 K4 | UC-SDM-19 | W |

### 2.5 Umum

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-24 | **Rekaman bukti** (bukti kompetensi, kebutuhan petugas, seleksi, orientasi, asesmen, evaluasi ulang, realisasi, evaluasi efektivitas) tidak dapat dihapus; hanya dapat dikoreksi dengan alasan, dan setiap koreksi terlacak | KNF-SDM-05 | UC-SDM-03, 05, 06, 09, 12, 14, 18, 19 | W |
| AB-SDM-25 | **Master** (Kompetensi, Tugas/Alat) hanya dapat dihapus bila belum dirujuk data lain; selebihnya diarsipkan | Matriks CRUDL | UC-SDM-01, 11 | W |

### 2.6 Status monev

| AB | Aturan | Sumber | UC | Lapis |
|---|---|---|---|---|
| AB-SDM-26 | **Persentase PKG-04** untuk satu periode:<br>• **Pembagi** = sesi praktikum berstatus *terlaksana* pada periode itu<br>• **Pembilang** = sesi yang lolos keempat syarat:<br>  S1 kelas sesi punya kebutuhan petugas untuk peran asisten dan laboran (AB-SDM-14)<br>  S2 jumlah baris penugasan berlaku pada tanggal sesi ≥ jumlah minimal tiap peran; asisten dicocokkan lewat kelas, laboran lewat ruang sesi (AB-SDM-16)<br>  S3 setiap petugas di S2 memenuhi syarat jabatan pada tanggal sesi (AB-SDM-13)<br>  S4 setiap asisten di S2 punya seleksi lulus untuk mata kuliah kelas itu pada periode itu (AB-SDM-15)<br>• **Skor**: 100% → 4; 90–<100% → 3; 70–<90% → 2; <70% → 1. Bila pembagi 0, skor tidak dihitung<br>• Untuk setiap sesi yang tidak lolos, ditampilkan syarat yang gagal | KF-SDM-12; analisis PKG-04 | UC-SDM-10, 22 | W |
| AB-SDM-27 | **Persentase PKG-10** pada tanggal acuan:<br>• **Pembagi** = pasangan pelaksana × tugas/alat aktif **[KONFIRMASI KB-1]**<br>• **Pembilang** = pasangan yang lolos:<br>  S1 ada asesmen *layak* untuk tugas/alat itu atau bukti kompetensi berlaku untuk semua kompetensinya<br>  S2 ada otorisasi berlaku dengan lingkup terisi (AB-SDM-18)<br>  S3 bila otorisasi *terbimbing*, supervisornya punya otorisasi *mandiri* berlaku untuk tugas/alat yang sama<br>  S4 tidak ada evaluasi ulang berstatus Terbuka untuk otorisasi pasangan itu<br>• **Skor** dan tampilan syarat yang gagal sama dengan AB-SDM-26 | KF-SDM-26; analisis PKG-10 | UC-SDM-16, 22 | W |
| AB-SDM-28 | **Kriteria tertinggi PKG-14** pada tanggal acuan = *k* terbesar sehingga K1 sampai K*k* semuanya lolos (berurutan):<br>  K1 ada Rencana Pelatihan Disahkan yang periodenya mencakup tanggal acuan, dengan kebutuhan mencakup semua PLP/laboran dan teknisi aktif<br>  K2 setiap item rencana itu lengkap dan sesuai gap (AB-SDM-04)<br>  K3 setiap item tidak batal yang jadwal selesainya ≤ tanggal acuan punya realisasi untuk setiap peserta, dengan sertifikat atau bukti hadir **dan** bukti penerapan<br>  K4 setiap realisasi di K3 punya evaluasi efektivitas berisi kesimpulan dan tindak lanjut<br>Sistem menampilkan kriteria tertinggi, tautan ke rekaman buktinya, dan kriteria berikutnya yang belum lolos beserta sebabnya. **Skor akhir ditetapkan penilai** | KF-SDM-36; analisis PKG-14 | UC-SDM-22 | W |

---

## 3. Tabel deskripsi use case

Semua use case selain «CRUDL» dan «report». Use case bertanda ★ dirinci alurnya di bagian 4. Prakondisi umum semua use case: aktor sudah teridentifikasi oleh sistem dan memegang grup akses yang sesuai (tidak diulang di tabel).

| UC | Tujuan | Aktor | Prakondisi | Pascakondisi sukses | Eksepsi |
|---|---|---|---|---|---|
| UC-SDM-05 Tetapkan Kebutuhan Petugas | Menetapkan jumlah minimal asisten dan laboran untuk setiap kelas | KaLab | Kelas periode berjalan terdaftar | Kebutuhan per kelas per peran tercatat dengan dasar penetapan | AB-SDM-14, AB-SDM-24 (koreksi) |
| UC-SDM-06 ★ Catat Hasil Seleksi Asisten | Merekam asisten yang lolos seleksi per mata kuliah | Pengelola Lab | Mata kuliah dan periode terdaftar | Seleksi tercatat; Personel asisten tersedia | AB-SDM-15, AB-SDM-24 |
| UC-SDM-07 ★ Susun Surat Tugas | Menyusun penugasan asisten per kelas dan laboran per ruang | Pengelola Lab | Periode, kelas, ruang terdaftar | Surat Tugas berstatus Draf dengan baris penugasan | AB-SDM-01, AB-SDM-16 |
| UC-SDM-08 Buat Revisi Surat Tugas (O) | Mengganti petugas di tengah periode | KaLab | Ada Surat Tugas Disahkan | Surat baru berstatus Draf, salinan baris surat lama, tertaut ke surat yang direvisi. Surat lama tetap Disahkan sampai revisi disahkan (AB-SDM-10) | — |
| UC-SDM-09 Catat Orientasi Petugas Baru (O) | Merekam orientasi atau supervisi petugas baru | Pengelola Lab | Personel terdaftar | Orientasi tercatat dengan jenis, pelaksana, tanggal, dan bukti | AB-SDM-24 |
| UC-SDM-12 ★ Catat Asesmen Keterampilan | Menilai kemampuan personel menjalankan tugas/alat | Pengelola Lab | Tugas/Alat dan Personel terdaftar | Asesmen tercatat; bila *layak*, bukti kompetensi demonstrasi terbentuk | AB-SDM-17, AB-SDM-24 |
| UC-SDM-13 ★ Susun Otorisasi | Menyusun izin personel untuk satu tugas/alat | KaLab | Tugas/Alat terdaftar | Otorisasi berstatus Draf dengan masa berlaku awal | AB-SDM-01, AB-SDM-18 |
| UC-SDM-14 Catat Pemicu Evaluasi Ulang | Merekam kejadian yang mengharuskan otorisasi ditinjau | Pengelola Lab | Ada otorisasi yang pernah disahkan | Evaluasi ulang berstatus Terbuka | AB-SDM-19 |
| UC-SDM-15 ★ Putuskan Evaluasi Ulang Otorisasi | Menetapkan keputusan atas evaluasi ulang | Pengelola Lab | Ada evaluasi ulang Terbuka | Evaluasi berstatus Diputuskan dengan hasil, penilai, dan keputusan | AB-SDM-19 |
| UC-SDM-17 ★ Susun Rencana Pelatihan | Menyusun kebutuhan dan item pelatihan untuk satu tahun | KaLab | Periode tahunan terdaftar | Rencana berstatus Draf dengan kebutuhan dan item | AB-SDM-01, AB-SDM-20 |
| UC-SDM-18 Catat Realisasi Pelatihan | Merekam keikutsertaan peserta dalam satu item pelatihan | Pengelola Lab | Ada rencana Disahkan | Realisasi tercatat dengan tanggal, durasi, sertifikat, bukti penerapan; item berstatus terlaksana | AB-SDM-21, AB-SDM-24 |
| UC-SDM-19 ★ Catat Evaluasi Efektivitas Pelatihan | Menilai dampak pelatihan pada kinerja peserta | Pengelola Lab | Ada realisasi tanpa evaluasi | Evaluasi tercatat; bila *efektif*, bukti kompetensi pelatihan terbentuk | AB-SDM-23, AB-SDM-24 |
| UC-SDM-20 Batalkan Item Pelatihan (O) | Menandai item yang tidak jadi dilaksanakan | KaLab | Ada item berstatus rencana | Item berstatus batal dengan alasan | AB-SDM-22 |
| UC-SDM-23 ★ Ajukan Dokumen SDM | Menyerahkan dokumen SDM yang lengkap untuk ditandatangani | Pengelola Lab | Ada dokumen SDM Draf | Dokumen berstatus Diajukan; untuk rencana, kebutuhan dibekukan; riwayat tercatat | AB-SDM-01–04 |
| UC-SDM-24 Terbitkan Dokumen SDM (O) | Mendapatkan PDF Surat Tugas atau Rencana Pelatihan untuk ditandatangani | Pengelola Lab | Dokumen berstatus Diajukan | PDF tersedia. Tidak ada perubahan data | Dokumen berjenis Otorisasi → gagal |
| UC-SDM-25 Unggah Dokumen SDM Bertanda Tangan | Melampirkan bukti tanda tangan pejabat | Pengelola Lab | Ada dokumen Diajukan | Berkas terlampir; riwayat tercatat | AB-SDM-05 |
| UC-SDM-26 Kembalikan Dokumen SDM | Mengembalikan dokumen kepada penyusun untuk diperbaiki | KaLab | Ada dokumen Diajukan | Dokumen berstatus Draf; riwayat dengan alasan tercatat | AB-SDM-08, AB-SDM-09 |
| UC-SDM-27 ★ Sahkan Dokumen SDM | Mencatat pengesahan dokumen yang sudah ditandatangani | KaLab | Ada dokumen Diajukan | Dokumen Disahkan dengan pengesah, pencatat, tanggal sah; dokumen lama Diganti; riwayat tercatat | AB-SDM-06, 07, 08, 10, 12 |
| UC-SDM-28 Cabut Dokumen SDM | Menghentikan berlakunya dokumen | KaLab | Ada dokumen Disahkan | Dokumen Dicabut; riwayat dengan alasan tercatat | AB-SDM-08, AB-SDM-09 |

---

## 4. Alur lengkap use case kunci

Dipilih karena punya aturan bisnis, membuat rekaman otomatis, atau mengubah status ([use-case-sdm.md](use-case-sdm.md) bagian 9.1). Use case ini menjadi dasar SSD di langkah 8. UC-SDM-22 memakai pola «report» (bagian 5.2) dengan aturan AB-SDM-26–28.

### UC-SDM-06 Catat Hasil Seleksi Asisten

**Alur utama**
1. Pengelola Lab menyerahkan periode dan mata kuliah.
2. Sistem menampilkan seleksi yang sudah tercatat untuk mata kuliah itu dan daftar Personel berjenis asisten.
3. Pengelola Lab menyerahkan calon (Personel yang ada), nilai mata kuliah, skor wawancara, simulasi, dan pengembangan modul, penilai, tanggal, keputusan *lulus*, dan berkas berita acara. [V1, V2]
4. Sistem menampilkan seleksi yang tercatat beserta pelapor. [E1, E2]

**Varian**
- **V1 Calon belum terdaftar sebagai Personel.** V1.1 Pengelola Lab menyerahkan nama calon sebagai pengganti Personel. V1.2 Sistem membuat Personel berjenis asisten dengan jabatan Asisten Praktikum (AB-SDM-15). V1.3 Kembali ke langkah 4.
- **V2 Lulus dengan pengecualian.** V2.1 Pengelola Lab menyerahkan keputusan *lulus dengan pengecualian*, alasan, dan penyetuju. V2.2 Kembali ke langkah 4.

**Eksepsi**
- **E1 Pengecualian tanpa alasan atau penyetuju (AB-SDM-15).** E1.1 Sistem menampilkan data yang wajib. E1.2 Kembali ke langkah 3.
- **E2 Seleksi untuk calon, mata kuliah, dan periode yang sama sudah ada (AB-SDM-15).** E2.1 Sistem menampilkan seleksi yang ada. E2.2 Use case gagal; perbaikan dilakukan dengan koreksi (AB-SDM-24).

### UC-SDM-07 Susun Surat Tugas

**Alur utama**
1. Pengelola Lab menyerahkan nomor surat dan periode. [V1]
2. Sistem menampilkan Surat Tugas berstatus Draf, daftar kelas periode itu beserta kebutuhan petugasnya, daftar ruang, dan daftar Personel.
3. Pengelola Lab menyerahkan baris penugasan: personel, peran, kelas (asisten) atau ruang (laboran), berlaku mulai, dan berlaku sampai.
4. Sistem menampilkan surat beserta barisnya dan penanda kelengkapan terhadap AB-SDM-02 (baris tidak lengkap, asisten tanpa seleksi lulus, kelas yang kebutuhannya belum terpenuhi). [V2, E1]

**Varian**
- **V1 Melanjutkan surat Draf.** V1.1 Pengelola Lab memilih Surat Tugas Draf yang sudah ada. V1.2 Sistem menampilkan surat beserta barisnya. V1.3 Kembali ke langkah 3. Bila surat bukan Draf, berlaku E1.
- **V2 Disimpan untuk dilanjutkan.** V2.1 Pengelola Lab menghentikan penyusunan. V2.2 Use case berhasil; surat tetap Draf.

**Eksepsi**
- **E1 Surat tidak lagi berstatus Draf (AB-SDM-01).** E1.1 Sistem menampilkan status surat. E1.2 Use case gagal.

Penanda kelengkapan tidak menghentikan penyimpanan; kelengkapan baru diwajibkan saat surat diajukan (UC-SDM-23, AB-SDM-02).

### UC-SDM-12 Catat Asesmen Keterampilan

**Alur utama**
1. Pengelola Lab meminta daftar tugas/alat berkewenangan khusus.
2. Sistem menampilkan daftar tugas/alat: nama, jenis, kompetensi yang disyaratkan, dan pelaksana.
3. Pengelola Lab memilih satu tugas/alat dan menyerahkan personel, penilai, metode, skor, unsur kritis terpenuhi, kesimpulan *layak*, catatan pengembangan, dan berkas lembar penilaian. [V1]
4. Sistem menampilkan asesmen yang tercatat dan bukti kompetensi berjenis demonstrasi yang terbentuk beserta masa berlakunya.

**Varian**
- **V1 Kesimpulan *belum layak*.** V1.1 Pengelola Lab menyerahkan data yang sama dengan kesimpulan *belum layak* dan catatan pengembangan. V1.2 Sistem menampilkan asesmen yang tercatat tanpa bukti kompetensi baru. V1.3 Use case berhasil.

Pembentukan bukti kompetensi (AB-SDM-17) adalah akibat langkah 4, tanpa interaksi tambahan (KF *hidden*, §4.7.2).

### UC-SDM-13 Susun Otorisasi

**Alur utama**
1. KaLab menyerahkan personel dan tugas/alat. [V1]
2. Sistem menampilkan Otorisasi berstatus Draf dengan masa berlaku awal (AB-SDM-18), asesmen dan bukti kompetensi personel yang relevan, serta daftar personel yang punya otorisasi *mandiri* berlaku untuk tugas/alat itu.
3. KaLab menyerahkan dasar (asesmen atau bukti kompetensi), lingkup dan pembatasan, level, supervisor (bila terbimbing), berlaku mulai, dan berlaku sampai.
4. Sistem menampilkan otorisasi beserta penanda kelengkapan terhadap AB-SDM-03. [E1]

**Varian**
- **V1 Otorisasi baru dari keputusan evaluasi ulang** (diperpanjang, dibatasi, naik level). V1.1 KaLab memilih evaluasi ulang yang sudah diputuskan. V1.2 Sistem menampilkan otorisasi Draf dengan personel, tugas/alat, dan lingkup dari otorisasi lama. V1.3 Kembali ke langkah 3.

**Eksepsi**
- **E1 Otorisasi tidak lagi berstatus Draf (AB-SDM-01).** E1.1 Sistem menampilkan status otorisasi. E1.2 Use case gagal.

### UC-SDM-15 Putuskan Evaluasi Ulang Otorisasi

**Alur utama**
1. Pengelola Lab meminta daftar evaluasi ulang yang masih Terbuka.
2. Sistem menampilkan daftar: personel, tugas/alat, pemicu, tanggal pemicu, dan masa berlaku otorisasi.
3. Pengelola Lab memilih satu evaluasi dan menyerahkan penilai, hasil, tanggal keputusan, dan keputusan *diperpanjang*. [V1, V2]
4. Sistem menampilkan evaluasi berstatus Diputuskan dan tindak lanjut yang perlu dilakukan: menyusun otorisasi baru (UC-SDM-13). [E1, E2]

**Varian**
- **V1 Keputusan *dicabut*.** V1.1 Pengelola Lab menyerahkan keputusan *dicabut*. V1.2 Sistem menampilkan evaluasi Diputuskan dan tindak lanjut: KaLab mencabut otorisasi (UC-SDM-28). V1.3 Use case berhasil.
- **V2 Keputusan *tetap berlaku* (KP-1).** V2.1 Pengelola Lab menyerahkan keputusan *tetap berlaku*. V2.2 Sistem menampilkan evaluasi Diputuskan tanpa tindak lanjut. V2.3 Use case berhasil.

Keputusan *dibatasi* dan *naik level* mengikuti alur utama (tindak lanjut otorisasi baru).

**Eksepsi**
- **E1 Hasil atau penilai kosong (AB-SDM-19).** E1.1 Sistem menampilkan data yang wajib. E1.2 Kembali ke langkah 3.
- **E2 Evaluasi tidak lagi Terbuka (AB-SDM-19)**, misalnya sudah diputuskan dari sesi lain. E2.1 Sistem menampilkan keputusan yang ada. E2.2 Use case gagal.

### UC-SDM-17 Susun Rencana Pelatihan

**Alur utama**
1. KaLab menyerahkan judul dan periode tahunan. [V2]
2. Sistem menampilkan Rencana berstatus Draf beserta daftar kebutuhan yang terisi awal: setiap PLP/laboran dan teknisi aktif dengan kompetensi wajib yang kurang, atau "tidak ada gap" (AB-SDM-20).
3. KaLab menyerahkan tambahan atau perbaikan kebutuhan beserta keterangan.
4. Sistem menampilkan kebutuhan yang diperbarui dan daftar kompetensi serta Personel yang dapat dipilih untuk item.
5. KaLab menyerahkan item pelatihan: kompetensi sasaran, jenis, materi, peserta, penyelenggara, anggaran, jadwal, dan kriteria keberhasilan.
6. Sistem menampilkan rencana beserta kebutuhan, item, dan penanda kelengkapan terhadap AB-SDM-04. [V1, E1]

**Varian**
- **V1 Disimpan untuk dilanjutkan.** V1.1 KaLab menghentikan penyusunan. V1.2 Use case berhasil; rencana tetap Draf.
- **V2 Melanjutkan rencana Draf.** V2.1 KaLab memilih rencana Draf. V2.2 Sistem menampilkan rencana dengan kebutuhan dan itemnya. V2.3 Kembali ke langkah 3. Bila rencana bukan Draf, berlaku E1.

**Eksepsi**
- **E1 Rencana tidak lagi berstatus Draf (AB-SDM-01).** E1.1 Sistem menampilkan status rencana. E1.2 Use case gagal.

### UC-SDM-19 Catat Evaluasi Efektivitas Pelatihan

**Alur utama**
1. Pengelola Lab meminta daftar realisasi yang belum dievaluasi.
2. Sistem menampilkan daftar: peserta, item, kompetensi sasaran, tanggal realisasi, dan kriteria keberhasilan.
3. Pengelola Lab memilih satu realisasi dan menyerahkan metode, skor sebelum dan sesudah, penilai, kesimpulan *efektif*, rekaman peningkatan layanan, tindak lanjut, dan berkas. [V1]
4. Sistem menampilkan evaluasi yang tercatat dan bukti kompetensi berjenis pelatihan yang terbentuk. [E1]

**Varian**
- **V1 Kesimpulan *perlu pengembangan*.** V1.1 Pengelola Lab menyerahkan data yang sama dengan kesimpulan *perlu pengembangan* dan tindak lanjut. V1.2 Sistem menampilkan evaluasi tanpa bukti kompetensi baru. V1.3 Use case berhasil.

**Eksepsi**
- **E1 Realisasi sudah punya evaluasi (AB-SDM-23).** E1.1 Sistem menampilkan evaluasi yang ada. E1.2 Use case gagal; perbaikan dengan koreksi (AB-SDM-24).

### UC-SDM-23 Ajukan Dokumen SDM

**Alur utama**
1. Pengelola Lab meminta daftar dokumen SDM Draf yang disusunnya.
2. Sistem menampilkan daftar dokumen Draf: jenis (Surat Tugas, Otorisasi, Rencana Pelatihan), nomor atau judul, periode atau personel, dan tanggal terakhir diubah.
3. Pengelola Lab memilih satu dokumen dan mengajukannya.
4. Sistem menampilkan dokumen dengan status Diajukan dan tanggal ajukan; untuk Rencana Pelatihan, kebutuhan ditandai dibekukan. [E1, E2]

**Eksepsi**
- **E1 Dokumen belum lengkap (AB-SDM-02, 03, 04 sesuai jenis).** E1.1 Sistem menampilkan bagian yang belum lengkap, misalnya asisten tanpa seleksi lulus, supervisor tanpa otorisasi mandiri, atau PLP yang belum tercantum di kebutuhan. E1.2 Use case gagal; dokumen tetap Draf.
- **E2 Dokumen tidak lagi berstatus Draf (AB-SDM-01).** E2.1 Sistem menampilkan status dokumen saat ini. E2.2 Use case gagal.

### UC-SDM-27 Sahkan Dokumen SDM

**Alur utama**
1. KaLab meminta daftar dokumen SDM Diajukan.
2. Sistem menampilkan daftar dokumen Diajukan: jenis, nomor atau judul, penyusun, tanggal ajukan, dan keterangan berkas bertanda tangan.
3. KaLab memilih satu dokumen.
4. Sistem menampilkan ringkasan isi dokumen, berkas bertanda tangan, riwayat pengesahan, dan daftar Personel yang jabatannya berwenang mengesahkan jenis dokumen itu.
5. KaLab menyerahkan pengesah tercatat dan tanggal sah.
6. Sistem menampilkan dokumen berstatus Disahkan dengan pengesah, pencatat, tanggal sah, dan dokumen yang digantikan (bila ada). [E1, E2, E3]

**Eksepsi**
- **E1 Berkas bertanda tangan belum ada (AB-SDM-06).** E1.1 Sistem menampilkan bahwa berkas belum diunggah. E1.2 Use case gagal; berkas diunggah lewat UC-SDM-25.
- **E2 Pengesah tidak berwenang (AB-SDM-07).** E2.1 Sistem menampilkan jabatan yang berwenang untuk jenis dokumen itu. E2.2 Kembali ke langkah 5. Bila berkas ditandatangani pejabat yang tidak berwenang, KaLab mengembalikan dokumen (UC-SDM-26).
- **E3 Sudah ada Rencana Pelatihan Disahkan untuk periode yang sama (AB-SDM-12).** E3.1 Sistem menampilkan rencana yang berlaku. E3.2 Use case gagal.

Penggantian dokumen lama (AB-SDM-10) dan pencatatan riwayat (AB-SDM-11) adalah akibat langkah 6, tanpa interaksi tambahan.

---

## 5. Pola bersama «CRUDL» dan «report» (§6.7)

### 5.1 Pola «CRUDL»

**Create:** 1. Aktor menyerahkan data konsep. 2. Sistem menampilkan data yang tercatat. [E1]
**Retrieve:** 1. Aktor memilih satu rekaman. 2. Sistem menampilkan seluruh datanya beserta data terkait.
**Update:** 1. Aktor memilih satu rekaman dan menyerahkan data yang diubah. 2. Sistem menampilkan data terbaru. [E1]
**Delete:** 1. Aktor memilih satu rekaman untuk dihapus. 2. Sistem menampilkan bahwa rekaman sudah tidak ada. [E2]
**List:** 1. Aktor menyerahkan filter (opsional). 2. Sistem menampilkan daftar rekaman yang sesuai.

**Eksepsi bersama**
- **E1 Data wajib kosong atau tidak valid.** Sistem menampilkan field yang bermasalah; kembali ke langkah 1.
- **E2 Rekaman tidak boleh dihapus** (master yang masih dirujuk, AB-SDM-25; rekaman bukti, AB-SDM-24). Sistem menampilkan alasannya dan menawarkan pengarsipan atau koreksi; use case gagal untuk penghapusan.

| UC | Konsep | Data wajib | Aturan khusus |
|---|---|---|---|
| UC-SDM-01 Kelola Kompetensi | Kompetensi | Nama (unik), jenis. Kode acuan opsional | AB-SDM-25 |
| UC-SDM-02 Kelola Syarat Kompetensi Jabatan | Kompetensi wajib per Jabatan | Jabatan, daftar kompetensi | — |
| UC-SDM-03 Kelola Bukti Kompetensi | Bukti Kompetensi | Personel, kompetensi, jenis bukti, tanggal perolehan, berkas. Nomor, penerbit, berlaku sampai opsional | AB-SDM-13, AB-SDM-24 (tidak dihapus) |
| UC-SDM-11 Kelola Tugas/Alat Berkewenangan Khusus | Tugas/Alat + pelaksana | Nama, jenis, kompetensi disyaratkan, masa berlaku standar (bulan). Pelaksana, lokasi, cara pembatasan (O) opsional saat disimpan | AB-SDM-25 |

### 5.2 Pola «report»

1. Aktor menyerahkan filter laporan.
2. Sistem menampilkan isi laporan.

Laporan tidak mengubah data. Bentuk keluarannya (layar atau PDF) adalah keputusan desain (§4.3.4).

| UC | Filter | Isi | Aturan |
|---|---|---|---|
| UC-SDM-04 Lihat Matriks Kompetensi | Tanggal acuan, jabatan | Personel × kompetensi wajib dengan penanda dimiliki-berlaku / kedaluwarsa / kurang | AB-SDM-13 |
| UC-SDM-10 Lihat Daftar Petugas per Sesi | Periode | Per sesi terlaksana: tanggal, kelas, ruang, kebutuhan, petugas, status S1–S4, syarat yang gagal | AB-SDM-26 |
| UC-SDM-16 Lihat Daftar Operator Sah | Tanggal acuan, tugas/alat | Per tugas/alat: personel, level, supervisor, berlaku sampai | AB-SDM-18 |
| UC-SDM-21 Lihat Rekap Pelatihan Personel (O) | Personel, periode | Kebutuhan, item yang diikuti, realisasi, evaluasi, bukti kompetensi yang terbentuk | — |
| UC-SDM-22 Lihat Status Monev SDM | Periode / tanggal acuan | PKG-04 dan PKG-10: persentase, skor, unit yang tidak lolos dan syaratnya. PKG-14: kriteria tertinggi, tautan bukti, kriteria berikutnya yang belum lolos. Laporan bukti untuk penilai memuat juga rekaman pendukung (orientasi, pembatasan akses) | AB-SDM-26–28 |

---

## 6. Cek silang

### 6.1 KF *hidden* → AB

| KF *hidden* | AB |
|---|---|
| KF-SDM-04 | AB-SDM-13 |
| KF-SDM-11 | AB-SDM-02 |
| KF-SDM-12 | AB-SDM-26 |
| KF-SDM-21 | AB-SDM-17 |
| KF-SDM-23 | AB-SDM-03 |
| KF-SDM-24 | AB-SDM-10, 18 |
| KF-SDM-26 | AB-SDM-27 |
| KF-SDM-30 | AB-SDM-20 |
| KF-SDM-32 | AB-SDM-04 |
| KF-SDM-35 | AB-SDM-23 |
| KF-SDM-36 | AB-SDM-28 |
| KF-SDM-41 | AB-SDM-26–28 (tautan bukti) |
| KF-SDM-43 | AB-SDM-07 |

Semua 13 KF *hidden* punya AB. AB tanpa KF khusus (AB-SDM-01, 05, 08, 09, 11, 12, 24, 25) bersumber dari state machine, KNF, atau matriks CRUDL, dan berada di dalam KF yang sudah ada.

### 6.2 Kriteria instrumen → AB

| Kriteria | AB |
|---|---|
| PKG-04 S1–S4 | AB-SDM-26 (memakai AB-SDM-13–16, 02, 07) |
| PKG-10 penyebut, S1–S4 | AB-SDM-27 (memakai AB-SDM-03, 17–19) |
| PKG-14 K1–K4 | AB-SDM-28 (memakai AB-SDM-04, 12, 20–23) |

### 6.3 Temuan untuk langkah sebelumnya

| Temuan | Tindakan |
|---|---|
| Kandidat aturan dari langkah 5 (`berlaku_sampai ≥ hari ini` saat otorisasi diajukan; realisasi hanya bila rencana disahkan) | Masuk AB-SDM-03 (c) dan AB-SDM-21 |
| Masa berlaku bukti demonstrasi dari asesmen belum ditetapkan di KF-SDM-21 | AB-SDM-17 **[USULAN PENULIS]**: sama dengan masa berlaku standar tugas/alat |
| AB-SDM-12 (satu rencana Disahkan per tahun) belum tertulis di KF | Sudah tercermin di kontrak Core (`«unique» periode_id`); tidak perlu KF baru |
| Supervisor tidak boleh personel itu sendiri | Ditambah di AB-SDM-03 (d) |

---

## 7. Temuan untuk langkah 8 (SSD)

Kandidat operasi sistem dari alur bagian 4. Command mengubah data, query hanya membaca (CQS, §7.1). Nama final di langkah 8.

| UC | Query | Command |
|---|---|---|
| UC-SDM-06 | daftar seleksi per MK/periode, daftar personel asisten | catat seleksi |
| UC-SDM-07 | detail surat (+ kelas, kebutuhan, ruang, personel, kelengkapan) | buat surat tugas, simpan baris penugasan |
| UC-SDM-12 | daftar tugas/alat | catat asesmen |
| UC-SDM-13 | detail otorisasi (+ dasar, calon supervisor, kelengkapan) | buat otorisasi, ubah otorisasi |
| UC-SDM-15 | daftar evaluasi terbuka | putuskan evaluasi |
| UC-SDM-17 | detail rencana (+ kebutuhan awal, kelengkapan) | buat rencana, simpan kebutuhan, simpan item |
| UC-SDM-19 | daftar realisasi belum dievaluasi | catat evaluasi efektivitas |
| UC-SDM-23 | daftar dokumen SDM (filter: status Draf, penyusun) | ajukan dokumen |
| UC-SDM-27 | daftar dokumen SDM (filter: status Diajukan); detail dokumen + pengesah berwenang | sahkan dokumen |
| UC-SDM-22 | status monev | — |

Query daftar dokumen di UC-SDM-23 dan 27 berpola sama dan disatukan dengan parameter `filter`.

## 8. Isu terbuka

- [ ] AB-SDM-02: Surat Tugas ditolak bila ada asisten tanpa seleksi lulus **[KONFIRMASI KB-3]**
- [ ] AB-SDM-07: jabatan pengesah Surat Tugas dan Rencana Pelatihan **[KONFIRMASI K7, K10]**
- [ ] AB-SDM-17: masa berlaku bukti demonstrasi **[USULAN PENULIS]**
- [ ] AB-SDM-19: keputusan *tetap berlaku* **[KONFIRMASI KP-1]**
- [ ] AB-SDM-27: penyebut PKG-10 = pelaksana yang ditetapkan KaLab **[KONFIRMASI KB-1]**
