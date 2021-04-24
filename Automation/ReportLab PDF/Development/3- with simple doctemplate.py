# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors

from reportlab.rl_config import TTFSearchPath
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#adding custom fonts to RL search path
fonts_path = os.getcwd() + "\\fonts"
TTFSearchPath.append(fonts_path)

pdf_path = os.getcwd() + "\\pdf\\Simple-Doc-Template.pdf"
#registering custom fonts
pdfmetrics.registerFont(TTFont('pala', 'pala.ttf'))
pdfmetrics.registerFont(TTFont('palab', 'palab.ttf'))
pdfmetrics.registerFont(TTFont('Palatino Linotype', 'Palatino Linotype.ttf'))


styles = getSampleStyleSheet()

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('pala', 9)
    canvas.drawString(40,720,'PLATINUM FILINGS LLC')
    canvas.drawString(40,708,'99 WEST HAWTHORNE AVENUE')
    canvas.drawString(40,696,'SUITE 408')
    canvas.drawString(40,684,'VALLLEY STREAM, NY 11580')

    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(468, 741.6,'Invoice')
    canvas.setFont('Helvetica', 10)
    
    canvas.drawString(468, 725, f'Page {doc.page}')

    canvas.setLineWidth(.3)
    canvas.rect(378, 648, 223, 36)
    canvas.line(378, 671, 601, 671)
    canvas.line(464, 648, 464, 684)

    canvas.setFont('Helvetica', 9)
    canvas.drawString(385, 674,'Invoice Date')
    canvas.drawString(470, 674,'Invoice Number')
    
    canvas.setFont('pala', 9)
    canvas.drawString(385, 660,'April 14, 2021')
    canvas.drawString(470, 660,'2020-5742')
    
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.rect(20, 504, 270, 117)
    canvas.line(20, 599, 290, 599)
    canvas.setFont('palab', 9)
    canvas.drawString(40, 605,'Bill To:')

    canvas.setFont('pala', 9)
    
    canvas.drawString(40, 585,'Test Orders Invoices')
    canvas.drawString(40, 573,'123 Center Str')
    canvas.drawString(40, 561,'Boko Town, Boko 999999')

    
    canvas.rect(310, 504, 270, 117)
    canvas.line(310, 599, 580, 599)

    canvas.setFont('palab', 9)
    canvas.drawString(320, 605,'Order Information:')
    canvas.drawString(320, 585,'Order Date: ')
    canvas.drawString(320, 573,'Order Name: ')
    canvas.drawString(320, 561,'Client Matter Number: ')
    canvas.drawString(320, 549,'Total Amount Due: ')
    canvas.drawString(320, 537,'Processed By: ')
    canvas.drawString(320, 525,'Authorized By: ')

    canvas.setFont('pala', 9)
    canvas.drawString(390, 585,'April 14, 2021')
    canvas.drawString(390, 573,'Test orders Aaron')
    
    canvas.drawString(405, 549,'$144945')
    canvas.drawString(390, 537,'Aaron Sauber')
    canvas.drawString(390, 525,'Judith Testing')

    
    canvas.setStrokeColorRGB(0.8, 0.8, 0.8)
    canvas.line(72, 635, 540, 635)

    canvas.setFillColorRGB(0, 0.4, 0.7)
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(1)
    canvas.rect(20, 465, 572, 18, fill=1)
    canvas.setFillColorRGB(1, 1, 1)
    canvas.setFont('Helvetica', 10)
    canvas.drawString(30, 470,'SUMMARY')

    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('pala', 9)
    canvas.drawString(40,720,'PLATINUM FILINGS LLC')
    canvas.drawString(40,708,'99 WEST HAWTHORNE AVENUE')
    canvas.drawString(40,696,'SUITE 408')
    canvas.drawString(40,684,'VALLLEY STREAM, NY 11580')

    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(468, 741.6,'Invoice')
    canvas.setFont('Helvetica', 10)
    
    canvas.drawString(468, 725, f'Page {doc.page}')

    canvas.setLineWidth(.3)
    canvas.rect(378, 648, 223, 36)
    canvas.line(378, 671, 601, 671)
    canvas.line(464, 648, 464, 684)

    canvas.setFont('Helvetica', 9)
    canvas.drawString(385, 674,'Invoice Date')
    canvas.drawString(470, 674,'Invoice Number')
    
    canvas.setFont('pala', 9)
    canvas.drawString(385, 660,'April 14, 2021')
    canvas.drawString(470, 660,'2020-5742')
    canvas.restoreState()
 

data= [
    ['PRODUCT', 'DESCRIPTION', 'JURISDICTION', 'PRICE', 'QTY', 'TOTAL'],
    ['AK - Certified Charter', 'Company Name Llc', 'Alaska', '$55.00', '1.00', '$55.00'],
    ['AK - Filing', 'Company Name Llc', 'West Baton Rouge - LA', '$75.00', '1.00', '$75.00']
    ]

style = TableStyle(
    [
        ("BOX" , (0, 0), (-1, -1), 0.7 , colors.black),
        ("GRID" , (0, 0), (5 ,3), 0.7 , colors.black),
        ("BACKGROUND" , (0, 0), (5, 0), colors.grey),
        ("ALIGN" , (0, 1), (-1, -1), "LEFT" ),
        ("ALIGN" , (0, 0), (5, 0), "CENTER" ),
        ("FONTNAME" , (0, 1), (-1, -1), "pala" ),
        ("FONTSIZE" , (0, 1), (-1, -1), 8),
    ]
    )
table = Table(data, style=style)
doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=20, leftMargin=20,
                        topMargin=200)
table._argW[0]=2.1*inch
table._argW[1]=2.2*inch
table._argW[2]=2*inch 
Story = [Spacer(0,120)]#[Spacer(1,2*inch)]
#style = styles["Normal"]
# for i in range(10):
#     bogustext = ("Paragraph number %s. " % i) *20
#     p = Paragraph(bogustext, style)
#     Story.append(p)
#     Story.append(Spacer(0,0.2*inch))
Story.append(table)

doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    

