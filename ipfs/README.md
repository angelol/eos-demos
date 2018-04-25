# EOS IPFS Demo
The purpose of this demo is to show how you can store larger strings or bigger files in IPFS instead of the on-chain shared memory. Let's say you have a decentralized blogging platform and you want to store all the meta information on-chain, but the HTML of the blog post could get quite large, so you want to store it in IPFS. The smart contract will then only store the IPFS hash of the file.

This is a stop-gap measure because the integrated EOS-Storage won't be finished for the mainnet release in June 2018.

## Limitations
If you are using this, your local IPFS node will pin the file and serve it to other IPFS nodes, but if it goes offline, the data will be lost as well. You should run a proper IPFS node on a server and or ask people from your community to pin these files as well.
