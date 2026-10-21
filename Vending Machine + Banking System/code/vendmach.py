import json
def start():
    with open("accounts.json", "r") as file:
        account = json.load(file)
    rem = None
    def machine():
        print('')
        print('***VENDING MACHINE***')
        print('')
    def items():
        print('Available Items: \n\n ITEM                    PRICE\n\n1. Candy                  05\n2. Doritos                20\n3. Protein Bar            45\n4. Snickers               25\n5. Popcorn                20')
        print('')
    def buying():
        with open("accounts.json", "r") as file:
            account = json.load(file)
        bid = int(input('Enter Bank ID: '))
        id = int(account[0])
        if bid == id:
            balance = int(account[2])
            print('')
            print('Account Verified')
            print('Balance: ', account[2])
            print('')
            print('What do you want?')
            item = int(input('Enter the number: '))
            if item == 1:
                print('')
                print('SELECTED: Candy')
                quan = int(input('Enter Quantity: '))
                print('')
                def candy():
                    i = 1
                    avc = 30
                    while i<=avc and i != quan+1:
                        print('Candy')
                        i+=1
                    avc-=quan
                    if avc <=0:
                        print('')
                        print('***There are no Candies left***') 
                        print('')
                        global rem 
                        rem = 0            
                reb = balance - 5*quan
                if reb <= balance and reb >=0:
                    candy()
                    accounts = [account[0], account[1], reb]
                    with open("accounts.json", "w") as file:
                        json.dump(accounts, file)
                    with open("accounts.json", "r") as file:
                        account1 = json.load(file)
                        print('')
                        print('New Balance: ', account1[2]) 
                        print('')
                else:
                    print('')
                    print('Insufficient Balance!')
                    print('')
                what = input("Do you want to buy anything else?('Y'/'N'): ")
                if what == 'Y':
                    items()
                    buying()
            elif item == 2:
                print('')
                print('SELECTED: Doritos')
                quan = int(input('Enter Quantity: '))
                print('')
                def doritos():
                    i = 1
                    avc = 30
                    while i<=avc and i != quan+1:
                        print('Doritos')
                        i+=1
                    avc-=quan
                    if avc <=0:
                        print('')
                        print('***There are no Doritos left***') 
                        print('')
                        global rem 
                        rem = 0   
                reb = balance - 20*quan  
                if reb <= balance and reb >=0:       
                    doritos()  
                    accounts = [account[0], account[1], reb]
                    with open("accounts.json", "w") as file:
                        json.dump(accounts, file)
                    with open("accounts.json", "r") as file:
                        account1 = json.load(file)
                    print('')
                    print('New Balance: ', account1[2]) 
                    print('')
                else:
                    print('')
                    print('Insufficient Balance!')
                    print('')
                what = input("Do you want to buy anything else?('Y'/'N'): ")
                if what == 'Y':
                    items()
                    buying()    
            elif item == 3:
                print('')
                print('SELECTED: Protein Bar')
                quan = int(input('Enter Quantity: '))
                print('')
                def protein():
                    i = 1
                    avc = 30
                    while i<=avc and i != quan+1:
                        print('Protein Bar')
                        i+=1
                    avc-=quan
                    if avc <=0:
                        print('')
                        print('***There are no Protein Bars left***') 
                        print('')
                        global rem 
                        rem = 0            
                reb = balance-45*quan
                if reb <= balance and reb >=0:     
                    protein()  
                    accounts = [account[0], account[1], reb]
                    with open("accounts.json", "w") as file:
                        json.dump(accounts, file)
                    with open("accounts.json", "r") as file:
                        account1 = json.load(file)
                    print('')
                    print('New Balance: ', account1[2]) 
                    print('')
                else:
                    print('')
                    print('Insufficient Balance!')
                    print('')    
                what = input("Do you want to buy anything else?('Y'/'N'): ")
                if what == 'Y':
                    items()
                    buying()               
            elif item == 4:
                print('')
                print('SELECTED: Snickers')
                quan = int(input('Enter Quantity: '))
                print('')
                def snickers():
                    i = 1
                    avc = 30
                    while i<=avc and i != quan+1:
                        print('Snickers')
                        i+=1
                    avc-=quan
                    if avc <=0:
                        print('')
                        print('***There are no Snickers left***') 
                        print('')
                        global rem 
                        rem = 0
                reb = balance-25*quan            
                if reb <= balance and reb >=0:
                    snickers()   
                    accounts = [account[0], account[1], reb]
                    with open("accounts.json", "w") as file:
                        json.dump(accounts, file)
                    with open("accounts.json", "r") as file:
                        account1 = json.load(file)
                    print('')
                    print('New Balance: ', account1[2]) 
                    print('')
                else:
                    print('')
                    print('Insufficient Balance!')
                    print('')
                what = input("Do you want to buy anything else?('Y'/'N'): ")
                if what == 'Y':
                    items()
                    buying()    
            elif item == 5:
                print('')
                print('SELECTED: Popcorn')
                quan = int(input('Enter Quantity: '))
                print('')
                def popcorn():
                    i = 1
                    avc = 30
                    while i<=avc and i != quan+1:
                        print('Popcorn')
                        i+=1
                    avc-=quan
                    if avc <=0:
                        print('')
                        print('***There are no Popcorns left***') 
                        print('')
                        global rem 
                        rem = 0            
                reb = balance-20*quan
                if reb <= balance and reb >=0:
                    popcorn()  
                    accounts = [account[0], account[1], reb]
                    with open("accounts.json", "w") as file:
                        json.dump(accounts, file)
                    with open("accounts.json", "r") as file:
                        account1 = json.load(file)
                    print('')
                    print('New Balance: ', account1[2]) 
                    print('')
                else:
                    print('')
                    print('Insufficient Balance!')
                    print('')  
                what = input("Do you want to buy anything else?('Y'/'N'): ")
                if what == 'Y':
                    items()
                    buying() 
            else:
                print('')
                print('INVALID INPUT!')
                print('')
        else:
             print('')
             print('Invalid ID')
    machine()
    items()
    buying()