# Design Class Diagram Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 10 (terakhir) alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (class diagram). Dasar implementasi addon `labfik_core` dan `labfik_org` di Odoo 17 Community.

Diagram: [class-tata-kelola.drawio](class-tata-kelola.drawio), 4 halaman (DCD-1 s.d. DCD-4), termasuk kelas view inti (bagian 11). Awalnya dibuat dengan skrip [design_class.py](../tools/drawio/contoh-tata-kelola/design_class.py); sejak 19 November 2026 diagram disunting langsung, sehingga skrip itu tinggal arsip. Lolos `validate.py` dengan prefiks `tk-`. **Tampilan visual belum dicek di draw.io.**

Sumber: [conceptual-model-tata-kelola.md](conceptual-model-tata-kelola.md) (CM-1–4), katalog operasi di [ssd-tata-kelola.md](ssd-tata-kelola.md), AB-01–25 di [expanded-use-case-tata-kelola.md](expanded-use-case-tata-kelola.md), kontrak Core di CLAUDE.md bagian 6.

---

## 1. Aturan yang dipakai

| Aturan | Sumber | Penerapan |
|---|---|---|
| DCD dimulai dari salinan conceptual model, lalu: tambah method, beri arah asosiasi, rinci tipe, ubah struktur bila perlu | Wazlawick §13.6 | Bagian 3 (dari CM ke desain) |
| Tanggung jawab dibagi ke objek yang memegang datanya (*delegation*), bukan dikumpulkan di kontroler (*concentration*) | §13.2, §13.5 | Operasi SSD menjadi method model, bukan method satu kontroler. Contoh: cek wewenang didelegasikan ke `hr.job.punya_wewenang()` |
| Pembagian method: *get/set* atribut, *add/remove* tautan, dan method delegasi | §13.2, Tabel 13–1 | Method *get/set* dasar disediakan ORM Odoo dan tidak digambar; yang digambar hanya method delegasi, *compute*, *constraint*, dan *hook* |
| Arah asosiasi mengikuti arah pesan | §13.6 | Many2one berarah dari anak ke induk atau dari perujuk ke yang dirujuk; komposisi = One2many + Many2one `cascade`; agregasi = Many2many atau Many2one tanpa `cascade` (bagian 3.3) |
| Perilaku bersama sebagai *mixin* `AbstractModel`; model turunan memakai `_inherit` | Arahan Pak Widi 13 Nov 2026; CLAUDE.md langkah 10 | Empat mixin di `labfik_core` |
| Urutan baku yang tidak boleh terlewat ditulis sebagai **Template Method** dengan **hook** | CLAUDE.md bagian 8 ("override `action_sahkan()` langsung" adalah kesalahan) | `action_ajukan()` dan `action_sahkan()` |
| Model bawaan diperluas, bukan disalin | Keputusan 14 Nov 2026 | `hr.employee`, `hr.job` dengan `_inherit` tanpa `_name` baru |
| Notasi DCD proyek | CLAUDE.md bagian 5 | Gaya polos hitam-putih; jenis kelas lewat stereotype: «AbstractModel» (nama miring), «Odoo», «Core», model baru tanpa stereotype, `+`/`#`, «override», {abstract}, {hook} |

---

## 2. Daftar model

### 2.1 Addon `labfik_core` (`depends: ['hr', 'mail']`)

| Model | Jenis | Label | Asal di CM | Keterangan |
|---|---|---|---|---|
| `labfik.approval.mixin` | AbstractModel | — | DokumenDisahkan + Pengesahan | Siklus S1, Template Method pengesahan |
| `labfik.approval.log` | Model | [T] | KejadianPengesahan | Riwayat generik (`res_model`, `res_id`) untuk semua dokumen; tidak bisa diubah atau dihapus |
| `labfik.period.mixin` | AbstractModel | — | asosiasi *berlaku_pada* Periode | Masa berlaku, `is_berlaku`, penjadwal kedaluwarsa (O) |
| `labfik.criteria.mixin` | AbstractModel | — | `/kriteria_tertinggi` | Kriteria K1–K4 berurutan; `_cek_k1()`–`_cek_k4()` {abstract} |
| `labfik.evidence.mixin` | AbstractModel | — | RekamanBukti | Tanggal, pelapor, bukti; koreksi terlacak, tidak bisa dihapus |
| `hr.employee` (diperluas) | Model Odoo | [M] | Personel | + `jenis_personel`, `unit`. Bawaan: `name`, `job_id`, `user_id` |
| `hr.job` (diperluas) | Model Odoo | [M] | Jabatan | + `unit`, `is_eksternal`, `atasan_id`, `pengganti_id`, `syarat_kompetensi`, `tugas_ids`, `wewenang_ids`. `syarat_kompetensi` (Text) adalah uraian naratif; modul SDM menambah `syarat_kompetensi_ids` (Many2many) dari `labfik_sdm` untuk perhitungan (I-2). Data awal (fiktif, seed): Kepala Laboratorium, Laboran, Teknisi, **Asisten Praktikum**, dan jabatan eksternal Dekan, Ketua Jurusan |
| `labfik.jabatan.tugas` | Model | [M] | Tugas | Anak `hr.job` |
| `labfik.jabatan.wewenang` | Model | [M] | Wewenang | Anak `hr.job`; unik per (jabatan, tindakan, jenis dokumen). `tindakan` tetap {menyusun, mengesahkan}; "menyetujui"/"menetapkan" di modul lain = mengesahkan (I-4). Modul lain menambah `jenis_dokumen` dengan `selection_add` |
| `labfik.ruang`, `labfik.periode` | Model | [M] | Ruang, Periode | Master Core. Ruang: `kode`, `name`, `kapasitas` (usulan Praktikum, disetujui 15 November 2026, I-3) |
| Grup `labfik_pengguna` ⊂ `labfik_laboran` ⊂ `labfik_kalab` | `res.groups` (data XML) | — | — | Didefinisikan di `labfik_core` karena `approval.mixin` memeriksa `labfik_kalab` (bagian 7, I-5) |

