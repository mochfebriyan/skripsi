# Brief Role 3: Pelaksanaan Sesi & Dashboard Skor

17 Oktober 2026 · Febriyan · Bagian dari proyek LabFIK Compliance (lihat [brief-seluruh-projek.md](brief-seluruh-projek.md))

## Ringkasan

- **Apa:** modul Odoo yang mencatat pelaksanaan setiap sesi praktikum LabFIK pada saat sesi berlangsung, lalu menghitung skor indikator monev secara otomatis dan menampilkannya dalam *dashboard* yang bisa ditelusuri sampai ke sesi.
- **Indikator yang dipegang:** Proses 18 (sesi terlaksana sesuai jadwal, modul, dan waktu). *Dashboard* juga menampilkan skor 4 indikator lain milik kelompok (Pengelolaan 4, Persiapan 15–17), dengan data dan aturan dari Role 1 dan Role 2.
- **Masalah utama:** saat ini persentase Proses 18 tidak bisa dihitung ataupun diverifikasi. Lebih dari separuh kelas praktikum tidak punya rekaman sama sekali, dan rekaman yang ada dibuat untuk honor, bukan sebagai bukti mutu.
- **Posisi sistem:** alat pencatatan, pembuktian, dan pemantauan. Sistem **tidak menjamin** skor naik. Skor tetap ditentukan oleh apakah sesi benar-benar terlaksana.
- **Usulan judul:** Kustomisasi Modul Odoo untuk Pencatatan Pelaksanaan Sesi dan Perhitungan Otomatis Skor Indikator Monev Laboratorium (Studi Kasus: Laboratorium FIK UPN "Veteran" Jakarta)

## Posisi dalam proyek

| Role | Modul | Indikator | Hubungan dengan Role 3 |
|---|---|---|---|
| Role 1 | Asisten Praktikum | Pengelolaan 4 | Memberi data penugasan asisten/laboran per sesi. Role 3 mengirim presensi asisten untuk dasar honor |
| Role 2 | Perencanaan & Persiapan Sesi | Persiapan 15, 16, 17 | Memberi sesi rencana (jadwal), modul berversi, dan checklist kesiapan. **Sesi rencana adalah pembagi Proses 18** |
| **Role 3** | Pelaksanaan Sesi & Dashboard | Proses 18 + *dashboard* 5 indikator | Mencatat realisasi, perubahan, dan sesi pengganti. Menghitung dan menampilkan skor. Tugas lintas modul: black box dan UAT |

Role 3 berada **paling hilir**. Semua role memakai satu model data sesi praktikum, jadi model ini harus disepakati di awal (lihat *Kontrak data dengan Role 1 & 2*).

## Indikator Proses 18

Isi rubrik dari Instrumen Monev Laboratorium UPNVJ 2026 v1.1:

- **Bunyi:** sesi praktikum terlaksana sesuai jadwal, modul, dan waktu kegiatan yang ditetapkan. Penerapan umum. Penanggung jawab: Dosen dan KaLab.
- **Pembagi:** seluruh sesi praktikum yang **direncanakan** pada periode monev.
- **Pembilang:** sesi rencana yang terlaksana sesuai ketentuan, atau yang diubah secara sah dengan tujuan dan waktu setara.
- **Syarat memenuhi:** kegiatan, durasi, dan tujuan sesuai; perubahan sah; sesi tertunda baru dihitung memenuhi **setelah sesi penggantinya selesai dalam periode pelaporan**.
- **Bukti:** (1) jadwal, (2) jurnal sesi, (3) presensi praktikan, asisten, laboran, dan dosen, (4) modul yang dipakai, (5) *log book* praktikum, (6) perubahan yang disetujui, (7) penggantian sesi.
- **Skor:** dihitung dari persentase. 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% → 1. Bukti yang tidak bisa diverifikasi → 1.

