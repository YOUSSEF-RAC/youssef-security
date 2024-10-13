from cryptography.fernet import Fernet

def encrypt_text(plain_text, cipher):
    encrypted_text = cipher.encrypt(plain_text.encode())
    print(f"Encrypted text: {encrypted_text}")
    return encrypted_text

def decrypt_text(encrypted_text, cipher):
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    print(f"Decrypted text: {decrypted_text}")
    return decrypted_text

if __name__ == "__main__":
    choice = input("Do you want to (1) Encrypt or (2) Decrypt? ")

    if choice == "1":
        key = Fernet.generate_key()  # Generate a  key
        cipher = Fernet(key)  
        text_to_encrypt = input("Enter the text you want to encrypt: ")
        encrypted = encrypt_text(text_to_encrypt, cipher)
        print(f"Key to decrypt: {key.decode()}")  # Display the key
    elif choice == "2":
        text_to_decrypt = input("Enter the encrypted text): ")
        
        try:
            encrypted_message = eval(text_to_decrypt)  
        except Exception as e:
            print("Error input. .")
            print(f"Exception: {e}")
            exit()

        key_for_decrypt = input("Enter the decryption key: ").encode()

        try:
            decrypt_cipher = Fernet(key_for_decrypt)  
            decrypted = decrypt_text(encrypted_message, decrypt_cipher)
        except ValueError:
            print("The key is not valid.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid choice.")
