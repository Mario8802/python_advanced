import string


def is_palindrome(word):
    cleaned_word = word.lower()
    cleaned_word = "".join(filter(lambda char: char.isalnum(), cleaned_word))

    return cleaned_word == cleaned_word[::-1]


print(is_palindrome("It's very boring afternoon!"))
