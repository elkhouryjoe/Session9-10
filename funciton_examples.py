def greet():
    """
    simple function printing hello
    :return: 0
    """
    print("Hello")
    return 0

def greet_improved(name):
    """
    more complex greet that takes a name as a param
    :param name: the name of the person to greet
    :return:
    """

    print("hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_operation(x,y):
    """
    custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x+y
    """
    result = 10*x + y
    return result

print(custom_operation(5,8))
x = custom_operation(5,9)
print(f"the result of custom operation is: {x}")
x = custom_operation(y=9, x=5) # arguments by name!
print(f"the result of custom operation is: {x}")