# range function takes start, stop, and step which you can also see using
# help(range) this will show all the parameters and their default values
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue (skips the current iteration)
# break (breaks out of the loop)

# this is time library which we will use later here its just to show some delay while printing on the screen;
import time

# here we have created a while loop which is having a max_run value
# based on which we are running the loop until max_run is greater than 0
# loop should continue running
# ex:
# when max_run is in 2,4,6,8,20 these even numbers this the continue will be executed
# for other values it will go to next if condition which is checking if max_run is equal to 11
# if it is equal to 11 then it will break the loop
# but as we have discussed in one example if we make this 10 insted of 11 which will conflict with the above condition
# so first if condition will pass and it will not go to second if condition, so order in which you put your code matters here.

max_run = 21
while max_run > 0:
    print(max_run)
    max_run -= 1
    time.sleep(0.5)
    if max_run % 2 == 0:
        continue
    if max_run == 11:
        break


# here we are using a for loop to iterate over dictionary
# we have multiple options to do so first loop in keys ex: a, b, c
# second we can loop in values ex: 1, 2, 3
# or lastly we can loop over both key and value pair which will be like (a,1), (b,2), (c,3)
for value in {'a': 1, 'b': 2, 'c': 3}.values():
    print(value)

