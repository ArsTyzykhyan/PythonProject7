from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        products = []
        with open(self.__file_name, 'r') as f:
            for line in f:
                products.append(line.strip())
        return products

    def add(self, *products):
        for product in products:
            with open(self.__file_name, 'r') as f:
                for line in f:
                    if product.name == line.split(',')[0]:
                        print(f'Продукт {product.name} уже есть в магазине')
                        break
                else:
                    with open(self.__file_name, 'a') as f:
                        f.write(f'{product}\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())