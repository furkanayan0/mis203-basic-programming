import time
import random
import string
import sys

def simulate_decryption(length):
    # Characters to use for the animation and password
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Generate the actual target password behind the scenes
    target_password = "".join(random.choice(chars) for _ in range(length))
    
    print("\nINITIALIZING SECURE PROTOCOL...")
    time.sleep(1)
    print(f"TARGET LENGTH: {length} bytes")
    print("BYPASSING SECURITY MAINFRAME...\n")
    time.sleep(1.5)

    current_attempt = [""] * length
    
    # The animation loop
    for i in range(length):
        # Cycle through random characters to create a "cracking" visual effect
        for _ in range(15):
            random_char = random.choice(chars)
            random_tail = "".join(random.choice(chars) for _ in range(length - i - 1))
            
            # \r overwrites the current line in the terminal, creating the animation
            sys.stdout.write(f"\r[>] Cracking: {''.join(current_attempt[:i])}{random_char}{random_tail}")
            sys.stdout.flush()
            time.sleep(0.04)
            
        # Lock in the correct character for this position
        current_attempt[i] = target_password[i]

    # Final output display
    sys.stdout.write(f"\r[>] Cracking: {''.join(current_attempt)}\n")
    sys.stdout.flush()
    
    print("\n[+] ACCESS GRANTED. SECURE KEY GENERATED.")
    print(f"==>  {target_password}  <==\n")

if __name__ == "__main__":
    print("--- MIS-203 SECURE VAULT ---")
    
    # Input validation using a while loop and try-except
    while True:
        user_input = input("Enter desired security key length (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("System shutting down...")
            break
            
        try:
            # Type conversion
            key_length = int(user_input)
            
            # Conditional statements to validate logic
            if key_length < 4:
                print("Error: Key must be at least 4 characters for security reasons.")
            elif key_length > 50:
                print("Error: Maximum key length is 50 to prevent system overload.")
            else:
                simulate_decryption(key_length)
                break
                
        except ValueError:
            print("Access Denied: Invalid input type. Please enter a whole number.")
