# Analisis Data Indikator Pengelolaan 10 (otorisasi personel)

14 November 2026 · Zahir · PKG-10 · Bagian dari proyek LabFIK Compliance · Modul: SDM & Kompetensi (di sheet: Organization Management)

**Status: DRAF.** Bahan kerja Langkah 0 (prasyarat rancangan); bahan Bab I dan 2.2. Belum ada hasil wawancara: pertanyaan SDM & Kompetensi no. 16–19 di lembar "Wawancara FIKLAB Compliance" belum dijawab KaLab maupun laboran.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2. Package terkait: [PKG-04](analisis-data-pengelolaan-4.md) (Kompetensi, Bukti Kompetensi, Seleksi) dan [PKG-14](analisis-data-pengembangan-14.md) (pelatihan).

**Catatan penomoran:** di sheet ada **tiga baris "Pengelolaan 10"**: capaian KPI, legalitas lab, dan otorisasi personel. Dokumen ini hanya membahas baris **otorisasi personel** (PKG-10). Dua baris lainnya tidak termasuk 21 indikator proyek.

---

## 0. Sumber yang dipakai

| Sumber | Sifat | Dipakai untuk |
|---|---|---|
| Instrumen Monev Laboratorium UPNVJ 2026 v1.1, tab *Analysis* baris "Pengelolaan 10 (otorisasi)" | **Acuan resmi** | Target, kriteria, bukti dukung, usulan entitas |
| SNI ISO/IEC 17025:2017 klausul 6.2.5 e–f (otorisasi dan pemantauan kompetensi) dan 6.2.6 (pemberian wewenang) | **Acuan resmi** | Otorisasi per kegiatan, pemantauan berkala |
| Pedoman Diklatfung PLP 2022 (kompetensi) | Acuan resmi yang disebut instrumen; **belum dimiliki** **[VALIDASI]** | — |
| `07_SOP_Kompetensi_Penugasan_Otorisasi` (langkah 6, 10, tabel keputusan) dan `09_Formulir_…` (FRM-ASM-001 Asesmen Keterampilan, FRM-OTR-001 Otorisasi Tugas) | **Draf GPT** ("Templat contoh", isian simulasi) | Contoh format saja |
| `LABFIK-ISO17025-STD-01` Standar Sumber Daya, Kompetensi Personel, Peralatan | **Draf** versi 0.1 berisi placeholder **[VALIDASI asal dokumen]** | Contoh format saja |
| Dokumen nyata tentang izin, asesmen, atau otorisasi personel di LabFIK | **Tidak ditemukan** di Drive proyek (14 November 2026) | — |
| Slide "Presentasi Laboratorium PKKMB FIK" (baris 8 `ISO_LAB_SI`) | **Nyata** (bahan presentasi) | Alat/akses khusus per ruang: 3D printer dan VR (301), peralatan robotika (302), switch (304); form "pinjam 3D printer" dan "install software"; 4 laboran per ruang + 1 teknisi jaringan ([bedah dokumen](bedah-dokumen-sdm.md) A10, A21) |
| [kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md) | Draf Langkah 3 | Otorisasi tanpa `period.mixin` (K-3) |

**Kondisi saat ini sebagian diketahui:** lab punya alat khusus dan form permintaan untuk dua layanan (A21), tetapi tidak ada rekaman izin per personel. Alat mana yang wajib izin, siapa yang memberi izin, dan bagaimana pembatasannya masih **[KONFIRMASI KaLab/laboran]**.

---

## Ringkasan

| | Pengelolaan 10 |
|---|---|
| Inti | Setiap orang yang menjalankan tugas atau alat berkewenangan khusus punya otorisasi yang sah, sesuai kompetensinya, dan dievaluasi ulang bila ada perubahan |
| PJ | KaLab; PLP/laboran |
| Jenis skor | **Persentase** |
| Unit | 1 pasangan **personel × tugas/alat** yang memerlukan otorisasi dan aktif pada periode monev |
| Level cakupan (usulan) | **Otomatis** untuk persentase; keabsahan bukti diperiksa penilai |
| Posisi dalam dependensi | Hilir di dalam modul: memakai Kompetensi dan Bukti Kompetensi (PKG-04) dan sertifikat pelatihan (PKG-14). Hasil asesmen menambah Bukti Kompetensi |

