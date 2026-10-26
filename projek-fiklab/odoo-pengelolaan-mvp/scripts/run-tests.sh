#!/usr/bin/env bash
# Menjalankan seluruh test case modul labfik_org pada basis data sementara.
#   ./scripts/run-tests.sh
# Keluar dengan kode bukan nol bila ada test yang gagal.
set -euo pipefail
cd "$(dirname "$0")/.."

DB="labfik_test"
docker compose up -d --wait db
docker compose exec -T db dropdb -U odoo --if-exists "$DB"

LOG="$(mktemp)"
set +e
docker compose run --rm odoo odoo -d "$DB" -i labfik_org --without-demo=all \
  --test-enable --test-tags /labfik_org --stop-after-init --log-level=test 2>&1 | tee "$LOG"
RC=${PIPESTATUS[0]}
set -e

echo
echo "================ RINGKASAN ================"
grep -E "Ran [0-9]+ tests|tests? (failed|errors?)|[0-9]+ failed, [0-9]+ error" "$LOG" | tail -5 || true
if grep -qE "(ERROR|FAIL):" "$LOG"; then
  echo "Ada test yang GAGAL:"; grep -E "(ERROR|FAIL):" "$LOG" | head -40
  RC=1
fi
docker compose exec -T db dropdb -U odoo --if-exists "$DB" || true
exit $RC
