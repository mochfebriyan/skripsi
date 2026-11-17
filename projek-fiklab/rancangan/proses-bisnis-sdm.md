# Proses Bisnis TO-BE Modul SDM & Kompetensi

14 November 2026, direvisi 17 November 2026 · Zahir · PKG-04, PKG-10, PKG-14

**Status: DRAF.** Langkah 5 alur rancangan TO-BE ([CLAUDE.md](../../CLAUDE.md) bagian 4). **Masuk proposal** Bab II 2.3 (activity diagram dan state machine diagram).

Diagram: [activity-state-sdm.drawio](activity-state-sdm.drawio), 8 halaman diagram (A1–A4, S1–S4) dan 1 halaman catatan. Dibuat dengan skrip [tools/drawio/sdm/activity_state.py](../tools/drawio/sdm/activity_state.py), yang fungsi gambar dan gayanya disalin dari `contoh-tata-kelola/activity_state.py` versi `main`; data dan prefiks `sdm-` diganti. Gaya polos hitam-putih; judul, legenda, sumber, dan [KONFIRMASI] ada di halaman catatan (CLAUDE.md bagian 5). Diagram lolos `validate.py` dengan prefiks `sdm-`. **Tampilan visual belum dicek di draw.io**, karena draw.io tidak tersedia saat diagram dibuat.

Sumber: [kebutuhan-sdm.md](kebutuhan-sdm.md) (KF-SDM-01–43, aktor), [brief-sdm.md](../brief/brief-sdm.md) (cakupan Inti + Pelengkap, keputusan 14 November 2026), [kontrak-core-sdm.md](kontrak-core-sdm.md) (mixin, K-3, K-6), dan analisis PKG-04, 10, 14.

## 0. Perubahan dibanding versi 14 November 2026

| Versi lama | Versi ini | Alasan |
|---|---|---|
| Pengesahan dipanggil sebagai «call behavior» ke activity A1 modul Tata Kelola (TK-A1); status Surat Tugas dan Rencana Pelatihan "sama dengan S1 Tata Kelola" | Pengesahan dokumen SDM digambar sendiri: **A4 Pengesahan Dokumen SDM** dan **S4 Surat Tugas dan Rencana Pelatihan**. Mekanisme teknisnya tetap `labfik.approval.mixin` (Core) | Arahan Zahir (17 November 2026): diagram hanya berisi scope modul SDM, tanpa activity atau use case modul lain |
| Transisi *unggah berkas* di S1 Otorisasi tidak digambar ("mengikuti S1 Tata Kelola") | Digambar | Sama |
| *Ganti otorisasi lama* sebagai tugas «service» di A2 | Menjadi bagian A4 (*Ganti status dokumen lama*) | Satu tempat untuk semua penggantian dokumen SDM |
| Warna modul, garis merah untuk transisi baru, catatan di samping diagram | Polos hitam-putih; transisi baru ditandai **\***; catatan di halaman terakhir | CLAUDE.md bagian 5 versi `main` (16 November 2026) |

Kode A1–A3 dan S1–S3 tidak berubah. A4 dan S4 adalah kode baru (CLAUDE.md bagian 7: nomor tidak digeser).

---

## 1. Aturan yang dipakai

| Aturan | Bab Wazlawick | Penerapan |
|---|---|---|
| Diagram hanya untuk proses yang nontrivial (multi-aktor, bercabang, beraturan); konsep yang hanya dikelola (CRUDL) tidak digambar | §3.2 ("nontrivial business use cases"), §3.4 | Master Kompetensi, syarat jabatan, Bukti Kompetensi, Tugas/Alat tidak punya activity |
| Jenis tugas: «user» (memakai sistem), «service» (otomatis), «manual» (di luar sistem) | §3.2.1 | Seleksi calon, uji keterampilan, ikut pelatihan, persetujuan pengecualian, cetak, dan tanda tangan = «manual» |
| Gateway: keputusan tanpa nama, kondisi sebagai `[guard]` di panah; *merge* untuk menyatukan jalur | §3.2.2, §3.2.4 | Semua keputusan ◇ tidak dinamai |
| Lajur per aktor | §3.2.3 | Lajur KaLab, Laboran/PLP, Sistem, ditambah lajur pihak di luar sistem (penyetuju pengecualian di A1, pejabat penanda tangan di A4) |
| Nama tugas = kata kerja kuat + objek domain, tanpa "dan/atau" | §3.2.4 | Semua tugas |
| State machine untuk objek yang berganti status; transisi `event [guard] / efek` | §3.3 | S1–S4 |
| Tabel status × transisi untuk menemukan transisi yang terlewat; transisi baru bisa menjadi kebutuhan baru | §3.3, Tabel 3–1 | Bagian 4; temuan ditandai **\*** di diagram |
| Status yang hanya mengubah nilai = **transisi stabil**, cukup atribut atau nilai terhitung | §9.3.1 | *Berlaku/Lewat masa berlaku* (Otorisasi), *Menunggu evaluasi/Dievaluasi* (Item), status berlaku Bukti Kompetensi dan baris Penugasan |
| Bagian proses yang dipakai bersama digambar sekali dan dipanggil | CLAUDE.md langkah 5 | **A4 Pengesahan Dokumen SDM** dipanggil A1–A3 dengan «call behavior» |

