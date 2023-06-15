
def palindrome_string(str):
    new_str = str[::-1]
    if str == new_str:
        return True
    else:
        return False

