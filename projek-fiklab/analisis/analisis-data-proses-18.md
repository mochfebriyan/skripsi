# Analisis Data Indikator Proses 18 (MVP)

24 Oktober 2026 · Febriyan (Role 3) · Bagian dari proyek LabFIK Compliance

Alur analisis: **target → luaran (bukti dukung) → data transaksi (*fact*) → master data (*dimension*)**. Cakupannya sengaja dibatasi ke MVP. Hanya data yang bisa **dicatat oleh sistem sendiri** yang menjadi syarat wajib. Data yang bergantung pada pihak lain (fakultas, SIAKAD, Role 1/2) diberi jalan pengganti agar modul tetap bisa jalan bila datanya tidak tersedia.

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Sesi praktikum terlaksana sesuai jadwal, modul, dan waktu kegiatan yang ditetapkan |
| Unit | Satu sesi praktikum yang **direncanakan** pada periode monev |
| Pembagi | Seluruh sesi rencana pada periode monev |
| Memenuhi bila | Kegiatan, durasi, dan tujuan sesuai; perubahan sah; sesi tertunda baru dihitung setelah penggantinya selesai dalam periode |
| Skor | 100% → 4, 90–<100% → 3, 70–<90% → 2, <70% atau bukti tidak dapat diverifikasi → 1 |

Bukti dukung: (1) jadwal, (2) jurnal sesi, (3) presensi praktikan, asisten, laboran, dosen, (4) modul yang dipakai, (5) *log book*, (6) perubahan disetujui, (7) penggantian sesi.

## 2. Aturan "memenuhi" versi MVP

Rubrik diringkas menjadi lima cek. Satu sesi rencana dinyatakan memenuhi bila semua cek lolos.

| Cek | Arti | Data yang dipakai |
|---|---|---|
| C1 Terlaksana | Ada jurnal sesi yang sudah dikirim | Jurnal |
| C2 Sesuai jadwal | Tanggal pelaksanaan = tanggal rencana, **atau** ada perubahan yang disetujui | Sesi, jurnal, perubahan |
| C3 Sesuai durasi | Durasi aktual ≥ ambang × durasi rencana | Jurnal, sesi, parameter |
| C4 Sesuai modul dan tujuan | Pertemuan ke-*n* yang dilaksanakan = rencana, modul dilampirkan, dan dosen mengonfirmasi | Jurnal |
| C5 Bukti lengkap | Ada presensi petugas, presensi praktikan, dan minimal satu entri *log book* | Jurnal (baris presensi dan *log book*) |

Sesi yang ditunda dihitung memenuhi hanya bila sesi penggantinya lolos C1–C5 **sebelum** periode ditutup.

Hal-hal berikut **tidak** dijadikan syarat di MVP. Sistem cukup menampilkannya sebagai peringatan:
- **Ketepatan waktu pengisian jurnal.** Rubrik tidak menyebutnya langsung, tetapi jurnal tetap dikunci setelah batas waktu.
- **Kesesuaian dengan RPS per pertemuan.**
- **Kecocokan presensi dengan daftar penugasan.**

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Jadwal sesi | 1 | Daftar sesi rencana bertanggal |
| Jurnal sesi | 2, 4 | Satu per sesi: waktu aktual, pertemuan ke-, topik, lampiran/tautan modul, kendala, foto |
| Presensi | 3 | Baris presensi di dalam jurnal |
| *Log book* | 5 | Baris entri kegiatan di dalam jurnal |
| Perubahan dan pengganti | 6, 7 | Pengajuan, keputusan, dan tautan ke sesi pengganti |
| Skor dan daftar sesi tidak memenuhi | — | Dihitung otomatis dari data di atas, tidak disimpan sebagai tabel terpisah |

## 4. Data transaksi (*fact*): cukup 3 tabel

| Fact | Grain | Isi | Model Odoo |
|---|---|---|---|
| **Sesi** | 1 sesi bertanggal | MK, kelas, ruang, pertemuan ke-, tanggal, jam mulai–selesai rencana, status, `sesi_asal_id` (bila pengganti) | *inherit* `op.session` |
| **Jurnal sesi** | 1 per sesi terlaksana | waktu mulai/selesai aktual, pertemuan ke- dilaksanakan, topik, modul, kendala, foto, pengisi, konfirmasi dosen, status (draf/terkirim/terkunci). Punya dua tabel anak: **presensi** (orang, peran, hadir) dan ***log book*** (waktu, uraian) | model baru + `op.attendance.line` untuk praktikan |
| **Perubahan sesi** | 1 pengajuan | sesi asal, jenis, alasan, pengaju, penyetuju, status (diajukan/disetujui/ditolak), sesi pengganti | model baru |

