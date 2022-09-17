arr = [[1,2,3],[4,5,6]]
#1 2 3
#4 5 6

#1 4
#2 5
#3 6
arr2 = list(map(list,zip(*arr)))
for row in arr2:
  print(row)