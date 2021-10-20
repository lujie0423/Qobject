from win32com.client.gencache import EnsureDispatch
from win32com.client import constants
from bs4 import BeautifulSoup
import requests

yourExcelFile = 'C:\\Users\\jie.lu\\Desktop\\SMOKE_版本.xlsx'
newFileName = 'C:\\Users\\jie.lu\\Desktop\\test_111.htm'

xl = EnsureDispatch('Excel.Application')
wb = xl.Workbooks.Open(yourExcelFile)
wb.SaveAs(newFileName, constants.xlHtml)
xl.Workbooks.Close()
xl.Quit()
del xl

