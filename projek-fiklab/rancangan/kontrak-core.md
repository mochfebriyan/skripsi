# Kontrak Core Bersama (`labfik_core`)

15 November 2026, diperbarui 16 November 2026 · Febriyan (rangkuman dari tiga branch + usulan kelompok Aset & Safety) · Core, dipakai PKG-01–21

**Status: DRAF.** Bahan kerja bersama, bukan bagian proposal. Dokumen ini merangkum **semua model dan mixin Core** yang sudah dirancang atau diusulkan di pekerjaan masing-masing, beserta model Odoo yang diperluas, atribut, dan method-nya. Tabel ringkas di [CLAUDE.md](../../CLAUDE.md) bagian 6 tetap berlaku sebagai ringkasan; rinciannya ada di sini.

## Sumber

| Branch (commit lokal) | Modul | File yang dibaca | Isi yang diambil |
|---|---|---|---|
| `febriyan-skripsi` (`27f8956`) | Tata Kelola & Dokumen | [design-class-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/design-class-tata-kelola.md) bagian 2.1, 4, 6, 7; skrip `design_class.py` (DCD-1, DCD-2) | Perancang mixin, `hr.employee`/`hr.job`, `labfik.jabatan.*`, `labfik.ruang`, `labfik.periode`. Sudah sampai Langkah 10 (DCD) |
| `herrens-skripsi` (`e0a8bee`) | Pelaksanaan Praktikum | `brief-praktikum.md` bagian "Kontrak Core (Langkah 3)" a–f; `proses-bisnis-praktikum.md` bagian 3.1 dan 4.4 | Perancang Mata Kuliah, Kelas, Sesi; usulan `kapasitas` ruang dan wewenang baru. Sudah sampai Langkah 5 |
| `zahir-skripsi` (`5b04786`) | SDM & Kompetensi | `kontrak-core-sdm.md` (K-1–K-6, KC-1–KC-7) | Pemakai Core; perluasan `hr.job`, `hr.employee`, `jabatan.wewenang` dari `labfik_sdm`. Sudah sampai Langkah 3 |
| Kelompok Aset & Safety (berkas, 16 November 2026) | Asset Management, Safety Management | `model-core.drawio` halaman "Model Core (Update) - Master Bersama & Aset", Baris 4 dan catatan "Aturan Pakai Bersama Domain Aset" | Usulan master aset ke Core, digabung ke diagram lewat skrip `tools/drawio/core/model_core.py`: `labfik.alat`, `labfik.alat.kategori`, `labfik.lokasi.simpan`, `labfik.bahan`; tambahan field di `hr.employee`, `labfik.ruang`, `labfik.jabatan.wewenang`. Tahap rancangan kelompok itu belum diketahui **[VALIDASI]** |

`git fetch` tidak bisa dijalankan saat penyusunan, jadi yang dibaca adalah salinan branch terakhir di laptop penyusun. Perubahan yang di-*push* sesudahnya belum tercakup **[VALIDASI]**.

**Tingkat kepastian atribut.** Hanya model rancangan Tata Kelola yang sudah melewati Langkah 10, sehingga tipe field-nya sudah final menurut rancangan. Model dari Praktikum (Mata Kuliah, Kelas, Sesi) baru sampai Langkah 3–5: nama field sudah ditetapkan pemiliknya, tetapi tipenya ditandai **[USULAN PENULIS]** dan baru ditetapkan di Langkah 10 Praktikum. Model aset (C-10–C-13) dan field tambahan dari kelompok Aset & Safety sudah **digabung** dengan isi Core yang ada (bagian 6, I-10–I-16); penempatannya di Core masih [KONFIRMASI kelompok].

---

## 1. Addon dan dependensi

```
hr, mail (Odoo 17 CE, LGPL-3)
   └── labfik_core     master bersama, perluasan hr, 4 mixin, approval.log, grup akses,
        │              mata kuliah, kelas, sesi, master aset (alat, kategori, lokasi simpan, bahan)
        ├── labfik_org         Tata Kelola (Febriyan)      depends: labfik_core
        ├── labfik_sdm         SDM & Kompetensi (Zahir)    depends: labfik_core
        │     └── labfik_praktikum   Praktikum (Herrens)   depends: labfik_core, labfik_sdm, survey (I-7)
        └── kelompok lain (aset, safety); modul jembatan bila butuh model labfik_org
```

- Arah Praktikum → SDM (keputusan Febriyan, 15 November 2026, I-7; sama dengan brief awal di pemetaan bersama). Urutan kerjanya memang Praktikum membangkitkan Sesi → SDM menugaskan petugas → Praktikum mengisi jurnal, tetapi itu **dependensi data**, bukan dependensi addon: Sesi dan Kelas ada di Core, jadi SDM menugaskan petugas cukup dengan merujuk `labfik.sesi`/`labfik.kelas` tanpa bergantung ke `labfik_praktikum`.
- Satu-satunya titik yang menyentuh kedua modul adalah pencocokan petugas yang ditugaskan dengan petugas yang hadir. Pencocokan itu dilakukan **di Praktikum** saat jurnal diisi (PKG-18), karena Praktikum yang memakai datanya. Karena itu `labfik_praktikum` bergantung ke `labfik_sdm`, dan `labfik_sdm` **tidak boleh** bergantung ke `labfik_praktikum`, supaya tidak melingkar.

