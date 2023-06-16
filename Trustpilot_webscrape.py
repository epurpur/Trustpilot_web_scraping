
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

url = "https://www.trustpilot.com/review/www.misfitsmarket.com"


source = requests.get(url)
print(source.text)
soup = BeautifulSoup(source.content, 'html.parser')

reviewer_names = soup.find_all('span', class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17")
#print(reviewer_names.text)

for i in reviewer_names:
    print(i.text)
    print()
    print()

# for item in soup.find_all('div', class_="styles_consumerInfoWrapper__KP3Ra"):
#     print(item)

#styles_consumerInfoWrapper__KP3Ra
