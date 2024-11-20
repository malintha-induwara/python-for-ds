marks = input("Enter marks: ")

marks = int(marks)

if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")