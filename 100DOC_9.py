"""Hunt a new Apartment:
You're looking to move into a new apartment,
and you're given a list of blocks where each
block contains an apartment that you could
move into. In order to pick your apartment,
you want to optimize its location. 
You also have a list of requirements: a list
of buildings that are important to you. For
instance, you might value having a school and
a gym near your apartment.
The list of blocks that you have contains
information at every block about all of the
buildings that are present and absent at the
block in question.
For instance, for every block, you might know
whether a school, a pool, an office, and a
gym are present.
In order to optimize your life, you want to
minimize the farthest distance you'd have
to walk from your apartment to reach any of
your required buildings.
Write a function that takes in a list of
blocks and a list of your required buildings
and that returns the location (the index) of
the block that's most optimal for you.

blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

sample output:
3 
Explanation
At index 3, the farthest you'd have to walk to reach a gym, school, or a store is 1 block; at any other index, you'd have to walk farther

"""


def findFarthest(block, requirement,blocks):
  farP=0
  farA=[100]
  if block+1 != len(blocks):
    for i in range(block+1,len(blocks)):

      farP=farP+1
      if blocks[i][requirement]==True:
        farA.append(farP)

        farP=0
        break
  farP=0
  if block-1 != -1:

    for i in range(block-1,-1,-1):
      farP=farP+1
      if blocks[i][requirement]==True:

        farA.append(farP)
        farP=0
        break
  mini=min(farA)
  print(mini)
  return mini
      



def apartmentHunting(blocks, reqs):
  farthest={}
  farthestDict={}
  #traverse list of blocks
  for i in range(0,len(blocks)):
    #traverse requirements
    for j in reqs:
      if blocks[i][j]==True:
        farthest[j]=0
  
        
      else:
        farthest[j]=findFarthest(i,j,blocks)
        print()
    maxim=0

  
    for k in farthest:
      if farthest[k]>maxim:
        maxim=farthest[k]
    farthestDict[i]=maxim

  minim= farthestDict[0]
  index=0
  for i in farthestDict:
    if farthestDict[i]<minim:
      minim=farthestDict[i]
      index=i
  

  return index
  

  

      
      
    
