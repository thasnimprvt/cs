print("STUDENTS LIST") 
print ("---------------------------")
n=int(input("enter the no: of students "))

students=[]

marks=[]

g=[]

print(" STUDENT DATA ENTRY")

print("------------------------")

for i in range(1,n+1):

    name=input("student name "+ str(i) +" :")

    mark=input("mark :")

    students.append(name)

    marks.append(mark)

    print("--------------------")

top_score=max(marks)

for i in range(n):

    if int(marks[i])>40:

        g.append('A')

    elif int(marks[i])>30:

        g.append('B')

    elif int(marks[i])>20:

       g.append('C')

    elif int(marks[i])>10:

        g.append('D')

    else:

        g.append('FAIL')

print("STUDENT GRADE LIST")

 

print("=========================")        

for i in range(n):

    if marks[i]==top_score :

        print(students[i] +" - "+g[i] +  " <-(TOPPER)")

    else :

        print(students[i] +" - "+g[i])
