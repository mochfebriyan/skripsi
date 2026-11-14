# Proses Bisnis TO-BE Modul Pelaksanaan Praktikum

14 November 2026 · Herrens · PKG-15, 16, 17, 18, 19, 20

**Status: DRAF. Diagram ini masuk proposal (Bab II 2.3).** Langkah 5 rancangan TO-BE.

Diagram: [activity-state-praktikum.drawio](activity-state-praktikum.drawio), 8 halaman. Skrip pembuatnya: [tools/drawio/praktikum/activity_state.py](../tools/drawio/praktikum/activity_state.py) (salinan pola dari `contoh-tata-kelola/`, data diganti; dijalankan ulang bila isi berubah). `validate.py` dengan prefiks `prk-`: **OK** di kedelapan halaman. Tampilan visual **belum dicek di draw.io**.

## Posisi dalam metode

Input: [kebutuhan-praktikum.md](kebutuhan-praktikum.md) (KF-PRK-01 s.d. 44), [brief](../brief/brief-praktikum.md) (cakupan dan kontrak Core), [studi dokumen](../analisis/bedah-dokumen-praktikum.md) (langkah POB 2025 → TO-BE). Output dipakai di Langkah 6 (use case diturunkan dari tugas «user» dan event state machine).

## Pedoman yang dipakai (Wazlawick 2024, Bab 3 dan §9.3)

| Aturan | Penerapan |
|---|---|
| §3.2.1 Jenis tugas: *user*, *service*, *manual* | «user» putih = aktor memakai sistem; «service» abu-abu = sistem; «manual» krem putus-putus = di luar sistem (hanya *Laksanakan praktikum*); «call behavior» ungu = memanggil activity lain |
| §3.2.2 Gerbang keputusan tidak melakukan tugas; kondisi di panah | ◇ tanpa nama, `[guard]` di panah; tugas yang menghasilkan keputusan ditaruh sebelum ◇ |
| §3.2.3 *Pool* dan *lane* per aktor | Swimlane per aktor + lajur Sistem. Aktor abstrak *Pengisi Jurnal* dan *Pengaju* menjadi satu lajur |
| §3.2.4 Nama tugas = kata kerja kuat + objek domain, tanpa "dan/atau" | Semua tugas memakai pola ini (mis. *Periksa bentrok ruang*, bukan "Pemeriksaan konflik dan kapasitas") |
| §3.3 State machine: `event [guard] / efek`; Tabel 3–1 status × transisi untuk menemukan transisi yang terlewat | S1–S3 + bagian 3. Transisi baru ditandai merah |
| §3.4 Hanya elemen kunci yang digambar; konsep yang hanya dikelola tidak perlu diagram | Data Mata Kuliah, Kelas, impor alokasi, Versi Modul (status sederhana), Jurnal (dua status), Pemeriksaan Kesiapan (tanpa siklus status) **tidak** digambar; cukup tabel di bagian 3.4 |
| §9.3.1 *Stable transition*: status yang bisa dihitung dari data tidak perlu disimpan | *Terlewat* (Sesi) dan *Dibuka/Ditutup* (Survei) menjadi status turunan, bukan state |
| CLAUDE.md: bagian proses yang dipakai banyak proses digambar sekali, dipanggil dengan «call behavior» | Pengesahan jadwal memanggil **A1 Pengesahan Dokumen milik Tata Kelola**; keputusan tunda di A3 memanggil **A4 Perubahan Sesi** |

## 1. Daftar diagram

