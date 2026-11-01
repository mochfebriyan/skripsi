# Analisis Data Indikator Pengembangan 13 (MVP)

1 November 2026 · Febriyan · Bagian dari proyek LabFIK Compliance · Modul: Tata Kelola & Dokumen (PKG-13)

Alur analisis mengikuti [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md) dan [analisis Pengelolaan 1–3](analisis-data-pengelolaan-1-3.md): **target → aturan memenuhi → luaran (bukti dukung) → data transaksi (*fact*) → master data (*dimension*) → dependensi**.

Cakupannya sengaja dibatasi ke MVP. Data yang bergantung pada pihak lain diberi jalan pengganti. Isi sheet untuk baris ini awalnya ditulis Herrens (PIC analisis awal), lalu package-nya pindah ke modul Tata Kelola & Dokumen per 1 November 2026.

Kondisi saat ini **belum diketahui**: apakah LabFIK pernah menyusun analisis kebutuhan, renstra, atau roadmap pengembangan, dan siapa yang mengesahkannya. Semua klaim kondisi saat ini ditandai **[KONFIRMASI]**.

---

## Ringkasan

| | Pengembangan 13 |
|---|---|
| Inti | Rencana pengembangan lab disusun dari analisis kesenjangan (gap) empat aspek, lalu dijalankan dan diukur manfaatnya |
| PJ | KaLab; Dekanat |
| Jenis skor | Kriteria berurutan 1–4 |
| Unit | 1 paket dokumen dan rekaman |
| Level cakupan (usulan) | Semi-otomatis |
| Pola | **Sama dengan Pengelolaan 1**: rencana → realisasi → tinjauan |
| Posisi dalam dependensi | Hilir di dalam modul (memakai Personel/Jabatan dari Pengelolaan 3). Data gap-nya bisa ditarik dari modul lain, tetapi opsional |
| Acuan | Pedoman Diklatfung PLP 2022 (pengembangan), Standar SPMI UPNVJ 2025, Dokumen ISO UPNVJ |

**Temuan utama:**
1. **Pengembangan 13 bisa dibangun di atas model rencana Pengelolaan 1.** Kedua indikator sama-sama berisi rencana disahkan → item lengkap → realisasi → tinjauan. Bedanya ada di tiga hal:
   - **Analisis gap** per aspek sebagai dasar item.
   - **Prioritas berbasis risiko/manfaat.**
   - K4 meminta **pengukuran manfaat**, bukan sekadar tinjauan capaian.
2. **Dimensi analisis gap adalah titik temu modul.** Aspek kompetensi berasal dari SDM, sarana dari Aset, dan layanan dari hasil monev/kepuasan. Untuk MVP, semua aspek diisi manual. Tautan otomatis menyusul.
3. **Roadmap muncul di dua indikator.** Bukti 1 Pengelolaan 1 adalah "roadmap lab", dan Bukti 3 Pengembangan 13 adalah "roadmap". Perlu diputuskan apakah keduanya satu dokumen **[VALIDASI ke Pak Widi]**.

---

## 1. Target

| | Isi (Instrumen Monev v1.1) |
|---|---|
| Target | Rencana pengembangan laboratorium didasarkan pada analisis kesenjangan kebutuhan tridharma, kompetensi, sarana, dan layanan |
| Penerapan / PJ | Umum / KaLab; Dekanat |
| Unit | 1 paket dokumen dan rekaman |
| Skor | 4: kriteria 1–4 terpenuhi berurutan · 3: kriteria 1–3 · 2: hanya kriteria 1 atau 1–2 · 1: kriteria 1 belum terpenuhi atau bukti tidak dapat diverifikasi |

Bukti dukung:
1. analisis gap;
2. kebutuhan kurikulum/CPMK, riset, dan PkM;
3. *roadmap*;
4. prioritas, biaya, target, PIC, dan jadwal;
5. realisasi.

Kriteria di instrumen:
1. Analisis kebutuhan dan rencana pengembangan disahkan.
2. Gap, prioritas berbasis risiko/manfaat, biaya, target, dan PIC lengkap.
3. Program pengembangan berjalan sesuai tahapan dan realisasinya dapat ditelusuri.
4. Manfaat pengembangan bagi pembelajaran/layanan diukur dan rencana diperbarui.

## 2. Aturan "memenuhi" versi MVP

Kriteria diperiksa **berurutan**. Kriteria berikutnya tidak dihitung bila kriteria sebelumnya belum berbukti.

