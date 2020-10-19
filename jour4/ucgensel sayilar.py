def tri_numbers(x):
    if(x > 0):
        result = x+tri_numbers(x-1)
        print(result)
    else:
        result = 0
    return(result)


tri_numbers(5)
print(dir(list))
