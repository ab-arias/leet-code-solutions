class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1 == None and list2 == None:
            return None
        
        newList = ListNode()

        if list1.val >= list2.val:
            newList.val = list2.val
            newList.next = self.mergeTwoLists(list1, list2.next)
        
        if list2.val > list1.val:
            newList.val = list1.val
            newList.next = self.mergeTwoLists(list1.next, list2)

        return newList