- `labfik_core` hanya `depends: ['hr', 'mail']`. Tidak bergantung ke OpenEduCat (`op.session` tidak dipakai) dan tidak ke modul fungsional mana pun.
- Dokumen Induk, Versi Dokumen, dan KPI ada di `labfik_org`, **bukan** Core. Modul lain yang butuh relasi ke model itu memakai modul jembatan (mis. `labfik_safety_org`) atau mengusulkan pemindahan ke Core.

---

## 2. Daftar model Core

| # | Model | Jenis | Label | Extend / inherit | Dirancang oleh | Status rancangan |
|---|---|---|---|---|---|---|
| C-1 | `hr.employee` (Personel) | Model Odoo diperluas | [M] | `_inherit = 'hr.employee'` (tanpa `_name` baru) | Febriyan | Final (DCD-2) |
| C-2 | `hr.job` (Jabatan) | Model Odoo diperluas | [M] | `_inherit = 'hr.job'` (tanpa `_name` baru) | Febriyan | Final (DCD-2) |
| C-3 | `labfik.jabatan.tugas` | Model baru | [M] | — (anak `hr.job`) | Febriyan | Final |
| C-4 | `labfik.jabatan.wewenang` | Model baru | [M] | — (anak `hr.job`) | Febriyan | Final; pilihan `jenis_dokumen` diperluas modul lain (bagian 4) |
| C-5 | `labfik.ruang` | Model baru | [M] | — | Febriyan | Final; + `kapasitas` (I-3, disetujui 15 November 2026) |
| C-6 | `labfik.periode` | Model baru | [M] | — | Febriyan | Final |
| C-7 | `labfik.mata.kuliah` | Model baru | [M] | — | Herrens | Langkah 3; nama model [USULAN PENULIS] |
| C-8 | `labfik.kelas` | Model baru | [M] | — | Herrens | Langkah 3; nama model [USULAN PENULIS] |
| C-9 | `labfik.sesi` | Model baru | **[T]** (satu-satunya transaksi di Core) | — (**tidak** mewarisi `op.session`) | Herrens | Langkah 5; status mengikuti versi SDM (I-1), S1 Sesi Herrens perlu disesuaikan |
| M-1 | `labfik.approval.mixin` | AbstractModel | — | `_inherit = 'mail.thread'` | Febriyan | Final (DCD-1) |
| M-2 | `labfik.approval.log` | Model baru | [T] | — | Febriyan | Final |
| M-3 | `labfik.period.mixin` | AbstractModel | — | — | Febriyan | Final |
| M-4 | `labfik.criteria.mixin` | AbstractModel | — | — | Febriyan | Final |
| M-5 | `labfik.evidence.mixin` | AbstractModel | — | — | Febriyan | Final |
| C-10 | `labfik.alat` | Model baru | [M] | — | Aset (PKG-07) | Digabung 16 November 2026 [KONFIRMASI kelompok] |
| C-11 | `labfik.alat.kategori` | Model baru | [M] | — | Aset (PKG-07/08) | Digabung 16 November 2026 [KONFIRMASI kelompok] |
| C-12 | `labfik.lokasi.simpan` | Model baru | [M] | — (anak `labfik.ruang`) | Aset & Safety | Digabung 16 November 2026 [KONFIRMASI kelompok] |
| C-13 | `labfik.bahan` | Model baru | [M] | — | Aset & Safety (PKG-07/11) | Digabung 16 November 2026 [KONFIRMASI kelompok] |
| G | Grup akses `labfik_pengguna` ⊂ `labfik_laboran` ⊂ `labfik_kalab` | `res.groups` | — | `labfik_pengguna` mewarisi `base.group_user` | Febriyan | Di `labfik_core` (I-5); grup dosen dan asisten di `labfik_praktikum` |

**Tidak ada di Core:**
- `labfik.controlled.mixin`: dihapus (keputusan Febriyan, 14 November 2026). Ketiga modul sudah mencatatnya sebagai tidak dipakai.
- Mahasiswa: tercantum di pemetaan sebagai master Core, tetapi tidak dipakai modul mana pun. Praktikum mencatat praktikan hanya sebagai jumlah, atau NIM di baris nilai bila impor nilai dipakai (Pelengkap).
- Mitra Eksternal, Indikator Monev: usulan kelompok Aset/Safety di pemetaan, belum dirancang. Lokasi Penyimpanan sudah diusulkan sebagai `labfik.lokasi.simpan` (C-12).
- Transaksi aset (peminjaman, pemeliharaan, kalibrasi, afkir, stok bahan) tetap di addon Aset/Safety, bukan Core. Core hanya menyimpan masternya [ASUMSI].

---

## 3. Atribut dan method per model

Konvensi: `+` publik, `#` internal, {compute}, {related}, {abstract}, {hook}, «override». Field bawaan Odoo yang dipakai ditulis miring. Field warisan mixin tidak ditulis ulang di model turunan.

### C-1 `hr.employee` (Personel) [M]

Isinya: semua orang **internal FIK** yang punya peran di lab, yaitu dosen, laboran/PLP, teknisi, asisten, petugas K3, dan pejabat pengesah tanpa akun. Pihak eksternal tidak dicatat dan bukan aktor. Praktikan (mahasiswa peserta) **bukan** Personel.

