import json

# Note that the json string contains and object with an array of objects inside.
# each of the objects hold different attributes that are of type number, string or boolean.
# In JSON format the attributes and the values must be surrounded by double quotes.
json_string = '''
{
    "workers": [
        {
            "id": 1,
            "name": "John",
            "age": 45,
            "full-time": true
        },   
        {
            "id": 2,
            "name": "Mathew",
            "age": 25,
            "full-time": false
        } 
    ]
}
'''

# Note that the method's name is "loads" because we are loading form a string that contains JSON to a Python dictionary.
data = json.loads(json_string)
print(type(data))
print(data)

# Define a new worker. The new_worker is a Python dictionary therefore the boolean starts with uppercase.
new_worker = {
    "id": 3,
    "name": "Carl",
    "age": 38,
    "full-time": True
}
print("\n\n")
print(type(new_worker))
print(new_worker)

# Add the new_worker to the list of workers from the JSON string. Technically is adding a Python dictionary
# to a List of Python dictionaries.
data["workers"].append(new_worker)

# Add other data to the dictionary besides workers. You are not forced to add the same kind of data,
# a Python dicitonary can have any kind of data
data['test'] = True
data['shift'] = "Night"

# Deserialize (tranform) the Python dictionary into a JSON string, indenting the elements 4 spaces and sorting the
# keys of the dictionary
new_json_string = json.dumps(data, indent=4, sort_keys=True)
print("\n\n")
print(type(new_json_string))
print(new_json_string)




