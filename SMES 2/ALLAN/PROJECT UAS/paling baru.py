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
    time.sleep(3)
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
    
    print(len(p1),": player one cards total")
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
    recur_del_threes(0,sty)

    temp = {}
    if style == "1":
        temp['♠️3'] = max(cards_on_the_table.values())
        cards_on_the_table.pop('♠️3')
        cards_on_the_table['♠️3'] = max(temp.values())
    elif style == "2":
        temp['S3'] = max(cards_on_the_table.values())
        cards_on_the_table.pop('S3')
        cards_on_the_table['S3'] = max(temp.values())
    else:
        temp['♠️3'] = max(cards_on_the_table.values())
        cards_on_the_table.pop('♠️3')
        cards_on_the_table['♠️3'] = max(temp.values())
    
    print(f"player {firstnm + 1} will be playing first")

    return firstnm

def CheckThrownCards(): #method untuk menunjukkan semua kartu yang telah dibuang oleh pemain-pemain
    print("\nthrown cards are : ")
    for i in cards_on_the_table:
        print(f"{i}", end= " | ")

def RecursivePlay(turns, win, skip): #fungsi rekursif untuk memainkan game secara berulang kali sampai ada pemenang
    time.sleep(2)
    CheckThrownCards() 
    #ShowAllPlayerCards()
    if win != None:
        print("wineerr ", win)
        return win

    else:
        print(f"\nskiped {skip} times")
        if skip == 3:
            cards_on_the_table[list(cards_on_the_table.keys())[-1]] = 0
            print(cards_on_the_table[list(cards_on_the_table.values)[-1]], "became free")
            skip = 0 
        
        current_highest_card = max(list(p1.values()) + list(p2.values()) + list(p3.values()) + list(p4.values()))
        is_thrown_highcard = False
        for plyr in players:
            for keys in plyr:
                if plyr[keys] == current_highest_card:
                    ky = keys
        print("highest card",current_highest_card, "or", ky)
        if turns == 0:
            print(f"\n{bwhite}your turn{res}")
            if max(list(p1.values())) < list(cards_on_the_table.values())[-1]:
                print("\nyou skipped")
                RecursivePlay(turns + 1,None, skip + 1)
            else:
                print("\nyour turn to play")
                print("here is your hand : ")
                for i in p1:
                    print(fgreen + f"{i}" + res, end= " | ")
                throw = str(input(f"what card do you want to throw : {fgreen}"))
                print(res)
                while throw not in list(p1.keys()):
                    print("card unavailable")
                    throw = str(input("please input again : "))
                while (p1[throw] < list(cards_on_the_table.values())[-1]):
                    print(f"\n{throw} card is too low")
                    throw = str(input("please input again: "))
                
                if p1[throw] == current_highest_card:
                    is_thrown_highcard = True
                    print(f"{bwhite}{Black}player {turns + 1} throws {throw}{res}")
                    cards_on_the_table[throw] = 0
                    p1.pop(throw)
                else:
                    print(f"{bwhite}{Black}player {turns + 1} throws {throw}{res}")
                    cards_on_the_table[throw] = p1[throw]
                    p1.pop(throw)
     
        elif(turns == 1) or (turns == 2) or (turns == 3):
            print(f"\n{bwhite}player {turns + 1}'s turn{res}")
            if max(list(players[turns].values())) < list(cards_on_the_table.values())[-1]:
                print(f"\n{bwhite}{Black} player {turns + 1} skiped{res}")
                if turns != 3:
                    RecursivePlay(turns + 1, None, skip + 1)
                elif turns == 3:
                    RecursivePlay(turns - 3, None, skip + 1)
                pass
                
            else:
                enemy_throw = random.choice(list(players[turns].keys()))
                while (players[turns][enemy_throw] < list(cards_on_the_table.values())[-1]):
                    #print(f"\n{enemy_throw} card is not available")
                    enemy_throw = random.choice(list(players[turns].keys()))

                if players[turns][enemy_throw] == current_highest_card:
                    is_thrown_highcard = True
                    print(f"{bwhite}{Black}player {turns + 1} throws {enemy_throw}{res}")
                    cards_on_the_table[enemy_throw] = 0
                    players[turns].pop(enemy_throw)
                else:
                    print(f"\n{bwhite}{Black}player {turns + 1} throws {enemy_throw}{res}")
                    cards_on_the_table[enemy_throw] = players[turns][enemy_throw]
                    players[turns].pop(enemy_throw)
    
    if (len(p1) == 0) or (len(p2) == 0) or (len(p3) == 0) or (len(p4) == 0):
            RecursivePlay(turns, turns + 1, 0)

    if is_thrown_highcard:
        RecursivePlay(turns, None, 0)

    else:                                           
        if turns != 3:
            RecursivePlay(turns + 1, None, 0)
        elif turns == 3:
            RecursivePlay(turns - 3, None, 0)
    
### ▬MAIN PROGRAM▬ ###
p1 = {}
p2 = {}
p3 = {}
p4 = {}
cl = {} #temporary card-list place holder
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
print(f"{'-' * 50}") #################################
RecursivePlay(who_plays_first, None, 0)
ShowAllPlayerCards()