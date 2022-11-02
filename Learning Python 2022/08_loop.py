# while loop
i = 0
while i < 51:
    print(i)
    i += 1

# for loop
A = [1, 2, 3]
for j in A:
    print(j)

dict = {
    "name": "Udit",
    "age": 18
}

# itreating a dictionary
for key in dict.keys():
    print(f"{key} --> {dict[key]}")


# range(start,stop,stepover)

# print 0 to 100 by skipping every 2 values
for item in range(0, 101, 2):
    print(item)

# enumurate -> Helps to print index and items of an itreable thing
for index, item in enumerate(["Hello", "Udit", "Here"]):
    print(index, item)

# break and continue
for items in [1, 2, 3, 4, 5]:
    if items == 3:
        break
    print(items)  # 1,2

for items in [1, 2, 3, 4, 5]:
    if items == 3:
        continue
    print(items)  # 1,2,4,5
