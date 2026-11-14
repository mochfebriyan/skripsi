# Analisis Data Indikator Pengembangan 14 (pelatihan PLP/laboran)

14 November 2026 · Zahir · PKG-14 · Bagian dari proyek LabFIK Compliance · Modul: SDM & Kompetensi (di sheet: Organization Management)

**Status: DRAF.** Bahan kerja Langkah 0 (prasyarat rancangan); bahan Bab I dan 2.2. Disusun ulang dari nol oleh pemegang modul. Isi baris sheet ditulis Herrens sebagai PIC analisis awal dan dipakai sebagai bahan. Belum ada hasil wawancara: pertanyaan SDM & Kompetensi no. 9–12 di lembar "Wawancara FIKLAB Compliance" belum dijawab KaLab maupun laboran.

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) bagian 2. Package terkait: [PKG-04](analisis-data-pengelolaan-4.md) (pemilik master Kompetensi dan Bukti Kompetensi) dan PKG-10 (otorisasi).

---

## 0. Sumber yang dipakai

| Sumber | Sifat | Dipakai untuk |
|---|---|---|
| Instrumen Monev Laboratorium UPNVJ 2026 v1.1, tab *Analysis* baris ID 14 | **Acuan resmi** | Target, kriteria K1–K4, bukti dukung, usulan entitas Herrens |
| SNI ISO/IEC 17025:2017 klausul 6.2.2 dan 6.2.5 c (rekaman pelatihan personel) | **Acuan resmi** | Persyaratan kompetensi terdokumentasi dan rekaman pelatihan |
| Pedoman Diklatfung PLP 2022 | Acuan resmi yang disebut instrumen; **belum dimiliki** **[VALIDASI]** | Jenis pelatihan fungsional PLP |
| `09_Formulir_Perencanaan_Kompetensi_Risiko`, bagian FRM-DIK-001 "Rencana Pelatihan dan Evaluasi Penerapan" | **Draf GPT** ("Templat contoh", isian simulasi) | Contoh format saja |
| `07_SOP_Kompetensi_Penugasan_Otorisasi`, langkah 4–5 | **Draf GPT** | Contoh format saja |
| Folder "PELATIHAN" (baris 10 `ISO_LAB_SI`, "Peningkatan Kompetensi Personel Laboratorium") | **Nyata**: dua sertifikat milik laboran ruang 201 (sertifikat kompetensi BNSP berlaku 3 tahun; sertifikat pelatihan 24 JP tanpa masa berlaku) | Bukti as-is K3; bentuk field Realisasi dan Bukti Kompetensi ([bedah dokumen](bedah-dokumen-sdm.md) A13, D4) |
| SK SOTK FIK 2025 (baris 9 `ISO_LAB_SI`) | **Nyata** | Pembinaan personel: KaLab (pembinaan anggota lab), Wadek Bidang Keuangan dan Umum (pembinaan karier dan evaluasi kinerja tendik) ([bedah dokumen](bedah-dokumen-sdm.md) A20) |
| [kontrak-core-sdm.md](../rancangan/kontrak-core-sdm.md) | Draf Langkah 3 | Mixin Rencana Pelatihan; *hook* pembekuan kebutuhan |

*Koreksi (Langkah 2):* versi pertama dokumen ini menulis "dokumen nyata tentang pelatihan PLP tidak ditemukan". Folder di baris 10 `ISO_LAB_SI` ternyata berisi dua sertifikat nyata.

**Kondisi saat ini sebagian diketahui.** Bukti yang diunggah lab hanya sertifikat lepas milik satu laboran, tanpa analisis kebutuhan, rencana, maupun evaluasi (A13). Siapa yang menyusun dan mengesahkan rencana pelatihan, dan apakah sertifikat itu relevan dengan gap tugasnya, masih **[KONFIRMASI KaLab]**.

---

## Ringkasan

| | Pengembangan 14 |
|---|---|
| Inti | Kebutuhan kompetensi PLP/laboran dipetakan → rencana pelatihan disahkan → pelatihan dijalankan dan diterapkan → efektivitas dievaluasi dan kebutuhan berikutnya diperbarui |
| PJ | KaLab; Dekanat SDM |
| Jenis skor | **Kriteria berurutan K1–K4** |
| Unit | 1 paket dokumen dan rekaman (usulan: per periode tahunan) |
| Level cakupan (usulan) | **Semi-otomatis** |
| Pola | Rencana → realisasi → evaluasi, mirip Pengelolaan 1 dan Pengembangan 13 (Tata Kelola) |
| Posisi dalam dependensi | Hilir di dalam modul: memakai Kompetensi, syarat kompetensi per Jabatan, dan Bukti Kompetensi milik PKG-04. Hasilnya menambah Bukti Kompetensi |

