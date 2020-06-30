nums = range(20)

# list
l1 = [x for x in nums]
print(f"l1={l1}")

# square list
l2 = [x ** 2 for x in l1]
print(f"l2 = {l2}")

# conditional list
l3 = [x for x in l2 if x % 2 == 1]
print(f"l3 = {l3}, type is {type(l3)}")

# conditions are logical and
l4 = [x for x in l3 if x % 2 == 1 if x % 3 == 0]
# is equivalent to l4 = [x for x in l3 if x % 2 == 1 and x % 3 == 0]
print(f"l4 = {l4}")

# generator - parentheses
t1 = (x for x in nums)
print(f"{type(t1)}")
print(t1)

# dict - curly brackets
d1 = {x: x for x in nums}
print(d1)

# access the k,v
d2 = {x: y * y for x, y in d1.items()}
print(f"d2 = {d2}")
