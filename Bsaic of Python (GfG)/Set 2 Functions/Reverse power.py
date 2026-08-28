#Enter amount and power to calculate reverse power
n = int(input("Enter a number: "))

# reverse number
rev = int(str(n)[::-1])

# power
result = n ** rev

print(result)