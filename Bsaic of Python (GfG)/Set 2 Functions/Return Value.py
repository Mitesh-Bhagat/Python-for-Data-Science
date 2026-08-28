class ReturnValue:
    def ReturnValue(self, n):
        return 2 * n
n = int(input("Enter a number: "))
obj = ReturnValue()
print(obj.ReturnValue(n))