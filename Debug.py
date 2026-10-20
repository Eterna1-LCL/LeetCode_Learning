class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        ans = None
        
        while list1 != None and list2 != None:
            
            cur_list1 = list1.val
            cur_list2 = list2.val
            
            if cur_list1 <= cur_list2:
                ans = ListNode(cur_list1, list2)
            else:
                ans = ListNode(cur_list2, list1)
            
            list1 = list1.next
            list2 = list2.next

        return ans

if __name__ == "__main__":
    s = Solution()
    ans = s.mergeTwoLists([1,2,4], [1,3,4])
    print(ans)