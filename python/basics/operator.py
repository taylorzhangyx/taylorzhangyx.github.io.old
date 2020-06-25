print(100 / 3)  # -> 33.33333333336
# '//' Floor division
print(100 // 3)  # -> 33

# '**' Exponentiation
print(2 ** 10)  # -> 1024

# Logical Operators, and, or, not
# not replaces !, but != still remains the same
# and replaces &&,
# or replaces ||
if not (10 < 14 and 5 < 3 or 3 > 99):
    print("logical operators")

# Identity Operators:
# Identity operators are used to compare the objects,
# not if they are equal, but if they are actually
# the same object, with the same memory location:
# is, is not
print(1 is 1)  # -> true


class one:
    obj = 1


x = one()
y = one()
print(x is y)  # -> false
