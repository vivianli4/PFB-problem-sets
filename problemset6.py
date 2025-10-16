#!/usr/bin/env python3
#Oct 16, 2025 Vivian Li 

# #question1 and 2
# with open ("python_06.txt", 'r') as myPoem:
#     for line in myPoem:
#         line =line.upper()
#         print(line)

# #question3 reverse complementing a file
# seqList=[]
# with open ("python_06.seq.txt", 'r') as mySeq, open ("reversed_comp.txt", 'w') as reverseComp:
#     for line in mySeq:
#         seqList=line.split('\t')
#         seqList[1][::-1]
#         seqList[1]=seqList[1].translate(str.maketrans('ATCG', 'TAGC'))
#         reverseComp.write(f'{seqList[0]} \t {seqList[1]} \n')
        
#question4 opening a fastq file
with open ("python_06.fastq.txt", 'r') as fastq:
    numLines=0
    numSequenceID=0
    numChar=0
    numNuc=0
    averageLen=0
    averageLenSeq=0
    fasta_list=[]
    for line in fastq:
        fasta_list=line.split('\n')
        line=line.rstrip()
        numChar+=len(line)
        averageLen+=numChar
        if numLines%4==1:
            numSequenceID+=1
            numNuc+=len(line)
            averageLenSeq+=len(line)
        numLines+=1
    averageLen=averageLen/numLines
    averageLenSeq=averageLenSeq/numSequenceID
    print(f'(number of lines is {numLines} and number of characters is {numChar} . The number of Sequence IDs is {numSequenceID} and the number of nucleotides is {numNuc}. The average length of all the lines is {averageLen} while the average line length of lines that contain sequences is {averageLenSeq}')

#question5 generate gene lists
 