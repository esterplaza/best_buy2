import pytest
from products import Product


def test_creating_normal_product():
    assert Product("test_name", price=1450, quantity=100)


def test_creating_product_with_invalid_details_result_exception():
    with pytest.raises(ValueError,
                       match="Invalid name, name should not be empty!"):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError,
                       match="Invalid value, negative values are not allowed!"):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_when_product_reaches_0_quantity_result_inactive():
    test_product = Product("test_name", price=1450, quantity=0)
    assert test_product.is_active() is False
    test_product2 = Product("test_name2", price=1400, quantity=100)
    test_product2.buy(100)
    assert test_product2.is_active() is False


def test_buy():
    test_product = Product("test_name", price=1450, quantity=100)
    test_product.buy(50)
    assert test_product.get_quantity() == 50


def test_buy_larger_quantity_result_exception():
    test_product = Product("test_name", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Error while making order! Quantity larger than what exists."):
        test_product.buy(150)
