import requests, sys, bs4, webbrowser

res = requests.get('http://reddit.com')
res.raise_for_status

soup = bs4.BeautifulSoup(res.text)


linkElems = soup.select('.title a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open(linkElems[i].get('href'))














'''
for Amazon
res = requests.get ('http://amazon.com/s/field-keywords=' + ''.join(sys.argv[1:]))
res.raise_for_status

soup = bs4.BeautifulSoup(res.text)
links = soup.select('access-detail-page a')
numOpen = min(2,len(links))
for i in range(numOpen):
	webbrowser.open('http://amazon.com/s/field-keywords=' + links[i].get('href'))
	'''