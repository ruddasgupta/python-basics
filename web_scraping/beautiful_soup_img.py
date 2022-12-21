import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # Making a GET request
    r = requests.get('https://www.flipkart.com/')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    images_list = []

    images = soup.select('img')
    for image in images:
        src = image.get('src')
        alt = image.get('alt')
        images_list.append({"src": src, "alt": alt})

    for image in images_list:
        print(image)