
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re

url = "https://www.trustpilot.com/review/www.misfitsmarket.com"


source = requests.get(url)
soup = BeautifulSoup(source.content, 'html.parser')

""" From each page I need teh user name, star rating, review title, review content, and date """

# reviewer name
reviewer_names = soup.find_all('span', class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17")
final_reviewer_names = []

for i in reviewer_names:
    name = i.text
    final_reviewer_names.append(name)


# star ratings
star_ratings = soup.find_all('div', class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty")
final_star_ratings = []
for i in star_ratings:
    # need the index 6 ([6]) character because original alt_text looks like this: "Rated 5 out of 5 stars".  I only want the first number from this
    alt_text = (i.img.get('alt')[6])
    final_star_ratings.append(alt_text)

#need to remove first item from final_star_ratings
final_star_ratings = final_star_ratings[1:]


#review titles
review_titles = soup.find_all('h2', class_="typography_heading-s__f7029")

final_review_titles = []
for i in review_titles:
    review_title = i.text
    final_review_titles.append(review_title)
    # print(review_title)


# review contents
review_contents = soup.find_all('p', class_="typography_color-black__5LYEn")
final_review_contents = []
for i in review_contents:
    content = i.text
    final_review_contents.append(content)

    
# date
dates = soup.find_all('p', class_="typography_body-m__xgxZ_")

final_dates = []
for i in dates:
    text = i.text
    
    # use regular expression to find date in this text
    date_regex = r"(?i)(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}"
    dates = re.findall(date_regex, text)
    
    if len(dates) > 0:
        final_dates.append(dates[0])
        
    
# put it all together in a pandas dataframe
reviews_df = pd.DataFrame({
    "Name": final_reviewer_names,
    "Star Rating": final_star_ratings,
    "Review Title": final_review_titles,
    "Review Content": final_review_contents,
    "Date": final_dates
    })

#convert 'Date' column to pandas datetime object
# reviews_df['Date'] = pd.to_datetime(reviews_df['Date']).dt.date