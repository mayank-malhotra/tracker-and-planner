class Investment:
    def __init__(self, name: str, type: str, amount: int, annual_return_rate: float, tenure: int):
        self.name = name
        self.type = type
        self.amount = amount
        self.annual_return_rate = annual_return_rate
        self.tenure = tenure #tenure in months

    def __str__(self) -> str:
        return f"Investment: {self.name}, Type: ${self.type},  Amount: ${self.amount}, Annual Return Rate: {self.annual_return_rate}, Tenure : {self.tenure}%"

    def calculate_annual_return(self) -> float:
        return self.amount * (self.annual_return_rate / 100)

    def amount_invested(self) -> int:
        if self.type == "L":
            return "{:,}".format(round(self.amount))
        return "{:,}".format(round(self.amount * self.tenure))

    def calculate_future_value_lumpsum(self) -> int:
        future_value = self.amount * (1 + self.annual_return_rate / 100) ** self.tenure
        return "{:,}".format(round(future_value))

    def calculate_future_value(self) -> int:
        if self.type == "L":
            return self.calculate_future_value_lumpsum()
        monthly_rate = self.annual_return_rate / 12 / 100  # Convert annual rate to monthly and percentage to decimal
        future_value = (
            self.amount * 
            (((1 + monthly_rate)**self.tenure - 1) / monthly_rate) *
            (1 + monthly_rate)
        )
        return "{:,}".format(round(future_value))

    def update_amount(self, new_amount: float) -> None:
        self.amount = new_amount

    def update_annual_return_rate(self, new_rate: float) -> None:
        self.annual_return_rate = new_rate