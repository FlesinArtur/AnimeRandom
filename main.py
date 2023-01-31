import requests
from bs4 import BeautifulSoup

website = "https://anitube.in.ua/?do=random_anime"


def get_anime_html():
    connect_anime = requests.get(website)
    anime_html = connect_anime.content.decode('utf-8')
    return anime_html


def get_anime_info(anime_html):
    soup = BeautifulSoup(anime_html, 'html.parser')
    anime_url = soup.find("link", rel="canonical").get('href').strip()
    anime_title = soup.find("title").text.replace("аніме українською онлайн", "").strip()
    anime_description = soup.find("div", class_="story_c_text").find(class_="my-text").text.strip()
    anime_information = soup.find("div", class_="story_c_text").find_parent()
    anime_information.find("div", class_="story_c_text").decompose()
    anime_information = anime_information.text.strip("\n").replace("\n\n", "\n")
    return {
        "url": anime_url,
        "title": anime_title,
        "information": anime_information,
        "description": anime_description
    }


def print_anime_info(info):
    print(f'Назва:\n{info["title"]}')
    print(f'Посилання:\n{info["url"]}')
    print(f'Інформація:\n{info["information"]}')
    print(f'Опис:\n{info["description"]}')


if __name__ == '__main__':
    html = get_anime_html()
    anime = get_anime_info(html)
    print_anime_info(anime)
