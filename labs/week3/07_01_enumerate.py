# use a for loop with enumerate to go over the long word and
# sum all the indices for every single vowel
list_of_vowels = ["A","E","I","O","U"]
def sum_of_indices(word):
    print(word)
    word = word.upper()     #search for vowels becomes case-insensitive
    sum = 0
    for i in word:
        if i in list_of_vowels:
            sum += word.index(i)
    print(f"The sum of indices of vowels present in the above text is '{sum}'.")
            
    
# example:
#
# input: "hi I me
# i=1, I=3, e = 6,
# the sum is: 10

a_long_word = "the quick brown fox jumped over the lazy dog and then ran around and got very happy happy happy yes!"
sum_of_indices(a_long_word)
# the sum should be 1147 (you can check your code with this)
