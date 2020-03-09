import random as r
import time
import numpy as np


number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Bube', 'Dame', 'König']
farbe = ['Herz', 'Karo', 'Kreuz', 'Pik']
gezogen = [[''] * len(number) for i in range(len(farbe))]
valuep = 0
valueb = 0
i = 0
bankkarten = 0
stopturn = False
akarte1 = 0
akarte2 = 0

totalgames = 0
winbank = 0
winplayer = 0

money = 10000 #the amount of money you start with
betrag = 0

#pics a card from the deck (gezogen) and makes sure no card piced more than once
def ziehkarte():
    t = 1
    while t == 1:
        ZAHL = number[r.randint(0, len(number)-1)]
        FARBE = farbe[r.randint(0, len(farbe)-1)]
        if gezogen[farbe.index(FARBE) -1][number.index(ZAHL) -1] != '':
            b0 = gezogen[0].count('X')
            b1 = gezogen[1].count('X')
            b2 = gezogen[2].count('X')
            b3 = gezogen[3].count('X')
            b = b0 + b1 + b2 + b3
            
            if b == 52:
                return FARBE, ZAHL
                break
            else:
                continue
        else:
            gezogen[farbe.index(FARBE) -1][number.index(ZAHL) -1] = 'X'
            return FARBE, ZAHL
            t = 0

#Draws 2 cards for the bank buzt only shows akarte1 (card1), also adds the values of both cards under valueb            
def kartebank():
    global akarte1
    global akarte2
    global valueb
    global bankkarten
    karte1 = ziehkarte()
    akarte1 = np.array(karte1)
    print(' '.join(str(elem) for elem in akarte1))  #card1
    karte2 = ziehkarte()
    akarte2 = np.array(karte2)
    print('HIDDEN')                                 #represntation of card2
    bankkarten = [[''] * 2 for i in range(2)]
    bankkarten[0][0] = akarte1[0]
    bankkarten[0][1] = akarte1[1]
    bankkarten[1][0] = akarte2[0]
    bankkarten[1][1] = akarte2[1]
    print('')
    #print(bankkarten)  #see the piced crad for the bank
    try:
        valueb = int(bankkarten[0][1]) + int(bankkarten[1][1])  #if both cards no facecard the no Error ...
    except:
        try:
            a = 0
            b = 0
            if bankkarten[1][1] == 'Ace' or bankkarten[1][1] == 'König' or bankkarten[1][1] == 'Dame' or bankkarten[1][1] == 'Bube':
                a += 1
            else:
                pass
            if bankkarten[0][1] == 'Bube' or bankkarten[0][1] == 'Dame' or bankkarten[0][1] == 'König' or bankkarten[0][1] == 'Ace':
                b += 1
            else:
                pass
            if b == 0 and a == 1:
                if bankkarten[1][1] == 'Ace':
                    valueb = 11 + int(bankkarten[0][1])
                else:
                    valueb = 10 + int(bankkarten[0][1])
            if b == 1 and a == 0:
                if bankkarten[0][1] == 'Ace':
                    valueb = 11 + int(bankkarten[1][1])
                    
                else:
                    valueb = 10 + int(bankkarten[1][1])
            if b == 1 and a == 1:
                if bankkarten[0][1] == 'Ace':
                    if bankkarten[1][1] == 'Ace':
                        valueb = 12
                    else:
                        valueb = 21
                elif bankkarten[0][1] != 'Ace':
                    if bankkarten[1][1] == 'Ace':
                        valueb = 21
                    else:
                        valueb = 20
            else:
                pass
        except:
            pass

