# Cakupan Rancangan Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF, menunggu persetujuan.** Dokumen ini menetapkan **cakupan rancangan untuk proposal**: lebih lengkap dari MVP, tetapi tidak sebesar rancangan penuh hasil langkah 5–10. Setelah disetujui, artefak rancangan (proses bisnis, use case, SSD, design class diagram) diselaraskan ke cakupan ini.

## 1. Tiga lapis

| Lapis | Arti | Di proposal |
|---|---|---|
| **Inti** | Tanpa ini ada kriteria instrumen (K1–K4, S1–S5) yang tidak bisa dibuktikan, atau alur pengesahan putus | Dirancang penuh; prioritas implementasi |
| **Pelengkap** | Memperkuat rancangan (format dokumen lab, kelengkapan siklus) dengan biaya kecil | Dirancang penuh; dibangun bila waktu cukup |
| **Lanjutan** | Menambah kenyamanan atau kedalaman, tetapi tidak dibutuhkan untuk membuktikan kriteria | **Tidak** digambar di diagram proposal; disebut di batasan masalah dan saran pengembangan |

**Cakupan proposal = Inti + Pelengkap.**

Rancangan lengkap (versi saat ini) tetap disimpan sebagai rujukan lapis Lanjutan. Tidak ada yang dihapus dari riwayat.

## 2. Prinsip pemilahan

1. **Lantai ditentukan instrumen.** Setiap kriteria K1–K4 dan S1–S5 harus punya kebutuhan, use case, dan rekaman bukti. Inilah yang membuat jumlah use case tidak bisa turun banyak; yang dipangkas terutama **kedalaman** (varian, model pendukung, otomatisasi).
2. **Satu mekanisme, satu jalur utama.** Pengesahan cukup satu jalur (ajukan → kembalikan / sahkan → cabut). Jalur alternatif (tarik, catatan kertas) ke Lanjutan. Pemeriksaan tidak dipisah dari pengesahan.
3. **Teks dulu, master kemudian.** Bila analisis sudah menyediakan jalan pengganti berupa teks bebas (tautan Renstra), master khususnya ke Lanjutan.
4. **Unggah dulu, form kemudian.** Dokumen yang jarang berubah atau tidak diminta pembimbing diisi lewat sistem (Renstra) cukup sebagai dokumen unggahan yang disahkan.
5. **Hitung, bukan jadwalkan.** Penanda yang bisa dihitung dari data (perlu ditinjau, masih berlaku) tidak butuh pengingat terjadwal.
6. **Pertahankan yang menunjukkan desain.** Inheritance (mixin), log pengesahan, dan Template Method tetap ada: biayanya kecil dan inilah yang diminta pembimbing.

## 3. Ringkasan per area

| Area | Inti | Pelengkap | Lanjutan |
|---|---|---|---|
| **Pengesahan** | Ajukan (cek kelengkapan), kembalikan dengan alasan, unggah TTD, sahkan (cek wewenang), cabut, log pengesahan. **Pejabat yang menandatangani di luar sistem (Dekan)** dicatat sebagai pengesah; KaLab sebagai pencatat. Penolakan di atas kertas dicatat KaLab lewat aksi kembalikan yang sama. Pemeriksaan menyatu dengan pengesahan (tidak ada tahap atau field pemeriksa) | Kedaluwarsa otomatis (penjadwal harian) | Tarik pengajuan, pengaturan modul |
| **PKG-02 SOP/IK** | Dokumen induk, unggah versi (satu berlaku), distribusi, sosialisasi, tinjau ulang + penanda "perlu ditinjau", persentase memenuhi, daftar induk dan riwayat revisi | Pengguna lab membaca versi berlaku; satu versi diproses per dokumen (AB-13) | Pengingat tinjau ulang terjadwal |
| **PKG-03 Struktur** | Personel, jabatan (tugas, wewenang, atasan, pengganti), SK + baris penetapan, rapat, evaluasi, bagan (daftar hierarki), matriks kewenangan (daftar) | Ekspor SK format fakultas | Koordinasi antarjabatan, bagan organisasi visual |
| **PKG-01 Rencana** | Rencana tahunan (RKT): item dengan KPI, target, PIC, jadwal, anggaran, **tautan Renstra berupa teks**; realisasi + bukti; tinjauan → rencana berikutnya; Renstra/roadmap sebagai **dokumen unggahan** yang disahkan; ekspor PDF RKT; master KPI | Narasi ringkas di RKT (ringkasan, latar belakang, tujuan, ruang lingkup) untuk ekspor; revisi rencana; satu dokumen berlaku per jenis dan periode (AB-14) | Form Renstra lengkap (visi, misi, sasaran, program, baseline); IKU sebagai dokumen terpisah; master Sasaran Renstra + matriks keterkaitan; pengingat realisasi |
| **PKG-13 Pengembangan** | Rencana jenis pengembangan: temuan gap 4 aspek, item dengan nilai risiko dan manfaat, ukuran manfaat di tinjauan | Ekspor PDF rencana pengembangan (template sama dengan RKT); prioritas dihitung dari risiko × manfaat | Penarikan data gap otomatis dari modul lain |
| **Status monev** | Persentase PKG-02; kriteria tertinggi K1–K4 PKG-01/03/13 dengan tautan bukti; akses baca penilai | — | Grafik tren antarperiode |

