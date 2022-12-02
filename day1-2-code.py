f = open("day1-input.txt", "r")
lines = f.read().split("\n")

i = 0
max_sum = 0
curr_sum = 0

top_sums = [0, 0, 0]

while i < len(lines):
  if lines[i] == "":
    if curr_sum > top_sums[0]:
      top_sums.append(curr_sum)
      top_sums.sort()
      top_sums = top_sums[1:4]
    
    print("curr_sum --> ", curr_sum)
    print("top_sums --> ", top_sums)
    print("---------------------")

    curr_sum = 0
  else:
    curr_sum += int(lines[i])
  
  i += 1

print("FINAL MAX SUMS --> ", top_sums)
print("MAX SUMS SUM --> ", sum(top_sums))