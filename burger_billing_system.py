menu_items = [
    ("aloo tikki", 5),
    ("maharaja", 10),
    ("mac special", 15)
]


def display_menu(menu_items):
    print("Sr.   Name              Price")
    print("------------------------------")
    for sr, item in enumerate(menu_items, start=1):
        name, price = item
        print(f"{sr}.   {name:<15} {price:>5}$")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(menu_items):
                return choice
            else:
                print(f"Please enter a number between 1 and {len(menu_items)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def is_student():
    while True:
        student_status = input("Are you a student? (yes/no): ").strip().lower()
        if student_status in ['yes', 'no']:
            return student_status == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def wants_delivery():
    while True:
        delivery_status = input("Do you want delivery? (yes/no): ").strip().lower()
        if delivery_status in ['yes', 'no']:
            return delivery_status == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def wants_tip():
    while True:
        tip_status = input("Do you want to add a tip? (yes/no): ").strip().lower()
        if tip_status in ['yes', 'no']:
            return tip_status == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def get_tip_amount():
    while True:
        try:
            print("\nSelect a tip amount:")
            print("1. $2")
            print("2. $5")
            print("3. $10")
            print("4. Enter custom amount")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                return 2.00
            elif choice == 2:
                return 5.00
            elif choice == 3:
                return 10.00
            elif choice == 4:
                while True:
                    custom_tip = float(input("Enter your custom tip amount: "))
                    if custom_tip >= 0:
                        return custom_tip
                    else:
                        print("Tip amount must be non-negative.")
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def apply_delivery_charge(total_cost):
    """Apply a 5% delivery charge if the user wants delivery."""
    delivery_rate = 0.05  # 5% delivery charge
    delivery_charge = total_cost * delivery_rate
    total_cost += delivery_charge
    return delivery_charge, total_cost


def calculate_final_cost(item_cost, quantity, student, delivery, tip):
    subtotal = item_cost * quantity
    if student:
        discount = 0.20  # 20% discount
        discount_amount = subtotal * discount
        subtotal -= discount_amount
    else:
        discount_amount = 0

    delivery_charge = 0
    if delivery:
        delivery_charge, subtotal = apply_delivery_charge(subtotal)

    if tip > 0:
        subtotal += tip

    return subtotal, discount_amount, delivery_charge, tip


def handle_choice(choice, menu_items):
    name, price = menu_items[choice - 1]
    quantity = get_quantity()
    student = is_student()
    delivery = wants_delivery()
    tip = 0
    if wants_tip():
        tip = get_tip_amount()

    final_amount, discount_amount, delivery_charge, tip = calculate_final_cost(price, quantity, student, delivery, tip)

    # Print final bill
    print("\n****************** Final Bill **********************")
    print(f"Sr.    Name           Price    Quantity    Total Price")
    print(f"1.     {name:<15} {price:>1}$   {quantity:>5} {price * quantity:>16.2f}$")
    print("-" * 50)
    print(f"{'':>40}{price * quantity:>10.2f}$")  # Subtotal

    if student:
        print(f"Student discount 20%{'':>22}{-discount_amount:>7.2f}$")

    if delivery:
        print(f"Delivery charge 5%{'':>24}{+delivery_charge:>7.2f}$")

    if tip > 0:
        print(f"Tip{'':>39}{+tip:>7.2f}$")

    print("-" * 50)
    print(f"Total bill{'':>31}{final_amount:>7.2f}$")
    print("\nThank you and come again")


def main():
    while True:
        display_menu(menu_items)
        choice = get_user_choice()
        handle_choice(choice, menu_items)

        another_order = input("Would you like to place another order? (yes/no): ").strip().lower()
        if another_order != 'yes':
            print("Thank you for your order!")
            break


main()