| Field / method | Tipe | Keterangan |
|---|---|---|
| `jenis_personel` | Selection {`dosen`, `laboran_plp`, `teknisi`, `asisten`, `petugas_k3`} | Ditambahkan Core |
| `unit` | Selection | Ditambahkan Core |
| `aset_dikelola_ids` | One2many `labfik.alat` | Kebalikan `labfik.alat.penanggung_jawab_id`. Usulan Aset (16 November 2026); tipe dibetulkan dari {related} (I-11) |
| *`name`*, *`job_id`* → `hr.job`, *`user_id`* → `res.users` [0..1] | bawaan | Pejabat fakultas (mis. Dekan) = `hr.employee` **tanpa** `user_id` |
| `unlink()` «override» | — | Ditolak bila masih dirujuk; arsip lewat `active` (AB-23) |

Keputusan: asisten lab (mahasiswa) = `hr.employee` dengan `jenis_personel = asisten` dan `job_id` = **Asisten Praktikum** (Febriyan dan Herrens, 14 November 2026).

### C-2 `hr.job` (Jabatan) [M]

| Field / method | Tipe | Keterangan |
|---|---|---|
| `unit` | Selection {`lab_fik`, `prodi_if`, `prodi_si`, `fakultas`} | |
| `is_eksternal` | Boolean | Jabatan di luar lab (Dekan, Ketua Jurusan, Wadek) |
| `atasan_id` | Many2one `hr.job` [0..1] | `_cek_atasan()` @constrains: tanpa siklus |
| `pengganti_id` | Many2one `hr.job` [0..1] | Jabatan pengganti bila berhalangan |
| `syarat_kompetensi` | Text [0..1] | Uraian naratif untuk SK/struktur (PKG-03). Berdampingan dengan `syarat_kompetensi_ids` yang ditambahkan `labfik_sdm` (I-2) |
| `tugas_ids` | One2many `labfik.jabatan.tugas` | |
| `wewenang_ids` | One2many `labfik.jabatan.wewenang` | |
| `is_lengkap` | Boolean {compute} | `_compute_is_lengkap()` |
| `+ punya_wewenang(tindakan, jenis): bool` | method | Dipanggil `approval.mixin._cek_wewenang()` |
| `@model + cari_pemegang_berwenang(tindakan, jenis): hr.employee` | method | |
| `unlink()` «override» | — | AB-23 |

Data awal (*seed*, fiktif): Kepala Laboratorium, Laboran, Teknisi, **Asisten Praktikum**; jabatan eksternal Dekan, Ketua Jurusan. Praktikum juga memakai jabatan Dosen; SDM menambah Teknisi Jaringan dan Wadek Bidang Keuangan dan Umum lewat data `labfik_sdm`.

### C-3 `labfik.jabatan.tugas` [M]

| Field | Tipe |
|---|---|
| `jabatan_id` | Many2one `hr.job` (induk) |
| `urutan` | Integer |
| `uraian` | Text |

### C-4 `labfik.jabatan.wewenang` [M]

| Field | Tipe | Keterangan |
|---|---|---|
| `jabatan_id` | Many2one `hr.job` (induk) | |
| `tindakan` | Selection {`menyusun`, `mengesahkan`} | Tetap dua pilihan. "Menyetujui" dan "menetapkan" di modul lain = `mengesahkan` (I-4) |
| `jenis_dokumen` | Selection | Nilai dasar dari Tata Kelola: `sop_ik`, `renstra`, `rencana_tahunan`, `rencana_pengembangan`, `sk_penetapan`. Modul lain menambah lewat `selection_add` (bagian 4), termasuk Aset: `baso`, `usulan_disposal`, `program_pemeliharaan` (I-10) |
| — | `_sql_constraints` | unique(`jabatan_id`, `tindakan`, `jenis_dokumen`) |

Wewenang **mengesahkan sebagai pejabat** diatur di sini, bukan oleh grup akses. Karena itu Dekan tidak butuh akun.

### C-5 `labfik.ruang` [M]

| Field | Tipe | Keterangan |
|---|---|---|
| `kode` | Char «unique» | «unique» ditambahkan di diagram 16 November 2026 |
| `name` | Char | |
| `kapasitas` | Integer | Jumlah kursi mahasiswa. Usulan Herrens, **disetujui** Febriyan 15 November 2026 (I-3). Untuk cek kapasitas PKG-15 C3; juga dipakai PKG-08 (Aset) |
| `penanggung_jawab_id` | Many2one `hr.employee` [0..1] | Usulan Aset (16 November 2026) [KONFIRMASI kelompok] |
| `alat_ids` | One2many `labfik.alat` | Kebalikan `labfik.alat.ruang_id`. Usulan Aset |
| `workstation_count` | Integer {compute} | Jumlah PC. Usulan Aset; cara hitung ditetapkan Aset (I-12) |

Isi awal yang diusulkan Herrens: 8 ruang (FIKLAB-201, 301–304, 401–403) **[VALIDASI]**.

### C-6 `labfik.periode` [M]

| Field | Tipe | Keterangan |
|---|---|---|
| `name` | Char | |
| `jenis` | Selection (semester / tahun anggaran) | |
| `tanggal_mulai`, `tanggal_selesai` | Date | Usulan Herrens sudah terpenuhi oleh rancangan ini |

### C-7 `labfik.mata.kuliah` [M]

Dirancang Herrens (Langkah 3). Tipe field [USULAN PENULIS].

| Field | Tipe | Keterangan |
|---|---|---|
| `kode` | Char «unique» | Kunci impor, karena nama MK tidak seragam antarperiode |
| `name` | Char | |
| `prodi` | Selection / Char | |
| `semester` | Integer | Tidak ada di kontrak minimum Zahir; tidak bertentangan |

### C-8 `labfik.kelas` [M]

Dirancang Herrens (Langkah 3). Tipe field [USULAN PENULIS].

