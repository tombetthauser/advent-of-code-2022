f = open("day4-input.txt", "r")
lines = f.read().split("\n")

overlaps = 0

for line in lines:
  split1 = line.split(",")
  split2 = [int(ele) for ele in split1[0].split("-")]
  split3 = [int(ele) for ele in split1[1].split("-")]

  if split2[0] <= split3[0] and split2[1] >= split3[1]:
    overlaps += 1
  if split3[0] <= split2[0] and split3[1] >= split2[1]:
    overlaps += 1
  
  # print(split1, split2, split3, overlaps)
print(overlaps)