# System Sequence Diagram dan Katalog Operasi Modul SDM & Kompetensi

19 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 8 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 ("sequence diagram"). Katalog operasi dan kamus DTO adalah bahan kerja untuk conceptual model (langkah 9) dan design class diagram (langkah 10).

Diagram: [ssd-sdm.drawio](ssd-sdm.drawio), 10 halaman SSD dan 1 halaman catatan. Dibuat dengan skrip [tools/drawio/sdm/ssd.py](../tools/drawio/sdm/ssd.py), yang fungsi gambar dan gayanya disalin dari `contoh-tata-kelola/ssd.py` versi `main`. Diagram lolos `validate.py` dengan prefiks `sdm-`. Tampilan visual dicek lewat ekspor PNG draw.io saat penyusunan Bab II.

Sumber: [expanded-use-case-sdm.md](expanded-use-case-sdm.md) (alur lengkap, AB-SDM-01–28, pola «CRUDL» dan «report»).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Lifeline `:Aktor`, `:Antarmuka` (*boundary*), `:Kontroler` (*façade controller*). Aktor hanya berkomunikasi dengan antarmuka | §7.2, §7.4 | Semua SSD |
| *System event* dan *system return* berupa informasi, bukan pemanggilan operasi | §7.3 | Panah kepala terbuka dan putus-putus |
| **Command** `op(args)` mengubah data tanpa nilai balik; **query** `dto = op(args)` hanya membaca (CQS) | §7.1, §7.4 | Panah kepala segitiga penuh; kolom "Jenis" di katalog |
| Data majemuk ditulis sebagai `dto_x` dan didefinisikan di kamus; `*` = koleksi; *terpilih* = pilihan dari daftar | §7.3 | Bagian 4 |
| **Stateless**: `user_id` dan rekaman terpilih dikirim ulang ke setiap operasi | §7.5 | Semua operasi yang butuh identitas pengguna |
| Alur alternatif sebagai `opt «exception»` / `opt «variant»`; use case lain sebagai `ref` | §7.6 | Fragmen di setiap SSD |
| Operasi berpola sama disatukan | CLAUDE.md langkah 8 | `daftar_dokumen(filter, …)`, `status_dokumen()`, `cek_kelengkapan()`, pola «CRUDL», `koreksi_rekaman()` |

**Kontroler:** satu *façade controller* untuk modul SDM (§7.4). Di langkah 10, operasi dipetakan ke method model Odoo, bukan ke satu kelas kontroler.

**Rekaman yang baru dibuat.** Setelah command `buat_x()` atau `catat_x()`, SSD membaca rekaman baru dengan `rincian_x(x)`. Di Odoo, `create()` mengembalikan rekaman yang dibuat; ini penyimpangan CQS yang diterima, sama dengan contoh Tata Kelola.

---

## 2. Daftar SSD

| SSD | Use case | Fragmen alternatif |
|---|---|---|
| SSD-1 | UC-SDM-06 Catat Hasil Seleksi Asisten | V1 calon baru, V2 pengecualian, E1 dan E2 (AB-SDM-15) |
| SSD-2 | UC-SDM-07 Susun Surat Tugas | V1 lanjutkan draf, E1 (AB-SDM-01) |
| SSD-3 | UC-SDM-12 Catat Asesmen Keterampilan | V1 belum layak |
| SSD-4 | UC-SDM-13 Susun Otorisasi | V1 dari evaluasi ulang, E1 (AB-SDM-01) |
| SSD-5 | UC-SDM-15 Putuskan Evaluasi Ulang Otorisasi | V1 dicabut → `ref` UC-SDM-28, V2 tetap berlaku, E1 dan E2 (AB-SDM-19) |
| SSD-6 | UC-SDM-17 Susun Rencana Pelatihan | V2 lanjutkan draf, E1 (AB-SDM-01) |
| SSD-7 | UC-SDM-19 Catat Evaluasi Efektivitas Pelatihan | V1 perlu pengembangan, E1 (AB-SDM-23) |
| SSD-8 | UC-SDM-23 Ajukan Dokumen SDM | E1 (AB-SDM-02/03/04), E2 (AB-SDM-01) |
| SSD-9 | UC-SDM-27 Sahkan Dokumen SDM | E1 (AB-SDM-06) → `ref` UC-SDM-25, E2 (AB-SDM-07), E3 (AB-SDM-12) |
| SSD-10 | UC-SDM-22 Lihat Status Monev SDM | — (query saja) |

