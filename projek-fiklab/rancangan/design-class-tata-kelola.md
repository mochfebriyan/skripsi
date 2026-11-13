# Design Class Diagram Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF. Diagram ini masuk proposal (Bab II 2.3).** Step 10, langkah terakhir rancangan TO-BE.

Diagram: [class-tata-kelola.drawio](class-tata-kelola.drawio), 3 halaman. File ini menggantikan class diagram v1 dengan nama file yang sama.

| Halaman | Isi |
|---|---|
| DCD 1/3 | Inheritance: 5 mixin, `mail.thread`, model log pengesahan, kelas konkret beserta method *override* |
| DCD 2/3 | Struktur organisasi (PKG-03) dan pengendalian dokumen (PKG-02) |
| DCD 3/3 | Perencanaan (PKG-01, PKG-13) |

## 1. Dari conceptual model ke design class diagram

Wazlawick (2024) §13.6: DCD dimulai dari salinan conceptual model, lalu dimodifikasi dengan langkah-langkah berikut.

| Modifikasi (§13.6) | Penerapan |
|---|---|
| **Method ditambahkan** | Command dan query dari katalog operasi SSD menjadi method (bagian 3) |
| **Asosiasi diberi arah** | Many2one/Many2many = asosiasi berarah dari pemilik field. One2many + Many2one inverse = dua arah. Arah mengikuti kebutuhan query: misalnya `Jabatan → Personel` lewat `pemegang_aktif_ids` karena `cari_pemegang_berwenang()` dipanggil dari pengesahan |
| **Atribut diperinci** | Tipe primitif menjadi tipe field Odoo: String → `Char`, Text → `Text`/`Html`, Natural → `Integer`, Decimal → `Float`, Money → `Monetary`, Berkas → `Binary`/`ir.attachment`. Atribut turunan `/x` → `compute` |
| **Struktur boleh berubah** | (a) Generalisasi *DokumenTerkendali* → `controlled.mixin` + `approval.mixin`. (b) Tujuh konsep riwayat (CM-1) → satu model `labfik.approval.log`. (c) Atribut bertanggal dan berbukti pada rekaman → `evidence.mixin`. (d) Periode → `period.mixin`. (e) Status kriteria K1–K4 → `criteria.mixin` |
| **Atribut internal** | Method berawalan `#` (garis bawah di Odoo) hanya dipanggil dari dalam model |

## 2. Inheritance (DCD 1/3)

### 2.1 Mixin

| Mixin (`AbstractModel`) | Isi | Dipakai oleh | Dasar |
|---|---|---|---|
| `labfik.controlled.mixin` | kode, revisi, unit pemilik, tanggal dibuat | plan, assignment, document.version | ISO 8.3.2 (identifikasi dan status revisi) |
| `labfik.approval.mixin` (turunan `mail.thread`, `mail.activity.mixin`) | Status (S1), ringkasan pengesahan terakhir, `log_ids`; 8 command pengesahan; hook | plan, assignment, document.version | A1, S1, UC-21–28, KF-31–34, 39–41 |
| `labfik.period.mixin` | periode, tanggal mulai/selesai, `is_berlaku`; tugas terjadwal kedaluwarsa | plan, assignment | K1 "masih berlaku", UC-31, KF-42 |
| `labfik.criteria.mixin` | `status_k1`–`k4`, `kriteria_tertinggi`; `_cek_k1()`–`_cek_k4()` {abstract} | plan, assignment | KF-36; PKG-01, 03, 13 |
| `labfik.evidence.mixin` | tanggal, pelapor, bukti, keterangan | realisasi, meeting, org.evaluation, distribution, socialization, review, tinjauan | Rekaman K3/K4, S3–S5 |

Perubahan dibanding class diagram v1:
- Field tinjau ulang pindah dari `controlled.mixin` ke `document.version`, karena hanya SOP/IK yang punya siklus tinjau ulang (S2).
- `tinjauan` tidak lagi memakai `period.mixin`, karena tinjauan melekat pada rencana yang sudah berperiode.

### 2.2 Model log pengesahan (baru)

`labfik.approval.log` menyimpan satu baris per kejadian di S1: ajukan, tarik, periksa, kembalikan, unggah_ttd, sahkan, cabut, kedaluwarsa. Log ini merujuk dokumen secara generik lewat `res_model` + `res_id`, sehingga satu model log melayani ketiga jenis dokumen (pola yang sama dengan `mail.message` di Odoo). Field `putaran` menandai pengajuan ke berapa, menggantikan konsep Pengajuan {ordered} di CM-1.

Field ringkas di `approval.mixin` (`pengesah_id`, `tanggal_sah`, `file_ttd`, …) menyimpan **keadaan terakhir** untuk tampilan cepat. Log menyimpan **seluruh riwayat** sebagai bukti.

### 2.3 Template Method pada pengesahan

