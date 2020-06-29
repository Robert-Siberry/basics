name=input("Please enter the students name: ")

hw=int(input("Please enter "+name+"s ICT homework mark: "))

while hw==0 or hw>25:
    hw=int(input("Please enter a homework mark out of 25: "))

a=int(input("Please enter "+name+"s ICT assessment mark: "))

while a==0 or a>50:
    a=int(input("Please enter an assessment mark out of 50:"))

fe=int(input("Please enter "+name+"s ICT final exam mark: "))

while fe==0 or fe>100:
    fe=int(input("Please enter a mark out of 100: "))

print("Homework Mark = ", hw)
print("Assessment Mark = ", a)
print("Final Exam Mark = ", fe)

total=hw+a+fe

print("Total = ", total, "out of 175")

if total>=149:
    print(name+" passed ICT with distinction")
elif total>=87:
    print(name+" passed ICT")
else:
    print(name+" failed ICT")