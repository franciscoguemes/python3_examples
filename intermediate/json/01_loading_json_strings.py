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

# Print the first worker
print("\n\n")
print(data["workers"][0])

# Modify properties from the first worker
data["workers"][0]["age"] = 46
data["workers"][0]["full-time"] = False

print("\n\n")
print(data["workers"][0])
