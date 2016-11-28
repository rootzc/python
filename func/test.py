#!/usr/bin/env python
#-*-coding : utf-8 -*-
#import string

def f(x):
	return [x[0].upper()+x[1:].lower()]


L = ['asd','asdSS','ASAS']

print map(f,L)
