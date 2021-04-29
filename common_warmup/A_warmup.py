# quick reverse
a = [1, 2, 3]
print(a[::-1])

# quick swap
x, y = 1, 2
x, y = y, x
print(x, y) # 2 1

# stack
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
    print('pop empty')

# queue
