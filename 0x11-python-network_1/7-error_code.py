#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get(argv[1])

    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