| Halaman | Isi | PKG | KF utama |
|---|---|---|---|
| Activity TO-BE (1-5) | A1 Persiapan jadwal dan modul periode | 15 | 01, 03–06, 12–13 |
| Activity TO-BE (2-5) | A2 Pemakaian lab di luar praktikum | 15 | 04, 08–11 |
| Activity TO-BE (3-5) | A3 Pelaksanaan satu sesi | 16, 17, 18 | 15–20, 22–26 |
| Activity TO-BE (4-5) | A4 Perubahan sesi | 18 | 27–28, 04 |
| Activity TO-BE (5-5) | A5 Survei kepuasan per periode | 20 | 33–38, 41 |
| State Machine TO-BE (1-3) | S1 Sesi | 15, 18 | 03, 06, 25–28 |
| State Machine TO-BE (2-3) | S2 Pengajuan dengan persetujuan sederhana (pemakaian lab, perubahan sesi) | 15, 18 | 08–09, 27–28 |
| State Machine TO-BE (3-3) | S3 Survei | 20 | 33–37, 41 |

## 2. Ringkasan alur

- **A1 Persiapan (sebelum semester).** Dua jalur paralel. Tim jadwal fakultas menyusun jadwal kelas praktikum dan mengirim berkasnya (di luar sistem); laboran mengimpor berkas itu, sistem membangkitkan Sesi untuk semua kelas dan memeriksa bentrok ruang. Bentrok dicatat sebagai rekaman konflik dan laboran menyampaikannya ke fakultas untuk diperbaiki; bila tidak ada bentrok, sistem memeriksa kapasitas lalu laboran menyusun penetapan jadwal yang disetujui (disahkan) KaLab lewat A1 Tata Kelola. Cara jadwal masuk ke Odoo (impor berkas, tanpa API) adalah **[ASUMSI]**; saat disahkan, sistem mencatat tanggal publikasi dan menandai Sesi terpublikasi. Sejajar, dosen menerbitkan versi modul (berkas, rubrik, daftar *software*, daftar bahan) dan sistem mengganti versi lama.
- **A2 Pemakaian lab.** Pengguna lab mengajukan; bila bentrok, waktu diubah; KaLab menyetujui (jadwal terpadu diperbarui) atau menolak dengan alasan.
- **A3 Satu sesi.** Sebelum jam mulai, laboran memeriksa kesiapan; butir *software* dan bahan dibuat dari modul; substitusi bahan disetujui dosen; keputusan tunda memanggil A4. Bila siap, praktikum berlangsung (di luar sistem), lalu Pengisi Jurnal mengisi jurnal, presensi petugas, dan *log book*, kemudian mengirim; sistem memvalidasi dan mengubah Sesi menjadi Terlaksana. Penilaian praktikan tidak dicatat per sesi; penilaian dilihat lewat tautan LeADS per kelas (KF-PRK-31), dengan impor Excel sebagai pelengkap (KF-PRK-50); tidak digambar karena hanya satu aktor dan satu langkah (§3.4).
- **A4 Perubahan.** Jadwal tetap selama semester kecuali ada perubahan; pengaju utama adalah dosen pengampu (kelas jadi daring atau pindah jadwal). Pengaju mengajukan; KaLab menolak atau menyetujui; bila ada pengganti, sistem memeriksa bentrok lalu membangkitkan Sesi pengganti yang merujuk Sesi asal; status Sesi asal diubah (Diganti / Dibatalkan / tetap dengan moda daring).
- **A5 Survei.** KaLab menyusun dan menetapkan survei (sistem memeriksa enam aspek, butir terbuka, target); responden mengisi selama survei dibuka; sistem menghitung rekap; KaLab mencatat evaluasi dan RTL; pada periode berikutnya KaLab menilai efektivitas RTL dan K4 menjadi lengkap.

## 3. Tabel status × transisi

Baris = status asal, kolom = status tujuan. Setiap sel kosong ditanyakan: "apakah transisi ini mungkin terjadi?" (§3.3, Tabel 3–1). **Cetak tebal** = transisi yang baru ditemukan lewat tabel ini (garis merah di diagram). **?** = pertanyaan untuk KaLab **[KONFIRMASI]**.

### 3.1 S1 Sesi

