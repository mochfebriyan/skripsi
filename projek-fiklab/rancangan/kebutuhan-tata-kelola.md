# Kebutuhan Sistem Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 4 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). Bahan Bab II 2.2 Usulan Solusi, dan dasar untuk proses bisnis (langkah 5) dan use case (langkah 6). Dokumen ini bukan diagram, jadi tidak masuk 2.3 secara langsung.

Sumber:
- [brief-tata-kelola-dokumen.md](../brief/brief-tata-kelola-dokumen.md): masalah M1–M4, cakupan rancangan (Inti + Pelengkap), batasan masalah, dan keputusan 13–14 November 2026.
- [analisis-data-pengelolaan-1-3.md](../analisis/analisis-data-pengelolaan-1-3.md) dan [analisis-data-pengembangan-13.md](../analisis/analisis-data-pengembangan-13.md): kriteria K1–K4 dan S1–S5, luaran, entitas.
- [bedah-dokumen-tata-kelola.md](../analisis/bedah-dokumen-tata-kelola.md): temuan as-is A1–A12, model, field, dan laporan.

---

## 0. Aturan yang dipakai

Mengikuti Wazlawick (2024) bab 4.2 dan 4.7:

| Aturan | Bab | Penerapan di dokumen ini |
|---|---|---|
| Aktor adalah peran yang berinteraksi dengan sistem, **bukan** profil keamanan | 4.2 | Grup akses hanya usulan. Dekan, penilai, dan pihak eksternal tidak berinteraksi dengan sistem, jadi bukan aktor |
| Kebutuhan fungsional **evident** (E) dikerjakan lewat antarmuka dengan sepengetahuan pengguna; **hidden** (H) dikerjakan sistem sebagai akibat fungsi lain | 4.7.2 | Kolom "Jenis". KF hidden tidak menjadi use case sendiri, tetapi dicatat pada use case pemicunya di langkah 6 |
| Kebutuhan nonfungsional yang terikat fungsi = **logis** (aturan bisnis) atau **teknologis**; yang berlaku untuk seluruh sistem = **suplementer** | 4.7.3–4.7.4, 4.7.7 | Aturan bisnis ditulis sebagai AB-xx di langkah 7. Bagian 3 hanya memuat kebutuhan teknologis dan suplementer, dikelompokkan menurut ISO/IEC 25010 |
| Permanen atau transien | 4.7.5 | Ditandai bila relevan (misalnya siklus tinjau ulang) |
| Wajib dan diinginkan | 4.7.6 | Prioritas **W** = lapis Inti, **O** = lapis Pelengkap (brief, bagian Cakupan rancangan) |
| Setiap kebutuhan tertelusur ke sumbernya | 4.7.1 | Kolom "Kriteria/bukti" dan tabel keterlacakan di bagian 4 |

Kebutuhan di luar cakupan brief **tidak** ditulis sebagai KF. Daftarnya ada di bagian 5.

---

## 1. Aktor

| Aktor | Siapa | Peran utama di sistem | Grup akses (usulan) |
|---|---|---|---|
| **KaLab** | Kepala Laboratorium. Menurut slide PKKMB ada satu per prodi (A8–A9) | Mengelola Personel, Jabatan, dan KPI. Menyusun Renstra, rencana tahunan, rencana pengembangan, dan SK pengelola. Mencatat rapat, evaluasi, dan tinjauan. **Satu-satunya pencatat pengesahan.** Memantau status monev dan menerbitkan laporan bukti | `labfik_kalab` |
| **Laboran/PLP** | Laboran, PLP, dan teknisi | Menyusun Dokumen Induk dan mengunggah versi SOP/IK. Mencatat distribusi, sosialisasi, dan tinjau ulang. Mengisi realisasi item rencana yang menjadi PIC-nya | `labfik_laboran` |
| **Pengguna Lab** | Dosen dan asisten | Membaca SOP/IK versi berlaku (lapis Pelengkap) | `labfik_pengguna` |
| **Penjadwal** «system» | Pemicu waktu (`ir.cron`) | Menandai dokumen berperiode kedaluwarsa saat periodenya habis (lapis Pelengkap) | — |

Grup akses berjenjang: `labfik_kalab` mewarisi `labfik_laboran`, dan `labfik_laboran` mewarisi `labfik_pengguna` **[USULAN PENULIS]**.

