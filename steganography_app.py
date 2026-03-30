import cv2

class SteganoApp:
    def __init__(self):
        print("--- Image Steganography App Initialized ---")

    def encode(self, cover_path, secret_path, output_path):
        cover = cv2.imread(cover_path)
        secret = cv2.imread(secret_path)
        
        # Resize secret to match cover
        secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))
        
        # Hide secret MSBs in cover LSBs
        stego_img = (cover & 0xF0) | (secret >> 4)
        cv2.imwrite(output_path, stego_img)
        print(f"Success! Encoded image saved as {output_path}")

    def decode(self, stego_path, output_path):
        stego_img = cv2.imread(stego_path)
        # Extract lower 4 bits and shift them back to MSB position
        extracted = (stego_img & 0x0F) << 4
        cv2.imwrite(output_path, extracted)
        print(f"Success! Extracted secret saved as {output_path}")

if __name__ == "__main__":
    app = SteganoApp()
    # Example usage for your assignment:
    app.encode('cover.jpg', 'secret.jpg', 'stego_result.png')
    app.decode('stego_result.png', 'decoded_secret.png')
