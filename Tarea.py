texto = "supercalfragilisticoespiralidoso"
print(texto[16:20])
print(len(texto))
print(texto[::-1])

posicion = 0
letra = int(texto[0:32])
mod = letra % 2
if mod > 0:
    print(letra)
posicion = posicion + 1