**Temuan utama:**
1. **Analisis kebutuhan kompetensi (bukti 1) tidak perlu diinput dari nol.** Gap per personel bisa dihitung dari data PKG-04: syarat kompetensi jabatan dibandingkan dengan Bukti Kompetensi yang dimiliki. Ini laporan [R], bukan tabel baru.
2. **Siklus kompetensi tertutup di modul ini.** Evaluasi yang menyatakan pelatihan efektif menghasilkan Bukti Kompetensi baru (jenis "pelatihan"). Matriks Kompetensi PKG-04 ikut berubah, dan gap periode berikutnya berkurang.
3. **Tidak bisa memakai model rencana Tata Kelola (`labfik.plan*`).** Model itu ada di `labfik_org`, sedangkan `labfik_sdm` hanya bergantung ke `labfik_core`. Yang dipakai adalah mixin Core: `labfik.approval.mixin` (pengesahan rencana), `labfik.period.mixin` (satu rencana per periode tahunan), `labfik.criteria.mixin` (status K1–K4), dan `labfik.evidence.mixin` (sertifikat dan bukti). Pembekuan kebutuhan saat diajukan memakai *hook* `_sebelum_ajukan()` yang sudah disediakan `approval.mixin`. Rencana Pelatihan ditulis sebagai model sendiri, dan perilaku bersamanya diwarisi dari mixin.

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Kompetensi PLP/laboran dikembangkan melalui pelatihan yang relevan dan dievaluasi penerapannya |
| Penerapan / PJ | Umum / KaLab; Dekanat SDM |
| Unit | 1 paket dokumen dan rekaman |
| Skor | 4: kriteria 1–4 terpenuhi berurutan · 3: kriteria 1–3 · 2: hanya kriteria 1 atau 1–2 · 1: kriteria 1 belum terpenuhi atau bukti tidak dapat diverifikasi |
| Acuan | Pedoman Diklatfung PLP 2022 (kompetensi dan pengembangan profesi) · SNI ISO/IEC 17025:2017 6.2.5 |

Bukti dukung: (1) analisis kebutuhan kompetensi, (2) rencana Diklatfung/bimtek/sertifikasi sesuai jabatan, (3) sertifikat, (4) praktik/demonstrasi pascapelatihan, (5) rekaman peningkatan layanan.

Kriteria di instrumen:
1. Kebutuhan kompetensi dan rencana pengembangan personel ditetapkan.
2. Materi, peserta, anggaran, jadwal, dan kriteria keberhasilan sesuai gap tugas.
3. Pelatihan terlaksana dan keterampilan diterapkan pada pekerjaan nyata.
4. Efektivitas pelatihan dibuktikan melalui asesmen ulang/kinerja, dan kebutuhan berikutnya diperbarui.

**Siapa yang dicakup (keputusan Zahir, 14 November 2026):** instrumen menyebut **PLP/laboran**, jadi peserta dibatasi ke personel berjabatan PLP/laboran dan teknisi. Asisten dan dosen tidak dihitung untuk indikator ini **[KONFIRMASI pembimbing]**.

**Periode (keputusan Zahir, 14 November 2026):** satu Rencana Pelatihan **per tahun**. PLP/laboran adalah pegawai, bukan mahasiswa, sehingga siklusnya tidak mengikuti semester. Tahun anggaran atau tahun kalender **[KONFIRMASI KaLab]**.

## 2. Aturan "memenuhi"

Kriteria diperiksa **berurutan**. Kriteria berikutnya tidak dihitung bila kriteria sebelumnya belum berbukti. Sistem menampilkan **kriteria tertinggi yang lengkap secara data**. Skor akhir ditetapkan penilai.

