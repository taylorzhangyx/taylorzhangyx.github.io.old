x = 1

# get the type of x
print(type(x))

# check if x is a type
print(type(x) is int)  # -> True


# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type: 	bool
# Binary Types:	    bytes, bytearray, memoryview

# PEP 484 only works for static type checking
# Thus when python compile, the type checking will work
# However, at runtime, the typing is dynamically changing and the typing system is not in effect.
