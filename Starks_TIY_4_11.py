pizzas = ["pepperoni", "meat lovers", "cheese"]
friends_pizzas = pizzas[:]
for pizza in pizzas:
    print(f"My favorite pizza is {pizza}.\n")

print(f"{pizzas[0].title()} is my favorite pizza topping.")
print(f"{pizzas[1].title()} is also good.")
print(f"{pizzas[2].title()} is my least favorite type of pizza.")
print("I really like pizza.")

pizzas.append("bbq")
friends_pizzas.append("pineapple")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
