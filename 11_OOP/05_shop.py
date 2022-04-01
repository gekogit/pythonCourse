"""
5▹ Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.
"""


class Product:

    def __init__(self, name, color, prise):
        self.name = name
        self.color = color
        self.prise = prise

    def __repr__(self):
        return f'{self.name} -- {self.color} -- {self.prise}$'


class Shop:
    sold = []

    def __init__(self, products):
        self.products = products

    def show(self):
        print("\n\nShop items:")
        for product in self.products:
            print(product)
        if len(self.sold) > 0:
            print('\nAlready sold:')
            for el in self.sold:
                print(el)

    def try_product(self, index):
        print(20*'*')
        print(f'Try: {self.products[index]}')

    def buy_product(self, index):
        print(20 * '*')
        print(f'Bought: {self.products[index]}')
        self.sold.append(self.products.pop(index))

    def return_product(self, index):
        print(20 * '*')
        print(f'Returned: {self.sold[index]}')
        self.products.append(self.sold.pop(index))


def main():
    p1 = Product('beret', 'braun', 15)
    p2 = Product('cowboy', 'black', 230)
    p3 = Product('cloche', 'red', 43)

    hat_land = Shop([p1, p2, p3])
    hat_land.show()
    hat_land.try_product(1)
    hat_land.buy_product(1)
    hat_land.show()
    hat_land.return_product(0)
    hat_land.show()


if __name__ == '__main__':
    main()
