import ticket
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red

t = ticket.Ticket(190*mm, 62*mm)
t.add_drawable(ticket.Image("sample01.png"))
#t.add_drawable(ticket.Border(color=red))
t.add_drawable(ticket.Box(17*mm, 12*mm, 30*mm, 10*mm, bordercolor=red, borderwidth=1*mm))
t.add_drawable(ticket.Counter(20*mm, 15*mm, fontname='Courier-Bold', fontsize=20))

# Note: Available width = page width - 2* cropmark size - margin left - margin right (donc 210 - 5*2 , si 0 left et 0 right
#LETTER size = 8.5 x 11 = 215.9mm   x 279.4
#A4 size                = 210mm       297 mm
layout = ticket.PageLayout(t, 100, numoffset=100, pagesize=LETTER, bleed=2*mm, bottom=0*mm, left=5*mm, top=1*mm, right=5*mm)

c = canvas.Canvas('sample01.pdf', layout.pagesize)
#print(c.getAvailableFonts())
layout.generate(c, order=ticket.SEQUENTIALORDER, cropmarks=True)
c.save()
