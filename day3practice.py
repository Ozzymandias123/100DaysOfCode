# Pizza order

'''
Based on a user's order, work out their final bill. Use the input() function
to get a user's preferences and then add up the total for their
order and tell them how much they have to pay.

Small pizza (S) $15
Medium pizza (M) $20
Large pizza (L) $25

Add pepperoni for small pizza (Y or N) +$2
Add pepperoni for medium pizza (Y or N) +$3
Add extra cheese for any size pizza (Y or N)  +$1

Print "Welcome to Python Pizza Deliveries"
Propmt the user input "What size pizza do you want? S, M or L: "

If user size is S
   Display

'''

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza?: Y or N: ")
extra_cheese = input("Do you want wxtra cheese? Y or N: ")
bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
    else:
        print("You typed the wrong input.")

if extra_cheese == "y":
    bill += 1

print(f"The final bill is: {bill}")


# todo: work out how much they need to pay based on their size choice

# todo: work out how much to add to their bill based on their pepperoni choice.
# todo: work out their final amount based on whether if they want extra cheese
