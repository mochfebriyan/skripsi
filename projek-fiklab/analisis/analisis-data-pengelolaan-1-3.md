# Analisis Data Indikator Pengelolaan 1, 2, 3 (MVP)

26 Oktober 2026 (disunting 1 November 2026) · Febriyan · Bagian dari proyek LabFIK Compliance · Modul: Tata Kelola & Dokumen (di sheet: Organization Management)

Package keempat di modul ini, Pengembangan 13, dianalisis di [analisis-data-pengembangan-13.md](analisis-data-pengembangan-13.md). Scope modul secara utuh ada di [brief-tata-kelola-dokumen.md](../brief/brief-tata-kelola-dokumen.md).

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md): **target → aturan memenuhi → luaran (bukti dukung) → data transaksi (*fact*) → master data (*dimension*) → dependensi**. Cakupannya sengaja dibatasi ke MVP. Hanya data yang bisa **dicatat oleh sistem sendiri** yang menjadi syarat wajib. Data yang bergantung pada pihak lain diberi jalan pengganti.

Kondisi saat ini: per 26 Oktober 2026, KaLab menyampaikan secara lisan bahwa FIKLAB **belum punya** SK pengelola, SOP yang disahkan, maupun rencana kerja. Pernyataan ini masih harus dicatat sebagai hasil wawancara (nama, jabatan, tanggal) sebelum dikutip **[KONFIRMASI]**.

---

## Ringkasan

| | Pengelolaan 1 | Pengelolaan 2 | Pengelolaan 3 |
|---|---|---|---|
| Inti | Rencana kerja tahunan (sasaran, KPI, target, anggaran, PIC) | SOP dan instruksi kerja tersedia, disahkan, mutakhir, dapat diakses | Struktur organisasi, tugas, wewenang, dan pengganti petugas |
| PJ | KaLab; Dekanat | KaLab; PLP/laboran | Dekan; KaLab |
| Jenis skor | Kriteria berurutan 1–4 | **Persentase** | Kriteria berurutan 1–4 |
| Unit | 1 paket dokumen dan rekaman | 1 SOP wajib | 1 paket dokumen dan rekaman |
| Level cakupan (usulan) | Semi-otomatis | **Otomatis** | Semi-otomatis |
| Fact baru | 4 | 3 | 3 |
| Master baru | 2 | 1 | 2 (salah satunya master bersama) |
| Posisi dalam dependensi | Hilir: butuh ID 3, bisa memakai *dashboard* | Tengah: butuh ID 3, dipakai indikator lain sebagai bukti SOP | **Hulu**: master personel dan jabatan dipakai ID 1, 2, 4, 10, 14, 18 |
| Acuan ISO/IEC 17025 | — | 8.3 (pengendalian dokumen) | 5.5–5.6 (struktur, tanggung jawab, wewenang) |

**Temuan utama:**
1. **Pengelolaan 3 adalah fondasi.** Master *personel* dan *jabatan* yang dibangun di sini dipakai hampir semua indikator lain di kelompok. Model ini harus disepakati paling awal, siapa pun PIC-nya nanti.
2. **Pengelolaan 1 dan 3 punya pola yang sama dengan Pengembangan 13 dan 14**: dokumen disahkan → isinya lengkap → dijalankan → dievaluasi dan diperbaiki. Pola ini bisa dibangun **satu kali** sebagai komponen generik ("paket dokumen dengan bukti per kriteria"), tidak perlu dibuat terpisah per indikator.
3. **Pengelolaan 2 punya pola yang sama dengan Pengelolaan 13** (dokumen dan rekaman mutu dikendalikan, belum ada PIC). Keduanya adalah pengendalian dokumen: versi, pengesahan, tinjau ulang, dan distribusi.

---

# Pengelolaan 1: Rencana Kerja Tahunan

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Laboratorium memiliki rencana kerja tahunan yang memuat sasaran, indikator kinerja, target, anggaran, dan penanggung jawab |
| Penerapan / PJ | Umum / KaLab; Dekanat |
| Unit | 1 paket dokumen dan rekaman |
| Skor | 4: kriteria 1–4 terpenuhi berurutan · 3: kriteria 1–3 · 2: hanya kriteria 1 atau 1–2 · 1: kriteria 1 belum terpenuhi atau bukti tidak dapat diverifikasi |

