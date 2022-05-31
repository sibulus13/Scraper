from bs4 import BeautifulSoup
import requests

link = f'https://www.genmp3.net/tracks.php?u=https%3A%2F%2Fsoundcloud.com%2Fmichael-huang-723382387%2Fsets%2Fall-likes&t=https%3A%2F%2Fsoundcloud.com%2Fmichael-huang-723382387%2Fsets%2Fall-likes'
fname = f'html.txt'
session = dryscrape.Session()
session.visit(link)
response = session.body()
r = requests.get(link)
soup = BeautifulSoup(response, 'html.parser')
# print(soup.encode("utf-8"))
with open(fname, "w", encoding="utf-8") as f:
    f.write(str(soup))
    
# for a_tag in soup.find_all('a', id=lambda x: x and x.startswith('mp3Down'), href=True):
#     print(a_tag)
#     print(a_tag['href'])