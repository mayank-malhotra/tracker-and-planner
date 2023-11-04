import pytest
from src.wealth_calculator import Investment


def test_calculate_annual_return():
    investment = Investment("Equity", "Stock", 1000, 5)
    assert investment.calculate_annual_return() == 50

def test_update_amount():
    investment = Investment("Equity", "Stock", 1000, 5)
    investment.update_amount(2000)
    assert investment.amount == 2000

def test_update_annual_return_rate():
    investment = Investment("Equity", "Stock", 1000, 5)
    investment.update_annual_return_rate(12)
    assert investment.annual_return_rate == 12