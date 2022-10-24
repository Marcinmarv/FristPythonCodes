from art import logo

import random
from replit import clear

koniec_gry = False

while not koniec_gry:
  print(logo)
  zycia = 0
  liczba = random.choice(range(1,100))
  #print(liczba)
  rodzaj = input("Witaj w Magicznej Liczbie!\nPomyślałem o liczbie między 1-100!\nWybierz poziom. Napisz 'p' dla prostego i 't' dla trudnego: ")
  if rodzaj == "p":
    zycia +=10
    print("Masz 10 prób!")
  else:
    zycia +=5
    print("Masz 5 prób!")
  gierka = False
  while not gierka:
    if zycia == 0:
      gierka = True
      print("Koniec szans! Koniec gry!")
    zgadywana = int(input("Podaj liczbę: "))
    if zgadywana == liczba:
      print("Brawo! Zgadłeś! Chyba oszukiwałeś :)")
      gierka = True
    elif zgadywana > liczba:
      zycia -= 1
      print(f"Za wysoka\nSpróbuj raz jeszcze\nPozostało Ci {zycia} szans!")
      if zycia == 0:
        gierka = True
        print(f"Koniec szans! Koniec gry!\nPoprawna liczba to {liczba}")
    elif zgadywana < liczba:
      zycia -= 1
      print(f"Za niska\nSpróbuj raz jeszcze\nPozostało Ci {zycia} szans!")
      if zycia == 0:
        gierka = True
        print(f"Koniec szans! Koniec gry!\nPoprawna liczba to {liczba}")
  gramy = input("Chcesz zagrać raz jeszcze?\nNapisz 't' na tak lub 'n' na nie ")
  if gramy == "t":
    clear()
    
  elif gramy == "n":
    koniec_gry = True
