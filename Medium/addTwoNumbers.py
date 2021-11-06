
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def traverse(self, l):
        num = ""
        while l is not None:
            num += str(l.val)
            l = l.next
        num = num[::-1]
        return num
    def makeSLL(self, ans):
        l3 = ListNode(int(ans[0]))
        temp = l3
        for i in range(1, len(ans)):
            temp.next = ListNode(int(ans[i]))
            temp = temp.next
        return l3
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1 = self.traverse(l1)
        temp2 = self.traverse(l2)
        res = int(temp1) + int(temp2)
        res_str = (str(res))[::-1]
        l3 = self.makeSLL(res_str)
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
# print(l3)
while l3 is not None:
    print(l3.val)
    l3 = l3.next