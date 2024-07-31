#!/usr/bin/python3
""" extending Python script file 0 to export data in the CSV forma"""

if __name__ == "__main__":

    import requests
    import sys

    urlUsers = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(sys.argv[1])
    rUsers = requests.get(urlUsers)
    urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(sys.argv[1])
    rTodos = requests.get(urlTodos)

    with open("{}.csv".format(sys.argv[1]), 'a') as f:
        for i in rTodos.json():
            f.write('"{}","{}","{}","{}"\n'
                    .format(sys.argv[1], rUsers.json()['username'],
                            i['completed'], i['title']))
