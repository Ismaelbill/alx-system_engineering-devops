#!/usr/bin/python3
""" extending Python script file 0 to export data in the json forma"""

if __name__ == "__main__":

    import requests
    import sys

    urlUsers = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(sys.argv[1])
    rUsers = requests.get(urlUsers)
    urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(sys.argv[1])
    rTodos = requests.get(urlTodos)
    check = False
    with open("{}.json".format(sys.argv[1]), 'a') as f:
        f.write('{{"{}": ['.format(sys.argv[1]))
        for i in rTodos.json():
            if check:
                f.write(", ")
            check = True
            f.write('{{"task": "{}", "completed": {}, "username": "{}"}}'
                .format(i['title'], str(i['completed']).lower(), rUsers.json()['username']))
        f.write(']}')
