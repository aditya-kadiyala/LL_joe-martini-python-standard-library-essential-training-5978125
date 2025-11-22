# the key parameter can be used to sort complex objects


class Product():
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price))

    def discount_price(self):
        return self.price - (self.price * self.discount)


prodlist = [
    Product("Widget", 50, 0.05),
    Product("Doohickey", 40, 0.15),
    Product("Thingamabob", 35, 0.0),
    Product("Gadget", 65, 0.20)
]

# TODO: use the key parameter to select a field to sort on
def sort_prod_by_price(product):
    return product.price

products_by_price = sorted(prodlist, key = sort_prod_by_price)
print(prodlist)
print(products_by_price)

# TODO: define a lambda function as the sorting key
print(sorted(prodlist, key = lambda product: product.name))

# TODO: the key parameter can also call a method on the object
print(sorted(prodlist, key = lambda product: product.discount_price()))
