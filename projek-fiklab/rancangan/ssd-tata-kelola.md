# System Sequence Diagram & Operasi Sistem Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Step 8 rancangan TO-BE. Diagram: [ssd-tata-kelola.drawio](ssd-tata-kelola.drawio), 8 halaman (SSD-1 sampai SSD-8). Sumbernya adalah alur di [expanded-use-case-tata-kelola.md](expanded-use-case-tata-kelola.md) bagian 3.

Inilah diagram yang dimaksud Pak Widi dengan "sequence diagram". Menurut Wazlawick, sequence diagram di tahap analisis adalah **system sequence diagram (SSD)**: sistem diperlakukan sebagai kotak hitam. Sequence diagram antar-objek di dalam sistem baru dibuat di tahap desain (Bab 13).

## Konvensi (Wazlawick 2024, Bab 7)

| Unsur | Arti | Dasar |
|---|---|---|
| Lifeline `:Aktor`, `:Antarmuka` (boundary), `:Kontroler` (control) | Aktor hanya berkomunikasi lewat antarmuka. Kontroler adalah *façade* yang membungkus lapisan domain | §7.2, §7.4 |
| Panah hitam penuh | **System event**: informasi dari aktor ke antarmuka | §7.4 |
| Panah hitam putus-putus | **System return**: informasi dari antarmuka ke aktor | §7.4 |
| Panah ungu `op(args)` | **Command**: mengubah data, tanpa nilai balik | §7.1 (CQS) |
| Panah ungu `dto = op(args)` | **Query**: membaca data, tanpa mengubahnya | §7.1 (CQS) |
| `dto_x`, `x*`, *terpilih* | Data majemuk (lihat kamus), koleksi, pilihan dari daftar | §7.3 |
| `user_id` di setiap operasi | **Stateless**: kontroler tidak mengingat apa pun di antara operasi | §7.5 |
| `opt «exception»`, `opt «variant»`, `ref` | Alur alternatif dan rujukan ke use case lain | §7.6 |
| Aktor kedua di kanan | Penerima pemberitahuan (pemeriksa, pengesah, atau penyusun) | §7.2 (Gambar 7–1) |

## 1. Daftar SSD

| SSD | Use case | Aktor | Alur alternatif |
|---|---|---|---|
| SSD-1 | UC-21 Ajukan Dokumen | Penyusun → Pemeriksa/Pengesah | E1 kelengkapan (AB-01), E2 tidak ada pengesah berwenang (AB-02) |
| SSD-2 | UC-24 Kembalikan Dokumen | Pemeriksa/Pengesah → Penyusun | V1 penolakan di atas kertas, E1 alasan kosong (AB-05) |
| SSD-3 | UC-26 Unggah Dokumen Bertanda Tangan | Penyusun → Pengesah | V1 ganti berkas, E1 berkas rusak, E2 penanda tangan tidak berwenang |
| SSD-4 | UC-27 Sahkan Dokumen | Pengesah → Penyusun | V1 tidak menyetujui (ref SSD-2), V2 atas nama Dekan, E1 berkas belum ada (ref SSD-3), E2 pemeriksaan wajib (AB-09) |
| SSD-5 | UC-08 Unggah Versi Dokumen | Laboran | V1 versi pertama, E1 versi sedang diproses (AB-13), E2 nomor revisi |
| SSD-6 | UC-11 Tinjau Ulang Dokumen | Laboran/KaLab | V1 perlu revisi (ref SSD-5), V2 tidak diperlukan (ref UC-28), E1 catatan kosong |
| SSD-7 | UC-16 Susun Rencana | KaLab | V1 pengembangan (gap), V2 revisi, V3 lanjutkan draf, E1 periode, E2 PIC |
| SSD-8 | UC-18 Isi Realisasi Rencana | PIC | E1 alasan (AB-10), E2 bukti (AB-12), E3 bukan PIC (AB-11) |

## 2. Katalog operasi sistem (§7.7)

