def search4vowels(phrase:str)-> set:
    """zwraca samogłoski we frazie podanej jako argument"""
    vowels=set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str = "aeiou")->set:
    "zwraca zbiór liter ze zmiennej letters znalezionych  w zmiennej phrase"""
    return set(letters).intersection(set(phrase))

# print (search4vowels ('ania'))
    


