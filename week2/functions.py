# function declaration
def pretty_message(name): # name is function parameter which we will pass while calling the function
    print("=============================")
    print(f"hello, {name} how are you ?") # we are using f string to format the string which is helping us on printing the users name on the full message
    print("=============================")

print("hi there")
# this is where we are calling the pretty message function
pretty_message("lekhnath")
pretty_message("ankit")
pretty_message("sumit")


# what is function
# synctax to create a function is def functionname():
# by doing this we can create a function and put some block of code that we can use later


# function parameters
# we have two different kind of function parameters
# one is positional parameter another is keyword paramater
# difference
# ex 1 for positional arg
#   definition -> def function(arg1, arg2):
#   call       -> function(1, 2)
# here 1 will be passed to arg1 and 2 will be passed to arg2
# because this is positional argument and order on which you sent the value matters

def positional_argument(one, two, three):
    print(one, two, three)
positional_argument(1, 2, 3)

# ex 2 for keyword arg
# definition -> def function(arg1, arg2):
# call       -> function(arg2=1, arg1=2)
# here we are calling this function and passing keyword argument by saying that
# pass 1 in arg2 and pass 2 in arg1  which is denoted by arg1=2 and arg2=1


def keyword_argument(one, two, three):
    print(one, two, three)

keyword_argument(three=1, two=3, one=2)


# example on low level how args and keyword args works
# for example if we are passign positional arguments it will convert that into a list if we
# use a special syntax for that which is *args with this way we can pass any number of positional arguments
# ex:
def position_argument_with_filler(*args):
    print(args)

position_argument_with_filler(1, 2, 3, 4, 5)

# example of kwargs and how it work in low level
# for keyword arguments we can use **kwargs which is a special syntax for this
# and here also you can pass any no of keyword arguments
# ex:
def keyword_argument_with_fillter(**kwargs):
    print(kwargs)

keyword_argument_with_fillter(one=1, two=2, three=3, four=4)


# finally we can also mix those two so that function can take any no of positional and keyword argument
# ex:
def mix_argument_with_filler(*args, **kwargs):
    print(args, kwargs)
mix_argument_with_filler(1,2, 3, 4, one=1, two=2, three=3)

# what is return statement
# whenever or whereever a return statement is hit while calling a function
# that function will exit and return the location from where it all started or where its was called from
# ex:
# here the message after the return statement wont work
# and also the value on the return statemt will go the the location where this function is being called
# for example we can use variable = function() syntax to assign the value which is returned by the function call
def return_example():
    print("hi before return")
    return "this is the return"
    print("hi this is after return")

returned_value = return_example()
print(returned_value)