Instrumen mengacu antara lain pada **SNI ISO/IEC 17025:2017**. Butir yang relevan:

- **7.5.1:** rekaman teknis memuat tanggal dan identitas personel, dan "harus direkam pada saat dibuat".
- **7.5.2:** perubahan rekaman harus dapat ditelusuri ke versi sebelumnya, beserta tanggal dan personel yang mengubah.

Dasar resmi bahwa monev 2026 mengarah ke ISO 17025 belum ada; lihat Pertanyaan terbuka.

**Penerjemahan rubrik ke aturan sistem (draf):**

| Kondisi sesi rencana | Hasil |
|---|---|
| Terlaksana pada tanggal dan jam rencana, durasi ≥ ambang, topik sesuai modul pertemuan ke-n, jurnal dan presensi lengkap | Memenuhi |
| Dibatalkan → perubahan disetujui → pengganti selesai dalam periode, dengan durasi dan tujuan setara | Memenuhi |
| Pengganti belum selesai saat periode ditutup | Tidak memenuhi |
| Batal tanpa pengganti, tidak ada jurnal atau presensi, atau durasi kurang | Tidak memenuhi, dengan alasan tercatat |

Dua ambang **belum ditetapkan** oleh instrumen dan perlu diputuskan KaLab: toleransi keterlambatan mulai dan durasi minimal sesi.

## Kondisi saat ini (*as-is*)

1. **Rencana:** sheet "Alokasi Pertemuan Asisten Praktikum" berisi satu baris per kelas, dengan kolom pertemuan 1–15 + UTS/UAS yang diisi nama asisten. **Kolom Hari dan Jam kosong di semua periode.** Kelas tanpa asisten tetap tercantum, tapi kolom pertemuannya kosong.
2. **Realisasi:** asisten mengisi Google Form "Pelaksanaan Asistensi Praktikum". Isinya tanggal, jam, ruang, pertemuan ke-, jumlah mahasiswa hadir, dosen hadir (ya/tidak), topik, kesiapan sarana, kendala, link modul, dan foto.
3. **Lembar kegiatan kertas:** diisi bersamaan dengan form, hanya sebagai **bukti fisik untuk pengajuan honor ke rektorat**. Isinya tidak memuat rincian kegiatan, dan KaLab sebenarnya tidak terlalu membutuhkannya. Lembar ini **tidak bisa dipakai sebagai *log book* praktikum**.
4. **Rekap:** dilakukan manual di sheet jawaban form. Ada sheet per asisten, per mata kuliah, cek jumlah di kertas, rekap honor (Rp25.000 per sesi), status rekening dan KTP, serta "Ketercakupan Praktikum" (jumlah pertemuan dibagi 16). Sheet ketercakupan itu pada dasarnya **versi manual dari *dashboard* Role 3**.

Seluruh pencatatan dirancang untuk **honor**, sehingga hanya sesi yang punya asisten yang tercatat.

## Temuan data

Sumber: kedua sheet di atas, dibaca penuh pada 17 Oktober 2026. Form berisi 1.103 respons dari 4 periode: 2024/2025 Genap (312), 2025/2026 Ganjil (286), 2025/2026 Genap (466), dan 2026/2027 Ganjil (39, masih berjalan, data sampai 14 Okt 2026). Ada 8 ruang: FIKLAB-201, 301–304, 401–403. Rencana dicocokkan dengan laporan berdasarkan kode MK + kelas + pertemuan ke-.

### Cakupan rencana ↔ realisasi (temuan utama)

| Periode | Kelas praktikum | Kelas tanpa asisten | Sesi berasisten direncanakan | Punya laporan |
|---|---|---|---|---|
| 2025/2026 Ganjil | 71 | 40 (56%) | 351 | 260 (**74%**) |
| 2025/2026 Genap | 79 | 33 (42%) | 644 | 415 (**64%**) |
| 2026/2027 Ganjil* | 72 | 40 (56%) | 303 | 34 (11%) |

