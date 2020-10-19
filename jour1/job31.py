# creating empty list

lst = []

# number of elemetns as input
n = int(input("Enter number of students : "))

# iterating till the range
for i in range(0, n):
    note = int(input("Entrer le note: "))
    div = note // 5
    if (div+1)*5-note > 2:
        lst.append(note)  # adding the element
    else:
        lst.append((div+1)*5)
print(lst)
