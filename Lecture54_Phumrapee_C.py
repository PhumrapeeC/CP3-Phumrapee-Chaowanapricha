def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result


def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)


def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False


def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")


def menuSelect():
    userSelected = int(input(">> "))
    return userSelected


if login() == True:
    showMenu()
    selectedMenu = menuSelect()
    if selectedMenu == 1:
        price = int(input("Price (THB) : "))
        print(vatCalculate(price))
    elif selectedMenu == 2:
        print(priceCalculate())