\* Masih berjalan, jadi bukan baseline.

- Kelas tanpa asisten **tidak punya rekaman apa pun**. Pembagi Proses 18 mencakup kelas-kelas ini, sehingga skor saat ini praktis tidak dapat diverifikasi.
- Untuk sesi berasisten saja, cakupannya 64–74%, setara skor 1–2.
- Ada 30 laporan (15 per periode) yang tidak ada di rencana.

### Kualitas rekaman

| Temuan | Angka | Kaitan |
|---|---|---|
| Keterlambatan pengisian (median) | 1 hari (2024/2025 Genap, 2025/2026 Ganjil); **30 hari** (2025/2026 Genap) | ISO 7.5.1: "direkam pada saat dibuat" |
| Laporan > 30 hari setelah sesi | 25% / 11% / **50%** (2024/2025 Genap / 2025/2026 Ganjil / 2025/2026 Genap) | Sama |
| Durasi tidak valid (jam selesai < jam mulai, salah AM/PM) | 140 laporan (13%) | Perlu validasi input |
| Tanggal salah tahun (2005/2006) | 5 | Perlu validasi input |
| Hari tidak cocok dengan tanggal | 55 | Perlu validasi input |
| Laporan ganda (MK, kelas, pertemuan sama) | 48 | Perlu constraint unik per sesi |
| Sesi dilaporkan asisten berbeda dari rencana | 35 (2025/2026 Genap), 1 (2025/2026 Ganjil) | Penggantian asisten tidak tercatat |
| Sesi "online/Zoom/GMeet" tanpa catatan persetujuan | ±50 | Perubahan sesi tidak tercatat |
| Durasi median | 100 menit (Ganjil) vs 50 menit (2025/2026 Genap) | Tidak ada durasi rencana, jadi syarat "durasi sesuai" tidak bisa dinilai |
| Format nama MK | Berubah tiap periode (tanpa kode, kode di belakang, kode di depan) | Perlu master MK (Role 2) |
| Presensi laboran | Tidak ada | Bukti (3) tidak lengkap |
| Presensi praktikan | Hanya jumlah, tidak per nama | Bukti (3) lemah |
| Dosen hadir "Ya" | 50% / 38% / 88% / 95% per periode | — |
| Field rinci "Kehadiran Dosen Praktikum" | Baru terisi 3,5% (field baru) | — |
| Link modul terisi | 92% secara keseluruhan; 27% kosong di 2024/2025 Genap | Modul diunggah saat atau setelah sesi, tanpa versi (Persiapan 15, Role 2) |
| Kesiapan sarana | Siap 998, Dapat disesuaikan 84, Belum siap 11 | Diisi asisten, bukan laboran (Persiapan 16, Role 2) |
| Rekap honor form vs lembar kegiatan | Selisih pada 7 dari 21 asisten yang punya data | Data untuk Role 1 |

**Catatan privasi:** kedua sheet memuat nama, NIM, nomor HP, dan status rekening/KTP asisten. Data seed, demo, dan lampiran wajib dianonimkan. Minta izin KaLab sebelum angka-angka ini dikutip di proposal.

## Temuan dari kode yang ada (modul Rafika + OpenEduCat)

