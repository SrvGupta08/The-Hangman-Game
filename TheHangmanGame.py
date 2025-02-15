import random
import hangman_words
import hangman_arts

word_list = hangman_words.word_list
stages = hangman_arts.stages
logo = hangman_arts.logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

size_of_choosen_word = len(chosen_word)
placeholder = ''
for i in range(size_of_choosen_word):
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"!!!You have {lives} lives left!!!")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You have already guessed " + guess)

    display = ""
    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + " that's not in the word")
        if lives == 0:
            game_over = True
            print("You lose!\nThe word was " + chosen_word)

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")

