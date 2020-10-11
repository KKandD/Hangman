import random
#wczytuję listę krajów z pliku
list_of_countries = open("countries.txt").read().splitlines()

#losowanie 1 kraju z listy
selected_country = random.choice(list_of_countries)
#print(selected_country)
print(len(selected_country))


def lives_count():
    if level_dificultity == 1:
        lives = 6
    elif level_dificultity == 2:
        lives = 4
    elif level_dificultity == 3:
        lives = 2

def level_dificultity():
    pass
