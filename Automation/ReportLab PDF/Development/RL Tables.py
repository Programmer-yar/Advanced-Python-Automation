import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

pdf_path = os.getcwd() + "\\pdf\\simple_table.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
# container for the 'Flowable' objects
elements = []
data= [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
    ]

t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(1,1),(3,2),colors.green),
('TEXTCOLOR',(0,0),(1,3),colors.red)]))
elements.append(t)
# write the document to disk
doc.build(elements)