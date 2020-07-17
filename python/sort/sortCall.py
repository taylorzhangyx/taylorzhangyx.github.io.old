class A:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{{l: {self.left}, r: {self.right}}}"


template1 = [4, 3, 7, 2, 3, 1, 8, 0, 2]
template2 = [(1, 2), (4, 2), (9, 32), (2, 12), (32, 23)]
template3 = [
    A(2, 3),
    A(4, 1),
    A(5, 9),
    A(3, 7),
    A(2, 9),
    A(8, 5),
]

print(template1)
print(template2)
print(template3)


t1 = sorted(template1)
t2 = sorted(template2, key=lambda tup: tup[0])
t3 = sorted(template3, key=lambda a: a.left)

print(t1)
print(t2)
print(t3)

# sort will sort the tuple by the first element
print("t2", template2)
template2.sort()
print("t23", template2)
