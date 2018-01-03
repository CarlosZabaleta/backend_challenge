import urllib2
from urllib import urlencode
import urlparse
import json


def get_url():
    url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1"
    params = {'page': 1}
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    print(urlparse.urlunparse(url_parts))


get_url()

# def show_pages(number):
#     json_obj = urllib2.urlopen(url)
#     data = json.load(json_obj)
#     for each in (data['menus']):
#         if "parent_id" in each:
#             print 'id-' + str(each["id"]), 'parent-' + str(each["parent_id"]), 'child' + str(each["child_ids"])
#         else:
#             print "id-" + str(each['id']), "child-" + str(each['child_ids'])


# x = 1
# while x < 5:
#     show_pages(str(x))
#     x = x + 1
