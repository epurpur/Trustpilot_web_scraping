

"""this file is a compilation of URLS in order to keep the Truspilot_webscrape.py file cleaner"""

def imperfect_foods():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #13 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,14)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/imperfectfoods.com?page={i}")

    return url_list



def misfits_market():
    """ Creates list of url strings for each page of reviews"""
    
    url_list = []
    
    # 39 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1, 40)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/www.misfitsmarket.com?page={i}")
    
    return url_list




def hungry_harvest():
    
    return ["https://www.trustpilot.com/review/www.hungryharvest.net"]



def grocery_outlet():
    
    return ["https://www.trustpilot.com/review/www.groceryoutlet.com"]



def oddbox():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #750 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,751)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/www.oddbox.co.uk?page={i}")

    return url_list



def earth_and_wheat():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #35 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,36)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/earthandwheat.com?page={i}")

    return url_list



def motatos_uk():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #122 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,123)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/motatos.co.uk?page={i}")

    return url_list

    
    
def odd_coffee_co():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #107 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,108)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/oddcoffeeco.com?page={i}")

    return url_list



def wonky_veg_boxes():
    """ Creates list of url strings for each page of reviews"""

    return ["https://www.trustpilot.com/review/www.wonkyvegboxes.co.uk"]



def morrisons():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #387 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,388)]
    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/morrisons.com?page={i}")

    return url_list



def lidl_uk():
    """ Creates list of url strings for each page of reviews"""

    url_list = []
    
    #184 pages of reviews at the time of data collection
    page_number_list = [num for num in range(1,185)]

    
    for i in page_number_list:
        url_list.append(f"https://www.trustpilot.com/review/www.lidl.co.uk?page={i}")
 
    return url_list

