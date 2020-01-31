# pizza.py
number_of_pizzas = eval(input("how many pizzas do you want"))
cost_per_pizza = eval(input("how much pizza"))
subtotal = number_of_pizzas * cost_per_pizza
tax = subtotal * 0.08
total = subtotal + tax
print("your total is", total)
