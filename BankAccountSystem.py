import json
passwords={}
accountinfo={}
balance=0
def store(dict,username,password):
    dict[username]=password
def accountstore(dict,username,balance):
    dict[username]=balance

def again():
    again=raw_input("Would you like to do another operation? 'y/n': ").lower()
    if again=="y":
        account()
    elif again=="n":
        logoff()
    else:
        print "Sorry. Unrecognized input. Please try again..."
        again()

def create():
    askuser=str(raw_input("Please create a username: "))
    with open("logininfo.json","r") as sp:
        passwords=json.load(sp)
    with open("accountinfo.json","r") as ai:
        accountinfo=json.load(ai)
    if askuser in passwords:
        print "Sorry. That username already exists. "
        another=raw_input("Would you like to create another username? 'y/n': ").lower()
        if another=="y":
            create()
        elif another=="n":
            exit()
        else:
            print "Unrecognized input. Please try again..."
            create()
    else:
        askpass=str(raw_input("Please create a password: "))
        reask=str(raw_input("Please confirm your password: "))
        if askpass==reask:
            store(passwords,askuser,askpass)
            accountstore(accountinfo,askuser,balance)
            with open("logininfo.json","w") as sp:
                json.dump(passwords,sp)
            with open("accountinfo.json","w") as ai:
                json.dump(accountinfo,ai)
            print "Your account has been successfully created!"
            print "Please login using your new account..."
            login()
        else:
            print "Sorry. The two passwords do not match. Please try again..."
            create()

    
def login():
    global user
    user=str(raw_input("Please enter your username: "))
    with open("logininfo.json","r") as sp:
        passwords=json.load(sp)
    if user in passwords:
        passask=str(raw_input("Please enter your password: "))
        if passwords[user]==passask:
            print "Welcome to your account",user
            account()
        else:
            print "Sorry. That was an incorrect password. Please try again..."
            login()
    else:
        print "Sorry. No account with that username was found. Please try again..."
        login()



def account():
    with open ("accountinfo.json","r") as ai:
        accountinfo=json.load(ai)
    print "What would you like to do today?"
    useropt=int(raw_input("View balace- Enter 1, Deposit money- Enter 2, Withdraw money- Enter 3, Exit- Enter 4: "))
    if useropt==1:
        print "Your current balance is:", accountinfo[user]
        again()
    elif useropt==2:
        dmoney=float(raw_input("How much money would you like to deposit?: "))
        if dmoney<100000000:
            accountinfo[user]+=dmoney
            print "Success! Your account balance is now: ",accountinfo[user]
            with open ("accountinfo.json","w") as ai:
                json.dump(accountinfo,ai)
            again()
        else:
            print "Sorry. We only allow deposits upto: 100000000"
            account()
    elif useropt==3:
        wmoney=float(raw_input("How much money would you like to withdraw?: "))
        if accountinfo[user]-wmoney >= 0:
            accountinfo[user]-=wmoney
            print "Success! Your account balance is now: ",accountinfo[user]
            with open("accountinfo.json","w") as ai:
                json.dump(accountinfo,ai)
            again()
        else:
            print "Sorry. Your account balance cannot be below 0. Please try again..."
            account()
    elif useropt==4:
        logoff()
    else:
        print "Sorry. Unrecognized input. Please try again..."
        account()

def logoff():
    print "Thanks for visiting our virtual banking system. Bye."
    exit()


def start():
    print "Welcome to our virtual banking system"
    askaccount=raw_input("Do you already have an account? 'y/n': ").lower()
    if askaccount=="y":
        login()
    elif askaccount=="n":
        create()
    else:
        print "Sorry. Unrecognized input. Please try again..."
start()
