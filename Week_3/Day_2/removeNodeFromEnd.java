/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class removeNodeFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = new ListNode(0);
        temp.next = head;
        ListNode tej = temp;
        ListNode slow = temp;

        for (int i = 0; i < n; i++) tej = tej.next;
        while (tej.next != null) {
            tej = tej.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return temp.next;
        
    }
}