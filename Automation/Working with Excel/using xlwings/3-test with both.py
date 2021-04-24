import xlwings
import openpyxl

wb = openpyxl.load_workbook('calculator.xlsx')
sheet_1 = wb['Sheet1']
sheet_1['A1'].value = 2000
sheet_1['B1'].value = 3000
wb.save('calculator.xlsx')

excel_app = xlwings.App(visible=False)
excel_book = excel_app.books.open('calculator.xlsx')
sheet_1 = excel_book.sheets[0]
c3 = sheet_1.range('C1').value
print(c3)

excel_book.save()
excel_book.close()
excel_app.quit()

#data = load_workbook('PATH_TO_YOUR_XLSX_FILE', data_only=True)
