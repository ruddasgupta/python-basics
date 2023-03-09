import requests


if __name__ == '__main__':
    url = "https://my-json-server.typicode.com/typicode/demo/posts"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
