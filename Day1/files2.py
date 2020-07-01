f=open("textfile.txt", "w")


for i in range(10):
    f.write("This is a new line %d\r\n" %(i+1))

f.close()
f=open("textfile.txt", "r")



if f.mode == 'r':
    contents = f.read()
    print(contents)


#f=open("textfile.txt")
#lines=f.readlines()
#print(lines)

f.close()