'''Copy a list to your clipboard and this will add 'x', so you can input it into a SQL query'''

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
	if (lines.index(each) +1 ) % 8 == 0:
		easy.append(str(each)+'\n')
	else:
		easy.append(str(each))

text = ' '.join(easy)
	
pyperclip.copy(text)
















'''
This can also be done useing functions

import pyperclip

def paste():
	text = pyperclip.paste()
	lines = text.splitlines()
	return lines

def sqlFormat(List):
	for i in range(len(List) - 1):
		List[i] = "\'" + List[i] + "',"
	List[-1] = "\'" + List[-1] + "'"
	return List

def removeBlank(List):
	for i in List:
		if i == "'',":
			List.remove(i)
	return List

def copy(List):
	text = ' '.join(List)
	pyperclip.copy(text)



copy(removeBlank(sqlFormat(paste())))
'''









