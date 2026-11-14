# Kontrak Core untuk Modul SDM & Kompetensi

14 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 3 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). Bahan kerja: isinya dipakai di Langkah 9–10 (conceptual model dan DCD) dan diteruskan ke pemilik Core (Febriyan) serta pemilik Sesi (Herrens). Tidak ada diagram di langkah ini.

**Prinsip dari pengguna (14 November 2026):** Core **tidak diubah**. Modul SDM hanya memakai, mewarisi, atau memperluas Core dari addon `labfik_sdm`. Kebutuhan yang tidak bisa dipenuhi tanpa mengubah Core diajukan sebagai usulan ke pemiliknya.

**Keputusan pengguna (Zahir, 14 November 2026):**
1. Perubahan **tidak di-*merge* ke `main`** dulu; semua tetap di branch masing-masing. SDM merujuk kontrak Core versi branch `febriyan-skripsi`.
2. **Kelas, Mata Kuliah, dan Sesi masuk Core** (K-5). Sesi adalah transaksi (kejadian bisnis), tetapi ditaruh di Core sebagai **pengecualian** karena dipakai enam package dan menghindari ketergantungan melingkar.
3. Penugasan dicatat sebagai **Surat Tugas bergaris** (K-6).

## Sumber

| Sumber | Versi | Dipakai untuk |
|---|---|---|
| Tabel kontrak Core di `CLAUDE.md` bagian 6 | **Branch `origin/febriyan-skripsi`**, commit `e796842` (14 Nov 2026). Versi ini **belum ada di `main`** maupun di branch `zahir-skripsi`, yang masih memuat `controlled.mixin` dan status asisten [KONFIRMASI] | Daftar model dan mixin Core yang berlaku |
| `design-class-tata-kelola.md` + `design_class.py` | `origin/febriyan-skripsi` | Field, method, dan *hook* persis tiap mixin; grup akses |
| `brief-seluruh-projek.md` | `main` | Usulan Sesi di Core (*inherit* `op.session`), pertanyaan terbuka kelompok |
| [brief-sdm.md](../brief/brief-sdm.md), [analisis PKG-04](../analisis/analisis-data-pengelolaan-4.md), [PKG-10](../analisis/analisis-data-pengelolaan-10.md), [PKG-14](../analisis/analisis-data-pengembangan-14.md) | `zahir-skripsi` (commit `ab55048`) | Kebutuhan model SDM |
| [bedah-dokumen-sdm.md](../analisis/bedah-dokumen-sdm.md) | Draf belum di-commit | Temuan A6, A10, A18, A20 yang berdampak ke kontrak |

## Aturan yang dipakai

