print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")

min = 1
max = 1001

idx = 0
while idx < 10:
    guess = int((max - min) / 2) + min
    print(f"Zgaduję {guess}")
    ans_1 = input('Podaj czy jest to "Za mało", "Za dużo" czy "Zgadłeś": ')

    if ans_1 == "Zgadłeś":
        print("Wygrałem!")
        break
    elif ans_1 == "Za dużo":
        max = guess
        idx += 1
    else:
        min = guess
        idx += 1
