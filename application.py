# Flask などの必要なライブラリをインポートする
import os
from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads
from cotoha_api import CotohaApi

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# APP_ROOT の設定
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"


@app.route("/")
def index():
    # app.logger.debug(lines['result'])
    action = "parse"
    return render_template('index.html', action=action)


@app.route('/read', methods=['POST'])
def read():
    # json の場所を指定する
    f = open(APP_ROOT + "data/json/neko.json", "r")
    lines = loads(f.read())

    # global lines
    # app.logger.debug(lines)

    # line_number = int(request.args.get('line_number'))  # ['GET']
    line_number = int(request.form['line_number'])  # ['POST']

    line_number = __checkLineNumber__(len(lines), line_number)
    next_line_number = __checkLineNumber__(len(lines), line_number + 1)

    d = lines['result'][line_number]

    d['text_length'] = len(d['form'])
    d['next_line_number'] = next_line_number

    return dumps(d)


@app.route('/parse', methods=['POST'])
def parse():
    f = open(APP_ROOT + "data/text/sentence/neko.txt", "r")
    document = f.read()
    # num_lines = sum(1 for line in open(
    #     APP_ROOT + 'data/text/sentence/neko.txt'))
    lines = document.splitlines()

    line_number = int(request.form['line_number'])

    line_number = __checkLineNumber__(len(lines), line_number)
    next_line_number = __checkLineNumber__(len(lines), line_number + 1)

    # COTOHA APIインスタンス生成
    cotoha_api = CotohaApi()
    # 解析対象文
    sentence = lines[line_number]
    # 構文解析API実行
    result = cotoha_api.parse(sentence)

    kana_list = list()
    for chunks in result['result']:
        for token in chunks["tokens"]:
            kana_list.append(token["kana"])

    d = {}
    d['sentence'] = sentence
    d['kana'] = ' '.join(kana_list)
    d['text_length'] = len(sentence)
    d['next_line_number'] = next_line_number

    return dumps(d)


def __checkLineNumber__(lines, index):
    if(lines <= index):
        index = 0
    return index


# # メッセージをランダムに表示するメソッド
# def picked_up():
#     messages = [
#         "こんにちは、あなたの名前を入力してください",
#         "やあ！お名前は何ですか？",
#         "あなたの名前を教えてね"
#     ]
#     # NumPy の random.choice で配列からランダムに取り出し
#     return np.random.choice(messages)

# # ここからウェブアプリケーション用のルーティングを記述
# # index にアクセスしたときの処理
# @app.route('/')
# def index():
#     title = "ようこそ"
#     message = picked_up()
#     # index.html をレンダリングする
#     return render_template('index.html',
#                            message=message, title=title)

# # /post にアクセスしたときの処理
# @app.route('/post', methods=['GET', 'POST'])
# def post():
#     title = "こんにちは"
#     if request.method == 'POST':
#         # リクエストフォームから「名前」を取得して
#         name = request.form['name']
#         # index.html をレンダリングする
#         return render_template('index.html',
#                                name=name, title=title)
#     else:
#         # エラーなどでリダイレクトしたい場合はこんな感じで
#         return redirect(url_for('index'))


if __name__ == '__main__':
    # app.debug = True  # デバッグモード有効化
    # app.run(host='0.0.0.0')  # どこからでもアクセス可能に
    app.run(debug=True)

    # run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
