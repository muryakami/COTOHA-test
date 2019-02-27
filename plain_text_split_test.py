FILE_NAME = 'data/neko.txt'

f = open(FILE_NAME)
lines = f.read()
f.close()

# print(lines)

for line in lines.splitlines():
    line = line.strip()

    if (not line):
        continue

    line = line.replace("。", "。\n")
    line = line.replace("「", "\n「")
    line = line.replace("」", "」\n")

    line = line.strip()

    if (line[-1] != "\n"):
        line += "\n"

    print(line, end='')
    # print("\n\n")
