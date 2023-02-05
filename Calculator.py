import math

select_message  = "Select one of the following items:"
selection_1     = """B) - Binary Mathematical Operations such as addition and subtraction.
U) - Unary Mathematical Operations such as square root, and log."""
selection_2     = """A) - Advanced Mathematical Operations using variables or arrays.
V) - Define variables and assign them values.
M) - Check the memory.
R) - Clear the memory."""
selection_3     = "X) - Exit."
exit_message    = "Closing the program..."
advanced_exit   = "Returning to the main menu..."

def print_main_selection():
    print("Welcome to the Command-Line Calculator!")
    print("Developer: Keigo Katanaga")
    print("Version: 1.0")
    print("Date: 01/15/2022")
    print("------------------------------------------")
    print(select_message, '\n', selection_1, '\n', selection_2, '\n', selection_3, sep='')
    print("------------------------------------------")

def print_advanced_selection():
    print("------------------------------------------")
    print(select_message, '\n', selection_1, '\n', selection_3, sep='')
    print("------------------------------------------")

def ask_selection():
    selection = input("Enter your selection: ").upper()
    while selection not in selection_dictionary:
        selection = input("Error: Please enter a specified selection: ").upper()
    return selection

def ask_advanced_selection():
    advanced_selection = input("Enter your advanced selection: ").upper()
    while advanced_selection not in selection_dictionary["A"]:
        advanced_selection = input("Error: Please enter a specified selection: ").upper()
    return advanced_selection
    
def ask_num_or_var(selection, message):
    value = 0

    while True:
        try:
            value = input(message)
            return float(value)
        except ValueError:
            if selection == "A":
                if value in variable_memory:
                    return variable_memory[value]
                print("Error: Please enter a number or a specified variable")
            else:
                print("Error: Please enter a number")

def ask_operation(selection):
    operation = input("Enter the operation: ").upper()
    while operation not in selection_dictionary[selection]:
        operation = input("Error: please enter a proper operation: ").upper()
    return operation
    
def operate(selection, operation, first, second = 0):
    print_unary = { "S": lambda x,z : print(f"Square root of {x} is {z:.2f}"),
                    "L": lambda x,z : print(f"Log of {x} is {z:.2f}"),
                    "E": lambda x,z : print(f"Exponent of {x} (e^{x}) is {z:.2f}"),
                    "C": lambda x,z : print(f"Ceiling of {x} is {z:.2f}"),
                    "F": lambda x,z : print(f"Floor of {x} is {z:.2f}")}

    if selection == "B":
        result = selection_dictionary[selection][operation](first, second)
        print(first, operation, second, "is", result)
    else:
        result = selection_dictionary[selection][operation](first)
        print_unary[operation](first, result)
    return result

def print_result(memory):
    position = ''
    while True:
        try:
            position = int(input("Pick a position to print, where 0 prints everything and a non-zero input only prints one result: "))
            if position == 0:
                print(memory)
            elif position > 0:
                print(f"Index {position - 1} contains: {memory[position - 1]:.2f}")
            else:
                print(f"Index {position} contains: {memory[position]:.2f}")
            break
        except:
            print("Error: Please enter an integer within range (0-", len(memory), ")")

selection_dictionary = {"B": {  "+": lambda x,y : x+y, 
                                "-": lambda x,y : x-y, 
                                "*": lambda x,y : x*y, 
                                "/": lambda x,y : x//y, 
                                "%": lambda x,y : x%y, 
                                "^": lambda x,y : x**y}, 
                        "U": {  "S": lambda x : math.sqrt(x), 
                                "L": lambda x : math.log(x), 
                                "E": lambda x : math.exp(x), 
                                "C": lambda x : math.ceil(x), 
                                "F": lambda x : math.floor(x)}, 
                        "A": ("B", "U", "X"), 
                        "V": "Variable", 
                        "M": "Memory", 
                        "X": "Exit"}
variable_memory      = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}

print_main_selection()

selection = ''
result_memory = []

while selection != 'X':
    selection = ask_selection()

    if selection == 'B':
        num_one = ask_num_or_var(selection, "Enter the first number: ")

        operation = ask_operation(selection)

        num_two = ask_num_or_var(selection, "Enter the second number: ")

        result_memory.append(operate(selection, operation, num_one, num_two))
    
    elif selection == 'U':
        operation = ask_operation(selection)

        num_one = ask_num_or_var(selection, "Enter a number: ")

        result_memory.append(operate(selection, operation, num_one))

    elif selection == 'A':
        print_advanced_selection()
        advanced_selection = ''

        while advanced_selection != 'X':
            advanced_selection = ask_advanced_selection()

            if advanced_selection == 'B':
                num_one = ask_num_or_var(selection, "Enter the first number: ")

                operation = ask_operation(advanced_selection)

                num_two = ask_num_or_var(selection, "Enter the second number: ")

                result_memory.append(operate(advanced_selection, operation, num_one, num_two))
            
            elif advanced_selection == 'U':
                operation = ask_operation(advanced_selection)

                num_one = ask_num_or_var(selection, "Enter a number: ")

                result_memory.append(operate(advanced_selection, operation, num_one))
            
            elif advanced_selection == 'X':
                print(advanced_exit)
                break

            print("------------------------------------------")
    
    elif selection == 'V':
        variable = input("Choose a variable (a-e): ")
        while variable not in variable_memory:
            variable = input("Error: please enter a variable name (a-e): ")
        
        variable_memory[variable] = ask_num_or_var(selection, "Enter a number: ")
        print("Variable", variable, "now contains:", variable_memory[variable])

    elif selection == 'M':
        position = ''
        if len(result_memory) == 1:
            print("There are", len(result_memory), "item in memory.")
        else:
            print("There are", len(result_memory), "items in memory.")
        
        print_result(result_memory)

    elif selection == 'C':
        print("Clearing the memory...")
        result_memory.clear()
        
    elif selection == 'X':
        print(exit_message)
        break

    print("------------------------------------------")
