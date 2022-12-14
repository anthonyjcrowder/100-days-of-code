#Step 5

import random
import hangman_words
import hangman_art

logo = hangman_art.logo

print(logo)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
wrong_guesses = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
      wrong_guesses.append(guess)

    print("\n")
    print("Guesses so far:")
    print(f"{' '.join(wrong_guesses)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    stages = hangman_art.stages
    print(stages[lives])