# Phase 2 data provenance (NSFNET)

Retrieval date (sandbox clock, UTC): 2026-10-25T23:21Z. Phase 1 files were not touched.

## What is used
| item | value |
|---|---|
| Topology + capacities | `Network_nsfnetbw.ned` (5,271 bytes), SHA-256 `fe497b0bce187d1b7fe454e92c8778357dfa21ef2587878723d7d43d52824e7e` |
| Routing check file | `results_nsfnetbw_9_Routing_SP_k_1.tar.gz` (2,275,104 bytes), SHA-256 `4bfa5c42470bae5c0724c9ae4d995a5577c8672487f0af46abccf39224304217`; extracted `Routing.txt`, `params.ini`, `simulationResults.txt` (all hashes in `data/raw/SHA256SUMS.txt`) |
| Where it came from | GitHub repo `Data-Science-Projects/demo-routenet` (a THIRD-PARTY fork of RouteNet's demo), commit `5f5ebd706a3ac174d220b38743bbcd9479663015`, path `tests/unit-resources/nsfnetbw/` |
| Fork license | BSD-3-Clause text (copyright Rusek, Almasan, Sowatskey, Matute) covers that repository's code; copy saved as `LICENSE_fork_BSD3.txt` |

## Status of the claims (be strict)
* **Not obtained from an official BNN-UPC / KDN host.** `knowledgedefinednetworking.org` and `bnn.upc.edu` are unreachable from the sandbox. The official GitHub repos (`BNN-UPC/NetworkModelingDatasets` @ cfecb7a, `knowledgedefinednetworking/demo-routenet` @ 6fe5600, `BNN-UPC/datanetAPI`, `BNN-UPC/BNNetSimulator`, `BNN-UPC/GNNetworkingChallenge`) were cloned; none contains a `.ned`/`.gml`/NSFNET data file.
* **Not verified identical to the official `nsfnetbw` archive.** The fork file is the only copy available; no official checksum exists to compare against. Mailing-list text (kdn-users) suggests the NED was also shared on the project mailing list, but that was not downloaded or compared.
* **Dataset license NOT verified.** The BNN-UPC datasets repo has no LICENSE file; the fork's BSD-3 text is for its code. Redistribution of the data is therefore an open question; the raw files here must not be published until resolved.
* The topology is what the NED declares (14 nodes, 21 duplex links, 18x10 kbps + 3x40 kbps). Phase 2 validated it internally (`results/topology_validation.json`): connected, port counts match declared gates, and `Routing.txt` reconstructs a min-hop route for all 182 ordered pairs.
* The 500 shipped samples (lambda=9) are PACKET-LEVEL SIMULATION outputs, not measured traffic. They were used only to ground the *low* load level (`results/sample_load_summary.json`): max link utilization 0.54-0.69, 0 drops, median total offered rate 69.326 kbps.
* Units: the NED capacity unit "kbps" is treated as an abstract capacity unit (CU); OMNeT++ `simulationDuration` is in relative time units, so nothing here is a physical bit rate.

## Not used / not available in this sandbox
* Topology Zoo `Nsfnet.gml/.graphml` (13 nodes, 15 edges, no capacities per the project owner) and `external-gnn-research/datasets/README.md`, `data/nsfnet-v4.tar.gz` (zero bytes) exist only on the owner's machine. They were not inspected here and the zero-byte file was not touched. The Zoo NSFNET graph is a different graph from the 14-node simulation topology and is not substituted.
* GEANT2: no authentic file obtained (only the PNG in the BNN repo). GEANT2 validation is therefore BLOCKED, not faked.

## Synthetic parts (labelled as such)
Everything about traffic in Phase 2 is a seeded SYNTHETIC generator (`src/p2/sim.py::make_scenario`): 60 flows, uniformly random ordered node pairs, volume = load x 69.326 / 60 x U(0.2, 1.8). It is calibrated in total volume to the shipped lambda=9 samples at load=1, and scaled up for higher loads. It is not real-world or measured traffic.