Core juga memuat `labfik.mata.kuliah`, `labfik.kelas`, dan `labfik.sesi` [T] yang dirancang modul Praktikum. Ketiganya tidak dipakai Tata Kelola sehingga tidak digambar di DCD ini. Rincian semua model Core dan keputusan I-1 s.d. I-9 ada di [kontrak-core.md](kontrak-core.md) dan [model-core.drawio](model-core.drawio).

### 2.2 Addon `labfik_org` (`depends: ['labfik_core']`)

| Model | `_inherit` | Label | Asal di CM |
|---|---|---|---|
| `labfik.assignment` | approval, period, criteria | [T] | SK Penetapan |
| `labfik.assignment.line` | — | [T] | BarisPenetapan |
| `labfik.meeting` | evidence | [T] | Rapat Koordinasi |
| `labfik.org.evaluation` | evidence | [T] | Evaluasi Struktur |
| `labfik.document` | mail.thread | [M] | DokumenInduk |
| `labfik.document.version` | approval, mail.thread | [T] | Versi Dokumen |
| `labfik.document.distribution` | evidence | [T] | Distribusi |
| `labfik.document.socialization` | evidence | [T] | Sosialisasi |
| `labfik.document.review` | evidence | [T] | Tinjau Ulang |
| `labfik.renstra` | approval, period | [T] | Renstra |
| `labfik.kpi` | — | [M] | KPI |
| `labfik.plan` | approval, period, criteria | [T] | Rencana |
| `labfik.plan.line` | — | [T] | ItemRencana |
| `labfik.plan.gap` | — | [T] | TemuanGap |
| `labfik.realisasi` | evidence | [T] | Realisasi |
| `labfik.tinjauan` | evidence | [T] | Tinjauan Rencana |
| `labfik.tinjauan.manfaat` | — | [T] | UkuranManfaat |
| `labfik.org.monev` | AbstractModel (layanan) | [R] | — (status monev hanya hasil hitung) |

Semua nama sesuai daftar nama yang sudah dipakai Tata Kelola (CLAUDE.md bagian 6) ditambah `labfik.renstra`, `labfik.kpi`, dan `labfik.org.monev`.

**Penempatan Dokumen Induk, Versi, dan KPI (keputusan Febriyan, 14 November 2026):** tetap di `labfik_org`. Model dipindah ke `labfik_core` hanya bila ada modul lain yang terkonfirmasi memakainya. Kandidat yang tercatat di brief bersama: Dokumen Induk untuk SOP limbah PKG-09 (Safety) dan KPI untuk PKG-21 (Aset) **[KONFIRMASI kelompok]**. Pemindahan tidak mengubah rancangan model, hanya addon tempatnya.

---

## 3. Dari conceptual model ke desain (§13.6)

| Perubahan | CM | DCD | Alasan |
|---|---|---|---|
| Generalisasi menjadi *mixin* | DokumenDisahkan, RekamanBukti | `approval.mixin`, `evidence.mixin` | Odoo mewujudkan generalisasi lintas tabel lewat `AbstractModel` + `_inherit` |
| Konsep kejadian 0..1 menjadi field | Pengesahan | `pengesah_id`, `pencatat_id`, `tanggal_sah` (readonly) di mixin | Hanya ada satu pengesahan per dokumen; kejadiannya tetap tercatat lengkap di `approval.log`. Field hanya bisa ditulis oleh `action_sahkan()` |
| Konsep kejadian * menjadi model log generik | KejadianPengesahan | `labfik.approval.log` (`res_model`, `res_id`) | Satu tabel riwayat untuk lima jenis dokumen; `log_ids` di mixin adalah field *compute* |
| Asosiasi refleksif per model | `revisi_dari` di DokumenDisahkan | `revisi_dari_id` di `labfik.plan`, `labfik.assignment`, `labfik.renstra` | Mixin tidak bisa membuat Many2one ke "dirinya sendiri". Untuk versi SOP/IK, penggantian ditentukan lewat Dokumen Induk yang sama. Penentuan dokumen yang diganti diserahkan ke *hook* `_dokumen_diganti()` |
| Periode menjadi mixin | asosiasi *berlaku_pada* | `labfik.period.mixin` (`periode_id`) | Dipakai tiga model; menyatukan `is_berlaku` dan penjadwal |
| Atribut turunan menjadi `compute` | `/perlu_ditinjau`, `/memenuhi`, `/kriteria_tertinggi`, `/prioritas`, `/versi_berlaku` | `compute` (+ `store` atau `search` bila dipakai sebagai filter) | — |
| Enumerasi menjadi `Selection` | Semua «enumeration» | `fields.Selection` | — |
| Rujukan ke Personel menjadi atribut bertipe | peran pengesah, pic, pelapor, peserta | `hr.employee` | Model bawaan Odoo boleh ditulis sebagai atribut bertipe (CLAUDE.md bagian 5) |
| Nama peran menjadi nama field Odoo | *berlaku_pada*, *revisi_dari* / *pengganti*–*digantikan*, *dievaluasi*, *ditugaskan_di*, *lokasi_penggunaan*, *menjawab*, *ukuran_manfaat*, *temuan_gap*, *item* | `periode_id`, `revisi_dari_id`, `sk_id`, `ruang_ids`, `lokasi_ids`, `gap_ids`, `manfaat_ids`, `gap_ids`, `line_ids` | Konvensi Odoo: Many2one diakhiri `_id`, One2many/Many2many diakhiri `_ids` |
| Layanan baru | — | `labfik.org.monev` | Tempat `get_status()` untuk UC-28; mendelegasikan perhitungan ke model pemilik data |
| Mata uang | `anggaran: Money` | `Monetary` + `currency_id` | Aturan Odoo untuk nilai uang |

---

### 3.1 Field usulan studi dokumen yang tidak diambil

Daftar model di [bedah-dokumen-tata-kelola.md](../analisis/bedah-dokumen-tata-kelola.md) bagian 5 disusun sebelum cakupan dipangkas. Field berikut tidak masuk DCD atau berganti nama:

| Model | Field di bedah dokumen | Di DCD | Alasan |
|---|---|---|---|
| `hr.employee` | `parent_id` | Tetap ada sebagai field bawaan, tidak dipakai | Atasan dibaca dari jabatan (`hr.job.atasan_id`), bukan per orang |
| `hr.job` | `dasar_dokumen_id` | Tidak diambil | PKG-03 K2 hanya memeriksa tugas, wewenang, atasan, dan pengganti; dasar hukumnya ada di SK |
| `labfik.document` | `lokasi_penggunaan_ids` | `lokasi_ids` | Ganti nama |
| `labfik.document` | `dokumen_terkait_ids`, `rekaman_dihasilkan` | Tidak diambil | Tidak dibutuhkan S1–S5 |
| `labfik.document.version` | `tanggal_dibuat`, `tanggal_revisi` | `create_date` bawaan; `tanggal_efektif` dan `tanggal_sah` | Tidak perlu field sendiri |
| `labfik.plan.line` | `baseline`, `bukti_diharapkan`, `komponen_anggaran` | Tidak diambil | PKG-01 K2 hanya meminta KPI, target, PIC, jadwal, anggaran, dan keterkaitan Renstra |
| `labfik.realisasi` | `alasan_tidak_relevan` (status *tidak relevan*) | Tidak diambil; status capaian tinggal empat nilai | Tidak dibutuhkan K3 |
| `labfik.assignment` | `dasar_hukum_ids`, `diktum`, `tembusan` | Tidak diambil | Dasar hukum cukup ditulis di `mengingat`; diktum dibangkitkan dari baris penetapan saat SK diterbitkan (KF-26, Pelengkap) |
| `labfik.org.evaluation` | `assignment_baru_id` | `sk_revisi_id` | Ganti nama |

### 3.2 Jenis pewarisan Odoo dan penempatannya

Ditambahkan untuk menjawab catatan bimbingan November 2026 ("penempatan class untuk inheritance"). Odoo punya tiga cara pewarisan; modul ini memakai dua.

| Jenis | Sintaks | Arti | Di modul ini | Cara digambar |
|---|---|---|---|---|
| **Mixin** (abstrak) | `_inherit = ['labfik.approval.mixin', …]` pada model dengan `_name` baru | Field dan method bersama ditulis sekali di `AbstractModel` (tanpa tabel); model turunan mewarisinya dan mengisi method `{abstract}`/`{hook}` (polimorfisme, bagian 4) | 4 mixin di `labfik_core`; 11 model turunan di `labfik_org` | «AbstractModel» bernama miring; segitiga kosong dari turunan ke mixin. Di DCD-1 mixin diletakkan di **atas** dan turunan di **bawah**, sehingga arah pewarisan terbaca dari bawah ke atas. Di DCD-2–4 cukup `{inherit: …}` di header; field warisan tidak ditulis ulang |
| **Ekstensi** (*classical*) | `_inherit = 'hr.employee'` **tanpa** `_name` baru | Menambah field dan method ke model bawaan; tabelnya tetap tabel model bawaan | `hr.employee` (Personel), `hr.job` (Jabatan), diperluas di `labfik_core` | «Odoo» + `{_inherit: hr.employee} di labfik_core` di header kelas (DCD-2). Tidak digambar sebagai generalisasi, karena tidak ada kelas baru |
| **Delegasi** | `_inherits = {'res.partner': 'partner_id'}` | Model baru dengan tabel sendiri yang tertaut ke tabel induk | Tidak dipakai | — |

Kedua mixin pencatat (`approval.mixin`, `evidence.mixin`) sendiri mewarisi `mail.thread` (bawaan Odoo) untuk riwayat perubahan; ini digambar sebagai generalisasi ke kelas «Odoo» `mail.thread` di DCD-1.

### 3.3 Jenis relasi antarkelas

Ditambahkan untuk menjawab catatan bimbingan November 2026 (asosiasi, komposisi, agregasi, generalisasi). Dasar: Wazlawick §8.4.5 dan catatan kaki pola *Composite* di §11: bagian yang bisa dimiliki lebih dari satu keseluruhan memakai *shared aggregation* (belah ketupat putih), bagian yang eksklusif memakai *composite aggregation* (belah ketupat hitam).

| Relasi | Notasi | Wujud di Odoo | Contoh di modul ini |
|---|---|---|---|
| Asosiasi berarah | Garis dengan panah terbuka; label = nama field + multiplisitas | Many2one atau Many2many | `labfik.plan.line.kpi_id` → KPI; `labfik.realisasi.line_id` → Item Rencana; `labfik.document.review.version_id` → Versi |
| **Komposisi** (master–detail kuat) | Belah ketupat **hitam** di sisi master | One2many di master + Many2one `ondelete='cascade'` di detail; detail ikut terhapus | Rencana → Item Rencana, Temuan Gap; SK → Baris Penetapan; Jabatan → Tugas, Wewenang; Dokumen Induk → Versi; Tinjauan → Ukuran Manfaat |
| **Agregasi** (master–detail lemah) | Belah ketupat **putih** di sisi master | Many2many, atau Many2one dengan `ondelete='set null'`/`'restrict'`; detail tetap ada bila master dihapus dan boleh dimiliki banyak master | `hr.job` ◇— `hr.employee` (`job_id` / `employee_ids`, bawaan); `labfik.document` ◇— `labfik.ruang` (`lokasi_ids`); `labfik.meeting` ◇— `hr.employee` (`peserta_ids`) |
| Generalisasi | Segitiga kosong ke induk | `_inherit` ke mixin (bagian 3.2) | Rencana, SK, Renstra, Versi → `approval.mixin`; Rapat, Distribusi, Realisasi, … → `evidence.mixin` |
| Turunan | Garis putus-putus `{compute}` | Field `compute` | `approval.mixin.log_ids`; `labfik.document.versi_berlaku_id` |

