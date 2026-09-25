def calculate_canadian_cash():
    total_cost = 0.0

    print("Enter the prices of the items (press Enter on a blank line to finish):")

    while True:
        user_input = input("Enter price: ").strip()
        if user_input == "":
            break
            
        try:
            price = float(user_input)
            total_cost += price
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    total_pennies = round(total_cost * 100)
    remainder = total_pennies % 5
    if remainder < 2.5:
        cash_pennies = total_pennies - remainder
    else:
        cash_pennies = total_pennies + (5 - remainder)
    cash_payment = cash_pennies / 100
    print(f"Total: ${total_cost:.2f}")
    print(f"Cash payment: ${cash_payment:.2f}")
if __name__ == "__main__":
    calculate_canadian_cash()