`action_sahkan()` hanya ditulis di mixin, dengan urutan yang tidak bisa dilewati model turunan:
1. `_cek_wewenang(user, 'mengesahkan')` (AB-02)
2. berkas TTD ada (AB-03)
3. pemeriksaan sudah dilakukan bila wajib (AB-09)
4. status → disahkan
5. `_catat_log('sahkan', …)`
6. `_setelah_disahkan()`

Model turunan hanya mengisi hook `_setelah_disahkan()`:

| Model | Isi hook | Aturan |
|---|---|---|
| `labfik.document.version` | Versi berlaku lain dari dokumen yang sama → diganti; hitung jadwal tinjau | AB-04, AB-08 |
| `labfik.assignment` | SK berlaku sebelumnya → diganti; penugasan jabatan berlaku | AB-14, A4 |
| `labfik.plan` | Rencana berlaku dengan jenis dan periode sama → diganti | AB-14 |

Ini memperbaiki v1, yang meng-*override* `action_sahkan()` langsung. Cara v1 itu berisiko melewatkan pengecekan wewenang bila `super()` lupa dipanggil.

### 2.4 Polimorfisme

| Method {abstract} | `labfik.plan` | `labfik.assignment` | `labfik.document.version` |
|---|---|---|---|
| `_jenis_dokumen()` | dari `jenis` (rencana_strategis, rkt, iku, rencana_pengembangan) | `sk_pengelola` | dari jenis dokumen induk (sop, ik, formulir) |
| `_cek_kelengkapan()` | AB-01 bagian rencana | AB-01 bagian SK | AB-01 bagian versi |
| `_cek_k1()`–`_cek_k4()` | K1–K4 PKG-01/13 | K1–K4 PKG-03 | — (PKG-02 dihitung di `document.is_memenuhi`) |

## 3. Katalog operasi SSD → method

Semua 36 operasi dari [ssd-tata-kelola.md](ssd-tata-kelola.md) bagian 2 punya tempat. "ORM" berarti cukup dipenuhi operasi standar Odoo (`create`, `write`, `search`, `read`) lewat view, tanpa method khusus.

### 3.1 Command

| Operasi SSD | Method / mekanisme | Model |
|---|---|---|
| `ajukan_dokumen` | `action_ajukan()` | approval.mixin |
| `tarik_pengajuan` | `action_tarik(alasan)` | approval.mixin |
| `periksa_dokumen` | `action_periksa(catatan)` | approval.mixin |
| `kembalikan_dokumen` | `action_kembalikan(alasan)` | approval.mixin |
| `catat_pengembalian` | `action_catat_pengembalian(alasan, nama, jabatan)` | approval.mixin |
| `lampirkan_berkas_ttd` | `action_lampirkan_ttd(berkas, tanggal_ttd, nama)` | approval.mixin |
| `sahkan_dokumen` | `action_sahkan(atas_nama=None)` | approval.mixin (+ hook) |
| `cabut_dokumen` | `action_cabut(alasan)` | approval.mixin |
| `terbitkan_dokumen` | `action_terbitkan()` (laporan QWeb) | plan, assignment |
| `kedaluwarsakan_dokumen` | `_cron_kedaluwarsakan()` (`ir.cron`) | period.mixin |
| `kirim_pengingat` | `_cron_kirim_pengingat_tinjau()`, `_cron_kirim_pengingat_realisasi()` | document.version, plan.line |
| `buat_versi` | `action_buat_versi(dto_versi_baru)` | document |
| `catat_tinjau_ulang` | ORM `create` + `_perbarui_tanggal_tinjau()` | document.review |
| `buat_rencana`, `ubah_isi_rencana`, `simpan_item_rencana`, `simpan_gap` | ORM `create` / `write` pada rencana dan One2many-nya | plan, plan.line, plan.gap |
| `buat_revisi_rencana` | `action_buat_revisi()` | plan |
| `catat_realisasi` | ORM `create` + `_check_alasan()`, `_check_bukti()`, `_check_pic()` | realisasi |

### 3.2 Query

| Operasi SSD | Method / mekanisme | Model |
|---|---|---|
| `daftar_dokumen(filter, user_id)` | ORM `search` dengan domain per filter (menu atau *filter* di list view) | approval.mixin (per model) |
| `rincian_dokumen`, `status_dokumen` | ORM `read` (field + `log_ids`) | approval.mixin |
| `cek_kelengkapan` | `get_kelengkapan()` → `_cek_kelengkapan()` | approval.mixin |
| `daftar_dokumen_induk`, `rincian_versi` | ORM | document, document.version |
| `info_versi` | `get_info_versi()` | document |
| `daftar_jadwal_tinjau` | `daftar_jadwal_tinjau(user)` | document.version |
| `rincian_tinjau`, `status_tinjau` | ORM `read` (+ `status_kemutakhiran` compute) | document.version |
| `daftar_rencana`, `rincian_rencana` | ORM | plan |
| `status_item_rencana` | `get_status_item()` | plan |
| `status_gap` | `get_status_gap()` | plan |
| `daftar_item_pic` | `daftar_item_pic(user, periode_lapor)` | plan.line |
| `rincian_item` | ORM | plan.line |
| `capaian_item` | `get_capaian(periode_lapor)` | plan.line |
| (DTO) `pengesah_berwenang*`, `penerima_pemberitahuan` | `cari_pemegang_berwenang(tindakan, jenis)` | jabatan |
| (UC-29) persentase PKG-02 | `persentase_memenuhi()` | document |
| (UC-29) K1–K4 | `kriteria_tertinggi` (compute) | criteria.mixin |

