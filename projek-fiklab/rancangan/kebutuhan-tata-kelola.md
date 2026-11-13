# Kebutuhan Sistem Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · Bagian dari proyek LabFIK Compliance · PKG-01, 02, 03, 13

**Status: DRAF.** Dasar untuk use case diagram, class diagram, activity diagram, dan sequence diagram (Bab II 2.3).

Sumber:
- [brief-tata-kelola-dokumen.md](../brief/brief-tata-kelola-dokumen.md): masalah M1–M4 dan batasan.
- [analisis-data-pengelolaan-1-3.md](../analisis/analisis-data-pengelolaan-1-3.md) dan [analisis-data-pengembangan-13.md](../analisis/analisis-data-pengembangan-13.md): kriteria K1–K4 dan S1–S5.
- [bedah-dokumen-tata-kelola.md](../analisis/bedah-dokumen-tata-kelola.md): model, field, dan laporan.

---

## 1. Aktor

| Aktor | Siapa | Peran utama di sistem | Grup akses (usulan) |
|---|---|---|---|
| **KaLab** | Kepala Laboratorium (saat ini satu per prodi) | Menyusun rencana, SK pengelola, rapat, dan tinjauan. Mengesahkan dokumen yang menjadi wewenangnya (misalnya POB lab) | `labfik_kalab` |
| **Laboran/PLP** | Laboran dan teknisi | Menyusun dan mengunggah SOP/IK, mencatat distribusi dan sosialisasi, mengisi realisasi kegiatan yang menjadi PIC-nya | `labfik_laboran` |
| **Dekan** | Pimpinan fakultas | Mengesahkan SK pengelola, Renstra/RKT, rencana pengembangan, dan POB fakultas | `labfik_pengesah` |
| **Pemeriksa** | Wakil Dekan / unit mutu / GKM | Memeriksa dokumen sebelum disahkan. Tahap ini **opsional** | `labfik_pengesah` |
| **Pengguna Lab** | Dosen, asisten, mahasiswa | Membaca SOP/IK versi berlaku. Tercatat sebagai peserta sosialisasi | `labfik_pengguna` |
| **Penilai Monev** | Auditor internal, LPMPP, atau tim monev | Melihat status indikator dan buktinya (hanya baca) | `labfik_penilai` |
| **Admin** | Pengelola sistem | Mengelola master bersama dan pengaturan | `labfik_admin` |

Hal yang perlu dicatat:
- Hak akses mengikuti **jabatan aktif** di SK pengelola, bukan nama orang. Misalnya, siapa pun yang sedang memegang jabatan KaLab otomatis punya wewenang KaLab.
- Dekan dan Pemeriksa mungkin tidak login sendiri ke sistem **[KONFIRMASI]**. Kalau begitu, KaLab mengunggah PDF yang sudah ditandatangani Dekan, lalu menekan *Sahkan* atas nama pengesah. Sistem tetap mencatat siapa yang menekan tombol dan siapa pengesah yang tertera di dokumen.
- Satu atau dua KaLab (per prodi) masih menunggu keputusan apakah sistem melayani satu lab FIK atau per prodi **[KONFIRMASI]**.

---

## 2. Kebutuhan fungsional

**Prioritas:**
- **W** = wajib (MVP), karena dibutuhkan untuk membuktikan kriteria instrumen.
- **O** = opsional, dikerjakan bila waktu cukup.

### A. Struktur organisasi (PKG-03)

| ID | Kebutuhan | Aktor | Model | Kriteria | Prio |
|---|---|---|---|---|---|
| KF-01 | Sistem dapat mengelola data **Personel** (dosen, laboran/PLP, teknisi, asisten, petugas K3, pihak eksternal) | Admin, KaLab | `labfik.personel` | Master bersama | W |
| KF-02 | Sistem dapat mengelola **Jabatan**: unit, atasan (garis instruksi), koordinasi, jabatan pengganti, daftar tugas, dan daftar wewenang per jenis dokumen | KaLab, Admin | `labfik.jabatan` | PKG-03 K2 | W |
| KF-03 | KaLab dapat menyusun **SK penetapan pengelola** berperiode, berisi baris personel × jabatan × ruang | KaLab | `labfik.assignment` | PKG-03 K1 | W |
| KF-04 | Sistem dapat **mengekspor SK** ke PDF mengikuti format SK fakultas (Lampiran I bagan, Lampiran II tugas) | KaLab | [R] | PKG-03 Bukti 1–3 | W |
| KF-05 | Sistem dapat menampilkan **bagan organisasi** dari relasi jabatan | KaLab, Penilai | [R] | PKG-03 Bukti 2 | W |
| KF-06 | Sistem dapat menampilkan **matriks kewenangan** (jabatan × wewenang) | KaLab, Penilai | [R] | PKG-03 Bukti 4 | W |
| KF-07 | KaLab dapat mencatat **rapat koordinasi** (agenda, peserta, keputusan, notulen) | KaLab | `labfik.meeting` | PKG-03 K3 | W |
| KF-08 | KaLab dapat mencatat **evaluasi struktur** dan menautkannya ke SK atau jabatan hasil revisi | KaLab | `labfik.org.evaluation` | PKG-03 K4 | W |

