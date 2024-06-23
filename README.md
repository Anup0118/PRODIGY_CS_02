This repository contains a Python script for encrypting and decrypting images using a simple key-based method. The encryption process involves adding a specified key value to the pixel values of the image, while decryption involves subtracting the same key value to retrieve the original image.

How It Works:

1. Loading the Image: The image is loaded using the PIL library.
2. Encryption: Each pixel value is incremented by the key value, and the result is taken modulo 256 to ensure it remains within the valid range for image pixel values.
3. Decryption: Each pixel value in the encrypted image is decremented by the key value, and the result is taken modulo 256 to retrieve the original pixel value.

