"""
Wrap the code below in a try - except
What is the correct exception to use?

Fix the error by "padding" the word with blank spaces when the excption is hit.
"""

word = "hellothis"

for i in range(12):
    try:
        print(word[i])
    except IndexError:
        word += " "
    
print(f"'{word}' has {len(word[word.find('s')+1:])} extra characters. Totalling to {len(word)}.")