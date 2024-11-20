x = input("Enter a number: ")

x = int(x)

if x < 0:
    print("Value is negative")
elif x % 7 == 0:
    print("Value is multiplication of 7")
else:
    print("Value is positive and not a multiplication of 7")
    