### B. Pengendalian dokumen (PKG-02)

| ID | Kebutuhan | Aktor | Model | Kriteria | Prio |
|---|---|---|---|---|---|
| KF-09 | Sistem dapat mengelola **Dokumen Induk**: kode, jenis, kategori, asal (lab/fakultas/universitas), status wajib, dasar kebutuhan, lokasi penggunaan, dan dokumen terkait | KaLab, Laboran | `labfik.document` | PKG-02 S1 | W |
| KF-10 | Laboran dapat **mengunggah versi baru** SOP/IK (file, nomor revisi, bagian yang diubah, ringkasan, alasan revisi) | Laboran | `labfik.document.version` | PKG-02 S2 | W |
| KF-11 | Sistem menjaga **hanya satu versi berlaku** per dokumen. Saat versi baru disahkan, versi lama otomatis berstatus *diganti* | Sistem | `labfik.document.version` | PKG-02 S2, ISO 8.3.2 | W |
| KF-12 | Laboran dapat mencatat **distribusi** versi berlaku ke titik penggunaan (ruang/portal) | Laboran | `labfik.document.distribution` | PKG-02 S4 | W |
| KF-13 | Laboran dapat mencatat **sosialisasi** versi berlaku beserta pesertanya | Laboran | `labfik.document.socialization` | PKG-02 S5 | W |
| KF-14 | Sistem menghitung **tanggal tinjau ulang** berikutnya dan menandai dokumen yang terlambat ditinjau | Sistem | mixin kendali | PKG-02 S3 | W |
| KF-15 | Sistem mengirim **pengingat** menjelang tanggal tinjau ulang | Sistem | `mail.activity` | PKG-02 S3 | O |
| KF-16 | Pengguna Lab dapat **mencari dan membaca** SOP/IK versi berlaku. Versi lama hanya bisa dilihat KaLab, Laboran, dan Penilai | Pengguna Lab | `labfik.document` | PKG-02 (dapat diakses) | W |
| KF-17 | Sistem dapat mencetak **Daftar Induk Dokumen** dan **riwayat revisi** | KaLab, Penilai | [R] | PKG-02 Bukti 1, 3 | W |
| KF-38 | Laboran/KaLab dapat mencatat **tinjau ulang** versi berlaku. Hasilnya: *tetap berlaku* (tanggal tinjau berikutnya diperbarui) atau *perlu revisi* (lanjut ke unggah versi baru) | Laboran, KaLab | `labfik.document.review` | PKG-02 S3, ISO 8.3.2b | W |

### C. Perencanaan (PKG-01, PKG-13)

