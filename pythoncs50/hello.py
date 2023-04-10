def format_name(name)->str:
    name = name.strip()
    name = name.title()
    return name

def print_first_name(name):
    name = (format_name(name).split(" "))[0]
    print(f"Hello, {name}!", end='\n')

def print_last_name(name):
    name = (format_name(name).split(" "))[1]
    print(f"Hello, {name}!", end='\n')

if __name__ == "__main__":
    name = input("what's your first and last name?\n")
    print_first_name(name)
    print_last_name(name)