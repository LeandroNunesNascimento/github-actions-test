import os
import json
import sys
inputvariable = os.environ['INPUT_STORE']
print(inputvariable)
print('Hello World!')


# Nested JSON data
nested_data = {
    'name': sys.argv[1],
    'age': sys.argv[2],
    'children': [
        {
            'name': sys.argv[3],
            'age': sys.argv[4]
        },
        {
            'name': sys.argv[5],
            'age': sys.argv[6]
        }
    ]
}

# Write nested JSON data to a file
with open('nested_data.json', 'w') as f:
    json.dump(nested_data, f)

# Output:
# This will create a file named 'nested_data.json' and write the nested JSON data into it.
