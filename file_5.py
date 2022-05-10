file=open("file4.txt","r")
str=" "
while str:
    str=file.readline()
    print(str)
file.close()