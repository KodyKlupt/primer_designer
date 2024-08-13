import Bio
import Bio.Seq
from Bio.Seq import Seq
from Bio.Seq import MutableSeq
import pandas as pd
import numpy as np
import time
import os   
import primers

dna = input("Enter DNA sequence: ")
dna = dna.upper()

x= input("Enter start position: ")
x = int(x)
x = x-1

y = input("Enter end position: ")
y = int(y)

print(dna[x:y])

dna = MutableSeq(dna)
dna[x:y] = input("Enter mutation sequence: ")
dna = dna.upper()
print(dna)

dna = Seq(str(dna))
truncate_dna = dna[x-10:y+20]

print(truncate_dna)



