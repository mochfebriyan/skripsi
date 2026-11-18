# Design Class Diagram Modul Pelaksanaan Praktikum

16 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Langkah 10 (terakhir) alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (*class diagram*). Dasar implementasi addon `labfik_praktikum` dan model Praktikum di `labfik_core` (Odoo 17 Community).

Diagram: [class-praktikum.drawio](class-praktikum.drawio), 5 halaman (DCD-1 s.d. DCD-5). Skrip pembuatnya: [tools/drawio/praktikum/design_class.py](../tools/drawio/praktikum/design_class.py) (mesin gambar dari `contoh-tata-kelola/design_class.py` branch `febriyan-skripsi`; prefiks `prk-dcd`, penempatan label, dan data diganti). `validate.py` dengan prefiks `prk-`: **OK** di kelima halaman; [cek_tampilan.py](../tools/drawio/praktikum/cek_tampilan.py): **0** garis menembus kotak lain. Tampilan dicek lewat ekspor PNG draw.io desktop (16 Nov 2026). **Gaya diubah ke polos hitam-putih** (17 Nov 2026, CLAUDE.md bagian 5): tanpa warna, huruf Times New Roman, judul dan catatan dipindah ke halaman `Catatan … (bahan kerja)` di akhir file. Diperiksa ulang 18 Nov 2026: `validate.py` dengan prefiks `prk-` **OK** di semua halaman; `cek_tampilan.py` **0** garis menembus kotak lain. Tampilan di draw.io belum dilihat ulang setelah perubahan gaya.

Sumber: [conceptual-model-praktikum.md](conceptual-model-praktikum.md) (CM-1–4), katalog operasi dan kamus DTO di [ssd-praktikum.md](ssd-praktikum.md), AB-PRK-01–34 di [expanded-use-case-praktikum.md](expanded-use-case-praktikum.md), [kontrak-core.md](kontrak-core.md) (16 November 2026), DCD Tata Kelola (`design-class-tata-kelola.md`, branch `febriyan-skripsi`) untuk mixin Core, dan rancangan SDM (`kontrak-core-sdm.md`, `kebutuhan-sdm.md`, branch `zahir-skripsi`) untuk penugasan petugas.

---

## 1. Aturan yang dipakai

| Aturan | Sumber | Penerapan |
|---|---|---|
| DCD dimulai dari salinan conceptual model, lalu: tambah method, beri arah asosiasi, rinci tipe, ubah struktur bila perlu | Wazlawick §13.6 | Bagian 3 |
| Tanggung jawab diberikan ke objek yang memegang datanya (*delegation*), bukan dikumpulkan di kontroler (*concentration*) | §13.2, §13.5 | Operasi SSD menjadi method model. Contoh: wewenang → `hr.job.punya_wewenang()`; petugas sesi → `labfik.sesi.get_petugas_ditugaskan()` → `labfik.sdm.penugasan`; status monev → `get_cek_monev()`, `berbukti`, `get_kriteria()` di model pemilik data |
| Jenis method: *get/set* atribut, *add/remove* tautan, dan method delegasi | §13.2, Tabel 13–1 | *get/set* dan *add/remove* disediakan ORM Odoo dan tidak digambar; yang digambar: method delegasi, `compute`, `constrains`, *hook*, «override» |
| Arah asosiasi mengikuti arah pesan; controller tidak dirujuk | §13.6 | Many2one dari perujuk ke yang dirujuk (anak → induk, transaksi → master); komposisi = One2many + Many2one |
| Perilaku bersama sebagai *mixin* `AbstractModel`, model turunan memakai `_inherit` | Arahan Pak Widi; CLAUDE.md langkah 10 | Tiga mixin Core dipakai (`approval`, `evidence`, `criteria`) + satu mixin modul (`labfik.praktikum.pengajuan.mixin`) |
| Urutan baku ditulis sebagai **Template Method** dengan **hook**; turunan tidak meng-*override* method utama | CLAUDE.md bagian 8 | `action_putuskan()` (pengajuan), `action_kirim()` (jurnal), `action_sahkan()` (jadwal, milik Core) |
| Model bawaan atau milik addon lain diperluas dengan `_inherit` tanpa `_name` baru, bukan disalin | Keputusan 14 Nov 2026; kontrak Core | `labfik.sesi` (Core), `survey.survey`, `survey.question`, `res.config.settings`, `labfik.jabatan.wewenang` (`selection_add`) |
| Notasi DCD proyek | CLAUDE.md bagian 5 | Jenis kelas hanya lewat stereotype: «AbstractModel» (nama miring) = mixin, «Odoo», «Core»/«SDM»; model baru milik modul tanpa stereotype; perluasan `_inherit` = segitiga kosong berlabel «_inherit»; `+`/`#`, «override», {abstract}, {hook}. Halaman rincian hanya menulis `{inherit: …}` di header, tanpa menggambar ulang mixin Core (sama dengan DCD Tata Kelola) |
| Sweet spot | CLAUDE.md bagian 1 | Struktur dipilih yang paling sederhana selama AB dan kriteria tetap terjaga (bagian 3.2) |

---

## 2. Daftar model

### 2.1 Di addon `labfik_core` (dirancang Praktikum, kontrak C-7–C-9)

| Model | Label | Asal di CM | Isi |
|---|---|---|---|
| `labfik.mata.kuliah` | [M] | MataKuliah | `kode` «unique», `name`, `prodi`, `semester`, `active`; `unlink()` «override» (AB-PRK-31) |
| `labfik.kelas` | [M] | Kelas | `mata_kuliah_id`, `periode_id`, `name`, `jumlah_mahasiswa`, `dosen_koordinator_id`, `dosen_ids`, `active`; unik (MK, periode, nama) |
| `labfik.sesi` | [T] | Sesi | Field tersimpan sesuai kontrak C-9 (`jam_mulai`/`jam_selesai` dari `Interval<Jam>`), `is_diganti` {compute}; `_cek_jam()`, `_cek_pertemuan_unik()` |

