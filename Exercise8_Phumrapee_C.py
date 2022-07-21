usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "customer" and passwordInput == "1234":
    print("----- Welcome to Phumrapee's shop -----")
    print("Please select products below")
    print("1.Watermelon X1 : 100 THB")
    print("2.Pineapple  X1 : 150 THB")
    print("3.Coke       X1 : 10 THB")
    print("---------------------------------------")
    products = int(input("Enter here: "))
    if products == 1:
        num = int(input("Enter the number of products: "))
        total = num*100
        print("---------------------------------------")
        print(f"1.Watermelon X{num} : {total} THB")
        print("---------------------------------------")
    elif products == 2:
        num = int(input("Enter the number of products: "))
        total = num*150
        print("---------------------------------------")
        print(f"1.Pineapple X{num} : {total} THB")
        print("---------------------------------------")
    elif products == 3:
        num = int(input("Enter the number of products: "))
        total = num*10
        print("---------------------------------------")
        print(f"1.Coke X{num} : {total} THB")
        print("---------------------------------------")

else:
    print("Incorrect username or password !!")