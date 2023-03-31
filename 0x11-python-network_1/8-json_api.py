#!/usr/bin/python3
"""takes in a letter and sends a POST request to http://0.0.0.0:5000/search_
user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    let = {'q': ""}

    if len(argv) <= 1:
        print("No result")
    else:
        let['q'] = argv[1]

        resp = requests.post('http://0.0.0.0:5000/search_user', data=let)

        data = resp.json()

        if data:
            print(f"{[data['id']]} {data['name']}")
        elif data == "":
            print("Not a valid JSON")
        else:
            print("No result")
