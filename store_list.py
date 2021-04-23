
a=open("store list.txt","r")
f=a.readlines()
s=[]
for i in f:
    s.append(i)
print(s)
#read line by line and store in a list
