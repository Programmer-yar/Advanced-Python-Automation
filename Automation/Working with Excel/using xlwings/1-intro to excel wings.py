import xlwings as xw

wb = xw.Book('calculator.xlsx')
sheet_1 = wb.sheets[0]

#read the value of specific cell
a1 = sheet_1.range('A1').value
print(a1)

sheet_1.range('A2').value = 10
sheet_1.range('B2').value = 20

c3 = sheet_1.range('C2').value
print(c3)
