import urllib2
import json


def show_pages(number):
    url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=" + number
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    for each in (data['menus']):
        if "parent_id" in each:
            print 'id-' + str(each["id"]), 'parent-' + str(each["parent_id"]), 'child' + str(each["child_ids"])
        else:
            print "id-" + str(each['id']), "child-" + str(each['child_ids'])


x = 1
while x < 5:
    show_pages(str(x))
    x = x + 1