| Aturan | Sumber | Penerapan |
|---|---|---|
| Komponen yang sudah bekerja **tertutup untuk diubah, terbuka untuk diperluas** (*open-closed*) | Wazlawick §4.7.1 | Core tidak diubah. `labfik_sdm` memakai `_inherit` pada `hr.job`/`hr.employee`, `selection_add` pada jenis dokumen wewenang, dan data *seed* |
| ***Specification class***: atribut yang sama untuk semua *exemplar* ditaruh di kelas spesifikasi; atribut yang berbeda per *exemplar* di kelas *exemplar* | §11.3 | **Kompetensi** = spesifikasi; **Bukti Kompetensi** = *exemplar* milik satu personel (nomor, penerbit, masa berlaku). Syarat di Jabatan merujuk spesifikasi, bukan *exemplar* |
| Pasangan tanggal awal–akhir adalah satu **interval**; objek yang berlaku sementara memakai pola ***effectivity*** | §11.11, §11.12.1 | Masa berlaku Bukti Kompetensi dan Otorisasi, serta rentang berlaku Penugasan, ditulis sebagai interval tanggal milik objeknya sendiri, bukan `periode_id` (lihat [K-3](#k-3-periodmixin-tidak-cocok-untuk-masa-berlaku-perorangan)) |
| ***Superseding***: objek baru menggantikan objek lama tanpa menghapusnya | §11.9.2 | Otorisasi versi baru mengganti versi lama lewat *hook* `_dokumen_diganti()` di `approval.mixin` |
| Tanggung jawab diberikan ke objek yang memegang datanya (**delegasi**), bukan dipusatkan di satu kelas | §13.2 (Tabel 13–1) | Cek wewenang tetap didelegasikan ke `hr.job.punya_wewenang()` (Core). Cek kompetensi didelegasikan ke personel (`hr.employee`, diperluas SDM), bukan ke Penugasan atau Otorisasi |
| Grup akses tidak sama dengan aktor | §4.2 (dikutip DCD Tata Kelola) | SDM memakai grup Core `labfik_laboran` dan `labfik_kalab`; wewenang mengesahkan tetap lewat Jabatan |

---

## 1. Yang dipakai SDM dari Core

| Model / mixin Core | Isi yang dipakai (dari DCD Tata Kelola) | Dipakai oleh (model SDM, nama sementara) | Cara | Cocok? |
|---|---|---|---|---|
| `hr.employee` (diperluas Core) | `jenis_personel` {dosen, laboran_plp, teknisi, asisten, petugas_k3}, `unit`, `job_id`, `user_id`; `unlink()` ditolak | Semua rujukan orang: calon/asisten, laboran, penilai, peserta pelatihan, supervisor | Rujuk (Many2one). Filter PKG-10: `jenis_personel = laboran_plp`; PKG-14: `in (laboran_plp, teknisi)` | ✓. Keputusan Febriyan (asisten = `hr.employee` jenis *asisten*, jabatan **Asisten Praktikum**) menjawab [KONFIRMASI] di brief SDM |
| `hr.job` (diperluas Core) | `unit`, `is_eksternal`, `syarat_kompetensi: Text`, `punya_wewenang(tindakan, jenis)`, `cari_pemegang_berwenang()` | Syarat kompetensi per jabatan; pengesah Penugasan, Otorisasi, Rencana Pelatihan | Rujuk + perluas (lihat bagian 2) | **Sebagian**: `syarat_kompetensi` berupa teks, sedangkan SDM butuh daftar Kompetensi terstruktur ([K-1](#k-1-syarat_kompetensi-di-core-berupa-teks)) |
| `labfik.jabatan.wewenang` | `tindakan` {menyusun, mengesahkan}, `jenis_dokumen: Selection`, unik per (jabatan, tindakan, jenis) | Wewenang mengesahkan dokumen SDM | Perluas pilihan `jenis_dokumen` + *seed* baris wewenang (bagian 2) | ✓ lewat `selection_add` ([K-2](#k-2-jenis-dokumen-sdm-belum-terdaftar)) |
| `labfik.ruang` | Master ruang | Sasaran penugasan **laboran per ruang** (temuan A10) | Rujuk | ✓ |
| `labfik.periode` | `name`, `jenis`, `tanggal_mulai`, `tanggal_selesai` | Periode seleksi (semester), Rencana Pelatihan (tahunan), periode monev | Rujuk | ✓ |
| `labfik.approval.mixin` + `labfik.approval.log` | `state` {draf, diajukan, disahkan, diganti, dicabut, kedaluwarsa}; `action_ajukan()`, `action_sahkan(pengesah, tanggal_sah)` (Template Method), `berkas_ttd` wajib, `_jenis_dokumen()` / `_cek_kelengkapan()` {abstract}; *hook* `_sebelum_ajukan()`, `_sebelum_disahkan()`, `_dokumen_diganti()`, `_setelah_disahkan()`; sahkan hanya grup `labfik_kalab` | Surat Tugas/Penugasan, Otorisasi, Rencana Pelatihan | `_inherit` | ✓ |
| `labfik.period.mixin` | `periode_id` → `labfik.periode`; `tanggal_mulai/selesai` {related}; `is_berlaku` {compute}; penjadwal kedaluwarsa (O) | Rencana Pelatihan (periode tahunan) | `_inherit` | ✓ untuk Rencana Pelatihan; **tidak cocok** untuk Otorisasi ([K-3](#k-3-periodmixin-tidak-cocok-untuk-masa-berlaku-perorangan)) |
| `labfik.criteria.mixin` | `kriteria_tertinggi` {compute}, `get_kriteria(tanggal_acuan)`, `_cek_k1()`–`_cek_k4(tanggal)` {abstract} | Rencana Pelatihan (PKG-14 K1–K4) | `_inherit` | ✓ |
| `labfik.evidence.mixin` | `tanggal`, `pelapor_id`, `bukti_ids` (lampiran), `keterangan`; `unlink()` ditolak; `action_koreksi()`; *hook* `_boleh_dikoreksi()` | Bukti Kompetensi, Kebutuhan Petugas, Seleksi, Asesmen, Evaluasi Ulang Otorisasi, Realisasi Pelatihan, Evaluasi Efektivitas | `_inherit` | ✓ |
| Grup `labfik_pengguna` ⊂ `labfik_laboran` ⊂ `labfik_kalab` | Hak baca/tulis berjenjang | Aktor SDM: Laboran/PLP (mencatat), KaLab (menetapkan, mengesahkan) | Rujuk di ACL `labfik_sdm` | ✓, asalkan grup didefinisikan di `labfik_core` ([K-4](#k-4-lokasi-grup-akses)) |
| `labfik.controlled.mixin` | — | — | — | Tidak dipakai (Core terbaru menghapusnya; SDM memang tidak membutuhkannya) |

### Peta mixin per model SDM

| Model SDM | Mixin | *Hook* / method abstrak yang diisi |
|---|---|---|
| `labfik.sdm.kompetensi` [M] | — | — |
| `labfik.sdm.bukti.kompetensi` [T] | evidence | `berlaku_sampai` + `is_berlaku` {compute} sendiri (*effectivity*, §11.12.1) |
| `labfik.sdm.kebutuhan.petugas` [T] | evidence | — (pelapor = penetap; bukti = formulir alokasi) |
| `labfik.sdm.seleksi` [T] | evidence | `memenuhi_syarat_nilai` {compute} |
| `labfik.sdm.surat.tugas` [T] (K-6) | approval | `_jenis_dokumen()` = `penugasan_petugas`; `_cek_kelengkapan()` (≥1 baris, setiap baris lengkap); `_dokumen_diganti()` = surat yang direvisi |
| `labfik.sdm.penugasan` [T] (baris Surat Tugas) | — | Sah bila suratnya `disahkan`; `is_berlaku(tanggal)` dari `berlaku_mulai/sampai` |
| `labfik.sdm.tugas.khusus` [M] | — | — |
| `labfik.sdm.asesmen` [T] | evidence | — |
| `labfik.sdm.otorisasi` [T] | approval (tanpa period) | `_jenis_dokumen()` = `otorisasi`; `_cek_kelengkapan()` (dasar kompetensi, lingkup, supervisor bila terbimbing); `_dokumen_diganti()` = otorisasi berlaku untuk pasangan yang sama (*superseding*) |
| `labfik.sdm.evaluasi.otorisasi` [T] | evidence | — |
| `labfik.sdm.rencana.pelatihan` [T] | approval, period, criteria | `_jenis_dokumen()` = `rencana_pelatihan`; `_cek_kelengkapan()`; **`_sebelum_ajukan()` = bekukan Kebutuhan Kompetensi** (keputusan analisis PKG-14); `_cek_k1()`–`_cek_k4()` |
| `labfik.sdm.realisasi.pelatihan` [T] | evidence | — |
| `labfik.sdm.evaluasi.pelatihan` [T] | evidence | Bila efektif → buat Bukti Kompetensi (delegasi, §13.2) |
| `labfik.sdm.monev` | AbstractModel (layanan) | `get_status()`; pola sama dengan `labfik.org.monev` |

---

## 2. Perluasan oleh `labfik_sdm` (Core tidak diubah)

| Perluasan | Bentuk | Alasan |
|---|---|---|
| `hr.job` + `syarat_kompetensi_ids` | `_inherit = 'hr.job'`; Many2many ke `labfik.sdm.kompetensi` | Syarat terstruktur untuk menghitung S3 (PKG-04), S1 (PKG-10), dan gap (PKG-14). Field teks Core `syarat_kompetensi` tetap ada sebagai uraian naratif ([K-1](#k-1-syarat_kompetensi-di-core-berupa-teks)) |
| `hr.employee` + `bukti_kompetensi_ids` (One2many) + `punya_kompetensi(kompetensi, tanggal)` + `kompetensi_kurang(tanggal)` | `_inherit = 'hr.employee'` | Delegasi (§13.2): personel yang memegang buktinya, jadi personel yang menjawab "apakah saya punya kompetensi X yang berlaku pada tanggal T" |
| `labfik.jabatan.wewenang.jenis_dokumen` + `penugasan_petugas`, `otorisasi`, `rencana_pelatihan` | `selection_add` | Agar `approval.mixin._cek_wewenang()` bisa memeriksa pengesah dokumen SDM tanpa kode baru ([K-2](#k-2-jenis-dokumen-sdm-belum-terdaftar)) |
| Baris wewenang awal | Data XML `labfik_sdm`: (KaLab, mengesahkan, otorisasi); (KaLab, mengesahkan, penugasan_petugas) **[KONFIRMASI K7]**; (KaLab dan/atau Wadek Bidang Keuangan dan Umum, mengesahkan, rencana_pelatihan) **[KONFIRMASI K10]** | Data, bukan perubahan Core. Wadek dicatat sebagai `hr.job` dengan `is_eksternal = True`, seperti Dekan di Tata Kelola |
| Jabatan awal | Data XML: Laboran/PLP, Teknisi Jaringan, Asisten Praktikum (bila belum ada dari `labfik_core`) | Sumber: slide PKKMB (D8a) dan keputusan Febriyan |

---

## 3. Isu kontrak dan keputusan

### K-1 `syarat_kompetensi` di Core berupa teks

**Masalah.** DCD Tata Kelola mendefinisikan `hr.job.syarat_kompetensi: Text [0..1]`. Analisis PKG-04 (keputusan 14 Nov 2026) mengasumsikan Core belum punya field ini dan SDM menambahkan versi terstruktur. Teks tidak bisa dipakai untuk menghitung S3 PKG-04 atau gap PKG-14.

**Keputusan [USULAN PENULIS].** Core tetap. `labfik_sdm` menambah `syarat_kompetensi_ids` (Many2many). Pembagian makna:

| Field | Pemilik | Makna | Dipakai oleh |
|---|---|---|---|
| `syarat_kompetensi` (Text) | Core | Uraian naratif untuk dokumen struktur/SK (PKG-03) | Tata Kelola |
| `syarat_kompetensi_ids` (Many2many) | SDM | Daftar Kompetensi yang wajib dimiliki; dasar perhitungan | SDM |

Risiko: dua field dengan nama mirip bisa diisi tidak selaras. Mitigasi: label tampilan dibedakan ("Uraian syarat kompetensi" vs "Kompetensi wajib"), dan di form SDM yang diedit hanya field terstruktur. **[KONFIRMASI Febriyan]**: apakah keduanya boleh hidup berdampingan, atau Febriyan lebih memilih Core memakai field SDM saat `labfik_sdm` terpasang.

### K-2 Jenis dokumen SDM belum terdaftar

**Masalah.** `approval.mixin._cek_wewenang()` memanggil `hr.job.punya_wewenang('mengesahkan', self._jenis_dokumen())`. Pilihan `jenis_dokumen` di `labfik.jabatan.wewenang` saat ini hanya jenis dokumen Tata Kelola.

**Keputusan.** `labfik_sdm` memakai `selection_add` untuk menambah tiga jenis. Ini mekanisme standar Odoo untuk memperluas *Selection* dari addon lain tanpa mengubah addon asal. **[KONFIRMASI Febriyan]**: `jenis_dokumen` memang `fields.Selection` (bukan Many2one ke master) dan tidak di-*hardcode* di method lain.

### K-3 `period.mixin` tidak cocok untuk masa berlaku perorangan

**Masalah.** `labfik.period.mixin` menautkan dokumen ke satu `labfik.periode` (master periode bersama). Brief dan analisis PKG-10 menulis Otorisasi mewarisi `period.mixin`. Padahal masa berlaku otorisasi dihitung **per orang** sejak tanggal disahkan (mis. 12 bulan); setiap otorisasi punya rentang sendiri yang tidak sama dengan semester atau tahun anggaran. Hal yang sama berlaku untuk Bukti Kompetensi (sertifikat BNSP berlaku 3 tahun sejak terbit, temuan A13) dan rentang Penugasan (mulai pertemuan 5, temuan A6).

**Keputusan [USULAN PENULIS].** Ketiga model **tidak** memakai `period.mixin`. Masa berlaku menjadi interval tanggal milik objek (§11.11, §11.12.1): `berlaku_mulai`, `berlaku_sampai`, dan `is_berlaku` {compute} dihitung dari tanggal acuan. Konsekuensi:
- Status Otorisasi tidak otomatis berubah menjadi `kedaluwarsa` (penjadwal itu milik `period.mixin`). S2 PKG-10 memakai `is_berlaku`, bukan `state`. Ini sejalan dengan prinsip *sweet spot* "hitung, bukan jadwalkan".
- Operasi interval (apakah tanggal T di dalam masa berlaku) ditulis tiga kali. Bila mengganggu, `labfik_sdm` boleh membuat mixin lokal `labfik.sdm.interval.mixin` (di modul SDM, bukan Core).
- `period.mixin` tetap dipakai Rencana Pelatihan (satu rencana per periode tahunan).

### K-4 Lokasi grup akses

**Masalah.** Grup `labfik_pengguna`, `labfik_laboran`, `labfik_kalab` didefinisikan di DCD Tata Kelola, tetapi tabel kontrak Core tidak menyebut grup. Bila grup itu ada di `labfik_org`, `labfik_sdm` tidak bisa merujuknya tanpa bergantung ke modul Tata Kelola. Aksi `action_sahkan()` di `approval.mixin` (Core) juga memeriksa grup `labfik_kalab`, jadi secara logika grup itu memang harus ada di Core.

**Keputusan.** SDM mengasumsikan ketiga grup ada di `labfik_core` **[ASUMSI; KONFIRMASI Febriyan]**. SDM tidak membuat grup sendiri.

### K-5 Kelas, Mata Kuliah, dan Sesi tidak ada di Core

**Masalah.** PKG-04 bergantung pada Kelas (Kebutuhan Petugas, Penugasan), Mata Kuliah (Seleksi), dan Sesi (unit penilaian, penyebut). Ketiganya **tidak tercantum** di tabel kontrak Core maupun DCD Tata Kelola. Brief bersama (`main`) mengusulkan Sesi di Core dengan *inherit* `op.session` (OpenEduCat), tetapi brief Tata Kelola menetapkan "Odoo 17 Community, berdiri sendiri tanpa OpenEduCat", dan `labfik_core` hanya `depends: ['hr', 'mail']`. Statusnya masih pertanyaan terbuka kelompok ("Apakah Sesi masuk Core dan dibangkitkan PKG-15?").

**Mengapa harus di Core, bukan di modul Praktikum.** `labfik_praktikum` bergantung ke `labfik_sdm` (pemetaan: PKG-18 memakai Penugasan PKG-04). Bila Kelas/Sesi ditaruh di `labfik_praktikum`, `labfik_sdm` harus bergantung balik ke `labfik_praktikum` → **dependensi melingkar**.

**Keputusan Zahir (14 November 2026), diajukan ke Herrens dan Febriyan [KONFIRMASI kelompok].** Tiga model ditambahkan ke `labfik_core` (penambahan, bukan perubahan model yang ada), tanpa OpenEduCat. Kelas dan Mata Kuliah adalah master. **Sesi adalah transaksi** (kejadian bisnis: satu pertemuan pada tanggal tertentu) yang sengaja menjadi **satu-satunya transaksi di Core**, sesuai alasan di [pemetaan bersama](../analisis/pemetaan-package-instrumen.md) ("Kenapa Sesi ditaruh di Core, padahal transaksi?"): dipakai enam package (04, 08, 15, 16, 17, 18) dan menghindari ketergantungan melingkar. Kontrak minimum yang dibaca SDM:

| Model (nama usulan) | Field minimum yang dibaca SDM | Ditulis oleh | Dibaca SDM untuk |
|---|---|---|---|
| `labfik.mata.kuliah` [M] | `kode` «unique», `name`, `prodi` | PKG-15 / data awal | Seleksi per MK |
| `labfik.kelas` [M] | `mata_kuliah_id`, `periode_id`, `name` (A, B, PBI, …) | PKG-15 | Kebutuhan Petugas, Penugasan asisten |
| `labfik.sesi` [T] | `kelas_id`, `tanggal`, `pertemuan_ke`, `ruang_id` (→ `labfik.ruang`), `state` {terjadwal, terlaksana, batal} | Dibangkitkan PKG-15; `state = terlaksana` diisi PKG-18 | Unit PKG-04, penyebut (sesi terlaksana), laboran dari ruang sesi |

SDM tidak menulis ke ketiga model ini. Sementara belum disepakati, rancangan SDM menggambar ketiganya sebagai kelas «Core (usulan)» putus-putus.

**Tambahan untuk Herrens (dari temuan A18).** Laporan pelaksanaan sekarang tidak bisa dicocokkan dengan alokasi karena tidak ada ID bersama. Di TO-BE, petugas yang hadir di sesi (PKG-18) sebaiknya merujuk `hr.employee` yang sama dengan Penugasan (PKG-04), bukan teks nama.

### K-6 Pengesahan per baris penugasan terlalu berat

**Masalah.** Analisis PKG-04 menulis Penugasan Petugas memakai `approval.mixin` per baris (personel × kelas). Pada 2026/2027 Ganjil ada 32 kelas berasisten ditambah penugasan laboran per ruang (temuan A6, A10). Bila tiap baris harus diajukan, diunggah berkas bertanda tangan, dan disahkan, KaLab mengulang langkah yang sama puluhan kali, padahal surat tugas di dunia nyata biasanya satu dokumen untuk banyak orang (bandingkan "Daftar Nama Asisten" per periode di POB 2025, temuan A3/D1).

**Keputusan Zahir (14 November 2026): Surat Tugas bergaris.** Pola yang sama dengan SK Penetapan Tata Kelola (`labfik.assignment` + `labfik.assignment.line`):
- `labfik.sdm.surat.tugas` [T]: satu surat per periode (atau per gelombang), `_inherit` approval; disahkan **sekali** untuk semua barisnya; `_dokumen_diganti()` = surat yang direvisi.
- `labfik.sdm.penugasan` [T]: baris surat (personel, kelas **atau** ruang, peran, `berlaku_mulai/sampai`); sah bila suratnya `disahkan`.
- Pengganti di tengah semester (Pelengkap): revisi surat (versi baru mengganti versi lama) atau surat tambahan berisi baris pengganti; dipilih di Langkah 4.

Dampak: "Surat Tugas" berubah dari [R] menjadi [T] dengan baris. Analisis PKG-04 dan brief perlu disesuaikan (bagian 7.3).

---

## 4. Yang disediakan SDM ke modul lain

| Data / method | Dipakai oleh | Arah addon |
|---|---|---|
| `labfik.sdm.penugasan` (petugas per kelas/ruang dan rentang berlaku) | PKG-18 (cocokkan petugas hadir), PKG-08 (jumlah petugas per sesi) | `labfik_praktikum` → `labfik_sdm` (sesuai pemetaan); PKG-08 lewat modul jembatan (kelompok lain) |
| `hr.employee.punya_kompetensi()`, Matriks Kompetensi | Opsional PKG-13 (gap aspek kompetensi) | Bila diotomatiskan: `labfik_org` → `labfik_sdm` atau modul jembatan |
| Daftar Operator Sah / cek berwenang (personel, tugas/alat, tanggal) | Peluang untuk Aset/Praktikum | Tidak dirancang sekarang |

## 5. Dependensi addon

```
hr, mail
   └── labfik_core      Personel/Jabatan (hr), ruang, periode, 4 mixin, grup
                        + usulan K-5: mata kuliah, kelas, sesi
        ├── labfik_org         Tata Kelola
        ├── labfik_sdm         SDM & Kompetensi   (depends: labfik_core)
        │     └── labfik_praktikum   Praktikum    (depends: labfik_sdm)
        └── (kelompok lain: aset, safety; jembatan bila perlu)
```

`labfik_sdm` hanya bergantung ke `labfik_core`. Tidak ada rujukan ke `labfik_org` maupun `labfik_praktikum`.

---

## 6. Perbandingan dengan contoh Tata Kelola

| Aspek | Tata Kelola (`origin/febriyan-skripsi`) | SDM (dokumen ini) |
|---|---|---|
| Peran terhadap Core | **Pemilik**: merancang mixin, `hr.employee`/`hr.job`, ruang, periode | **Pemakai**: memetakan kebutuhan ke Core yang ada |
| Bentuk keluaran Langkah 3 | Tidak ada dokumen terpisah; kontrak ditulis di CLAUDE.md bagian 6, brief ("Kontrak dengan modul lain"), dan DCD bagian 2.1 | Dokumen terpisah ini, dengan daftar isu (K-1–K-6) yang diajukan ke pemilik Core |
| Cara memakai mixin | Empat mixin dipakai 13 model `labfik_org` | Empat mixin dipakai 9 model SDM; `period.mixin` hanya di Rencana Pelatihan (K-3) |
| Pola dokumen bergaris | SK Penetapan + baris | Diusulkan sama untuk Surat Tugas + baris Penugasan (K-6) |
| Ketergantungan ke modul lain | Dokumen Induk/KPI tetap di `labfik_org`; modul lain lewat jembatan | Butuh Kelas/MK/Sesi dari Core (K-5); tanpa itu terjadi ketergantungan melingkar |

---

## 7. Cek silang, isu terbuka, dan koreksi

### 7.1 Cek silang ke langkah sebelumnya

| Keputusan sebelumnya | Hasil cek terhadap Core | Status |
|---|---|---|
| Kompetensi = master sendiri; syarat ditambahkan `labfik_sdm` ke `hr.job` (analisis PKG-04, brief) | Core ternyata sudah punya `syarat_kompetensi` (Text). Perluasan tetap bisa, tetapi kini ada dua field | Disesuaikan (K-1) |
| Asisten sebagai Personel [KONFIRMASI] (brief) | Diputuskan Febriyan: `hr.employee` jenis *asisten*, jabatan Asisten Praktikum | Terjawab (belum di `main`) |
| Otorisasi mewarisi `approval` + `period` (analisis PKG-10, brief pola B) | `period.mixin` memakai `periode_id`, tidak cocok untuk masa berlaku perorangan | **Diubah** (K-3) |
| Rencana Pelatihan mewarisi `approval` + `criteria`; kebutuhan dibekukan saat diajukan (analisis PKG-14) | Ada *hook* `_sebelum_ajukan()` yang pas; `period.mixin` cocok (periode tahunan) | ✓, ditambah `period` |
| Bukti Kompetensi dan Realisasi mewarisi `evidence` (brief pola C) | ✓; `unlink()` ditolak sesuai sifat bukti | ✓ |
| Penugasan per kelas dengan rentang berlaku (bedah dokumen A6) dan laboran per ruang (A10) | `labfik.ruang` ada di Core; Kelas belum ada (K-5) | Sebagian |
| Aktor KaLab dan Laboran/PLP (brief) | Grup `labfik_kalab`, `labfik_laboran` ada; lokasinya perlu dipastikan (K-4) | Sebagian |
| Sesi/Kelas dari Core (brief, analisis PKG-04) | Tidak ada di kontrak Core | Terbuka (K-5) |
| Cakupan Inti/Pelengkap (brief) | Tidak ada perluasan yang menambah fitur di luar cakupan. K-6 mengubah bentuk Surat Tugas, bukan menambah fitur | ✓ |

### 7.2 [KONFIRMASI]

| No | Pertanyaan | Ke siapa |
|---|---|---|
| KC-1 | Boleh `syarat_kompetensi` (Text, Core) dan `syarat_kompetensi_ids` (Many2many, SDM) berdampingan? (K-1) | Febriyan |
| KC-2 | `labfik.jabatan.wewenang.jenis_dokumen` adalah `Selection` yang boleh diperluas dengan `selection_add`? (K-2) | Febriyan |
| KC-3 | Grup `labfik_pengguna/laboran/kalab` didefinisikan di `labfik_core`? (K-4) | Febriyan |
| KC-4 | Zahir sudah memutuskan Kelas, Mata Kuliah, Sesi masuk `labfik_core` (tanpa OpenEduCat). Tinggal persetujuan pemilik: setuju field minimum di K-5? Siapa yang menulis `state` sesi? | Herrens, Febriyan |
| KC-5 | Petugas hadir di PKG-18 merujuk `hr.employee` (bukan teks)? (K-5, A18) | Herrens |
| KC-6 | ~~Merge ke `main`?~~ **Diputuskan Zahir:** belum di-*merge*; perubahan tetap di branch masing-masing | — |
| KC-7 | ~~Surat Tugas bergaris?~~ **Diputuskan Zahir:** ya (K-6) | — |
| Lama | K7 (kontrak asisten = dasar penugasan?) dan K10 (pengesah rencana pelatihan) dari bedah dokumen menentukan baris wewenang awal | KaLab |

### 7.3 Dokumen lain yang perlu ikut berubah

**Status (14 November 2026):** perubahan untuk brief dan analisis PKG-04, PKG-10, PKG-14 **sudah diterapkan**. Dua file bersama (`CLAUDE.md`, `brief-seluruh-projek.md`) sengaja tidak diubah.

| Dokumen | Perubahan |
|---|---|
| [brief-sdm.md](../brief/brief-sdm.md) "Pola bersama" baris B | Otorisasi: hapus `period.mixin` (K-3) |
| [brief-sdm.md](../brief/brief-sdm.md) "Kontrak dengan modul lain" | Rujuk dokumen ini; tambah K-5 (Kelas/MK/Sesi di Core) dan perluasan `selection_add` |
| [brief-sdm.md](../brief/brief-sdm.md) "Pertanyaan terbuka", butir kelompok | Asisten sebagai Personel terjawab (keputusan Febriyan); ganti dengan KC-1–KC-6 |
| [analisis-data-pengelolaan-4.md](../analisis/analisis-data-pengelolaan-4.md) bagian 3–6 | Isu penempatan Kompetensi: Core sudah punya `syarat_kompetensi` (Text) → K-1. Surat Tugas: [R] → [T] bergaris dengan baris Penugasan (K-6). Sesi, Kelas, MK: dari Core (K-5) |
| [analisis-data-pengelolaan-10.md](../analisis/analisis-data-pengelolaan-10.md) bagian 4 | Otorisasi: `approval.mixin` saja + interval sendiri (K-3); "kedaluwarsa dari period.mixin" diganti `is_berlaku` |
| [analisis-data-pengembangan-14.md](../analisis/analisis-data-pengembangan-14.md) bagian 4 | Rencana Pelatihan: tambah `period.mixin`; pembekuan kebutuhan lewat `_sebelum_ajukan()` |
| `CLAUDE.md` (file bersama, branch `zahir-skripsi`) | Belum memuat keputusan Core terbaru (asisten, `controlled.mixin`). Tunggu *merge* dari Febriyan; jangan diubah sendiri |
| `brief-seluruh-projek.md` (file bersama) | Baris "Sesi … *inherit* `op.session`" bertentangan dengan Core tanpa OpenEduCat → diajukan lewat KC-4, tidak diubah sendiri |

### 7.4 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| Langkah 0–2 (analisis, brief, bedah dokumen) | Kontrak Core dibaca dari `CLAUDE.md` di branch sendiri dan tag `rancangan-tatkel-v1`, padahal versi terbaru ada di `origin/febriyan-skripsi` | Langkah ini memakai versi `febriyan-skripsi`; perbedaannya dicatat (KC-6) |
| Analisis PKG-04 bagian 6 (keputusan "pilihan 2") | Mengira Core belum punya syarat kompetensi, sehingga SDM "menambahkan" field. Core ternyata sudah punya versi teks | K-1 |
| Brief pola B dan analisis PKG-10 | Otorisasi ditulis mewarisi `period.mixin` tanpa mengecek bahwa mixin itu berbasis `periode_id` | K-3 |
| Analisis PKG-04 | Penugasan memakai pengesahan per baris tanpa menimbang jumlah barisnya | K-6 (usulan) |
| Brief "Kontrak dengan modul lain" | Kelas, MK, dan Sesi ditulis "dari Core" seolah sudah dikontrakkan, padahal belum | K-5 |
