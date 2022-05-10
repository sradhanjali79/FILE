# file=open("file3.txt","r")
# str=" "
# c=0
# while str:
#     str=file.readline()
#     if str not in " \n":
#         c=c+1
# print(c)
# file.close()

file=open("file3.txt","r")
x=file.read()
f=x.split("\n")
c=0
i=0
while i<len(f):
    if f[i] not in "\n":
        c=c+1
    i=i+1
print(c)
file.close()
