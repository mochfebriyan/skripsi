# Kontrak Core untuk Modul SDM & Kompetensi

15 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF, versi 2.** Langkah 3 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). Bahan kerja: dipakai di Langkah 9–10 (conceptual model dan DCD), dan diteruskan ke pemilik Core (Febriyan), pemilik Mata Kuliah/Kelas/Sesi (Herrens), serta kelompok lain yang ingin tahu model SDM. Tidak ada diagram di dokumen ini.

**Isi dokumen:**
1. Model Core yang **dipakai** SDM, lengkap dengan atributnya (bagian 2).
2. Model Core yang **diperluas** SDM dengan `_inherit` tanpa `_name` baru (bagian 3).
3. Model **baru** di addon `labfik_sdm`: mewarisi *mixin* apa dan atributnya apa saja (bagian 4–5).

Lalu isu kontrak, yang disediakan SDM ke modul lain, dan dependensi addon (bagian 6–8).

**Prinsip dari pengguna (14 November 2026):** Core **tidak diubah**. Modul SDM hanya memakai, mewarisi, atau memperluas Core dari addon `labfik_sdm`. Kebutuhan yang tidak bisa dipenuhi tanpa mengubah Core diajukan sebagai usulan ke pemiliknya.

**Status atribut.** Atribut model SDM di bagian 3–5 adalah **[USULAN PENULIS]**, diturunkan dari KF-SDM-01–43 ([kebutuhan-sdm.md](kebutuhan-sdm.md)) dan *use case* ([use-case-sdm.md](use-case-sdm.md)). Nama dan tipe final ditetapkan di Langkah 10 (DCD). Atribut Core di bagian 2 disalin dari rancangan pemiliknya dan **tidak** diusulkan ubah oleh SDM.

---

## 0. Perubahan dibanding versi 1

Versi 1: 14 November 2026, commit `6a99fc5`, hanya peta mixin dan isu K-1–K-6.

| Versi 1 | Versi 2 | Alasan |
|---|---|---|
| Daftar model SDM tanpa atribut | Katalog atribut per model (bagian 2–5) | Permintaan pengguna; bahan bersama untuk kelompok lain |
| K-5: Kelas, MK, Sesi diusulkan ke Core dengan field minimum versi SDM; status Sesi {terjadwal, terlaksana, batal} | Memakai kontrak Herrens (brief Praktikum, 14 Nov 2026); status Sesi mengikuti S1 Praktikum {rencana, terpublikasi, ditunda, terlaksana, diganti, dibatalkan} | Kelas/MK/Sesi sudah dikontrakkan oleh pemiliknya |
| `labfik.sdm.seleksi.memenuhi_syarat_nilai` {compute} | Dihapus | Ambang nilai MK tidak dirancang (kebutuhan bagian 5 dan 7.5) |
| Anak Rencana Pelatihan disebut "anak kebutuhan/item" tanpa nama | `labfik.sdm.kebutuhan.pelatihan`, `labfik.sdm.item.pelatihan` | Perlu nama model untuk kontrak |
| Tidak ada model Orientasi | `labfik.sdm.orientasi` (Pelengkap) | Terlewat di versi 1 (kebutuhan bagian 7.4) |
| Keputusan evaluasi ulang tanpa *tetap berlaku* | Ditambah `tetap_berlaku` **[KONFIRMASI KP-1]** | Temuan tabel status × transisi S2 (proses bisnis bagian 4.2) |
| Dependensi `labfik_praktikum` → `labfik_sdm` wajib | Opsional; Herrens mengusulkan `labfik_praktikum` cukup `depends: ['labfik_core', 'survey']` | Brief Praktikum bagian "Dampak ke rencana addon" |
| — | Pemetaan *hook* SDM yang dijalankan di dalam *use case* pengesahan Tata Kelola (bagian 5) | Temuan langkah 6 (KU-4) |

---

## 1. Aturan yang dipakai

