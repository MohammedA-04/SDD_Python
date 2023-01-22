def StringReplace(string):
    length = len(string)

    if length > 2:
        if string[-3:] == 'ing':
            string += 'ly'
        else:
            string += 'ing'
        return string

print(StringReplace('toast'))
print(StringReplace('sing'))
print(StringReplace('si'))

# So toast bigger than 2 --> else 'toast' + 'ing'
# So sing is bigger than 2 --> last 3 is equal to  'ing' -> 'sing' + 'ly'
# 'Si' smaller than 2 so not true hence it can't enter if block