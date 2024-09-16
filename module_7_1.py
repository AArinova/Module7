#from pprint import pprint

class Product:

    def __init__(self, p_name: str, p_weight: float, p_category: str):
        self.name = p_name
        self.weight = p_weight
        self.category = p_category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'

class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_list = file.read()
        file.close()
        return products_list #str

    def add(self, *products):
        in_shop_list = self.get_products()
        for item in products:
            if item.name in in_shop_list:
                print(f'Продукт {item.name} уже есть в магазине.')
            else:
                with open(self.__file_name, "a") as f:
                    print(item, file=f)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
