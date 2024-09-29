class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return "Нет продуктов в магазине."
                return data
        except FileNotFoundError:
            return "Файл с продуктами не найден."

    def add(self, *products):
        try:
            with open(self.__file_name, 'r+', encoding='utf-8') as file:
                existing_products = {line.split(', ')[0] for line in file}

                for product in products:
                    if product.name in existing_products:
                        print(f'Продукт {product} уже есть в магазине')
                    else:
                        file.write(str(product) + '\n')
                        print(f'Продукт {product} добавлен в магазин')
        except FileNotFoundError:
            with open(self.__file_name, 'w', encoding='utf-8') as file:
                for product in products:
                    file.write(str(product) + '\n')
                    print(f'Продукт {product} добавлен в магазин')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')


print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
