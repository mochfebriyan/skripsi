# Conceptual Model Modul SDM & Kompetensi

19 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 9 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** (Bab II 2.3.4, atas permintaan penulis 19 November 2026); sebelumnya direncanakan sebagai bahan kerja.

Diagram: [conceptual-model-sdm.drawio](conceptual-model-sdm.drawio), 5 halaman (CM-1a, CM-1b, CM-2, CM-3, CM-4) dan 1 halaman catatan. Dibuat dengan skrip [tools/drawio/sdm/conceptual_model.py](../tools/drawio/sdm/conceptual_model.py), yang fungsi gambar dan gayanya disalin dari `contoh-tata-kelola/conceptual_model.py` versi `main`. Diagram lolos `validate.py` dengan prefiks `sdm-` dan sudah diekspor ke PNG (`penulisan-skripsi/gambar/sdm/cm-01..05.png`) lewat draw.io desktop; tampilannya sudah dicek.

**Perubahan tata letak (19 November 2026):** label peran kini ditaruh di luar kotak sesuai sisi tempat garis keluar/masuk; CM-1 dipecah menjadi CM-1a (Kompetensi) dan CM-1b (Seleksi dan Penugasan) karena terlalu padat; kotak Personel, Periode, dan Mata Kuliah digambar lebih dari sekali agar garis tidak bersilangan; batasan «unique» gabungan ditulis di dalam kotak kelas, bukan di label garis; CM-3 disusun atas-bawah. Isi model (konsep, atribut, asosiasi) tidak berubah. Rujukan "CM-1" di dokumen lain berarti CM-1a dan CM-1b.

Sumber: [ssd-sdm.md](ssd-sdm.md) (kamus DTO), [expanded-use-case-sdm.md](expanded-use-case-sdm.md) (AB-SDM-01–28), [proses-bisnis-sdm.md](proses-bisnis-sdm.md) (S1–S4).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Hanya konsep, atribut primitif, dan asosiasi bernama peran; tanpa method, tanpa Odoo, tanpa atribut bertipe kelas atau `*_id` | §8, §10.4 | Semua halaman. Rujukan ke orang ditulis sebagai asosiasi ke Personel dengan peran (pemilik, penilai, penyetuju, supervisor, …) |
| Atribut turunan `/nama`; «unique»; komposisi hanya untuk bagian–keseluruhan | §8.2, §8.4.5 | `/berlaku`, `/kompetensi_kurang`, `/status`, `/status_evaluasi`, `/kriteria_tertinggi`; komposisi: Surat–Baris, Seleksi–Pengecualian, Evaluasi–Keputusan, Rencana–Kebutuhan/Item, Item–Pembatalan, Dokumen–Riwayat |
| Data yang baru muncul saat status berubah = **konsep kejadian** (*modal class*) | §9.3.2 | Pengecualian, KeputusanEvaluasi, PembatalanItem, Pengesahan, KejadianPengesahan |
| Generalisasi untuk perilaku dan atribut bersama | §8.3 | DokumenSDM (3 turunan), RekamanBukti (8 turunan) |
| Pola Bab 11 | §11.3, §11.9.2, §11.12.1 | *Specification class* (Kompetensi / BuktiKompetensi), *superseding* (`menggantikan`), *effectivity* (interval berlaku) |
| Setiap isi kamus DTO punya tempat di model | CLAUDE.md langkah 9 | Bagian 4 |

---

## 2. Isi diagram

| Halaman | Konsep milik SDM | Konsep Core (rincian di Core) |
|---|---|---|
| CM-1a Kompetensi | Kompetensi, BuktiKompetensi | Jabatan, Personel |
| CM-1b Seleksi dan Penugasan | KebutuhanPetugas, Seleksi, Pengecualian, SuratTugas, BarisPenugasan, Orientasi | Personel, Mata Kuliah, Kelas, Periode, Ruang, Sesi |
| CM-2 Otorisasi | TugasKhusus, Asesmen, Otorisasi, EvaluasiUlang, KeputusanEvaluasi | Personel |
| CM-3 Pengesahan dan Rekaman Bukti | *DokumenSDM*, Pengesahan, KejadianPengesahan, *RekamanBukti* | Personel |
| CM-4 Pelatihan | RencanaPelatihan, KebutuhanKompetensi, ItemPelatihan, PembatalanItem, RealisasiPelatihan, EvaluasiEfektivitas | Personel, Periode |

**Jumlah:** 23 konsep SDM (2 abstrak, 5 konsep kejadian), 7 konsep Core, 21 enumerasi.

---

## 3. Keputusan dan alasannya

