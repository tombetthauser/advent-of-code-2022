f = open("day3-input.txt", "r")
lines = f.read().split("\n")

total = 0
vals = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0
while i < len(lines):
  a = lines[i]
  b = lines[i+1]
  c = lines[i+2]
  
  shared = None

  for char in a:
    if char in b and char in c:
      shared = char

  val = vals.index(shared)
  total += val
  i += 3

print(total)