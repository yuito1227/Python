import sys

def hasCycle(self, head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
            slow = slow.next
            fast.next,next
            if sloe == fast:
                return True
    retuen False

def main(lines):
    for i, line in enumerate(lines):
        hasCycle(head, ListNode))
        


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
