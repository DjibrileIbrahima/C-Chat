
import socket
from cryptography.hazmat.primitives import hashes
from aes import AES
from key import Key


class Client:
    def __init__(self, addr, port, buffer_size=1024):
        self.addr = addr
        self.port = port
        self.buffer_size = buffer_size

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.addr, self.port))
        print(f"Connected to server at {addr}: {port}")

    def send(self, msg_bytes: bytes):
        self.s.sendall(msg_bytes)

    def recv(self, buffer_size=None) -> bytes:
        if buffer_size is None:
            buffer_size = self.buffer_size
        msg_bytes = self.s.recv(self.buffer_size)

        return msg_bytes

    def close(self):
        self.s.close()

# this program prompts the client for a message that will be sent encoded to the server
# when the client enters exit the program stops

if __name__ == '__main__':
    client = Client('localhost', 35656)
    key = Key().read('key.bytes')
    cryptor = AES(key)

    while True:
        msg = input('Enter message to send: ')
        if msg.lower() == 'exit':
            client.send(b"exit")
            break
        else:
            ciphertext = cryptor.encrypt(msg)
            digest = hashes.Hash(hashes.SHA256())
            digest.update(ciphertext) 
            hmac = digest.finalize()
            packet = hmac + ciphertext
            #print(f"\n[Client] Sending ciphertext (hex): {ciphertext.hex()}")
            #print(f"[Client] Sending SHA256 (hex): {hmac.hex()}")
            client.send(packet)

            data = client.recv()
            if data == b"exit":
                print("Server disconnected.")
                break
            hmac_received = data[:32]       # SHA-256 digest = 32 bytes
            ciphertext_received = data[32:] # Ciphertext = 32 bytes
            
            # Verify HMAC
            digest = hashes.Hash(hashes.SHA256())
            digest.update(ciphertext_received)
            hmac_computed = digest.finalize()

            if hmac_received != hmac_computed:
                print(f"HMAC RECEIVED: {hmac_received.hex()}\n")
                print(f"HMAC COMPUTED: {hmac_computed.hex()}\n")
                print(f"HMAC verification failed! Message may have been tampered with.")
                break
            
            #Verification successful
            plaintext = cryptor.decrypt(ciphertext_received)
            #print(f"\n[Client] Received ciphertext (hex): {ciphertext_received.hex()}")
            #print(f"[Client] Received SHA256 (hex): {hmac_received.hex()}")
            print(f"Server: {plaintext}")
            
    client.close()