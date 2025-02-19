# Blockchain for Charity and Donations

This is a simple blockchain implementation in Python to ensure transparency in the use of donated funds. The blockchain allows you to add transactions, mine new blocks, and verify the integrity of the blockchain.

## Prerequisites

- Python 3.x installed on your system

## Installation

1. Clone the repository or download the source code.
2. Navigate to the directory containing the `blockchain.py` file.

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `blockchain.py` file.
3. Run the following command to execute the script:

   ```sh
   python blockchain.py

## What to Expect
When you run the script, the following actions will be performed:

A new blockchain will be created with a genesis block.
Two transactions will be added to the list of pending transactions.
A new block will be mined, including the pending transactions.
The blockchain will be displayed, showing the details of each block.
The validity of the blockchain will be checked and displayed.
## Example Output

Block 0 [
  Timestamp: 1739968581.663293
  Transactions: []
  Previous Hash: 0
  Hash: 562cc1590256e074bde1df04e144e910ea41516048f8d5f4b37d9e2c26ba9b9d
]
Block 1 [
  Timestamp: 1739968581.663351
  Transactions: [{'sender': 'Alice', 'receiver': 'Bob', 'amount': 50}, {'sender': 'Bob', 'receiver': 'Charlie', 'amount': 25}]
  Previous Hash: 562cc1590256e074bde1df04e144e910ea41516048f8d5f4b37d9e2c26ba9b9d
  Hash: a1b97bf11f36bff692b867deafb0f20ed85e01653cc50ab1c6dec5c0284e7311
]
Is blockchain valid? True || False
