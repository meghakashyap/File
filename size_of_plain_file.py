def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("unique.txt"))

#2nd way
file=open("unique.txt","w")
a=file.write("hey Unique person \n How are you\n Actually i am here for my study\n ")
print(a)
# size of file