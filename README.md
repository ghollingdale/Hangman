# Hangman
#### *A George Hollingdale game written in Python 3.11*
***
This is a basic Hangman game written in Python. The goal of the game is to guess a secret word, guessing letter by letter. If all of the letters of the word have been guessed before 5 incorrect attempts, then the player wins.

# Installation
You will need to have Python installed to your device to run this program. It is executable in your devices terminal.
# Usage
To play the game:   
* Run the program
* Input a letter into the field and hit enter
    * If the input is a valid (lowercase letter, not already chosen) it will be accepted
    * If the input is invalid (e.g. a number, more than one leter etc.) it will be rejected and the user is prompted to enter a new letter
* The program checks the letter against the secret word
    * If the letter **is** in the secret word, the letter is shown and the user moves on to a new guess
    * If the letter **isn't** in the secret word, the user loses a life and is prompted to give a new guess
* The game continues to cycle until either five lives are lost, or the word is correctly guessed!
 To play the game again, kill the terminal and reboot the program.

# Timeline
The game took me around 8-9 hours to complete.
* The main code took me about 6-7 hours including testing/debugging
* The program aesthetics including print text and output formatting took around 1-2 hourIs

# Personal situation
I am a junior at Becode following an AI bootcamp. I had  zero programming experience before May '23. This is my first full project in Python. 