# How deque is implemented?
# Deque is a doubly linked list

from collections import deque

dq = deque("abcde")

# Iterate over the deque
for x in dq:
    print(x)

# make dq as a queue

# push
dq.append("n")
# dequeue
s1 = dq.popleft()
print(s1.upper())  # A

# make dq as stack

# push
dq.append("m")
s2 = dq.pop()
print(s2.upper())  # M

# rotate the dequeue to the right
# deque(['b', 'c', 'd', 'e', 'n'])
dq.rotate(1)
print(dq)  # deque(['n', 'b', 'c', 'd', 'e'])

# rotate the dequeue to the left
dq.rotate(-1)
print(dq)  # deque(['b', 'c', 'd', 'e', 'n'])

# add multiple elements at once
dq.extend("xyz")  # this should be a iterable
print(dq)  # deque(['b', 'c', 'd', 'e', 'n', 'x', 'y', 'z'])
