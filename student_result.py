1. a=int(input("Enter first number:")) 
b=int(input("Enter second number:")) 
sum=a+b 
print("result=",sum) 
2. P=float(input("Enter principle amount:")) 
R=float(input("Enter rate:")) 
T=float(input("Enter time:")) 
result=(P*R*T)/100 
print("Simple intrest",result) 
3. a=int(input("Enter the first number:")) 
b=int(input("Enter the second value:")) 
sum=a+b 
sub=a-b 
mul=a*b 
div=a/b 
print("sum=",sum) 
print("difference=",sub) 
print("product=",mul) 
print("division",div) 
4. r=float(input("Enter radius of circle:")) 
pi=3.14 
result=pi*r*r 
print("Area of circle is found to be:",result) 
5. a=str(input("Enter the string:")) 
repeat=a*4 
print("repetation is:",concat) 
6. a=str(input("Enter the first string:")) 
b=str(input("Enter the next string:")) 
concat=a+b 
print("concatination is:",concat) 
7. import math 
r=float(input("Enter the radius of the circle:")) 
area=math.pi*r*r 
print("Radius if the circle is:",area) 
8. a=int(input("Enter the first number")) 
b=int(input("Enter the second number")) 
result=a//b 
print("Floor division result:",result)     
 
9. x=int(input("Enter the number:")) 
result=x**2 
print("The square of the given numberis=",result) 
 
10. a=int(input("Enter the number:")) 
if a%2==0: 
    print(a,"is a even number") 
else: 
    print(a,"is a odd number") 
 
11. a=int(input("Enter the number:")) 
if a%2==0: 
    print(a,"is a even number") 
else: 
    print(a,"is a odd number") 
 
12. for i in range(1,11): 
    print(i) 
 
13. for i in range(1,21): 
    print(i) 
 
14. for i in range(10,0,-1): 
    print(i) 
 
15. for i in range(1,16): 
    if i%2!=0: 
        print(i)  
 
16. for i in range(1,11): 
    print(i,end=' ') 
 
17. x=int(input("Enter a number:")) 
if(x>0): 
    print("The given number is positive") 
else: 
    print("The given number is negative") 
 
18. x=int(input("Enter a number:")) 
if (x%2==0): 
    print("The given number is even") 
else: 
    print("The given number is odd") 
 
19. x=int(input("Enter the age of the person:")) 
if (x>=18): 
    print("The person is eligible to vote") 
else: 
    print("The person is not eligible to vote") 
 
20. M=int(input("Enter the marks of the student:")) 
if (M>=30): 
    print("The student passed") 
else: 
    print("The student failed") 
 
21. s=input("Get the signal colour:") 
if (s=="Red"): 
    print("STOP") 
elif (s=="Yellow"): 
    print("GET READY") 
elif (s=="Green"): 
    print("GOOOOO!") 
else: 
    print("As your wish") 
 
22. a=int(input("Enter a number:")) 
if a%2==0: 
    print("Even number") 
     
    if(a>30): 
        print("Number is greater than 30....GREAT!!") 
         
print("BYEE!!")         
 
23. x=int(input("Enter the number:")) 
if (x>0): 
    print("Positive number") 
 
    if x%2==0: 
        print("It is an even number") 
    else: 
        print("It is a odd number") 
else: 
    print("Negative number") 
print("Thank you")        
 
24. x=int(input("Enter your age:")) 
if (x>=18): 
    print("The person is eligible to vote") 
 
    if (x>60): 
        print("The voter is senior") 
    else: 
        print("He/She is a normal voter") 
else: 
    print("The person is not eligible to vote") 
 
25. marks=int(input("Enter student's marks:")) 
if (marks>=35): 
    print("Pass") 
 
    if (marks>=75): 
        print("Distinction") 
         
    elif (marks>=60): 
        print("First class") 
    else: 
        print("Pass") 
else: 
    print("FAIL") 
 
26. num=int(input("Enter the number:")) 
if (num>0): 
    print("It is positive") 
    if (num%2==0): 
        print("The number is positive and even as well!") 
    else: 
        print("The number is positive and odd") 
elif (num==0): 
    print("The number is zero") 
else: 
    print("It is negative") 
 
27. x=int(input("Enter your salary:")) 
if (x>50000): 
    print("Tax applied") 
    if (x>100000): 
        print("Tax applied 20%") 
    else: 
        print("Tax applied 10%") 
else: 
    print("No tax applied!") 
 
28. correct_password="Kavery2006" 
password=input("Enter password:") 
if password==correct_password: 
    print("Login successful") 
else: 
    print("Wrong password") 
 
29. x=int(input("Enter first number")) 
y=int(input("Enter second number")) 
z=int(input("Enter third number")) 
if (x>y and x>z): 
    print(x,"is the greater number") 
elif(y>x and y>z): 
    print(y,"is greater number") 
else: 
    print(z,"is greater number") 
 
30. name='kavery' 
for i in name: 
    print(i) 
 
31. name='kavery','ram','shyam' 
for i in name: 
    print(i) 
    if i=='kavery': 
        print("hi it's me") 
    elif i=='ram': 
        print("hello it's me") 
    elif i=='shyam': 
        print("hey it's me") 
    else: 
        print("nobody") 
print("Thank you!!")      
 
32. numbers=[2,3,5,-2,-10] 
for i in numbers: 
square = i ** 2 
print(square) 
33. total=0 
for i in range(1,11): 
total=total+i 
print(total)     
34. total=0 
for i in range(1,21): 
if i%2==0: 
total=total+i 
print(total)         
35. total=0 
for i in range(1,21): 
if i%2!=0: 
total=total+i 
print(total)         
36. for i in range(10,0,-1): 
print(i)
