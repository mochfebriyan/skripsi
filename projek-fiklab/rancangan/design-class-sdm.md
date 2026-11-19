# Design Class Diagram Modul SDM & Kompetensi

19 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 10 (terakhir) alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (class diagram). Dasar implementasi addon `labfik_sdm` di Odoo 17 Community.

Diagram: [class-sdm.drawio](class-sdm.drawio), 4 halaman (DCD-1–DCD-4) dan 1 halaman catatan. Dibuat dengan skrip [tools/drawio/sdm/design_class.py](../tools/drawio/sdm/design_class.py), yang fungsi gambar dan gayanya disalin dari `contoh-tata-kelola/design_class.py` versi `main`. Satu perubahan: nama field dan multiplisitas ditulis di tengah garis, bukan di ujung, agar label tidak menimpa isi kotak. Diagram lolos `validate.py` dengan prefiks `sdm-`, dan tampilannya sudah dicek lewat ekspor PNG draw.io desktop.

Sumber: [conceptual-model-sdm.md](conceptual-model-sdm.md) (CM-1–4), katalog operasi di [ssd-sdm.md](ssd-sdm.md), AB-SDM-01–28 di [expanded-use-case-sdm.md](expanded-use-case-sdm.md), dan [kontrak-core-sdm.md](kontrak-core-sdm.md) (atribut usulan; dokumen ini yang berlaku bila berbeda).

---

## 1. Aturan yang dipakai

| Aturan | Sumber | Penerapan |
|---|---|---|
| DCD dimulai dari salinan conceptual model, lalu: tambah method, beri arah asosiasi, rinci tipe, ubah struktur bila perlu | Wazlawick §13.6 | Bagian 3 |
| Tanggung jawab dibagi ke objek yang memegang datanya (*delegation*) | §13.2, §13.5 | Cek kompetensi di `hr.employee`; berlaku tidaknya di bukti, baris penugasan, dan otorisasi; layanan monev hanya mendelegasikan |
| Arah asosiasi mengikuti arah pesan; komposisi = One2many + Many2one | §13.6 | Panah Many2one dari anak/perujuk ke yang dirujuk |
| Perilaku bersama sebagai *mixin* `AbstractModel`; model turunan memakai `_inherit` | Arahan Pak Widi; CLAUDE.md langkah 10 | Empat mixin Core; tidak ada mixin baru di SDM |
| Urutan baku = **Template Method** dengan **hook** | CLAUDE.md bagian 8 | `action_ajukan()` / `action_sahkan()` milik Core tidak di-*override*; model SDM mengisi `_cek_kelengkapan()`, `_sebelum_ajukan()`, `_sebelum_disahkan()`, `_dokumen_diganti()`, `_cek_k1()–_cek_k4()` |
| Model bawaan diperluas, bukan disalin | Kontrak Core | `hr.employee`, `hr.job` dengan `_inherit` tanpa `_name` baru; `selection_add` pada jenis dokumen wewenang |
| Notasi DCD proyek | CLAUDE.md bagian 5 | «AbstractModel» miring, «Odoo», «Core», model baru tanpa stereotype, `+`/`#`, «override», {abstract}, {hook} |

---

## 2. Daftar model

### 2.1 Dari Core (dipakai, tidak diubah)

| Model | Dipakai untuk |
|---|---|
| `labfik.approval.mixin` + `labfik.approval.log` | Surat Tugas, Otorisasi, Rencana Pelatihan |
| `labfik.period.mixin` | Rencana Pelatihan |
| `labfik.criteria.mixin` | Rencana Pelatihan (K1–K4) |
| `labfik.evidence.mixin` | Delapan rekaman bukti |
| `labfik.kelas`, `labfik.mata.kuliah`, `labfik.periode`, `labfik.ruang`, `labfik.sesi` | Rujukan; dibaca saja |

### 2.2 Perluasan oleh `labfik_sdm`

