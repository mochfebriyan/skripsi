# Conceptual Model Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF. Bahan kerja, tidak dicantumkan di proposal.** Ini Step 9 rancangan TO-BE. Diagram: [conceptual-model-tata-kelola.drawio](conceptual-model-tata-kelola.drawio), 3 halaman.

Conceptual model menjawab "konsep apa saja yang ada di domain lab dan bagaimana hubungannya", **tanpa** keputusan teknis Odoo. Design class diagram (Step 10, masuk proposal) dibangun di atasnya dengan menambahkan method dari katalog operasi SSD, mixin, dan tipe field Odoo.

## Aturan yang dipakai (Wazlawick 2024, Bab 8–11)

| Aturan | Penerapan |
|---|---|
| Hanya konsep, atribut, dan asosiasi; **tanpa method** (§8.1) | Tidak ada operasi di diagram |
| Atribut hanya bertipe **primitif** (§8.2). Relasi ke konsep lain wajib berupa **asosiasi**, bukan atribut bertipe kelas atau `*_id` (§10.4) | Semua `pic_id: Personel` di class diagram v1 diganti garis asosiasi dengan peran (`pic`, `pengesah`, `peserta`, …) |
| Atribut turunan `/nama` (§8.2.3), atribut unik «unique» (§8.3.1) | `/tanggal_tinjau_berikutnya`, `/status_kemutakhiran`, `/persen_capaian`, `/prioritas`, `/kriteria_tertinggi`, `/memenuhi`; «unique» pada kode dan nomor SK |
| Komposisi dipakai hemat, hanya untuk hubungan bagian–keseluruhan yang sungguhan (§8.4.5) | Rencana ◆ item/sasaran/program/baseline/gap; SK ◆ Penetapan; Jabatan ◆ Tugas/Wewenang; Dokumen Induk ◆ Versi; riwayat pengesahan. Realisasi **bukan** komposisi (catatan tentang item, bukan bagian item) |
| Asosiasi tanpa arah navigasi (§8.4.2) | Arah ditentukan di desain (Step 10) |
| **Modal class** (§9.3): data yang baru muncul saat status berubah dimodelkan sebagai konsep, bukan atribut opsional | Riwayat pengesahan (bagian 2.1) |
| Pola analisis (Bab 11) | Bagian 3 |

## 1. Daftar konsep

| Konsep | Halaman | Jenis | Asal (di mana kata bendanya muncul) |
|---|---|---|---|
| *DokumenTerkendali* | CM-1 | Abstrak, generalisasi Rencana, SKPenetapan, VersiDokumen | S1 (semua dokumen berbagi siklus status) |
| Pengajuan | CM-1 | Riwayat | UC-21, UC-22, UC-24 |
| Penarikan | CM-1 | Kejadian | UC-22 (S1 *tarik kembali*) |
| Pemeriksaan | CM-1 | Kejadian | UC-23; `dto_rincian_dokumen.catatan_pemeriksaan` |
| Pengembalian | CM-1 | Kejadian | UC-24 (termasuk V1, dicatat atas nama pengesah) |
| BerkasTTD | CM-1 | Kejadian, riwayat | UC-26; `dto_ttd` |
| Pengesahan | CM-1 | Kejadian | UC-27; `dto_status.pengesah, pencatat` |
| Pencabutan | CM-1 | Kejadian | UC-28 |
| Personel | CM-1–3 | Independen (CRUDL) | UC-01 |
| Jabatan, Tugas, Wewenang | CM-2 | Independen + bagian | UC-02, A4, bedah dokumen D6 |
| SKPenetapan, Penetapan | CM-2 | Dokumen terkendali + bagian | UC-03, bedah D6 |
| Rapat | CM-2 | Rekaman | UC-04 |
| EvaluasiStruktur | CM-2 | Rekaman | UC-05 |
| RuangLab | CM-2 | Independen (Core) | Bedah D1, D5 |
| DokumenInduk | CM-2 | Independen (CRUDL) | UC-07 |
| VersiDokumen | CM-2 | Dokumen terkendali | UC-08; `dto_versi_baru` |
| Distribusi, Sosialisasi, TinjauUlang | CM-2 | Rekaman | UC-09, UC-10, UC-11 |
| Rencana | CM-3 | Dokumen terkendali | UC-16; `dto_rencana_baru`, `dto_isi_rencana` |
| SasaranStrategis, Program, Baseline, TemuanGap, ItemRencana | CM-3 | Bagian Rencana | UC-16; `dto_isi_rencana`, `dto_item`, `dto_gap` |
| KPI | CM-3 | Independen (CRUDL) | UC-14 |
| SasaranRenstra | CM-3 | Independen (CRUDL) | UC-15 |
| Periode | CM-3 | Independen (Core) | UC-16 |
| Realisasi | CM-3 | Rekaman | UC-18; `dto_realisasi` |
| TinjauanRencana, UkuranManfaat | CM-3 | Rekaman + bagian | UC-19 |

