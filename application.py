# Flask などの必要なライブラリをインポートする
import os
from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# json の場所を指定する
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
f = open(APP_ROOT + "data/json/neko.json", "r")
lines = loads(f.read())


@app.route("/")
def index():
    # app.logger.debug(lines['result'])
    action = "read"
    return render_template('index.html', action=action)


@app.route('/read', methods=['POST'])
def get_text():
    global lines
    # app.logger.debug(lines)

    line_number = int(request.form['line_number'])
    # app.logger.debug(line_number)
    if(len(lines['result']) <= line_number):
        line_number = 0

    next_line_number = line_number + 1
    # app.logger.debug(next_line_number)
    if(len(lines['result']) <= next_line_number):
        next_line_number = 0

    d = lines['result'][line_number]
    # app.logger.debug(d)
    d['text_length'] = len(d['form'])
    d['next_line_number'] = next_line_number

    return dumps(d)


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
