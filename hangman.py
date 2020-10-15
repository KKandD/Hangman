import random

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

player_state = []

print("Welcome to Hangman Countries!")
print("\nHow to play:")
print("You will see a number of short lines together that represent the number of letters in the word you have to guess. ")
print("Write the letter that you think is included in the word.")
print("If you guess the correct letter, that letter will appear in the appropriate position in the word. It will replace one of the little lines ")
print("If the letter you guessed is not in the word, a part of the body will appear on the diagram below word .")
print("If the body becomes completed, you are 'hanged' which means you have lost.")
print("If you guess all the letters in the word before you are 'hanged', you win.")
input("Press ENTER to continue\n")

# wczytuję listę krajów z pliku
list_of_countries = open("countries.txt").read().splitlines()

# losowanie 1 kraju z listy
selected_country = random.choice(list_of_countries).upper()
# print(selected_country)
# zostawiam do sprawdzania, potem usuniemy

# zliczenie liczby liter w wylosowanym wyrazie (chyba nie bedzie to będzie potrzebne, na razie zostawiam, najwyzej usuniemy)
number_of_letters = len(selected_country)

# print(number_of_letters)
# zostawiam do sprawdzania, potem usuniemy


# zamiana string ze słowem na listę
list_of_letters = list(selected_country)
player_state = ["_"] * len(list_of_letters)
print(list_of_letters)

# zostawiam do sprawdzania, potem usuniemy

choose_level = input(
    "\nChoose Level of Difficulty:\n1-Easy (6 lives)\n2-Medium (4 lives)\n3-Hard (2 lives)\n")
lives = 0

while choose_level != "1" and choose_level != "2" and choose_level != "3":
    # Po wybraniu opcji trudnośći przypisuje nam liczbę żyćków
    print("Choose correct Level of Difficulty")
    choose_level = input(
        "\nChoose Level of Difficulty:\n1-Easy (6 lives)\n2-Medium (4 lives)\n3-Hard (2 lives)\n")

if choose_level == "1":
    lives = 6
elif choose_level == "2":
    lives = 4
elif choose_level == "3":
    lives = 2


# wyświwetlanie obrazków w zależności od liczby pozostałych żyć
def print_hangman():
    if choose_level == "1":
        if lives == 6:
            print(hangman_pics[0])
        elif lives == 5:
            print(hangman_pics[1])
        elif lives == 4:
            print(hangman_pics[2])
        elif lives == 3:
            print(hangman_pics[3])
        elif lives == 3:
            print(hangman_pics[4])
        elif lives == 2:
            print(hangman_pics[5])
        elif lives == 1:
            print(hangman_pics[6])
        else:
            print(hangman_pics[7])
    elif choose_level == "2":
        if lives == 4:
            print(hangman_pics[0])
        elif lives == 3:
            print(hangman_pics[1])
        elif lives == 2:
            print(hangman_pics[3])
        elif lives == 1:
            print(hangman_pics[5])
        else:
            print(hangman_pics[6])
    else:
        if lives == 2:
            print(hangman_pics[0])
        elif lives == 1:
            print(hangman_pics[3])
        else:
            print(hangman_pics[6])


def hidden_letters():
    print_hangman()
    print(" ".join(player_state))

# walidacja inputu

# dodaje zgadniętą literę do wyświetlanego wyniku


def guess():
    global lives

    found = False
    for i in range(len(list_of_letters)):
        letter = list_of_letters[i]

        if letter.upper() == player_guess.upper():
            found = True
            player_state[i] = letter
            #count = list_of_letters.count(letter)
            # print(count)
            # letter_place = list_of_letters.index(letter)

            # print(letter_place)
    print("Was found " + str(found))
    if not found :
        lives -= 1
    hidden_letters()
    # obsługa żyć

# def compare_lists():


hidden_letters()

while lives > 0 and player_state != list_of_letters:

    player_guess = input()

    guess()


if lives <= 0:
    print("GAME OVER")
else:
    print("Congrats! You WIN!!!")