| Field | Tipe | Keterangan |
|---|---|---|
| `mata_kuliah_id` | Many2one `labfik.mata.kuliah` | |
| `periode_id` | Many2one `labfik.periode` | |
| `name` | Char | A, B, PBI, … |
| `jumlah_mahasiswa` | Integer | |
| `dosen_koordinator_id` | Many2one `hr.employee` | |
| `dosen_ids` | Many2many `hr.employee` | |
| — | `_sql_constraints` | unique(`mata_kuliah_id`, `periode_id`, `name`) |

Diisi pertama kali oleh Praktikum (impor dari berkas alokasi fakultas).

### C-9 `labfik.sesi` [T]

Dirancang Herrens (Langkah 3 dan state machine S1 Sesi di Langkah 5). Tipe field [USULAN PENULIS].

| Field | Tipe | Keterangan |
|---|---|---|
| `kelas_id` | Many2one `labfik.kelas` | |
| `pertemuan_ke` | Integer | Satu Sesi asli per (kelas, pertemuan) |
| `jenis_pertemuan` | Selection {`praktikum`, `uts`, `uas`} | Pertemuan 8 dan 16 tetap dibangkitkan |
| `moda` | Selection {`luring`, `daring`} | |
| `tanggal` | Date | |
| `jam_mulai`, `jam_selesai` | Float (*widget* jam) | |
| `ruang_id` | Many2one `labfik.ruang` | |
| `state` | Selection {`terjadwal`, `terlaksana`, `batal`} | Versi SDM (keputusan Febriyan, 15 November 2026, I-1) |
| `sesi_asal_id` | Many2one `labfik.sesi` [0..1] | Diisi bila sesi ini pengganti |

**Pemetaan dari S1 Sesi Herrens (6 status) ke 3 status** [USULAN PENULIS; KONFIRMASI Herrens]. Status yang bisa dihitung dari data lain tidak disimpan (*stable transition*, Wazlawick §9.3.1, aturan yang juga dipakai Herrens untuk *Terlewat*):

| Status Herrens | Menjadi | Cara membedakannya |
|---|---|---|
| Rencana | `terjadwal` | `is_terpublikasi` {compute} = Penetapan Jadwal periode itu `disahkan` |
| Terpublikasi | `terjadwal` | idem |
| Ditunda | `terjadwal` | `is_ditunda` {compute} = ada Perubahan Sesi yang masih diajukan |
| Terlaksana | `terlaksana` | Jurnal Sesi terkirim dan valid |
| Diganti | `batal` | `is_diganti` {compute} = ada sesi lain dengan `sesi_asal_id` = sesi ini |
| Dibatalkan | `batal` | Tanpa sesi pengganti |

Transisi KF-PRK-45 (jadwal dicabut → kembali Rencana) dan KF-PRK-46 (perubahan ditolak → kembali Terpublikasi) tidak lagi mengubah `state`; keduanya otomatis terbaca dari `is_terpublikasi` dan `is_ditunda`.

**Aturan pakai bersama** (Herrens, [USULAN PENULIS; KONFIRMASI kelompok]):
- Sesi hanya dibangkitkan oleh PKG-15, atau sebagai pengganti lewat Perubahan Sesi PKG-18.
- Hanya Praktikum yang mengubah `state`.
- Modul lain **tidak menambah field** ke `labfik.sesi`. Mereka membuat model sendiri yang merujuk `sesi_id`. SDM sudah menyatakan tidak menulis ke Mata Kuliah, Kelas, dan Sesi.
- Sesi yang sudah punya jurnal atau penugasan tidak boleh dihapus; perubahan jadwal lewat Perubahan Sesi.

### C-10 `labfik.alat` [M]

Usulan kelompok Aset (PKG-07), 16 November 2026 [KONFIRMASI kelompok]. Satu baris = satu unit alat.

| Field / method | Tipe | Keterangan |
|---|---|---|
| `kode_operasional` | Char «unique» | Kode QR per unit |
| `kode_bmn` | Char [0..1] | Kode barang milik negara |
| `nup` | Integer [0..1] | Nomor urut pendaftaran BMN |
| `name` | Char | |
| `kategori_id` | Many2one `labfik.alat.kategori` | |
| `ruang_id` | Many2one `labfik.ruang` | |
| `lokasi_simpan_id` | Many2one `labfik.lokasi.simpan` [0..1] | |
| `serial_number` | Char [0..1] | |
| `kondisi` | Selection {`baik`, `rusak_ringan`, `rusak_berat`} | |
| `status` | Selection {`tersedia`, `dipinjam`, `perbaikan`, `afkir`} | Hanya addon Aset yang mengubah; modul lain membaca (I-13) |
| `penanggung_jawab_id` | Many2one `hr.employee` | |
| `is_perlu_kalibrasi` | Boolean | Nilai awal dari `kategori_id.butuh_kalibrasi_internal`, bisa diubah per unit (I-14) |
| `tgl_terakhir_verifikasi` | Date [0..1] | |
| `+ action_set_tersedia()`, `+ action_set_perbaikan()` | method | |
| `+ check_ketersediaan_sesi(sesi): bool` | method {hook} | Dipakai Praktikum (PKG-15/18). Versi Core hanya memeriksa `status` dan `ruang_id`; addon Aset meng-*override* untuk menambah cek peminjaman, karena data peminjaman tidak terlihat dari Core (I-16) |

### C-11 `labfik.alat.kategori` [M]

Usulan kelompok Aset (PKG-07/08), 16 November 2026 [KONFIRMASI kelompok].

