file = open("Input4.txt","r")

#byr birthyear
#iyr Issue year
#eyr Exp year
#hgt height
#hcl Hair color

#ecl eye color
#pid passport ID
#cid Country ID

lines = file.read().split('\n\n')
lines = [items.replace('\n',' ') for items in lines]
ID = [threecode.split(' ') for threecode in lines]

key=ID[0][1].split(':',2)
#splitting ID (eyrs:1233)

print(ID[0][1])

#key[0] is first part key [1] is second part

for i in ID:
    for j in i:
        for k in j:
            splitelem = j.split(':',2)

#split the keys & values into two list

print(splitelem)
