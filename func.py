#!/usr/bin/env python
# -*- coding : utf-8

def sort_perm(arr):
	if len(arr) == 0:
		return ;
	else:
		i = 0;
		while i<len(arr):
			j=0
			while j<len(arr)-1-i:
				if(arr[j]>arr[j+1]):
					tmp = arr[j+1]
					arr[j+1] = arr[j]
					arr[j] = tmp
				j+=1
			i+=1

			
	


vec = [1,9,2,8,37,4,5]
print vec
sort_perm(vec)
print vec
					
			
