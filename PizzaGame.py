# 🍕 Online Pizza Shop Game

print("🔥 Welcome to our Online Pizza Shop! 🔥\n")

# Ask for pizza size
size = input("Which size pizza do you want? (M, L, XL): ").upper()

# Ask for toppings
paperoni = input("Do you want paperoni? (Y/N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

# Initialize bill
bill = 0

# Add price based on size
if size == "M":
    bill = 10
elif size == "L":
    bill = 15
elif size == "XL":
    bill = 20
else:
    print("Invalid size selected! Defaulting to M ($10)")
    bill = 10

# Add toppings price
if paperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 5

# Print final bill nicely
print("\n🧾 Here is your bill summary:")
print(f"Pizza size: {size}")
print(f"Paperoni: {'Yes' if paperoni=='Y' else 'No'}")
print(f"Extra cheese: {'Yes' if extra_cheese=='Y' else 'No'}")
print(f"💰 Total bill: ${bill}")
print("\nThank you for ordering! Enjoy your pizza 🍕")
