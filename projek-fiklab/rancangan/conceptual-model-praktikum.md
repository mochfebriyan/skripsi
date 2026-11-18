# Conceptual Model Modul Pelaksanaan Praktikum

16 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF.** Langkah 9 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Bahan kerja**, tidak masuk proposal. Dasar design class diagram (langkah 10).

Diagram: [conceptual-model-praktikum.drawio](conceptual-model-praktikum.drawio), 4 halaman (CM-1 s.d. CM-4). Skrip pembuatnya: [tools/drawio/praktikum/conceptual_model.py](../tools/drawio/praktikum/conceptual_model.py) (mesin gambar dari `contoh-tata-kelola/conceptual_model.py`; prefiks `prk-cm` dan data diganti). `validate.py` dengan prefiks `prk-`: **OK** di keempat halaman. [cek_tampilan.py](../tools/drawio/praktikum/cek_tampilan.py): **0** garis menembus kotak lain. Tampilan dicek lewat ekspor PNG draw.io desktop (16 Nov 2026); label ujung asosiasi yang menimpa atribut dan satu garis generalisasi yang melewati kotak sudah dirapikan. **Gaya diubah ke polos hitam-putih** (17 Nov 2026, CLAUDE.md bagian 5): tanpa warna, huruf Times New Roman, judul dan catatan dipindah ke halaman `Catatan … (bahan kerja)` di akhir file. Diperiksa ulang 18 Nov 2026: `validate.py` dengan prefiks `prk-` **OK** di semua halaman; `cek_tampilan.py` **0** garis menembus kotak lain. Tampilan di draw.io belum dilihat ulang setelah perubahan gaya.

Sumber: kamus DTO dan katalog operasi di [ssd-praktikum.md](ssd-praktikum.md) bagian 3–4 dan temuan bagian 7; AB-PRK-01–34 di [expanded-use-case-praktikum.md](expanded-use-case-praktikum.md); state machine S1–S3 di [proses-bisnis-praktikum.md](proses-bisnis-praktikum.md); [kontrak-core.md](kontrak-core.md) versi 16 November 2026 (termasuk master aset dari kelompok Aset & Safety); rancangan SDM dan Tata Kelola di branch anggota lain (bagian 5.3); contoh referensi [conceptual-model-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/conceptual-model-tata-kelola.md).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Model konseptual menggambarkan informasi di ranah masalah, bukan solusi: hanya konsep, atribut, asosiasi. Tanpa method dan detail teknologi | §8.1 | Tidak ada `_inherit`, `Many2one`, `survey.survey`, atau nama model Odoo di diagram |
| Atribut hanya bertipe primitif atau enumerasi; konsep lain tidak boleh menjadi tipe atribut dan tidak ada atribut kunci asing (`sesi_id`) | §8.2, §10.4 | Semua rujukan antarkonsep berupa asosiasi bernama peran (`pengaju`, `pemutus`, `penyetuju`, `pengirim`, `penetap`, `pic`, …) |
| Atribut turunan `/nama` hanya dibaca dan punya definisi | §8.2.3 | `/is_terpublikasi`, `/tepat_waktu`, `/response_rate`, `/kriteria_tertinggi`, …; definisinya di catatan tiap halaman |
| Enumerasi untuk himpunan nilai tetap; enumerasi tidak berasosiasi | §8.2.4 | 18 enumerasi (status, jenis, kategori, aspek, peran) |
| Tipe primitif untuk nilai berpola | §8.2.5 | `Interval<T>` (§11.11), `Jam`, `Persen`, `URL`, `Berkas` |
| «unique» untuk nilai yang tidak boleh kembar | §8.3.1 | Kode Mata Kuliah; keunikan majemuk ditulis sebagai invarian |
| Peran bernama di ujung asosiasi, multiplisitas di kedua ujung; asosiasi dinamai lewat peran, bukan nama asosiasi | §8.4, §8.4.1 | Semua asosiasi |
| Asosiasi turunan satu arah, ditandai `/` | §8.4.3–8.4.4 | `/sesi_asal`, `/versi_berlaku [periode]`, `/survei_berikutnya` |
| Komposisi hanya untuk bagian–keseluruhan sungguhan; sisi keseluruhan bermultiplisitas 1 | §8.4.5 | Pemeriksaan ◆ Butir, Versi Modul ◆ Kebutuhan, Jurnal ◆ Presensi/Log Book, Survei ◆ Butir, Respons ◆ Jawaban, Evaluasi ◆ Kesimpulan/RTL, dan konsep kejadian terhadap induknya |
| Koleksi tanpa atribut sendiri cukup sebagai peran asosiasi; `{ordered}` bila urutan bermakna | §9.1 | `{ordered} versi`, `{ordered} log_book`, `{ordered} butir`, `{ordered} berkas` |
| Generalisasi hanya bila turunan berbagi properti dan masing-masing punya properti sendiri; instans tidak berganti kelas. Peran orang bukan subkelas | §9.2.1–9.2.2 | Pengajuan, ButirPemeriksaan, Jawaban. Dosen, laboran, asisten tetap satu konsep Personel dengan peran di asosiasi |
| Status yang hanya nilai = transisi stabil (atribut); data yang baru muncul saat status berubah = **konsep kejadian** 0..1, status menjadi turunan | §9.3.1–9.3.2 | Bagian 3 |
| Invarian untuk aturan yang tidak tergambar oleh multiplisitas | §9.4 | Kotak "Invarian" di setiap halaman, merujuk AB-PRK |
| Konsep dan atribut dicari dari teks use case dan argumen operasi SSD; use case kompleks lebih dulu | §10.2, §10.5 | Bagian 4 (cek terhadap kamus DTO) |
| Konsep dependen langsung berasosiasi wajib dengan pelengkapnya | §10.3–10.4 | Sesi–Kelas, Pemeriksaan–Sesi, Jurnal–Sesi, Butir–Pemeriksaan, RTL–Evaluasi |
| Pola analisis Bab 11 bila memberi manfaat | §11 | Bagian 3.2 |

