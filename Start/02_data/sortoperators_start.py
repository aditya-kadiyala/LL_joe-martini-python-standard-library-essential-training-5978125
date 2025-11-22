# the key parameter can be used to sort complex objects
from operator import attrgetter, methodcaller, itemgetter


class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discount_price(self):
        return self.price - (self.price * self.discount)


prodlist = [
    Product("Widget A", 50, 10, 0.05),
    Product("Widget B", 40, 8, 0.15),
    Product("Widget C", 35, 12, 0.0),
    Product("Widget D", 65, 7, 0.20),
    Product("Widget E", 70, 7, 0.12)
]


# TODO: the operator module functions provide easy ways to select fields
# attrgetter() retrieves a given attribute or property from an object
# itemgetter() retrieves an item at a given index in a collection
# methodcaller() calls the given method on the object

print("Using the attrgetter method:")
# print(prodlist)
# print(sorted(prodlist, key = attrgetter("weight")))
# print(sorted(prodlist, key = attrgetter("weight"), reverse=True))
# print()
# print(prodlist)
# print(sorted(prodlist, key = attrgetter("name")))
# print(sorted(prodlist, key = attrgetter("name"), reverse=True))
# print()
# print(prodlist)
# print(sorted(prodlist, key = attrgetter("weight")))
# print(sorted(prodlist, key = attrgetter("weight", "price"), reverse=True))

print("Using methodcaller to invoke a method:")
# print(prodlist)
# print(sorted(prodlist, key = methodcaller("discount_price")))
# print(sorted(prodlist, key = methodcaller("discount_price"), reverse=True))

# TODO: Use itemgetter to retrieve an index from a tuple or list
inventory = [("Widget A", 5), ("Widget C", 2), ("Widget B", 4),
             ("Widget D", 7), ("Widget E", 4)]

print("Using itemgetter to invoke a method:")
print(inventory)
print()
print(sorted(inventory, key = lambda item : item[0]))
print(sorted(inventory, key = itemgetter(0)))
print()
print(sorted(inventory, key = lambda item : item[1]))
print(sorted(inventory, key = itemgetter(1)))


