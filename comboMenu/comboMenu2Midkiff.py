total=0                             #accumulative variable
krabbypattyselected=False           #flag variable
coralbitesselected=False
krabbypattymealselected=False
seafoamsodaselected=False
kelpringsselected=False
other=False
sauces=False

print(f'''
                             GALLEY GRUB
        Krabby Patty..........1.25  Krabby Meal..........3.50 
            w/sea cheese......1.50  Double Krabby Meal...3.75
        Double Krabby Patty...2.00  Triple Krabby Meal...4.00
            w/sea cheese......2.25  Salty Sea Dog........1.25
        Triple Krabby Patty...3.00  Footlong.............2.00
            w/sea cheese......3.25  Sailors Surprise.....3.00
                                    Golden Loaf..........2.00
        Coral Bits                      w/sauce..........2.50
        Small.................1.00
        Medium................1.25  Kelp Shake...........2.00
        Large.................1.50      SEAFOAM SODA
                                       Small.....1.00                              
        Kelp Rings............1.50     Medium....1.25
            salty sauce....... .50     Large.....1.50
''')

krabbypatty = input("please pick a type of krabby patty single(s) for $1.25, single w/cheese(sc) $1.50, double(d) for $2.00, double w/cheese(dc) $2.25, triple(t) for 3.00, tiple w/cheese(tc) for 3.25, krabby meal(km) for 3.50, double krabby meal(dkm) for $3.75, or tripple krabby meal(tkm) for 4.00")
#if(krabbypatty=="s" or krabbypatty=="d" or krabbypatty=="t):"
#    sandwichSelected=True
print(krabbypatty)
krabbypattyselected=True   #changes the value from false to true    
if krabbypatty == "s":  #this is krabby patty single
    total += total+1.25
elif krabbypatty == "sc": #this is krabby patty single with cheese
    total += total+1.50
elif krabbypatty == "d":   #this is double kabby patty 
    total += total+2.00
elif krabbypatty == "dc":   # this is double krabby patty with chees
    total += total+2.25
elif krabbypatty == "t":   #this is triple krabby patty 
    total += total+3.00
elif krabbypatty == "tc":   #this is triple krabby patty with cheese
    total += total+3.25
elif krabbypatty == "km":   #Krabby patty meall single
    total += total+3.50 
elif krabbypatty == "dkm":   #Double krabby patty meal
    total += total+3.75
elif krabbypatty == "tkm":   #triple krabby patty meal 
    total += total+4.00

other = input("would you like a salty sea dog(ssd) for $1.25, footlong(fl) for $2.00, Sailor Surprise(ss) for $3.00, golden loaf(gl) for $2.00, golden loaf w\sauce(gls) for $2.50 ")
other=True   #changes the value from false to true
if other == "ssd":    #salty sea dog
    total += total+1.25
elif other == "fl":    #foot long
    total += total+2.00
elif other == "ss":   #sailor surprise
    total += total+3.00
elif other == "gl":    #golden loaf
    total += total+2.00
elif other == "gls":    #golden loaf with sauce
    total += total+2.50

coralBites = input(" what size coral Bites would you like? ")
if(coralBites=="y"):
    coralBites = input("would you like a s for $1, m for $1.25, or l for $1.50? ")
    coralbitesSeleceted=True   #changes the value from false to true
if (coralBites == "s"):    #small
    total = total + 1.00
elif (coralBites == "m"):  #medium
    total = total + 1.25
elif (coralBites == "l"):  #large
    total = total + 1.50   

kelprings = input(" would you like kelp rings? ")
if(kelprings=="y"):
    coralBites = input("")
    kelpringsselected=True    #changes the value from false to true

seafoamsoda = input("would you like a seafoam soda, y or n?")
if(seafoamsoda=="y"):
    seafoamsoda=input("s for $1.00, m for $1.25, 1 for $1.50")
    seafoamsodaselected=True  #changes the value from false to true
    print("you said" ,seafoamsoda, "drink") #print (string,string,string,string,string,string,string)
if seafoamsoda == "s": #if statement  #small sea foam soda
    total += total+1.00
elif seafoamsoda == "m":  #if#medium seafoam soda
    total += total+1.25
elif seafoamsoda == "1": #large seafoam soda
    total += total+1.50

sauces = int(input(" how many sauces would you like? "))*.25
total+=sauces 

if(krabbypattyselected and seafoamsodaselected and coralbitesSeleceted and kelpringsselected and krabbypattymealselected):     #and looks for 2 true statements
#if variable==true AND variable==true AND variable==true AND variable==true
    total-=1
'''
print("you ordered a " +krabbypatty + "krabbypatty")
print("you ordered a" ,krabbypatty,"krabbypatty")
print(krabbypatty + "krabbypatty")
print(seafoamsoda + "seafoamsoda")
'''

print('Your order is a {0} krabbypatty, a {1} seafoamsoda, a {2} coralbites, {3} kelprings, {4} other, and {5} krabbypattymeal \nfor a total of '.format(krabbypatty,seafoamsoda,coralBites,other,kelprings))
 
print('''
Your order is: 
{0} krabbypatty,
{1} seafoamsoda,
{2} coralbites,
{3} kelprings,
{4} sauces
{5} other
For a total of ${4}
'''.format(krabbypatty,seafoamsoda,coralBites,kelprings,other,sauces,total))



#print("you're total is",total)
print('${:,.2f}'.format(total))   #string formatting 