import urllib2
from urllib import urlencode
import urlparse
import json

# Add the page param to the URL


def get_url(num_page):
    url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2"
    params = {'page': num_page}
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)

# Request data from an especific URL


dic_fin = {}


def request_data():
    num_page = 1
    while True:
        url = get_url(num_page)
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        for each in (data['menus']):
            if "parent_id" in each:
                print 'id-' + str(each["id"]), 'child' + str(each["child_ids"])
            else:
                print "id-" + str(each['id']), "child-" + str(each['child_ids'])
            if data['pagination']['total'] == each["id"]:
                print (data['pagination']['total'])
                return num_page

        num_page += 1


print request_data()
