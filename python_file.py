import urllib2
from urllib import urlencode
import urlparse
import json
import timeit
# Add changeble params to the URL

def get_url(num_page,id_number):
    url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json"
    params = {"id": id_number,"page": num_page}
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)

# Request data from an specific URL

def request_data():
    global num_page, num_id
    while True:
        url = get_url(num_page,num_id)
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        for each in (data["menus"]): # Take data from URL
            if "parent_id" in each: # if the object has parent_id
                dic_fin[str(each["id"])] = [each["parent_id"], each["child_ids"]]
            else: # use "0" to difference between root_id and all the children
                dic_fin[str(each["id"])] = ['0', each["child_ids"]]
            if data["pagination"]["total"] == each["id"]: # Take total.pagination from each page as the limitation
                return dic_fin
        num_page += 1

# Find all the children belonging to the id_root


def find_children(id_root):
    # if id_root not in id_list: #
        id_list.append(int(id_root))
        aux = []
        aux.extend(dic_fin[id_root][1])
        while len(aux)!= 0:
            value = aux.pop(0)
            if dic_fin[str(value)][1] != []:
                if value not in id_list:
                    aux.extend(dic_fin[str(value)][1])
            id_list.append(value)
        total_ids.extend(id_list)
        return id_list
    # print "xxxx"

def no_duplicates (lista_du):
    return len(lista_du) == len(set(lista_du))

#Search between the elements until find the id_root


def find_id_root(data):
    # global total_ids
    for key, value in data.iteritems(): # Return an iterator over the data's dictionary's (key, value)
        id = key
        if int(id) in total_ids:
            continue
        id_parent = value[0]
        while str(id_parent) != "0": # Look for id_parent = 0 to get the id_root
            id = data[str(id)][0]
            id_parent = data[str(id)][0] # id_parent breaks out of the loop
        data_branch = find_children(str(id)) # data_branch is a list with an id_root and all the id_root's children
        output(data_branch)
        del data_branch[:] # Delete the data_branch to use for the next branch


def output(lista):
    global boom1, boom, boombo
    first = {"root_id":lista[0], "children":lista[1:]}
    if no_duplicates(lista):
        boom.append(first)
        boombo["Valid_menus"] = boom
    else:
        boom1.append(first)
        boombo["Invalid_menus"] = boom1

num_page = 1
num_id = 1 #posible inputs 1 or 2
total_ids = []
dic_fin = {}
id_list = []
boom = []
boombo = {}
boom1 = []
dic_fin = request_data()

#Stored elements from data are like {12,[9,[13,14]]}
#{id_root,[id_parent,[children]]}

final = find_id_root(dic_fin)
print (boombo)

print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)