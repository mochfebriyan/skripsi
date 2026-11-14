# System Sequence Diagram dan Katalog Operasi Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 8 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 ("sequence diagram"). Katalog operasi dan kamus DTO adalah bahan kerja untuk conceptual model (langkah 9) dan design class diagram (langkah 10).

Diagram: [ssd-tata-kelola.drawio](ssd-tata-kelola.drawio), 8 halaman (SSD-1 s.d. SSD-8). Dibuat dengan skrip [ssd.py](../tools/drawio/contoh-tata-kelola/ssd.py) dan lolos `validate.py` dengan prefiks `tk-`. **Tampilan visual belum dicek di draw.io.**

Sumber: [expanded-use-case-tata-kelola.md](expanded-use-case-tata-kelola.md) (alur lengkap, AB-01–25, pola «CRUDL» dan «report»).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Lifeline `:Aktor`, `:Antarmuka` (*boundary*), `:Kontroler` (*façade controller*). Aktor hanya berkomunikasi dengan antarmuka | §7.2, §7.4 | Semua SSD |
| *System event* (aktor → antarmuka) dan *system return* (antarmuka → aktor) berupa informasi, bukan pemanggilan operasi | §7.3 | Panah hitam penuh dan putus-putus |
| **Command** `op(args)` mengubah data dan tidak mengembalikan nilai; **query** `dto = op(args)` hanya membaca (CQS) | §7.1, §7.4 | Panah ungu; kolom "Jenis" di katalog |
| Data majemuk lebih dari tiga elemen ditulis sebagai `dto_x` dan didefinisikan di kamus; `*` = koleksi; *terpilih* = pilihan dari daftar | §7.3 | Bagian 4 |
| **Stateless**: kontroler tidak mengingat apa pun di antara operasi; `user_id` dan rekaman terpilih dikirim ulang ke setiap operasi | §7.5 | Semua operasi yang butuh identitas pengguna |
| Alur alternatif sebagai `opt «exception»` / `opt «variant»`; use case lain sebagai `ref` | §7.6 | Fragmen di setiap SSD |
| Operasi berpola sama disatukan | CLAUDE.md langkah 8 | `daftar_dokumen(filter, …)`, `cek_kelengkapan()`, pola «CRUDL» |

**Kontroler:** satu *façade controller* per modul (§7.4, subpola pertama), karena modul ini kecil. Di langkah 10, operasi dipetakan ke method model Odoo, bukan ke satu kelas kontroler.

---

## 2. Daftar SSD

| SSD | Use case | Fragmen alternatif |
|---|---|---|
| SSD-1 | UC-01 Ajukan Dokumen | E1 (AB-02), E2 (AB-01), E3 (O, AB-12) |
| SSD-2 | UC-03 Unggah Dokumen Bertanda Tangan | V1 ganti berkas, E1 (AB-03) |
| SSD-3 | UC-05 Sahkan Dokumen | E1 (AB-04) → `ref` SSD-2, E2 (AB-05), E3 (O, AB-11) |
| SSD-4 | UC-15 Unggah Versi Dokumen | V1 versi pertama, E1 (AB-13), E2 (O, AB-12) |
| SSD-5 | UC-18 Tinjau Ulang Dokumen | V1 perlu revisi → `ref` SSD-4, E1 (AB-15) |
| SSD-6 | UC-23 Susun Rencana | V1 rencana pengembangan, V3 lanjutkan draf, E1 (AB-01) |
| SSD-7 | UC-25 Isi Realisasi Rencana | V2 koreksi (AB-22), E1 dan E2 (AB-18) |
| SSD-8 | UC-28 Lihat Status Monev | — (query saja) |

Varian yang tidak digambar karena tidak menambah operasi: UC-23 V2 (simpan untuk dilanjutkan; tidak ada operasi baru) dan UC-25 V1 (KaLab mengisi untuk PIC lain; operasinya sama).

---

