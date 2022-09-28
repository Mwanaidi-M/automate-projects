# import the module
import json

# READING JSON DATA
# open the json file
with open("example_2.json") as example_json:
    # calling load() and pass it the json file object
    example_data = json.load(example_json)

# print(example_data)

string_of_json = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
# calling loads() and pass it the json file object
string_data = json.loads(string_of_json)

# print(string_data)

# WRITING JSON
data_py = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
        {
            "batter":
                [
                    {"id": "1001", "type": "Regular"},
                    {"id": "1002", "type": "Chocolate"},
                    {"id": "1003", "type": "Blueberry"},
                    {"id": "1004", "type": "Devil's Food"}
                ]
        },
    "topping":
        [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"}
        ]
}

# json.dumps() function (which means “dump string,”) will translate a Python value into a string
# of JSON-formatted data.
data_as_json = json.dumps(data_py)

print(data_as_json)

# json.dump() will write the python value to a file, you need to open a json file in "w" mode,
# pass the file object and the python value to the function.
with open("donut.json", "w") as donut_json:
    json.dump(data_py, donut_json)

