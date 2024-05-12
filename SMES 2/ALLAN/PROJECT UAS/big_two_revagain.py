import random
import time
from colorama import Fore, Back, Style
red = Fore.RED
Bred = Back.RED + Fore.BLACK
Bgrin = Back.GREEN + Fore.BLACK
Black = Fore.BLACK
res = Style.RESET_ALL

def CardGenerate(cl): #fungsi menghasilkan semua 52 kartu main secara otomatis
    #style = str(input("use Unicode or Alphabet for symbol? 1/2 : "))
    #if style == "1": # memilih penggunaan output yang akan digunakan untuk simbol kartu
    #    default_symbols = ['♦️', '♣️', '♥️', '♠️'] #list simbol limbol kartu (logo/Unicode)
    #elif style == "2":
    default_symbols = ['D', 'C', 'H', 'S'] #list simbol limbol kartu (alfabet)
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
    """
    print(len(p1)," : player one cards total")
    print(len(p2)," : player two cards total")
    print(len(p3)," : player three cards total")
    print(len(p4)," : player four cards total")
    print(len(cards_list)," : cards left on the dealer")
    """
    
def Play():
    print()
    time.sleep(0.3)
    print(Back.WHITE + Fore.BLACK + "Game initiating..." + res)
    time.sleep(0.3)
    print("\nYou are player number one.")
    #srtd_hand = sorted(p1.items(), key=lambda x: x[1])
    print("Here is your hand:")
    for i in p1:
        print(Fore.GREEN + f"{i}" + res)

    #putaran pertama | buang 3
    print()
    for turn in players:
        print()
        print(f"Player {players.index(turn)+1}")
        for check in turn:
            print(check)
            

### -MAIN PROGRAM- ###
p1 = {}
p2 = {}
p3 = {}
p4 = {}
cl = {} #card-list
cards_on_the_table = {}
players = [p1, p2, p3, p4] #list yang menyimpan masing-masing dictionary p1, p2, p3, p4

cards_list = CardGenerate(cl)

ShowDealerCards()
while len(cards_list) != 0:
    #ShowDealerCards()
    #print()
    GiveCard()

ShowAllPlayerCards()
Play()