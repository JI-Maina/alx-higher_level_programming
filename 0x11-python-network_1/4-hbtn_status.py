#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using requests package
"""

if __name__ == "__main__":
    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')

    r = resp.text

    print("Body response:")
    print("\t- type: ", type(r))
    print("\t- content: ", r)
