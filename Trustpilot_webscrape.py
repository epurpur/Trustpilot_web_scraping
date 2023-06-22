
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import urls as url_list

#### Question:  Should I automate this with Selenium??

##### CHANGE THIS ACCORDING TO THE COMPANY YOU WANT DATA FROM. View options in urls.py file
urls = url_list.lidl_uk()



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
    
    try:
        for i in star_ratings:
            # need the index 6 ([6]) character because original alt_text looks like this: "Rated 5 out of 5 stars".  I only want the first number from this
            alt_text = (i.img.get('alt')[6])
            temp_star_ratings.append(alt_text)
        
        
    except Exception:
        temp_star_ratings.append("0")  # all others are string so add this as string too
        
    #need to remove first item from temp_star_ratings
    temp_star_ratings = temp_star_ratings[1:]
    final_star_ratings += [item for item in temp_star_ratings]
    
    
    
    
    
    #review titles
    review_titles = soup.find_all('h2', class_="typography_heading-s__f7029")
    
    for i in review_titles:
        review_title = i.text
        final_review_titles.append(review_title)
    
    
    
    
    
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
        # use regex to find the tag of html content
        content_regex = r'<p class="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn" data-service-review-text-typography="true">(.*?)</p>'
        content = re.findall(content_regex, i)   
        extracted.append(content)

    #now that I have 'extracted' above, I need to fill the empty values with a placeholder of "empty value"
    #except "empty value" needs to be a list of a single item like this: ["empty value"] because the rest of them are
    filler = [["empty value"] if not sublist else sublist for sublist in extracted]

    #lastly, add all items from filler as items in a single list
    for sublist in filler:
        final_review_contents.extend(sublist)

    
    
    
        
    # # date
    # dates = soup.find_all('p', class_="typography_body-m__xgxZ_")
    
    # try:
    #     for i in dates:
    #         text = i.text
            
    #         # use regular expression to find date in this text
    #         date_regex = r"(?i)(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}"
    #         dates = re.findall(date_regex, text)
            
    #         if len(dates) > 0:
    #             final_dates.append(dates[0])
                
    # except Exception:
    #     final_dates.append('January 1, 1900')
    
    # date
    dates = soup.find_all('div', class_="styles_reviewContent__0Q2Tg")
    
    date_strings = []
    
    for i in dates:
        string = str(i)
        date_strings.append(string)
        
    #loop through date_strings items to remove unwanted html
    extracted = []  #this holds the final string, whether it is empty or not. Will only be empty in rare case that review was flagged for some warning
    for i in date_strings:
        # use regex to find tag of date content. This could be empty!
        # content_regex = r"(?i)(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}"
        content_regex = r"(?i)(?!Friday, May 26, 2023)(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}"
        content = re.findall(content_regex, i)
        extracted.append(content)
        
    #now that I have 'extracted' above, I need to fill the empty values with a placeholder of "empty value"
    #except "empty value" needs to be a list of a single item like this: ["empty value"] because the rest of them are
    filler = [["empty value"] if not sublist else sublist for sublist in extracted]

    #lastly, add all items from filler as items in a single list
    for sublist in filler:
        final_dates.extend(sublist)

        
    
# THIS IS ONLY FOR LIDL_UK. There is a weird comment that triggers an extra date to be found by the regular expression
final_dates.pop(163)
    
    
# put it all together in a pandas dataframe
# reviews_df = pd.DataFrame({
#     "Name": final_reviewer_names,
#     "Star Rating": final_star_ratings,
#     "Review Title": final_review_titles,
#     "Review Content": final_review_contents,
#     "Date": final_dates
#     })





