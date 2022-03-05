def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Returneaza string - se numeste Documentation Comment
    si se trece intre "" sau ''
    :param string: un string care va fi transformat
    :returns: stringul fara spatii si cu prima litera mare
    """
    new_string = string.strip()  # elimina spatiile de la inceput si sfarsit
    new_string = new_string.capitalize()
    return new_string


def add(first, second):
    """Adds two values
    Parameters:
        first: primul parametru care va fi adunat
        second: al doilea parametru care va fi adunat
    Returns:
        Suma celor doi parametri
    """
    return first + second


print(cleanup("  text de transformat"))
print(cleanup("tesT"))
print(cleanup(" un text "))
print(cleanup(" un text de schimbat in functia cleanup"))
print(cleanup.__doc__)
help(cleanup)
help(add)