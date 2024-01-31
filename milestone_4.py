#%%

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game instance.
        
        Parameters:
        word_list (list): A list of words to choose from for the game.
        num_lives (int): The number of lives the player starts with.
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
        guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
            self.num_letters -= 1
            print(f"Good guess! {guess} is in the word.")
            print(self.num_letters)
        else :
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        """
        Continuously ask the player for a letter guess, checks whather the input is valid and different to previous guesses and adds the letter guess to the list of previous guesses.
        """
        while True:
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
word_list = ['banana', 'pineapple', 'papaya', 'dragonfruit', 'guava']
game = Hangman(word_list)

game.ask_for_input()
