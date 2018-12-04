# def add_numbers(number1, number2):
#     print(int(number1) + int(number2))
# print("adding 1 + 2:")
# add_numbers(1, 2)
#
# def print_value(value):
#     print(value)
#
# my_variable1="Carla"
# print_value(my_variable1)

#import this
#print(this)

def add_numbers(num1, num2):
    result = int(num1) + int(num2)
    return result

print(add_numbers(1, 4))

def is_num_negative(n):
    if n < 0:
        return True
    return False
the_number = input("Enter a number:")
if is_num_negative(int(the_number)):
    print("negative")
else:
    print("positive")

def hello(name="Unknown"):
    print("Hello " + name)
print(hello())