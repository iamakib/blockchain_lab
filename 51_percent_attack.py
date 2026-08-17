import hashlib

# Creating a block
class Block:
    def __init__(self,data,previous_hash):
        self.data=data
        self.previous_hash=previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data=(
            str(self.data)+
            str(self.previous_hash)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()

# Creating Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [Block("Genesis Block","0"*64)]

    def add_block(self,data):
        self.chain.append(Block(data,self.chain[-1].hash))

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash for block",i)
                return False
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash for block",i)
                return False

            print("Blockchain is valid")

            return True

    def get_chain_length(self):
        return len(self.chain)

    def get_chain_hashrate(self):
        total_hashrate = 0
        for block in self.chain:
            total_hashrate += int(block.hash,16)

        return total_hashrate

    def check_for_51_percent_attack(self):
        total_hashrate = self.get_chain_hashrate()

        for i in range (self.get_chain_length()):
            block_hash = int(self.chain[i].hash,16)

            if block_hash/total_hashrate > 0.51:
                print("51 percent attack detected at block",i)
                return True
            
        print("No 51 percent attack detected")
        return False


blockchain = Blockchain()
blockchain.add_block(
    Block("Alice pays Bob 5 BTC", "")
)

blockchain.add_block(
    Block("Bob pays Charlie 3 BTC", "")
)

blockchain.add_block(
    Block("Charlie pays David 2 BTC", "")
)

print("Chain Length:",blockchain.get_chain_length()) 

print("\nChecking Blockchain:")
blockchain.validate_chain()   

print("\nChecking 51% Attack:")
bool = blockchain.check_for_51_percent_attack()