#!/usr/bin/python3
"""1 - export to csv module"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    to_do_list = requests.get(url + "todos", user_id).json()

    my_data = []
    for activity in to_do_list:
        if activity.get("userId") == int(user_id):
            data = []
            data.append(activity.get("userId"))
            data.append(user_name)
            data.append(activity.get("completed"))
            data.append(activity.get("title"))
            my_data.append(data)

    with open("{}.csv".format(user_id), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(my_data)
