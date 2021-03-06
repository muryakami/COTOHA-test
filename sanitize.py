import lxml.html
from lxml.html.clean import Cleaner

# ダウンロードした XHTML ファイルのファイル名を書きます。
# ちなみに 789_14547.html は《吾輩は猫である》です。
FILE_NAME = 'data/xhtml/789_14547.html'

with open(FILE_NAME, encoding='shift_jis') as f:
    data = f.read().encode('shift_jis')

cleaner = Cleaner(page_structure=False, remove_tags=(
    'ruby', 'br'), kill_tags=('rt', 'rp'))
cln_html = cleaner.clean_html(data).decode('utf-8')

plain_text = lxml.html.fromstring(cln_html).find_class('main_text')[
    0].text_content()
# print(plain_text)

# 別ファイルへの保存
PLAIN_TEXT = FILE_NAME.replace('xhtml', 'text').replace('.html', '.txt')
print(PLAIN_TEXT)
with open(PLAIN_TEXT, 'w') as f:
    f.write(plain_text)
