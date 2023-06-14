#importing random module
import random
#Defining Hangman class
class Hangman:
    pass
    #Initializing attributes
    def __init__(self):
        #set list of possible_words
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        #randomise a word from possible_word as the word_to_find
        self.word_to_find = list(random.choice(self.possible_words))
        #set number of lives to 5
        self.lives = 5
        #set display board of correct letters as a list of underscore elements
        self.correctly_guessed_letters = []
        for letter in self.word_to_find:
            self.correctly_guessed_letters.append("_")
        #create an empty list to store incorrect guesses
        self.wrongly_guessed_letters = []
        #set turn and error count to zero
        self.turn_count = 0
        self.incorrect_guess_count = 0

    #Start the game loop and check whether win/loss conditions are met
    def game_start(self):
        if self.lives > 0 and "_" in self.correctly_guessed_letters():
           self.play()
        elif self.lives > 0 and "_" not in self.correctly_guessed_letters:
            self.You_win()
        else:
            self.You_lose()
        #Print a status update of the game
        print("You have" , self.lives , "lives remaining.")
        print("Current progress:" , self.correctly_guessed_letters)
        print("You have taken" , self.incorrect_guess_count , "guesses so far")
        print("You have already used these letters:" , self.wrongly_guessed_letters)

    #Manage a game turn and update the turn/board status 
    ###INCOMPLETE - need to work on enumeration and indexing
    def play(self):
        guess = input("Please enter a letter as your guess:")
        if checkvalidity(guess) == False:
            play()
        else:
            if guess in self.word_to_find:

    ##Win function
    def You_win(self):
        return print("Congratulations you have won inside" , self.turn_count , "attempts!")
    
    ##Lose function
    def You_lose(self):
        return print("You lose. Too bad! Try again next time.")

    ##An attempt at checking validity. 
    ## Not yet tested.
    def checkvalidity(self):
        guess = list(guess)
        if len(guess) != 1:
            return False
        elif guess[0] != type(str):
            return False
        else:
            return True


        
#Test = Hangman()