Agregasi hanya digambar untuk tiga relasi di atas, karena di sana makna "menghimpun tanpa memiliki" jelas: personel tetap ada walaupun jabatannya dihapus, ruang dipakai banyak dokumen, dan peserta rapat adalah personel yang sama di banyak rapat. Rujukan lain ke `hr.employee` (`peserta_ids` Sosialisasi dan Tinjauan, `pic_id`, `pelapor_id`) tetap ditulis sebagai atribut bertipe, karena halaman DCD-3 dan DCD-4 tidak memuat kelas `hr.employee` dan model bawaan Odoo boleh ditulis begitu (CLAUDE.md bagian 5).

## 4. Template Method dan hook

`labfik.approval.mixin` menetapkan urutan yang **tidak di-override** oleh model turunan. Model turunan hanya mengisi *hook* dan method {abstract}.

**`action_ajukan()`**
1. `state` harus `draf` (AB-01).
2. `_cek_kelengkapan()` {abstract} harus mengembalikan daftar kosong (AB-02).
3. `_sebelum_ajukan()` {hook}.
4. `_ubah_status('diajukan', 'diajukan')`: tulis status dan `tanggal_ajukan`, lalu catat log (AB-09).

**`action_sahkan(pengesah, tanggal_sah)`** (hanya grup KaLab, AB-06)
1. `state` harus `diajukan`.
2. `berkas_ttd` harus ada (AB-04).
3. `_cek_wewenang(pengesah)` → `pengesah.job_id.punya_wewenang('mengesahkan', self._jenis_dokumen())` (AB-05).
4. `_sebelum_disahkan()` {hook}.
5. Tulis `pengesah_id`, `pencatat_id` = pengguna, `tanggal_sah`; `state = disahkan`; catat log.
6. `_dokumen_diganti()` {hook} → setiap dokumen yang dikembalikan diubah menjadi `diganti` dan dicatat di log (AB-08).
7. `_setelah_disahkan()` {hook}.

| Model | `_jenis_dokumen()` | `_cek_kelengkapan()` | `_sebelum_ajukan()` | `_sebelum_disahkan()` | `_dokumen_diganti()` | `_cek_k1()`–`_cek_k4()` |
|---|---|---|---|---|---|---|
| `labfik.document.version` | `sop_ik` | berkas, revisi, tanggal efektif; untuk revisi: bagian diubah, ringkasan, alasan | AB-12 (O) | — | versi `disahkan` lain di Dokumen Induk yang sama | — |
| `labfik.renstra` | `renstra` | judul, periode, berkas | — | — | `revisi_dari_id` | — |
| `labfik.plan` | `rencana_tahunan` / `rencana_pengembangan` (dari `jenis`) | AB-02 per jenis | — | AB-11 (O) | `revisi_dari_id` | AB-25 PKG-01 / PKG-13 menurut `jenis` |
| `labfik.assignment` | `sk_penetapan` | nomor, periode, ≥1 baris | — | — | `revisi_dari_id` | AB-25 PKG-03 |

`_setelah_disahkan()` tidak diisi model mana pun saat ini. *Hook* ini tetap disediakan untuk modul lain, misalnya rencana pelatihan PKG-14 di modul SDM.

Pola yang sama di `labfik.evidence.mixin`: `unlink()` selalu ditolak (AB-22); `action_koreksi(nilai, alasan)` menulis nilai baru dan mencatat alasannya di chatter, kecuali `_boleh_dikoreksi()` {hook} mengembalikan `False` (Tinjau Ulang).

---

## 5. Pemetaan operasi SSD → method

Setiap operasi di katalog SSD (bagian 3) dipetakan ke method atau ORM standar.

### 5.1 Pengesahan

| Operasi SSD | Method / ORM |
|---|---|
| `daftar_dokumen(filter, user_id)` | `search_read()` dengan domain per filter (`state`, `penyusun_id.user_id`) pada model dokumen; tampilan daftar Odoo |
| `rincian_dokumen(dokumen, user_id)` | `read()` + `log_ids` {compute} |
| `status_dokumen(dokumen)` | `read(['state', 'tanggal_ajukan', 'tanggal_sah', 'pengesah_id', 'pencatat_id', …])` |
| `cek_kelengkapan(dokumen)` | `get_kelengkapan()` → `_cek_kelengkapan()` |
| `daftar_pengesah_berwenang(dokumen)` | `get_pengesah_berwenang()` → `hr.job.cari_pemegang_berwenang('mengesahkan', _jenis_dokumen())` |
| `ajukan_dokumen` | `action_ajukan()` |
| `terbitkan_dokumen` | `action_terbitkan()` → QWeb report |
| `unggah_berkas_ttd` | `action_unggah_ttd(berkas)` |
| `kembalikan_dokumen` | `action_kembalikan(alasan)` |
| `sahkan_dokumen` | `action_sahkan(pengesah, tanggal_sah)` |
| `cabut_dokumen` | `action_cabut(alasan)` |
| `kedaluwarsakan_dokumen(tanggal)` | `period.mixin._cron_kedaluwarsakan()` via `ir.cron` harian (O) |

### 5.2 Pola «CRUDL» (Personel, Jabatan, Dokumen Induk, KPI, Renstra)

| Operasi SSD | ORM |
|---|---|
| `buat_<konsep>` | `create()` |
| `ubah_<konsep>` | `write()` (Renstra: hanya saat `draf`, AB-01) |
| `hapus_<konsep>` | `unlink()` «override» (AB-23; Renstra AB-01) |
| `arsipkan_<konsep>` | `action_archive()` (field `active`) |
| `rincian_<konsep>` | `read()` |
| `daftar_<konsep>` | `search_read()` |

### 5.3 Struktur organisasi

| Operasi SSD | Method / ORM |
|---|---|
| `buat_sk` | `labfik.assignment.create()` |
| `simpan_baris_penetapan` | `write({'baris_ids': [...]})` (AB-01) |
| `rincian_sk` | `read()` |
| `catat_rapat` | `labfik.meeting.create()` |
| `catat_evaluasi` | `labfik.org.evaluation.create()` |
| `tautkan_revisi_evaluasi` | `action_tautkan_revisi(sk, jabatan)` |
| `koreksi_rekaman` | `evidence.mixin.action_koreksi(nilai, alasan)` |
| `laporan_struktur(tanggal_acuan)` | QWeb report dari `hr.job` (`atasan_id`, `tugas_ids`, `wewenang_ids`) dan baris SK yang berlaku |

