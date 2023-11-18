import ticket
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red
import os


# Replace this with your file path
Data_file_path = 'data/config.py'

# Check if the file exists
if os.path.exists(Data_file_path):
    from data import config

    TICKETS_WIDTH_MM = config.TICKETS_WIDTH_MM
    TICKETS_HEIGHT_MM = config.TICKETS_HEIGHT_MM

    TICKETS_IMAGE_PATH = config.TICKETS_IMAGE_PATH

    FIRST_COUNTER_X_POS_MM = config.FIRST_COUNTER_X_POS_MM
    FIRST_COUNTER_Y_POS_MM = config.FIRST_COUNTER_Y_POS_MM

    FIRST_COUNTER_BOX_WIDTH_MM = config.FIRST_COUNTER_BOX_WIDTH_MM
    FIRST_COUNTER_BOX_LENGTH_MM = config.FIRST_COUNTER_BOX_LENGTH_MM
    FIRST_COUNTER_BOX_BORDER_COLOR = config.FIRST_COUNTER_BOX_BORDER_COLOR
    FIRST_COUNTER_BOX_BORDERWIDTH = config.FIRST_COUNTER_BOX_BORDERWIDTH

    FIRST_COUNTER_POS_OFFSET_X = config.FIRST_COUNTER_POS_OFFSET_X
    FIRST_COUNTER_POS_OFFSET_Y = config.FIRST_COUNTER_POS_OFFSET_Y
    FIRST_COUNTER_FONTNAME = config.FIRST_COUNTER_FONTNAME
    FIRST_COUNTER_FONTSIZE = config.FIRST_COUNTER_FONTSIZE

    SECOND_COUNTER_ACTIVATE = config.SECOND_COUNTER_ACTIVATE
    SECOND_COUNTER_X_POS_OFFSET_MM = config.SECOND_COUNTER_X_POS_OFFSET_MM
    SECOND_COUNTER_Y_POS_OFFSET_MM = config.SECOND_COUNTER_Y_POS_OFFSET_MM

    NB_TICKETS_TOTAL = config.NB_TICKETS_TOTAL
    NB_TICKETS_PER_BUNDLE = config.NB_TICKETS_PER_BUNDLE

    PAGE_LAYOUT_TICKETS_NUMOFFSET = config.PAGE_LAYOUT_TICKETS_NUMOFFSET
    PAGE_LAYOUT_TICKETS_PAGESIZE = config.PAGE_LAYOUT_TICKETS_PAGESIZE
    PAGE_LAYOUT_TICKETS_BLEED_MM = config.PAGE_LAYOUT_TICKETS_BLEED_MM
    PAGE_LAYOUT_TICKETS_MARGIN_BOTTOM_MM = config.PAGE_LAYOUT_TICKETS_MARGIN_BOTTOM_MM
    PAGE_LAYOUT_TICKETS_MARGIN_LEFT_MM = config.PAGE_LAYOUT_TICKETS_MARGIN_LEFT_MM
    PAGE_LAYOUT_TICKETS_MARGIN_TOP_MM = config.PAGE_LAYOUT_TICKETS_MARGIN_TOP_MM
    PAGE_LAYOUT_TICKETS_MARGIN_RIGHT_MM = config.PAGE_LAYOUT_TICKETS_MARGIN_RIGHT_MM

    LAYOUT_GENERATION_ORDER = config.LAYOUT_GENERATION_ORDER
    LAYOUT_GENERATION_CROPMARKS = config.LAYOUT_GENERATION_CROPMARKS
    LAYOUT_GENERATION_INVERT = config.LAYOUT_GENERATION_INVERT
    LAYOUT_BUNDLE_ACTIVATE = config.LAYOUT_BUNDLE_ACTIVATE



else:
    TICKETS_WIDTH_MM = 84
    TICKETS_HEIGHT_MM = 62

    TICKETS_IMAGE_PATH = "sample01.png"

    FIRST_COUNTER_X_POS_MM = 17
    FIRST_COUNTER_Y_POS_MM = 12

    FIRST_COUNTER_BOX_WIDTH_MM = 30
    FIRST_COUNTER_BOX_LENGTH_MM = 10
    FIRST_COUNTER_BOX_BORDER_COLOR = red
    FIRST_COUNTER_BOX_BORDERWIDTH = 1

    FIRST_COUNTER_POS_OFFSET_X = 3
    FIRST_COUNTER_POS_OFFSET_Y = 3
    FIRST_COUNTER_FONTNAME = "Courier-Bold"
    FIRST_COUNTER_FONTSIZE = 20

    SECOND_COUNTER_ACTIVATE = False
    SECOND_COUNTER_X_POS_OFFSET_MM = 45
    SECOND_COUNTER_Y_POS_OFFSET_MM = 0

    NB_TICKETS_TOTAL = 100
    NB_TICKETS_PER_BUNDLE = 5

    PAGE_LAYOUT_TICKETS_NUMOFFSET = 100
    PAGE_LAYOUT_TICKETS_PAGESIZE = A3
    PAGE_LAYOUT_TICKETS_BLEED_MM = 2
    PAGE_LAYOUT_TICKETS_MARGIN_BOTTOM_MM = 0
    PAGE_LAYOUT_TICKETS_MARGIN_LEFT_MM = 0
    PAGE_LAYOUT_TICKETS_MARGIN_TOP_MM = 0
    PAGE_LAYOUT_TICKETS_MARGIN_RIGHT_MM = 0

    LAYOUT_GENERATION_ORDER = ticket.SEQUENTIALORDER
    LAYOUT_GENERATION_CROPMARKS = True
    LAYOUT_GENERATION_INVERT = False
    LAYOUT_BUNDLE_ACTIVATE = False

