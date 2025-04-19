import secrets
import string

def generate_random_string(prefix, length=8):
    """Generates a random string with a given prefix."""
    alphabet = string.ascii_lowercase + string.digits
    random_string = ''.join(secrets.choice(alphabet) for _ in range(length))
    return f"{prefix}-{random_string}.rideaware.org"

def main():
    """Prompts the user to select a server type and generates a random URL."""
    while True:
        print("Select a server type:")
        print("1. PostgreSQL (psql)")
        print("2. Redis (redis)")
        print("3. RabbitMQ (rabbitmq)")
        print("4. Sandbox Web Server (sandbox)")
        print("5. Staging Web Server (staging)")

        choice = input("Enter a number (1-5) to select a server type, or 'q' to quit: ")

        if choice == '1':
            prefix = "psql"
        elif choice == '2':
            prefix = "redis"
        elif choice == '3':
            prefix = "rabbitmq"
        elif choice == '4':
            prefix = "sandbox"
        elif choice == '5':
            prefix = "staging"
        elif choice == 'q':
            break
        else:
            print("Invalid choice.  Please enter a number between 1 and 5.")
            continue

        random_url = generate_random_string(prefix)
        print(f"Generated URL: {random_url}")
        
        another = input("Generate do you need another URL? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
