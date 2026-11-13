# Expanded Use Case Modul Tata Kelola & Dokumen

13 November 2026 · Febriyan · PKG-01, 02, 03, 13

**Status: DRAF. Bahan kerja, tidak dicantumkan di proposal.** Dokumen ini adalah Step 7 rancangan TO-BE dan menjadi bahan untuk:
- system sequence diagram (Step 8);
- conceptual model (Step 9);
- skenario uji *black box* (Bab II 2.4).

Use case yang dijabarkan diambil dari [use-case-tata-kelola.md](use-case-tata-kelola.md).

## Aturan penulisan (Wazlawick 2024, Bab 6)

- **Alur utama** berupa urutan transaksi bergantian: aktor mengirim informasi, sistem menampilkan informasi. Alurnya lurus, tanpa "jika" atau perulangan (§6.2, §6.4).
- **Essential:** tidak menyebut tombol, layar, atau menu. "Memilih" berarti memilih dengan cara apa pun yang nanti dirancang (§6.4.1, §6.4.3).
- **Data disebut eksplisit** (§6.4.2). Langkah internal seperti "sistem menyimpan" tidak ditulis (§6.4.4).
- **Varian** (V) = cara lain mencapai tujuan. **Eksepsi** (E) = hambatan, biasanya lahir dari satu aturan bisnis. Setiap alur alternatif menyatakan akhirnya: *berhasil*, *gagal*, atau *kembali ke langkah n* (§6.3).
- **Prakondisi** dianggap benar sebelum use case dimulai dan tidak diperiksa lagi. **Pascakondisi** = hasil bila berhasil (§6.6).

## 1. Aturan bisnis

Eksepsi merujuk ke kode aturan di bawah. Aturan ini nantinya juga menjadi bahan aturan validasi (constraint) di design class diagram.

| Kode | Aturan | Sumber |
|---|---|---|
| AB-01 | Dokumen hanya bisa diajukan bila kelengkapannya terpenuhi. Isinya berbeda per jenis: **Rencana**: setiap item punya kegiatan, target, satuan, jadwal, PIC, dan anggaran; rencana strategis punya minimal satu sasaran dan satu program; rencana pengembangan punya temuan gap untuk keempat aspek (atau alasan tidak ada gap), dan setiap item merujuk minimal satu temuan gap serta punya nilai risiko dan manfaat. **SK**: nomor SK, periode, minimal satu baris penetapan, dan setiap jabatan yang ditetapkan punya tugas, wewenang, dan atasan. **Versi SOP/IK**: berkas naskah, nomor revisi, periode tinjau ulang, dan ringkasan perubahan (untuk revisi ke-1 dan seterusnya) | KF-24, PKG-01/03/13 K2 |
| AB-02 | Pengesahan, pengembalian oleh pengesah, dan pencabutan hanya oleh pemegang **jabatan aktif** yang punya wewenang untuk **jenis dokumen** tersebut | KF-33, bedah dokumen A3 |
| AB-03 | Pengesahan membutuhkan berkas bertanda tangan | KF-33, brief batasan 3 |
| AB-04 | Satu dokumen induk hanya punya satu versi berlaku. Versi lama otomatis Diganti saat versi baru disahkan | KF-11, ISO 8.3.2 |
| AB-05 | Pengembalian, penarikan, dan pencabutan wajib disertai alasan | KF-39–41 |
| AB-06 | Dokumen yang sudah diajukan atau disahkan tidak bisa diubah isinya. Perubahan dilakukan lewat pengembalian ke Draf atau lewat revisi | S1, ISO 8.3.2 |
| AB-07 | Rekaman bukti (rapat, evaluasi, distribusi, sosialisasi, tinjau ulang, realisasi, tinjauan) tidak dihapus. Koreksi lewat ubah dan tercatat di riwayat **[KONFIRMASI]** | Matriks CRUDL |
| AB-08 | Tanggal tinjau ulang berikutnya = tanggal berlaku (atau tanggal tinjauan terakhir) + periode tinjau ulang | KF-14, PKG-02 S3 |
| AB-09 | Bila tahap pemeriksaan aktif untuk suatu jenis dokumen, dokumen harus Diperiksa sebelum bisa disahkan | KF-32 |
| AB-10 | Realisasi hanya bisa diisi untuk rencana yang Disahkan dan masih berlaku. Status capaian "tidak relevan" wajib disertai alasan | KF-27, IKU bagian 8 |
| AB-11 | Realisasi suatu item hanya diisi oleh PIC item itu atau KaLab | KF-27 |
| AB-12 | Realisasi wajib disertai minimal satu bukti | PKG-01 K3 ("realisasi berbukti") |
| AB-13 | Untuk satu dokumen induk, hanya boleh ada satu versi yang sedang diproses (Draf, Diajukan, atau Diperiksa) **[USULAN PENULIS]** | Mencegah dua revisi berjalan bersamaan |
| AB-14 | Dalam satu unit, hanya boleh ada satu dokumen berlaku untuk jenis rencana dan periode yang sama, serta satu SK penetapan berlaku. Dokumen baru yang disahkan menggantikan yang lama **[ASUMSI]** | S1 *revisi baru disahkan* |

