'''Question 1 : Bit counting(CodeWars)

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case '''

def count_bits(n):
    b = bin(n).replace("0b", "")
    count =0
    for int in b:
        if int == '1':
            count+=1
        
    print (count)

count_bits(203)

''' Question 2 :  '''
''' Convert Binary Number in a Linked List to Integer
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10 '''
''' 
Example 2:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880 '''
# Solution
# reverse(n3)
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def getDecimalValue(self, head:ListNode) -> int:
        num = head.val
        while(head.next is not None):
            num = num*2 + head.next.val
            head = head.next
        return num





