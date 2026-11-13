# Proses Bisnis TO-BE Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF.** Langkah pertama rancangan TO-BE setelah metode diselaraskan dengan Wazlawick (2024). Diagram: [activity-state-tata-kelola.drawio](activity-state-tata-kelola.drawio) (6 halaman).

## Posisi dalam metode

Urutan rancangan mengikuti Wazlawick (2024): proses bisnis (Bab 3) → use case sistem diturunkan dari proses bisnis (Bab 4) → expanded use case (Bab 6) → system sequence diagram (Bab 7) → conceptual model (Bab 8–11) → design class diagram (Bab 13).

Dokumen ini adalah langkah pertama. Masukannya:
- [brief](../brief/brief-tata-kelola-dokumen.md) dan analisis PKG-01/02/03/13: kriteria K1–K4 dan S1–S5;
- [bedah dokumen](../analisis/bedah-dokumen-tata-kelola.md): temuan as-is A1–A12;
- [kebutuhan](kebutuhan-tata-kelola.md): KF-01–38.

Use case diagram dan class diagram yang sudah ada ([use-case-tata-kelola.drawio](use-case-tata-kelola.drawio), [class-tata-kelola.drawio](class-tata-kelola.drawio)) akan **diturunkan ulang** dari dokumen ini pada langkah berikutnya.

## Pedoman yang dipakai (Wazlawick 2024, Bab 3)

