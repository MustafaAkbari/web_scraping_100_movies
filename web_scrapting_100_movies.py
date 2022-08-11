import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=WEBSITE_URL)
website = response.text
soap = BeautifulSoup(website, "html.parser")
movie_title = soap.find_all(name="h3", class_="title")
movie_list = [movie.string for movie in movie_title]
reverse_movie_list = movie_list[::-1]
for movie in reverse_movie_list:
    print(movie)
    with open("top_100_movies.txt", "a", encoding="utf8") as movie_data:
        movie_data.write(f"{movie}\n")
