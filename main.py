import requests
from bs4 import BeautifulSoup


req = requests.get("https://www.globo.com/")
req.encoding = "utf-8"

if req.status_code == 200:
    print('Requisição bem sucedida!')

soup = BeautifulSoup(req.text, 'html.parser')

posts = soup.find_all(class_='post')

all_post = []

for post in posts:
    titulo = post.find(class_="hui-premium__link")
    #title = info.find("title")
    #preview = info.p.text
    #author = info.find(class_="post-author").text
    #time = info.find(class_="post-date")['datetime']
    all_post.append(
        {'titulo': titulo

         #'preview': preview,
         #'author': author,
         #'time': time
         })

    print(all_post)
