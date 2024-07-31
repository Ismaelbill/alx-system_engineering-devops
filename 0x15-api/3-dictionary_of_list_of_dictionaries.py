#!/usr/bin/python3
""" extending Python script file 0 to export data in the json forma"""

if __name__ == "__main__":

    import requests
    import sys

    urlUsers = "https://jsonplaceholder.typicode.com/users/"
    rUsers = requests.get(urlUsers)
    lengthUsers = len(rUsers.json())
    minusLengthUsers = lengthUsers - 1
    count = 1
    with open("todo_all_employees.json", "w") as f:
        f.write("{")
        for i in rUsers.json():
            urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(i['id'])
            rTodos = requests.get(urlTodos)
            f.write('"{}": '.format(i['id']))
            f.write('[')
            check = False
            for j in rTodos.json():
                if check:
                    f.write('}, ')
                check = True
                bool = str(j['completed']).lower()
                f.write('{{"username": "{}", "task": "{}", "completed": {}'
                        .format(i['username'], j['title'], bool))
            f.write("}]")
            count += 1
            if minusLengthUsers > count:
                f.write(", ")

        f.write("}")
