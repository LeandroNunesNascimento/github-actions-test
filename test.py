import os
import json
import sys
inputvariable = os.environ['INPUT_STORE']
print(inputvariable)
print('Hello World!')

# Nested JSON data
nested_data = {
    'name': 'luis',
    'age': 30,
    'children': [
        {
            'name': 'Alice',
            'age': 5
        }
        {
            'name': 'Bob',
            'age': 7
        }
    ]
}


# Write nested JSON data to a file
with open('nested_data.json', 'w') as f:
    json.dump(nested_data, f)
