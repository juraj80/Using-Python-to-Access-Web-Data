import urllib
from BeautifulSoup import*

url=raw_input('Enter URL: ')
count=int(raw_input('Enter count: '))
position=int(raw_input('Enter position: '))

results=list()

num=0
while num<count:
	print 'num: ',num
	print 'url: ',url
	html=urllib.urlopen(url).read()
	soup=BeautifulSoup(html)
	urllist=list()
	namelist=list()
	tags=soup('a')
	for tag in tags:
		urllist.append(tag.get('href',None))
		namelist.append(tag.contents[0])
	url=urllist[position-1]
	results.append(namelist[position-1])
	num=num+1 

print results

	
	

