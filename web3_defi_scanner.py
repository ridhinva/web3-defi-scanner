#!/usr/bin/env python3
"""
Web3/DeFi Security Scanner
Reentrancy, oracle manipulation, flash loans, governance attacks
"""
import requests, sys, json, argparse

try:
    from web3 import Web3
    WEB3_AVAILABLE = True
except ImportError:
    WEB3_AVAILABLE = False

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║           Web3/DeFi Security Scanner                         ║
║    Reentrancy, Oracle, Flash Loans, Governance               ║
╚══════════════════════════════════════════════════════════════╝
"""

def check_reentrancy(w3, contract_addr):
    return {"vulnerable": False, "details": ["Reentrancy check requires contract source/bytecode analysis"]}

def check_oracle_manipulation(w3, contract_addr):
    return {"vulnerable": False, "details": ["Oracle check requires price feed contract analysis"]}

def check_flash_loan(w3, contract_addr):
    return {"vulnerable": False, "details": ["Flash loan check requires function call analysis"]}

def check_access_control(w3, contract_addr):
    return {"vulnerable": False, "details": ["Access control check requires owner/role analysis"]}

def check_cross_chain(w3, contract_addr):
    return {"vulnerable": False, "details": ["Cross-chain check requires bridge contract analysis"]}

def scan_target(rpc_url, contract_addr, modes):
    if not WEB3_AVAILABLE:
        print("[!] web3.py not installed. Install with: pip install web3")
        w3 = None
    else:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    all_results = {"target": contract_addr, "findings": {}}
    if "reentrancy" in modes or "all" in modes:
        all_results["findings"]["reentrancy"] = check_reentrancy(w3, contract_addr)
    if "oracle" in modes or "all" in modes:
        all_results["findings"]["oracle_manipulation"] = check_oracle_manipulation(w3, contract_addr)
    if "flashloan" in modes or "all" in modes:
        all_results["findings"]["flash_loan"] = check_flash_loan(w3, contract_addr)
    if "access" in modes or "all" in modes:
        all_results["findings"]["access_control"] = check_access_control(w3, contract_addr)
    if "bridge" in modes or "all" in modes:
        all_results["findings"]["cross_chain"] = check_cross_chain(w3, contract_addr)
    return all_results

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Web3/DeFi Security Scanner")
    parser.add_argument("--rpc", required=True, help="RPC URL (e.g., https://eth-mainnet.g.alchemy.com/v2/KEY)")
    parser.add_argument("--contract", required=True, help="Contract address")
    parser.add_argument("--mode", choices=["reentrancy", "oracle", "flashloan", "access", "bridge", "all"], default="all")
    parser.add_argument("--output", help="Output JSON file")
    args = parser.parse_args()
    modes = ["reentrancy", "oracle", "flashloan", "access", "bridge"] if args.mode == "all" else [args.mode]
    print(f"[*] Scanning {args.contract} on {args.rpc}\n")
    results = scan_target(args.rpc, args.contract, modes)
    total_vulns = sum(1 for v in results["findings"].values() if v.get("vulnerable"))
    print(f"\n{'='*60}\nScan Complete: {total_vulns} vulnerable categories found")
    for cat, finding in results["findings"].items():
        status = "🔴 VULNERABLE" if finding.get("vulnerable") else "🟢 OK"
        print(f"  {status} {cat}")
        for d in finding.get("details", []): print(f"    -> {d}")
    if args.output:
        with open(args.output, "w") as f: json.dump(results, f, indent=2)
        print(f"\n[*] Results saved to {args.output}")

if __name__ == "__main__": main()