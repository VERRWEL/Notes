import random
from colorama import Fore, Back, Style
red = Fore.RED
Bred = Back.RED + Fore.BLACK
Bgrin = Back.GREEN + Fore.BLACK
Black = Fore.BLACK
res = Style.RESET_ALL

def CardGenerate(cl): #method menghasilkan semua 42 kartu main secara otomatis
    default_symbols = ['D', 'C', 'H', 'S'] #list simbol limbol kartu yaitu Diamond, Clove, Hearten, dan Spaids
    l = 1
    for i in default_symbols:   
        for j in range(1, 14):
            cl[i+str(j)] = l
            l = l + 1
    return cl

def ShowDealerCards(): #method untuk menunjukkan semua kartu yang ada
    for i in cards_list:
        print(f"{i} : {cards_list[i]}")

def GiveCard(): #method tuntuk membagikan kartu pada masing-masing pemain seacra acak
    choose_player = random.choice(list(players))
    if len(list(choose_player)) == 13:
        GiveCard()
    else:
        choose_card = random.randint(0, len(cards_list))
        try:
            choose_player[list(cards_list)[choose_card]] = cards_list[list(cards_list)[choose_card]]
            cards_list.pop(list(cards_list)[choose_card])
        except:
            print()

def ShowAllPlayerCards():
    print(f"{Fore.GREEN}PLAYER 1 : {list(p1)} \n{Fore.BLUE}PLAYER 2 : {list(p2)} \n{Fore.MAGENTA}PLAYER 3 : {list(p3)} \n{Fore.YELLOW}PLAYER 4 : {list(p4)}{res}")
    print(len(p1)," : player one cards total")
    print(len(p2)," : player two cards total")
    print(len(p3)," : player three cards total")
    print(len(p4)," : player four cards total")
    print(len(cards_list)," : cards left to give")

def Play():
    pass

### -MAIN PROGRAM- ###
p1 = {}
p2 = {}
p3 = {}
p4 = {}
cl = {} #card-list
players = [p1, p2, p3, p4] #list yang menyimpan masing-masing dictionary p1, p2, p3, p4

cards_list = CardGenerate(cl)

while len(cards_list) != 0:
    ShowDealerCards()
    print()
    GiveCard()

ShowAllPlayerCards()