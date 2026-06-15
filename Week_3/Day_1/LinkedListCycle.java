/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
    if (head == null || head.next ==null) {
        return false;  // Empty/single node
    }
    ListNode slow = head;
    ListNode tej = head;

    while (tej != null && tej.next != null) {
        slow = slow.next;      // 1 step move
        tej = tej.next.next; // 2 steps movement

        if (slow == tej) return true; // cycle occurred
    }
    return false;  // cycle not found
        
    }
}