---

## 2. Isi diagram

### CM-1 · Jadwal, sesi, dan pengajuan (PKG-15; perubahan sesi PKG-18)

| Konsep | Jenis | Isi dan alasan |
|---|---|---|
| **MataKuliah** | Master (Core) | «unique» `kode`, `nama`, `prodi`, `semester` (kontrak Core C-7) |
| **Kelas** | Master (Core) | `nama`, `jumlah_mahasiswa`; peran `dosen_koordinator` 0..1 dan `dosen` 1..* (C-8). Dipakai AB-PRK-09 dan 16 |
| **Sesi** | Transaksi (Core) | `pertemuan_ke`, `jenis_pertemuan`, `moda`, `tanggal`, `jam: Interval<Jam>`, `status` {terjadwal, terlaksana, batal} (I-1). Turunan: `/is_terpublikasi`, `/is_ditunda`, `/is_diganti`, `/is_terlewat`, `/berasisten`, `/melebihi_kapasitas`, `/memenuhi_pkg15…18` |
| **PenetapanJadwal** | Turunan DokumenDisahkan | Satu per Periode (AB-PRK-05). `/tanggal_publikasi` = tanggal sah (AB-PRK-06); `/jumlah_sesi`. Status, pengesahan, dan riwayatnya diwarisi dari konsep **DokumenDisahkan** milik Tata Kelola, tidak digambar ulang |
| ***Pengajuan*** | Abstrak | Induk PemakaianLab dan PerubahanSesi; keduanya mengikuti S2. `tanggal_ajukan`, `/status`; peran `pengaju` |
| **PemakaianLab** | Turunan Pengajuan | `keperluan`, `nama_pemohon`, `unit_pemohon`, `tanggal`, `jam`; `ruang` 1. Pemohon tanpa akun; `pengaju` = laboran yang mencatat |
| **PerubahanSesi** | Turunan Pengajuan | `jenis` {pindah, daring, batal}, `alasan`; `sesi` 1 (sesi asal) |
| **UsulanPengganti** | Bagian PerubahanSesi | `tanggal`, `jam`, `ruang`. Ada hanya untuk jenis pindah, jadi dipisah supaya PerubahanSesi tidak punya atribut opsional bergantung jenis (§11.2) |
| **KeputusanPengajuan** | Kejadian | `tanggal_putus`, `hasil` {disetujui, ditolak}, `alasan`, `karena_bentrok` (KF-PRK-09); peran `pemutus` (KaLab, AB-PRK-10) dan `sesi_pengganti` 0..1 |
| **Penarikan (O)** | Kejadian | `tanggal` (KF-PRK-47, AB-PRK-11) |
| Interval&lt;T&gt; | «primitive» | `awal`, `akhir`, invarian `awal < akhir` |

Stub: Periode, Ruang, Personel (Core), DokumenDisahkan (Tata Kelola).

### CM-2 · Versi modul dan kesiapan sesi (PKG-15 C4, PKG-16, PKG-17)

| Konsep | Jenis | Isi dan alasan |
|---|---|---|
| **VersiModul** | Transaksi | `nomor_versi`, `berkas`, `tautan_leads`, `rubrik`, `tanggal_terbit`, `status` {draf, berlaku, diganti}; `mata_kuliah` 1, `periode` 1, `penerbit` 1. MataKuliah punya `/versi_berlaku [periode]` (AB-PRK-07) |
| **KebutuhanSoftware** | Bagian VersiModul | `nama`, `versi`, `berbayar` (PKG-16 S3) |
| **KebutuhanBahan** | Bagian VersiModul | `jumlah_per_mahasiswa`; `bahan` 1 → master **Bahan** Core (C-13) |
| **PemeriksaanKesiapan** | Turunan RekamanBukti | 0..1 per Sesi (AB-PRK-13). `waktu_periksa`, `keputusan`, `/tepat_waktu` (S1), `/jumlah_pc_tersedia` (O, isian awal `jumlah_berfungsi`). Pemeriksa = `pelapor` warisan |
| ***ButirPemeriksaan*** | Abstrak, bagian Pemeriksaan | `hasil` {baik, diperbaiki, bermasalah}, `keterangan` |
| **ButirUtilitas** | Turunan butir | `kategori` {jaringan, listrik, proyektor_audio} |
| **ButirStasiunKerja** | Turunan butir | `jumlah_berfungsi`, `/jumlah_dibutuhkan` (S2) |
| **ButirSoftware** | Turunan butir | `lisensi_sah` (S3); `kebutuhan` 1 |
| **ButirBahan** | Turunan butir | `jumlah_tersedia`, `kondisi_baik`, `berlabel`, `tanggal_kedaluwarsa` [0..1] (KF-PRK-19), `/jumlah_dibutuhkan` (PKG-17 B1–B2); `kebutuhan` 1 |
| **SubstitusiBahan** | Kejadian | `alasan`, `/status_persetujuan`; `bahan_pengganti` 1 (B3) |
| **PersetujuanSubstitusi** | Kejadian | `waktu`; `penyetuju` = dosen kelas (AB-PRK-16) |
| Alat | Stub (Core C-10, diisi kelompok Aset) | Hanya dibaca (O, KF-PRK-52). Sesi mendapat `/alat_tidak_tersedia` (turunan): alat di ruang sesi yang tidak tersedia untuk sesi itu. Menjadi peringatan pada butir kategori padanannya, bukan butir sendiri (ditambahkan 16 Nov 2026, temuan 5.2 no. 2) |

### CM-3 · Pelaksanaan sesi (PKG-18) dan penilaian individual (PKG-19)