Hasil utama Bab 7 adalah daftar **command** dan **query** yang harus disediakan sistem. Daftar ini menjadi bahan method di design class diagram (Step 10).

Operasi yang berpola sama sudah disatukan dengan parameter `filter`. Misalnya empat query "daftar dokumen menunggu …" menjadi satu `daftar_dokumen(filter, user_id)`.

Kolom **Tempat (sementara)** adalah usulan model Odoo pemilik operasi. Penempatan final ditentukan di Step 10.

### 2.1 Command (mengubah data, tanpa nilai balik)

| Operasi | Dipakai di | Aturan yang diperiksa | Tempat (sementara) |
|---|---|---|---|
| `ajukan_dokumen(dokumen, user_id)` | SSD-1 | AB-01, AB-02 | `approval.mixin.action_ajukan()` |
| `kembalikan_dokumen(dokumen, alasan, user_id)` | SSD-2 | AB-02, AB-05 | `approval.mixin.action_kembalikan()` |
| `catat_pengembalian(dokumen, alasan, nama_pengesah, jabatan_pengesah, user_id)` | SSD-2 V1 | AB-05 | `approval.mixin` (varian dari `action_kembalikan`) |
| `lampirkan_berkas_ttd(dokumen, dto_ttd, user_id)` | SSD-3 | AB-02 | `approval.mixin` |
| `sahkan_dokumen(dokumen, user_id [, atas_nama])` | SSD-4 | AB-02, AB-03, AB-04, AB-09, AB-14 | `approval.mixin.action_sahkan()` (di-*override* di versi dokumen) |
| `buat_versi(dokumen_induk, dto_versi_baru, user_id)` | SSD-5 | AB-13, nomor revisi | `labfik.document` |
| `catat_tinjau_ulang(dokumen, dto_hasil_tinjau, user_id)` | SSD-6 | AB-08 | `labfik.document.review` |
| `buat_rencana(dto_rencana_baru, user_id)` | SSD-7 | periode vs rencana induk | `labfik.plan` |
| `buat_revisi_rencana(rencana, user_id)` | SSD-7 V2 | rencana Disahkan | `labfik.plan.action_buat_revisi()` |
| `ubah_isi_rencana(rencana, dto_isi_rencana, user_id)` | SSD-7 | AB-06 (hanya Draf) | `labfik.plan` |
| `simpan_item_rencana(rencana, dto_item*, user_id)` | SSD-7 | PIC aktif, AB-06 | `labfik.plan.line` |
| `simpan_gap(rencana, dto_gap*, user_id)` | SSD-7 V1 | AB-06 | `labfik.plan.gap` |
| `catat_realisasi(item, dto_realisasi, user_id)` | SSD-8 | AB-10, AB-11, AB-12 | `labfik.realisasi` |

**Command dari use case tanpa SSD.** Use case ini cukup dijelaskan di tabel deskripsi; alurnya sederhana (satu event, satu command):

| Operasi | Use case | Aturan | Tempat (sementara) |
|---|---|---|---|
| `tarik_pengajuan(dokumen, alasan, user_id)` | UC-22 | AB-05 | `approval.mixin` |
| `periksa_dokumen(dokumen, catatan, user_id)` | UC-23 | AB-02 | `approval.mixin.action_periksa()` |
| `terbitkan_dokumen(dokumen, user_id)` | UC-25 | jenis = rencana/SK | `labfik.plan`, `labfik.assignment` (laporan QWeb) |
| `cabut_dokumen(dokumen, alasan, user_id)` | UC-28 | AB-02, AB-05 | `approval.mixin.action_cabut()` |
| `kedaluwarsakan_dokumen(tanggal)` | UC-31 | — | `period.mixin` (tugas terjadwal) |
| `kirim_pengingat(tanggal)` | UC-32 | — | `controlled.mixin`, `labfik.plan.line` (tugas terjadwal) |

### 2.2 Query (membaca data, tanpa mengubah)

