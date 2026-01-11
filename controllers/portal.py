from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class SupportPortal(CustomerPortal):

    # Lijst met tickets
    @http.route(['/my/tickets'], type='http', auth="user", website=True)
    def portal_my_tickets(self, **kw):
        partner = request.env.user.partner_id
        tickets = request.env["support.ticket"].sudo().search(
            [("partner_id", "=", partner.id)],
            order="create_date desc"
        )

        return request.render("numanski_support.portal_my_tickets", {
            "tickets": tickets,
        })

    # Ticket detail
    @http.route(['/my/tickets/<int:ticket_id>'], type='http', auth="user", website=True)
    def portal_ticket_detail(self, ticket_id, **kw):
        ticket = request.env["support.ticket"].sudo().browse(ticket_id)

        if ticket.partner_id != request.env.user.partner_id:
            return request.redirect("/my")

        return request.render("numanski_support.portal_ticket_detail", {
            "ticket": ticket,
        })

    # Nieuw ticket formulier
    @http.route(['/my/tickets/new'], type='http', auth="user", website=True)
    def portal_ticket_new(self, **kw):
        return request.render("numanski_support.portal_ticket_new", {})

    # Ticket aanmaken (POST)
    @http.route(['/my/tickets/create'], type='http', auth="user", website=True, methods=["POST"])
    def portal_ticket_create(self, **post):
        partner = request.env.user.partner_id

        ticket = request.env["support.ticket"].sudo().create({
            "name": post.get("subject"),
            "description": post.get("description"),
            "partner_id": partner.id,
            "priority": post.get("priority", "1"),
        })

        ticket.message_post(
            body=post.get("description"),
            message_type="comment",
            subtype_xmlid="mail.mt_comment",
        )

        return request.redirect(f"/my/tickets/{ticket.id}")