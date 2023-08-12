def simple_calculator():
    print("Welcome to Simple calc") 
    # contin = False
    total = 0
    to_continue = input("would you like to start, press c to conitnue or q to quit\n")
    while(to_continue != "q"):
        # total = 0
        if to_continue == "c":
            first_num = int(input("choose a number: "))
            # op = {1:"+", 2:"-", 3:"*",4:"/"}
            user_input = int(input("Select an operation, \n 1 : + \n 2: - \n 3 : *\n 4 : \ \n"))
            sec_num = int(input("choose a second number \n"))
            if user_input == 1:
                total = first_num + sec_num
                print(total)
            elif user_input == 2: 
                total = first_num - sec_num
                print("Your current total: ", total)
            elif user_input == 3: 
                total = first_num * sec_num
                print(total)
            elif user_input == 4: 
                total = first_num / sec_num
                print(total)
            # print(total)
        else: 
            print("Invalid choice")
        to_continue = input("Would you like to continue, press c to conitnue or q to quit \n") 
    print("Final Total:", total)
    print("Thank you bye!")
simple_calculator()