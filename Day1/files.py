f=open("teams.txt", "w+")


for i in range(5):
    f.write("Sports Team %d\r\n" %(i+1))

f.close()

f=open("teams.txt")
lines=f.readlines()
print(lines[0])
print(lines[2])

#if f.mode == 'r':
    #contents =f.read()
   #print(contents)



