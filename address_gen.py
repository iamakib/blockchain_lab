
import hashlib
import socket
import base58
from ecdsa import SigningKey, SECP256k1

# Step 1: Generate ECDSA private key
private_key = SigningKey.generate(curve=SECP256k1)

# Step 2: Generate public key
public_key = private_key.verifying_key

# Get compressed public key
public_bytes = public_key.to_string(encoding="compressed")

# Step 3: SHA-256
sha_hash = hashlib.sha256(public_bytes).digest()

# Step 4: RIPEMD-160
ripemd = hashlib.new('ripemd160')
ripemd.update(sha_hash)
public_hash = ripemd.digest()

# Step 5: Add version prefix 00
version = b'\x00'

# Step 6: Create payload
payload = version + public_hash

# Step 7: Double SHA-256
hash1 = hashlib.sha256(payload).digest()
hash2 = hashlib.sha256(hash1).digest()

# Step 8: Get first 4 bytes as checksum
checksum = hash2[:4]

# Step 9: Append checksum to payload
final_data = payload + checksum

# Step 10: Base58 encoding
address = base58.b58encode(final_data).decode()

print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_bytes.hex())
print("SHA-256:", sha_hash.hex())
print("RIPEMD-160:", public_hash.hex())
print("Payload:", payload.hex())
print("Checksum:", checksum.hex())

print("\nBitcoin Address:")
print(address)

# Step 11: Send address to another node
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 5000))

client.send(address.encode())

print("\nAddress sent successfully!")

client.close()
