num = input("Enter your dimensions with number of disks and number of tower: ")
num = num.split(", ")
print(f"there are {num[0]} disks, and there are {num[1]} tower")


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)


# Driver code
n = int(num[0])
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods
