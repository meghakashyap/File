a=[2,3,4,5,6,7,8,9]
file=open("even.txt","w")
i=0
empty=[]
while i<len(a):
    if a[i]%2==0:
        empty.append(a[i])
    i+=1
file.write(str(empty))
file=open("even.txt","r")
print(file.read())
file.close()