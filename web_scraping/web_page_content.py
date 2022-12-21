import requests

if __name__ == '__main__':
    # Making a GET request
    r = requests.get('https://www.flipkart.com/')

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    print(r.content)

    # print url code
    print(r.url)

    # print status code
    print(r.status_code)