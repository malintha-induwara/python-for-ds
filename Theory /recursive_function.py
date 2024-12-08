def find_factorail(number):
    if number ==0 or number ==1:
        return 1
    else:
        return (number * find_factorail(number-1))


print(find_factorail(0))
print(find_factorail(1))
print(find_factorail(2))
print(find_factorail(3))
print(find_factorail(4))
print(find_factorail(5))

# This cause a RecursionError maximum dpeth is 1000
print(find_factorail(1900))