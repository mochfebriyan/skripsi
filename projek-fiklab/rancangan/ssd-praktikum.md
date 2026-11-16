# System Sequence Diagram dan Katalog Operasi Modul Pelaksanaan Praktikum

16 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Langkah 8 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 ("sequence diagram"). Katalog operasi dan kamus DTO adalah bahan kerja untuk conceptual model (langkah 9) dan design class diagram (langkah 10).

Diagram: [ssd-praktikum.drawio](ssd-praktikum.drawio), 5 halaman (SSD-1 s.d. SSD-5). Skrip pembuatnya: [tools/drawio/praktikum/ssd.py](../tools/drawio/praktikum/ssd.py) (mesin gambar dari `contoh-tata-kelola/ssd.py`; prefiks `prk-ssd`, lebar lajur, dan data diganti). `validate.py` dengan prefiks `prk-`: **OK** di kelima halaman. Tampilan dicek lewat ekspor PNG draw.io desktop (16 Nov 2026).

Sumber: [expanded-use-case-praktikum.md](expanded-use-case-praktikum.md) (alur lengkap UC-PRK-03, 11, 13, 15, 23; AB-PRK-01–34; pola «CRUDL» dan «report»; calon operasi di bagian 7).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Lifeline `:Aktor`, `:Antarmuka` (*boundary*), `:Kontroler` (*façade controller*). Aktor hanya berkomunikasi dengan antarmuka | §7.2, §7.4 | Semua SSD |
| *System event* (aktor → antarmuka) dan *system return* (antarmuka → aktor) berupa informasi, bukan pemanggilan operasi | §7.3 | Panah hitam penuh dan putus-putus |
| **Command** `op(args)` mengubah data dan tidak mengembalikan nilai; **query** `dto = op(args)` hanya membaca (CQS) | §7.1, §7.4 | Panah ungu; kolom "Jenis" di katalog |
| Data majemuk lebih dari tiga elemen ditulis `dto_x` dan didefinisikan di kamus; `*` = koleksi; *terpilih* = pilihan dari daftar | §7.3 | Bagian 4 |
| **Stateless**: kontroler tidak mengingat apa pun di antara operasi; `user_id` dan rekaman terpilih dikirim ulang ke setiap operasi | §7.5 | Semua operasi yang butuh identitas pengguna |
| Alur alternatif sebagai `opt «exception»` / `opt «variant»`; use case lain sebagai `ref` | §7.6 | Fragmen di setiap SSD |
| Operasi berpola sama disatukan dengan parameter `filter` | CLAUDE.md langkah 8 | `daftar_sesi`, `daftar_pengajuan`, `daftar_survei`, pola «CRUDL» |

**Kontroler:** satu *façade controller* untuk modul (§7.4, subpola pertama), sama dengan Tata Kelola. Di langkah 10, operasi dipetakan ke method model Odoo, bukan ke satu kelas kontroler.

---

## 2. Daftar SSD

| SSD | Use case | Aktor kedua | Fragmen alternatif |
|---|---|---|---|
| SSD-1 | UC-PRK-03 Impor Jadwal Kelas | — | V1 tanpa berkas, E1 (AB-PRK-01), E2 (AB-PRK-04), E3 baris tidak valid |
| SSD-2 | UC-PRK-11 Periksa Kesiapan Sesi | Dosen kelas (pemberitahuan substitusi, O) | V1 substitusi → `ref` UC-PRK-12, E1 (AB-PRK-13), E2 (AB-PRK-15), E3 (AB-PRK-16), E4 (AB-PRK-13) |
| SSD-3 | UC-PRK-13 Kirim Jurnal Sesi | — | V1 simpan draf, E1 (AB-PRK-17), E2 (AB-PRK-18), E3 (AB-PRK-19) |
| SSD-4 | UC-PRK-15 Putuskan Perubahan Sesi | Pengaju (pemberitahuan, O) | V1/V2 daring/batal, V3 ditolak, E1 (AB-PRK-01), E2 (AB-PRK-12), E3 (AB-PRK-10) |
| SSD-5 | UC-PRK-23 Catat Evaluasi Survei | — | E1, E2 (AB-PRK-29) |

Kelima SSD adalah use case kunci yang alurnya sudah dirinci di langkah 7. Use case lain cukup tercakup di katalog (bagian 3), seperti contoh Tata Kelola. SSD tambahan tidak menambah operasi baru dan hanya akan memperbanyak halaman.

---

## 3. Katalog operasi

Katalog ini mencakup **semua** use case. Operasi untuk use case tanpa SSD diturunkan dari tabel deskripsi dan pola di expanded use case. **Jenis**: C = command, Q = query. **AB** = aturan yang dicek oleh operasi itu (eksepsi bila dilanggar). (O) = hanya bila KF Pelengkapnya dibangun.

