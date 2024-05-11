import random
from colorama import Fore, Back, Style
red = Fore.RED
Bred = Back.RED + Fore.BLACK
Bgrin = Back.GREEN + Fore.BLACK
Black = Fore.BLACK
res = Style.RESET_ALL

cards_list = {}

def CardGenerate(): #method menghasilkan semua 42 kartu main secara otomatis
    default_symbols = ['D', 'C', 'H', 'S'] #list simbol limbol kartu yaitu Diamond, Clove, Hearten, dan Spaids
    l = 1
    for i in default_symbols:   
        for j in range(1, 14):
            cards_list[i+str(j)] = l
            l = l + 1
    for ut in cards_list:
        print(f"{ut} : {cards_list[ut]},")
    return cards_list

def TestPlay(): #method untuk test keribilitas value kartu
    tmp = random.choice(list(cards_list))
    ply = input(f"right now {tmp} is on the table \nwhat card to put? ")
    try:
        if cards_list[ply] > cards_list[tmp]:
            print(Bgrin + "win" + res)
        elif cards_list[ply] < cards_list[tmp]:
            print(Bred + "loose" + res,)
        elif cards_list[ply] == cards_list[tmp]:
            print("cheat")
        print(f"\nresult : \non the table = {tmp} with a value of {cards_list[tmp]} \nthrown = {ply} with a value of {cards_list[ply]}")
    except:
        print(f"cardo no existo ({ply})")



def shufle(cards):
    pass

#Main program 
p1 = {}
p2 = {}
p3 = {}
p4 = {}
players = [p1, p2, p3, p4]

#generate cards and printing the resulted cards
CardGenerate()
for ut in cards_list:
    print(f"{ut} : {cards_list[ut]},")

#before shuffle
print("\nmain program out before shufle()", p1, p2, p3, p4)

#after shuffle
print("\nmain program out after shufle()", p1, p2, p3, p4)

#print all card hands for each players
print("in other words :")
for okok in players:
    print(okok)
    print()
print("p1 : ",len(list(p1)))
print("p2 : ",len(list(p2)))
print("p3 : ",len(list(p3)))
print("p4 : ",len(list(p4)))

