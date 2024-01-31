#%%

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game instance with a word list and number of lives.

        Parameters:
        - word_list (list): A list of words to choose from for the game.
        - num_lives (int): The number of lives the player starts with.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Process the player's guess, updating game state and providing feedback.
        
        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            if guess not in self.word_guessed:
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                print(f"Good guess! {guess} is in the word.")
                self.num_letters = len(set(self.word) - set(self.word_guessed))  # Recalculate unique letters left
                
            else:
                print(f"You already guessed {guess}.")
        else :
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        """
        Ask the player for a letter guess and handle the input validation.
        """
    
        guess = input('Guess a letter:')

#check input is a single alphabetical character

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")

        elif guess in self.list_of_guesses:
            print("You already tried that letter!")

        else : 
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


# %%


def play_game(word_list):
    """
    Start and manage the Hangman game loop. Determines if the player has won or lost.

    Parameters:
    - word_list (list): A list of words to choose from for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives) #instance of the Hangman class
    print('Welcome to hangman. Guess the word to win! Hint: The word is a fruit')
    print('you have 5 lives')
   
    
    while True:
        print(f"Word: {' '.join(game.word_guessed)}")
        print(f"Letters Guessed: {' '.join(game.list_of_guesses)}")
        print(f"Lives Remaining: {game.num_lives}")

        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break
            

word_list = ['banana', 'pineapple', 'papaya', 'dragonfruit', 'guava']

play_game(word_list)