import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

g_driver_path = r"..\..\..\Downloads\chromedriver.exe"
g_service = Service(g_driver_path)

google_browser = webdriver.Chrome(service=g_service)

google_browser.get(r"https://inventwithpython.com")

# try:
#
#     books_imgs = google_browser.find_elements(By.CLASS_NAME, "card-img-top")
#     if not books_imgs:
#         print("No images available.")
#     else:
#         print(f"Found {len(books_imgs)} images.")
#         print(books_imgs)
# except:
#     print("Unable to find an element with that class name.")
