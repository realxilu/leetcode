# NEGATIVE NUMBER
a = 2.718
print(-a)

# FAST ARR REVERSE
a = [1, 2, 3]
print(a[::-1])

# FAST SWAP
x, y = 1, 2
x, y = y, x
print(x, y)  # 2 1

# ARRAY CONCAT
[1, 2] + [3, 4] + [5, 6, 7]

# STRING CONCAT
a = 'Hello'
b = 'World'
print(a + ' ' + b)

# ARRAY MULTIPLICATION
['Onibaba'] * 10

# LIST COMPREHENSION
['Onibaba' for _ in range(10)]

# IF-ELSE
age = 15
print('kid' if age < 18 else 'adult')

# ARRAY SLICING
nums = [1, 2, 3, 4]
start, stop = 1, 3
nums[start:stop]  # items start through stop - 1
nums[start:]      # items start through the rest of the array
nums[:stop]       # items from the beginning through stop - 1
nums[:]           # nums copy of the whole array

# MIXED OP
1 + (True)  # 2

# MATRIX TRANSPITION
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for row in matrix:
    print(row)

transposed_matrix = zip(*matrix)
for row in transposed_matrix:
    print(row)
