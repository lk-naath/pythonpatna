# topics
# 1. mutable variable
# 2. emutable variable

num = 123

string = "123455"
array = [2,3,3,4,5]
dicts = {'a': 1, 'b': 2}
sets = {1,2, 2, 3, 4, 5, 5}
tupple = (1,2,3)

# print(array[1:-1])
# print(array[0], array[-1])
array[0] = 5
dicts['a'] = 5
# assigment not allowed in string
# string[0] = '5'
# tupple[0] = 5

# print(string[0], array[0], dicts['a'], tupple[0])

print(list(string))
print(int(string))
print(float(string))
print(f"'{str(array)}'")
print(list(dicts.keys()))
print(list(tupple))
print(tuple(array))
print(list(sets))
print(set(array))

print(list(reversed(array)))
print(list(reversed(string)))
print(sum(array))
