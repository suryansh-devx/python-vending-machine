import banking
import vendmach 
def init():
    print('  ')
    print('***This is a Vending Machine + Banking System.***\n***Here you can create a bank account, deposit money and buy items from the vending machine using the account.***')
    print('  ')
    goto = input("What do you want to do? To go to the Bank, enter 'BN', to go to the Vending Machine, enter 'VM': ")
    if goto == 'BN' or goto =='bn':
        banking.start()
    elif goto == 'VM' or goto == 'vm':
        vendmach.start()
    else:
        print("***Invalid Input***")

init()