
name = "Bro" # global scope (available inside & outside functions)
x= 1
def display_name():
    name = "Code"    # local scope (available only inside this function)
    x= 3
    print(name)

display_name()
print(name)
print(x)