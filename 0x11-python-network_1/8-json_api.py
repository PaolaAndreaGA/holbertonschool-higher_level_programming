#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    q=""
    if len(argv) >= 2:
        q = argv[1]
    data = {'q': q}
    try:
        req: requests.post(url, data)
        json = req.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except:
                print("Not a valid JSON")
