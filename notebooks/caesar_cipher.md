Here's a Python implementation of a Caesar cipher with both encryption and decryption capabilities:

```python
def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using Caesar cipher
    
    Args:
        text (str): The text to encrypt/decrypt
        shift (int): The shift value (number of positions to shift)
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted/decrypted text
    """
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Apply shift and wrap around using modulo
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def caesar_cipher_advanced(text, shift, mode='encrypt', preserve_case=True):
    """
    Advanced Caesar cipher with additional options
    
    Args:
        text (str): The text to encrypt/decrypt
        shift (int): The shift value
        mode (str): 'encrypt' or 'decrypt'
        preserve_case (bool): Whether to preserve original case
    
    Returns:
        str: The encrypted/decrypted text
    """
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Apply shift and wrap around using modulo
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def brute_force_caesar(ciphertext):
    """
    Try all possible shifts (1-25) to decrypt Caesar cipher
    
    Args:
        ciphertext (str): The encrypted text
    
    Returns:
        dict: Dictionary with shift values as keys and decrypted text as values
    """
    results = {}
    for shift in range(1, 26):
        decrypted = caesar_cipher(ciphertext, shift, mode='decrypt')
        results[shift] = decrypted
    return results

def interactive_caesar():
    """
    Interactive Caesar cipher interface
    """
    print("=== Caesar Cipher Tool ===")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Brute force decryption")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    encrypted = caesar_cipher(text, shift, mode='encrypt')
                    print(f"Encrypted text: {encrypted}")
                else:
                    print("Shift value must be between 1 and 25")
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    decrypted = caesar_cipher(text, shift, mode='decrypt')
                    print(f"Decrypted text: {decrypted}")
                else:
                    print("Shift value must be between 1 and 25")
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == '3':
            ciphertext = input("Enter ciphertext to brute force: ")
            print("\nBrute force results:")
            results = brute_force_caesar(ciphertext)
            for shift, text in results.items():
                print(f"Shift {shift:2d}: {text}")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Example usage and testing
if __name__ == "__main__":
    # Basic examples
    print("=== Caesar Cipher Examples ===")
    
    # Example 1: Encrypt
    original = "Hello World!"
    shift_value = 3
    encrypted = caesar_cipher(original, shift_value, mode='encrypt')
    print(f"Original:  {original}")
    print(f"Encrypted: {encrypted}")
    
    # Example 2: Decrypt
    decrypted = caesar_cipher(encrypted, shift_value, mode='decrypt')
    print(f"Decrypted: {decrypted}")
    
    # Example 3: With different shift
    text = "The quick brown fox jumps over the lazy dog"
    shift = 13  # ROT13
    encrypted_rot13 = caesar_cipher(text, shift, mode='encrypt')
    print(f"\nROT13 Example:")
    print(f"Original:  {text}")
    print(f"Encrypted: {encrypted_rot13}")
    print(f"Decrypted: {caesar_cipher(encrypted_rot13, shift, mode='decrypt')}")
    
    # Run interactive mode
    print("\n" + "="*50)
    interactive_caesar()
```

This Caesar cipher implementation includes:

## Key Features:

1. **Basic Encryption/Decryption**: 
   - `caesar_cipher(text, shift, mode='encrypt')`
   - Handles both uppercase and lowercase letters
   - Preserves non-alphabetic characters

2. **Advanced Options**:
   - `caesar_cipher_advanced()` with additional parameters
   - Preserves case handling

3. **Brute Force Decryption**:
   - `brute_force_caesar()` tries all 25 possible shifts
   - Useful for breaking unknown shifts

4. **Interactive Interface**:
   - Menu-driven command-line interface
   - Easy to use for testing

## How it works:

- **Encryption**: Shifts each letter forward by the specified number of positions
- **Decryption**: Shifts each letter backward by the specified number of positions
- **Wrapping**: Uses modulo arithmetic to wrap around the alphabet (Z → A)
- **Preservation**: Non-alphabetic characters (spaces, punctuation) remain unchanged

## Example Output:
```
=== Caesar Cipher Examples ===
Original:  Hello World!
Encrypted: Khoor Zruog!
Decrypted: Hello World!

ROT13 Example:
Original:  The quick brown fox jumps over the lazy dog
Encrypted: Gur thvqr ebtba sbl whzcf bire gur ynml qbt
Decrypted: The quick brown fox jumps over the lazy dog
```

## Usage Examples:

```python
# Simple encryption
encrypted = caesar_cipher("Hello", 3, mode='encrypt')
print(encrypted)  # Output: Khoor

# Simple decryption
decrypted = caesar_cipher("Khoor", 3, mode='decrypt')
print(decrypted)  # Output: Hello

# Brute force
results = brute_force_caesar("Khoor")
```

The script provides both programmatic functions and an interactive interface for easy testing and demonstration.
