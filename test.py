import os
import json
import sys
inputvariable = os.environ['INPUT_STORE']
print(inputvariable)
print('Hello World!')

# Nested JSON data
nested_data = {
    'name': $argv[1],
    'age': $argv[2],
    'children': [
        {
            'name': argv[3],
            'age': argv[4]
        },
        {
            'name': argv[5],
            'age': argv[6]
        }
    ]
}

# Write nested JSON data to a file
with open('nested_data.json', 'w') as f:
    json.dump(nested_data, f)
