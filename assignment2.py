#Given a list as a parameter,
# write a function that returns a list of numbers that are less than ten

#For example: Say your input parameter to the
#function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

l_1 = [1,11,14,5,8,9]
l_2 = []

for i in l_1:
    if i <= 9:
        l_2.append(i)
print(l_2)

#Write a function that takes in two lists 
#and returns the two lists merged together and sorted
#You can use the .sort method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_and_sort(l_1, l_2):
  merged_list = l_1 + l_2
  merged_list.sort()
  return merged_list

print(merge_and_sort(l_1, l_2))