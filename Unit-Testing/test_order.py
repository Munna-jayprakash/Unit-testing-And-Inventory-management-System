import pytest 
from order import (calculate_discount,calculate_gst,calculate_ordeer_total)

def test_calculate_discount():
    assert calculate_discount(1000,10)==100
def test_calculate_gst():
    assert calculate_gst(1000,18)==180
def test_calculate_order_total():
    assert calculate_ordeer_total(1000,10,18)==1062
def test_zero_discount():
    assert calculate_discount(0,0)==0
def test_neg_price():
    with pytest.raises(ValueError):
        calculate_discount(-100,10)
def test_invalid_disc():
    with pytest.raises(ValueError):
        calculate_discount(1000,120)