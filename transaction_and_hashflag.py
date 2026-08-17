from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import Key

#create sender's private key
private_key = Key()

print("Private Key: ")
print(private_key.wif())

print("Bitcoin Address: ")
print(private_key.address())

#create a transaction
tx = Transaction(network='bitcoin')

tx.add_input(
    prev_txid='11111',
    output_n=0,
    value=1000000,
    address=private_key.address()
)

tx.add_output(
    value=900000,
    address='1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
)

signature_hash = tx.signature_hash(
    sign_id=0,
    hash_type=1,
    witness_type='legacy',
    as_hex=True
)


print("\nSignature Hash:")
print(signature_hash)

tx.sign(
    keys=private_key,
    index_n=0,
    hash_type=1,
)

print("\nDigital signature")
print(tx)

