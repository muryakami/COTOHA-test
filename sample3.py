import os
from bottle import get, post, request, static_file, run
from json import dumps, loads


@get('/reading/<filepath:path>')
def reading(filepath):
    return static_file(filepath, root=APP_ROOT)


@post('/get_text')
def get_text():
    global lines

    line_number = int(request.forms.get("line_number"))
    if(len(lines) <= line_number):
        line_number = 0

    next_line_number = line_number + 1
    if(len(lines) <= next_line_number):
        next_line_number = 0

    d = lines[line_number]
    d['text_length'] = len(d['utsusemi'])
    d['next_line_number'] = next_line_number

    return dumps(d)


APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"
f = open(APP_ROOT + "json/Meros.json", "r")
lines = loads(f.read())

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
