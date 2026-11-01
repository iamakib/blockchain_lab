import hashlib

#Function to calculate hash
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

#function to calculate and print merkle tree
def merkle_tree(transactions):
    hashes = []

    for transaction in transactions:
        hashes.append(sha256(transaction))

    levels = [hashes.copy()]

    while len(hashes)>1:
        new_hashes = []

        if len(hashes) %2 == 1:
            hashes.append(hashes[-1])

        for i in range(0,len(hashes),2):
            combined = hashes[i] + hashes[i+1]
            parent_hash = sha256(combined)
            new_hashes.append(parent_hash)

        levels.append(new_hashes.copy())

        hashes = new_hashes


    print("Printing merkle tree\n")
    for i,level in enumerate(reversed(levels)):
        print(f"\nLevel {i}:")

        for h in level:
            print(h)

    return hashes[0]

# Main code
transactions = [
    "Alice pays Bob 5 BTC",
    "Bob pays Charlie 2 BTC",
    "Charlie pays David 1 BTC",
    "David pays Eva 3 BTC"
]

root = merkle_tree(transactions)

print("\nMerkle Root:")
print(root)