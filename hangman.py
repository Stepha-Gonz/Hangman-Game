import random
import figures
from words import word_list



print (figures.logo)
chosen_word=random.choice(word_list)
print(chosen_word)
word_length= len(chosen_word)
print(f"The length of the word is {word_length} characters ")
placeholder=""
for letter in chosen_word:
    placeholder+= "_"
print(f"Word to Guess {placeholder}")


lives=6
guessed_letters=[]
not_guessed_letters=[]
game_over=False
while not game_over:
    word_guess=""
    print(f"Your lives: {lives}")
    guess=input("Choose a letter: ").lower()

    if guess in guessed_letters:
        print("You have already selected this letter")
    for letter in chosen_word:
        if letter == guess:
            word_guess+=letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            word_guess+= letter
        else:
            word_guess+="_"





    if guess not in chosen_word:
        if guess in not_guessed_letters:
            print("You have already selected this letter")
        if guess not in not_guessed_letters:

            lives-=1
            not_guessed_letters.append(guess)
            print(f"{guess} is not in the word")

            if lives == 0:
                game_over=True
                print(f"You run out of lives, You lose.the word was {chosen_word}")

    if "_" not in word_guess:
        print("congratulations you win!")
        game_over=True
    print(word_guess)

    print(figures.stages[lives])