Varian yang tidak digambar karena tidak menambah operasi: UC-SDM-07 V2 dan UC-SDM-17 V1 (simpan untuk dilanjutkan).

---

## 3. Katalog operasi

Mencakup **semua** use case. Operasi untuk use case tanpa SSD diturunkan dari tabel deskripsi dan pola di expanded use case. Kolom **AB** = aturan yang dicek operasi itu.

### 3.1 Pengesahan dokumen SDM

`dokumen` = Surat Tugas, Otorisasi, atau Rencana Pelatihan.

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_dokumen_ringkas* = daftar_dokumen(filter, user_id)` | Q | UC-SDM-07, 17, 23, 25–28 | — | `filter` ∈ {`draf_saya`, `diajukan`, `disahkan`} + `jenis` |
| `dto_rincian_dokumen = rincian_dokumen(dokumen, user_id)` | Q | UC-SDM-25–28 | — | Ringkasan isi, berkas, riwayat |
| `dto_status = status_dokumen(dokumen)` | Q | Semua yang mengubah status | — | |
| `dto_kelengkapan* = cek_kelengkapan(dokumen)` | Q | UC-SDM-07, 13, 17, 23 | AB-SDM-02, 03, 04 | Isi pemeriksaan berbeda per jenis |
| `dto_personel_ringkas* = daftar_pengesah_berwenang(dokumen)` | Q | UC-SDM-27 | AB-SDM-07 | |
| `ajukan_dokumen(dokumen, user_id)` | C | UC-SDM-23 | AB-SDM-01–04, 11 | Draf → Diajukan; rencana: kebutuhan dibekukan |
| `berkas_pdf = terbitkan_dokumen(dokumen, user_id)` | Q | UC-SDM-24 (O) | — | Surat Tugas dan Rencana Pelatihan saja |
| `unggah_berkas_ttd(dokumen, berkas_ttd, user_id)` | C | UC-SDM-25 | AB-SDM-05, 11 | |
| `kembalikan_dokumen(dokumen, alasan, user_id)` | C | UC-SDM-26 | AB-SDM-08, 09, 11 | Diajukan → Draf |
| `sahkan_dokumen(dokumen, pengesah, tanggal_sah, user_id)` | C | UC-SDM-27 | AB-SDM-06, 07, 08, 10, 11, 12 | Diajukan → Disahkan; dokumen lama → Diganti |
| `cabut_dokumen(dokumen, alasan, user_id)` | C | UC-SDM-28 | AB-SDM-08, 09, 11 | Disahkan → Dicabut |

### 3.2 Pola «CRUDL»

Berlaku untuk `<konsep>` ∈ {`kompetensi`, `syarat_jabatan`, `bukti_kompetensi`, `tugas_khusus`} (UC-SDM-01, 02, 03, 11).

| Operasi | Jenis | AB |
|---|---|---|
| `buat_<konsep>(dto_<konsep>, user_id)` | C | Validasi data wajib |
| `ubah_<konsep>(rekaman, dto_<konsep>, user_id)` | C | Bukti kompetensi: lewat `koreksi_rekaman()` (AB-SDM-24) |
| `hapus_<konsep>(rekaman, user_id)` | C | AB-SDM-25; bukti kompetensi tidak dihapus (AB-SDM-24) |
| `arsipkan_<konsep>(rekaman, user_id)` | C | Kompetensi, Tugas/Alat (AB-SDM-25) |
| `dto_<konsep> = rincian_<konsep>(rekaman)` | Q | — |
| `dto_<konsep>_ringkas* = daftar_<konsep>(filter)` | Q | — |

`syarat_jabatan` adalah daftar kompetensi wajib pada satu jabatan: `ubah_syarat_jabatan(jabatan, kompetensi*, user_id)`. Pelaksana tugas/alat disimpan bersama tugas/alat lewat `dto_tugas_khusus` (koleksi di dalam DTO).

### 3.3 Rekaman bukti dan data Core

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `koreksi_rekaman(rekaman, dto_koreksi, alasan, user_id)` | C | UC-SDM-03, 05, 06, 09, 12, 14, 18, 19 | AB-SDM-24 | Satu operasi koreksi untuk semua rekaman bukti; terlacak |
| `dto_personel_ringkas* = daftar_personel(filter)` | Q | UC-SDM-06, 07, 13, 17 | — | Membaca Personel Core; `filter` ∈ {`aktif`, `asisten`, `laboran_plp`} |
| `dto_matriks = matriks_kompetensi(tanggal_acuan, filter)` | Q | UC-SDM-04 | AB-SDM-13 | «report» |

### 3.4 Penugasan petugas (PKG-04)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_kebutuhan_kelas* = daftar_kebutuhan_petugas(periode)` | Q | UC-SDM-05 | — | Kelas periode itu beserta kebutuhannya |
| `tetapkan_kebutuhan_petugas(kelas, dto_kebutuhan*, user_id)` | C | UC-SDM-05 | AB-SDM-14 | Satu baris per peran |
| `dto_seleksi_ringkas* = daftar_seleksi(periode, mata_kuliah)` | Q | UC-SDM-06 | — | |
| `catat_seleksi(dto_seleksi, user_id)` | C | UC-SDM-06 | AB-SDM-15 | Membuat Personel asisten bila perlu |
| `buat_surat_tugas(dto_surat_baru, user_id)` | C | UC-SDM-07 | — | Surat Draf |
| `simpan_baris_penugasan(surat, dto_penugasan*, user_id)` | C | UC-SDM-07 | AB-SDM-01, 16 | Mengganti seluruh baris surat Draf |
| `dto_surat = rincian_surat_tugas(surat)` | Q | UC-SDM-07, 08 | — | Termasuk kelas, kebutuhan, ruang |
| `buat_revisi_surat_tugas(surat, user_id)` | C | UC-SDM-08 (O) | — | Menyalin baris ke surat Draf baru yang tertaut |
| `catat_orientasi(dto_orientasi, user_id)` | C | UC-SDM-09 (O) | — | |
| `dto_petugas_sesi* = daftar_petugas_sesi(periode)` | Q | UC-SDM-10 | AB-SDM-26 | «report» |