### 5.4 Pengendalian dokumen SOP/IK

| Operasi SSD | Method / ORM |
|---|---|
| `daftar_dokumen_induk` | `labfik.document.search_read()` |
| `info_versi` | `labfik.document.get_info_versi()` |
| `buat_versi` | `labfik.document.version.create()` (AB-13 `_sql_constraints`) |
| `rincian_versi(dokumen_induk, revisi)` | `search_read([('document_id', '=', …), ('revisi', '=', …)])`. Di Odoo, `create()` sudah mengembalikan rekaman baru (penyimpangan CQS yang diterima, SSD bagian 5) |
| `catat_distribusi` | `labfik.document.distribution.create()` |
| `catat_sosialisasi` | `labfik.document.socialization.create()` |
| `daftar_versi_berlaku` | `search_read([('state', '=', 'disahkan')], order='tanggal_tinjau_berikutnya')` |
| `catat_tinjau_ulang` | `labfik.document.review.create()` → memicu `_compute_tanggal_tinjau()` |
| `status_tinjau` | `read(['tanggal_tinjau_berikutnya', 'perlu_ditinjau'])` |
| `baca_dokumen_berlaku` | `baca_berkas()` (O) |
| `laporan_pengendalian_dokumen` | QWeb report dari `labfik.document` + versi + rekaman |

### 5.5 Rencana

| Operasi SSD | Method / ORM |
|---|---|
| `buat_rencana` | `labfik.plan.create()` |
| `simpan_temuan_gap` | `write({'gap_ids': [...]})` (AB-01) |
| `simpan_item_rencana` | `write({'line_ids': [...]})` (AB-01) |
| `rincian_rencana` | `read()` |
| `daftar_rencana` | `search_read()` |
| `buat_revisi_rencana` | `action_buat_revisi()` (O): `copy()` + `revisi_dari_id` |
| `daftar_item_pic(user_id)` | `labfik.plan.line.search_read([('pic_id.user_id', '=', uid), ('plan_id.state', '=', 'disahkan')])` |
| `catat_realisasi` | `labfik.realisasi.create()` |
| `koreksi_realisasi` | `action_koreksi(nilai, alasan)` |
| `capaian_item` | `labfik.plan.line.get_capaian()` |
| `catat_tinjauan` | `labfik.tinjauan.create()` (+ `manfaat_ids`) |
| `tautkan_rencana_berikutnya` | `action_tautkan_rencana_berikutnya(rencana)` |
| `laporan_rencana` | QWeb report dari `labfik.plan` |

### 5.6 Status monev

| Operasi SSD | Method |
|---|---|
| `status_monev(tanggal_acuan)` | `labfik.org.monev.get_status(tanggal_acuan)` → `labfik.document.hitung_persentase()` + `get_kriteria()` pada `labfik.plan` dan `labfik.assignment` |

Semua 45 operasi khusus dan 6 operasi pola «CRUDL» terpetakan.

---

## 6. Pemetaan aturan bisnis → mekanisme Odoo

| AB | Mekanisme | Tempat |
|---|---|---|
| AB-01 | Cek `state` di `action_ajukan()`; `write()`/`unlink()` «override» menolak perubahan isi bila bukan `draf` (perubahan status oleh action memakai konteks internal) | `approval.mixin` |
| AB-02 | `_cek_kelengkapan()` {abstract} dipanggil `action_ajukan()` | model turunan |
| AB-03 | Cek `state == 'diajukan'` di `action_unggah_ttd()` | `approval.mixin` |
| AB-04 | Langkah 2 Template Method `action_sahkan()` | `approval.mixin` |
| AB-05 | `_cek_wewenang()` → `hr.job.punya_wewenang()` | `approval.mixin`, `hr.job` |
| AB-06 | Grup akses `labfik_kalab` pada tombol dan `@api` cek grup di `action_kembalikan/sahkan/cabut()` | `approval.mixin`, XML view |
| AB-07 | Parameter `alasan` wajib di `action_kembalikan()` dan `action_cabut()` | `approval.mixin` |
| AB-08 | Langkah 6 Template Method + hook `_dokumen_diganti()` | `approval.mixin` + turunan |
| AB-09 | `_ubah_status()` selalu membuat baris `approval.log`; `write()`/`unlink()` log ditolak | `approval.mixin`, `approval.log` |
| AB-10 (O) | `ir.cron` harian → `_cron_kedaluwarsakan()` | `period.mixin` |
| AB-11 (O) | Hook `_sebelum_disahkan()` | `labfik.plan` |
| AB-12 (O) | Hook `_sebelum_ajukan()` + `@api.constrains` | `labfik.document.version` |
| AB-13 | `_sql_constraints` unique(document_id, revisi) | `labfik.document.version` |
| AB-14 | `_compute_tanggal_tinjau()` (store) dan `_search_perlu_ditinjau()` | `labfik.document.version` |
| AB-15, AB-16 | `@api.constrains` | `distribution`, `socialization`, `review` |
| AB-17 (O) | *Record rule* grup `labfik_pengguna`: `[('state', '=', 'disahkan')]` | `labfik.document.version` |
| AB-18 | `@api.constrains` (rencana disahkan, bukti wajib) + `_sql_constraints` unique(line_id, periode_lapor) + *record rule* (pelapor = PIC atau grup KaLab) | `labfik.realisasi` |
| AB-19, AB-20 | `@api.constrains` | `labfik.tinjauan` |
| AB-21 (O) | `compute` | `labfik.plan.line` |
| AB-22 | `unlink()` «override» ditolak; `action_koreksi()` + `mail.thread` *tracking*; hook `_boleh_dikoreksi()` | `evidence.mixin` |
| AB-23 | `unlink()` «override» menolak bila dirujuk; arsip lewat `active` | `hr.employee`, `hr.job`, `labfik.document`, `labfik.kpi` |
| AB-24 | `cek_monev()` + `@model hitung_persentase()` | `labfik.document` |
| AB-25 | `get_kriteria()` (Template: berhenti di kriteria pertama yang gagal) + `_cek_k1()`–`_cek_k4()` {abstract} | `criteria.mixin` + `labfik.plan`, `labfik.assignment` |

