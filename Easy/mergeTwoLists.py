
'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

'''


# SINGLY-LINKED LIST SOLUTION.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def traverse(self, l):
        while l is not None:
            print(l.val)
            l = l.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return l1
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        l3 = ListNode()
        temp = l3
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            # self.traverse(temp)
            temp = temp.next

        if l1 is None:
            temp.next = l2
        if l2 is None:
            temp.next = l1
        return l3.next
   

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)

sol = Solution()
l3 = sol.mergeTwoLists(l1, l2)
sol.traverse(l3)




# LIST SOLUTION

def mergeTwoLists(l1, l2):
    i = 0
    j = 0
    l3 = []
    if not l1 and l2:
        return []
    elif not l2:
        return l1
    elif not l1:
        return l2
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            l3.append(l2[j])
            j += 1
    l3 += l1[i:]
    l3 += l2[j:]
    return l3


list1 = [1,2,3,3]
list2 = [3,4,5,6]
print(mergeTwoLists(list1, list2))

