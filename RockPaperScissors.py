import random
import time
import os
import unicodedata

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)

def printTurn(turn):
    print("          Player: "+turn+"\n          Player: "+turn+"\n")

def checkWinner(Player1, Player2):
    if caseless_equal(Player1, Player2):
        winner = "Draw"
    elif caseless_equal(Player1, "Piedra"):
        if caseless_equal(Player2, "Papel"):
            winner = "Player 2"
        else:
            winner = "Player 1"
    elif caseless_equal(Player1, "Papel"):
        if caseless_equal(Player2, "Piedra"):
            winner = "Player 1"
        else:
            winner = "Player 2"
    elif caseless_equal(Player1, "Tijera"):
        if caseless_equal(Player2, "Piedra"):
            winner = "Player 2"
        else:
            winner = "Player 1"
    else:
        winner = "Error"
        
    return winner

def inCaseless(option, optionArray):
    for i in optionArray:
        if caseless_equal(option, i):        #checar que hay una comparación no sensible a mayúsculas
            return True 
    return False

def playerMove():
    options = ["Piedra","Papel","Tijera"]
    inputPlayer = ""
    booleanCheck = False
    while not booleanCheck:
        inputPlayer = input("  Haz tu jugada: ")
        booleanCheck = inCaseless(inputPlayer,options)
    return inputPlayer

def moveAI(lastPlayer, lastResult):
    if lastResult == 1:   #significa que en la última jugada ganó el Player 1 o hubo un empate
        if caseless_equal(lastPlayer[-1], "Piedra"):
            attempt = random.choice(["Papel","Piedra"])        
        elif caseless_equal(lastPlayer[-1], "Papel"):
            attempt = random.choice(["Tijera","Papel"])
        elif caseless_equal(lastPlayer[-1], "Tijera"):
            attempt = random.choice(["Piedra","Tijera"])
    if lastResult == 0:   #significa que en la última jugada ganó el Player 2 o hubo un empate
        if caseless_equal(lastPlayer[-1], "Piedra"):
            attempt = random.choice(["Tijera","Piedra"])
        elif caseless_equal(lastPlayer[-1], "Papel"):
            attempt = random.choice(["Piedra","Papel"])
        elif caseless_equal(lastPlayer[-1], "Tijera"):
            attempt = random.choice(["Papel","Tijera"])
    return attempt

def score():
    
    os.system("cls")

    print()
    print("             TURN {} of 10".format(attempt))
    print("             -----------------------")
    print("             Player 1: {} - {} : Player2".format(player1Points,player2Points))
    print("             ------------------------")
    print()


player1Points = 0
player2Points = 0
attempt = 1
playerAttempts = ["Piedra"]
lastResult = 1

while True:
    score()

    player1 = playerMove()

    player2 = moveAI(playerAttempts, lastResult)
    print("player: "+player1+"  ia: "+player2)
        
    winner = checkWinner(player1, player2)

    print()
    printTurn(player1)
    print()
    printTurn(player2)
    print()
    print("    Player 2: ", player2)
    print()

    attempt +=1

    playerAttempts.append(player1)

    if caseless_equal(winner, "Player 1"):
        player1Points += 1
        lastResult = 1
        print("     Player 1 win")
        print()
    elif caseless_equal(winner, "Player 2"):
        player2Points += 1
        lastResult = 0
        print("     Player 2 win")
        print()
    elif caseless_equal(winner, "Draw"):
        print("     Draw")
        print()
    input("     Enter for continue ...")

    if attempt == 10:
        score()
        mensaje1 = "GAME OVER"
        if player1Points > player2Points:
            mensaje2 = "Player 1 Win"
        elif player1Points < player2Points:
            mensaje2 = "Player 2 Win"
        else:
            mensaje2 = "   DRAW"
        print()
        print()
        print("    {}".format(mensaje1))
        print("    {}".format(mensaje2))
        print()
        print()
        print()

        break
        
            
