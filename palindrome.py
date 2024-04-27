def palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
