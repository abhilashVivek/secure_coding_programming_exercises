# recreate your previous generator from 01, but use a generator expression

start = 1
stop = 11


my_gen = (i for i in range(start, stop +1) if i % 2 == 0)  # fill out the code to make it work!


# practice using your generator
for i in my_gen:
    print(i)


print("second run!")
print()
# does it work two times?
for i in my_gen:
    print(i)
# it wont work  because it has already generated all th numbers and now its empty