import sys

"""
I used the The Algorithm Design Manual by Steven S. Skiena
to see what a balanced binary search tree should look like
"""

"""
in order to convert the list to one
suitable for a balanced bst:

1. convert list into sorted list
2. make the middle of the sorted list the root of a tree
3. create left and right subtree's via recursion

similar to binary search algorithm

e.g. 4 2 5 6 8 1 9
-> 1 2 4 5 6 8 9
->    5
  /      \
1 2 4    6 8 9

->     5
    /     \
    2      8
  /  \    /  \
  1   4   6   9
"""

"""
first need to set up the nodes in the tree
"""

class Node:
  def __init__(self, value):
    self.value = value #value of this individual node
    self.left = None
    self.right = None

"""
now to set up a list suitable for
a balanced bst
"""

def prepareListForBalancing(preparedList):

  if not preparedList:
    return

  middle = len(preparedList) // 2

  root = Node(preparedList[middle])

  leftSide = preparedList[:middle]
  rightSide = preparedList[middle + 1:] 

  root.left = prepareListForBalancing(leftSide)
  root.right = prepareListForBalancing(rightSide)

  return root

def presentList(node):
  resultStrings
  if not node:
    return
    
  resultStrings.append(str(node.value))
  presentList(node.left)
  presentList(node.right)

numlines=int(sys.stdin.readline())
for i in range(0,numlines):
  linearray=list(map(int,sys.stdin.readline().split()))
  linearray=linearray[1:]
  #linearray now contains the list of values found on the line (excluding the first item which is the number of elements on the line), do something with it...
  
  resultStrings = []
  seperator = " "
  sortedList = sorted(linearray)
  tree = prepareListForBalancing(sortedList)
  presentList(tree)
  print(seperator.join(resultStrings))
  
"""
commenting this out I don't know what it's for

print("178 57 26 157 679 397 898",end='')
print()
print("342 56 38 79 581 381 709",end='')
print()
"""
