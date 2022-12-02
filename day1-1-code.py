f = open("day1-input.txt", "r")
lines = f.read().split("\n")

i = 0
max_sum = 0
curr_sum = 0

while i < len(lines):
  if lines[i] == "":
    max_sum = max(curr_sum, max_sum)
    
    print("curr_sum --> ", curr_sum)
    print("max_sum --> ", max_sum)
    print("---------------------")

    curr_sum = 0
  else:
    curr_sum += int(lines[i])
  
  i += 1

print("FINAL MAX SUM --> ", max_sum)