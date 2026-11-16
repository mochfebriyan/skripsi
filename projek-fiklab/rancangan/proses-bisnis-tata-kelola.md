# Proses Bisnis TO-BE Modul Tata Kelola & Dokumen

14 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah 5 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (activity diagram dan state machine diagram).

Diagram: [activity-state-tata-kelola.drawio](activity-state-tata-kelola.drawio), 6 halaman diagram (A1–A4, S1–S2) + 1 halaman catatan kerja. Gaya polos hitam-putih tanpa warna isi dan garis putus-putus; jenis tugas dibedakan lewat stereotype, catatan dipindah ke halaman terakhir agar diagram ringkas saat disisipkan ke naskah (keputusan Febriyan, 16 November 2026). Dibuat dengan skrip [activity_state.py](../tools/drawio/contoh-tata-kelola/activity_state.py) dan lolos `validate.py` dengan prefiks `tk-`. **Tampilan visual belum dicek di draw.io**, karena draw.io tidak tersedia saat diagram dibuat.

Sumber: [kebutuhan-tata-kelola.md](kebutuhan-tata-kelola.md) (KF-01–45, aktor), [brief-tata-kelola-dokumen.md](../brief/brief-tata-kelola-dokumen.md) (cakupan Inti + Pelengkap, keputusan 13–14 November 2026), dan analisis PKG-01, 02, 03, 13.

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Diagram hanya untuk elemen kunci yang nontrivial. Konsep yang hanya dikelola (CRUDL) tidak digambar | §3.4 | Master Personel, Jabatan, KPI, dan Dokumen Induk tidak punya activity. Renstra tidak punya activity karena alurnya hanya unggah lalu A1 |
| Activity untuk proses (orang melakukan sesuatu); state machine untuk objek yang berganti status | §3.4 | A1–A4 untuk proses; S1–S2 untuk dokumen yang disahkan dan versi SOP/IK |
| Jenis tugas: «user» (memakai sistem), «service» (otomatis), «manual» (di luar sistem) | §3.2.1 | Tanda tangan dan peninjauan dokumen cetak = «manual». Pejabat penanda tangan hanya punya tugas «manual» |
| Lajur per aktor | §3.2.3 | Lajur sesuai aktor di kebutuhan, ditambah lajur Sistem dan lajur pejabat penanda tangan (di luar sistem) |
| Nama tugas = kata kerja + objek domain, tanpa "dan/atau"; keputusan tidak dinamai | §3.2.4 | Semua tugas. Kondisi ditulis sebagai `[guard]` di panah |
| Transisi `event [guard] / efek`; tabel status × transisi untuk menemukan transisi yang terlewat | §3.3, Tabel 3–1 | Bagian 4.2 |
| Status yang hanya menambah atau mengubah nilai = transisi stabil; cukup dihitung, bukan kelas baru | §9.3.1 | Sub-status S2 (*Mutakhir*, *Perlu Ditinjau*) dihitung dari tanggal |
| Bagian proses yang dipakai bersama digambar sekali dan dipanggil | CLAUDE.md bagian 4, langkah 5 | A1 dipanggil A2, A3, A4 dengan «call behavior» |

---

## 2. Daftar proses dan objek

| Kode | Diagram | Jenis | PKG | Alasan digambar |
|---|---|---|---|---|
| **A1** | Pengesahan Dokumen | Activity | Semua | Multi-aktor, ada kegiatan di luar sistem, bercabang (kembalikan, berkas tidak valid), dan dipakai bersama |
| **A2** | Siklus SOP/IK | Activity | 02 | Urutan S1–S5, paralel distribusi dan sosialisasi, siklus tinjau ulang |
| **A3** | Siklus Rencana | Activity | 01, 13 | Urutan K1–K4, dua aktor (KaLab, PIC), menunggu periode lapor, cabang per jenis rencana |
| **A4** | Siklus Struktur | Activity | 03 | Urutan K1–K4 dengan perulangan rapat dan evaluasi |
| **S1** | Status dokumen yang disahkan | State machine | Semua | Objek bisnis utama yang berganti status. Menyatukan status dari empat analisis |
| **S2** | Kemutakhiran versi SOP/IK | State machine | 02 | Rincian status Disahkan untuk kriteria S3 |

**Tidak digambar:**

| Hal | Alasan |
|---|---|
| Kelola Personel, Jabatan, KPI, Dokumen Induk | CRUDL (§3.4). Pengisian jabatan muncul sebagai satu tugas di A4 |
| Unggah Renstra | Alurnya hanya unggah lalu A1, tanpa siklus |
| Laporan (daftar induk, bagan, matriks, laporan pelaksanaan, status monev) | Bukan proses; menjadi use case «report» di langkah 6 |
| Pengguna Lab membaca SOP/IK | Satu tugas baca (KF-17, Pelengkap) |
| Status monev (KF-43, KF-44) | Dihitung saat dibaca, bukan tugas dalam alur |

---

## 3. Activity diagram

### 3.1 A1 · Pengesahan Dokumen

**Lajur:** Penyusun (KaLab / Laboran), Sistem, KaLab (pencatat pengesahan), Pejabat penanda tangan (di luar sistem).

**Alur utama:** penyusun mengajukan dokumen → sistem memeriksa kelengkapan isi sesuai jenis dokumen → status menjadi Diajukan → untuk rencana dan SK, penyusun menerbitkan PDF dari isi dokumen (SOP/IK dan Renstra sudah berupa berkas) → dokumen dicetak → pejabat meninjau dan menandatangani di luar sistem → penyusun mengunggah PDF bertanda tangan → KaLab mengesahkan → sistem memeriksa berkas dan wewenang pengesah → status menjadi Disahkan, dokumen lama menjadi Diganti, dan riwayat dicatat.

**Cabang:**
- `[belum lengkap]`: penyusun melengkapi isi, lalu mengajukan lagi.
- `[tidak disetujui]` (pejabat menolak di atas kertas): KaLab mengembalikan dokumen, status kembali ke Draf, penyusun memperbaiki, lalu mengajukan lagi. Ini satu-satunya jalur penolakan (brief, prinsip 2).
- `[berkas belum ada / pengesah tidak berwenang]`: kembali ke unggah berkas. Bila pengesah tidak berwenang, berkas harus ditandatangani pejabat yang berwenang lebih dulu.

| Tugas | Jenis | Lajur | KF |
|---|---|---|---|
| Ajukan dokumen | «user» | Penyusun | KF-01 |
| Periksa kelengkapan isi dokumen | «service» | Sistem | KF-01, KF-30 |
| Lengkapi isi dokumen | «user» | Penyusun | (ubah draf, CRUDL dokumen asal) |
| Ubah status menjadi Diajukan | «service» | Sistem | KF-01, KF-07 |
| Terbitkan dokumen PDF | «user» | Penyusun | KF-35 (Inti), KF-26, KF-41 (Pelengkap) |
| Hasilkan PDF dari isi dokumen | «service» | Sistem | KF-35, KF-26, KF-41 |
| Cetak dokumen | «manual» | Penyusun | — |
| Tinjau isi dokumen cetak | «manual» | Pejabat | — |
| Kembalikan dokumen | «user» | KaLab | KF-03 |
| Ubah status menjadi Draf | «service» | Sistem | KF-03, KF-07 |
| Perbaiki dokumen | «user» | Penyusun | (ubah draf) |
| Tanda tangani dokumen | «manual» | Pejabat | — |
| Unggah PDF bertanda tangan | «user» | Penyusun | KF-02 |
| Sahkan dokumen | «user» | KaLab | KF-04 |
| Periksa berkas dan wewenang pengesah | «service» | Sistem | KF-05 |
| Ubah status menjadi Disahkan | «service» | Sistem | KF-04 |
| Ganti status dokumen lama | «service» | Sistem | KF-08 |
| Catat riwayat pengesahan | «service» | Sistem | KF-07 |

Bila pejabat penanda tangan adalah KaLab sendiri, lajur KaLab dan lajur pejabat diperankan orang yang sama.

### 3.2 A2 · Siklus SOP/IK (PKG-02)

**Lajur:** Laboran/PLP, KaLab, Sistem.

