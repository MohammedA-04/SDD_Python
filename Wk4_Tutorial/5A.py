# 5A Function checks whether passed string is a palindrome
# Palindrome = a word, phrase or seq that reads the same backwards as forwards

def isPalindrome(str):
    l_pos = 0
    r_pos = len(str) - 1

    while r_pos >= l_pos:
        if not str[l_pos] == str[r_pos]:
            return False
        l_pos += 1
        r_pos -= 1
    return True

print(isPalindrome('aza'))
