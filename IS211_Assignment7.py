# Creating a Pig Game
import random
import sys

class Player():
    def __init__(self):
        self.turn = False
        self.hold = False
        self.roll = True
        self.score = 0
        self.name = None

    def decide(self):
        decision = raw_input('Would you like to "Hold (H)" or "Roll (R) ?". Type H or R. ')
        decision = decision.lower()
        if decision == 'r' or decision == 'R':
            self.hold = False
            self.roll = True
        elif decision == 'h' or decision == 'H':
            self.hold = True
            self.roll = False
        else:
            print 'Invalid input, please type "H" or "R".'
            self.decide()

class Die():
    def __init__(self):
        self.value = int()
        seed = 0

    def roll(self):
        self.value = random.randint(1, 6)

class Pig_game():
    def __init__(self, player1, player2, die):
        self.turn_score = 0
        self.die = Die()
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = 'Player 1'
        self.player2.name = 'Player 2'

        coin_toss = random.randint(1,2)
        if coin_toss == 1:
            self.current_player = self.player1
            print 'Player 1 will start the game'
        elif coin_toss == 2:
            self.current_player = self.player2
            print 'Player 2 will start the game'
        self.turn()

    def next_turn(self):
        self.turn_score = 0
        if self.player1.score >= 100:
            print 'Player 1 won the game with score:', self.player1.score
            # print 'Score:', self.player1.score
            self.endgame()
            game_start()
        elif self.player2.score >= 100:
            print 'Player 2 won the game with score:', self.player2.score
            # print "Score:", self.player2.score
            self.endgame()
            game_start()
        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            print 'Next turn, Active player : ', self.current_player.name
            self.turn()

    def turn(self):
        self.die.roll()
        if (self.die.value == 1):
            print 'You Rolled a 1! No points added, your turn is over.'
            print 'Player 1 Score:', self.player1.score
            print 'Player 2 Score:', self.player2.score
            self.turn_score = 0
            self.next_turn()
        else:
            self.turn_score = self.turn_score + self.die.value
            print 'You rolled a:', self.die.value
            print 'Current Value is:', self.turn_score
            print 'Player 1 Score:', self.player1.score
            print 'Player 2 Score:', self.player2.score
            self.current_player.decide()
            if (self.current_player.hold == True and self.current_player.roll == False):
                self.current_player.score = self.current_player.score + self.turn_score
                self.next_turn()
            elif (self.current_player.hold == False and self.current_player.roll == True):
                self.turn()

    def endgame(self):
        self.player1 = None
        self.player2 = None
        self.die = None
        self.turn_score = None

def game_start():
    '''
    It call all the classes and start the game based on user's input.
    :return:
    '''
    user_input = raw_input("\nLets start a New Game? Y/N  ")
    user_input = user_input.lower()
    if user_input == 'y':
        player1 = Player()
        player2 = Player()
        die = Die()
        Pig_game(player1,player2,die)  # Start the game
    else:
        print 'Please type Y or N to beign'
        sys.exit()

if __name__ == '__main__':
    game_start()