Skor **dihitung saat dibuka** (*computed*/SQL *view*) dari ketiga tabel ini. Hasil akhir per periode cukup disimpan **satu kali saat periode ditutup**, sebagai arsip bukti.

Riwayat perubahan rekaman memakai fitur bawaan Odoo (`mail.thread` + `tracking`). Tidak perlu tabel tambahan.

## 5. Master data (*dimension*): cukup 5 tabel, sisanya pilihan tetap

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Periode | Batas pembagi dan tanggal tutup | `mst_periodesemt` (sudah ada) | Periode monev dianggap sama dengan semester |
| Mata kuliah + kelas | Identitas sesi | `mst_coursesemt`, `mst_kodekelas` (sudah ada) | Diimpor dari sheet Alokasi |
| Ruang lab | Lokasi sesi | `lab.master.ruangan` (sudah ada) | 8 ruang diinput manual |
| Personel (dosen, laboran, asisten) | Pengisi, presensi, penyetuju | `mst_dosen`, `op.student.assistant`, `res.users` (sudah ada) | Laboran diinput manual (jumlahnya sedikit) |
| Mahasiswa | Presensi praktikan per nama | `op.student` | **Bila KRS tidak tersedia:** presensi praktikan dicatat sebagai jumlah hadir, seperti form sekarang |

Selain kelima tabel itu, semuanya cukup berupa **pilihan tetap** (*selection field*) atau **pengaturan**, bukan tabel master:
- **Pilihan tetap:** status sesi, status jurnal, peran (praktikan/asisten/laboran/dosen), jenis perubahan, alasan perubahan, dan mode (luring/daring).
- **Pengaturan yang diisi KaLab** (`res.config.settings`): ambang durasi minimal, toleransi keterlambatan, batas jam pengisian jurnal, dan sah tidaknya sesi daring. Bila KaLab belum menetapkan, dipakai nilai awal yang disebutkan di proposal.

## 6. Ketergantungan pada pihak lain dan jalan penggantinya

| Butuh | Dari | Bila tidak ada |
|---|---|---|
| Sesi rencana bertanggal (pembagi) | Role 2 | Sesi dibangkitkan dari templat mingguan `jadwal.praktikum` × tanggal periode, atau diimpor dari sheet Alokasi. **Ini satu-satunya ketergantungan yang wajib** |
| Modul berversi | Role 2 | Jurnal menyimpan tautan atau lampiran modul (C4 tetap jalan, tanpa cek versi) |
| Penugasan petugas | Role 1 | Presensi petugas diisi langsung di jurnal tanpa dicocokkan ke penugasan |
| KRS peserta | SIAKAD | Presensi praktikan berupa jumlah |
| RPS per pertemuan | Dosen/prodi | C4 memakai pertemuan ke-*n* + konfirmasi dosen |
| Aturan siapa yang menyetujui perubahan | KaLab | MVP: semua perubahan disetujui KaLab |

## 7. Ditunda (di luar MVP)

Bagian berikut berguna, tetapi baru dikerjakan bila waktu dan data memungkinkan:
- *Snapshot* skor harian atau mingguan untuk grafik tren.
- Master RPS per pertemuan, kalender libur, dan modul berversi (wilayah Role 2).
- Pencocokan presensi dengan penugasan dan KRS.
- Aturan kewenangan persetujuan per jenis perubahan.
- Tanda bahaya kritis dari indikator Q09.
- Laporan ketepatan waktu pengisian per pengisi.

## 8. Pertanyaan minimum sebelum mulai

- [ ] **KaLab:** apakah periode monev sama dengan semester, dan kapan periode ditutup?
- [ ] **KaLab:** berapa ambang durasi minimal dan toleransi keterlambatan? Apakah sesi daring sah?
- [ ] **KaLab:** siapa yang mengisi jurnal pada kelas tanpa asisten?
- [ ] **Role 1 & 2:** master data mana yang dipakai, `mst_*` atau `op.*`? Siapa yang membangkitkan sesi bertanggal?