Semua 25 AB terpetakan.

---

## 7. Grup akses

| Grup | Mewarisi | Hak utama |
|---|---|---|
| `labfik_pengguna` | `base.group_user` | Membaca versi SOP/IK `disahkan` (O) |
| `labfik_laboran` | `labfik_pengguna` | Membuat dan mengubah Dokumen Induk, versi, distribusi, sosialisasi, tinjau ulang; mengisi realisasi item miliknya; melihat laporan pengendalian dokumen |
| `labfik_kalab` | `labfik_laboran` | Semua master, rencana, SK, rapat, evaluasi, tinjauan; **mengembalikan, mengesahkan, mencabut**; status monev |

Ketiga grup didefinisikan di addon **`labfik_core`**, bukan `labfik_org`, karena `approval.mixin` (Core) memeriksa `labfik_kalab` dan modul lain juga memakainya. Grup yang hanya dipakai satu modul (mis. `labfik_dosen`, `labfik_asisten` di Praktikum) tinggal di modul itu (keputusan I-5, [kontrak-core.md](kontrak-core.md)).

Grup ini tidak sama dengan aktor (Wazlawick §4.2). Wewenang **mengesahkan sebagai pejabat** diatur oleh `labfik.jabatan.wewenang`, bukan oleh grup. Karena itu Dekan tidak membutuhkan akun.

---

## 8. Perubahan dibanding versi sebelumnya

Versi sebelumnya ada di tag `rancangan-tatkel-v1` (DCD 1/3–3/3).

| Versi lama | Versi ini | Alasan |
|---|---|---|
| `labfik.personel`, `labfik.jabatan` (model sendiri) | `hr.employee`, `hr.job` diperluas + `labfik.jabatan.tugas`, `labfik.jabatan.wewenang` | Keputusan 14 Nov 2026 (arahan memperluas addon LGPL) |
| `approval.mixin` dengan status `diperiksa`, `action_tarik()`, `action_periksa()`, `action_catat_pengembalian()`, field `jabatan_pengesah_id`, `nama_penanda_tangan` | Tanpa tahap pemeriksaan dan penarikan; satu `action_kembalikan()`; pengesah = `hr.employee` | Keputusan 14 Nov 2026 |
| `_setelah_disahkan()` dipakai untuk mengganti dokumen lama | Hook khusus `_dokumen_diganti()` di Template Method; `_setelah_disahkan()` tetap ada untuk modul lain | Penggantian dokumen adalah aturan baku (AB-08), jadi masuk urutan tetap |
| `labfik.controlled.mixin` (kode, revisi, unit pemilik) | **Tidak dipakai** | Kode dan revisi hanya dipakai Dokumen Induk/Versi dan SK dengan makna berbeda; mixin tiga field tidak sepadan dengan manfaatnya |
| `mail.activity.mixin`, pengingat | Tidak dipakai | Prinsip "hitung, bukan jadwalkan" |
| `labfik.plan` jenis strategis dan IKU | `labfik.renstra` terpisah (unggahan); IKU dihapus | Keputusan 14 Nov 2026 |
| — | `labfik.org.monev` (layanan status monev), `labfik.tinjauan.manfaat`, `labfik.plan.gap` dirinci | Langkah 7–9 |
| Semua relasi bagian–keseluruhan digambar sebagai komposisi atau asosiasi biasa; `peserta_ids` Rapat hanya berupa atribut | **Agregasi** (belah ketupat putih) untuk `hr.job`–`hr.employee`, `labfik.document`–`labfik.ruang` (`lokasi_ids`), dan `labfik.meeting`–`hr.employee` (`peserta_ids`, kini digambar sebagai garis di DCD-2); legenda notasi ditambah; subbagian 3.2 (jenis pewarisan) dan 3.3 (jenis relasi) | Catatan bimbingan Pak Widi (November 2026). Diagram diedit langsung agar rapian manual tidak tertimpa; skrip arsip ikut diperbarui |
| DCD hanya berisi model | **Kelas view inti** di DCD-2 (`hr_job_view_hierarchy`), DCD-3 (`document_version_view_kanban`, `document_version_view_form`), DCD-4 (`plan_view_form`, `plan_line_view_calendar`, `realisasi_view_pivot`); catatan notasi view di halaman catatan; bagian 11 | Catatan bimbingan Pak Widi 19 November 2026 (kelas view, kanban/pivot/tree/Gantt). Skrip arsip **tidak** diperbarui |
| `labfik.realisasi` tanpa target | `+ target: Float {related: line_id.target, store}`, `group_operator='max'` | Pivot dan graph target vs capaian (bagian 11.3). Nilai tetap milik Item Rencana; tidak ada perubahan CM, UC, atau AB |

**Penyesuaian dengan kontrak Core bersama (15 November 2026):** `labfik.ruang` + `kapasitas` (I-3); grup akses ditempatkan di `labfik_core` (I-5); catatan `syarat_kompetensi_ids` dari SDM (I-2) dan `tindakan` wewenang tetap dua pilihan (I-4). Diagram DCD-2 dan DCD-3 dibuat ulang.

**Perubahan kontrak Core (keputusan Febriyan, 14 November 2026):** `labfik.controlled.mixin` dihapus dari daftar mixin Core; CLAUDE.md bagian 6 sudah diperbarui. Bila modul lain membutuhkannya, mixin itu bisa diusulkan kembali tanpa mengubah rancangan ini.

---

## 9. Cek silang akhir

