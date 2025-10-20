#!/usr/bin/env python3
#Oct 19, 2025 Vivian Li
import re
import sys
import subprocess
#problem 1 create function to format DNA
# def chop_dna (sequence, max_length):
#     sequence=sequence.rstrip()
#     for i in range(0,len(sequence),max_length):
#         print(i)
#         sequence=sequence[i:i+max_length]+'/n'
#     return sequence

# input = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT'''
# print(chop_dna(input, 80))

#problem4 modify the chop_dna script to take a fasta file and a max length
# def chop_dna (fasta_file, max_length):
#     fasta_list={}
#     sequence=''
#     for line in fasta_file:
#         found=re.search(r'(^>\S+)(.*)', line)
#         if found:
#             fasta_list[found.group(1), found.group(2)]=''
#         else:
#             for key in fasta_list.keys():
#                 fasta_list[key]+=line
#     for key in fasta_list:
#         new_sequence=''
#         for i in range(0,len(fasta_list[key]),max_length):
#             sequence=fasta_list[key]
#             sequence=sequence.rstrip()
#             new_sequence+=sequence[i:i+max_length]+'\n'
#             print(i)
#         fasta_list[key]=new_sequence
#     return fasta_list

# with open (sys.argv[1], 'r') as input:
#     max_length=int(sys.argv[2])

#     print(chop_dna(input, max_length))

#problem 5 create function that calculates the GC content

# def count_GC (sequence):
#     sequence=sequence.strip('')
#     nt_count={}
#     nt_count['A']= len(re.findall('A',sequence))
#     nt_count['T']= len(re.findall('T',sequence))
#     nt_count['G']= len(re.findall('G',sequence))
#     nt_count['C']= len(re.findall('C',sequence))
#     gc_content= (nt_count['G']+nt_count['C'])/(nt_count['G']+nt_count['C']+nt_count['A']+nt_count['T'])
#     return gc_content

# dna='''GG
# CC
# AA
# TT'''
# print(f'the GC content is {count_GC(dna):.2%}')

#problem6

    # def reverse_comp (sequence):
    # reverse_sequence= sequence[::-1]
    # sequence=reverse_sequence.translate(str.maketrans('ATCG', 'TAGC'))
    # return sequence

    # print(reverse_comp('ATGATGATG'))

#problem7 pipeline with subprocess.run (runs unix like code in python)
#subprocess.check_output is equivalent to subprocess.run()
#just make sure shell=True so you can write it as one string
find_problemsets=subprocess.check_output('ls -l | grep problemset', shell=True)
#decodes the byte code into a string for printing
find_problemsets=find_problemsets.decode('utf-8')
#check to make sure that the run was good/check exit status
oops=subprocess.check_call('ls -l', shell=True)
#do a second command
find_version= subprocess.check_output('python --version', shell=True)
oppsie=subprocess.check_call('python --version', shell=True)