## 3. Katalog operasi

Katalog ini mencakup **semua** use case. Operasi untuk use case tanpa SSD diturunkan dari tabel deskripsi dan pola di expanded use case. Kolom **AB** = aturan yang dicek oleh operasi itu (eksepsi bila dilanggar).

### 3.1 Pengesahan (dipakai semua dokumen)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_dokumen_ringkas* = daftar_dokumen(filter, user_id)` | Q | UC-01, 03, 04, 05, 06 | — | `filter` ∈ {`draf_saya`, `diajukan`, `disahkan`}, ditambah jenis dokumen. Satu query untuk semua daftar dokumen |
| `dto_rincian_dokumen = rincian_dokumen(dokumen, user_id)` | Q | UC-03, 04, 05, 06 | — | Isi ringkas, berkas, riwayat |
| `dto_status = status_dokumen(dokumen)` | Q | Semua yang mengubah status | — | Dibaca setelah setiap command |
| `dto_kelengkapan* = cek_kelengkapan(dokumen)` | Q | UC-01 E1, UC-23 | AB-02 | Juga dipakai saat menyusun rencana untuk menampilkan penanda kelengkapan |
| `dto_personel_ringkas* = daftar_pengesah_berwenang(dokumen)` | Q | UC-05 | AB-05 | Personel yang jabatannya berwenang mengesahkan jenis dokumen itu |
| `ajukan_dokumen(dokumen, user_id)` | C | UC-01 | AB-01, 02, 09, 12 (O) | Draf → Diajukan |
| `berkas_resmi = terbitkan_dokumen(dokumen, user_id)` | Q | UC-02 | — | Menghasilkan PDF format lab. Tidak mengubah data, jadi query |
| `unggah_berkas_ttd(dokumen, berkas_ttd, user_id)` | C | UC-03 | AB-03, 09 | Mengganti berkas bila sudah ada |
| `kembalikan_dokumen(dokumen, alasan, user_id)` | C | UC-04 | AB-06, 07, 09 | Diajukan → Draf |
| `sahkan_dokumen(dokumen, pengesah, tanggal_sah, user_id)` | C | UC-05 | AB-04, 05, 06, 08, 09, 11 (O), 14 | Diajukan → Disahkan; dokumen lama → Diganti; tanggal tinjau dihitung |
| `cabut_dokumen(dokumen, alasan, user_id)` | C | UC-06 | AB-06, 07, 09 | Disahkan → Dicabut |
| `kedaluwarsakan_dokumen(tanggal)` | C | UC-07 (O) | AB-09, 10 | Dipanggil Penjadwal; tanpa `user_id` |

### 3.2 Pola «CRUDL»

Berlaku untuk `<konsep>` ∈ {`personel`, `jabatan`, `dokumen_induk`, `kpi`, `renstra`} (UC-08, 09, 14, 21, 22).

| Operasi | Jenis | AB |
|---|---|---|
| `buat_<konsep>(dto_<konsep>, user_id)` | C | Validasi data wajib (expanded use case bagian 5.1) |
| `ubah_<konsep>(rekaman, dto_<konsep>, user_id)` | C | AB-01 (khusus Renstra) |
| `hapus_<konsep>(rekaman, user_id)` | C | AB-23; AB-01 (Renstra) |
| `arsipkan_<konsep>(rekaman, user_id)` | C | AB-23 (pengganti hapus bila sudah dirujuk) |
| `dto_<konsep> = rincian_<konsep>(rekaman)` | Q | — |
| `dto_<konsep>_ringkas* = daftar_<konsep>(filter)` | Q | — |

Jabatan juga punya anak tugas dan wewenang. Keduanya disimpan bersama jabatan lewat `dto_jabatan` (koleksi di dalam DTO), bukan operasi terpisah.

