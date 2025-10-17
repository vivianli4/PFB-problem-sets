#!/usr/bin/env python3
#Oct 17, 2025 Vivian Li 
import sys
import re

file_name=sys.argv[1]
#problem1 first attempt at question with TA
# with open (file_name, 'r') as fasta:
#     fasta_list={}
#     for line in fasta:
#         line=line.rstrip()
#         found=re.search(r'(^>\S+)', line)
#         if found:
#             sequence=''
#             gene_id=found.group(1)
#             fasta_list[gene_id]={}
#         else:
#             sequence +=line
#             countA=sequence.count('A')
#             countG=sequence.count('G')
#             countT=sequence.count('T')
#             countC=sequence.count('C')
#             fasta_list[gene_id]['A']=countA
#             fasta_list[gene_id]['G']=countG
#             fasta_list[gene_id]['T']=countT
#             fasta_list[gene_id]['C']=countC
#seccond attempt at problem 1 
