''' Copy a url to your clipboard or type one in the terminal and this will turn it into fun.txt in your working directory'''
import requests, sys, pyperclip
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

res = requests.get(address)
res.raise_for_status()
# Change fun.txt to a dynamic name that identifies the file
playFile = open('fun.txt','wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close