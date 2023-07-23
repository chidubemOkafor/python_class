import requests
from bs4 import BeautifulSoup

url = "https://goku.sx"
response = requests.get(url + "/home")

content = BeautifulSoup(response.text, "html.parser")


home_movies = content.find("div", class_="section-items section-items-default")
trending = home_movies.find_all("div", class_="item")

trending_movies_dictionary = {}
for trending_movies in trending:
    movie_info = trending_movies.find("div", class_="movie-info")
    info_split = movie_info.find("div", class_="info-split")
    div = info_split.find_all("div")
    movie_link = movie_info.find("a", class_="movie-link")

    print()
    trending_movies_dictionary["title"] = movie_link.text.strip()
    trending_movies_dictionary["year"] = div[0].text
    trending_movies_dictionary["duration"] = div[2].text
    trending_movies_dictionary["link"] = url + movie_link["href"]
    print()

    print(trending_movies_dictionary)