**Bukan aktor** (keputusan di brief, 14 November 2026):

| Pihak | Alasan | Jejaknya di sistem |
|---|---|---|
| Dekan dan pejabat penanda tangan lain | Hanya menandatangani dokumen cetak | Dicatat sebagai Personel tanpa akun. Namanya disimpan sebagai **pengesah tercatat**, dan KaLab sebagai **pencatat** |
| Penilai monev | Menerima bukti berupa dokumen PDF yang diunggah lab ke iso.upnvj | Tidak ada. Laporan bukti diterbitkan KaLab (KF-45) |
| Pihak eksternal (vendor, tamu, pihak luar FIK) | Tidak berperan dalam tata kelola lab | Tidak dicatat sama sekali, termasuk tidak sebagai Personel |
| Admin teknis Odoo | Bukan peran domain | Pemasangan addon dan pengaturan teknis di luar rancangan |

Catatan untuk langkah 6: KaLab dan Laboran sama-sama berperan sebagai **penyusun** dokumen dan **PIC** item rencana. Kandidat aktor abstrak: *Pengelola Lab*, dengan KaLab dan Laboran sebagai turunannya.

---

## 2. Kebutuhan fungsional

Kolom:
- **Jenis:** E = *evident*, H = *hidden*.
- **Prio:** W = lapis Inti (tanpa ini ada kriteria yang tidak terbukti atau alur pengesahan putus), O = lapis Pelengkap.
- **Model (usulan):** nama sementara dari bedah dokumen bagian 5. Nama final ditetapkan di design class diagram (langkah 10).

### A. Pengesahan (dipakai semua dokumen)

Satu jalur: **ajukan → kembalikan atau sahkan → cabut**. Pemeriksaan menyatu dengan pengesahan, dan penolakan yang terjadi di atas kertas dicatat lewat aksi kembalikan yang sama.

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-01 | Penyusun dapat **mengajukan** dokumen untuk disahkan. Pengajuan ditolak bila isi dokumen belum lengkap menurut jenisnya (lihat KF-30) | KaLab, Laboran | `labfik.approval.mixin` | K1 PKG-01/03/13, S2 PKG-02 | E | W |
| KF-02 | Penyusun dapat **mengunggah PDF bertanda tangan** untuk dokumen yang sudah diajukan | KaLab, Laboran | `labfik.approval.mixin` | K1, S2 | E | W |
| KF-03 | KaLab dapat **mengembalikan** dokumen yang diajukan kepada penyusun dengan alasan | KaLab | `labfik.approval.mixin` | K1, S2 | E | W |
| KF-04 | KaLab dapat **mengesahkan** dokumen dengan mencatat pengesah tercatat (pejabat penanda tangan) dan tanggal sah. Sistem mencatat KaLab sebagai pencatat | KaLab | `labfik.approval.mixin` | K1, S2 | E | W |
| KF-05 | Sistem **menolak pengesahan** bila PDF bertanda tangan belum diunggah, atau bila pengesah tercatat tidak memegang jabatan yang berwenang mengesahkan jenis dokumen itu | Sistem | `labfik.approval.mixin`, `hr.job` | S2 ("pengesah dari jabatan berwenang"), ISO 8.3.2a | H | W |
| KF-06 | KaLab dapat **mencabut** dokumen yang sedang berlaku dengan alasan | KaLab | `labfik.approval.mixin` | ISO 8.3.2 (dokumen usang dicegah dipakai) | E | W |
| KF-07 | Sistem mencatat setiap **kejadian pengesahan** (diajukan, dikembalikan, berkas diunggah, disahkan, dicabut, diganti, kedaluwarsa) sebagai riwayat berisi waktu, pelaku, pengesah tercatat, alasan, dan berkas | Sistem | `labfik.approval.log` | PKG-02 Bukti 3 (bukti pengesahan dan revisi) | H | W |
| KF-08 | Saat versi atau revisi baru disahkan, sistem otomatis mengubah versi sebelumnya menjadi **diganti**, sehingga hanya satu yang berlaku | Sistem | `labfik.approval.mixin` | S2, ISO 8.3.2c | H | W |
| KF-09 | Penjadwal menandai dokumen berperiode **kedaluwarsa** saat periodenya habis | Penjadwal | `labfik.period.mixin` | K1 ("masih berlaku") | H | O |

