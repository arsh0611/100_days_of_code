"""    Given a string, return a "rotated left 2" version
where the first 2 chars are moved to the end. The string
length will be at least 2.

Sample Input -> Output

rotate2('Hello') → 'lloHe'
rotate2('java') → 'vaja'

"""
a=input()
b=""

for i in range(2,len(a)):
  b=b+a[i]
b=b+a[0]
b=b+a[1]
print(b)


