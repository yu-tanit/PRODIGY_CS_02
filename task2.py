from PIL import Image

def swap_pixels(img):
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (g, b, r)  # Swap red and green channels

def encrypt_image(image_path):
    img = Image.open(image_path)
    swap_pixels(img)
    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print("Image encrypted and saved as:", encrypted_path)

def decrypt_image(image_path):
    img = Image.open(image_path)
    swap_pixels(img)  # Swapping pixels again restores the original image
    decrypted_path = image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print("Image decrypted and saved as:", decrypted_path)

def main():
    image_path = input("Enter the path to the image file: ")
    action = input("Do you want to encrypt or decrypt the image? (encrypt/decrypt): ").lower()

    if action == 'encrypt':
        encrypt_image(image_path)
    elif action == 'decrypt':
        decrypt_image(image_path)
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