---

## 2. Daftar proses dan objek

| Kode | Diagram | Jenis | PKG | Alasan digambar |
|---|---|---|---|---|
| **A1** | Seleksi dan Penugasan Petugas | Activity | 04 | Multi-aktor (KaLab, Laboran, penyetuju di luar sistem), bercabang (tidak lulus / lulus / pengecualian), perulangan per calon, pengesahan |
| **A2** | Otorisasi Personel | Activity | 10 | Urutan S1–S4: kompetensi → otorisasi → evaluasi ulang; perulangan pengembangan dan perpanjangan |
| **A3** | Siklus Pelatihan PLP | Activity | 14 | Urutan K1–K4 dalam satu tahun; menunggu jadwal; cabang batal; hasil kembali ke matriks kompetensi |
| **A4** | Pengesahan Dokumen SDM | Activity | 04, 10, 14 | Dipakai tiga dokumen (Surat Tugas, Otorisasi, Rencana Pelatihan); multi-aktor (penyusun, KaLab, pejabat di luar sistem); bercabang (belum lengkap, dikembalikan, berkas/wewenang tidak valid) |
| **S1** | Otorisasi | State machine | 10 | Objek bisnis utama PKG-10 dengan masa berlaku sendiri (kontrak Core K-3) |
| **S2** | Evaluasi Ulang Otorisasi | State machine | 10 | Status *Terbuka* menentukan S4 |
| **S3** | Item Pelatihan | State machine | 14 | Status *Terlaksana/Batal/Dievaluasi* menentukan K3–K4 |
| **S4** | Surat Tugas dan Rencana Pelatihan | State machine | 04, 14 | Status pengesahan menentukan PKG-04 S2 dan PKG-14 K1 |

**Tidak digambar:**

| Hal | Alasan |
|---|---|
| Kelola Kompetensi, syarat jabatan, Bukti Kompetensi, Tugas/Alat | CRUDL (§3.4). Penetapan pelaksana tugas/alat muncul sebagai satu tugas di A2 |
| Status berlaku Bukti Kompetensi dan baris Penugasan | Transisi stabil yang dihitung dari tanggal (§9.3.1); tidak ada event |
| Orientasi/supervisi petugas baru (KF-SDM-16) | Satu tugas pencatatan, Pelengkap |
| Matriks, Daftar Petugas per Sesi, Daftar Operator Sah, rekap, status monev | Bukan proses; menjadi *use case* «report» di langkah 6 |

---

## 3. Activity diagram

### 3.1 A1 · Seleksi Asisten dan Penugasan Petugas (PKG-04)

**Lajur:** KaLab, Laboran/PLP, Sistem, Penyetuju pengecualian (di luar sistem).

**Alur utama:**
1. KaLab menetapkan kebutuhan petugas per kelas.
2. KaLab menyeleksi calon asisten di luar sistem (wawancara, simulasi, pengembangan modul; POB 2025).
3. Untuk calon yang lulus, Laboran mencatat hasil seleksi, dan sistem membuat Personel asisten bila belum ada. Langkah ini berulang untuk setiap calon.
4. Laboran menyusun Surat Tugas: asisten → kelas, laboran → ruang, dengan rentang berlaku.
5. Surat Tugas disahkan lewat **A4**.

**Cabang:**
- `[tidak lulus]`: selesai untuk calon itu; tidak dicatat (keputusan 14 Nov 2026).
- `[lulus dengan pengecualian]`: penyetuju menyetujui pengecualian di atas kertas, lalu hasil seleksi dicatat beserta alasan dan penyetuju.
- `[perlu pengganti]` (Pelengkap): KaLab membuat revisi Surat Tugas, yang disahkan lagi lewat A4.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Tetapkan kebutuhan petugas | «user» | KaLab | KF-SDM-09 | S1 |
| Seleksi calon asisten | «manual» | KaLab | — | — |
| Setujui pengecualian syarat | «manual» | Penyetuju | — | S4 |
| Catat hasil seleksi | «user» | Laboran | KF-SDM-07, 08 | S4, bukti 5–6 |
| Buat personel asisten | «service» | Sistem | KF-SDM-07 (efek) | — |
| Susun surat tugas | «user» | Laboran | KF-SDM-10 (15 O) | S2, bukti 2 |
| Sahkan dokumen SDM (A4) | «call behavior» | Laboran | KF-SDM-06, 11, 43 (17 O) | S2 |
| Buat revisi surat tugas | «user» | KaLab | KF-SDM-14 (O) | S2 |

