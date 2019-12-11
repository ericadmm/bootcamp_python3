texto = "supercalfragilisticoespiralidoso"
print(texto[16:20])
print(len(texto))
print(texto[::-1])

def sq(num1, num2):
    if num1 == num2:
        return("square")
    else:
        return("rectangle")

print(sq(1,1))
print(sq(1,2))
print(sq(2,2))
print(sq(2,3))
print(sq(15,15))
print(sq(25,10))
print(sq(14,14))
print(sq(14,24))
print(sq(137,137))
print(sq(145,205))

def imp_pares(cadena):
    pos = 0
    for i in cadena:
        if pos % 2 == 0:
            print(i)
        pos = pos + 1

imp_pares("supercalifragilisticoespiralidoso")
