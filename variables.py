# 1. Store a product name, its price and a quantity, then print the total cost. 
# 2. Swap the values of two variables without a third one. 
# 3.Print type(10), type(10.0) and type("10"). Why are they different?

product_name = "Laptop"
price = 999.99
quantity = 2
total_cost = price * quantity
print("Total cost for", quantity, product_name + "s is:", total_cost)

a, b = 5, 10
a, b = b, a
print("After swapping: a =", a, ", b =", b)

print(type(10))      
print(type(10.0)) 
print(type("10"))  
print(type(True)) 