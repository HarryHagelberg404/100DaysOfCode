print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n"))

bill_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?\n")) / 100

total_people = int(input("How many people to split the bill?\n"))

total_sum = ((total_bill * bill_percentage) + total_bill) / total_people

print(f"Each person should pay: {round(total_sum, 2)} swedish crowns for their respective dinner.")