Tanpa KF-09, status "masih berlaku" pada K1 tetap dihitung dari tanggal periode saat status monev dibaca (KF-44). Jadi KF-09 memperkuat, bukan syarat.

### B. Pengendalian dokumen SOP/IK (PKG-02)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-10 | Laboran dapat mengelola **Dokumen Induk**: kode, judul, jenis (SOP, IK, formulir, dokumen eksternal), kategori, asal (lab/fakultas/universitas), status wajib, dasar kebutuhan (kegiatan/risiko), lokasi penggunaan, siklus tinjau ulang, dan tanggal ditetapkan sebagai wajib | Laboran, KaLab | `labfik.document` | S1, Bukti 1 | E | W |
| KF-11 | Laboran dapat **mengunggah versi** SOP/IK: berkas, nomor revisi, tanggal efektif, bagian yang diubah, ringkasan dan alasan perubahan. Versi lalu disahkan lewat KF-01–KF-04 | Laboran | `labfik.document.version` | S2, Bukti 2 | E | W |
| KF-12 | Laboran dapat mencatat **distribusi** versi berlaku ke lokasi penggunaan (ruang lab) | Laboran | `labfik.document.distribution` | S4, Bukti 3 | E | W |
| KF-13 | Laboran dapat mencatat **sosialisasi** versi berlaku beserta pesertanya | Laboran | `labfik.document.socialization` | S5, Bukti 3 | E | W |
| KF-14 | Laboran atau KaLab dapat mencatat **tinjau ulang** versi berlaku dengan hasil *tetap berlaku* atau *perlu revisi* | Laboran, KaLab | `labfik.document.review` | S3, ISO 8.3.2b | E | W |
| KF-15 | Sistem menghitung **tanggal tinjau berikutnya** dari tanggal sah atau tinjau ulang terakhir ditambah siklus tinjau, lalu menandai versi yang lewat tanggal sebagai *perlu ditinjau* | Sistem | `labfik.document.version` | S3 | H | W |
| KF-16 | KaLab dan Laboran dapat melihat **Daftar Induk Dokumen** dan **riwayat revisi** per dokumen | KaLab, Laboran | [R] | Bukti 1, 3 | E | W |
| KF-17 | Pengguna Lab dapat **mencari dan membaca** SOP/IK versi berlaku. Versi lama dan draf tidak tampil bagi Pengguna Lab | Pengguna Lab | `labfik.document` | "dapat diakses pengguna" (target PKG-02) | E | O |
| KF-18 | Sistem hanya mengizinkan **satu versi dalam proses** (draf atau diajukan) per Dokumen Induk | Sistem | `labfik.document.version` | ISO 8.3.2c | H | O |

Catatan: S4 (tersedia di titik penggunaan) dibuktikan oleh KF-12, bukan KF-17. Karena itu KF-17 cukup di lapis Pelengkap. Siklus tinjau ulang disimpan per Dokumen Induk, bukan sebagai pengaturan modul. Dengan begitu nilainya **transien** (bisa berubah per dokumen) tanpa layar pengaturan (§4.7.5).

### C. Struktur organisasi (PKG-03)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-19 | KaLab dapat mengelola **Personel**: orang internal FIK yang berperan di lab (dosen, laboran/PLP, teknisi, asisten, petugas K3) dan pejabat penanda tangan tanpa akun, dengan jenis dan unit/prodi | KaLab | `hr.employee` (diperluas) | Master bersama | E | W |
| KF-20 | KaLab dapat mengelola **Jabatan**: unit, atasan (garis instruksi), jabatan pengganti, daftar tugas, dan daftar wewenang (tindakan × jenis dokumen) | KaLab | `hr.job` (diperluas), `labfik.jabatan.tugas`, `labfik.jabatan.wewenang` | K2, Bukti 3 | E | W |
| KF-21 | KaLab dapat menyusun **SK penetapan pengelola** berperiode, berisi baris penetapan personel × jabatan (dan ruang bila ada). SK lalu disahkan lewat KF-01–KF-04 | KaLab | `labfik.assignment` | K1, Bukti 1 | E | W |
| KF-22 | KaLab dapat mencatat **rapat koordinasi**: tanggal, agenda, peserta, keputusan, notulen | KaLab | `labfik.meeting` | K3, Bukti 5 | E | W |
| KF-23 | KaLab dapat mencatat **evaluasi struktur** (temuan beban kerja, efektivitas koordinasi, keputusan) dan menautkannya ke SK atau jabatan yang direvisi | KaLab | `labfik.org.evaluation` | K4 | E | W |
| KF-24 | KaLab dapat melihat **bagan organisasi** sebagai daftar hierarki jabatan (garis instruksi) beserta uraian tugas per jabatan | KaLab | [R] | Bukti 2, 3 | E | W |
| KF-25 | KaLab dapat melihat **matriks kewenangan** (jabatan × wewenang) | KaLab | [R] | Bukti 4 | E | W |
| KF-26 | KaLab dapat **menerbitkan SK** sebagai PDF mengikuti format SK fakultas (Lampiran I bagan, Lampiran II tugas) | KaLab | [R] | Bukti 1–3 | E | O |