| Kriteria | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| K1 Ditetapkan | Kebutuhan kompetensi dipetakan dan rencana pelatihan disahkan | Ada Rencana Pelatihan berstatus *disahkan* untuk periode itu, lengkap dengan pengesah, tanggal, dan berkas. Setiap PLP/laboran aktif tercantum di analisis kebutuhan, baik yang punya gap maupun yang dinyatakan "tidak ada gap" | Keabsahan pengesahan; apakah gap masuk akal |
| K2 Sesuai gap | Setiap item rencana lengkap dan menjawab gap | Setiap item pelatihan punya kompetensi sasaran, peserta, materi, anggaran, jadwal, dan kriteria keberhasilan. Kompetensi sasaran termasuk gap pesertanya **[USULAN PENULIS]** | Relevansi materi dengan gap tugas |
| K3 Terlaksana dan diterapkan | Pelatihan berjalan dan keterampilannya dipakai | Setiap item yang jadwalnya sudah lewat punya Realisasi untuk setiap peserta, dengan sertifikat atau bukti hadir **dan** bukti praktik/demonstrasi pascapelatihan | Keaslian sertifikat; apakah penerapannya nyata |
| K4 Efektivitas dan pembaruan | Efektivitas dibuktikan dan kebutuhan berikutnya diperbarui | Setiap Realisasi punya Evaluasi Efektivitas berisi skor sebelum dan sesudah atau penilaian kinerja, kesimpulan (efektif / perlu pengembangan), dan tindak lanjut kebutuhan berikutnya | Kualitas asesmen ulang dan rekaman peningkatan layanan |

Ambang K3 ("setiap item") bisa terlalu ketat bila pelatihan dibatalkan dari pihak penyelenggara. **Keputusan (Zahir, 14 November 2026):** item boleh diberi status *batal* dengan alasan wajib, dan item batal tidak dihitung di K3 **[KONFIRMASI pembimbing]**.

## 3. Luaran

| Luaran | Bukti ke- | Jenis | Keterangan |
|---|---|---|---|
| Analisis Kebutuhan Kompetensi | 1 | [R] | Per PLP/laboran: syarat kompetensi jabatan dibandingkan dengan Bukti Kompetensi yang berlaku → daftar gap. Dihitung dari data PKG-04. Hasilnya dibekukan ke rencana saat diajukan (lihat bagian 4) |
| Rencana Pelatihan disahkan | 2 | [T] + berkas bertanda tangan | Header + item pelatihan |
| Sertifikat | 3 | Lampiran di [T] Realisasi Pelatihan | — |
| Praktik/demonstrasi pascapelatihan | 4 | Lampiran di [T] Realisasi Pelatihan | — |
| Rekaman peningkatan layanan | 5 | Lampiran/uraian di [T] Evaluasi Efektivitas | — |
| Rekap pelatihan PLP per periode | — | [R] | Rencana vs realisasi vs efektivitas per personel |
| Status K1–K4 | — | [R] | Dari `labfik.criteria.mixin` |
| Matriks Kompetensi | — | [R] milik PKG-04 | Ikut berubah setelah evaluasi efektif |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Rencana Pelatihan** | 1 rencana per periode | berkas; status dan riwayat pengesahan dari `labfik.approval.mixin`; periode tahunan dari `labfik.period.mixin`; status K1–K4 dari `labfik.criteria.mixin`. **Anak 1, Kebutuhan Kompetensi:** personel, kompetensi, keterangan gap (atau "tidak ada gap"), sumber (otomatis dari matriks / ditambah KaLab). **Anak 2, Item Pelatihan:** kompetensi sasaran, jenis (Diklatfung/bimtek/sertifikasi/pelatihan internal), materi, peserta, penyelenggara, anggaran, jadwal, kriteria keberhasilan, status (rencana/terlaksana/batal) | Kebutuhan dibekukan saat rencana diajukan (*hook* `_sebelum_ajukan()`), supaya bukti 1 tidak berubah setelah disahkan. Pengesah: KaLab dan/atau Wadek Bidang Keuangan dan Umum **[KONFIRMASI K10]** |
| **Realisasi Pelatihan** | 1 peserta × 1 item | item, personel, tanggal pelaksanaan, penyelenggara, durasi jam (mis. 24 JP, dari sertifikat nyata D4), sertifikat, bukti praktik/demonstrasi pascapelatihan; tanggal, pelapor, berkas, keterangan dari `labfik.evidence.mixin` | Bukti K3 (bukti dukung 3 dan 4). Sheet: "Upload PDF sertifikat" |
| **Evaluasi Efektivitas Pelatihan** | 1 per Realisasi | metode (asesmen ulang / penilaian kinerja atasan), skor sebelum, skor sesudah, penilai, kesimpulan (efektif / perlu pengembangan), rekaman peningkatan layanan, tindak lanjut kebutuhan berikutnya | Bukti K4. Dicatat terpisah dari Realisasi karena terjadi di waktu lain, oleh aktor lain (*modal class*, Wazlawick §9.3.2). Bila efektif, sistem membuat **Bukti Kompetensi** (PKG-04) berjenis pelatihan |

Riwayat perubahan memakai `mail.thread` + `tracking`.

