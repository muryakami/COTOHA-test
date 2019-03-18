# -*- coding:utf-8 -*-

import os
import json
import urllib.request
import configparser

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


# COTOHA API操作用クラス
class CotohaApi:
    # 初期化
    def __init__(self, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, developer_api_base_url=DEVELOPER_API_BASE_URL, access_token_publish_url=ACCESS_TOKEN_PUBLISH_URL):
        self.client_id = client_id
        self.client_secret = client_secret
        self.developer_api_base_url = developer_api_base_url
        self.access_token_publish_url = access_token_publish_url
        self.getAccessToken()

    # アクセストークン取得
    def getAccessToken(self):
        # アクセストークン取得URL指定
        url = self.access_token_publish_url
        # ヘッダ指定
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        # リクエストボディ指定
        data = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }
        # リクエストボディ指定をJSONにエンコード
        data = json.dumps(data).encode()
        # リクエスト生成
        req = urllib.request.Request(url, data, headers)
        # リクエストを送信し、レスポンスを受信
        res = urllib.request.urlopen(req)
        # レスポンスボディ取得
        res_body = res.read()
        # レスポンスボディをJSONからデコード
        res_body = json.loads(res_body)
        # レスポンスボディからアクセストークンを取得
        self.access_token = res_body["access_token"]

    # 構文解析API
    def parse(self, sentence):
        # URL指定
        url = self.developer_api_base_url + "v1/parse"
        # リクエストボディ指定
        data = {
            "sentence": sentence
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 固有表現抽出API
    def ne(self, sentence):
        # URL指定
        url = self.developer_api_base_url + "v1/ne"
        # リクエストボディ指定
        data = {
            "sentence": sentence
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 照応解析API
    def coreference(self, document):
        # URL指定
        url = self.developer_api_base_url + "beta/coreference"
        # リクエストボディ指定
        data = {
            "document": document
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # キーワード抽出API
    def keyword(self, document):
        # URL指定
        url = self.developer_api_base_url + "v1/keyword"
        # リクエストボディ指定
        data = {
            "document": document
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 類似度算出API
    def similarity(self, s1, s2):
        # 類似度算出API URL指定
        url = self.developer_api_base_url + "v1/similarity"
        # リクエストボディ指定
        data = {
            "s1": s1,
            "s2": s2
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 文タイプ判定API
    def sentenceType(self, sentence):
        # URL指定
        url = self.developer_api_base_url + "v1/sentence_type"
        # リクエストボディ指定
        data = {
            "sentence": sentence
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 感情分析API
    def sentiment(self, sentence):
        # URL指定
        url = self.developer_api_base_url + "v1/sentiment"
        # リクエストボディ指定
        data = {
            "sentence": sentence
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # ユーザ属性推定API
    def userAttribute(self, document):
        # URL指定
        url = self.developer_api_base_url + "beta/user_attribute"
        # リクエストボディ指定
        data = {
            "document": document
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 言い淀み除去API
    def removeFiller(self, text):
        # URL指定
        url = self.developer_api_base_url + "beta/remove_filler"
        # リクエストボディ指定
        data = {
            "text": text
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # 音声認識結果誤り検知API
    def detectMisrecognition(self, sentence):
        # URL指定
        url = self.developer_api_base_url + "beta/detect_misrecognition"
        # リクエストボディ指定
        data = {
            "sentence": sentence
        }
        # リクエストを送信し、レスポンスを受信
        return self.__apiHelper__(url, data)

    # API ヘルパー
    def __apiHelper__(self, url, data):
        # ヘッダ指定
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json;charset=UTF-8",
        }

        # リクエストボディ指定をJSONにエンコード
        data = json.dumps(data).encode()
        # リクエスト生成
        req = urllib.request.Request(url, data, headers)
        # リクエストを送信し、レスポンスを受信
        try:
            res = urllib.request.urlopen(req)
        # リクエストでエラーが発生した場合の処理
        except urllib.request.HTTPError as e:
            # ステータスコードが401 Unauthorizedならアクセストークンを取得し直して再リクエスト
            if e.code == 401:
                print("get access token")
                self.access_token = getAccessToken(
                    self.client_id, self.client_secret)
                headers["Authorization"] = "Bearer " + self.access_token
                req = urllib.request.Request(url, data, headers)
                res = urllib.request.urlopen(req)
            # 401以外のエラーなら原因を表示
            else:
                print("<Error> " + e.reason)

        # レスポンスボディ取得
        res_body = res.read()
        # レスポンスボディをJSONからデコード
        res_body = json.loads(res_body)
        # レスポンスボディから解析結果を取得
        return res_body