| Model | Tambahan |
|---|---|
| `hr.employee` | `bukti_kompetensi_ids`; `punya_kompetensi()`, `kompetensi_kurang()`, `memenuhi_syarat_jabatan()` |
| `hr.job` | `syarat_kompetensi_ids` |
| `labfik.jabatan.wewenang` | `jenis_dokumen` += `penugasan_petugas`, `otorisasi`, `rencana_pelatihan` (`selection_add`) |

### 2.3 Model baru `labfik_sdm` (`depends: ['labfik_core']`)

| Model | `_inherit` | Label | Asal di CM | DCD |
|---|---|---|---|---|
| `labfik.sdm.kompetensi` | — | [M] | Kompetensi | 2 |
| `labfik.sdm.bukti.kompetensi` | evidence | [T] | BuktiKompetensi | 2 |
| `labfik.sdm.kebutuhan.petugas` | evidence | [T] | KebutuhanPetugas | 2 |
| `labfik.sdm.seleksi` | evidence | [T] | Seleksi + Pengecualian | 2 |
| `labfik.sdm.surat.tugas` | approval | [T] | SuratTugas | 2 |
| `labfik.sdm.penugasan` | — | [T] | BarisPenugasan | 2 |
| `labfik.sdm.orientasi` (O) | evidence | [T] | Orientasi | 2 |
| `labfik.sdm.tugas.khusus` | — | [M] | TugasKhusus | 3 |
| `labfik.sdm.asesmen` | evidence | [T] | Asesmen | 3 |
| `labfik.sdm.otorisasi` | approval | [T] | Otorisasi | 3 |
| `labfik.sdm.evaluasi.otorisasi` | evidence | [T] | EvaluasiUlang + KeputusanEvaluasi | 3 |
| `labfik.sdm.rencana.pelatihan` | approval, period, criteria | [T] | RencanaPelatihan | 4 |
| `labfik.sdm.kebutuhan.pelatihan` | — | [T] | KebutuhanKompetensi | 4 |
| `labfik.sdm.item.pelatihan` | — | [T] | ItemPelatihan + PembatalanItem | 4 |
| `labfik.sdm.realisasi.pelatihan` | evidence | [T] | RealisasiPelatihan | 4 |
| `labfik.sdm.evaluasi.pelatihan` | evidence | [T] | EvaluasiEfektivitas | 4 |
| `labfik.sdm.monev` | AbstractModel (layanan) | [R] | — (hasil hitung) | 4 |

**Jumlah:** 16 model bertabel (2 master, 14 transaksi) dan 1 layanan. Semua nama memakai pola `labfik.sdm.*` dan tidak bentrok dengan Tata Kelola.

---

## 3. Dari conceptual model ke desain (§13.6)

| Perubahan | CM | DCD | Alasan |
|---|---|---|---|
| Generalisasi menjadi *mixin* Core | DokumenSDM, RekamanBukti | `approval.mixin`, `evidence.mixin` | Mekanisme Core yang sudah ada; tidak dibuat ulang |
| Konsep kejadian 0..1 menjadi field | Pengecualian, KeputusanEvaluasi, PembatalanItem, Pengesahan | `alasan_pengecualian` + `penyetuju_id`; `keputusan`, `hasil`, `penilai_id`, `tanggal_keputusan`; `alasan_batal` + status *batal*; field pengesahan di mixin | Hanya ada satu kejadian per objek; riwayat pengesahan tetap utuh di `approval.log` |
| Konsep kejadian * menjadi log generik | KejadianPengesahan | `labfik.approval.log` (Core) | Satu tabel riwayat untuk semua dokumen yang disahkan |
| Asosiasi refleksif *menggantikan* | DokumenSDM | Surat Tugas: `revisi_dari_id`; Otorisasi: dicari lewat pasangan (employee, tugas_khusus) di `_dokumen_diganti()` | Mixin tidak bisa merujuk dirinya sendiri; otorisasi tidak perlu field karena kuncinya pasangan |
| Asosiasi turunan menjadi method | `/kompetensi_kurang` | `hr.employee.kompetensi_kurang(tanggal)` | Bergantung pada tanggal acuan, jadi tidak bisa disimpan |
| Atribut turunan menjadi `compute` | `/berlaku`, `/status`, `/status_evaluasi`, `/kriteria_tertinggi` | `is_berlaku`, `is_sah`, `status` (store), `status_evaluasi`, `kriteria_tertinggi` | `status` evaluasi disimpan (`store`) agar bisa difilter |
| Enumerasi menjadi `Selection` | Semua «enumeration» | `fields.Selection` | — |
| Rujukan Personel menjadi atribut bertipe | pemilik, penilai, penyetuju, supervisor, pelaksana, peserta | `hr.employee` | Model bawaan Odoo boleh ditulis sebagai atribut bertipe (CLAUDE.md bagian 5) |
| Layanan baru | — | `labfik.sdm.monev` | Tempat perhitungan UC-SDM-22; mendelegasikan ke model pemilik data |
| Mata uang | `anggaran: Money` | `Monetary` + `currency_id` | Aturan Odoo |

