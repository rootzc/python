#!/usr/bin/env python
#-*- coding -*-

list = []
for num in range(10):
	list.append(num)
print list

print "==============for struct =========================="
sum = 0
for i in range(101):
	sum = sum + i
print sum
print "========================================"
sum=0
for i in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum+i
print sum


print "===============while struct ========================="
sum = 0
i = 0
while i<=100:
	sum = sum + i
	i +=1
print sum 
