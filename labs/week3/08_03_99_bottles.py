# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it
num = 100
while num > 0:
    print(f"there are '{num}' jars of payasam on the counter ...... now i ate one!")
    num -=1
while num == 0:
    print(f"there are '{num}' jars of payasam on the counter - none left to eat!\nnow I will go vomit....")
    break