- **Platform:** Odoo 17 (`'version': '17.0.1.0'`). Modul `PendaftaranAsisten` bergantung pada `openeducat_core`, `openeducat_admission`, `openeducat_attendance`, dan `openeducat_timetable`.
- **`op.session` sudah dipakai Rafika** sebagai sesi bertanggal, dengan `start_datetime`, `end_datetime`, dan state `draft/confirm/done/cancel`. Lihat `asprak_allocation.py` (alokasi) dan `self_allocation.py` (cek bentrok). Model ini sebaiknya di-*inherit* menjadi sesi praktikum, bukan membuat model baru.
- **`jadwal.praktikum` hanya template mingguan** (hari + jam), bukan sesi bertanggal.
- **Presensi OpenEduCat** (`op.attendance.sheet`/`op.attendance.line`) terhubung ke `op.session`, tetapi **hanya untuk mahasiswa** (`op.student`). Presensi asisten, laboran, dan dosen harus ditambahkan.
- **`lab.readiness.checklist`** terhubung ke fasilitas, bukan ke sesi. Ini wilayah Role 2, tapi perlu dihubungkan ke sesi agar *dashboard* bisa menghitung Persiapan 16.
- **Ada dua set master data:** `mst_*` milik Rafika (`mst_coursesemt`, `mst_dosen`, `mst_kodekelas`, `mst_periodesemt`) dan `op.course`/`op.faculty`/`op.batch` milik OpenEduCat. **Pilihan ini harus disepakati dengan Role 2.**
- **Field yang belum ada:** waktu aktual, topik dan pertemuan ke-, modul yang dipakai, *log book*, relasi sesi asal ↔ pengganti, dan status perubahan.

## Lingkup modul Role 3

1. **Jurnal sesi:** waktu mulai dan selesai aktual, topik, pertemuan ke-, modul yang dipakai (ditautkan ke modul berversi milik Role 2), kendala, dan foto. Jurnal hanya dibuka pada hari sesi dan dikunci setelah batas waktu. Ini menjawab masalah keterlambatan.
2. **Presensi empat pihak:** praktikan per nama (`op.attendance`), asisten, laboran, dan dosen.
3. ***Log book* praktikum digital:** isi kegiatan per sesi, menggantikan fungsi bukti yang tidak bisa dipenuhi lembar kertas. *Opsional:* mencetak rekap sebagai bukti fisik honor untuk rektorat, supaya asisten tidak mengisi dua kali (koordinasi dengan Role 1).
4. **Perubahan dan sesi pengganti:** pengajuan perubahan, persetujuan KaLab, sesi pengganti yang terhubung ke sesi asal, dan status yang mengikuti aturan "dihitung setelah pengganti selesai".
5. ***Audit trail*:** riwayat perubahan rekaman (*tracking* `mail.thread`), sesuai ISO 7.5.2.
6. **Mesin skor:** registri indikator berisi kode aspek + nomor (karena nomor di instrumen tidak unik), pembagi, aturan memenuhi, dan alasan gagal; dihitung per periode monev, dengan skor 1–4 dari ambang persentase. Setiap role menyumbang aturan indikatornya sendiri. Kelompok lain atau kelompok tahun depan bisa menambah indikator tanpa mengubah mesinnya.
7. ***Dashboard*:** persentase dan skor 5 indikator per periode, bisa diklik sampai ke daftar sesi yang tidak memenuhi beserta alasannya.
8. **Importer data historis:** sheet Alokasi menjadi sesi rencana, dan form Pelaksanaan menjadi jurnal. Gunanya ada dua: data uji nyata tanpa menunggu modul Role 1/2, dan baseline untuk membandingkan skor manual dengan skor sistem.

## Batasan masalah (usulan)

1. Mitra: praktikum terjadwal di LabFIK UPNVJ (8 ruang). Peminjaman lab untuk kegiatan lain tidak termasuk.
2. Pencatatan dibangun untuk Proses 18. *Dashboard* menampilkan 5 indikator, tetapi data dan aturan Pengelolaan 4 dan Persiapan 15–17 berasal dari Role 1 dan 2. 59 indikator monev lainnya tidak dicakup.
3. Tahapan yang dicakup: pelaksanaan sesi sampai penutupan periode. Rekrutmen, penugasan, penjadwalan, kesiapan sarana, dan honor berada di penelitian lain.
4. Platform Odoo 17 + OpenEduCat, melanjutkan modul Anandar (2026).
5. Data: data historis 2025/2026 Ganjil–Genap yang dianonimkan. **[Putuskan: apakah ada uji coba di semester berjalan?]**
6. Sistem adalah alat pencatatan, pembuktian, dan pemantauan. Sistem tidak menjamin indikator terpenuhi dan tidak menggantikan verifikasi asesor monev. Ambang aturan mengikuti ketetapan KaLab.
7. Pengujian: black box dan UAT.

