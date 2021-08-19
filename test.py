import xlrd

wb= xlrd.open_workbook('C:\\Users\\jie.lu\\Desktop\\SMOKE_版本.xlsx')
sheet1 = wb.sheet_by_index(0)  #这里的excel文档内只有一个表格，0代表第一个

rows = sheet1.nrows