import urllib2
from urllib import urlencode
import urlparse
import json
import timeit


# Author: Carlos Zabaleta
# Purpose: Resolve the Backend Intern Challenge and Extra Challenge - Summer 2018
# Language: Python


# Add changeble params to the URL

def get_url(num_page, id_number):
    url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json"
    params = {"id": id_number, "page": num_page}
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


# Request data from an specific URL

def request_data():
    global num_page, num_id
    while True:
        url = get_url(num_page, num_id)
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        for each in (data["menus"]):  # Take data from URL
            if "parent_id" in each:  # if the object has parent_id
                data_dict[str(each["id"])] = [each["parent_id"], each["child_ids"]]
            else:  # use "0" to difference between root_id and all the children
                data_dict[str(each["id"])] = ['0', each["child_ids"]]
            if data["pagination"]["total"] == each["id"]:  # Take total.pagination from each page as the limitation
                return data_dict
        num_page += 1


# Find all the children belonging to the id_root


def find_children(id_root):
    data_branch.append(id_root)  # Add the id_root in data_branch position [0]
    aux = []  # Auxiliary array to storage the children ids
    aux.extend(data_dict[id_root][1])  # Add the children of the id_root to aux array
    while len(aux) != 0:
        value = aux.pop(0)  # delete and save the first element of aux array in value
        if data_dict[str(value)][1] is not []:  # check if id "value" has children
            if value not in data_branch:  # check if id "value" is already in data_branch
                aux.extend(data_dict[str(value)][1])  # add children to aux array
        data_branch.append(value)  # add value to data_branch
    id_control.extend(data_branch)  # add data_branch to the id_control list
    return data_branch


def no_duplicates(list_du):
    return len(list_du) == len(set(list_du))


# Search between the elements until find the id_root


def find_id_root(data):
    # global id_control
    for key, value in data.iteritems():  # Return an iterator over the data's dictionary's (key, value)
        id = key  # save value
        if int(id) in id_control:  # to avoid repetition if an id as already in id_control
            continue  # continue with the next key
        id_parent = value[0] # save value
        while str(id_parent) != "0":  # Look for id_parent = 0 to get the id_root
            id = data[str(id)][0]
            id_parent = data[str(id)][0]  # id_parent breaks out of the loop
        data_branch = find_children(str(id))  # data_branch is a list with an id_root and all the id_root's children
        output(data_branch)  # send a data_array to generate the required output
        del data_branch[:]  # Delete the data_branch to use for the next branch


def output(data_branch):
    values_dict = {"root_id": data_branch[0], "children": data_branch[1:]}
    if no_duplicates(data_branch):  # Look for duplicates in the values_dict
        valid_menu_array.append(values_dict)
        output_dict["Valid_menus"] = valid_menu_array
    else:
        invalid_menu_array.append(values_dict)
        output_dict["Invalid_menus"] = invalid_menu_array


num_page = 1
num_id = 1  # posible inputs 1 or 2
id_control = []
data_dict = {}
data_branch = []
valid_menu_array = []
output_dict = {}
invalid_menu_array = []
data_dict = request_data()

# Stored elements from data are like {12,[9,[13,14]]}
# {id_root,[id_parent,[children]]}

find_id_root(data_dict)
print (output_dict)

print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
