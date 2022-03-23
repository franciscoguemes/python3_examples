import json

# Open a text file in read mode
with open("data_in.json", "r") as f:
    # Load the content of the file (JSON text) into a Python dictionary
    data = json.load(f)

print(type(data))
print(data)

# Define a list of new workers. The new_workers is a Python List of dictionaries therefore the booleans starts with
# uppercase.
new_workers = [
    {
        "id": 3,
        "name": "Carl",
        "age": 38,
        "full-time": True
    },
    {
        "id": 4,
        "name": "Donald",
        "age": 39,
        "full-time": True
    },
]
print("\n\n")
print(type(new_workers))
print(new_workers)

# Add the new_workers list to the list of workers from the JSON string. Technically is adding a List of Python
# dictionaries to a List of Python dictionaries. Note that we are adding a list to another list, therefore we need to
# use the method "extend" instead of the method "append"
data["workers"].extend(new_workers)

# Add other data to the dictionary besides workers. You are not forced to add the same kind of data,
# a Python dicitonary can have any kind of data
data['test'] = True
data['shift'] = "Morning"


# Write data into file. Note that the dump function serializes a Python dictionary into a JSON text file.
with open("data_out.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=False)