Bukti kompetensi (S3) dicatat lewat CRUDL di luar alur ini, dan status S1–S4 setiap sesi dihitung saat dibaca (KF-SDM-12).

### 3.2 A2 · Otorisasi Personel (PKG-10)

**Lajur:** KaLab, Laboran/PLP (penilai dan pencatat), Sistem.

**Alur utama:**
1. KaLab menetapkan pelaksana tugas/alat.
2. Bila personel belum punya bukti kompetensi berlaku, Laboran menguji keterampilannya di luar sistem dan mencatat asesmen. Bila *layak*, sistem membuat Bukti Kompetensi.
3. KaLab menyusun Otorisasi, yang disahkan lewat **A4**. Di dalam A4, otorisasi lama untuk pasangan yang sama diganti.
4. Saat muncul pemicu (masa berlaku habis, alat berubah, insiden, lama tidak aktif), Laboran mencatat evaluasi ulang.

**Cabang:**
- `[bukti kompetensi berlaku ada]`: langsung ke penyusunan Otorisasi.
- `[belum layak]`: personel mengikuti pengembangan kompetensi di luar sistem, lalu diuji ulang.
- Setelah evaluasi ulang:
  - `[diperpanjang / dibatasi / naik level]` → Otorisasi baru (kembali ke penyusunan);
  - `[tetap berlaku]` → kembali menunggu pemicu (**temuan**, bagian 4.2);
  - `[dicabut]` → KaLab mencabut otorisasi.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Tetapkan pelaksana tugas/alat | «user» | KaLab | KF-SDM-18, 19 | Penyebut, bukti 1 |
| Uji keterampilan personel | «manual» | Laboran | — | S1 |
| Catat asesmen keterampilan | «user» | Laboran | KF-SDM-20 | S1, bukti 2 |
| Ikuti pengembangan kompetensi | «manual» | Laboran | — (bisa lewat A3) | — |
| Buat bukti kompetensi | «service» | Sistem | KF-SDM-21 | S1 |
| Susun otorisasi | «user» | KaLab | KF-SDM-22 | S2, S3 |
| Sahkan dokumen SDM (A4) | «call behavior» | KaLab | KF-SDM-06, 23, 24, 43 | S2 |
| Catat evaluasi ulang otorisasi | «user» | Laboran | KF-SDM-25 | S4, bukti 5 |
| Cabut otorisasi | «user» | KaLab | KF-SDM-06 | S4 |

"Muncul pemicu" (⧗) adalah kejadian di dunia nyata yang dicatat manual, bukan penjadwal (kontrak Core K-3). Otorisasi yang lewat masa berlakunya otomatis gagal S2 lewat status terhitung (S1).

Di langkah 6, tugas *Catat evaluasi ulang otorisasi* dipecah menjadi dua *use case* (Catat Pemicu dan Putuskan), mengikuti status *Terbuka* di S2. Activity ini belum dipecah karena menunggu jawaban KU-1 (bagian 6.3).

### 3.3 A3 · Siklus Pelatihan PLP/Laboran (PKG-14)

**Lajur:** KaLab, Laboran/PLP (peserta dan pencatat), Sistem.

**Alur utama:**
1. KaLab membuat Rencana Pelatihan untuk satu tahun, dan sistem mengisi kebutuhan awal dari selisih Kompetensi wajib dan Bukti Kompetensi.
2. KaLab melengkapi kebutuhan dan menyusun item pelatihan.
3. Rencana disahkan lewat **A4**; kelengkapan dicek dan kebutuhan dibekukan saat diajukan.
4. Saat jadwal item tiba, peserta mengikuti pelatihan, lalu Laboran mencatat realisasi.
5. Peserta menerapkan keterampilan di pekerjaan. Saat waktu evaluasi tiba, efektivitas dicatat; bila *efektif*, sistem membuat Bukti Kompetensi.
6. Langkah 4–5 berulang sampai semua item selesai atau batal.

**Cabang:** `[batal]` → KaLab menandai item batal dengan alasan (Pelengkap); `[perlu pengembangan]` → tidak ada bukti baru, kebutuhannya muncul lagi di rencana tahun berikutnya.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Buat rencana pelatihan | «user» | KaLab | KF-SDM-29 | K1 |
| Isi kebutuhan dari matriks kompetensi | «service» | Sistem | KF-SDM-30 | K1, bukti 1 |
| Lengkapi kebutuhan kompetensi | «user» | KaLab | KF-SDM-29 | K1 |
| Susun item pelatihan | «user» | KaLab | KF-SDM-31 | K2, bukti 2 |
| Sahkan dokumen SDM (A4) | «call behavior» | KaLab | KF-SDM-06, 32, 43 (39 O) | K1 |
| Ikuti pelatihan | «manual» | Laboran | — | K3 |
| Tandai item batal | «user» | KaLab | KF-SDM-37 (O) | K3 |
| Catat realisasi pelatihan | «user» | Laboran | KF-SDM-33 | K3, bukti 3–4 |
| Terapkan keterampilan di pekerjaan | «manual» | Laboran | — | K3 |
| Catat evaluasi efektivitas | «user» | Laboran | KF-SDM-34 | K4, bukti 5 |
| Buat bukti kompetensi | «service» | Sistem | KF-SDM-35 | K4 |

