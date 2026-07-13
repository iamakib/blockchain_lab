from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048
)
public_key = private_key.public_key()

# Orginal msg to byte
message = input('Enter a message to verify : ')
message = message.encode()

#Generate digital signature using private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print('Orginal Message')
print(message.decode())

print('\n Digital Signature')
print(signature.hex())

# changing the message
# message = message.decode()
# message = 'any'

#verify signature using public key

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print('Signature verification Success')

except:
    print('Signature Verification Failed')