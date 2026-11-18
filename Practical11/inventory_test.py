import pytest
from inventory import calculate_total_price, apply_discount, check_stock

def test_calculate_total_price():
    assert calculate_total_price(500, 4) == 2000
def test_apply_discount():
    assert apply_discount(2000, 10) == 200
def test_check_stock():
    check_stock(10, 5) == "Stock is available"
def test_calculate_total_price_neg():
    with pytest.raises(ValueError):
        calculate_total_price(-100, 10)
def test_invalid_disc():
    with pytest.raises(ValueError):
        apply_discount(2000, 110)
def test_neg_disc():
    with pytest.raises(ValueError):
        apply_discount(2000, -10)
def test_unavailable_stock():
    with pytest.raises(ValueError):
        check_stock(10, 18)