**Alur utama:** daftarkan Dokumen Induk (bila dokumen baru) → susun naskah di luar sistem → unggah versi → **A1** → sistem menghitung tanggal tinjau berikutnya → distribusi dan sosialisasi dicatat secara paralel → menunggu tanggal tinjau terlewati → sistem menandai versi *perlu ditinjau* → laboran meninjau ulang.

**Cabang setelah tinjau ulang:** `[tetap berlaku]` → tanggal tinjau diperbarui dan siklus berulang; `[perlu revisi]` → kembali ke susun naskah (versi baru); `[tidak diperlukan lagi]` → KaLab mencabut dokumen.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Daftarkan dokumen induk | «user» | Laboran | KF-10 | S1 |
| Susun naskah SOP/IK | «manual» | Laboran | — | — |
| Unggah versi dokumen | «user» | Laboran | KF-11 | S2 |
| Sahkan dokumen (A1) | «call behavior» | Laboran | KF-01–08 | S2 |
| Hitung tanggal tinjau berikutnya | «service» | Sistem | KF-15 | S3 |
| Catat distribusi dokumen | «user» | Laboran | KF-12 | S4 |
| Catat sosialisasi dokumen | «user» | Laboran | KF-13 | S5 |
| Tandai versi perlu ditinjau | «service» | Sistem | KF-15 | S3 |
| Tinjau ulang dokumen | «user» | Laboran | KF-14 | S3 |
| Perbarui tanggal tinjau berikutnya | «service» | Sistem | KF-15 | S3 |
| Cabut dokumen | «user» | KaLab | KF-06 | — |
| Ubah status menjadi Dicabut | «service» | Sistem | KF-06, KF-07 | — |

"Tanggal tinjau terlewati" (⧗) adalah penanda yang dihitung, bukan pengingat terjadwal (brief, prinsip 5). Tinjau ulang boleh dilakukan sebelum tanggalnya tiba.

### 3.3 A3 · Siklus Rencana (PKG-01, PKG-13)

**Lajur:** KaLab, PIC item (Laboran / KaLab), Sistem.

**Alur utama:** untuk rencana pengembangan, catat temuan gap lebih dulu → susun item rencana → **A1** (kelengkapan item dicek saat diajukan) → menunggu akhir periode lapor → PIC mengisi realisasi item → berulang selama periode rencana berjalan → saat periode berakhir, KaLab mencatat tinjauan → untuk rencana pengembangan, catat ukuran manfaat.

**Cabang:** `[perlu revisi rencana]` → KaLab membuat revisi rencana (KF-37, **Pelengkap**) lalu kembali ke penyusunan item dan A1.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Catat temuan gap | «user» | KaLab | KF-39 | PKG-13 K2 |
| Susun item rencana | «user» | KaLab | KF-29, KF-39 | PKG-01 K2, PKG-13 K2 |
| Sahkan dokumen (A1) | «call behavior» | KaLab | KF-01–08 | K1 |
| Isi realisasi item | «user» | PIC | KF-31 | K3 |
| Buat revisi rencana | «user» | KaLab | KF-37 (O) | K4 |
| Catat tinjauan rencana | «user» | KaLab | KF-32 | K4 |
| Catat ukuran manfaat | «user» | KaLab | KF-40 | PKG-13 K4 |

Rencana periode berikutnya dimulai lagi dari awal diagram sebagai rekaman baru, dan keputusan tinjauan ditautkan ke rencana itu (KF-32). Renstra tidak ikut siklus ini.

### 3.4 A4 · Siklus Struktur (PKG-03)

**Lajur:** KaLab saja. Semua tugas sistem di alur ini sudah ada di A1.

**Alur utama:** lengkapi data jabatan (tugas, wewenang, atasan, pengganti) → susun SK penetapan pengelola → **A1** (pengesah biasanya Dekan) → catat rapat koordinasi, berulang → saat waktunya, catat evaluasi struktur.

**Cabang setelah evaluasi:** `[struktur tetap ∧ masa SK berjalan]` → kembali ke rapat; `[struktur perlu diubah]` → kembali ke data jabatan dan SK revisi (SK lama menjadi Diganti); `[masa SK berakhir]` → selesai, SK baru dimulai dari awal.

