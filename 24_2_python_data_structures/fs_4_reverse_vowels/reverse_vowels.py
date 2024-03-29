def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiou'
    vowels_list = [] 
    vowels_str = ''
    index = 0

    for char in s:
        if char.lower() in vowels:
            vowels_list.append(char)

    vowels_list.reverse()

    for char in s:
        if char.lower() in vowels:
            vowels_str += vowels_list[index]
            index += 1
        else:
            vowels_str += char
    
    return vowels_str