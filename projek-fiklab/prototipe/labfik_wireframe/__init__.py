from . import models


def post_init(env):
    """Bahasa Indonesia untuk antarmuka (rupiah diatur di data_master.xml)."""
    env["res.lang"]._activate_lang("id_ID")
    env["ir.module.module"].search([("state", "=", "installed")])._update_translations(["id_ID"])
    env.ref("base.user_admin").write({"lang": "id_ID", "tz": "Asia/Jakarta"})
