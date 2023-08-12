def simple_calculator():
    operations = {
                "+" : lambda a,b: a + b,
                "-" : lambda a,b: a - b,
                "*" : lambda a,b: a * b,
                "/" : lambda a,b: a / b if b != 0 else None }

    print("Welcome to Simple calc")
    
    to_continue = input("Would you like to start? Press 'c' to continue or 'q' to quit\n")

    while to_continue != "q":
        if to_continue == "c":
            first_num = float(input("Choose a number: "))
            user_input = input("Select an operation, +, -, *, or /\n")
            sec_num = float(input("Choose a second number:\n"))
            if user_input in operations:
                total = operations[user_input](first_num, sec_num)  
                if total is not None:
                    print("Total:", total)
        
            else: 
                print("Invalid operation")
        else:
            print("Invalid choice")

        to_continue = input("Would you like to continue? Press 'c' to continue or 'q' to quit\n")

    print("Thank you, goodbye!")

simple_calculator()
