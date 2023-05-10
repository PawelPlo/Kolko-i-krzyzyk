while True:
    nr_1 = "-"
    nr_2 = "-"
    nr_3 = "-"
    nr_4 = "-"
    nr_5 = "-"
    nr_6 = "-"
    nr_7 = "-"
    nr_8 = "-"
    nr_9 = "-"
    wygrana_1 = [1, 2, 3]
    wygrana_1 = sorted(wygrana_1)
    wygrana_2 = [4, 5, 6]
    wygrana_2 = sorted(wygrana_2)
    wygrana_3 = [7, 8, 9]
    wygrana_3 = sorted(wygrana_3)
    wygrana_4 = [1, 5, 9]
    wygrana_4 = sorted(wygrana_4)
    wygrana_5 = [3, 5, 7]
    wygrana_5 = sorted(wygrana_5)
    wygrana_6 = [1, 4, 7]
    wygrana_6 = sorted(wygrana_6)
    wygrana_7 = [2, 5, 8]
    wygrana_7 = sorted(wygrana_7)
    wygrana_8 = [3, 6, 9]
    wygrana_8 = sorted(wygrana_8)
    gra = 0
    ruch = 0
    zapytanie = input("czy chcesz rozpoczac nowa gre? t/n:")
    if zapytanie == "n":
        break
    if zapytanie != "t" and zapytanie != "n":
        print("wybrales zla opcje")
        continue
    if zapytanie == "t":
        print("Kolko i krzyzyk. Gre rozpoczyna komputer. Komputer gra znakiem 'x', Ty znakiem 'o'")
        print("""Uklad pol: 
         [1]  [2]  [3] 
         [4]  [5]  [6] 
         [7]  [8]  [9]""")
        print()
        numery_komputera = []
        numery_gracza = []
        gra = 0
        ruch = 0
        from random import random
        for gra in range(0, 100):
            wybor_komputera = int(1 + random() * 9)
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
            print("Ruch komputera:")
            print("""       {}  {}  {} 
       {}  {}  {} 
       {}  {}  {} """.format(nr_1, nr_2, nr_3, nr_4, nr_5, nr_6, nr_7, nr_8, nr_9))
            print()
            ruch = ruch + 1
            if wygrana_1 == sorted(numery_komputera) or wygrana_2 == sorted(numery_komputera) or wygrana_3 == sorted(numery_komputera):
                print("Komputer wygral")
                break
            if wygrana_4 == sorted(numery_komputera) or wygrana_5 == sorted(numery_komputera) or wygrana_6 == sorted(numery_komputera):
                print("Komputer wygral")
                break
            if wygrana_7 == sorted(numery_komputera) or wygrana_8 == sorted(numery_komputera):
                print("Komputer wygral")
                break
            if ruch == 9:
                print("Gra skonczona")
                continue
            else:
                while True:
                    wybor_gracza = input("Wskaz nr pola, ktore chcesz zaznaczyc:  ")
                    wybor_gracza = int(wybor_gracza)
                    if wybor_gracza in numery_komputera or wybor_gracza in numery_gracza:
                        print("Wybrales zle pole")
                    else:
                        numery_gracza.append(wybor_gracza)
                        break
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
                print("""       {}  {}  {} 
       {}  {}  {} 
       {}  {}  {} """.format(nr_1, nr_2, nr_3, nr_4, nr_5, nr_6, nr_7, nr_8, nr_9))
                ruch = ruch + 1
                if wygrana_1 == sorted(numery_gracza) or wygrana_2 == sorted(numery_gracza) or wygrana_3 == sorted(numery_gracza):
                    print("Wygrales")
                    break
                if wygrana_4 == sorted(numery_gracza) or wygrana_5 == sorted(numery_gracza) or wygrana_6 == sorted(numery_gracza):
                    print("Wygrales")
                    break
                if wygrana_7 == sorted(numery_gracza) or wygrana_8 == sorted(numery_gracza):
                    print("Wygrales")
                    break
                else:
                    print("Twoj ruch\n\n")
                    continue


