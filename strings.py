name="Damodar"
city='Tempe'
print(name + " from " + city)
print("=" * 20)
print(len(name))
print(name[0:4], name[4:])
print(city[0], city[-1])

# Daily usage methods
status = " Delivered "
print("[" + status.strip()+ "]")
print(status.strip().lower())
print("delivered".upper(), "tempe".title())
print("10-17-2026".replace("-", "/"))
print("101,Delivered,Tempe".split(","))
print(" | ".join(["a","b","c"]))
print("deliver" in "delivered", "orders.csv".endswith(".csv"))
print("deliver" not in "delivered")
status = status.strip()
print(status)

# F-Strings
name, orders, revenue = "Divya", 3, 4143.9
print(f"{name} placed {orders} orders and generated revenue of {revenue}")
print(f"{revenue:,.2f}")
print(f"{orders:05d}")
print(f"{name:<8}|{name:>8}")
print(f"{0.258:.1%}")

# 1. Print the first 3 letters of "Hyderabad". 
# 2. Turn "order_date" into "Order Date" (replace and title). 
# 3. Count the letter "a" in "Bengaluru" with .count("a").

print("Hyderabad"[0:3])
print("order_date".replace("_", " ").title())
print("Bengaluru".count("a"))