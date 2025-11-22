# String formatting methods and best practices
from string import Template
import datetime

# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
# print(the_str)
# print(the_template.substitute(animal = "fox", action = "jumped"))

# args = {
#   "animal": "cow",
#   "action": "walked"
# }
# print(the_template.substitute(args))

# TODO: Using str.format()
str1 = "foo"
val1 = 123

print("Output: Value of {} is {}.".format(str1, val1))
print("Output: {1} is the value of {0}.".format(str1, val1))
print("Output: HEX Value of {var2}({var1}) is {var1:x} or {var1:X}.".format(var2 = str1, var1 = val1))



# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07

# Modernized way of formatting string unlike 21, 22, 23
nyd = datetime.datetime(2026, 1, 1)
print(f"{product.upper()} has a price of {price}, with tax {tax:.2%} the total is {round(price + (price * tax), 2)}")
print(f"but only on {nyd: %B %d %Y}")