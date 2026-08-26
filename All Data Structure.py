import array

# 1️⃣ ARRAY (fixed type)
arr = array.array('i', [10, 20, 30, 50, 70, 80])
arr.append(55)      # Insert last
arr.insert(3, 15)   # Insert specific
arr.pop()           # Remove last
arr.remove(20)      # Remove specific
print("\nArray:", arr)

# 2️⃣ LIST (ordered, mutable)
lst = [1, 2, 3, 4]
lst.append(5)
lst.extend([6, 7])
lst.insert(2, 99)
lst.remove(3)
lst.pop()
lst[0] = 100        # Update
print("\nList:", lst)
print("Slice:", lst[1:4])
print("Reversed:", lst[::-1])
print("Sorted:", sorted(lst))

# 3️⃣ TUPLE (ordered, immutable)
tup = (10, 20, 30, 40)
print("\nTuple:", tup)
print("Index of 30:", tup.index(30))
print("Count of 20:", tup.count(20))
print("Slice:", tup[1:3])

# 4️⃣ SET (unordered, unique)
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.remove(2)
s.discard(10)       # No error if not found
s.pop()             # Removes random element
print("\nSet:", s)
print("Union:", s.union({7, 8}))
print("Intersection:", s.intersection({3, 4}))
print("Difference:", s.difference({1, 5}))

# 5️⃣ DICTIONARY (key-value)
d = {"name": "Mitesh", "age": 21}
d["course"] = "Computer Engineering"
d.update({"skills": ["Python", "Cybersecurity"]})
d.pop("age")
print("\nDictionary:", d)
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))
print("Get:", d.get("name"))
print("Default Get:", d.get("grade", "Not Found"))