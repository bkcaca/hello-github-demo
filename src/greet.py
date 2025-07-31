# greet.py
def hello(name):
    if not name.strip():
        return "Error: Name can not be empty!"
    return f"Hello, {name}! Welcome to GitHub Collaboration."

if __name__ == "__main__":
    user = input("Your name: ")
    print(hello(user))
