# sorting stability guarantees that objects with the same key will
# have their order preserved even after the data is sorted


class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discountPrice(self):
        return self.price - (self.price * self.discount)


prodlist = [
    Product("Doohickey", 40, 10, 0.15),
    Product("Widget", 50, 10, 0.05),
    Product("Doohickey", 40, 8, 0.15),
    Product("Thingamabob", 35, 12, 0.0),
    Product("Gadget", 65, 7, 0.20)
]

print(sorted(prodlist, key=lambda p: p.price))

# TODO: sort by two different keys, taking advantage of stability
sorted_by_weight = sorted(prodlist, key = lambda product: product.weight)
print(prodlist)
print(sorted_by_weight)
print(sorted(sorted_by_weight, key = lambda p: p.price, reverse = True))

# See sortoperators file for different way(operator module) instead of using lambda functions