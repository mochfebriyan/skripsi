#!/usr/bin/env bash
# Backup basis data + filestore (lampiran). Keduanya wajib: file lampiran tidak ada di basis data.
#   ./scripts/backup.sh [nama_db]   → backups/<db>-<waktu>.sql.gz dan .filestore.tgz
set -euo pipefail
cd "$(dirname "$0")/.."
DB="${1:-labfik}"
TS="$(date +%Y%m%d-%H%M%S)"
mkdir -p backups
docker compose exec -T db pg_dump -U odoo --no-owner "$DB" | gzip > "backups/$DB-$TS.sql.gz"
docker compose run --rm -T --entrypoint bash odoo -c "tar -C /var/lib/odoo/filestore -czf - $DB" > "backups/$DB-$TS.filestore.tgz"
echo "Backup tersimpan: backups/$DB-$TS.sql.gz dan backups/$DB-$TS.filestore.tgz"
