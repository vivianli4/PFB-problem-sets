#!/usr/bin/env python3
#Oct 15, 2025 Vivian Li 

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
count =0
sum=0
while count <= 100 : 
    print(count)
    sum=sum+count
    count+=1
print(sum)