| Field | Tipe | Keterangan |
|---|---|---|
| `kode` | Char «unique» | |
| `name` | Char | |
| `jenis` | Selection {`hardware_pc`, `instrumen_ukur`, `jaringan`, `mesin_lab`, `multimedia`} | |
| `rasio_per_mahasiswa` | Float | Standar instrumen Monev PKG-08 |
| `interval_pemeliharaan_bulan` | Integer | |
| `butuh_kalibrasi_internal` | Boolean | Nilai awal untuk `labfik.alat.is_perlu_kalibrasi` (I-14) |

### C-12 `labfik.lokasi.simpan` [M]

Usulan kelompok Aset & Safety, 16 November 2026 [KONFIRMASI kelompok]. Sub-lokasi di dalam ruang (rak, meja, lemari).

| Field | Tipe | Keterangan |
|---|---|---|
| `ruang_id` | Many2one `labfik.ruang` (induk) | |
| `kode` | Char | |
| `name` | Char | |
| `jenis` | Selection {`meja_workstation`, `rak_penyimpanan`, `lemari_alat`, `lemari_b3`, `laci`} | `lemari_b3` dipakai Safety |
| `kapasitas_tampung` | Integer | |
| `keterangan` | Text [0..1] | |
| — | `_sql_constraints` | unique(`ruang_id`, `kode`) |

### C-13 `labfik.bahan` [M]

Usulan kelompok Aset & Safety (PKG-07/11), 16 November 2026 [KONFIRMASI kelompok]. Bahan habis pakai.

| Field | Tipe | Keterangan |
|---|---|---|
| `kode` | Char «unique» | |
| `name` | Char | |
| `satuan` | Char | pcs, roll, box, ml |
| `jenis` | Selection {`elektronika`, `kabel_konektor`, `cairan_kimia`, `reagen`, `atki`} | |
| `stok_minimum` | Float | Stok berjalan dan mutasi bahan di addon Aset/Safety (I-15) |
| `lokasi_simpan_id` | Many2one `labfik.lokasi.simpan` | |
| `is_berbahaya_b3` | Boolean | Penanda untuk Safety |

**Aturan pakai bersama domain aset** (dari diagram, kelompok Aset & Safety, [KONFIRMASI kelompok]):
- Praktikum (PKG-15/18) mengecek ketersediaan PC/alat lewat `labfik.alat` di ruang terkait, tanpa tabel duplikat.
- Hanya addon Aset yang mengubah `labfik.alat.status` (I-13); `check_ketersediaan_sesi()` diperluas Aset (I-16).
- Safety (PKG-11/17) memakai `labfik.alat` untuk inspeksi K3 berkala (APAR, kelistrikan) dan `labfik.lokasi.simpan` untuk lemari B3.
- Kalibrasi alat dilakukan internal oleh laboran. Bukti hasil uji dicatat lewat `labfik.evidence.mixin`, tanpa vendor luar.
- Pengesahan berita acara (BASO, usulan afkir) memakai `labfik.approval.mixin`, dengan wewenang di `labfik.jabatan.wewenang`.

### M-1 `labfik.approval.mixin` (AbstractModel, `_inherit = 'mail.thread'`)

| Field | Tipe |
|---|---|
| `state` | Selection {`draf`, `diajukan`, `disahkan`, `diganti`, `dicabut`, `kedaluwarsa`} = `draf` |
| `penyusun_id` | Many2one `hr.employee` |
| `tanggal_ajukan` | Datetime (readonly) |
| `berkas_ttd` | Binary [0..1] |
| `pengesah_id` | Many2one `hr.employee` [0..1] (readonly) |
| `pencatat_id` | Many2one `res.users` [0..1] (readonly) |
| `tanggal_sah` | Date [0..1] (readonly) |
| `log_ids` | `labfik.approval.log` [*] {compute} |

| Method | Jenis |
|---|---|
| `+ action_ajukan()` | Template Method: cek `draf` → `_cek_kelengkapan()` kosong → `_sebelum_ajukan()` → ubah status + log |
| `+ action_unggah_ttd(berkas)` | Hanya saat `diajukan` |
| `+ action_kembalikan(alasan)` | Grup `labfik_kalab`; alasan wajib |
| `+ action_sahkan(pengesah, tanggal_sah)` | Template Method (grup `labfik_kalab`): cek `diajukan` → `berkas_ttd` ada → `_cek_wewenang()` → `_sebelum_disahkan()` → tulis pengesah → `_dokumen_diganti()` jadi `diganti` → `_setelah_disahkan()` |
| `+ action_cabut(alasan)` | Grup `labfik_kalab`; alasan wajib |
| `+ action_terbitkan(): report`, `+ get_kelengkapan(): list`, `+ get_pengesah_berwenang(): hr.employee` | |
| `+ unlink()` «override» | Ditolak bila bukan `draf` |
| `# _jenis_dokumen(): str`, `# _cek_kelengkapan(): list` | {abstract}, diisi model turunan |
| `# _cek_wewenang(pengesah)` | → `pengesah.job_id.punya_wewenang('mengesahkan', self._jenis_dokumen())` |
| `# _sebelum_ajukan()`, `# _sebelum_disahkan()`, `# _dokumen_diganti(): recordset`, `# _setelah_disahkan()` | {hook} |
| `# _ubah_status(status_baru, kejadian, alasan, berkas)` | Selalu menulis baris `approval.log` |

