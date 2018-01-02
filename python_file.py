import urllib2
import json

url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1"

json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

for each in (data['menus']):
    print(str(each["id"]) + " " + str(each["child_ids"]))
