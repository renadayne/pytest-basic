from typing import List

class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.sumOfQuantity = 0
        self.max_size = max_size
        self.energy_drinks = {}
        self.energy_drink_dict : dict() = {
            "Monster" : 30,
            "Redbull" : 12,
            "WakeUp" : 8,
            "PuNi" : 100
        }
        self.invalid_drinks :List[str] = []

        
    def add_energy_drinks_to_cart(self, type_of_product: str, quantity: int):
        if(type_of_product in self.energy_drink_dict):
            if type_of_product in self.energy_drinks:
                self.energy_drinks[type_of_product] += quantity
                self.sumOfQuantity += quantity
                self.energy_drinks.append(type_of_product)
            else:
                self.energy_drinks[type_of_product] = quantity
                self.sumOfQuantity += quantity
                
        else: 
            print(type_of_product + " not include in energy drink list")
            self.invalid_drinks.append(type_of_product)

    def total_quantity(self) -> int:
        return self.sumOfQuantity

    def size_of_cart(self) -> int:
        return len(self.energy_drinks)
    
    def total_value(self) -> int:
        total = 0
        for drink, quantity in self.energy_drinks.items():
            if drink in self.energy_drink_dict:
                price = self.energy_drink_dict[drink]
                total += price * quantity
        return total

class Customer(ShoppingCart):
    def __init__(self, max_size: int, amount_paid: float, customer_name: str):
        super().__init__(max_size)
        self.amount_paid = amount_paid
        self.customer_name = customer_name

    def payment(self, customerPayment: bool):
        total_amount = self.total_value()
        if self.amount_paid >= total_amount:
            change = self.amount_paid - total_amount
            if(customerPayment == True):
                print("Payment successful!")
                print("Customer:", self.customer_name)
                print("Change:", change)
            return True
        else:
            amount_due = total_amount - self.amount_paid
            if(customerPayment == True):
                print("Payment failed. Amount due:", amount_due)
            return False

    def add_to_purchase_history(self, total_amount):
        self.purchase_history[self.customer_name] = total_amount


class Staff:
    def __init__(self):
        self.customers = []

    def auto_add_customers(self, customer_list):
        self.customers.extend(customer_list)
      

    def add_customer(self, customer):
        self.customers.append(customer)
    
    def total_revenue(self):
        total = 0
        for customer in self.customers:
            if (customer.payment(False)):
                total += customer.total_value()
        return total
   
    def customer_purchase_list(self):
        purchase_list = {}
        for customer in self.customers:
            if isinstance(customer, Customer):
                if customer.payment(False):
                    total_value = customer.total_value()
                    purchase_list[customer.customer_name] = total_value
        return purchase_list
    
    def number_customer(self, check_legit: bool) -> int:
        countCustomer = 0
        if(check_legit == True):
            for customer in self.customers:
                if(customer.payment(False)):
                    countCustomer += 1
        else:
            for customer in self.customers:
                countCustomer +=1
        return countCustomer
    
class Adminstrator(Staff):
    def __init__(self):
        self.staff_name : dict()
        super().__init__()

    def check_staff_name(self, staff_id):
        staff_name = ""
        # staff_name = staff_id.get



first_customer = Customer(20, 1500, "NyNy") 
first_customer.add_energy_drinks_to_cart("Redbull", 5) 
first_customer.add_energy_drinks_to_cart("PuNi", 10) 
first_customer.add_energy_drinks_to_cart("Highlands", 3) 
first_customer.add_energy_drinks_to_cart("Starbucks", 10)

second_customer = Customer(20, 900, "Bomman") 
second_customer.add_energy_drinks_to_cart("Monster", 5)

third_customer = Customer(20, 0, "Jack5tr") 
third_customer.add_energy_drinks_to_cart("PuNi", 10)

staff = Staff()
# staff.add_customer(first_customer)
# staff.add_customer(second_customer)
# staff.add_customer(third_customer)
staff.auto_add_customers([first_customer, second_customer, third_customer])

revenue = staff.total_revenue()
purchase_list = staff.customer_purchase_list()

print("Total revenue:", revenue)
print("Customer purchase list:", purchase_list)
