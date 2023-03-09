import httplib2
import json


if __name__ == '__main__':
    url = "https://my-json-server.typicode.com/typicode/demo/posts"

    payload={}
    headers = {}

    http = httplib2.Http()
    response = http.request(url)
    json_response = json.loads(response[1])

    print(json_response)