| ID | Kebutuhan | Aktor | Model | Kriteria | Prio |
|---|---|---|---|---|---|
| KF-18 | Sistem dapat mengelola master **KPI**: rumus, satuan, frekuensi, PIC, sumber bukti, acuan ISO | KaLab | `labfik.kpi` | PKG-01 Bukti 4 | W |
| KF-19 | Sistem dapat mengelola **Sasaran Renstra** (UPNVJ/UPPS/prodi) | KaLab, Admin | `labfik.sasaran.renstra` | PKG-01 K2 | O (bisa diganti teks bebas) |
| KF-20 | KaLab dapat menyusun **rencana strategis**: narasi, visi-misi, sasaran strategis, program, dan baseline | KaLab | `labfik.plan` (strategis) | PKG-01 Bukti 1 | W |
| KF-21 | KaLab dapat menyusun **RKT**: item kegiatan dengan KPI, baseline, target, jadwal, PIC, anggaran, komponen anggaran, dan tautan ke sasaran/program/Renstra | KaLab | `labfik.plan` (tahunan) | PKG-01 K2 | W |
| KF-22 | KaLab dapat menyusun **dokumen IKU** (KPI + target periode) | KaLab | `labfik.plan` (iku) | PKG-01 Bukti 4 | W, bentuknya menunggu **[KONFIRMASI]** |
| KF-23 | KaLab dapat menyusun **rencana pengembangan**: analisis gap empat aspek, lalu item program dengan nilai risiko, manfaat, prioritas, biaya, target, PIC, dan jadwal | KaLab | `labfik.plan` (pengembangan) | PKG-13 K1–K2 | W |
| KF-24 | Sistem **memeriksa kelengkapan** rencana sebelum boleh diajukan, misalnya semua item punya KPI, target, PIC, jadwal, dan anggaran, serta keempat aspek gap terisi | Sistem | `labfik.plan` | PKG-01 K2, PKG-13 K2 | W |
| KF-25 | Sistem dapat **mengekspor rencana** ke PDF: Renstra+RKT, IKU, dan Rencana Pengembangan, mengikuti format dokumen lab | KaLab | [R] | PKG-01 Bukti 1–2, PKG-13 Bukti 1–4 | W |
| KF-26 | KaLab dapat membuat **revisi** dari rencana yang sudah disahkan. Rencana lama berstatus *diganti* dan riwayatnya tetap tersimpan | KaLab | `labfik.plan` | PKG-01 K4, ISO 8.3.2 | W |
| KF-27 | PIC dapat mengisi **realisasi** per item per periode lapor: capaian, anggaran terpakai, status capaian, analisis, tindak lanjut, dan bukti | Laboran, KaLab | `labfik.realisasi` | PKG-01 K3, PKG-13 K3 | W |
| KF-28 | Sistem dapat mencetak **laporan capaian** triwulan/semester | KaLab, Penilai | [R] | PKG-01 Bukti 5 | W |
| KF-29 | KaLab dapat mencatat **tinjauan** (peserta, ringkasan, keputusan) yang tertaut ke rencana berikutnya. Untuk rencana pengembangan, tinjauan juga memuat ukuran manfaat (nilai sebelum dan sesudah) | KaLab | `labfik.tinjauan` | PKG-01 K4, PKG-13 K4 | W |
| KF-30 | Sistem dapat menampilkan **matriks keterkaitan** Renstra × RKT × ISO | KaLab, Penilai | [R] | PKG-01 Bukti 3 | O (wajib bila KF-19 dibuat) |
| KF-43 | Sistem mengirim **pengingat pengisian realisasi** kepada PIC di akhir periode lapor | Sistem (Penjadwal) | `mail.activity` | PKG-01 K3 | O |

### D. Pengesahan (dipakai semua dokumen)

| ID | Kebutuhan | Aktor | Model | Kriteria | Prio |
|---|---|---|---|---|---|
| KF-31 | Dokumen mengikuti siklus status **Draf → Diajukan → (Diperiksa) → Disahkan → Diganti / Dicabut / Kedaluwarsa** (state machine S1 di [proses-bisnis-tata-kelola.md](proses-bisnis-tata-kelola.md)) | Semua penyusun & pengesah | mixin pengesahan | K1 (PKG-01, 03, 13), S2 (PKG-02) | W |
| KF-39 | Penyusun dapat **menarik kembali** pengajuan (Diajukan → Draf) dengan alasan | Penyusun | mixin pengesahan | Ditemukan dari S1 | W |
| KF-40 | Pemeriksa atau pengesah dapat **mengembalikan** dokumen ke penyusun (Diajukan/Diperiksa → Draf) dengan alasan. Bila penolakan terjadi di atas kertas, penyusun mencatatnya atas nama pengesah | Pemeriksa, Pengesah | mixin pengesahan | Ditemukan dari S1, A1 | W |
| KF-41 | Jabatan berwenang dapat **mencabut** dokumen berlaku (Disahkan → Dicabut) dengan alasan | Pengesah | mixin pengesahan | Ditemukan dari S1, A2 | W |
| KF-42 | Sistem otomatis menandai dokumen berperiode (rencana, SK) **Kedaluwarsa** saat periodenya berakhir | Sistem (Penjadwal) | mixin pengesahan, periode | K1 "masih berlaku" | W |
| KF-32 | KaLab dapat mengatur **pengaturan modul**: tahap *diperiksa* aktif per jenis dokumen, dan siklus tinjau ulang standar | KaLab | Pengaturan | PKG-02 S3 | O (siklus tinjau ulang: W) |
| KF-33 | *Sahkan* hanya dapat dilakukan bila **PDF bertanda tangan sudah diunggah** dan pengguna memegang **jabatan yang berwenang** untuk jenis dokumen itu | Sistem | mixin pengesahan | K1, S2 | W |
| KF-34 | Sistem mencatat **jejak audit**: siapa melakukan apa dan kapan, termasuk perubahan field penting | Sistem | `mail.thread` | Keterlacakan bukti | W |