### D. Rencana kerja tahunan (PKG-01)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-27 | KaLab dapat mengelola master **KPI**: definisi, rumus (pembilang, penyebut), satuan, frekuensi, sumber data/bukti | KaLab | `labfik.kpi` | Bukti 4 | E | W |
| KF-28 | KaLab dapat mencatat **Renstra lab** sebagai dokumen unggahan berperiode multi-tahun. Renstra disahkan lewat KF-01–KF-04 | KaLab | `labfik.renstra` | K1, Bukti 1 | E | W |
| KF-29 | KaLab dapat menyusun **rencana kerja tahunan** dengan item berisi kegiatan, KPI, target, satuan, PIC, jadwal, anggaran, dan rujukan Renstra institusi (teks) | KaLab | `labfik.plan` (jenis tahunan), `labfik.plan.line` | K2, Bukti 2, 4 | E | W |
| KF-30 | Sistem **memeriksa kelengkapan rencana** sebelum diajukan. Rencana tahunan: setiap item punya KPI, target, PIC, jadwal, anggaran, dan rujukan Renstra. Rencana pengembangan: ditambah keempat aspek gap terisi (atau dinyatakan "tidak ada gap" dengan alasan) dan setiap item menunjuk temuan gap serta punya nilai risiko dan manfaat | Sistem | `labfik.plan` | K2 PKG-01, K2 PKG-13 | H | W |
| KF-31 | PIC dapat mengisi **realisasi** item rencana per periode lapor: capaian, anggaran/biaya terpakai, status capaian, tindak lanjut, dan bukti. Dipakai rencana tahunan dan rencana pengembangan | Laboran, KaLab | `labfik.realisasi` | K3 PKG-01, K3 PKG-13 | E | W |
| KF-32 | KaLab dapat mencatat **tinjauan rencana** (tanggal, peserta, ringkasan capaian, keputusan) dan menautkan keputusan ke rencana periode berikutnya | KaLab | `labfik.tinjauan` | K4 PKG-01, K4 PKG-13 | E | W |
| KF-33 | KaLab dapat melihat **matriks keterkaitan** sebagai daftar item rencana per rujukan Renstra | KaLab | [R] | Bukti 3 | E | W |
| KF-34 | KaLab dapat melihat **laporan pelaksanaan** (target, capaian, status, tindak lanjut per item) untuk satu periode lapor | KaLab | [R] | Bukti 5 PKG-01, Bukti 5 PKG-13 | E | W |
| KF-35 | KaLab dapat **menerbitkan rencana kerja tahunan** sebagai PDF mengikuti format dokumen lab, untuk ditandatangani | KaLab | [R] | Bukti 2, 4 | E | W |
| KF-36 | KaLab dapat mengisi **narasi ringkas** rencana (ringkasan, latar belakang, tujuan, ruang lingkup) yang ikut tercetak di PDF | KaLab | `labfik.plan` | Format D1 | E | O |
| KF-37 | KaLab dapat membuat **revisi** dari rencana yang sudah disahkan. Rencana lama menjadi *diganti* (KF-08) dan riwayatnya tersimpan | KaLab | `labfik.plan` | K4 ("rencana diperbarui") | E | O |
| KF-38 | Sistem hanya mengizinkan **satu rencana berlaku** per jenis dan periode | Sistem | `labfik.plan` | K1 | H | O |

### E. Rencana pengembangan (PKG-13)

