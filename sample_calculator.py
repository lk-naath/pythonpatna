
def sum(one, two):
    return one + two

def subtract(one, two):
    return one - two

def multiply(one, two):
    return one * two



print("please enter your choice")
print("1. sum")
print("2. subtract")
print("3. multiply")

one = int(input("first number:: "))
two = int(input("second number:: "))

choice = input("your choice:: ")


match choice:
    case '1':
        print(sum(one, two))
    case '2':
        print(subtract(one, two))
    case '3':
        print(multiply(one, two))

        
        


    
