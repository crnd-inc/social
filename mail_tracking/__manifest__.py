# Copyright 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# Copyright 2018 David Vidal - <david.vidal@tecnativa.com>
# Copyright 2018 Tecnativa - Ernesto Tejeda
# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Email tracking",
    "summary": "Email tracking system for all mails sent",
    "version": "12.0.1.1.0",
    "category": "Social Network",
    "website": "http://github.com/OCA/social",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "decimal_precision",
        "mail",
    ],
    "data": [
        "data/tracking_data.xml",
        "security/mail_tracking_email_security.xml",
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/mail_tracking_email_view.xml",
        "views/mail_tracking_event_view.xml",
        "views/res_partner_view.xml",
    ],
    "qweb": [
        "static/src/xml/mail_tracking.xml",
    ],
    "pre_init_hook": "pre_init_hook",
}
