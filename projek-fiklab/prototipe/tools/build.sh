#!/usr/bin/env bash
# Bangun ulang database wireframe dari nol, jalankan Odoo, lalu ambil screenshot ke rancangan/wireframe/.
# Jalankan dari folder projek-fiklab/prototipe:  bash tools/build.sh
set -euo pipefail
ADDONS=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons
docker compose down -v
docker compose up -d db
sleep 5
docker compose run --rm odoo -- --addons-path=$ADDONS -d labfik_wf -i labfik_wireframe --without-demo=all --stop-after-init
docker compose up -d odoo
until curl -sf -o /dev/null http://localhost:8069/web/login; do sleep 2; done
mkdir -p ../rancangan/wireframe
docker run --rm --network prototipe_default \
  -v "$PWD/tools:/tools:ro" -v "$PWD/../rancangan/wireframe:/out" \
  mcr.microsoft.com/playwright/python:v1.47.0-jammy \
  bash -c "pip -q show playwright >/dev/null 2>&1 || pip -q install --root-user-action=ignore playwright==1.47.0; python -I /tools/shoot.py http://odoo:8069 /out"
echo "Selesai. Odoo: http://localhost:8069 (admin/admin). Screenshot: rancangan/wireframe/"
