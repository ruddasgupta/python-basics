import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # Making a GET request
    r = requests.get('https://www.flipkart.com/')

    # check status code for response received
    # success code - 200
    print(r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Getting the title tag
    print(soup.title)

    # Getting the name of the tag
    print(soup.title.name)

    # Getting the name of parent tag
    print(soup.title.parent.name)