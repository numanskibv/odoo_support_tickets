from datetime import timedelta
from odoo import models, fields, api

class SupportTicket(models.Model):
    _name = "support.ticket"
    _description = "Support Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc"

    name = fields.Char(string="Subject", required=True, tracking=True)
    ticket_ref = fields.Char(string="Ticket", readonly=True, copy=False)
    partner_id = fields.Many2one("res.partner", string="Customer", tracking=True)
    user_id = fields.Many2one("res.users", string="Assigned to", tracking=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("waiting", "Waiting"),
            ("done", "Solved"),
        ],
        default="new",
        tracking=True,
    )
    priority = fields.Selection(
    [
        ("0", "Low"),
        ("1", "Normal"),
        ("2", "High"),
        ("3", "Urgent"),
    ],
    default="1",
    tracking=True,
)
    sla_deadline = fields.Datetime(string="SLA Deadline", tracking=True)
    is_overdue = fields.Boolean(compute="_compute_is_overdue", store=True)
    
    
    description = fields.Text()
    

@api.model
def create(self, vals):
    if not vals.get("ticket_ref"):
        vals["ticket_ref"] = self.env["ir.sequence"].next_by_code("support.ticket")

    if not vals.get("sla_deadline"):
        # simpele SLA: 48 uur vanaf aanmaken
        vals["sla_deadline"] = fields.Datetime.now() + timedelta(hours=48)

    return super().create(vals)

    # 📧 Incoming mail → new ticket
    @api.model
    def message_new(self, msg, custom_values=None):
        subject = msg.get("subject") or "No subject"

        partner = self.env["res.partner"].search(
            [("email", "=", msg.get("from"))], limit=1
        )

        values = {
            "name": subject,
            "partner_id": partner.id if partner else False,
            "description": msg.get("body"),
        }

        if custom_values:
            values.update(custom_values)

        ticket = super().message_new(msg, values)
        return ticket

    # 📧 Reply → existing ticket
    def message_update(self, msg, update_vals=None):
        return super().message_update(msg, update_vals)
    
    from datetime import datetime


    @api.depends("sla_deadline", "state")
    def _compute_is_overdue(self):
        now = fields.Datetime.now()
        for rec in self:
                rec.is_overdue = (
                rec.state not in ("done",)
                and rec.sla_deadline
                and rec.sla_deadline < now
            )
    