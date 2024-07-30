#!/usr/bin/python3
"""0-gather_data_from_an_API module"""

import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    to_do_list = requests.get(url + "todos").json()

    all_users_ids = []
    for activity in to_do_list:
        if activity.get("userId") not in all_users_ids:
            all_users_ids.append(activity.get("userId"))
    my_data = {}
    for i in range(len(all_users_ids)):
        user_id = all_users_ids[i]
        user = requests.get(url + "users/{}".format(user_id)).json()

        user_name = user.get("username")
        value = []

        for activity in to_do_list:
            task = {}
            if activity.get("userId") == int(user_id):
                task["username"] = user_name
                task["task"] = activity.get("title")
                task["completed"] = activity.get("completed")
                value.append(task)
        my_data[user_id] = value

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(my_data, file)
