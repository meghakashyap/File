file=open("demo.txt","r")
a=file.readlines()
i=0
while i<len(a):
    i+=1
print(i)  
file.close()
#count the line 