## 4. Rincian per unsur

### 4.1 Use case (dari [use-case-tata-kelola.md](use-case-tata-kelola.md))

| Lapis | Use case |
|---|---|
| **Inti (24)** | UC-01 Personel, 02 Jabatan, 03 Susun SK, 04 Rapat, 05 Evaluasi, 06 Laporan Struktur, 07 Dokumen Induk, 08 Unggah Versi, 09 Distribusi, 10 Sosialisasi, 11 Tinjau Ulang, 13 Laporan Pengendalian Dokumen, 14 KPI, 16 Susun Rencana, 18 Isi Realisasi, 19 Catat Tinjauan, 20 Laporan Rencana (tanpa matriks keterkaitan), 21 Ajukan, 24 Kembalikan (tanpa varian kertas), 25 Terbitkan Dokumen Resmi (RKT), 26 Unggah TTD, 27 Sahkan, 28 Cabut, 29 Status Monev |
| **Pelengkap (2)** | UC-12 Baca Dokumen Berlaku, UC-31 Kedaluwarsakan Dokumen Berperiode |
| **Lanjutan (4)** | UC-15 Kelola Sasaran Renstra, UC-22 Tarik Pengajuan, UC-30 Atur Pengaturan Modul, UC-32 Kirim Pengingat Jadwal |

Perubahan aktor di diagram proposal:
- **Dekan** keluar. Dekan menandatangani di luar sistem (Wazlawick §4.4: aktor sistem harus berinteraksi langsung). Identitasnya tetap tercatat sebagai pengesah di log.
- **Pemeriksa** dihapus seluruhnya, termasuk UC-23 Periksa Dokumen (nomor dibiarkan kosong). Memeriksa dan mengesahkan dianggap satu kesatuan: pejabat yang mengesahkan sudah memeriksa isinya, dan log pengesahan menjadi buktinya.
- Aktor abstrak **Pengesah Dokumen** tidak diperlukan lagi: UC-24 Kembalikan dan UC-27 Sahkan dilakukan **KaLab**, baik untuk dokumen yang ia sahkan sendiri (POB lab) maupun yang ditandatangani Dekan (SK, RKT, rencana pengembangan).
- Aktor abstrak **Penyusun Dokumen** (KaLab, Laboran) tetap.
- Aktor **Penjadwal** tetap (UC-31).

### 4.2 Kebutuhan (dari [kebutuhan-tata-kelola.md](kebutuhan-tata-kelola.md))

| Lapis | KF |
|---|---|
| **Inti** | 01, 02, 03, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 17, 18, 20 (Renstra sebagai unggahan), 21, 23, 24, 25 (RKT), 27, 28, 29, 31 (tanpa status Diperiksa), 33 (pengesah eksternal dicatat KaLab), 34, 35, 36, 37, 38, 40 (termasuk penolakan di atas kertas), 41 |
| **Pelengkap** | 04 (ekspor SK), 16, 25 (rencana pengembangan), 26, 42 |
| **Lanjutan** | 15, 19, 22, 30, 32, 39, 43 |

### 4.3 Aturan bisnis (dari [expanded-use-case-tata-kelola.md](expanded-use-case-tata-kelola.md))

| Lapis | AB |
|---|---|
| **Inti** | AB-01–08, AB-10–12. **AB-02 disesuaikan:** yang menjalankan *sahkan*, *kembalikan*, dan *cabut* di sistem adalah KaLab; pengesah yang **tercatat** (dari berkas bertanda tangan) harus pemegang jabatan berwenang untuk jenis dokumen itu |
| **Pelengkap** | AB-13, AB-14 |
| Dihapus | AB-09 (pemeriksaan wajib); nomor dibiarkan kosong karena pemeriksaan menyatu dengan pengesahan |

### 4.4 Model dan field (dari [design-class-tata-kelola.md](design-class-tata-kelola.md))