Rencana pengembangan memakai konsep rencana yang sama dengan PKG-01, dibedakan jenisnya. KF-28–KF-38 berlaku juga, kecuali yang khusus Renstra. Yang ditambahkan:

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-39 | KaLab dapat menyusun **rencana pengembangan** berisi temuan gap per aspek (tridharma, kompetensi, sarana, layanan: kondisi saat ini, kebutuhan/standar, sumber data, uraian gap, lampiran) dan item program yang menunjuk temuan gap, dengan nilai risiko, nilai manfaat, biaya, target, PIC, dan jadwal | KaLab | `labfik.plan` (jenis pengembangan), `labfik.plan.gap`, `labfik.plan.line` | K1–K2, Bukti 1, 2, 4 | E | W |
| KF-40 | Tinjauan rencana pengembangan memuat **ukuran manfaat** per item yang selesai: indikator manfaat, nilai sebelum, nilai sesudah, sumber | KaLab | `labfik.tinjauan` (anak ukuran manfaat) | K4 | E | W |
| KF-41 | KaLab dapat **menerbitkan rencana pengembangan** sebagai PDF dengan templat yang sama dengan rencana tahunan | KaLab | [R] | Bukti 1–4 | E | O |
| KF-42 | Sistem menghitung **prioritas** item (tinggi/sedang/rendah) dari nilai risiko × manfaat | Sistem | `labfik.plan.line` | K2 ("prioritas berbasis risiko/manfaat") | H | O |

Tanpa KF-42, prioritas diisi KaLab langsung di item, jadi K2 tetap terbukti.

### F. Status monev

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-43 | Sistem menghitung **persentase SOP wajib yang memenuhi** S1–S5, beserta daftar SOP yang tidak memenuhi dan cek yang gagal | Sistem | `labfik.document` | PKG-02 (otomatis) | H | W |
| KF-44 | Sistem menentukan **kriteria tertinggi yang lengkap secara data** (K1–K4) untuk PKG-01, 03, dan 13, beserta tautan ke rekaman buktinya | Sistem | `labfik.criteria.mixin` | PKG-01, 03, 13 (semi-otomatis) | H | W |
| KF-45 | KaLab dapat melihat **status monev** keempat indikator dan **menerbitkan laporan bukti** sebagai PDF untuk diserahkan ke penilai | KaLab | [R] | Semua | E | W |

Sesuai batasan masalah butir 4, sistem tidak menetapkan skor akhir PKG-01, 03, dan 13. Skor ditetapkan penilai dari bukti yang diserahkan.

**Ringkasan:** 45 KF. Lapis Inti (W): 36. Lapis Pelengkap (O): 9 (KF-09, 17, 18, 26, 36, 37, 38, 41, 42). *Evident*: 34. *Hidden*: 11 (KF-05, 07, 08, 09, 15, 18, 30, 38, 42, 43, 44).

---

## 3. Kebutuhan nonfungsional dan suplementer

Kebutuhan nonfungsional **logis** (aturan bisnis, misalnya "pengesah harus berwenang") tidak diulang di sini. Semuanya akan menjadi AB-xx di expanded use case (langkah 7), dengan KF di atas sebagai sumbernya.

| ID | Kebutuhan | Kategori ISO/IEC 25010 | Terikat ke |
|---|---|---|---|
| KNF-01 | Berjalan di **Odoo 17 Community**, tanpa OpenEduCat dan tanpa aplikasi Enterprise (mis. *Documents*). Addon `labfik_org` bergantung pada `labfik_core`, dan `labfik_core` bergantung pada `hr` dan `mail` | Kompatibilitas: koeksistensi | Seluruh sistem |
| KNF-02 | Perilaku bersama (pengesahan, dokumen terkendali, periode, kriteria, bukti) dirancang sekali sebagai **mixin** dan diwarisi model yang memakainya. Personel dan Jabatan **memperluas** `hr.employee` dan `hr.job`, tidak membuat model sendiri (arahan Pak Widi, 13–14 November 2026) | Pemeliharaan: modularitas, *reusability* | Seluruh sistem |
| KNF-03 | Master Personel, Jabatan, Ruang, Periode, dan mekanisme pengesahan dapat dipakai modul lain (SDM, Praktikum, Aset, Safety) tanpa disalin | Pemeliharaan: *reusability* | KF-01–09, 19–20 |
| KNF-04 | Hak akses berbasis grup Odoo (bagian 1) dan *record rule*. Pengguna Lab hanya membaca versi berlaku. Hanya KaLab yang bisa mengesahkan, mengembalikan, dan mencabut | Keamanan: kerahasiaan, integritas | KF-03–06, 17 |
| KNF-05 | Perubahan field penting pada dokumen (status, pengesah, berkas, isi item rencana) terlacak dengan `mail.thread` + *tracking*, di samping riwayat pengesahan KF-07 | Keamanan: akuntabilitas | KF-07 |
| KNF-06 | **Tanpa tanda tangan digital.** Keabsahan dibuktikan dengan PDF bertanda tangan manual, pengesah tercatat, dan pencatat | Keamanan: autentisitas, *non-repudiation* | KF-02, 04, 05 |
| KNF-07 | **Tanpa integrasi** dengan sistem kepegawaian, keuangan, SIAKAD, LeADS, atau SIMPEL. Data dari luar (Renstra institusi, anggaran, kebutuhan kurikulum) diinput manual atau dilampirkan | Kompatibilitas: interoperabilitas | Seluruh sistem |
| KNF-08 | Dokumen dan laporan diterbitkan sebagai **PDF (QWeb report)** yang meniru format dokumen lab (D1, D6), supaya bisa ditandatangani dan diunggah ke iso.upnvj | Portabilitas: *replaceability* | KF-16, 24–26, 33–35, 41, 45 |
| KNF-09 | Persentase PKG-02 dan kriteria tertinggi K1–K4 harus **sama dengan hitungan manual** pada skenario uji | Kesesuaian fungsional: ketepatan | KF-43, 44 |
| KNF-10 | Antarmuka berbahasa **Indonesia**, dengan istilah yang sama dengan instrumen monev (kriteria, bukti dukung, SOP wajib) | Usabilitas: *learnability* | Seluruh sistem |
| KNF-11 | Data uji dan *seed* **fiktif**. NIP/NIM tidak wajib diisi. Pilot memakai minimal satu dokumen nyata (1 SOP dan 1 draf struktur) | Kebebasan dari risiko | Seluruh sistem |

---

## 4. Keterlacakan

### 4.1 Masalah → tujuan → KF

| Masalah (brief, Bab I 1.2) | Tujuan (1.4) | KF |
|---|---|---|
| M1. SK pengelola, rencana kerja, dan rencana pengembangan belum disahkan; SOP ada tetapi nomor, tanggal efektif, dan pengesahannya tidak lengkap (A1, A2, A7, A10) | T1. Menuntun penyusunan dan pengesahan struktur, SOP, rencana kerja, dan rencana pengembangan | KF-01–05, 10–11, 19–21, 27–30, 35, 39 |
| M2. Kriteria "dijalankan" dan "dievaluasi" butuh rekaman kegiatan yang belum ada | T2. Rekaman realisasi, rapat, tinjauan, dan evaluasi yang tertaut ke dokumen asalnya | KF-12–14, 22–23, 31–32, 34, 40 |
| M3. Belum ada pengendalian dokumen (A2, A3, A4, A12) | T3. Pengendalian dokumen berversi dengan pengesah sesuai jabatan dan riwayat pengesahan | KF-05–09, 10–18 |
| M4. Status indikator dihitung manual dan tidak tertelusur ke buktinya | T4. Status monev yang tertaut ke bukti | KF-16, 24–25, 33, 43–45 |

### 4.2 Kriteria instrumen → KF (cek lantai)

Setiap kriteria punya kebutuhan pencatatan (rekaman bukti) dan kebutuhan pengecekan oleh sistem.

