'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

'''

def DNA_strand(dna):
    
    dont_rep = ''
    for i in dna:
        if i == 'A':
            dont_rep += 'T'
        if i == 'T':
            dont_rep += 'A'
        if i == 'G':
            dont_rep += 'C'
        if i == 'C':
            dont_rep += 'G'

    return dont_rep


def DNA_strand(dna):

    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))