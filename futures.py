
import requests
import csv
from bs4 import BeautifulSoup
response = requests.get(
    "https://www.taifex.com.tw/cht/5/stockMargining")
soup = BeautifulSoup(response.text, "html.parser")

table = soup.table
table_rows=table.find_all('tr')
output_rows=[]
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    output_rows.append(row)
print(output_rows)


response2 = requests.get(
    "https://histock.tw/stock/future.aspx")
soup2 = BeautifulSoup(response2.text, "html.parser")


table2= soup2.find('table', {'class': 'gvTB mt10'})
table_rows2=table2.find_all('tr')
output_rows2=[]
for tr in table_rows2:
    td = tr.find_all('td')
    row = [i.text for i in td]
    output_rows2.append(row)
print(output_rows2)
    
    
with open('myfile.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(output_rows)
with open('myfile2.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(output_rows2)
      




