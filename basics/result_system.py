name = input("Enter student name: ")

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total marks:", total)
print("Average:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print(name, "has PASSED")
else:
    print(name, "has FAILED")
