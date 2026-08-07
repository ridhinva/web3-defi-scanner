# Web3/DeFi Security Scanner

<p align="center">
  ![Stars](https://img.shields.io/github/stars/ridhinva/web3-defi-scanner?style=for-the-badge)
  ![Forks](https://img.shields.io/github/forks/ridhinva/web3-defi-scanner?style=for-the-badge)
  ![Issues](https://img.shields.io/github/issues/ridhinva/web3-defi-scanner?style=for-the-badge)
  ![License](https://img.shields.io/github/license/ridhinva/web3-defi-scanner?style=for-the-badge)
  ![Last Commit](https://img.shields.io/github/last-commit/ridhinva/web3-defi-scanner?style=for-the-badge)
  ![Build Status](https://img.shields.io/github/actions/workflow/status/ridhinva/web3-defi-scanner/ci.yml?style=for-the-badge)
  ![Web3](https://img.shields.io/badge/Web3%2FDeFi-Smart%20Contract%20Scanner-critical?style=for-the-badge)
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
</p>

---

## 🎯 Overview

**Web3/DeFi smart contract vulnerability scanner** for reentrancy, oracle manipulation, flash loans, governance attacks, and cross-chain bridge vulnerabilities.

| Check | Severity | Description |
|-------|----------|-------------|
| Reentrancy | 🔴 CRITICAL | Single/multi/cross-function reentrancy |
| Oracle Manipulation | 🔴 CRITICAL | Price feed manipulation, TWAP bypass |
| Flash Loan Attacks | 🔴 CRITICAL | Arbitrage, liquidation, governance |
| Access Control Missing | 🟠 HIGH | Owner-only, role-based gaps |
| Integer Overflow/Underflow | 🟠 HIGH | Solidity <0.8.0 |
| Unchecked External Calls | 🟠 HIGH | send/transfer vs call |
| Signature Replay | 🟡 MEDIUM | ECDSA malleability, EIP-1271 |
| Cross-Chain Bridge Vulns | 🔴 CRITICAL | Validator compromise, message replay |


---

## 🚀 Quick Start

```bash
git clone https://github.com/ridhinva/web3-defi-scanner.git
cd web3-defi-scanner
pip install requests web3
python3 web3_defi_scanner.py --target 0xContractAddress --rpc https://eth-mainnet.g.alchemy.com/v2/KEY
```

---

## ⚖️ Disclaimer

For authorized security testing only. Do not scan contracts without permission.
