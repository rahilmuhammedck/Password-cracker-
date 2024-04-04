import hashlib

def crack_md5_hash(hashed_password, password_list):
    for password in password_list:
        if hashlib.md5(password.encode()).hexdigest() == hashed_password:
            return password
    return None

def main():
    password_input = input("Enter the MD5 hashed password or plaintext password: ").strip()

    # Check if input is already hashed (32-character hexadecimal string)
    if len(password_input) == 32 and all(c in "0123456789abcdef" for c in password_input):
        # Input is already hashed, attempt to crack it directly
        hashed_password = password_input
        plaintext_password = crack_md5_hash(hashed_password, password_list)
        if plaintext_password:
            print(f"Plaintext password: {plaintext_password}, Hashed password: {hashed_password}")
        else:
            print("Password not found in the list.")
    else:
        # Input is plaintext, hash it and then attempt to crack
        plaintext_password = password_input
        hashed_password = hashlib.md5(plaintext_password.encode()).hexdigest()
        plaintext_password = crack_md5_hash(hashed_password, password_list)
        if plaintext_password:
            print(f"Plaintext password: {plaintext_password}, Hashed password: {hashed_password}")
        else:
            print("Password not found in the list.")

if __name__ == "__main__":
    # Load a list of common passwords from a file
    with open('common_passwords.txt', 'r') as file:
        password_list = [password.strip() for password in file.readlines()]

    main()
