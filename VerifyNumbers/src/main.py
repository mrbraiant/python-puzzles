def validating_numbers(start_number: int, end_number: int) -> None:
    for number in range(start_number, end_number):
        if number % 3 == 0 and number % 5 == 0:
            print("ThreeFive")
        elif number % 3 == 0:  # Check if the number is a multiple of 3
            print("Three")
        elif number % 5 == 0:
            print("Five")
        else:
            print(number)
    print("Validated successfully")
    

def print_numbers() -> None:
    # Loop through numbers 1 to 100 (inclusive)
    validating_numbers(1, 101)
    

# Call the function to execute
print_numbers()
