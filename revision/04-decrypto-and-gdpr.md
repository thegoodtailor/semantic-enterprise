# Brief 04 — De-Crypto (whole book) + GDPR/Erasure Rebuild (Stage 1 + Stage 2)

Decision: scrub every crypto/employer-identifiable reference book-wide; recast in a **generic trading venue / capital-markets firm**. The seven domains survive unchanged (Pre-Trade, Trading, Custody, Post-Trade & Risk, Market Intelligence, Treasury, Finance) — they all exist at any exchange, broker-dealer, or market operator. "Crypto-shredding" the *cryptography term* stays; everything cryptocurrency goes.

## A. Replacement mapping (Stage 1, per-chapter agents)

| Current | Replace with | Sites (pre-split lines) |
|---|---|---|
| "crypto exchange" / "cryptocurrency exchange" / "mid-size crypto exchange" | "trading venue", "capital-markets firm", "the exchange" (generic securities exchange) | ~355, ~547, ~931, ~1520, ~1860, ~2236 |
| **"the Bullish acquisition integration"** | "the pending acquisition integration" | ~2224 — **highest priority; names the employer** |
| MiCA as regulatory inflection / "MiCA changed the Customer definition" | **MiFID II client recategorisation** — it is literally the retail→professional/eligible-counterparty reclassification the examples already describe | ~1082, ~1086, ~1453, ~1481, ~1485, ~2224 |
| MiCA as ontology-change-over-time example (2024 vs 2026 Customer) | **the IBOR/LIBOR→risk-free-rate transition** — the canonical "the meaning of a core term changed under regulation" event (what "the reference rate" *is* was redefined; contracts re-papered; both definitions live in history) | bitemporal-ontology passages ~1082–1086, ~1481–1489 |
| "BTC position" / "what is our BTC position?" | "our largest single-name position" / "our EUR rates position" | ~539 |
| "Trading volume for BTC/USD in Q1 was 142,000 BTC" | an equity or FX pair, e.g. "EUR/USD Q1 volume" with consistent units | ~1890 |
| "wallet balance" / "custody wallets" / "assets must move from one wallet to another, with cryptographic proof" | "custody account balance" / "depot positions" / "assets move between custody accounts, with an unbroken settlement record (CSD confirmation)" | ~547, ~931, ~1860 area |
| "333 GL accounts at a crypto exchange" | "at a brokerage" / "at a trading firm" (the example is venue-agnostic) | ~355 |
| "finance redefined the treatment of staking rewards" | "finance redefined the treatment of securities-lending revenue" | ~2302 |
| "crypto-asset service providers", "every crypto exchange", "MiCA-adjacent privacy law" | drop / generalize per part B | ~1453+ |
| "market-making" examples, "maker rebates", "tri-party repo", "rehypothecated collateral" | already venue-generic — **keep** | — |

After Stage 1, continuity agent re-greps: `crypto|BTC|wallet|MiCA|Bullish|staking|on-chain|coin|token(?!s? of)` — the last carefully: "token" in the LLM sense stays everywhere.

**Tone note for the rewrite agents:** the seven-domains, four-registers, KYC-reclassification, and custody examples lose nothing in translation — securities exchanges have sharper, older versions of every one of these problems (settlement discipline since the 1970s paper crisis; client-categorisation law since MiFID 2007). If anything the recast *raises* the book's authority: the claims now bind on every regulated market, not one asset class.

## B. The erasure section, rebuilt (Stage 2 — replaces "The Right to Be Forgotten" ~1451–1469)

The current section's legal case is wrong twice (it assumes the erasure right binds where it is in fact disapplied, and it frames crypto-shredding as settled law) and crypto-framed throughout. Rebuild on the *real* — and more interesting — legal structure, set at any EU consumer-facing financial institution (retail brokerage / wealth platform):

1. **The collision is real but it is two clocks, not one right.** GDPR Art. 17 grants erasure; **Art. 17(3)(b) disapplies it where retention is a legal obligation** — and AML law (AMLD4 Art. 40; from July 2027, AMLR Art. 77) *requires* keeping CDD/KYC and transaction records 5 years after the relationship ends (member states may extend; AMLR adds **mandatory deletion at expiry**). So the substrate faces two legally mandated clocks: **keep-for-exactly-N-years** and **delete-on-request** (which applies to data *outside* the legal-hold categories — marketing, behavioral, analytics-only personal data).
2. **The architecture is retention-clock-driven crypto-shredding.** Split identifying data from the factual skeleton; encrypt PII per subject; destroy keys **when the retention clock expires** (serving AMLR's mandatory deletion on an immutable substrate) and **on request** for non-held categories. The bitemporal history, aggregates, and published Gold versions survive as a de-identified skeleton. Same machinery, two triggers.
3. **State crypto-shredding's status honestly: converging, not concluded.** No EDPB guideline blesses it; WP29 05/2014 and EDPB 01/2025 treat keyed encryption as pseudonymisation; the strongest support is CJEU *EDPS v SRB* (Sept 2025): a relative "means reasonably likely" re-identification test — after key destruction, none remain. Caveats that must appear: all key copies/escrows/backups destroyed; cipher strength against future attack; per-subject key granularity is real infrastructure. (Engineering canon: Verraes' event-sourcing crypto-shredding pattern; NIST SP 800-88 cryptographic erase.)
4. **Pattern update:** retitle to *Crypto-Shredding on Two Clocks*; Context/Problem now framed as the two-clock conflict at a regulated financial institution; Example: a former client's KYC file shredded **5 years and one day after relationship end** by scheduled key destruction, while their marketing-consent data was shredded on request years earlier; the trades and quarter-end reports still reconstruct, the client is an opaque token.

Sources for the rewrite agent: AMLD4 Art. 40 (eur-lex 32015L0849); AMLR Art. 77 (eur-lex 2024/1624, applies 2027-07-10); anti-money-laundering.eu/new-record-retention-periods-under-art-77-amlr; Clifford Chance on *SRB* (cliffordchance.com/.../pseudonymized-data-after-srb); verraes.net/2019/05/eventsourcing-patterns-throw-away-the-key.

**Bonus alignment:** the MiFID II recategorisation substitution (part A) means the Time chapter's running example (retail→institutional reclassification, backdated) becomes *the same regulatory universe* as the erasure section — one coherent regulated-firm storyline instead of a crypto patchwork.