### 2.2 Addon `labfik_praktikum` (`depends: ['labfik_core', 'labfik_sdm', 'survey']`)

| Model | `_inherit` | Label | Asal di CM | DCD |
|---|---|---|---|---|
| `labfik.sesi` (perluasan) | `labfik.sesi` | [T] | turunan Sesi | DCD-1 |
| `labfik.praktikum.jadwal` | approval | [T] | PenetapanJadwal | DCD-1 |
| `labfik.praktikum.impor.jadwal` (+ `.baris`) | TransientModel | wizard | — (hasil desain) | DCD-1 |
| `labfik.praktikum.pengajuan.mixin` | AbstractModel, mail.thread | — | Pengajuan + KeputusanPengajuan + Penarikan | DCD-2 |
| `labfik.praktikum.pemakaian` | pengajuan | [T] | PemakaianLab | DCD-2 |
| `labfik.praktikum.perubahan` | pengajuan | [T] | PerubahanSesi + UsulanPengganti | DCD-2 |
| `labfik.praktikum.modul` | mail.thread | [T] | VersiModul | DCD-3 |
| `labfik.praktikum.modul.software`, `.modul.bahan` | — | [T] | KebutuhanSoftware, KebutuhanBahan | DCD-3 |
| `labfik.praktikum.kesiapan` | evidence | [T] | PemeriksaanKesiapan; Sesi `/alat_tidak_tersedia` dipindah ke sini sebagai `alat_tidak_tersedia_ids` {compute} karena hanya dipakai formulir pemeriksaan (O) | DCD-3 |
| `labfik.praktikum.kesiapan.butir` | — | [T] | ButirPemeriksaan + 4 turunan + SubstitusiBahan + PersetujuanSubstitusi | DCD-3 |
| `labfik.praktikum.jurnal` | evidence | [T] | JurnalSesi + PengirimanJurnal | DCD-4 |
| `labfik.praktikum.jurnal.petugas`, `.jurnal.logbook` | — | [T] | PresensiPetugas, EntriLogBook | DCD-4 |
| `labfik.praktikum.penilaian` (+ `.baris`) | evidence | [T] | PenilaianKelas, BarisNilai (O); BerkasNilai → `berkas_nilai_ids` | DCD-4 |
| `res.config.settings` (perluasan) | `res.config.settings` | — | PengaturanPraktikum | DCD-4 |
| `survey.survey` (perluasan) | `survey.survey`, criteria | [T] | Survei + PenetapanSurvei | DCD-5 |
| `survey.question` (perluasan) | `survey.question` | [T] | ButirSurvei | DCD-5 |
| `survey.user_input`, `.line` | bawaan, tidak diperluas | [T] | Respons, Jawaban | DCD-5 |
| `labfik.praktikum.evaluasi.survei` | evidence | [T] | EvaluasiSurvei | DCD-5 |
| `labfik.praktikum.evaluasi.kesimpulan`, `.evaluasi.rtl` | — | [T] | KesimpulanAspek, RencanaTindakLanjut + PenilaianEfektivitas | DCD-5 |
| `labfik.praktikum.monev` | AbstractModel (layanan) | [R] | — (status monev hanya hasil hitung) | DCD-5 |

Nama model mengikuti pola `labfik.praktikum.*` (kontrak Core bagian 5) dan nama yang sudah dipakai di kebutuhan dan brief. Tidak ada yang bentrok dengan nama Tata Kelola (CLAUDE.md bagian 6).

**Perluasan Core lewat data** (tidak mengubah Core): `labfik.jabatan.wewenang.jenis_dokumen` `selection_add` {`jadwal_praktikum`, `pemakaian_lab`, `perubahan_sesi`, `survei_kepuasan`} (I-4); data wewenang (Kepala Laboratorium, `mengesahkan`, empat jenis itu) **[KONFIRMASI KaLab]**; grup `labfik_dosen`, `labfik_asisten` (I-5).

---

## 3. Dari conceptual model ke desain (§13.6)

### 3.1 Perubahan struktur