## Kontrak data dengan Role 1 & 2

Field minimum pada sesi praktikum (*inherit* `op.session`) yang perlu disepakati bersama:

| Field | Diisi oleh | Dipakai untuk |
|---|---|---|
| Periode, MK, kelas, ruang, pertemuan ke- | Role 2 | Kunci sesi, pembagi |
| Tanggal dan jam rencana, durasi rencana | Role 2 | "Sesuai jadwal/waktu" |
| Modul berversi untuk pertemuan ke-n | Role 2 | "Sesuai modul", Persiapan 15 |
| Status persetujuan jadwal | Role 2 | Persiapan 15 |
| Checklist kesiapan per sesi | Role 2 | Persiapan 16, 17 |
| Laboran dan asisten yang ditugaskan, surat tugas | Role 1 | Pengelolaan 4, pembanding presensi |
| Jurnal, waktu aktual, presensi 4 pihak, *log book* | **Role 3** | Proses 18 |
| Status pelaksanaan, perubahan, sesi asal/pengganti | **Role 3** | Proses 18 |
| Presensi asisten pada sesi terlaksana | Role 3 → Role 1 | Honor |

## Metode dan pengujian

- **Usulan metode: Water-Scrum-Fall.**
  - *Water*: analisis *as-is*, wawancara, dan desain model data bersama ketiga role.
  - *Scrum*: sprint fitur dengan demo ke KaLab, karena aturan seperti ambang dan prosedur ganti sesi baru akan jelas setelah ada prototipe.
  - *Fall*: black box, UAT, dan *deployment*.
- Ada preseden di UPNVJ 2026: Gulo (Odoo, inventori Puskesmas) dan Permana (Odoo FSM, PT TMD).
- Sebaiknya ketiga role memakai metode yang sama.
- Rujukan metode yang terbit ≥2022 belum diverifikasi. Rujukan asli, West (Forrester, 2011), terlalu tua untuk batas 2022.
- **Evaluasi:** black box, UAT, dan perbandingan skor Proses 18 hitungan manual vs hitungan sistem pada data 2025/2026 Genap. **Kenaikan skor tidak dipakai sebagai ukuran**, karena di luar kendali sistem.

## Struktur proposal (Pedoman TA FIK 2025, jenis Prototipe/Proyek)

- **Bab I:**
  - 1.1 Latar Belakang
  - 1.2 **Identifikasi Masalah** (bukan Rumusan Masalah)
  - 1.3 Batasan Masalah
  - 1.4 Tujuan dan Manfaat
  - 1.5 Jadwal Kegiatan
- **Bab II Rancangan Proyek:**
  - 2.1 Observasi: temuan data detail masuk di sini
  - 2.2 Usulan Solusi: rubrik Proses 18 dan metode
  - 2.3 Rancangan
  - 2.4 Rencana Pengujian
- **Tidak ada bab Tinjauan Pustaka.** Rubrik tetap memberi bobot 20% untuk penguasaan studi terkait, jadi paragraf penelitian terdahulu di Latar Belakang harus kuat.
- **Rubrik penilaian:** kesesuaian judul 15, penerapan teknologi 15, masalah jelas 20, studi terkait 20, **kesesuaian metode 30**.
- **Proposal ditolak** antara lain bila solusi tidak menyelesaikan masalah (3.4c). Karena itu masalah, tujuan, dan fitur dipetakan satu lawan satu (lihat tabel di bawah).
- **Lampiran wajib:** dokumen observasi dan wawancara, serta Surat Keterangan Riset dari LabFIK.
- **Batas waktu:** pengajuan seminar proposal paling lambat minggu ke-10 perkuliahan; similarity maksimal 25%.

