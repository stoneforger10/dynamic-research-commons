# DynamicResearchCommons

> Historical graph-composition experiment; **not a separate Builder resubmission**. Steward feedback found material architectural overlap with DynamicLearningPath. The single replacement mechanism is [CompetencyEvidenceRouter](https://github.com/stoneforger10/competency-evidence-router), which routes learner state from independently fetched and semantically assessed rubric/work evidence rather than owner-controlled graph transitions. The Explorer links below prove only this historical contract.

DynamicResearchCommons is a GenLayer Intelligent Contract primitive for composing collaborative research structures. It stores research objects and typed relations, then resolves an immutable composition commit from independently fetched object documents.

The contract is not a publication oracle and does not certify scientific truth. Its consensus boundary is structural: validators refetch every registered source, recompute full-response SHA-256 hashes, check dependency ordering, and semantically decide whether the fetched documents explicitly support the proposed composition. Leader and validators must return the exact same report. `COMPOSED` advances the workspace sequence; `REJECTED` and `INCONCLUSIVE` are append-only and do not advance it.

Workflow: `create_space → register_object → connect_objects → resolve_composition`.

Security properties include HTTPS-only sources, exact hash commitments, owner-bound writes, immutable commit keys, parent-sequence binding, bounded deadlines, duplicate-edge rejection and fail-closed unavailable or contradictory evidence. No caller-supplied summary, score or confidence controls the result.

Run the GenVM linter and direct tests before deployment. See `LIVE_PROOFS.md` for finalized StudioNet evidence.

The `examples/research/` fixtures are public, content-addressed demo documents used by the live lifecycle.
