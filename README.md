# Percolator + PerculatorAgent

Formally verified perpetual DEX risk engine for Solana — with an AI documentation & Q&A assistant.

> ⚠️ **Educational / Research Project**
>
> This repository is NOT production ready and has NOT been audited.  
> Do not use with real funds.

---

# 🧠 Percolator

Percolator is a Rust-based accounting and risk engine for decentralized perpetual futures exchanges on Solana.

Its core goal is **correctness under extreme conditions**: liquidations, insolvency, and systemic loss events are explicitly modeled and formally verified.

Rather than focusing on UI or trading UX, Percolator focuses on:

- Balance-sheet safety
- Crisis resolution
- Loss socialization
- Margin accounting
- Mathematical invariants

It is designed as a **protocol core**, not a full exchange.

---

## ✨ Core Properties

### 📊 Risk & Accounting

- Cross-margin portfolios
- Position tracking
- Collateral management
- Liquidation logic
- Crisis resolution

### 🔥 Bad Debt Waterfall

Losses are resolved in strict order:

1. Insurance fund
2. Warm / vesting PnL
3. Equity haircut (socialized)

This guarantees bounded losses and prevents catastrophic underflow.

### ⚖️ Formal Verification

Large parts of the system are verified using **Kani**:

- AMM invariants
- Crisis bounds
- Vesting conservation
- Liquidation correctness
- Haircut limits

The intent is to mathematically prove:

> Users can never withdraw more value than exists on the exchange balance sheet.

### 🚀 Performance-Oriented Design

- `no_std` compatible core
- Zero allocations in hot paths
- O(1) crisis resolution
- Modular matching engines (AMM / orderbook / RFQ)

---

# 🤖 PerculatorAgent

PerculatorAgent is an AI-powered assistant layered on top of the Percolator codebase.

It provides:

- Semantic code search
- Natural language Q&A
- Auto documentation
- Web UI

Think of it as **ChatGPT trained specifically on your repo**.

---

## What PerculatorAgent Does

### ✅ Code Embeddings

- Scans all `.rs` files
- Chunks source code
- Builds vector embeddings using `sentence-transformers`
- Stores them in FAISS

This enables semantic retrieval of relevant code.

---

### ✅ Retrieval-Augmented Generation (RAG)

When you ask a question:

1. Your question is embedded
2. FAISS finds the most relevant Rust code
3. Those snippets are injected into the LLM prompt
4. OpenAI generates an answer grounded in your actual code

This prevents hallucination and keeps answers repo-specific.

---

### ✅ Web Interface

A lightweight FastAPI + HTML frontend provides:

- One-click indexing
- Text box for questions
- Live answers

No frontend framework required.

---

# 🌐 Web UI

After starting the server: https://x.com/i/communities/2020190633978122458/
