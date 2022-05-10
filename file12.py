# file=open("file12.txt","r")
# file1=open("delhi.txt","w")
# file2=open("shimla.txt","w")
# file3=open("other.txt","w")
# x=file.read()
# file4=x.split("\n") 
# i=0
# while i<len(file4):
#     if "delhi" in file4[i]:
#         file1.write(file4[i])
#         file1.write("\n")
#     elif "shimla" in file4[i]:
#          file2.write(file4[i])
#          file2.write("\n")
#     else:
#          file3.write(file4[i])
#          file3.write("\n")
#     i=i+1

# file.close()

file=open("file12.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
x=file.read()
file4=x.split("\n") 
for i in range(len(file4)):
    if "delhi" in file4[i]:
        file1.write(file4[i])
        file1.write("\n")
    elif "shimla" in file4[i]:
         file2.write(file4[i])
         file2.write("\n")
    else:
         file3.write(file4[i])
         file3.write("\n")
    # i=i+1

file.close()

