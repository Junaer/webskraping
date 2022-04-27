import requests
from bs4 import BeautifulSoup

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    title = article.find('a', class_='tm-article-snippet__title-link')
    href = f"https://habr.com{title.attrs.get('href')}"
    response = requests.get(href)
    response.raise_for_status()
    inner_text = response.text
    soup = BeautifulSoup(inner_text, features='html.parser')
    full_article = soup.find('article', class_='tm-page-article__content tm-page-article__content_inner')
    full_article_text = full_article.text
    for word in KEYWORDS:
        if word in full_article_text:
            time = full_article.find('time')
            title = full_article.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1')
            print(time.text)
            print(title.text)
            print(href)
            print('__________________________________________________')