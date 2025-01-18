import time
import os
from web3 import Web3
from web3.exceptions import TransactionNotFound

# Replace with your own Ethereum node URL
ETH_NODE_URL = 'https://eth-mainnet.g.alchemy.com/v2/<your-api-key>'
web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

def is_contract(address):
    """Check if an address is a contract."""
    code = web3.eth.get_code(address)
    return len(code) > 2  # Check if the code length is greater than 0 (0x)

def load_existing_contracts(filename):
    """Load existing contracts from the file into a set."""
    seen_contracts = set()
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # Ensure the line is not empty
                    contract_info = line.split(' - ')
                    if len(contract_info) == 2:
                        seen_contracts.add(contract_info[0].strip())
    except FileNotFoundError:
        # If the file does not exist, return an empty set
        return seen_contracts
    return seen_contracts

def create_new_filename(base_name="generated", extension=".txt"):
    """Create a unique filename for the new contracts file."""
    i = 1
    while True:
        filename = f"{base_name}{i}{extension}"
        if not os.path.exists(filename):
            return filename
        i += 1

def main():
    seen_contracts = load_existing_contracts('../contracts/contracts.txt')  # Load existing contracts
    filename = create_new_filename()  # Create a new unique filename

    while True:
        try:
            # Get pending transactions
            pending_block = web3.eth.get_block('pending')
            pending_txs = pending_block['transactions']

            for tx_hash in pending_txs:
                try:
                    tx = web3.eth.get_transaction(tx_hash)

                    # Check if the transaction sends funds
                    if tx['value'] > 0 and tx['to'] is not None:
                        # Check if the recipient is a contract
                        if is_contract(tx['to']) and tx['to'] not in seen_contracts:
                            seen_contracts.add(tx['to'])
                            
                            # Get the contract's total balance
                            total_balance = web3.eth.get_balance(tx['to'])
                            total_balance_in_eth = web3.from_wei(total_balance, 'ether')
                            
                            # Append new contract details to the new file
                            with open(filename, 'a') as f:
                                f.write(f"{tx['to']} - {total_balance_in_eth} ETH\n")
                            print(f"New funded contract: {tx['to']} - {total_balance_in_eth} ETH")

                except TransactionNotFound:
                    # Continue with the next transaction if one is not found
                    continue

        except Exception as e:
            print(f"Error while fetching pending transactions: {e}")

        time.sleep(5)  # Sleep to avoid overwhelming the node

if __name__ == "__main__":
    main()
