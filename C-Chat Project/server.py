
import socket
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from aes import AES
from key import Key

class Server:
    def __init__(self, addr, port, buffer_size=1024):
        self.addr = addr
        self.port = port
        self.buffer_size = buffer_size

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.addr, self.port))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        print(f"Accepted connection from ({addr}, {port})")

    def accept(self):
        self.client, addr = self.s.accept()
        return addr

    def send(self, msg_bytes: bytes):
        self.conn.sendall(msg_bytes)

    def recv(self, buffer_size=None) -> bytes:
        if buffer_size is None:
            buffer_size = self.buffer_size
        msg_bytes = self.conn.recv(buffer_size)

        return msg_bytes

    def close(self):
        self.conn.close()

# this program waits for the client's encoded message then the server decode and read
# and then user can reply
# when the user enters exit the program stops

if __name__ == '__main__':
    server = Server('localhost', 35656)
    #server = Server('10.110.74.41', 12345)
    
    key = Key().read('key.bytes')
    cryptor = AES(key)
    
    while True:
         #TODO: your code here
        data = server.recv()   
        if data == b"exit":
            print("Client disconnected.")
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
        #print(f"\n[Server] Received ciphertext (hex): {ciphertext_received.hex()}")
        #print(f"[Server] Received SHA256 (hex): {hmac_received.hex()}")
        print(f"Client: {plaintext}")

        msg = input('Enter message to send: ')
        if msg.lower() == 'exit':
            server.send(b"exit")
            break
        else:         
            ciphertext = cryptor.encrypt(msg)
            digest = hashes.Hash(hashes.SHA256())
            digest.update(ciphertext) 
            hmac = digest.finalize()
            packet = hmac + ciphertext
            #print(f"\n[Server] Sending ciphertext (hex): {ciphertext.hex()}")
            #print(f"[Server] Sending SHA256 (hex): {hmac.hex()}")
            server.send(packet)

    server.close()