Bukti dukung: (1) *roadmap* lab, (2) rencana kerja tahunan disahkan, (3) matriks keterkaitan Renstra UPNVJ/UPPS/prodi, (4) KPI dengan definisi, sumber data, target, dan anggaran, (5) laporan pelaksanaan kegiatan kerja laboratorium.

## 2. Aturan "memenuhi" versi MVP

Kriteria diperiksa **berurutan**. Kriteria berikutnya tidak dihitung bila kriteria sebelumnya belum berbukti.

| Kriteria | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| K1 Disahkan | Rencana strategis (*roadmap*) dan rencana tahunan disahkan dan masih berlaku | Ada rencana berstatus *disahkan*, ada pengesah dan tanggal, periode mencakup hari ini | Keabsahan dokumen |
| K2 Lengkap dan selaras | Sasaran, KPI terukur, target, PIC, jadwal, dan anggaran lengkap, serta tertaut ke Renstra institusi | Setiap item rencana punya KPI, target, PIC, jadwal, anggaran, dan minimal satu tautan Renstra | Apakah KPI benar-benar terukur dan selaras |
| K3 Dijalankan | Kegiatan dijalankan, realisasi KPI dan anggaran dapat ditelusuri | Setiap item punya minimal satu realisasi beserta bukti | Kewajaran realisasi |
| K4 Ditinjau | Capaian ditinjau minimal tahunan, dan keputusan perbaikan masuk ke rencana berikutnya | Ada tinjauan pada periode ini, dan keputusannya tertaut ke item rencana periode berikutnya | Kualitas keputusan perbaikan |

Sistem menampilkan **sampai kriteria ke berapa buktinya lengkap**. Skor akhir ditetapkan penilai (semi-otomatis).

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Rencana strategis (*roadmap*) | 1 | Dokumen multi-tahun beserta status pengesahan |
| Rencana kerja tahunan | 2 | Header rencana + item rencana |
| Matriks keterkaitan Renstra | 3 | Dihasilkan dari tautan item rencana ke sasaran Renstra, tidak dibuat manual |
| Daftar KPI | 4 | Definisi, sumber data, target, anggaran |
| Laporan pelaksanaan | 5 | Rekap realisasi per item, dihasilkan dari data realisasi |
| Status kriteria K1–K4 | — | Dihitung dari data di atas |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Rencana** | 1 dokumen rencana | jenis (strategis/tahunan), periode berlaku, status (draf/diajukan/disahkan/kedaluwarsa), pengesah, tanggal sah, lampiran | Satu model untuk *roadmap* dan rencana tahunan |
| **Item rencana** | 1 sasaran/kegiatan dalam rencana | sasaran, KPI, target, satuan, PIC, jadwal, anggaran, tautan Renstra | Anak dari Rencana |
| **Realisasi** | 1 laporan realisasi per item per periode lapor | nilai capaian, anggaran terpakai, bukti, pelapor, tanggal | Bukti K3 |
| **Tinjauan** | 1 tinjauan per periode | tanggal, peserta, ringkasan capaian, keputusan, tautan ke item rencana berikutnya | Bukti K4 |

Riwayat perubahan memakai `mail.thread` + `tracking`. Tidak perlu tabel tambahan.

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Periode | Masa berlaku rencana | Master periode bersama | Tahun anggaran diinput manual |
| **KPI** | Definisi, pembilang/penyebut, sumber data, satuan | **Baru** | KPI ditulis langsung di item rencana (tanpa master) |
| **Sasaran Renstra** | Matriks keterkaitan (UPNVJ/UPPS/prodi) | **Baru**, diisi dari dokumen Renstra | Tautan berupa teks bebas. **Jalan ini yang dipakai** di cakupan rancangan (brief, 14 November 2026) |
| Personel | PIC, pengesah, pelapor | **Master bersama dari Pengelolaan 3** | `res.users` |
| Jabatan | Pengesah sah (KaLab/Dekan) | Master bersama dari Pengelolaan 3 | Peran tetap di grup keamanan |

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Personel dan jabatan | Pengelolaan 3 | Wajib | Pakai `res.users` + grup keamanan |
| Dokumen Renstra UPNVJ/UPPS/prodi | Eksternal (universitas/fakultas) | Wajib untuk K2 | Matriks keterkaitan berupa lampiran |
| Data anggaran | Eksternal (keuangan fakultas) | Wajib untuk K2–K3 | Anggaran diinput manual di item rencana |
| Realisasi KPI otomatis | *Dashboard* / registri indikator | Opsional | Realisasi diinput manual |

