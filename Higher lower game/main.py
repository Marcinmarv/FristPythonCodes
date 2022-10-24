from art import logo
from art import vs
print(logo)
from game_data import data
import random
from replit import clear


def game():
    score = 0
    end = False
    first={}
    first= random.choice(data)
    while not end:
      print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
      second = {}
      second = random.choice(data)
      print(vs)
      print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")
      second_2 = second
      chosen = input("Who has more fallowers? Type A or B ")
      if chosen.upper() == "A":
        chosen = first
        com = second
      else:
        chose = second
        com = first
      if chosen['follower_count'] > com['follower_count']:
        print("Dobra odpowiedz!")
        score += 1
        print(score)
        first = second_2
        clear()
        print(logo)
        print(f"Masz racje Twój wynik to:{score}!")
      else:
        end = True
        print(f"Zła odpowiedź koniec gry! Twój wynik to {score}!")
        
game()
