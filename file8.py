size=int(input("enter any number"))
file=open("file8.txt","w")
for i in range(size):
    roll_no=int(input("enter your roll no."))
    name=input("enter your name")
    marks=float(input("enter your mark"))
    rec=str(roll_no)+","+name+","+str(marks)+"\n"
    file.write(rec)
file.close()

