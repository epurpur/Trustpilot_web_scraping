

import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

###############################################################################

# establish Google Chrome webdriver
webdriver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=webdriver_path)

url = "https://www.trustpilot.com/review/www.misfitsmarket.com?page=10"

# Get Page via URL
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

""" From each page I need the user name, star rating, review title, review content, and date """

# reviewer name

holders = soup.find_all('div', class_="styles_reviewContent__0Q2Tg")
html_strings = []

#convert html to strings and store in html_strings list
for i in holders:
    string = str(i)
    html_strings.append(string)
    
#loop through html_strings items to remove unwanted html
extracted = []   # this holds the final string, whether it is empty or not
for i in html_strings:
    content_regex = r'<p class="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn" data-service-review-text-typography="true">(.*?)</p>'
    content = re.findall(content_regex, i)   
    extracted.append(content)


#now that I have 'extracted' above, I need to fill the empty values with a placeholder of "empty value"
#except "empty value" needs to be a list of a single item like this: ["empty value"] because the rest of them are
filler = [["empty value"] if not sublist else sublist for sublist in extracted]

#lastly, add all items from filler as items in a single list
final_review_contents = [item for sublist in filler for item in sublist]

driver.quit()

###############################################################################

# url = "https://www.trustpilot.com/review/www.misfitsmarket.com?page=10"

# source = requests.get(url)
# soup = BeautifulSoup(source.content, 'lxml')

# holders = soup.find_all('div', class_="styles_reviewContent__0Q2Tg")
# html_strings = []

# #convert html to strings and store in html_strings list
# for i in holders:
#     string = str(i)
#     html_strings.append(string)
    
# #loop through html_strings items to remove unwanted html
# extracted = []   # this holds the final string, whether it is empty or not
# for i in html_strings:
#     content_regex = r'<p class="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn" data-service-review-text-typography="true">(.*?)</p>'
#     content = re.findall(content_regex, i)   
#     extracted.append(content)

