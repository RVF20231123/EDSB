print ("ello")

l = [1, 2, 3, 4]
d = list(map(lambda x: x**2, l))
print(d)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)



names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

# Use zip to combine names and scores
combined = list(zip(names, scores))

print(combined)