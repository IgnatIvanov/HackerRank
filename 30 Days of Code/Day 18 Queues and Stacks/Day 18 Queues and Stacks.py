import sys

class Solution:
    def __init__(self):
        self.my_queue = []
        self.my_stack = []
    
    def pushCharacter(self, ch):
        self.my_stack.append(ch)
        
    def enqueueCharacter(self, ch):
        self.my_queue.append(ch)
        
    def popCharacter(self):
        if len(self.my_stack) > 0:
            return self.my_stack.pop()
        else:
            return ''
        
    def dequeueCharacter(self):
        if len(self.my_queue) > 0:
            return self.my_queue.pop(0)
        else:
            return ''

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    