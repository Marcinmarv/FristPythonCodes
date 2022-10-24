from art import logo
from art import vs
print(logo)
from game_data import data
import random
from replit import clear
def giera():
    score = 0
    end = False
    pierwsza={}
    pierwsza= random.choice(data)
    while not end:
      print(f"Compare A: {pierwsza['name']}, a {pierwsza['description']}, from {pierwsza['country']}")
      druga = {}
      druga = random.choice(data)
      print(vs)
      print(f"Compare B: {druga['name']}, a {druga['description']}, from {druga['country']}")
      druga2 = druga
      chose = input("Who has more fallowers? Type A or B ")
      if chose.upper() == "A":
        chose = pierwsza
        kom = druga
      else:
        chose = druga
        kom = pierwsza
      if chose['follower_count'] > kom['follower_count']:
        print("Dobra odpowiedz!")
        score += 1
        print(score)
        pierwsza = druga2
        clear()
        print(logo)
        print(f"Masz racje Twój wynik to:{score}!")
      else:
        end = True
        print(f"Zła odpowiedź koniec gry! Twój wynik to {score}!")
        

# def gra():
  
# pierwsza={}
# pierwsza= random.choice(data)
# print(f"Compare A: {pierwsza['name']}, a {pierwsza['description']}, from {pierwsza['country']}")
  
  
  
# a= random.choice(data)

# gra()
giera()