| Aturan | Sumber | Penerapan |
|---|---|---|
| Komponen yang sudah bekerja **tertutup untuk diubah, terbuka untuk diperluas** (*open-closed*) | Wazlawick §4.7.1 | Core tidak diubah. `labfik_sdm` memakai `_inherit` pada `hr.job`/`hr.employee`, `selection_add` pada jenis dokumen wewenang, dan data *seed* |
| ***Specification class***: atribut yang sama untuk semua *exemplar* ditaruh di kelas spesifikasi; atribut yang berbeda per *exemplar* di kelas *exemplar* | §11.3 | **Kompetensi** = spesifikasi; **Bukti Kompetensi** = *exemplar* milik satu personel (nomor, penerbit, masa berlaku). Syarat di Jabatan merujuk spesifikasi, bukan *exemplar* |
| Pasangan tanggal awal–akhir adalah satu **interval**; objek yang berlaku sementara memakai pola ***effectivity*** | §11.11, §11.12.1 | Masa berlaku Bukti Kompetensi dan Otorisasi, serta rentang berlaku baris Penugasan, ditulis sebagai interval tanggal milik objeknya sendiri, bukan `periode_id` ([K-3](#k-3-periodmixin-tidak-cocok-untuk-masa-berlaku-perorangan)) |
| ***Superseding***: objek baru menggantikan objek lama tanpa menghapusnya | §11.9.2 | Otorisasi baru mengganti yang lama lewat *hook* `_dokumen_diganti()` di `approval.mixin` |
| Tanggung jawab diberikan ke objek yang memegang datanya (**delegasi**) | §13.2 (Tabel 13–1) | Cek wewenang didelegasikan ke `hr.job.punya_wewenang()` (Core). Cek kompetensi didelegasikan ke personel (`hr.employee`, diperluas SDM), bukan ke Penugasan atau Otorisasi |
| Konsep kejadian 0..1 boleh menjadi field di desain; kejadian * menjadi model sendiri | §13.6; contoh DCD Tata Kelola bagian 3 | Keputusan evaluasi ulang (0..1) menjadi field di `labfik.sdm.evaluasi.otorisasi`; realisasi dan evaluasi pelatihan (*) menjadi model sendiri |
| Field warisan *mixin* tidak ditulis ulang | CLAUDE.md bagian 5 | Tabel atribut di bagian 4 hanya memuat field milik model itu; field warisan disebut di kolom "Mewarisi" |
| Grup akses tidak sama dengan aktor | §4.2 | SDM memakai grup Core `labfik_laboran` dan `labfik_kalab`; wewenang mengesahkan tetap lewat Jabatan |

**Notasi tipe** (mengikuti DCD Tata Kelola): `M2O` = Many2one, `O2M` = One2many, `M2M` = Many2many, `[0..1]` = boleh kosong, `{compute}` = dihitung, `{related}` = ikut field lain, «unique» = `_sql_constraints`. Label model: **[M]** master, **[T]** transaksi, **[R]** report (pedoman pengisian bagian 4).

---

## 2. Model Core yang dipakai SDM

Sumber atribut:
- `hr.*`, ruang, periode, *mixin*, grup: DCD Tata Kelola (`origin/febriyan-skripsi`, `design-class-tata-kelola.md` dan `design_class.py`, 14 Nov 2026).
- Mata Kuliah, Kelas, Sesi: brief Praktikum bagian "Kontrak Core" butir d (`origin/herrens-skripsi`, 14 Nov 2026).
- `kapasitas` Ruang: usulan Herrens **[KONFIRMASI kelompok]**.

Semua model di bagian ini ada di addon `labfik_core` (`depends: ['hr', 'mail']`).

### 2.1 Master orang dan organisasi

**`hr.employee`** · Personel [M] · model Odoo CE `hr`, diperluas Core

| Atribut | Tipe | Asal | Dipakai SDM untuk |
|---|---|---|---|
| `name` | Char | Bawaan Odoo | Semua rujukan orang |
| `job_id` | M2O `hr.job` | Bawaan Odoo | Syarat kompetensi jabatan (S3 PKG-04, gap PKG-14) |
| `user_id` | M2O `res.users` [0..1] | Bawaan Odoo | Pejabat tanpa akun (Dekan, Wadek) tidak punya `user_id` |
| `jenis_personel` | Selection {dosen, laboran_plp, teknisi, asisten, petugas_k3} | Core | Filter PKG-10 (`laboran_plp`); PKG-14 (`laboran_plp`, `teknisi`); asisten dibuat dengan `asisten` |
| `unit` | Selection | Core | — |
| `unlink()` «override» | — | Core (AB-23 TK) | Personel yang sudah dirujuk tidak dihapus, hanya diarsipkan |

**`hr.job`** · Jabatan [M] · model Odoo CE `hr`, diperluas Core

| Atribut / method | Tipe | Dipakai SDM untuk |
|---|---|---|
| `unit` | Selection {lab_fik, prodi_if, prodi_si, fakultas} | — |
| `is_eksternal` | Boolean | Wadek/Koor Prodi sebagai pengesah tanpa akun |
| `atasan_id`, `pengganti_id` | M2O `hr.job` [0..1] | — |
| `syarat_kompetensi` | Text [0..1] | Tidak dipakai untuk hitungan; tetap uraian naratif ([K-1](#k-1-syarat_kompetensi-di-core-berupa-teks)) |
| `tugas_ids` | O2M `labfik.jabatan.tugas` | — |
| `wewenang_ids` | O2M `labfik.jabatan.wewenang` | Pengesah Surat Tugas, Otorisasi, Rencana Pelatihan |
| `is_lengkap` | Boolean {compute} | — |
| `punya_wewenang(tindakan, jenis)` | → bool | Dipanggil `approval.mixin._cek_wewenang()` (KF-SDM-43) |
| `cari_pemegang_berwenang(tindakan, jenis)` | @model → `hr.employee` | Daftar pengesah berwenang saat Sahkan Dokumen |

Data awal Core: Kepala Laboratorium, Laboran, Teknisi, **Asisten Praktikum**, Dekan (eksternal), Ketua Jurusan (eksternal).

**`labfik.jabatan.wewenang`** · Wewenang Jabatan [M] · anak `hr.job`

| Atribut | Tipe | Catatan |
|---|---|---|
| `jabatan_id` | M2O `hr.job` | — |
| `tindakan` | Selection {menyusun, mengesahkan} | — |
| `jenis_dokumen` | Selection | Diperluas SDM dengan `selection_add` (bagian 3, [K-2](#k-2-jenis-dokumen-sdm-belum-terdaftar)) |
| «unique» | (jabatan_id, tindakan, jenis_dokumen) | — |

### 2.2 Master tempat, waktu, dan akademik

| Model | Label | Atribut | Dipakai SDM untuk |
|---|---|---|---|
| `labfik.ruang` | Ruang Lab [M] | `kode` Char, `name` Char, `kapasitas` Integer (usulan Herrens) | Sasaran penugasan **laboran per ruang** (A10); laboran sesi dibaca dari ruang sesi |
| `labfik.periode` | Periode [M] | `name` Char, `jenis` Selection (semester / tahun anggaran), `tanggal_mulai` Date, `tanggal_selesai` Date | Periode seleksi dan Surat Tugas (semester), Rencana Pelatihan (tahunan), periode monev |
| `labfik.mata.kuliah` | Mata Kuliah [M] | `kode` Char «unique», `name` Char, `prodi`, `semester` | Seleksi asisten per MK |
| `labfik.kelas` | Kelas [M] | `mata_kuliah_id` M2O, `periode_id` M2O, `name` Char, `jumlah_mahasiswa` Integer, `dosen_koordinator_id` M2O `hr.employee`, `dosen_ids` M2M `hr.employee`; «unique» (MK, periode, nama) | Kebutuhan Petugas, baris penugasan asisten |

Mata Kuliah dan Kelas diisi modul Praktikum (impor alokasi). SDM hanya membaca.

### 2.3 Transaksi Core: Sesi

**`labfik.sesi`** · Sesi Praktikum [T] · satu-satunya transaksi di Core, tidak mewarisi `op.session`

| Atribut | Tipe | Dipakai SDM untuk |
|---|---|---|
| `kelas_id` | M2O `labfik.kelas` | Mencari asisten (baris penugasan per kelas) dan kebutuhan petugas |
| `pertemuan_ke` | Integer | Tampilan Daftar Petugas per Sesi |
| `jenis_pertemuan` | Selection {praktikum, uts, uas} | — |
| `moda` | Selection {luring, daring} | — |
| `tanggal`, `jam_mulai`, `jam_selesai` | Date, Float, Float | Tanggal acuan S2–S3 (penugasan dan kompetensi berlaku pada tanggal sesi) |
| `ruang_id` | M2O `labfik.ruang` | Mencari laboran (baris penugasan per ruang) |
| `state` | Selection {rencana, terpublikasi, ditunda, terlaksana, diganti, dibatalkan} (S1 Praktikum) | **Penyebut PKG-04 = sesi `terlaksana`** |
| `sesi_asal_id` | M2O `labfik.sesi` [0..1] | — |

**Aturan pakai bersama dari Herrens** (diikuti SDM): modul lain **tidak menambah field** ke `labfik.sesi`; hanya Praktikum yang mengubah statusnya. SDM tidak menulis ke Sesi. Bila `state` belum diisi PKG-18 saat implementasi, sesi `terpublikasi` yang tanggalnya sudah lewat dianggap terlaksana **[ASUMSI]** (kebutuhan KF-SDM-12).

### 2.4 Mixin dan riwayat pengesahan

Model SDM yang mewarisi *mixin* mendapat semua atribut dan method di bawah tanpa menulisnya ulang.

**`labfik.approval.mixin`** · AbstractModel · siklus pengesahan (S1 Tata Kelola)

| Atribut | Tipe |
|---|---|
| `state` | Selection {draf, diajukan, disahkan, diganti, dicabut, kedaluwarsa} = draf |
| `penyusun_id` | M2O `hr.employee` |
| `tanggal_ajukan` | Datetime (readonly) |
| `berkas_ttd` | Binary [0..1] |
| `pengesah_id` | M2O `hr.employee` [0..1] (readonly) |
| `pencatat_id` | M2O `res.users` [0..1] (readonly) |
| `tanggal_sah` | Date [0..1] (readonly) |
| `log_ids` | `labfik.approval.log` [*] {compute} |

| Method | Jenis | Diisi model SDM? |
|---|---|---|
| `action_ajukan()`, `action_unggah_ttd(berkas)`, `action_kembalikan(alasan)`, `action_sahkan(pengesah, tanggal_sah)`, `action_cabut(alasan)`, `action_terbitkan()` | Publik; Template Method, **tidak di-override** | Tidak |
| `get_kelengkapan()`, `get_pengesah_berwenang()` | Publik | Tidak |
| `_jenis_dokumen()` | {abstract} | **Ya** |
| `_cek_kelengkapan()` | {abstract} | **Ya** |
| `_sebelum_ajukan()`, `_sebelum_disahkan()`, `_dokumen_diganti()`, `_setelah_disahkan()` | {hook} | Bila perlu (bagian 5) |
| `_cek_wewenang(pengesah)`, `_ubah_status(...)` | Internal | Tidak |

**`labfik.approval.log`** · Riwayat Pengesahan [T]: `res_model` Char, `res_id` Integer, `kejadian` Selection {diajukan, dikembalikan, berkas_diunggah, disahkan, diganti, dicabut, kedaluwarsa}, `waktu` Datetime, `pelaku_id` M2O `res.users`, `pengesah_id` M2O `hr.employee`, `alasan` Text, `berkas` Binary. Tidak bisa diubah atau dihapus. SDM tidak menulis langsung; log dibuat oleh `approval.mixin`.

**`labfik.period.mixin`** · AbstractModel: `periode_id` M2O `labfik.periode`; `tanggal_mulai`, `tanggal_selesai` Date {related}; `is_berlaku` Boolean {compute}; `berlaku_pada(tanggal)` → bool; `_cron_kedaluwarsakan()` (Pelengkap Tata Kelola).

**`labfik.criteria.mixin`** · AbstractModel: `kriteria_tertinggi` Integer {compute}; `get_kriteria(tanggal_acuan)` → dict (berhenti di kriteria pertama yang gagal); `_cek_k1(tanggal)` … `_cek_k4(tanggal)` {abstract}.

**`labfik.evidence.mixin`** · AbstractModel: `tanggal` Date, `pelapor_id` M2O `hr.employee`, `bukti_ids` M2M `ir.attachment`, `keterangan` Text [0..1]; `action_koreksi(nilai, alasan)`; `unlink()` «override» selalu ditolak; `_boleh_dikoreksi()` {hook}.

### 2.5 Grup akses

| Grup | Mewarisi | Dipakai SDM |
|---|---|---|
| `labfik_pengguna` | `base.group_user` | Tidak ada hak khusus SDM |
| `labfik_laboran` | `labfik_pengguna` | Laboran/PLP: mencatat seleksi, bukti kompetensi, asesmen, evaluasi ulang, realisasi, evaluasi efektivitas; menyusun draf Surat Tugas |
| `labfik_kalab` | `labfik_laboran` | KaLab: master Kompetensi dan Tugas/Alat, syarat jabatan, kebutuhan petugas, otorisasi, rencana pelatihan; kembalikan, sahkan, cabut; status monev |

Herrens menambah usulan grup `labfik_dosen` dan `labfik_asisten` untuk Praktikum. SDM tidak memakainya, karena asisten bukan aktor modul SDM.

### 2.6 Yang tidak dipakai

| Model / mixin | Alasan |
|---|---|
| `labfik.controlled.mixin` | Dihapus dari kontrak Core (keputusan Febriyan, 14 Nov 2026); SDM tidak membutuhkannya |
| `labfik.jabatan.tugas` | Uraian tugas jabatan adalah wilayah PKG-03 |
| `period.mixin` untuk Otorisasi, Bukti Kompetensi, Penugasan | Masa berlaku perorangan ([K-3](#k-3-periodmixin-tidak-cocok-untuk-masa-berlaku-perorangan)) |
| Model `labfik_org` (Dokumen Induk, KPI, SK Penetapan, dll.) | `labfik_sdm` tidak bergantung ke `labfik_org` |

---

## 3. Perluasan Core oleh `labfik_sdm`

Semua perluasan ditulis di addon `labfik_sdm` memakai `_inherit` **tanpa** `_name` baru. Model aslinya tetap milik Core; tidak ada baris kode Core yang diubah.

| Model asal | Cara | Yang ditambahkan | Tipe | Alasan / KF |
|---|---|---|---|---|
| `hr.job` | `_inherit = 'hr.job'` | `syarat_kompetensi_ids` (label "Kompetensi wajib") | M2M `labfik.sdm.kompetensi` | Syarat terstruktur untuk S3 PKG-04 dan gap PKG-14 (KF-SDM-02; [K-1](#k-1-syarat_kompetensi-di-core-berupa-teks)) |
| `hr.employee` | `_inherit = 'hr.employee'` | `bukti_kompetensi_ids` | O2M `labfik.sdm.bukti.kompetensi` (`employee_id`) | Personel memegang buktinya (delegasi §13.2) |
| | | `punya_kompetensi(kompetensi, tanggal)` | → bool | Ada bukti berlaku pada tanggal itu (KF-SDM-04) |
| | | `kompetensi_kurang(tanggal)` | → recordset `labfik.sdm.kompetensi` | Selisih `job_id.syarat_kompetensi_ids` dan bukti berlaku; dipakai matriks, S3, dan isi awal kebutuhan pelatihan (KF-SDM-04, 05, 30) |
| | | `memenuhi_syarat_jabatan(tanggal)` | → bool | `kompetensi_kurang(tanggal)` kosong (S3 PKG-04) |
| `labfik.jabatan.wewenang` | `_inherit` + `selection_add` pada `jenis_dokumen` | `penugasan_petugas`, `otorisasi`, `rencana_pelatihan` | Selection | Agar `_cek_wewenang()` memeriksa pengesah dokumen SDM tanpa kode baru (KF-SDM-43; [K-2](#k-2-jenis-dokumen-sdm-belum-terdaftar)) |

**Data awal (XML `labfik_sdm`, fiktif bila berisi orang):**

| Data | Isi | Catatan |
|---|---|---|
| Baris wewenang | (Kepala Laboratorium, mengesahkan, otorisasi); (Kepala Laboratorium, mengesahkan, penugasan_petugas) **[KONFIRMASI K7]**; (Kepala Laboratorium dan/atau Wadek Bidang Keuangan dan Umum, mengesahkan, rencana_pelatihan) **[KONFIRMASI K10]** | Wadek dicatat sebagai `hr.job` dengan `is_eksternal = True`, seperti Dekan |
| Jabatan | Laboran/PLP, Teknisi Jaringan, Asisten Praktikum (bila belum ada dari `labfik_core`) | Sumber: slide PKKMB (D8a) dan keputusan Febriyan |

---

## 4. Model baru di addon `labfik_sdm`

### 4.1 Ringkasan

Semua nama mengikuti pola `labfik.sdm.<objek>` (CLAUDE.md bagian 6) dan tidak bentrok dengan nama yang sudah dipakai Tata Kelola.

| Model | Label | Mewarisi (`_inherit`) | Merujuk Core | PKG | Lapis |
|---|---|---|---|---|---|
| `labfik.sdm.kompetensi` | Kompetensi [M] | — | — | 04, 10, 14 | Inti |
| `labfik.sdm.bukti.kompetensi` | Bukti Kompetensi [T] | `labfik.evidence.mixin` | `hr.employee` | 04, 10, 14 | Inti |
| `labfik.sdm.kebutuhan.petugas` | Kebutuhan Petugas [T] | `labfik.evidence.mixin` | `labfik.kelas` | 04 | Inti |
| `labfik.sdm.seleksi` | Seleksi Asisten [T] | `labfik.evidence.mixin` | `hr.employee`, `labfik.mata.kuliah`, `labfik.periode` | 04 | Inti |
| `labfik.sdm.surat.tugas` | Surat Tugas [T] | `labfik.approval.mixin` | `labfik.periode` | 04 | Inti |
| `labfik.sdm.penugasan` | Baris Penugasan [T] | — (anak Surat Tugas) | `hr.employee`, `labfik.kelas`, `labfik.ruang` | 04 | Inti |
| `labfik.sdm.orientasi` | Orientasi Petugas [T] | `labfik.evidence.mixin` | `hr.employee` | 04 | Pelengkap |
| `labfik.sdm.tugas.khusus` | Tugas/Alat Berkewenangan Khusus [M] | — | `hr.employee` | 10 | Inti |
| `labfik.sdm.asesmen` | Asesmen Keterampilan [T] | `labfik.evidence.mixin` | `hr.employee` | 10 | Inti |
| `labfik.sdm.otorisasi` | Otorisasi [T] | `labfik.approval.mixin` (tanpa `period.mixin`) | `hr.employee` | 10 | Inti |
| `labfik.sdm.evaluasi.otorisasi` | Evaluasi Ulang Otorisasi [T] | `labfik.evidence.mixin` | `hr.employee` | 10 | Inti |
| `labfik.sdm.rencana.pelatihan` | Rencana Pelatihan [T] | `labfik.approval.mixin`, `labfik.period.mixin`, `labfik.criteria.mixin` | `labfik.periode` | 14 | Inti |
| `labfik.sdm.kebutuhan.pelatihan` | Kebutuhan Kompetensi [T] | — (anak Rencana) | `hr.employee` | 14 | Inti |
| `labfik.sdm.item.pelatihan` | Item Pelatihan [T] | — (anak Rencana) | `hr.employee` | 14 | Inti |
| `labfik.sdm.realisasi.pelatihan` | Realisasi Pelatihan [T] | `labfik.evidence.mixin` | `hr.employee` | 14 | Inti |
| `labfik.sdm.evaluasi.pelatihan` | Evaluasi Efektivitas [T] | `labfik.evidence.mixin` | `hr.employee` | 14 | Inti |
| `labfik.sdm.monev` | Status Monev SDM [R] | `AbstractModel` (layanan, tanpa tabel) | `labfik.sesi`, `labfik.periode` | 04, 10, 14 | Inti |

**Jumlah:** 16 model bertabel (2 master, 14 transaksi) + 1 layanan. Pewarisan *mixin*: `evidence` 8 model, `approval` 3 model, `period` 1, `criteria` 1.

**Laporan tanpa model sendiri** (tampilan atau QWeb dari model di atas): Matriks Kompetensi (KF-SDM-05), Daftar Petugas per Sesi (KF-SDM-13), Daftar Operator Sah (KF-SDM-27), Rekap Pelatihan Personel (KF-SDM-38), laporan bukti (KF-SDM-42).

```
labfik.evidence.mixin ──┬── bukti.kompetensi ── kebutuhan.petugas ── seleksi ── orientasi
                        ├── asesmen ── evaluasi.otorisasi
                        └── realisasi.pelatihan ── evaluasi.pelatihan
labfik.approval.mixin ──┬── surat.tugas ──◆ penugasan
                        ├── otorisasi
                        └── rencana.pelatihan ──◆ kebutuhan.pelatihan, ◆ item.pelatihan
labfik.period.mixin ────┘   (rencana.pelatihan saja)
labfik.criteria.mixin ──    (rencana.pelatihan saja)
tanpa mixin:  kompetensi [M], tugas.khusus [M]
```
(◆ = komposisi: One2many di induk + Many2one `ondelete='cascade'` di anak.)

### 4.2 Area Kompetensi

**`labfik.sdm.kompetensi`** · Kompetensi [M] · tanpa *mixin* · KF-SDM-01

| Atribut | Tipe | Keterangan |
|---|---|---|
| `name` | Char | Wajib, «unique» |
| `jenis` | Selection {pendidikan, keahlian, sertifikasi, pelatihan_fungsional} | — |
| `kode_acuan` | Char [0..1] | Mis. kode skema SKKNI |
| `keterangan` | Text [0..1] | — |
| `active` | Boolean | Arsip, pengganti hapus |
| `unlink()` «override» | — | Ditolak bila dirujuk syarat jabatan, bukti, tugas/alat, atau item pelatihan |

**`labfik.sdm.bukti.kompetensi`** · Bukti Kompetensi [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-03, 04, 21, 35

Field warisan: `tanggal` (= tanggal terbit/perolehan, sekaligus awal masa berlaku), `pelapor_id`, `bukti_ids` (berkas), `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `employee_id` | M2O `hr.employee` | Wajib; pemilik bukti |
| `kompetensi_id` | M2O `labfik.sdm.kompetensi` | Wajib |
| `jenis_bukti` | Selection {pendidikan, pelatihan, sertifikasi, pengalaman, demonstrasi} | `demonstrasi` dibuat dari asesmen; `pelatihan` dari evaluasi efektivitas |
| `nomor_dokumen` | Char [0..1] | — |
| `penerbit` | Char [0..1] | — |
| `berlaku_sampai` | Date [0..1] | Kosong = berlaku tanpa batas (mis. ijazah) |
| `is_berlaku` | Boolean {compute} | `tanggal ≤ hari ini` dan (`berlaku_sampai` kosong atau `≥ hari ini`) |
| `asesmen_id` | M2O `labfik.sdm.asesmen` [0..1] | Sumber bila dibuat otomatis (KF-SDM-21) |
| `evaluasi_pelatihan_id` | M2O `labfik.sdm.evaluasi.pelatihan` [0..1] | Sumber bila dibuat otomatis (KF-SDM-35) |
| `berlaku_pada(tanggal)` | → bool | Dipakai S3 PKG-04, S1 PKG-10, gap PKG-14 |

### 4.3 Area Penugasan Petugas (PKG-04)

**`labfik.sdm.kebutuhan.petugas`** · Kebutuhan Petugas [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-09 (S1)

Field warisan: `tanggal` (tanggal penetapan), `pelapor_id` (= KaLab penetap), `bukti_ids` (formulir alokasi), `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `kelas_id` | M2O `labfik.kelas` | Wajib; periode ikut kelas |
| `peran` | Selection {asisten, laboran} | — |
| `jumlah_minimal` | Integer | `≥ 0`; 0 = kelas memang tidak butuh petugas peran itu |
| `dasar_penetapan` | Text | Alasan berbasis risiko/beban kerja |
| «unique» | (kelas_id, peran) | Satu kebutuhan per kelas per peran |

**`labfik.sdm.seleksi`** · Seleksi Asisten [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-07, 08 (S4)

Field warisan: `tanggal` (tanggal seleksi), `pelapor_id`, `bukti_ids` (berita acara, KHS), `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `employee_id` | M2O `hr.employee` | Wajib. Bila calon belum ada, Personel dibuat saat simpan (`jenis_personel` = asisten, `job_id` = Asisten Praktikum) |
| `mata_kuliah_id` | M2O `labfik.mata.kuliah` | Wajib |
| `periode_id` | M2O `labfik.periode` | Wajib |
| `nilai_mk` | Char | Nilai huruf MK yang dipersyaratkan; satu-satunya data KHS yang diketik (KNF-SDM-07) |
| `skor_wawancara`, `skor_simulasi`, `skor_modul` | Float [0..1] | Komponen seleksi POB 2025 |
| `penilai_id` | M2O `hr.employee` | — |
| `keputusan` | Selection {lulus, lulus_pengecualian} | Calon tidak lulus tidak dicatat |
| `alasan_pengecualian` | Text [0..1] | Wajib bila `lulus_pengecualian` |
| `penyetuju_id` | M2O `hr.employee` [0..1] | Wajib bila `lulus_pengecualian`; pejabat yang menyetujui di atas kertas |
| «unique» | (employee_id, mata_kuliah_id, periode_id) | — |
| `create()` «override» / `_pastikan_personel()` | — | Membuat Personel asisten bila belum ada (rincian di Langkah 10) |

**`labfik.sdm.surat.tugas`** · Surat Tugas [T] · `_inherit = ['labfik.approval.mixin']` · KF-SDM-10, 11, 14, 15 (S2)

Field warisan: semua field `approval.mixin` (`state`, `penyusun_id`, `berkas_ttd`, `pengesah_id`, `tanggal_sah`, …).

| Atribut | Tipe | Keterangan |
|---|---|---|
| `name` | Char | Nomor surat |
| `periode_id` | M2O `labfik.periode` | Wajib |
| `penugasan_ids` | O2M `labfik.sdm.penugasan` | Baris surat (komposisi) |
| `berkas_komitmen` | Binary [0..1] | Pernyataan komitmen petugas (Pelengkap, KF-SDM-15) |
| `revisi_dari_id` | M2O `labfik.sdm.surat.tugas` [0..1] | Surat yang direvisi (Pelengkap, KF-SDM-14) |
| `action_buat_revisi()` | → surat baru | `copy()` + `revisi_dari_id` (Pelengkap) |

**`labfik.sdm.penugasan`** · Baris Penugasan [T] · tanpa *mixin* (sah karena suratnya disahkan) · KF-SDM-10

| Atribut | Tipe | Keterangan |
|---|---|---|
| `surat_tugas_id` | M2O `labfik.sdm.surat.tugas` | Wajib, `ondelete='cascade'` |
| `employee_id` | M2O `hr.employee` | Wajib |
| `peran` | Selection {asisten, laboran} | — |
| `kelas_id` | M2O `labfik.kelas` [0..1] | Wajib bila `peran = asisten` |
| `ruang_id` | M2O `labfik.ruang` [0..1] | Wajib bila `peran = laboran` |
| `berlaku_mulai`, `berlaku_sampai` | Date | Rentang berlaku (A6: tidak selalu mulai pertemuan 1) |
| `is_sah` | Boolean {compute} | `surat_tugas_id.state = 'disahkan'` |
| `berlaku_pada(tanggal)` | → bool | `is_sah` dan tanggal di dalam rentang. Dipakai S2 PKG-04 dan modul Praktikum (opsional) |

**`labfik.sdm.orientasi`** · Orientasi Petugas [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-16 (Pelengkap, bukti 7 PKG-04)

Field warisan: `tanggal`, `pelapor_id`, `bukti_ids`, `keterangan` (catatan).

| Atribut | Tipe | Keterangan |
|---|---|---|
| `employee_id` | M2O `hr.employee` | Petugas baru |
| `jenis` | Selection {orientasi, supervisi} | — |
| `pelaksana_id` | M2O `hr.employee` | Yang memberi orientasi atau supervisi |

### 4.4 Area Otorisasi Personel (PKG-10)

**`labfik.sdm.tugas.khusus`** · Tugas/Alat Berkewenangan Khusus [M] · tanpa *mixin* · KF-SDM-18, 19, 28

| Atribut | Tipe | Keterangan |
|---|---|---|
| `name` | Char | Wajib |
| `jenis` | Selection {tugas, alat, software} | — |
| `lokasi` | Char [0..1] | Nama alat atau ruang sebagai teks. Master Alat milik kelompok Aset, tidak dirujuk |
| `kompetensi_ids` | M2M `labfik.sdm.kompetensi` | Kompetensi yang disyaratkan |
| `masa_berlaku_bulan` | Integer | Masa berlaku standar otorisasi; mengisi awal `berlaku_sampai` |
| `pelaksana_ids` | M2M `hr.employee` (domain `jenis_personel = laboran_plp`) | **Penyebut PKG-10**: pasangan pelaksana × tugas/alat **[KONFIRMASI KB-1]** |
| `cara_pembatasan` | Selection {dikunci, akun, diawasi, lainnya} [0..1] | Pelengkap, bukti 4 PKG-10 |
| `berkas_pembatasan` | Binary [0..1] | Pelengkap |
| `active` | Boolean | Arsip |
| `unlink()` «override» | — | Ditolak bila sudah punya asesmen atau otorisasi |

Keterbatasan yang disengaja (*sweet spot*): `pelaksana_ids` tidak menyimpan riwayat. Bila KaLab mengeluarkan pelaksana, persentase periode lampau ikut berubah. Riwayat pelaksana dicatat sebagai saran pengembangan.

**`labfik.sdm.asesmen`** · Asesmen Keterampilan [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-20, 21 (S1)

Field warisan: `tanggal`, `pelapor_id`, `bukti_ids` (lembar penilaian), `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `employee_id` | M2O `hr.employee` | Wajib |
| `tugas_khusus_id` | M2O `labfik.sdm.tugas.khusus` | Wajib |
| `penilai_id` | M2O `hr.employee` | — |
| `metode` | Selection {demonstrasi, uji_praktik, tinjauan_sertifikat} | — |
| `skor` | Float [0..1] | — |
| `unsur_kritis_terpenuhi` | Boolean | — |
| `kesimpulan` | Selection {layak, belum_layak} | — |
| `catatan_pengembangan` | Text [0..1] | — |
| `bukti_kompetensi_ids` | O2M `labfik.sdm.bukti.kompetensi` (`asesmen_id`) | Hasil otomatis |
| `_buat_bukti_kompetensi()` | internal | Saat `kesimpulan = layak`: satu Bukti Kompetensi berjenis `demonstrasi` untuk setiap kompetensi tugas/alat |

**`labfik.sdm.otorisasi`** · Otorisasi [T] · `_inherit = ['labfik.approval.mixin']`, **tanpa** `period.mixin` · KF-SDM-22, 23, 24 (S2, S3)

Field warisan: semua field `approval.mixin`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `employee_id` | M2O `hr.employee` | Wajib |
| `tugas_khusus_id` | M2O `labfik.sdm.tugas.khusus` | Wajib |
| `asesmen_id` | M2O `labfik.sdm.asesmen` [0..1] | Dasar |
| `bukti_kompetensi_ids` | M2M `labfik.sdm.bukti.kompetensi` | Dasar lain (mis. sertifikat) |
| `lingkup` | Text | Lingkup dan pembatasan |
| `level` | Selection {terbimbing, mandiri} | — |
| `supervisor_id` | M2O `hr.employee` [0..1] | Wajib bila `terbimbing` |
| `berlaku_mulai`, `berlaku_sampai` | Date | Interval sendiri ([K-3](#k-3-periodmixin-tidak-cocok-untuk-masa-berlaku-perorangan)); `berlaku_sampai` diisi awal dari `masa_berlaku_bulan` |
| `is_berlaku` | Boolean {compute} | `state = disahkan` dan hari ini di dalam interval. Sub-status *Berlaku / Lewat masa berlaku* (S1 SDM) |
| `evaluasi_ids` | O2M `labfik.sdm.evaluasi.otorisasi` | — |
| `berlaku_pada(tanggal)` | → bool | Dipakai S2 dan S3 PKG-10 |

**`labfik.sdm.evaluasi.otorisasi`** · Evaluasi Ulang Otorisasi [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-25 (S4)

Field warisan: `tanggal` (= tanggal pemicu), `pelapor_id`, `bukti_ids`, `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `otorisasi_id` | M2O `labfik.sdm.otorisasi` | Wajib |
| `pemicu` | Selection {masa_berlaku_habis, alat_berubah, insiden, lama_tidak_aktif, lainnya} | Diisi saat Catat Pemicu (UC-SDM-14) |
| `status` | Selection {terbuka, diputuskan} = terbuka | S2 SDM; *Terbuka* membuat S4 gagal |
| `penilai_id` | M2O `hr.employee` [0..1] | Diisi saat Putuskan (UC-SDM-15) |
| `hasil` | Text [0..1] | — |
| `keputusan` | Selection {diperpanjang, dibatasi, naik_level, dicabut, tetap_berlaku} [0..1] | `tetap_berlaku` **[KONFIRMASI KP-1]** |
| `tanggal_keputusan` | Date [0..1] | — |
| `otorisasi_baru_id` | M2O `labfik.sdm.otorisasi` [0..1] | Otorisasi pengganti bila diperpanjang/dibatasi/naik level (penelusuran) |
| `action_putuskan(keputusan, hasil, penilai)` | Publik | Hanya bila `status = terbuka`; mengubah `status` ke `diputuskan` |

Keputusan (kejadian 0..1) sengaja ditulis sebagai field, bukan model sendiri, mengikuti perlakuan Pengesahan di DCD Tata Kelola. Di conceptual model (Langkah 9) keputusan tetap boleh digambar sebagai konsep kejadian (*modal class*, §9.3.2).

### 4.5 Area Pelatihan PLP/Laboran (PKG-14)

**`labfik.sdm.rencana.pelatihan`** · Rencana Pelatihan [T] · `_inherit = ['labfik.approval.mixin', 'labfik.period.mixin', 'labfik.criteria.mixin']` · KF-SDM-29–32, 36 (K1–K4)

Field warisan: semua field `approval.mixin`; `periode_id`, `tanggal_mulai`, `tanggal_selesai`, `is_berlaku` dari `period.mixin`; `kriteria_tertinggi` dari `criteria.mixin`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `name` | Char | Judul rencana |
| `kebutuhan_ids` | O2M `labfik.sdm.kebutuhan.pelatihan` | Komposisi |
| `item_ids` | O2M `labfik.sdm.item.pelatihan` | Komposisi |
| `kebutuhan_dibekukan` | Boolean (readonly) | `True` sejak diajukan |
| «unique» | (periode_id) untuk rencana yang belum diganti/dicabut | Satu rencana per tahun |
| `action_isi_kebutuhan()` | Publik | Mengisi awal kebutuhan dari `hr.employee.kompetensi_kurang()` setiap PLP/laboran dan teknisi aktif (KF-SDM-30) |

**`labfik.sdm.kebutuhan.pelatihan`** · Kebutuhan Kompetensi [T] · anak Rencana · KF-SDM-29, 30 (K1)

| Atribut | Tipe | Keterangan |
|---|---|---|
| `rencana_id` | M2O `labfik.sdm.rencana.pelatihan` | Wajib, `ondelete='cascade'` |
| `employee_id` | M2O `hr.employee` | Wajib |
| `kompetensi_id` | M2O `labfik.sdm.kompetensi` [0..1] | Kosong bila tidak ada gap |
| `tidak_ada_gap` | Boolean | `True` = personel tercantum tanpa kebutuhan |
| `sumber` | Selection {matriks, tambahan} | Dari isi otomatis atau ditambah KaLab |
| `keterangan` | Text [0..1] | Wajib bila `tidak_ada_gap` |

**`labfik.sdm.item.pelatihan`** · Item Pelatihan [T] · anak Rencana · KF-SDM-31, 37 (K2, K3)

| Atribut | Tipe | Keterangan |
|---|---|---|
| `rencana_id` | M2O `labfik.sdm.rencana.pelatihan` | Wajib, `ondelete='cascade'` |
| `kompetensi_id` | M2O `labfik.sdm.kompetensi` | Kompetensi sasaran |
| `jenis` | Selection {diklatfung, bimtek, sertifikasi, internal} | — |
| `materi` | Text | — |
| `peserta_ids` | M2M `hr.employee` | — |
| `penyelenggara` | Char | — |
| `anggaran` | Monetary + `currency_id` | Aturan Odoo untuk nilai uang |
| `jadwal_mulai`, `jadwal_selesai` | Date | — |
| `kriteria_keberhasilan` | Text | — |
| `status` | Selection {rencana, terlaksana, batal} = rencana | S3 SDM; label tampilan "Direncanakan" |
| `alasan_batal` | Text [0..1] | Wajib bila `batal` (Pelengkap) |
| `status_evaluasi` | Selection {menunggu_evaluasi, dievaluasi} {compute} | Sub-status terhitung (§9.3.1) |
| `realisasi_ids` | O2M `labfik.sdm.realisasi.pelatihan` | — |
| `action_batalkan(alasan)` | Publik | Hanya bila `status = rencana` (Pelengkap, UC-SDM-20) |

**`labfik.sdm.realisasi.pelatihan`** · Realisasi Pelatihan [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-33 (K3)

Field warisan: `tanggal` (tanggal pelaksanaan), `pelapor_id`, `bukti_ids` (bukti praktik/demonstrasi pascapelatihan), `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `item_id` | M2O `labfik.sdm.item.pelatihan` | Wajib; rencananya harus `disahkan` |
| `employee_id` | M2O `hr.employee` | Peserta; harus ada di `item_id.peserta_ids` |
| `penyelenggara` | Char | Diisi awal dari item |
| `durasi_jam` | Float | — |
| `berkas_sertifikat` | Binary [0..1] | Disalin ke Bukti Kompetensi bila evaluasi efektif |
| «unique» | (item_id, employee_id) | — |

Efek: realisasi pertama mengubah `item_id.status` menjadi `terlaksana`.

**`labfik.sdm.evaluasi.pelatihan`** · Evaluasi Efektivitas [T] · `_inherit = ['labfik.evidence.mixin']` · KF-SDM-34, 35 (K4)

Field warisan: `tanggal`, `pelapor_id`, `bukti_ids`, `keterangan`.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `realisasi_id` | M2O `labfik.sdm.realisasi.pelatihan` | Wajib, «unique» |
| `metode` | Selection {asesmen_ulang, penilaian_kinerja} | — |
| `skor_sebelum`, `skor_sesudah` | Float | — |
| `penilai_id` | M2O `hr.employee` | — |
| `kesimpulan` | Selection {efektif, perlu_pengembangan} | — |
| `peningkatan_layanan` | Text [0..1] | Rekaman peningkatan layanan |
| `tindak_lanjut` | Text [0..1] | Kebutuhan berikutnya |
| `_buat_bukti_kompetensi()` | internal | Saat `efektif`: Bukti Kompetensi berjenis `pelatihan` untuk `item_id.kompetensi_id`, berkas dari `berkas_sertifikat` |

### 4.6 Status monev

**`labfik.sdm.monev`** · Status Monev SDM [R] · `AbstractModel` (layanan, tanpa tabel), pola sama dengan `labfik.org.monev` · KF-SDM-12, 26, 36, 40–42

| Method | Isi |
|---|---|
| `get_status(tanggal_acuan)` → dict | Ringkasan tiga indikator untuk UC-SDM-22 |
| `@model status_sesi(periode)` → list | PKG-04: untuk setiap `labfik.sesi` `terlaksana`, cek S1 (kebutuhan kelas ada), S2 (`penugasan.berlaku_pada(tanggal sesi)` memenuhi jumlah minimal; asisten lewat kelas, laboran lewat ruang), S3 (`hr.employee.memenuhi_syarat_jabatan(tanggal sesi)`), S4 (seleksi lulus untuk MK kelas) |
| `@model status_pasangan(tanggal)` → list | PKG-10: untuk setiap pasangan `tugas.khusus.pelaksana_ids`, cek S1 (bukti kompetensi berlaku), S2 (`otorisasi.berlaku_pada()`), S3 (supervisor berwenang bila terbimbing), S4 (tidak ada evaluasi `terbuka`) |
| `@model hitung_persentase(unit)` → float | Persentase unit memenuhi |
| PKG-14 | Didelegasikan ke `labfik.sdm.rencana.pelatihan.get_kriteria()` (`criteria.mixin`) |
| `action_laporan_bukti()` | QWeb PDF tiga indikator + rekaman pendukung (orientasi, pembatasan akses) **[KONFIRMASI KU-3]** |

---

## 5. Hook dan method abstrak yang diisi model SDM

Urutan Template Method `action_ajukan()` dan `action_sahkan()` milik Core **tidak di-override**. Model SDM hanya mengisi method di tabel ini. Karena UC-01 Ajukan dan UC-05 Sahkan adalah *use case* Tata Kelola, isi *hook* inilah cara KF *hidden* SDM berjalan di dalam *use case* modul lain ([use-case-sdm.md](use-case-sdm.md) bagian 7.1).

| Model | `_jenis_dokumen()` | `_cek_kelengkapan()` | `_sebelum_ajukan()` | `_dokumen_diganti()` | `_cek_k1()`–`_cek_k4()` |
|---|---|---|---|---|---|
| `labfik.sdm.surat.tugas` | `penugasan_petugas` | ≥1 baris; tiap baris punya personel, peran, kelas/ruang sesuai peran, rentang; tiap asisten punya seleksi lulus untuk MK kelasnya (KF-SDM-11, KB-3) | — | `revisi_dari_id` (Pelengkap) | — |
| `labfik.sdm.otorisasi` | `otorisasi` | Kompetensi tugas/alat terbukti (asesmen *layak* atau bukti berlaku); `lingkup` terisi; bila `terbimbing`, supervisor ada dan punya otorisasi `mandiri` berlaku untuk tugas/alat yang sama (KF-SDM-23); `berlaku_sampai ≥ hari ini` (kandidat AB dari S1) | — | Otorisasi `disahkan` lain untuk pasangan (employee, tugas/alat) yang sama (KF-SDM-24, *superseding*) | — |
| `labfik.sdm.rencana.pelatihan` | `rencana_pelatihan` | Setiap PLP/laboran dan teknisi aktif tercantum di kebutuhan; setiap item lengkap; kompetensi sasaran item termasuk kebutuhan pesertanya (KF-SDM-32) | **Bekukan kebutuhan** (`kebutuhan_dibekukan = True`) | Kosong (revisi tidak dirancang, KU-2) | K1 rencana disahkan + kebutuhan lengkap; K2 item lengkap sesuai gap; K3 setiap item tidak batal punya realisasi; K4 setiap realisasi punya evaluasi |

`_sebelum_disahkan()` dan `_setelah_disahkan()` tidak diisi model SDM.

Pada model `evidence.mixin`, `_boleh_dikoreksi()` tidak diisi (semua rekaman SDM boleh dikoreksi dengan alasan). Satu pengecualian: `keputusan` di Evaluasi Ulang hanya ditulis lewat `action_putuskan()`.

---

## 6. Isu kontrak dan keputusan

### K-1 `syarat_kompetensi` di Core berupa teks

**Masalah.** Core mendefinisikan `hr.job.syarat_kompetensi: Text [0..1]`. Teks tidak bisa dipakai untuk menghitung S3 PKG-04 atau gap PKG-14.

**Keputusan [USULAN PENULIS].** Core tetap. `labfik_sdm` menambah `syarat_kompetensi_ids` (M2M, bagian 3).

| Field | Pemilik | Makna | Dipakai oleh |
|---|---|---|---|
| `syarat_kompetensi` (Text) | Core | Uraian naratif untuk dokumen struktur/SK (PKG-03) | Tata Kelola |
| `syarat_kompetensi_ids` (M2M) | SDM | Daftar Kompetensi yang wajib dimiliki; dasar perhitungan | SDM |

Risiko: dua field bernama mirip bisa tidak selaras. Mitigasi: label dibedakan ("Uraian syarat kompetensi" dan "Kompetensi wajib"); form SDM hanya menampilkan field terstruktur. **[KONFIRMASI Febriyan, KC-1]**

### K-2 Jenis dokumen SDM belum terdaftar

**Masalah.** `_cek_wewenang()` memanggil `punya_wewenang('mengesahkan', self._jenis_dokumen())`, sedangkan pilihan `jenis_dokumen` baru berisi jenis dokumen Tata Kelola.

**Keputusan.** `selection_add` di `labfik_sdm` (bagian 3). Ini mekanisme standar Odoo untuk memperluas *Selection* dari addon lain. **[KONFIRMASI Febriyan, KC-2]**: `jenis_dokumen` memang `fields.Selection` dan tidak di-*hardcode* di method lain. Herrens juga mengusulkan jenis baru (`jadwal_praktikum`, `pemakaian_lab`, `perubahan_sesi`, `survei_kepuasan`) dan tindakan baru (`menyetujui`, `menetapkan`). Sebaiknya kedua modul memakai cara yang sama, yaitu `selection_add` dari addon masing-masing.

### K-3 `period.mixin` tidak cocok untuk masa berlaku perorangan

**Masalah.** `period.mixin` menautkan dokumen ke satu `labfik.periode` bersama. Masa berlaku otorisasi dihitung per orang sejak disahkan (mis. 12 bulan). Hal yang sama berlaku untuk Bukti Kompetensi (sertifikat BNSP 3 tahun sejak terbit, A13) dan baris Penugasan (mulai pertemuan 5, A6).

**Keputusan [USULAN PENULIS].** Ketiga model **tidak** memakai `period.mixin`. Masa berlaku menjadi interval tanggal milik objek (§11.11, §11.12.1), dengan `is_berlaku` {compute} dan `berlaku_pada(tanggal)`. Konsekuensinya:
- Otorisasi tidak otomatis `kedaluwarsa`; S2 PKG-10 memakai `is_berlaku`, bukan `state`. Prinsip "hitung, bukan jadwalkan".
- Operasi interval ditulis tiga kali. Bila mengganggu, `labfik_sdm` boleh membuat mixin lokal `labfik.sdm.interval.mixin`, di modul SDM, bukan Core.
- `period.mixin` tetap dipakai Rencana Pelatihan (satu rencana per tahun).

### K-4 Lokasi grup akses

**Masalah.** Grup didefinisikan di DCD Tata Kelola, tetapi tabel kontrak Core di CLAUDE.md tidak menyebutnya. `action_sahkan()` di Core memeriksa `labfik_kalab`, jadi grup itu harus ada di Core.

**Keputusan.** SDM mengasumsikan `labfik_pengguna`, `labfik_laboran`, `labfik_kalab` ada di `labfik_core` **[ASUMSI; KONFIRMASI Febriyan, KC-3]**. SDM tidak membuat grup sendiri.

### K-5 Kelas, Mata Kuliah, dan Sesi di Core

**Status (15 Nov 2026): terjawab sebagian.** Herrens sudah menulis kontrak ketiganya (bagian 2.2–2.3). CLAUDE.md bagian 6 mencatatnya sebagai keputusan Herrens, 14 November 2026.

Yang masih perlu disepakati:
- Nama model `labfik.mata.kuliah`, `labfik.kelas`, `labfik.sesi` masih [USULAN PENULIS] di CLAUDE.md.
- SDM membaca `state = 'terlaksana'`, nilai yang dipakai S1 Praktikum. Bila Herrens mengganti nama status, `labfik.sdm.monev.status_sesi()` ikut berubah **[KONFIRMASI Herrens, KC-4]**.
- Petugas hadir di Jurnal Sesi (PKG-18) sebaiknya merujuk `hr.employee` yang sama dengan baris Penugasan, bukan teks nama (temuan A18) **[KONFIRMASI Herrens, KC-5]**.

### K-6 Surat Tugas bergaris

**Keputusan Zahir (14 November 2026).** Penugasan dicatat sebagai Surat Tugas (`approval.mixin`, disahkan sekali per periode) dengan baris `labfik.sdm.penugasan`. Ini pola yang sama dengan SK Penetapan Tata Kelola (`labfik.assignment` + `labfik.assignment.line`). Alasannya: 32 kelas berasisten ditambah laboran per ruang (A6, A10) tidak masuk akal disahkan satu per satu.

---

## 7. Yang disediakan SDM ke modul lain

| Data / method | Dipakai oleh | Sifat | Arah addon |
|---|---|---|---|
| `labfik.sdm.penugasan.berlaku_pada(tanggal)`, baris per kelas/ruang | PKG-18 (cocokkan petugas hadir), PKG-08 kelompok Aset (jumlah petugas per sesi) | Opsional | Modul pemakai `depends` ke `labfik_sdm`, atau modul jembatan |
| `hr.employee.punya_kompetensi()`, `kompetensi_kurang()`, Matriks Kompetensi | Opsional PKG-13 (gap aspek kompetensi); peluang PKG-06/11 Safety (kompetensi K3) | Opsional | `labfik_org` → `labfik_sdm`, atau modul jembatan |
| `labfik.sdm.kompetensi` | Modul lain yang butuh daftar kompetensi (mis. petugas K3) | Opsional | Sama |
| `labfik.sdm.otorisasi.berlaku_pada()` (operator sah per tugas/alat) | Peluang untuk Aset/Praktikum | Tidak dirancang sekarang | — |

Semua model SDM yang **dipakai** modul lain tetap di `labfik_sdm`, tidak dipindah ke Core. Pemindahan baru dipertimbangkan bila ada pemakai yang terkonfirmasi, mengikuti perlakuan Febriyan untuk Dokumen Induk dan KPI.

---

## 8. Dependensi addon

```
hr, mail
   └── labfik_core      hr.employee/hr.job (diperluas), jabatan.tugas/wewenang, ruang, periode,
                        mata.kuliah, kelas, sesi, 4 mixin, approval.log, grup
        ├── labfik_org         Tata Kelola       (depends: labfik_core)
        ├── labfik_sdm         SDM & Kompetensi  (depends: labfik_core)
        ├── labfik_praktikum   Praktikum         (depends: labfik_core, survey;
        │                                         + labfik_sdm bila pencocokan petugas dipakai)
        └── kelompok Aset, Safety (+ modul jembatan bila perlu)
```

`labfik_sdm` hanya bergantung ke `labfik_core`, tanpa rujukan ke `labfik_org` maupun `labfik_praktikum`. Arah Praktikum → SDM sekarang opsional (usulan Herrens) **[KONFIRMASI kelompok]**.

---

## 9. Cek silang, isu terbuka, dan koreksi

### 9.1 Cek silang

| Cek | Hasil |
|---|---|
| Setiap KF yang menyebut model punya model atau field di bagian 3–4 | ✓ KF-SDM-01–43. Laporan (05, 13, 27, 38, 42) tanpa model sendiri |
| Setiap konsep di matriks CRUDL langkah 6 punya model | ✓ 15 konsep → 16 model (Rencana Pelatihan dipecah menjadi induk + 2 anak) |
| Setiap kriteria punya field sumber | ✓ PKG-04 S1 `kebutuhan.petugas`, S2 `penugasan` + `surat.tugas.state`, S3 `bukti.kompetensi` + `hr.job.syarat_kompetensi_ids`, S4 `seleksi`; PKG-10 penyebut `tugas.khusus.pelaksana_ids`, S1–S4 `asesmen`/`bukti`, `otorisasi`, `supervisor_id`, `evaluasi.otorisasi.status`; PKG-14 K1–K4 `rencana`/`kebutuhan`/`item`/`realisasi`/`evaluasi.pelatihan` |
| Status sama dengan state machine langkah 5 | ✓ S1 Otorisasi = `approval.mixin.state` + `is_berlaku`; S2 = `status` {terbuka, diputuskan}; S3 = `item.status` {rencana, terlaksana, batal} + `status_evaluasi` |
| Nama model tidak bentrok dengan Tata Kelola | ✓ semua berawalan `labfik.sdm.` |
| Field warisan tidak ditulis ulang | ✓ |
| Data pribadi | ✓ Tidak ada nama orang, NIM, atau nomor HP; `nilai_mk` hanya nilai huruf MK yang dipersyaratkan (KNF-SDM-07) |

### 9.2 [KONFIRMASI]

| No | Pertanyaan | Ke siapa |
|---|---|---|
| KC-1 | `syarat_kompetensi` (Text, Core) dan `syarat_kompetensi_ids` (M2M, SDM) boleh berdampingan? (K-1) | Febriyan |
| KC-2 | `jenis_dokumen` adalah `Selection` yang boleh diperluas `selection_add`? (K-2) | Febriyan |
| KC-3 | Grup `labfik_pengguna/laboran/kalab` didefinisikan di `labfik_core`? (K-4) | Febriyan |
| KC-4 | Nama model dan nama status `labfik.sesi` (khususnya `terlaksana`) sudah final? (K-5) | Herrens |
| KC-5 | Petugas hadir di PKG-18 merujuk `hr.employee`? (K-5, A18) | Herrens |
| KC-8 | `labfik_praktikum` tanpa `depends` wajib ke `labfik_sdm`? (bagian 8) | Herrens, kelompok |
| KP-1, KB-1, KB-3, KU-2, KU-3 | Lihat [use-case-sdm.md](use-case-sdm.md) bagian 9.2; tercermin di field `keputusan`, `pelaksana_ids`, `_cek_kelengkapan()` Surat Tugas, `_dokumen_diganti()` Rencana, `action_laporan_bukti()` | Zahir |
| Lama | K7 (pengesah Surat Tugas), K10 (pengesah Rencana Pelatihan) menentukan baris wewenang awal | KaLab |

KC-6 (merge ke `main`) dan KC-7 (Surat Tugas bergaris) sudah diputuskan Zahir di versi 1.

### 9.3 Dokumen lain yang perlu ikut berubah

| Dokumen | Perubahan |
|---|---|
| [brief-sdm.md](../brief/brief-sdm.md) "Kontrak dengan modul lain" | Rujuk bagian 7 dokumen ini; arah Praktikum → SDM menjadi opsional |
| [analisis-data-pengelolaan-4.md](../analisis/analisis-data-pengelolaan-4.md) | `memenuhi_syarat_nilai` di Seleksi dihapus (sudah dicatat di kebutuhan 7.5) |
| [kebutuhan-sdm.md](kebutuhan-sdm.md) kolom "Model (usulan)" KF-SDM-29, 31 | Nama anak Rencana: `labfik.sdm.kebutuhan.pelatihan`, `labfik.sdm.item.pelatihan` |
| `CLAUDE.md` bagian 6 (file bersama) | Tidak diubah. Usulan untuk kelompok: tambahkan baris "Grup akses `labfik_pengguna/laboran/kalab`" ke tabel kontrak Core (K-4) |
| Pemilik Core (Febriyan) dan Praktikum (Herrens) | Kirim bagian 3 (perluasan), bagian 5 (hook), dan KC-1–KC-5, KC-8 |

### 9.4 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| Versi 1, K-5 | Status Sesi ditulis {terjadwal, terlaksana, batal} tanpa mengecek kontrak Herrens | Mengikuti S1 Praktikum (bagian 2.3) |
| Versi 1, peta mixin | `labfik.sdm.seleksi` masih punya `memenuhi_syarat_nilai` {compute}, padahal ambang nilai sudah diputuskan tidak dirancang di langkah 4 | Dihapus |
| Versi 1, peta mixin | `labfik.sdm.orientasi` terlewat | Ditambah (bagian 4.3) |
| Versi 1, bagian 5 | Dependensi `labfik_praktikum` → `labfik_sdm` ditulis wajib; analisis Herrens menunjukkan semua kaitan ke SDM opsional | Bagian 8 |
| Langkah 6 | Keputusan *tetap berlaku* dan pemecahan evaluasi ulang belum punya tempat di model | Field `keputusan` dan `status` di `labfik.sdm.evaluasi.otorisasi` |
