# file=open("file7.txt","w")
# for i in range(5):
#     name=input("enter any name")
#     file.write(name)
#     file.write("\n")
# file.close()

file=open("file7.txt","w")
name=[]
for i in range(5):
    z=input("enter any name")
    name.append(z+"\n")
file.writelines(name)    
file.close()