Enumerasi: StatusDokumen, JenisDokumen (CM-1); JenisPersonel, KategoriDokumen, AlasanRevisi (CM-2); StatusCapaian, KomponenAnggaran, Frekuensi (CM-3). Enumerasi kecil ditulis langsung di tipe atribut.

## 2. Keputusan pemodelan

### 2.1 Riwayat pengesahan sebagai konsep (bukan field)

Di class diagram v1, pengesahan hanya berupa field di mixin (`pengesah_id`, `tanggal_sah`, `file_ttd`, …). Field seperti itu hanya menyimpan **keadaan terakhir**. Padahal dari S1 dan expanded use case:
- satu dokumen bisa diajukan → dikembalikan → diajukan lagi berkali-kali;
- berkas bertanda tangan bisa diganti (UC-26 V1);
- setiap kejadian membawa data sendiri: alasan, pencatat, jabatan pengesah saat itu.

Sesuai §9.3.2, kejadian-kejadian ini dimodelkan sebagai konsep: **Pengajuan** (riwayat, {ordered}), yang punya paling banyak satu **Pemeriksaan**, **Pengembalian**, **Penarikan**, dan **Pengesahan**, serta banyak **BerkasTTD**. **Pencabutan** melekat langsung ke dokumen.

Bagi monev, ini berarti **jejak pengesahan bisa ditelusuri penuh**: siapa, kapan, dengan jabatan apa, dan berkas mana. Nilai ini langsung relevan untuk ISO 8.3.2 dan PKG-02 S2.

### 2.2 DokumenTerkendali sebagai generalisasi domain

Rencana, SK Penetapan, dan Versi SOP/IK **memang** jenis-jenis dokumen terkendali di domain lab: ketiganya punya revisi, status, dan riwayat pengesahan yang sama. Karena itu generalisasi di sini adalah generalisasi **konseptual** (§9.2.1), bukan sekadar trik penulisan kode. Di Step 10, generalisasi ini diwujudkan sebagai mixin Odoo.

### 2.3 Asosiasi turunan

| Asosiasi | Definisi |
|---|---|
| `Jabatan./pemegang_aktif` | Personel pada Penetapan milik SK berstatus disahkan yang periodenya mencakup hari ini |
| `DokumenInduk./versi_berlaku` | Versi berstatus disahkan (paling banyak satu, AB-04) |

Keduanya menjawab kebutuhan `pengesah_berwenang*` dan `penerima_pemberitahuan` di kamus DTO tanpa menyimpan data ganda.

## 3. Pola analisis yang dipakai (Bab 11)

| Pola | Di mana |
|---|---|
| *Organizational hierarchy* (§11.8) | Jabatan–atasan, ditambah pengganti dan koordinasi |
| *Effectivity* (§11.12.1) | SKPenetapan, Penetapan, Rencana (melalui Periode): berlaku dalam rentang tanggal |
| *History* (§11.12.2) | Pengajuan {ordered}, versi {ordered}, tinjau ulang {ordered} |
| *Superseding* (§11.9.2) | `revisi_dari` / `pengganti` pada DokumenTerkendali; status Diganti |
| *Specification class* (§11.3) | KPI (definisi) ↔ ItemRencana (target per periode) |
| Transisi stabil (§9.3.1) | `status: StatusDokumen`, `jenis` pada Rencana |

