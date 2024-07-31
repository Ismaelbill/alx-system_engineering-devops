#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress. """

if __name__ == "__main__":

    import requests
    import sys

    urlUsers = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(sys.argv[1])
    rUsers = requests.get(urlUsers)
    urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(sys.argv[1])
    rTodos = requests.get(urlTodos)
    totalTasks = 0
    completedTasks = 0
    Tasks = ""
    for i in rTodos.json():
        if i['completed']:
            completedTasks += 1
            Tasks += "\t {}\n".format(i['title'])
        totalTasks += 1

    print("Employee {} is done with tasks({}/{}):\
          ".format(rUsers.json()['name'], completedTasks, totalTasks))
    print(Tasks, end='')
