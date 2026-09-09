# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1: ListNode = l1
        current_l2: ListNode = l2
        tens_sum: int = 0
        dummy: ListNode = ListNode()
        current: ListNode = dummy

        while current_l1 is not None and current_l2 is not None:
            current.next = ListNode()
            current = current.next
            node_sum: int = current_l1.val + current_l2.val
            node_sum+=tens_sum
            
            digit: int = node_sum % 10
            tens_sum: int = node_sum // 10

            current.val = digit

            current_l1 = current_l1.next
            current_l2 = current_l2.next

        if current_l1 is None and current_l2 is not None:
            while current_l2 is not None:
                current.next = ListNode()
                current = current.next
                node_sum: int = current_l2.val + tens_sum
                digit: int = node_sum % 10
                tens_sum: int = node_sum // 10

                current.val = digit
                current_l2 = current_l2.next

        if current_l1 is not None and current_l2 is None:
            while current_l1 is not None:
                current.next = ListNode()
                current = current.next
                node_sum: int = current_l1.val + tens_sum
                digit: int = node_sum % 10
                tens_sum: int = node_sum // 10

                current.val = digit
                current_l1 = current_l1.next

        if tens_sum != 0:
            current.next = ListNode(tens_sum)

        return dummy.next

