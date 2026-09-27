# StudioNet live proofs

Network: GenLayer StudioNet (chain 61999)

Contract: `0x016221f3d9f4736e4561219C934d532c58A7D577`

Explorer: https://explorer-studio.genlayer.com/address/0x016221f3d9f4736e4561219C934d532c58A7D577

Deployed source matches `contracts/DynamicResearchCommons.py` byte-for-byte. SHA-256: `fdfb0ffde142ef29c8108483973b67e80812789d18d28fd66a2f057188891f87`.

## Finalized transactions

- Deployment: https://explorer-studio.genlayer.com/tx/0xfc0f22a71cfc88845d28de21b730fa105765d9c39698ea239fdc39b98e9c5099
- Space creation: https://explorer-studio.genlayer.com/tx/0x66de6c916ff2d97be2194f050be976e4c00b705a4a856dfc9f7ef1c57b31c6c8
- Idea source commitment: https://explorer-studio.genlayer.com/tx/0xb91877fdc12cbc78d97e831d76bf4771a8a9b8829ca73e7a5672c5118a048209
- Method source commitment: https://explorer-studio.genlayer.com/tx/0x4f5626c622ae39d69ec545f27edf89438e43f089cf74d990909b60d489240996
- Experiment source commitment: https://explorer-studio.genlayer.com/tx/0xbed9fa931514385d3ad874640595bc76a127c35d55e149c42ac146084f2ca522
- Method → experiment dependency: https://explorer-studio.genlayer.com/tx/0xfd86f04c5419ec4caf7ffe28cd68d22b2b39c02bb5916f177fcbb02030908b69
- Idea → method dependency: https://explorer-studio.genlayer.com/tx/0x2ec23f62ecebe661f8d98cc289268470ccb2a28871eb135ce70dddef0789b1e2
- Valid composition (`COMPOSED`, sequence 1): https://explorer-studio.genlayer.com/tx/0x965ada90be0b7de0733f370d2b1e74e8378ec3f460425d2ddeca9366aaacb910
- Reversed composition (`INCONCLUSIVE`, forward dependency check false; sequence unchanged): https://explorer-studio.genlayer.com/tx/0xf718bd26bdd47f087df9d6c81f2c699a4151d4e2795532540d1b9c524255061a

The valid report recorded HTTP 200, exact source hashes, semantic `USABLE`, and forward dependencies. The reversed report recorded `forward_dependencies: false` and did not change the workspace sequence.