### 3.5 Otorisasi (PKG-10)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_tugas_khusus_ringkas* = daftar_tugas_khusus(filter)` | Q | UC-SDM-12, 13 | — | Bentuk khusus `daftar_<konsep>` |
| `catat_asesmen(tugas_khusus, dto_asesmen, user_id)` | C | UC-SDM-12 | AB-SDM-17 | *Layak* → bukti kompetensi demonstrasi |
| `dto_asesmen = rincian_asesmen(asesmen)` | Q | UC-SDM-12 | — | |
| `buat_otorisasi(personel, tugas_khusus, user_id)` | C | UC-SDM-13 | AB-SDM-18 | Otorisasi Draf, masa berlaku awal |
| `buat_otorisasi_dari_evaluasi(evaluasi, user_id)` | C | UC-SDM-13 V1 | — | Menyalin personel, tugas/alat, lingkup |
| `ubah_otorisasi(otorisasi, dto_otorisasi, user_id)` | C | UC-SDM-13 | AB-SDM-01 | |
| `dto_otorisasi = rincian_otorisasi(otorisasi)` | Q | UC-SDM-13 | — | Termasuk dasar dan calon supervisor |
| `catat_pemicu(otorisasi, dto_pemicu, user_id)` | C | UC-SDM-14 | AB-SDM-19 | Evaluasi Terbuka |
| `dto_evaluasi_ringkas* = daftar_evaluasi(filter, user_id)` | Q | UC-SDM-14, 15 | — | `filter` ∈ {`terbuka`, `semua`} |
| `putuskan_evaluasi(evaluasi, dto_keputusan, user_id)` | C | UC-SDM-15 | AB-SDM-19 | Terbuka → Diputuskan |
| `dto_evaluasi = rincian_evaluasi(evaluasi)` | Q | UC-SDM-15 | — | Termasuk tindak lanjut |
| `dto_operator* = daftar_operator_sah(tanggal_acuan, tugas_khusus)` | Q | UC-SDM-16 | AB-SDM-18 | «report» |

