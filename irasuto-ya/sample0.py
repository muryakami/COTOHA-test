import requests
import re
import urllib.request as urlreq
from bs4 import BeautifulSoup
from pprint import PrettyPrinter

pages = range(1, 6)
linkData = []

pp = PrettyPrinter(indent=4)

for p in pages:
    if p == 1:
        r = urlreq.Request(
            'https://www.irasutoya.com/search/label/%E8%81%B7%E6%A5%AD')
        with urlreq.urlopen(r) as r:
            r = r.read()
        # pp.pprint(r)
        # print("\n\n")
        soup = BeautifulSoup(r, 'lxml')
        pp.pprint(soup)
        print("\n\n")
        links = soup.select("a[href]")
        # for a in links:
        #     href = a.attrs['href']
        #     if re.search('irasutoya.*blog-post.*html$', href):
        #         if not href in linkData:
        #             linkData.append(href)
        #             print(href)
        #     if re.search('max-results=20&start=20&by-date=false$', href):
        #         r = href
        #         break
        # for link in linkData:
        #     res = requests.get(link)
        #     soup = BeautifulSoup(res.text, "lxml")
        #     links = soup.select(".separator > a")
        #     for a in links:
        #         imageLink = a.get('href')
        #         filename = re.search(".*\/(.*png|.*jpg)$", imageLink)
        #         try:
        #             urlreq.urlretrieve(
        #                 imageLink, "../pictures/"+filename.group(1))
        #             print(imageLink)
        #         except ValueError:
        #             print("ValueError!")
    else:
        r = urlreq.Request(r)
        # with urlreq.urlopen(r) as r:
        #     r = r.read()
        # soup = BeautifulSoup(r, 'lxml')
        # links = soup.select("a[href]")
        # for a in links:
        #     href = a.attrs['href']
        #     if re.search('irasutoya.*blog-post.*html$', href):
        #         if not href in linkData:
        #             linkData.append(href)
        #             print(href)
        #     if re.search('max-results=20&start='+str(p*20)+'&by-date=false$', href):
        #         r = href
        #         break
        # for link in linkData:
        #     res = requests.get(link)
        #     soup = BeautifulSoup(res.text, "lxml")
        #     links = soup.select(".separator > a")
        #     for a in links:
        #         imageLink = a.get('href')
        #         filename = re.search(".*\/(.*png|.*jpg)$", imageLink)
        #         try:
        #             urlreq.urlretrieve(
        #                 imageLink, "../pictures/"+filename.group(1))
        #             print(imageLink)
        #         except ValueError:
        #             print("ValueError!")
