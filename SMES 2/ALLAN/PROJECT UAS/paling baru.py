import random
import time
try:
    from colorama import Fore, Back, Style
    red = Fore.RED
    fgreen = Fore.GREEN
    Black = Fore.BLACK
    fblue = Fore.BLUE
    fmagenta = Fore.MAGENTA
    fyelow = Fore.YELLOW
    res = Style.RESET_ALL
    bwhite = Back.WHITE 
except:
    print("colorma not included")
    red = str("")
    fgreen = str("")
    Black = str("")
    fblue = str("")
    fmagenta = str("")
    fyelow = str("")
    res = str("")
    bwhite = str("")

def CardGenerate(cl): #fungsi menghasilkan semua 52 kartu main secara otomatis
    style = str(input("gunakan Unicode(gambar) atau Huruf sebagai simbol kartu? 1/2 : "))
    if style == "1": # memilih penggunaan output yang akan digunakan untuk simbol kartu
        default_symbols = {'♦️' : 0.1, '♣️' : 0.2, '♥️' : 0.3, '♠️' : 0.4} #list simbol limbol kartu (logo/Unicode)
    elif style == "2":
        default_symbols = {'D' : 0.1, 'C' : 0.2, 'H' : 0.3, 'S' : 0.4} #list simbol limbol kartu (alfabet)
        print("D = Diamond\nC = Clove\nH = Hearten\nS = Spaids")
    else:
        default_symbols = {'♦️' : 0.1, '♣️' : 0.2, '♥️' : 0.3, '♠️' : 0.4} #list simbol limbol kartu (logo/Unicode)

    Hrank = {'J':11, 'Q':12, 'K':13, 'A':14, '2':15}
    for symbol in default_symbols:
        for lowR in range(3,11):
            cl[symbol + str(lowR)] = lowR + default_symbols[symbol]
        for highR in Hrank:
            cl[symbol + str(highR)] = Hrank[highR] + default_symbols[symbol]
    return cl, style

def ShowDealerCards(): #method untuk menunjukkan semua kartu yang ada
    for cards in cards_list:
        print(f"{cards} : {cards_list[cards]}")
    print("cards total : ",len(cards_list))

def GiveCard(): #method tuntuk membagikan kartu pada masing-masing pemain seacra acak
    choose_player = random.choice(list(players))
    if len(list(choose_player)) != 13:
        choose_card = random.randint(0, len(cards_list))
        try:
            choose_player[list(cards_list)[choose_card]] = cards_list[list(cards_list)[choose_card]]
            cards_list.pop(list(cards_list)[choose_card])
        except:
            print("", end=" ")
    else:
        GiveCard()

def ShowAllPlayerCards(): #method untuk menunjukkan semua kartu yang ada pada masing masing pemain
    print(f"\n{fgreen}PLAYER 1 : {list(p1)} \n{fblue}PLAYER 2 : {list(p2)} \n{fmagenta}PLAYER 3 : {list(p3)} \n{fyelow}PLAYER 4 : {list(p4)}{res}")
    
    print(len(p1)," : player one cards total")
    print(len(p2)," : player two cards total")
    print(len(p3)," : player three cards total")
    print(len(p4)," : player four cards total")
    print(len(cards_list)," : cards left on the dealer")
    print(len(cards_on_the_table)," : cards thrown on the table")

def InitiatePlay(sty): #fungsi untuk memainkan game 
    print()
    time.sleep(0.3)
    print(bwhite + Black + "Game initiating..." + res)
    time.sleep(0.3)
    print("\nYou are player number one.")
    print("Here is your hand:")
    for i in p1:
        print(fgreen + f"{i}" + res, end= " | ")

    #putaran pertama | buang 3
    print()
    for turn in players:
        print()
        print(f"Player {players.index(turn)+1}")
        for check in turn:
            if (turn[check] == 3.1) or (turn[check] == 3.2) or (turn[check] == 3.3):
                print(check)
                cards_on_the_table[check] = turn[check]
            elif turn[check] == 3.4:
                first = players[players.index(turn)]
                firstnm = players.index(turn)
                cards_on_the_table[check] = turn[check]
                print(red + f"{check}" ,res)
    
    def recur_del_threes(iteration,style):
        if iteration != 4:
            for y in range(1,5):
                if style == "1":
                    for i in ['♦️3','♣️3','♥️3','♠️3'] :
                        if i in players[iteration]:
                            #print(players[iteration])
                            players[iteration].pop(i)
                elif style == "2":
                    for it in ['D3','C3','H3','S3'] :
                        if it in players[iteration]:
                            #print(players[iteration])
                            players[iteration].pop(it)
                else:
                    for ith in ['♦️3','♣️3','♥️3','♠️3'] :
                        if ith in players[iteration]:
                            #print(players[iteration])
                            players[iteration].pop(ith)
            recur_del_threes(iteration + 1, style)

    recur_del_threes(0,style)
    print(f"\n{bwhite}{Black}Player {firstnm + 1} will be playing first{res}")

    return firstnm

def CheckThrownCards(): #method untuk menunjukkan semua kartu yang telah dibuang oleh pemain-pemain
    print("thrown cards are : ")
    for i in cards_on_the_table:
        print(f"{i}", end= " | ")

def RecursivePlay(turns): #fungsi rekursif untuk memainkan game secara berulang kali sampai ada pemenang
    win = None  
    if win != None:
        return win

    else:
        if turns == 0:
            print("\nyour turn to play")
            print("here is your hand : ")
            for i in p1:
                print(fgreen + f"{i}" + res, end= " | ")
            throw = str(input("what card do you want to throw : "))

### ▬MAIN PROGRAM▬ ###
p1 = {}
p2 = {}
p3 = {}
p4 = {}
cl = {} #card-list
cards_on_the_table = {} #kartu yang telah dibuang dan sudah tidak dipegang oleh para pemain maupun dealer
players = [p1, p2, p3, p4] #list yang menyimpan masing-masing dictionary p1, p2, p3, p4

cards_list, style = CardGenerate(cl)

#ShowDealerCards()
while len(cards_list) != 0:
    #ShowDealerCards()
    #print()
    GiveCard()

print(f"\n{bwhite}{Black}generated card : {res}")
ShowAllPlayerCards()
who_plays_first = InitiatePlay(style)
print()
print(f"{'-' * 50}")
ShowAllPlayerCards()
#print(CheckThrownCards())
CheckThrownCards()
#print(cards_on_the_table)
print(f"\n\nthe one who plays first is : player[{who_plays_first}] as index of variable in array players. which is player {who_plays_first+1}")
RecursivePlay(who_plays_first)