## 4. Aturan bisnis → mekanisme Odoo

| Aturan | Mekanisme | Tempat |
|---|---|---|
| AB-01 kelengkapan | `_cek_kelengkapan()` dipanggil `action_ajukan()` | approval.mixin + override |
| AB-02 wewenang | `_cek_wewenang()` → `jabatan.punya_wewenang()` | approval.mixin |
| AB-03 berkas TTD | pengecekan di `action_sahkan()` | approval.mixin |
| AB-04 satu versi berlaku | `_setelah_disahkan()` | document.version |
| AB-05 alasan wajib | parameter wajib `action_tarik/kembalikan/cabut` (lewat *wizard*) | approval.mixin |
| AB-06 tidak bisa diubah setelah diajukan | `write()` ditolak bila `state ≠ draf` (kecuali field sistem) | approval.mixin |
| AB-07 rekaman bukti tidak dihapus | `unlink()` ditolak [KONFIRMASI] | evidence.mixin |
| AB-08 jadwal tinjau | `_compute_tanggal_tinjau()`, `_perbarui_tanggal_tinjau()` | document.version, review |
| AB-09 pemeriksaan wajib | pengecekan di `action_sahkan()` + pengaturan per jenis | approval.mixin |
| AB-10–12 realisasi | `@api.constrains` `_check_alasan()`, `_check_bukti()`, `_check_pic()` | realisasi |
| AB-13 satu versi diproses | `@api.constrains` `_check_satu_versi_diproses()` | document.version |
| AB-14 satu dokumen berlaku per jenis dan periode | `_setelah_disahkan()` | plan, assignment |
| «unique» | `_sql_constraints` | jabatan, document, kpi, sasaran.renstra, assignment, ruang |

## 5. Perubahan dibanding class diagram v1

| v1 | DCD | Alasan |
|---|---|---|
| Referensi ke Personel ditulis `pic_id: Personel` tanpa garis | Asosiasi berarah dengan label nama field | Dari conceptual model (§10.4); arah dari §13.6 |
| Riwayat pengesahan tidak ada | `labfik.approval.log` | CM-1, §9.3.2 |
| Status: draf, diajukan, diperiksa, disahkan, diganti, dicabut | Ditambah **kedaluwarsa** | S1 |
| Method pengesahan: ajukan, periksa, sahkan, cabut | Ditambah tarik, kembalikan, catat_pengembalian, lampirkan_ttd, get_kelengkapan, `_catat_log`, hook `_setelah_disahkan` | S1, SSD |
| `action_sahkan()` di-*override* di versi | Hook `_setelah_disahkan()` (Template Method) | Pengecekan inti tidak bisa terlewat |
| Field `pencatat_id`, `tanggal_ttd`, `nama_penanda_tangan` tidak ada | Ada di mixin dan log | Kamus DTO SSD |
| Field tinjau ulang di `controlled.mixin` | Di `document.version` | Hanya SOP/IK yang punya S2 |
| `tinjauan` mewarisi `period.mixin` | Tidak lagi | Tinjauan melekat ke rencana |
| `document.version.action_sahkan()` | `document.action_buat_versi()`, `version.daftar_jadwal_tinjau()`, `_cron_kirim_pengingat_tinjau()` | SSD-5, SSD-6, UC-32 |
| Jabatan: `get_pemegang_aktif`, `punya_wewenang` | Ditambah `cari_pemegang_berwenang()` | `pengesah_berwenang*` di SSD |
| KPI, plan.line tanpa method | `get_capaian()`, `daftar_item_pic()`, `_cron_kirim_pengingat_realisasi()` | SSD-8, KF-43 |

## 6. Isu terbuka

- [x] ~~`labfik.personel` vs `hr.employee` vs model Rafika~~: dipakai `labfik.personel` (model sendiri). Kelompok diperkirakan mengikuti rancangan ini **[ASUMSI, 13 Nov 2026]**. Bila nanti berubah ke `hr.employee`, kelas ini menjadi ekstensi `_inherit = 'hr.employee'` dan semua asosiasi tetap sama.
- [ ] Mixin ditempatkan di `labfik_core` agar bisa dipakai modul lain (mis. pengesahan rencana pelatihan PKG-14)?
- [ ] `pencatat_id` (KaLab atas nama Dekan) bergantung pada jawaban "apakah Dekan login" **[KONFIRMASI]**.
- [ ] AB-07 (rekaman bukti tidak dihapus) **[KONFIRMASI]**.
