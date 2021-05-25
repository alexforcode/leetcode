"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence,
return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.

Constraints:
    1 <= s.length <= 10**5
    s[i] is either 'A', 'C', 'G', or 'T'.
"""
from typing import List, Set


def find_repeated_dna_sequences(s: str) -> List[str]:
    sequences: Set[str] = set()
    repeated: Set[str] = set()
    target: int = 10

    for idx in range(len(s) - target + 1):
        sequence: str = s[idx:idx + target]

        if sequence in sequences:
            repeated.add(sequence)
        else:
            sequences.add(sequence)

    return list(repeated)


if __name__ == '__main__':
    assert find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') == ['AAAAACCCCC', 'CCCCCAAAAA']
    assert find_repeated_dna_sequences('AAAAAAAAAAAAA') == ['AAAAAAAAAA']
