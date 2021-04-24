from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.pagesizes import letter

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []
#add some flowables
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
styleN))
s1 = story[:]

c = Canvas('myframes.pdf', pagesize=letter)
f1 = Frame(inch, inch, 3*inch, 4.5*inch, showBoundary=1)
f2 = Frame(4.1*inch, inch, 3*inch, 4.5*inch, showBoundary=1)
f1.addFromList(story,c)
f2.addFromList(s1,c)
c.save()