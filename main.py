calculator_input = "a"
input_list = ["a"]
x = 0

print("Input for calculator: ")
calculator_input = input()

str(calculator_input)
input_list = calculator_input.split()
input_list.extend("0")

if input_list[1] == "/" :
    print("this is a division")
    x = int(input_list[0]) / int(input_list[2])
    print(str(x))

elif input_list[1] == "*" :
    print("this is a multiplication")
    x = int(input_list[0]) * int(input_list[2])
    print(str(x))

elif input_list[1] == "-" :
    print("this is a substraction")
    x = int(input_list[0]) - int(input_list[2])
    print(str(x))

elif input_list[1] == "+" :
    print("this is a sum")
    x = int(input_list[0]) + int(input_list[2])
    print(str(x))
else:
    print("there is any valid operator")
