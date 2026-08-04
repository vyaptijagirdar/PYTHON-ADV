class PaymentStrategy:
    def pay(self, amount):
        pass  # Base method to override


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy  # Store payment method

    def set_strategy(self, strategy):
        self.strategy = strategy  # Change payment method

    def pay(self, amount):
        self.strategy.pay(amount)  # Use selected strategy to pay


# Create payment strategies
credit = CreditCardPayment()
paypal = PayPalPayment()

# Use Credit Card
payment = PaymentContext(credit)
payment.pay(1000)

# Change to PayPal
payment.set_strategy(paypal)
payment.pay(500)
