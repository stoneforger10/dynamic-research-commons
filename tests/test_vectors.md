# Test vectors

- Valid fetched sources and forward `depends-on` edges produce `COMPOSED` and increment sequence.
- Reversed dependency order produces `REJECTED` and leaves sequence unchanged.
- Hash mismatch, HTTP failure or ambiguous semantic output produces `INCONCLUSIVE`.
- Reusing a commit ID or stale parent sequence is rejected before nondeterministic execution.