**Peta masalah, tujuan, dan fitur:**

| Masalah (1.2) | Tujuan (1.4) | Fitur |
|---|---|---|
| M1. Pelaksanaan sesi tidak terekam utuh dan tidak bisa dipasangkan dengan rencana | T1. Pencatatan pelaksanaan yang terhubung ke sesi rencana, termasuk perubahan dan pengganti | 1, 4, 8 |
| M2. Rekaman tidak memenuhi syarat bukti (terlambat, tanpa laboran, tanpa *log book*, perubahan tidak tercatat) | T2. Rekaman yang dicatat saat sesi, memuat identitas personel, presensi 4 pihak, dan perubahan yang tertelusur | 1, 2, 3, 5 |
| M3. Skor dihitung manual menjelang monev dan tidak tertelusur per sesi | T3. Skor Proses 18 dihitung otomatis dengan *dashboard* 5 indikator yang bisa ditelusuri | 6, 7 |

**Manfaat:**
- KaLab: bukti siap saat monev, dan kelas tertinggal terpantau sepanjang semester.
- Asisten, laboran, dosen: cukup mencatat satu kali.
- Proyek: mesin skor bisa diperluas ke indikator lain.
- Akademik: contoh penerapan Odoo untuk pembuktian mutu laboratorium.

Jangan menjanjikan kenaikan skor.

## Status draf Bab I

- [Latar Belakang](../pendahuluan/draft/pendahuluan-role-3.md): 7 paragraf, beserta daftar pustaka. Sisa placeholder: dasar resmi ISO 17025, data wawancara KaLab, dan metode (usulan Water-Scrum-Fall).
- Identifikasi Masalah, Batasan, Tujuan dan Manfaat: struktur sudah disepakati (bagian di atas), prosa belum ditulis.
- Jadwal Kegiatan: belum.

## Referensi yang sudah diverifikasi

Setiap referensi dicek ke halaman jurnal, PDF, atau abstrak repository.

| Referensi | Dipakai untuk | DOI / tautan | Catatan |
|---|---|---|---|
| Annam *et al.* (2026), JPPIK 4(2) 34–43 | Praktikum penting tapi pelaksanaannya sering belum optimal | 10.29303/jppik.v4i2.1602 | Konteksnya IPA; ganti dengan sumber bidang komputer bila ada |
| Widyantoro *et al.* (2025), *Health Education Laboratory* 1(1) 33–40 | SI lab: inventaris, peminjaman, jadwal, pemakaian | 10.29238/helab.v1i1.2165 | Draf lama salah tulis tahun (2024) |
| Ismail *et al.* (2026), JIP 12(3) 519–528 | E-SPMI: dokumen dan validasi audit mutu internal | 10.33795/jip.v12i3.9580 | Urutan penulis di PDF berbeda dengan di situs jurnal |
| Nurramadhona *et al.* (2025), JIP 12(1) 9–18 | Analisis ketercapaian otomatis + *dashboard*, sumbernya penilaian auditor | 10.33795/jip.v12i1.8432 | Penelitian paling dekat; celah penelitian kita dirumuskan dari sini |
| Nurrohmah & Wiratama (2022), Ultima InfoSys 13(2) 77–84 | Odoo *open source* dan bisa dikustomisasi | 10.31937/si.v13i2.2802 | Terbit online 31 Jan 2023, label volume 2022 |
| Tiara (2026), skripsi UPNVJ | Monitoring IKU, realisasi direkam dan ditautkan ke Repository | repository.upnvj.ac.id/51983 | — |
| Anandar (2026), skripsi UPNVJ | Modul Odoo OpenEduCat tahap perencanaan (Waterfall, SUS 81,88) | repository.upnvj.ac.id/51635 | Pendahulu langsung |
| Odoo S.A. (2023), Security in Odoo 17.0 | Hak akses dan *record rule* per grup | odoo.com/documentation/17.0 | 2023 adalah tahun rilis v17 |
| BSN (2018), SNI ISO/IEC 17025:2017 | 7.5.1–7.5.2 rekaman teknis | — | Lebih tua dari 2022, tapi dipakai karena standar acuan instrumen |
| UPNVJ (2026), Instrumen Monev v1.1 | Rubrik Proses 18 | Dokumen internal | — |