Rencana tahun berikutnya dimulai lagi dari awal diagram. Kebutuhannya otomatis berkurang karena bukti kompetensi baru sudah masuk matriks; inilah wujud K4 "kebutuhan berikutnya diperbarui".

### 3.4 A4 · Pengesahan Dokumen SDM (dipanggil A1, A2, A3)

**Lajur:** Penyusun (KaLab / Laboran), Sistem, KaLab (pencatat pengesahan), Pejabat penanda tangan (di luar sistem).

**Alur utama:**
1. Penyusun mengajukan dokumen SDM.
2. Sistem memeriksa kelengkapan sesuai jenis dokumen; bila lengkap, status menjadi Diajukan.
3. Untuk Surat Tugas dan Rencana Pelatihan, penyusun menerbitkan PDF dari isi dokumen (Pelengkap).
4. Penyusun mencetak dokumen, dan pejabat meninjau serta menandatanganinya di luar sistem.
5. Penyusun mengunggah PDF bertanda tangan, lalu KaLab mencatat pengesahan.
6. Sistem memeriksa berkas dan wewenang pengesah. Bila valid: status menjadi Disahkan, dokumen lama diganti, dan riwayat dicatat.

**Cabang:** `[belum lengkap]` → penyusun melengkapi lalu mengajukan ulang; `[otorisasi]` → tanpa penerbitan PDF oleh sistem; `[tidak disetujui]` → KaLab mengembalikan, status kembali Draf, penyusun memperbaiki; `[berkas belum ada / pengesah tidak berwenang]` → kembali ke unggah.

| Tugas | Jenis | Lajur | KF | Kriteria |
|---|---|---|---|---|
| Ajukan dokumen SDM | «user» | Penyusun | KF-SDM-06 | PKG-04 S2, PKG-10 S2, PKG-14 K1 |
| Periksa kelengkapan dokumen | «service» | Sistem | KF-SDM-11 (Surat Tugas), 23 (Otorisasi), 32 (Rencana, + bekukan kebutuhan) | PKG-04 S4, PKG-10 S1/S3, PKG-14 K1–K2 |
| Lengkapi isi dokumen; Perbaiki dokumen | «user» | Penyusun | (ubah draf di *use case* penyusunnya) | — |
| Ubah status menjadi Diajukan / Draf / Disahkan | «service» | Sistem | KF-SDM-06 | — |
| Terbitkan dokumen PDF + Hasilkan PDF | «user» + «service» | Penyusun, Sistem | KF-SDM-17, 39 (O) | Bukti 2 PKG-04, PKG-14 |
| Cetak dokumen; Tinjau isi dokumen cetak; Tanda tangani dokumen | «manual» | Penyusun, Pejabat | — | — |
| Kembalikan dokumen | «user» | KaLab | KF-SDM-06 | — |
| Unggah PDF bertanda tangan | «user» | Penyusun | KF-SDM-06 | — |
| Sahkan dokumen | «user» | KaLab | KF-SDM-06 | S2 / K1 |
| Periksa berkas dan wewenang pengesah | «service» | Sistem | KF-SDM-43 | S2 ("penugasan sah") |
| Ganti status dokumen lama | «service» | Sistem | KF-SDM-14 (Surat Tugas revisi), 24 (Otorisasi pasangan sama) | PKG-10 S2 |
| Catat riwayat pengesahan | «service» | Sistem | KF-SDM-06 | — |

Pejabat penanda tangan (KaLab, Wadek, atau Koor Prodi) bukan aktor sistem. Bila pejabatnya KaLab sendiri, lajur KaLab dan lajur pejabat diperankan orang yang sama. Mekanisme teknisnya `labfik.approval.mixin` di Core: urutan ajukan dan sahkan tetap, model SDM hanya mengisi pemeriksaan kelengkapan dan penggantian dokumen ([kontrak-core-sdm.md](kontrak-core-sdm.md) bagian 5).

---

## 4. State machine

Transisi yang ditemukan lewat tabel status × transisi ditandai **\*** di diagram.

### 4.1 S1 · Otorisasi