| Dari \ Ke | Rencana | Terpublikasi | Ditunda | Terlaksana | Diganti | Dibatalkan |
|---|---|---|---|---|---|---|
| (awal) | bangkitkan (A1) | bangkitkan pengganti (A4) | | | | |
| **Rencana** | | jadwal periode disahkan | | ? | | hapus (keluar) |
| **Terpublikasi** | **jadwal dicabut [belum ada jurnal]** | perubahan disetujui [daring] | keputusan tunda | kirim jurnal [valid] | perubahan disetujui [pengganti] | perubahan disetujui [batal] |
| **Ditunda** | | **perubahan ditolak** | | ? | perubahan disetujui [pengganti] | perubahan disetujui [batal] |
| **Terlaksana** | | ? | | | | |
| **Diganti** | | ? | | | | |
| **Dibatalkan** | | ? | | | | |

| Sel | Pertanyaan | Asumsi sementara |
|---|---|---|
| Rencana → Terlaksana | Bolehkah sesi yang jadwalnya belum disahkan dilaksanakan dan dilaporkan? | Tidak. Jurnal hanya bisa diisi untuk Sesi Terpublikasi; sesi semacam itu dihitung tidak memenuhi C1 PKG-15 |
| Ditunda → Terlaksana | Bila sesi ditunda tetapi akhirnya tetap berjalan (kendala teratasi), bagaimana? | Lewat **perubahan ditolak** (kembali Terpublikasi), lalu jurnal dikirim |
| Terlaksana → Terpublikasi | Jurnal terkirim ternyata salah: dibuka kembali? | Tidak mengubah status Sesi; koreksi isi jurnal tercatat di riwayat (`mail.thread`). Pengembalian jurnal oleh laboran menunggu P11 |
| Diganti / Dibatalkan → Terpublikasi | Bisakah keputusan perubahan dibatalkan? | Tidak. Buat perubahan baru untuk Sesi pengganti |

### 3.2 S2 Pengajuan dengan persetujuan sederhana

| Dari \ Ke | Diajukan | Disetujui | Ditolak | Ditarik |
|---|---|---|---|---|
| (awal) | ajukan [pemakaian: tidak bentrok] | | | |
| **Diajukan** | | setujui [KaLab] | tolak [alasan] | **tarik kembali [oleh pengaju]** |
| **Disetujui** | | | | ? |
| **Ditolak** | ? | | | |

| Sel | Pertanyaan | Asumsi sementara |
|---|---|---|
| Disetujui → (batal) | Pemakaian lab yang sudah disetujui lalu tidak jadi dipakai: perlu status *Dibatalkan*? | Belum dirancang; ruang tetap tercatat terpakai. Ditanyakan di P3 |
| Ditolak → Diajukan | Bisakah pengajuan yang ditolak diajukan ulang? | Tidak; buat pengajuan baru (riwayat penolakan tetap ada) |

### 3.3 S3 Survei

| Dari \ Ke | Draf | Ditetapkan | Dievaluasi | Siklus Selesai |
|---|---|---|---|---|
| (awal) | buat | | | |
| **Draf** | | tetapkan [enam aspek ∧ butir terbuka ∧ target ∧ berwenang] | | |
| **Ditetapkan** | **batalkan penetapan [sebelum tanggal buka]** | | catat evaluasi + RTL [tanggal tutup lewat] | |
| **Dievaluasi** | | ? | | nilai efektivitas RTL [survei periode berikutnya dievaluasi] |

| Sel | Pertanyaan | Asumsi sementara |
|---|---|---|
| Ditetapkan → Draf setelah dibuka | Butir salah ditemukan setelah survei dibuka? | Tidak boleh; buat survei baru agar respons tidak tercampur |
| Dievaluasi → Ditetapkan | Evaluasi perlu diulang? | Tidak mengubah status; evaluasi diedit dengan riwayat |

### 3.4 Objek yang tidak digambar (status sederhana)

