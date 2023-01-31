import requests
from bs4 import BeautifulSoup

website = "https://anitube.in.ua/?do=random_anime"


def get_anime_html():
    connect_anime = requests.get(website)
    anime_html = connect_anime.content.decode('utf-8')
    return anime_html


def get_anime_info(anime_html):
    soup = BeautifulSoup(anime_html, 'html.parser')
    anime_url = soup.find("link", rel="canonical")
    print(anime_url.get('href'))
    anime_title = soup.find("title").text.replace("аніме українською онлайн", "")
    print(anime_title)
    anime_description = soup.find("div", class_="story_c_text").find(class_="my-text").text
    anime_information = soup.find("div", class_="story_c_text").find_parent()
    anime_information.find("div", class_="story_c_text").decompose()
    print(anime_information.text.strip(), end='\n\n')
    print(anime_description)


if __name__ == '__main__':
    html = get_anime_html()
    get_anime_info(html)
