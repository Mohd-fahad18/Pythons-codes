menu={'pizza':69,
      'popcorn':55,
      'fries':35,
      'cold drink':25}

cart=[]
total=0

print("---MENU---")
for key,value in menu.items():
    print(f"{key:10} : ${value:2f}")

while True :
    food= input(" entre the item (q to quit) :")
    if food == "q":
        break
    elif menu.get(food) :
        cart.append(food)

print("---YOUR ORDER---")
for food in cart :
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is : ${total : .2f}")