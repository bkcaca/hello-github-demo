# greet.py
def hello(name):
    if not name.strip():
        return "Error: Name cannot be empty!"
    return f"Hello, {name}! Welcome to GitHub Collaboration."

def main():
    user = input("Your name: ")
    print(hello(user))

if __name__ == "__main__":
    main()
