#%%
import random
#  TODO create list of 5 favourite fruit

word_list = ['banana', 'pineapple', 'papaya', 'dragonfruit', 'guava']
print(word_list)

word = random.choice(word_list)
print(word)

while True:
    
    guess = input('guess a single letter')

#check input is a single alphabetical character

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break

    else :
        print("Invalid letter. Please, enter a single alphabetical character.")




# %%
def check_guess(guess):

    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
 
    else :
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('guess a single letter')

#check input is a single alphabetical character

        if len(guess) == 1 and guess.isalpha():
            print('Good guess!')
            break

        else : 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()



# %%
