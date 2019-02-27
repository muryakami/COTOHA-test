import requests
import re
import urllib.request as urlreq
from bs4 import BeautifulSoup
from pprint import PrettyPrinter

linkData = []

pp = PrettyPrinter(indent=4)

# query = "怒っている"

# r = urlreq.Request(
#     'https://irasutoya-sear.ch/')
# r = urlreq.Request("https://www.yahoo.co.jp/")
# with urlreq.urlopen(r) as r:
#     r = r.read()
# pp.pprint(r)
# print("\n\n")
# soup = BeautifulSoup(r, 'lxml')
# pp.pprint(soup)
# print("\n\n")

# r = requests.get('https://irasutoya-sear.ch/')
r = requests.get("https://www.yahoo.co.jp/")
pp.pprint(r.text)
print("\n\n")
soup = BeautifulSoup(r.text, 'lxml')
pp.pprint(soup)
print("\n\n")

links = soup.select("a[href]")
# pp.pprint(links)
# print("\n\n")
for a in links:
    href = a.attrs['href']
    if re.search('irasutoya.*blog-post.*html$', href):
        if not href in linkData:
            linkData.append(href)
            print(href)
    # if re.search('max-results=20&start=20&by-date=false$', href):
    #     r = href
    #     break

# for link in linkData:
#     res = requests.get(link)
#     soup = BeautifulSoup(res.text, "lxml")
#     links = soup.select(".separator > a")
#     for a in links:
#         imageLink = a.get('href')
#         filename = re.search(".*\/(.*png|.*jpg)$", imageLink)
#         try:
#             urlreq.urlretrieve(
#                 imageLink, "../pictures/test/"+filename.group(1))
#             print(imageLink)
#         except ValueError:
#             print("ValueError!")
