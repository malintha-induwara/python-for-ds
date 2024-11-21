#Calculate cost

def calculate_cost(price,quantity,discount=0,tax=0):
    cost = price * quantity
    cost = cost - (cost * discount / 100)
    cost = cost + (cost * tax / 100)
    return cost

print(calculate_cost(100,2))
print(calculate_cost(100,2,10,20))