| Konsep | Jenis | Isi dan alasan |
|---|---|---|
| **JurnalSesi** | Turunan RekamanBukti | 0..1 per Sesi (AB-PRK-17). `jam_aktual`, `topik`, `jumlah_hadir`, `tautan_presensi_simpel`, `kendala`, `/status`, `/durasi_memenuhi`; `versi_modul_dipakai` 1. Foto = `bukti` warisan |
| **PengirimanJurnal** | Kejadian | `waktu_kirim`, `/terlambat` (O); peran `pengirim` |
| **PresensiPetugas** | Bagian Jurnal | `peran` {dosen, laboran, asisten}, `kehadiran` {penuh, sebagian, tidak}, `/sesuai_penugasan` (O); `petugas` → Personel (I-8) |
| **EntriLogBook** | Bagian Jurnal | `waktu`, `uraian`; `{ordered} 1..*` (C5) |
| BarisPenugasan | Stub (SDM, PKG-04) | Baris Surat Tugas SDM: asisten → `kelas_sasaran`, laboran → ruang, dengan peran dan rentang berlaku (KF-SDM-10). Sesi mendapat `/petugas_ditugaskan` (turunan): personel pada baris dari Surat Tugas disahkan yang berlaku pada tanggal sesi, asisten lewat kelas sesi, laboran lewat ruang sesi. Dipakai `/berasisten` dan `/sesuai_penugasan` (I-7) |
| **PenilaianKelas** | Turunan RekamanBukti | 0..1 per Kelas (AB-PRK-23). `tautan_leads`, `/ada_rubrik`, `/berbukti` |
| **BarisNilai (O)** | Bagian Penilaian | `nim` (tanpa nama), `jumlah_tugas_individual`, `nilai_akhir`, `ada_umpan_balik`, `remedial`, `/lengkap` (P1–P4) |
| **BerkasNilai (O)** | Bagian Penilaian | `waktu_impor`, `berkas`; `{ordered}` sebagai riwayat impor (AB-PRK-24) |
| **PengaturanPraktikum** | «singleton» | `ambang_durasi`, `batas_hari_jurnal`, `sesi_daring_sah`, `batas_lulus = 60` (UC-PRK-28) |

### CM-4 · Survei kepuasan pengguna (PKG-20)

| Konsep | Jenis | Isi dan alasan |
|---|---|---|
| **Survei** | Transaksi | `judul`, `jenis_responden`, `populasi`, `target_response_rate`, `masa_buka: Interval<Date>`; turunan `/status`, `/status_buka`, `/jumlah_responden`, `/response_rate`, `/kriteria_tertinggi`; `/survei_berikutnya` |
| **PenetapanSurvei** | Kejadian | `tanggal`; `penetap` (AB-PRK-26, K1) |
| **ButirSurvei** | Bagian Survei | `urutan`, `pertanyaan`, `jenis` {skala, terbuka}, `aspek` (6 aspek), `/rerata` |
| **Respons** | Transaksi | `waktu`; **tanpa** asosiasi ke Personel (anonim, AB-PRK-28) |
| ***Jawaban*** → JawabanSkala, JawabanTerbuka | Abstrak + turunan | `nilai` (1–5) atau `teks`; `butir` 1 |
| **EvaluasiSurvei** | Turunan RekamanBukti | 0..1 per Survei (AB-PRK-29) |
| **KesimpulanAspek** | Bagian Evaluasi | `aspek`, `kesimpulan` (argumen `kesimpulan_aspek*` di `catat_evaluasi_survei`) |
| **RencanaTindakLanjut** | Bagian Evaluasi | `aspek`, `prioritas`, `tindakan`, `tenggat`, `/rerata_sebelum`, `/rerata_sesudah`; `pic` 1 |
| **PenilaianEfektivitas** | Kejadian | `tanggal`, `efektif` {ya, sebagian, tidak}, `catatan`; `penilai` (K4, AB-PRK-30) |

---

## 3. Keputusan pemodelan

### 3.1 Struktur

