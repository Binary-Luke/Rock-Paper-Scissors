import random

class rps():
    def __init__(self):
        self.win_1 = "Computer wins!"
        self.win_2 = "You win !"
        options = ['rock', 'paper', 'scissors']
        self.computer = random.choice(options)
    
    
    def findPlayer(self):
        self.p1 = input("Rock, Paper, or Scissors: --> ")

    
    def run(self):
        print("Rock ... Paper ... Scissor ... Shoot! The computer played -->", self.computer)
        if self.p1 == self.computer:
            print("Draw!")
        elif self.p1 == 'rock':
            if self.computer == 'scissors':
                print(self.win_2)
            else:
                print(self.win_1)
        elif self.p1 == 'scissors':
            if self.computer == 'paper':
                print(self.win_2)
            else:
                print(self.win_1)
        elif self.p1 == 'paper':
            if self.computer == 'rock':
                print(self.win_2)
            else:
                print(self.win_1)
        elif self.p1 == 'roaches':
            print("WORLD DOMINATION !")
        else:
            print(self.p1.upper(), "DESTROYS ALL!!!")

def RockPaperScissors():
    play = ''
    while play != 'quit':
        
        game = rps()
        game.findPlayer()
        game.run()
        play = input("Play or quit? ")

RockPaperScissors()