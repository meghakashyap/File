# first way
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open("colors.txt","w") as file:
    for x in color:
        file.write("%s\n"%x)
a= open("colors.txt")
print(a.read())

#2nd way
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a=open("mus.txt","w")
i=0
while i<len(color):
    a.write(color[i])
    a.write("\n")
    i+=1
a=open("mus.txt","r")
b=a.read()
print(b)

#append list in a file