| Keputusan | Alasan | Bab |
|---|---|---|
| **Pengajuan abstrak** dengan PemakaianLab dan PerubahanSesi | Keduanya mengikuti S2 (diajukan → disetujui/ditolak/ditarik) dan memakai `pengaju`, Keputusan, dan Penarikan yang sama; masing-masing punya atribut sendiri. Ini cikal bakal satu *mixin* pengajuan di langkah 10 (sudah diisyaratkan di SSD bagian 5) | §9.2.1 |
| **Kejadian sebagai konsep 0..1**: KeputusanPengajuan, Penarikan, PengirimanJurnal, SubstitusiBahan, PersetujuanSubstitusi, PenetapanSurvei, PenilaianEfektivitas | Data itu baru ada setelah transisi tertentu (tanggal putus, alasan, pemutus, waktu kirim, penyetuju, penetap). Atribut opsional akan membuat konsep induk tidak kohesif dan butuh invarian berpasangan (Gambar 11–2) | §9.3.2, §11.2 |
| **Status turunan bila bisa dihitung dari kejadian**: `/status` Pengajuan, Jurnal, Survei, `/status_persetujuan` | Sama dengan Gambar 9–23: status *invoice* dihitung dari ada tidaknya *payment*. Tidak ada dua sumber kebenaran untuk satu fakta | §9.3.2 |
| **Status yang disimpan**: `Sesi.status` (3 nilai, kontrak Core I-1) dan `VersiModul.status` | Sesi `batal` tanpa pengganti dan `terlaksana` tidak bisa dihitung dari satu kejadian saja tanpa membuat konsep baru; nilai sudah disepakati di Core. Versi Modul diganti oleh versi lain, bukan oleh kejadian | §9.3.1 |
| **ButirPemeriksaan abstrak dengan empat turunan** | Setiap kategori punya atribut sendiri (`jumlah_berfungsi`, `lisensi_sah`, `jumlah_tersedia`/`berlabel`) dan butir tidak berganti kategori. Kategori utilitas (jaringan, listrik, proyektor) tidak punya atribut berbeda, jadi satu turunan dengan atribut `kategori` (Gambar 9–15) | §9.2.1 |
| **Jawaban abstrak** dengan skala dan terbuka | Atribut nilai berbeda; superkelas menggeneralisasi asosiasi ke ButirSurvei (seperti `HostingState` di Gambar 9–26) | §9.2.1 |
| **Peran orang tidak menjadi subkelas** | Dosen, laboran, asisten, KaLab, pemutus, penyetuju adalah peran Personel di asosiasi tertentu; orang yang sama bisa memegang beberapa peran | §9.2.2 |
| **UsulanPengganti dipisah** dari PerubahanSesi | Hanya ada untuk jenis pindah; menghindari tiga atribut opsional bergantung `jenis` | §11.2 |
| **Respons tidak berasosiasi dengan Personel** | Respons anonim adalah aturan bisnis (AB-PRK-28); model sendiri yang menjamin, bukan pengecekan | §11.13 |
| **Rekaman bukti** (Pemeriksaan, Jurnal, Penilaian Kelas, Evaluasi Survei) menurun dari **RekamanBukti** Tata Kelola | Atribut dan aturan AB-PRK-31 (tidak dihapus, hanya dikoreksi) sama dengan rekaman bukti modul lain; cikal bakal `labfik.evidence.mixin` | §9.2.1 |
| **PenetapanJadwal menurun dari DokumenDisahkan** Tata Kelola | Pengesahan jadwal memakai alur Tata Kelola (UC-01–05); tidak digambar ulang | §9.2.1 |
| **PengaturanPraktikum sebagai «singleton»** tanpa asosiasi | Nilai ambang adalah variabel sistem yang dibaca atribut turunan (seperti `Sismob.assessment_term()` di Gambar 8–3), bukan informasi tentang konsep lain | §8.2.2, §8.3.2 |
| **Status monev tidak menjadi konsep** | Hanya hasil hitung: `/memenuhi_pkg15…18` per Sesi, `/berbukti` per Kelas, `/lengkap` per baris nilai, `/kriteria_tertinggi` per Survei; persentase dihitung saat dibaca (`status_monev()`) | §8.2.3 |
| **Rekaman konflik tidak menjadi konsep** | Laporan KF-PRK-11 disusun dari Keputusan ditolak dengan `karena_bentrok` (KF-PRK-09) dan PerubahanSesi yang disetujui. Bentrok yang ditolak saat impor tidak tersimpan karena Sesi belum dibuat **[ASUMSI; KONFIRMASI pembimbing]** | — |
| **Koreksi rekaman tidak menjadi konsep** | Cukup dilacak sebagai riwayat perubahan (KNF-PRK-07), sama dengan Tata Kelola | — |
| **Petugas yang ditugaskan dibaca dari SDM sebagai asosiasi turunan**, bukan penugasan per sesi | SDM menugaskan asisten per kelas dan laboran per ruang dengan rentang berlaku (KF-SDM-10, 12). Menyalin penugasan ke setiap Sesi akan menjadi asosiasi redundan (Gambar 8–16). Dosen dibaca dari Kelas.dosen, karena SDM tidak menugaskan dosen | §8.4.3 |
| **Pola mingguan kelas tidak disimpan** | Hanya dipakai saat impor untuk membangkitkan 16 tanggal; setelah itu Sesi yang bertanggal adalah sumber kebenaran | — |

### 3.2 Pola analisis (Bab 11)

| Pola | Dipakai di | Manfaat |
|---|---|---|
| *Range/Interval* (§11.11) | `Sesi.jam`, `PemakaianLab.jam`, `UsulanPengganti.jam`, `JurnalSesi.jam_aktual`, `Survei.masa_buka` | Pasangan awal–akhir yang saling terkait menjadi satu atribut. Aturan "akhir > awal" (AB-PRK-18, sebagian AB-PRK-26) dan cek "beririsan" untuk bentrok (AB-PRK-01) cukup ditulis sekali di tipe Interval |
| *Superseding* (§11.9.2) | `/sesi_asal` – `/is_diganti` (Sesi pengganti); VersiModul berlaku → diganti | Sesi dan versi lama tetap tersimpan sebagai riwayat, tidak dihapus |
| *Specification class* (§11.3) | KebutuhanBahan → Bahan (master Core); KebutuhanSoftware → ButirSoftware | Nama dan satuan bahan tidak diketik ulang di setiap modul; butir pemeriksaan mengambil spesifikasi dari versi modul |
| *History* (§11.12.2) | `{ordered} versi` per Mata Kuliah, `{ordered} berkas` nilai | Riwayat versi dan berkas impor tetap terbaca |
| *Effectivity* (§11.12.1) | Periode pada Kelas, VersiModul, PenetapanJadwal, Survei; `masa_buka` | Masa berlaku dibaca dari periode |
| *Organizational hierarchy*, *Account/transaction*, *Quantity*, *Measure* | Tidak dipakai | Tidak ada kebutuhan yang menuntutnya; jumlah bahan cukup Real + satuan di Bahan |

---

## 4. Cek kelengkapan terhadap kamus DTO

Setiap isi kamus DTO di [ssd-praktikum.md](ssd-praktikum.md) bagian 4 harus punya tempat di model (CLAUDE.md langkah 9).

