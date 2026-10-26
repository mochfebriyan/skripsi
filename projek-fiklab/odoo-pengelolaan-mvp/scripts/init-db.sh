#!/usr/bin/env bash
# Membuat basis data baru dan memasang modul labfik_org.
#   ./scripts/init-db.sh                 → basis data "labfik" tanpa data contoh
#   ./scripts/init-db.sh labfik_demo --demo → basis data dengan data contoh fiktif
set -euo pipefail
cd "$(dirname "$0")/.."

DB="${1:-labfik}"
DEMO_FLAG="--without-demo=all"
if [[ "${2:-}" == "--demo" ]]; then DEMO_FLAG=""; fi

docker compose up -d --wait db
echo ">> Memasang modul labfik_org ke basis data '$DB' ..."
docker compose run --rm odoo odoo -d "$DB" -i labfik_org --load-language=id_ID $DEMO_FLAG --stop-after-init

echo ">> Mengatur bahasa admin ke Bahasa Indonesia ..."
docker compose run --rm -T odoo odoo shell -d "$DB" --no-http --log-level=warn <<'PY'
env['res.lang']._activate_lang('id_ID')
env.ref('base.user_admin').write({'lang': 'id_ID', 'tz': 'Asia/Jakarta'})
env.cr.commit()
PY

docker compose up -d odoo
echo ">> Selesai. Buka http://localhost:8069 lalu pilih basis data '$DB'."
echo "   Login awal: admin / admin (segera ganti kata sandinya)."
