# 2B Activity | Write a Python function to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.

def changedollar(placeholder):
    char = placeholder[0]
    placeholder = placeholder.replace(char, '$')
    placeholder = char + placeholder[1:]
    return placeholder

print(changedollar('restart'))





