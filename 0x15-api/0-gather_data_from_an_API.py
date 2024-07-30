#!/usr/bin/python3
"""0-gather_data_from_an_API module"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    uer = requests.get(url + "users/{}".format(user_id)).json()
    to_do_list = requests.get(url + "todos", user_id).json()

    done_task_count = 0
    total_tasks = 0

    for activity in to_do_list:
        if activity.get("userId") == int(user_id):
            if activity.get("completed") is True:
                done_task_count += 1
            total_tasks += 1

    count = "{}/{}".format(done_task_count, total_tasks)
    print("Employee {} is done with tasks({}):".format(uer.get("name"), count))

    for activity in to_do_list:
        user_id_match = int(user_id) == activity.get("userId")
        completed = activity.get("completed") is True
        if user_id_match and completed:
            print("\t ", activity.get("title"))
