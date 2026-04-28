print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

# el dinero total multiplicado por el porcentaje decimal

final_tip = float(bill) * (int(tip) / 100)
final_people = int(people) / float(final_tip)
each_people = (float(bill) + final_tip) / int(people)
print(f"Each person should pay: ${each_people:.2f}")