| Kriteria | Arti | Cek oleh sistem | Cek oleh penilai |
|---|---|---|---|
| K1 Disahkan | Analisis kebutuhan dan rencana pengembangan disahkan dan masih berlaku | Ada rencana jenis *pengembangan* berstatus *disahkan*, dengan PDF bertanda tangan, pengesah, dan tanggal. Periodenya mencakup tanggal penilaian. Analisis gap ada di dalam rencana itu | Keabsahan dokumen |
| K2 Lengkap | Gap, prioritas, biaya, target, PIC lengkap | (a) Analisis gap memuat **keempat aspek**: setiap aspek punya minimal satu temuan, atau dinyatakan "tidak ada gap" dengan alasan **[USULAN PENULIS]**. (b) Setiap item program menunjuk minimal satu temuan gap dan punya prioritas (dengan nilai risiko dan manfaat), biaya, target, PIC, dan jadwal | Apakah gap dan prioritas masuk akal |
| K3 Berjalan | Program berjalan sesuai tahapan dan realisasinya tertelusur | Setiap item yang jadwal mulainya sudah lewat punya minimal satu realisasi berbukti (ambang sama dengan Pengelolaan 1 K3) | Kewajaran realisasi |
| K4 Manfaat diukur | Manfaat bagi pembelajaran/layanan diukur, dan rencana diperbarui | Ada tinjauan pada periode itu. Setiap item yang selesai punya **ukuran manfaat** (nilai sebelum dan sesudah). Minimal satu keputusan tertaut ke rencana berikutnya atau ke revisi rencana | Kualitas pengukuran manfaat |

Seperti Pengelolaan 1 dan 3, sistem menampilkan **kriteria tertinggi yang lengkap secara data**. Skor akhir ditetapkan penilai.

## 3. Luaran

| Luaran | Bukti ke- | Keterangan |
|---|---|---|
| Analisis gap | 1, 2 | Tabel temuan per aspek. Aspek tridharma memuat kebutuhan kurikulum/CPMK, riset, dan PkM. Dokumen pendukung dilampirkan |
| Rencana pengembangan (*roadmap*) disahkan | 3 | Header rencana + PDF bertanda tangan di register dokumen (PKG-02). Opsional ditautkan ke rencana strategis Pengelolaan 1 |
| Daftar program | 4 | Item rencana: prioritas, biaya, target, PIC, jadwal, tautan ke temuan gap |
| Laporan realisasi | 5 | Dihasilkan dari data realisasi per item |
| Rekap manfaat | — (bukti K4) | Dihasilkan dari ukuran manfaat pada tinjauan |
| Dokumen Rencana Pengembangan [R] | 1–4 | Cetak format baku, mirip cetak rencana kerja Pengelolaan 1 |
| Status kriteria K1–K4 | — | Dihitung dari data di atas |

## 4. Data transaksi (*fact*)

| Fact | Grain | Isi | Catatan |
|---|---|---|---|
| **Rencana Pengembangan** | 1 dokumen rencana | Periode (bisa multi-tahun), status (draf/diajukan/disahkan/diganti/selesai), pengesah, tanggal sah, PDF, tautan opsional ke rencana strategis. Dua tabel anak: **temuan gap** (aspek, kondisi saat ini, kebutuhan/standar, sumber data, uraian gap, lampiran) dan **item program** (temuan gap yang dijawab, uraian, nilai risiko, nilai manfaat, prioritas, biaya, target, PIC, jadwal) | Bisa memakai model rencana Pengelolaan 1 dengan `jenis = pengembangan`. Temuan gap adalah tabel anak baru |
| **Realisasi Rencana Pengembangan** | 1 laporan per item per periode lapor | Tahapan/capaian, biaya terpakai, bukti, pelapor, tanggal | Sama dengan realisasi Pengelolaan 1 |
| **Tinjauan Rencana Pengembangan** | 1 tinjauan per periode | Tanggal, peserta, ringkasan, keputusan yang tertaut ke rencana berikutnya. Anak: **ukuran manfaat** per item (indikator manfaat, nilai sebelum, nilai sesudah, sumber) | Sama dengan tinjauan Pengelolaan 1, ditambah ukuran manfaat |

Riwayat perubahan memakai `mail.thread` + `tracking`.

**Penyesuaian terhadap sheet:** di sheet, "Dokumen Rencana Pengembangan" ditulis sebagai report. Itu sesuai, karena dokumennya hasil cetak. "Master aspek pengembangan" hanya berisi empat nilai tetap (tridharma, kompetensi, sarana, layanan), jadi cukup **pilihan tetap**, bukan master.

## 5. Master data (*dimension*)

