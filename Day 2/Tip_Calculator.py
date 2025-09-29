print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip_percent=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_amount=bill*tip_percent/100
total_bill=bill+tip_amount
share=round(total_bill/people,2)
print(f"Each person should pay: ${share}")
