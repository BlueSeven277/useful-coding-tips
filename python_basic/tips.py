'''
    Some useful tips.
    Use simple code to achieve difficult functions - what I learned to provide pretty code from recent work
'''
# 1. Tell if the list contains same elements
def judge_unique(lst):
    return len(lst) == len(set(lst))

lst = [1, 1, 2, 3, 4, 5, 5]
print(judge_unique(lst))
lst2 = [1, 2, 3, 4, 5]
print(judge_unique(lst2))


# 2. Print a string for n times
s = "hello "
print(s*5)


# 3. Filter elements in a list
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# 4.Zip or unzip

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']
# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)

# unzip 
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(set(transposed))


# 5. print connection by 'join' instead of for loop

hobbies = ["basketball", "football", "swimming"]

print("My hobbies are: " + ", ".join(hobbies))