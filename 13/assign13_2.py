import urllib
from BeautifulSoup import *
url=raw_input("Enter URL: ")
inp=raw_input("Enter count: ")
count=int(inp)
inp1=raw_input("Enter position: ")
position=int(inp1)
results=list()
while count>0:
	html=urllib.urlopen(url).read()
	soup=BeautifulSoup(html)
	tags=soup('a')
	linklist=list() #list with extracted links
	namelist=list() #list with extracted names
	for tag in tags:
		linklist.append(tag.get('href',None))#append value of href
		namelist.append(tag.contents[0])#append tag content, name in this case
	url=linklist[position-1]#update variable url
	count=count-1
	results.append(namelist[position-1])
print results[-1]