Berlaku untuk `labfik.sdm.otorisasi`: status pengesahan dari `labfik.approval.mixin` ditambah masa berlaku sendiri (bukan `period.mixin`).

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| ● | buat | Draf | KF-SDM-22 |
| Draf | ajukan `[kompetensi terbukti ∧ lingkup terisi ∧ supervisor berwenang bila terbimbing]` / catat riwayat | Diajukan | KF-SDM-23 |
| Draf | hapus `[belum pernah diajukan]` | ◉ | CRUDL |
| Diajukan | kembalikan / catat alasan | Draf | KF-SDM-06 |
| Diajukan | unggah berkas bertanda tangan / catat riwayat | Diajukan | KF-SDM-06 |
| Diajukan | sahkan `[berkas ada ∧ pengesah berwenang]` / catat pengesah; otorisasi lama pasangan sama → Diganti | Disahkan.Berlaku | KF-SDM-06, 43, 24 |
| Disahkan.Berlaku | when(hari ini > berlaku_sampai) **\*** | Disahkan.Lewat masa berlaku | KF-SDM-24 |
| Disahkan (kedua sub-status) | otorisasi baru pasangan sama disahkan | Diganti | KF-SDM-24 |
| Disahkan (kedua sub-status) | cabut `[evaluasi ulang: dicabut]` / catat alasan | Dicabut | KF-SDM-06, 25 |

**Tabel status × transisi** (§3.3, Tabel 3–1). Baris = asal, kolom = tujuan.

| Dari \ Ke | Draf | Diajukan | Berlaku | Lewat masa | Diganti | Dicabut |
|---|---|---|---|---|---|---|
| **Draf** | — | ajukan | ✗ (1) | ✗ | ✗ | ✗ (2) |
| **Diajukan** | kembalikan | unggah berkas | sahkan | ✗ (3) | ✗ (4) | ✗ (5) |
| **Berlaku** | ✗ (6) | ✗ (6) | — | **when(lewat berlaku_sampai)** | otorisasi baru | cabut |
| **Lewat masa** | ✗ | ✗ | ✗ (7) | — | otorisasi baru | cabut |
| **Diganti** | ✗ (8) | ✗ | ✗ | ✗ | — | ✗ |
| **Dicabut** | ✗ (8) | ✗ | ✗ | ✗ | ✗ | — |

Huruf tebal = transisi yang tidak ada di analisis PKG-10 (analisis memakai status *kedaluwarsa* dari `period.mixin`) dan ditemukan lewat tabel ini.

1. Pengesahan selalu lewat pengajuan, agar kelengkapan dicek.
2. Draf yang tidak dipakai dihapus, bukan dicabut.
3. **Temuan:** otorisasi yang `berlaku_sampai`-nya sudah lewat sebelum disahkan akan langsung masuk *Lewat masa berlaku*. Usulan: kelengkapan saat diajukan juga mensyaratkan `berlaku_sampai ≥ hari ini`. Ini kandidat aturan bisnis baru (langkah 7).
4. Dua otorisasi untuk pasangan yang sama yang diajukan bersamaan tidak saling mengganti sampai salah satunya disahkan.
5. Otorisasi yang diajukan tidak dicabut; KaLab memakai **kembalikan**.
6. Otorisasi yang sudah disahkan tidak diedit. Perubahan lingkup, level, atau masa berlaku dibuat sebagai otorisasi baru (*superseding*, §11.9.2), sehingga riwayat utuh.
7. Perpanjangan setelah lewat masa berlaku dilakukan dengan otorisasi baru (→ Diganti), bukan dengan menghidupkan otorisasi lama.
8. **[ASUMSI]** Diganti dan Dicabut adalah status akhir.

### 4.2 S2 · Evaluasi Ulang Otorisasi

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| ● | catat pemicu | Terbuka | KF-SDM-25 |
| Terbuka | putuskan `[keputusan ∈ {diperpanjang, dibatasi, naik level}]` / susun otorisasi baru | Diputuskan | KF-SDM-25, 22 |
| Terbuka | putuskan `[keputusan = dicabut]` / cabut otorisasi | Diputuskan | KF-SDM-25, 06 |
| Terbuka | putuskan `[keputusan = tetap berlaku]` **\*** | Diputuskan | **Belum ada di KF-SDM-25** |

| Dari \ Ke | Terbuka | Diputuskan |
|---|---|---|
| **Terbuka** | — | putuskan (tiga varian keputusan) |
| **Diputuskan** | ✗ (1) | — |

**Temuan dari sel "Terbuka → Diputuskan":** analisis PKG-10 dan KF-SDM-25 hanya punya keputusan *diperpanjang, dibatasi, dinaikkan, dicabut*. Padahal pemicu bisa terjadi tanpa perlu perubahan, misalnya alat diganti tetapi kompetensi personel masih memadai. Tanpa keputusan **tetap berlaku**, evaluasi ulang itu akan selamanya *Terbuka* dan membuat S4 gagal. Keputusan ini sekaligus menjadi jalan keluar bila pemicu tercatat keliru, karena rekaman bukti tidak boleh dihapus (`evidence.mixin`). → KF-SDM-25 perlu ditambah (bagian 6.4).

