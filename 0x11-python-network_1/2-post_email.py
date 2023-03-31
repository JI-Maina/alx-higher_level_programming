#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    data = f"email={argv[2]}".encode('utf-8')

    with urlopen(argv[1], data) as response:
        resp = response.read().decode('utf-8')

    print(resp)
