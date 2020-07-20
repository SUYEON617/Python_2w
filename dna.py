#! /usr/bin/env python

dna='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(dna)
print("A :", dna.count('A'))
print("T :", dna.count('T'))
print("C :", dna.count('C'))
print("G :", dna.count('G'))

toR='GATGGAACTTGACTACGTAAATT'
print(toR.replace('T','U'))

com='AAAACCCGGT'
s=com.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()

print(''.join(reversed(s)))

j={'A':'T','T':'A','C':'G','G':'C'}

a=list(com)
print(a)

li=[]
for x in a:
    r=j.get(x)
    li.append(r)
print(''.join(reversed(li)))