1. **[ASUMSI]** Keputusan yang berubah dicatat sebagai evaluasi ulang baru, bukan membuka kembali yang lama.

### 4.3 S3 · Item Pelatihan

Item pelatihan adalah anak Rencana Pelatihan. Yang disimpan hanya *rencana / terlaksana / batal*; sub-status *Menunggu evaluasi* dan *Dievaluasi* dihitung (§9.3.1).

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| ● | tambah item `[rencana Draf]` | Direncanakan | KF-SDM-31 |
| Direncanakan | hapus item `[rencana masih Draf]` **\*** | ◉ | CRUDL |
| Direncanakan | catat realisasi `[rencana Disahkan]` (peserta pertama) | Terlaksana.Menunggu evaluasi | KF-SDM-33 |
| Direncanakan | tandai batal `[alasan diisi]` | Batal | KF-SDM-37 (O) |
| Terlaksana.Menunggu evaluasi | when(setiap realisasi punya evaluasi efektivitas) | Terlaksana.Dievaluasi | KF-SDM-34 |

| Dari \ Ke | Direncanakan | Menunggu evaluasi | Dievaluasi | Batal |
|---|---|---|---|---|
| **Direncanakan** | — | catat realisasi | ✗ (1) | tandai batal |
| **Menunggu evaluasi** | ✗ (2) | — | when(semua dievaluasi) | ✗ (3) |
| **Dievaluasi** | ✗ | (4) | — | ✗ (3) |
| **Batal** | ✗ (5) | ✗ | ✗ | — |

1. Evaluasi butuh realisasi lebih dulu.
2. Realisasi tidak dihapus (`evidence.mixin`), jadi item tidak kembali ke Direncanakan.
3. Item tidak bisa batal setelah ada realisasi; peserta yang tidak hadir cukup tidak punya realisasi.
4. Bila realisasi peserta baru dicatat setelah semua dievaluasi, sub-status otomatis kembali ke *Menunggu evaluasi* karena dihitung dari data. Tidak perlu event.
5. **[ASUMSI]** Batal adalah status akhir. Pelatihan pengganti masuk rencana tahun berikutnya; revisi rencana setelah disahkan tidak dirancang (KU-2).

**Temuan:** *hapus item* (rencana masih Draf) tidak tertulis di analisis; ini bagian CRUDL item di dalam rencana, jadi tidak perlu KF baru. *Catat realisasi* butuh guard `[rencana Disahkan]`; kandidat aturan bisnis (langkah 7).

### 4.4 S4 · Surat Tugas dan Rencana Pelatihan

Berlaku untuk `labfik.sdm.surat.tugas` dan `labfik.sdm.rencana.pelatihan` (`labfik.approval.mixin`).

| Dari | Event `[guard]` / efek | Ke | KF |
|---|---|---|---|
| ● | buat | Draf | KF-SDM-10, 14 (Surat Tugas); KF-SDM-29 (Rencana) |
| Draf | ajukan `[kelengkapan per jenis]` / catat riwayat; Rencana: bekukan kebutuhan | Diajukan | KF-SDM-11, 32 |
| Draf | hapus `[belum pernah diajukan]` | ◉ | CRUDL |
| Diajukan | kembalikan / catat alasan | Draf | KF-SDM-06 |
| Diajukan | unggah berkas bertanda tangan / catat riwayat | Diajukan | KF-SDM-06 |
| Diajukan | sahkan `[berkas ada ∧ pengesah berwenang]` / catat pengesah, pencatat, tanggal sah | Disahkan | KF-SDM-06, 43 |
| Disahkan | revisi surat tugas disahkan `[Surat Tugas]` | Diganti | KF-SDM-14 (O) |
| Disahkan | cabut / catat alasan | Dicabut | KF-SDM-06 |

| Dari \ Ke | Draf | Diajukan | Disahkan | Diganti | Dicabut |
|---|---|---|---|---|---|
| **Draf** | — | ajukan | ✗ (1) | ✗ | ✗ (2) |
| **Diajukan** | kembalikan | unggah berkas | sahkan | ✗ | ✗ (3) |
| **Disahkan** | ✗ (4) | ✗ | — | revisi disahkan (Surat Tugas) | cabut |
| **Diganti** | ✗ | ✗ | ✗ | — | ✗ |
| **Dicabut** | ✗ | ✗ | ✗ | ✗ | — |

1. Pengesahan selalu lewat pengajuan, agar kelengkapan dicek.
2. Draf yang tidak dipakai dihapus.
3. Dokumen yang diajukan dikembalikan, bukan dicabut.
4. Dokumen yang sudah disahkan tidak diedit. Surat Tugas diubah lewat revisi (Pelengkap); Rencana Pelatihan tidak direvisi (KU-2).

