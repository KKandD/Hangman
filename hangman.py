
print("Welcome to Hangman Countries!")
print("\nHow to play: \nYou will see a number of short lines together that represent the number of letters in the word you have to guess.")
print("Write the letter that you think is included in the word.")
print("If you guess the correct letter, that letter will appear in the appropriate position in the word. It will replace one of the little lines ")
print("If the letter you guessed is not in the word, a part of the body will appear on the diagram below word.\nIf the body becomes completed, you are 'hanged' which means you have lost.")
print("If you guess all the letters in the word before you are 'hanged', you win.")
print("\nChoose Level of Difficulty: \n1-Easy (6 lives) \n2-Medium (4 lives) \n3-Hard (2 lives)")

def lives_count():
    if level_dificultity == 1:
        lives = 6
    elif level_dificultity == 2:
        lives = 4
    elif level_dificultity == 3:
        lives = 2

def level_dificultity():
    pass

#
#
#
#
