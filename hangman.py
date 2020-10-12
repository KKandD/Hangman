import random

print("Welcome to Hangman Countries!")
print("\nHow to play:")
print("You will see a number of short lines together that represent the number of letters in the word you have to guess. ")
print("Write the letter that you think is included in the word.")
print("If you guess the correct letter, that letter will appear in the appropriate position in the word. It will replace one of the little lines ")
print("If the letter you guessed is not in the word, a part of the body will appear on the diagram below word .")
print("If the body becomes completed, you are 'hanged' which means you have lost.")
print("If you guess all the letters in the word before you are 'hanged', you win.")
input("Press ENTER to continue\n")

choose_level = input("\nChoose Level of Difficulty:\n1-Easy (6 lives)\n2-Medium (4 lives)\n3-Hard (2 lives)\n")

#Po wybraniu opcji trudnośći przypisuje nam liczbę żyćków
lives = 0
if choose_level == "1":
    lives = 6
elif choose_level == "2":
    lives = 4
elif choose_level == "3":
    lives = 2


#wczytuję listę krajów z pliku
list_of_countries = open("countries.txt").read().splitlines()

#losowanie 1 kraju z listy
selected_country = random.choice(list_of_countries)
print(selected_country)
#zostawiam do sprawdzania, potem usuniemy

#zliczenie liczby liter w wylosowanym wyrazie (chyba nie bedzie to będzie potrzebne, na razie zostawiam, najwyzej usuniemy)
number_of_letters = len(selected_country)
print(number_of_letters)
# zostawiam do sprawdzania, potem usuniemy

#zamiana string ze słowem na listę
list_of_letters = list(selected_country)
print(list_of_letters)
# zostawiam do sprawdzania, potem usuniemy

def hidden_letters():
    print_hidden_letters = ""
    for letter in list_of_letters:
        if letter == " ":
            letter = " "
        else:
            letter = "_ "
        print_hidden_letters += letter  
    print(print_hidden_letters)
hidden_letters()

# list_of_hidden_letters = hidden_letters(letter)

# print(list_of_hidden_letters)

player_guess = input()

#dodaje zgadniętą literę do wyświetlanego wyniku
def zgadywanie():
    print_zgadywanie = ""

    for letter in list_of_letters:
        if letter == player_guess:
            letter = player_guess
        elif letter == player_guess.upper():
            letter = player_guess
        elif letter == player_guess.lower():
            letter = player_guess
        elif letter == " ":
            letter = " "
        else:
            letter = "_ "
        print_zgadywanie += letter
    print(print_zgadywanie.upper())

zgadywanie()

        
