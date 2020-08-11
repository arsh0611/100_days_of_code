"""    Ceasar Cipher Encryptor

    Given a non-empty string of lowercase
    letters and a non-negative integer
    representing a key, Write a function
    that returns a new string obtained by
    shifting any letter in the input string
    by k positions in the alphabet, where k
    is the key. Note that letters should "wrap"
    around the alphabet; in other words,
    the letter "z" shifted by one returns the
    letter "a"

Sample Input:

string = "xyz"

key = 2


Sample Output:

"zab"


Optimal Space & Time Complexity
O(1) & O(n), where n is the length of the
input string. """

def convert(s): 
    new = "" 
    for x in s: 
        new += x  
    return new 

def caesar(value,key):
  a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  indexi=a.index(value)
  indexi=(indexi+key)%26
  return a[indexi]
  
def split(word): 
    return [char for char in word]

def caesarCipherEncryptor(string, key):
    
    string_array=split(string)
    string_array_second=[]
    for i in range(0,len(string_array)):
      string_array_second.append(caesar(string_array[i],key))

    return(convert(string_array_second))
    
    
    