### 3.3 Struktur organisasi (PKG-03)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `buat_sk(dto_sk, user_id)` | C | UC-10 | — | SK Draf; bila revisi, `dto_sk.revisi_dari` diisi |
| `simpan_baris_penetapan(sk, dto_baris_penetapan*, user_id)` | C | UC-10 | AB-01 | Mengganti seluruh baris SK Draf |
| `dto_sk = rincian_sk(sk)` | Q | UC-10, 12 | — | |
| `catat_rapat(dto_rapat, user_id)` | C | UC-11 | — | |
| `catat_evaluasi(sk, dto_evaluasi, user_id)` | C | UC-12 | — | |
| `tautkan_revisi_evaluasi(evaluasi, sk_revisi, jabatan_direvisi*, user_id)` | C | UC-12 | — | Boleh dilakukan kemudian |
| `koreksi_rekaman(rekaman, dto_koreksi, user_id)` | C | UC-11, 12, 16, 17, 26 | AB-22 | Satu operasi koreksi untuk semua rekaman bukti; koreksinya terlacak. Tinjau ulang tidak dikoreksi (AB-22) |
| `dto_laporan_struktur = laporan_struktur(tanggal_acuan)` | Q | UC-13 | — | «report» |

### 3.4 Pengendalian dokumen SOP/IK (PKG-02)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_dokumen_induk_ringkas* = daftar_dokumen_induk(filter, user_id)` | Q | UC-15, 14 | — | Bentuk khusus `daftar_<konsep>` |
| `dto_info_versi = info_versi(dokumen_induk)` | Q | UC-15 | — | |
| `buat_versi(dokumen_induk, dto_versi_baru, user_id)` | C | UC-15 | AB-12 (O), 13 | Versi Draf |
| `dto_versi = rincian_versi(dokumen_induk, revisi)` | Q | UC-15 | — | Rekaman baru dibaca lewat kunci alami (Dokumen Induk + revisi), lihat bagian 5 |
| `catat_distribusi(versi, dto_distribusi*, user_id)` | C | UC-16 | AB-15, 16 | Satu atau lebih lokasi sekaligus |
| `catat_sosialisasi(versi, dto_sosialisasi, user_id)` | C | UC-17 | AB-15 | Minimal satu peserta |
| `dto_versi_berlaku* = daftar_versi_berlaku(filter, user_id)` | Q | UC-16, 17, 18, 19 | AB-14, 17 (O) | Diurutkan dari tanggal tinjau paling lama terlewati |
| `catat_tinjau_ulang(versi, dto_tinjau, user_id)` | C | UC-18 | AB-14, 15 | Memperbarui tanggal tinjau bila hasil *tetap berlaku* |
| `dto_status_tinjau = status_tinjau(versi)` | Q | UC-18 | AB-14 | |
| `berkas = baca_dokumen_berlaku(dokumen_induk, user_id)` | Q | UC-19 (O) | AB-17 | |
| `dto_laporan_dokumen = laporan_pengendalian_dokumen(filter)` | Q | UC-20 | AB-14 | «report» |

