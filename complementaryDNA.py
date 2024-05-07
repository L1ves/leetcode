def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[n] for n in dna)

def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))