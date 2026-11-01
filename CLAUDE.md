# Repo skripsi Febriyan: LabFIK Compliance

Repo ini milik Febriyan, mahasiswa FIK UPN "Veteran" Jakarta. Isinya bahan dan kode skripsi yang menjadi bagian dari proyek kelompok **LabFIK Compliance**: sistem Odoo untuk Laboratorium FIK yang menghasilkan bukti bagi Instrumen Monev Laboratorium UPNVJ 2026. Pembimbingnya Pak Widi. Bahasa kerja: Indonesia.

## Scope final (1 November 2026)

Febriyan memegang modul **Tata Kelola & Dokumen**:
- PKG-01 Pengelolaan 1 (rencana kerja tahunan)
- PKG-02 Pengelolaan 2 (SOP dan IK)
- PKG-03 Pengelolaan 3 (struktur organisasi)
- PKG-13 Pengembangan 13 (rencana pengembangan lab)

Modul ini juga mengelola master bersama **Personel, Jabatan, Dokumen Induk, dan KPI**.

**Sudah tidak berlaku:** scope lama "Role 3" (Proses 18, Evaluasi 19, *dashboard* 8 indikator) dan pembagian Role 1–3 versi 26 Oktober 2026. Jangan memakainya kecuali diminta. Riwayatnya ada di git sebelum 1 November 2026.

## Baca dulu

1. [projek-fiklab/brief/brief-seluruh-projek.md](projek-fiklab/brief/brief-seluruh-projek.md): proyek secara keseluruhan (modul, pemegang, Core, keputusan, pertanyaan terbuka).
2. [projek-fiklab/brief/brief-tata-kelola-dokumen.md](projek-fiklab/brief/brief-tata-kelola-dokumen.md): scope skripsi Febriyan.

## Peta folder

| Path | Isi |
|---|---|
| `projek-fiklab/brief/` | Dua brief di atas |
| `projek-fiklab/analisis/` | Pedoman pengisian sheet dan pemetaan package (keduanya **bersama kelompok**), serta analisis Pengelolaan 1–3 dan Pengembangan 13 (milik Febriyan) |
| `projek-fiklab/docs/` | Rujukan: Instrumen Monev xlsx (tab *Analysis*), SNI ISO/IEC 17025:2017, Pedoman TA FIK 2025, daftar dosen FIK |
| `projek-fiklab/pendahuluan/reference/` | Rujukan Bab 1: Bab 1 skripsi Rafika, daftar judul skripsi terkait. Draf pendahuluan lama sudah dihapus |
| `skripsi_rafika/` | Kode skripsi Rafika Anandar (2026), modul `PendaftaranAsisten` di atas OpenEduCat. **Hanya acuan; jangan diubah** |

## Urutan sumber kebenaran

Instrumen Monev (xlsx) dan ISO/IEC 17025 → brief → analisis → rancangan → kode. Saat ini belum ada rancangan teknis maupun kode untuk modul ini; MVP dan PRD lama sengaja dihapus agar rancangan tidak bias ke contoh itu. Jangan menghidupkannya kembali dari riwayat git kecuali diminta.

Bila ada yang bertentangan, ikuti sumber yang lebih kiri, lalu sebutkan konfliknya ke Febriyan.

## Konvensi

- **Proyek mencakup 21 indikator; 1 package = 1 indikator.** Nomor PKG (PKG-01–21) adalah identitas resmi indikator, karena penomoran di sheet tidak rapi (nomor ganda, baris tanpa aspek, kode Q/E). Tulis PKG + aspek + nomor + kata kunci, misalnya `PKG-10 Pengelolaan 10 (otorisasi)`. Baris sheet di luar 21 indikator tidak dicakup.
- **Pemegang modul:** Febriyan = Tata Kelola & Dokumen, Zahir = SDM & Kompetensi, Herrens = Pelaksanaan Praktikum (termasuk PKG-20 kepuasan pengguna). Asset Management dan Safety Management dipegang kelompok lain (Wisnu, Patih).
- Gunakan **nama master baku** dan label entitas `[T]`/`[M]`/`[R]` dari pedoman pengisian sheet (bagian 4).
- Sebutkan **level cakupan** (otomatis / semi-otomatis / bukti tertaut). Jangan mengklaim skor "dihitung otomatis" untuk indikator kriteria berurutan.
- Tandai hal yang belum pasti dengan **[KONFIRMASI]**, **[VALIDASI]**, **[ASUMSI]**, atau **[USULAN PENULIS]**. Klaim kondisi LabFIK saat ini harus berasal dari wawancara atau data, bukan dugaan.
- Jangan menjanjikan kenaikan skor monev. Sistem adalah alat pencatatan, pembuktian, dan pemantauan.
- Dokumen proposal mengikuti Pedoman TA FIK 2025 jenis **Prototipe/Proyek**: Bab I dengan 1.2 *Identifikasi Masalah*, dan Bab II *Rancangan Proyek*.

## Larangan

- **Data pribadi tidak boleh masuk repo:** nama asisten/mahasiswa, NIM, nomor HP, rekening/KTP, nilai. Data demo dan seed harus fiktif.
- **Paket Dokumen Monev di Drive LabFIK** (M01–M21) adalah draf hasil generate GPT. Paket ini **bukan** sumber kebutuhan dan bukan bukti kondisi nyata.
- File bersama (`brief-seluruh-projek.md`, `pedoman-pengisian-sheet-analisis.md`, `pemetaan-package-instrumen.*`, `docs/`) juga dipakai kelompok. Perubahan di sana sebaiknya disampaikan ke Zahir dan Herrens.