### 3.5 Rencana (PKG-01, PKG-13)

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `buat_rencana(dto_rencana_baru, user_id)` | C | UC-23 | — | Rencana Draf, jenis tahunan atau pengembangan |
| `simpan_temuan_gap(rencana, dto_gap*, user_id)` | C | UC-23 V1 | AB-01 | Hanya rencana pengembangan |
| `simpan_item_rencana(rencana, dto_item*, user_id)` | C | UC-23 | AB-01, 21 (O) | Prioritas dihitung bila AB-21 dibangun |
| `dto_rencana = rincian_rencana(rencana)` | Q | UC-23, 24, 26 | — | |
| `dto_rencana_ringkas* = daftar_rencana(filter, user_id)` | Q | UC-23 V3, 24, 26 | — | `filter` ∈ {`draf_saya`, `disahkan`, `pernah_disahkan`} |
| `buat_revisi_rencana(rencana, user_id)` | C | UC-24 (O) | — | Menyalin isi ke rencana Draf baru yang tertaut |
| `dto_item_pic* = daftar_item_pic(user_id)` | Q | UC-25 | — | Item dari rencana Disahkan; KaLab melihat semua |
| `catat_realisasi(item, dto_realisasi, user_id)` | C | UC-25 | AB-18 | |
| `koreksi_realisasi(realisasi, dto_realisasi, user_id)` | C | UC-25 V2 | AB-22 | Bentuk khusus `koreksi_rekaman` |
| `dto_capaian = capaian_item(item)` | Q | UC-25 | — | |
| `catat_tinjauan(rencana, dto_tinjauan, user_id)` | C | UC-26 | AB-19, 20 | Termasuk ukuran manfaat untuk rencana pengembangan |
| `tautkan_rencana_berikutnya(tinjauan, rencana_berikut, user_id)` | C | UC-26 | AB-19 | Boleh dilakukan kemudian |
| `dto_laporan_rencana = laporan_rencana(rencana, periode_lapor)` | Q | UC-27 | — | «report» |

### 3.6 Status monev

| Operasi | Jenis | UC | AB | Keterangan |
|---|---|---|---|---|
| `dto_status_monev = status_monev(tanggal_acuan)` | Q | UC-28 | AB-24, 25 | «report» |

**Jumlah:** 24 command dan 21 query khusus, ditambah 6 operasi pola «CRUDL» × 5 konsep.

---

## 4. Kamus DTO

Notasi: `‹…›` = gabungan data, `*` = koleksi, `(O)` = hanya bila KF Pelengkapnya dibangun. Rekaman yang dirujuk (dokumen, versi, rencana, item, personel, …) ditulis dengan namanya saja; di implementasi berupa ID yang tidak terlihat pengguna (§7.3).

### 4.1 Pengesahan

| DTO | Isi |
|---|---|
| `dto_dokumen_ringkas` | ‹dokumen, jenis_dokumen, judul, periode, status, penyusun, tanggal_ajukan, ada_berkas_ttd, tanggal_ubah› |
| `dto_rincian_dokumen` | ‹dto_dokumen_ringkas, ringkasan_isi, berkas_ttd, riwayat*: dto_riwayat› |
| `dto_riwayat` | ‹kejadian, waktu, pelaku, pengesah, alasan, berkas› |
| `dto_status` | ‹dokumen, status, tanggal_ajukan, tanggal_sah, pengesah, pencatat, dokumen_diganti, tanggal_tinjau_berikutnya› |
| `dto_kelengkapan` | ‹bagian, keterangan_kurang› |
| `dto_personel_ringkas` | ‹personel, nama, jenis_personel, jabatan, unit› |

### 4.2 Struktur organisasi

| DTO | Isi |
|---|---|
| `dto_personel` | ‹nama, jenis_personel, unit, jabatan, akun_pengguna› |
| `dto_jabatan` | ‹nama, unit, is_eksternal, atasan, pengganti, syarat_kompetensi, tugas*: ‹urutan, uraian›, wewenang*: ‹tindakan, jenis_dokumen›› |
| `dto_sk` | ‹nomor_sk, judul, periode, menimbang, mengingat, revisi_dari› |
| `dto_baris_penetapan` | ‹personel, jabatan, ruang*, tanggal_mulai, tanggal_selesai› |
| `dto_rapat` | ‹tanggal, agenda, peserta*, keputusan, notulen› |
| `dto_evaluasi` | ‹tanggal, temuan_beban_kerja, efektivitas_koordinasi, keputusan, struktur_diubah› |
| `dto_koreksi` | ‹field yang dikoreksi dengan nilai barunya, alasan_koreksi› |
| `dto_laporan_struktur` | ‹tanggal_acuan, hierarki*: ‹jabatan, atasan, tingkat, pemegang*›, tugas*: ‹jabatan, uraian*›, matriks*: ‹jabatan, tindakan, jenis_dokumen›› |

