#!/usr/bin/python3
"""0-gather_data_from_an_API module"""

import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    to_do_list = requests.get(url + "todos", user_id).json()

    user_name = user.get("username")
    value = []

    for activity in to_do_list:
        task = {}
        if activity.get("userId") == int(user_id):
            task["task"] = activity.get("title")
            task["completed"] = activity.get("completed")
            task["username"] = user_name
            value.append(task)

    my_data = {user_id: value}
    with open("{}.json".format(user_id), mode="w") as file:
        json.dump(my_data, file)
