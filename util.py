import os
import json

filename = "words.json"

#read json
def read_json(filename):
    print ("read json")
    if not default_json_exists(filename):
        create_default_json(filename)
        print ("new json file created")
    jsonFile = open(filename, 'r')
    data = json.load(jsonFile)
    jsonFile.close()
    return data

#write json data
def write_json(data, filename):
    jsonFile = open(filename, 'w+')
    jsonFile.write(json.dumps(data))
    jsonFile.close()

#create default json
def create_default_json (filename):
    data = {}
    write_json (data, filename)

# default json exists
def default_json_exists (filename):
    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
        return False;
    return True;






