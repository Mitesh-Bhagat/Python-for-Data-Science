import math

n = int(input("Enter number: "))

while True:
    print(n, end=" ")
    
    if n == 1:
        break
    
    if n % 2 == 0:
        n = int(math.sqrt(n))
    else:
        n = int(math.pow(n, 1.5))