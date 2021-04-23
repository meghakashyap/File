file=open("textfile.txt","w")
a=file.write("Hey its a text file \n Its a demo file \n I made this file of learning purpose \n Actually i ma learning python in NAVGURUKUL")
print(a)
file.close()

import shutil
shutil.copy("textfile.txt","copy.txt")
a=open("copy.txt","r")
print(a.read())


#2nd way
file=open("textfile.txt","r")
a=file.read()
print(a)
file1=open("copy_demo.py","w")
b=file1.write(a)
file1.close()
file.close()

#copy the file