### 4.3 Pengendalian dokumen SOP/IK

| DTO | Isi |
|---|---|
| `dto_dokumen_induk` | ‹kode, judul, jenis, kategori, asal, is_wajib, dasar_kebutuhan, tanggal_ditetapkan_wajib, lokasi_penggunaan*, siklus_tinjau› |
| `dto_dokumen_induk_ringkas` | ‹dokumen_induk, kode, judul, jenis, revisi_berlaku, perlu_ditinjau› |
| `dto_info_versi` | ‹dokumen_induk, revisi_berlaku, revisi_berikutnya, riwayat_revisi*: ‹revisi, tanggal_sah, ringkasan_perubahan›, versi_dalam_proses› |
| `dto_versi_baru` | ‹berkas, revisi, tanggal_efektif, bagian_diubah, ringkasan_perubahan, alasan_revisi› |
| `dto_versi` | ‹versi, dokumen_induk, revisi, tanggal_efektif, status› |
| `dto_versi_berlaku` | ‹versi, kode, judul, revisi, tanggal_sah, tanggal_tinjau_berikutnya, perlu_ditinjau› |
| `dto_distribusi` | ‹lokasi, tanggal, petugas› |
| `dto_sosialisasi` | ‹tanggal, metode, peserta*, bukti› |
| `dto_tinjau` | ‹tanggal_tinjau, hasil, catatan› |
| `dto_status_tinjau` | ‹versi, tanggal_tinjau_terakhir, hasil_terakhir, tanggal_tinjau_berikutnya, perlu_ditinjau› |
| `dto_laporan_dokumen` | ‹daftar_induk*: ‹dto_dokumen_induk_ringkas, tanggal_sah, pengesah, tanggal_tinjau_berikutnya, lokasi_penggunaan*›, riwayat_revisi*, distribusi*, sosialisasi*, tinjau_ulang*› |

### 4.4 Rencana

| DTO | Isi |
|---|---|
| `dto_kpi` | ‹kode, nama, definisi, rumus_pembilang, rumus_penyebut, satuan, frekuensi, sumber_data› |
| `dto_kpi_ringkas` | ‹kpi, kode, nama, satuan› |
| `dto_renstra` | ‹judul, periode, berkas› |
| `dto_rencana_baru` | ‹jenis_rencana, judul, periode, narasi (O)› |
| `dto_rencana_ringkas` | ‹rencana, jenis_rencana, judul, periode, status› |
| `dto_rencana` | ‹dto_rencana_ringkas, narasi (O), temuan_gap*: dto_gap, item*: dto_item, revisi_dari› |
| `dto_gap` | ‹aspek, kondisi_saat_ini, kebutuhan, sumber_data, uraian_gap, lampiran, tidak_ada_gap, alasan_tidak_ada_gap› |
| `dto_item` | ‹kegiatan, kpi, target, satuan, pic, jadwal_mulai, jadwal_selesai, anggaran, rujukan_renstra; khusus pengembangan: temuan_gap*, nilai_risiko, nilai_manfaat, prioritas› |
| `dto_item_pic` | ‹item, rencana, kegiatan, kpi, target, satuan, jadwal_mulai, jadwal_selesai, realisasi_terakhir› |
| `dto_realisasi` | ‹periode_lapor, capaian, biaya_terpakai, status_capaian, tindak_lanjut, bukti› |
| `dto_capaian` | ‹item, target, capaian_terakhir, realisasi*: ‹periode_lapor, capaian, status_capaian, pelapor, tanggal_lapor›› |
| `dto_tinjauan` | ‹tanggal, peserta*, ringkasan_capaian, keputusan, ukuran_manfaat*: ‹item, indikator, nilai_sebelum, nilai_sesudah, sumber›› |
| `dto_laporan_rencana` | ‹rencana, matriks_keterkaitan*: ‹rujukan_renstra, item*›, pelaksanaan*: ‹item, target, capaian, status_capaian, tindak_lanjut›, tinjauan*: dto_tinjauan› |

