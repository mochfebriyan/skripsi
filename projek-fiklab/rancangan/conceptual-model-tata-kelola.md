# Conceptual Model Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 9 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Bahan kerja**, tidak masuk proposal. Dasar design class diagram (langkah 10).

Diagram: [conceptual-model-tata-kelola.drawio](conceptual-model-tata-kelola.drawio), 4 halaman (CM-1 s.d. CM-4). Dibuat dengan skrip [conceptual_model.py](../tools/drawio/contoh-tata-kelola/conceptual_model.py) dan lolos `validate.py` dengan prefiks `tk-`. **Tampilan visual belum dicek di draw.io.**

Sumber: kamus DTO dan katalog operasi di [ssd-tata-kelola.md](ssd-tata-kelola.md), aturan bisnis AB-01–25 di [expanded-use-case-tata-kelola.md](expanded-use-case-tata-kelola.md), state machine S1–S2 di [proses-bisnis-tata-kelola.md](proses-bisnis-tata-kelola.md).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Hanya konsep, atribut primitif, dan asosiasi. Tanpa method dan tanpa detail teknologi (Odoo) | §8.1 | Tidak ada `_inherit`, `Many2one`, atau `*_id` |
| Konsep tidak boleh menjadi tipe atribut, dan atribut tidak boleh menjadi kunci asing (`owner_id`) | §8.2, §10.4 | Semua rujukan antarkonsep ditulis sebagai asosiasi dengan nama peran (pengesah, pic, pelapor, …) |
| Atribut turunan ditulis `/nama` beserta definisinya; hanya bisa dibaca | §8.2.3 | `/tanggal_sah`, `/perlu_ditinjau`, `/memenuhi`, `/kriteria_tertinggi`, `/prioritas`, … |
| Enumerasi untuk nilai tetap | §8.2.4 | Status, jenis, kategori, aspek, tindakan |
| «unique» untuk nilai yang tidak boleh kembar | §8.3.1 | Kode Dokumen Induk, kode KPI, nomor SK, revisi per Dokumen Induk |
| Komposisi hanya untuk bagian–keseluruhan yang sungguhan; sisi keseluruhan bermultiplisitas 1 | §8.4.5 | Jabatan ◆ Tugas/Wewenang, SK ◆ BarisPenetapan, Dokumen Induk ◆ Versi, Rencana ◆ Item/TemuanGap, Tinjauan ◆ UkuranManfaat, Dokumen ◆ Riwayat |
| Asosiasi turunan untuk rujukan yang dihitung | §8.4.3 | `/pengesah_berwenang`, `/versi_berlaku` |
| Generalisasi hanya bila turunannya benar-benar "adalah" induknya dan berbagi atribut atau asosiasi | §9.2.1 | DokumenDisahkan dan RekamanBukti |
| Data yang baru muncul saat status berubah menjadi **konsep kejadian**, bukan atribut opsional (*modal class*, transisi monoton naik) | §9.3.2 | Pengesahan, KejadianPengesahan |
| Status yang hanya berupa nilai yang bisa dihitung = transisi stabil | §9.3.1 | Kemutakhiran versi (S2) sebagai atribut turunan |
| Konsep dan atribut dicari dari teks use case dan argumen operasi SSD | §10.2 | Bagian 4 (cek kamus DTO) |
| Pola Bab 11 bila cocok | §11 | Bagian 3 |

---

## 2. Isi diagram

### CM-1 · Dokumen yang disahkan, riwayat pengesahan, dan rekaman bukti

| Konsep | Jenis | Isi dan alasan |
|---|---|---|
| ***DokumenDisahkan*** | Abstrak | Induk Renstra, Rencana, SK Penetapan, dan Versi Dokumen. Semuanya mengikuti S1 dan memakai mekanisme pengesahan yang sama. Atribut: `status`, `/jenis_dokumen`, `/tanggal_ajukan`, `/tanggal_sah`, `/berkas_ttd`. Asosiasi: `penyusun` (Personel), `/pengesah_berwenang` (turunan, AB-05), `revisi_dari` (refleksif) |
| **Pengesahan** | Kejadian | Muncul saat dokumen disahkan: `tanggal_sah`, peran `pengesah` (pejabat penanda tangan) dan `pencatat` (KaLab). 0..1 per dokumen |
| **KejadianPengesahan** | Kejadian | Riwayat setiap transisi S1 (AB-09): `jenis`, `waktu`, `alasan`, `berkas`, peran `pelaku`. Bagian dari dokumen (komposisi, berurutan waktu) |
| ***RekamanBukti*** | Abstrak | Induk tujuh rekaman kegiatan: Rapat Koordinasi, Evaluasi Struktur, Distribusi, Sosialisasi, Tinjau Ulang, Realisasi, Tinjauan Rencana. Atribut bersama `tanggal`, `bukti`, `keterangan`, dan peran `pelapor`. Aturan bersama AB-22 (tidak dihapus, hanya dikoreksi) |

