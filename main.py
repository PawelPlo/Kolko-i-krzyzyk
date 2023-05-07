from random import random
nr_1 = "-"
nr_2 = "-"
nr_3 = "-"
nr_4 = "-"
nr_5 = "-"
nr_6 = "-"
nr_7 = "-"
nr_8 = "-"
nr_9 = "-"
numery_komputera = list()
numery_gracza = list()
gra = 0



for gra in range(0, 100):
    wybor_komputera = int(1 + random() * 9)
    print(wybor_komputera)
    if wybor_komputera in numery_komputera or wybor_komputera in numery_gracza:
        continue
    else:
        numery_komputera.append(wybor_komputera)
    if 1 in numery_komputera:
        nr_1 = "x"
    if 1 in numery_gracza:
        nr_1 = "o"
    if 2 in numery_komputera:
        nr_2 = "x"
    if 2 in numery_gracza:
        nr_2 = "o"
    if 3 in numery_komputera:
        nr_3 = "x"
    if 3 in numery_gracza:
        nr_3 = "o"
    if 4 in numery_komputera:
        nr_4 = "x"
    if 4 in numery_gracza:
        nr_4 = "o"
    if 5 in numery_komputera:
        nr_5 = "x"
    if 5 in numery_gracza:
        nr_5 = "o"
    if 6 in numery_komputera:
        nr_6 = "x"
    if 6 in numery_gracza:
        nr_6 = "o"
    if 7 in numery_komputera:
        nr_7 = "x"
    if 7 in numery_gracza:
        nr_7 = "o"
    if 8 in numery_komputera:
        nr_8 = "x"
    if 8 in numery_gracza:
        nr_8 = "o"
    if 9 in numery_komputera:
        nr_9 = "x"
    if 9 in numery_gracza:
        nr_9 = "o"

    print(""" {}  {}  {} 
 {}  {}  {} 
 {}  {}  {} """.format(nr_1, nr_2, nr_3, nr_4, nr_5, nr_6, nr_7, nr_8, nr_9))
    print("Ruch komputera\n\n")
    wybor_gracza = input("Wskaz nr pola, ktore chcesz zaznaczyc:  ")
    wybor_gracza = int(wybor_gracza)
    if wybor_gracza not in numery_komputera or wybor_gracza not in numery_gracza:
        numery_gracza.append(wybor_gracza)
    else:
        print("Wybrales zajete pole")
        wybor_gracza = input("Wskaz nr pola, ktore chcesz zaznaczyc:  ")
    if 1 in numery_komputera:
        nr_1 = "x"
    if 1 in numery_gracza:
        nr_1 = "o"
    if 2 in numery_komputera:
        nr_2 = "x"
    if 2 in numery_gracza:
        nr_2 = "o"
    if 3 in numery_komputera:
        nr_3 = "x"
    if 3 in numery_gracza:
        nr_3 = "o"
    if 4 in numery_komputera:
        nr_4 = "x"
    if 4 in numery_gracza:
        nr_4 = "o"
    if 5 in numery_komputera:
        nr_5 = "x"
    if 5 in numery_gracza:
        nr_5 = "o"
    if 6 in numery_komputera:
        nr_6 = "x"
    if 6 in numery_gracza:
        nr_6 = "o"
    if 7 in numery_komputera:
        nr_7 = "x"
    if 7 in numery_gracza:
        nr_7 = "o"
    if 8 in numery_komputera:
        nr_8 = "x"
    if 8 in numery_gracza:
        nr_8 = "o"
    if 9 in numery_komputera:
        nr_9 = "x"
    if 9 in numery_gracza:
        nr_9 = "o"
    print(""" {}  {}  {} 
 {}  {}  {} 
 {}  {}  {} """.format(nr_1, nr_2, nr_3, nr_4, nr_5, nr_6, nr_7, nr_8, nr_9))
    print("Twoj ruch\n\n")
    continue


