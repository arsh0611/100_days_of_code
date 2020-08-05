"""Given a tree, find and return the node
for which sum of data of all children and
the node itself is maximum. In the sum,
data of node itself and data of immediate
children is to be taken."""

tree_data = list(map(int, input().split()))
child = []
res = {}

while len(tree_data) > 0:
  
  try:
    if len(child) == 0:
      root = tree_data[0]
      n = tree_data[1]
      tree_data = tree_data[2:]
      
    else:
      root = child[0]
      n = tree_data[0]
      tree_data = tree_data[1:]
      child = child[1:]
    child = tree_data[:n]
    tree_data = tree_data[n:]
    
  except:
    break

  finally:
    if sum(child) in res.keys():
      res[sum(child)] = res[sum(child)] , root
    else:
      res[sum(child)] = root

print(res[max(res.keys())])
    
