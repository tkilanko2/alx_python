#!/usr/bin/python3

def main():
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments and appropriate label
    if num_arguments == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num_arguments == 1:
        print("Number of argument(s): 1.")
        print("1:", sys.argv[1])
    else:
        print(f"Number of argument(s): {num_arguments}.")
        for i in range(1, num_arguments + 1):
            print(f"{i}: {sys.argv[i]}")
            
