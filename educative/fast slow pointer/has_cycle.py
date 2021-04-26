def has_cycle(head):
  slow, fast = head, head

  while True:
    if fast is None or fast.next is None:
      return False

    slow = slow.next
    fast = fast.next.next

    if slow is fast:
      return True

  return False