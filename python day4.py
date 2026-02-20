
# anagram 
# def anagram(a,h): 
#     str1=str1.replaced("","").lower()
#     str2=str2.replaced("","").lower() 
#     if sorted(str1)==sorted(str2): 
#         return True 
#     else:
#         return False 
# word1=input("enter the word 1:") 
# word2=input("enter the word2:") 
# if is_anagram(word1,word2): 
#     print("it is an anagram") 
# else:
#     print("it is not an anagram")

# fizz buzz 

# for i in range(1,n+1): 
#     if i%3==0 and i%5==0: 
#         print("fizz buzz") 
#     elif 1%3==0: 
#         print("fizz") 
#     elif i%5==0: 
#         print("buzz") 
   

# 1822 leet code 

# 58 leet code 

# 349 leet code  
# from typing import List

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next
