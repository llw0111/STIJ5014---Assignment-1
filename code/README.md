# Cross-Chain Bridge Project (Ethereum ↔ Polkadot)

This project provides a cross-chain bridge solution between **Ethereum** and **Polkadot**, enabling seamless token transfers using the **ChainBridge** protocol. The repository includes smart contracts, a Substrate pallet, relayer configurations, and scripts to facilitate the interaction between the two blockchains.

---

## 📁 Project Structure

```
cross-chain-bridge-project/
│-- contracts/
│   └── CrossChainTokenBridge.sol  # Ethereum smart contract
│-- pallets/
│   └── token_bridge.rs            # Substrate pallet for Polkadot
│-- config/
│   └── config.json                 # Relayer configuration file
│-- scripts/
│   └── start_relayer.sh             # Script to start the relayer
│-- README.md                         # Documentation
│-- .gitignore
```

---

## ⚙️ Prerequisites

Ensure you have the following tools installed:

| Tool            | Purpose                                        | Installation Command / Link                        |
|-----------------|------------------------------------------------|---------------------------------------------------|
| Node.js & NPM   | Required for running ChainBridge relayer        | `sudo apt install nodejs npm`                     |
| Solidity        | Ethereum smart contract development             | Use Remix IDE or `npm install -g solc`            |
| Rust & Substrate| Required for compiling Polkadot pallets         | [Install Substrate](https://substrate.dev/)       |
| Metamask        | Ethereum wallet for testing interactions        | [Download Metamask](https://metamask.io/)          |
| Polkadot.js     | Polkadot wallet and UI for managing assets       | [Polkadot.js Extension](https://polkadot.js.org/) |

---

## 🚀 Deployment Guide

### Step 1: Deploy Ethereum Smart Contract

1. Open [Remix IDE](https://remix.ethereum.org).
2. Create a new file under `contracts/` and name it `CrossChainTokenBridge.sol`.
3. Copy and paste the contract code.
4. Compile and deploy the contract on Ethereum testnet (e.g., **Goerli** or **Sepolia**).
5. Copy the deployed contract address for later use.

---

### Step 2: Deploy Substrate Pallet on Polkadot

1. Clone the Substrate node template:

```bash
git clone https://github.com/substrate-developer-hub/substrate-node-template
cd substrate-node-template
```

2. Create a new pallet and add the required Rust code.
3. Build and run the Substrate node:

```bash
cargo build --release
./target/release/node-template --dev --tmp
```

---

### Step 3: Set Up ChainBridge Relayer

1. Clone ChainBridge:

```bash
git clone https://github.com/ChainSafe/chainbridge
cd chainbridge
npm install
```

2. Edit the `config.json` file under `config/` with appropriate values.
3. Start the relayer:

```bash
./scripts/start_relayer.sh
```

---

## 🧪 Example Usage

### 1. Lock Tokens on Ethereum

**Input:**
- Function: `lockTokens(uint256 amount, string targetChain)`
- Example Call: 

```solidity
lockTokens(1000000000000000000, "Polkadot")
```

**Expected Output:**
- Event `TokensLocked` emitted, containing:
  - `user`: The sender's Ethereum address.
  - `amount`: 1 ETH (1000000000000000000 wei).
  - `targetChain`: "Polkadot".
- The relayer detects the event and forwards it to the Polkadot chain.

---

### 2. Unlock Tokens on Polkadot

**Input:**
- Function: `unlock_tokens(account_id, amount)`
- Example Call (via Polkadot.js):

```rust
unlock_tokens(5G9uBv...user_address..., 1000000000000000000)
```

**Expected Output:**
- Event `TokensUnlocked` emitted, containing:
  - `user`: The recipient's Polkadot address.
  - `amount`: 1 ETH equivalent in Polkadot.
- The corresponding amount is credited to the recipient's balance.

---

## 🛠️ Troubleshooting

| Issue                      | Possible Cause                      | Solution                                  |
|---------------------------|-------------------------------------|-------------------------------------------|
| Relayer not detecting events | Incorrect start block or RPC issues | Verify `start_block` and check RPC status |
| Ethereum gas fees too high  | Network congestion                  | Adjust gas price or try during off-peak   |
| Substrate transaction fails| Incorrect input or insufficient funds | Check balance and input values            |

