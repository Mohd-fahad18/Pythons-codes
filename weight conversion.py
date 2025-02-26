weight=float(input("enter your weight :"))
unit= input("kilogram or pouds? (K or L):")

if unit == "K":
    weight = weight*2.205
    unit="lbs."
     
elif unit == "L":
    weight = weight/2.205
    unit="kgs."

print(f"your weight is: {weight:.2f} {unit}")