## 4. Pengecekan kelengkapan terhadap kamus DTO

Setiap isi DTO di [ssd-tata-kelola.md](ssd-tata-kelola.md) bagian 3 harus punya tempat sebagai atribut, asosiasi, atau turunan.

| Isi DTO | Tempat di conceptual model |
|---|---|
| `tanggal_ttd`, `nama_penanda_tangan`, `berkas` | BerkasTTD |
| `pengesah`, `jabatan_pengesah`, `pencatat`, `atas_nama` | Pengesahan → peran `pengesah`, `pencatat`, `jabatan_pengesah` (atas nama = pengesah ≠ pencatat) |
| `alasan` | Pengembalian, Penarikan, Pencabutan |
| `catatan_pemeriksaan` | Pemeriksaan.catatan |
| `riwayat_pengajuan` | DokumenTerkendali ◆ Pengajuan {ordered} |
| `dokumen_diganti` | asosiasi `revisi_dari` / `pengganti` |
| `pengesah_berwenang*`, `penerima_pemberitahuan` | Turunan: Wewenang × `Jabatan./pemegang_aktif` |
| `status_kemutakhiran`, `tanggal_tinjau_berikutnya` | VersiDokumen (turunan) |
| `versi_diproses`, `versi_berlaku`, `riwayat_versi` | VersiDokumen.status; `/versi_berlaku`; versi {ordered} |
| `butir` / `terpenuhi` (`dto_kelengkapan`) | Tidak disimpan. Hasil pengecekan AB-01 saat diajukan |
| `bagian_terisi`, `bagian_belum`, `lengkap`, `butir_kurang` | Tidak disimpan. Turunan dari isi Rencana dan ItemRencana |
| `prioritas`, `rekap_anggaran`, `persen_capaian` | Turunan |
| `jumlah_temuan` (`dto_status_gap`) | Turunan dari TemuanGap per aspek |

**Hasil:** semua isi DTO punya tempat. Tidak ada konsep yang terputus: setiap konsep terhubung ke Personel atau DokumenTerkendali, sehingga modelnya merupakan satu graf (§8.3.2).

## 5. Bekal untuk Step 10 (design class diagram)

| Dari conceptual model | Keputusan desain yang perlu diambil |
|---|---|
| Riwayat pengesahan (7 konsep) | (a) Satu model log pengesahan (`labfik.approval.log`, satu baris per kejadian: ajukan, periksa, kembalikan, tarik, sahkan, cabut) ditambah field ringkas di `approval.mixin` untuk keadaan terakhir; atau (b) hanya memakai riwayat `mail.thread`. **Usulan: (a)**, karena riwayat terstruktur bisa dicari dan dilaporkan sebagai bukti monev, sedangkan pesan chatter berupa teks bebas |
| Generalisasi *DokumenTerkendali* | Diwujudkan sebagai `AbstractModel` (mixin), sesuai arahan Pak Widi |
| Asosiasi bertanda peran | Menjadi `Many2one` / `One2many` / `Many2many` dengan nama field = nama peran (`pengesah_id`, `peserta_ids`, …) |
| Atribut turunan `/…` | Menjadi field `compute` |
| Kejadian bertanggal (Rapat, Distribusi, …) | Atribut `tanggal`, `bukti` dan peran pelapor disatukan lewat `evidence.mixin` |
| Personel | Opsi model masih **[KONFIRMASI]** bersama kelompok |

## 6. Isu terbuka

- [ ] Kontrak konsep Personel bersama Zahir dan Herrens.
- [ ] `pencatat` pada Pengembalian dan Pengesahan bergantung pada jawaban "apakah Dekan login" **[KONFIRMASI]**.
- [ ] Atribut khusus rencana pengembangan (`nilai_risiko`, `nilai_manfaat`) masih atribut biasa di ItemRencana. Kalau jumlahnya bertambah, pertimbangkan konsep terpisah (§9.3.2).
