def greet():
    print("Hello!")
    print("Welcome to Udemy Python Course")
    print("You have taken your first steps!")


greet()


#Function with inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today, {name}?")
    print(f"Hope to see you soon, {name}!")

input_name = input("Please enter your name: ")
greet_with_name(input_name)