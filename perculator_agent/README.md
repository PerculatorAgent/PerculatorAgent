# Percolator — Formally Verified Risk Engine for Perpetual DEXs

> Educational & research project. NOT production ready.

Percolator is a Rust-based risk and accounting engine for decentralized perpetual futures exchanges on Solana.
It focuses on correctness, formal verification, and crisis-safe accounting.

## Features

- Portfolio-based margining
- Crisis / bad-debt waterfall (insurance → warming PnL → equity haircut)
- AMM + orderbook compatible matching
- no_std friendly core
- Kani formal verification harnesses
- O(1) loss socialization

## Quick Start

### Prerequisites

- Rust (stable)
- Solana CLI
- Optional: kani-verifier

### Build

```bash
cargo build-sbf
cargo build --release --bin percolator
```

### Local Deploy

```bash
solana-test-validator &
percolator deploy --all
```

### Tests

```bash
cargo test --lib
cargo kani -p proofs-kani
```

## PerculatorAgent

PerculatorAgent is a lightweight documentation assistant that:

- Scans Rust files
- Extracts structs / enums / functions
- Uses an LLM to summarize them
- Produces auto-generated markdown docs

### Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key
python percolator_agent.py
```

Output is written to DOCS_AUTO.md.

## License

Apache 2.0
