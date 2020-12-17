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
#how to split ID (eyrs:1233) to 'EYRS' '123'

print(ID)
print(ID[0])
print(ID[0][0])
#key[0] is first part key [1] is second part

for firstl in ID:
    for elem in firstl:
        for k in elem:
            splitelem = elem.split(':',2)

#split the keys & values into two list
#write a function that takes a list of a passport and see if it's valid. better practice to write function outside for loop & call it inside
#in the first for loop, call that function with that firstL
#if func true +1 if not do not.
#use split, 
    
print(splitelem[1])
