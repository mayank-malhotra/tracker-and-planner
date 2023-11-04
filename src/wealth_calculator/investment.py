class Investment:
    def __init__(self, name, investment_type, amount, annual_return_rate):
        self.name = name
        self.investment_type = investment_type
        self.amount = amount
        self.annual_return_rate = annual_return_rate

    def __str__(self):
        return f"Investment: {self.name}, Type: {self.investment_type}, Amount: ${self.amount}, Annual Return Rate: {self.annual_return_rate}%"

    def calculate_annual_return(self):
        return self.amount * (self.annual_return_rate / 100)

    def update_amount(self, new_amount):
        self.amount = new_amount

    def update_annual_return_rate(self, new_rate):
        self.annual_return_rate = new_rate