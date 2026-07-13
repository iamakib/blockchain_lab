import hashlib

# Function to calculate hash
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

#Function to calculate merkel root
def merkle_root(transactions):
    hashes = []

    for transaction in transactions:
        hashes.append(sha256(transaction))
    
    print('Transaction hases')
    for h in hashes:
        print(h)
    
    while len(hashes) > 1:
        new_hashes = []

        if(len(hashes)%2!=0):
            hashes.append(hashes[-1])

        for  i in range(0,len(hashes),2):
            combined = hashes[i] + hashes[i+1]

            parent_hash = sha256(combined)

            new_hashes.append(parent_hash)
        
        hashes = new_hashes
    
    return hashes[0]

# main code
transactions = [
    "Alice pays Bob 10 BTC",
    "Bob pays Charlie 5 BTC",
    "Charlie pays David 2 BTCs",
    "David pays Eve 1 BTC"
]

root = merkle_root(transactions)


print("\nMerkle Root:")
print(root)