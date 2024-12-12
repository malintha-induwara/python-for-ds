#you have list of integers represneting temaerature in celsius then write a python program using map 
#function to convert these values into fahrenheit
#use the formula F = (9/5)*C + 32


celsius = [20,30,25,40,15]

def celsius_to_fahrenheit(c):
    return c*(9//5) + 32

# fahrenheit = list(map(celsius_to_fahrenheit, celsius))

fahrenheit = list(map(lambda c: c*(9//5)+32,celsius))

print(fahrenheit)