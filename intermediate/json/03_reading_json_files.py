import json

# Open a text file in read mode
with open("data_in.json", "r") as f:
    # Load the content of the file (JSON text) into a Python dictionary
    data = json.load(f)

print("\n\n")
print(type(data))
print(data)

print("\n\n")
print(data.items())
