# QUEUE
from collections import deque
q = deque()  # thread-safe

try:
    q.append(1)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
except:
    print('exception thrown')

# STACK
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
try:
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
except:
    print('exception thrown')

# HASHMAP/DICTIONARY
dic = {}
dic['a'] = 'alex'
dic['b'] = 'bob'
dic['c'] = 'charie'

print(dic['a'])
print(dic['b'])
print(dic['c'])
print(dic.get('a'))
print(dic.get('a', '-1000'))
# if the key doesn't exist return a default value
print(dic.get('z', '-1000'))

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

# int values need conversion
for k, v in dic.items():
    print(k + ' -> ' + v)

# --------------------
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

1 + (True) #2 