Model turunan **tidak** meng-*override* `action_ajukan()`/`action_sahkan()`, hanya mengisi *hook* dan method {abstract}.

### M-2 `labfik.approval.log` [T]

| Field | Tipe |
|---|---|
| `res_model` | Char |
| `res_id` | Integer |
| `kejadian` | Selection {`diajukan`, `dikembalikan`, `berkas_diunggah`, `disahkan`, `diganti`, `dicabut`, `kedaluwarsa`} |
| `waktu` | Datetime |
| `pelaku_id` | Many2one `res.users` [0..1] |
| `pengesah_id` | Many2one `hr.employee` [0..1] |
| `alasan` | Text [0..1] |
| `berkas` | Binary [0..1] |

`write()` dan `unlink()` «override» ditolak: log tidak bisa diubah atau dihapus.

### M-3 `labfik.period.mixin` (AbstractModel)

| Field / method | Tipe |
|---|---|
| `periode_id` | Many2one `labfik.periode` |
| `tanggal_mulai`, `tanggal_selesai` | Date {related} dari periode |
| `is_berlaku` | Boolean {compute} |
| `+ berlaku_pada(tanggal): bool` | method |
| `@model # _cron_kedaluwarsakan()` | `ir.cron` harian (lapis Pelengkap) |

Hanya cocok untuk dokumen yang berlaku **per periode bersama** (semester / tahun anggaran). Masa berlaku perorangan tidak memakai mixin ini (I-6).

### M-4 `labfik.criteria.mixin` (AbstractModel)

| Field / method | Tipe |
|---|---|
| `kriteria_tertinggi` | Integer {compute} |
| `+ get_kriteria(tanggal_acuan): dict` | Berhenti di kriteria pertama yang gagal |
| `# _compute_kriteria_tertinggi()` | |
| `# _cek_k1(tanggal)` … `# _cek_k4(tanggal)` | {abstract} |

Sistem hanya menunjukkan kriteria tertinggi yang **lengkap secara data**; skor akhir ditetapkan penilai.

### M-5 `labfik.evidence.mixin` (AbstractModel)

Dipakai juga untuk hasil uji/kalibrasi internal alat (usulan Aset, 16 November 2026).

| Field / method | Tipe |
|---|---|
| `tanggal` | Date |
| `pelapor_id` | Many2one `hr.employee` |
| `bukti_ids` | Many2many `ir.attachment` |
| `keterangan` | Text [0..1] |
| `+ action_koreksi(nilai, alasan)` | Nilai baru + alasan tercatat di chatter |
| `+ unlink()` «override» | Selalu ditolak: rekaman bukti tidak dihapus |
| `# _boleh_dikoreksi(): bool` | {hook} |

### G Grup akses

| Grup | Mewarisi | Hak utama (dari DCD Tata Kelola) |
|---|---|---|
| `labfik_pengguna` | `base.group_user` | Membaca dokumen yang `disahkan` |
| `labfik_laboran` | `labfik_pengguna` | Mencatat (dokumen, realisasi, rekaman bukti) |
| `labfik_kalab` | `labfik_laboran` | Semua master; mengembalikan, mengesahkan, mencabut |

**Aturan penempatan grup (I-5):** grup masuk `labfik_core` bila dirujuk kode Core atau dipakai lebih dari satu modul; selain itu tinggal di modul pemakainya.

| Grup | Tempat | Alasan |
|---|---|---|
| `labfik_pengguna`, `labfik_laboran`, `labfik_kalab` | `labfik_core` | `approval.mixin` (Core) memeriksa `labfik_kalab`; ketiga modul memakai KaLab dan Laboran |
| `labfik_dosen`, `labfik_asisten` (mewarisi `labfik_pengguna`) | `labfik_praktikum` | Hanya Praktikum yang punya aktor Dosen dan Asisten yang login (mengisi jurnal, menerbitkan modul), lengkap dengan *record rule* per kelas. Di SDM, asisten hanya **objek** yang dicatat (diseleksi, ditugaskan), bukan pengguna. SDM tidak bergantung ke Praktikum (I-7), jadi bila nanti SDM juga butuh grup ini, grupnya dipindah ke Core |

Grup tetap tidak sama dengan jabatan: hak **mengesahkan** diatur `labfik.jabatan.wewenang`, bukan grup.

---

## 4. Perluasan Core oleh modul lain (Core tidak diubah)

| Modul | Model Core | Bentuk | Isi |
|---|---|---|---|
| SDM | `hr.job` | `_inherit` | + `syarat_kompetensi_ids`: Many2many `labfik.sdm.kompetensi`, label "Kompetensi wajib"; berdampingan dengan `syarat_kompetensi` (Text) Core (I-2, disetujui). Ditambahkan di `labfik_sdm` karena model Kompetensi ada di sana |
| SDM | `hr.employee` | `_inherit` | + `bukti_kompetensi_ids`: One2many `labfik.sdm.bukti.kompetensi`; + `punya_kompetensi(kompetensi, tanggal)`; + `kompetensi_kurang(tanggal)` |
| SDM | `labfik.jabatan.wewenang.jenis_dokumen` | `selection_add` | `penugasan_petugas`, `otorisasi`, `rencana_pelatihan` |
| SDM | `labfik.jabatan.wewenang` | Data XML | (KaLab, mengesahkan, otorisasi); (KaLab, mengesahkan, penugasan_petugas) [KONFIRMASI]; (KaLab dan/atau Wadek, mengesahkan, rencana_pelatihan) [KONFIRMASI] |
| Praktikum | `labfik.jabatan.wewenang.jenis_dokumen` | `selection_add` (hanya `jenis_dokumen`; `tindakan` tidak diperluas) | Pasangan wewenang: (`mengesahkan`, `jadwal_praktikum`), (`mengesahkan`, `pemakaian_lab`), (`mengesahkan`, `perubahan_sesi`), (`mengesahkan`, `survei_kepuasan`) (I-4) |
| Praktikum | `res.groups` | Data XML `labfik_praktikum` | `labfik_dosen`, `labfik_asisten` (I-5) |
| Praktikum | `survey.survey` (Odoo) | `_inherit` + `labfik.criteria.mixin` | Paket survei kepuasan per periode (PKG-20) |
| Aset | `labfik.jabatan.wewenang.jenis_dokumen` | `selection_add` | `baso`, `usulan_disposal`, `program_pemeliharaan` (I-10) |
| Aset | `labfik.alat` | `_inherit` | *Override* `check_ketersediaan_sesi()` untuk menambah cek peminjaman (I-16) |

