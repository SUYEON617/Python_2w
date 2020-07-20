#! /usr/bin/env python

fruit='apple'
print(fruit.index('p'))
print(fruit.upper())
print('\t'.join(fruit))
print(fruit.split())

bio='   fastqc      d'
print(bio.lstrip())
print(bio.rstrip('d'))
print(bio.replace('fastq','fasta'))
