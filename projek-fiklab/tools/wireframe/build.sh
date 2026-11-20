#!/usr/bin/env bash
# Bangun ulang database wireframe dari nol, jalankan Odoo 17, lalu ambil screenshot dengan Playwright.
#
#   bash projek-fiklab/tools/wireframe/build.sh <addon> <database> <folder_keluaran>
#   contoh: bash projek-fiklab/tools/wireframe/build.sh labfik_wireframe_sdm labfik_wf_sdm projek-fiklab/rancangan/wireframe-sdm
#
# Addon dicari di projek-fiklab/prototipe/<addon>/ dan harus memuat wireframe_shots.json.
# Alur lengkap: wireframe-CLAUDE.md di root repo.
set -euo pipefail
[ $# -eq 3 ] || { sed -n 4,5p "$0"; exit 1; }
HERE=$(cd "$(dirname "$0")" && pwd)
export WF_ADDON=$1 WF_DB=$2
export WF_ADDONS_DIR=$(cd "$HERE/../../prototipe" && pwd)
mkdir -p "$3"; OUT=$(cd "$3" && pwd)
[ -f "$WF_ADDONS_DIR/$WF_ADDON/wireframe_shots.json" ] || { echo "Tidak ada $WF_ADDONS_DIR/$WF_ADDON/wireframe_shots.json"; exit 1; }
[ -f "$WF_ADDONS_DIR/.gitignore" ] || printf '__pycache__/\n*.pyc\n' > "$WF_ADDONS_DIR/.gitignore"
ADDONS=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons
cd "$HERE"
docker compose down -v
docker compose up -d db
sleep 5
docker compose run --rm odoo -- --addons-path=$ADDONS -d "$WF_DB" -i "$WF_ADDON" --without-demo=all --stop-after-init
docker compose up -d odoo
until curl -sf -o /dev/null http://localhost:8069/web/login; do sleep 2; done
docker run --rm --network labfik-wireframe_default \
  -v "$HERE:/tools:ro" -v "$WF_ADDONS_DIR:/addons:ro" -v "$OUT:/out" \
  mcr.microsoft.com/playwright/python:v1.47.0-jammy \
  bash -c "pip -q show playwright >/dev/null 2>&1 || pip -q install --root-user-action=ignore playwright==1.47.0; python -I /tools/shoot.py http://odoo:8069 /out $WF_ADDON $WF_DB"
echo "Selesai. Odoo: http://localhost:8069 (admin/admin), database $WF_DB. Screenshot: $OUT"
echo "Hentikan: (cd $HERE && docker compose down)"