| Pemeriksaan | Hasil |
|---|---|
| Setiap konsep CM punya model | Ya (bagian 2, kolom "Asal di CM"); Pengesahan dilebur ke mixin (bagian 3) |
| Setiap operasi SSD punya method atau ORM | Ya (bagian 5) |
| Setiap AB punya mekanisme | Ya (bagian 6) |
| Status sama dengan S1 | Ya: `draf`, `diajukan`, `disahkan`, `diganti`, `dicabut`, `kedaluwarsa` |
| Field warisan tidak ditulis ulang | Ya; model turunan hanya menulis field sendiri dan «override» |
| Kriteria instrumen | K1 → `approval.mixin` + `period.mixin`; K2–K4 dan S1–S5 → `_cek_k*()` dan `cek_monev()` |
| Data pribadi | Tidak ada nama orang, NIM, atau nomor HP di rancangan |
| Setiap UC punya layar | Ya (bagian 11.2): UC-01–06 lewat tombol header form turunan `approval.mixin`; UC-07 tanpa layar (`ir.cron`); UC-13, 20, 27, 28 lewat laporan QWeb (UC-27 juga pivot); sisanya list/form |
| Field dan atribut view ada | Ya: semua field di kelas view ada di model; atribut arsitektur view diperiksa di kode sumber Odoo 17 (image `odoo:17`, 20 November 2026) |

## 10. Isu terbuka

- [x] `labfik.controlled.mixin` dihapus dari kontrak Core (keputusan 14 November 2026)
- [ ] Dokumen Induk/Versi (PKG-09) dan KPI (PKG-21) dipakai modul lain? Bila ya, pakai modul jembatan (mis. `labfik_safety_org`) atau pindahkan ke `labfik_core` **[KONFIRMASI kelompok]**
- [x] Asisten lab sebagai `hr.employee` dengan jenis personel *asisten* dan jabatan (`hr.job`) **Asisten Praktikum** (keputusan 14 November 2026)
- [ ] Tampilan diagram belum dicek di draw.io **[VALIDASI]**
- [x] Garis yang ujungnya tidak menempel (`tk-dcd1-g-dis-evi`, `tk-dcd1-g-tin-evi`, `tk-dcd3-d-doc-ver`) sudah tersambung; `validate.py` bersih (20 November 2026)
- [x] Kelas view inti (catatan bimbingan 19 November 2026) digambar di DCD-2–4 (bagian 11)
- [x] Gantt tidak dipakai karena hanya ada di Odoo Enterprise; jadwal kegiatan memakai *calendar view* (keputusan Febriyan, 20 November 2026)
- [ ] Wireframe untuk enam view inti (bagian 11.4) dan tempatnya di proposal
- [ ] Kelas view dan field `target` belum masuk naskah Bab 2 (paragraf 2.3.4 dan gambar DCD-2–4 diganti setelah diekspor dari draw.io)

---

## 11. Lapisan antarmuka (view)

Ditambahkan 20 November 2026 untuk catatan bimbingan Pak Widi 19 November 2026: class diagram memuat kelas view; antarmuka memakai view kanban, pivot, tree, dan Gantt. Bagian ini menggantikan draf `view-tata-kelola.md` (dihapus) agar semua rancangan kelas tetap di satu dokumen.

### 11.1 Aturan

| Aturan | Sumber | Penerapan |
|---|---|---|
| Antarmuka diturunkan dari use case/SSD: layar harus memungkinkan aktor menjalankan semua alur use case | Wazlawick §16.1 | Setiap view menyebut UC yang dilayaninya. View tanpa UC tidak dibuat |
| Komponen dasar *List*, *Details*, *Form*, terikat ke kelas di DCD (*data binding*) | §16.3 | List = view `tree` Odoo ("tree" dalam arahan Pak Widi), Details + Form = view `form`. Satu view selalu milik **satu model utama**; model lain ikut tampil lewat field relasi |
| Pola *master-detail* dan *search* | §16.5 | Form dengan tab One2many (Item Rencana di Rencana); view `search` dengan filter dan *group by* |
| Tombol = operasi sistem | §16.6 | Operasi kelas view menunjuk method `action_*` (bagian 5), sehingga keterlacakannya UC → tombol → method → AB |
| *Sweet spot* | CLAUDE.md bagian 1 | Kanban, calendar, pivot, hierarchy hanya bila menjawab kebutuhan atau bukti tertentu. Model «CRUDL» cukup list + form. **Kelas view hanya digambar untuk view inti** (11.4) |

**Notasi kelas view** (juga di halaman catatan drawio): stereotype = jenis view («form», «kanban», «calendar», «pivot», «hierarchy»); nama = XML ID `ir.ui.view`; atribut = field yang tampil per bagian layar plus atribut arsitektur view (`default_group_by`, `date_start`, `row/col/measure`); operasi = tombol → method; garis putus-putus «view» = dependensi ke model utama.

**Jenis view Odoo 17 Community** (diperiksa di kode sumber image `odoo:17`, build 17.0-20260908, 20 November 2026):

| Jenis | Ada di Community | Catatan |
|---|---|---|
| list (`<tree>`), form, kanban, calendar, pivot, graph, search | Ya (`web`) | Kanban: `default_group_by`, `records_draggable`. Calendar: `date_start`, `date_stop`, `color`, `mode`, `quick_create` |
| hierarchy | Ya (`web_hierarchy`, LGPL-3, `depends: ['web']`) | Atribut `parent_field` menerima Many2one ke model yang sama, jadi bisa memakai `hr.job.atasan_id` |
| gantt | **Tidak** (`web_gantt` milik Enterprise) | Tidak dipakai. Jadwal kegiatan memakai calendar dengan rentang tanggal |

### 11.2 Matriks model × jenis view

✓ = disediakan; **E** = tabel anak (*embedded*) di form induk, tanpa menu sendiri; — = tidak; (O) = Pelengkap; **tebal** = view inti yang digambar sebagai kelas view.