### 3.1 Jadwal dan Sesi (PKG-15)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_pratinjau_impor = pratinjau_impor(periode, dto_baris_jadwal*, tanggal_pertemuan_pertama)` | Q | UC-PRK-03 | AB-PRK-01, 02, 03, 04 | Menghitung 16 tanggal per kelas, bentrok, kelas terkunci, baris salah, dan peringatan kapasitas **tanpa menyimpan** |
| `impor_jadwal(periode, dto_baris_jadwal*, tanggal_pertemuan_pertama, user_id)` | C | UC-PRK-03 | AB-PRK-01, 02, 03, 04 | Membuat Mata Kuliah dan Kelas yang belum ada, lalu 16 Sesi `terjadwal` per kelas; kelas bentrok/terkunci dilewati |
| `dto_ringkasan_jadwal = ringkasan_jadwal(periode)` | Q | UC-PRK-03, 04 | AB-PRK-03 | Dibaca setelah impor; juga menjadi isi dokumen Penetapan Jadwal |
| `dto_konflik* = cek_bentrok(dto_waktu_ruang, kecuali)` | Q | UC-PRK-03, 07, 08, 15 | AB-PRK-01 | Satu query bentrok untuk impor, pemakaian, dan sesi pengganti. `kecuali` = rekaman yang diabaikan (mis. Sesi asal) |
| `dto_sesi_ringkas* = daftar_sesi(filter, user_id)` | Q | UC-PRK-11, 13, 14 | AB-PRK-06 | `filter` ∈ {`kesiapan_hari_ini`, `belum_berjurnal`, `terjadwal_saya`}. Memuat atribut hitung `is_terpublikasi`, `is_ditunda`, `is_terlewat` |
| `dto_status_sesi = status_sesi(sesi)` | Q | UC-PRK-13, 15 | AB-PRK-06 | Dibaca setelah setiap command yang mengubah Sesi |
| `buat_penetapan_jadwal(periode, user_id)` | C | UC-PRK-04 | AB-PRK-05 | Penetapan Jadwal Draf berisi daftar Sesi periode. Pengajuan, berkas bertanda tangan, dan pengesahan memakai operasi Tata Kelola (`ajukan_dokumen`, `terbitkan_dokumen`, `unggah_berkas_ttd`, `sahkan_dokumen`) |
| `dto_penetapan_jadwal = rincian_penetapan_jadwal(periode)` | Q | UC-PRK-04 | — | Rekaman dibaca lewat kunci alami (satu per periode, AB-PRK-05) |
| `dto_laporan_jadwal = laporan_jadwal(filter)` | Q | UC-PRK-10 | AB-PRK-01 | «report»; jadwal terpadu + rekaman konflik |

