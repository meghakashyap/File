name=["megha","raghav","jyoti","abhay"]
num=[2,3,4,5]
file=open("data.txt","w")
i=0
while i<len(name):
    tem=name[i]+str(num[i])
    file.write(tem)
    file.write("\n")
    i+=1
file=open("data.txt","r")
print(file.read())
file.close()