| Perubahan | CM | DCD | Alasan |
|---|---|---|---|
| Generalisasi menjadi *mixin* | Pengajuan (abstrak), RekamanBukti, DokumenDisahkan | `labfik.praktikum.pengajuan.mixin`; `evidence.mixin`, `approval.mixin` (Core) | Odoo mewujudkan generalisasi lintas tabel dengan `AbstractModel` + `_inherit` |
| Kejadian 0..1 menjadi field di model induk | KeputusanPengajuan, Penarikan, PengirimanJurnal, SubstitusiBahan, PersetujuanSubstitusi, PenetapanSurvei, PenilaianEfektivitas | `pemutus_id`, `tanggal_putus`, `alasan_tolak`, `karena_bentrok`, `tanggal_tarik`; `waktu_kirim`, `pengirim_id`; `alasan_substitusi`, `penyetuju_id`, `waktu_setuju`; `penetap_id`, `tanggal_tetap`; `efektif`, `penilai_id`, `tanggal_nilai` | Setiap kejadian paling banyak satu kali per rekaman, jadi tabel log terpisah tidak memberi manfaat (berbeda dengan `approval.log` yang menyimpan banyak kejadian). Field kejadian `readonly` dan hanya ditulis oleh method `action_*`; riwayat perubahan dicatat `mail.thread` |
| Status turunan disimpan | `/status` Pengajuan, Jurnal, Survei | `state` (pengajuan, jurnal), `status_lab` {compute, store} (survei) | Dipakai untuk filter, *record rule*, dan tampilan daftar. Nilainya tetap hanya diubah oleh method `action_*` (atau `compute` untuk survei), sehingga satu sumber kebenaran tetap terjaga |
| Generalisasi butir menjadi satu model | ButirPemeriksaan + ButirUtilitas, StasiunKerja, Software, Bahan | `labfik.praktikum.kesiapan.butir` dengan `kategori` + `_cek_isian_kategori()` | Subkelas Odoo (`_inherits`) membuat lima tabel untuk satu daftar butir di satu formulir. Satu tabel dengan kategori lebih sederhana dibangun dan dipahami; aturan "atribut per jenis" yang dijaga generalisasi CM dipindah ke `@api.constrains` dan tampilan per kategori (sweet spot) |
| Generalisasi jawaban memakai bawaan | Jawaban → JawabanSkala, JawabanTerbuka | `survey.user_input.line` bawaan | Addon `survey` sudah menyimpan jawaban numerik dan teks; tidak perlu model baru |
| Bagian 0..1 dilebur | UsulanPengganti | `usulan_tanggal`, `usulan_jam_mulai`, `usulan_jam_selesai`, `usulan_ruang_id` di Perubahan | Hanya tiga field; `_cek_usulan()` menjaga "wajib bila pindah" (AB-PRK-12) |
| Asosiasi turunan menjadi field tersimpan | `/sesi_asal` | `labfik.sesi.sesi_asal_id` (Core) | Core tidak bisa membaca Perubahan Sesi di `labfik_praktikum`; kontrak C-9 sudah memuat field ini |
| Asosiasi turunan menjadi method | `/versi_berlaku [periode]`, `/petugas_ditugaskan`, `/survei_berikutnya` | `labfik.praktikum.modul.get_berlaku(mata_kuliah, tanggal)`, `labfik.sesi.get_petugas_ditugaskan()`, `survey.survey.get_survei_berikutnya()` | Bergantung parameter (tanggal) atau melintasi addon; *query* lebih jelas daripada field `compute` |
| Atribut turunan menjadi `compute` | `/is_*`, `/tepat_waktu`, `/terlambat`, `/durasi_memenuhi`, `/berbukti`, `/lengkap`, `/response_rate`, `/rerata*`, `/kriteria_tertinggi` | `compute` (+ `store` atau `search` bila dipakai filter: `is_terpublikasi`, `is_terlewat`, `tepat_waktu`, `terlambat`, `berbukti`, `status_lab`) | — |
| Field hitung Sesi dipindah ke perluasan | `/is_terpublikasi`, `/is_ditunda`, `/is_terlewat`, `/berasisten`, `/melebihi_kapasitas`, `/memenuhi_*` | `labfik.sesi` `_inherit` di `labfik_praktikum` | Datanya ada di Penetapan Jadwal, Perubahan, Jurnal (Praktikum) dan penugasan (SDM). Core hanya `depends: ['hr', 'mail']` (kontrak bagian 1). Hanya `is_diganti` yang di Core |
| Interval menjadi dua field | `Interval<Jam>`, `Interval<Date>` | `jam_mulai`/`jam_selesai` (Float, *widget* jam), `tanggal_buka`/`tanggal_tutup` | Odoo tidak punya tipe interval; aturan `awal < akhir` di `@api.constrains`, cek beririsan di satu method `cek_bentrok`/`cari_bentrok` |
| Riwayat berkas | BerkasNilai `{ordered}` | `berkas_nilai_ids: ir.attachment [*]` | Lampiran bawaan sudah punya `create_date` untuk urutan |
| Singleton menjadi pengaturan | PengaturanPraktikum | `res.config.settings` + `ir.config_parameter` (`prk_*`) | Cara baku Odoo untuk satu set nilai pengaturan |
| Model hasil desain | — | `labfik.praktikum.impor.jadwal` (+ `.baris`) TransientModel; `labfik.praktikum.monev` AbstractModel | Impor dan pratinjau butuh tempat sementara (*wizard*); status monev butuh layanan tanpa tabel (sama dengan `labfik.org.monev` Tata Kelola) |
| Rujukan Personel menjadi atribut bertipe | peran pengaju, pemutus, penyetuju, pengirim, petugas, penetap, pic, penilai, penerbit | `hr.employee` | Model bawaan Odoo boleh ditulis sebagai atribut bertipe (CLAUDE.md bagian 5) |
| Enumerasi menjadi `Selection` | Semua «enumeration» | `fields.Selection` | — |

### 3.2 Pilihan yang ditimbang (sweet spot)

| Pilihan | Diambil | Tidak diambil, karena |
|---|---|---|
| Pengajuan memakai `approval.mixin` Core | Mixin pengajuan sendiri | `approval.mixin` mensyaratkan draf, berkas bertanda tangan, dan riwayat pengesahan; S2 hanya diajukan → diputuskan. Memaksakan `approval.mixin` menambah langkah yang tidak dibutuhkan kriteria mana pun |
| Butir sebagai empat model | Satu model berkategori | Lihat bagian 3.1 |
| Log kejadian generik untuk pengajuan, jurnal, survei | Field + `mail.thread` | Kejadian tidak berulang |
| Model rekaman konflik | Laporan dari `karena_bentrok` dan perubahan | Tidak ada kriteria yang gagal tanpanya; `karena_bentrok` cukup (KF-PRK-09, 11) |
| Penjadwal (`ir.cron`) untuk terlewat, terlambat, status buka | `compute` dengan `search` | Prinsip "hitung, bukan jadwalkan" (CLAUDE.md bagian 1) |
| Model survei sendiri | Perluas `survey` | Addon LGPL-3 sudah menyediakan formulir publik, token anonim, dan rekap jawaban |

