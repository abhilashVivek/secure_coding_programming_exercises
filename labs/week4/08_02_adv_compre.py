# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...288]}


#SOLUTION
start = 1
end=301       

dict1 = {i*3 : [i for i in range(1,i*3+1) if i%2==0] for i in range(start,end +1)}

print(dict1)