| Objek | Status | Catatan |
|---|---|---|
| Penetapan Jadwal | Draf → Diajukan → Disahkan → Diganti / Dicabut | Memakai **S1 Tata Kelola** (`labfik.approval.mixin`), tanpa *Kedaluwarsa*. *Dicabut* memicu transisi baru di S1 Sesi (Terpublikasi → Rencana) |
| Versi Modul | Draf → Berlaku → Diganti | *Berlaku → Ditarik* (modul salah tanpa pengganti)? **[KONFIRMASI]**; asumsi: terbitkan versi perbaikan |
| Jurnal Sesi | Draf → Dikirim | *Dikirim → Draf* (dikembalikan laboran) bergantung fungsi verifikasi (P11); belum dirancang |
| Pemeriksaan Kesiapan | Tanpa siklus status | Keputusan (siap / siap setelah perbaikan / tunda) adalah nilai, bukan status |

## 4. Temuan untuk langkah berikutnya

### 4.1 Kebutuhan baru dari transisi yang ditemukan

Ditambahkan ke [kebutuhan-praktikum.md](kebutuhan-praktikum.md) dengan nomor lanjutan (nomor lama tidak digeser):

| KF | Asal | Kebutuhan | Prio |
|---|---|---|---|
| KF-PRK-45 | S1 Terpublikasi → Rencana | Saat Penetapan Jadwal dicabut, Sesi periode itu yang belum punya jurnal kembali ke Rencana | W (menjaga C1 tetap benar) **[KONFIRMASI]** |
| KF-PRK-46 | S1 Ditunda → Terpublikasi | Saat Perubahan Sesi atas sesi yang ditunda ditolak, Sesi kembali Terpublikasi | W |
| KF-PRK-47 | S2 Diajukan → Ditarik | Pengaju dapat menarik pengajuan pemakaian atau perubahan sebelum diputuskan | O |
| KF-PRK-48 | S3 Ditetapkan → Draf | KaLab dapat membatalkan penetapan survei sebelum tanggal buka | O |

### 4.2 Bahan *use case* (Langkah 6, §4.5–4.6)

Tugas «user» yang berurutan tanpa jeda oleh aktor yang sama digabung menjadi satu *use case*; yang bisa ditunda (beda hari atau aktor) dipisah.

| Kandidat *use case* | Dari | Aktor |
|---|---|---|
| Impor Jadwal Kelas (sistem membangkitkan Sesi; pola mingguan manual sebagai jalan pengganti) | A1 | Laboran |
| Susun Penetapan Jadwal → lalu UC pengesahan milik Tata Kelola | A1 | Laboran; KaLab |
| Terbitkan Versi Modul | A1 | Dosen |
| Ajukan Pemakaian Lab | A2 | Pengguna Lab |
| Putuskan Pemakaian Lab | A2, S2 | KaLab |
| Periksa Kesiapan Sesi (mulai, isi butir, tetapkan keputusan) | A3 | Laboran |
| Setujui Substitusi Bahan | A3 | Dosen |
| Kirim Jurnal Sesi (isi jurnal, presensi, *log book*) | A3, S1 | Pengisi Jurnal |
| Catat Penilaian Kelas (tautan LeADS); Impor Nilai Kelas (Pelengkap) | — (satu aktor, tidak digambar) | Dosen, Laboran |
| Ajukan Perubahan Sesi | A4, S1 | Pengaju |
| Putuskan Perubahan Sesi (termasuk tentukan waktu pengganti) | A4, S1 | KaLab |
| Tarik Pengajuan | S2 | Pengaju, Pengguna Lab |
| Susun Survei; Tetapkan Survei; Batalkan Penetapan Survei | A5, S3 | KaLab |
| Isi Survei | A5 | Responden |
| Catat Evaluasi Survei (termasuk RTL) | A5, S3 | KaLab |
| Nilai Efektivitas Tindak Lanjut | A5, S3 | KaLab |
| «CRUDL» Mata Kuliah, Kelas; impor alokasi | — | Laboran |
| «report» Jadwal Terpadu, Rekaman Konflik, Rekap Kesiapan, Rekap Keterlaksanaan, Kelas Tanpa Bukti Penilaian, Rekap Survei, Status Monev; Terbitkan Laporan Bukti | — | KaLab dan lainnya |

### 4.3 Tugas «service» → kebutuhan *hidden*

