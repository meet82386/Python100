from bs4 import BeautifulSoup
import requests

data = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(data, "html.parser")

titles = soup.select(selector=".titleline a")
titles_name = [titles[i].string for i in range(len(titles)) if i % 2 == 0]
titles_link = [titles[i]['href'] for i in range(len(titles)) if i % 2 == 0]
upvotes = soup.select(selector=".score")
upvotes = [int(i.string.rstrip(" points")) for i in upvotes]

maxi_number = max(upvotes)
maxi_index = upvotes.index(maxi_number)
print("Highest Rated Blog: ")
print(titles_name[maxi_index])
print(titles_link[maxi_index])
print(upvotes[maxi_index])
