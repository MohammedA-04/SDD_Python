# Task 2E - Language game where you move 1st letter to the end + add '.ay'
    # For Example 'Python' -> 'ythonpay'

# Steps needed:
# / Ask user to input word in English
# / Make sure user input English Word
# / Covert the word from English to Pig Latin
# / Display the Translation Result
print("Hello Pigs")
Pyg = "ay"
Original = input("Input any WORD in the English Language =")


if len(Original) > 0 and Original.isalpha():
    Word = Original.lower()                    # Convert to Lowercase so it worked on
    First = Original[0]                        # [0] Index 1 = 1st Letter [E.g., 'D']
else:
    print ("empty")                            # If FALSE then "Empty"

New_word = Word + First + Pyg                  # New Word will consist of these variables
New_word = New_word[1:]                        # Miss [Index 0] and Start From [Index 1]
print(f"Answer In Pig Latin", New_word)        # Pt2.. So [*d*] // [og] + [d] + [ay] = ogday
