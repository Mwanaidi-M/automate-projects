"""
PROJECT: Image Site Downloader
The program is meant to go to a photo-sharing site like Pixel or Unsplash,
searches for a category of photos, and then downloads at least 10 of the resulting
images to a folder.

Program steps:
- Get the site url
- Get the category to search for from the commandline argv
- Request an image search page for the given category
- Get the images' css selector from the search to get the src of the images
- save them to a list
- create a folder to hold the images
- download the images to the folder
"""

import os
import random
import sys

import bs4
import requests

# unsplash image search site url
unsplash_url = r"https://unsplash.com/s/photos/"

# get search category from command line
search_category = '-'.join(sys.argv[1:])

# directory to hold the images - unsplash<search_category>
os.makedirs(f"unsplash-{search_category}", exist_ok=True)

# absolute path of the directory created
img_dir_path = os.path.abspath(f"unsplash-{search_category}")

# print(img_dir_path)

# complete url of the image search
full_url = unsplash_url + search_category

# print full url to check if it's okay
# print(full_url)

# make request for the url
try:
    res_obj = requests.get(full_url)
    res_obj.raise_for_status()

# display error message if there is an error
except Exception as exc:
    print(f"Opps! There was a problem: {exc}")

# if all is okay, proceed with further work
else:
    # print(res_obj.status_code)
    # get the html content of the response
    content_soup = bs4.BeautifulSoup(res_obj.text, "html.parser")

    # get the images with the given css selector
    imgElement = content_soup.select("div>.YVj9w")

    # if resultset is empty, notify user
    if not imgElement:
        print("No images found with that class.")
    # else, loop through each element, using the image src attribute to download
    # the image to the directory created above.
    else:
        # print(len(imgElement))

        # get 10 random images from the imgElement resultset (want to download 10 images only)
        dwnld_imgs = random.sample(imgElement, 10)

        # setting a minimum of images to download i.e. 10 images for a start
        for imgs in range(len(dwnld_imgs)):

            # Get the img src which has the url first
            imgUrl = imgElement[imgs].get("src")

            # get the img title tag or alt tag (depending on which tag the img has) text with
            # img description; which will be used as the img file name using the first 2 words
            if imgElement[imgs].get("alt") is None:
                imgName = '-'.join(imgElement[imgs].get("title").split(' ')[:2])
            else:
                imgName = '-'.join(imgElement[imgs].get("alt").split(' ')[:2])

            # print the img name to test
            # print(imgAltName)

            # inform user which image is bein downloaded
            print(f"Downloading image: {imgUrl}")

            # download the img from url
            try:
                img_response = requests.get(imgUrl)
                img_response.raise_for_status()

            # if there is an issue downloading the img, notify user
            except Exception as img_exc:
                print(f"There was an issue: {img_exc}")

            else:
                # save the image to the directory created for that category by
                # creating the file(joined the abs img dir path with the img alt name created
                # and opening it in 'wb' mode, loop through the request response.iter_content
                # and write the chunk into the file object
                with open(f"{os.path.join(img_dir_path,imgName)}.png", "wb") as new_img:
                    for chunk in img_response.iter_content():
                        new_img.write(chunk)

                # print this image once that img download is completed
                print("Download complete.")
