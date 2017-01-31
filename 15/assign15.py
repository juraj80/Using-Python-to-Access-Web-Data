import urllib
import json

url=raw_input('Enter URL: ')
uh=urllib.urlopen(url)
data=uh.read()
input=json.loads(data)  #deserialization
print 'User count: ', len(input)
sum=0
for item in input['comments']:
	sum=sum+int(item['count'])

print sum
