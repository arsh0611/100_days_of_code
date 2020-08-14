"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58

Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def num_conversion(input_number):
  Roman_Dict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
  ans=""
  x=input_number
  i=False
  
  
  while(input_number>0):
    i=False

    print(input_number)
    if x+1 ==5 or x+1==10:
      ans=ans+Roman_Dict[1]
      ans=ans+Roman_Dict[x+1]
      input_number=input_number-x
      x=input_number
      i=True
      
    elif x+10 ==100 or x+10 ==100:
      ans=ans+Roman_Dict[10]
      ans=ans+Roman_Dict[x+10]
      input_number=input_number-x
      x=input_number
      i=True
    elif x+100 == 500 or x+100 == 1000:
      ans=ans+Roman_Dict[100]
      ans=ans+Roman_Dict[x+100]
      input_number=input_number-x
      x=input_number
      i=True
      
    elif(x in Roman_Dict):
      ans=ans+Roman_Dict[x]
      print("inner x initial ", x)
      
      input_number=input_number-x
      x=input_number
      i=True
      print("initial x later ",x)
    if i == False:
      x=x-1
    print("x ",x)
  return ans
  
  return res
if __name__ == "__main__":
  input_number = 9
  print(num_conversion(input_number))




