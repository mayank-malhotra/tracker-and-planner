from src.wealth_calculator.investment import Investment

def get_investment_details():
    print("Enter SIP investment details: ")
    investment_name = input("Enter investment type (e.g., Stocks): ")
    investment_type = input(" Choose investment type between SIP(S) and Lumpsum(L): ")
    if investment_type not in ["S", "L"]:
        raise ValueError("Invalid investment type. Please choose between SIP(S) and Lumpsum(L)")
    elif investment_type == "L":
        amount = float(input("Enter one time investment amount: "))
        rate_of_return = float(input("Enter Annual rate of return you are expecting(in %): "))
        tenure = float(input("Enter tenure in years you want to withdraw: "))
        return Investment(investment_name, investment_type, amount, rate_of_return, tenure)
    amount = float(input("Enter investment amount per month: "))
    rate_of_return = float(input("Enter Annual rate of return you are expecting (in %): "))
    tenure = float(input("Enter tenure in months you want to do investment: "))
    return Investment(investment_name, investment_type, amount, rate_of_return, tenure)

def main():
    investment = get_investment_details()
    amount_invested = investment.amount_invested()
    print(f"Investment you made: {amount_invested}")
    future_value = investment.calculate_future_value()
    if investment.type == "L":
        print(f"You will get: {future_value} after {investment.tenure} years")
    else: print(f"You will get: {future_value} after {investment.tenure} months")

if __name__ == "__main__":
    main()
