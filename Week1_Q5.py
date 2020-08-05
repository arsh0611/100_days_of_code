"""    Print the following pattern Pattern for N = 4

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 """


n = int(input())
s = str(n)*(2*n - 1)
rev = [s]

for i in range(1,n):
  print(*s)
  s = s[:i] + str(n-i)*(2*n - 2*i -1) + s[2*n -i -1:]
  rev.append(s)

  
while rev:
  print(*rev.pop())

