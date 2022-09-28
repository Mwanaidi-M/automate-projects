# import the csv module
import csv

# To read data from a CSV file with the csv module, you need to create a Reader
# object which lets you iterate over lines in the CSV file.
# open the csv file first,
with open("sample-csv.csv") as sample_csv:
    # create the Reader object by passing the file
    sample_reader = csv.reader(sample_csv)

    # most direct way to access the values in the Reader object is to convert
    # it to a plain list by passing it to list()
    sample_list = list(sample_reader)

# checking the length of the list
# print(len(sample_list))

# printing the list
# print(sample_list)

# accessing the value at a particular row and column with the expression
# print(sample_list[0][1])

# opening a large csv file,
with open("unique-pass.csv") as unique_csv:
    # creating the reader
    unique_reader = csv.reader(unique_csv)

    # loop through the data, to get the row number, use the Reader object’s line_num
    # variable, which contains the number of the current line.
    for row in unique_reader:
        # print(f"Row #{unique_reader.line_num}: {row}")
        pass

content_random = [
    ['eggs', 'Hello', 23],
    ['macon', 'Ola', 22],
    ['chicken', 'Wello, Horld!', 12]
]


# to write objects to a csv file, create a Writer object, On Windows, you’ll also need to pass a blank
# string for the open() function’s newline kwarg or else the rows created will be double-spaced.
with open("random.csv", "w", newline="") as random_csv:
    random_writer = csv.writer(random_csv)

    # The writerow() method for Writer objects takes a list argument.
    # The return value of writerow() is the number of characters written to the file
    # for that row (including newline characters).
    for content in content_random:
        random_writer.writerow(content)

