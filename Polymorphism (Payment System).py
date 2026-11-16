# # Question 10 – Polymorphism (Payment System)

class Payment:
    def pay(self):
        print("Payment Processing")
    
class UPIPayment:
    def pay(self):
        print("Payment using UPI")

class CardPayment:
    def pay(self):
        print("Payment using Card")

a1 = Payment()
a2 = UPIPayment()
a3 = CardPayment()

a1.pay()
a2.pay()
a3.pay()