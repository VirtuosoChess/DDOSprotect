import requests

def make_request(method, url, data):
    if method == "POST":
        response = requests.post(url, json=data)
    elif method == "GET":
        response = requests.get(url, params=data)
    else:
        raise ValueError("Unsupported HTTP method.")
    return response
