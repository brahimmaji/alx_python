from sys import argv

def print_arguments():
    num_args = len(argv) - 1  

    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print(f"Number of argument(s): {num_args}, {'argument' if num_args == 1 else 'arguments'}:")
        
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    print_arguments()