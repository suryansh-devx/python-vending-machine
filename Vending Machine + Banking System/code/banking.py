import random
import vendmach
import json
def start():
    def bank():
        print('')
        print('***BANK***')
    def create():
        account = []
        with open("accounts.json", "w") as file:
            json.dump([account], file)
        print('')
        print('CREATING NEW ACCOUNT.')
        print('')
        name = input('Enter your Name: ')
        id = random.choice(range(1000, 10000))
        print('')
        print('***Bank account successfully created successfully.***')
        print('Your Bank ID is:', id )
        print('Balance: 0')
        balance = 0
        print('')
        account = [id, name, balance]
        with open("accounts.json", "w") as file:
            json.dump(account, file)
    bank()
    def deposit():
        id = int(input('Enter Bank ID: '))
        with open("accounts.json", "r") as file:
            account = json.load(file)
        if id in account:
            print(' ')
            print('DETAILS')
            print('ID: ', account[0])
            print('NAME: ', account[1])
            print('BALANCE: ', account[2])
            print('')
            add = int(input('How much do you want to deposit?: '))
            balance = account[2] + add
            accounts = [account[0], account[1], balance]
            with open("accounts.json", "w") as file:
                json.dump(accounts, file)
            print('')
            print('NEW BALANCE: ', accounts[2])
        else:
            print('INVALID ID')
    def details():
        with open("accounts.json", "r") as file:
            account = json.load(file)
        print('')
        print('ACCOUNT DETAILS: ')
        print('')
        print('ID: ', account[0])
        print('NAME: ', account[1])
        print('BALANCE: ', account[2])
        print('')
    print('')
    what = int(input('What do you want to do?\n\n1. Create Account\n2. Deposit Money in Existing Account\n3. Check Account Details\n\nEnter the number: '))
    if what == 1:
        print('')
        create()
        print('')
        what = input("Do you want to deposit money now? OR Go to the Vending Machnie?('D'/'V'): ")
        if what == 'D' or what == 'd':
            deposit()
        elif what == 'V' or what == 'v':
            vendmach.start()
    elif what == 2:
        print('')
        deposit()
        print('')
        what2 = input("Do you want to go to the Vending Machine now?('Y'/'N'):")
        if what2 == 'Y':
            vendmach.start()
    elif what == 3:
        print('')
        details()
        print('')
        what2 = input("Do you want to go to the Vending Machine now?('Y'/'N'):")
        if what2 == 'Y':
            vendmach.start()
    else:
        print('')
        print('INVALID INPUT')
        start()