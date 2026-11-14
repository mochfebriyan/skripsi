# Bedah Dokumen SDM & Kompetensi (Studi Dokumen)

14 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Bahan kerja Langkah 2. Temuan as-is (bagian 3) masuk 2.1 Observasi. Semua usulan model dan field masih **[USULAN PENULIS]** sampai ditetapkan di rancangan (Langkah 9–10), dalam batas [cakupan rancangan](../brief/brief-sdm.md#cakupan-rancangan) di brief.

## Tujuan

Dokumen ini membedah dokumen dan data lab yang berkaitan dengan personel praktikum, kompetensi, otorisasi, dan pelatihan. Setiap bagian dokumen diterjemahkan menjadi **field dan model** untuk rancangan TO-BE, dan setiap field ditelusuri ke dasarnya (instrumen, ISO, atau hanya format).

| Bagian proposal | Yang dipakai |
|---|---|
| 2.1 Observasi (studi dokumen) | [Bagian 3: Temuan as-is](#3-temuan-as-is-bahan-21-observasi) |
| 2.2 Usulan Solusi | [Bagian 2: Peran dan peluang otomasi](#2-peran-di-dokumen-dan-peluang-otomasi) |
| 2.3 Rancangan (class diagram) | [Bagian 5](#5-pola-berulang--inheritance) dan [bagian 6](#6-daftar-model-to-be-konsolidasi) |
| Lampiran | Seluruh dokumen ini sebagai hasil studi dokumen |

## Aturan yang dipakai

| Aturan | Sumber | Penerapan di dokumen ini |
|---|---|---|
| Semua sumber dipakai, termasuk dokumen; **asal setiap kebutuhan dilacak** agar bisa divalidasi ke sumbernya | Wazlawick §4.7, §4.7.1 | Kolom **Dasar** dan **Sumber** di setiap tabel |
| Bila dua sumber memberi spesifikasi berbeda, dicari kesepakatan atau dipakai pihak yang paling berwenang | Wazlawick §4.7.1 | Urutan: Instrumen/ISO → dokumen nyata → draf. Konflik dicatat di bagian 3 |
| Kebutuhan **evident** (pertukaran data dengan pengguna) dipisah dari **hidden** (dihitung sistem tanpa aksi pengguna) | Wazlawick §4.7.2 | Kolom **Jenis** di [bagian 6](#6-daftar-model-to-be-konsolidasi) dan [bagian 7](#7-laporan-r-dan-nilai-terhitung) |
| Batasan yang menempel pada fungsi = nonfungsional; batasan umum = suplementer | Wazlawick §4.7.3 | [Bagian 8: Data pribadi](#8-data-pribadi-batasan-nonfungsional) |
| Peran di luar organisasi = *business actor*; di dalam = *business worker* | Wazlawick §2.6.1 | [Bagian 2](#2-peran-di-dokumen-dan-peluang-otomasi) |
| Peran *worker* yang hanya menjadi perantara (rekap, salin data) adalah kandidat otomasi | Wazlawick §2.6.2 | [Bagian 2](#2-peran-di-dokumen-dan-peluang-otomasi) |
| Field dari draf GPT dipakai **hanya bila** juga didukung instrumen atau analisis | CLAUDE.md bagian 3, 8 | Kolom **Dasar**: `Instr`, `ISO`, `Analisis`, atau `Format` |
| Data pribadi tidak disalin | CLAUDE.md bagian 3 | Nama, NIM, nomor HP, email, dan nilai dari dokumen nyata **tidak** ditulis. Yang dicatat hanya struktur kolom, jumlah, dan jabatan |

Label `[T]`/`[M]`/`[R]` dan nama master mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md#4-konvensi-penamaan). Nama model memakai pola `labfik.sdm.<objek>` (CLAUDE.md bagian 6).

---

## 1. Dokumen yang dibedah

| ID | Dokumen | Lokasi | Sifat | Tanggal / periode | PKG |
|---|---|---|---|---|---|
| D1 | POB Manajemen Praktikum dan Asistensi FIK, beserta formulirnya (alokasi, pendaftaran, berita acara penilaian, daftar asisten, monitoring alokasi dan pelaksanaan, lembar pelaksanaan, kuesioner, evaluasi kendala) | `LABFIK_POB_Praktikum.pdf`, Drive proyek | **Nyata**. Kolom nomor dokumen, tanggal efektif, dan pengesahan **kosong** | 2025 | 04 |
| D2 | Spreadsheet "Alokasi Pertemuan Asisten Praktikum" (versi diubah 13 November 2026) | Google Sheets milik akun LabFIK. Tab: `ALOKASI_ASISTEN_PER_MINGGU_2627` (2026/2027 Ganjil), `ALOKASI_ASISTEN_PER_MINGGU_2526` (2025/2026 Genap), `Sheet7` (2025/2026 Ganjil), `LOV Nama Asisten …`, dan tab rekap | **Data nyata** (memuat data pribadi). **Dihitung penuh** dari ekspor xlsx, lihat [cara hitung](#cara-hitung-d2-dan-d3) | 3 periode; 2026/2027 Ganjil masih berjalan | 04 |
| D3 | Spreadsheet "Pelaksanaan Asistensi Praktikum LABFIK UPNVJ (Responses)" (jawaban Google Form; versi diubah 6 November 2026) | Google Sheets milik akun LabFIK. Tab: `Form Responses 1`, `KONTAK_ASISTEN`, `Per Pertemuan`, `Per Asisten`, `Per Mata Kuliah` | **Data nyata** (memuat data pribadi). **Dihitung penuh** dari ekspor xlsx | 1.147 jawaban: 2024/2025 Genap 312, 2025/2026 Ganjil 286, 2025/2026 Genap 466, 2026/2027 Ganjil 83 | 04 (dan 18) |
| D4 | Folder "Peningkatan Kompetensi Personel Laboratorium" (baris 10 sheet `ISO_LAB_SI`): dua sertifikat milik satu personel | Drive LabFIK, ditautkan dari iso.upnvj | **Nyata** | Desember 2024 dan Oktober 2025 | 14 (dan 04, 10) |
| D5 | Sheet `ISO_LAB_SI`: daftar 23 dokumen yang diunggah lab ke iso.upnvj | Google Sheets (Febriyan) | **Nyata** (daftar) | 2026 | semua |
| D6 | Paket Manajemen Praktikum LABFIK 2026: STD-PRK-03 (seleksi, kualifikasi, alokasi asisten), FRM-PRK-02 (formulir seleksi), FRM-PRK-09 (komitmen asisten), REG-PRK-01 (workbook register operasional), MTX-PRK-01 (matriks revisi POB) | Drive proyek, folder `LABFIK_Paket_Manajemen_Praktikum_2026` | **Draf** (README: "DRAFT", pengembangan dari D1 dan "Lembar Seleksi Asisten"). Gaya dan istilahnya diduga hasil GPT **[VALIDASI]** | September 2026 | 04 |
| D7 | Paket Dokumen Monev: `07_SOP_Kompetensi_Penugasan_Otorisasi`, `09_Formulir_Perencanaan_Kompetensi_Risiko` (FRM-ASM-001, FRM-OTR-001, FRM-TGS-001, FRM-DIK-001) | Drive proyek, folder `DOCUMENTS` | **Draf GPT** (status "Templat contoh", isian simulasi) | Oktober 2026 | 04, 10, 14 |
| D8a | "Presentasi Laboratorium PKKMB FIK 2025" (Google Slides; isi slide pertama menyebut PKKMB 2026), baris 8 `ISO_LAB_SI` | Drive LabFIK, dibuka dari tautan baris 8 | **Nyata** (bahan presentasi, bukan penetapan) | 2025/2026 | 04, 10 |
| D8b | "SK SOTK FIK 2025.pdf": Keputusan Dekan No. 3258/UN61/KP.04.00/2025 tentang SOTK FIK, baris 9 `ISO_LAB_SI` | Drive LabFIK, dibuka dari tautan baris 9 | **Nyata**, ditetapkan Dekan | September 2025 | 04, 14 |

Keduanya juga dibedah Febriyan di [bedah-dokumen-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/analisis/bedah-dokumen-tata-kelola.md) (D5, D6 di sana); di sini dibaca langsung untuk bagian yang menyangkut SDM.

**Dicek tetapi tidak dipakai:** baris 17 `ISO_LAB_SI` ("Logbook Penggunaan Laboratorium") ternyata jawaban form peminjaman ruang lab, dan baris 18/20 adalah salinan jadwal kuliah FIK 2026/2027 Ganjil. Keduanya tidak memuat data petugas, jadi milik modul Praktikum/Aset.

**Dokumen yang disebut tetapi tidak ditemukan:** "Lembar Seleksi Asisten Praktikum" (README D6 menyebutnya "diberikan") dan "Surat Kontrak Asisten Praktikum" (langkah 5 D1). Keduanya dokumen nyata yang paling dekat dengan S2 dan S4 PKG-04 **[KONFIRMASI: minta salinan ke KaLab]**.

**Tidak ada dokumen nyata tentang izin, asesmen, atau otorisasi personel (PKG-10).** Satu-satunya jejak adalah daftar alat/akses khusus per ruang dan form layanan di slide PKKMB (A21). Kebutuhan PKG-10 tetap diturunkan dari instrumen lewat [analisis Pengelolaan 10](analisis-data-pengelolaan-10.md).

---

## 2. Peran di dokumen dan peluang otomasi

Peran yang muncul di D1 dan D2, dipilah menurut Wazlawick §2.6.1:

| Peran | Muncul di | Jenis (§2.6.1) | Yang dilakukan di dokumen | Di TO-BE |
|---|---|---|---|---|
| Koordinator Program Studi | D1 langkah 1; Formulir Alokasi (diajukan oleh) | *Business actor* (prodi, di luar lab) | Mengirim daftar MK praktikum dan jumlah kelas | Bukan aktor sistem. Data MK/kelas datang dari Core/PKG-15 |
| Wakil Dekan Bidang Akademik | Formulir Alokasi (disetujui oleh) | *Business actor* | Menyetujui alokasi MK dengan asisten | Bukan aktor sistem (penanda tangan) |
| Dekan | D1 langkah 2 dan pengesahan POB | *Business actor* | Mengumumkan rekrutmen (bersama KaLab); mengesahkan POB | Bukan aktor sistem |
| Kepala Laboratorium | D1 langkah 2, 4, 12, 13; Formulir Alokasi (ditinjau oleh) | *Business worker* | Menyeleksi calon asisten (administrasi, wawancara, teknis); evaluasi kegiatan | **Aktor sistem** |
| Laboran | D1 langkah 8, 12, 16; Monitoring Alokasi dan Pelaksanaan (paraf) | *Business worker* | Menyiapkan sarana; memantau alokasi dan pelaksanaan asisten | **Aktor sistem** |
| Teknisi Laboratorium | D1 (kualifikasi pelaksana); D8a (1 teknisi jaringan) | *Business worker* | Mengelola sarana dan prasarana | Peserta PKG-14 (keputusan 14 Nov 2026); PKG-10 **[KONFIRMASI apakah termasuk laboran]** |
| Asisten Praktikum | D1 langkah 3–7, 9–11, 14–15; D2; D3 | *Business worker* setelah dikontrak (calon asisten = *business actor*) | Mendaftar, diseleksi, dikontrak, memilih pertemuan bersama dosen, mengisi Google Form tiap sesi | Objek penugasan (Personel). **Bukan aktor sistem** di proposal (brief) |
| Dosen Pengampu / Koordinator / Tandem | D1; D2 (tiga kolom dosen) | *Business actor* (prodi) | Memberi materi, mengembangkan modul, menilai | Tidak dicakup modul ini |
| Bagian Tata Usaha | D1 (kolom pelaksana) | *Business actor* | Tidak dijelaskan di penjelasan prosedur | Tidak dicakup |

**Peluang otomasi (§2.6.2):** di dokumen nyata ada tiga pekerjaan perantara yang hanya menyalin atau merekap data. Ketiganya diganti laporan `[R]` yang dihitung dari data, tidak diinput:

| Pekerjaan perantara saat ini | Sumber | Di TO-BE |
|---|---|---|
| Pivot "Rekap Per Matkul", "Rekap Per Asisten", "Total Alokasi Asisten" disusun manual dari sheet alokasi | D2 | Daftar Sesi dan Petugas `[R]`, dihitung dari Penugasan |
| Kolom "CEK IF 9=7" (cek kesamaan asisten antarminggu) dan "Jumlah Alokasi Per Kelas" | D2 | Tidak diperlukan: penugasan per kelas dicatat sekali dengan rentang berlaku |
| Pivot "Per Pertemuan", "Per Asisten", "Per Mata Kuliah" dari jawaban Google Form untuk honor | D3 | Di luar cakupan (honor). Pelaksanaan sesi milik PKG-18 |

---

## 3. Temuan as-is (bahan 2.1 Observasi)

Temuan hanya berasal dari isi dokumen. Klaim tentang praktik sehari-hari tetap harus dikonfirmasi lewat wawancara.

| No | Temuan | Sumber | Dampak ke indikator | Status |
|---|---|---|---|---|
| A1 | POB manajemen praktikum dan asistensi **sudah ada** (versi 2025) dan mengatur alur 17 langkah: alokasi MK → pengumuman rekrutmen → pendaftaran → seleksi → kontrak → alokasi jadwal → … → rekapitulasi | D1 | PKG-04: prosedur seleksi dan penugasan asisten punya dasar tertulis | Fakta dokumen |
| A2 | Kolom **nomor dokumen, tanggal efektif, jadwal reviu, dan pengesahan POB kosong** | D1 | PKG-04 S2 (penugasan sah) tidak bisa merujuk prosedur yang disahkan. Beririsan dengan PKG-02 (Tata Kelola) | Fakta dokumen. Ada tidaknya versi bertanda tangan **[VALIDASI]** |
| A3 | Seleksi asisten oleh KaLab terdiri atas **seleksi administrasi** (nilai sesuai syarat), **wawancara** (motivasi), dan **teknis** (mengajar dan mengembangkan modul). Berita acara mencatat tiga nilai: wawancara, simulasi pengajaran, pengembangan modul, beserta nama, NIP, dan jabatan penilai | D1 langkah 4; Berita Acara Penilaian | PKG-04 S4 (syarat internal) dan bukti 5 (uji keterampilan): bentuk rekamannya sudah ada di format | Fakta dokumen |
| A4 | **Besaran syarat nilai MK tidak tertulis** di POB: hanya "nilai sesuai syarat". Formulir pendaftaran punya kolom "Nilai", "Hasil Periksa", dan "Tempuh Kesesuaian" per MK yang dipilih | D1 | PKG-04 bukti 6 (KHS asisten, usulan ≥70): ambang belum ditetapkan. Klaim "nilai A" di pendahuluan belum punya sumber dokumen | Fakta dokumen; besaran syarat **[KONFIRMASI KaLab]** |
| A5 | Asisten **memilih pertemuan** yang diisi lewat koordinasi dengan dosen berdasarkan jadwal kelas | D1 langkah 6 | Mendukung keputusan penugasan **per kelas** (asisten memilih kelas) | Fakta dokumen |
| A6 | Sheet alokasi mencatat **satu nama asisten per kelas per pertemuan** (14 kolom pertemuan: 1–7 dan 9–15). Di kelas yang punya asisten, hampir selalu **satu asisten untuk seluruh semester** (107 dari 109 kelas; satu kelas berisi 2 nama dan satu kelas 3 nama). Pertemuan pertama yang terisi **tidak selalu pertemuan 1**: 2025/2026 Ganjil mulai pertemuan 2–7, 2025/2026 Genap semuanya pertemuan 1, 2026/2027 Ganjil sebagian besar pertemuan 5 (29 kelas), sisanya 9 dan 13 | D2 (hitung penuh) | PKG-04: penugasan memang per kelas, tetapi perlu **rentang berlaku** (mulai pertemuan/tanggal). Pergantian asisten di tengah semester jarang tetapi ada (pengganti = Pelengkap) | Fakta data. Alasan mulai terlambat **[KONFIRMASI K8]** |
| A7 | Kelas tanpa asisten (semua sel pertemuan kosong): **2025/2026 Ganjil 40 dari 71 (56,3%)**, **2025/2026 Genap 33 dari 79 (41,8%)**, **2026/2027 Ganjil 40 dari 72 (55,6%)**. Sheet tidak punya kolom yang menyatakan kelas itu **memang tidak butuh** asisten | D2 (hitung penuh) | PKG-04 S1: kebutuhan petugas tidak ditetapkan, jadi kelas tanpa asisten tidak bisa dinilai. Angka draf pendahuluan (42–56%) **terkonfirmasi** | Fakta data |
| A8 | Sheet "LOV Nama Asisten 2526 Genap" memuat angka ringkas **630 vs 1.008 (62,50%)** tanpa keterangan. Hitungan ulang untuk periode yang sama: 644 dari 1.106 sel pertemuan terisi (58,2%). 1.008 = 72 kelas × 14 pertemuan, yaitu jumlah kelas periode **lain** (2026/2027 Ganjil) | D2 (hitung penuh) | Angka ringkas di sheet tidak bisa dipakai sebagai bukti; rumusnya kemungkinan merujuk rentang yang salah | Fakta data. Rumus sel **[VALIDASI ke laboran]** |
| A9 | **Laboran/PLP tidak tercatat** di sheet alokasi maupun jawaban Google Form (tidak ada kolom yang memuat kata "laboran"). Data petugas hanya mencakup asisten dan dosen | D2, D3 (hitung penuh) | PKG-04: laboran/PLP, petugas yang wajib di setiap sesi, tidak punya rekaman penugasan | Fakta data |
| A10 | Slide PKKMB mencantumkan tenaga kependidikan lab dengan **ruang tanggungannya**: 1 laboran untuk ruang 201, 1 untuk 301, 1 untuk 302–304, 1 untuk 401–403, dan 1 **teknisi jaringan** tanpa ruang. Bebannya tidak rata: satu laboran memegang tiga ruang | D8a, slide "Tenaga Kependidikan & Staff Kebersihan" | PKG-04: penugasan laboran **per ruang**, bukan per kelas. Sesi mendapat laboran dari ruangnya. S1 ("kebutuhan menurut beban kerja") relevan untuk laboran yang memegang 3 ruang | Slide bukan penetapan resmi **[KONFIRMASI K3]** |
| A11 | Asisten melapor **setiap sesi** lewat Google Form: periode, MK, kelas, tanggal, jam, ruang (8 ruang FIKLAB-201 s.d. 403), pertemuan ke, jumlah mahasiswa hadir, dosen hadir (ya/tidak), topik, kesiapan sarana, kendala, modul, foto. Total 1.147 laporan dari 67 nama asisten berbeda | D3 (hitung penuh) | Bukan milik PKG-04 (pelaksanaan = PKG-18). Tetapi menunjukkan sesi **terlaksana** dan siapa asisten yang **benar-benar hadir**; ini yang dipakai untuk penyebut PKG-04. Sesi tanpa asisten tidak punya laporan sama sekali, jadi penyebut tidak bisa diambil dari D3 | Fakta data |
| A12 | Kualitas data D3 rendah: kolom "NIM Asisten" hanya berisi NIM pada 789 dari 1.147 baris (sisanya nama huruf kecil atau kosong); kolom "Dosen Koordinator" bernilai `#REF!` di **semua** baris; 166 baris punya tanggal sesi yang berselisih lebih dari 60 hari dari *timestamp* (salah ketik tahun atau tertukar hari/bulan); format nama MK berubah antarperiode (2024/2025 Genap tanpa kode MK) | D3 (hitung penuh) | Pembuktian berbasis Google Form rapuh. Menguatkan masalah M4 di brief (skor tidak tertelusur) | Fakta data |
| A13 | Bukti "Peningkatan Kompetensi Personel" yang diunggah ke iso.upnvj hanya berisi **dua sertifikat milik satu personel**: (a) sertifikat kompetensi BNSP/LSP (skema Data Analyst, 7 unit kompetensi berkode SKKNI, **berlaku 3 tahun**), (b) sertifikat pelatihan dari lembaga swasta (24 JP, tanpa masa berlaku). Tidak ada analisis kebutuhan, rencana pelatihan, maupun evaluasi efektivitas | D4, D5 | PKG-14: K1 (kebutuhan dan rencana ditetapkan) belum berbukti; yang ada hanya sebagian bukti K3. Pemegang kedua sertifikat adalah **laboran ruang 201** (cocok dengan nama di D8a), jadi memang personel yang dicakup PKG-14. Relevansinya dengan tugas lab (ruang 201 = Lab Software Engineering) tidak dinyatakan di dokumen mana pun (K2 "sesuai gap tugas") | Fakta dokumen. Relevansi dengan gap tugas **[KONFIRMASI KaLab]** |
| A14 | Status "Terverifikasi 100%" tercantum pada semua 23 baris di `ISO_LAB_SI`, termasuk baris 10 yang isinya hanya dua sertifikat | D5 | Status di web tidak bisa dipakai sebagai bukti terpenuhinya kriteria | Fakta dokumen (sama dengan temuan A12 Tata Kelola) |
| A15 | POB mencatat "Evaluasi Kinerja Asisten" sebagai rekaman, tetapi **formulirnya tidak ada** di lampiran POB | D1 (Pencatatan dan Pendataan no. 4) | Bukan syarat PKG-04. Dicatat sebagai celah dokumen | Fakta dokumen |
| A16 | Tidak ditemukan daftar tugas/alat berkewenangan khusus, izin pemakaian alat, maupun asesmen keterampilan personel | D1–D5 | PKG-10: belum ada bukti apa pun | Tidak ditemukan di dokumen yang dibagikan. Belum tentu tidak ada **[KONFIRMASI]** |
| A17 | SK SOTK FIK hanya memuat satu jabatan lab, **Kepala Laboratorium**, dengan rincian tugas a–k. Laboran/PLP, teknisi, dan asisten tidak disebut; tenaga fungsional hanya muncul sebagai "Kelompok Jabatan Fungsional" umum. Jadi **syarat kompetensi per jabatan lab tidak tertulis** di dokumen resmi mana pun | D8b, Lampiran I dan II (butir 10 dan 12) | PKG-04 S3 dan PKG-14 K1: syarat kompetensi harus ditetapkan KaLab (batasan masalah 6 di brief) | Fakta dokumen |
| A18 | Laporan pelaksanaan (D3) dan alokasi (D2) **tidak punya kunci bersama** untuk asisten (tidak ada ID; NIM tidak ada di D2 per kelas). Dicocokkan lewat kode MK + kelas + nama: nama pelapor **cocok** dengan asisten teralokasi pada 271/286 laporan (2025/2026 Ganjil), 403/466 (2025/2026 Genap), dan 62/83 (2026/2027 Ganjil); sisanya **berbeda** (9, 47, 20). Sebagian selisih kemungkinan hanya beda ejaan nama | D2 × D3 (hitung penuh) | PKG-04 S2: tidak bisa dibuktikan bahwa petugas yang bertugas = petugas yang ditugaskan. TO-BE: penugasan dan pelaksanaan merujuk **Personel yang sama** (satu ID) | Fakta data. Pemisahan "beda ejaan" vs "beda orang" **[VALIDASI]** |
| A19 | Ada laporan pelaksanaan dari asisten di kelas yang **tidak punya alokasi**: 5 laporan (2025/2026 Ganjil) dan 16 laporan (2025/2026 Genap) | D2 × D3 (hitung penuh) | PKG-04 S2: ada asisten bertugas tanpa penugasan tercatat (mungkin pengganti informal atau alokasi tidak diperbarui) | Fakta data. Penyebabnya **[KONFIRMASI K9]** |
| A20 | Pembinaan dan pengembangan personel lab tersebar di beberapa jabatan: KaLab bertugas "melakukan pembinaan kepada anggota laboratorium" (butir 10 huruf f); **Wakil Dekan Bidang Keuangan dan Umum** bertugas "pembinaan karier dan kesejahteraan … Tenaga Kependidikan" dan "pemantauan dan evaluasi kinerja … Tenaga Kependidikan" (butir 5 huruf b dan f); Kepala Bagian Umum mengurus kepegawaian (butir 11 huruf e) | D8b, Lampiran II | PKG-14: "Dekanat SDM" di instrumen kemungkinan adalah Wadek Bidang Keuangan dan Umum, jadi pengesah Rencana Pelatihan = KaLab dan/atau Wadek II. Tetap **bukan aktor sistem** (keputusan kelompok) | Fakta dokumen. Siapa pengesah rencana pelatihan **[KONFIRMASI K10]** |
| A21 | Slide PKKMB menyebut alat/akses khusus per ruang: **3D printer** dan **VR** (ruang 301), **peralatan robotika** (302), **switch** (304); serta form layanan **"pinjam 3D printer"** dan **"install software"** | D8a, slide ruang dan slide "Links" | PKG-10: kandidat isi master Tugas/Alat Berkewenangan Khusus. Ada form permintaan untuk dua layanan, tetapi tidak ada bukti izin **per personel** | Fakta dokumen. Alat mana yang wajib izin **[KONFIRMASI KaLab, pertanyaan wawancara no. 16]** |

### Cara hitung D2 dan D3

Supaya angka A6–A8, A11–A12, A18–A19 bisa diulang:
1. Kedua spreadsheet diekspor ke xlsx lewat Google Drive (14 November 2026).
2. **Kelas** = baris tab alokasi yang kolom "Kelas"-nya terisi. **Kelas tanpa asisten** = semua 14 kolom pertemuan (1–7, 9–15) kosong. **Pertemuan pertama** = kolom pertemuan terkiri yang terisi.
3. **Laporan** = baris tab `Form Responses 1` yang *timestamp*-nya terisi, dikelompokkan menurut kolom "Periode" (`2526 Ganjil` ↔ `Sheet7`, `2526 Genap` ↔ `ALOKASI_ASISTEN_PER_MINGGU_2526`, `2026/2027 Ganjil` ↔ `ALOKASI_ASISTEN_PER_MINGGU_2627`). 2024/2025 Genap tidak punya tab alokasi.
4. **Pencocokan** = kode MK (pola tiga huruf + enam angka di nama MK) + kelas, lalu nama pelapor dibandingkan (huruf kecil) dengan nama di sel pertemuan kelas itu.
5. Skrip hanya mencetak jumlah; nama dan NIM tidak dicetak maupun disimpan di repo.

**Rumusan as-is ringkas:** penugasan asisten LabFIK sudah punya prosedur (POB 2025, belum disahkan) dan dicatat rutin di *spreadsheet* per kelas per pertemuan, tetapi rekaman itu tidak menyatakan **kebutuhan** petugas (42–56% kelas tanpa asisten tanpa keterangan), tidak menghubungkan asisten dengan **hasil seleksinya**, tidak bisa dicocokkan dengan laporan pelaksanaan karena tidak ada kunci bersama, dan tidak mencatat **laboran/PLP** sama sekali. Rekaman kompetensi personel hanya berupa sertifikat lepas tanpa rencana dan evaluasi pelatihan. Pemegang sertifikat itu laboran yang memegang satu ruang, sementara laboran lain memegang tiga ruang. Rekaman otorisasi tugas/alat tidak ditemukan, padahal lab punya alat khusus (3D printer, VR, robotika, switch) dan form permintaan untuk sebagian layanannya.

---

## 4. Bedah per dokumen

Kolom tabel:
- **Bagian:** bagian dokumen sumber.
- **Field (usulan):** nama field di sistem.
- **Model:** model Odoo tujuan (nama sementara).
- **Dasar:** `Instr` = kriteria/bukti Instrumen Monev, `ISO` = ISO/IEC 17025, `Analisis` = keputusan di dokumen analisis, `Format` = hanya untuk tampilan atau ekspor.

### 4.1 D1: POB Manajemen Praktikum dan Asistensi 2025

**Kepala dokumen POB**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Nomor dokumen, tanggal pembuatan/revisi/efektif, jadwal reviu, pengesahan Dekan | **Tidak diambil.** POB adalah dokumen terkendali milik Tata Kelola (PKG-02) | `labfik.document` (Tata Kelola) | ISO 8.3 |
| Kualifikasi pelaksana (KaLab, laboran, teknisi, dosen, asisten, praktikan) | Isi awal (*seed*) **Jabatan**: nama jabatan dan uraian tugas singkat | `hr.job` (Core) | Instr PKG-04 (peran petugas) |

**Langkah dan formulir yang relevan dengan PKG-04**

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Langkah 1 + Formulir Alokasi Praktikum dengan Asisten (periode, prodi, kode MK, nama MK, jumlah kelas; diajukan Koor Prodi, ditinjau KaLab, disetujui Wadek) | Kelas yang butuh asisten → **Kebutuhan Petugas**: `kelas_id`, `peran` (asisten/laboran), `jumlah_minimal`, `dasar_penetapan` (teks), `penetap_id`, `tanggal_penetapan`. Berkas formulir alokasi bertanda tangan sebagai lampiran | `labfik.sdm.kebutuhan.petugas` | Instr PKG-04 S1 (kebutuhan ditetapkan menurut beban kerja) |
| Langkah 2: pengumuman rekrutmen (nama MK, jumlah asisten dibutuhkan) | **Tidak diambil.** Rekrutmen di luar cakupan (batasan 7) | — | — |
| Langkah 3 + Formulir Pendaftaran (identitas, pembimbing akademik, pemberi rekomendasi, lampiran KHS, daftar MK dipilih: kode, nama, **nilai**, hasil periksa, kesesuaian) | Pendaftaran tidak dibangun. Yang diambil hanya isi per MK ke **Seleksi Kompetensi**: `personel_id`, `mata_kuliah_id`, `periode_id`, `nilai_mk`, `memenuhi_syarat_nilai` (dihitung dari ambang), berkas KHS (akses terbatas) | `labfik.sdm.seleksi` | Instr PKG-04 S4 dan bukti 6 |
| Langkah 4 + Berita Acara Penilaian (tanggal, tempat, penilai, NIP, jabatan, waktu; per calon: nilai wawancara, simulasi pengajaran, pengembangan modul, catatan; disetujui oleh) | `tanggal_seleksi`, `penilai_id`, `skor_wawancara`, `skor_simulasi`, `skor_modul`, `catatan`, `keputusan` (lulus/tidak lulus/lulus dengan pengecualian), `alasan_pengecualian`, `penyetuju_pengecualian_id`, berkas berita acara | `labfik.sdm.seleksi` | Instr PKG-04 S4 dan bukti 5 (uji keterampilan); Analisis PKG-04 (pengecualian + penyetuju) |
| Langkah 5: kontrak asisten dengan Fakultas (Surat Kontrak) | Berkas kontrak sebagai lampiran **Penugasan** (lapis Pelengkap: komitmen) | `labfik.sdm.penugasan` | Instr PKG-04 S2 (penugasan sah) bila kontrak = dasar penugasan **[KONFIRMASI]** |
| Langkah 6 + Formulir Alokasi Asisten; Daftar Nama Asisten (NIM, kode, nama, HP) | **Penugasan Petugas** per kelas: `personel_id`, `kelas_id`, `peran`, `berlaku_mulai`, `berlaku_sampai`, status pengesahan, berkas surat tugas | `labfik.sdm.penugasan` | Instr PKG-04 S2 dan bukti 1–2. Rentang berlaku dari temuan A6 |
| Monitoring Alokasi dan Pelaksanaan Asisten (per kode MK dan kelas: kolom A dan L per pertemuan 1–15, ΣA, ΣL; laboran dan paraf) | **Tidak diambil sebagai form.** Hasil yang setara = Daftar Sesi dan Petugas `[R]`. Arti kolom A/L tidak dijelaskan (dugaan: alokasi vs laksana) **[VALIDASI]** | `[R]` | Instr PKG-04 bukti 1 |
| Langkah 9–11, Lembar Pelaksanaan, Kuesioner | **Tidak diambil.** Milik PKG-18/PKG-20 (Praktikum) | — | — |
| Pencatatan no. 4: Evaluasi Kinerja Asisten (formulir tidak ada) | **Tidak diambil.** Bukan syarat PKG-04 (temuan A15) | — | — |

### 4.2 D2: Spreadsheet Alokasi Pertemuan Asisten

Satu file berisi beberapa sheet per periode: `ALOKASI_ASISTEN_PER_MINGGU_<periode>`, `LOV Nama Asisten <periode>`, dan beberapa pivot rekap.

| Bagian (kolom) | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Periode, Program Studi, Semester, Kode MK, Nama MK, Kelas, Hari, Jam Mulai, Jam Selesai | **Tidak diambil oleh modul ini.** Master Periode, Mata Kuliah, Kelas, dan jadwal Sesi ada di Core/PKG-15 (kolom hari dan jam di sheet kosong) | Core | Analisis PKG-04 (dependensi) |
| Dosen Koordinator, Dosen Kelas, Dosen Tandem | **Tidak diambil.** Dosen bukan petugas yang dinilai di PKG-04 | — | Instr PKG-04 (hanya laboran/PLP dan asisten) |
| Pertemuan 1–15 (satu nama asisten per sel) | **Penugasan Petugas** per kelas dengan `berlaku_mulai`/`berlaku_sampai`. Pengganti untuk satu pertemuan = penugasan per sesi (Pelengkap) | `labfik.sdm.penugasan` | Instr PKG-04 S2; temuan A6 |
| Jumlah Alokasi Per Kelas, CEK IF 9=7 | Tidak disimpan. Diganti status kebutuhan terpenuhi yang dihitung | `[R]` (hidden) | Instr PKG-04 S1–S2 |
| LOV Nama Asisten (NIM, nama, prodi, HP, email) | Asisten sebagai **Personel**. Nomor HP dan email tidak diperlukan untuk bukti, jadi tidak disimpan modul ini | `hr.employee` (Core) | Analisis PKG-04; bagian 8 |
| (Tidak ada kolom) kebutuhan asisten per kelas | **Kebutuhan Petugas** baru, termasuk nilai 0 untuk kelas yang memang tidak butuh asisten | `labfik.sdm.kebutuhan.petugas` | Instr PKG-04 S1; temuan A7 |
| (Tidak ada kolom) laboran per kelas/ruang | **Penugasan Petugas** untuk laboran; sasarannya ruang atau kelas **[KONFIRMASI]** | `labfik.sdm.penugasan` | Instr PKG-04 (laboran/PLP wajib); temuan A9–A10 |

### 4.3 D3: Jawaban Google Form Pelaksanaan Asistensi

| Bagian (kolom) | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Periode, MK, kelas, tanggal, hari, waktu mulai/akhir, ruang, pertemuan ke | **Tidak diambil oleh modul ini.** Atribut Sesi (Core, PKG-15/18) | Core | — |
| Nama asisten, NIM asisten (pelapor sesi) | Dibaca sebagai **petugas yang hadir** untuk dibandingkan dengan Penugasan (opsional, PKG-18 → 04) | Milik PKG-18 | Analisis PKG-04 (penyebut dan kehadiran) |
| Jumlah kehadiran mahasiswa, dosen hadir, topik, kesiapan sarana, kendala, modul, foto, status | **Tidak diambil.** Milik PKG-16/17/18 (Praktikum) | — | — |

D3 tidak menambah field baru untuk modul SDM. Nilainya bagi PKG-04 ada di temuan A11–A12: sesi yang **terlaksana** (penyebut) memang perlu data pelaksanaan dari modul Praktikum.

### 4.4 D4: Sertifikat personel

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| Jenis dokumen (sertifikat kompetensi BNSP / sertifikat pelatihan) | `jenis_bukti` (pendidikan / pelatihan / sertifikasi / pengalaman / demonstrasi) | `labfik.sdm.bukti.kompetensi` | Instr PKG-04 S3 (pendidikan, pelatihan, pengalaman, demonstrasi) |
| Nomor sertifikat, nomor registrasi, ID verifikasi | `nomor_dokumen` | `labfik.sdm.bukti.kompetensi` | Instr PKG-04 bukti 4 (dapat diverifikasi) |
| Lembaga penerbit (LSP, lembaga pelatihan) | `penerbit` (teks) | `labfik.sdm.bukti.kompetensi` | Format (penilai memeriksa keaslian) |
| Bidang / skema / kualifikasi (mis. "Data Analyst") | `kompetensi_id` (Many2one ke master Kompetensi) | `labfik.sdm.bukti.kompetensi` | Instr PKG-04 S3, PKG-14 K1 |
| Daftar unit kompetensi berkode SKKNI | **Tidak diambil sebagai tabel.** Cukup di berkas. Kode skema boleh dicatat di master Kompetensi (`kode_acuan`, opsional) | `labfik.sdm.kompetensi` | Format |
| Masa berlaku ("3 tahun") | `berlaku_sampai`; status berlaku dihitung dari tanggal | `labfik.sdm.bukti.kompetensi` | Instr PKG-04 S3 (terverifikasi); ISO 6.2.5 f |
| Tanggal terbit / tanggal pelaksanaan | `tanggal` (dari `labfik.evidence.mixin`) | mixin | Instr PKG-14 K3 |
| Jumlah jam pelajaran (24 JP) | `durasi_jam` | `labfik.sdm.realisasi.pelatihan` | Format (pelengkap rekap pelatihan) |
| Berkas PDF sertifikat | `berkas` (dari `labfik.evidence.mixin`) | mixin | Instr PKG-14 bukti 3 |
| Pemilik sertifikat | `personel_id` | `labfik.sdm.bukti.kompetensi` | Instr PKG-14 (PLP/laboran) |

**Satu sertifikat bisa berperan ganda:** sertifikat pelatihan adalah bukti **Realisasi Pelatihan** (PKG-14 K3), dan setelah evaluasi efektif menjadi **Bukti Kompetensi** (PKG-04 S3, PKG-10 S1). Sertifikat kompetensi BNSP langsung menjadi Bukti Kompetensi. Berkasnya cukup diunggah sekali **[USULAN PENULIS]**.

### 4.5 D6: Paket Manajemen Praktikum 2026 (draf, pembanding)

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| STD-PRK-03 tahapan seleksi (administrasi, *subject competency test*, simulasi, pengoperasian sarana, wawancara) dan bobot 35/25/20/10/10 | Skor per komponen **tidak** dijadikan field terpisah. Cukup skor total + keputusan + berkas rubrik (D1 sudah punya tiga nilai) | `labfik.sdm.seleksi` | Instr PKG-04 bukti 5 hanya meminta hasil uji. Bobot rinci = ditunda (brief) |
| STD-PRK-03 kriteria lulus (total ≥75, *subject* ≥70, nilai MK ≥B) | Ambang nilai MK = **pengaturan KaLab**, bukan konstanta | Pengaturan | Instr PKG-04 bukti 6 (usulan ≥70); besaran **[KONFIRMASI]** |
| STD-PRK-03 "kualifikasi bersifat *course-specific* dan *semester-specific*" | Seleksi per MK per periode | `labfik.sdm.seleksi` | Analisis PKG-04 (keputusan 14 Nov 2026). Draf hanya mendukung |
| FRM-PRK-02 keputusan QUALIFIED / QUALIFIED WITH CONDITION / NOT QUALIFIED | Pilihan `keputusan` (lulus / lulus dengan pengecualian / tidak lulus) | `labfik.sdm.seleksi` | Analisis PKG-04 (pengecualian tercatat) |
| FRM-PRK-09 pernyataan komitmen (identitas, MK diampu, 8 butir pernyataan, tanda tangan asisten, dosen koordinator, KaLab) | Berkas komitmen di Penugasan (lapis Pelengkap). Butir pernyataan tidak dijadikan field | `labfik.sdm.penugasan` | Instr PKG-04 sheet ("Komitmen Petugas Praktikum") |
| REG-PRK-01 sheet `Assistant_Qualification` (nilai MK, 5 skor, skor akhir, lulus?, status, evaluator, tanggal) | Sama dengan baris Berita Acara di 4.1 | `labfik.sdm.seleksi` | Instr PKG-04 S4 |
| REG-PRK-01 sheet `Class_Master` (*complexity*, *equipment risk*, *base need*, *recommended/assigned assistants*, *coverage %*) | Hanya `jumlah_minimal` dan `dasar_penetapan` (teks) di Kebutuhan Petugas. Skor kompleksitas/risiko tidak diambil | `labfik.sdm.kebutuhan.petugas` | Instr PKG-04 S1 ("menurut risiko/beban kerja"); perhitungan risiko = ditunda |
| REG-PRK-01 sheet `Assistant_Allocation` (*start date*, *end date*, *conflict/exception*) | `berlaku_mulai`, `berlaku_sampai` | `labfik.sdm.penugasan` | Didukung temuan A6 (data nyata) |
| REG-PRK-01 `Session_Log`, `Assistant_Session_Log`, `Honor_Recap`, `Midterm_Control`, `Workstation_Register`, `Incidents`, `Module_Register` | **Tidak diambil.** Milik Praktikum/Aset atau di luar cakupan (honor) | — | — |

### 4.6 D7: Paket Dokumen Monev (draf GPT, pembanding)

| Bagian | Field (usulan) | Model | Dasar |
|---|---|---|---|
| SOP 07 "Persyaratan Kompetensi per Fungsi" (FN01–FN05: fungsi, kemampuan, bukti yang ditinjau) | Bentuknya = syarat kompetensi per jabatan. Isi FN01–FN05 **tidak** dipakai sebagai *seed* (simulasi) | `hr.job` + `labfik.sdm.kompetensi` | ISO 6.2.2 (persyaratan kompetensi per fungsi terdokumentasi) |
| FRM-ASM-001 Asesmen Keterampilan (calon dan fungsi, penilai, persyaratan, unjuk kerja, nilai, **unsur kritis**, simpulan, pengembangan) | `penilai_id`, `metode`, `skor`, `unsur_kritis_terpenuhi`, `kesimpulan`, `catatan_pengembangan`, berkas | `labfik.sdm.asesmen` | Instr PKG-10 bukti 2; Analisis PKG-10 |
| FRM-OTR-001 Otorisasi (nomor, personel dan asesmen, lingkup, alat/sistem, pembatasan, supervisi, masa berlaku, pengesah, pembekuan) | `lingkup`, `pembatasan`, `level`, `supervisor_id`, `berlaku_mulai`/`berlaku_sampai` (mixin periode), status (mixin pengesahan) | `labfik.sdm.otorisasi` | Instr PKG-10 S2–S3; ISO 6.2.6 |
| FRM-TGS-001 Penugasan Sesi Pengganti (petugas utama, pengganti, supervisor, verifikasi) | Penugasan per sesi untuk pengganti (Pelengkap). Kolom verifikasi dan aktual pelaksanaan tidak diambil | `labfik.sdm.penugasan` | Analisis PKG-04 (pengganti = Pelengkap) |
| FRM-DIK-001 Rencana Pelatihan dan Evaluasi Penerapan (personel dan kebutuhan, program, kriteria, rencana, pelaksanaan, demonstrasi, penerapan, efektivitas, usulan review otorisasi) | Sudah tercakup di Rencana (kebutuhan, item), Realisasi (demonstrasi), Evaluasi (efektivitas). "Usulan review otorisasi" tidak diambil | `labfik.sdm.rencana.pelatihan`, `.realisasi.pelatihan`, `.evaluasi.pelatihan` | Instr PKG-14 K1–K4 |

D7 tidak menambah field yang belum ada di analisis. Gunanya hanya mengonfirmasi bentuk formulir.

---

## 5. Pola berulang → inheritance

| Pola | Muncul di dokumen | Model yang memakainya | Mekanisme |
|---|---|---|---|
| **Keputusan bertanda tangan** (diajukan/ditinjau/disetujui) | Formulir Alokasi D1, Berita Acara D1, FRM-PRK-09 D6, FRM-OTR-001 D7 | Penugasan Petugas, Otorisasi, Rencana Pelatihan | `labfik.approval.mixin` (Core) |
| **Bukti berkas** (tanggal, pemilik, berkas, nomor) | Sertifikat D4, KHS D1, berita acara D1 | Bukti Kompetensi, Realisasi Pelatihan | `labfik.evidence.mixin` (Core) |
| **Masa berlaku** | Sertifikat BNSP 3 tahun (D4); masa berlaku otorisasi (D7) | Otorisasi (dengan kedaluwarsa); Bukti Kompetensi (status berlaku dihitung) | `labfik.period.mixin` (Core) untuk Otorisasi |
| **Rentang berlaku per periode** | Penugasan mulai pertemuan 3/5 (D2), *start/end date* (D6) | Penugasan Petugas | Field tanggal biasa |
| **Kriteria berurutan** | Tidak ada di dokumen; dari instrumen | Rencana Pelatihan (PKG-14) | `labfik.criteria.mixin` (Core) |

---

## 6. Daftar model TO-BE (konsolidasi)

Nama teknis sementara; ditetapkan di Langkah 10.

| Model | Label | Isi utama | Sumber dokumen | Jenis kebutuhan (§4.7.2) |
|---|---|---|---|---|
| `labfik.sdm.kompetensi` | [M] Kompetensi | nama, jenis, kode acuan (opsional, mis. skema SKKNI), aktif | D4, D7 | Evident |
| `hr.job` (diperluas `labfik_sdm`) | [M] Jabatan + syarat kompetensi | `syarat_kompetensi_ids` | D1 (kualifikasi pelaksana), D7 (bentuk) | Evident |
| `labfik.sdm.bukti.kompetensi` | [T] Bukti Kompetensi | personel, kompetensi, jenis bukti, nomor, penerbit, berlaku sampai; *mixin* bukti | D4 | Evident; status berlaku = hidden |
| `labfik.sdm.kebutuhan.petugas` | [T] Kebutuhan Petugas | kelas, peran, jumlah minimal, dasar, penetap | D1 (formulir alokasi), D2 (celah A7) | Evident |
| `labfik.sdm.seleksi` | [T] Seleksi Kompetensi | calon, MK, periode, nilai MK, skor, penilai, keputusan, pengecualian + penyetuju, berkas | D1 (pendaftaran, berita acara), D6 | Evident; "memenuhi syarat nilai" = hidden |
| `labfik.sdm.penugasan` | [T] Penugasan Petugas | personel, kelas (atau ruang untuk laboran **[KONFIRMASI]**), peran, berlaku mulai/sampai, surat tugas; *mixin* pengesahan | D1, D2, D6 | Evident |
| `labfik.sdm.tugas.khusus` | [M] Tugas/Alat Berkewenangan Khusus | nama, jenis, kompetensi disyaratkan, masa berlaku standar, cara pembatasan | Tidak ada dokumen nyata (A16) | Evident |
| `labfik.sdm.asesmen` | [T] Asesmen Keterampilan | personel, tugas/alat, penilai, metode, skor, unsur kritis, kesimpulan | D7 (bentuk saja) | Evident |
| `labfik.sdm.otorisasi` | [T] Otorisasi Personel | personel, tugas/alat, lingkup, level, supervisor; *mixin* pengesahan + periode | D7 (bentuk saja) | Evident; kedaluwarsa = hidden |
| `labfik.sdm.evaluasi.otorisasi` | [T] Evaluasi Ulang Otorisasi | otorisasi, pemicu, keputusan | D7 (bentuk saja) | Evident |
| `labfik.sdm.rencana.pelatihan` (+ anak kebutuhan dan item) | [T] Rencana Pelatihan | periode, kebutuhan (dibekukan), item; *mixin* pengesahan + kriteria | D7 (bentuk saja), A13 (celah) | Evident; status K1–K4 = hidden |
| `labfik.sdm.realisasi.pelatihan` | [T] Realisasi Pelatihan | item, peserta, tanggal, durasi jam, sertifikat, bukti penerapan; *mixin* bukti | D4 | Evident |
| `labfik.sdm.evaluasi.pelatihan` | [T] Evaluasi Efektivitas | realisasi, metode, skor sebelum/sesudah, kesimpulan, tindak lanjut | D7 (bentuk saja) | Evident; pembuatan Bukti Kompetensi = hidden |

**Dibanding analisis:** tidak ada model baru. Ada **dua penambahan field** yang lahir dari dokumen nyata: `berlaku_mulai`/`berlaku_sampai` di Penugasan (A6) dan `durasi_jam` di Realisasi Pelatihan (D4). Ada **satu pertanyaan struktur**: sasaran penugasan laboran adalah ruang atau kelas (A10).

## 7. Laporan [R] dan nilai terhitung

| Laporan / nilai | Menggantikan (dokumen as-is) | Dasar | Jenis (§4.7.2) |
|---|---|---|---|
| Daftar Sesi dan Petugas (status S1–S4 per sesi) | Monitoring Alokasi dan Pelaksanaan (D1), pivot rekap (D2) | Instr PKG-04 bukti 1 | Hidden (dihitung) |
| Surat Tugas | Daftar Nama Asisten (D1), surat kontrak (D1) | Instr PKG-04 bukti 2 | Evident (diterbitkan) |
| Matriks Kompetensi | Tidak ada | Instr PKG-04 bukti 3 | Hidden |
| Daftar Operator Sah | Tidak ada | Instr PKG-10 bukti 3 | Hidden |
| Analisis Kebutuhan Kompetensi, Rekap Pelatihan | Tidak ada (A13) | Instr PKG-14 bukti 1 | Hidden |
| Persentase PKG-04/10, kriteria tertinggi PKG-14 | Status "Terverifikasi 100%" di iso.upnvj (A14) | Instr | Hidden |

## 8. Data pribadi (batasan nonfungsional)

Batasan ini menempel pada fungsi tertentu, jadi termasuk kebutuhan **nonfungsional** (§4.7.3). Kandidat KF/NF di Langkah 4:

| Data di dokumen nyata | Muncul di | Di TO-BE |
|---|---|---|
| NIM, nama asisten | D2, D3 | Disimpan di Personel (Core). Data uji fiktif |
| Nomor HP, email pribadi | D2 (LOV), D1 (daftar asisten) | **Tidak disimpan** modul SDM (tidak dibutuhkan sebagai bukti) |
| Nilai MK / KHS | D1 (pendaftaran) | Hanya nilai MK yang dipersyaratkan; berkas KHS berakses terbatas (KaLab, laboran) |
| NIP penilai | D1 (berita acara) | Lewat Personel (Core), tidak diketik ulang |
| Foto pelaksanaan | D3 | Tidak dicakup (milik PKG-18) |

## 9. Perbandingan dengan contoh Tata Kelola

Dibandingkan dengan [bedah-dokumen-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/analisis/bedah-dokumen-tata-kelola.md) (branch `febriyan-skripsi`):

| Aspek | Tata Kelola | SDM (dokumen ini) |
|---|---|---|
| Struktur | Tujuan, aturan baca, dokumen, temuan as-is, bedah per dokumen, pola → inheritance, daftar model, laporan | Sama, ditambah **aturan Wazlawick dengan nomor §**, **peran dan peluang otomasi** (§2.6), **kolom evident/hidden** (§4.7.2), dan bagian **data pribadi** (§4.7.3) |
| Jenis sumber | Dokumen (Renstra, POB, SK, IK); sebagian besar draf GPT | Lebih banyak **data operasional nyata** (D2, D3) dan bukti nyata (D4). Draf hanya pembanding |
| Hasil utama | Banyak field naratif untuk ekspor dokumen (Renstra, RKT) | Hampir tidak ada field naratif. Hasilnya **rekaman per orang/kelas** dan laporan terhitung |
| Data pribadi | Nama pejabat di SK dan slide | Jauh lebih banyak (NIM, HP, email, nilai) → bagian 8 |
| Celah | Dokumen tidak terkendali | Rekaman tidak terhubung (seleksi ↔ penugasan), laboran tidak tercatat, PKG-10 tanpa dokumen |
| Model dari dokumen | Banyak (rencana, item, KPI, dokumen induk, versi) | Tidak ada model baru di luar analisis; hanya dua field tambahan |

---

## 10. Cek silang, isu terbuka, dan koreksi

### 10.1 Cek silang ke langkah sebelumnya

| Cek | Hasil |
|---|---|
| Setiap kriteria instrumen punya rekaman bukti | PKG-04 S1–S4 ✓ (S1 dari celah A7, S2–S4 dari D1/D2). PKG-10 S1–S4 ✓ dari instrumen dan D7 (bentuk saja), **tanpa dokumen nyata**. PKG-14 K1–K4 ✓; dokumen nyata hanya mendukung K3 (D4) |
| Field dari draf GPT/draf punya dasar | Semua baris D6 dan D7 yang diambil punya dasar `Instr` atau `Analisis`. Bobot rubrik, skor kompleksitas/risiko kelas, dan butir komitmen **tidak** diambil |
| Model konsisten dengan analisis dan brief | Ya, nama dan jumlah transaksi sama. Tambahan: 2 field (A6, D4) |
| Cakupan brief tidak dilanggar | Ya. Pendaftaran, honor, alokasi otomatis, bobot rubrik, dan log sesi tetap tidak diambil |
| Keputusan pengguna (14 Nov 2026) didukung dokumen | Penugasan per kelas ✓ (A5, A6). Seleksi dipisah dari asesmen ✓ (D1 vs D7 berbeda bentuk dan pelaku). PKG-14 per tahun: tidak ada dokumen yang menentang |

### 10.2 [KONFIRMASI] yang muncul atau menguat di langkah ini

| No | Pertanyaan | Ke siapa | Menentukan |
|---|---|---|---|
| K1 | Minta salinan **Lembar Seleksi Asisten** dan **Surat Kontrak Asisten** | KaLab | S2, S4 PKG-04 |
| K2 | Besaran syarat nilai MK asisten (A? B? 70?) dan cara pengecualian dicatat | KaLab / Koor Prodi | Pengaturan ambang; pendahuluan A5 |
| K3 | Laboran ditugaskan **per ruang** atau per kelas? | KaLab | Struktur Penugasan Petugas |
| K4 | Apakah teknisi termasuk laboran (PKG-10)? D8a mencantumkan "Teknisi Jaringan" sebagai jabatan terpisah dari 4 laboran | KaLab | Cakupan PKG-10 |
| K5 | ~~Jabatan pemilik dua sertifikat~~ **Terjawab oleh D8a**: laboran ruang 201. Sisa pertanyaan: apakah kedua sertifikat itu relevan dengan gap tugasnya? | KaLab | K2 PKG-14 |
| K6 | Arti kolom A/L di formulir Monitoring Alokasi (D1) dan rumus sel "630 vs 1.008" (D2) | Laboran | Kejelasan angka ringkas (A8) |
| K7 | Apakah kontrak asisten = dasar sahnya penugasan, atau perlu surat tugas terpisah? | KaLab | S2 PKG-04 |
| K8 | Kenapa pada 2026/2027 Ganjil asisten baru mulai di pertemuan 5? (seleksi terlambat? pertemuan awal tanpa praktikum?) | KaLab / laboran | Apakah pertemuan sebelum mulai dihitung sebagai sesi "tanpa petugas" di PKG-04 |
| K9 | Siapa yang menunjuk asisten yang melapor di kelas tanpa alokasi (A19) atau berbeda dari alokasi (A18)? | Laboran | Alur pengganti (Pelengkap) |
| K10 | Siapa yang menyetujui rencana pelatihan PLP/laboran: KaLab, Wadek Bidang Keuangan dan Umum, atau keduanya? (A20) | KaLab | Pengesah Rencana Pelatihan (PKG-14 K1) |

### 10.3 Dokumen lain yang perlu ikut berubah

**Status (14 November 2026):** perubahan untuk analisis PKG-04, PKG-14, dan brief **sudah diterapkan**. Draf pendahuluan (Google Docs) belum.

| Dokumen | Perubahan |
|---|---|
| [analisis-data-pengelolaan-4.md](analisis-data-pengelolaan-4.md) bagian 0 | Tambah D1–D4 sebagai sumber nyata; tandai paket 2026 sebagai pembanding |
| [analisis-data-pengelolaan-4.md](analisis-data-pengelolaan-4.md) bagian 4 | Penugasan Petugas: tambah `berlaku_mulai`/`berlaku_sampai` (A6); catat opsi sasaran **ruang** untuk laboran (A10, K3) |
| [analisis-data-pengembangan-14.md](analisis-data-pengembangan-14.md) bagian 0 dan 4 | "Dokumen nyata tidak ditemukan" → ada D4 (dua sertifikat). Tambah `durasi_jam` di Realisasi |
| [brief-sdm.md](../brief/brief-sdm.md) tabel as-is | Rujuk A1–A19 di sini; A5 brief (nilai A) tetap [KONFIRMASI] karena POB tidak menyebut besarannya (A4); A3 brief (42–56%) **terkonfirmasi** (A7) dan status [VALIDASI]-nya bisa dicabut, dengan rujukan ke cara hitung |
| Draf pendahuluan (Google Docs) | Kalimat "seleksi mensyaratkan nilai A" belum punya sumber dokumen (A4). Angka 42–56% boleh dipertahankan; rinci per periode (A7). Tambah fakta laboran tidak tercatat (A9), petugas yang melapor tidak selalu sama dengan yang dialokasikan (A18), dan bukti PKG-14 hanya sertifikat lepas (A13) |
| [pemetaan-package-instrumen.md](pemetaan-package-instrumen.md) (file bersama) | Tidak perlu diubah di langkah ini |

### 10.4 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| [analisis-data-pengembangan-14.md](analisis-data-pengembangan-14.md) bagian 0 | Ditulis "Dokumen nyata tentang pelatihan PLP: **tidak ditemukan**". Folder baris 10 `ISO_LAB_SI` ternyata berisi dua sertifikat nyata. Waktu itu pencarian tidak membuka tautan di `ISO_LAB_SI` | Perbarui sesuai 10.3 |
| [analisis-data-pengelolaan-4.md](analisis-data-pengelolaan-4.md) bagian 4 | Penugasan per kelas ditulis tanpa rentang berlaku, seolah asisten selalu bertugas sejak pertemuan 1 | Tambah rentang berlaku (A6) |
| Analisis PKG-04 dan brief | Penugasan laboran diasumsikan sama dengan asisten (per kelas), padahal satu-satunya sumber (slide PKKMB) menyebut laboran per ruang | Jadikan K3 sebelum Langkah 4 |
| Versi pertama dokumen ini (A10, A17) | Slide PKKMB dan SK SOTK hanya dikutip lewat ringkasan Febriyan, tidak dibuka langsung | Dibaca langsung (D8a, D8b). Ringkasan Febriyan terkonfirmasi, ditambah rincian ruang per laboran, tugas pembinaan (A20), dan alat khusus (A21) |
| [brief-sdm.md](../brief/brief-sdm.md) A3 | Angka "42–56% kelas tanpa alokasi" dikutip dari pendahuluan tanpa cara hitung | Sudah dihitung ulang (A7: 41,8–56,3%); cara hitung tercatat di bagian 3 |
| Versi pertama dokumen ini (A6–A8, A11–A12) | Ditulis dari **sampel baris** yang ditampilkan alat baca Drive, bukan seluruh data; A6 sempat menyimpulkan "mulai pertemuan 3 atau 5" dari beberapa baris saja | Diganti dengan hitungan penuh dari ekspor xlsx (bagian [cara hitung](#cara-hitung-d2-dan-d3)) |
| Analisis PKG-04 bagian 0 | D1 disebut "belum bernomor dan belum disahkan" tanpa mengecek apakah ada versi bertanda tangan | Tetap, tetapi ditandai [VALIDASI] (A2) |

## 11. Langkah berikutnya

1. Perbarui dokumen di 10.3 setelah disetujui.
2. Ajukan K1–K7 bersama pertanyaan wawancara yang sudah ada.
3. Langkah 3: sepakati kontrak Core (Sesi/Kelas, asisten sebagai Personel, syarat kompetensi di `hr.job`) dengan Febriyan dan Herrens.
4. Langkah 4: kebutuhan `KF-SDM-nn`.
