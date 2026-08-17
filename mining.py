import hashlib
import time

class Block:
    def __init__(self,data,previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""

    def calculate_hash(self):
        block_data= (
            str(self.data)+
            str(self.previous_hash)+
            str(self.nonce)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine(self,difficulty):
        target="0" * difficulty

        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(target):
                break
            self.nonce += 1

# Main program
data="Akib pays zaman 10 BTC"
previous_hash = "0"*64

block = Block(data,previous_hash)

difficulty = 4

start_time = time.time()
block.mine(difficulty)
end_time = time.time()

print("Mining Successful!")

print("\nBlock Data:")
print(block.data)

print("\nPrevious Hash:")
print(block.previous_hash)

print("\nNonce:")
print(block.nonce)

print("\nBlock Hash:")
print(block.hash)

print("\nDifficulty:")
print(difficulty)

print("\nMining Time:")
print(end_time - start_time, "seconds")
