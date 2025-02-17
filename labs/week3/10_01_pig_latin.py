# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay


story = """

At a great meeting of the Animals, who had gathered to elect a new ruler, the Monkey was asked to dance. This he did so well, with a thousand funny capers and grimaces, that the Animals were carried entirely off their feet with enthusiasm, and then and there, elected him their king.

The Fox did not vote for the Monkey and was much disgusted with the Animals for electing so unworthy a ruler.

One day he found a trap with a bit of meat in it. Hurrying to King Monkey, he told him he had found a rich treasure, which he had not touched because it belonged by right to his majesty the Monkey.

The greedy Monkey followed the Fox to the trap. As soon as he saw the meat he grasped eagerly for it, only to find himself held fast in the trap. The Fox stood off and laughed.

"You pretend to be our king," he said, "and cannot even take care of yourself!"

Shortly after that, another election among the Animals was held.
"""

words = story.split()
new_list = []
suffix = "ay"
punctuations = [".",",","!","?","'","(",")",":",";","/","-","_",'"']
for word in words:
    word_without_punctuation = word.strip('".,!?/-_:;()')
    pl_word = ""
    if word_without_punctuation:
        letter1 = word_without_punctuation[0:1]
        remaining = word_without_punctuation[1:]
        index = -1
        punctuation = ""
        while word[index] in punctuations:
            punctuation = word[index] + punctuation
            index -=1
        if punctuation:
            pl_word = pl_word + remaining + letter1 + suffix + punctuation
        else:
            pl_word = pl_word + remaining + letter1 + suffix
        new_list.append(pl_word)
new_string = ""
for i in new_list:
    new_string = new_string + " " + i
print(new_string)           #im not able to figure out how to add next line character in the new string
        