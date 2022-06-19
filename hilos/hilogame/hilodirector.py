import random
from random import *
from numpy import integer

#create draw function to get cards
def draw(self):
    self.value = randint(1, 13)
def output(self):
    print(f'The card is {self.value}')
def secoutput(self):
    self.value = randint(1, 13)

#director for the program 
class Director:
    def __init__(self):
        self.points = 300
        self.is_playing = True
        self.correct_guess = True
        self.card_value = draw(self)
        self.card_value2 = secoutput(self)
        self.total_score = 300
        self.guess = ""
    #set values for the cards
    def draw(self):
        self.card_value = randint(1, 13)
    #print output value for user
    def output(self):
        print(f'\nThe card is a {self.card_value}')
    #print second output value (second number)
    def secoutput(self):
        self.card_value2 = randint(1, 13)
        print(f'\n{self.card_value2} was the new card')
    #starts the game up running through the different functions
    def game_start(self):
        while self.is_playing:
            draw(self)
            output(self)
            self.get_guess()
            self.secoutput()
            self.do_updates()
            self.score_display()
            self.cont_game()
    #user input for their guess
    def get_guess(self):
        guess = input("\nHigher or lower? (h/l): ")
        return guess.lower
    #logic to dtermine if the user is right or wrong
    def correct_guess(self):
        if int(self.card_value) < int(self.second_card_value) and self.guess == "h":
            correct_guess = True
            return correct_guess
        elif int(self.card_value) > int(self.second_card_value) and self.guess == "l":
            correct_guess = True
            return correct_guess
        else:
            correct_guess = False
            return correct_guess
    #controls score and updates
    def do_updates(self):
            if self.correct_guess == True:
                self.total_score += 100
            else:
                self.total_score -= 75
    #displays score
    def score_display(self):
        print(f'Your score is {self.total_score}')
    #prompts user if they would like to play again
    def cont_game(self):
        play_again = input("\nWould you like to play again? (Y/N): ")
        self.is_playing = (play_again.upper == "Y")
#holds our project in a neat bundle and only activates the parts we want
def main():
    director = Director()
    while director.is_playing == True:
        director.game_start()
        
if __name__ == "__main__":
    main()