| Indikator | Kriteria | KF pencatatan | KF pengecekan |
|---|---|---|---|
| PKG-01 | K1 Renstra dan rencana tahunan disahkan, masih berlaku | KF-28, 29, 01–04 | KF-05, 44 (KF-09, 38 memperkuat) |
| | K2 Sasaran, KPI, target, PIC, jadwal, anggaran lengkap dan tertaut Renstra | KF-27, 29 | KF-30, 44 |
| | K3 Realisasi dapat ditelusuri | KF-31 | KF-44 |
| | K4 Ditinjau, keputusan masuk rencana berikutnya | KF-32 (KF-37) | KF-44 |
| PKG-02 | S1 Terdaftar dengan dasar kebutuhan | KF-10 | KF-43 |
| | S2 Disahkan oleh jabatan berwenang | KF-11, 01–04 | KF-05, 08, 43 |
| | S3 Mutakhir | KF-14 | KF-15, 43 |
| | S4 Tersedia di titik penggunaan | KF-12 | KF-43 |
| | S5 Disosialisasikan | KF-13 | KF-43 |
| PKG-03 | K1 Struktur dan pengangkatan disahkan | KF-19, 21, 01–04 | KF-05, 44 |
| | K2 Tugas, kewenangan, alur pelaporan, pengganti lengkap | KF-20 | KF-44 |
| | K3 Penugasan dan koordinasi mengikuti struktur | KF-22 | KF-44 |
| | K4 Dievaluasi, struktur diperbaiki | KF-23 | KF-44 |
| PKG-13 | K1 Analisis kebutuhan dan rencana pengembangan disahkan | KF-39, 01–04 | KF-05, 44 |
| | K2 Gap, prioritas, biaya, target, PIC lengkap | KF-39 (KF-42) | KF-30, 44 |
| | K3 Program berjalan, realisasi tertelusur | KF-31 | KF-44 |
| | K4 Manfaat diukur, rencana diperbarui | KF-32, 40 (KF-37) | KF-44 |

Semua kriteria terpenuhi oleh KF lapis Inti. KF Pelengkap di dalam tanda kurung hanya memperkuat.

PKG-03 K3 hanya dibuktikan dengan rapat koordinasi. Pengecekan penugasan dan presensi petugas terhadap jabatan (opsional di analisis) bergantung pada SDM (PKG-04) dan Praktikum (PKG-18), jadi tidak ditulis sebagai KF.

### 4.3 Cakupan rancangan di brief → KF

| Area | Inti | Pelengkap |
|---|---|---|
| Pengesahan | KF-01–08 | KF-09 |
| PKG-02 SOP/IK | KF-10–16 | KF-17, 18 |
| PKG-03 Struktur | KF-19–25 | KF-26 |
| PKG-01 Rencana | KF-27–35 | KF-36, 37, 38 |
| PKG-13 Pengembangan | KF-39, 40 (+ KF-29–34 bersama) | KF-41, 42 |
| Status monev | KF-43–45 | — |

Tidak ada KF di luar tabel cakupan brief.

---

## 5. Yang tidak ditulis sebagai kebutuhan

Mengikuti batasan masalah butir 5 di brief (saran pengembangan):

| Hal | Alasan tidak dirancang |
|---|---|
| Form Renstra lengkap (visi, misi, sasaran, program, baseline) dan master sasaran Renstra institusi | Renstra berlaku 5 tahun, cukup diunggah. Rujukan Renstra cukup teks di item rencana |
| Dokumen IKU tersendiri | Definisi KPI masuk master KPI, target masuk item rencana. Instrumen tidak meminta dokumen terpisah |
| Penarikan pengajuan oleh penyusun | Bisa diganti dengan meminta KaLab mengembalikan (KF-03) |
| Pengaturan modul (tahap pemeriksaan, siklus tinjau standar) | Tahap pemeriksaan dihapus. Siklus tinjau disimpan per Dokumen Induk (KF-10) |
| Pengingat terjadwal (tinjau ulang, realisasi) | Penandanya dihitung dari data (KF-15, KF-44) |
| Bagan organisasi visual dan garis koordinasi antarjabatan | Cukup daftar hierarki (KF-24). Koordinasi dibuktikan lewat rapat (KF-22) |
| Grafik tren status monev antarperiode | Tidak dibutuhkan kriteria mana pun |
| Penarikan data gap otomatis dari SDM, Aset, dan status monev | Modul sumbernya belum ada. Gap diisi manual (KF-39) |
| Tahap pemeriksaan terpisah | Pemeriksaan menyatu dengan pengesahan (keputusan 14 November 2026) |
| Akses penilai monev, aktor Dekan | Keduanya bukan aktor (bagian 1) |

---

## 6. Perubahan dibanding versi sebelumnya

Versi sebelumnya ada di tag `rancangan-tatkel-v1` (13 November 2026, KF-01 s.d. KF-43, versi rancangan lengkap). Dokumen ini **disusun ulang dengan penomoran baru**. Nomor KF versi lama tidak berlaku lagi dan tidak dipetakan satu lawan satu.

