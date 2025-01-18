# Mempool Contract Monitor

This project provides a tool to monitor the mempool for smart contract transactions. It captures transactions where the contract balance is greater than zero and saves the relevant data to a `contract.txt` file. This tool can be used for various purposes, including detecting arbitrage opportunities, tracking token balances, or analyzing contract activity.

## Features

- Monitors the mempool for smart contract transactions.
- Filters transactions with balances greater than zero.
- Saves contract addresses and balances to a `contract.txt` file.
- Real-time monitoring for contract activity.

## Prerequisites

- Python 3.8+
- Web3.py library (for Ethereum interaction)
- Access to an Ethereum node or a public API provider like Infura or Alchemy