| Tugas «service» | KF | Ditempelkan ke *use case* |
|---|---|---|
| Periksa bentrok ruang / waktu pengganti | KF-PRK-04 | Bangkitkan Sesi, Ajukan Pemakaian, Putuskan Perubahan |
| Periksa kapasitas ruang | KF-PRK-05 | Bangkitkan Sesi |
| Catat tanggal publikasi; Tandai sesi terpublikasi | KF-PRK-06 (hook `_setelah_disahkan()`), 26 | Pengesahan (Tata Kelola) |
| Ganti versi modul lama | KF-PRK-13 | Terbitkan Versi Modul |
| Buat butir pemeriksaan | KF-PRK-16 | Periksa Kesiapan Sesi |
| Validasi jurnal; Ubah status sesi | KF-PRK-25, 26 | Kirim Jurnal Sesi |
| Bangkitkan sesi pengganti; Ubah status sesi asal | KF-PRK-28, 26 | Putuskan Perubahan Sesi |
| Periksa kelengkapan survei | KF-PRK-34 | Tetapkan Survei |
| Hitung rekap per aspek; Perbarui status K1–K4 | KF-PRK-38, 41 | Catat Evaluasi, Nilai Efektivitas |
| Kirim notifikasi pengajuan/keputusan | KF-PRK-49 (baru) | Ajukan / Putuskan Pemakaian dan Perubahan |

### 4.4 Dampak ke dokumen lain

- **Kebutuhan:** KF-PRK-45–48 ditambahkan. **Notifikasi** pengajuan dan keputusan muncul di A2 dan A4 tetapi belum punya KF; ditambahkan sebagai **KF-PRK-49** (O, *hidden*, memakai `mail.activity`/`mail.thread` bawaan).
- **Kontrak Core:** S1 Sesi menetapkan nilai `labfik.sesi.state` = Rencana, Terpublikasi, Ditunda, Terlaksana, Diganti, Dibatalkan, field `moda` (luring/daring), dan field `jenis_pertemuan` (praktikum/UTS/UAS; pertemuan 8 dan 16 tetap dibangkitkan). Perlu dicatat di kontrak Core bersama (brief, bagian d) **[KONFIRMASI kelompok]**.
- **Tata Kelola:** A1 memanggil activity pengesahan milik Tata Kelola; jenis dokumen baru `jadwal_praktikum` perlu dikenali `_jenis_dokumen()` (diusulkan ke Febriyan, sudah tercatat di kontrak Core c).

## 5. Pertanyaan terbuka

- [ ] Sel **?** di bagian 3.1–3.3 (KaLab).
- [ ] Jadwal dicabut setelah disahkan: Sesi kembali ke Rencana? (KF-PRK-45)
- [ ] Pemakaian lab yang disetujui lalu batal dipakai (P3).
- [ ] Sesi daring sah atau tidak (P12, pengaturan KF-PRK-43).
- [ ] Pemeriksaan per sesi atau per hari (P8); pengisi jurnal kelas tanpa asisten (P10, P13).

## Perbandingan dengan Tata Kelola

| | Tata Kelola (tag `rancangan-tatkel-v1`) | Praktikum |
|---|---|---|
| Activity | A1 pengesahan bersama + A2–A4 per dokumen | A1–A5 per proses; pengesahan **dipanggil** dari Tata Kelola, tidak digambar ulang |
| State machine | S1 status dokumen, S2 kemutakhiran SOP | S1 Sesi (objek kunci), S2 pengajuan bersama, S3 survei |
| Status turunan (§9.3.1) | *Perlu Ditinjau* dihitung | *Terlewat*, *Dibuka/Ditutup* dihitung |
| Penjadwal (pemicu waktu) | Ada (kedaluwarsa, pengingat) | Tidak ada; waktu hanya muncul sebagai ⧗ tunggu dan status turunan |
| Nama halaman | `Activity TO-BE A1 - …` | `Activity TO-BE (1-5) - …` mengikuti CLAUDE.md bagian 5 |
