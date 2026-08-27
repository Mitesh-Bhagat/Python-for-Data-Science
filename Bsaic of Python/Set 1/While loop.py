class Solution:
    def utility (self, x):
        while x >= 0:
            print(x, end = " ")
            x -= 1

if __name__ == "__main__":
    x = int(input("Enter number: "))
    obj = Solution()
    obj.utility(x)