---

## 5. Pemakaian mixin per modul

| Mixin | Tata Kelola (`labfik_org`) | SDM (`labfik_sdm`) | Praktikum (`labfik_praktikum`) |
|---|---|---|---|
| `approval` | `labfik.document.version`, `labfik.renstra`, `labfik.plan`, `labfik.assignment` | Surat Tugas, Otorisasi, Rencana Pelatihan | Penetapan Jadwal (hook `_setelah_disahkan()` menandai Sesi `terpublikasi`) |
| `period` | `labfik.renstra`, `labfik.plan`, `labfik.assignment` | Rencana Pelatihan | Tidak dipakai (cukup `periode_id` biasa) |
| `criteria` | `labfik.plan`, `labfik.assignment` | Rencana Pelatihan | Survei (`survey.survey`) |
| `evidence` | Rapat, Evaluasi Struktur, Distribusi, Sosialisasi, Tinjau Ulang, Realisasi, Tinjauan | Bukti Kompetensi, Kebutuhan Petugas, Seleksi, Asesmen, Evaluasi Otorisasi, Realisasi Pelatihan, Evaluasi Pelatihan | Pemeriksaan Kesiapan, Jurnal Sesi, Evaluasi Survei, RTL |

Nama model SDM dan Praktikum masih sementara sampai Langkah 10 di modul masing-masing. Pola nama: `labfik.sdm.*`, `labfik.praktikum.*`.

Kelompok Aset & Safety baru menyebut pemakaian `approval` (BASO, usulan afkir) dan `evidence` (hasil uji/kalibrasi, inspeksi K3). Nama model transaksinya belum ada di diagram [VALIDASI].

---

## 6. Keputusan atas perbedaan antar-branch

Keputusan Febriyan sebagai pemilik Core, 15 November 2026. Yang masih menunggu ditandai.

| No | Hal | Perbedaan yang ditemukan | Keputusan |
|---|---|---|---|
| I-1 | Nilai `labfik.sesi.state` | Herrens 6 status (S1 Sesi); Zahir 3 status (K-5) | **Ikuti SDM:** {`terjadwal`, `terlaksana`, `batal`}. Status lain dihitung (pemetaan di C-9) |
| I-2 | Syarat kompetensi jabatan | Core: Text; SDM: Many2many | **Keduanya dipakai.** Text di Core untuk uraian SK; Many2many ditambahkan `labfik_sdm` untuk perhitungan |
| I-3 | `kapasitas` ruang | Herrens mengusulkan field `kapasitas` (Integer) di `labfik.ruang`, bukan model baru | **Disetujui:** `labfik.ruang` = `kode`, `name`, `kapasitas` |
| I-4 | Pilihan `tindakan` wewenang | Herrens menambah `menyetujui`, `menetapkan` | **Tidak diperluas.** Menyetujui/menetapkan = `mengesahkan`, sejalan dengan dihapusnya tahap pemeriksaan di Tata Kelola. Modul hanya menambah `jenis_dokumen` |
| I-5 | Lokasi grup akses | Belum ditulis; Herrens menambah dosen dan asisten | **Tiga grup dasar di Core**; `labfik_dosen` dan `labfik_asisten` di `labfik_praktikum` (aturan di bagian G) |
| I-6 | Masa berlaku perorangan | SDM tidak memakai `period.mixin` untuk Otorisasi, Bukti Kompetensi, Penugasan (K-3) | Sesuai; tidak mengubah Core |
| I-7 | Arah dependensi Praktikum–SDM | Zahir: Praktikum → SDM; Herrens: Praktikum tanpa SDM | **Praktikum → SDM** (brief awal). `labfik_praktikum` depends `labfik_sdm`; SDM hanya bergantung ke Core karena Sesi dan Kelas ada di Core. Pencocokan penugasan dengan presensi dilakukan di Praktikum saat jurnal diisi. Keputusan sebelumnya (SDM → Praktikum) dibatalkan |
| I-8 | Petugas di Jurnal Sesi | Herrens menulis "personel" tanpa tipe | **Wajib `employee_id`: Many2one `hr.employee`** di baris presensi petugas, bukan teks |
| I-9 | Pihak eksternal | Brief Praktikum menulis "masih terbuka" | **Sudah diputuskan:** bukan Personel dan bukan aktor (CLAUDE.md bagian 6) |
| I-10 | Pilihan `jenis_dokumen` wewenang | Diagram Aset (16 November 2026) menulis daftar tertutup {`sop_ik`, `renstra`, `baso`, `usulan_disposal`, `program_pemeliharaan`}; nilai Tata Kelola lain, SDM, dan Praktikum hilang | **Digabung:** semua nilai berlaku. Nilai dasar Tata Kelola di Core; tiga nilai Aset ditambahkan lewat `selection_add` dari addon Aset, sama seperti SDM dan Praktikum |
| I-11 | `hr.employee.aset_dikelola_ids` | Diagram menulis {related}; tidak ada jalur field dari `hr.employee` ke alat, jadi {related} tidak bisa jalan | **Dibetulkan:** One2many `labfik.alat`, kebalikan `penanggung_jawab_id`. Isinya sama dengan maksud Aset |
| I-12 | `labfik.ruang.workstation_count` dan `kapasitas` | Dua angka kapasitas di ruang | **Digabung, keduanya dipakai:** `kapasitas` = kursi mahasiswa (Praktikum, PKG-15), `workstation_count` = jumlah PC {compute}. Rumus hitung ditetapkan Aset [KONFIRMASI Aset] |
| I-13 | Pengubah `labfik.alat.status` | Belum ditulis | **Ditambahkan aturan:** hanya addon Aset yang mengubah `status`; modul lain hanya membaca (pola sama dengan `labfik.sesi.state`) |
| I-14 | Penanda kalibrasi ganda | `labfik.alat.is_perlu_kalibrasi` dan `labfik.alat.kategori.butuh_kalibrasi_internal` | **Digabung, keduanya dipakai:** nilai kategori menjadi nilai awal, bisa diubah per unit |
| I-15 | Stok bahan | Ada `stok_minimum`, tanpa stok berjalan | **Digabung:** `stok_minimum` di Core; stok berjalan dan mutasi bahan di addon Aset/Safety |
| I-16 | `labfik.alat.check_ketersediaan_sesi()` di Core | Data peminjaman nanti ada di addon Aset, yang bergantung ke Core; Core tidak bisa membacanya | **Dibetulkan:** versi Core hanya memeriksa `status` dan `ruang_id` {hook}; addon Aset meng-*override* lewat `_inherit` untuk menambah cek peminjaman |

