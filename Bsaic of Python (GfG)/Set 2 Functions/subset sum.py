#Given an array of integers, find all possible subset sums of the given array.
class Solution:
    def subsetSums(self, arr):
        result = []

        def solve(i, current_sum):
            if i == len(arr):
                result.append(current_sum)
                return

            solve(i + 1, current_sum + arr[i])
            solve(i + 1, current_sum)

        solve(0, 0)
        return result
arr = list(map(int, input("Enter elements: ").split()))

obj = Solution()
print(obj.subsetSums(arr))