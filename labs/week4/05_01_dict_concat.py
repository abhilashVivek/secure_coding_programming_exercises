# Exercise

# Write a program to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Expected Results: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic_list = [dic1,dic2,dic3]

dict_op ={}
for i in dic_list:
    dict_op.update(i)

print(dict_op)