### 6.1 Perubahan yang perlu dilakukan di tiap branch

| Branch | Dokumen | Perubahan |
|---|---|---|
| `herrens-skripsi` | `proses-bisnis-praktikum.md` + `activity-state-praktikum.drawio` (S1 Sesi), bagian 4.4 | Status Sesi menjadi 3 (I-1); Rencana/Terpublikasi/Ditunda/Diganti menjadi atribut hitung |
| `herrens-skripsi` | `kebutuhan-praktikum.md` KF-PRK-45, 46 | Bukan transisi status lagi; cukup dicatat sebagai perilaku hitung (I-1) |
| `herrens-skripsi` | `brief-praktikum.md` Kontrak Core bagian c | Wewenang memakai tindakan `mengesahkan` saja (I-4); hapus "pihak eksternal masih terbuka" (I-9); bagian d: nilai `state` (I-1) |
| `herrens-skripsi` | `brief-praktikum.md` "Yang dipakai" baris Penugasan PKG-04 dan "Dampak ke rencana addon"; `analisis-data-proses-18.md` | `labfik_praktikum` depends `labfik_sdm`; presensi petugas di jurnal dicocokkan dengan penugasan SDM (I-7) |
| `herrens-skripsi` | `kebutuhan-praktikum.md` KF-PRK-23; `analisis-data-proses-18.md` Jurnal Sesi | Presensi petugas merujuk `hr.employee` (I-8) |
| `zahir-skripsi` | `kontrak-core-sdm.md` K-5 (nilai `state`), bagian 4–5 (arah addon) | `state` {terjadwal, terlaksana, batal} dan arah addon (Praktikum → SDM) sudah sesuai; tidak ada perubahan (I-1, I-7) |
| `zahir-skripsi` | `kontrak-core-sdm.md` KC-1, KC-3, KC-4, KC-5 | Terjawab oleh I-2, I-5, I-1, I-8 |
| `febriyan-skripsi` | `design-class-tata-kelola.md` bagian 7 | Sebut bahwa tiga grup ada di `labfik_core` (I-5) |
| `febriyan-skripsi` | `design_class.py` → `class-tata-kelola.drawio` (DCD-2, DCD-3), `design-class-tata-kelola.md` bagian 2.1 | `labfik.ruang` + `kapasitas: Integer` (I-3) |

---

## 7. Pertanyaan terbuka

| No | Pertanyaan | Ke siapa |
|---|---|---|
| 1 | Pemetaan 6 status Sesi ke 3 status (C-9) dapat diterima? | Herrens |
| 2 | Siapa yang menulis kode `labfik_core` saat implementasi, dan di branch mana? | Kelompok |
| 3 | Dokumen Induk (PKG-09) dan KPI (PKG-21) dipakai kelompok Safety/Aset? Bila ya, modul jembatan atau pindah ke Core | Kelompok lain |
| 4 | Isi awal ruang (8 ruang) dan nilai `unit`/`prodi` sesuai kondisi FIK? | KaLab **[VALIDASI]** |
| 5 | Master aset (C-10–C-13) disetujui masuk `labfik_core`, dan hasil penggabungan I-10–I-16 diterima? Rumus `workstation_count` (I-12) | Kelompok Aset & Safety |
| 6 | Nama addon Aset dan Safety, serta model transaksinya (peminjaman, pemeliharaan, kalibrasi, inspeksi K3) | Kelompok Aset & Safety |
