#!/usr/bin/env python3
#Oct 15, 2025 Vivian Li 

import sys

#question 2 list manipulation
# taxa_string = 'sapiens : eruectus : neaderthalensis'
# #print(taxa_string)
# #split the string at the delimeter ":"
# taxa_list = taxa_string.split(":")
# #print(type(taxa_list))

# #print based on alphabetically sorted list
# #print(sorted(taxa_list, key=None, reverse=False))

# #print based on shortest to longest names in list
# taxa_list_iterator = iter(taxa_list)
# print(sorted(len(name) for name in taxa_list_iterator))

#question 4: write a while loop
# count =0
# sum=0
# while count <= 100 : 
#     print(count)
#     sum=sum+count
#     count+=1
# print(sum)

#question 5 find the product of 10!
# count=0
# product = 10
# while count <10:
#     product = product * (count+1)
#     count=count+1
# print(product)

# #question6 for loop through list
# even_total=0
# odd_total=0
# myList=[101,2,15,22,95,33,2,27,72,15,52]

# for num in myList: 
#     if num%2 ==0: 
#         even_total=even_total+num
#         print(num)
#     else:
#         print(num)
#         odd_total=odd_total+num
# print(f'Sum of even numbers: {even_total}\nSum of odd numbers: {odd_total}')

#question8 loops and ranges
# nums=range(1,101)
# for i in nums:
#     print(i)

#question 9 

# num_list= [range(100)]
# num_list2= [range(1, 101)]

# #print(num_list)
# print(num_list2)

# #question 10 user inputs
# min=int(sys.argv[1])
# max=int(sys.argv[2]) +1
# ranges=range(min,max)
# for i in ranges:
#     print(i)

# #question11 do the same as 10 but using line comprehesion
# min=int(sys.argv[1])
# max=int(sys.argv[2]) +1
# ranges=[i for i in range(min, max)]
# print(ranges)

#question 12 add a condition that only odd numbers are added to list
# min=int(sys.argv[1])
# max=int(sys.argv[2]) +1
# ranges=[i for i in range(min, max)]
# oddNumbers=[num for num in ranges if num%2==1]
# print(oddNumbers)

#question13
sequences= ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in sequences:
    print(f'{sequences.index(i)}\t{len(i)}\t{i} \n')


