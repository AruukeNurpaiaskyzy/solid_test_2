from abc import ABC, abstractmethod
class Order:
    items = []
    quantities = []
    prices = []
    status = "open"
    def add_item(self, items, quantity, price):
        self.items.append(items)
        self.quantities.append(quantity) 
        self.prices.append(price)
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities [i] * self.prices[i]
            return total
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, secutiy_code):
        pass
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order ):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"
    


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 45)
order.add_item("USB cable", 2, 50)

print(order.total_price())
processor = PaypalPaymentProcessor('jhbdjfn@gmail.com')
processor.pay(order)



         


