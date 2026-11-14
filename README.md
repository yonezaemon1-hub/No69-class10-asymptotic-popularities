# Research No.69 - Class 10 asymptotic popularities

**Asymptotic Popularities in a Triple Consecutive-Pattern-Avoidance Class**

Ryutaro Yonezu, Independent Researcher. Preprint v1.0, 14 November 2026.

This is an unrefereed mathematical preprint. Human peer review has not taken place. Historical novelty remains **INCONCLUSIVE**; no claim of priority is made.

## Result and scope

For permutations avoiding the three **consecutive** patterns 123, 132, and 312, the manuscript proves the asymptotic popularities

| Remaining pattern | Asymptotic popularity |
| --- | --- |
| 213 | 1/2 |
| 231 | 1/2 |
| 321 | 0 |

It also proves `log(A_n)/(n log n) -> 1/2`, where `A_n` is the number of these avoiders. The enumeration itself is known from Kitaev (2003) and OEIS A079512 and is not claimed as new.

The proof uses a minimum-element decomposition, an injective block construction, and concentration of the number of ascents. Finite computations test instances; the infinite statements rest on the written proof.

## Files and reproduction

- `No69_v1.0_PREPRINT.pdf`: four-page manuscript.
- `No69_v1.0_SOURCE.tex`: frozen LaTeX source.
- `No69_v1.0_REPRODUCIBILITY.zip`: frozen Python/C++ reproduction kit and exact data.
- `SHA256SUMS.txt`: SHA-256 checksums of these three publication assets.
- The Python/C++ sources and `EXACT_TABLE.csv` are also exposed unchanged at the repository root for inspection.

Run with standard-library Python 3.10 or newer:

```sh
python -B -I verify_v02.py
python -B -I verify_class10.py
```

The first verifier checks exact pattern identities by exhaustive enumeration through n=9, computes ascents independently through n=1200, and checks finite instances of the block bound. The second checks endpoint-refined statistics, the known enumeration through n=100, and marked identities through n=1200. Neither finite verifier certifies an infinite theorem or historical novelty.

Independent AI proof reviews reported no material gap within their stated scope. Windows PowerShell 5.1 / Python 3.12 finite reproduction was reported as passing by the author. The Windows transcript has not been independently authenticated and is not distributed. No human or formal proof-assistant certification is claimed.

## Prior work check

Hassler and Kirgizov, *Emerging consecutive pattern avoidance*, DMTCS 28:1 (2026), DOI [10.46298/dmtcs.16861](https://doi.org/10.46298/dmtcs.16861), arXiv:2511.02442v3, lists Class 10 as open in Table 1. The DMTCS published PDF was checked during publication on 15 November 2026. This completes the particular final-table check described as pending in the frozen manuscript; it does not establish exhaustive historical novelty or exclude all general-theorem overlaps.

## Rights

Copyright (c) 2026 Ryutaro Yonezu. **All rights reserved.** No Creative Commons or open-source license is granted.

The GitHub release and archival record contain the same three frozen assets. Their URLs and DOI are added after publication has been verified.
