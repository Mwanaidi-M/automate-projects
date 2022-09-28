"""
This project is meant to showcase how to work with the requests, beautifulSoup and webbrowser modules.
The program is supposed to Open all the product pages or a number of product pages after searching a shopping
site such as Etsy. It will:
• Get product search keywords from the command line arguments.
• Retrieve the search results page.
• Opens a browser tab for each result.
"""

# get all modules
import requests, sys, bs4, webbrowser

# search url for etsy
etsy_search_url = r"https://www.etsy.com/search?q="

# search keywords
search_kw = ' '.join(sys.argv[1:])

# full product search url
product_search_url = etsy_search_url + search_kw

try:
    # request the page
    res_obj = requests.get(product_search_url)
    res_obj.raise_for_status()

# display error message in case of an issue
except Exception as exc:
    print(f"Oops! {exc}")

# if no errors are present get a list of the product page links
else:
    # get the HTML version of the page
    content_soup = bs4.BeautifulSoup(res_obj.text, features="html.parser")

    # generate a list made up of 'a' tag elements with the links
    prod_links = content_soup.select(".listing-link")

    # checked the length of the list
    # print(len(prod_links))

    # number of tabs we want to open
    num_tabs = min(5, len(prod_links))

    # loop through the range given and open a tab for each link using the href attribute
    for num in range(num_tabs):
        webbrowser.open(prod_links[num].get('href'))

# print(product_search_url)
