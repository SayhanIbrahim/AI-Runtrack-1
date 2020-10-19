def rectangle(width, height):
    for i in range(height):
        if i == 0:
            for j in range(width):
                if j == 0:
                    print("|", end="")
                elif j < width-1:
                    print("-", end="")
                elif j == (width-1):
                    print("|")
                else:
                    break

        elif i == (height-1):
            for j in range(width):
                if j == 0:
                    print("|", end="")
                elif j < width-1:
                    print("-", end="")
                elif j == (width-1):
                    print("|")
        else:
            print("|", (width - 4) * " ", "|")


width = int(input("Etrer de width: "))
height = int(input("Etrer de height: "))
rectangle(width, height)
