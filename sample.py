# -*- coding: utf-8 -*-

import os
import json
import configparser
import codecs
from cotoha_api_python3 import CotohaApi


# ソースファイルの場所取得
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"

# 設定値取得
config = configparser.ConfigParser()
config.read(APP_ROOT + "config.ini")
CLIENT_ID = config.get("COTOHA API", "Developer Client id")
CLIENT_SECRET = config.get("COTOHA API", "Developer Client secret")
DEVELOPER_API_BASE_URL = config.get("COTOHA API", "Developer API Base URL")
ACCESS_TOKEN_PUBLISH_URL = config.get("COTOHA API", "Access Token Publish URL")

# COTOHA APIインスタンス生成
cotoha_api = CotohaApi(CLIENT_ID, CLIENT_SECRET,
                       DEVELOPER_API_BASE_URL, ACCESS_TOKEN_PUBLISH_URL)

# 解析対象文
sentence = "すもももももももものうち"
# sentence = input()

# 構文解析API実行
result = cotoha_api.parse(sentence)

# 出力結果を見やすく整形
result_formated = json.dumps(result, indent=4, separators=(',', ': '))
print(codecs.decode(result_formated, 'unicode-escape'))