| Tugas | Jenis | KF | Kriteria |
|---|---|---|---|
| Lengkapi data jabatan | «user» | KF-20 | K2 |
| Susun SK penetapan pengelola | «user» | KF-21 | K1 |
| Sahkan dokumen (A1) | «call behavior» | KF-01–08 | K1 |
| Catat rapat koordinasi | «user» | KF-22 | K3 |
| Catat evaluasi struktur | «user» | KF-23 | K4 |

---

## 4. State machine

### 4.1 S1 · Status dokumen yang disahkan

Berlaku untuk semua dokumen yang memakai mekanisme pengesahan (`labfik.approval.mixin`): Renstra, rencana tahunan, rencana pengembangan, SK penetapan, dan versi SOP/IK.

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| ● | buat | Draf | CRUDL |
| Draf | ajukan `[isi lengkap]` / catat riwayat | Diajukan | KF-01 |
| Draf | hapus `[belum pernah diajukan]` | ◉ | CRUDL |
| Diajukan | kembalikan / catat alasan | Draf | KF-03 |
| Diajukan | unggah berkas bertanda tangan / catat riwayat | Diajukan | KF-02 |
| Diajukan | sahkan `[berkas ada ∧ pengesah berwenang]` / catat pengesah, pencatat, tanggal sah; dokumen lama → Diganti | Disahkan | KF-04, KF-05, KF-08 |
| Disahkan | revisi atau versi baru disahkan | Diganti | KF-08 |
| Disahkan | cabut / catat alasan | Dicabut | KF-06 |
| Disahkan | when(periode berakhir) `[dokumen berperiode]` | Kedaluwarsa | KF-09 (Pelengkap, Penjadwal) |

**Penyatuan status** (CLAUDE.md, langkah 5):

| Analisis | Status di analisis | Di S1 |
|---|---|---|
| PKG-01 | draf, diajukan, disahkan, kedaluwarsa | Sama |
| PKG-02 | draf, diajukan, **berlaku**, dicabut | berlaku → **Disahkan** |
| PKG-13 | draf, diajukan, disahkan, diganti, **selesai** | selesai → **Kedaluwarsa** |
| Bedah dokumen | disusun, **diperiksa**, disahkan | Diperiksa dihapus (keputusan 14 November 2026) |

Label "berlaku" tetap boleh dipakai di antarmuka sebagai keterangan status Disahkan.

### 4.2 Tabel status × transisi S1 (§3.3, Tabel 3–1)

Baris = status asal, kolom = status tujuan. Sel kosong ditanyakan: apakah ada kejadian yang memindahkan dokumen di antara keduanya?

| Dari \ Ke | Draf | Diajukan | Disahkan | Diganti | Dicabut | Kedaluwarsa |
|---|---|---|---|---|---|---|
| **Draf** | — | ajukan | ✗ (1) | ✗ | ✗ (2) | ✗ (3) |
| **Diajukan** | **kembalikan** | **unggah berkas** | sahkan | ✗ (4) | ✗ (5) | ✗ (6) |
| **Disahkan** | ✗ (7) | ✗ (7) | — | revisi disahkan | cabut | when(periode berakhir) |
| **Diganti** | ✗ (8) | ✗ | ✗ | — | ✗ | ✗ |
| **Dicabut** | ✗ (8) | ✗ | ✗ | ✗ | — | ✗ |
| **Kedaluwarsa** | ✗ (8) | ✗ | ✗ | ✗ | ✗ | — |

Huruf tebal = transisi yang tidak ada di analisis mana pun dan ditemukan lewat tabel ini (ditandai * di diagram). Ditambah *hapus draf* ke status akhir.

