class Students:
    def __init__(Self, name, age, level, test1, test2, test3):
        Self.name = name
        Self.age = age
        Self.level = level
        Self.test1 = test1
        Self.test2 = test2
        Self.test3 = test3


S1 = Students("John", "22", "Student", 45, 32, 50)
S2 = Students("Robert", "24", "Student", 50, 45, 50)
S3 = Students("David", "30", "Student", 35, 45, 50)
S4 = Students("Andrew", "25", "Student", 35, 40, 48)
S5 = Students("Mark", "26", "Student", 46, 50, 39)


print(S1.name, S1.age, S1.level, "= S1")
print(S2.name, S2.age, S2.level, "= S2")
print(S3.name, S3.age, S3.level, "= S3")
print(S4.name, S4.age, S4.level, "= S4")
print(S5.name, S5.age, S5.level, "= S5")

d = {"S1":S1, "S2":S2, "S3":S3, "S4":S4, "S5":S5}

s = str(input("Please select the student(i.e. S1, S2, S3) you want to see the average score for: "))
#print(d[s])

a = (getattr(d[s], "test1"))
#print(a)
b = (getattr(d[s], "test2"))
#print(b)
c = (getattr(d[s], "test3"))
#print(c)
t = (a+b+c)/3

print(str(getattr(d[s], "name")+"s average test score is"(t)))
