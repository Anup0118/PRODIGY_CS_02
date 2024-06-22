from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image, key):
    img_array = np.array(image, dtype=np.uint8)

    # Cast to a larger type to prevent overflow
    encrypted_array = (img_array.astype(np.int32) + key) % 256

    # Cast back to uint8
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    return encrypted_image

def decrypt_image(image, key):
    img_array = np.array(image, dtype=np.uint8)

    # Cast to a larger type to prevent overflow
    decrypted_array = (img_array.astype(np.int32) - key) % 256

    # Cast back to uint8
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    return decrypted_image

def main():
    image_path = r'C:\Users\LENOVO\Pictures\Saved Pictures\Image.jpg'
    original_image = load_image(image_path)
    
    key = 50

    encrypted_image = encrypt_image(original_image, key)
    save_image(encrypted_image, 'encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")

    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, 'decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")

if __name__ == "__main__":
    main()
