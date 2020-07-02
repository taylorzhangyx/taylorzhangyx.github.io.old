# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Version 1, O(NlogN) but space is O(N)
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            head = ListNode()
            cur = head
            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 != None else l2
            return head.next

        dummyHead = ListNode()
        dummyHead.next = head
        # merge sort
        l = []
        while head != None:
            temp = head.next
            head.next = None
            l.append(head)
            head = temp
        # l has all nodes
        length = len(l)
        while len(l) > 1:
            s = 0
            l2 = []
            while s < len(l):
                if s + 1 < len(l):
                    l2.append(merge(l[s], l[s + 1]))
                else:
                    l2.append(l[s])
                s += 2
            l = l2
        return l[0] if len(l) > 0 else None


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:

        # get a sub list of length subl after dummy node
        def getsub(dummy, subl):
            head = dummy.next
            count = 0
            end = dummy
            while count < subl and end.next != None:
                end = end.next
                count += 1
            dummy.next = end.next
            end.next = None
            return head

        # merge sorted list l1 and l2
        def merge(l1, l2):
            subdummy = ListNode()
            cur = subdummy
            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 != None else l2
            return subdummy.next

        # get the end node of list l
        def getEnd(l):
            temp = l
            while temp != None and temp.next != None:
                temp = temp.next
            return temp

        # insert list l right after the tar node
        def insert(tar, l):
            nxt = tar.next
            end = getEnd(l)
            tar.next = l
            end.next = nxt
            return end

        dummy = ListNode()
        dummy.next = head

        subl = 1  # the length of the sublist
        while True:
            count = 0
            cur = dummy
            while cur != None and cur.next != None:
                l1 = getsub(cur, subl)
                l2 = getsub(cur, subl)
                sortedSubHead = merge(l1, l2)
                cur = insert(cur, sortedSubHead)
                count += 1
            subl *= 2
            if (
                count <= 1
            ):  # we want to end the loop if the inner loop runs less than 2 times
                break
        return dummy.next