**Tidak dipakai:** Fahrurrozi (2024), yang dirujuk Rafika, tidak dapat ditemukan.

## Risiko dan mitigasi

| Risiko | Mitigasi |
|---|---|
| Role 3 tertahan karena bergantung pada sesi rencana (Role 2) dan penugasan (Role 1) | Sepakati kontrak data di minggu awal. Pakai importer data historis agar bisa jalan sendiri |
| Penguji mempertanyakan klaim "*dashboard* 5 indikator" | Batasan no. 2: aturan 4 indikator lain milik Role 1/2, Role 3 membangun mesin dan tampilannya |
| Klaim berlebihan "meningkatkan skor monev" | Pembingkaian sebagai alat bukti dan pemantauan. Evaluasi lewat akurasi skor dan UAT |
| Ambang aturan (telat, durasi) tidak pernah ditetapkan | Jadikan parameter yang bisa diatur KaLab, nilai awalnya hasil wawancara |
| Data pribadi bocor ke lampiran atau demo | Anonimkan saat import, dan jangan *commit* data mentah |
| Kebiasaan lapor terlambat tetap berlanjut | Jurnal dibuka hanya pada hari sesi, dengan notifikasi. Laporan yang telat ditandai sebagai "tidak memenuhi" |

## Pertanyaan terbuka

**Untuk Pak Widi**
- [ ] Apa dasar resmi bahwa monev 2026 mengacu ke ISO/IEC 17025?
- [ ] Apakah *dashboard* sebagai mesin skor generik boleh menjadi kontribusi utama Role 3?
- [ ] Apakah ketiga role memakai Water-Scrum-Fall? Di proposal, metode diletakkan di mana?
- [ ] Apakah ada uji coba di semester berjalan, atau cukup data historis?

**Untuk KaLab/PLP (wawancara, wajib sebagai lampiran)**
- [ ] Berapa toleransi keterlambatan mulai dan durasi minimal sesi?
- [ ] Bagaimana prosedur batal dan ganti sesi, dan siapa yang menyetujui? Apakah sesi online dianggap sah?
- [ ] Bagaimana sesi di kelas tanpa asisten berjalan dan dicatat?
- [ ] Di mana jadwal hari dan jam resminya ("Rangkuman Alokasi Slot Praktikum")?
- [ ] Apakah lembar kegiatan kertas juga diisi terlambat bersama form?
- [ ] Apa saja syarat bukti fisik honor dari rektorat?
- [ ] Bolehkah angka dari kedua sheet dikutip di proposal? Apakah LabFIK bisa menerbitkan Surat Keterangan Riset?

**Untuk Role 1 & 2**
- [ ] Master data mana yang dipakai: `mst_*` atau `op.*`?
- [ ] Field kontrak data di atas.
- [ ] Format modul berversi dan checklist kesiapan per sesi.
- [ ] Alur presensi asisten → honor.

## Langkah berikutnya

1. Konfirmasi pertanyaan untuk Pak Widi, lalu kunci struktur Bab I dan metode.
2. Wawancara KaLab/PLP dan siapkan dokumen lampirannya.
3. Tulis prosa 1.2–1.4, lalu 1.5 Jadwal Kegiatan (mengacu ke batas minggu ke-10).
4. Rapat kontrak data dengan Role 1 dan 2.
5. Mulai Bab II: 2.1 Observasi dari temuan data di brief ini.