| DTO | Tempat di model | Catatan |
|---|---|---|
| `dto_baris_jadwal` | MataKuliah (kode, nama, prodi), Kelas (nama, jumlah_mahasiswa, dosen), Sesi (ruang, jam) | `hari` dan tanggal pertemuan pertama hanya argumen pembangkitan; tidak disimpan (bagian 3.1) |
| `dto_pratinjau_impor`, `dto_ringkasan_jadwal`, `dto_waktu_ruang`, `dto_konflik` | Dihitung dari Sesi, Ruang, PemakaianLab | Tidak disimpan |
| `dto_sesi_ringkas`, `dto_status_sesi` | Sesi + turunannya; `ada_pemeriksaan`, `ada_jurnal` = ada tidaknya tautan; `sesi_pengganti` = KeputusanPengajuan.sesi_pengganti; `waktu_kirim_jurnal`, `jurnal_terlambat` = PengirimanJurnal | |
| `dto_penetapan_jadwal` | PenetapanJadwal + DokumenDisahkan dan Pengesahan (Tata Kelola) | |
| `dto_laporan_jadwal` | Sesi + PemakaianLab dengan /status disetujui; penolakan = KeputusanPengajuan ditolak | `kegiatan` = MK/kelas atau `keperluan` |
| `dto_versi_modul`, `dto_info_modul` | VersiModul, KebutuhanSoftware, KebutuhanBahan, Bahan; `riwayat_versi` = `{ordered} versi`; `pengguna_mengampu` dihitung dari Kelas.dosen | **Berubah:** `nama` dan `satuan` bahan dari master Bahan Core (temuan 5.2 no. 1) |
| `dto_pemakaian`, `dto_perubahan`, `dto_pengganti` | PemakaianLab, PerubahanSesi, UsulanPengganti; `dto_pengganti` = Sesi pengganti yang dibangkitkan | |
| `dto_pengajuan_ringkas`, `dto_rincian_pengajuan` | Pengajuan + turunannya, KeputusanPengajuan; `ringkasan` dihitung | |
| `dto_form_kesiapan` | Dihitung dari /versi_berlaku dan kategori tetap; `jumlah_mahasiswa` dari Kelas; (O) `alat_tidak_tersedia` = Sesi `/alat_tidak_tersedia` → Alat (Core), `jumlah_pc_tersedia` = PemeriksaanKesiapan `/jumlah_pc_tersedia`; `workstation_count` dari Ruang (Core) | Tidak disimpan sampai `catat_pemeriksaan()`. Bagian Alat ditambahkan 16 Nov 2026 (KF-PRK-52) |
| `dto_hasil_butir`, `dto_pemeriksaan`, `dto_substitusi` | ButirPemeriksaan dan turunannya, SubstitusiBahan, PersetujuanSubstitusi, PemeriksaanKesiapan; `substitusi_menunggu` dihitung | `kondisi` → `kondisi_baik: Boolean` (analisis PKG-17: baik/tidak). `bahan_pengganti` → Bahan |
| `dto_konteks_jurnal` | Sesi, /versi_berlaku, `/petugas_ditugaskan` (dari BarisPenugasan SDM), Kelas, `/berasisten` | `peran` petugas = peran di baris penugasan |
| `dto_jurnal`, `dto_rincian_jurnal` | JurnalSesi, PresensiPetugas, EntriLogBook, PengirimanJurnal; `foto` = `bukti` warisan; `petugas_tidak_sesuai` = presensi dengan /sesuai_penugasan salah | |
| `dto_kelengkapan`, `dto_laporan_pelaksanaan` | Dihitung | |
| `dto_penilaian_kelas`, `dto_baris_nilai`, `dto_status_praktikan` | PenilaianKelas, BarisNilai; `p1`–`p4`, `lengkap` dihitung; `jumlah_baris_nilai` dihitung | |
| `dto_survei`, `dto_butir_survei`, `dto_survei_ringkas`, `dto_formulir_survei` | Survei, ButirSurvei; `tanggal_buka`/`tanggal_tutup` = `masa_buka` | |
| `dto_jawaban` | Respons, JawabanSkala, JawabanTerbuka | |
| `dto_rekap_survei` | Turunan Survei dan ButirSurvei; `rerata_aspek` dihitung saat dibaca; `jawaban_terbuka` = JawabanTerbuka | |
| `dto_rtl`, `dto_efektivitas`, `dto_banding_rtl` | RencanaTindakLanjut, PenilaianEfektivitas | `kesimpulan_aspek*` (argumen `catat_evaluasi_survei`) = KesimpulanAspek |
| `dto_status_survei`, `dto_laporan_survei`, `dto_status_monev` | Dihitung dari model | «report» |
| `dto_mata_kuliah`, `dto_kelas` | MataKuliah, Kelas | `dto_kelas.dosen` mencakup dua peran: `dosen_koordinator` dan `dosen` (C-8) |
| `dto_pengaturan` | PengaturanPraktikum | |
| `dto_koreksi` | Pelacakan perubahan | Tidak menjadi konsep |

**Hasil:** semua isi DTO punya tempat. Ada dua informasi di model yang tidak ada di DTO: `penetap`/`tanggal` PenetapanSurvei dan `pengirim` PengirimanJurnal. Keduanya diisi dari `user_id` dan tanggal saat operasi (`tetapkan_survei`, `kirim_jurnal`), jadi tidak perlu operasi baru. `penetap` diperlukan AB-PRK-26 (penetap berwenang, tanggal tetap < tanggal buka; analisis PKG-20 K1).

---

## 5. Cek silang

### 5.1 Terhadap aturan, status, dan kriteria

