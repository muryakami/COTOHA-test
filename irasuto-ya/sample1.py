import sys
import os
import re
import urllib.request as urlreq
from bs4 import BeautifulSoup
import requests

# 一時的に保存するページのリスト
linkData = []

if len(sys.argv) != 3:
    print("Usage: python.exe irasutoya_down.py <SearchWord> <max num>")
    quit()

keyword = sys.argv[1]
max = int(sys.argv[2])

# 検索結果から各ページのリンク先をmaxページ分だけ取得
for num in range(0, max, 20):
    res = requests.get("http://www.irasutoya.com/search?q=" +
                       keyword+"&max-results=20&start="+str(num))
    soup = BeautifulSoup(res.text, "lxml")

    # Linkの箇所をselect
    links = soup.select("a[href]")
    for a in links:
        # Linkタグのhref属性の箇所を抜き出す
        href = a.attrs['href']
        # 画像データに対応するページのリンク先のみをリストに格納
        if re.search(r"irasutoya.*blog-post.*html$", href):
            if not href in linkData:
                linkData.append(href)

# 各ページから画像データのリンクを取得して、画像を保存
for link in linkData:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "lxml")

    # 記事中の画像データを抜き出す
    # class separator -> a の抜き出し
    links = soup.select(".separator > a")
    for a in links:
        # hrefのデータを取得
        imageLink = a.get('href')
        # ファイル名の取得
        filename = re.search(r".*\/(.*png|.*jpg)$", imageLink)
        # 画像をダウンロードする
        urlreq.urlretrieve(imageLink, "down/"+filename.group(1))
        # デバッグ用にダウンロード先Linkを表示
        print(imageLink)
