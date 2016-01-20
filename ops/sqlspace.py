''' Copy a list of cells to yoru clipboard and this will ready them for SQL all on one line'''

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
	text = ''.join(List)
	pyperclip.copy(text)



copy(removeBlank(sqlFormat(paste())))










