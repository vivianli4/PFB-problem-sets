#!/usr/bin/env python3
#Oct 17, 2025 Vivian Li 

import re

#question1 find every instance of the word Nobody and print the position
# with open ('Python_07_nobody.txt', 'r') as song, open('Delia.txt', 'w') as newSong:
#     for line in song:
#         for match in re.finditer(r"Nobody", line):
#             print(match.start())

#question2 replace every instance of the word Nobody with a new name and save it as a new text file
# with open ('Python_07_nobody.txt', 'r') as song, open('Delia.txt', 'w') as newSong:
#     for line in song:
#         newLine=re.sub(r'Nobody', r'Delia', line)
#         newSong.write(newLine)

#question3 
# with open('Python_07.fasta.txt', 'r') as fasta:
#     for line in fasta:
#          for found in re.finditer(r'(^>\S+)(.*)', line):
#             print(found.group(1), found.group(2))

#question4
# with open('Python_07.fasta.txt', 'r') as fasta:
#     for line in fasta:
#         for found in re.finditer(r'(^>\S+)(.*)', line):
#             print(f'id: {found.group(1)} desc: {found.group(2)}')

#question5 fasta parser 
fasta_list={}
with open('Python_07.fasta.txt', 'r') as fasta:
    for line in fasta:
        found=re.search(r'(^>\S+)(.*)', line)
        if found:
            fasta_list[found.group(1), found.group(2)]=''
        else:
            for key in fasta_list.keys():
                fasta_list[key]+=line
    print(fasta_list)