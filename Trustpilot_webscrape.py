
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

url = "https://www.trustpilot.com/review/www.misfitsmarket.com"


source = requests.get(url)
soup = BeautifulSoup(source.content, 'html.parser')

""" From each page I need teh user name, star rating, review title, review content, and date """

# reviewer name
reviewer_names = soup.find_all('span', class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17")
#print(reviewer_names.text)

# for i in reviewer_names:
#     print(i.text)
#     print()
#     print()



# star ratings
star_ratings = soup.find_all('div', class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty")
for i in star_ratings:
    alt_text = (i.img.get('alt'))
    # print(alt_text)
    # print(alt_text[6])
    

#review titles
review_titles = soup.find_all('h2', class_="typography_heading-s__f7029")
for i in review_titles:
    review_title = i.text
    # print(review_title)


# review contents
review_contents = soup.find_all('p', class_="typography_color-black__5LYEn")
for i in review_contents:
    content = i.text
    # print(content)
    # print()
    
# date
########START HERE#######
dates = soup.find_all('p', class_="typography_appearance-default__AAY17")
for i in dates:
    print(i.text)
    print()