### 3.2 Versi Modul

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_info_modul = info_modul(mata_kuliah, periode, user_id)` | Q | UC-PRK-05 | AB-PRK-09 | Versi berlaku, riwayat versi, dan apakah pengguna mengampu MK itu |
| `terbitkan_versi_modul(mata_kuliah, periode, dto_versi_modul, user_id)` | C | UC-PRK-05 | AB-PRK-07, 08, 09 | Versi lama menjadi Diganti |
| `dto_versi_modul* = daftar_modul_berlaku(user_id)` | Q | UC-PRK-06 | — | MK yang diampu atau diasistensi pengguna |
| `dto_versi_modul = modul_berlaku(mata_kuliah, tanggal)` | Q | UC-PRK-06, 11, 13 | AB-PRK-07 | Dipakai `form_kesiapan()` dan `konteks_jurnal()` |

### 3.3 Pengajuan: pemakaian lab dan perubahan sesi (pola S2)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `ajukan_pemakaian(dto_pemakaian, user_id)` | C | UC-PRK-07 | AB-PRK-01 | Dicatat laboran atas permintaan pengguna lab |
| `ajukan_perubahan(sesi, dto_perubahan, user_id)` | C | UC-PRK-14 | AB-PRK-12 | Sesi terbaca `is_ditunda` |
| `dto_pengajuan_ringkas* = daftar_pengajuan(filter, user_id)` | Q | UC-PRK-08, 09, 15 | — | `filter` ∈ {`pemakaian_diajukan`, `perubahan_diajukan`, `pengajuan_saya`} |
| `dto_rincian_pengajuan = rincian_pengajuan(pengajuan)` | Q | UC-PRK-07, 08, 09, 14, 15 | — | |
| `putuskan_pengajuan(pengajuan, keputusan, alasan, karena_bentrok, dto_pengganti, user_id)` | C | UC-PRK-08, 15 | AB-PRK-01, 10, 12 | `karena_bentrok` menandai penolakan yang menjadi rekaman konflik (KF-PRK-09; parameter ditambahkan 16 Nov 2026 di langkah 10). `dto_pengganti` hanya untuk perubahan berjenis pindah. Efek per jenis: pemakaian → jadwal terpadu; perubahan → Sesi `batal` + pengganti, atau moda daring |
| `tarik_pengajuan(pengajuan, user_id)` | C | UC-PRK-09 (O) | AB-PRK-11 | |

### 3.4 Kesiapan (PKG-16, 17)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_form_kesiapan = form_kesiapan(sesi)` | Q | UC-PRK-11 | AB-PRK-13, 14 | Butir dihitung dari kategori tetap + Versi Modul berlaku, belum disimpan |
| `keputusan_boleh* = keputusan_tersedia(sesi, dto_hasil_butir*)` | Q | UC-PRK-11 | AB-PRK-15, 16 | Keputusan yang sah untuk hasil butir itu |
| `catat_pemeriksaan(sesi, dto_hasil_butir*, keputusan, user_id)` | C | UC-PRK-11 | AB-PRK-13, 14, 15, 16 | Menyimpan pemeriksaan, butir, dan waktu periksa |
| `dto_pemeriksaan = rincian_pemeriksaan(sesi)` | Q | UC-PRK-11 | AB-PRK-13 | Kunci alami: satu pemeriksaan per Sesi |
| `dto_substitusi* = daftar_substitusi(filter = menunggu_saya, user_id)` | Q | UC-PRK-12 | — | Butir bahan bersubstitusi pada kelas yang diampu dosen |
| `setujui_substitusi(butir, user_id)` | C | UC-PRK-12 | AB-PRK-16 | Hanya dosen kelas Sesi itu |

### 3.5 Pelaksanaan Sesi (PKG-18)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_konteks_jurnal = konteks_jurnal(sesi, user_id)` | Q | UC-PRK-13 | AB-PRK-17 | Identitas Sesi, Versi Modul berlaku, petugas ditugaskan (SDM), jumlah mahasiswa |
| `simpan_jurnal(sesi, dto_jurnal, user_id)` | C | UC-PRK-13 | AB-PRK-18 | Jurnal draf; boleh diulang |
| `dto_rincian_jurnal = rincian_jurnal(sesi)` | Q | UC-PRK-13 | AB-PRK-20 (O) | Kunci alami: satu jurnal per Sesi. Memuat penanda petugas tidak sesuai penugasan |
| `dto_kelengkapan* = cek_kelengkapan_jurnal(sesi)` | Q | UC-PRK-13 | AB-PRK-19 | Dibaca saat eksepsi E3 (CQS: `kirim_jurnal()` tidak mengembalikan daftar kekurangan) |
| `kirim_jurnal(sesi, user_id)` | C | UC-PRK-13 | AB-PRK-17, 19, 20 (O), 21 (O) | Jurnal terkirim; Sesi `terlaksana` |
| `dto_laporan_pelaksanaan = laporan_pelaksanaan(filter)` | Q | UC-PRK-16 (O) | AB-PRK-13–22 | «report» |

### 3.6 Penilaian Individual (PKG-19)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `catat_penilaian_kelas(kelas, dto_penilaian_kelas, user_id)` | C | UC-PRK-17 | AB-PRK-23 | Tautan LeADS per kelas |
| `dto_penilaian_kelas = rincian_penilaian_kelas(kelas)` | Q | UC-PRK-17, 18 | — | Kunci alami: satu per kelas per periode |
| `impor_nilai(kelas, dto_baris_nilai*, user_id)` | C | UC-PRK-18 (O) | AB-PRK-24 | Mengganti seluruh baris kelas; berkas lama tetap di riwayat |
| `dto_status_praktikan* = status_praktikan(kelas)` | Q | UC-PRK-18 (O) | AB-PRK-25 | P1–P4 per NIM |

