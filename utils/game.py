# Importing random module
import random
#Defining Hangman class
class Hangman:
    pass
    
    #Sets attributes needed for program.
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = []
        for letter in self.word_to_find:
            self.correctly_guessed_letters.append("_")
        self.wrongly_guessed_letters = []
        self.turn_count = 0

    # Start the game loop and check whether win/loss conditions are met. 
    # Loads respective method.
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

    # Manages a game turn. 
    # Calls checkvalidity and prints Error if not met, then restarts method. 
    # Changes uppercase inputs to lower.
    # Checks whether guess is in word to find and moves the game forward.
    def play(self):
        guess = input("\nPlease enter a letter as your guess: ")
        while self.checkvalidity(guess) == False:
            print("\nError. Please enter a single lowercase letter that hasn't been guessed yet.")
            print("You have" , self.lives , "live(s) remaining.")
            print("Current progress:" , *self.correctly_guessed_letters)
            print("You have already used these letters:" , *self.wrongly_guessed_letters)
            self.play()
        guess = guess.lower()
        if guess in self.word_to_find:
            print("\nCorrect!", guess , "is in the secret word!")
            self.turn_count += 1
            for position , correct_letter in enumerate(self.word_to_find):
                if guess == correct_letter:
                    self.correctly_guessed_letters[position] = guess
            self.game_start()
        elif guess not in self.word_to_find:
            self.turn_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(guess)
            print("\nIncorrect guess.")
            self.game_start()
        else:
            pass                                  

    # Win function.
    # Resets the game and prints congratulatory message.
    # Quits program
    def You_win(self):
        print("\nCongratulations you have won with" , self.lives , "live(s) remaining!")
        return quit()
    
    # Lose function
    # Resets the game and prints loser message.
    # Quits program
    def You_lose(self):
        print("\nOut of lives! You lose. Too bad. Better luck next time.")
        return quit()

    # Validity check.
    # Returns False if input is longer than one character, not in the alphabet, or already in wrongly_guessed_letters or correctly_guessed_letters.
    # Otherwise accepts input and returns True.
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