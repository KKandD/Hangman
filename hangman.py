import random
#wczytuję listę krajów z pliku
list_of_countries = open("countries.txt").read().splitlines()

#losowanie 1 kraju z listy
selected_country = random.choice(list_of_countries)
#print(selected_country)
#zostawiam do sprawdzania, potem usuniemy

#zliczenie liczby liter w wylosowanym wyrazie (chyba nie bedzie to będzie potrzebne, na razie zostawiam, najwyzej usuniemy)
number_of_letters = len(selected_country)
#print(number_of_letters)
# zostawiam do sprawdzania, potem usuniemy

#zamiana string ze słowem na listę
list_of_letters = list(selected_country)
#print(list_of_letters)
# zostawiam do sprawdzania, potem usuniemy

def lives_count():
    if level_dificultity == 1:
        lives = 6
    elif level_dificultity == 2:
        lives = 4
    elif level_dificultity == 3:
        lives = 2

def level_dificultity():
    pass
