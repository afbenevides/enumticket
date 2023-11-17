import ticket
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red, black

t = ticket.Ticket(190 * mm, 65 * mm)
t.add_drawable(ticket.Image("Ticket_FDAT_2023-2.png"))
# t.add_drawable(ticket.Border(color=red))

# counter
pos_x = 122 * mm
pos_y = 4 * mm

t.add_drawable(ticket.Box(pos_x, pos_y, 19 * mm, 7 * mm, bordercolor=black, borderwidth=0.25 * mm))
t.add_drawable(ticket.Counter(pos_x + 3 * mm, pos_y + 2.2 * mm, fontname='Courier-Bold', fontsize=12))

t.add_drawable(ticket.Box(pos_x + 45 * mm, pos_y, 19 * mm, 7 * mm, bordercolor=black, borderwidth=0.25 * mm))
t.add_drawable(ticket.Counter(pos_x + 45 * mm + 3 * mm, pos_y + 2.2 * mm, fontname='Courier-Bold', fontsize=12))

# Note: Available width = page width - 2* cropmark size - margin left - margin right (donc 210 - 5*2 , si 0 left et 0 right
# LETTER size = 8.5 x 11 = 215.9mm   x 279.4
# A4 size                = 210mm       297 mm

Nb_billets_total = 3000

layout = ticket.PageLayout(t, Nb_billets_total, numoffset=1, pagesize=LETTER, bleed=0 * mm, bottom=0 * mm, left=5 * mm,
                           top=1 * mm, right=5 * mm)

c = canvas.Canvas('FICHIER_complet.pdf', layout.pagesize)
# print(c.getAvailableFonts())

layout.generate(c, order=ticket.STACKORDER, cropmarks=True, invert=True)
c.save()

# # creation des print par paquet brochables
# nb_billets_par_paquet = 5
# nb_billets_par_page = layout.colcount * layout.rowcount
# nb_billet_par_layout = (nb_billets_par_page * nb_billets_par_paquet)
# nb_layout_a_produire = Nb_billets_total // nb_billet_par_layout
#
# for n in range(nb_layout_a_produire):
#     layout = ticket.PageLayout(t, nb_billet_par_layout, numoffset=((n*nb_billet_par_layout)+1), pagesize=LETTER, bleed=2 * mm, bottom=0 * mm,
#                                left=5 * mm, top=1 * mm, right=5 * mm)
#
#     c = canvas.Canvas('Layout_'+str(n)+'.pdf', layout.pagesize)
#     # print(c.getAvailableFonts())
#     layout.generate(c, order=ticket.STACKORDER, cropmarks=True, invert=True)
#     c.save()
