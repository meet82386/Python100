from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text

soup = BeautifulSoup(data, "html.parser")
movies = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")
movies = [i.string for i in movies]
movies.reverse()

with open("movies.txt", "w") as file:
    for i in movies:
        file.write(i)
        file.write("\n")