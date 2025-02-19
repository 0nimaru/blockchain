import hashlib
import json
from time import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount
        }

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = self.format_timestamp(timestamp)
        self.transactions = [tx.to_dict() for tx in transactions]
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def format_timestamp(self, timestamp):
        return "{:.6f}".format(timestamp)

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, time(), [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            return False

        new_block = Block(len(self.chain), time(), self.pending_transactions, self.get_latest_block().hash)
        self.chain.append(new_block)
        self.pending_transactions = []
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Transactions: {block.transactions}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Hash: {block.hash}")
            print("]")

# Example usage
blockchain = Blockchain()

# Add some transactions
blockchain.add_transaction(Transaction("Alice", "Bob", 50))
blockchain.add_transaction(Transaction("Bob", "Charlie", 25))

# Mine a block
blockchain.mine_block()

# Display the blockchain
blockchain.display_chain()

# Check if the blockchain is valid
print("Is blockchain valid?", blockchain.is_chain_valid())
