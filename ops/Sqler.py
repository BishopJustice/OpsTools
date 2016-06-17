'''Copy a list to your clipboard and this will add 'x', so you can input it into a SQL query.'''

import pyperclip

text = pyperclip.paste()
lines = text.splitlines()

for i in range(len(lines) - 1):
    lines[i] = "\'" + lines[i] + "',"
lines[-1] = "\'" + lines[-1] + "'"


for i in lines:
    if i == "'',":
        lines.remove(i)

easy = []
for each in lines:
    if (lines.index(each) + 1) % 8 == 0:
        easy.append(str(each) + '\n')
    else:
        easy.append(str(each))

text = ' '.join(easy)

pyperclip.copy(text)