- **Aturan bisnis.** Setiap AB-PRK merujuk atribut atau asosiasi yang ada. AB-01 → `jam: Interval`, Ruang, `/status` PemakaianLab. AB-02 → invarian (kelas, pertemuan_ke). AB-03 → `/melebihi_kapasitas`. AB-04 → PenetapanJadwal, JurnalSesi. AB-05/06 → PenetapanJadwal, `/is_terpublikasi`. AB-07 → `/versi_berlaku`. AB-08 → invarian VersiModul. AB-09 → Kelas.dosen, `penerbit`. AB-10 → Keputusan.alasan, `pemutus`. AB-11 → Penarikan. AB-12 → `jenis`, UsulanPengganti, `sesi_pengganti`. AB-13 → Sesi 1 — 0..1 Pemeriksaan, `/tepat_waktu`. AB-14 → Kebutuhan*, ButirSoftware.lisensi_sah. AB-15 → `keputusan`, `hasil`. AB-16 → Substitusi, Persetujuan, `penyetuju`. AB-17 → Sesi 1 — 0..1 Jurnal. AB-18 → Interval. AB-19 → Presensi, LogBook, `jumlah_hadir`, `versi_modul_dipakai`, `/berasisten`. AB-20 → `/sesuai_penugasan`. AB-21 → `/terlambat`. AB-22 → `/durasi_memenuhi`, `moda`, `/sesi_asal`, Periode. AB-23 → PenilaianKelas.tautan_leads. AB-24 → BarisNilai.nim, BerkasNilai. AB-25 → `/lengkap`. AB-26 → ButirSurvei.aspek/jenis, PenetapanSurvei. AB-27 → PenetapanSurvei, `masa_buka`. AB-28 → Respons tanpa Personel, `masa_buka`. AB-29 → EvaluasiSurvei, RTL.`pic`. AB-30 → PenilaianEfektivitas, `/survei_berikutnya`. AB-31 → RekamanBukti. AB-32–34 → atribut `/memenuhi_*`, `/berbukti`, `/lengkap`, `/kriteria_tertinggi`.
- **Status.** S1 Sesi = `StatusSesi` {terjadwal, terlaksana, batal} + turunan; S2 = `StatusPengajuan` {diajukan, disetujui, ditolak, ditarik}; S3 = `StatusSurvei` {draf, ditetapkan, dievaluasi, siklus_selesai}; Versi Modul {draf, berlaku, diganti} dan Jurnal {draf, terkirim} sama dengan proses bisnis bagian 3.4. Nama konsep sama dengan dokumen sebelumnya, kecuali "Rencana Pemakaian Lab" di matriks CRUDL use case yang di sini ditulis **PemakaianLab** (sama dengan nama di SSD).
- **Kriteria instrumen.** PKG-15 C1 (PenetapanJadwal, `/is_terpublikasi`), C2 (Sesi.jam + ruang, PemakaianLab), C3 (Kelas.jumlah_mahasiswa, Ruang.kapasitas), C4 (VersiModul berlaku, `tanggal_terbit`). PKG-16 S1 (`/tepat_waktu`), S2 (ButirUtilitas, ButirStasiunKerja), S3 (ButirSoftware.lisensi_sah), S4 (`keputusan`). PKG-17 B1 (ButirBahan dari KebutuhanBahan), B2 (`jumlah_tersedia`, `kondisi_baik`, `berlabel`), B3 (Substitusi + Persetujuan). PKG-18 C1 (Jurnal + Pengiriman), C2 (`moda`, `sesi_daring_sah`, Sesi pengganti), C3 (`jam_aktual`, `ambang_durasi`), C4–C5 (Presensi, `jumlah_hadir`, LogBook, `versi_modul_dipakai`). PKG-19 P1–P4 (BarisNilai, VersiModul.rubrik, `batas_lulus`), kelas berbukti (PenilaianKelas). PKG-20 K1 (PenetapanSurvei, populasi, `masa_buka`), K2 (ButirSurvei.aspek/jenis, target), K3 (Respons, `/response_rate`, EvaluasiSurvei, KesimpulanAspek, RTL), K4 (PenilaianEfektivitas). Setiap kriteria punya rekaman bukti di model.
- **Matriks Konsep × CRUDL** (use case bagian 6): setiap konsep di sana ada di model. Konsep baru di model (kejadian, butir, kebutuhan) adalah bagian dari konsep yang sudah ada di matriks.

### 5.2 Temuan dan ketidaksesuaian dengan langkah sebelumnya

| No | Temuan | Tindakan |
|---|---|---|
| 1 | Kontrak Core 16 November menambah master **Bahan** (C-13) dari kelompok Aset & Safety. Kamus DTO masih menulis bahan sebagai teks (`nama`, `satuan`) di `dto_versi_modul` dan `bahan_pengganti` di `dto_hasil_butir` | KebutuhanBahan dan SubstitusiBahan merujuk Bahan. Kamus DTO di [ssd-praktikum.md](ssd-praktikum.md) diperbarui. Bila master Bahan tidak disetujui masuk Core, kembali ke teks bebas **[KONFIRMASI kelompok]** |
| 2 | Aturan pakai bersama domain aset di kontrak Core menulis bahwa Praktikum mengecek ketersediaan PC/alat lewat `labfik.alat` (C-10, `check_ketersediaan_sesi()`). Versi awal model ini tidak memakai Alat karena analisis PKG-16 memeriksa per kategori di tingkat ruang | **Diubah 16 Nov 2026** (keputusan Herrens: ikuti ketentuan Core dengan prinsip *sweet spot*): Alat dimodelkan sebagai stub master Core yang **hanya dibaca**, lewat asosiasi turunan Sesi `/alat_tidak_tersedia` dan atribut turunan `/jumlah_pc_tersedia` (lapis Pelengkap, KF-PRK-52). Butir tetap per kategori; tidak ada butir per unit, dan hasil tetap ditetapkan laboran (I-13) |
| 3 | `kondisi` bahan di kamus DTO belum punya nilai | Mengikuti analisis PKG-17 (baik/tidak): `kondisi_baik: Boolean` |
| 4 | `dto_kelas.dosen` tidak membedakan dosen koordinator dan dosen kelas, padahal kontrak Core C-8 punya keduanya dan AB-PRK-09 memakai keduanya | Model memakai dua peran. DTO cukup dibaca sebagai keduanya; tidak mengubah operasi |
| 5 | Matriks CRUDL use case memakai nama "Rencana Pemakaian Lab"; SSD dan model memakai "PemakaianLab" | Nama baku: **Pemakaian Lab**. Label matriks use case dan judul state machine S2 disamakan saat audit 16 Nov 2026; analisis PKG-15 (Langkah 0) tetap memakai nama lama sebagai riwayat |
| 6 | Versi awal CM-3 menulis stub "PenugasanPetugas" sebagai penugasan **per sesi**. Rancangan SDM menugaskan asisten per kelas dan laboran per ruang dengan rentang berlaku (bagian 5.3) | **Dibetulkan:** stub BarisPenugasan + asosiasi turunan `/petugas_ditugaskan` di Sesi. Kesalahan sendiri, ditemukan lewat cek silang |
| 8 | Saat menyusun DCD ditemukan dua isian KF Inti yang tidak tertangkap di CM versi pertama: penanda penolakan **karena bentrok** (KF-PRK-09, bahan laporan konflik KF-PRK-11) dan **tanggal kedaluwarsa** bahan (KF-PRK-19). Keduanya juga tidak ada di kamus DTO | Ditambahkan: `KeputusanPengajuan.karena_bentrok`, `ButirBahan.tanggal_kedaluwarsa [0..1]`. Kesalahan sendiri (langkah 8–9) |
| 7 | Teks "petugas yang ditugaskan (dari SDM)" di `dto_konteks_jurnal` dan AB-PRK-20 tidak menyebut cara pencocokannya | Kini jelas: asisten lewat kelas sesi, laboran lewat ruang sesi, berlaku pada tanggal sesi. AB-PRK-20 tidak berubah bunyinya |

