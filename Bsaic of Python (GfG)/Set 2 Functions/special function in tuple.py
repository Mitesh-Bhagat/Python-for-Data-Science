list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Step 1
zipped = list(zip(list1, list2))
print(zipped)

# Step 2 → only even from list1
filtered = list(filter(lambda x: x % 2 == 0, list1))
print(filtered)

# Step 3 → multiply by 2
mapped = list(map(lambda x: x * 2, filtered))
print(mapped)   