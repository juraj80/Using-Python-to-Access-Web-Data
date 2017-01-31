import urllib
import xml.etree.ElementTree as ET

url=raw_input("Enter location: ")
print 'Retrieving',url
uh=urllib.urlopen(url)
data=uh.read()
print 'Retrieved', len(data),'characters'
tree=ET.fromstring(data)
sum=0
for child in tree.find('comments'):
	sum=sum+int(child[1].text)

print sum


'''
tree=ET.fromstring(url)

counts=tree.findall('.//count') #XPath selector - list of elements

sum=0
for count in counts:
	sum=sum+int(count.text)
print sum
'''

'''
DATA FORMAT
<comments>
	<comment>
		<name>Matthias</name>
		<count>97</count>
	</comment>
.
.
</comments>
'''