| Operasi | Hasil | Dipakai di |
|---|---|---|
| `daftar_dokumen(filter, user_id)` | `dto_dokumen_ringkas*` | SSD-1–4. Filter: `draf_saya`, `menunggu_tindakan_saya`, `menunggu_ttd`, `menunggu_pengesahan_saya` |
| `rincian_dokumen(dokumen)` | `dto_rincian_dokumen` | SSD-2, 3, 4 |
| `status_dokumen(dokumen)` | `dto_status` | SSD-1–4 |
| `cek_kelengkapan(dokumen)` | `dto_kelengkapan*` | SSD-1 |
| `daftar_dokumen_induk()` | `dto_dokumen_induk*` | SSD-5 |
| `info_versi(dokumen_induk)` | `dto_info_versi` | SSD-5 |
| `rincian_versi(dokumen_induk, revisi)` | `dto_versi` | SSD-5 |
| `daftar_jadwal_tinjau(user_id)` | `dto_jadwal_tinjau*` | SSD-6 |
| `rincian_tinjau(dokumen)` | `dto_rincian_tinjau` | SSD-6 |
| `status_tinjau(dokumen)` | `dto_status_tinjau` | SSD-6 |
| `daftar_rencana(filter, user_id)` | `dto_rencana_ringkas*` | SSD-7. Filter: `draf_saya`, `disahkan` |
| `rincian_rencana(rencana)` | `dto_rencana` | SSD-7 |
| `status_item_rencana(rencana)` | `dto_status_item*`, `rekap_anggaran` | SSD-7 |
| `status_gap(rencana)` | `dto_status_gap` | SSD-7 V1 |
| `daftar_item_pic(user_id, periode_lapor)` | `dto_item_pic*` | SSD-8 |
| `rincian_item(item)` | `dto_rincian_item` | SSD-8 |
| `capaian_item(item, periode_lapor)` | `dto_capaian` | SSD-8 |

**Jumlah:** 19 command (13 dari SSD + 6 dari use case tanpa SSD) dan 17 query. Command dan query untuk use case «CRUDL» dan «report» mengikuti pola standar (buat/baca/ubah/arsip/daftar) dan tidak perlu diperinci lagi (§7.7).

### 2.3 Padanan di Odoo

| Konsep Wazlawick | Wujud di Odoo 17 |
|---|---|
| `:Antarmuka` | *View* (form, list, kanban) dan *wizard* (`TransientModel`) untuk isian seperti alasan pengembalian |
| `:Kontroler` (façade) | Method publik pada model. Command = method `action_*` yang dipanggil tombol (`type="object"`). Query = baca lewat ORM (`search_read`, field `compute`) |
| `user_id` (stateless) | `self.env.user`, selalu tersedia di setiap pemanggilan |
| Pemberitahuan ke aktor kedua | `mail.activity` / `message_post` dari `mail.thread` |
| Tugas Penjadwal | `ir.cron` |

## 3. Kamus DTO (§7.3)

DTO adalah kumpulan data yang dikirim atau ditampilkan sekaligus. Isinya adalah sebagian atribut kelas di conceptual model, sehingga kamus ini menjadi masukan langsung untuk Step 9.