### CM-2 · Struktur organisasi (PKG-03)

| Konsep | Isi dan alasan |
|---|---|
| **Personel** | `nama`, `jenis`, `unit`. Asosiasi `jabatan` 0..1: jabatan yang dipakai untuk cek wewenang pengesah (AB-05) |
| **Jabatan** | `nama`, `unit`, `is_eksternal`, `syarat_kompetensi`, `/lengkap` (PKG-03 K2). Refleksif `atasan` dan `pengganti` |
| **Tugas**, **Wewenang** | Bagian dari Jabatan (komposisi). Wewenang = `tindakan` × `jenis_dokumen` (keputusan 14 November 2026) |
| **SK Penetapan** | Turunan DokumenDisahkan. `nomor_sk`, `judul`, `menimbang`, `mengingat`, `/kriteria_tertinggi`. Berlaku pada satu Periode |
| **BarisPenetapan** | Bagian dari SK: personel × jabatan × ruang, dengan tanggal mulai dan selesai |
| **Rapat Koordinasi**, **Evaluasi Struktur** | Turunan RekamanBukti. Evaluasi menunjuk SK yang dievaluasi, dan bila struktur diubah, SK revisi dan jabatan yang direvisi |

### CM-3 · Pengendalian dokumen SOP/IK (PKG-02)

| Konsep | Isi dan alasan |
|---|---|
| **DokumenInduk** | Daftar induk: kode, judul, jenis, kategori, asal, status wajib, dasar kebutuhan, tanggal ditetapkan wajib, siklus tinjau. `/memenuhi` = S1–S5 (AB-24). Lokasi penggunaan = Ruang (keputusan 14 November 2026) |
| **Versi Dokumen** | Turunan DokumenDisahkan; bagian dari DokumenInduk. Revisi unik per induk (AB-13). `/tanggal_tinjau_berikutnya`, `/perlu_ditinjau` (AB-14, S2) |
| **Distribusi**, **Sosialisasi**, **Tinjau Ulang** | Turunan RekamanBukti, masing-masing menunjuk satu versi |

### CM-4 · Rencana (PKG-01, PKG-13)

| Konsep | Isi dan alasan |
|---|---|
| **Renstra** | Turunan DokumenDisahkan. Hanya judul, berkas, dan periode (keputusan 14 November 2026) |
| **Rencana** | Turunan DokumenDisahkan. `jenis` (tahunan, pengembangan), `judul`, `narasi`, `/kriteria_tertinggi` |
| **TemuanGap** | Bagian dari Rencana pengembangan; satu per aspek, atau dinyatakan "tidak ada gap" |
| **ItemRencana** | Bagian dari Rencana. KPI 0..1 (wajib saat diajukan, AB-02), `pic` 1, `menjawab` temuan gap |
| **KPI** | Master. `frekuensi` sebagai enumerasi |
| **Realisasi** | Turunan RekamanBukti; satu per item per periode lapor (AB-18) |
| **Tinjauan Rencana** | Turunan RekamanBukti; `ditinjau` 1 dan `rencana_berikut` 0..1 (AB-19) |
| **UkuranManfaat** | Bagian dari Tinjauan; menunjuk item yang diukur (AB-20) |

Master Core yang dirujuk sebagai *stub*: **Periode** dan **Ruang**.

---

## 3. Keputusan pemodelan