### E. Status monev

| ID | Kebutuhan | Aktor | Model | Kriteria | Prio |
|---|---|---|---|---|---|
| KF-35 | Sistem menghitung **persentase SOP wajib yang memenuhi** (S1–S5) beserta daftar SOP yang tidak memenuhi dan alasannya | Sistem | [R] | PKG-02 (otomatis) | W |
| KF-36 | Sistem menampilkan **kriteria tertinggi yang lengkap secara data** (K1–K4) untuk PKG-01, 03, dan 13, beserta tautan ke rekaman buktinya | Sistem | mixin kriteria | PKG-01, 03, 13 (semi-otomatis) | W |
| KF-37 | Penilai Monev dapat **melihat status dan membuka bukti** tanpa bisa mengubah data | Penilai | — | Semua | W |

Sesuai batasan di brief, skor akhir PKG-01, 03, dan 13 **ditetapkan penilai**. Sistem hanya menunjukkan sampai kriteria ke berapa datanya lengkap.

---

## 3. Kebutuhan nonfungsional

| ID | Kebutuhan |
|---|---|
| KNF-01 | Berjalan di **Odoo 17 Community** tanpa OpenEduCat dan tanpa aplikasi Enterprise (misalnya *Documents*) |
| KNF-02 | Hak akses berbasis **grup Odoo** (bagian 1) dan **record rule**. Misalnya Pengguna Lab hanya melihat versi berlaku, dan Penilai hanya bisa membaca |
| KNF-03 | Ekspor dokumen memakai **QWeb report (PDF)** dengan format yang meniru dokumen lab dan SK fakultas |
| KNF-04 | **Tanpa tanda tangan digital.** Pengesahan dibuktikan dengan PDF bertanda tangan manual dan catatan siapa yang menekan *Sahkan* |
| KNF-05 | **Tanpa integrasi** dengan sistem kepegawaian, keuangan, SIAKAD, LeADS, atau SIMPEL |
| KNF-06 | Antarmuka berbahasa **Indonesia** |
| KNF-07 | Model dirancang dengan **inheritance (mixin)** agar perilaku bersama (kendali dokumen, pengesahan, periode, bukti, kriteria) tidak ditulis berulang (arahan Pak Widi) |
| KNF-08 | Data uji **fiktif**. Pilot memakai minimal satu dokumen nyata (1 SOP dan 1 draf struktur) |
| KNF-09 | Master Personel dan Jabatan dapat dipakai **modul lain** (SDM, Praktikum, Aset, Safety) tanpa disalin |

---

## 4. Keterlacakan masalah → kebutuhan

| Masalah (brief 1.2) | Tujuan | Kebutuhan |
|---|---|---|
| M1. SK pengelola, rencana kerja, dan rencana pengembangan belum disahkan; SOP lab ada tetapi tidak terkendali | T1. Menuntun penyusunan dan pengesahan | KF-01–04, KF-09–10, KF-18–25, KF-31–33 |
| M2. Kriteria "dijalankan" dan "dievaluasi" butuh rekaman yang belum ada | T2. Rekaman realisasi, rapat, tinjauan, evaluasi | KF-07–08, KF-12–13, KF-26–29 |
| M3. Belum ada pengendalian dokumen | T3. Pengendalian dokumen berversi dengan pengesah sesuai jabatan | KF-09–17, KF-31–34, KF-38, KF-39–42 |
| M4. Status indikator dihitung manual dan tidak tertelusur | T4. Status monev | KF-05–06, KF-17, KF-28, KF-30, KF-35–37 |

---

## 5. Use case

Daftar use case sistem, penurunannya dari proses bisnis, dan pemetaan ke KF ada di [use-case-tata-kelola.md](use-case-tata-kelola.md). Daftar kandidat use case versi sebelumnya (UC-01–23) sudah diganti.

KF yang dijalankan sistem dan tidak berdiri sebagai use case sendiri: KF-11, 14, 24, 34, 35, 36 (masuk ke use case yang memicunya, lihat bagian 2 dokumen use case).

---

## 6. Pertanyaan terbuka

- [ ] Apakah Dekan dan Pemeriksa login sendiri ke sistem, atau KaLab yang mengunggah PDF bertanda tangan atas nama mereka? (bagian 1)
- [ ] Satu lab FIK atau per prodi? (bagian 1; bedah dokumen A11)
- [ ] IKU dokumen terpisah atau bagian RKT? (KF-22)
- [ ] Sasaran Renstra sebagai master atau cukup teks bebas? Bergantung pada ketersediaan dokumen Renstra UPNVJ/UPPS/prodi (KF-19)
