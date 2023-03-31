#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using urllib package
"""

if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()

    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content", data)

    body = data.decode('utf8')
    print("\t- utf8 content", body)
