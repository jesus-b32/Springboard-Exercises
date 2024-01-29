def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # lower_phrase = phrase.lower()

    word_list = phrase.split()
    capitalized_words = [word.capitalize() for word in word_list]

    return ' '.join(capitalized_words)
    # for word in word_list:


