try:
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")
except ValueError:
    print("You entered a string instead of an int")