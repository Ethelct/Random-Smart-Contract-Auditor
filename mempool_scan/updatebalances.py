import os
from web3 import Web3

# Set up your Web3 provider
provider_url = "https://eth-mainnet.g.alchemy.com/v2/<your-api-key>"
w3 = Web3(Web3.HTTPProvider(provider_url))

# Check if connected to the Ethereum network
if not w3.is_connected():
    raise Exception("Could not connect to Ethereum network.")

# Function to get balance of an address in ETH
def get_balance(address):
    balance_wei = w3.eth.get_balance(address)
    return w3.from_wei(balance_wei, 'ether')

# Read addresses from contracts1.txt
with open('../contracts/contracts.txt', 'r') as file:
    addresses = [line.strip() for line in file.readlines()]

# Fetch balances and prepare data to write back to the file
balances = []
for address in addresses:
    balance = get_balance(address)
    balances.append(f"{address} - {balance} ETH")

# Overwrite contracts1.txt with addresses and their balances
with open('../contracts/contracts.txt', 'w') as file:
    file.write("\n".join(balances))

print("Balances updated successfully in contracts.txt.")
