class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def display_info(self):
        print("the name : ", self.name)
        print("the price : ", self.price)
        print("the stock : ", self.stock)
    def update_price(self, new_price):
        self.price = new_price
    def buy(self, quantity):
        if(quantity <= 0 or quantity >= self.stock):
            print("the buying not allowed with this condition")
            return
        self.stock -= quantity

product1 = Product("phone", 4000, 10)

product1.display_info()
product1.buy(2)
product1.update_price(4400)
product1.display_info()
    