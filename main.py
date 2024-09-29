import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

game_over = False

correct_letters = []

while not game_over:
    guess = input('Guess a letter: ').lower()

    word_length = len(chosen_word)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print('You win!')