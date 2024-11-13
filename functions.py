# Functions

# custom Function with default args

FILEPATH = "todos.txt"

# 1 Returns a value - 1 arg or param
def get_todos(filepath=FILEPATH):
    # with open('files/subfiles/todos.txt', 'r') as file_local:
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# 2 Does not return a value - 2 Args or param
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# Add __name__ == "__main__": construct
if __name__ == "__main__":
    print("Hello")
    print(get_todos())