| Keputusan | Alasan |
|---|---|
| Pengecualian seleksi, keputusan evaluasi ulang, dan pembatalan item menjadi konsep sendiri, bukan atribut opsional | Ketiganya hanya ada setelah kejadian tertentu dan membawa data sendiri (alasan, penyetuju, penilai, tanggal) (§9.3.2). Di DCD boleh dilebur menjadi field karena multiplisitasnya 0..1 (§13.6) |
| `/kompetensi_kurang` sebagai asosiasi turunan Personel → Kompetensi | Satu definisi dipakai empat tempat: Matriks Kompetensi, S3 PKG-04, kelengkapan otorisasi, dan pengisian awal kebutuhan pelatihan (AB-SDM-13, 20) |
| `/status` EvaluasiUlang dihitung dari ada-tidaknya KeputusanEvaluasi | Transisi stabil (§9.3.1); tidak ada dua sumber kebenaran untuk status *Terbuka* |
| Pelaksana tugas/alat sebagai asosiasi TugasKhusus–Personel tanpa tanggal | *Sweet spot*: penyebut PKG-10 cukup daftar pelaksana saat ini; riwayat pelaksana dicatat sebagai saran pengembangan (kontrak Core bagian 4.4) |
| DokumenSDM tanpa status *kedaluwarsa* | Modul SDM tidak memakai penjadwal (K-3); keberlakuan dihitung dari tanggal |
| Kebutuhan Petugas per kelas, bukan per sesi | Keputusan 14 November 2026 (brief); S1 PKG-04 dicek lewat kelas sesi |

---

## 4. Cek kelengkapan terhadap kamus DTO

| DTO (ssd-sdm.md) | Tempat di model |
|---|---|
| `dto_dokumen_ringkas`, `dto_rincian_dokumen`, `dto_status`, `dto_riwayat` | DokumenSDM + Pengesahan + KejadianPengesahan (CM-3) |
| `dto_kelengkapan` | Hasil hitung AB-SDM-02–04; tidak disimpan |
| `dto_kompetensi`, `dto_bukti_kompetensi`, `dto_matriks` | Kompetensi, BuktiKompetensi, `/kompetensi_kurang` (CM-1) |
| `dto_kebutuhan_kelas`, `dto_kebutuhan` | KebutuhanPetugas + Kelas (CM-1) |
| `dto_seleksi`, `dto_seleksi_ringkas` | Seleksi + Pengecualian (CM-1). `nama_calon` hanya data masukan untuk membuat Personel |
| `dto_surat`, `dto_penugasan` | SuratTugas + BarisPenugasan (CM-1) |
| `dto_orientasi` | Orientasi (CM-1) |
| `dto_petugas_sesi` | Sesi + KebutuhanPetugas + BarisPenugasan + `/kompetensi_kurang` + Seleksi; S1–S4 dihitung (AB-SDM-26) |
| `dto_tugas_khusus`, `dto_asesmen` | TugasKhusus, Asesmen (CM-2) |
| `dto_otorisasi`, `dto_operator` | Otorisasi (CM-2); `calon_supervisor` = hasil hitung |
| `dto_pemicu`, `dto_keputusan`, `dto_evaluasi` | EvaluasiUlang + KeputusanEvaluasi (CM-2); `tindak_lanjut` dihitung dari keputusan |
| `dto_rencana`, `dto_kebutuhan_pelatihan`, `dto_item_pelatihan` | RencanaPelatihan + KebutuhanKompetensi + ItemPelatihan + PembatalanItem (CM-4) |
| `dto_realisasi`, `dto_evaluasi_pelatihan` | RealisasiPelatihan + EvaluasiEfektivitas (CM-4) |
| `dto_status_monev`, `dto_persentase`, `dto_kriteria`, `dto_unit_monev` | Hasil hitung AB-SDM-26–28; tidak disimpan |

Semua isi kamus DTO punya tempat di model atau dinyatakan sebagai hasil hitung.

---

## 5. Temuan untuk langkah 10

- Konsep kejadian 0..1 (Pengecualian, KeputusanEvaluasi, PembatalanItem, Pengesahan) dilebur menjadi field di model pemiliknya; KejadianPengesahan (*) memakai `labfik.approval.log` dari Core.
- DokumenSDM → `labfik.approval.mixin`; RekamanBukti → `labfik.evidence.mixin`; keduanya sudah ada di Core.
- `menggantikan` → *hook* `_dokumen_diganti()`; untuk Surat Tugas ditambah field `revisi_dari_id`.
- Asosiasi turunan `/kompetensi_kurang` → method `hr.employee.kompetensi_kurang(tanggal)`.
