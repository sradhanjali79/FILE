file=open("file4.txt","r")
str=" "
c=0
c1=0
while str:
    str=file.readline()
    c=c+len(str)
    c1=c1+len(str.strip())
print(c)
print(c1)
file.close()