**Penyesuaian terhadap sheet:** "Kompetensi Matrix (Report)" di sheet ID 14 adalah report yang sama dengan Matriks Kompetensi ID 4, sehingga cukup satu report milik PKG-04. Ini sudah diusulkan juga di [pemetaan](pemetaan-package-instrumen.md).

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Periode | Periode rencana (tahunan) | Core: `labfik.periode` | — |
| Personel | Peserta, penilai, pengesah | Core: `hr.employee` | Data contoh |
| Jabatan | Membatasi peserta ke PLP/laboran; syarat kompetensi; siapa berwenang mengesahkan | Core: `hr.job` (syarat kompetensi ditambahkan `labfik_sdm`) | — |
| Kompetensi | Kompetensi sasaran dan gap | PKG-04 (modul sendiri) | — |

Cukup berupa **pilihan tetap**: jenis pelatihan, metode evaluasi, kesimpulan efektivitas, status item.

**Tidak ada master baru.** Penyelenggara pelatihan cukup teks bebas, tidak dibuat master.

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Kompetensi, syarat kompetensi jabatan, Bukti Kompetensi | PKG-04 (modul sendiri) | **Wajib** | — (dibangun di modul yang sama, lebih dulu) |
| Personel, Jabatan, Periode, mixin pengesahan/kriteria/bukti | Core | Wajib | — |
| Anggaran | Eksternal (keuangan/Dekanat SDM) | Wajib untuk K2 | Nilai anggaran diinput manual per item |
| Sertifikat Diklatfung/bimtek | Eksternal (penyelenggara) | Wajib untuk K3 | Diunggah manual |
| Gap aspek kompetensi untuk rencana pengembangan lab | Dipakai **oleh** PKG-13 (Tata Kelola) | Opsional | PKG-13 mengisi gap kompetensi secara manual |

**Arah dependensi dengan PKG-13 [KONFIRMASI kelompok]:** analisis PKG-13 Febriyan mencatat bahwa gap kompetensi dari PKG-14 opsional dipakai untuk aspek kompetensi rencana pengembangan. Bila nanti diotomatiskan, `labfik_org` yang bergantung ke `labfik_sdm`, bukan sebaliknya. Untuk sekarang keduanya diisi terpisah, sehingga tidak ada dependensi addon.

## 7. Ditunda (tidak dirancang; saran pengembangan)

- Penganggaran rinci (mata anggaran, pencairan, SPJ). Cukup nilai anggaran per item.
- Pendaftaran peserta ke pelatihan eksternal dan integrasi dengan sistem kepegawaian universitas.
- Pengingat jadwal pelatihan dan pengingat evaluasi pascapelatihan (penjadwal).
- Kuesioner reaksi peserta (Kirkpatrick level 1). Instrumen hanya meminta asesmen ulang/kinerja.
- Angka kredit jabatan fungsional PLP.

## 8. Pertanyaan untuk narasumber

Sudah ada di lembar wawancara (SDM & Kompetensi no. 9–12), belum dijawab. Yang paling menentukan rancangan:

| No. wawancara | Pertanyaan inti | Menentukan |
|---|---|---|
| 9 | Bagaimana kebutuhan pelatihan PLP ditentukan? Siapa menyusun dan menyetujui rencana pelatihan: KaLab, Wadek Bidang Keuangan dan Umum (SK SOTK butir 5b), atau keduanya? | Pengesah Rencana Pelatihan (K1), baris wewenang `rencana_pelatihan` di `hr.job` |
| 10, 11 | Bukti apa yang disimpan setelah pelatihan, dan di mana? | Isi Realisasi (K3) |
| 12 | Bagaimana keberhasilan pelatihan dinilai, oleh siapa, dan kapan? Hasilnya dipakai untuk pelatihan berikutnya? | Metode dan penilai Evaluasi Efektivitas (K4) |
| Tambahan | Rencana pelatihan disusun per tahun anggaran atau per tahun akademik? Berapa PLP/laboran aktif? | Grain periode; ukuran data uji |
| Tambahan | Apakah teknisi juga dihitung sebagai PLP/laboran untuk indikator ini? | Batas peserta |

## 9. Kompleksitas (perkiraan)

| T | M lokal | R |
|---|---|---|
| 3 (Rencana Pelatihan dengan 2 anak, Realisasi Pelatihan, Evaluasi Efektivitas) | 0 | 3 (Analisis Kebutuhan Kompetensi, Rekap Pelatihan, status K1–K4); Matriks Kompetensi memakai milik PKG-04 |

Sama dengan pemetaan lama (3 T / 0 M / 0 R). Report bertambah karena analisis kebutuhan dan rekap kini dihitung dari data, tidak diinput.
