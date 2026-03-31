### Desision Tree
| Problem Type                                   | Preferred Approach | WHY (Reason)                                                                                        |
| ---------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------- |
| Generate all subsequences                      | Either             | Both produce 2^n results; no constraints so either mental model works                               |
| Subsequence sum = K                            | Include/Skip       | Each element must be considered (take or not). Binary decision maps directly to recursion + pruning |
| Count subsequences                             | Include/Skip       | Counting naturally follows binary branching (include contributes + exclude contributes)             |
| Print one valid subsequence                    | Include/Skip       | Easy early stopping when a branch satisfies condition                                               |
| LIS (Longest Increasing Subsequence) recursion | Include/Skip       | State depends on “previous picked index”. That aligns with binary decisions and DP memoization      |
| DP conversion problems                         | Include/Skip       | Include/skip transitions map cleanly into DP states (index, state variables)                        |
| Unique subsets with duplicates                 | Loop               | Loop allows skipping duplicates at same recursion level using `i > start` rule                      |
| Combination Sum / k-combinations               | Loop               | You choose next candidate from a pool, not binary include/exclude of fixed index                    |
| Backtracking candidate selection               | Loop               | Problems where you iterate choices from remaining options naturally use loops                       |
| Increasing subsequences (print all)            | Loop               | Need flexibility to start from any future index satisfying condition                                |
| Permutations                                   | Loop + visited     | Order changes; must pick from remaining unused elements each step                                   |
| Problems needing pruning by range              | Loop               | Loop lets you stop early (e.g., sorted array and sum exceeds target)                                |