**Tanpa status *Kedaluwarsa*.** Rencana Pelatihan mewarisi `period.mixin`, tetapi modul SDM tidak memakai penjadwal (kontrak Core K-3). Rencana yang periodenya sudah lewat tetap *Disahkan*; "masih berlaku" untuk K1 dihitung dari periode (`is_berlaku`). **[ASUMSI]** Diganti dan Dicabut adalah status akhir.

### 4.5 Penyatuan status

| Objek | Status di analisis / kebutuhan | Di rancangan ini |
|---|---|---|
| Otorisasi | draf, diajukan, disahkan, diganti, dicabut, **kedaluwarsa** (analisis PKG-10 versi awal, `period.mixin`) | *Kedaluwarsa* dihapus; diganti sub-status terhitung **Lewat masa berlaku** (S1, kontrak Core K-3) |
| Evaluasi ulang | terbuka, diputuskan | Sama (S2) |
| Item pelatihan | rencana, terlaksana, batal | **Direncanakan**, Terlaksana, Batal; ditambah sub-status terhitung Menunggu evaluasi/Dievaluasi (S3) |
| Surat Tugas, Rencana Pelatihan | status `approval.mixin` | **S4**: Draf, Diajukan, Disahkan, Diganti (Surat Tugas saja), Dicabut. *Kedaluwarsa* tidak dipakai |
| Bukti Kompetensi, baris Penugasan | berlaku / tidak berlaku | Nilai terhitung dari tanggal; tidak digambar |

Label "Direncanakan" dipakai di diagram; nilai teknisnya tetap `rencana`.

---

## 5. Perbandingan dengan contoh Tata Kelola