**Peluang integrasi:** bila KPI lab adalah skor indikator monev (misalnya % sesi terlaksana dari Proses 18), realisasinya bisa diambil langsung dari *dashboard*, tanpa input manual. Ini juga beririsan dengan Pengelolaan 10 versi "Capaian KPI laboratorium dipantau" (belum ada PIC).

## 7. Ditunda

- Penganggaran rinci (mata anggaran, pencairan). Cukup nilai anggaran per item.
- Integrasi dengan sistem keuangan fakultas.
- Tren realisasi multi-tahun.

---

# Pengelolaan 2: SOP dan Instruksi Kerja

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Seluruh SOP dan instruksi kerja yang diperlukan untuk layanan laboratorium tersedia, disahkan, mutakhir, dan dapat diakses pengguna |
| Penerapan / PJ | Umum / KaLab; PLP/laboran |
| Unit | 1 SOP wajib |
| Pembagi | Jumlah SOP wajib dalam daftar kebutuhan yang **ditetapkan sebelum monev** |
| Pembilang | Jumlah SOP wajib yang memenuhi seluruh kriteria |
| Memenuhi bila | SOP disahkan, mutakhir, sesuai kegiatan/risiko, tersedia di titik penggunaan, dan disosialisasikan. (APD dinilai di indikator lain, P05) |
| Skor | 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% atau bukti tidak dapat diverifikasi → 1 |

Bukti dukung: (1) daftar induk kebutuhan SOP berbasis kegiatan/risiko, (2) SOP tata tertib, praktikum, operasi/manajemen, K3, alat, peminjaman, kedaruratan, dan limbah, (3) bukti pengesahan, revisi, distribusi, dan sosialisasi.

Acuan ISO/IEC 17025:2017 8.3.2: dokumen disetujui sebelum terbit oleh personel berwenang, dikaji ulang berkala, status revisinya teridentifikasi, dan versi yang berlaku tersedia di tempat penggunaan.

## 2. Aturan "memenuhi" versi MVP

Satu SOP wajib dinyatakan memenuhi bila semua cek lolos.

| Cek | Arti | Data yang dipakai |
|---|---|---|
| S1 Terdaftar | SOP ada di daftar induk dengan dasar kebutuhan (kegiatan/risiko), dan ditetapkan sebelum tanggal tutup periode | Daftar induk |
| S2 Disahkan | Ada versi berstatus *berlaku* dengan pengesah dari jabatan berwenang dan tanggal sah | Versi SOP, jabatan |
| S3 Mutakhir | Tanggal tinjau ulang berikutnya belum terlewati | Versi SOP |
| S4 Tersedia di titik penggunaan | Versi berlaku terdistribusi ke semua lokasi yang ditetapkan untuk SOP itu | Distribusi |
| S5 Disosialisasikan | Ada rekaman sosialisasi untuk versi berlaku | Sosialisasi |

Kesesuaian isi SOP dengan kegiatan/risiko **tidak** dicek sistem, karena itu penilaian isi oleh penilai.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Daftar induk SOP | 1 | Termasuk dasar kebutuhan dan lokasi penggunaan |
| Dokumen SOP berversi | 2 | File per versi, versi lama tetap tersimpan |
| Riwayat pengesahan dan revisi | 3 | Dari data versi |
| Rekaman distribusi dan sosialisasi | 3 | Per versi |
| Persentase dan daftar SOP tidak memenuhi | — | Dihitung otomatis |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Versi SOP** | 1 revisi dokumen | SOP induk, nomor revisi, file, status (draf/diajukan/berlaku/dicabut), pengesah, tanggal sah, tanggal tinjau berikutnya, ringkasan perubahan | Hanya satu versi *berlaku* per SOP |
| **Distribusi** | 1 versi × 1 lokasi | versi, lokasi (ruang/papan/portal), tanggal, petugas | Bukti S4 |
| **Sosialisasi** | 1 kegiatan sosialisasi | versi, tanggal, metode, bukti; tabel anak **peserta** | Bukti S5 |

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| **Daftar induk SOP** | Pembagi; kode, judul, kategori, dasar kebutuhan, lokasi penggunaan, status wajib | **Baru** | — (ini inti indikator) |
| Ruang lab / lokasi | Titik penggunaan | Master ruang bersama (sudah ada `lab.master.ruangan`) | 8 ruang + "portal" diinput manual |
| Personel dan jabatan | Pengesah, peserta sosialisasi | Master bersama dari Pengelolaan 3 | `res.users` |

