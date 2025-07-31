"""A simple greeting application."""

def hello(name: str) -> str:
    """Returns a greeting message."""
    if not name.strip():
        return "Error: Name cannot be empty!"
    return f"Hello, {name}! Welcome to GitHub Collaboration."

def main():
    """Main function to run the application."""
    user = input("Your name: ")
    print(hello(user))

if __name__ == "__main__":
    main()
