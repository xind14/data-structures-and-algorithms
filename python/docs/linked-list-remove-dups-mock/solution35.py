def remove_duplicates(head):
  seen_values=set()
  current=head
  prev=None
  
  while current:
    if current.value in seen_values:
      prev.next=current.next
    else:
       seen_values.add(current.value)
       prev=current
       current=current.next
  return head