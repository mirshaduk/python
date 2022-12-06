students={}
n=int(input("Enter the number of students "))
for i in range(n):
    name=input("Enter the name of the student ")
    marks=int(input("Enter the marks of old  student "))
    students[name]=marks
students = dict(sorted(students.items(), key=lambda x:x[1],reverse=True))
for i in students:
    print(i,":",students[i])
s=input("do you want to change the marks of students press(Y/N ")
if s=="Y" or s=="y":
    a=input("Enter the name ofthe student whom you want to change the marks ")
    newmarks=int(input("Enter the new mark of the student "))
    b=(list(students).index(a))+1
    for i in students:
        if i==a:
            students[i]=newmarks
    students = dict(sorted(students.items(), key=lambda x: x[1],reverse=True))
    C=(list(students).index(a))+1
    for i in students:
        print(i,":",students[i])
    print("The previos rank was {} and the currentrank is {}.".format(b,c))
else:
    print("OK,Have a nice day! ")