---

## 4. Template Method dan hook yang diisi model SDM

Urutan `action_ajukan()` dan `action_sahkan()` ditetapkan Core ([kontrak-core.md](kontrak-core.md) M-1). Model SDM hanya mengisi:

| Model | `_jenis_dokumen()` | `_cek_kelengkapan()` | `_sebelum_ajukan()` | `_sebelum_disahkan()` | `_dokumen_diganti()` | `_cek_k1()`–`_cek_k4()` |
|---|---|---|---|---|---|---|
| `labfik.sdm.surat.tugas` | `penugasan_petugas` | AB-SDM-02 | — | — | `revisi_dari_id` (O) | — |
| `labfik.sdm.otorisasi` | `otorisasi` | AB-SDM-03 | — | — | otorisasi Disahkan lain untuk pasangan yang sama (AB-SDM-10) | — |
| `labfik.sdm.rencana.pelatihan` | `rencana_pelatihan` | AB-SDM-04 | bekukan kebutuhan | tolak bila sudah ada rencana Disahkan untuk periode itu (AB-SDM-12) | kosong (KU-2) | AB-SDM-28 |

---

## 5. Pemetaan operasi SSD → method

### 5.1 Pengesahan dokumen SDM

| Operasi SSD | Method / ORM |
|---|---|
| `daftar_dokumen(filter, user_id)` | `search_read()` per model dokumen dengan domain `state`, `penyusun_id.user_id`; satu tampilan daftar per jenis |
| `rincian_dokumen(dokumen, user_id)` | `read()` + `log_ids` {compute} |
| `status_dokumen(dokumen)` | `read(['state', 'tanggal_ajukan', 'tanggal_sah', 'pengesah_id', 'pencatat_id'])` |
| `cek_kelengkapan(dokumen)` | `get_kelengkapan()` → `_cek_kelengkapan()` |
| `daftar_pengesah_berwenang(dokumen)` | `get_pengesah_berwenang()` (Core) |
| `ajukan_dokumen` | `action_ajukan()` (Core) |
| `terbitkan_dokumen` | `action_terbitkan()` → QWeb report (O) |
| `unggah_berkas_ttd` | `action_unggah_ttd(berkas)` |
| `kembalikan_dokumen` | `action_kembalikan(alasan)` |
| `sahkan_dokumen` | `action_sahkan(pengesah, tanggal_sah)` |
| `cabut_dokumen` | `action_cabut(alasan)` |

### 5.2 Pola «CRUDL» dan rekaman bukti

