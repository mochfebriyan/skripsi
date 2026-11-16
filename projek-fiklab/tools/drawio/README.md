# Alat diagram draw.io

Semua diagram rancangan TO-BE dibuat sebagai file `.drawio`. Diagram modul Tata Kelola dibuat lewat skrip Python di [contoh-tata-kelola/](contoh-tata-kelola/), bukan digambar tangan. Hasilnya: prefiks ID, gaya, notasi, dan tata letak konsisten, serta diagram bisa dibuat ulang setelah isinya berubah.

## Isi folder

| File | Fungsi |
|---|---|
| `validate.py` | Memeriksa struktur `.drawio`: garis putus, ID ganda, ID tanpa prefiks modul, kotak bertumpuk. Jalankan setiap selesai membuat atau mengubah diagram |
| `contoh-tata-kelola/activity_state.py` | Activity diagram dengan swimlane + state machine (A1–A4, S1–S2) |
| `contoh-tata-kelola/use_case.py` | Use case diagram multi-halaman dengan package dan aktor abstrak |
| `contoh-tata-kelola/ssd.py` | System sequence diagram (lifeline aktor/antarmuka/kontroler, fragmen `opt`, `ref`) |
| `contoh-tata-kelola/conceptual_model.py` | Conceptual model (konsep, atribut, asosiasi berperan, komposisi, generalisasi, enumerasi) |
| `contoh-tata-kelola/design_class.py` | Design class diagram Odoo (mixin, method, asosiasi berarah, kolom bertumpuk otomatis) |

## Cara pakai untuk modul lain

1. Salin skrip contoh yang sesuai ke folder kerja sementara (bukan ke `contoh-tata-kelola/`).
2. Ganti **data**-nya (daftar node, kelas, pesan, aktor) dengan isi modulmu. Fungsi gambar (`cls`, `n`, `e`, `msg`, `pkg`, …) tidak perlu diubah.
3. Ganti **prefiks ID** (`tk-…`) dengan prefiks modulmu. Gaya (polos hitam-putih, Times New Roman, catatan di halaman terakhir) **jangan diubah**; aturannya di `CLAUDE.md` bagian 5.
4. Jalankan dengan argumen file keluaran:
   ```
   python3 -I skrip.py projek-fiklab/rancangan/<jenis>-<slug-modul>.drawio
   python3 -I projek-fiklab/tools/drawio/validate.py projek-fiklab/rancangan/<jenis>-<slug-modul>.drawio <prefiks>-
   ```
5. Buka di draw.io untuk cek tampilan. Rapikan posisi atau garis dengan tangan bila perlu.

Catatan:
- Skrip di `contoh-tata-kelola/` adalah **arsip** yang menghasilkan diagram Tata Kelola. Jangan dijalankan ke file Tata Kelola bila diagram itu sudah dirapikan manual, karena hasil rapian akan tertimpa.
- Label memakai HTML (`html=1`). Tulis `&` biasa di data; skrip yang meng-escape.
- Tidak ada dependensi selain Python standar.