| DTO | Isi |
|---|---|
| `dto_dokumen_ringkas` | ‹jenis, judul, penyusun, tanggal_ajukan, status, ada_berkas_ttd› |
| `dto_rincian_dokumen` | ‹jenis, judul, isi ringkas, penyusun, riwayat_pengajuan, catatan_pemeriksaan, berkas_ttd, pengesah_berwenang*› |
| `dto_status` | ‹status, tanggal_ajukan, tanggal_sah, pengesah, jabatan_pengesah, pencatat, alasan, dokumen_diganti, tanggal_tinjau_berikutnya, penerima_pemberitahuan› |
| `dto_kelengkapan` | ‹butir, terpenuhi› |
| `dto_ttd` | ‹berkas, tanggal_ttd, nama_penanda_tangan› |
| `dto_dokumen_induk` | ‹kode, judul, jenis, kategori› |
| `dto_info_versi` | ‹versi_berlaku ‹revisi, tanggal_berlaku›, riwayat_versi*, versi_diproses› |
| `dto_versi_baru` | ‹berkas, revisi, tanggal_dibuat, bagian_diubah, ringkasan_perubahan, alasan_revisi, periode_tinjau› |
| `dto_versi` | ‹revisi, status, tanggal_dibuat, ringkasan_perubahan› |
| `dto_jadwal_tinjau` | ‹dokumen, versi_berlaku, tanggal_tinjau_berikutnya, status_kemutakhiran› |
| `dto_rincian_tinjau` | ‹versi_berlaku, riwayat_tinjau*› |
| `dto_hasil_tinjau` | ‹hasil, tanggal, catatan› |
| `dto_status_tinjau` | ‹hasil, status_kemutakhiran, tanggal_tinjau_berikutnya, jabatan_pencabut› |
| `dto_rencana_baru` | ‹jenis, nama, periode, rencana_induk› |
| `dto_rencana` | ‹jenis, nama, periode, status, bagian_terisi*, bagian_belum*› |
| `dto_isi_rencana` | ‹narasi (ringkasan, latar_belakang, tujuan, ruang_lingkup, referensi, landasan, visi, misi, penutup), baseline*, sasaran*, program*› |
| `dto_item` | ‹kegiatan, kpi, baseline, target, satuan, jadwal_mulai, jadwal_selesai, pic, bukti_diharapkan, anggaran, komponen_anggaran, sasaran, program, sasaran_renstra*; untuk pengembangan: gap*, nilai_risiko, nilai_manfaat› |
| `dto_status_item` | ‹item, lengkap, butir_kurang*, prioritas› |
| `dto_gap` | ‹aspek, kondisi_saat_ini, kebutuhan, sumber_data, uraian_gap, lampiran› |
| `dto_status_gap` | ‹aspek, jumlah_temuan›* |
| `dto_rencana_ringkas` | ‹jenis, nama, periode, status› |
| `dto_item_pic` | ‹item, kegiatan, kpi, target, satuan, jadwal, realisasi_terakhir› |
| `dto_rincian_item` | ‹item, realisasi*› |
| `dto_realisasi` | ‹periode_lapor, capaian, anggaran_terpakai, status_capaian, alasan_tidak_relevan, analisis_tindakan, pic_tindak_lanjut, tenggat, bukti*› |
| `dto_capaian` | ‹capaian, target, persen_capaian, status_capaian› |

## 4. Temuan untuk langkah berikutnya

| Temuan | Dampak |
|---|---|
| **Atribut baru** dari DTO: `tanggal_ttd`, `nama_penanda_tangan` (berkas TTD); `pencatat` dan `atas_nama` (pengesahan oleh KaLab atas nama Dekan); `alasan` (pengembalian, penarikan, pencabutan); `catatan_pemeriksaan` | Masuk ke conceptual model (Step 9) dan `approval.mixin` (Step 10) |
| `status_kemutakhiran` muncul di DTO tetapi bukan field tersimpan | Atribut turunan ({compute}) dari S2, sesuai catatan *modal class* |
| `pengesah_berwenang*` dibutuhkan di beberapa DTO | Perlu query wewenang di Jabatan: siapa pemegang jabatan aktif dengan wewenang *mengesahkan* untuk jenis dokumen tertentu |
| Empat query daftar dokumen dan tiga query status disatukan | Antarmuka cukup satu daftar dokumen dengan filter, cocok dengan menu Odoo per status |
| Pemberitahuan ke aktor kedua muncul di semua SSD pengesahan | Dipenuhi `mail.activity` (sudah diwarisi lewat `approval.mixin`) |

## 5. Langkah berikutnya

Step 9 adalah **conceptual model** (Wazlawick Bab 8–11): konsep, atribut primitif, dan asosiasi saja, tanpa method dan tanpa detail Odoo. Diturunkan dari kata benda di expanded use case dan kamus DTO di atas (Bab 10).
