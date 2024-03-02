def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    if service_choice1 != "-":
        if service_choice2 != "-":
            total = services[service_choice1] + services[service_choice2] + base_wash
        else: total = services[service_choice1] + base_wash
    else: total = base_wash
    print(f"ZyCar Wash")
    print(f"Base car wash - $10")
    if service_choice1 != "-":
        print(f"{service_choice1} - ${services[service_choice1]}")
    if service_choice2 != "-":
        print(f"{service_choice2} - ${services[service_choice2]}")
    print(f"-----")
    print(f"Total price: ${total}")
    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
