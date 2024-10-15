from PIL import Image
import random

def encrypt_image(image_path, key):
    """Encrypts the image by applying a basic mathematical operation to each pixel."""
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256
            pixels[i, j] = (r_encrypted, g_encrypted, b_encrypted)
    encrypted_image_path = "encrypted_image.png"
    image.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(image_path, key):
    """Decrypts the image by reversing the encryption formula."""
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256
            b_decrypted = (b - key) % 256

        
            pixels[i, j] = (r_decrypted, g_decrypted, b_decrypted)

    decrypted_image_path = "decrypted_image.png"
    image.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

def swap_pixels(image_path, seed):
    """Encrypts the image by swapping pixels based on a random seed."""

    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    pixel_indices = [(i, j) for i in range(width) for j in range(height)]

    random.seed(seed)
    random.shuffle(pixel_indices)

    shuffled_image = Image.new("RGB", (width, height))
    shuffled_pixels = shuffled_image.load()

    for (i, j), (x, y) in zip(pixel_indices, pixel_indices[::-1]):
        shuffled_pixels[i, j] = pixels[x, y]

    shuffled_image_path = "swapped_image.png"
    shuffled_image.save(shuffled_image_path)
    print(f"Image encrypted by pixel swapping and saved as {shuffled_image_path}")

def reverse_swap_pixels(image_path, seed):
    """Decrypts the image by reversing the pixel swap."""
    
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    pixel_indices = [(i, j) for i in range(width) for j in range(height)]

    random.seed(seed)
    random.shuffle(pixel_indices)

    reversed_image = Image.new("RGB", (width, height))
    reversed_pixels = reversed_image.load()

    for (i, j), (x, y) in zip(pixel_indices[::-1], pixel_indices):
        reversed_pixels[i, j] = pixels[x, y]

    reversed_image_path = "reversed_swapped_image.png"
    reversed_image.save(reversed_image_path)
    print(f"Image decrypted by reversing pixel swap and saved as {reversed_image_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt image (using math operations)")
    print("2. Decrypt image (using math operations)")
    print("3. Encrypt image (by swapping pixels)")
    print("4. Decrypt image (by reversing pixel swap)")

    choice = input("Enter your choice (1/2/3/4): ")
    image_path = input("Enter the image file path: ")

    if choice == '1':
        key = int(input("Enter the encryption key (numeric value): "))
        encrypt_image(image_path, key)
    elif choice == '2':
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(image_path, key)
    elif choice == '3':
        seed = int(input("Enter the swap seed (numeric value): "))
        swap_pixels(image_path, seed)
    elif choice == '4':
        seed = int(input("Enter the swap seed (same as encryption seed): "))
        reverse_swap_pixels(image_path, seed)
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
