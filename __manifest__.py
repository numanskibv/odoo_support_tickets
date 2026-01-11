{
    "name": "Numanski Supportdesk",
    "version": "18.0.1.0.0",
    "category": "Services",
    "summary": "Simple Supportdesk for Odoo Community",
    "author": "Numanski",
    "depends": ["mail", "contacts", "portal", "website"],
    "data": [
        "data/sequence.xml",
        "security/ir.model.access.csv",
        "views/support_ticket_views.xml",
        "views/support_menu.xml",
        "views/portal_templates.xml",
],
    "application": True,
    "license": "LGPL-3",
}