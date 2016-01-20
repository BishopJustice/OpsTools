''' Takes list seperated by new line characters on your clipboard and opens their websites'''

import webbrowser, pyperclip

addresses = pyperclip.paste().split('\n')

for each in addresses:
	webbrowser.open(each)
