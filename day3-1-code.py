f = open("day3-input.txt", "r")
lines = f.read().split("\n")

total = 0
vals = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for line in lines:
  a = line[:(len(line)//2)]
  b = line[(len(line)//2):]
  
  shared = None

  for char in a:
    if char in b:
      shared = char

  val = vals.index(shared)
  total += val
  print(shared, val, total)

print(total)