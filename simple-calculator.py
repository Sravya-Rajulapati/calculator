print ("welcome to simple caluclator :")
x = int(input("enter x value  "))
y = int(input("enter y value "))
user_input= input("Please enter the operation serial number for it to perform: \n 1.Add \n 2.Substract \n 3.Multiply \n 4.Divide \n")

def main(user_input):
    match user_input:
        case "1":
            add()
        case "2":
            sub()
        case "3":
            multiply()
        case "4":
            division()

    # if (user_input == "1"):
    #     add()
    # elif user_input == "2":
    #     sub()
    # elif user_input == "3":
    #     multiply()
    # elif user_input == "4":
    #     division()  

def add():
    print(f"addition of {x} and {y} is {x + y}")

def sub():
    print(f"Substraction of {x} and {y} is {x - y}")

def multiply():
    print(f"Product of {x} and {y} is {x * y}")  

def division():
    if y == 0:
        print("cannot be divided by zero")
    else:
        print(f"Division of {x} and {y} is {x / y}") 

if __name__ == '__main__':
  main(user_input)