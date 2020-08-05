 """   Print the following pattern for the given number of rows.

    Pattern for N = 5

1 2 3 4 5
11 12 13 14 15
21 22 23 24 25
16 17 18 19 20
6 7 8 9 10

"""

n = int(input())
odd = []
even = []

for i in range(n):
  s = ""
  for j in range(n*i+1,n*i+n+1):
    if j == n*i + n:
      s += str(j)
    else:
      s += str(j) + " "
  if i%2 == 0:
    even.append(s)
  else:
    odd.append(s)
rev = even [:: -1]
for i in range(len(even)):
  print(rev.pop())
while bool(odd):
  print(odd.pop())
