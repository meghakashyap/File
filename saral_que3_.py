banks= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("banks_name.txt","w")
i=0
while i<len(banks):
    a=file.write(banks[i])
    a=file.write("\n")
    i+=1

file=open("banks_name.txt","r")
print(file.read())

#append in file banks name