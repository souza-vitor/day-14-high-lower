import art
import game_data
import random
from replit import clear

def describe(num):
  return f"{game_data.data[num]['name']}, {game_data.data[num]['description']}, from {game_data.data[num]['country']}."

random_num = random.randint(0, len(game_data.data) - 1)

random_num2 = random.randint(0, len(game_data.data) - 1)

guess = ''
score = 0

while guess != False:
  print(art.logo)
  
  print(f"Current score: {score}")
  print()
  
  print(f"Compare A: {describe(random_num)}")

  print(art.vs)

  print(f"Compare B: {describe(random_num2)}")

  a = game_data.data[random_num]["follower_count"]
  b = game_data.data[random_num2]["follower_count"]

  response = ''

  if a > b:
    response = "a"
  elif b > a:
    response = "b"

  guess = input("Who has more followers? Type 'a' or 'b': ").lower()

  if guess == response:
    score += 1
    
    random_num = random.randint(0, len(game_data.data) - 1)
    random_num2 = random.randint(0, len(game_data.data) - 1)

    clear()
    
  else:
    guess = False

clear()
print(art.logo)
print(f"You're wrong. Your final score is {score} points.")