**Cukup sebagai pilihan tetap**, tidak perlu tabel master: kategori SOP (tata tertib, praktikum, operasi/manajemen, K3, alat, peminjaman, kedaruratan, limbah), jenis dokumen (SOP/IK/formulir), status versi, dan metode sosialisasi.

**Pengaturan KaLab:** siklus tinjau ulang standar (misalnya 1 tahun).

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Jabatan yang berwenang mengesahkan | Pengelolaan 3 | Wajib untuk S2 | Pengesah = pengguna di grup KaLab |
| Daftar kegiatan/risiko | Pengembangan 23 (risiko, belum ada PIC) | Opsional | Dasar kebutuhan berupa teks bebas |
| Komponen pengendalian dokumen | Pengelolaan 13 (dokumen mutu, belum ada PIC) | Beririsan | Dibangun di sini, lalu dipakai ulang oleh Pengelolaan 13 |

**Dipakai oleh indikator lain:** SOP K3, alat, limbah, dan kedaruratan adalah bukti untuk indikator milik kelompok lain (misalnya Pengelolaan 6 dan 9). Daftar induk SOP sebaiknya bisa dirujuk dari indikator lain.

**Catatan Odoo:** aplikasi *Documents* hanya ada di edisi Enterprise. Di *Community Edition*, versi SOP dibangun sebagai model sendiri dengan `ir.attachment` + `mail.thread` **[CEK edisi yang dipakai]**.

## 7. Ditunda

- Alur persetujuan bertingkat (penyusun → pemeriksa → pengesah). Cukup satu pengesah; pemeriksaan menyatu dengan pengesahan (keputusan 14 November 2026, lihat brief).
- Kuis pemahaman setelah sosialisasi.
- Pengingat otomatis menjelang tanggal tinjau ulang. Sistem cukup menampilkan penanda "perlu ditinjau"; pengingat menjadi saran pengembangan.

---

# Pengelolaan 3: Struktur Organisasi, Tugas, dan Wewenang

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Struktur organisasi laboratorium, tugas, tanggung jawab, wewenang, dan pengganti petugas ditetapkan dan dijalankan |
| Penerapan / PJ | Umum / Dekan; KaLab |
| Unit | 1 paket dokumen dan rekaman |
| Skor | Kriteria berurutan 1–4 (sama dengan Pengelolaan 1) |

Bukti dukung: (1) SK/penetapan pengelola, (2) bagan organisasi, (3) uraian tugas KaLab, PLP/laboran, dosen, asisten, dan petugas K3, (4) matriks kewenangan, (5) bukti koordinasi.

Acuan ISO/IEC 17025:2017 5.5–5.6: struktur organisasi dan posisinya di organisasi induk, tanggung jawab, wewenang, dan hubungan antarpersonel ditentukan.

## 2. Aturan "memenuhi" versi MVP

| Kriteria | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| K1 Disahkan | Struktur dan pengangkatan personel disahkan | Ada SK berstatus *berlaku* dengan pengesah, tanggal, dan daftar personel–jabatan | Keabsahan SK |
| K2 Lengkap | Uraian tugas, batas kewenangan, alur pelaporan, dan petugas pengganti lengkap | Setiap jabatan aktif punya uraian tugas, kewenangan, atasan, dan pengganti | Kejelasan isi |
| K3 Dijalankan | Penugasan dan koordinasi mengikuti struktur | Ada rapat koordinasi pada periode ini. **Opsional:** penugasan petugas sesi (Pengelolaan 4) dan presensi petugas (Proses 18) hanya berisi personel dengan jabatan yang sesuai | Kesesuaian praktik |
| K4 Dievaluasi | Beban kerja dan efektivitas koordinasi dievaluasi, struktur diperbaiki bila perlu | Ada evaluasi pada periode ini, dan keputusannya tertaut ke SK atau uraian tugas yang direvisi | Kualitas evaluasi |

