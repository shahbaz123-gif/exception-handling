def check_age():
    while True:
        age_input = input("Enter your age: ")
        
        # Check if the input is a valid integer
        try:
            age = int(age_input)
        except ValueError:
            print("Error: Age must be a number. Try again.")
            continue
        
        # Check if the age is a positive number
        if age < 0:
            print("Error: Age cannot be negative. Try again.")
        else:
            break
    
    # Check if age is even or odd
    if age % 2 == 0:
        print(f"Your age ({age}) is even!")
    else:
        print(f"Your age ({age}) is odd!")

# Run the function
check_age()