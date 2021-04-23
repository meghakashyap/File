from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("demo.txt"))

# 2nd way
file=open("unique.txt","r")
a=file.read().split()
i=0
empty=[]
while i<len(a):
    c=0
    e=[]
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    e.append(a[i])
    e.append(c)
    if e not in empty:
        empty.append(e)
    i+=1
print(empty)
file.close()
#count the frequency of words