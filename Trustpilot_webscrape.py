
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# establish Google Chrome webdriver
# webdriver_path = "./chromedriver"
# driver = webdriver.Chrome(executable_path=webdriver_path)

urls = [ 
        "https://www.trustpilot.com/review/www.misfitsmarket.com", 
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=2",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=3",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=4",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=5",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=6",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=7",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=8",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=9",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=10",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=11",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=12",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=13",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=14",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=15",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=16",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=17",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=18",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=19",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=20",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=21",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=22",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=23",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=24",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=25",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=26",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=27",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=28",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=29",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=30",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=31",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=32",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=33",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=34",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=35",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=36",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=37",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=38",
        "https://www.trustpilot.com/review/www.misfitsmarket.com?page=39",
        
        ]

# Get page via url
# driver.get(url)

final_reviewer_names = []
final_star_ratings = []
final_review_titles = []
final_review_contents = []
final_dates = []

for url in urls:

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser')
    
    """ From each page I need the user name, star rating, review title, review content, and date """
    
    # reviewer name
    reviewer_names = soup.find_all('span', class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17")
    
    for i in reviewer_names:
        name = i.text
        final_reviewer_names.append(name)
    
    
    
    
    
    # star ratings
    star_ratings = soup.find_all('div', class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty")
    temp_star_ratings = []
    for i in star_ratings:
        # need the index 6 ([6]) character because original alt_text looks like this: "Rated 5 out of 5 stars".  I only want the first number from this
        alt_text = (i.img.get('alt')[6])
        temp_star_ratings.append(alt_text)
    
    #need to remove first item from temp_star_ratings
    temp_star_ratings = temp_star_ratings[1:]
    final_star_ratings += [item for item in temp_star_ratings]
    
    
    
    
    
    
    
    #review titles
    review_titles = soup.find_all('h2', class_="typography_heading-s__f7029")
    
    for i in review_titles:
        review_title = i.text
        final_review_titles.append(review_title)
    
    
    
    
    
    ####### START HERE. How to catch this if therere is no review?
    # review contents
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
    for sublist in filler:
        final_review_contents.extend(sublist)

    
    
    
    
        
    # date
    dates = soup.find_all('p', class_="typography_body-m__xgxZ_")
    
    for i in dates:
        text = i.text
        
        # use regular expression to find date in this text
        date_regex = r"(?i)(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}"
        dates = re.findall(date_regex, text)
        
        if len(dates) > 0:
            final_dates.append(dates[0])
        
    
# put it all together in a pandas dataframe
# reviews_df = pd.DataFrame({
#     "Name": final_reviewer_names,
#     "Star Rating": final_star_ratings,
#     "Review Title": final_review_titles,
#     "Review Content": final_review_contents,
#     "Date": final_dates
#     })

#convert 'Date' column to pandas datetime object
# reviews_df['Date'] = pd.to_datetime(reviews_df['Date']).dt.date




# kill webdriver at the end
# driver.quit()