**Temuan utama:**
1. **Otorisasi cocok dengan `labfik.approval.mixin`.** Siklusnya *diajukan → disahkan → diganti/dicabut*, dengan pengesah dan berkas. **Koreksi (Langkah 3):** `labfik.period.mixin` **tidak** dipakai, karena mixin itu menautkan dokumen ke satu periode bersama (`periode_id`), sedangkan masa berlaku otorisasi dihitung per orang sejak disahkan. Masa berlaku ditulis sebagai interval tanggal milik Otorisasi sendiri, dan status berlaku dihitung saat dibaca ([kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md) K-3).
2. **Masalah penyebut.** Instrumen menghitung "seluruh pasangan yang memerlukan otorisasi dan **aktif**". Orang yang memakai alat **tanpa** izin justru tidak tercatat di data otorisasi. Usulan: pasangan aktif diturunkan dari **jabatan pelaksana** di master tugas/alat (mis. tugas "administrasi server" dijalankan oleh jabatan laboran), sehingga orang yang wajib berizin tetapi belum berizin tetap masuk penyebut **[USULAN PENULIS; belum diputuskan, ditunda ke Langkah 4]**.
3. **Asesmen Keterampilan dipisah dari Seleksi Kompetensi PKG-04** (keputusan Zahir, 14 November 2026). Seleksi: per mata kuliah, saat rekrutmen, khusus asisten. Asesmen: per tugas/alat, kapan saja, untuk semua personel. Keduanya boleh menghasilkan Bukti Kompetensi.

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Seluruh personel/pengguna yang menjalankan tugas atau alat dengan kewenangan khusus memiliki otorisasi sesuai kompetensi |
| Penerapan / PJ | Umum / KaLab; PLP/laboran |
| Unit | Pasangan personel × tugas/alat |
| Jenis skor | Persentase (100% unit yang memenuhi) |
| Skor | 4: 100% unit memenuhi dan bukti dapat diverifikasi · 3: 90% sampai <100% · 2: 70% sampai <90% · 1: <70%, bukti gagal diverifikasi, atau bahaya kritis belum dikendalikan |
| Acuan | SNI ISO/IEC 17025:2017 6.2.5 dan 6.2.6 · Pedoman Diklatfung PLP 2022 (kompetensi) |

Bukti dukung: (1) matriks tugas/alat yang memerlukan otorisasi, (2) asesmen keterampilan, (3) daftar operator sah, (4) pembatasan akses, (5) evaluasi ulang.

**Rumus:** pembilang = jumlah pasangan personel × tugas/alat yang punya bukti kompetensi dan otorisasi berlaku; penyebut = seluruh pasangan yang memerlukan otorisasi dan aktif pada periode monev.

**Siapa yang dicakup (keputusan Zahir, 14 November 2026):** hanya **PLP/laboran**. Asisten, dosen, dan mahasiswa praktikan tidak dicakup. Instrumen menyebut "personel/pengguna" dan sheet memasukkan praktikan ke master personel, jadi pembatasan ini perlu disampaikan di batasan masalah **[KONFIRMASI pembimbing]**. Apakah teknisi dihitung sebagai laboran **[KONFIRMASI KaLab]**.

## 2. Aturan "memenuhi"

| Syarat | Arti (instrumen) | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| S1 Kompetensi dibuktikan | Kompetensi untuk tugas/alat itu terbukti | Ada **Asesmen Keterampilan** berkesimpulan *layak* untuk tugas/alat itu, **atau** Bukti Kompetensi berlaku untuk semua kompetensi yang disyaratkan tugas/alat itu | Mutu asesmen, keaslian sertifikat |
| S2 Cakupan kewenangan ditetapkan | Otorisasi sah dengan lingkup spesifik | Ada **Otorisasi** berstatus *disahkan* untuk pasangan itu, dengan lingkup/pembatasan terisi, dan tanggal penilaian berada dalam masa berlakunya | Keabsahan pengesah |
| S3 Pemula disupervisi | Pengguna pemula bekerja di bawah supervisi | Bila otorisasi berlevel *terbimbing*: ada supervisor yang **sendiri punya otorisasi mandiri** untuk tugas/alat yang sama | Supervisi benar-benar terjadi |
| S4 Dievaluasi bila ada perubahan | Otorisasi ditinjau saat ada perubahan | Tidak ada **pemicu evaluasi ulang** yang masih terbuka (belum diputuskan) pada pasangan itu | Kewajaran keputusan evaluasi |

