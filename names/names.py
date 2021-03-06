from bst import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# create a binary search tree using the first value in the names_1 list
bst = BSTNode(names_1[0])

# iterate through the names_1 list and add each name into the tree
for name in names_1:
    bst.insert(name)
# iterate through the names_2 list, checking if any names are already included in the tree
for name in names_2:
    # if any name is already in the tree, add the name to the duplicates list created above
    if bst.contains(name):
            duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print('\nThe original run-time used nested for statements and achieved a runtime of over 7.6 seconds')
print('My new solution uses a Binary Search Tree class and cuts the runtime down to less than 0.14 seconds\n')