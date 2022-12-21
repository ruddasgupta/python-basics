import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    # Making a GET request
    r = requests.get('https://www.forbes.com/')

    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', class_='main-content main-content--universal-header')
    content = s.find_all('p')

    print(content)