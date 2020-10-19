def triangle(height):
    j = 0
    width = height
    for i in range(height):
        if i < (height-1):
            print((width-1) * " ", "/", j * " ", '\\', sep="")
        else:
            print((width - 1) * "", "/", j * "_", '\\', sep="")
        j = j + 2
        width = width-1


height = int(input("Entrer height: "))
triangle(height)
