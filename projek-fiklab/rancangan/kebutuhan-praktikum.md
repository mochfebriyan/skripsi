# Kebutuhan Sistem Modul Pelaksanaan Praktikum

14 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Bahan kerja Langkah 4 (bahan Bab II 2.2). Dasar untuk proses bisnis, use case, SSD, dan class diagram (Langkah 5–10).

Sumber:
- [brief-praktikum.md](../brief/brief-praktikum.md): masalah M1–M6, cakupan rancangan (Inti/Pelengkap), batasan, kontrak Core.
- Analisis PKG: [15](../analisis/analisis-data-persiapan-15.md), [16](../analisis/analisis-data-persiapan-16.md), [17](../analisis/analisis-data-persiapan-17.md), [18](../analisis/analisis-data-proses-18.md), [19](../analisis/analisis-data-evaluasi-19.md), [20](../analisis/analisis-data-evaluasi-20.md): aturan "memenuhi" (C, S, B, P, K).
- [bedah-dokumen-praktikum.md](../analisis/bedah-dokumen-praktikum.md): pelaku, field, dan model.

## Aturan yang dipakai (Wazlawick 2024)

| Aturan | Penerapan di dokumen ini |
|---|---|
| §4.2 Aktor sistem adalah peran (orang atau sistem luar) yang berinteraksi lewat *use case*; aktor tidak sama dengan profil keamanan | Aktor diturunkan dari pelaku *worker*/*actor* di studi dokumen bagian 2. Grup akses ditulis terpisah sebagai usulan |
| §4.2 Sistem luar menjadi aktor hanya bila berinteraksi langsung dengan sistem | SIAKAD, LeADS, SIMPEL **bukan aktor**: tidak ada pertukaran data langsung (impor berkas dan tautan saja) |
| §4.7 Setiap kebutuhan dapat ditelusuri ke asalnya | Kolom "Kriteria" merujuk kriteria instrumen; bagian 4 menelusuri masalah → tujuan → KF |
| §4.7.2 Kebutuhan fungsional *evident* (diketahui pengguna) dan *hidden* (dijalankan sistem) | Kolom "Jenis": **E** = *evident*, **H** = *hidden*. Kebutuhan H tidak menjadi *use case* sendiri; ditempelkan ke *use case* pemicunya di Langkah 6 |
| §4.7.3–4.7.4 Kebutuhan nonfungsional *logical* (aturan bisnis) dan *technological*; kebutuhan suplementer berlaku untuk seluruh sistem | Aturan bisnis rinci ditulis sebagai AB-PRK di Langkah 7. Bagian 3 hanya memuat kebutuhan nonfungsional dan suplementer |
| §4.7.5 Kebutuhan *permanent* vs *transient* | Ambang dan kebijakan yang mungkin berubah dijadikan **pengaturan** (KNF-PRK-12); aturan dari bunyi instrumen dianggap permanen |
| §4.7.6 Wajib vs diinginkan | **W** = lapis Inti (tanpa ini ada kriteria instrumen yang tidak terbukti); **O** = lapis Pelengkap (CLAUDE.md bagian 1) |
| §4.7.7 Kebutuhan suplementer dikelompokkan menurut ISO/IEC 25010, tanpa mengisi kategori yang tidak dibutuhkan | Kolom "Kategori 25010" di bagian 3 |

---

## 1. Aktor

| Aktor | Siapa (Jabatan) | Peran utama di sistem | Grup akses (usulan) |
|---|---|---|---|
| **KaLab** | Kepala Laboratorium | **Mengesahkan** Penetapan Jadwal, **menyetujui** pemakaian lab dan perubahan sesi, menyusun dan menetapkan survei, mengisi evaluasi survei, menerbitkan laporan bukti | `labfik_kalab` |
| **Laboran** | Laboran/PLP, Teknisi | Mengelola Mata Kuliah dan Kelas, membangkitkan Sesi, menyusun dan mengajukan Penetapan Jadwal, memeriksa kesiapan, hadir dan mengisi jurnal bila bertugas | `labfik_laboran` |
| **Dosen** | Dosen (koordinator, kelas, tandem) | Menerbitkan Versi Modul beserta rubrik, daftar *software*, dan daftar bahan; menyetujui substitusi bahan; mengisi jurnal dan catatan penilaian bila bertugas | `labfik_dosen` |
| **Asisten** | Asisten Praktikum (`hr.employee` dengan jabatan Asisten Praktikum) | Mengisi jurnal sesi dan catatan penilaian; mengajukan perubahan sesi | `labfik_asisten` |
| ***Pengisi Jurnal*** (abstrak) | Asisten yang bertugas; untuk kelas tanpa asisten, **dosen yang mengajar** kelas itu **[ASUMSI dari keterangan Herrens, 14 Nov 2026; KONFIRMASI wawancara P10, P13]** | Mengisi Jurnal Sesi, presensi petugas, *log book*, dan catatan penilaian | — (generalisasi di Langkah 6) |
| **Pengguna Lab** | Dosen, peneliti, atau unit yang memakai ruang di luar praktikum | Mengajukan Rencana Pemakaian Lab | `labfik_pengguna` |
| **Responden** | Praktikan, dosen, asisten (sesuai populasi survei) | Mengisi survei kepuasan lewat tautan, tanpa nama | Publik (tautan survei bawaan addon `survey`) |
| **Admin** | Pengelola sistem | Mengelola pengaturan dan grup akses | `labfik_admin` |

Catatan:
- **Penilai monev bukan aktor sistem**, mengikuti keputusan Tata Kelola: penilai menerima bukti dalam bentuk PDF yang diterbitkan sistem (KF-PRK-37).
- **Tidak ada aktor Penjadwal.** Tidak ada kebutuhan yang dipicu waktu; status yang bergantung pada waktu (misalnya periode tertutup, jurnal terlambat) **dihitung** saat dibuka, bukan dijadwalkan (prinsip "hitung, bukan jadwalkan").
- Koordinator Prodi, Wakil Dekan, Dekan, Tata Usaha, SIAKAD, LeADS, dan SIMPEL berada di luar batas sistem (studi dokumen bagian 2).

---

## 2. Kebutuhan fungsional

**Kolom:** Jenis E = *evident*, H = *hidden* (§4.7.2) · Prio W = Inti, O = Pelengkap (§4.7.6).

### A. Jadwal dan Sesi (PKG-15)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-01 | Laboran dapat mengelola **Mata Kuliah** (kode unik, nama, prodi, semester) dan **Kelas** per periode (nama, jumlah mahasiswa, dosen koordinator, dosen kelas) | Laboran | `labfik.mata.kuliah`, `labfik.kelas` (Core) | PKG-15 C3, pembagi 15–19 | E | W |
| KF-PRK-02 | Laboran dapat **mengimpor** Mata Kuliah dan Kelas dari berkas alokasi per periode, dengan kode MK sebagai kunci | Laboran | Core | — (mempercepat KF-PRK-01) | E | O |
| KF-PRK-03 | Laboran dapat **membangkitkan Sesi** bertanggal untuk satu kelas dari pola mingguan (hari, jam mulai–selesai, ruang), tanggal mulai, dan jumlah pertemuan dalam periode; pertemuan UTS dan UAS dilewati | Laboran | `labfik.sesi` (Core) | PKG-15 pembagi, PKG-18 pembagi | E | W |
| KF-PRK-04 | Sistem **menolak** Sesi atau pemakaian lab yang tumpang tindih ruang dan waktu dengan Sesi lain atau pemakaian yang disetujui, dan menyebutkan bentroknya | Sistem | `labfik.sesi`, `labfik.praktikum.pemakaian` | PKG-15 C2 | H | W |
| KF-PRK-05 | Sistem **memperingatkan** bila jumlah mahasiswa kelas melebihi kapasitas ruang Sesi, dan menandai Sesi itu tidak memenuhi C3 | Sistem | `labfik.sesi` | PKG-15 C3 | H | W |
| KF-PRK-06 | Laboran dapat menyusun **Penetapan Jadwal** periode dan mengajukannya; KaLab mengunggah PDF jadwal bertanda tangan lalu **mengesahkannya** (wewenang `mengesahkan`, `jadwal_praktikum` dipegang Jabatan KaLab **[ASUMSI dari keterangan Herrens; KONFIRMASI P5]**); saat disahkan, tanggal publikasi tercatat dan Sesi periode itu ditandai terpublikasi | Laboran, KaLab | `labfik.praktikum.jadwal` (+ `labfik.approval.mixin`) | PKG-15 C1, bukti 4 | E | W |
| KF-PRK-07 | Sistem dapat **mengekspor jadwal periode ke PDF** untuk ditandatangani | KaLab | [R] QWeb | PKG-15 C1 | E | W |
| KF-PRK-08 | Pengguna Lab dapat **mengajukan pemakaian lab** di luar praktikum (jenis kegiatan, ruang, tanggal, jam, keperluan) | Pengguna Lab | `labfik.praktikum.pemakaian` | PKG-15 bukti 1–2 | E | W |
| KF-PRK-09 | KaLab (penyetuju yang ditetapkan, keputusan Herrens 14 Nov 2026) dapat **menyetujui atau menolak** pemakaian lab dengan alasan; penolakan karena bentrok tercatat sebagai rekaman konflik | KaLab | `labfik.praktikum.pemakaian` | PKG-15 bukti 2, 5 | E | W |
| KF-PRK-10 | Sistem menampilkan **jadwal terpadu** per ruang: Sesi dan pemakaian yang disetujui | KaLab, Laboran, Dosen, Asisten | [R] | PKG-15 bukti 1 | E | W |
| KF-PRK-11 | Sistem menampilkan **rekaman konflik jadwal**: tumpang tindih yang terdeteksi dan penyelesaiannya | KaLab | [R] | PKG-15 bukti 5 | E | W |

### B. Versi Modul (PKG-15, dipakai 16, 17, 19)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-12 | Dosen dapat **menerbitkan Versi Modul** per MK per periode: berkas atau tautan modul, nomor versi, berkas rubrik, daftar *software* (nama, versi minimal, bebas/berbayar), dan daftar bahan per pertemuan (nama, jumlah) | Dosen | `labfik.praktikum.modul` (+ `labfik.controlled.mixin`) | PKG-15 C4; PKG-16 S3; PKG-17 B1; PKG-19 P2 | E | W |
| KF-PRK-13 | Sistem menjaga **satu versi berlaku** per MK per periode; saat versi baru terbit, versi lama berstatus *diganti* | Sistem | `labfik.praktikum.modul` | PKG-15 C4, ISO 7.2.1.3 | H | W |
| KF-PRK-14 | Dosen, Asisten, dan Laboran dapat **membuka Versi Modul berlaku** untuk MK yang diampu atau diasistensi sebelum sesi | Dosen, Asisten, Laboran | `labfik.praktikum.modul` | PKG-15 C4 ("dapat diakses") | E | W |

Akses modul oleh praktikan: **lewat LeADS UPNVJ** (keterangan Herrens, 14 Nov 2026), bukan lewat sistem lab. Versi Modul menyimpan tautan LeADS atau berkasnya; sistem lab tidak membagikan modul ke praktikan.

### C. Kesiapan alat, *software*, dan bahan (PKG-16, 17)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-15 | Laboran dapat mencatat **Pemeriksaan Kesiapan** untuk satu Sesi (per sesi, mengikuti bunyi instrumen; satuan lain menunggu P8) sebelum jam mulai: butir per kategori (PC/stasiun kerja, *software*, jaringan, listrik, proyektor/audio, bahan) dengan hasil baik / diperbaiki sebelum sesi / bermasalah, dan jumlah stasiun kerja berfungsi | Laboran | `labfik.praktikum.kesiapan` (+ `.butir`) | PKG-16 S1–S2 | E | W |
| KF-PRK-16 | Sistem **membuat butir *software* dan bahan otomatis** dari daftar di Versi Modul yang berlaku untuk Sesi itu | Sistem | `labfik.praktikum.kesiapan.butir` | PKG-16 S3, PKG-17 B1 | H | W |
| KF-PRK-17 | Laboran mencentang **lisensi sah** untuk *software* berbayar | Laboran | `labfik.praktikum.kesiapan.butir` | PKG-16 S3, bukti 4 | E | W |
| KF-PRK-18 | Laboran mencatat **keputusan** siap / siap setelah perbaikan / tunda; keputusan tunda membuka pengajuan Perubahan Sesi (KF-PRK-27) | Laboran | `labfik.praktikum.kesiapan` | PKG-16 S4, bukti 6 | E | W |
| KF-PRK-19 | Laboran mencatat butir **bahan**: jumlah tersedia, kondisi, berlabel, kedaluwarsa (bila relevan), dan **substitusi** (bahan pengganti, alasan) | Laboran | `labfik.praktikum.kesiapan.butir` | PKG-17 B2–B3 | E | W |
| KF-PRK-20 | Dosen pengampu kelas **menyetujui substitusi** bahan | Dosen | `labfik.praktikum.kesiapan.butir` | PKG-17 B3 | E | W |
| KF-PRK-21 | Sistem menampilkan **rekap kesiapan per ruang**: butir bermasalah per kategori dan keputusan tunda per periode | KaLab, Laboran | [R] | — (pemantauan) | E | O |

### D. Pelaksanaan sesi (PKG-18)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-22 | Pengisi Jurnal dapat mengisi **Jurnal Sesi** untuk satu Sesi: jam mulai dan selesai aktual, topik, Versi Modul yang dipakai, jumlah praktikan hadir, tautan presensi SIMPEL (opsional), kendala, foto. Identitas sesi (MK, kelas, tanggal, ruang, pertemuan) diambil dari Sesi, tidak diketik | Pengisi Jurnal | `labfik.praktikum.jurnal` | PKG-18 C1–C4, bukti 2, 4 | E | W |
| KF-PRK-23 | Pengisi Jurnal mencatat **presensi petugas**: dosen, asisten, laboran, dengan tingkat kehadiran penuh / sebagian / tidak hadir | Pengisi Jurnal | `labfik.praktikum.jurnal.petugas` | PKG-18 C5, bukti 3 | E | W |
| KF-PRK-24 | Pengisi Jurnal mencatat **entri *log book*** (waktu, uraian kegiatan) | Pengisi Jurnal | `labfik.praktikum.jurnal.logbook` | PKG-18 C5, bukti 5 | E | W |
| KF-PRK-25 | Pengisi Jurnal **mengirim** jurnal; sistem menolak bila jam selesai ≤ jam mulai, bila Sesi sudah punya jurnal terkirim, atau bila presensi dosen dan laboran belum diisi | Pengisi Jurnal, Sistem | `labfik.praktikum.jurnal` | PKG-18 C1, C3, C5 | E | W |
| KF-PRK-26 | Sistem **memperbarui status Sesi** dari jurnal terkirim, keputusan tunda, dan perubahan yang disetujui (nama status ditetapkan di state machine Langkah 5) | Sistem | `labfik.sesi` | PKG-18 C1–C2 | H | W |
| KF-PRK-27 | Pengisi Jurnal, Dosen, atau Laboran dapat **mengajukan Perubahan Sesi** (pindah jadwal, pindah ruang, daring, batal dan diganti) dengan alasan dan usulan waktu/ruang pengganti | Pengisi Jurnal, Dosen, Laboran | `labfik.praktikum.perubahan` | PKG-18 bukti 6–7 | E | W |
| KF-PRK-28 | KaLab (penyetuju yang ditetapkan, keputusan Herrens 14 Nov 2026) dapat **menyetujui atau menolak** Perubahan Sesi; bila disetujui dengan pengganti, sistem membangkitkan Sesi pengganti yang merujuk Sesi asal (dengan cek konflik KF-PRK-04) | KaLab | `labfik.praktikum.perubahan`, `labfik.sesi` | PKG-18 C2, bukti 6–7 | E | W |
| KF-PRK-29 | Sistem menampilkan **rekap keterlaksanaan per kelas** (sesi rencana, terlaksana, memenuhi) | KaLab, Laboran | [R] | — (pemantauan; menggantikan rekap manual) | E | O |
| KF-PRK-30 | Sistem **menandai jurnal terlambat** (dikirim lebih dari batas hari setelah sesi) | Sistem | `labfik.praktikum.jurnal` | ISO 7.5.1 | H | O |

### E. Penilaian individual (PKG-19)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-31 | Pengisi Jurnal dapat menambahkan **catatan penilaian** pada jurnal sesi asesmen: jenis asesmen, bentuk (individual / kelompok dengan komponen individual / kelompok saja), penilai, jumlah dinilai, jumlah lengkap, jumlah menerima umpan balik, jumlah perlu remediasi, jumlah diremediasi, tautan atau berkas bukti, catatan moderasi | Pengisi Jurnal | `labfik.praktikum.jurnal.penilaian` | PKG-19 P1–P4, bukti 2–5 | E | W |
| KF-PRK-32 | Sistem menampilkan **daftar kelas tanpa bukti penilaian** (tanpa sesi asesmen, sesi asesmen tanpa rubrik, atau remediasi tertunda) | KaLab | [R] | — (pemantauan) | E | O |

### F. Kepuasan pengguna (PKG-20)

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-33 | KaLab dapat **menyusun survei** periode di addon `survey`: periode, jenis responden, jumlah populasi, target *response rate*, tanggal buka–tutup, butir skala dan butir terbuka; setiap butir skala diberi salah satu dari **enam aspek** | KaLab | `survey.survey`, `survey.question` (*extend*) | PKG-20 K1–K2 | E | W |
| KF-PRK-34 | KaLab **menetapkan** survei sebelum tanggal buka; sistem menolak bila ada aspek tanpa butir, tidak ada butir terbuka, atau target respons kosong | KaLab, Sistem | `survey.survey` | PKG-20 K1–K2 | E | W |
| KF-PRK-35 | Responden **mengisi survei tanpa nama** lewat tautan | Responden | `survey.user_input` (bawaan) | PKG-20 K3, bukti 5 | E | W |
| KF-PRK-36 | KaLab mencatat **Evaluasi Survei**: kesimpulan per aspek dan **Rencana Tindak Lanjut** (aspek, prioritas, tindakan, PIC, tenggat, status) | KaLab | `labfik.praktikum.evaluasi.survei` (+ `.rtl`) | PKG-20 K3–K4, bukti 4, 6 | E | W |
| KF-PRK-37 | KaLab memberi **penilaian efektivitas** setiap RTL berdasarkan perbandingan rerata aspek dengan survei periode berikutnya | KaLab | `labfik.praktikum.evaluasi.rtl` | PKG-20 K4 | E | W |
| KF-PRK-38 | Sistem menampilkan **rekap hasil per aspek** (responden, *response rate*, rerata per aspek dan per butir, jawaban terbuka) dan **perbandingan antarperiode** per aspek | KaLab | [R] | PKG-20 bukti 2–5, K3–K4 | E | W |

### G. Status monev dan bukti

| ID | Kebutuhan | Aktor | Model | Kriteria | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-PRK-39 | Sistem menghitung **persentase** PKG-15, 16, 17, 18 per periode beserta **daftar unit tidak memenuhi** dan cek yang gagal; PKG-17 dinyatakan N/A bila tidak ada sesi berbahan | Sistem | [R] | PKG-15 C1–C4, PKG-16 S1–S4, PKG-17 B1–B3, PKG-18 C1–C5 | H | W |
| KF-PRK-40 | Sistem menghitung **persentase pendekatan** PKG-19 (Σ lengkap ÷ Σ hadir pada sesi asesmen) | Sistem | [R] | PKG-19 | H | W |
| KF-PRK-41 | Sistem menampilkan **kriteria tertinggi K1–K4** PKG-20 yang lengkap secara data, dengan tautan bukti | Sistem | `labfik.criteria.mixin` | PKG-20 | H | W |
| KF-PRK-42 | KaLab dapat **menerbitkan laporan bukti** per indikator per periode sebagai PDF (ringkasan skor/kriteria, daftar unit, tautan rekaman) untuk diserahkan ke penilai | KaLab | [R] QWeb | Semua ("bukti dapat diverifikasi") | E | W |
| KF-PRK-43 | KaLab dapat mengatur **pengaturan modul**: ambang durasi minimal sesi, batas hari pengisian jurnal, sah tidaknya sesi daring | KaLab | Pengaturan | PKG-18 C3 | E | W |
| KF-PRK-44 | Sistem mencatat **jejak audit** perubahan field penting dan menolak penghapusan rekaman bukti | Sistem | `mail.thread`, `labfik.evidence.mixin` | Keterlacakan bukti | H | W |

**Jumlah:** 44 KF (39 W, 5 O). Lapis Pelengkap: KF-PRK-02, 21, 29, 30, 32. Tampilan grafik pada perbandingan antarperiode (KF-PRK-38) juga Pelengkap; daftarnya tetap W.

---

## 3. Kebutuhan nonfungsional dan suplementer

| ID | Kebutuhan | Jenis (§4.7.3–4.7.5) | Kategori 25010 (§4.7.7) |
|---|---|---|---|
| KNF-PRK-01 | Berjalan di **Odoo 17 Community**, `depends: ['labfik_core', 'survey']`, tanpa OpenEduCat dan tanpa addon Enterprise | Suplementer, teknologis | Compatibility |
| KNF-PRK-02 | Hak akses berbasis **grup Odoo** (bagian 1) dan *record rule*: dosen hanya menerbitkan modul MK yang diampu; asisten dan dosen hanya mengisi jurnal Sesi kelasnya; responden survei tanpa akun | Suplementer, teknologis | Security (confidentiality, integrity) |
| KNF-PRK-03 | **Tidak menyimpan data per praktikan** (presensi per nama, nilai); hanya jumlah dan tautan bukti | Suplementer, logis | Security (confidentiality) |
| KNF-PRK-04 | Survei **anonim**: respons tidak menyimpan identitas responden | Nonfungsional (KF-PRK-35) | Security (confidentiality) |
| KNF-PRK-05 | Identitas sesi (MK, kelas, tanggal, jam rencana, ruang, pertemuan) **tidak diketik ulang** oleh pengisi jurnal | Nonfungsional (KF-PRK-22) | Usability (user error protection) |
| KNF-PRK-06 | Validasi input mencegah jam tidak valid dan laporan ganda (studi dokumen A17) | Nonfungsional (KF-PRK-25) | Usability (user error protection) |
| KNF-PRK-07 | Rekaman bukti (jurnal terkirim, pemeriksaan, evaluasi) **tidak dapat dihapus**; perubahan tercatat | Suplementer | Security (accountability, nonrepudiation) |
| KNF-PRK-08 | Model memakai **inheritance**: *mixin* Core (`controlled`, `approval`, `evidence`, `criteria`) dan perluasan addon LGPL (`hr`, `survey`), sesuai arahan Pak Widi | Suplementer, teknologis | Maintainability (reusability, modularity) |
| KNF-PRK-09 | Modul lain (SDM, Aset) dapat merujuk Sesi tanpa menambah field ke `labfik.sesi` | Suplementer | Maintainability (modularity) **[KONFIRMASI kelompok]** |
| KNF-PRK-10 | **Tanpa integrasi** langsung dengan SIAKAD, LeADS, SIMPEL; data kelas lewat impor berkas, bukti lewat tautan | Suplementer | Compatibility (interoperability) |
| KNF-PRK-11 | Antarmuka berbahasa **Indonesia** | Suplementer | Usability |
| KNF-PRK-12 | Ambang durasi, batas hari pengisian jurnal, dan sah tidaknya sesi daring adalah **pengaturan** yang dapat diubah KaLab (*transient*). Enam aspek survei dan aturan kriteria mengikuti instrumen (*permanent*) | Nonfungsional | Portability (adaptability) |
| KNF-PRK-13 | Jadwal periode dan laporan bukti diekspor sebagai **PDF (QWeb)** | Suplementer, teknologis | Usability (operability) |
| KNF-PRK-14 | Jurnal sesi dapat diisi dari **peramban ponsel** (pengisi saat ini melapor lewat Google Form) | Suplementer, *desired* (§4.7.6) | Usability (operability) |
| KNF-PRK-15 | Data uji **fiktif**; data nyata hanya dikutip sebagai angka agregat | Suplementer | Security (confidentiality) |

---

## 4. Keterlacakan masalah → tujuan → kebutuhan

| Masalah (brief) | Tujuan | Kebutuhan |
|---|---|---|
| M1. Tidak ada jadwal sesi bertanggal yang ditetapkan; jam dan ruang diketik ulang; konflik tidak terdeteksi | T1. Jadwal sesi disahkan dan dipublikasikan sebelum sesi, dengan cek konflik dan kapasitas | KF-PRK-01–11, KNF-PRK-05 |
| M2. Modul tidak berversi dan tidak terbukti tersedia sebelum sesi | T2. Modul berversi yang menjadi acuan *software*, bahan, dan rubrik | KF-PRK-12–14 |
| M3. Kesiapan dicatat asisten sesudah sesi, tanpa keputusan tunda | T3. Pemeriksaan kesiapan oleh laboran sebelum sesi | KF-PRK-15–21 |
| M4. Pencatatan pelaksanaan untuk honor; kelas tanpa asisten tidak terekam; kualitas rekaman rendah | T4. Satu jurnal per sesi untuk semua kelas; perubahan sesi disetujui | KF-PRK-22–30, KNF-PRK-05–07 |
| M5. Bukti penilaian dan kepuasan tidak ada di lab | T5. Catatan penilaian per sesi asesmen; survei dan tindak lanjut per periode | KF-PRK-31–38 |
| M6. Status indikator dihitung manual dan tidak tertelusur | T6. Status monev tertaut ke bukti | KF-PRK-39–44 |

## 5. Keterlacakan kriteria instrumen → kebutuhan

Lantai rancangan: setiap kriteria punya kebutuhan dan rekaman bukti (CLAUDE.md bagian 1).

| PKG | Kriteria | Kebutuhan |
|---|---|---|
| 15 | C1 jadwal sah dan dipublikasikan | 06, 07 |
| 15 | C2 tanpa konflik (+ kegiatan lain tercatat) | 04, 08, 09, 10, 11 |
| 15 | C3 sesuai kapasitas | 01, 05 |
| 15 | C4 modul berlaku tersedia sebelum sesi | 12, 13, 14 |
| 16 | S1–S4 | 15, 16, 17, 18 |
| 17 | B1–B3 | 12, 16, 19, 20 |
| 18 | C1–C5 | 22–28, 43 |
| 19 | P1–P4 | 12 (rubrik), 31 |
| 20 | K1–K4 | 33–38 |
| Semua | Persentase / kriteria tertinggi / bukti | 39–42, 44 |

Kebutuhan *hidden* (H) yang tidak berdiri sebagai *use case* sendiri: KF-PRK-04, 05, 13, 16, 26, 30, 39, 40, 41, 44. Di Langkah 6 masing-masing ditempelkan ke *use case* pemicunya.

---

## 6. Pertanyaan terbuka

- [ ] Pengesah jadwal = KaLab **[ASUMSI]**; dipastikan lewat wawancara P5 (KF-PRK-06)
- [ ] Pengisi jurnal kelas tanpa asisten = dosen yang mengajar **[ASUMSI]**; dipastikan lewat wawancara P10, P13 (aktor Pengisi Jurnal)
- [ ] Pemeriksaan kesiapan per sesi (mengikuti instrumen) atau per ruang per hari? (KF-PRK-15; P8)
- [x] Penyetuju pemakaian lab dan perubahan sesi: **KaLab** (keputusan 14 Nov 2026)
- [x] Akses modul oleh praktikan: **lewat LeADS UPNVJ** (14 Nov 2026)
- [ ] Persentase pendekatan PKG-19: **dipakai sementara** (keputusan Herrens, 14 Nov 2026); tetap ditanyakan ke pembimbing (KF-PRK-40)