---

## 4. Template Method dan hook

### 4.1 `labfik.praktikum.pengajuan.mixin.action_putuskan(hasil, alasan, karena_bentrok, pengganti=None)`

1. `state` harus `diajukan`.
2. `_cek_wewenang(pemutus)` → `pemutus.job_id.punya_wewenang('mengesahkan', self._jenis_pengajuan())` (AB-PRK-10). Pemutus = `hr.employee` pengguna.
3. Bila `hasil = ditolak`: `alasan` wajib (AB-PRK-10); tulis `state`, `pemutus_id`, `tanggal_putus`, `alasan_tolak`, `karena_bentrok`; ke langkah 7.
4. `_sebelum_disetujui(pengganti)` {hook}: cek bentrok (AB-PRK-01) dan, untuk perubahan, Sesi masih `terjadwal` (AB-PRK-12).
5. Tulis `state = disetujui`, `pemutus_id`, `tanggal_putus`.
6. `_efek_disetujui(pengganti)` {hook}.
7. `_beri_tahu()` (O, KF-PRK-49).

| Model | `_jenis_pengajuan()` | `_sebelum_disetujui()` | `_efek_disetujui()` |
|---|---|---|---|
| `labfik.praktikum.pemakaian` | `pemakaian_lab` | `labfik.sesi.cari_bentrok(ruang, tanggal, jam, kecuali=self)` kosong | — (masuk jadwal terpadu lewat `state`) |
| `labfik.praktikum.perubahan` | `perubahan_sesi` | `sesi_id.state == 'terjadwal'`; untuk pindah: `cari_bentrok(pengganti, kecuali=sesi_id)` kosong | pindah → `sesi_id._ganti(tanggal, jam, ruang)` membuat Sesi pengganti (`sesi_asal_id`), Sesi asal `batal`, isi `sesi_pengganti_id`; daring → `moda = daring`; batal → `state = batal` |

### 4.2 `labfik.praktikum.jurnal.action_kirim()`

1. `_cek_sesi()`: Sesi `terjadwal`, `is_terpublikasi`, `tanggal ≤ hari ini`, belum ada jurnal terkirim (AB-PRK-17).
2. `get_kekurangan()` kosong: presensi dosen dan laboran, asisten bila `sesi_id.berasisten`, `jumlah_hadir`, `modul_id`, ≥ 1 log book (AB-PRK-19).
3. Tulis `state = terkirim`, `waktu_kirim`, `pengirim_id`.
4. `sesi_id._tandai_terlaksana()`: satu-satunya jalan `state` Sesi menjadi `terlaksana` (aturan pakai Sesi: hanya Praktikum yang mengubah `state`).

### 4.3 Hook Core yang diisi

| Model | Hook / abstract | Isi |
|---|---|---|
| `labfik.praktikum.jadwal` (approval) | `_jenis_dokumen()` | `jadwal_praktikum` |
| | `_cek_kelengkapan()` | setiap Kelas periode itu punya Sesi (AB-PRK-05) |
| | `_dokumen_diganti()` | tidak diisi (satu aktif per periode, `_cek_satu_aktif_per_periode()`; jadwal yang dicabut disusun ulang sebagai rekaman baru) |
| | `_setelah_disahkan()` | **tidak diisi**: `is_terpublikasi` Sesi dihitung dari `state` jadwal |
| `kesiapan`, `jurnal`, `penilaian`, `evaluasi.survei` (evidence) | `_boleh_dikoreksi()` | kesiapan dan penilaian selalu boleh; jurnal hanya bila belum terkirim atau oleh grup laboran/KaLab **[USULAN PENULIS; menunggu P11]** |
| `survey.survey` (criteria) | `_cek_k1()`–`_cek_k4()` | K1 `penetap_id` + `tanggal_tetap < tanggal_buka`; K2 `get_kekurangan_penetapan()` kosong; K3 ada respons, `response_rate`, evaluasi tercatat; K4 setiap RTL punya `efektif` (AB-PRK-34) |

---

## 5. Pemetaan operasi SSD → method

### 5.1 Jadwal dan Sesi

| Operasi SSD | Method / ORM |
|---|---|
| `pratinjau_impor` | `labfik.praktikum.impor.jadwal.action_pratinjau()`: `_baca_berkas()` → baris; isi `status`/`pesan` per baris (bentrok `cari_bentrok`, `_cek_terkunci(periode, kelas)`, baris salah, kapasitas). Tidak membuat Sesi |
| `impor_jadwal` | `action_impor()` → `_bangkitkan_sesi(kelas, baris)` untuk baris `siap` (AB-PRK-01–04) |
| `ringkasan_jadwal` | `labfik.praktikum.jadwal.get_ringkasan()` / `impor.jadwal.ringkasan` {compute} |
| `cek_bentrok` | `@model labfik.sesi.cari_bentrok(ruang, tanggal, jam_mulai, jam_selesai, kecuali)` (memeriksa Sesi `terjadwal` bermoda `luring` dan pemakaian `disetujui`) |
| `daftar_sesi(filter)` | `labfik.sesi.search_read()` dengan domain per filter (`is_terpublikasi`, `tanggal`, `jurnal`, `kelas_id.dosen_ids`/penugasan) |
| `status_sesi` | `read(['state', 'is_terpublikasi', 'is_ditunda', 'is_diganti', …])` |
| `buat_penetapan_jadwal` | `labfik.praktikum.jadwal.create()` (`_cek_satu_aktif_per_periode()`); pengajuan dan pengesahan memakai `action_ajukan()`, `action_terbitkan()`, `action_unggah_ttd()`, `action_kembalikan()`, `action_sahkan()`, `action_cabut()` (Core) |
| `rincian_penetapan_jadwal` | `search_read([('periode_id', '=', …)])` |
| `laporan_jadwal` | QWeb report dari `labfik.sesi` + `labfik.praktikum.pemakaian` (`state = disetujui`; ditolak `karena_bentrok` + Sesi `is_diganti` sebagai rekaman konflik) |

