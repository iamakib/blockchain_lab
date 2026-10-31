
import hashlib
import socket
import base58

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 5000))
server.listen(1)

print("Waiting for Bitcoin address...")

# Accept connection
conn, addr = server.accept()

# Receive address
address = conn.recv(1024).decode()

print("\nReceived Bitcoin Address:")
print(address)

# Step 1: Base58 decoding
decoded = base58.b58decode(address)

# Step 2: Separate payload and checksum
payload = decoded[:-4]
received_checksum = decoded[-4:]

# Step 3: Double SHA-256
hash1 = hashlib.sha256(payload).digest()
hash2 = hashlib.sha256(hash1).digest()

# Step 4: Calculate checksum
calculated_checksum = hash2[:4]

# Step 5: Verify address
if (len(decoded) == 25 and
    payload[0] == 0x00 and
    received_checksum == calculated_checksum):

    print("\nBitcoin Address is VALID!")

else:
    print("\nBitcoin Address is INVALID!")

conn.close()
server.close()