### 4.5 Status monev

| DTO | Isi |
|---|---|
| `dto_status_monev` | ‹tanggal_acuan, pkg02: ‹pembagi, pembilang, persentase, skor, tidak_memenuhi*: ‹dokumen_induk, cek_gagal*››, kriteria*: ‹indikator, kriteria_tertinggi, bukti*: ‹kriteria, rekaman›, kriteria_berikut, sebab_belum_lolos›› |

---

## 5. Keputusan dan catatan

| Keputusan | Alasan |
|---|---|
| **Satu query daftar dokumen** dengan `filter` untuk UC-01, 03, 04, 05, 06 | Pola sama, hanya status dan penyusun yang berbeda (CLAUDE.md langkah 8) |
| **`cek_kelengkapan()` sebagai query terpisah** dari `ajukan_dokumen()` | Command tidak boleh mengembalikan data (CQS); daftar kekurangan dibaca lewat query saat eksepsi E1, dan dipakai ulang di UC-23 |
| **`terbitkan_dokumen()` adalah query** | Menghasilkan berkas tanpa mengubah data |
| **Satu operasi `koreksi_rekaman()`** untuk semua rekaman bukti | AB-22 sama untuk semua; di langkah 10 menjadi perilaku *mixin* |
| **Rekaman baru dibaca lewat kunci alami**, mis. `rincian_versi(dokumen_induk, revisi)` | Command tidak mengembalikan ID baru (CQS). Di Odoo, `create()` memang mengembalikan rekaman; penyimpangan kecil ini dicatat dan diterima di langkah 10 |
| **`pengesah` dikirim oleh KaLab di `sahkan_dokumen()`**, bukan diambil dari `user_id` | Pengesah (pejabat penanda tangan) berbeda dari pencatat (pengguna yang login) |
| **`kedaluwarsakan_dokumen(tanggal)` tanpa `user_id`** | Dipicu Penjadwal; pelaku di riwayat dicatat sebagai sistem |

---

## 6. Cek silang

### 6.1 Use case → operasi

Setiap use case punya minimal satu operasi:

| UC | Operasi | UC | Operasi |
|---|---|---|---|
| UC-01 | `daftar_dokumen`, `ajukan_dokumen`, `cek_kelengkapan`, `status_dokumen` | UC-15 | `daftar_dokumen_induk`, `info_versi`, `buat_versi`, `rincian_versi` |
| UC-02 | `terbitkan_dokumen` | UC-16 | `daftar_versi_berlaku`, `catat_distribusi` |
| UC-03 | `daftar_dokumen`, `unggah_berkas_ttd`, `rincian_dokumen` | UC-17 | `daftar_versi_berlaku`, `catat_sosialisasi` |
| UC-04 | `daftar_dokumen`, `rincian_dokumen`, `kembalikan_dokumen` | UC-18 | `daftar_versi_berlaku`, `catat_tinjau_ulang`, `status_tinjau` |
| UC-05 | `daftar_dokumen`, `rincian_dokumen`, `daftar_pengesah_berwenang`, `sahkan_dokumen` | UC-19 | `daftar_versi_berlaku`, `baca_dokumen_berlaku` |
| UC-06 | `daftar_dokumen`, `rincian_dokumen`, `cabut_dokumen` | UC-20 | `laporan_pengendalian_dokumen` |
| UC-07 | `kedaluwarsakan_dokumen` | UC-21, 22 | pola «CRUDL» |
| UC-08, 09 | pola «CRUDL» | UC-23 | `buat_rencana`, `simpan_temuan_gap`, `simpan_item_rencana`, `rincian_rencana`, `daftar_rencana`, `daftar_kpi`, `daftar_personel`, `cek_kelengkapan` |
| UC-10 | `buat_sk`, `simpan_baris_penetapan`, `rincian_sk` | UC-24 | `daftar_rencana`, `buat_revisi_rencana` |
| UC-11 | `catat_rapat`, `koreksi_rekaman` | UC-25 | `daftar_item_pic`, `catat_realisasi`, `koreksi_realisasi`, `capaian_item` |
| UC-12 | `catat_evaluasi`, `tautkan_revisi_evaluasi`, `koreksi_rekaman` | UC-26 | `daftar_rencana`, `catat_tinjauan`, `tautkan_rencana_berikutnya`, `koreksi_rekaman` |
| UC-13 | `laporan_struktur` | UC-27 | `laporan_rencana` |
| UC-14 | pola «CRUDL» | UC-28 | `status_monev` |

