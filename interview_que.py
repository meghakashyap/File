
file=open("language.txt","r")
demo=file.read()
i=0
while (demo[i:]):
    print(demo[i])
    i+=1
file.close()