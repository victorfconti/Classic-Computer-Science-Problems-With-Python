class CompressedGene:
    
    def __init__(self, gene: str) -> None:
        self.__compress_gene(gene)
    

    def __compress_gene(self, gene: str)->None:
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError('Nucleotideo inválido {}'.format(nucleotide))
    
    def __gene_decompress(self):
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
        return gene[::-1]

    def __str__(self)-> str:
        return self.__gene_decompress()

compressed_gene: CompressedGene = CompressedGene("ACGT")
print(compressed_gene)