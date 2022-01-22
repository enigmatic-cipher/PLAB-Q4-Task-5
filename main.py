"""
Given a list of size n as input. Print sum of elements greater than 3. Also print the sum of elements that are less than 3.
Input-> [2,3,5,10]
Output-> 
Below3=2 
Above3=15
"""

ls = [2,3,5,10]
ln = len(ls)
sum = 0
sum1 = 0
for i in range(0,ln):
  e = ls[i]
  if (e<3):
    sum = sum + e
  elif (e>3):
    sum1 = sum1 + e
print(f"Below3={sum}")
print(f"Above3={sum1}")
