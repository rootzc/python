#!/usr/bin/env python
#-*-coding:utf-8 -*-

#the yield keyword for intrrupt the func ,when you call next(),it will be continue
def fib(num):
	"斐波纳妾函数"
	i,f1,f2 = 0,0,1
	while i<num:
		yield f2 #make the func to be a generator
		tmp = f1
		f1 = f2
		f2 = tmp + f2
		i+=1
L = [n for n in fib(6)]
print L