### 5.2 Versi Modul

| Operasi SSD | Method / ORM |
|---|---|
| `info_modul` | `search_read()` per (MK, periode) + `_cek_pengampu(employee)` |
| `terbitkan_versi_modul` | `create()` lalu `action_terbitkan()`: `_cek_pengampu` (AB-PRK-09), `_cek_isi` (AB-PRK-08), versi `berlaku` lama → `diganti` (AB-PRK-07) |
| `daftar_modul_berlaku` | `search_read([('state', '=', 'berlaku'), …])` + *record rule* dosen/asisten |
| `modul_berlaku` | `@model get_berlaku(mata_kuliah, tanggal)` |

### 5.3 Pengajuan

| Operasi SSD | Method / ORM |
|---|---|
| `ajukan_pemakaian` | `labfik.praktikum.pemakaian.create()` (`_cek_jam_bentrok()`) |
| `ajukan_perubahan` | `labfik.praktikum.perubahan.create()` (`_cek_usulan()`) |
| `daftar_pengajuan(filter)` | `search_read()` pada kedua model menurut filter |
| `rincian_pengajuan` | `read()` |
| `putuskan_pengajuan` | `action_putuskan(hasil, alasan, karena_bentrok, pengganti)` (bagian 4.1) |
| `tarik_pengajuan` (O) | `action_tarik()` |

### 5.4 Kesiapan

| Operasi SSD | Method / ORM |
|---|---|
| `form_kesiapan` | `@model labfik.praktikum.kesiapan.get_form(sesi)`; bagian Alat (O, KF-PRK-52) dari `_compute_ketersediaan_alat()` → `alat_tidak_tersedia_ids`, `jumlah_pc_tersedia`; `workstation_count` dibaca dari `labfik.ruang` |
| `keputusan_tersedia` | `@model get_keputusan_tersedia(hasil_butir)` |
| `catat_pemeriksaan` | `@model catat(sesi, hasil_butir, keputusan)` → `create()` dengan `butir_ids`; `_cek_keputusan()` |
| `rincian_pemeriksaan` | `search_read([('sesi_id', '=', …)])` |
| `daftar_substitusi` | `labfik.praktikum.kesiapan.butir.search_read([('status_substitusi', '=', 'menunggu'), ('kesiapan_id.sesi_id.kelas_id.dosen_ids.user_id', '=', uid)])` |
| `setujui_substitusi` | `action_setujui_substitusi()` |

### 5.5 Pelaksanaan Sesi

| Operasi SSD | Method / ORM |
|---|---|
| `konteks_jurnal` | `@model labfik.praktikum.jurnal.get_konteks(sesi)` → `sesi.get_modul_berlaku()`, `sesi.get_petugas_ditugaskan()` |
| `simpan_jurnal` | `create()` / `write()` saat `state = draf` |
| `rincian_jurnal` | `search_read([('sesi_id', '=', …)])` |
| `cek_kelengkapan_jurnal` | `get_kekurangan()` |
| `kirim_jurnal` | `action_kirim()` (bagian 4.2) |
| `laporan_pelaksanaan` (O) | QWeb report dari kesiapan dan jurnal |

### 5.6 Penilaian Individual

| Operasi SSD | Method / ORM |
|---|---|
| `catat_penilaian_kelas` | `labfik.praktikum.penilaian.create()` / `write()` |
| `rincian_penilaian_kelas` | `search_read([('kelas_id', '=', …)])` |
| `impor_nilai` (O) | `action_impor_nilai(berkas)`: hapus `baris_ids` lama, buat baris baru, simpan berkas di `berkas_nilai_ids` (AB-PRK-24) |
| `status_praktikan` (O) | `get_status_praktikan()` |

### 5.7 Kepuasan Pengguna

| Operasi SSD | Method / ORM |
|---|---|
| `buat_survei` | `survey.survey.create()` |
| `simpan_butir_survei` | `write({'question_ids': [...]})` |
| `rincian_survei` | `read()` |
| `cek_kelengkapan_survei` | `get_kekurangan_penetapan()` |
| `tetapkan_survei` | `action_tetapkan()` |
| `batalkan_penetapan_survei` (O) | `action_batalkan_penetapan()` |
| `formulir_survei`, `kirim_respons` | Controller publik bawaan addon `survey` (token); `_create_answer()` «override» menolak di luar `tanggal_buka`–`tanggal_tutup` |
| `daftar_survei(filter)` | `search_read()` dengan domain `status_lab` / `status_buka` |
| `rekap_survei` | `get_rekap()` |
| `catat_evaluasi_survei` | `labfik.praktikum.evaluasi.survei.create()` dengan `kesimpulan_ids`, `rtl_ids` |
| `status_survei` | `read(['status_lab'])` + `get_kriteria(tanggal_acuan)` |
| `banding_rtl` | `read(['rerata_sebelum', 'rerata_sesudah'])` pada `rtl_ids` |
| `nilai_efektivitas` | `labfik.praktikum.evaluasi.survei.action_nilai_efektivitas(nilai)` |
| `laporan_survei` | QWeb report dari survei, evaluasi, RTL |

### 5.8 Status monev, bersama, CRUDL

| Operasi SSD | Method / ORM |
|---|---|
| `status_monev` | `@model labfik.praktikum.monev.get_status(periode, tanggal_acuan)` → `_persentase(pkg)` memanggil `labfik.sesi.get_cek_monev(pkg)` per Sesi; `_status_pkg19()` membaca `penilaian.berbukti` dan `baris.lengkap`; PKG-20 `survey.get_kriteria()` |
| `terbitkan_laporan_bukti` | `@model terbitkan_laporan_bukti(periode, tanggal_acuan)` → QWeb report |
| `koreksi_rekaman` | `evidence.mixin.action_koreksi(nilai, alasan)` |
| `buat_/ubah_/rincian_/daftar_<konsep>` (Mata Kuliah, Kelas) | `create()`, `write()`, `read()`, `search_read()` |
| `hapus_<konsep>` | `unlink()` «override» (AB-PRK-31) |
| `arsipkan_<konsep>` | `action_archive()` (`active`) |
| `rincian_pengaturan`, `ubah_pengaturan` | `res.config.settings` (`get_values()`/`set_values()` bawaan) |

Semua 21 command, 32 query khusus, 6 operasi pola «CRUDL», dan 2 operasi pengaturan terpetakan. Penyimpangan CQS `create()` Odoo diterima, sama dengan Tata Kelola (SSD bagian 5).

---

## 6. Pemetaan aturan bisnis → mekanisme Odoo

| AB | Mekanisme | Tempat |
|---|---|---|
| AB-PRK-01 | `cari_bentrok()` (Sesi `terjadwal` bermoda `luring` + pemakaian `disetujui`) dipanggil `action_pratinjau()`, `_cek_jam_bentrok()` @constrains, dan *hook* `_sebelum_disetujui()` | `labfik.sesi` (perluasan), impor, pemakaian, perubahan |
| AB-PRK-02 | `_cek_pertemuan_unik()` @constrains (Sesi tanpa `sesi_asal_id`); `_bangkitkan_sesi()` memberi jenis UTS/UAS pada pertemuan 8 dan 16 | `labfik.sesi` (Core), impor |
| AB-PRK-03 | `melebihi_kapasitas` {compute}; status baris impor | `labfik.sesi` (perluasan), impor |
| AB-PRK-04 | `_cek_terkunci(periode, kelas)`: terkunci bila periode punya jadwal `diajukan`/`disahkan` atau Sesi kelas sudah berjurnal; `unlink()` «override» Sesi | impor, `labfik.sesi` (perluasan) |
| AB-PRK-05 | `_cek_kelengkapan()` + `_cek_satu_aktif_per_periode()` @constrains (paling banyak satu jadwal berstatus `draf`/`diajukan`/`disahkan` per periode); wewenang lewat `approval.mixin` | `labfik.praktikum.jadwal` |
| AB-PRK-06 | `is_terpublikasi` {compute, search}; `tanggal_publikasi` {related} | `labfik.sesi` (perluasan), jadwal |
| AB-PRK-07 | `action_terbitkan()` mengganti versi `berlaku` lama | `labfik.praktikum.modul` |
| AB-PRK-08 | `_cek_isi()` @constrains + `_sql_constraints` unique(MK, periode, nomor_versi) | `labfik.praktikum.modul` |
| AB-PRK-09 | `_cek_pengampu()` di `action_terbitkan()` + *record rule* grup dosen | `labfik.praktikum.modul` |
| AB-PRK-10 | `_cek_wewenang()` + alasan wajib di `action_putuskan()` | pengajuan mixin |
| AB-PRK-11 (O) | `action_tarik()`: pengaju (atau laboran pencatat), hanya saat `diajukan` | pengajuan mixin |
| AB-PRK-12 | `_cek_usulan()` @constrains; `_sebelum_disetujui()`; `_efek_disetujui()` | `labfik.praktikum.perubahan` |
| AB-PRK-13 | `_sql_constraints` unique(sesi_id); `_cek_sesi()` @constrains (Sesi `terjadwal` dan `is_terpublikasi`; ditambahkan saat audit 16 Nov 2026); `tepat_waktu` {compute, store} | `labfik.praktikum.kesiapan` |
| AB-PRK-14 | `get_form()` dari `sesi.get_modul_berlaku()`; `_cek_isian_kategori()` (lisensi software berbayar); bagian Alat (O): `_compute_ketersediaan_alat()` hanya memanggil `labfik.alat.check_ketersediaan_sesi()` dan tidak menulis ke `labfik.alat` (I-13) | kesiapan, butir |
| AB-PRK-15 | `_cek_keputusan()` @constrains; `get_keputusan_tersedia()` | `labfik.praktikum.kesiapan` |
| AB-PRK-16 | `_cek_substitusi()` @constrains; `action_setujui_substitusi()` hanya dosen kelas; `_cek_keputusan()` | butir, kesiapan |
| AB-PRK-17 | `_sql_constraints` unique(sesi_id); `_cek_sesi()` | `labfik.praktikum.jurnal` |
| AB-PRK-18 | `_cek_jam()` @constrains | `labfik.praktikum.jurnal`, `labfik.sesi` |
| AB-PRK-19 | `get_kekurangan()` di `action_kirim()` | `labfik.praktikum.jurnal` |
| AB-PRK-20 (O) | `sesuai_penugasan` {compute} dari `sesi.get_petugas_ditugaskan()` | `labfik.praktikum.jurnal.petugas` |
| AB-PRK-21 (O) | `terlambat` {compute, store} dari `prk_batas_hari_jurnal` | `labfik.praktikum.jurnal` |
| AB-PRK-22 | `durasi_memenuhi` {compute}; `get_cek_monev('18')` (moda, `prk_sesi_daring_sah`, pengganti sebelum tanggal selesai periode) | jurnal, `labfik.sesi` (perluasan) |
| AB-PRK-23 | `_sql_constraints` unique(kelas_id); `tautan_leads` `required` | `labfik.praktikum.penilaian` |
| AB-PRK-24 (O) | `action_impor_nilai()`; `_sql_constraints` unique(penilaian_id, nim); templat impor tanpa kolom nama | penilaian, baris |
| AB-PRK-25 (O) | `lengkap` {compute} dengan `prk_batas_lulus` | `labfik.praktikum.penilaian.baris` |
| AB-PRK-26 | `action_tetapkan()` → `get_kekurangan_penetapan()` + `penetap.job_id.punya_wewenang('mengesahkan', 'survei_kepuasan')` | `survey.survey` |
| AB-PRK-27 (O) | `action_batalkan_penetapan()`: hanya sebelum `tanggal_buka` | `survey.survey` |
| AB-PRK-28 | `access_mode = 'public'`, tanpa `partner_id`; `_create_answer()` «override» cek masa buka | `survey.survey` |
| AB-PRK-29 | `_cek_setelah_tutup()` @constrains + unique(survey_id); `_cek_baris_lengkap()` RTL | evaluasi survei, RTL |
| AB-PRK-30 | `action_nilai_efektivitas()`: survei berikutnya `status_lab ≥ dievaluasi`; `rerata_sebelum`/`rerata_sesudah` {compute} | evaluasi survei, RTL |
| AB-PRK-31 | `evidence.mixin.unlink()` (ditolak) + `action_koreksi()`; `unlink()` «override» master (dirujuk Sesi) | Core mixin, MK, Kelas |
| AB-PRK-32 | `labfik.sesi.get_cek_monev(pkg)` + `monev._persentase()` | perluasan Sesi, monev |
| AB-PRK-33 | `penilaian.berbukti` {compute, store} + `monev._status_pkg19()` | penilaian, monev |
| AB-PRK-34 | `criteria.mixin.get_kriteria()` + `_cek_k1()`–`_cek_k4()` | `survey.survey` |

