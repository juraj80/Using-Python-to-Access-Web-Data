import urllib
from BeautifulSoup import *

url=raw_input('Enter - ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup('span')
count=0
for tag in tags:
	num=int(tag.contents[0])
	count=count+num
print count

'''
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs

'''