### 6.2 AB → operasi

Setiap AB dicek oleh minimal satu operasi (kolom "AB" di bagian 3). AB-24 dan AB-25 dihitung oleh `status_monev()`; AB-14 dipakai oleh `sahkan_dokumen()`, `catat_tinjau_ulang()`, dan query yang menampilkan penanda perlu ditinjau.

### 6.3 Ketidaksesuaian dengan langkah sebelumnya

- Expanded use case bagian 8 menyebut "tambah item" dan "tambah temuan gap". Di sini menjadi `simpan_item_rencana()` dan `simpan_temuan_gap()` yang menyimpan seluruh koleksi sekaligus, karena aktor menyerahkan item sebagai satu kumpulan (§6.4, "actor informs …" sekali).
- UC-12 dan UC-26 di expanded use case tidak punya alur lengkap. Operasi tautan "kemudian" (`tautkan_revisi_evaluasi`, `tautkan_rencana_berikutnya`) muncul dari pascakondisi di tabel deskripsi.

---

## 7. Temuan untuk langkah 9 (conceptual model)

Konsep dan atribut yang harus punya tempat di model, diambil dari kamus DTO:

| Kelompok | Konsep kandidat |
|---|---|
| Pengesahan | Dokumen yang disahkan (umum untuk SK, Renstra, Rencana, Versi), **Kejadian pengesahan** (riwayat) sebagai konsep kejadian (§9.3.2), bukan atribut |
| Struktur | Personel, Jabatan, Tugas, Wewenang, SK Penetapan, Baris Penetapan, Rapat Koordinasi, Evaluasi Struktur, Ruang, Periode |
| Dokumen SOP/IK | Dokumen Induk, Versi, Distribusi, Sosialisasi (+ peserta), Tinjau Ulang; lokasi penggunaan = Ruang (master Core) |
| Rencana | Renstra, Rencana, Temuan Gap, Item Rencana, KPI, Realisasi, Tinjauan Rencana, Ukuran Manfaat |
| Turunan | `/perlu_ditinjau`, `/tanggal_tinjau_berikutnya`, `/prioritas`, `/kriteria_tertinggi`, `/persentase` |
| Koreksi | Koreksi rekaman: cukup dilacak sebagai riwayat perubahan (`mail.thread`); perlu diputuskan apakah menjadi konsep sendiri |

Keputusan untuk langkah 9 (Febriyan, 14 November 2026):
- **Lokasi penggunaan** = Ruang dari master Core saja. Tidak ada nilai "portal"; S4 dibuktikan lewat distribusi ke setiap ruang yang ditetapkan.
- **Wewenang** = konsep anak Jabatan (komposisi, *has-a*) dengan atribut *tindakan* (menyusun, mengesahkan) dan *jenis dokumen* (pilihan tetap). Bukan turunan Jabatan. Di langkah 10: `hr.job` diperluas (`_inherit`) dengan One2many ke model baru `labfik.jabatan.wewenang`; pola yang sama untuk tugas.

## 8. Isu terbuka

- [ ] Tampilan diagram belum dicek di draw.io **[VALIDASI]**
- [ ] Penyimpangan CQS pada `create()` Odoo diterima (bagian 5) **[USULAN PENULIS]**
