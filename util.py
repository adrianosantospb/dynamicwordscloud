import os
import json

filename = "words.json"

#read json
def read_json():
    if not default_json_exists(filename):
        create_default_json(filename)
        print ("new json file created")
    jsonFile = open(filename, 'r')
    data = json.load(jsonFile)
    jsonFile.close()
    return data

#write json data
def write_json(data):
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

# return index
def word_exists (data, word):
    for i in range (len(data["words"])):
        if data["words"][i]["word"] == word:
            return i
    return -1

def add_word (words):
    d = read_json()
    for pos in range(len(words)):
        wrd = words[pos]
        indx = word_exists(d, wrd)
        if indx > -1:
            d["words"][indx]["repetitions"] = int(d["words"][indx]["repetitions"]) + 1
        else:
            d["words"].append({"word": wrd, "repetitions": 1})
    write_json(d)


def save_updates (json_data):
    final = '{"words" :' + json_data + '}'
    j = json.loads(final)
    for pos in range(len(j["words"])):
        j["words"][pos]["repetitions"]=int(j["words"][pos]["repetitions"])
    write_json(j)

