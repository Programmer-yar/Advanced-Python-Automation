import openpyxl

#loads the excel sheet as 'workbook Object'
wb = openpyxl.load_workbook('example.xlsx')
print('Type of object: ', type(wb))

#gives the list of all sheet in an excel file
print('all sheet names: ', wb.sheetnames)

#get sheet by name in a work book object
sheet_2 = wb['Sheet2']
print(sheet_2)


print('type of sheet#2: ', type(sheet_2))
print(sheet_2.title)

#current sheet
print(wb.active)


