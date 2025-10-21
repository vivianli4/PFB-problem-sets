#!/usr/bin/env python3
#Oct 17, 2025 Vivian Li 
import sys
import re

#file_name=sys.argv[1]
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

#second round, iterating through every nucleotide in each line isntead
#if it's not already a key, then create one FIRST
#then add 1 to it each other iteration of your for loop
# file_name='Python_08.fasta.txt'
# with open (file_name, 'r') as fasta:
#     fasta_dict={}
#     for line in fasta:
#         line=line.strip()
#         if line.startswith('>'):
#             gene_id=re.search(r'^>(\S+)', line).group(1)
#             fasta_dict[gene_id]={}
#         else:
#             for nt in line:
#                 if nt not in fasta_dict[gene_id]:
#                     print(f'{nt} not yet found in dict')
#                     fasta_dict[gene_id][nt]=1
#                 else:
#                     fasta_dict[gene_id][nt]+=1
                    
    #print(fasta_dict)               
#problem2 break every sequence into codons
# with open ('Python_08_test.fasta.txt', 'r') as fasta open ('Python_08.codons-frame01.nt', 'w') as output:
#     fasta_list={}
#     for line in fasta:
#         line=line.strip()
#         if line.startswith('>'):
#             gene_id=re.search(r'^>(\S+)', line).group(1)
#             fasta_list[gene_id]=[]
#         else:
#             fasta_list[gene_id]= [line[i:i+3] for i in range (0, len(line), 3)]
#             #if it's not a header, then i want to take the line and 
#             #break it into lists of 3
#     output=fasta_list

#problem3 produce  codons in the first 3 reading frames
with open ('Python_08_test.fasta.txt', 'r') as fasta, open ('Python_08.codons-6frames.nt', 'w') as output:
    fw_fasta_dict={}
    rev_fasta_dict={}
    reverseseq=''
    sequence=''
    for line in fasta:
        line=line.strip()
        if line.startswith('>'):
            gene_id=re.search(r'^>(\S+)', line).group(1)
            fw_fasta_dict[gene_id]=''
            rev_fasta_dict[gene_id]=''
        else:
            fw_fasta_dict[gene_id]+=line
            rev_fasta_dict[gene_id]=fw_fasta_dict[gene_id][::-1].translate(str.maketrans('ATCG', 'TAGC'))
            #fasta_dict[gene_id]= [line[i:i+3] for i in range (1, len(line), 3)]
    codons_dict={}
    for gene in fw_fasta_dict:
        curr=fw_fasta_dict[gene]
        for frame in range(0,3):
            f=str(frame)
            codons_dict[gene+'_frame'+f]=[]
            for nt in range (frame, len(curr), 3):
                codon=curr[nt:nt+3]
                if len(codon)==3:
                    codons_dict[gene+'_frame'+f].append(codon)
    for gene in rev_fasta_dict:
        curr=rev_fasta_dict[gene]
        for frame in range(3,6):
            f=str(frame)
            codons_dict[gene+'_frame'+f]=[]
            for nt in range (frame, len(curr), 3):
                codon=curr[nt:nt+3]
                if len(codon)==3:
                    codons_dict[gene+'_frame'+f].append(codon) 
        
    for key,value in codons_dict.items():
        string=f'{key}\n{value}\n'
        output.write(string)

#with open ('Python_08.codons-6frames.nt', 'r') as codontable, open ('Python_08.translated.aa', 'w') as proteintable

