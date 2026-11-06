# Cara pakai OOAD (Wazlawick 2024) Knowledge Pack

1. Buka Project di Claude: project baru, atau project BABOK yang sudah ada kalau mau dua buku sekaligus.
2. Copy isi `PROJECT_INSTRUCTIONS.md` ke kolom **Instructions** project. Kalau digabung dengan BABOK, tempel kedua instruksi berurutan (BABOK dulu, lalu yang ini).
3. Upload **semua file di folder `OOAD_Wazlawick_2024_Knowledge/`** (19 file .md) ke **Project knowledge**. Jangan ikut upload PDF atau markdown mentahnya, karena isinya jadi dobel.
4. Ukurannya sekitar 215 ribu token (ditambah BABOK sekitar 290 ribu), jadi Claude otomatis memakai mode pencarian (RAG). Karena itu file dipecah per bab dan tiap sub-bagian membawa nama section induknya.
5. Tips bertanya: sebut tahap atau artefaknya, misalnya "buatkan BPMN as-is pendaftaran PKKMB sesuai bab 3", "turunkan use case dari BPMN ini (§4.5)", "cek expanded use case saya dengan aturan bab 6".

Isi tiap file dan tabel "tugas → bab" ada di `00_INDEX_README.md`.
