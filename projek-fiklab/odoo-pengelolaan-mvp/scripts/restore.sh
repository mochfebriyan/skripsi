#!/usr/bin/env bash
# Memulihkan backup ke basis data baru.
#   ./scripts/restore.sh backups/labfik-20261026-120000 labfik_pulih
set -euo pipefail
cd "$(dirname "$0")/.."
PREFIX="$1"
DB="$2"
[[ -f "$PREFIX.sql.gz" && -f "$PREFIX.filestore.tgz" ]] || { echo "File backup tidak lengkap: $PREFIX"; exit 1; }
SRC_DB="$(basename "$PREFIX" | sed -E 's/-[0-9]{8}-[0-9]{6}$//')"

docker compose up -d --wait db
docker compose exec -T db createdb -U odoo "$DB"
gunzip -c "$PREFIX.sql.gz" | docker compose exec -T db psql -q -U odoo -d "$DB" > /dev/null
docker compose run --rm -T --entrypoint bash odoo -c \
  "mkdir -p /var/lib/odoo/filestore/$DB && tar -C /tmp -xzf - && cp -a /tmp/$SRC_DB/. /var/lib/odoo/filestore/$DB/" < "$PREFIX.filestore.tgz"
echo "Dipulihkan ke basis data '$DB'."
