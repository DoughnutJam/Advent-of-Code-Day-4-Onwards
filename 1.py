file = open("Input4.txt","r")

with open("Input4.txt") as file:
    lines = file.read().splitlines()


size = len(lines) 
idx_list = [idx + 1 for idx, val in
            enumerate(lines) if val == ''] 
  
  
res = [lines[i: j] for i, j in
        zip([0] + idx_list, idx_list + 
        ([size] if idx_list[-1] != size else []))]

print(res[0])


for i in res:
    for j in res:
        fullstring= ' '.join(res[0])

print(fullstring)
