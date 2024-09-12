candy_list = ["reeses", "switzerland chocolate", "twizzlers", "snickers",
              "hersheys"]
alternate_candy = candy_list[:]
cost = ["1.30$", "10.00$","3.40$", "1.30$", "1.30$"]


print("Everyone in our group would like:")
for candy in candy_list:
    print(candy.title())

candy_cost = candy_list + cost
for candy in candy_cost:
    print(candy.title())

print("If item 2 is not available then replace it with one of the new types"
      " you entered into your list.")
alternate_candy.append("air heads")
del alternate_candy[2]
print("If item 3 is not available then replace it with one of the new types"
      " you entered into your list.")
alternate_candy.append("sour patch kids")
del alternate_candy[1]

print(candy_list)
print(alternate_candy)