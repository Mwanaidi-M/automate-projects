"""
Project: Removing the Header from CSV Files

Say you have the boring job of removing the first line from several hundred CSV files. You could
open each file in Excel, delete the first row, and resave the file—but that would take hours.

To create a program for this task you will need to open every file with the .csv extension in any
given directory, read in the contents of the CSV file, and rewrite the contents without
the first row to a file of the same name. This will replace the old contents of the CSV file with
the new, headless contents.

At a high level, the program must do the following:
• Find all the CSV files in any given directory from the command-line.
• Read in the full contents of each file.
• Write out the contents, skipping the first line, to a new CSV file in a different directory.

At the code level, this means the program will need to do the following:
• Loop over a list of files from os.listdir(), skipping the non-CSV files.
• Create a CSV Reader object and read in the contents of the file, use the line_num attribute
    to figure out which line to skip.
• Create a CSV Writer object and write out the read-in data to the new file.
"""

import csv
import os
import sys
import time

# get the directory path given by user in a try-except clause to catch any issues such as, not passing
# a directory or passing an incorrect path
try:
    user_dir_path = sys.argv[1]

# display a message if there is an error/issue
except Exception as exc:
    # print(sys.exc_info()[:2])
    print("Oops no directory given.")

# carry out process if there is no error/issue
else:
    # print(user_dir_path)
    # print(os.listdir(user_dir_path))

    # create a directory to hold the csv files with headers removed
    removed_headers = os.path.join(user_dir_path, "removed-headers")
    os.makedirs(removed_headers, exist_ok=True)

    # print(os.path.abspath(user_dir_path))

    # loop through the given directory path
    for file in os.listdir(os.path.abspath(user_dir_path)):
        # create an empty list to hold the csv rows
        content_rows = []

        # check if the file has a .csv extension
        if file.endswith(".csv"):
            # open the file in read mode, create a Reader object, loop through the object,
            # skip the first row line and append the rest to the list
            with open(os.path.join(user_dir_path, file)) as file_csv:
                file_reader = csv.reader(file_csv)

                for row in file_reader:
                    if file_reader.line_num != 1:
                        content_rows.append(row)

            print(f"Removing header from: {os.path.join(user_dir_path, file)}...")

            # delay the response message by 2 secs (just for fun)
            time.sleep(2)
            # open the file in the new directory in "w" mode & add newline kwarg,
            # create a Writer object, loop through the list and write to the file.
            with open(os.path.join(removed_headers, file), "w", newline="") as new_csv:
                new_writer = csv.writer(new_csv)

                for row in content_rows:
                    new_writer.writerow(row)

            print(f"Done removing header.")

