f = open("day2-input.txt", "r")
lines = f.read().split("\n")

lookup = {
  "A": "Rock",
  "X": "Rock",
  "B": "Paper",
  "Y": "Paper",
  "C": "Scissors",
  "Z": "Scissors",
}

losses = {
  "AZ", # Rock beats Scissors
  "BX", # Paper beats Paper
  "CY", # Scissors beats Rock
}

ties = {
  "AX",
  "BY",
  "CZ",
}

points = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3,
  'win': 6,
  'loss': 0,
  'tie': 3,
}

total_score = 0

for line in lines:
  player1 = line[0]
  player2 = line[2]
  print(f"{player1} ---> {player2}")
  print(f"{lookup[player1]} --> {lookup[player2]}")

  if f"{player1}{player2}" in ties:
    print("tie game!")
    total_score += points[lookup[player2]] + points["tie"]
  elif f"{player1}{player2}" in losses:
    print("You lose!")
    total_score += points[lookup[player2]] + points["loss"]
  else:
    print("You win!")
    total_score += points[lookup[player2]] + points["win"]
  
  print("TOTAL SCORE --> ", total_score)
  print("-----------")

  print("--------------------------")
  print("FINAL TOTAL SCORE --> ", total_score)
