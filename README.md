# 💻 Computer Organization Final Project 2025

> 📌 **Note:** The benchmarks involve working sets that may entirely fit within a large L3 cache. To better observe differences in associativity and replacement policies, experiments in **Q3** and **Q4** were conducted with both **1MB** and **256KB** L3 cache sizes.

---

## 📝 Project Tasks Overview

| Task | Description |
|------|-------------|
| **Q1** | GEM5 + NVMain integration and build (40%) |
| **Q2** | Enable and verify L3 cache functionality (15%)<br>✅ Check that L3 cache entries appear in the simulation logs |
| **Q3** | Configure L3 cache as 2-way and fully-associative, then compare performance (15%)<br>✅ Benchmark: `quicksort`<br>✅ Use miss rate to verify correctness |
| **Q4** | Implement and test a **Frequency-Based Replacement Policy** (FBRP) (15%)<br>✅ Compare with default LRU |
| **Q5** | Evaluate **Write-Back** vs **Write-Through** policies on a 4-way cache (15%)<br>✅ Benchmark: `multiply`<br>✅ Use write request count to verify write-through policy |

---

## 📁 Project Directory Structure

- `Commands/`: Command scripts and logs used during simulation

- `modified_code/`: Modified source code files
  - `Caches.py`: gem5/configs/common/Caches.py , Q2
  - `Options.py`: gem5/configs/common/Options.py`, Q2
  - `CPU.py`: gem5/src/cpu/Base/CPU.py, Q2
  - `XBar.py`: gem5/src/mem/XBar.py, Q2
  - `CacheConfig.py`: gem5/configs/common/CacheConfig.py, Q2
  - `fb_rp.cc`: gem5/src/mem/cache/replacement_policies/fb_rp.cc, Q4 added
  - `fb_rp.hh`: gem5/src/mem/cache/replacement_policies/fb_rp.hh, Q4 added
  - `ReplacementPolicies.py`: gem5/src/mem/cache/replacement_policies/ReplacementPolicies.py, Q4
  - `SConscript`: gem5/src/mem/cache/replacement_policies/SConscript, Q4
  - `Caches.py`: gem5/configs/common/Caches.py, Q4
  - `base.cc` :gem5/src/mem/cache/base.cc, Q5
  
- `Q2/`: Logs for Question 2 (L3 cache enabled)
  - `q2_stats.txt`: Output from gem5 `stats.txt`
  - `q2_nvmainoutput`: Terminal output from NVMain

- `Q3/`: Logs for Question 3 (2-way vs. full-way associativity test with quicksort)
  - `1MB/`
    - `2-way/`
      - `q3_1mb_2way_stats.txt`: gem5 stats for 2-way, 1MB L3 cache
      - `q3_1mb_2way_nvmainoutput`: Terminal output
    - `full-way/`
      - `q3_1mb_full_stats.txt`: gem5 stats for full-way, 1MB L3 cache
      - `q3_1mb_full_nvmainoutput`: Terminal output
  - `256KB/`
    - `2-way/`
      - `q3_256kb_2way_stats.txt`: gem5 stats for 2-way, 256KB L3 cache
      - `q3_256kb_2way_nvmainoutput`: Terminal output
    - `full-way/`
      - `q3_256kb_full_stats.txt`: gem5 stats for full-way, 256KB L3 cache
      - `q3_256kb_full_nvmainoutput`: Terminal output

- `Q4/`: Logs for Question 4 (Frequency-Based Replacement Policy vs. LRU)
  - `LRU/`
    - `1MB/`
      - `q4_1mb_lru_stats.txt`: LRU policy stats for 1MB
      - `q4_1mb_lru_nvmainoutput`: Terminal output
    - `256KB/`
      - `q4_256kb_lru_stats.txt`: LRU policy stats for 256KB
      - `q4_256kb_lru_nvmainoutput`: Terminal output
  - `FBRP/`
    - `1MB/`
      - `q4_1mb_fbrp_stats.txt`: FBRP policy stats for 1MB
      - `q4_1mb_fbrp_nvmainoutput`: Terminal output
    - `256KB/`
      - `q4_256kb_fbrp_stats.txt`: FBRP policy stats for 256KB
      - `q4_256kb_fbrp_nvmainoutput`: Terminal output

- `Q5/`: Logs for Question 5 (Write-Back vs. Write-Through with multiply benchmark)
  - `write back/`
    - `q5_wb_stats.txt`: gem5 stats for write-back policy
    - `q5_wb_nvmainoutput`: Terminal output
  - `writethrough/`
    - `q5_wt_stats.txt`: gem5 stats for write-through policy
    - `q5_wt_nvmainoutput`: Terminal output

```
.
├── Commands/                 # Terminal commands used
├── modified_code/           # Modified source files
├── Q2/
│   ├── q2_stats.txt         # gem5 stats output
│   └── q2_nvmainoutput      # Terminal output
├── Q3/
│   ├── 1MB/
│   │   ├── 2-way/
│   │   └── full-way/
│   └── 256KB/
│       ├── 2-way/
│       └── full-way/
├── Q4/
│   ├── LRU/
│   │   ├── 1MB/
│   │   └── 256KB/
│   └── FBRP/
│       ├── 1MB/
│       └── 256KB/
├── Q5/
│   ├── write back/
│   └── write through/
```

Each directory contains:
- `*_stats.txt`: Output from gem5's `stats.txt`
- `*_nvmainoutput`: Corresponding terminal output from NVMain

---
## 👩‍💻 Author
> Joanna