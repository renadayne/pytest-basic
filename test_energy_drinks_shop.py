from energy_drinks_shop import ShoppingCart
from energy_drinks_shop import Staff
from energy_drinks_shop import Customer
from energy_drinks_shop import Adminstrator
from staff_database import StaffDatabase
import pytest
from unittest.mock import Mock

@pytest.fixture
def cart(): 
    return ShoppingCart(10)

admin = Adminstrator()
staff_seller = Staff()
    


def test_add_energy_drinks_to_cart(cart):
    cart.add_energy_drinks_to_cart("Redbull", 5)
    cart.add_energy_drinks_to_cart("Monster", 6)
    cart.add_energy_drinks_to_cart("Haha", 2)
    cart.add_energy_drinks_to_cart("Flo", 3)
    assert cart.size_of_cart() == 2
    assert cart.total_quantity() == 11

# def check_cart_overflow():
#     for _ in range(5):
#         overfl_cart.add_energy_drinks_to_cart("Monster", 1)
#     with pytest.raises(OverflowError):
#         overfl_cart.add_energy_drinks_to_cart("Monster", 1)

def test_total_revenue():
    first_customer = Customer(30, 5000, "Rena")
    first_customer.add_energy_drinks_to_cart("Redbull", 5)
    first_customer.add_energy_drinks_to_cart("haha", 3)
    first_customer.add_energy_drinks_to_cart("Monster", 4)

    second_customer = Customer(20, 900, "Bomman") 
    second_customer.add_energy_drinks_to_cart("Monster", 5)

    third_customer = Customer(20, 0, "Jack5tr") 
    third_customer.add_energy_drinks_to_cart("PuNi", 10)
    staff_seller.auto_add_customers([first_customer, second_customer, third_customer])
    assert staff_seller.total_revenue() == 330

def test_customer_purchase():
    purchase_list = staff_seller.customer_purchase_list()
    assert type(purchase_list) == dict
    assert "Rena" in purchase_list
    assert "Aren" not in purchase_list

def test_number_customer():
    assert staff_seller.number_customer(True) == 2
    assert staff_seller.number_customer(False) == 3

# def test_check_info_staff():
#     staff_database = StaffDatabase()
#     staff_database.get = Mock(return_value= 356)
#     assert admin.== "Arghhhh"