## 2. Tabel deskripsi use case

Semua use case selain «CRUDL» dan «report» (keduanya memakai pola di [bagian 4](#4-pola-use-case-berstereotype-67)). Kolom **Rinci** menunjuk ke alur lengkap di bagian 3.

| UC | Tujuan | Aktor | Prakondisi | Pascakondisi (berhasil) | Eksepsi / aturan | Rinci |
|---|---|---|---|---|---|---|
| UC-03 Susun SK Penetapan Pengelola | SK pengelola tersusun sebagai draf | KaLab | Jabatan dan personel yang akan ditetapkan sudah terdaftar | SK berstatus Draf berisi nomor, periode, menimbang, mengingat, diktum, dan baris personel × jabatan × ruang | Personel tidak aktif; periode tidak valid; varian: SK baru dari SK sebelumnya | — |
| UC-04 Catat Rapat Koordinasi | Bukti koordinasi (PKG-03 K3) | KaLab | SK berlaku | Rapat tercatat: tanggal, agenda, peserta, keputusan, notulen, bukti | Peserta kosong; AB-07 | — |
| UC-05 Catat Evaluasi Struktur | Bukti evaluasi (PKG-03 K4) | KaLab | SK berlaku | Evaluasi tercatat, tertaut ke SK baru atau jabatan yang direvisi (bila ada) | AB-07 | — |
| UC-08 Unggah Versi Dokumen | Versi baru SOP/IK tersedia sebagai draf | Laboran | Dokumen induk terdaftar | Versi berstatus Draf | AB-13; nomor revisi tidak valid | [3.1](#31-uc-08-unggah-versi-dokumen) |
| UC-09 Catat Distribusi Dokumen | Bukti tersedia di titik penggunaan (PKG-02 S4) | Laboran | Versi berlaku ada | Distribusi tercatat: versi, lokasi, tanggal, petugas, bukti | Lokasi bukan lokasi penggunaan dokumen; AB-07 | — |
| UC-10 Catat Sosialisasi Dokumen | Bukti sosialisasi (PKG-02 S5) | Laboran | Versi berlaku ada | Sosialisasi tercatat: versi, tanggal, metode, peserta, bukti | Peserta kosong; AB-07 | — |
| UC-11 Tinjau Ulang Dokumen | Kemutakhiran versi terbukti (PKG-02 S3) | Laboran, KaLab | Versi berlaku ada | Hasil tinjauan tercatat; tanggal tinjau berikutnya diperbarui atau dokumen menunggu revisi | Catatan kosong untuk hasil "perlu revisi" | [3.2](#32-uc-11-tinjau-ulang-dokumen) |
| UC-16 Susun Rencana | Rencana tersusun sebagai draf | KaLab | Periode tersedia | Rencana berstatus Draf beserta isinya | Periode di luar rencana induk; PIC tidak aktif | [3.3](#33-uc-16-susun-rencana) |
| UC-18 Isi Realisasi Rencana | Bukti pelaksanaan (K3) | Laboran, KaLab | Rencana Disahkan dan berlaku | Realisasi tercatat beserta bukti | AB-10, AB-11, AB-12 | [3.4](#34-uc-18-isi-realisasi-rencana) |
| UC-19 Catat Tinjauan Rencana | Bukti tinjauan (K4) | KaLab | Rencana Disahkan atau Kedaluwarsa | Tinjauan tercatat: peserta, ringkasan, keputusan, ukuran manfaat (pengembangan), tautan ke rencana berikutnya | Ukuran manfaat kosong untuk rencana pengembangan; AB-07 | — |
| UC-21 Ajukan Dokumen | Dokumen masuk proses pengesahan | *Penyusun* | Dokumen Draf | Dokumen Diajukan; pemeriksa/pengesah diberi tahu | AB-01; belum ada jabatan berwenang (AB-02) | [3.5](#35-uc-21-ajukan-dokumen) |
| UC-22 Tarik Pengajuan Dokumen | Dokumen kembali bisa disunting | *Penyusun* | Dokumen Diajukan, belum Diperiksa | Dokumen Draf, alasan tercatat | AB-05 | — |
| UC-23 Periksa Dokumen | Dokumen dinyatakan layak untuk disahkan | Pemeriksa | Dokumen Diajukan; pemeriksaan aktif untuk jenisnya | Dokumen Diperiksa; catatan pemeriksaan tercatat | Bukan pemeriksa berwenang | — |
| UC-24 Kembalikan Dokumen | Dokumen dikembalikan untuk diperbaiki | Pemeriksa, *Pengesah* | Dokumen Diajukan atau Diperiksa | Dokumen Draf, alasan tercatat, penyusun diberi tahu | AB-05; AB-02 | [3.6](#36-uc-24-kembalikan-dokumen) |
| UC-25 Terbitkan Dokumen Resmi | Dokumen rutin siap ditandatangani | *Penyusun* | Rencana/SK Diajukan (pemeriksaan tidak aktif) atau Diperiksa | Dokumen resmi tersedia sesuai format dokumen lab | Jenis dokumen bukan dokumen rutin (SOP/IK) | — |
| UC-26 Unggah Dokumen Bertanda Tangan | Bukti tanda tangan pengesah tersedia | *Penyusun* | Dokumen Diajukan/Diperiksa; dokumen resmi sudah diterbitkan (rencana/SK) | Berkas bertanda tangan tersimpan; pengesah diberi tahu | Berkas tidak terbaca | [3.7](#37-uc-26-unggah-dokumen-bertanda-tangan) |
| UC-27 Sahkan Dokumen | Dokumen berlaku resmi | *Pengesah* | Aktor memegang jabatan berwenang; dokumen Diajukan/Diperiksa | Dokumen Disahkan; dokumen/versi lama Diganti (bila ada); jadwal tinjau ulang dibuat (SOP/IK) | AB-03, AB-09, AB-04, AB-14 | [3.8](#38-uc-27-sahkan-dokumen) |
| UC-28 Cabut Dokumen | Dokumen tidak berlaku lagi | *Pengesah* | Dokumen Disahkan | Dokumen Dicabut, alasan tercatat | AB-05; AB-02 | — |
| UC-30 Atur Pengaturan Modul | Aturan modul sesuai kebijakan lab | KaLab | — | Pengaturan tahap pemeriksaan per jenis dokumen dan siklus tinjau ulang standar tersimpan | Siklus tinjau ulang ≤ 0 | — |
| UC-31 Kedaluwarsakan Dokumen Berperiode | Status dokumen sesuai masa berlakunya | Penjadwal | Ada dokumen Disahkan yang periodenya sudah berakhir | Dokumen Kedaluwarsa; KaLab diberi tahu | — | — |
| UC-32 Kirim Pengingat Jadwal | Aktor tidak melewatkan tenggat | Penjadwal | Ada versi yang mendekati tanggal tinjau ulang, atau periode lapor realisasi berakhir | Pengingat terkirim ke Laboran/KaLab atau PIC item | — (opsional, KF-15 dan KF-43) | — |

## 3. Expanded use case kunci

Delapan use case di bawah dijabarkan penuh karena menjadi inti siklus dokumen dan siklus rencana. Kedelapannya juga kandidat untuk system sequence diagram di Step 8.

### 3.1 UC-08 Unggah Versi Dokumen

**Aktor:** Laboran · **Pemangku kepentingan:** KaLab, Pengguna Lab · **Prakondisi:** dokumen induk sudah terdaftar (UC-07).

**Alur utama**
1. Laboran memilih dokumen induk.
2. Sistem menampilkan kode, judul, jenis, kategori, versi berlaku (nomor revisi, tanggal berlaku), dan riwayat versi. [V1]
3. Laboran mengirim berkas naskah, nomor revisi, tanggal pembuatan, bagian yang diubah, ringkasan perubahan, alasan revisi, dan periode tinjau ulang.
4. Sistem menampilkan versi baru berstatus Draf beserta nomor revisinya.

**V1 Versi pertama** (belum ada versi berlaku)
- V1.1 Sistem menampilkan bahwa dokumen belum punya versi berlaku.
- V1.2 Laboran mengirim berkas naskah, nomor revisi 0, tanggal pembuatan, dan periode tinjau ulang.
- V1.3 Kembali ke langkah 4.

**E1 Ada versi yang sedang diproses** (AB-13), di langkah 2
- E1.1 Sistem menampilkan versi yang sedang Draf, Diajukan, atau Diperiksa.
- E1.2 Use case **gagal**. Laboran melanjutkan versi itu.

**E2 Nomor revisi tidak lebih besar dari versi berlaku**, di langkah 3
- E2.1 Sistem menampilkan nomor revisi berlaku.
- E2.2 Kembali ke langkah 3.

**Pascakondisi:** versi baru berstatus Draf, siap diajukan (UC-21).

### 3.2 UC-11 Tinjau Ulang Dokumen

**Aktor:** Laboran, KaLab · **Prakondisi:** dokumen punya versi Disahkan.

**Alur utama**
1. Aktor meminta daftar dokumen yang perlu atau akan ditinjau ulang.
2. Sistem menampilkan dokumen beserta versi berlaku, tanggal tinjau ulang berikutnya, dan status kemutakhirannya (Mutakhir / Perlu Ditinjau).
3. Aktor memilih satu dokumen.
4. Sistem menampilkan rincian versi berlaku dan riwayat tinjau ulang sebelumnya.
5. Aktor mengirim hasil tinjauan "tetap berlaku", tanggal tinjauan, dan catatan. [V1, V2]
6. Sistem menampilkan hasil tinjauan dan tanggal tinjau ulang berikutnya (AB-08).

**V1 Perlu revisi**, di langkah 5
- V1.1 Aktor mengirim hasil "perlu revisi", tanggal tinjauan, dan catatan bagian yang perlu direvisi.
- V1.2 Sistem menampilkan versi berstatus Menunggu Revisi.
- V1.3 Use case **berhasil**. Revisi dilanjutkan lewat UC-08.

**V2 Tidak diperlukan lagi**, di langkah 5
- V2.1 Aktor mengirim hasil "tidak diperlukan lagi", tanggal tinjauan, dan alasan.
- V2.2 Sistem menampilkan bahwa dokumen diusulkan untuk dicabut beserta jabatan yang berwenang mencabut.
- V2.3 Use case **berhasil**. Pencabutan dilakukan lewat UC-28.

**E1 Catatan kosong** untuk hasil "perlu revisi" atau "tidak diperlukan lagi"
- E1.1 Sistem menampilkan bahwa catatan wajib diisi.
- E1.2 Kembali ke langkah 5.

**Pascakondisi:** tinjauan tercatat. Versi kembali Mutakhir dengan jadwal baru, Menunggu Revisi, atau diusulkan dicabut (state machine S2).

### 3.3 UC-16 Susun Rencana

**Aktor:** KaLab · **Pemangku kepentingan:** Dekan, PIC kegiatan, Penilai Monev · **Prakondisi:** periode yang akan direncanakan tersedia.

**Alur utama**
1. KaLab mengirim jenis rencana (strategis, tahunan, IKU, atau pengembangan), nama, periode, dan rencana induk (bila ada). [V2, V3]
2. Sistem menampilkan rencana baru berstatus Draf beserta bagian yang harus diisi untuk jenis tersebut. [V1]
3. KaLab mengirim isi naratif (ringkasan, latar belakang, tujuan, ruang lingkup, referensi, landasan, penutup; untuk rencana strategis juga visi dan misi), baseline (data, nilai awal, sumber, PIC), serta untuk rencana strategis: sasaran strategis (kode, sasaran, KPI, target akhir) dan program (kode, nama, kegiatan utama, luaran, tahapan).
4. Sistem menampilkan rencana beserta bagian yang sudah dan belum terisi.
5. KaLab mengirim item rencana: kegiatan, KPI, baseline, target, satuan, jadwal mulai dan selesai, PIC, bukti yang diharapkan, anggaran, komponen anggaran, serta sasaran, program, dan sasaran Renstra terkait.
6. Sistem menampilkan daftar item beserta kelengkapan tiap item (AB-01) dan rekap anggaran per komponen.

**V1 Rencana pengembangan**, setelah langkah 2
- V1.1 KaLab mengirim temuan gap: aspek (tridharma, kompetensi, sarana, layanan), kondisi saat ini, kebutuhan atau standar, sumber data, uraian gap, dan lampiran.
- V1.2 Sistem menampilkan temuan per aspek dan aspek yang belum punya temuan.
- V1.3 Kembali ke langkah 3. Pada langkah 5, item juga memuat temuan gap yang dijawab, nilai risiko, dan nilai manfaat. Pada langkah 6, sistem juga menampilkan prioritas tiap item.

**V2 Revisi dari rencana yang disahkan**, menggantikan langkah 1
- V2.1 KaLab memilih rencana Disahkan yang akan direvisi.
- V2.2 Sistem menampilkan salinan isi rencana sebagai draf revisi, tertaut ke rencana asal.
- V2.3 Kembali ke langkah 3.

**V3 Melanjutkan draf**, menggantikan langkah 1
- V3.1 KaLab memilih rencana berstatus Draf.
- V3.2 Kembali ke langkah 4.

**E1 Periode di luar periode rencana induk**, di langkah 1
- E1.1 Sistem menampilkan periode rencana induk.
- E1.2 Kembali ke langkah 1.

**E2 PIC bukan personel aktif**, di langkah 5
- E2.1 Sistem menampilkan item dengan PIC tidak aktif.
- E2.2 Kembali ke langkah 5.

**Pascakondisi:** rencana berstatus Draf, siap diajukan (UC-21).

### 3.4 UC-18 Isi Realisasi Rencana

**Aktor:** Laboran, KaLab (sebagai PIC item) · **Prakondisi:** rencana Disahkan dan masih berlaku (AB-10).

**Alur utama**
1. PIC meminta daftar item rencana yang menjadi tanggung jawabnya untuk periode lapor berjalan.
2. Sistem menampilkan item: kegiatan, KPI, target, satuan, jadwal, dan realisasi sebelumnya.
3. PIC memilih satu item.
4. Sistem menampilkan rincian item dan riwayat realisasinya.
5. PIC mengirim periode lapor, capaian, anggaran terpakai, status capaian, analisis dan tindak lanjut, PIC tindak lanjut, tenggat, serta berkas bukti.
6. Sistem menampilkan realisasi beserta persentase capaian terhadap target.

**E1 Status "tidak relevan" tanpa alasan** (AB-10)
- E1.1 Sistem menampilkan bahwa alasan wajib diisi.
- E1.2 Kembali ke langkah 5.

**E2 Tanpa bukti** (AB-12)
- E2.1 Sistem menampilkan bahwa minimal satu bukti wajib dilampirkan.
- E2.2 Kembali ke langkah 5.

**E3 Bukan PIC item dan bukan KaLab** (AB-11), di langkah 3
- E3.1 Sistem menampilkan PIC item tersebut.
- E3.2 Use case **gagal**.

**Pascakondisi:** realisasi tercatat dengan bukti; status kriteria K3 diperbarui.

### 3.5 UC-21 Ajukan Dokumen

**Aktor:** *Penyusun Dokumen* (KaLab untuk rencana dan SK, Laboran untuk SOP/IK) · **Prakondisi:** dokumen berstatus Draf.

**Alur utama**
1. Penyusun memilih dokumen Draf.
2. Sistem menampilkan jenis, judul, periode atau nomor revisi, dan daftar kelengkapan (terpenuhi atau belum).
3. Penyusun mengajukan dokumen.
4. Sistem menampilkan status Diajukan, tanggal pengajuan, dan jabatan pemeriksa atau pengesah yang akan menerima pemberitahuan.

**E1 Kelengkapan belum terpenuhi** (AB-01), di langkah 3
- E1.1 Sistem menampilkan bagian yang belum lengkap.
- E1.2 Use case **gagal**. Dokumen tetap Draf.

**E2 Tidak ada pemegang jabatan berwenang** (AB-02), di langkah 3
- E2.1 Sistem menampilkan bahwa belum ada jabatan aktif yang berwenang memeriksa atau mengesahkan jenis dokumen ini.
- E2.2 Use case **gagal**.

**Pascakondisi:** dokumen Diajukan, tanggal pengajuan tercatat, pemeriksa atau pengesah diberi tahu.

### 3.6 UC-24 Kembalikan Dokumen

**Aktor:** Pemeriksa, *Pengesah Dokumen* · **Prakondisi:** dokumen berstatus Diajukan atau Diperiksa.

**Alur utama**
1. Aktor memilih dokumen yang menunggu pemeriksaan atau pengesahannya.
2. Sistem menampilkan rincian dokumen, riwayat pengajuan, catatan pemeriksaan, dan berkas bertanda tangan (bila ada).
3. Aktor mengirim keputusan pengembalian beserta alasannya.
4. Sistem menampilkan status Draf, alasan, tanggal pengembalian, dan penyusun yang diberi tahu.

**V1 Penolakan terjadi di atas kertas** (pengesah tidak memakai sistem, A1)
- V1.1 Penyusun memilih dokumen yang ditolak.
- V1.2 Sistem menampilkan rincian dokumen.
- V1.3 Penyusun mengirim alasan penolakan dan nama serta jabatan pengesah yang menolak.
- V1.4 Kembali ke langkah 4.

**E1 Alasan kosong** (AB-05)
- E1.1 Sistem menampilkan bahwa alasan wajib diisi.
- E1.2 Kembali ke langkah 3.

**E2 Aktor tidak berwenang** (AB-02), di langkah 1
- E2.1 Use case **gagal**.

**Pascakondisi:** dokumen Draf, alasan tercatat, penyusun diberi tahu.

### 3.7 UC-26 Unggah Dokumen Bertanda Tangan

**Aktor:** *Penyusun Dokumen* · **Prakondisi:** dokumen Diajukan (pemeriksaan tidak aktif) atau Diperiksa. Untuk rencana dan SK, dokumen resmi sudah diterbitkan (UC-25).

**Alur utama**
1. Penyusun memilih dokumen yang menunggu pengesahan.
2. Sistem menampilkan rincian dokumen serta nama dan jabatan pengesah yang berwenang.
3. Penyusun mengirim berkas bertanda tangan, tanggal tanda tangan, dan nama penanda tangan.
4. Sistem menampilkan berkas yang diterima dan status "siap disahkan".

**V1 Mengganti berkas yang sudah diunggah**
- V1.1 Sistem menampilkan berkas sebelumnya di langkah 2.
- V1.2 Kembali ke langkah 3. Berkas sebelumnya tetap tercatat di riwayat.

**E1 Berkas tidak terbaca**
- E1.1 Sistem menampilkan bahwa berkas tidak dapat dibaca.
- E1.2 Kembali ke langkah 3.

**E2 Penanda tangan bukan pemegang jabatan berwenang** (AB-02), di langkah 3
- E2.1 Sistem menampilkan pemegang jabatan yang berwenang.
- E2.2 Kembali ke langkah 3.

**Pascakondisi:** berkas bertanda tangan tersimpan, pengesah diberi tahu.

### 3.8 UC-27 Sahkan Dokumen

**Aktor:** *Pengesah Dokumen* (KaLab untuk POB lab, Dekan untuk SK dan rencana) · **Pemangku kepentingan:** Penyusun, Pengguna Lab, Penilai Monev · **Prakondisi:** aktor memegang jabatan aktif yang berwenang mengesahkan jenis dokumen itu (AB-02); dokumen Diajukan atau Diperiksa.

**Alur utama**
1. Pengesah meminta daftar dokumen yang menunggu pengesahannya.
2. Sistem menampilkan dokumen sesuai wewenang jabatannya: jenis, judul, penyusun, tanggal pengajuan, dan ada tidaknya berkas bertanda tangan.
3. Pengesah memilih satu dokumen.
4. Sistem menampilkan rincian dokumen, catatan pemeriksaan (bila ada), dan berkas bertanda tangan.
5. Pengesah mengesahkan dokumen. [V1]
6. Sistem menampilkan status Disahkan, tanggal sah, nama dan jabatan pengesah, dokumen atau versi sebelumnya yang kini Diganti (bila ada, AB-04/AB-14), dan untuk SOP/IK juga tanggal tinjau ulang berikutnya (AB-08).

**V1 Pengesah tidak menyetujui**, di langkah 5
- V1.1 Use case berakhir tanpa perubahan. Pengembalian dilakukan lewat UC-24.

**V2 KaLab mengesahkan atas nama Dekan** **[KONFIRMASI]**, di langkah 1
- V2.1 KaLab memilih dokumen yang pengesahnya Dekan.
- V2.2 Kembali ke langkah 4. Pada langkah 6, sistem menampilkan Dekan sebagai pengesah dan KaLab sebagai pencatat.

**E1 Berkas bertanda tangan belum ada** (AB-03), di langkah 5
- E1.1 Sistem menampilkan bahwa berkas harus diunggah lebih dulu (UC-26).
- E1.2 Use case **gagal**.

**E2 Pemeriksaan wajib belum dilakukan** (AB-09), di langkah 5
- E2.1 Sistem menampilkan bahwa dokumen harus diperiksa lebih dulu.
- E2.2 Use case **gagal**.

**Pascakondisi:** dokumen Disahkan; dokumen atau versi sebelumnya Diganti (bila ada); untuk SOP/IK, jadwal tinjau ulang dibuat; jejak pengesahan tercatat.

## 4. Pola use case berstereotype (§6.7)

### 4.1 Pola «CRUDL»

Berlaku untuk UC-01 Kelola Personel, UC-02 Kelola Jabatan, UC-07 Kelola Dokumen Induk, UC-14 Kelola KPI, dan UC-15 Kelola Sasaran Renstra.

**Alur dasar**
- **Daftar (L):** aktor meminta daftar data; sistem menampilkan daftar dengan atribut ringkas. Ini titik awal semua alur lain.
- **Buat (C):** aktor mengirim atribut data; sistem menampilkan data baru.
- **Lihat (R):** aktor memilih satu data; sistem menampilkan semua atributnya.
- **Ubah (U):** aktor memilih data dan mengirim atribut yang diubah; sistem menampilkan data hasil ubah.
- **Hapus/Arsipkan (D):** aktor memilih data dan menghapus atau mengarsipkannya; sistem menampilkan data tidak lagi aktif.

**Varian**
- **V1:** aktor membatalkan pembuatan atau perubahan. Data tidak berubah.

**Eksepsi**
- **E1:** atribut wajib kosong atau tidak valid. Sistem menampilkan atribut bermasalah; kembali ke langkah kirim.
- **E2:** aktor tidak berwenang. Use case gagal.
- **E3:** data masih dirujuk data lain. Sistem menawarkan arsip, bukan hapus.

**Catatan per konsep**

| UC | Atribut utama | Hapus | Aturan khusus |
|---|---|---|---|
| UC-01 Personel | nama, jenis, pengguna sistem, unit | Arsip | **[KONFIRMASI]** model Personel bersama kelompok |
| UC-02 Jabatan | nama, kode, unit, eksternal, atasan, koordinasi, pengganti, syarat kompetensi, dasar dokumen; daftar tugas; daftar wewenang (tindakan × jenis dokumen) | Arsip | Atasan dan pengganti tidak boleh jabatan itu sendiri |
| UC-07 Dokumen Induk | kode, judul, jenis, kategori, asal, wajib, dasar kebutuhan, lokasi penggunaan, dokumen terkait, rekaman yang dihasilkan | Arsip | Kode unik |
| UC-14 KPI | kode, nama, sasaran kerja, rumus (pembilang, penyebut), satuan, frekuensi, jabatan PIC, sumber bukti, acuan ISO | Arsip | Kode unik |
| UC-15 Sasaran Renstra | kode, uraian, tingkat | Hapus bila belum dirujuk | — |

### 4.2 Pola «report»

Berlaku untuk UC-06, UC-13, UC-20, dan UC-29.

**Alur dasar**
1. Aktor mengirim kriteria laporan (periode, unit, jenis dokumen, atau indikator).
2. Sistem menampilkan isi laporan beserta tautan ke rekaman bukti.

**Eksepsi**
- **E1:** tidak ada data untuk kriteria itu. Sistem menampilkan bahwa data belum tersedia (tidak dianggap tercapai, sesuai IKU bagian 7).

| UC | Isi laporan |
|---|---|
| UC-06 | Bagan organisasi, matriks kewenangan, riwayat SK, rapat, dan evaluasi |
| UC-13 | Daftar induk dokumen, riwayat revisi, distribusi, sosialisasi, tinjau ulang |
| UC-20 | Laporan capaian per periode, matriks keterkaitan Renstra, rekap manfaat |
| UC-29 | Persentase SOP wajib yang memenuhi S1–S5 beserta daftar yang tidak memenuhi; kriteria tertinggi K1–K4 untuk PKG-01, 03, 13 beserta tautan bukti |

## 5. Isu terbuka (§6.6.4)

| Isu | Use case | Status |
|---|---|---|
| Dekan login sendiri atau diwakili KaLab (V2 UC-27) | UC-24, 26, 27 | **[KONFIRMASI]** Pak Widi / KaLab |
| Rekaman bukti tidak boleh dihapus (AB-07) | UC-04, 05, 09, 10, 11, 18, 19 | **[KONFIRMASI]** |
| Hanya satu versi diproses per dokumen (AB-13) | UC-08 | **[USULAN PENULIS]** |
| Satu dokumen berlaku per jenis dan periode (AB-14) | UC-27 | **[ASUMSI]** |
| Apakah bukti wajib untuk setiap realisasi (AB-12) | UC-18 | **[KONFIRMASI]**, mengikuti bunyi K3 |
| Apakah *Menunggu Revisi* masih dihitung mutakhir | UC-11 | **[KONFIRMASI]** (S2) |

## 6. Langkah berikutnya

Step 8 adalah **system sequence diagram** (Wazlawick Bab 7) untuk delapan use case di bagian 3. Setiap langkah aktor menjadi pesan dari aktor ke sistem, dan setiap langkah sistem menjadi pesan balasan. Alur alternatif digambar sebagai fragmen `opt` atau `alt`.