| Perubahan | Lapis | Pengganti di cakupan proposal |
|---|---|---|
| `labfik.sasaran.renstra` | Lanjutan | Field teks `tautan_renstra` di item rencana |
| `labfik.plan.sasaran`, `labfik.plan.program`, `labfik.plan.baseline` | Lanjutan | Renstra = rencana jenis strategis berisi periode + PDF + pengesahan; kondisi awal PKG-13 ada di temuan gap |
| Rencana jenis `iku` | Lanjutan | Target KPI per periode ada di item RKT |
| Narasi rencana 9 field Html | Dipangkas jadi 4 | `ringkasan`, `latar_belakang`, `tujuan`, `ruang_lingkup` |
| `jabatan.koordinasi_ids`, `kpi.ruang_ids` | Lanjutan | — |
| `approval.mixin`: method `action_tarik` | Lanjutan | — |
| `approval.mixin`: `pemeriksa_id`, `tanggal_periksa`, state `diperiksa`, method `action_periksa` | **Dihapus** | Pemeriksaan menyatu dengan pengesahan; buktinya `approval.log` kejadian *sahkan* |
| `action_catat_pengembalian` | Digabung | `action_kembalikan(alasan, ditolak_oleh=None)`: satu aksi untuk penolakan di sistem maupun di atas kertas |
| `action_sahkan(atas_nama)` | Inti | Pengesah tercatat = pejabat penanda tangan (mis. Dekan); `pencatat_id` = KaLab yang menekan *Sahkan* |
| `_cron_kirim_pengingat_tinjau`, `_cron_kirim_pengingat_realisasi` | Lanjutan | Penanda `is_perlu_tinjau` dan daftar realisasi yang belum diisi |
| `labfik.approval.log.kejadian` | Dikurangi | {ajukan, kembalikan, unggah_ttd, sahkan, cabut, kedaluwarsa} |
| Lima mixin, `approval.log`, hook `_setelah_disahkan()` | **Tetap** | Inheritance dan Template Method tetap menjadi inti desain |

Jumlah model konkret turun dari 27 menjadi 23 (termasuk master Core). Jumlah method pengesahan publik turun dari 8 menjadi 5 (ajukan, kembalikan, lampirkan TTD, sahkan, cabut).

### 4.5 Proses bisnis dan state machine

| Diagram | Perubahan |
|---|---|
| A1 Pengesahan | Lajur: Penyusun, Sistem, KaLab, dan **Pejabat penanda tangan (di luar sistem)** yang hanya berisi tugas «manual» "Tanda tangani dokumen cetak". Lajur Pemeriksa dan cabang "tahap pemeriksaan aktif" dihapus |
| A2 Siklus SOP/IK | Node "Kirim pengingat tinjau ulang" diganti "Tandai perlu ditinjau" (service) |
| A3 Siklus Rencana | Node "Kirim pengingat realisasi" dihapus |
| A4 Siklus Struktur | Tetap |
| S1 Status Dokumen | Status Diperiksa dan transisi *tarik kembali* dihapus; transisi lain tetap |
| S2 Kemutakhiran | Tetap |

### 4.6 SSD

| Di Bab II 2.3 | Di lampiran |
|---|---|
| SSD-1 Ajukan, SSD-4 Sahkan, SSD-5 Unggah Versi, SSD-6 Tinjau Ulang, SSD-8 Isi Realisasi | SSD-2 Kembalikan (tanpa V1), SSD-3 Unggah TTD, SSD-7 Susun Rencana (tanpa V1 IKU dan sasaran/program) |

## 5. Dampak ke proposal

| Bagian | Isi |
|---|---|
| 1.3 Batasan Masalah | Daftar lapis Lanjutan sebagai hal yang dirancang tetapi tidak dibangun, ditambah alasannya |
| 2.2 Usulan Solusi | Empat fitur utama + mekanisme pengesahan bersama, dengan penanda Inti/Pelengkap |
| 2.3 Rancangan Proyek | Diagram versi cakupan proposal (bagian 4.5–4.6, use case 26, DCD 23 model) |
| 2.4 Rencana Pengujian | Skenario *black box* untuk use case Inti; Pelengkap diuji bila dibangun |
| Saran pengembangan (Bab akhir) | Lapis Lanjutan |

## 6. Keputusan (14 November 2026)

| Pertanyaan | Jawaban (Febriyan) | Dampak |
|---|---|---|
| Apakah Dekan login? | **Tidak.** Dekan hanya menandatangani dokumen cetak di luar sistem | Dekan bukan aktor sistem; KaLab mencatat pengesahan dan penolakan; pengesah tercatat = Dekan, pencatat = KaLab |
| Tahap Pemeriksa? | **Tidak perlu.** Memeriksa dan mengesahkan satu kesatuan; log pengesahan oleh Dekan/KaLab sudah menjadi bukti dokumen diperiksa | UC-23, AB-09, state `diperiksa`, `pemeriksa_id`, `tanggal_periksa`, `action_periksa` dihapus (bukan Lanjutan). Kolom "Diperiksa" di blok tanda tangan dokumen cetak cukup ada di kertas, tidak dicatat sistem |
| Renstra diisi lewat sistem? | **Tidak.** Renstra berlaku 5 tahun (draf: 2027–2031) | Renstra cukup dokumen unggahan yang disahkan |

## 7. Isu terbuka

Tidak ada untuk saat ini.