| Versi lama | Versi ini | Alasan |
|---|---|---|
| Aktor Dekan, Pemeriksa, Penilai Monev, Admin | Dihapus | Dekan tidak login, pemeriksaan menyatu dengan pengesahan, penilai menerima PDF, admin bukan peran domain (keputusan 14 November 2026) |
| Personel termasuk pihak eksternal, model `labfik.personel` | Personel = `hr.employee` diperluas, hanya orang internal FIK | Keputusan 14 November 2026 |
| Status *Diperiksa* dan pengaturan tahap pemeriksaan (KF-31, KF-32 lama) | Dihapus | Satu jalur pengesahan |
| Tarik pengajuan (KF-39 lama) | Dihapus | Bagian 5 |
| Pengingat tinjau ulang dan realisasi (KF-15, KF-43 lama) | Dihapus | Prinsip "hitung, bukan jadwalkan" |
| Master Sasaran Renstra, form Renstra, IKU (KF-19, 20, 22 lama) | Dihapus. Renstra menjadi dokumen unggahan (KF-28) | Keputusan 14 November 2026 |
| Matriks Renstra × RKT × ISO (KF-30 lama) | Daftar item per rujukan Renstra (KF-33) | Rujukan Renstra berupa teks |
| Kedaluwarsa otomatis wajib (KF-42 lama) | Pelengkap (KF-09) | "Masih berlaku" dapat dihitung dari periode |
| Akses penilai (KF-37 lama) | Laporan bukti diterbitkan KaLab (KF-45) | Penilai bukan aktor |
| — | Ditambah: penolakan pengesahan otomatis dipisah (KF-05), cek kelengkapan rencana dirinci per jenis (KF-30), laporan pelaksanaan untuk PKG-13 (KF-34), tanda *evident/hidden* | Keterlacakan ke kriteria dan §4.7.2 |

---

## 7. Temuan untuk langkah berikutnya

- **Langkah 5 (proses bisnis).** Activity yang nontrivial: (a) pengesahan dokumen, multi-aktor dengan kegiatan manual tanda tangan di luar sistem, dipanggil sebagai «call behavior»; (b) siklus SOP/IK: unggah versi → sahkan → distribusi → sosialisasi → tinjau ulang; (c) siklus rencana: susun → sahkan → realisasi → tinjauan → rencana berikutnya (dipakai PKG-01 dan PKG-13); (d) penetapan dan evaluasi struktur. State machine: dokumen yang disahkan (draf → diajukan → berlaku → diganti/dicabut/kedaluwarsa) dan versi SOP (perlu ditinjau).
- **Langkah 6 (use case).** Master Personel, Jabatan, KPI, dan Dokumen Induk adalah kandidat «CRUDL». KF-16, 24, 25, 33, 34, 45 adalah kandidat «report». "Terbitkan" (KF-26, 35, 41) harus dinilai apakah *essential* (§4.3.4).
- **Langkah 7 (aturan bisnis).** Kandidat AB dari KF hidden: KF-05, 08, 15, 18, 30, 38, 42, 43, 44. KF-07 (riwayat) dan KF-09 (penjadwal) adalah perilaku sistem, bukan aturan.

## 8. Isu terbuka

- [ ] Sistem melayani **satu lab FIK** atau **per lab prodi**? Memengaruhi jumlah KaLab, unit jabatan, dan pembagi PKG-02 (A9, A11) **[KONFIRMASI KaLab]**. Sementara: satu lab FIK, jabatan dibedakan per unit **[ASUMSI]**.
- [ ] SK pengelola disusun lewat sistem lalu diterbitkan (KF-26 menjadi Inti), atau cukup diunggah? **[KONFIRMASI KaLab]**
- [ ] Dokumen mana yang disahkan KaLab dan mana yang ditandatangani Dekan? Ini isi awal wewenang jabatan (KF-20) **[KONFIRMASI KaLab]**
- [ ] Periode lapor realisasi per triwulan atau per semester? SK SOTK mewajibkan KaLab melapor tiap semester (A6) **[KONFIRMASI KaLab]**
- [x] Asisten lab dicatat sebagai `hr.employee` dengan jenis personel *asisten* dan jabatan (`hr.job`) **Asisten Praktikum** (KF-19). Keputusan Febriyan, 14 November 2026
