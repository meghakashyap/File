f=open("name_city.txt","r")
d=open("delhi.txt","a")
s=open("shimla.txt","a")
o=open("other.txt","a")
data=f.read()
data_in=data.split("\n")
for i in range(0,len(data_in)):
    if "delhi" in data_in[i]:
        d.write(data_in[i])
        d.write("\n")
    elif "shimla" in data_in[i]:
        s.write(data_in[i])
        s.write("\n")
    else:
        o.write(data_in[i])
        o.write("\n")
d.close()
s.close()
o.close()
f.close()

f=open("name_city","r")
d=open("delhi.txt","r")
s=open("shimla.txt","r")
o=open("other.txt","r")
print(d.read())
print(s.read())
print(o.read())
 
