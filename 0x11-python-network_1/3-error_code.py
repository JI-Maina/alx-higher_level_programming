#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import urlopen, HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as response:
            resp = response.read().decode('utf-8')
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        print(resp)