| Operasi SSD | Method / ORM |
|---|---|
| `buat_<konsep>`, `ubah_<konsep>` | `create()`, `write()` |
| `hapus_<konsep>` | `unlink()` «override» (`kompetensi`, `tugas.khusus`: AB-SDM-25; bukti: ditolak `evidence.mixin`) |
| `arsipkan_<konsep>` | `action_archive()` (field `active`) |
| `rincian_<konsep>`, `daftar_<konsep>` | `read()`, `search_read()` |
| `ubah_syarat_jabatan(jabatan, kompetensi*)` | `hr.job.write({'syarat_kompetensi_ids': …})` |
| `koreksi_rekaman(rekaman, dto_koreksi, alasan)` | `evidence.mixin.action_koreksi(nilai, alasan)` |
| `daftar_personel(filter)` | `hr.employee.search_read()` dengan domain `jenis_personel` |
| `matriks_kompetensi(tanggal_acuan, filter)` | `hr.employee.kompetensi_kurang(tanggal)` untuk setiap personel; tampilan QWeb/pivot |

### 5.3 Penugasan

| Operasi SSD | Method / ORM |
|---|---|
| `daftar_kebutuhan_petugas(periode)` | `labfik.kelas.search_read([('periode_id', '=', …)])` + `labfik.sdm.kebutuhan.petugas.search_read()` |
| `tetapkan_kebutuhan_petugas` | `labfik.sdm.kebutuhan.petugas.create()` / `write()` (`_sql_constraints`, `_cek_jumlah()`) |
| `daftar_seleksi(periode, mata_kuliah)` | `labfik.sdm.seleksi.search_read()` |
| `catat_seleksi` | `labfik.sdm.seleksi.create()` «override» → `_pastikan_personel()` |
| `buat_surat_tugas`, `rincian_surat_tugas` | `labfik.sdm.surat.tugas.create()`, `read()` |
| `simpan_baris_penugasan` | `write({'penugasan_ids': [...]})` (AB-SDM-01 di `approval.mixin.write()`) |
| `buat_revisi_surat_tugas` | `action_buat_revisi()` (O): `copy()` + `revisi_dari_id` |
| `catat_orientasi` | `labfik.sdm.orientasi.create()` (O) |
| `daftar_petugas_sesi(periode)` | `labfik.sdm.monev.status_sesi(periode)` |

### 5.4 Otorisasi

| Operasi SSD | Method / ORM |
|---|---|
| `daftar_tugas_khusus(filter)` | `search_read()` |
| `catat_asesmen`, `rincian_asesmen` | `labfik.sdm.asesmen.create()` «override» → `_buat_bukti_kompetensi()`; `read()` |
| `buat_otorisasi`, `ubah_otorisasi`, `rincian_otorisasi` | `create()` (+ `_onchange_tugas_khusus()` mengisi `berlaku_sampai`), `write()`, `read()` |
| `buat_otorisasi_dari_evaluasi(evaluasi)` | `@model buat_dari_evaluasi(evaluasi)`: `create()` dengan data otorisasi lama, lalu isi `otorisasi_baru_id` |
| `catat_pemicu` | `labfik.sdm.evaluasi.otorisasi.create()` (`_cek_otorisasi()`) |
| `daftar_evaluasi(filter)`, `rincian_evaluasi` | `search_read([('status', '=', 'terbuka')])`, `read()` |
| `putuskan_evaluasi` | `action_putuskan(keputusan, hasil, penilai, tanggal)` |
| `daftar_operator_sah(tanggal, tugas_khusus)` | `labfik.sdm.otorisasi.search()` + `berlaku_pada(tanggal)` |

### 5.5 Pelatihan

| Operasi SSD | Method / ORM |
|---|---|
| `buat_rencana_pelatihan` | `create()` lalu `action_isi_kebutuhan()` |
| `simpan_kebutuhan`, `simpan_item_pelatihan` | `write({'kebutuhan_ids' / 'item_ids': [...]})` (`_cek_dibekukan()`) |
| `rincian_rencana_pelatihan`, `daftar_kompetensi` | `read()`, `search_read()` |
| `daftar_item_pelatihan(filter)` | `labfik.sdm.item.pelatihan.search_read()` dengan domain `rencana_id.state`, `status` |
| `catat_realisasi` | `labfik.sdm.realisasi.pelatihan.create()` «override» (`_cek_item()`, item → terlaksana) |
| `batalkan_item` | `action_batalkan(alasan)` (O) |
| `daftar_realisasi(filter)`, `rincian_realisasi` | `search_read()` (tanpa evaluasi), `read()` |
| `catat_evaluasi_efektivitas` | `labfik.sdm.evaluasi.pelatihan.create()` «override» → `_buat_bukti_kompetensi()` |
| `rekap_pelatihan` | QWeb report dari realisasi dan evaluasi (O) |

