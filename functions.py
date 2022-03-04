def cleanup(string):
    """Sterge spatiile de la inceput si sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Returneaza string
    """
    new_string = string.strip()
    new_string = new_string.capitalize()
    return string


print(cleanup("  text de transformat"))