Dibandingkan dengan [proses-bisnis-tata-kelola.md](https://github.com/mochfebriyan/skripsi/blob/febriyan-skripsi/projek-fiklab/rancangan/proses-bisnis-tata-kelola.md) (branch `febriyan-skripsi`) sebagai contoh format. Perbandingan ini hanya di dokumen; diagram SDM tidak merujuk modul lain.

| Aspek | Tata Kelola | SDM (dokumen ini) |
|---|---|---|
| Isi | 4 activity (A1 Pengesahan, A2 SOP/IK, A3 Rencana, A4 Struktur), 2 state machine | 4 activity (A1–A3 proses PKG, A4 Pengesahan Dokumen SDM), 4 state machine |
| Pengesahan | A1 + S1, dipanggil A2–A4 | A4 + S1/S4, dipanggil A1–A3. Polanya sama; isinya khusus dokumen SDM (kelengkapan per jenis, penggantian otorisasi pasangan sama, pembekuan kebutuhan) |
| Pihak di luar sistem | Lajur pejabat penanda tangan | Lajur penyetuju pengecualian (A1) dan pejabat penanda tangan (A4) |
| Waktu (⧗) | Tanggal tinjau dan periode lapor (dihitung) | Jadwal pelatihan dan waktu evaluasi (kejadian nyata), pemicu evaluasi ulang (dicatat manual); tidak ada penjadwal |
| Sub-status terhitung (§9.3.1) | S2 Mutakhir/Perlu Ditinjau | S1 Berlaku/Lewat masa berlaku, S3 Menunggu evaluasi/Dievaluasi |
| Status kedaluwarsa | Ada (Penjadwal, Pelengkap) | Tidak ada (K-3) |
| Temuan dari tabel status × transisi | 3 transisi baru, tanpa KF baru | 1 transisi baru (lewat masa berlaku), **1 keputusan baru** yang mengubah KF-SDM-25, 2 kandidat aturan bisnis |
| Gaya dan skrip | `contoh-tata-kelola/activity_state.py`, hitam-putih | `sdm/activity_state.py`, fungsi dan gaya sama |

---

## 6. Cek silang, isu terbuka, dan koreksi

### 6.1 KF → proses

| KF | Muncul di |
|---|---|
| KF-SDM-01, 02, 03 | CRUDL (langkah 6) |
| KF-SDM-04 | Dihitung saat dibaca (guard di S1, status S3 di A1) |
| KF-SDM-05 | «report» |
| KF-SDM-06, 43 | A4 (dipanggil A1, A2, A3); S1, S4 |
| KF-SDM-07, 08 | A1 Catat hasil seleksi, Buat personel asisten, Setujui pengecualian (manual) |
| KF-SDM-09 | A1 Tetapkan kebutuhan petugas |
| KF-SDM-10, 11 | A1 Susun surat tugas; kelengkapan di A4 |
| KF-SDM-12, 13 | Dihitung / «report» |
| KF-SDM-14 | A1 Buat revisi surat tugas (O); A4 Ganti status dokumen lama; S4 |
| KF-SDM-15 | Bagian dari Susun surat tugas (lampiran, O) |
| KF-SDM-16 | Tidak digambar (pencatatan, O) |
| KF-SDM-17, 39 | A4 Terbitkan dokumen PDF (O) |
| KF-SDM-18, 19 | A2 Tetapkan pelaksana tugas/alat (+ CRUDL master) |
| KF-SDM-20, 21 | A2 Catat asesmen, Buat bukti kompetensi |
| KF-SDM-22, 23, 24 | A2 Susun otorisasi; A4 kelengkapan dan Ganti status dokumen lama; S1 |
| KF-SDM-25 | A2 Catat evaluasi ulang; S2 |
| KF-SDM-26, 27 | Dihitung / «report» |
| KF-SDM-28 | Bagian dari CRUDL Tugas/Alat (O) |
| KF-SDM-29–35 | A3; KF-SDM-32 di A4; S3, S4 |
| KF-SDM-36 | Dihitung saat dibaca |
| KF-SDM-37 | A3 Tandai item batal (O); S3 |
| KF-SDM-38, 40, 41, 42 | «report» / dihitung |

Semua KF punya tempat: tugas activity, transisi state machine, CRUDL, «report», atau perilaku sistem. Tidak ada KF yang bergantung pada proses modul lain.

### 6.2 Kriteria → tugas

| Indikator | Kriteria | Tugas «user» yang menghasilkan rekaman |
|---|---|---|
| PKG-04 | S1 / S2 / S3 / S4 | Tetapkan kebutuhan petugas / Susun surat tugas + A4 / Bukti Kompetensi (CRUDL) / Catat hasil seleksi |
| PKG-10 | Penyebut / S1 / S2 / S3 / S4 | Tetapkan pelaksana / Catat asesmen / Susun otorisasi + A4 / Susun otorisasi (supervisor) / Catat evaluasi ulang |
| PKG-14 | K1 / K2 / K3 / K4 | Buat rencana + Lengkapi kebutuhan + A4 / Susun item / Catat realisasi / Catat evaluasi efektivitas |

Setiap transisi state machine punya *use case* ([use-case-sdm.md](use-case-sdm.md) bagian 4.2) atau perilaku sistem (when-transition terhitung).

### 6.3 [KONFIRMASI]

| No | Pertanyaan | Ke siapa |
|---|---|---|
| KP-1 | Tambah keputusan **tetap berlaku** pada evaluasi ulang otorisasi (S2)? | Zahir (pengguna) |
| KP-2 | Siapa penyetuju pengecualian syarat asisten: Koor Prodi atau KaLab? (lajur A1) | KaLab (K2) |
| KU-1 | Pemicu dan keputusan evaluasi ulang biasanya di hari berbeda? Bila ya, tugas A2 dipecah dua seperti *use case*-nya | KaLab |
| KU-2 | Revisi Rencana Pelatihan setelah disahkan tidak dirancang (S3, S4) | Zahir |
| Belum dijawab dari langkah 4 | **KB-1** penyebut PKG-10 = pelaksana yang ditetapkan KaLab (default di A2); **KB-3** Surat Tugas ditolak bila asisten tanpa seleksi lulus (default di A4); KB-2 kebutuhan laboran per kelas | Zahir; KaLab |
| Lama | K7 (pengesah surat tugas), K10 (pengesah rencana pelatihan), wawancara no. 12, 16–18 | KaLab |
| Visual | Tampilan diagram belum dicek di draw.io **[VALIDASI]** | Zahir |

### 6.4 Dokumen lain yang perlu ikut berubah

| Dokumen | Perubahan |
|---|---|
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-25 | Tambah keputusan **tetap berlaku** (bila KP-1 disetujui) |
| [analisis-data-pengelolaan-10.md](../analisis/analisis-data-pengelolaan-10.md) bagian 4 (Evaluasi Ulang) | Sama: daftar keputusan ditambah *tetap berlaku* |
| Langkah 7 | Kandidat aturan bisnis `berlaku_sampai ≥ hari ini` saat otorisasi diajukan (S1 sel 3) dan `catat realisasi hanya bila rencana disahkan` (S3) |

### 6.5 Kesalahan sendiri yang ditemukan

| Di mana | Kesalahan | Koreksi |
|---|---|---|
| Versi 14 November 2026 | Pengesahan dan status Surat Tugas/Rencana memakai activity dan state machine modul Tata Kelola, sehingga diagram SDM bergantung pada diagram modul lain | A4 dan S4 (bagian 0) |
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-25 dan analisis PKG-10 | Keputusan evaluasi ulang tidak punya pilihan **tetap berlaku**, sehingga evaluasi yang tidak butuh perubahan akan terbuka selamanya dan menggagalkan S4 | KP-1 |
| [kebutuhan-sdm.md](kebutuhan-sdm.md) KF-SDM-22/23 | Tidak ada syarat masa berlaku belum lewat saat otorisasi diajukan | Kandidat AB (6.4) |
| Langkah 4 | KB-1 dan KB-3 diajukan sebagai pertanyaan tetapi tidak ditandai sebagai *default* yang dipakai bila belum dijawab | Dicatat eksplisit sebagai default (6.3) |
