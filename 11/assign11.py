import re
handle=open('regex_sum_337964.txt')
txt=handle.read()
str_list=re.findall('[0-9]+',txt)
sum=0
for item in str_list:
	item=int(item)
	sum=sum+item
print sum

'''
#alternative without read()

import re
fhand=open('regex.txt')
sum=0
for line in fhand:
	line=line.rstrip()
	num=re.findall('[0-9]+',line)
	if len(num)<1:continue
	for item in num:
		sum=sum+(int(item))
print sum
'''
