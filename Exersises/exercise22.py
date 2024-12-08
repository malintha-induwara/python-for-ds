#write a python program to create a class QuadraticEquation that represnt a quadratic equation of the 
#from ax^2 + bx + c = 0  

#the class should have
#1) Attributes private attributes __a,__b and __c to store the coefficients of the quadratic equation
#2) a constructor to initialize the coefficient a,b and c
#3) a private method __discriminant that caluclates and return the discriminantn(d=b^2-4ac)
#4) a public method find_roots that
#   *use the private discriminat method
#   * return the roots of the equation
        # d>0 two distinct real roots
        #d=0 one real root
        #d<0 two complex roots (no real roots)
#

import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __discriminant(self):
        return (self.__b**2) - (4*self.__a*self.__c)

    def find_roots(self):
        d = self.__discriminant()
        if d > 0:
            root1 = (-self.__b + math.sqrt(d)) / (2*self.__a)
            root2 = (-self.__b - math.sqrt(d)) / (2*self.__a)
            return root1, root2
        elif d == 0:
            root = -self.__b / (2*self.__a)
            return root
        else:
            return "No real roots"


q = QuadraticEquation(1, 5, 6)
q1 = QuadraticEquation(1, 2, 1)
q2 = QuadraticEquation(1, 1, 1)

print(q.find_roots())
print(q1.find_roots())
print(q2.find_roots())