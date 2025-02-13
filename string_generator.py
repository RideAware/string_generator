import secrets
import string

def generate_random_subdomain(length=8):
    # Choose from alphanumeric characters
    alphabet = string.ascii_lowercase + string.digits
    # Generate a random subdomain using the chosen alphabet
    subdomain = ''.join(secrets.choice(alphabet) for _ in range(length))
    return f"psql-{subdomain}.rideaware.org"
    
# Example usage:
random_url = generate_random_subdomain()
print(random_url)  # e.g., "a1b2c3d4.rideaware.org"

