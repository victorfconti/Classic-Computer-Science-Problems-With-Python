from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


gene_str: str = 'TGTTTAAAACGACTACCAAATCCGCATGTTAGGGGATTTCTTATTAATTCTTTTATCGTGAGGAACAGCGGATCTTAATGGATGGCCGCAGGTGGTATGGAAGCTAGCGCGGGTGAGAGGGTAATCAGCCGTGTTCACCTACACAACGCTAACGGGCGATTCTAGATTCCGCATTGCGTCTACTTAGATGTCTCAACGGTATCCGCAACTTGTGAAGTGCCTACTATCCTTAAACGCTCTCGCCCAGTAGCTTCCCATGTGAGCATCAATTGTTGTCCGGGCCGAGGTCATGTGCTCACGGAACTTACTGTATGAGTAGTGATTTGAAAGAGTTGTCAGTTTGCTGGTTCAGGTAAAGGTTCCTCACGCTACCTCAAAGTAAGAGAGCGGTCGTGACATTATCCGTGATTTTCTCACTACTATTAGTACTCACGACTCGATTCTGCCGCAGCCATGTTTCGCCAGAATGCCAGTCAGCATTAAGGAGAGCTCAGGGCAGGTCAACTCGCGTGAGGGTTACATGTTCGTTGGGCTCTTCCGACACGAACCTCAGTTAGCCTACATCCTACCAGAGGTCTGTGCCCCGGTGGTGAGAAGTGCGGATTTCGTATTTGCAGCTCGTCAGTACTTTCAGAATCATGGCCTGCACGGCAAAATGACGCTTATGGACTTCGACATGGCAACGCCTCGTTTCTACGTCAGGAGGAGAGTAACACTGCTGTCGGCAGAAGCGCCAAAGGAGTCTCTGAATTCTTATTCCCGAACATCCGTCTCCGTGCGGGAAAATCACCGACGGCGTTTTGAAGCCTAGGGGAACAGATTGGTCTAATTAGCTTAAGAGAGTAAATTCTGGGATCATTCAGTAGTAATCACAAATTTACGGTGGGGCTTTTTTGGCGGATCTTTACAGCTAACCAGGTGATTTCAACTAATTTAGTTGACGATTTAGGCGCGC'

def str_to_gene(s: str) -> Gene:
    gene: Gene = []
    
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)

    return gene


def linear_search(gene: Gene, key_codon: Codon) -> bool:
    
    for codon in gene:
        if codon == key_codon:
            return True
    
    return False

gene: Gene = str_to_gene(gene_str)

acg: Nucleotide = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Nucleotide = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
ata: Nucleotide = (Nucleotide.A, Nucleotide.T, Nucleotide.A)


def binary_search(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while low < high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True

    return False

print(linear_search(gene, acg))
print(linear_search(gene, gat))
print(linear_search(gene, ata))



my_sorted_gene: Gene = sorted(gene)

print(binary_search(my_sorted_gene, acg))
print(binary_search(my_sorted_gene, gat))
print(binary_search(my_sorted_gene, ata))
