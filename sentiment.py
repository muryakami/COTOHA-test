# -*- coding: utf-8 -*-

import os
import json
import configparser
import codecs
from cotoha_api import CotohaApi


# ソースファイルの場所取得
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
SETTINGS = "settings/config.ini"

# 設定値取得
config = configparser.ConfigParser()
config.read(APP_ROOT + SETTINGS)
CLIENT_ID = config.get("COTOHA API", "Developer Client id")
CLIENT_SECRET = config.get("COTOHA API", "Developer Client secret")
DEVELOPER_API_BASE_URL = config.get("COTOHA API", "Developer API Base URL")
ACCESS_TOKEN_PUBLISH_URL = config.get("COTOHA API", "Access Token Publish URL")

# COTOHA APIインスタンス生成
cotoha_api = CotohaApi(CLIENT_ID, CLIENT_SECRET,
                       DEVELOPER_API_BASE_URL, ACCESS_TOKEN_PUBLISH_URL)

# 解析対象文
sentence = "一方で、青空文庫の情報を利用するのはあまり簡単ではありません。基本的にはwww.aozora.gr.jpで配布されているHTMLやCSVを解析する必要がありますが、青空文庫には日々作品が追加されていくので、それを繰り返し行う必要があります。このような状況を改善しようと作り始めたのがPubserverという青空文庫の情報を配布するためのサーバーシステムです。これを使うと、RESTfulなAPI呼び出しで作品や著者・訳者のメタ情報や作品のコンテンツ情報を取得できます。この投稿では、Pubserverのシステム構成とそれらがどのように動いているのかを簡単にご説明したいと思います。"

# 構文解析API実行
result = cotoha_api.sentiment(sentence)

# 出力結果を見やすく整形
result_formated = json.dumps(result, indent=4, separators=(',', ': '))
print(codecs.decode(result_formated, 'unicode-escape'))
