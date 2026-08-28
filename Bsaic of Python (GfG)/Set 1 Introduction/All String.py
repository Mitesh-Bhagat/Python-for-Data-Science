# Sample string
text = "String Testing in python."

# 1. len() → Length of the string
print("Length:", len(text))  # Output: 25

# 2. count() → Count occurrences of a substring
print("Count of 'T':", text.count("t"))  # Output: 3

# 3. title() → Capitalize first letter of each word
print("Title Case:", text.title())  # String Testing in Python.'

# 4. lower() → Convert to lowercase
print("Lowercase:", text.lower())  # String Testing in Python.'

# 5. upper() → Convert to uppercase
print("Uppercase:", text.upper())  # String Testing in Python.'

# 6. find() → Find first occurrence of substring
print("Find 'Python':", text.find("python"))  # Output: -1

# 7. rfind() → Find last occurrence of substring
print("Reverse Find 'Python':", text.rfind("Testing"))  # Output: 7

# 8. replace() → Replace substring with another
print("Replace 'Python' with 'Java':", text.replace("python", "Java"))
# Output: 'hello world, welcome to Java programming. Java is powerful!'