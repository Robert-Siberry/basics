name=input("Please enter the students name: ")

hw=int(input("Please enter "+name+"s homework mark: "))

while hw==0 or hw>25:
    hw=int(input("Please enter a homework mark out of 25: "))

a=int(input("Please enter "+name+"s assessment mark: "))

while a==0 or a>50:
    a=int(input("Please enter an assessment mark out of 50:"))