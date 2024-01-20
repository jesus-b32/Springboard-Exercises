def print_upper_words(word_list, ):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    Can pass set of letter and will prints words that start with one of those letters
    """
    for word in word_list:
        print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]) #must_start_with={"h", "y"}


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e."""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

# this should print "Echo"
print_upper_words2(["hello", "hey", "goodbye", "yo", "yes", "echo"]) #must_start_with={"h", "y"}


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given letter"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