| Keputusan | Alasan | Bab |
|---|---|---|
| **Dua konsep abstrak**: DokumenDisahkan dan RekamanBukti | Atribut, asosiasi, dan aturannya sama persis untuk banyak konsep. Ini cikal bakal *mixin* yang diminta pembimbing (langkah 10) | §9.2.1 |
| **Pengesahan dan KejadianPengesahan sebagai konsep kejadian**, bukan `pengesah`, `tanggal_sah`, `alasan_kembali`, `alasan_cabut` di DokumenDisahkan | Data itu baru ada setelah transisi tertentu; atribut opsional membuat konsep tidak kohesif. Riwayat juga harus menyimpan pengembalian berkali-kali (CLAUDE.md bagian 8) | §9.3.2 |
| **Status S1 sebagai atribut enumerasi**; sub-status S2 sebagai atribut turunan | S1 tidak menambah struktur selain lewat konsep kejadian; S2 hanya nilai yang dihitung dari tanggal | §9.3.1 |
| **`revisi_dari` refleksif** di DokumenDisahkan | Satu pola penggantian untuk versi SOP/IK, revisi rencana, SK, dan Renstra; dokumen lama tetap tersimpan sebagai Diganti | §11.9.2 (*superseding*) |
| **Atasan dan pengganti sebagai asosiasi refleksif** di Jabatan | Struktur lab bisa berubah tanpa mengubah model; jabatan fakultas tetap bisa dirujuk sebagai atasan | §11.8 (*organizational hierarchy*) |
| **Periode sebagai master Core** yang dirujuk Renstra, Rencana, dan SK | Masa berlaku dokumen; K1 "masih berlaku" dihitung dari periode | §11.12.1 (*effectivity*) |
| **Satu konsep Rencana dengan atribut `jenis`**, bukan dua subkelas | Sesuai pola bersama di brief. Perbedaannya hanya TemuanGap, nilai risiko/manfaat, dan UkuranManfaat. Konsekuensinya: dua atribut ItemRencana boleh kosong untuk jenis tahunan; diterima demi kesederhanaan, dijaga AB-02 | §9.2.1 (dipertimbangkan, tidak dipakai) |
| **Jabatan pengesah dibaca dari asosiasi Personel–Jabatan**, bukan BarisPenetapan | AB-05: pejabat fakultas tidak ada di SK lab, dan SK pertama harus bisa disahkan | — |
| **Peserta sosialisasi** = Personel yang tercatat + `jumlah_peserta` | Mahasiswa bukan Personel (keputusan 14 November 2026). Daftar hadir sebagai `bukti` **[ASUMSI]** | — |
| **Status monev tidak menjadi konsep** | Hanya hasil hitung: `/memenuhi` di DokumenInduk, `/kriteria_tertinggi` di Rencana dan SK; persentase PKG-02 dihitung atas semua DokumenInduk wajib saat dibaca (`status_monev()`) | §8.2.3 |
| **Koreksi rekaman tidak menjadi konsep** | Cukup dilacak sebagai riwayat perubahan (KNF-05); dipetakan ke pelacakan perubahan di langkah 10 | — |

---

## 4. Cek kelengkapan terhadap kamus DTO

Setiap isi kamus DTO di SSD harus punya tempat di model (CLAUDE.md langkah 9).

| DTO | Tempat di model | Catatan |
|---|---|---|
| `dto_dokumen_ringkas` | DokumenDisahkan (`status`, `/jenis_dokumen`, `/tanggal_ajukan`, `/berkas_ttd`, `penyusun`) + atribut turunannya (judul, periode) | **Ditambahkan** saat cek ini: `penyusun` dan `/tanggal_ajukan`. Judul versi dibaca dari DokumenInduk. `tanggal_ubah` = pelacakan perubahan (langkah 10) |
| `dto_rincian_dokumen`, `dto_riwayat`, `dto_status` | DokumenDisahkan, KejadianPengesahan, Pengesahan, `revisi_dari`, Versi Dokumen | |
| `dto_kelengkapan` | Dihitung dari isi dokumen (AB-02) | Tidak disimpan |
| `dto_personel_ringkas`, `dto_personel` | Personel + `jabatan` | `akun_pengguna` adalah detail teknologi (langkah 10) |
| `dto_jabatan` | Jabatan, Tugas, Wewenang, `atasan`, `pengganti` | |
| `dto_sk`, `dto_baris_penetapan` | SK Penetapan, BarisPenetapan, Periode, Ruang | |
| `dto_rapat`, `dto_evaluasi` | Rapat Koordinasi, Evaluasi Struktur, RekamanBukti | |
| `dto_koreksi` | Pelacakan perubahan | Tidak menjadi konsep (bagian 3) |
| `dto_dokumen_induk*`, `dto_info_versi`, `dto_versi*` | DokumenInduk, Versi Dokumen, `/versi_berlaku` | `revisi_berikutnya` dan `versi_dalam_proses` dihitung |
| `dto_distribusi`, `dto_sosialisasi`, `dto_tinjau`, `dto_status_tinjau` | Distribusi, Sosialisasi, Tinjau Ulang, RekamanBukti | |
| `dto_kpi`, `dto_renstra` | KPI, Renstra | |
| `dto_rencana*`, `dto_gap`, `dto_item` | Rencana, TemuanGap, ItemRencana | `biaya` rencana pengembangan = `anggaran` |
| `dto_item_pic`, `dto_realisasi`, `dto_capaian` | ItemRencana, Realisasi | `capaian_terakhir` dihitung |
| `dto_tinjauan` | Tinjauan Rencana, UkuranManfaat | |
| `dto_laporan_*`, `dto_status_monev` | Dihitung dari model | «report» |

