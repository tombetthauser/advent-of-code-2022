f = open("day2-input.txt", "r")
lines = f.read().split("\n")

lookup = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors",
  "X": "loss",
  "Y": "draw",
  "Z": "win",
}

your_moves = {
  "AZ": "B", # Rock/A --> win --> Paper/B
  "BZ": "C", # Paper/B --> win --> Scissors/C
  "CZ": "A", # Scissors/C --> win --> Rock/A
  "AX": "C", # Rock/A --> lose --> Scissors/C
  "BX": "A", # Paper/B --> lose --> Rock/A
  "CX": "B", # Scissors/C --> lose --> Paper/B
  "AY": "A", # Rock/A --> draw --> Rock/A
  "BY": "B", # Paper/B --> draw --> Paper/B
  "CY": "C", # Scissors/C --> draw --> Scissors/C
}

points = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3,
  'X': 0,
  'Y': 3,
  'Z': 6,
}

total_score = 0

for line in lines:
  char1 = line[0]
  char2 = line[2]
  print(f"{char1} ---> {char2}")
  print(f"{lookup[char1]} --> {lookup[char2]}")

  chars = f"{char1}{char2}"

  your_move = your_moves[chars]
  print("your move --> ", your_move, " / ", lookup[your_move])

  score_add = points[char2] + points[lookup[your_move]]
  print("score addition --> ", score_add)
  total_score += score_add

  print("TOTAL SCORE --> ", total_score)
  print("-----------")

print("--------------------------")
print("FINAL TOTAL SCORE --> ", total_score)
