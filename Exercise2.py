def is_it_valid(n):
    dot=0
    other=0
    for i in n:
        if i == ".":
            dot+=1
        if i == "@":
            other+=1
    if dot and other >= 1:
        return(True)
    else:
        return(False)
x=input()
print(is_it_valid(x))
        