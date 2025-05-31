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
    def Pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit type")
            print(f"Verifying security_code: {security_code}")
            self.status = "paid"
        elif payment_type =="credit":
            print("processing credit card")
            print(f"Verifying security_code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

class PaymentProcessor:
    def pay_debit(self, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        self.status = "paid"
    


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 45)
order.add_item("USB cable", 2, 50)

print(order.total_price())
order.pay("debit", "0374574")



         