| Master | Dipakai untuk | Sumber | Bila belum tersedia |
|---|---|---|---|
| Periode | Masa berlaku rencana (tahunan atau multi-tahun) | Master Periode (Core) | Rentang tanggal diinput di rencana |
| Personel | PIC item, pengesah, pelapor, peserta tinjauan | Master bersama dari Pengelolaan 3 | `res.users` |
| Jabatan | Pengesah sah (KaLab/Dekan) | Master bersama dari Pengelolaan 3 | Pengguna di grup KaLab |
| KPI | Indikator manfaat (opsional) | Master KPI dari Pengelolaan 1 | Indikator manfaat ditulis sebagai teks |
| Sasaran Renstra | Keselarasan program dengan Renstra (opsional) | Master Sasaran Renstra dari Pengelolaan 1 | Tidak dipakai |

Yang cukup berupa **pilihan tetap**: aspek gap, skala risiko dan manfaat (misalnya 1–3), dan tingkat prioritas (tinggi/sedang/rendah, dihitung dari risiko × manfaat **[USULAN PENULIS]**).

Tidak ada master baru.

## 6. Dependensi dan jalan pengganti

| Butuh | Dari | Sifat | Bila tidak ada |
|---|---|---|---|
| Personel dan jabatan | Pengelolaan 3 (modul sendiri) | Wajib | `res.users` + grup keamanan |
| Register dokumen untuk PDF bertanda tangan | Pengelolaan 2 (modul sendiri) | Wajib untuk K1 | — (dibangun di modul yang sama) |
| Kebutuhan kurikulum/CPMK, riset, PkM | Eksternal (prodi, LPPM) | Wajib sebagai isi aspek tridharma | Diringkas manual + lampiran dokumen sumber |
| Data biaya | Eksternal (keuangan fakultas) | Wajib untuk K2 | Biaya diinput manual per item |
| Gap kompetensi | SDM (matriks kompetensi PKG-04, rencana pelatihan PKG-14) | Opsional | Diisi manual |
| Gap sarana | Aset (inventaris PKG-07, pemeliharaan PKG-12/21) | Opsional | Diisi manual |
| Gap layanan | Status indikator monev, kepuasan pengguna (PKG-20) | Opsional | Diisi manual |
| Rencana strategis / *roadmap* lab | Pengelolaan 1 (modul sendiri) | Opsional | Rencana pengembangan berdiri sendiri |

**Dipakai oleh:** opsional Pengembangan 14 (SDM). Gap aspek kompetensi bisa menjadi kebutuhan pelatihan laboran. Perlu disepakati dengan Zahir (pemegang SDM & Kompetensi).

## 7. Ditunda

- Matriks risiko formal (kemungkinan × dampak). Untuk MVP cukup skala risiko dan manfaat sederhana.
- Penarikan data gap otomatis dari modul SDM, Aset, dan status monev.
- Tren manfaat multi-tahun.
- Penganggaran rinci (mata anggaran, pencairan).

---

## Kompleksitas

Dihitung dengan cara di [pedoman pengisian sheet](pedoman-pengisian-sheet-analisis.md#6-cara-menghitung-kompleksitas). Angkanya **kasar**, hanya untuk perbandingan.

| Skenario | T | M | D | E | A | Data saat ini | Total |
|---|---|---|---|---|---|---|---|
| Dibangun terpisah | 3 | 0 | 1 (Pengelolaan 3) | 2 (kurikulum/riset/PkM, biaya) | 2 (pengesahan, tinjauan) | Belum diketahui (+2) | **10** |
| Di atas model rencana Pengelolaan 1 | 0 (hanya tabel anak temuan gap dan ukuran manfaat) | 0 | 1 | 2 | 2 | +2 | **7** |

## Pertanyaan minimum sebelum lanjut

**Untuk KaLab**
- [ ] Apakah LabFIK pernah menyusun analisis kebutuhan, renstra lab, atau *roadmap* pengembangan? Siapa yang menyusun dan mengesahkannya (KaLab, Dekan)?
- [ ] Rencana pengembangan disusun per tahun atau multi-tahun? Mengikuti tahun anggaran atau tahun akademik?
- [ ] Dari mana data kebutuhan kurikulum/CPMK, riset, dan PkM bisa didapat?
- [ ] Bagaimana manfaat pengembangan biasanya diukur, misalnya utilisasi ruang, kepuasan pengguna, atau capaian CPMK?

**Untuk Pak Widi**
- [ ] Apakah *roadmap* Pengelolaan 1 dan Pengembangan 13 boleh satu dokumen?
- [ ] Apakah aturan "keempat aspek wajib punya temuan atau alasan tidak ada gap" sesuai maksud instrumen?

**Untuk kelompok**
- [ ] Apakah gap kompetensi Pengembangan 13 dipakai sebagai masukan Pengembangan 14 (SDM)?
