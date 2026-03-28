marks=int(input("Enter student's marks:"))
if marks >= 35:
    print("Pass")

    if (marks>=75):
        print("Distinction")   
    elif (marks>=60):
        print("First class")
    else:
      print("Second class")
else:
    print("Fail")
