# Using Functoin, conditionals 
# Build: Calculator CLI (add, subtract,multiply, divide)


# class Calculator :

#     def __init__(self,add,subtract,multiply, divide,user):
#         self.add = add
#         self.subtract = subtract
#         self.multiply = multiply
#         self.divide =  divide


def add():
    a = int(input('Enter first number (only whole numbers): '))
    b = int(input('Enter second number (only whole numbers): '))
    return a + b

def subtract():
    a = int(input('Enter first number (only whole numbers): '))
    b = int(input('Enter second number (only whole numbers): '))
    return a - b

def multiply():
    a = int(input('Enter first number (only whole numbers): '))
    b = int(input('Enter second number (only whole numbers): '))
    return a * b

def divide():
    a = int(input('Enter first number (only whole numbers): '))
    b = int(input('Enter second number (only whole numbers): '))
    if b == 0:
        print('Cannot divide by zero.')
        return None
    return a / b

while True:
 choice = input('Choose !! \n 1)add \n 2)sub \n 3)mul \n 4)div \n ').strip()
 if choice == '1':
    print(add())
    break
 elif choice == '2':
    print(subtract())
    break
 elif choice == '3':
    print(multiply())
    break
 elif choice == '4':
    print(divide())
    break
 else:
    print('Invalid choice,please choice to proceed with the following !!')

# ...End of code...