Catatan:
- **Pemicu evaluasi ulang** (dari ISO 6.2.5 f dan draf SOP 07, perlu dikonfirmasi): masa berlaku habis, alat/metode/*software* berubah, terjadi insiden, lama tidak aktif. Masa berlaku dihitung sistem dari tanggal; pemicu lain dicatat manual oleh laboran/KaLab.
- **Bukti 4 (pembatasan akses)** tidak disebut di kalimat "unit dinyatakan memenuhi". **Keputusan (Zahir, 14 November 2026):** dicatat per tugas/alat di master (cara pembatasan + berkas bukti), **tidak** menjadi syarat persentase, dan sistem tidak memblokir pemakaian alat. Pembatasan fisik (kunci, akun) terjadi di luar sistem **[KONFIRMASI pembimbing]**.

## 3. Luaran

| Luaran | Bukti ke- | Jenis | Keterangan |
|---|---|---|---|
| Matriks Tugas/Alat Berkewenangan Khusus | 1 | [M] ditampilkan sebagai daftar | Isi master: tugas/alat, kompetensi yang disyaratkan, jabatan pelaksana, cara pembatasan |
| Asesmen keterampilan | 2 | [T] | — |
| Daftar Operator Sah | 3 | [R] | Per tugas/alat: siapa berizin, level, berlaku sampai. Dihasilkan dari Otorisasi |
| Pembatasan akses | 4 | Field + berkas di master | Lihat bagian 2 |
| Evaluasi ulang | 5 | [T] | — |
| Persentase PKG-10 per periode | — | [R] | Dari pasangan aktif dan status S1–S4 |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Asesmen Keterampilan** | 1 personel × 1 tugas/alat per kejadian | personel, tugas/alat, penilai, tanggal, metode (demonstrasi/uji praktik/tinjauan sertifikat), skor, unsur kritis terpenuhi (ya/tidak), kesimpulan (layak/belum layak), catatan pengembangan, berkas | Bila layak, sistem membuat Bukti Kompetensi (PKG-04) berjenis demonstrasi. Rekomendasi asesmen terpisah dari keputusan otorisasi (draf SOP 07; juga logis karena penilai ≠ pengesah) |
| **Otorisasi Personel** | 1 personel × 1 tugas/alat per versi | personel, tugas/alat, dasar (asesmen atau bukti kompetensi), lingkup dan pembatasan, level (*terbimbing*/*mandiri*), supervisor (wajib bila terbimbing), berkas; status, pengesah, riwayat dari `labfik.approval.mixin`; `berlaku_mulai`, `berlaku_sampai`, dan `is_berlaku` {compute} milik sendiri (bukan `period.mixin`) | Versi baru **mengganti** versi lama lewat *hook* `_dokumen_diganti()` (status *diganti*). Riwayat tidak hilang |
| **Evaluasi Ulang Otorisasi** | 1 per pemicu | otorisasi, pemicu (masa berlaku habis/alat atau metode berubah/insiden/lama tidak aktif/lainnya), tanggal pemicu, penilai, hasil, keputusan (diperpanjang/dibatasi/dinaikkan ke mandiri/dicabut), status (terbuka/diputuskan) | Bila diperpanjang/dibatasi/dinaikkan, dibuat Otorisasi versi baru. Bila dicabut, otorisasi lama berstatus *dicabut* |

