# Live readiness

- **Project:** Commerce Identity Fabric
- **Track:** Virtuals
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:22+00:00`

## Trust boundaries

- **Virtuals** — `rest_json` — Sync agent personas and commerce-facing identity metadata.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Slice** — `rest_json` — Drive checkout hooks and storefront policy changes.
- **SelfProtocol** — `rest_json` — Gate sensitive actions behind privacy-preserving proofs.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **SuperRare** — `rest_json` — Mint art-series media and auction metadata.

## Offline-ready partner paths

- **ENS** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call

## Live-only partner blockers

- **Virtuals**: VIRTUALS_API_URL — https://www.virtuals.io/
- **Slice**: SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/
- **SelfProtocol**: SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **SuperRare**: SUPERRARE_API_KEY, SUPERRARE_MINT_URL — https://superrare.com/

## Highest-sensitivity actions

- `selfprotocol_zk_verify` — SelfProtocol — Use SelfProtocol for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for CommerceIdentityRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for virtuals_fabric.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