Semua 34 AB terpetakan. Aturan pengesahan jadwal AB-01–09 milik Tata Kelola dijalankan `approval.mixin`.

---

## 7. Grup akses dan *record rule*

| Grup | Tempat | Mewarisi | Hak utama di modul ini |
|---|---|---|---|
| `labfik_pengguna` | Core | `base.group_user` | Membaca jadwal terpadu dan modul berlaku |
| `labfik_dosen` | `labfik_praktikum` | `labfik_pengguna` | Menerbitkan modul MK yang diampu; menyetujui substitusi kelasnya; mengisi jurnal dan penilaian kelasnya; mengajukan perubahan sesi |
| `labfik_asisten` | `labfik_praktikum` | `labfik_pengguna` | Mengisi jurnal kelas yang diasistensi; mengajukan perubahan sesi |
| `labfik_laboran` | Core | `labfik_pengguna` | Impor jadwal, Mata Kuliah, Kelas, penetapan jadwal (draf), pemakaian lab, pemeriksaan kesiapan, jurnal, penilaian |
| `labfik_kalab` | Core | `labfik_laboran` | Memutuskan pengajuan, mengesahkan jadwal, survei dan evaluasi, pengaturan, status monev |
| Admin | `base.group_system` (bawaan) | — | Pengaturan teknis. Aktor "Admin" (kebutuhan bagian 1) tidak butuh grup `labfik_admin` baru |

*Record rule* (KNF-PRK-02): dosen → modul dengan `mata_kuliah_id` pada kelas yang diampu; dosen dan asisten → jurnal Sesi kelasnya (dosen lewat `kelas_id.dosen_ids`, asisten lewat penugasan SDM yang berlaku). Hak **memutuskan/mengesahkan** tetap dicek lewat `labfik.jabatan.wewenang`, bukan grup.

---

## 8. Perubahan dibanding versi sebelumnya

Belum ada DCD sebelumnya untuk modul ini. Perubahan pada langkah sebelumnya yang ditemukan saat menyusun DCD:

| Dokumen | Perubahan | Alasan |
|---|---|---|
| [conceptual-model-praktikum.md](conceptual-model-praktikum.md) + diagram | + `KeputusanPengajuan.karena_bentrok`, + `ButirBahan.tanggal_kedaluwarsa` | KF-PRK-09 dan KF-PRK-19 (lapis Inti) belum tertangkap di CM versi pertama (temuan 5.2 no. 8 di dokumen CM) |
| [ssd-praktikum.md](ssd-praktikum.md) + SSD-4 | `putuskan_pengajuan(…, karena_bentrok, …)`; `dto_rincian_pengajuan` + `karena_bentrok`; `dto_hasil_butir` + `tanggal_kedaluwarsa` | Sama. Nama dan jumlah operasi tidak berubah |

**Revisi audit lintas-branch, 16 Nov 2026** ([audit-praktikum.md](audit-praktikum.md)):

