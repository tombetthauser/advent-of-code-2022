f = open("day4-input.txt", "r")
lines = f.read().split("\n")

f = open("day5-input.txt", "r")
sections = f.read().split("\n\n")

matrix = sections[0].split("\n")
matrix.reverse() 

move_splits = [move.split(" ") for move in sections[1].split("\n")]
move_dicts = [{"times": int(move[1]), "from": int(move[3]), "to": int(move[5])} for move in move_splits]

num_stacks = int(matrix[0].split(" ")[-2])
matrix.pop(0)

stacks = [[] for _ in range(num_stacks+1)]

for row in matrix:
  i = 1
  j = 1
  while i < len(row):
    if row[i] != " ":
      stacks[j].append(row[i])
    i += 4
    j += 1

def print_stack(stacks):
  for stack in stacks:
    print(stack)

print_stack(stacks)
print("---------------")

for move in move_dicts:
  times = move['times']
  start = move['from']
  target = move['to']
  
  print_stack(stacks)
  print(move)
  print("~~~~~~~~~")
  for _ in range(times):
    if len(stacks[start]) > 0:
      ele = stacks[start].pop()
      stacks[target].append(ele)

print_stack(stacks)

lasts = [stack[-1] for stack in stacks[1:]]
print("FINAL ANSWER --> ", ''.join(lasts))

#         [Z] 
#         [N]
#         [D]   
# [C] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2