### 3.6 Pelatihan (PKG-14)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `buat_rencana_pelatihan(dto_rencana_baru, user_id)` | C | UC-SDM-17 | AB-SDM-20 | Rencana Draf dengan kebutuhan terisi awal |
| `simpan_kebutuhan(rencana, dto_kebutuhan_pelatihan*, user_id)` | C | UC-SDM-17 | AB-SDM-01 | |
| `simpan_item_pelatihan(rencana, dto_item_pelatihan*, user_id)` | C | UC-SDM-17 | AB-SDM-01 | |
| `dto_rencana = rincian_rencana_pelatihan(rencana)` | Q | UC-SDM-17, 18 | — | |
| `dto_kompetensi_ringkas* = daftar_kompetensi(filter)` | Q | UC-SDM-17 | — | Bentuk khusus `daftar_<konsep>` |
| `dto_item_ringkas* = daftar_item_pelatihan(filter, user_id)` | Q | UC-SDM-18, 20 | — | `filter` ∈ {`siap_realisasi`, `rencana`} |
| `catat_realisasi(item, dto_realisasi, user_id)` | C | UC-SDM-18 | AB-SDM-21 | Item → terlaksana |
| `batalkan_item(item, alasan, user_id)` | C | UC-SDM-20 (O) | AB-SDM-22 | |
| `dto_realisasi_ringkas* = daftar_realisasi(filter, user_id)` | Q | UC-SDM-19 | — | `filter` ∈ {`belum_dievaluasi`, `semua`} |
| `dto_realisasi = rincian_realisasi(realisasi)` | Q | UC-SDM-18, 19 | — | Termasuk evaluasi dan bukti yang terbentuk |
| `catat_evaluasi_efektivitas(realisasi, dto_evaluasi_pelatihan, user_id)` | C | UC-SDM-19 | AB-SDM-23 | *Efektif* → bukti kompetensi pelatihan |
| `dto_rekap = rekap_pelatihan(personel, periode)` | Q | UC-SDM-21 (O) | — | «report» |

