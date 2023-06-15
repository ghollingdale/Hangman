#importing random module
import random
#Defining Hangman class
class Hangman:
    pass
    #Initializing attributes
    def __init__(self):
        #set attritubres
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = []
        for letter in self.word_to_find:
            self.correctly_guessed_letters.append("_")
        self.wrongly_guessed_letters = []
        self.turn_count = 0

    #Start the game loop and check whether win/loss conditions are met. Load respective method.
    def game_start(self):
        print("You have" , self.lives , "live(s) remaining.")
        print("Current progress:" , *self.correctly_guessed_letters)
        print("You have already used these letters:" , *self.wrongly_guessed_letters)
        if self.lives > 0: 
            if "_" in self.correctly_guessed_letters:
                self.play()
            elif "_" not in self.correctly_guessed_letters:
                self.You_win()
        else:
            self.You_lose()

    #Manage a game turn and update the turn/board status 
    ###INCOMPLETE - need to work on enumeration and indexing
    def play(self):
        guess = input("\nPlease enter a letter as your guess: ")
        #checks validity of input. Sends user back to input if invalid
        while self.checkvalidity(guess) == False:
            print("\nError. Please enter a single lowercase letter that hasn't been guessed yet.")
            print("You have" , self.lives , "live(s) remaining.")
            print("Current progress:" , *self.correctly_guessed_letters)
            print("You have already used these letters:" , *self.wrongly_guessed_letters)
            self.play()
        guess = guess.lower()
        #checks whether the guess is in the secret word. Increases turn counter. Replaces dash in correctly_guessed_letters with the guess, in the correct position.
        if guess in self.word_to_find:
            print("\nCorrect!", guess , "is in the secret word!")
            self.turn_count += 1
            for position , correct_letter in enumerate(self.word_to_find):
                if guess == correct_letter:
                    self.correctly_guessed_letters[position] = guess
            self.game_start()
        #checks whether guess isn't in word_to_find, then increases turn_counter and incorrect_guess_count, and reduces lives
        #Appends the incorrect guess to wrongly_guessed_letters
        elif guess not in self.word_to_find:
            self.turn_count += 1
            #self.incorrect_guess_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(guess)
            print("\nIncorrect guess.")
            self.game_start()
        else:
            pass
         


                                    

    ##Win function
    def You_win(self):
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        print("\nCongratulations you have won with" , self.lives , "live(s) remaining!")
        return quit()
        
    
    ##Lose function
    def You_lose(self):
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        print("\nOut of lives! You lose. Too bad. Better luck next time.")
        return quit()

    ##An attempt at checking validity. 
    ## Not yet tested.
    def checkvalidity(self , guess):
        if len(guess) != 1:
            return False
        elif guess.isalpha() != True:
            return False
        elif guess in self.wrongly_guessed_letters:
            return False
        elif guess in self.correctly_guessed_letters:
            return False
        else:
            return True

