import docx
from docx.enum.style import WD_STYLE_TYPE

document= docx.Document('list test.docx')

styles = document.styles
paragraph_styles = [
    s for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH
    ]
for style in paragraph_styles:
    print(style.name)