Riwayat perubahan memakai `mail.thread` + `tracking`. Catatan supervisi harian untuk pemula ditunda (bagian 7); yang dicek cukup keberadaan supervisor yang berwenang.

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| **Tugas/Alat Berkewenangan Khusus** | Daftar hal yang wajib berizin (bukti 1) | **Baru, milik PKG-10.** Isi: nama, jenis (tugas/alat/*software*), tautan ke Alat (opsional), kompetensi yang disyaratkan, jabatan pelaksana, masa berlaku otorisasi standar (bulan), cara pembatasan akses, berkas bukti pembatasan, aktif | — |
| Alat | Tautan bila objeknya alat fisik | Asset Management (kelompok lain) | Nama alat ditulis langsung di master Tugas/Alat |
| Kompetensi, Bukti Kompetensi | Syarat dan bukti S1 | PKG-04 (modul sendiri) | — |
| Personel, Jabatan | Pemegang otorisasi, penilai, pengesah, supervisor; jabatan pelaksana | Core | Data contoh |
| Periode | Periode monev | Core | — |

**Penyesuaian terhadap sheet:** "Jenis/Level Otorisasi" ditulis sebagai master di sheet. Isinya hanya beberapa nilai tetap, jadi cukup **pilihan tetap** (*terbimbing*/*mandiri*), sesuai pedoman 4a. Jumlah master baru: **1**.

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Kompetensi, Bukti Kompetensi | PKG-04 (modul sendiri) | **Wajib** | — |
| Sertifikat pelatihan sebagai bukti kompetensi | PKG-14 (modul sendiri, lewat Bukti Kompetensi) | Opsional | Bukti diinput manual |
| Personel, Jabatan, Periode, `approval.mixin`, `evidence.mixin` | Core (versi branch `febriyan-skripsi`) | Wajib | — |
| Master Alat | Asset Management (kelompok lain) | Opsional | Nama alat sebagai teks di master Tugas/Alat |
| Insiden alat sebagai pemicu evaluasi ulang | Safety/Asset (kelompok lain) | Opsional | Pemicu dicatat manual |
| Log penggunaan alat (siapa memakai alat apa) | PKG-18 / Q04 di pemetaan | Opsional | Pasangan aktif diturunkan dari jabatan pelaksana |

**Dipakai oleh (peluang):** fungsi "apakah personel X berwenang untuk tugas/alat Y pada tanggal Z" bisa dipakai modul lain, misalnya Praktikum atau Aset saat mencatat pemakaian alat. Ini bukan syarat PKG-10 dan tidak dirancang sekarang.

## 7. Ditunda (tidak dirancang; saran pengembangan)

- Pemblokiran otomatis pemakaian alat atau akun oleh sistem. Cukup daftar operator sah dan pencatatan.
- Catatan supervisi harian untuk pemula (log pendampingan per sesi). Cukup supervisor berwenang yang tercantum di otorisasi.
- Otorisasi untuk asisten, dosen, dan mahasiswa praktikan. Cakupan dibatasi ke PLP/laboran.
- Pengingat otorisasi akan kedaluwarsa (notifikasi) dan penjadwal yang mengubah status menjadi *kedaluwarsa*. Cukup `is_berlaku` yang dihitung dari tanggal saat dibaca.
- Integrasi pemicu insiden otomatis dari modul Safety.

## 8. Pertanyaan untuk narasumber

Sudah ada di lembar wawancara (SDM & Kompetensi no. 16–19), belum dijawab. Yang paling menentukan rancangan:

| No. wawancara | Pertanyaan inti | Menentukan |
|---|---|---|
| 16 | Alat, *software*, atau pekerjaan apa yang hanya boleh dilakukan orang tertentu? Siapa yang biasanya melakukannya? | Isi master Tugas/Alat dan jabatan pelaksana (penyebut) |
| 17 | Bagaimana memastikan seseorang mampu sebelum diizinkan: praktik, uji, atau cukup sertifikat? | Metode Asesmen; apakah sertifikat cukup untuk S1 |
| 18 | Apakah izin berlaku selamanya? Kapan ditinjau ulang atau dicabut? | Masa berlaku standar dan daftar pemicu (S4) |
| 19 | Bagaimana mencegah orang tak berizin: dikunci, akun, diawasi? Sistem sebaiknya menolak, memperingatkan, atau mencatat? | Bukti 4; konfirmasi bahwa pemblokiran ditunda |
| 2 | Siapa yang menetapkan dan menandatangani izin alat/tugas khusus? | Pengesah Otorisasi |
| Tambahan | Apakah teknisi termasuk laboran? Berapa PLP/laboran aktif? | Cakupan pengguna; ukuran data uji |

## 9. Kompleksitas (perkiraan)

| T | M lokal | R |
|---|---|---|
| 3 (Asesmen Keterampilan, Otorisasi Personel, Evaluasi Ulang Otorisasi) | 1 (Tugas/Alat Berkewenangan Khusus) | 2 (Daftar Operator Sah, persentase) |

Pemetaan lama mencatat 3 T / 2 M / 1 R. Satu master turun menjadi pilihan tetap (Jenis/Level Otorisasi).
