foods=[]
prices=[]
total=0
while True:
    food=input("entre food to buy (q to quit)")
    if food=="q":
        break

    else:
        price=float(input(f"entre the price of {food}: $"))
        foods.append(food)
        prices.append(price)
    
print("---YOUR CART---")
for food in foods:
    print(food)

for price in prices:
    total+= price

print()
print(f"your total is :{total}")
print("\nTHANK YOU !")

