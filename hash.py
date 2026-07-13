import hashlib

def sha_256(messgae):
    # Convert message to bytes
    messgae_bytes = messgae.encode()

    hash_value = hashlib.sha256(messgae_bytes)

    return hash_value.hexdigest()

message = input('Enter the plain message : ')
hash_result = sha_256(message)

print('\n Original message : ',message)
print('SHA-256 Hash :',hash_result)
print('Hash Length : ',len(hash_result))