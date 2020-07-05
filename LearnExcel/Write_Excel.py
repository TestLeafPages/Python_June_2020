import openpyxl

wb = openpyxl.Workbook()

sh = wb.active

sh.title = "Dev"

sh['A1'] = "FirstName"
sh['B1'] = "LastName"

sh['A2'] = "gopi"
sh['B2'] = "jaya"

wb.save("NewDev.xlsx")