Sistem menampilkan kriteria yang sudah berbukti. Skor akhir ditetapkan penilai (semi-otomatis).

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| SK penetapan | 1 | File SK + daftar personel–jabatan |
| Bagan organisasi | 2 | **Dihasilkan otomatis** dari relasi jabatan → atasan |
| Uraian tugas per jabatan | 3 | Dari master jabatan |
| Matriks kewenangan | 4 | **Dihasilkan otomatis** dari jabatan × kewenangan |
| Notulen koordinasi | 5 | Dari data rapat |
| Rekap beban kerja | — (bukti K4) | Bisa dihitung dari presensi petugas Proses 18 (jumlah sesi per laboran/asisten) |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **SK penetapan** | 1 SK | nomor, tanggal, pengesah (Dekan), masa berlaku, status, file; tabel anak **personel–jabatan** (personel, jabatan, mulai, selesai) | Riwayat SK tetap tersimpan |
| **Rapat koordinasi** | 1 rapat | tanggal, peserta, agenda, keputusan, notulen | Bukti K3 |
| **Evaluasi struktur** | 1 evaluasi per periode | temuan beban kerja, efektivitas koordinasi, keputusan perubahan, tautan ke SK/jabatan yang direvisi | Bukti K4 |

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| **Personel** | Semua orang yang punya peran di lab: KaLab, PLP/laboran, dosen, asisten, petugas K3 | **Master bersama, harus diputuskan.** Saat ini tersebar di `mst_dosen`, `op.faculty`, `op.student` / `op.student.assistant`, `res.users`. Odoo juga punya `hr.employee` di modul HR | Laboran diinput manual (jumlahnya sedikit) |
| **Jabatan** | Uraian tugas, kewenangan, atasan (alur pelaporan), jabatan/personel pengganti | **Baru.** Kandidat: `hr.job` (Odoo HR) atau model sendiri. `mst_role` milik Rafika hanya berisi nama peran, tanpa tugas dan wewenang | — (ini inti indikator) |
| Kewenangan | Isi matriks kewenangan | Cukup daftar di jabatan (teks atau pilihan) | — |
| Unit / lab | Posisi lab dalam organisasi induk (FIK) | Cukup pengaturan | — |

**Keputusan penting untuk kelompok:** master **Personel** dipakai oleh Pengelolaan 1 (PIC), 2 (pengesah), 4 dan 10 (petugas, otorisasi), 14 (laboran yang dilatih), dan 18 (presensi petugas). Bila tiap indikator membuat daftar personelnya sendiri, data akan tidak sinkron. Pilihan yang perlu dibandingkan:

| Opsi | Kelebihan | Kekurangan |
|---|---|---|
| `hr.employee` + `hr.job` (Odoo HR) | Bagan organisasi, atasan, dan jabatan sudah tersedia | Asisten adalah mahasiswa, bukan pegawai. Menambah dependensi modul |
| Model personel sendiri, ditautkan ke `res.partner`/`res.users`, `op.faculty`, `op.student` | Bisa mencakup dosen, laboran, dan asisten dalam satu tempat | Bagan organisasi harus dibuat sendiri |
| Pakai yang sudah ada di modul Rafika (`mst_dosen`, `op.student.assistant`, `res.users`) | Paling cepat | Laboran dan petugas K3 belum punya tempat. Tetap tersebar |

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| SK Dekan | Eksternal (fakultas) | Wajib untuk K1 | Diunggah sebagai file |
| Penugasan dan presensi petugas | Pengelolaan 4, Proses 18 | Opsional (memperkuat K3–K4) | K3–K4 dari rapat dan evaluasi saja |

**Dipakai oleh:** Pengelolaan 1, 2, 4, 10, Pengembangan 14, Proses 18. Pengelolaan 3 berada **paling hulu**.

