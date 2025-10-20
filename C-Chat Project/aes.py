
import random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#     """
#     A simple AES ECB wrapper for encryption and decryption.
#     Padding is handled by adding null bytes to the end of the plaintext.
#     Trailing whitespace in messages is removed after decryption.
#     """

class AES:
    def __init__(self, key: bytes):
        self.key = key
        self.key_len = len(key) * 8

    def encrypt(self, plaintext: str) -> bytes:
        plaintext_bytes = plaintext.encode('ascii')
        block_size = 16  # AES block size is always 16 bytes
        # PKCS7-like padding
        pad_len = block_size - (len(plaintext_bytes) % block_size)
        plaintext_bytes += bytes([pad_len] * pad_len)

        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext_bytes) + encryptor.finalize()

    def decrypt(self, ciphertext: bytes) -> str:
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        decryptor = cipher.decryptor()
        decrypted_bytes = decryptor.update(ciphertext) + decryptor.finalize()
        # remove PKCS7-like padding
        pad_len = decrypted_bytes[-1]
        return decrypted_bytes[:-pad_len].decode('ascii')




if __name__ == '__main__':

    # use a random key
    key_len = 256
    key = bytes([random.randint(0, 255) for _ in range(key_len // 8)])
    
    # instantiate an AES cryptor
    # now you can encrypt and decrypt messages
    cryptor = AES(key)

    # your custom plaintext message
    plaintext = "Hello! I am Djibrile Ibrahima"
    # encrypt
    ciphertext = cryptor.encrypt(plaintext)
    # decrypt
    decrypted = cryptor.decrypt(ciphertext)

    # check if everything works
    print(f"plaintext: {plaintext}")
    # typically unreadable, but we can print it as hex
    print(f"ciphertext: {ciphertext.hex()}")
    # check decrypted message
    print(f"decrypted: {decrypted}")
    # report if there is something wrong
    assert plaintext == decrypted, "Incorrect decryption!"

    # check the SHA256 of the ciphertext
    digest = hashes.Hash(hashes.SHA256())
    digest.update(ciphertext) 
    hmac = digest.finalize()
    print(f"SHA256 of ciphertext: {hmac.hex()}")
    