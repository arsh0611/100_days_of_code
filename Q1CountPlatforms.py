"""Given two arrays (both of size n), one containing
arrival time of trains and other containing the corresponding
trains departure time (in the form of an integer) respectively.
Return the minimum number of platform required, such that no
train waits. Arrival and departure time of a train can't be same"""

n= int(input())
arrival = list(map(int,input().split()))
departure = list(map(int, input().split()))

platform=[]
max =0
for i in range(len(arrival)):
  temp = platform[:]
  for j in temp:
    if departure[j]<arrival[i]:
      platform.remove(j)
      
  platform.append(i)
  temp = platform[:]
  if len(platform)>max:
    max=len(platform)
print(max,end="")