### 3.7 Status monev

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_status_monev = status_monev(periode, tanggal_acuan)` | Q | UC-SDM-22 | AB-SDM-26–28 | «report» |
| `dto_unit_monev = rincian_unit_monev(unit, tanggal_acuan)` | Q | UC-SDM-22 | AB-SDM-26–28 | Syarat per unit dan tautan bukti |
| `berkas_pdf = laporan_bukti(periode, tanggal_acuan)` | Q | UC-SDM-22 | — | PDF untuk penilai, termasuk rekaman pendukung (KU-3) |

**Jumlah:** 23 command dan 28 query khusus, ditambah 6 operasi pola «CRUDL» × 4 konsep.

---

## 4. Kamus DTO

Notasi: `‹…›` = gabungan data, `*` = koleksi, `(O)` = Pelengkap. Rekaman yang dirujuk ditulis dengan namanya saja; di implementasi berupa ID yang tidak terlihat pengguna (§7.3).

### 4.1 Pengesahan

| DTO | Isi |
|---|---|
| `dto_dokumen_ringkas` | ‹dokumen, jenis_dokumen, nomor_atau_judul, periode_atau_personel, status, penyusun, tanggal_ajukan, ada_berkas_ttd, tanggal_ubah› |
| `dto_rincian_dokumen` | ‹dto_dokumen_ringkas, ringkasan_isi, berkas_ttd, riwayat*: dto_riwayat› |
| `dto_riwayat` | ‹kejadian, waktu, pelaku, pengesah, alasan, berkas› |
| `dto_status` | ‹dokumen, status, tanggal_ajukan, tanggal_sah, pengesah, pencatat, dokumen_diganti› |
| `dto_kelengkapan` | ‹bagian, pesan› (satu baris per kekurangan; kosong = lengkap) |
| `dto_personel_ringkas` | ‹personel, nama, jenis_personel, jabatan› |

### 4.2 Kompetensi

| DTO | Isi |
|---|---|
| `dto_kompetensi` | ‹nama, jenis, kode_acuan, keterangan› |
| `dto_bukti_kompetensi` | ‹personel, kompetensi, jenis_bukti, nomor_dokumen, penerbit, tanggal, berlaku_sampai, berkas*, /berlaku› |
| `dto_matriks` | ‹tanggal_acuan, baris*: ‹personel, jabatan, sel*: ‹kompetensi, penanda (berlaku / kedaluwarsa / kurang)››› |
| `dto_koreksi` | ‹field*, nilai_baru*› |

### 4.3 Penugasan

| DTO | Isi |
|---|---|
| `dto_kebutuhan_kelas` | ‹kelas, mata_kuliah, kebutuhan*: dto_kebutuhan› |
| `dto_kebutuhan` | ‹peran, jumlah_minimal, dasar_penetapan, berkas*› |
| `dto_seleksi` | ‹personel atau nama_calon, mata_kuliah, periode, nilai_mk, skor_wawancara, skor_simulasi, skor_modul, penilai, tanggal, keputusan, alasan_pengecualian, penyetuju, berkas*› |
| `dto_seleksi_ringkas` | ‹seleksi, personel, nama, keputusan, tanggal› |
| `dto_surat_baru` | ‹nomor, periode› |
| `dto_surat` | ‹surat, nomor, periode, status, baris*: dto_penugasan, kelas*: dto_kebutuhan_kelas, ruang*, berkas_komitmen (O), revisi_dari (O)› |
| `dto_penugasan` | ‹personel, peran, kelas, ruang, berlaku_mulai, berlaku_sampai› |
| `dto_orientasi` (O) | ‹personel, jenis, pelaksana, tanggal, keterangan, berkas*› |
| `dto_petugas_sesi` | ‹sesi, tanggal, kelas, ruang, kebutuhan*, petugas*: dto_personel_ringkas, s1, s2, s3, s4, syarat_gagal*› |

### 4.4 Otorisasi

| DTO | Isi |
|---|---|
| `dto_tugas_khusus` | ‹nama, jenis, lokasi, kompetensi*, masa_berlaku_bulan, pelaksana*, cara_pembatasan (O), berkas_pembatasan (O)› |
| `dto_tugas_khusus_ringkas` | ‹tugas_khusus, nama, jenis, kompetensi*, jumlah_pelaksana› |
| `dto_asesmen` | ‹personel, penilai, metode, skor, unsur_kritis_terpenuhi, kesimpulan, catatan_pengembangan, tanggal, berkas*, bukti_kompetensi*: dto_bukti_kompetensi› |
| `dto_otorisasi` | ‹otorisasi, personel, tugas_khusus, status, dasar_asesmen, dasar_bukti*, lingkup, level, supervisor, berlaku_mulai, berlaku_sampai, /berlaku, calon_supervisor*: dto_personel_ringkas› |
| `dto_pemicu` | ‹pemicu, tanggal, keterangan› |
| `dto_evaluasi_ringkas` | ‹evaluasi, personel, tugas_khusus, pemicu, tanggal, berlaku_sampai_otorisasi, status› |
| `dto_keputusan` | ‹keputusan, hasil, penilai, tanggal_keputusan› |
| `dto_evaluasi` | ‹dto_evaluasi_ringkas, dto_keputusan, tindak_lanjut, otorisasi_baru› |
| `dto_operator` | ‹tugas_khusus, personel, level, supervisor, berlaku_sampai› |

### 4.5 Pelatihan

| DTO | Isi |
|---|---|
| `dto_rencana_baru` | ‹judul, periode› |
| `dto_rencana` | ‹rencana, judul, periode, status, kebutuhan_dibekukan, kebutuhan*: dto_kebutuhan_pelatihan, item*: dto_item_pelatihan› |
| `dto_kebutuhan_pelatihan` | ‹personel, kompetensi, tidak_ada_gap, sumber, keterangan› |
| `dto_item_pelatihan` | ‹kompetensi_sasaran, jenis, materi, peserta*, penyelenggara, anggaran, jadwal_mulai, jadwal_selesai, kriteria_keberhasilan, status, alasan_batal (O), /status_evaluasi› |
| `dto_item_ringkas` | ‹item, rencana, kompetensi_sasaran, jadwal, peserta*, status› |
| `dto_realisasi` | ‹item, peserta, tanggal, penyelenggara, durasi_jam, berkas_sertifikat, bukti_penerapan*, evaluasi: dto_evaluasi_pelatihan› |
| `dto_realisasi_ringkas` | ‹realisasi, peserta, item, kompetensi_sasaran, tanggal, kriteria_keberhasilan› |
| `dto_evaluasi_pelatihan` | ‹metode, skor_sebelum, skor_sesudah, penilai, kesimpulan, peningkatan_layanan, tindak_lanjut, tanggal, berkas*, bukti_kompetensi› |
| `dto_rekap` (O) | ‹personel, periode, kebutuhan*, item*, realisasi*, evaluasi*, bukti_kompetensi*› |

### 4.6 Status monev

| DTO | Isi |
|---|---|
| `dto_status_monev` | ‹periode, tanggal_acuan, pkg04: dto_persentase, pkg10: dto_persentase, pkg14: dto_kriteria› |
| `dto_persentase` | ‹pembagi, pembilang, persentase, skor, unit_gagal*: ‹unit, syarat_gagal*›› |
| `dto_kriteria` | ‹rencana, kriteria_tertinggi, kriteria_berikutnya, sebab_belum_lolos, tautan_bukti*› |
| `dto_unit_monev` | ‹unit, jenis_unit (sesi / pasangan / kriteria), syarat*: ‹kode, lolos, keterangan, tautan_bukti*›› |

---

## 5. Cek silang

| Cek | Hasil |
|---|---|
| Setiap use case punya operasi | ✓ UC-SDM-01–28 (bagian 3) |
| Setiap langkah aktor di alur lengkap = satu *system event* dengan command atau query | ✓ SSD-1–9 |
| Setiap eksepsi E merujuk AB dan punya fragmen | ✓ |
| Setiap AB dicek oleh minimal satu operasi | ✓ AB-SDM-01–28; AB-SDM-13 di `matriks_kompetensi`, `status_monev`, dan `buat_rencana_pelatihan` |
| CQS | ✓ Command tanpa nilai balik; `terbitkan_dokumen` dan `laporan_bukti` adalah query karena tidak mengubah data |
| Stateless | ✓ `user_id` di setiap operasi yang membutuhkan identitas pengguna |

**Temuan untuk langkah 9:** setiap isi kamus DTO harus punya tempat di conceptual model. Atribut turunan (`/berlaku`, `/status_evaluasi`, `s1`–`s4`, `persentase`, `kriteria_tertinggi`) dimodelkan sebagai atribut turunan, bukan disimpan.
