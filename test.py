#!/usr/bin/env python

from sys import argv
#print("test string\n")
list = [2, "smail", 5, 1, 3, 4, 2, 1, 55]
a=0
str = "test strng !"
def f(ar):
    dub=[]
    for i in list:
        
        if (i == ar):
            dub.append(list.index(i))
            print(" {} - {} YES".format(i, dub[a]))
        else:
            print("{} - {}no\n".format(i, a))
        a+1;
    for di in dub:
        print(di)

j = argv[1:]
k = int(j[0])
int(k)
print(type(k))
print(" {}".format(k))
f(k)