Jawaban untuk sel kosong:
1. Draf tidak bisa langsung disahkan. Pengesahan harus lewat pengajuan agar kelengkapan dicek.
2. Draf yang tidak dipakai **dihapus**, bukan dicabut. Pencabutan hanya untuk dokumen yang pernah berlaku.
3. Draf yang periodenya lewat tetap Draf; penyusun menghapus atau memperbaruinya.
4. Dua versi yang diajukan bersamaan dicegah oleh KF-18 (Pelengkap). Tanpa KF-18, versi yang masih Diajukan tetap Diajukan saat versi lain disahkan, lalu menggantikannya bila disahkan kemudian.
5. Dokumen yang diajukan tidak dicabut; KaLab memakai **kembalikan**.
6. **[ASUMSI]** Dokumen yang periodenya lewat sebelum disahkan dikembalikan KaLab, bukan dikedaluwarsakan Penjadwal.
7. Dokumen yang sudah disahkan tidak diedit. Perubahan dibuat sebagai **revisi** atau versi baru (rekaman baru), sehingga riwayatnya utuh.
8. **[ASUMSI]** Diganti, Dicabut, dan Kedaluwarsa adalah status akhir. Pengaktifan kembali tidak dirancang (brief, prinsip sweet spot); yang dibuat adalah revisi atau dokumen periode baru.

**Temuan:** ketiga transisi baru (kembalikan, unggah berkas, hapus draf) sudah punya kebutuhan (KF-03, KF-02, CRUDL). Tidak ada KF baru.

### 4.3 S2 · Kemutakhiran versi SOP/IK

Rincian status Disahkan untuk versi SOP/IK yang sedang berlaku. Sub-status:
- **Mutakhir**: tanggal tinjau berikutnya belum terlewati. Memenuhi PKG-02 S3.
- **Perlu Ditinjau**: tanggal tinjau berikutnya sudah terlewati.

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| (masuk Disahkan) | / hitung tanggal tinjau | Mutakhir | KF-15 |
| Mutakhir | when(tanggal tinjau terlewati) | Perlu Ditinjau | KF-15 |
| Perlu Ditinjau | tinjau `[hasil = tetap berlaku]` / perbarui tanggal tinjau | Mutakhir | KF-14, KF-15 |
| Mutakhir | tinjau `[hasil = tetap berlaku]` / perbarui tanggal tinjau | Mutakhir | KF-14, KF-15 |
| Disahkan (semua sub-status) | versi baru disahkan | Diganti | KF-08 |
| Disahkan (semua sub-status) | cabut | Dicabut | KF-06 |

**[ASUMSI]** Tinjauan dengan hasil *perlu revisi* tidak mengubah sub-status dan tidak memperbarui tanggal tinjau. Tinjauan itu memicu penyusunan versi baru di A2. Versi lama tetap dipakai sampai versi baru disahkan.

**Implementasi** (§9.3.1, transisi stabil): sub-status ini tidak disimpan sebagai nilai `state`. *Perlu Ditinjau* dihitung dari tanggal tinjau berikutnya dibanding hari ini. Dibanding rancangan di tag `rancangan-tatkel-v1`, sub-status *Menunggu Revisi* dan efek *kirim pengingat* dihapus, karena tidak dibutuhkan kriteria S3 dan bertentangan dengan prinsip "hitung, bukan jadwalkan".

---

## 5. Cek silang

### 5.1 KF → proses

| KF | Muncul di |
|---|---|
| KF-01–08 | A1, S1 |
| KF-09 | S1 (Pelengkap, Penjadwal) |
| KF-10–15 | A2, S2 |
| KF-16 | «report» (langkah 6) |
| KF-17 | Tidak digambar (baca saja, Pelengkap) |
| KF-18 | Aturan di tabel S1, sel (4) |
| KF-19 | CRUDL |
| KF-20–23 | A4 |
| KF-24, 25 | «report» |
| KF-26 | A1 (Terbitkan dokumen PDF, Pelengkap) |
| KF-27 | CRUDL |
| KF-28 | Unggah Renstra lalu A1 (tidak digambar) |
| KF-29–32 | A3 (KF-30 di A1, cek kelengkapan) |
| KF-33, 34 | «report» |
| KF-35 | A1 (Terbitkan dokumen PDF) |
| KF-36 | Bagian dari Susun item rencana / penyusunan rencana (Pelengkap) |
| KF-37 | A3 (Pelengkap) |
| KF-38 | Aturan di S1 (guard saat sahkan, Pelengkap) |
| KF-39, 40 | A3 |
| KF-41 | A1 (Pelengkap) |
| KF-42 | Dihitung dari item (Pelengkap) |
| KF-43–45 | Dihitung saat dibaca / «report» |

