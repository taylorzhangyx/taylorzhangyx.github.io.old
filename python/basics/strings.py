# % can be used to format strings:
x = "%s can be %s" % ("strings", "interpolated")
print(x)
# => 'strings can be interpolated'

# A newer, preferred way to format strings is the format method.
"{0} can be {1}".format("strings", "formatted")
# => 'strings can be formatted'
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
# => 'Bob wants to eat lasagna'
