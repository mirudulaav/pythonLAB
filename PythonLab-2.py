#STUDENT MARK PROCESSING
#CODING
a=int(input("Enter the marks obtained in subject1:"))
b=int(input("Enter the marks obtained in subject2:"))
c=int(input("Enter the marks obtained in subject3:"))
d=int(input("Enter the marks obtained in subject4:"))
e=int(input("Enter the marks obtained in subject5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")
