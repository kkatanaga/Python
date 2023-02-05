class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is not None or l2 is not None:
            sum = l1.val + l2.val

            if sum >= 10:
                carry = int(sum / 10)
                l3_head = ListNode(sum % 10)
            else:
                carry = 0
                l3_head = ListNode(sum)

            l1 = l1.next
            l2 = l2.next
            l3 = l3_head

        while l1 is not None or l2 is not None:
            if l1 is None:
                sum = l2.val + carry
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            if sum >= 10:
                carry = int(sum / 10)
                l3.next = ListNode(sum % 10)
            else:
                carry = 0
                l3.next = ListNode(sum)

            l3 = l3.next
        
        if carry != 0:
            l3.next = ListNode(carry)

        return l3_head

def printList(node):
    while node is not None:
        print(node.val)
        node = node.next

list_1 = ListNode(0)

list_2 = ListNode(0)

# list_1 = ListNode(9)
# list_1.next = ListNode(9)
# list_1.next.next = ListNode(9)
# list_1.next.next.next = ListNode(9)
# list_1.next.next.next.next = ListNode(9)
# list_1.next.next.next.next.next = ListNode(9)
# list_1.next.next.next.next.next.next = ListNode(9)

# list_2 = ListNode(9)
# list_2.next = ListNode(9)
# list_2.next.next = ListNode(9)
# list_2.next.next.next = ListNode(9)

list_3 = Solution.addTwoNumbers(Solution, list_1, list_2)
printList(list_3)