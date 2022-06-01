# Miguel vive en un pueblo frutero con su hermana en el valle de Oz. Todos los días cosecha bananas y naranjas de su campo. Como son abundantes, suele darle 2 bananas y 1 naranja a su hermana. 
# No obstante Miguel siempre quiere quedarse con por lo menos una naranja, por lo cual le da una naranja a su hermana sólo cuando se cosechan al menos 2 naranjas.
# Miguel ahora quiere modernizarse, compró una cinta transportadora que detecta cada fruta que la atraviesa y te pide ayuda para escribir un programa que reciba el código generado por la máquina y devuelva la cantidad de bananas y naranjas que le quedarán luego de quitar las frutas que le dará a su hermana.

def miguelito(cosecha):
    B = 0
    N = 0
    for i in range(len(list(cosecha))):
        if cosecha[i] == 'B':
            B += 1
        if cosecha[i] == 'N':
            N += 1
    B -= 2
    if B < 0:
        B = 0
    N -= 1
    if N < 1:
        N = 1

    return print(B,"Bananas y",N,"Naranjas.")


miguelito("BBBBBNNNNNNNN") #Se espera 3 Bananas y 7 Naranjas
miguelito("BN") #Se espera 0 Bananas y 1 Naranja