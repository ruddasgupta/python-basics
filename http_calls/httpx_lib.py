import httpx

if __name__ == '__main__':
    url = "https://my-json-server.typicode.com/typicode/demo/posts"

    payload={}
    headers = {}

    response = httpx.request("GET", url, headers=headers, data=payload)

    print(response.text)
