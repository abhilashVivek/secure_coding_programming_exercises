# complete the function below
# say_hello should accept a users name, and then print out a custom greeting with their name

# print(say_hello('gilad'))
# should output something funny like : "hey gilad, your pants are on fire!!!!"


def say_hello(name):
    print(f"{name.upper()}! In the flesh, as I live and breathe!")
    
say_hello(input("Enter your name: "))