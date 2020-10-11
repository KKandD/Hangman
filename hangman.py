list_of_countries = open("countries.txt").read().splitlines()

print(list_of_countries)

def lives_count():
    if level_dificultity == 1:
        lives = 6
    elif level_dificultity == 2:
        lives = 4
    elif level_dificultity == 3:
        lives = 2

def level_dificultity():
    pass
