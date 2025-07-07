num1 = input("Please enter the first number \n")
num2 = input("please enter the second number \n")

print("\n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (x) \n 4. Division (/)")

operation = int(input('please Enter your operation'))

if operation == 1:
    addition = int(num1) + int(num2)
    print(f'Addition (+) = {addition}')
    print(type(addition))

elif operation == 2:
    subtraction = int(num1)-int(num2)
    print(f'subtraction (-) = {subtraction}')
    print(type(subtraction))


elif operation == 3:
    multiplication = int(num1)* int(num2)
    print(f'Multiplication (x) = {multiplication}')
    print(type(multiplication))

elif operation == 4:
    if num1 == 0 or num2 == 0:
        print("Your answer is undefined...one of them contains a zero (0)")
        exit()
    else:
        division = int(num1)/int(num2)
        print(f'Division (/) = {division} ')
        print(type(division))
    



       