### 5.6 Status monev

| Operasi SSD | Method |
|---|---|
| `status_monev(periode, tanggal_acuan)` | `labfik.sdm.monev.get_status()` → `status_sesi()`, `status_pasangan()`, `rencana.get_kriteria()`, `hitung_skor()` |
| `rincian_unit_monev(unit, tanggal_acuan)` | `get_unit()` |
| `laporan_bukti` | `action_laporan_bukti()` → QWeb PDF |

Semua operasi katalog SSD terpetakan.

---

## 6. Pemetaan aturan bisnis → mekanisme Odoo

| AB | Mekanisme | Model |
|---|---|---|
| AB-SDM-01 | `approval.mixin.write()`/`unlink()` menolak bila bukan draf (Core AB-01) | tiga dokumen SDM |
| AB-SDM-02 | `_cek_kelengkapan()` «override» | `surat.tugas` |
| AB-SDM-03 | `_cek_kelengkapan()` «override» | `otorisasi` |
| AB-SDM-04 | `_cek_kelengkapan()` + `_sebelum_ajukan()` (bekukan) + `_cek_dibekukan()` @constrains di kebutuhan | `rencana.pelatihan`, `kebutuhan.pelatihan` |
| AB-SDM-05, 06, 07, 08, 09, 11 | Template Method Core (`action_unggah_ttd`, `action_sahkan`, `_cek_wewenang`, grup `labfik_kalab`, alasan wajib, `approval.log`) + baris wewenang (`selection_add` + data XML) | `approval.mixin`, `jabatan.wewenang` |
| AB-SDM-10 | `_dokumen_diganti()` «override» | `surat.tugas`, `otorisasi` |
| AB-SDM-12 | `_sebelum_disahkan()` «override» | `rencana.pelatihan` |
| AB-SDM-13 | `bukti.berlaku_pada()` + `hr.employee.kompetensi_kurang()` / `memenuhi_syarat_jabatan()` | `bukti.kompetensi`, `hr.employee` |
| AB-SDM-14 | `_sql_constraints` unique(kelas_id, peran) + `_cek_jumlah()` @constrains | `kebutuhan.petugas` |
| AB-SDM-15 | `_sql_constraints` + `_cek_pengecualian()` @constrains + `create()` «override» → `_pastikan_personel()` | `seleksi` |
| AB-SDM-16 | `penugasan.berlaku_pada()` + `_cek_sasaran()` @constrains + `is_sah` {compute} | `penugasan` |
| AB-SDM-17 | `create()` «override» → `_buat_bukti_kompetensi()` | `asesmen` |
| AB-SDM-18 | `is_berlaku` {compute} + `berlaku_pada()` + `_onchange_tugas_khusus()` | `otorisasi` |
| AB-SDM-19 | `_cek_otorisasi()` @constrains + `action_putuskan()` (cek status terbuka, data wajib) | `evaluasi.otorisasi` |
| AB-SDM-20 | `action_isi_kebutuhan()` | `rencana.pelatihan` |
| AB-SDM-21 | `_cek_item()` @constrains + `_sql_constraints` + `create()` «override» | `realisasi.pelatihan` |
| AB-SDM-22 | `action_batalkan()` (O) | `item.pelatihan` |
| AB-SDM-23 | `_sql_constraints` unique(realisasi_id) + `create()` «override» → `_buat_bukti_kompetensi()` | `evaluasi.pelatihan` |
| AB-SDM-24 | `evidence.mixin.unlink()` ditolak + `action_koreksi()` + `mail.thread` tracking | delapan rekaman bukti |
| AB-SDM-25 | `unlink()` «override» menolak bila dirujuk; arsip lewat `active` | `kompetensi`, `tugas.khusus` |
| AB-SDM-26 | `monev.status_sesi()` + `hitung_skor()` | `labfik.sdm.monev` |
| AB-SDM-27 | `monev.status_pasangan()` + `hitung_skor()` | `labfik.sdm.monev` |
| AB-SDM-28 | `criteria.mixin.get_kriteria()` + `_cek_k1()–_cek_k4()` «override» | `rencana.pelatihan` |