#Draws 2 cards for the player and adds the value together (valuep)
def kartespieler():
    global valuep
    karte1 = ziehkarte()
    akarte1 = np.array(karte1)
    print(' '.join(str(elem) for elem in akarte1))  #card1
    karte2 = ziehkarte()
    akarte2 = np.array(karte2)
    print(' '.join(str(elem) for elem in akarte2))  #card2
    karten = [[''] * 2 for i in range(2)]
    karten[0][0] = akarte1[0]
    karten[0][1] = akarte1[1]
    karten[1][0] = akarte2[0]
    karten[1][1] = akarte2[1]
    print('')
    #print(karten)  #see the piced crad for the player
    try:
        valuep = int(karten[0][1]) + int(karten[1][1])
    except:
        try:
            a = 0
            b = 0
            if karten[1][1] == 'Ace' or karten[1][1] == 'König' or karten[1][1] == 'Dame' or karten[1][1] == 'Bube':
                a += 1
            else:
                pass
            if karten[0][1] == 'Bube' or karten[0][1] == 'Dame' or karten[0][1] == 'König' or karten[0][1] == 'Ace':
                b += 1
            else:
                pass
            if b == 0 and a == 1:
                if karten[1][1] == 'Ace':
                    valuep = 11 + int(karten[0][1])
                else:
                    valuep = 10 + int(karten[0][1])
            if b == 1 and a == 0:
                if karten[0][1] == 'Ace':
                    valuep = 11 + int(karten[1][1])
                else:
                    valuep = 10 + int(karten[1][1])
            if b == 1 and a == 1:
                if karten[0][1] == 'Ace':
                    if karten[1][1] == 'Ace':
                        valuep = 12
                    else:
                        valuep = 21
                elif karten[0][1] != 'Ace':
                    if karten[1][1] == 'Ace':
                        valuep = 21
                    else:
                        valuep = 20
            else:
                pass
        except:
            pass
    print('Dein Zwischenstand: ', valuep)


#if called pics another card for the player and adds the value to valuep 
def hit():
    global valuep
    karte1 = ziehkarte()
    akarte1 = np.array(karte1)
    print(' '.join(str(elem) for elem in akarte1))
    try:
        valuep = valuep + int(akarte1[1])
    except:
        if akarte1[1] == 'Ace':
            valuep = valuep + 11
        else:
            valuep = valuep + 10
    print('You are at', valuep)


#if called pics another card for the bank and adds the value to valueb
def hitb():
    global valueb
    global bankkarten
    karte1 = ziehkarte()
    akarte1 = np.array(karte1)
    print('the banks next card:')
    print(' '.join(str(elem) for elem in akarte1))
    try:
        valueb = valueb + int(akarte1[1])
    except:
        if akarte1[1] == 'Ace':
            valueb = valueb + 11
        else:
            valueb = valueb + 10
    print('')


#called once player finished:   pics cards (hitb()) until valueb > or == 17 ... the calls won() to evaluate the winner
def bankturn():
    global valueb
    global bankkarten
    global akart2
    print('')
    print('The banks cards were:')
    print(' '.join(str(elem) for elem in akarte1))
    print(' '.join(str(elem) for elem in akarte2))
    time.sleep(0.5)
    print('')
    stop = False
    while stop != True:
        if valueb > 21:
            stop = True
            won()
            break
        elif valueb  > 17 or valueb == 17:
            print('The bank is at ', valueb)
            print('')
            time.sleep(1)
            won()
            stop = True
            break
        elif valueb < 17:
            print('The bank is at ', valueb)
            print('')
            time.sleep(1)
            hitb()
            if valueb  > 17 or valueb == 17:
                print('The bank is at ', valueb)
                print('')
                time.sleep(1)
                stop = True
                won()
                break
            else:
                continue
        time.sleep(0.5)


#if called: checks if player or bank is over 21, elif whos value is bigger, else equal ... if player won calls gives money (geldwon())         
def won():
    global i
    global stopturn
    global winplayer
    global winbank
    global totalgames
    if valuep > 21:
        print('')
        print('Sorry you are over 21 the bank won!')
        winbank += 1
        totalgames += 1
        print('---------------------------------------------------------------')
        stopturn = True
    elif valueb > 21:
        print('')
        print('Congratulations you won!')
        winplayer += 1
        totalgames += 1
        print('---------------------------------------------------------------')
        geldwon()
        print('---------------------------------------------------------------')
        stopturn = True
    elif valuep > valueb and i == 'S':
        print('')
        print('Congratulations you won!')
        winplayer += 1
        totalgames += 1
        print('---------------------------------------------------------------')
        geldwon()
        print('---------------------------------------------------------------')
        stopturn = True
    elif valueb > valuep and i == 'S':
        print('')
        print('Sorry the bank won')
        winbank += 1
        totalgames += 1
        print('---------------------------------------------------------------')
        stopturn = True
    elif valueb == valuep and i == 'S':
        print('')
        print('EQUAL ... nobody won!')
        totalgames += 1
        print('---------------------------------------------------------------')
        geldback()
        print('---------------------------------------------------------------')
        stopturn = True
    else:
        pass

