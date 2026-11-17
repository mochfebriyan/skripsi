# Kebutuhan Sistem Modul SDM & Kompetensi

14 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 4 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). Bahan Bab II 2.2 Usulan Solusi, dan dasar untuk proses bisnis (langkah 5) dan use case (langkah 6). Dokumen ini bukan diagram, jadi tidak masuk 2.3 secara langsung.

Sumber:
- [brief-sdm.md](../brief/brief-sdm.md): masalah M1–M4, cakupan rancangan (Inti + Pelengkap), batasan masalah, keputusan 14 November 2026.
- [analisis PKG-04](../analisis/analisis-data-pengelolaan-4.md), [PKG-10](../analisis/analisis-data-pengelolaan-10.md), [PKG-14](../analisis/analisis-data-pengembangan-14.md): syarat S1–S4 dan K1–K4, luaran, entitas.
- [bedah-dokumen-sdm.md](../analisis/bedah-dokumen-sdm.md): temuan as-is A1–A21, field, laporan.
- [kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md): mixin Core, perluasan, isu K-1–K-6.

---

## 0. Aturan yang dipakai

Mengikuti Wazlawick (2024) bab 4.2 dan 4.7:

| Aturan | Bab | Penerapan di dokumen ini |
|---|---|---|
| Aktor adalah peran yang berinteraksi dengan sistem lewat *use case*, **bukan** profil keamanan | §4.2 | Grup akses hanya usulan. Pihak yang hanya menandatangani (Dekan, Wadek, Koor Prodi), asisten, dan penilai tidak berinteraksi dengan sistem, jadi bukan aktor |
| Kebutuhan fungsional **evident** (E) terjadi lewat antarmuka dengan sepengetahuan pengguna; **hidden** (H) dikerjakan sistem sebagai akibat fungsi lain | §4.7.2 | Kolom "Jenis". KF *hidden* tidak menjadi *use case* sendiri, tetapi dicatat pada *use case* pemicunya di langkah 6 |
| Nonfungsional terikat fungsi = **logis** (aturan bisnis) atau **teknologis**; yang berlaku untuk seluruh sistem = **suplementer** | §4.7.3, §4.7.4, §4.7.7 | Aturan bisnis ditulis sebagai `AB-SDM-nn` di langkah 7. Bagian 3 hanya memuat kebutuhan teknologis dan suplementer, dikelompokkan menurut ISO/IEC 25010 (Tabel 4–2) |
| Permanen atau transien | §4.7.5 | Nilai yang diperkirakan berubah (syarat kompetensi per jabatan, masa berlaku standar per tugas/alat) disimpan sebagai **data per rekaman**, bukan konstanta atau layar pengaturan |
| Wajib dan diinginkan | §4.7.6 | Prioritas **W** = lapis Inti, **O** = lapis Pelengkap ([brief, Cakupan rancangan](../brief/brief-sdm.md#cakupan-rancangan)) |
| Setiap kebutuhan tertelusur ke sumbernya | §4.7.1 | Kolom "Kriteria/bukti" dan tabel keterlacakan di bagian 4 |
| Jangan mencari kebutuhan suplementer yang tidak ada hanya untuk mengisi kategori | §4.7.7 | Bagian 3 hanya memuat kategori ISO 25010 yang benar-benar relevan |

Kebutuhan di luar cakupan brief **tidak** ditulis sebagai KF. Daftarnya ada di bagian 5.

---

## 1. Aktor

| Aktor | Siapa | Peran utama di sistem | Grup akses (usulan, dari Core) |
|---|---|---|---|
| **KaLab** | Kepala Laboratorium (slide PKKMB: satu per prodi) | Mengelola master Kompetensi dan Tugas/Alat; menetapkan syarat kompetensi jabatan, kebutuhan petugas, dan pelaksana tugas/alat; menyusun Rencana Pelatihan; **satu-satunya pencatat pengesahan** (Surat Tugas, Otorisasi, Rencana Pelatihan); memantau status monev dan menerbitkan laporan bukti | `labfik_kalab` |
| **Laboran/PLP** | Laboran, PLP, teknisi | Mencatat hasil seleksi asisten, bukti kompetensi, asesmen keterampilan, evaluasi ulang otorisasi, realisasi pelatihan; menyusun draf Surat Tugas | `labfik_laboran` |

Grup berjenjang mengikuti Core: `labfik_kalab` ⊃ `labfik_laboran` ⊃ `labfik_pengguna` (kontrak Core K-4). Modul SDM **tidak** membutuhkan aktor Penjadwal: semua status berlaku dihitung dari tanggal saat dibaca (kontrak Core K-3).

**Bukan aktor:**

| Pihak | Alasan | Jejaknya di sistem |
|---|---|---|
| Dekan, Wadek Bidang Keuangan dan Umum, Koor Prodi | Hanya menandatangani dokumen cetak (keputusan kelompok, brief Tata Kelola) | Personel tanpa akun; tercatat sebagai **pengesah** atau **penyetuju pengecualian**. KaLab sebagai pencatat |
| Asisten praktikum | Tidak memakai sistem di proposal (brief, aktor) | Personel (`jenis_personel` = asisten, Jabatan = Asisten Praktikum), dibuat saat lulus seleksi |
| Calon asisten yang tidak lulus | Tidak dicatat (keputusan 14 Nov 2026) | Tidak ada |
| Dosen | Tidak dinilai di PKG-04/10/14 | Tidak ada di modul ini |
| Penilai monev | Menerima bukti berupa PDF | Tidak ada. Laporan bukti diterbitkan KaLab (KF-SDM-42) |

Catatan untuk langkah 6: KaLab dan Laboran sama-sama **mencatat** rekaman bukti (seleksi, bukti kompetensi, asesmen, realisasi). Kandidat aktor abstrak: *Pengelola Lab*, dengan KaLab dan Laboran sebagai turunannya, sama dengan usulan Tata Kelola.

---

## 2. Kebutuhan fungsional

Kolom:
- **Jenis:** E = *evident*, H = *hidden*.
- **Prio:** W = lapis Inti (tanpa ini ada kriteria yang tidak terbukti atau alur putus), O = lapis Pelengkap.
- **Model (usulan):** nama sementara dari kontrak Core bagian 1. Nama final di DCD (langkah 10).

### A. Kompetensi (dipakai ketiga indikator)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-01 | KaLab dapat mengelola master **Kompetensi**: nama, jenis (pendidikan/keahlian/sertifikasi/pelatihan fungsional), kode acuan opsional (mis. skema SKKNI) | KaLab | `labfik.sdm.kompetensi` | PKG-04 S3, PKG-10 S1, PKG-14 K1; ISO 6.2.2 | E | W |
| KF-SDM-02 | KaLab dapat menetapkan **Kompetensi wajib** per Jabatan. Untuk Asisten Praktikum hanya syarat umum; syarat per MK dicek lewat seleksi (KF-SDM-07) | KaLab | `hr.job` (+ `syarat_kompetensi_ids`) | PKG-04 S3, PKG-14 K1; ISO 6.2.2 | E | W |
| KF-SDM-03 | Pengelola lab dapat mencatat **Bukti Kompetensi** personel: kompetensi, jenis bukti (pendidikan/pelatihan/sertifikasi/pengalaman/demonstrasi), nomor dokumen, penerbit, tanggal, berlaku sampai (opsional), berkas | KaLab, Laboran | `labfik.sdm.bukti.kompetensi` | PKG-04 S3 dan bukti 4 | E | W |
| KF-SDM-04 | Sistem menentukan apakah sebuah bukti **masih berlaku** pada tanggal tertentu, dan apakah seorang personel **memenuhi seluruh Kompetensi wajib** jabatannya pada tanggal itu | Sistem | `labfik.sdm.bukti.kompetensi`, `hr.employee` | PKG-04 S3, PKG-14 K1 | H | W |
| KF-SDM-05 | KaLab dapat melihat **Matriks Kompetensi**: personel × Kompetensi wajib, dengan penanda dimiliki/berlaku/kurang | KaLab | [R] | PKG-04 bukti 3 | E | W |

### B. Pengesahan dokumen SDM (memakai mekanisme Core)

Satu jalur pengesahan untuk semua dokumen SDM: **ajukan → kembalikan atau sahkan → cabut**. Dipakai Surat Tugas, Otorisasi, dan Rencana Pelatihan. Mekanisme teknisnya `labfik.approval.mixin` dari Core.

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-06 | Pengelola lab dapat **mengajukan** dokumen SDM dan **mengunggah PDF bertanda tangan**; KaLab dapat **mengembalikan** dengan alasan, **mengesahkan** dengan mencatat pengesah dan tanggal sah, dan **mencabut** dokumen yang berlaku. Setiap kejadian tercatat di riwayat pengesahan | KaLab, Laboran | `labfik.approval.mixin`, `labfik.approval.log` (Core) | PKG-04 S2, PKG-10 S2, PKG-14 K1 | E | W |
| KF-SDM-43 | Sistem **menolak pengesahan** dokumen SDM bila pengesah tidak memegang jabatan yang berwenang mengesahkan jenis dokumen itu (`penugasan_petugas`, `otorisasi`, `rencana_pelatihan`) | Sistem | `hr.job.punya_wewenang()` (Core) + `selection_add` | PKG-04 S2 ("penugasan sah"), PKG-10 S2 | H | W |

KF-SDM-06 dan KF-SDM-43 adalah kebutuhan pengesahan milik modul SDM untuk tiga jenis dokumen SDM. Perilakunya diwarisi dari `labfik.approval.mixin` (Core); modul SDM hanya mengisi pemeriksaan kelengkapan dan penggantian dokumen per jenis ([kontrak-core-sdm.md](kontrak-core-sdm.md) bagian 5). Prosesnya digambar di activity A4 dan state machine S1/S4 ([proses-bisnis-sdm.md](proses-bisnis-sdm.md)).

### C. Penugasan petugas sesuai kompetensi (PKG-04)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-07 | Pengelola lab dapat mencatat **hasil seleksi asisten yang lulus** per mata kuliah dan periode: nilai MK, skor wawancara/simulasi/pengembangan modul, penilai, tanggal, keputusan (*lulus* / *lulus dengan pengecualian*), berkas berita acara dan KHS. Bila calon belum ada sebagai Personel, sistem membuatnya dengan `jenis_personel` = asisten dan Jabatan = Asisten Praktikum | KaLab, Laboran | `labfik.sdm.seleksi`, `hr.employee` | PKG-04 S4, bukti 5, 6 | E | W |
| KF-SDM-08 | Keputusan *lulus dengan pengecualian* wajib mencatat **alasan** dan **penyetuju** (Personel berjabatan berwenang) | KaLab | `labfik.sdm.seleksi` | PKG-04 S4 ("syarat internal"); masalah M1 | E | W |
| KF-SDM-09 | KaLab dapat menetapkan **Kebutuhan Petugas** per kelas per peran (asisten, laboran): jumlah minimal (boleh 0), dasar penetapan (teks), berkas formulir alokasi | KaLab | `labfik.sdm.kebutuhan.petugas` | PKG-04 S1; temuan A7 | E | W |
| KF-SDM-10 | Pengelola lab dapat menyusun **Surat Tugas** per periode berisi baris penugasan: asisten → kelas, laboran → ruang, masing-masing dengan `berlaku_mulai`/`berlaku_sampai`. Surat disahkan lewat KF-SDM-06 | KaLab, Laboran | `labfik.sdm.surat.tugas`, `labfik.sdm.penugasan` | PKG-04 S2, bukti 2; temuan A6, A10; kontrak K-6 | E | W |
| KF-SDM-11 | Sistem **memeriksa kelengkapan Surat Tugas** sebelum diajukan: ada minimal satu baris; setiap baris punya personel, peran, sasaran, dan rentang berlaku; setiap asisten punya hasil seleksi lulus (termasuk pengecualian) untuk MK kelas yang ditugaskan | Sistem | `labfik.sdm.surat.tugas` | PKG-04 S2, S4 | H | W |
| KF-SDM-12 | Sistem menentukan status **S1–S4 untuk setiap sesi terlaksana**: S1 kebutuhan kelas ditetapkan; S2 kebutuhan terisi baris Surat Tugas yang disahkan dan berlaku pada tanggal sesi (asisten lewat kelas, laboran lewat ruang sesi); S3 setiap petugas memenuhi Kompetensi wajib jabatannya pada tanggal sesi; S4 setiap asisten punya seleksi lulus untuk MK itu. Lalu menghitung **persentase** sesi memenuhi per periode | Sistem | `labfik.sdm.monev` | PKG-04 (otomatis) | H | W |
| KF-SDM-13 | KaLab dapat melihat **Daftar Sesi dan Petugas** per periode: sesi, kebutuhan, petugas, status S1–S4, dan syarat yang gagal | KaLab | [R] | PKG-04 bukti 1 | E | W |
| KF-SDM-14 | KaLab dapat membuat **revisi Surat Tugas** untuk pengganti di tengah semester; surat lama menjadi *diganti* dan riwayatnya tersimpan | KaLab | `labfik.sdm.surat.tugas` | PKG-04 S2 (pengganti) | E | O |
| KF-SDM-15 | Pengelola lab dapat melampirkan **pernyataan komitmen** petugas pada Surat Tugas | KaLab, Laboran | `labfik.sdm.surat.tugas` | Sheet ID 4 ("Komitmen Petugas Praktikum") | E | O |
| KF-SDM-16 | Pengelola lab dapat mencatat **orientasi atau supervisi** petugas baru: jenis, personel, pelaksana, tanggal, catatan, bukti | KaLab, Laboran | `labfik.sdm.orientasi` | PKG-04 bukti 7 (rekaman pendukung) | E | O |
| KF-SDM-17 | KaLab dapat **menerbitkan Surat Tugas** sebagai PDF untuk ditandatangani | KaLab | [R] | PKG-04 bukti 2 | E | O |

Status "sesi terlaksana" (penyebut) dibaca dari `state` Sesi di Core yang diisi PKG-18. Bila belum ada, sesi terjadwal yang tanggalnya sudah lewat dianggap terlaksana **[ASUMSI]** (analisis PKG-04 bagian 6).

### D. Otorisasi personel (PKG-10)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-18 | KaLab dapat mengelola master **Tugas/Alat Berkewenangan Khusus**: nama, jenis (tugas/alat/*software*), nama alat atau ruang (teks), Kompetensi yang disyaratkan, masa berlaku standar otorisasi (bulan) | KaLab | `labfik.sdm.tugas.khusus` | PKG-10 bukti 1; temuan A21 | E | W |
| KF-SDM-19 | KaLab dapat menetapkan **pelaksana** setiap tugas/alat, yaitu PLP/laboran yang menjalankannya. Pasangan pelaksana × tugas/alat menjadi **penyebut** PKG-10, sudah berizin atau belum **[USULAN PENULIS; KONFIRMASI pengguna]** | KaLab | `labfik.sdm.tugas.khusus` (daftar pelaksana) | PKG-10 penyebut ("pasangan yang memerlukan otorisasi dan aktif") | E | W |
| KF-SDM-20 | Pengelola lab dapat mencatat **Asesmen Keterampilan**: personel, tugas/alat, penilai, metode (demonstrasi/uji praktik/tinjauan sertifikat), skor, unsur kritis terpenuhi, kesimpulan (*layak*/*belum layak*), catatan pengembangan, berkas | KaLab, Laboran | `labfik.sdm.asesmen` | PKG-10 S1, bukti 2 | E | W |
| KF-SDM-21 | Saat asesmen berkesimpulan *layak*, sistem membuat **Bukti Kompetensi** berjenis demonstrasi untuk Kompetensi yang disyaratkan tugas/alat itu | Sistem | `labfik.sdm.asesmen` → `labfik.sdm.bukti.kompetensi` | PKG-10 S1 | H | W |
| KF-SDM-22 | KaLab dapat menyusun **Otorisasi**: personel, tugas/alat, dasar (asesmen atau bukti kompetensi), lingkup dan pembatasan, level (*terbimbing*/*mandiri*), supervisor, `berlaku_mulai`/`berlaku_sampai` (awal terisi dari masa berlaku standar). Otorisasi disahkan lewat KF-SDM-06 | KaLab | `labfik.sdm.otorisasi` | PKG-10 S2, bukti 3 | E | W |
| KF-SDM-23 | Sistem **memeriksa kelengkapan Otorisasi** sebelum diajukan: personel punya asesmen *layak* atau Bukti Kompetensi berlaku untuk semua Kompetensi yang disyaratkan; lingkup terisi; bila *terbimbing*, supervisor wajib dan supervisor punya otorisasi *mandiri* berlaku untuk tugas/alat yang sama | Sistem | `labfik.sdm.otorisasi` | PKG-10 S1, S3 | H | W |
| KF-SDM-24 | Sistem menentukan apakah otorisasi **berlaku** pada tanggal tertentu dari masa berlakunya; saat otorisasi baru untuk pasangan yang sama disahkan, otorisasi lama otomatis menjadi *diganti* | Sistem | `labfik.sdm.otorisasi` (`_dokumen_diganti()`) | PKG-10 S2 | H | W |
| KF-SDM-25 | Pengelola lab dapat mencatat **Evaluasi Ulang Otorisasi**: otorisasi, pemicu (masa berlaku habis/alat atau metode berubah/insiden/lama tidak aktif/lainnya), tanggal, penilai, hasil, keputusan (diperpanjang/dibatasi/dinaikkan ke mandiri/dicabut), status (*terbuka*/*diputuskan*). Keputusan diperpanjang/dibatasi/dinaikkan diwujudkan dengan Otorisasi baru (KF-SDM-22); dicabut lewat KF-SDM-06 | KaLab, Laboran | `labfik.sdm.evaluasi.otorisasi` | PKG-10 S4, bukti 5 | E | W |
| KF-SDM-26 | Sistem menentukan status **S1–S4 untuk setiap pasangan pelaksana × tugas/alat** dan menghitung **persentase** pada tanggal acuan: S1 kompetensi terbukti; S2 otorisasi disahkan dan berlaku; S3 bila terbimbing, supervisor berwenang; S4 tidak ada evaluasi ulang *terbuka* | Sistem | `labfik.sdm.monev` | PKG-10 (otomatis) | H | W |
| KF-SDM-27 | KaLab dapat melihat **Daftar Operator Sah** per tugas/alat: personel, level, berlaku sampai | KaLab | [R] | PKG-10 bukti 3 | E | W |
| KF-SDM-28 | KaLab dapat mencatat **cara pembatasan akses** (dikunci/akun/diawasi/lainnya) dan berkas buktinya di master Tugas/Alat | KaLab | `labfik.sdm.tugas.khusus` | PKG-10 bukti 4 (rekaman pendukung) | E | O |

### E. Pelatihan PLP/laboran (PKG-14)

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-29 | KaLab dapat menyusun **Rencana Pelatihan** untuk satu periode tahunan, berisi **kebutuhan kompetensi** per PLP/laboran dan teknisi (gap, atau "tidak ada gap" dengan keterangan) | KaLab | `labfik.sdm.rencana.pelatihan` (anak kebutuhan) | PKG-14 K1, bukti 1 | E | W |
| KF-SDM-30 | Sistem **mengisi awal daftar kebutuhan** dari selisih Kompetensi wajib jabatan dan Bukti Kompetensi berlaku setiap PLP/laboran dan teknisi aktif; KaLab boleh menambah kebutuhan lain | Sistem | `labfik.sdm.rencana.pelatihan` | PKG-14 K1, bukti 1 | H | W |
| KF-SDM-31 | KaLab dapat menambah **item pelatihan**: Kompetensi sasaran, jenis (Diklatfung/bimtek/sertifikasi/internal), materi, peserta, penyelenggara, anggaran, jadwal, kriteria keberhasilan | KaLab | `labfik.sdm.rencana.pelatihan` (anak item) | PKG-14 K2, bukti 2 | E | W |
| KF-SDM-32 | Sistem **memeriksa kelengkapan Rencana Pelatihan** sebelum diajukan: setiap PLP/laboran dan teknisi aktif tercantum di kebutuhan; setiap item lengkap; Kompetensi sasaran item termasuk gap pesertanya. Saat diajukan, daftar kebutuhan **dibekukan** | Sistem | `labfik.sdm.rencana.pelatihan` (`_cek_kelengkapan()`, `_sebelum_ajukan()`) | PKG-14 K1, K2 | H | W |
| KF-SDM-33 | Pengelola lab dapat mencatat **Realisasi Pelatihan** per peserta per item: tanggal, penyelenggara, durasi jam, sertifikat, bukti praktik/demonstrasi pascapelatihan | KaLab, Laboran | `labfik.sdm.realisasi.pelatihan` | PKG-14 K3, bukti 3, 4 | E | W |
| KF-SDM-34 | Pengelola lab dapat mencatat **Evaluasi Efektivitas** per realisasi: metode (asesmen ulang/penilaian kinerja), skor sebelum dan sesudah, penilai, kesimpulan (*efektif*/*perlu pengembangan*), rekaman peningkatan layanan, tindak lanjut kebutuhan berikutnya | KaLab, Laboran | `labfik.sdm.evaluasi.pelatihan` | PKG-14 K4, bukti 5 | E | W |
| KF-SDM-35 | Saat evaluasi berkesimpulan *efektif*, sistem membuat **Bukti Kompetensi** berjenis pelatihan untuk Kompetensi sasaran item, dengan sertifikat realisasi sebagai berkas | Sistem | `labfik.sdm.evaluasi.pelatihan` → `labfik.sdm.bukti.kompetensi` | PKG-14 K4 ("kebutuhan berikutnya diperbarui") | H | W |
| KF-SDM-36 | Sistem menentukan **kriteria tertinggi yang lengkap secara data** (K1–K4) untuk Rencana Pelatihan periode itu, beserta tautan ke rekaman buktinya | Sistem | `labfik.criteria.mixin` (Core) | PKG-14 (semi-otomatis) | H | W |
| KF-SDM-37 | KaLab dapat menandai item pelatihan **batal** dengan alasan wajib; item batal tidak dihitung di K3 | KaLab | `labfik.sdm.rencana.pelatihan` | PKG-14 K3 (keputusan 14 Nov 2026) | E | O |
| KF-SDM-38 | KaLab dapat melihat **rekap pelatihan per personel** (rencana, realisasi, efektivitas) | KaLab | [R] | Pendukung PKG-14 | E | O |
| KF-SDM-39 | KaLab dapat **menerbitkan Rencana Pelatihan** sebagai PDF untuk ditandatangani | KaLab | [R] | PKG-14 bukti 2 | E | O |

### F. Status monev

| ID | Kebutuhan | Aktor | Model (usulan) | Kriteria/bukti | Jenis | Prio |
|---|---|---|---|---|---|---|
| KF-SDM-40 | KaLab dapat melihat **status monev** ketiga indikator pada tanggal acuan: persentase PKG-04 dan PKG-10 (dari KF-SDM-12, 26) dan kriteria tertinggi PKG-14 (KF-SDM-36), masing-masing dengan **daftar unit yang belum memenuhi** dan syarat yang gagal | KaLab | `labfik.sdm.monev` [R] | Semua | E | W |
| KF-SDM-41 | Sistem **menautkan** setiap unit (sesi, pasangan, kriteria) ke rekaman buktinya (surat tugas, seleksi, bukti kompetensi, otorisasi, asesmen, realisasi, evaluasi) | Sistem | `labfik.sdm.monev` | Masalah M4 (tertelusur ke bukti) | H | W |
| KF-SDM-42 | KaLab dapat **menerbitkan laporan bukti** ketiga indikator sebagai PDF untuk diserahkan ke penilai | KaLab | [R] | Semua | E | W |

Sesuai batasan masalah butir 5 di brief, sistem tidak menetapkan skor akhir PKG-14; skor ditetapkan penilai.

**Ringkasan:** 43 KF (KF-SDM-01 s.d. 43). KF-SDM-43 (penolakan pengesahan oleh sistem) ditempatkan di area B tetapi bernomor terakhir karena ditambahkan setelah penomoran; nomor lain tidak digeser (CLAUDE.md bagian 7). Lapis Inti (W): 35. Lapis Pelengkap (O): 8 (KF-SDM-14, 15, 16, 17, 28, 37, 38, 39). *Evident*: 30. *Hidden*: 13 (KF-SDM-04, 11, 12, 21, 23, 24, 26, 30, 32, 35, 36, 41, 43). Pembuatan Personel asisten di KF-SDM-07 adalah efek dari KF itu, bukan KF terpisah.

---

## 3. Kebutuhan nonfungsional dan suplementer

Kebutuhan nonfungsional **logis** (aturan bisnis, mis. "supervisor harus berotorisasi mandiri") tidak diulang di sini; semuanya menjadi `AB-SDM-nn` di langkah 7 dengan KF di atas sebagai sumbernya.

| ID | Kebutuhan | Kategori ISO/IEC 25010 | Terikat ke |
|---|---|---|---|
| KNF-SDM-01 | Berjalan di **Odoo 17 Community** sebagai addon `labfik_sdm` yang hanya bergantung pada `labfik_core`; tanpa OpenEduCat dan tanpa aplikasi Enterprise | Kompatibilitas: koeksistensi | Seluruh modul |
| KNF-SDM-02 | Core **tidak diubah**. Perilaku bersama diwarisi dari mixin Core (`approval`, `period`, `criteria`, `evidence`); `hr.job`, `hr.employee`, dan jenis dokumen wewenang **diperluas** dengan `_inherit`/`selection_add` (Wazlawick §4.7.1; arahan Pak Widi) | Pemeliharaan: modularitas, *reusability* | Seluruh modul |
| KNF-SDM-03 | Penugasan, Kompetensi, dan Bukti Kompetensi dapat dibaca modul lain (Praktikum PKG-18, opsional Tata Kelola PKG-13) tanpa disalin | Pemeliharaan: *reusability* | KF-SDM-03, 10 |
| KNF-SDM-04 | Hak akses memakai grup Core: Laboran mencatat; hanya KaLab yang menetapkan master, syarat, kebutuhan, pelaksana, dan mengesahkan/mengembalikan/mencabut. Berkas KHS dan nilai MK hanya terlihat oleh KaLab dan Laboran | Keamanan: kerahasiaan, integritas | KF-SDM-06, 07 |
| KNF-SDM-05 | Rekaman bukti (seleksi, bukti kompetensi, asesmen, evaluasi, realisasi) **tidak dapat dihapus**; koreksi tercatat dengan alasan (`evidence.mixin`). Perubahan field penting terlacak dengan `mail.thread` | Keamanan: akuntabilitas, *non-repudiation* | KF-SDM-03, 07, 20, 25, 33, 34 |
| KNF-SDM-06 | **Tanpa tanda tangan digital.** Keabsahan dibuktikan dengan PDF bertanda tangan manual, pengesah tercatat, dan pencatat | Keamanan: autentisitas | KF-SDM-06 |
| KNF-SDM-07 | **Data pribadi minimum:** nomor HP, email pribadi, dan NIK tidak disimpan modul SDM; dari KHS hanya nilai MK yang dipersyaratkan yang diketik (bedah dokumen bagian 8) | Keamanan: kerahasiaan; kebebasan dari risiko | KF-SDM-07 |
| KNF-SDM-08 | **Tanpa integrasi** dengan SIAKAD, sistem kepegawaian, maupun Google Form/Sheets yang dipakai sekarang. Data awal pilot (asisten, kelas) boleh dimasukkan lewat fitur impor standar Odoo, tanpa kode khusus | Kompatibilitas: interoperabilitas; Portabilitas: instalabilitas | Seluruh modul |
| KNF-SDM-09 | Surat Tugas, Rencana Pelatihan, dan laporan bukti diterbitkan sebagai **PDF (QWeb report)** | Portabilitas: *replaceability* | KF-SDM-17, 39, 42 |
| KNF-SDM-10 | Persentase PKG-04 dan PKG-10 serta kriteria tertinggi PKG-14 harus **sama dengan hitungan manual** pada skenario uji | Kesesuaian fungsional: ketepatan | KF-SDM-12, 26, 36 |
| KNF-SDM-11 | Syarat kompetensi per jabatan, masa berlaku standar per tugas/alat, dan pelaksana tugas/alat disimpan sebagai **data** yang bisa diubah KaLab (transien, §4.7.5), bukan konstanta di kode | Portabilitas: adaptabilitas | KF-SDM-02, 18, 19 |
| KNF-SDM-12 | Antarmuka berbahasa **Indonesia**, dengan istilah yang sama dengan instrumen monev (sesi, petugas, otorisasi, kriteria, bukti dukung) | Usabilitas: *learnability* | Seluruh modul |
| KNF-SDM-13 | Data uji dan *seed* **fiktif**; tidak ada nama, NIM, atau nilai nyata di repo | Kebebasan dari risiko | Seluruh modul |

---

## 4. Keterlacakan

### 4.1 Masalah → tujuan → KF

| Masalah (brief, Bab I 1.2) | Tujuan (1.4) | KF |
|---|---|---|
| M1. Syarat kompetensi asisten bisa dilonggarkan tanpa persetujuan tercatat; pencatatan petugas hanya asisten untuk honor; kesesuaian kompetensi petugas per sesi tidak terbukti (A4, A7, A9, A18) | T1. Pengelolaan kompetensi dan penugasan petugas per sesi yang memeriksa kesesuaian kompetensi dan mencatat pengecualian | KF-SDM-01–05, 07–13 |
| M2. Belum ada rekaman tugas/alat berkewenangan khusus, asesmen, otorisasi, dan evaluasi ulangnya (A16, A21) | T2. Asesmen, otorisasi, dan evaluasi ulang otorisasi PLP/laboran | KF-SDM-18–27 |
| M3. Kebutuhan, pelaksanaan, dan efektivitas pelatihan PLP belum terhubung dengan kompetensi (A13) | T3. Rencana, realisasi, dan evaluasi efektivitas pelatihan yang memperbarui matriks kompetensi | KF-SDM-29–36 |
| M4. Skor dihitung manual menjelang monev dan tidak tertelusur ke bukti (A12, A14) | T4. Status ketiga indikator yang tertelusur ke bukti | KF-SDM-12, 26, 36, 40–42 |

### 4.2 Kriteria instrumen → KF (cek lantai)

| Indikator | Syarat/kriteria | KF pencatatan | KF pengecekan |
|---|---|---|---|
| PKG-04 | S1 Kebutuhan petugas ditetapkan menurut risiko/beban kerja | KF-SDM-09 | KF-SDM-12 |
| | S2 Penugasan sah | KF-SDM-10, 06 | KF-SDM-43, 11, 12 |
| | S3 Kompetensi relevan terbukti | KF-SDM-02, 03 | KF-SDM-04, 12 |
| | S4 Asisten memenuhi syarat internal | KF-SDM-07, 08 | KF-SDM-11, 12 |
| | Bukti 1–7 | KF-SDM-13, 10 (17), 05, 03, 07, 07, (16) | — |
| PKG-10 | Penyebut: pasangan yang memerlukan otorisasi dan aktif | KF-SDM-18, 19 | KF-SDM-26 |
| | S1 Kompetensi dibuktikan | KF-SDM-20, 03 | KF-SDM-21, 23, 26 |
| | S2 Cakupan kewenangan ditetapkan, berlaku | KF-SDM-22, 06 | KF-SDM-43, 24, 26 |
| | S3 Pengguna pemula disupervisi | KF-SDM-22 | KF-SDM-23, 26 |
| | S4 Dievaluasi bila ada perubahan | KF-SDM-25 | KF-SDM-26 |
| | Bukti 1–5 | KF-SDM-18, 20, 27, (28), 25 | — |
| PKG-14 | K1 Kebutuhan kompetensi dan rencana ditetapkan | KF-SDM-29, 06 | KF-SDM-30, 32, 36 |
| | K2 Materi, peserta, anggaran, jadwal, kriteria keberhasilan sesuai gap | KF-SDM-31 | KF-SDM-32, 36 |
| | K3 Pelatihan terlaksana dan diterapkan | KF-SDM-33 (37) | KF-SDM-36 |
| | K4 Efektivitas dibuktikan, kebutuhan berikutnya diperbarui | KF-SDM-34 | KF-SDM-35, 36 |

Semua syarat dan kriteria terpenuhi oleh KF lapis Inti. KF Pelengkap di dalam tanda kurung hanya memperkuat.

### 4.3 Cakupan rancangan di brief → KF

| Area | Inti | Pelengkap |
|---|---|---|
| Kompetensi | KF-SDM-01–05 | — |
| Pengesahan (Core) | KF-SDM-06, 43 | — |
| PKG-04 Penugasan | KF-SDM-07–13 | KF-SDM-14–17 |
| PKG-10 Otorisasi | KF-SDM-18–27 | KF-SDM-28 |
| PKG-14 Pelatihan | KF-SDM-29–36 | KF-SDM-37–39 |
| Status monev | KF-SDM-40–42 | — |

**Satu tambahan terhadap brief:** KF-SDM-19 (pelaksana tugas/alat) belum tertulis di tabel cakupan brief. KF ini dibutuhkan untuk penyebut PKG-10, jadi masuk lantai instrumen (Inti). Brief perlu disesuaikan (bagian 7.3).

---

## 5. Yang tidak ditulis sebagai kebutuhan

Mengikuti batasan masalah butir 7 di brief:

| Hal | Alasan tidak dirancang |
|---|---|
| Pendaftaran calon asisten, pencatatan calon yang tidak lulus | Sudah dibahas Anandar (2026); keputusan 14 Nov 2026 |
| Perhitungan honor asisten | Batasan masalah |
| Alokasi asisten otomatis (*minimum coverage*, cek bentrok) | Draf STD-PRK-03; tidak dibutuhkan kriteria |
| Bobot rubrik seleksi rinci dan **ambang nilai MK sebagai pengaturan** | Cukup skor dan keputusan penilai; pengecualian dicatat lewat KF-SDM-08. Besaran ambang masih [KONFIRMASI K2] |
| Kebutuhan petugas per sesi berbasis perhitungan risiko | Cukup per kelas (KF-SDM-09) |
| Otorisasi untuk asisten, dosen, dan praktikan; pemblokiran pemakaian alat oleh sistem; log supervisi harian | Keputusan 14 Nov 2026; brief batasan 7 |
| Penjadwal kedaluwarsa otorisasi dan pengingat (bukti kedaluwarsa, evaluasi pascapelatihan) | Status berlaku dihitung saat dibaca (kontrak Core K-3) |
| Pembukaan evaluasi ulang otomatis | Pemicu dicatat manual (KF-SDM-25); otorisasi lewat masa berlaku sudah gagal S2 lewat KF-SDM-24 |
| Penganggaran pelatihan rinci, angka kredit jabatan fungsional, kuesioner reaksi peserta | Brief batasan 7 |
| *Dashboard* grafik dan tren antarperiode | Cukup daftar status dengan tautan bukti (KF-SDM-40) |
| Pencatatan kehadiran petugas per sesi | Milik PKG-18 (Praktikum) |

---

## 6. Perbandingan dengan contoh Tata Kelola

Dibandingkan dengan [kebutuhan-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/kebutuhan-tata-kelola.md) (branch `febriyan-skripsi`):

| Aspek | Tata Kelola | SDM (dokumen ini) |
|---|---|---|
| Struktur | Aturan, aktor, KF per area, KNF ISO 25010, keterlacakan (masalah, kriteria, cakupan), tidak ditulis, perubahan, temuan, isu | Sama. Tidak ada bagian "perubahan dibanding versi sebelumnya" karena ini versi pertama |
| Kode | KF-01–45, KNF-01–11 | **KF-SDM-01–43**, **KNF-SDM-01–13** (prefiks wajib, CLAUDE.md bagian 2) |
| Aktor | KaLab, Laboran/PLP, Pengguna Lab, Penjadwal | KaLab, Laboran/PLP saja. Tidak ada Penjadwal (semua status dihitung) dan tidak ada Pengguna Lab (asisten bukan aktor) |
| Pengesahan | KF-01–09 mendefinisikan mekanismenya | KF-SDM-06, 43 untuk dokumen SDM sendiri; perilakunya diwarisi dari mekanisme Core (`approval.mixin`) |
| Jenis skor | 1 persentase (PKG-02), 3 kriteria berurutan | 2 persentase (PKG-04, 10), 1 kriteria berurutan (PKG-14) → lebih banyak KF *hidden* untuk menghitung unit |
| Ciri khas | Banyak KF penerbitan dokumen (SK, rencana) | Banyak KF yang **membuat rekaman otomatis** dari rekaman lain (asesmen → bukti kompetensi, evaluasi → bukti kompetensi, matriks → kebutuhan) |
| Rasio W/O | 36/9 | 35/8 |

---

## 7. Temuan, cek silang, isu terbuka, dan koreksi

### 7.1 Temuan untuk langkah berikutnya

- **Langkah 5 (proses bisnis).** Activity nontrivial: (a) seleksi asisten → Surat Tugas → pengesahan (multi-aktor, tanda tangan di luar sistem; pengesahan digambar sekali sebagai activity pengesahan dokumen SDM dan dipanggil dengan «call behavior»; revisi 17 November 2026); (b) siklus otorisasi: asesmen → otorisasi → pengesahan → evaluasi ulang → otorisasi baru/dicabut; (c) siklus pelatihan: rencana (kebutuhan dari matriks) → pengesahan → realisasi → evaluasi → bukti kompetensi. State machine: **Otorisasi** (draf → diajukan → disahkan → diganti/dicabut, plus status turunan *berlaku/tidak berlaku*), **Evaluasi Ulang** (terbuka → diputuskan), **Item Pelatihan** (rencana → terlaksana/batal). Surat Tugas dan Rencana Pelatihan: state machine pengesahan dokumen SDM (status dari `approval.mixin` Core).
- **Langkah 6 (use case).** Kandidat «CRUDL»: Kompetensi, Tugas/Alat (termasuk pelaksana), Kebutuhan Petugas, Bukti Kompetensi. Kandidat «report»: KF-SDM-05, 13, 27, 38, 40. "Terbitkan" (KF-SDM-17, 39, 42) dinilai *essential*-nya (§4.3.4).
- **Langkah 7 (aturan bisnis).** Kandidat AB dari KF *hidden*: KF-SDM-43, 08, 11, 12, 23, 24, 26, 32, 37 (alasan wajib). KF-SDM-21, 30, 35 adalah perilaku sistem (membuat rekaman), bukan aturan.

### 7.2 Cek silang ke langkah sebelumnya

| Cek | Hasil |
|---|---|
| Setiap syarat/kriteria instrumen punya KF pencatatan dan pengecekan | ✓ (bagian 4.2), termasuk penyebut PKG-10 yang sebelumnya belum diputuskan |
| Setiap fitur Inti di brief punya KF | ✓. Surat Tugas bergaris, laboran per ruang, rentang berlaku, Personel asisten dibuat saat lulus, Otorisasi tanpa `period.mixin`, pembekuan kebutuhan lewat *hook* |
| Tidak ada KF di luar cakupan brief | ✓, kecuali **KF-SDM-19** (pelaksana tugas/alat) yang dibutuhkan lantai instrumen; brief perlu ditambah |
| Model konsisten dengan kontrak Core | ✓. Satu model baru yang belum ada di kontrak: `labfik.sdm.orientasi` (Pelengkap, KF-SDM-16); di analisis PKG-04 sudah ada sebagai fact Orientasi/Supervisi |
| Keputusan pengguna 14 Nov 2026 | ✓ Semua tercermin (asisten `hr.employee`/Asisten Praktikum, Surat Tugas bergaris, Kelas/MK/Sesi di Core, PKG-10 hanya PLP/laboran, PKG-14 per tahun dan item batal) |
| Aktor konsisten dengan brief | ✓ KaLab dan Laboran/PLP. Penjadwal di brief (Pelengkap, kedaluwarsa otorisasi) **dihapus** karena K-3 |

### 7.3 [KONFIRMASI]

| No | Pertanyaan | Ke siapa |
|---|---|---|
| KB-1 | Penyebut PKG-10 = pasangan **pelaksana yang ditetapkan KaLab** × tugas/alat (KF-SDM-19)? | Zahir (pengguna) |
| KB-2 | Kebutuhan laboran per kelas selalu 1 (cukup nilai *default*), atau KaLab menetapkannya per kelas seperti asisten? | KaLab (K3) |
| KB-3 | KF-SDM-11 **menolak** Surat Tugas bila ada asisten tanpa seleksi lulus untuk MK kelasnya. Terlalu ketat untuk pengganti mendadak? Alternatifnya hanya peringatan, dan S4 gagal di status monev | Zahir; KaLab (K9) |
| Lama | K2 (ambang nilai), K3 (laboran per ruang), K7 (pengesah Surat Tugas), K10 (pengesah Rencana Pelatihan); KC-1–KC-5 kontrak Core | KaLab, Febriyan, Herrens |

### 7.4 Dokumen lain yang perlu ikut berubah

| Dokumen | Perubahan |
|---|---|
| [brief-sdm.md](../brief/brief-sdm.md) Cakupan rancangan, baris PKG-10 Inti | Tambah "pelaksana tiap tugas/alat (penyebut)" (KF-SDM-19) |
| [brief-sdm.md](../brief/brief-sdm.md) Cakupan, paragraf aktor | Hapus "Penjadwal (kedaluwarsa otorisasi, Pelengkap)" |
| [analisis-data-pengelolaan-10.md](../analisis/analisis-data-pengelolaan-10.md) bagian Ringkasan temuan 2 dan bagian 5 | Usulan "pasangan aktif dari jabatan pelaksana" diganti "pelaksana ditetapkan KaLab per tugas/alat" (bila KB-1 disetujui) |
| [kontrak-core-sdm.md](kontrak-core-sdm.md) peta mixin | Tambah `labfik.sdm.orientasi` (evidence, Pelengkap) |

### 7.5 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| Brief, paragraf aktor | Masih mencantumkan **Penjadwal** untuk kedaluwarsa otorisasi, padahal Langkah 3 (K-3) memutuskan status berlaku dihitung | 7.4 |
| Analisis PKG-10 | Penyebut ditunda tanpa catatan bahwa ia termasuk **lantai instrumen**; penundaan itu berisiko membuat PKG-10 tidak bisa dihitung | KF-SDM-19 + KB-1 |
| Analisis PKG-04 | Seleksi menyimpan "memenuhi syarat nilai (dihitung dari ambang)" seolah ada pengaturan ambang, padahal prinsip *sweet spot* menolak pengaturan yang tidak dibutuhkan kriteria | Ambang tidak dirancang (bagian 5); S4 dibuktikan oleh keputusan penilai dan pengecualian tercatat |
| Kontrak Core peta mixin | `labfik.sdm.orientasi` (fact Orientasi/Supervisi di analisis PKG-04) terlewat | 7.4 |
