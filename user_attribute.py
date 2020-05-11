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
# document = input()
document = 'どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。'

# 構文解析API実行
result = cotoha_api.userAttribute(document)

# 出力結果を見やすく整形
# result_formated = json.dumps(result, indent=4, separators=(',', ': '))
# print(codecs.decode(result_formated, 'unicode-escape'))

# response = list()
# for key, value in result['result'].items():
#     print('{0}: {1}'.format(key, value))

d = {}
for key, value in result['result'].items():
    d[key] = value
print(d['hobby'])
print(result['result']['hobby'])
