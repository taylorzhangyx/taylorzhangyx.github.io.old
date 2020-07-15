# here n is the closure value which stores in the function
def multiplier_of(n):
    def multiplier(number):
        return number * n

    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))


# nonlocal keyword


def increment_multiplier_of(n):
    def multiplier(number):
        nonlocal n  # since closure is readonly, by using nonlocal to allow sub-functions to modify the variable
        # if nonlocal is not used here, n will be defined as a unique local variable in multiplier
        n += 1
        return number * n

    return multiplier


multiplywithn = increment_multiplier_of(5)
print(multiplywithn(9))  # 6*9
print(multiplywithn(9))  # 7*9
print(multiplywithn(9))  # 8*9