| Bagian | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| `labfik.praktikum.jadwal` (DCD-1) | `_cek_satu_per_periode()` | `_cek_satu_aktif_per_periode()`: jadwal `dicabut` tidak dihitung | Jalan buntu: setelah jadwal dicabut (KF-PRK-45) jadwal baru tidak bisa disusun (AB-PRK-05) |
| Impor jadwal (DCD-1) | `_cek_terkunci(kelas)`: kelas yang sudah punya Sesi saat jadwal disahkan | `_cek_terkunci(periode, kelas)`: seluruh periode terkunci selama jadwal `diajukan`/`disahkan` | Kelas baru yang diimpor setelah pengesahan akan terbaca terpublikasi tanpa ada di jadwal bertanda tangan (PKG-15 C1, AB-PRK-04) |
| `labfik.sesi.cari_bentrok()` (DCD-1) | Semua Sesi `terjadwal` | Hanya Sesi `terjadwal` bermoda `luring` | Sesi daring tidak memakai ruang (AB-PRK-01) |
| `labfik.praktikum.kesiapan` (DCD-3) | Tanpa cek Sesi | + `_cek_sesi()` @constrains | Bagian "untuk Sesi yang terpublikasi" di AB-PRK-13 belum punya mekanisme |
| `labfik.praktikum.kesiapan` (DCD-3), pengecekan ulang alat dan bahan Core | `labfik.alat` tidak dipakai | + `alat_tidak_tersedia_ids` Many2many `labfik.alat` {compute}, `jumlah_pc_tersedia` Integer {compute}, `_compute_ketersediaan_alat()` (O); stub «Core» `labfik.alat` | Aturan pakai domain aset di kontrak Core (Praktikum mengecek PC/alat lewat `labfik.alat`); KF-PRK-52. Hanya membaca, tanpa tabel baru dan tanpa dependensi ke addon Aset |
| Bagian 5.1 | Operasi Tata Kelola tanpa kembalikan dan cabut | + `action_kembalikan()`, `action_cabut()` | Pencabutan jadwal dipakai KF-PRK-45 |
| Isu 10 no. 6 | Rekomendasi SDM memakai `is_terpublikasi` (lewat CM) | SDM cukup `state` Core | `is_terpublikasi` ada di `labfik_praktikum`, tidak terbaca SDM (I-7) |

---

## 9. Cek silang akhir

| Pemeriksaan | Hasil |
|---|---|
| Setiap konsep CM punya model atau field | Ya (bagian 2.2 kolom "Asal di CM"; bagian 3.1 untuk konsep yang dilebur) |
| Setiap operasi SSD punya method atau ORM | Ya (bagian 5) |
| Setiap AB punya mekanisme | Ya, 34 dari 34 (bagian 6) |
| Status sama dengan state machine | Sesi {terjadwal, terlaksana, batal} (S1, I-1); pengajuan {diajukan, disetujui, ditolak, ditarik} (S2); survei {draf, ditetapkan, dievaluasi, siklus_selesai} (S3); versi modul {draf, berlaku, diganti}; jurnal {draf, terkirim} |
| Field warisan tidak ditulis ulang | Ya; field `evidence`/`approval`/`criteria` hanya disebut sebagai catatan miring (mis. `pelapor_id (warisan) = pemeriksa`) |
| Kontrak Core | Field Sesi Core tidak ditambah dari modul lain; perluasan oleh pemilik (Praktikum). Wewenang hanya `selection_add` `jenis_dokumen`. `labfik.bahan` dipakai (C-13). `labfik.alat` (C-10) hanya dibaca lewat `check_ketersediaan_sesi()` (O, KF-PRK-52); `status` alat tidak ditulis (I-13) |
| Kriteria instrumen | PKG-15 C1–C4, 16 S1–S4, 17 B1–B3, 18 C1–C5 → `labfik.sesi.get_cek_monev(pkg)`; PKG-19 → `penilaian.berbukti`, `baris.lengkap`; PKG-20 K1–K4 → `survey._cek_k*()` |
| Data pribadi | Tidak ada nama orang, NIM, atau nomor HP di rancangan; baris nilai hanya NIM dari berkas impor saat dipakai (tidak di repo) |

---

## 10. Isu terbuka

- [ ] Field hitung Sesi ditambahkan `labfik_praktikum` lewat `_inherit`, bukan di Core; kontrak Core C-9 dan bagian 5 (*hook* `_setelah_disahkan()` untuk jadwal) perlu disesuaikan **[KONFIRMASI Febriyan]** (isu CM no. 2)
- [ ] Data wewenang: Kepala Laboratorium `mengesahkan` untuk `jadwal_praktikum`, `pemakaian_lab`, `perubahan_sesi`, `survei_kepuasan` **[KONFIRMASI KaLab]**
- [ ] `_boleh_dikoreksi()` jurnal terkirim: siapa yang boleh mengoreksi **[USULAN PENULIS; KONFIRMASI P11]**
- [ ] Nama field `survey.survey` bawaan Odoo 17 (`answer_done_count`, `access_mode`, `_create_answer`) perlu dicocokkan dengan kode sumber saat implementasi **[VALIDASI]**
- [ ] Rekaman konflik dari impor tidak tersimpan **[ASUMSI; KONFIRMASI pembimbing]**
- [ ] `kontrak-core-sdm.md` bagian 2.3 masih memakai 6 status Sesi. SDM cukup membaca `state` (Core); `is_terpublikasi` dan atribut hitung lain berada di `labfik_praktikum` dan tidak terbaca SDM **[KONFIRMASI Zahir]** (isu CM no. 7)
- [ ] Data wewenang Praktikum (Kepala Laboratorium, `mengesahkan`, empat `jenis_dokumen`) dan grup `labfik_dosen`/`labfik_asisten` sudah tercatat di kontrak Core bagian 4; kontrak Core bagian 5 masih menulis *hook* `_setelah_disahkan()` "menandai Sesi terpublikasi" **[KONFIRMASI Febriyan]**
