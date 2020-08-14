"""    Given 2 sets of integers,  M and N, print their symmetric
difference in ascending order. The term symmetric difference indicates
those values that exist in either  M or N  but do not exist in both.


Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.


Output Format

Output the symmetric difference integers in ascending order, one per line.


Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output

5
9
11
12"""
n1=int(input())
l1 = list(map(int,input().split()))
n2=int(input())
l2 = list(map(int,input().split()))
sol={}

for i in l1:
    if i in sol:
        sol[i]=sol[i]+1
    else:
        sol[i]=1
for i in l2:
    if i in sol:
        sol[i]=sol[i]+1
    else:
        sol[i]=1

for i in sorted (sol.keys()) :  
      
    if(sol[i]==1):
        print(i)

        
