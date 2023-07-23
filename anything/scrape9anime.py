import requests
from bs4 import BeautifulSoup

url = "https://9animetv.to"
home_url = url + "/home"

response = requests.get(home_url)
contents = BeautifulSoup(response.text, "html.parser")

latest_anime = contents.find_all("div", class_="flw-item item-qtip")
recently_updated = {}
counter = 0
for anime in latest_anime:
    counter = counter + 1
    recently_updated["id"] = counter
    file_poster = anime.find("div", class_="film-poster")
    file_detail = anime.find("div", class_="film-detail")

    name = file_detail.find("h3", class_="film-name")
    recently_updated["name"] = name.text.strip()

    link = name.find("a", class_="dynamic-name")
    recently_updated["link"] = url + link['href'].strip()

    quality = file_poster.find("div", class_="tick-item tick-quality")
    recently_updated["quality"] = quality.text.strip()

    sub_or_dub = file_poster.find("div", class_="tick ltr")
    recently_updated["translation"] = sub_or_dub.text.strip()

    episodes = file_poster.find("div", class_="tick rtl")
    recently_updated["episode"] = episodes.text.strip()
    print()
    print(recently_updated)