## 7. Ditunda

- Bagan organisasi interaktif. MVP cukup tampilan hierarki atau laporan.
- Analisis beban kerja rinci (jam kerja, ekuivalen penuh waktu). MVP cukup jumlah sesi per personel.
- Delegasi wewenang otomatis saat petugas berhalangan.

---

## Perbandingan kompleksitas (modul Tata Kelola & Dokumen)

Dihitung dengan cara yang ada di [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md#6-cara-menghitung-kompleksitas). Angkanya **kasar**, hanya untuk membandingkan antarindikator, bukan perkiraan waktu.

| Indikator | T (fact baru) | M (master baru) | D (dependensi wajib) | E (sistem/dokumen eksternal) | A (alur persetujuan) | Data saat ini | Total |
|---|---|---|---|---|---|---|---|
| Pengelolaan 1 | 4 | 2 | 1 (Pengelolaan 3) | 2 (Renstra, anggaran) | 2 (pengesahan, tinjauan) | Belum ada (+2) | **13** |
| Pengelolaan 2 | 3 | 1 | 1 (Pengelolaan 3) | 0 | 1 (pengesahan versi) | Belum ada (+2) | **8** |
| Pengelolaan 3 | 3 | 2 | 0 | 1 (SK Dekan) | 1 (pengesahan SK) | Belum ada (+2) | **9** |
| Pengembangan 13 | 3 (atau 0 bila memakai model rencana Pengelolaan 1) | 0 | 1 (Pengelolaan 3) | 2 (kurikulum/riset/PkM, biaya) | 2 (pengesahan, tinjauan) | Belum diketahui (+2) | **10** (atau **7**) |

Catatan pembacaan:
- **Pengelolaan 1** paling berat, karena banyak bergantung pada dokumen eksternal (Renstra, anggaran) yang belum tentu ada.
- **Pengelolaan 3** angkanya sedang, tetapi **bobot keputusannya paling besar**, karena master personel dan jabatan dipakai hampir semua package lain di proyek.
- **Pengembangan 13** turun dari 10 ke 7 bila dibangun di atas model rencana Pengelolaan 1.
- Di dalam modul ini ada dua komponen yang bisa dibangun sekali lalu dipakai bersama:
  - **"Paket dokumen + bukti per kriteria"**: Pengelolaan 1, 3, Pengembangan 13.
  - **"Pengendalian dokumen berversi"**: Pengelolaan 2, juga kandidat untuk Pengelolaan 13 (dokumen mutu, belum ada PIC).
- Pengembangan 14 (pelatihan) memakai pola kriteria yang sama, tetapi package-nya ada di modul SDM & Kompetensi.

## Pertanyaan minimum sebelum lanjut

**Untuk KaLab**
- [ ] Apakah LabFIK sudah punya *roadmap*/renstra lab dan rencana kerja tahunan? Siapa yang menyusun dan mengesahkan? Apakah memuat KPI dan anggaran?
- [ ] Apakah sudah ada daftar SOP/IK? Berapa jumlahnya, di mana disimpan (kertas, Drive, portal lab), dan siapa yang mengesahkan?
- [ ] Bagaimana SOP disosialisasikan ke asisten dan praktikan? Apakah ada rekamannya?
- [ ] Apakah ada SK struktur pengelola lab? Siapa saja yang tercantum (KaLab, laboran, petugas K3, koordinator)?
- [ ] Apakah uraian tugas laboran dan asisten sudah tertulis? Siapa pengganti bila KaLab atau laboran berhalangan?
- [ ] Apakah ada rapat koordinasi rutin? Apakah ada notulennya?

**Untuk kelompok (Zahir, Herrens)**
- [ ] Master personel memakai opsi yang mana (lihat tabel opsi di Pengelolaan 3)? Opsi yang dipilih menjadi kontrak bersama untuk semua modul.
- [ ] Apakah Zahir (pemegang SDM & Kompetensi) ingin memakai pola "paket dokumen + bukti per kriteria" untuk Pengembangan 14?
- [x] ~~Odoo *Community* atau *Enterprise*?~~ Community (keputusan 26 Okt 2026), sehingga aplikasi *Documents* tidak tersedia.
