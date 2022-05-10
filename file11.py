x= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("file11.txt","w")
for i in range(len(x)):
    file.write(x[i])
    file.write("\n")
file.close()