| Model | List | Form | Kanban | Calendar | Pivot / Graph | Lainnya | Laporan QWeb | UC |
|---|---|---|---|---|---|---|---|---|
| `hr.employee` Personel | ✓ bawaan | ✓ bawaan + field baru | ✓ bawaan | — | — | — | — | UC-08 |
| `hr.job` Jabatan | ✓ | ✓ + tab Tugas, Wewenang | — | — | — | **Hierarchy** | Struktur organisasi | UC-09, 13 |
| `labfik.jabatan.tugas`, `.wewenang` | E | — | — | — | — | — | — | UC-09 |
| `labfik.ruang`, `labfik.periode` (Core) | ✓ *editable* | — | — | — | — | — | — | (master) |
| `labfik.assignment` SK Penetapan | ✓ | ✓ + tab Baris, Riwayat | ✓ per status | — | — | — | SK resmi (UC-02) | UC-10, 01–06 |
| `labfik.assignment.line` | E | — | — | — | — | — | — | UC-10 |
| `labfik.meeting` Rapat | ✓ | ✓ | — | ✓ tanggal | — | — | — | UC-11 |
| `labfik.org.evaluation` | ✓ | ✓ | — | — | — | — | — | UC-12 |
| `labfik.document` Dokumen Induk | ✓ | ✓ + tab Versi, *chatter* | — | — | — | — | Pengendalian dokumen | UC-14, 20 |
| `labfik.document.version` Versi SOP/IK | ✓ | **✓** + tombol rekaman, Riwayat | **✓ per status** | ✓ jadwal tinjau (O) | — | — | Dokumen resmi (UC-02) | UC-15, 01–06, 18, 19 |
| `labfik.document.distribution` / `.socialization` / `.review` | ✓ | ✓ | — | — | — | — | — | UC-16, 17, 18 |
| `labfik.renstra` | ✓ | ✓ | — | — | — | — | — | UC-22, 01–06 |
| `labfik.kpi` | ✓ | ✓ | — | — | — | — | — | UC-21 |
| `labfik.plan` Rencana | ✓ | **✓** + tab Gap, Item, Narasi, Riwayat | ✓ per status | — | — | — | Rencana resmi, laporan rencana | UC-23, 24, 27, 01–06 |
| `labfik.plan.line` Item Rencana | ✓ ("Item saya") + E | ✓ | — | **✓ jadwal kegiatan** | ✓ anggaran, target | — | — | UC-23, 25, 27 |
| `labfik.plan.gap` | E | — | — | — | — | — | — | UC-23 |
| `labfik.realisasi` | ✓ | ✓ | — | — | **✓ target vs capaian** | — | — | UC-25, 27 |
| `labfik.tinjauan` (+ `.manfaat` E) | ✓ | ✓ | — | — | — | — | — | UC-26 |
| `labfik.approval.log` | E (tab Riwayat, *read-only*) | — | — | — | — | — | — | UC-01–06 |
| `labfik.org.monev` | — | — | — | — | — | — | Laporan status monev (HTML) | UC-28 |

`labfik.org.monev` adalah AbstractModel tanpa tabel, sehingga tidak bisa punya list atau pivot. Status monev cukup laporan HTML dari `get_status()`, tanpa model baru. Rekaman Distribusi, Sosialisasi, dan Tinjau Ulang dibuka dari *smart button* di form Versi, karena relasinya Many2one satu arah ke Versi (tidak ada One2many balik di DCD-3).

### 11.3 Alasan view tambahan

| View | Model | Isi | Alasan |
|---|---|---|---|
| Kanban per status | Versi SOP/IK, Rencana, SK | Kolom draf · diajukan · disahkan; kartu tidak bisa diseret (`records_draggable: False`) | KaLab melihat dokumen yang menunggu pengesahan (UC-04, 05). Status hanya berubah lewat tombol agar Template Method tidak terlewat (AB-01). Satu pola untuk semua turunan `approval.mixin` |
| Calendar rentang | Item Rencana | `jadwal_mulai`–`jadwal_selesai`, warna per PIC | Rencana berjadwal (PKG-01, PKG-13); pengganti Gantt |
| Calendar | Rapat | `tanggal` | Rapat koordinasi berkala (PKG-03) |
| Calendar (O) | Versi SOP/IK | `tanggal_tinjau_berikutnya` | Jadwal tinjau ulang (AB-14, PKG-02 S4) |
| Pivot + graph | Realisasi | Baris item, kolom periode lapor; ukuran target (`max`), capaian (`sum`) | Laporan rencana UC-27 (KF-33, 34). `target` di-*related* dari Item Rencana dan dijumlah dengan `max` supaya tidak berlipat di total baris |
| Pivot | Item Rencana | Baris PIC/rencana; ukuran anggaran, target | Ringkasan anggaran rencana pengembangan (PKG-13) |
| Hierarchy | Jabatan | Pohon dari `atasan_id` | Struktur organisasi (UC-13, PKG-03) |

**Filter tersimpan utama:** *Menunggu pengesahan* (`state = diajukan`) dan *Draf saya* di semua turunan `approval.mixin` = bentuk antarmuka operasi SSD `daftar_dokumen(filter, user_id)`; *Item saya* (`pic_id.user_id = uid`, rencana disahkan) = `daftar_item_pic(user_id)`; *Perlu ditinjau* di Versi; *Belum lengkap* (`is_lengkap = False`) di Jabatan.

### 11.4 View inti (digambar di DCD)

| # | Kelas view | Halaman | UC kunci | Menunjukkan |
|---|---|---|---|---|
| V1 | `document_version_view_kanban` «kanban» | DCD-3 | UC-04, 05 | Kanban per status (pola semua turunan `approval.mixin`) |
| V2 | `document_version_view_form` «form» | DCD-3 | UC-15, 01–06, 16–18 | Header status + tombol pengesahan, *smart button* rekaman, riwayat |
| V3 | `plan_view_form` «form» | DCD-4 | UC-23, 24, 26 | *Master-detail*: tab Temuan Gap dan Item Rencana |
| V4 | `plan_line_view_calendar` «calendar» | DCD-4 | UC-23, 25 | Jadwal kegiatan (pengganti Gantt) |
| V5 | `realisasi_view_pivot` «pivot» | DCD-4 | UC-25, 27 | Target vs capaian per periode |
| V6 | `hr_job_view_hierarchy` «hierarchy» | DCD-2 | UC-09, 13 | Struktur organisasi |

Laporan status monev (UC-28) bukan view, jadi tidak digambar sebagai kelas view. Wireframe nanti dibuat untuk V1–V6 ditambah satu contoh list (Dokumen Induk) dan laporan status monev.
