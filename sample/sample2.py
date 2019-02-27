from flask import Flask, render_template, request
import re

app = Flask(__name__)


def count_word(text):

    words = re.findall(r'[a-z0-9\\’\\\']+', text.lower())

    return len(words)


@app.route('/', methods=['POST', 'GET'])
def home():

    total = ''

    if request.method == 'POST':
        text = request.form['text']
        total = count_word(text)

        return render_template('main.html', total=total, sentence=text)

    return render_template('main.html', total=total)


if __name__ == "__main__":
    app.run(debug=True)