Tidak ada nomor KF, UC, AB, atau operasi yang berubah.

### 5.3 Cek silang ke branch anggota lain (16 November 2026)

Dibaca setelah `git fetch`, tanpa mengubah apa pun di branch itu: `origin/febriyan-skripsi` (`2df910f`), `origin/zahir-skripsi` (`322c9ac`), `origin/main` (`a449ec9`), `origin/shared-to-aset-safety` (`36a56b8`). `kontrak-core.md` di `febriyan-skripsi`, `zahir-skripsi`, dan `main` sama dengan salinan di branch ini (`shared-to-aset-safety` tidak dibandingkan).

| Isu | Ditemukan di | Jawaban | Dampak di sini |
|---|---|---|---|
| Bentuk penugasan petugas | SDM: `kebutuhan-sdm.md` KF-SDM-09–12, `kontrak-core-sdm.md` bagian 4.3 | Surat Tugas per periode (disahkan) berisi baris asisten → kelas, laboran → ruang, `berlaku_mulai`/`berlaku_sampai`. Kehadiran petugas per sesi dinyatakan milik PKG-18 | CM-3 dibetulkan (temuan 6) |
| Siapa ditugaskan sebagai petugas | SDM `kontrak-core-sdm.md` bagian 4.3 (`peran` {asisten, laboran}) | Dosen tidak ditugaskan SDM | Dosen sesi dibaca dari `Kelas.dosen` |
| *Hook* `_setelah_disahkan()` untuk jadwal | Tata Kelola: `design-class-tata-kelola.md` bagian 4 | *Hook* itu "tidak diisi model mana pun"; tetap disediakan untuk modul lain | `/is_terpublikasi` dihitung, tidak butuh *hook*. Yang perlu dibetulkan hanya tabel kontrak Core bagian 5 (isu 2) |
| RekamanBukti dan DokumenDisahkan | Tata Kelola: `design-class-tata-kelola.md` bagian 2 | Masing-masing menjadi `evidence.mixin` dan `approval.mixin`; atribut RekamanBukti = tanggal, pelapor, bukti, keterangan | Sama dengan stub di CM-1 s.d. CM-4 |
| Master Bahan | `main`: `tools/drawio/core/model_core.py` | `labfik.bahan` diberi label "Bahan Praktikum (habis pakai)" | Memperkuat keputusan KebutuhanBahan → Bahan (temuan 1) |
| Alat untuk PKG-16 | `main`: `pemetaan-package-instrumen.md` dan brief bersama ("Alat, Bahan · PKG-07 → 05, 07, 08, 10, 11, 12, 16, 17, 21") | Pemetaan memang mencatat PKG-16 memakai Alat | Temuan 2 diperhalus: bukan konflik. Sejak 16 Nov 2026 Alat dibaca sebagai Pelengkap (stub di CM-2) |
| Status Sesi di SDM | SDM `kontrak-core-sdm.md` bagian 2.3: `state` 6 nilai (S1 lama Praktikum) dan asumsi "sesi `terpublikasi` yang tanggalnya lewat dianggap terlaksana". `kebutuhan-sdm.md` KF-SDM-12 sudah memakai "sesi terjadwal yang tanggalnya lewat" | Tabel di `kontrak-core-sdm.md` bertentangan dengan keputusan Core I-1 (3 nilai) | Tidak mengubah model ini. Perlu disampaikan ke Zahir (isu 7; rekomendasi dibetulkan saat audit 16 Nov 2026) |
| Rekaman konflik, jenis responden survei | Semua branch | Tidak ada jawaban | Tetap terbuka |

---

## 6. Perubahan dibanding versi sebelumnya

Belum ada versi sebelumnya untuk modul ini. Revisi audit 16 Nov 2026 ([audit-praktikum.md](audit-praktikum.md)): invarian CM-1 menjadi "paling banyak satu PenetapanJadwal yang tidak dicabut per Periode" (AB-PRK-05); isu 7 dibetulkan (SDM tidak dapat membaca `is_terpublikasi`). Konsep dan asosiasi tidak berubah.

---

## 7. Temuan untuk langkah 10 (design class diagram)