Semua isi DTO punya tempat.

---

## 5. Cek silang

- **Aturan bisnis:** setiap AB merujuk atribut atau asosiasi yang ada. AB-05 → `/pengesah_berwenang`, Personel–Jabatan, Wewenang. AB-08 → `revisi_dari`. AB-13 → «unique» revisi. AB-14 → `/tanggal_tinjau_berikutnya`. AB-16 → `lokasi_penggunaan`. AB-18 → Realisasi «unique» (item, periode lapor). AB-19 → `ditinjau`, `rencana_berikut`. AB-24 → `/memenuhi`. AB-25 → `/kriteria_tertinggi`.
- **Status:** nama status sama dengan S1 (draf, diajukan, disahkan, diganti, dicabut, kedaluwarsa). Jenis kejadian sama dengan event S1.
- **Kriteria instrumen:** K1 (DokumenDisahkan + Pengesahan + Periode), PKG-01/13 K2 (ItemRencana, TemuanGap, KPI), PKG-03 K2 (Jabatan, Tugas, Wewenang), K3 (Realisasi, Rapat Koordinasi), K4 (Tinjauan Rencana, UkuranManfaat, Evaluasi Struktur), S1–S5 (DokumenInduk, Versi Dokumen, Distribusi, Sosialisasi, Tinjau Ulang).
- **Kesalahan di langkah sebelumnya:** kamus DTO `dto_dokumen_ringkas` sudah memuat `penyusun`, tetapi katalog operasi tidak punya operasi yang menetapkannya. Penyusun ditetapkan otomatis dari `user_id` saat dokumen dibuat (`buat_versi`, `buat_rencana`, `buat_sk`, `buat_renstra`). Tidak perlu operasi baru.

---

## 6. Perubahan dibanding versi sebelumnya

Versi sebelumnya ada di tag `rancangan-tatkel-v1` (CM-1 s.d. CM-4).

| Versi lama | Versi ini | Alasan |
|---|---|---|
| DokumenTerkendali + Pengajuan + Pemeriksaan + Pencabutan | DokumenDisahkan + Pengesahan + KejadianPengesahan | Tahap pemeriksaan dihapus; kejadian disatukan sebagai riwayat |
| Personel sebagai konsep dengan pihak eksternal | Personel tanpa pihak eksternal | Keputusan 14 November 2026 |
| Sasaran Renstra, IKU, Renstra berisi visi-misi | Renstra sebagai dokumen unggahan; rujukan Renstra berupa teks di item | Keputusan 14 November 2026 |
| Lokasi penggunaan termasuk portal | Ruang saja | Keputusan 14 November 2026 |
| — | RekamanBukti sebagai konsep abstrak | Satu aturan AB-22 untuk tujuh rekaman |

---

## 7. Temuan untuk langkah 10 (design class diagram)

| Konsep (CM) | Usulan di DCD |
|---|---|
| DokumenDisahkan + Pengesahan + KejadianPengesahan | `labfik.approval.mixin` (AbstractModel) + `labfik.approval.log` (model log), dengan Template Method `action_sahkan()` dan *hook* untuk turunan |
| `revisi_dari`, `/versi_berlaku` | Field di mixin; *hook* untuk menentukan dokumen yang diganti (versi per induk vs revisi) |
| Periode (Renstra, Rencana, SK) | `labfik.period.mixin` (+ penjadwal kedaluwarsa, Pelengkap) |
| `/kriteria_tertinggi` (Rencana, SK) | `labfik.criteria.mixin` dengan `_cek_k1()`–`_cek_k4()` {abstract} |
| RekamanBukti | `labfik.evidence.mixin`; AB-22 sebagai larangan hapus |
| Personel, Jabatan | `hr.employee` dan `hr.job` diperluas (`_inherit`); Tugas dan Wewenang = model baru One2many |
| Status, jenis, kategori | `fields.Selection` |
| Atribut turunan | `compute` (tersimpan bila dipakai untuk filter, mis. `perlu_ditinjau`) |

`labfik.controlled.mixin` (kode, revisi, unit pemilik) dari kontrak Core perlu dinilai ulang: di CM ini kode dan revisi hanya dibutuhkan DokumenInduk/Versi dan SK, jadi mixin itu mungkin tidak memberi manfaat yang sepadan.

## 8. Isu terbuka

- [ ] Peserta sosialisasi: Personel + jumlah peserta, dengan daftar hadir sebagai bukti **[ASUMSI]**
- [ ] Atribut nilai risiko/manfaat boleh kosong untuk rencana tahunan (satu konsep Rencana) **[USULAN PENULIS]**
- [ ] Tampilan diagram belum dicek di draw.io **[VALIDASI]**
