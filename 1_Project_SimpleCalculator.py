#Simple Calculator

value1= int(input("Enter your first value: "))
value2= int(input("Enter your second value: "))

print("Enter the operation that you want to perform from the following list: \n + for addition \n - for subtraction \n * for multiplication \n / for division")

op = input("Enter the openation: ")

match op:
    case "+":
        print(f"{value1} + {value2} = {value1+value2}")
        
