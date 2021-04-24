import xlwings as xw

wb = xw.Book('calculator.xlsx')
sheet_1 = wb.sheets[0]

c3 = sheet_1.range('C1').value
print(c3)
