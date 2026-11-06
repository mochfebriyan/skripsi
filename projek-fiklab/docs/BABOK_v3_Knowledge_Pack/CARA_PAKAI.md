# Cara pakai BABOK v3 Knowledge Pack

1. Buat Project baru di Claude (claude.ai → Projects → New project), misalnya "BABOK v3".
2. Buka `PROJECT_INSTRUCTIONS.md`, copy semua isinya, paste ke kolom **Instructions** project.
3. Upload **semua file di folder `BABOK_v3_Knowledge/`** (23 file .md) ke **Project knowledge**. Jangan upload PDF atau markdown mentah juga: isinya dobel dan bikin pencarian Claude lebih berisik.
4. Total sekitar 290 ribu token, jadi Claude akan otomatis memakai mode pencarian (RAG). Karena itu file dipecah per bab dengan nama yang jelas, dan setiap sub-bagian membawa nama task/teknik induknya.
5. Tips bertanya: sebut nomor atau nama task/teknik ("jelaskan 5.3 Prioritize Requirements", "teknik apa saja untuk 4.2?"). Pertanyaan yang spesifik membuat pencarian lebih tepat.

Isi tiap file ada di `00_INDEX_README.md`.