### 3.7 Kepuasan Pengguna (PKG-20)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `buat_survei(dto_survei, user_id)` | C | UC-PRK-19 | — | Perluasan `survey.survey`, status Draf |
| `simpan_butir_survei(survei, dto_butir_survei*, user_id)` | C | UC-PRK-19 | — | Menyimpan seluruh butir sekaligus |
| `dto_survei = rincian_survei(survei)` | Q | UC-PRK-19, 20, 21 | — | |
| `dto_kelengkapan* = cek_kelengkapan_survei(survei)` | Q | UC-PRK-19, 20 | AB-PRK-26 | Penanda K2 saat menyusun |
| `tetapkan_survei(survei, user_id)` | C | UC-PRK-20 | AB-PRK-26 | Draf → Ditetapkan; tautan isi terbentuk |
| `batalkan_penetapan_survei(survei, user_id)` | C | UC-PRK-21 (O) | AB-PRK-27 | Ditetapkan → Draf |
| `dto_formulir_survei = formulir_survei(token)` | Q | UC-PRK-22 | AB-PRK-28 | **Tanpa `user_id`**: responden anonim (KNF-PRK-04) |
| `kirim_respons(token, dto_jawaban*)` | C | UC-PRK-22 | AB-PRK-28 | **Tanpa `user_id`**; ditangani addon `survey` |
| `dto_survei_ringkas* = daftar_survei(filter, user_id)` | Q | UC-PRK-19–25 | — | `filter` ∈ {`draf`, `ditetapkan`, `siap_dievaluasi`, `siap_dinilai_efektivitas`} |
| `dto_rekap_survei = rekap_survei(survei)` | Q | UC-PRK-23, 25 | — | |
| `catat_evaluasi_survei(survei, kesimpulan_aspek*, dto_rtl*, user_id)` | C | UC-PRK-23 | AB-PRK-29 | Ditetapkan → Dievaluasi. Dinamai `_survei` agar tidak tertukar dengan `catat_evaluasi(sk, …)` Tata Kelola |
| `dto_status_survei = status_survei(survei)` | Q | UC-PRK-20, 21, 23, 24 | AB-PRK-34 | Status dan kriteria tertinggi K1–K4 |
| `dto_banding_rtl* = banding_rtl(survei)` | Q | UC-PRK-24 | AB-PRK-30 | Rerata aspek RTL pada periode ini dan berikutnya |
| `nilai_efektivitas(survei, dto_efektivitas*, user_id)` | C | UC-PRK-24 | AB-PRK-30 | Semua RTL sekaligus; Dievaluasi → Siklus Selesai |
| `dto_laporan_survei = laporan_survei(filter)` | Q | UC-PRK-25 | AB-PRK-29, 30 | «report» |

