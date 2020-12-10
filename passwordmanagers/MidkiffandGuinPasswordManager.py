bankPass=[]
wifiPass=[]
schoolPass=[]
entertaiment=[]
gamingPass=[]

ui=str(input("Would u like to Login In? (y/n) "))
if (ui=="y"):
    first=input("What is ur First name? ")
    last=input("What is ur Last name? ")
    User=input("What is ur Username? ")
    Pass=input("What is ur Password ")
    
while ui !="y":
    ui=str(input("Would u like to Login In? (y/n) "))


print(f'''
    Your First name is {first}
    Your Last name  is {last}
    Your UserName   is {User}
    Your Password   is {Pass}
''')
ui=input("Is this Information Correct? (y/n) ")


while  ui !="y":
    if (ui=="n"):
        first=input("What is ur First name? ")
        last=input("What is ur Last name? ")
        User=input("What is ur Username? ")
        Pass=input("What is ur Password ")

    print(f'''
        Your First name is {first}
        Your Last name  is {last}
        Your UserName   is {User}
        Your Password   is {Pass}
    ''')
    ui=input("Is this Information Correct? (y/n) ")
if (ui=="y"):
    catergory=input("What kind of Password is this? Bank(B), Wifi(W), School(S), Entertaiment(E), Gaming(G)   ")
    if (catergory=="B"):
        bankPass.append(Pass)
        print(bankPass)
    elif (catergory=="W"):
        wifiPass.append(Pass)
        print(wifiPass)
    elif (catergory=="S"):
        schoolPass.append(Pass)
        print(schoolPass)
    elif (catergory=="E"):
        entertaiment.append(Pass)
        print(entertaiment)
    elif (catergory=="G"):
        gamingPass.append(Pass)
        print(gamingPass)