
import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://www.taifex.com.tw/cht/5/stockMargining")
soup = BeautifulSoup(response.text, "html.parser")

for item in soup.find_all('table','table_c'):
     
     print(item.text)



