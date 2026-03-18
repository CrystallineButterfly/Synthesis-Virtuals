"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Commerce Identity Fabric",
  "track": "Virtuals",
  "pitch": "An identity fabric that maps agent personas, permissions, and payment surfaces into one reusable commerce and delegation layer.",
  "overlap_targets": [
    "ENS",
    "Slice",
    "SelfProtocol",
    "ERC-8004 Receipts",
    "PayWithLocus",
    "SuperRare"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
