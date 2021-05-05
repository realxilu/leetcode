# negative number
a = 2.718
print(-a)

# fast arr reverse
a = [1, 2, 3]
print(a[::-1])

# fast swap
x, y = 1, 2
x, y = y, x
print(x, y)  # 2 1

# array concat
[1, 2] + [3, 4]

# string concat
a = 'Hello'
b = 'World'
print(a + ' ' + b)

# ['Onibaba', 'Onibaba', ... 'Onibaba']
['Onibaba'] * 10

# list comprehension
['Onibaba' for _ in range(10)]

# if-else one liner
age = 15
print('kid' if age < 18 else 'adult')

# array manipulation
nums = [1, 2, 3, 4]
start, stop = 1, 3
nums[start:stop]  # items start through stop - 1
nums[start:]      # items start through the rest of the array
nums[:stop]       # items from the beginning through stop - 1
nums[:]           # nums copy of the whole array

1 + (True)  # 2

# dictionary dic['stuff'] vs dic.get('stuff')
dic = {}
dic['a'] = 1
dic['b'] = 2

print(dic['a'])
print(dic['b'])
print(dic.get('c'))
print(dic['c'])
