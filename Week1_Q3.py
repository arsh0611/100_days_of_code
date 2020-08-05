"""Print the following pattern for n number of rows. For eg. N = 5"""

n= int(input())

a=[" "]*2*n


for i in range(0,n):
    a[i]=i+1
    a[len(a)-i-1]=i+1
    print(''.join(map(str, a)))
