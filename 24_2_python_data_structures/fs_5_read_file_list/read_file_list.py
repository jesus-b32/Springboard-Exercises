def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    with open(filename) as file: # opening a file with an alias name using with statement; defualts to read mode
    #The with statement automatically takes care of closing the file once it leaves the with block, even in cases of error. Recommend to use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.
        for line in file:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")