def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list

  # ⚠️ edge case 주의
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  mergedHead = None
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead

  # 🔑 
  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  # 남은 list 를 뒤에 붙이도록
  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2

  return mergedHead

array1 = [2, 3, 5, 6]
array2 = [1, 4, 10]
list_head1 = create_linked_list(array1)
print("Original1:")
display (list_head1)
list_head2 = create_linked_list(array2)
print("\nOriginal2:")
display (list_head2)
new_head = merge_sorted(list_head1, list_head2)

print("\nMerged:")
display(new_head)