#if called returns the amount of money player has
def geld():
    global money
    print('Du hast', money, '€ !')

#cheks if player has money left 
def verloren():
    if money == 0:
        return True
    else:
        return False
        pass

#if called player gets the double of what he bid 
def geldwon():
    global money
    global betrag
    print('Du hast', betrag*2, '€ gewonnen !')
    money = money + betrag * 2
    print('')
    print('Du hast jetzt', money, '€ !')

#called if value of bank and player are equal ... returns the money bid to money
def geldback():
    global money
    global betrag
    print('Du hast', betrag, '€ zurückbekommen !')
    money = money + betrag

#takes input of player as money bid and subtracts from money if input bigger that money rutrns      
def setzebetrag():
    global money
    global betrag
    gesetzt = False
    while gesetzt == False:
        try:
            x = int(input('Bitte setze einen Betrag (in €)!'))
            if x > money:
                print("ERROR you don't have that much money.")
                gesetzt = False
                continue
            elif x == 0:
                print('Du kannst nicht nichts setzten!')
                continue
            else:
                betrag = x
                money = money - betrag
                print('')
                print('Ok', betrag, 'gesetzt')
                print('')
                print('Du hast noch', money, '€ übrig!')
                print('')
                print('RIEN NE VA PLUS!!!')
                gesetzt = True
        except:
            print('please make sure that you enter a valide amount (€)!')
            pass


#main loop of the game calls the functions etc.        
game = True
while game == True:
    global a
    global stopturn
    print('---------------------------------------------------------------')
    print('BLACK JACK:')
    print('---------------------------------------------------------------')
    time.sleep(1)
    geld()
    print('')
    setzebetrag()
    print('---------------------------------------------------------------')
    time.sleep(1)
    try:
        print('Total games:', totalgames, 'You won', winplayer, '     and The bank won', winbank, 'times!      you won', round((int(winplayer)/int(totalgames))*100), '% of the time.')
        print('---------------------------------------------------------------')
        time.sleep(1)
    except:
        pass
    print('Karte der Bank!:')
    print('')
    time.sleep(1)
    kartebank()
    time.sleep(0.5)
    print('')
    print('---------------------------------------------------------------')
    print('Deine Karten:')
    print('')
    time.sleep(1)
    kartespieler()
    time.sleep(0.5)
    print('')
    print('---------------------------------------------------------------')
    print('H I T - - - S T A Y - - - (D O U B L E) under construction!!!')
    print('---------------------------------------------------------------')
    stopturn = False
    while stopturn != True:
        global i
        try:
            i = input('(h/s):')
            i = i.upper()
        except:
            print('Error')
        if i == 'H' or i == 'S' or i == 'D':
            if i == 'H':
                print('')
                hit()
                won()
            elif i == 'S':
                stopturn = True
                bankturn()
                continue
            else:
                continue
    if verloren() == True:
        print('DU hast verloren, ... du hast kein Geld mehr!!!')
        time.sleep(1)
        print(':(')
        #a = 0
        #game = False
        break
    else:
        a = 1
        while a == 1:
            print('')
            try:
                b = str(input('nochmal spielen? (j/n):'))
                print('')
                b = b.upper()
                if b == 'J':
                    a = 0
                elif b == 'N':
                    print('Ok')
                    a = 0
                    game = False
                    break
            except:
                print('Das habe ich leider nicht verstanden!')
