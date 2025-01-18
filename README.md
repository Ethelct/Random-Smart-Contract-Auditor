# Mempool Contract Monitor

This project provides a tool to monitor the mempool for smart contract transactions. It captures transactions where the contract balance is greater than zero and saves the relevant data to a `contract.txt` file. This tool can be combined with Smart Contract auditors like Slither. After capturing the smart contract address, you can search for the relevant source code on Etherscan, or even decompile it.

Then using Slither you can check for vulnerabilities.

## Features

- Monitors the mempool for smart contract transactions.
- Filters transactions with balances greater than zero.
- Saves contract addresses and balances to a `contract.txt` file.
- Real-time monitoring for contract activity.
- Integrates with Slither for smart contract auditing.

## Prerequisites

- Python 3.8+
- Web3.py library (for Ethereum interaction)
- Access to an Ethereum node or a public API provider like Infura or Alchemy

## Usage

1. Run:
```sh 
python mempool_scan/scan.py
```

2. For the time smart contract addresses will be saved to contracts/contracts.txt with their balances.

### Example output
```sh
0x123abc... - 5 ETH
0x456def... - 3.2 ETH
...
```
3. Find the contract addresses on [Etherscan](https://etherscan.io/) and go to **Contract** tab.

4. Find the relevant source code or de-assemble the contract.

5. Install slither:

## Slither Installation

* Install **node.js**
* Install Slither:
```sh 
npm install -g slither-analyzer
```
* Install solc:
```sh
npm install -g solc
```
* Verify Slither installation:
```sh
slither --version
```

6. Make sure that the **Solc version** you are using matches that of the Solidity compiler. If not, run:

```sh
 solc-select install 0.x.x # Solidity compiler version
 solc-select use 0.x.x
 ```

 7. If you've got the source code, paste it on contracts/contracts in a new contract.sol file. I recommend you use names according to the number of the contract in the contracts.txt file, or its balance to memorize which contracts you audited.

 8. Run
```sh
slither <contract-file.sol>
```

## NOTE
**We do not recommend under any circumstances to use this tool for unethical purposes (frontrunning attacks, smart contract hacking exploitations etc).**