| Konsep (CM) | Usulan di DCD |
|---|---|
| PenetapanJadwal ← DokumenDisahkan | `_inherit = ['labfik.approval.mixin']`; `_jenis_dokumen()` = `jadwal_praktikum`; `_cek_kelengkapan()` = setiap kelas periode punya Sesi (AB-PRK-05) |
| Pengajuan (abstrak) + KeputusanPengajuan + Penarikan | *Mixin* pengajuan di `labfik_praktikum` (`AbstractModel`): `state`, `pengaju_id`, `tanggal_putus`, `pemutus_id`, `alasan`; Template Method `action_putuskan()` dengan *hook* `_efek_disetujui()` yang diisi PemakaianLab dan PerubahanSesi. Kejadian 0..1 cukup menjadi field di model yang sama, karena tidak berulang (beda dengan `approval.log` yang menyimpan banyak kejadian) |
| PengirimanJurnal, PersetujuanSubstitusi, PenetapanSurvei, PenilaianEfektivitas | Sama: field di model induk + pelacakan `mail.thread`; status turunan menjadi `state` tersimpan bila dipakai untuk filter dan *record rule* |
| RekamanBukti (Pemeriksaan, Jurnal, Penilaian Kelas, Evaluasi Survei) | `_inherit = ['labfik.evidence.mixin']`; AB-PRK-31 dari `unlink()` mixin |
| ButirPemeriksaan + 4 turunan | Satu model butir dengan `kategori` Selection dan field per kategori yang tampil sesuai kategori, **atau** model terpisah. Diputuskan di langkah 10 dengan membandingkan kerumitan (prinsip *sweet spot*) |
| Interval&lt;T&gt; | Dua field (`jam_mulai`, `jam_selesai`; `tanggal_buka`, `tanggal_tutup`) + satu `@api.constrains` bersama; cek beririsan dalam satu method `cek_bentrok()` |
| `/sesi_asal` (turunan di CM) | Disimpan sebagai `sesi_asal_id` di `labfik.sesi` (sudah di kontrak Core C-9), karena Core tidak bisa membaca PerubahanSesi yang ada di `labfik_praktikum` |
| `/is_terpublikasi`, `/is_ditunda`, `/is_terlewat`, `/berasisten`, `/memenuhi_*` di Sesi | Membutuhkan PenetapanJadwal, PerubahanSesi, Jurnal (di `labfik_praktikum`) dan Penugasan (di `labfik_sdm`). Jadi field `compute` ini ditambahkan **oleh `labfik_praktikum`** lewat `_inherit = 'labfik.sesi'`, bukan di Core. Hanya `is_diganti` yang bisa dihitung di Core. Lihat isu terbuka no. 2 |
| Survei, ButirSurvei, Respons, Jawaban | `survey.survey` (+ `labfik.criteria.mixin`), `survey.question` (+ `aspek`), `survey.user_input` dan `survey.user_input.line` bawaan addon `survey` |
| EvaluasiSurvei, KesimpulanAspek, RTL | Model baru `labfik.praktikum.*`; RTL One2many dari evaluasi |
| PengaturanPraktikum | `res.config.settings` + `ir.config_parameter` |
| Bahan | Many2one ke `labfik.bahan` (Core C-13) |

---

## 8. Isu terbuka

- [ ] Rekaman konflik (PKG-15 bukti 5) disusun dari penolakan `karena_bentrok` dan perubahan sesi; bentrok saat impor tidak tersimpan **[ASUMSI; KONFIRMASI pembimbing]**
- [ ] Kontrak Core C-9 menyebut `is_terpublikasi`, `is_ditunda`, `is_terlewat` sebagai field hitung di `labfik.sesi`, dan bagian 5 menyebut *hook* `_setelah_disahkan()` "menandai Sesi terpublikasi". Keduanya perlu disesuaikan: field itu ditambahkan `labfik_praktikum` sebagai pemilik Sesi, dan *hook* tidak lagi diperlukan karena `is_terpublikasi` dihitung (DCD Tata Kelola pun tidak mengisi *hook* itu). Disampaikan ke Febriyan sebagai pemilik [kontrak-core.md](kontrak-core.md) **[KONFIRMASI Febriyan]**
- [ ] Master Bahan (C-13) disetujui masuk Core; bila tidak, KebutuhanBahan kembali memakai teks **[KONFIRMASI kelompok]**
- [ ] Kontrak Core C-10 menulis pemakai pemeriksaan kesiapan sebagai "PKG-15/18"; pemeriksaan kesiapan adalah PKG-16. Rumus `workstation_count` ditetapkan kelompok Aset; `/jumlah_pc_tersedia` di model ini hanya menghitung alat jenis PC yang tersedia (temuan 5.2 no. 2) **[KONFIRMASI Febriyan; KONFIRMASI kelompok Aset]**
- [ ] Nilai `JenisResponden` {praktikan, dosen, asisten} **[ASUMSI]**; analisis PKG-20 baru menyebut "jenis responden sasaran"
- [ ] Pembatalan penetapan survei (O) menghapus PenetapanSurvei tanpa riwayat kejadian; riwayatnya cukup di pelacakan perubahan **[USULAN PENULIS]**
- [ ] `kontrak-core-sdm.md` bagian 2.3 (branch Zahir) masih memakai 6 status Sesi dan asumsi status `terpublikasi`. Menurut keputusan Core I-1: `state` {terjadwal, terlaksana, batal}. SDM cukup membaca `state = terlaksana` (field Core) sebagai penyebut PKG-04; asumsi pengganti bila PKG-18 belum terisi: sesi `terjadwal` yang tanggalnya lewat dianggap terlaksana (sudah demikian di `kebutuhan-sdm.md` KF-SDM-12). SDM **tidak** dapat memakai `is_terpublikasi`, karena field itu ditambahkan `labfik_praktikum` dan SDM tidak boleh bergantung ke Praktikum (I-7). *Versi sebelumnya isu ini menyarankan `is_terpublikasi`; keliru, dibetulkan saat audit 16 Nov 2026.* Disampaikan ke Zahir **[KONFIRMASI Zahir]**
- [ ] Asisten pengganti mendadak (tidak ada di Surat Tugas) hadir di sesi: cukup ditandai `/sesuai_penugasan` = salah (AB-PRK-20), tidak menolak jurnal. Sejalan dengan pertanyaan SDM KB-3 **[KONFIRMASI KaLab]**
