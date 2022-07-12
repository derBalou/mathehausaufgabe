import math

def f(x):
    return x**2 - 2

def bisection(a,b,n):
    # Test if the interval is valid
    if a > b:
        return 'Invalid interval'
    # Test if the interval is too small
    if not (f(a) < 0 and f(b) >= 0):
        return 'Invalid interval'
    x = (a + b)/2
    # Check if we have reached the desired accuracy
    if abs(f(x)) < 10**(-n):
        return x
    # Check wheter f(x) is bigger or smaller than 0
    if f(x) < 0:
        return bisection(x,b,n-1)
    elif f(x) > 0:
        return bisection(a,x,n-1)
    else:
        return x
    
# Test the function
print("Bisektion von f(x) = x² - 2 mit Terminierungsfall n = 5")
print("x: " + str(bisection(0,2,5)))
print("Abstand von sqrt(2): " + str(abs(bisection(0,2,5) - math.sqrt(2))))

print("Bisektion von f(x) = x² - 2 mit Terminierungsfall n = 10")
print("x: " + str(bisection(0,2,10)))
print("Abstand von sqrt(2): " + str(abs(bisection(0,2,10) - math.sqrt(2))))

print("Bisektion von f(x) = x² - 2 mit Terminierungsfall n = 15")
print("x: " + str(bisection(0,2,15)))
print("Abstand von sqrt(2): " + str(abs(bisection(0,2,15) - math.sqrt(2))))

input("Irgendeine Taste drücken zum beenden...")