FILE_NAME = 'data/text/neko.txt'

f = open(FILE_NAME)
lines = f.read()
f.close()

# 別ファイルへの保存
SENTENCES_FILE = FILE_NAME.replace('/text', '/text/sentence')
print(SENTENCES_FILE)
with open(SENTENCES_FILE, 'w') as f:

    # センテンス区切り
    for line in lines.splitlines():
        line = line.strip()

        if (not line):
            continue

        # line = line.replace("。」", "br1")
        # line = line.replace("。）", "br2")
        # line = line.replace("。", "。\n")
        # line = line.replace("br1", "。」")
        # line = line.replace("br2", "。）")

        line = line.replace("。", "。\n")
        line = line.replace("「", "\n「")
        line = line.replace("」", "」\n")
        line = line.strip()

        if (line[-1] != "\n"):
            line += "\n"
        print(line, end='')

        f.write(line)
        # print("\n\n")