| Pedoman | Penerapan |
|---|---|
| Hanya proses dan objek bisnis yang **nontrivial** yang dimodelkan (§3.4) | 4 activity diagram untuk proses inti dan 2 state machine untuk objek bisnis utama: dokumen. Kelola master (Personel, Jabatan, KPI, Dokumen Induk) tidak digambar karena trivial (pola CRUDL) |
| **Activity/BPMN untuk proses, state machine untuk objek** (§3.4) | A1–A4 = proses. S1–S2 = siklus status dokumen |
| Jenis tugas dibedakan: user, service, manual (§3.2.1) | Stereotype «user», «service», «manual» dengan warna berbeda |
| Swimlane per aktor (§3.2.3) | Setiap activity memakai lajur aktor + lajur Sistem |
| Nama tugas = **kata kerja kuat + objek domain**; tanpa "dan/atau"; gateway tidak diberi nama, kondisi ditulis di alur (§3.2.4) | Contoh: "Ajukan dokumen", "Catat distribusi dokumen". Kondisi ditulis sebagai `[guard]` |
| Lanjutan ke diagram lain lewat penanda tautan (§3.2.3) | Di UML ditulis sebagai **«call behavior»**: A2–A4 memanggil A1 |
| State machine: `event [guard] / efek` (§3.3) | S1, S2 |
| Tabel status × transisi untuk **menemukan transisi dan use case yang terlewat** (§3.3, Tabel 3–1) | [Bagian 3](#3-tabel-status--transisi-s1) |

## 1. Daftar diagram

| ID | Diagram | Jenis | PKG / kriteria | Aktor |
|---|---|---|---|---|
| **A1** | Pengesahan Dokumen | Activity (dipanggil A2–A4) | K1 (PKG-01/03/13), S2 (PKG-02) | Penyusun, Sistem, Pemeriksa, Pengesah |
| **A2** | Siklus Dokumen SOP/IK | Activity | PKG-02 S1–S5 | Laboran, KaLab, Sistem |
| **A3** | Siklus Rencana (strategis, RKT, IKU, pengembangan) | Activity | PKG-01 K1–K4, PKG-13 K1–K4 | KaLab, PIC, Sistem |
| **A4** | Siklus Struktur Organisasi (satu masa SK) | Activity | PKG-03 K1–K4 | KaLab, Sistem |
| **S1** | Status dokumen terkendali | State machine | Semua dokumen yang memakai `approval.mixin` | — |
| **S2** | Kemutakhiran versi SOP/IK yang berlaku | State machine (rincian status *Disahkan*) | PKG-02 S3 | — |

## 2. Ringkasan alur

**A1 Pengesahan Dokumen.**
1. Penyusun mengajukan dokumen.
2. Sistem memeriksa kelengkapan. Kalau kurang, penyusun melengkapi lalu mengajukan ulang.
3. Bila tahap pemeriksaan aktif, pemeriksa memeriksa dokumen dan bisa mengembalikannya untuk diperbaiki.
4. Untuk dokumen rutin (rencana, SK), penyusun **menerbitkan dokumen resmi** dan sistem menghasilkan PDF. Untuk SOP/IK, berkasnya sudah diunggah di A2.
5. Dokumen dicetak, lalu pengesah meninjau dan **menandatangani secara manual**. Bila tidak disetujui, penyusun mencatat pengembalian dan memperbaiki dokumen.
6. Penyusun mengunggah dokumen bertanda tangan.
7. Pengesah menekan *Sahkan*. Sistem memvalidasi berkas, mengubah status, dan mencatat jejak.

Pengesahan berlangsung **lintas hari**, jadi terbit, tanda tangan, unggah, dan sahkan adalah sesi terpisah.

**A2 Siklus SOP/IK.**
1. Dokumen baru didaftarkan di Dokumen Induk.
2. Naskah disusun di luar sistem, lalu versinya diunggah.
3. Versi disahkan lewat A1. Sistem mengganti status versi lama dan menjadwalkan tinjau ulang.
4. Distribusi dan sosialisasi dicatat secara paralel.
5. Saat jadwal tiba, sistem mengirim pengingat dan Laboran meninjau ulang. Ada tiga kemungkinan hasil:
   - **tetap berlaku**: jadwal diperbarui;
   - **perlu revisi**: kembali ke penyusunan naskah;
   - **tidak diperlukan lagi**: KaLab mencabut dokumen.

**A3 Siklus Rencana.**
1. Untuk rencana pengembangan, KaLab menyusun analisis gap dulu.
2. Item rencana disusun dan disahkan lewat A1.
3. Tiap akhir periode lapor, sistem mengirim pengingat, PIC mengisi realisasi, dan sistem memperbarui status kriteria.
4. Rencana bisa direvisi di tengah periode.
5. Saat periode berakhir, sistem menandai rencana kedaluwarsa. KaLab lalu mencatat tinjauan (ditambah ukuran manfaat untuk pengembangan) dan menetapkan keputusan perbaikan untuk rencana berikutnya.

**A4 Siklus Struktur.**
1. KaLab melengkapi uraian jabatan dan menyusun SK, lalu SK disahkan lewat A1 oleh Dekan.
2. Sistem memberlakukan penugasan jabatan, sehingga wewenang aktif mengikuti SK.
3. Rapat koordinasi dicatat sesuai jadwal. Evaluasi struktur dicatat bila sudah waktunya.
4. Bila struktur perlu diubah atau masa SK berakhir, masa SK ditutup dan siklus baru dimulai.

## 3. Tabel status × transisi (S1)

Baris = status asal, kolom = status tujuan. Dengan teknik Wazlawick (Tabel 3–1), setiap sel kosong ditanyakan: "apakah transisi ini mungkin terjadi?"

| Dari \ Ke | Draf | Diajukan | Diperiksa | Disahkan | Diganti | Dicabut | Kedaluwarsa |
|---|---|---|---|---|---|---|---|
| **Draf** | | ajukan | | | | | |
| **Diajukan** | **tarik kembali**, **kembalikan** | | periksa | sahkan | | | |
| **Diperiksa** | **kembalikan** | ? | | sahkan | | | |
| **Disahkan** | ? | | | | revisi baru disahkan | **cabut** | **when(periode berakhir)** |
| **Diganti** | | | | ? | | | |
| **Dicabut** | | | | ? | | | |
| **Kedaluwarsa** | | | | ? | | | |

Ditambah transisi *hapus* dari Draf ke status akhir (hanya untuk draf yang belum pernah diajukan).

**Cetak tebal** = transisi yang baru ditemukan lewat tabel ini. Transisi tersebut belum ada di analisis maupun class diagram sebelumnya. Sel **?** adalah pertanyaan untuk KaLab/Pak Widi **[KONFIRMASI]**:

| Sel | Pertanyaan | Asumsi sementara |
|---|---|---|
| Diperiksa → Diajukan | Bisakah pemeriksa meneruskan tanpa keputusan? | Tidak. Pemeriksa harus memutuskan layak atau dikembalikan |
| Disahkan → Draf | Bila ada salah ketik setelah disahkan, boleh diedit langsung? | Tidak. Harus lewat revisi agar jejak pengesahan utuh (ISO 8.3.2) |
| Diganti/Dicabut/Kedaluwarsa → Disahkan | Bisakah dokumen diaktifkan kembali (misalnya perpanjangan masa SK)? | Tidak. Dibuat sebagai revisi atau dokumen baru |

## 4. Temuan untuk langkah berikutnya

### 4.1 Penurunan use case (bahan Step 6, Wazlawick Bab 4)

Hasil akhirnya, beserta nomor UC yang baru, ada di [use-case-tata-kelola.md](use-case-tata-kelola.md). Kolom terakhir tabel di bawah memakai **nomor versi lama**.

Menurut Wazlawick, tugas **«user»** menjadi kandidat use case sistem. Tugas «service» menjadi fungsi sistem (bukan use case), dan tugas «manual» berada di luar sistem.

| Tugas «user» | Diagram | Kandidat use case | Bandingkan dengan UC lama |
|---|---|---|---|
| Ajukan dokumen | A1 | Ajukan Dokumen | UC-15 |
| Lengkapi / Perbaiki dokumen | A1 | Bagian dari menyunting dokumen masing-masing (bukan UC tersendiri) | — |
| Periksa dokumen | A1 | Periksa Dokumen | UC-16 |
| Kembalikan dokumen, Catat pengembalian dokumen | A1 | **Kembalikan Dokumen** (baru) | — |
| Terbitkan dokumen resmi | A1 | Terbitkan Dokumen Resmi | UC-18 (diganti nama, lebih *essential*) |
| Unggah dokumen bertanda tangan | A1 | **Unggah Dokumen Bertanda Tangan**, berdiri sendiri | UC-22. Ternyata **bukan fragmen**: dilakukan penyusun di sesi berbeda dari *Sahkan* oleh pengesah. Relasi «include» dihapus |
| Sahkan dokumen | A1 | Sahkan Dokumen | UC-17 |
| Daftarkan dokumen induk | A2 | Kelola Dokumen Induk «CRUDL» | UC-07 |
| Unggah versi dokumen | A2 | Unggah Versi Dokumen | UC-08 |
| Catat distribusi dokumen | A2 | **Catat Distribusi Dokumen** | UC-09 dipecah, karena nama dengan "dan" menandakan dua tugas (§3.2.4) |
| Catat sosialisasi dokumen | A2 | **Catat Sosialisasi Dokumen** | UC-09 dipecah |
| Tinjau ulang dokumen | A2 | Tinjau Ulang Dokumen | UC-21 |
| Cabut dokumen | A2 | **Cabut Dokumen** (baru; sudah ada di KF-31 tetapi belum punya UC) | — |
| Susun analisis gap, Susun item rencana | A3 | Susun Rencana (gap bagian dari rencana pengembangan) **[ditentukan di Step 6]** | UC-12 |
| Buat revisi rencana | A3 | Bagian dari Susun Rencana, atau UC tersendiri **[ditentukan di Step 6]** | UC-12 |
| Isi realisasi item | A3 | Isi Realisasi | UC-13 |
| Catat tinjauan rencana, Ukur manfaat program, Tetapkan keputusan perbaikan | A3 | Catat Tinjauan Rencana (satu sesi) | UC-14 |
| Lengkapi uraian jabatan | A4 | Kelola Jabatan «CRUDL» | UC-02 |
| Susun SK penetapan pengelola | A4 | Susun SK Penetapan | UC-03 |
| Catat rapat koordinasi | A4 | Catat Rapat Koordinasi | UC-05 |
| Catat evaluasi struktur | A4 | Catat Evaluasi Struktur | UC-06 |
| (dari S1) tarik kembali | S1 | **Tarik Pengajuan** (baru) | — |

### 4.2 Fungsi sistem dari tugas «service»

Fungsi ini tidak menjadi use case, tetapi menjadi aturan atau perilaku sistem:
- Periksa kelengkapan dokumen (KF-24)
- Catat pengajuan
- Kirim notifikasi pengajuan
- Hasilkan PDF dokumen (KF-25)
- Validasi pengesahan (KF-33)
- Ubah status (KF-31)
- Catat jejak (KF-34)
- Ganti status versi lama (KF-11)
- Jadwalkan tinjau ulang (KF-14)
- Kirim pengingat tinjau ulang (KF-15)
- Perbarui jadwal tinjau (KF-38)
- Berlakukan penugasan jabatan
- Tutup masa SK
- Tandai rencana kedaluwarsa
- **Kirim pengingat realisasi (baru)**
- Perbarui status kriteria (KF-36)

### 4.3 Dampak ke kebutuhan dan class diagram

| Temuan | Dampak |
|---|---|
| Status **Kedaluwarsa** belum ada di `approval.mixin.state` | Tambah ke daftar status. Transisinya dipicu waktu (`when`) |
| Event **kembalikan**, **tarik kembali**, **cabut** perlu alasan | Tambah field alasan (atau catatan wajib di riwayat) pada mixin pengesahan. Tambah method `action_kembalikan()`, `action_tarik()` |
| **Berlakukan penugasan jabatan** (A4) | Wewenang aktif dihitung dari baris SK yang berstatus Disahkan dan masih berlaku. Menguatkan KF-02/03 dan `jabatan.get_pemegang_aktif()` |
| **Pengingat realisasi** (A3) | Kandidat KF baru (opsional) |
| S2: *Perlu Ditinjau* dan *Menunggu Revisi* | Bukan nilai `state`, tetapi status turunan ({compute}). Ini *modal class* (§9.3). Perlu disebut eksplisit di conceptual model |
| Tiga set status di analisis lama (PKG-01, 02, 13) | Disatukan di S1: *berlaku* = Disahkan, *selesai* = Kedaluwarsa |

## 5. Pertanyaan terbuka

- [ ] Dekan/Pemeriksa login sendiri atau diwakili KaLab? (A1)
- [ ] Bisakah dokumen yang dicabut, diganti, atau kedaluwarsa diaktifkan kembali? (S1)
- [ ] Apakah *Menunggu Revisi* masih dihitung mutakhir untuk PKG-02 S3? (S2)
- [ ] Berapa frekuensi rapat koordinasi dan evaluasi struktur? (A4)
- [ ] Apakah pengesah bisa menolak setelah dokumen dicetak, dan bagaimana praktiknya? (A1, *Tinjau dokumen cetak*)

## Referensi

Wazlawick, R. S. (2024). *Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python* (2nd ed.). Morgan Kaufmann/Elsevier. Bab 3 (§3.2–3.4), Bab 9 (§9.3). Ringkasan per bab: `docs/OOAD_Wazlawick_2024_Knowledge_Pack/`.