Semua KF punya tempat: tugas activity, transisi state machine, CRUDL, «report», atau perilaku sistem.

### 5.2 Kriteria → tugas

Setiap kriteria punya tugas «user» yang menghasilkan rekaman buktinya: K1 → A1 (lewat A2/A3/A4); PKG-01/13 K2 → Susun item rencana, Catat temuan gap; PKG-03 K2 → Lengkapi data jabatan; K3 → Isi realisasi item, Catat rapat koordinasi; K4 → Catat tinjauan rencana, Catat ukuran manfaat, Catat evaluasi struktur; S1–S5 → tugas A2.

### 5.3 Kesalahan di langkah sebelumnya

- Di [kebutuhan-tata-kelola.md](kebutuhan-tata-kelola.md) bagian 7, S2 disebut "versi SOP (perlu ditinjau)". Di sini S2 berisi dua sub-status (Mutakhir, Perlu Ditinjau). Isinya sejalan; tidak perlu diubah.
- KF-36 (narasi rencana) tidak muncul sebagai tugas terpisah; ia bagian dari penyusunan rencana. Tidak ada perubahan KF.

---

## 6. Temuan untuk langkah 6 (use case)

Kandidat use case dari tugas «user» (§4.5) dan event state machine (§4.6). Penggabungan dan pemisahan diputuskan di langkah 6 dengan kriteria satu sesi (§4.3.1).

| Sumber | Kandidat use case | Catatan |
|---|---|---|
| A1, S1 ajukan | Ajukan dokumen | Dipakai semua jenis dokumen |
| A1 | Terbitkan dokumen PDF | Perlu diuji *essential* (§4.3.4): menghasilkan dokumen resmi yang ditandatangani, bukan sekadar "cetak" |
| A1, S1 unggah | Unggah PDF bertanda tangan | Beda hari dengan ajukan → use case terpisah |
| A1, S1 kembalikan | Kembalikan dokumen | KaLab |
| A1, S1 sahkan | Sahkan dokumen | KaLab |
| A2, S1 cabut | Cabut dokumen | KaLab, berlaku untuk semua dokumen |
| A2 | Unggah versi dokumen | Laboran |
| A2 | Catat distribusi dokumen, Catat sosialisasi dokumen | Dua use case, bisa beda hari |
| A2, S2 tinjau | Tinjau ulang dokumen | |
| A3 | Susun rencana (+ Catat temuan gap) | Gap dan item mungkin satu use case "Susun rencana pengembangan" bila diisi dalam satu sesi |
| A3 | Isi realisasi item, Catat tinjauan rencana (+ ukuran manfaat), Buat revisi rencana (O) | |
| A4 | Susun SK penetapan, Catat rapat koordinasi, Catat evaluasi struktur | |
| S1 when | Tandai kedaluwarsa (Penjadwal, O) | Aktor «system» |
| CRUDL | Personel, Jabatan, KPI, Dokumen Induk, Renstra | «CRUDL» |
| «report» | Daftar induk dan riwayat revisi, bagan organisasi, matriks kewenangan, matriks keterkaitan, laporan pelaksanaan, status monev | |

## 7. Isu terbuka

- [ ] Periode lapor realisasi per triwulan atau per semester (A3) **[KONFIRMASI KaLab]**
- [ ] Frekuensi rapat koordinasi dan evaluasi struktur (A4) **[KONFIRMASI KaLab]**
- [ ] Apakah dokumen Dicabut atau Kedaluwarsa pernah perlu diaktifkan kembali (S1, sel 8)? Sementara tidak **[ASUMSI]**
- [ ] Tinjauan "perlu revisi" tetap dihitung mutakhir sampai tanggal tinjau terlewati (S2)? **[ASUMSI]**, perlu disepakati dengan pembimbing bila dipertanyakan
- [ ] Tampilan diagram belum dicek di draw.io **[VALIDASI]**