t = ticket.Ticket(TICKETS_WIDTH_MM * mm, TICKETS_HEIGHT_MM * mm)
t.add_drawable(ticket.Image(TICKETS_IMAGE_PATH))
# t.add_drawable(ticket.Border(color=red))

# 1rst counter position
pos_x = FIRST_COUNTER_X_POS_MM * mm
pos_y = FIRST_COUNTER_Y_POS_MM * mm

t.add_drawable(ticket.Box(pos_x, pos_y, FIRST_COUNTER_BOX_WIDTH_MM * mm, FIRST_COUNTER_BOX_LENGTH_MM * mm, bordercolor=FIRST_COUNTER_BOX_BORDER_COLOR, borderwidth=FIRST_COUNTER_BOX_BORDERWIDTH * mm))
t.add_drawable(ticket.Counter(pos_x + FIRST_COUNTER_POS_OFFSET_X * mm, pos_y + FIRST_COUNTER_POS_OFFSET_Y * mm, fontname=FIRST_COUNTER_FONTNAME, fontsize=FIRST_COUNTER_FONTSIZE))

# Deactivate/activate second counter for raffle ticket double numerotation with False/True
if SECOND_COUNTER_ACTIVATE:
    t.add_drawable(ticket.Box(pos_x + SECOND_COUNTER_X_POS_OFFSET_MM * mm, pos_y + SECOND_COUNTER_Y_POS_OFFSET_MM * mm, FIRST_COUNTER_BOX_WIDTH_MM * mm, FIRST_COUNTER_BOX_LENGTH_MM * mm, bordercolor=FIRST_COUNTER_BOX_BORDER_COLOR, borderwidth=FIRST_COUNTER_BOX_BORDERWIDTH * mm))
    t.add_drawable(ticket.Counter(pos_x + SECOND_COUNTER_X_POS_OFFSET_MM * mm + FIRST_COUNTER_POS_OFFSET_X * mm, pos_y + SECOND_COUNTER_Y_POS_OFFSET_MM * mm + FIRST_COUNTER_POS_OFFSET_Y * mm, fontname=FIRST_COUNTER_FONTNAME, fontsize=FIRST_COUNTER_FONTSIZE))

# Note: Available width = page width - 2* cropmark size - margin left - margin right (donc 210 - 5*2 , si 0 left et 0 right
# LETTER size = 8.5 x 11 = 215.9mm   x 279.4
# A4 size                = 210mm       297 mm

# #enter here total number of tickets
# NB_TICKETS_TOTAL = NB_TICKETS_TOTAL

#Creation of PDF with all tickets
layout = ticket.PageLayout(t, NB_TICKETS_TOTAL, numoffset=PAGE_LAYOUT_TICKETS_NUMOFFSET, pagesize=PAGE_LAYOUT_TICKETS_PAGESIZE, bleed=PAGE_LAYOUT_TICKETS_BLEED_MM * mm, bottom=PAGE_LAYOUT_TICKETS_MARGIN_BOTTOM_MM * mm, left=PAGE_LAYOUT_TICKETS_MARGIN_LEFT_MM * mm,
                           top=PAGE_LAYOUT_TICKETS_MARGIN_TOP_MM * mm, right=PAGE_LAYOUT_TICKETS_MARGIN_RIGHT_MM * mm)

c = canvas.Canvas('data/Layout_0_complete_file.pdf', layout.pagesize)
# print(c.getAvailableFonts())

#Validate if now data folder exists, if not create it
if not os.path.exists('data/'):
    os.makedirs('data/')

layout.generate(c, order=LAYOUT_GENERATION_ORDER, cropmarks=LAYOUT_GENERATION_CROPMARKS, invert=LAYOUT_GENERATION_INVERT)
c.save()

# Creation of stapled bundles ready for prints
# deactivate/activate bundle creation with False/True
if LAYOUT_BUNDLE_ACTIVATE:
    nb_ticket_per_stapled_bundle = NB_TICKETS_PER_BUNDLE
    nb_tickets_per_page = layout.colcount * layout.rowcount
    nb_tickets_per_layout = (nb_tickets_per_page * nb_ticket_per_stapled_bundle)
    nb_layout_to_produce = NB_TICKETS_TOTAL // nb_tickets_per_layout

    for n in range(nb_layout_to_produce):
        layout = ticket.PageLayout(t, nb_tickets_per_layout, numoffset=((n * nb_tickets_per_layout) + PAGE_LAYOUT_TICKETS_NUMOFFSET), pagesize=PAGE_LAYOUT_TICKETS_PAGESIZE, bleed=PAGE_LAYOUT_TICKETS_BLEED_MM * mm, bottom=PAGE_LAYOUT_TICKETS_MARGIN_BOTTOM_MM * mm,
                                   left=PAGE_LAYOUT_TICKETS_MARGIN_LEFT_MM * mm, top=PAGE_LAYOUT_TICKETS_MARGIN_TOP_MM * mm, right=PAGE_LAYOUT_TICKETS_MARGIN_RIGHT_MM * mm)

        c = canvas.Canvas('data/Layout_'+str(n)+'.pdf', layout.pagesize)
        # print(c.getAvailableFonts())
        layout.generate(c, order=ticket.STACKORDER, cropmarks=LAYOUT_GENERATION_CROPMARKS, invert=LAYOUT_GENERATION_INVERT)
        c.save()
