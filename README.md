# Numanski Supportdesk — Odoo 18 Community Module

Custom supportdesk / ticketing module voor **Odoo 18 Community Edition** met klantenportaal.

Deze module biedt basis helpdeskfunctionaliteit zonder Enterprise-licentie en is bedoeld
voor eigen gebruik en verdere uitbreiding.

Module naam: `numanski_support`

---

## ✨ Functionaliteit

### 🎫 Support Tickets

Model: `support.ticket`

Velden:
- Ticketreferentie (sequence)
- Onderwerp
- Omschrijving
- Klant (partner)
- Status:
  - New
  - In Progress
  - Waiting
  - Done
- Prioriteit (Low / Normal / High / Urgent)
- SLA deadline
- Overdue indicator (computed)

Views:
- List
- Form
- Kanban

Overdue tickets worden visueel gemarkeerd in kanban.

---

### 💬 Chatter & Mail

- `mail.thread` integratie
- Interne communicatie via chatter
- Portal replies komen in hetzelfde ticket
- Klaar voor mail-threading (inkomende mail uitbreiding gepland)

---

### 🌐 Klantenportaal

Portal gebruikers kunnen:

- ✔ Eigen tickets bekijken
- ✔ Ticketdetails zien
- ✔ Reageren via website
- ✔ Nieuw ticket aanmaken via portal

Portal routes:
- `/my/tickets`
- `/my/tickets/<id>`
- `/my/tickets/new`
- `/my/tickets/create` (POST)

Op de portal homepage (`/my`) wordt een tegel **“Mijn tickets”** toegevoegd,
gestyled volgens de standaard Odoo 18 portal cards (zelfde layout als “Je facturen”).

---

## 🔐 Beveiliging

- Klanten kunnen alleen hun eigen tickets zien
- Validatie in portal controller op partner-id

---

## 🧩 Technische details

- Odoo versie: **18.0 Community**
- Inherits:
  - `mail.thread`
  - `mail.activity.mixin`
- Portal controllers in:
  - `controllers/portal.py`
- Portal templates in:
  - `views/portal_templates.xml`

---

## 📌 Bekende beperkingen

Nog niet geïmplementeerd:

- Bijlagen uploaden via portal
- Inkomende mail → automatische ticketcreatie
- Support teams
- Automatische tickettoewijzing
- Rapportages / dashboards

---

## 🛠️ Uitbreidingsideeën

Geplande uitbreidingen:

- 📎 Portal file uploads (attachments)
- 🏷 Ticket categorieën
- 🤖 Auto-assign op basis van categorie of workload
- 📧 Volledige mail → ticket → mail flow
- 👥 Meerdere contactpersonen per klant

---

## 📄 Licentie

Intern gebruik — nog niet gespecificeerd.

---

## 👤 Auteur

Numanski BV  
Interne ontwikkeling