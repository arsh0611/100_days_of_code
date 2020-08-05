"""Print the following pattern for the given
number of rows. Assume N is always odd. Note
: There is space after every star. Pattern
for N = 7"""

n = int(input())
row = []
s = ""
for i in range((n//2)+1):
  s += "*"
  row.append(" "*(2*i - 1) + s)
  print(" "*(2*i - 1) + s)
  s = s + " "    

row.pop()
while bool(row):
  print(row.pop())