### 3.8 Status monev dan laporan bukti

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_status_monev = status_monev(periode, tanggal_acuan)` | Q | UC-PRK-26 | AB-PRK-03, 22, 25, 32, 33, 34 | «report» |
| `berkas_laporan = terbitkan_laporan_bukti(periode, tanggal_acuan)` | Q | UC-PRK-27 | — | Menghasilkan PDF tanpa mengubah data, jadi query (sama dengan `terbitkan_dokumen` Tata Kelola) |

### 3.9 Bersama

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `koreksi_rekaman(rekaman, dto_koreksi, user_id)` | C | UC-PRK-11, 13, 17, 23 | AB-PRK-31 | Rekaman bukti tidak dihapus, hanya dikoreksi dan terlacak. Pola sama dengan Tata Kelola |

### 3.10 Pola «CRUDL»

Berlaku untuk `<konsep>` ∈ {`mata_kuliah`, `kelas`} (UC-PRK-01, 02). `pengaturan` (UC-PRK-28) hanya punya `rincian_` dan `ubah_` karena satu rekaman.

| Operasi | Jenis | AB |
|---|---|---|
| `buat_<konsep>(dto_<konsep>, user_id)` | C | Data wajib dan keunikan (expanded use case bagian 5.1) |
| `ubah_<konsep>(rekaman, dto_<konsep>, user_id)` | C | Sama |
| `hapus_<konsep>(rekaman, user_id)` | C | AB-PRK-31 (master yang sudah dirujuk Sesi tidak dihapus) |
| `arsipkan_<konsep>(rekaman, user_id)` | C | AB-PRK-31 (pengganti hapus) |
| `dto_<konsep> = rincian_<konsep>(rekaman)` | Q | — |
| `dto_<konsep>_ringkas* = daftar_<konsep>(filter)` | Q | — |

**Jumlah:** 21 command dan 32 query khusus, ditambah 6 operasi pola «CRUDL» × 2 konsep dan 2 operasi pengaturan.

---

## 4. Kamus DTO

Notasi: `‹…›` = gabungan data, `*` = koleksi, `(O)` = hanya bila KF Pelengkapnya dibangun. Rekaman yang dirujuk (sesi, kelas, periode, personel, …) ditulis dengan namanya saja; di implementasi berupa ID yang tidak terlihat pengguna (§7.3).

### 4.1 Jadwal dan Sesi

| DTO | Isi |
|---|---|
| `dto_baris_jadwal` | ‹kode_mk, nama_mk, prodi, nama_kelas, hari, jam_mulai, jam_selesai, ruang, dosen, jumlah_mahasiswa› (dosen dan jumlah mahasiswa opsional **[KONFIRMASI P2]**) |
| `dto_pratinjau_impor` | ‹kelas*: ‹mata_kuliah, nama_kelas, pola_mingguan, ruang, tanggal_pertemuan*: ‹pertemuan_ke, tanggal, jenis_pertemuan››, melebihi_kapasitas›, konflik*: dto_konflik, kelas_terkunci*, baris_salah*: ‹nomor_baris, kolom, pesan›› |
| `dto_ringkasan_jadwal` | ‹periode, jumlah_mk_baru, jumlah_kelas_baru, jumlah_sesi_terjadwal, kelas_melebihi_kapasitas*› |
| `dto_waktu_ruang` | ‹ruang, tanggal, jam_mulai, jam_selesai› |
| `dto_konflik` | ‹ruang, tanggal, jam_mulai, jam_selesai, rekaman_bentrok, jenis_rekaman (sesi / pemakaian)› |
| `dto_sesi_ringkas` | ‹sesi, mata_kuliah, kelas, pertemuan_ke, jenis_pertemuan, tanggal, jam_mulai, jam_selesai, ruang, moda, is_terpublikasi, is_ditunda, is_terlewat, ada_pemeriksaan, ada_jurnal› |
| `dto_status_sesi` | ‹sesi, state, is_terpublikasi, is_ditunda, is_diganti, sesi_pengganti, waktu_kirim_jurnal, jurnal_terlambat (O)› |
| `dto_penetapan_jadwal` | ‹periode, status, jumlah_sesi, tanggal_sah, pengesah, berkas_ttd› |
| `dto_laporan_jadwal` | ‹periode, jadwal_terpadu*: ‹ruang, tanggal, jam_mulai, jam_selesai, kegiatan, jenis (sesi / pemakaian)›, konflik*: dto_konflik, penolakan_bentrok*› |

### 4.2 Versi Modul

| DTO | Isi |
|---|---|
| `dto_versi_modul` | ‹mata_kuliah, periode, nomor_versi, berkas, tautan_leads, rubrik, software*: ‹nama, versi, berbayar›, bahan*: ‹bahan, jumlah_per_mahasiswa›, tanggal_terbit, status›. `bahan` = master Bahan Core (C-13); nama dan satuan dibaca dari sana (diperbarui 16 Nov 2026 di langkah 9, [KONFIRMASI kelompok]) |
| `dto_info_modul` | ‹mata_kuliah, periode, versi_berlaku: dto_versi_modul, riwayat_versi*: ‹nomor_versi, tanggal_terbit, status›, pengguna_mengampu› |

### 4.3 Pengajuan

| DTO | Isi |
|---|---|
| `dto_pemakaian` | ‹ruang, tanggal, jam_mulai, jam_selesai, keperluan, nama_pemohon, unit_pemohon› |
| `dto_perubahan` | ‹jenis_perubahan (pindah / daring / batal), alasan, usulan_pengganti: dto_waktu_ruang› |
| `dto_pengganti` | `dto_waktu_ruang` untuk Sesi pengganti (boleh berbeda dari usulan) |
| `dto_pengajuan_ringkas` | ‹pengajuan, jenis_pengajuan (pemakaian / perubahan), pengaju, tanggal_ajukan, ringkasan, status› |
| `dto_rincian_pengajuan` | ‹dto_pengajuan_ringkas, sesi_asal: dto_sesi_ringkas, dto_pemakaian atau dto_perubahan, keputusan, alasan_tolak, karena_bentrok (KF-PRK-09, ditambahkan 16 Nov 2026), pemutus, tanggal_putus, sesi_pengganti› |

### 4.4 Kesiapan

| DTO | Isi |
|---|---|
| `dto_form_kesiapan` | ‹sesi: dto_sesi_ringkas, jumlah_mahasiswa, butir*: ‹kategori (stasiun kerja / jaringan / listrik / proyektor / software / bahan), nama, versi_atau_jumlah_dibutuhkan, berbayar›› |
| `dto_hasil_butir` | ‹butir, hasil (baik / diperbaiki / bermasalah), keterangan; stasiun kerja: jumlah_berfungsi; software berbayar: lisensi_sah; bahan: jumlah_tersedia, kondisi (baik / tidak), berlabel, tanggal_kedaluwarsa (bila relevan, KF-PRK-19), bahan_pengganti (master Bahan Core), alasan_substitusi› |
| `dto_pemeriksaan` | ‹sesi, pemeriksa, waktu_periksa, tepat_waktu, keputusan (siap / siap setelah perbaikan / tunda), butir*: dto_hasil_butir, substitusi_menunggu*› |
| `dto_substitusi` | ‹butir, sesi, bahan, bahan_pengganti, alasan_substitusi, status_persetujuan› |

### 4.5 Pelaksanaan Sesi

| DTO | Isi |
|---|---|
| `dto_konteks_jurnal` | ‹sesi: dto_sesi_ringkas, versi_modul_berlaku, petugas_ditugaskan*: ‹personel, peran› (dari Surat Tugas SDM yang disahkan dan berlaku pada tanggal sesi: asisten lewat kelas, laboran lewat ruang; diperjelas 16 Nov 2026 di langkah 9), jumlah_mahasiswa, berasisten› |
| `dto_jurnal` | ‹jam_mulai_aktual, jam_selesai_aktual, topik, versi_modul_dipakai, jumlah_hadir, tautan_presensi_simpel, kendala, foto, presensi*: ‹personel, peran, kehadiran (penuh / sebagian / tidak)›, log_book*: ‹waktu, uraian›› |
| `dto_rincian_jurnal` | ‹dto_jurnal, status (draf / terkirim), waktu_kirim, terlambat (O), petugas_tidak_sesuai* (O)› |
| `dto_kelengkapan` | ‹bagian, keterangan_kurang› (dipakai juga untuk survei) |
| `dto_laporan_pelaksanaan` (O) | ‹kesiapan_per_ruang*: ‹ruang, butir_bermasalah_per_kategori, jumlah_tunda›, keterlaksanaan_per_kelas*: ‹kelas, rencana, terlaksana, memenuhi›› |

### 4.6 Penilaian Individual

| DTO | Isi |
|---|---|
| `dto_penilaian_kelas` | ‹kelas, tautan_leads, keterangan, ada_rubrik (dari Versi Modul), jumlah_baris_nilai (O)› |
| `dto_baris_nilai` (O) | ‹nim, jumlah_tugas_individual, nilai_akhir, ada_umpan_balik, remedial› (**tanpa nama**, AB-PRK-24) |
| `dto_status_praktikan` (O) | ‹nim, p1, p2, p3, p4, lengkap› |

### 4.7 Kepuasan Pengguna

| DTO | Isi |
|---|---|
| `dto_survei` | ‹periode, judul, jenis_responden, populasi, target_response_rate, tanggal_buka, tanggal_tutup› |
| `dto_butir_survei` | ‹urutan, pertanyaan, jenis (skala / terbuka), aspek (alat / bahan / layanan / keselamatan / akses / pengalaman belajar)› |
| `dto_survei_ringkas` | ‹survei, periode, jenis_responden, tanggal_buka, tanggal_tutup, status, status_turunan (belum dibuka / dibuka / ditutup)› |
| `dto_formulir_survei` | ‹judul, butir*: dto_butir_survei› |
| `dto_jawaban` | ‹butir, nilai_skala atau teks› |
| `dto_rekap_survei` | ‹survei, populasi, jumlah_responden, response_rate, target_response_rate, rerata_aspek*: ‹aspek, rerata›, rerata_butir*, jawaban_terbuka*› |
| `dto_rtl` | ‹aspek, prioritas, tindakan, pic, tenggat› |
| `dto_status_survei` | ‹survei, status, kriteria_tertinggi, bukti*: ‹kriteria, rekaman›, kriteria_berikut, sebab_belum_lolos› |
| `dto_banding_rtl` | ‹rtl, aspek, rerata_periode_ini, rerata_periode_berikut› |
| `dto_efektivitas` | ‹rtl, efektif (ya / sebagian / tidak), catatan› |
| `dto_laporan_survei` | ‹dto_rekap_survei, banding_antarperiode*, rtl*: ‹dto_rtl, dto_efektivitas›› |

### 4.8 Status monev, pengaturan, koreksi

| DTO | Isi |
|---|---|
| `dto_status_monev` | ‹periode, tanggal_acuan, persentase*: ‹pkg (15–18), pembagi, pembilang, persentase, skor, tidak_memenuhi*: ‹unit, cek_gagal*››, pkg19: ‹kelas_berbukti, persentase, praktikan_lengkap (O)›, pkg20: ‹kriteria_tertinggi, bukti*›› |
| `dto_mata_kuliah` | ‹kode, nama, prodi› |
| `dto_kelas` | ‹mata_kuliah, periode, nama_kelas, jumlah_mahasiswa, dosen› |
| `dto_pengaturan` | ‹ambang_durasi_persen, batas_hari_jurnal, sesi_daring_sah, batas_lulus› |
| `dto_koreksi` | ‹field yang dikoreksi dengan nilai barunya, alasan_koreksi› |

---

## 5. Keputusan dan catatan

| Keputusan | Alasan |
|---|---|
| **Antarmuka membaca berkas jadwal menjadi `dto_baris_jadwal*`**; operasi menerima baris, bukan berkas | Sama dengan fitur impor bawaan Odoo (`base_import`). V1 (satu kelas manual) memakai operasi yang sama dengan satu baris, jadi tidak perlu operasi kedua. Pembangunannya mudah |
| **`pratinjau_impor()` query, `impor_jadwal()` command** | Pratinjau tidak boleh menyimpan (CQS); laboran melihat bentrok dan kapasitas sebelum Sesi dibuat |
| **`mulai_pemeriksaan()` di langkah 7 dipecah** menjadi `form_kesiapan()` (Q) dan `catat_pemeriksaan()` (C) | Catatan di expanded use case bagian 7: membuat butir sekaligus mengembalikannya melanggar CQS |
| **Satu `cek_bentrok()`** untuk impor, pemakaian, dan Sesi pengganti | AB-PRK-01 sama di empat use case; di langkah 10 menjadi satu method Core/modul |
| **Satu `daftar_pengajuan()` / `rincian_pengajuan()` / `putuskan_pengajuan()`** untuk pemakaian lab dan perubahan sesi | Keduanya mengikuti state machine S2. Di langkah 10 menjadi kandidat *mixin* pengajuan dengan *hook* efek per jenis (Template Method) |
| **Rekaman baru dibaca lewat kunci alami**, mis. `rincian_pemeriksaan(sesi)`, `rincian_jurnal(sesi)` | Command tidak mengembalikan ID (CQS). Satu pemeriksaan dan satu jurnal per Sesi (AB-PRK-13, 17) membuat Sesi menjadi kunci yang cukup. Penyimpangan `create()` Odoo diterima di langkah 10, sama dengan Tata Kelola |
| **Operasi survei responden tanpa `user_id`** | Respons anonim (AB-PRK-28, KNF-PRK-04); dilayani addon `survey` lewat token tautan |
| **`terbitkan_laporan_bukti()` adalah query** | Menghasilkan PDF tanpa mengubah data |
| **Pengesahan jadwal tidak digambar ulang** | Memakai SSD Tata Kelola (UC-01–05) lewat `labfik.approval.mixin` |

---

## 6. Cek silang

### 6.1 Use case → operasi

| UC | Operasi | UC | Operasi |
|---|---|---|---|
| UC-PRK-01, 02 | pola «CRUDL» | UC-PRK-15 | `daftar_pengajuan`, `rincian_pengajuan`, `cek_bentrok`, `putuskan_pengajuan`, `status_sesi` |
| UC-PRK-03 | `pratinjau_impor`, `impor_jadwal`, `ringkasan_jadwal`, `cek_bentrok` | UC-PRK-16 (O) | `laporan_pelaksanaan` |
| UC-PRK-04 | `buat_penetapan_jadwal`, `rincian_penetapan_jadwal`, `ringkasan_jadwal` + operasi Tata Kelola | UC-PRK-17 | `catat_penilaian_kelas`, `rincian_penilaian_kelas` |
| UC-PRK-05 | `info_modul`, `terbitkan_versi_modul` | UC-PRK-18 (O) | `impor_nilai`, `status_praktikan` |
| UC-PRK-06 | `daftar_modul_berlaku`, `modul_berlaku` | UC-PRK-19 | `buat_survei`, `simpan_butir_survei`, `rincian_survei`, `cek_kelengkapan_survei` |
| UC-PRK-07 | `cek_bentrok`, `ajukan_pemakaian`, `rincian_pengajuan` | UC-PRK-20 | `daftar_survei`, `cek_kelengkapan_survei`, `tetapkan_survei`, `status_survei` |
| UC-PRK-08 | `daftar_pengajuan`, `rincian_pengajuan`, `cek_bentrok`, `putuskan_pengajuan` | UC-PRK-21 (O) | `daftar_survei`, `batalkan_penetapan_survei`, `status_survei` |
| UC-PRK-09 (O) | `daftar_pengajuan`, `tarik_pengajuan` | UC-PRK-22 | `formulir_survei`, `kirim_respons` |
| UC-PRK-10 | `laporan_jadwal` | UC-PRK-23 | `daftar_survei`, `rekap_survei`, `catat_evaluasi_survei`, `status_survei` |
| UC-PRK-11 | `daftar_sesi`, `form_kesiapan`, `keputusan_tersedia`, `catat_pemeriksaan`, `rincian_pemeriksaan`, `koreksi_rekaman` | UC-PRK-24 | `daftar_survei`, `banding_rtl`, `nilai_efektivitas`, `status_survei` |
| UC-PRK-12 | `daftar_substitusi`, `setujui_substitusi` | UC-PRK-25 | `laporan_survei` |
| UC-PRK-13 | `daftar_sesi`, `konteks_jurnal`, `simpan_jurnal`, `rincian_jurnal`, `cek_kelengkapan_jurnal`, `kirim_jurnal`, `status_sesi` | UC-PRK-26 | `status_monev` |
| UC-PRK-14 | `daftar_sesi`, `ajukan_perubahan`, `rincian_pengajuan` | UC-PRK-27 | `terbitkan_laporan_bukti` |
| | | UC-PRK-28 | `rincian_pengaturan`, `ubah_pengaturan` |

Setiap use case (28) punya minimal satu operasi.

### 6.2 AB → operasi

Setiap AB-PRK-01–34 dicek oleh minimal satu operasi (kolom "AB" di bagian 3). AB-PRK-06 dibaca lewat `daftar_sesi()` dan `status_sesi()`; AB-PRK-22, 25, 32–34 dihitung oleh `status_monev()`; AB-PRK-31 oleh `koreksi_rekaman()` dan `hapus_<konsep>()`.

### 6.3 Ketidaksesuaian dengan langkah sebelumnya

| Di langkah 7 | Di sini | Alasan |
|---|---|---|
| Calon operasi memakai `_id` (`sesi_id`, `impor_id`) | Rekaman ditulis dengan namanya (`sesi`) | §7.3: ID tidak terlihat pengguna; nama mengikuti contoh Tata Kelola |
| `konfirmasi_impor(impor_id)` | `impor_jadwal(periode, dto_baris_jadwal*, …)` sekali | Tidak perlu rekaman "impor" sementara; stateless (§7.5) |
| `catat_hasil_butir()` + `tetapkan_keputusan()` | Satu `catat_pemeriksaan()` | Hasil butir dan keputusan diserahkan dalam satu sesi kerja; pemeriksaan tidak disimpan setengah jadi |
| `putuskan_perubahan()` | `putuskan_pengajuan()` | Disatukan dengan UC-PRK-08 (pola S2) |
| `catat_evaluasi()` | `catat_evaluasi_survei()` | Menghindari nama yang sama dengan operasi Tata Kelola |

Tidak ada nomor KF, UC, atau AB yang berubah.

---

## 7. Temuan untuk langkah 9 (conceptual model)

Konsep dan atribut yang harus punya tempat di model, diambil dari kamus DTO:

| Kelompok | Konsep kandidat |
|---|---|
| Core (dipakai) | Mata Kuliah, Kelas, Sesi, Ruang, Periode, Personel, Jabatan |
| Jadwal | Penetapan Jadwal (dokumen yang disahkan), Rekaman Konflik **[ASUMSI: cukup dihitung ulang dari data, bukan konsep sendiri; diputuskan di langkah 9]** |
| Modul | Versi Modul, Kebutuhan Software (+ berbayar), Kebutuhan Bahan |
| Pengajuan | Pengajuan (umum) dengan dua jenis: Pemakaian Lab, Perubahan Sesi; Keputusan pengajuan sebagai **konsep kejadian** (§9.3.2) |
| Kesiapan | Pemeriksaan Kesiapan, Butir Pemeriksaan, Substitusi Bahan (+ persetujuan dosen sebagai kejadian) |
| Pelaksanaan | Jurnal Sesi, Presensi Petugas, Entri *Log Book* |
| Penilaian | Penilaian Kelas, Baris Nilai (O) |
| Kepuasan | Survei (perluasan `survey.survey`), Butir Survei + aspek, Respons (addon `survey`), Evaluasi Survei, RTL, Penilaian Efektivitas |
| Pengaturan | Pengaturan Praktikum (satu rekaman) |
| Turunan | `/is_terpublikasi`, `/is_ditunda`, `/is_terlewat`, `/is_diganti`, `/tepat_waktu`, `/terlambat`, `/response_rate`, `/kriteria_tertinggi`, `/persentase` |

---

## 8. Isu terbuka

- [ ] Penyimpangan CQS pada `create()` Odoo diterima, sama dengan Tata Kelola **[USULAN PENULIS]**
- [ ] Rekaman konflik: dihitung ulang atau disimpan sebagai bukti PKG-15 bukti 5? **[KONFIRMASI pembimbing]**
- [ ] Isi berkas jadwal fakultas (dosen, jumlah mahasiswa) **[KONFIRMASI P2]**
