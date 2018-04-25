# Watch an EOS Smart Contract and Pin Hashes to your IPFS node

This is proof-of-concept code to demonstrate how to watch an EOS smart contract that stores files in IPFS for new Hashes that need to be pinned and pin them on your IPFS node in regular intervals. This code could be run as a cronjob every minute.

## Limitations
This script imports all hashes every time it is run. This is very inefficient but necessary since old database entries might have their hashes changed.
