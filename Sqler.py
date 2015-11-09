import pyperclip

text = pyperclip.paste()
lines = text.splitlines()
for i in range(len(lines) - 1):
	lines[i] = "\'" + lines[i] + "',"
lines[-1] = "\'" + lines[-1] + "'"


for i in lines:
	if i == "'',":
		lines.remove(i)

text = '\n'.join(lines)
pyperclip.copy(text)










