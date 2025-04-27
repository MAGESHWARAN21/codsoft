import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters for better security.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def get_password_complexity():
    print("\nChoose password complexity:")
    print("1. Only Letters (a-z, A-Z)")
    print("2. Letters and Numbers (a-z, A-Z, 0-9)")
    print("3. Letters, Numbers, and Symbols (a-z, A-Z, 0-9, !@#$%^&* etc.)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password):
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved to 'saved_passwords.txt'.")

def main():
    print("=== Welcome to the Advanced Password Generator ===")
    
    while True:
        length = get_password_length()
        complexity = get_password_complexity()
        
        password = generate_password(length, complexity)
        print(f"\nGenerated Password: {password}")
        
        save_option = input("Do you want to save this password? (yes/no): ").lower()
        if save_option == 'yes':
            save_password_to_file(password)

        another = input("\nDo you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Password Generator!")
            break

if __name__ == "__main__":
    main()