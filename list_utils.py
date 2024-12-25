def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list, needle, 1)

def find_n(list, needle, n):
    """
    Devuelve True si en list hay n o más ocurrencias de needle 
    Devuelve False si hay menos o si n < 0
    """
    # si n > 0
    if n>=0:
        # Inicializamos el índice y el contador
        index = 0
        count = 0

        # Mientras no hayamos encontrado el elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
        # si lo encontramos, actualizamos el contador
            if needle == list[index]:
                count = count + 1
        # avanzamos al siguiente elemento
            index = index + 1
        
        return count>=n
    # devolvemos el resultado de comparar el contador con n

    else:
        return False
    
def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o más needles seguidos y False a todo lo demás
    """
    #si n>=0
    if n>=0:
        index = 0
        count = 0
        roll = False
        
    # Inicializo el índice, el contador y el indicador de racha
        while count < n and index < len(list):
    # Mientras no hay encontrado n needles seguidos o la lista no se haya acabado
            if needle == list[index]:
                roll = True
                count = count + 1
            else:
                roll = False
                count = 0
            index = index + 1

        return count >=n and roll
    
    else:
        return False

    # si lo encuentro, activo el indicador de rachas y actualizo el contador
    # si no lo encuentro, desactivo el indicador de racha y pongo a cero el contador
    # avanzo el siguiente elemento
    # devolvemos el resultado de comparar el contador con n siempre y cuando estemos en racha