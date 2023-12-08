import json

# initialising json object
ini_string = {'nikhil': 1, 'akash' : 5,
			'manjeet' : 10, 'akshat' : 15}

# printing initial json
ini_string = json.dumps(ini_string)
print ("initial 1st dictionary", ini_string)
print ("type of ini_object", type(ini_string))

# converting string to json
final_dictionary = json.loads(ini_string)

# printing final result
print ("final dictionary", str(final_dictionary))
print ("type of final_dictionary", type(final_dictionary))
