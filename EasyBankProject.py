users = ["User"]
passwords = ["Userpass"]
balances = [1000]
def bankuser():
    userreg = input("Enter your username: ")
    if userreg == users[0]:
        passreg = input("Enter your password: ")
        if passreg == passwords[0]:
            print("Succsesful")
            print()
        else:
            print("Something went wrong")
            print()
            bankuser()
    else:
        bankuser()
def withdraw():
    askhowmuch = float(input("How much do you want to withdraw?: $"))
    if askhowmuch >= balls[0]:
        print("You cannot withdraw more than you have.")
        print()
    elif askhowmuch >= 0:
        balls[0] -= askhowmuch
        print("Success!")
        print()
        return
    else:
        print("Something went wrong.")

def sendmoney():
    askhowmuch = float(input("How much do you want to receive?: $"))
    if askhowmuch >= 0:
        balls[0] += askhowmuch
        print("Success!")
        print()
        return
    else:
        print("Something went wrong.")

def viewstat():
    print(f"Your ballance: ${balls[0]}")

def menu():
    while True:
        print("Pick something!")
        print("1. Withdraw")
        print("2. Receive money")
        print("3. View my balance")
        print("0. Leave")
        choice = input("I pick: ")
        if choice == "1":
            withdraw()
        elif choice == "2":
            sendmoney()
        elif choice == "3":
            viewstat()
        elif choice == "0":
            break


def runprog():
    bankuser()
    menu()

if __name__ == "__main__":
    runprog()