Semua 28 AB terpetakan. Tidak ada `ir.cron`: modul SDM tidak memakai penjadwal (K-3).

---

## 7. Grup akses

Memakai grup Core ([kontrak-core.md](kontrak-core.md) G).

| Grup | Hak di modul SDM |
|---|---|
| `labfik_laboran` | Membuat dan mengoreksi rekaman bukti (bukti kompetensi, seleksi, orientasi, asesmen, evaluasi ulang, realisasi, evaluasi efektivitas); menyusun draf Surat Tugas; mengajukan dan mengunggah berkas |
| `labfik_kalab` | Semua hak Laboran; master Kompetensi dan Tugas/Alat; syarat jabatan; kebutuhan petugas; otorisasi; rencana pelatihan; **mengembalikan, mengesahkan, mencabut**; status monev |

Berkas KHS pada Seleksi hanya terlihat oleh dua grup ini (KNF-SDM-04, 07).

---

## 8. Cek silang akhir

| Pemeriksaan | Hasil |
|---|---|
| Setiap konsep CM punya model | ✓ (bagian 2.3); konsep kejadian 0..1 dilebur (bagian 3) |
| Setiap operasi SSD punya method atau ORM | ✓ (bagian 5) |
| Setiap AB punya mekanisme | ✓ 28 AB (bagian 6) |
| Status sama dengan S1–S4 | ✓ `approval.mixin.state` tanpa `kedaluwarsa` di SDM; `evaluasi.otorisasi.status`; `item.pelatihan.status` |
| Field warisan tidak ditulis ulang | ✓ |
| Selaras dengan kontrak Core bersama | ✓ I-1 (`sesi.state`), I-2 (`syarat_kompetensi_ids`), I-4, I-5, I-6, I-7 |
| Kriteria instrumen | PKG-04 S1–S4 → `status_sesi()`; PKG-10 S1–S4 → `status_pasangan()`; PKG-14 K1–K4 → `_cek_k1()–_cek_k4()` |
| Data pribadi | ✓ Tidak ada nama, NIM, atau nomor HP |

### 8.1 Perbedaan dengan kontrak-core-sdm.md versi 3

| Kontrak Core SDM | DCD ini | Alasan |
|---|---|---|
| `evaluasi.otorisasi.status` Selection biasa | `{compute, store}` dari ada-tidaknya keputusan | CM: status adalah turunan (§9.3.1) |
| `monev.hitung_persentase(unit)` | `hitung_skor(persentase)`; persentase dihitung di `status_sesi()`/`status_pasangan()` | Skor perlu ambang instrumen; persentase sudah keluar dari fungsi status |
| Tidak ada `_sebelum_disahkan()` untuk Rencana | Diisi (AB-SDM-12) | Temuan langkah 7 |
| `item.pelatihan.status_evaluasi` | Sama | — |

Ketiga baris itu sudah disesuaikan di kontrak-core-sdm.md (19 November 2026).

---

## 9. Isu terbuka

- [ ] KP-1, KB-1, KB-3, KU-1, KU-2, KU-3 (use case bagian 9.2) masih memakai *default*
- [ ] K7, K10: baris wewenang awal di data XML
- [ ] AB-SDM-17: masa berlaku bukti demonstrasi **[USULAN PENULIS]**
- [ ] KC-9: `memenuhi_syarat_jabatan()` belum tercatat di kontrak Core bersama
