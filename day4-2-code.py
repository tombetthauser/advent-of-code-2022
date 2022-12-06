f = open("day4-input.txt", "r")
lines = f.read().split("\n")

overlaps = 0

for line in lines:
  split1 = line.split(",")
  split2 = [int(ele) for ele in split1[0].split("-")]
  split3 = [int(ele) for ele in split1[1].split("-")]

  a1 = split2[0]
  a2 = split2[1]
  b1 = split3[0]
  b2 = split3[1]

  if split3[0] <= split2[0] <= split3[1]:
    overlaps += 1
  elif split3[0] <= split2[1] <= split3[1]:
    overlaps += 1
  elif split2[0] <= split3[1] <= split2[1]:
    overlaps += 1
  elif split2[0] <= split3[0] <= split2[1]:
    overlaps += 1
  
  print(split2, split3, overlaps)
  # print("a1 < b1 < a2", a1 < b1 < a2)
print(overlaps)